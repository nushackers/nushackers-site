"""Image loader utilities for Google Drive integration."""

import os
import re
import json
from pathlib import Path
from typing import Tuple
from io import BytesIO

import dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from constants import REPO_ROOT

# Load environment variables
dotenv.load_dotenv(REPO_ROOT / "scripts" / ".env")

# Google Drive API scope
DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


class ImageLoader:
    def __init__(self, year: int, session_number: int):
        self.year = year
        self.session_number = session_number
        self.service = self._authenticate_google_drive()

    def _authenticate_google_drive(self):
        """Authenticate with Google Drive using service account credentials."""
        credentials_json = os.getenv("GOOGLE_DRIVE_CREDENTIALS_JSON")

        if credentials_json:
            creds_dict = json.loads(credentials_json)
            credentials = Credentials.from_service_account_info(
                creds_dict,
                scopes=DRIVE_SCOPES
            )
        else:
            raise ValueError(
                "GOOGLE_DRIVE_CREDENTIALS_JSON environment variable is not set. Please configure it."
            )

        return build("drive", "v3", credentials=credentials)

    def _extract_file_id_from_drive_link(self, drive_link: str) -> str:
        """Extract the file ID from a Google Drive link or raw file ID."""
        match = re.search(r"/d/([a-zA-Z0-9-_]+)", drive_link)
        if match:
            return match.group(1)

        match = re.search(r"id=([a-zA-Z0-9-_]+)", drive_link)
        if match:
            return match.group(1)

        if re.match(r"^[a-zA-Z0-9-_]+$", drive_link):
            return drive_link

        raise ValueError(f"Could not extract file ID from Google Drive link: {drive_link}")

    def _get_file_extension(self, mime_type: str) -> str:
        """Determine file extension from MIME type."""
        mime_to_ext = {
            "image/jpeg": "jpg",
            "image/png": "png",
            "image/gif": "gif",
            "image/webp": "webp",
            "image/svg+xml": "svg",
            "image/bmp": "bmp",
            "image/tiff": "tiff",
        }

        if mime_type not in mime_to_ext:
            raise ValueError(f"Unsupported image MIME type: {mime_type}")

        return mime_to_ext[mime_type]

    def _load_image_from_drive(self, drive_link: str) -> Tuple[bytes, str]:
        """Download an image from Google Drive and return its bytes and file extension."""
        file_id = self._extract_file_id_from_drive_link(drive_link)

        try:
            file_metadata = self.service.files().get(
                fileId=file_id,
                fields="mimeType, name"
            ).execute()
        except Exception as e:
            raise FileNotFoundError(f"File not found on Google Drive (ID: {file_id}): {e}")

        mime_type = file_metadata.get("mimeType")
        if not mime_type or not mime_type.startswith("image/"):
            raise ValueError(f"File is not an image (MIME type: {mime_type})")

        file_extension = self._get_file_extension(mime_type)

        request = self.service.files().get_media(fileId=file_id)
        file_content = BytesIO()
        downloader = MediaIoBaseDownload(file_content, request)

        done = False
        while not done:
            _, done = downloader.next_chunk()

        return file_content.getvalue(), file_extension

    def _save_image(self, image_content: bytes, file_extension: str, idx: int) -> str:
        """Save image content to the repository static directory."""
        if not file_extension or not isinstance(file_extension, str):
            raise ValueError(f"Invalid file extension: {file_extension}")

        file_extension = file_extension.lstrip(".")

        save_dir = REPO_ROOT / "static" / "img" / str(self.year) / "fh"
        save_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{self.session_number}-{idx}.{file_extension}"
        save_path = save_dir / filename

        try:
            with open(save_path, "wb") as f:
                f.write(image_content)
        except IOError as e:
            raise IOError(f"Failed to save image to {save_path}: {e}")

        return str(save_path)

    def load_and_save_image_from_drive(self, drive_link: str, idx: int) -> str:
        """Load an image from Google Drive and save it to the static directory."""
        image_content, file_extension = self._load_image_from_drive(drive_link)
        return self._save_image(image_content, file_extension, idx)


if __name__ == "__main__":
    # Example usage
    drive_link = "https://drive.google.com/file/d/1vRJ2dtJe2hBbx6JIrptN_XktmG9D2Vdf/view?usp=drive_link"
    year = 2026
    session_number = 300
    idx = 1

    try:
        loader = ImageLoader(year, session_number)
        saved_path = loader.load_and_save_image_from_drive(drive_link, idx)
        print(f"Image saved to: {saved_path}")
    except Exception as e:
        print(f"Error: {e}")