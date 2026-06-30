"""
Image Loader Module for Google Drive Integration

This module provides functionality to:
1. Authenticate with Google Drive API
2. Load images from Google Drive links
3. Save images to the repository static directory

Note: This module is designed to integrate with the Friday Hacks script pipeline.
"""

import os
import re
import json
from pathlib import Path
from typing import Tuple
from io import BytesIO

import dotenv
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google.auth import default
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from constants import REPO_ROOT

# Load environment variables
dotenv.load_dotenv(REPO_ROOT / ".env")

# Google Drive API scope
DRIVE_SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


def authenticate_google_drive():
    """
    Authenticate with Google Drive API using service account credentials.

    Expects either GOOGLE_DRIVE_CREDENTIALS_JSON to contain the JSON credentials string,
    or GOOGLE_DRIVE_CREDENTIALS_PATH to point to a Google Service Account JSON key file.

    Returns:
        googleapiclient.discovery.Resource: An authenticated Google Drive service object.

    Raises:
        FileNotFoundError: If the credentials file is not found.
        ValueError: If credentials are not properly configured.
    """
    credentials_json = os.getenv('GOOGLE_DRIVE_CREDENTIALS_JSON')
    credentials_path = os.getenv('GOOGLE_DRIVE_CREDENTIALS_PATH')

    if credentials_json:
        creds_dict = json.loads(credentials_json)
        credentials = Credentials.from_service_account_info(
            creds_dict,
            scopes=DRIVE_SCOPES
        )
    elif credentials_path:
        if not os.path.exists(credentials_path):
            raise FileNotFoundError(f"Credentials file not found: {credentials_path}")
        credentials = Credentials.from_service_account_file(
            credentials_path,
            scopes=DRIVE_SCOPES
        )
    else:
        raise ValueError(
            "Neither GOOGLE_DRIVE_CREDENTIALS_JSON nor GOOGLE_DRIVE_CREDENTIALS_PATH "
            "environment variables are set. Please configure one of them."
        )

    # Build the Drive API service
    service = build('drive', 'v3', credentials=credentials)

    return service


def _extract_file_id_from_drive_link(drive_link: str) -> str:
    """
    Extract the file ID from a Google Drive link.

    Supports formats:
    - https://drive.google.com/file/d/{file_id}/view?usp=sharing
    - https://drive.google.com/open?id={file_id}
    - {file_id} (if it's just the ID)

    Args:
        drive_link: The Google Drive link or file ID

    Returns:
        str: The extracted file ID

    Raises:
        ValueError: If the file ID cannot be extracted
    """
    # Try format: https://drive.google.com/file/d/{file_id}/view
    match = re.search(r'/d/([a-zA-Z0-9-_]+)', drive_link)
    if match:
        return match.group(1)

    # Try format: https://drive.google.com/open?id={file_id}
    match = re.search(r'id=([a-zA-Z0-9-_]+)', drive_link)
    if match:
        return match.group(1)

    # Check if it's just the file ID
    if re.match(r'^[a-zA-Z0-9-_]+$', drive_link):
        return drive_link

    raise ValueError(f"Could not extract file ID from Google Drive link: {drive_link}")


def _get_file_extension(mime_type: str) -> str:
    """
    Determine file extension from MIME type.

    Args:
        mime_type: The MIME type of the file (e.g., 'image/jpeg')

    Returns:
        str: The file extension without the dot (e.g., 'jpg')

    Raises:
        ValueError: If the MIME type is not a recognized image type
    """
    mime_to_ext = {
        'image/jpeg': 'jpg',
        'image/png': 'png',
        'image/gif': 'gif',
        'image/webp': 'webp',
        'image/svg+xml': 'svg',
        'image/bmp': 'bmp',
        'image/tiff': 'tiff',
    }

    if mime_type not in mime_to_ext:
        raise ValueError(f"Unsupported image MIME type: {mime_type}")

    return mime_to_ext[mime_type]


def load_image_from_drive(drive_link: str, service=None) -> Tuple[bytes, str]:
    """
    Download an image from a Google Drive link and return its content and extension.

    Args:
        drive_link: The Google Drive link or file ID
        service: Optional pre-authenticated Google Drive service. If None, authenticates.

    Returns:
        Tuple[bytes, str]: A tuple of (image_content, file_extension) where:
            - image_content is the raw bytes of the image
            - file_extension is the file extension (without dot, e.g., 'jpg')

    Raises:
        ValueError: If the file ID cannot be extracted or MIME type is invalid
        FileNotFoundError: If the file is not found on Google Drive
        Exception: If there's an error communicating with Google Drive API
    """
    # Authenticate if service not provided
    if service is None:
        service = authenticate_google_drive()

    # Extract file ID from link
    file_id = _extract_file_id_from_drive_link(drive_link)

    # Get file metadata (to extract MIME type)
    try:
        file_metadata = service.files().get(
            fileId=file_id,
            fields='mimeType, name'
        ).execute()
    except Exception as e:
        raise FileNotFoundError(f"File not found on Google Drive (ID: {file_id}): {e}")

    mime_type = file_metadata.get('mimeType')

    # Validate it's an image
    if not mime_type or not mime_type.startswith('image/'):
        raise ValueError(f"File is not an image (MIME type: {mime_type})")

    # Get file extension
    file_extension = _get_file_extension(mime_type)

    # Download file content
    request = service.files().get_media(fileId=file_id)
    file_content = BytesIO()
    downloader = MediaIoBaseDownload(file_content, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    image_bytes = file_content.getvalue()

    return image_bytes, file_extension


def save_image(image_content: bytes, file_extension: str, year: int, session_number: int, idx: int) -> str:
    """
    Save image content to the repository static directory.

    Args:
        image_content: The raw bytes of the image
        file_extension: The file extension (without dot, e.g., 'jpg')
        year: The year of the Friday Hacks session
        session_number: The session number
        idx: The talk index within the session

    Returns:
        str: The full path to the saved image file

    Raises:
        ValueError: If file_extension is invalid
        IOError: If there's an error writing the file
    """
    # Validate file extension
    if not file_extension or not isinstance(file_extension, str):
        raise ValueError(f"Invalid file extension: {file_extension}")

    # Remove leading dot if present
    file_extension = file_extension.lstrip('.')

    # Construct the save path
    save_dir = REPO_ROOT / "static" / "img" / str(year) / "fh"
    save_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{session_number}-{idx}.{file_extension}"
    save_path = save_dir / filename

    # Write image to file
    try:
        with open(save_path, 'wb') as f:
            f.write(image_content)
    except IOError as e:
        raise IOError(f"Failed to save image to {save_path}: {e}")

    return str(save_path)
