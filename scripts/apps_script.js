const AY = "2627_1";
const START_NR = 250;
const TABLE_RANGE = "A:N";
const SCHEDULE_SHEET_NAME = "schedule";

// GitHub Workflow Constants (Placeholders)
const GITHUB_API_BASE = "https://api.github.com";
const OWNER = "nushackers";
const REPO = "nushackers-site";
const WORKFLOW_FILE = "fh_update_action.yml";
const TARGET_BRANCH = "master";

// Will load from env somehow
const GITHUB_PAT = "YOUR_GITHUB_PAT";

// Column Indices
const COL_SESSION         = 0;  // A
const COL_DATE            = 1;  // B
const COL_START_TIME      = 2;  // C
const COL_END_TIME        = 3;  // D
const COL_VENUE           = 4;  // E
const COL_TITLE           = 5;  // F
const COL_SPEAKER         = 6;  // G
const COL_DESC            = 7;  // H
const COL_SIGNUP_LINK     = 8;  // I
const COL_NO_HACK         = 9;  // J
const COL_NO_HACK_R       = 10; // K
const COL_READY           = 11; // L
const COL_FROM            = 12; // M
const COL_POSTER_LINK     = 13; // N

const READY_STATUS = "Yes";
const READY_STATUS_UPDATED = "Already added";

/**
 * Combines a date with a time Date object to create a full ISO timestamp.
 * Extracts time from the time Date object and combines with the actual session date.
 * @param {any} dateValue - The session date (Date object or string YYYY-MM-DD).
 * @param {Date} timeValue - The time as a Date object (1899-12-30 with actual time).
 * @returns {string} Combined ISO timestamp with +0800 timezone (e.g., "2026-04-12T19:00:00+0800").
 */
function combineDateAndTime(dateValue, timeValue) {
    if (!timeValue) {
        return null;
    }

    // Extract HH:MM:SS from the time Date object
    let hour, minute, second;
    if (timeValue instanceof Date) {
        hour = String(timeValue.getHours()).padStart(2, '0');
        minute = String(timeValue.getMinutes()).padStart(2, '0');
        second = String(timeValue.getSeconds()).padStart(2, '0');
    } else {
        return null; // Can't parse non-Date time value
    }

    // Format the date as YYYY-MM-DD
    let dateStr;
    if (typeof dateValue === 'string') {
        dateStr = dateValue.split('T')[0]; // Extract date part if ISO string
    } else if (dateValue instanceof Date) {
        const year = dateValue.getFullYear();
        const month = String(dateValue.getMonth() + 1).padStart(2, '0');
        const day = String(dateValue.getDate()).padStart(2, '0');
        dateStr = `${year}-${month}-${day}`;
    } else {
        return null; // Can't parse date value
    }

    return `${dateStr}T${hour}:${minute}:${second}+0800`;
}

/**
 * Filters rows based on column A.
 * Keeps rows that are NOT empty in column A.
 * @param {Array<Array<any>>} data - The 2D array of spreadsheet data.
 * @returns {Array<Array<any>>} Filtered data.
 */
function filterNonEmptyRows(data) {
    return data.filter(row => row[COL_SESSION] !== "" && row[COL_SESSION] !== null && row[COL_SESSION] !== undefined);
}

/**
 * Updates the ready status for all rows of a given session number.
 * @param {Sheet} sheet - The spreadsheet sheet object.
 * @param {number} sessionNumber - The session number to update.
 * @param {string} newStatus - The new status to set in COL_READY.
 */
function updateSessionReadyStatus(sheet, sessionNumber, newStatus) {
    const data = sheet.getRange(TABLE_RANGE).getValues();

    for (let i = 0; i < data.length; i++) {
        if (data[i][COL_SESSION] === sessionNumber) {
            const rowNum = i + 1; // Google Sheets is 1-indexed
            const colLetter = String.fromCharCode(65 + COL_READY); // A=65
            sheet.getRange(`${colLetter}${rowNum}`).setValue(newStatus);
        }
    }
}

/**
 * Triggers a GitHub workflow dispatch using the GitHub API.
 * @param {Object} inputs - Key-value pairs for the workflow inputs.
 */
function triggerWorkflow(inputs = {}) {
    const url = `${GITHUB_API_BASE}/repos/${OWNER}/${REPO}/actions/workflows/${WORKFLOW_FILE}/dispatches`;

    const response = UrlFetchApp.fetch(url, {
        method: "post",
        headers: {
            Authorization:  `Bearer ${GITHUB_PAT}`,
            Accept:         "application/vnd.github+json",
                "Content-Type": "application/json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        payload: JSON.stringify({
            ref:    TARGET_BRANCH,
            inputs: inputs,
        }),
        muteHttpExceptions: true
    });

    const responseCode = response.getResponseCode();

    // 204 No Content = success
    if (responseCode === 204) {
        console.log("✅ Workflow triggered successfully!");
        return;
    }

    // Anything else is an error
    let errorBody;
    try {
        errorBody = JSON.parse(response.getContentText());
    } catch {
        errorBody = { message: "Error parsing error response." };
    }

    console.error(`❌ Failed to trigger workflow (HTTP ${responseCode}):`, errorBody);
}

function processSessions() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SCHEDULE_SHEET_NAME);
    const rawData = sheet.getRange(TABLE_RANGE).getValues();

    const filteredData = filterNonEmptyRows(rawData);

    // Group by session number
    const sessions = {};
    for (const row of filteredData) {
        const sessionNum = row[COL_SESSION];
        if (!sessions[sessionNum]) {
            sessions[sessionNum] = [];
        }
        sessions[sessionNum].push(row);
    }

    // Filter and format ready sessions
    const readySessionsFormatted = [];

    for (const [sessionNum, rows] of Object.entries(sessions)) {
        // 1a & 1b: Only keep sessions where ALL talks are marked "Yes" for Ready for website
        const allReady = rows.every(row => row[COL_READY] === READY_STATUS);

        if (allReady) {
            // 2: Format rows
            const firstRow = rows[0];
            const sessionData = {
                session_number: parseInt(sessionNum, 10),
                date: firstRow[COL_DATE],
                venue: firstRow[COL_VENUE],
                signup_link: firstRow[COL_SIGNUP_LINK],
                no_hack: !!firstRow[COL_NO_HACK], // Convert to boolean
                no_hack_reason: firstRow[COL_NO_HACK_R], // optional, can be empty
                talks: rows.map(r => ({
                    start_time: combineDateAndTime(firstRow[COL_DATE], r[COL_START_TIME]),
                    end_time: combineDateAndTime(firstRow[COL_DATE], r[COL_END_TIME]),
                    title: r[COL_TITLE],
                    speaker: r[COL_SPEAKER],
                    description: r[COL_DESC],
                    from: r[COL_FROM],
                    poster: r[COL_POSTER_LINK]
                }))
            };
            readySessionsFormatted.push(sessionData);
        }
    }

    if (readySessionsFormatted.length === 0) {
        console.log("No sessions are ready to be updated.");
        return;
    }

    // Note: For now, assume single session updated at a time, so pick the last session
    readySessionsFormatted.sort((a, b) => a.session_number - b.session_number);
    const targetSession = readySessionsFormatted[readySessionsFormatted.length - 1];

    // Validate session details
    let isValid = true;
    if (!targetSession.no_hack) {
        for (const talk of targetSession.talks) {
            if (!talk.title || !talk.speaker || !talk.description) {
                isValid = false;
                break;
            }
        }
    }

    if (!isValid) {
        console.error(`Validation failed for session ${targetSession.session_number}: Missing required talk details.`);
        return; // 3a.ii: log to console as error, and continue (in this case, abort since we're acting on one session)
    }

    console.log(`Validation passed for session ${targetSession.session_number}. Dispatching workflow...`);

    // Send session details as inputs to GitHub workflow
    const workflowInputs = {
        start_nr: START_NR,
        session_data: JSON.stringify(targetSession),
        semester: AY
    };

    triggerWorkflow(workflowInputs);

    // Update the ready status in the spreadsheet for all rows of this session
    updateSessionReadyStatus(sheet, targetSession.session_number, READY_STATUS_UPDATED);
    console.log(`Updated session ${targetSession.session_number} ready status to "${READY_STATUS_UPDATED}".`);
}

function main() {
    processSessions();
}
