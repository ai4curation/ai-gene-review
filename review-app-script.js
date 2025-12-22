/**
 * Google Apps Script for Gene Review Voting System
 *
 * Sheet: https://docs.google.com/spreadsheets/d/1uGKRdDjwRsrE5F5IOIQnKSxAA05V9PDDMUb1Sei2pL0/edit
 *
 * Setup:
 * 1. Create a Google Sheet with columns: Timestamp | Gene_ID | Annotation_ID | Ref_ID | Action | Vote | User_IP | Session_ID
 * 2. Go to Extensions → Apps Script
 * 3. Paste this code
 * 4. Deploy as Web App (Execute as: You, Access: Anyone)
 * 5. Copy the deployment URL for use in your HTML (https://script.google.com/macros/s/AKfycbwPKH7d3seuPNBtB0ugVjqGeTiByyOGD5vkqB_Ck6K8eOcPQYbJqBOuz6GFgXHKBNWK/exec)
 */

// Configuration
const SHEET_NAME = 'Votes'; // Change if your sheet has a different name
const RATE_LIMIT_MINUTES = 60; // Prevent same session voting on same item within this time
const MAX_VOTES_PER_SESSION_PER_HOUR = 100; // Rate limiting

/**
 * Handle GET requests from the voting buttons
 */
function doGet(e) {
  try {
    // Get the active sheet
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);

    if (!sheet) {
      throw new Error('Sheet "' + SHEET_NAME + '" not found');
    }

    // Extract and validate parameters
    const params = {
      gene_id: e.parameter.gene_id || '',
      annotation_id: e.parameter.annotation_id || '',
      ref_id: e.parameter.ref_id || '',
      action: e.parameter.action || '',
      vote: e.parameter.vote || '',
      session_id: e.parameter.session_id || 'anonymous',
      user_agent: e.parameter.ua || 'unknown',
      callback: e.parameter.callback || null
    };

    // Check if this is an image beacon request (no callback = image request)
    const isImageRequest = !params.callback;

    // Validate required fields
    if (!params.gene_id || !params.annotation_id || !params.action || !params.vote) {
      // For image requests, still log but return image
      if (isImageRequest) {
        console.error('Missing parameters:', params);
        return createResponse(null, null, true);
      }
      return createResponse({
        status: 'error',
        message: 'Missing required parameters'
      }, params.callback, false);
    }

    // Validate vote value
    if (params.vote !== 'up' && params.vote !== 'down') {
      if (isImageRequest) {
        console.error('Invalid vote value:', params.vote);
        return createResponse(null, null, true);
      }
      return createResponse({
        status: 'error',
        message: 'Invalid vote value'
      }, params.callback, false);
    }

    // Check for duplicate votes (within time window)
    const duplicateCheck = checkForDuplicate(sheet, params);
    if (duplicateCheck.isDuplicate) {
      // For image requests, still return success image (user doesn't need to know)
      if (isImageRequest) {
        return createResponse(null, null, true);
      }
      return createResponse({
        status: 'duplicate',
        message: 'Already voted on this item recently',
        existingVote: duplicateCheck.existingVote
      }, params.callback, false);
    }

    // Check rate limiting
    if (isRateLimited(sheet, params.session_id)) {
      // For image requests, still return success image
      if (isImageRequest) {
        console.log('Rate limited:', params.session_id);
        return createResponse(null, null, true);
      }
      return createResponse({
        status: 'rate_limited',
        message: 'Too many votes. Please try again later.'
      }, params.callback, false);
    }

    // Record the vote
    const timestamp = new Date();
    sheet.appendRow([
      timestamp,
      params.gene_id,
      params.annotation_id,
      params.ref_id,
      params.action,
      params.vote,
      params.user_agent, // Using user_agent as proxy for IP (which Apps Script can't access)
      params.session_id
    ]);

    // Return appropriate response
    if (isImageRequest) {
      // For image beacons, just return the image
      return createResponse(null, null, true);
    } else {
      // For JSONP/JSON requests, return data
      return createResponse({
        status: 'success',
        message: 'Vote recorded',
        vote: params.vote,
        timestamp: timestamp.toISOString()
      }, params.callback, false);
    }

  } catch (error) {
    console.error('Error processing vote:', error);

    // Check if this was an image request (no callback)
    const isImageRequest = !(e.parameter.callback);

    if (isImageRequest) {
      // For image requests, still return an image even on error
      return createResponse(null, null, true);
    }

    return createResponse({
      status: 'error',
      message: error.toString()
    }, e.parameter.callback || null, false);
  }
}

/**
 * Handle POST requests (same as GET for this use case)
 */
function doPost(e) {
  return doGet(e);
}

/**
 * Check if this session already voted on this item recently
 */
function checkForDuplicate(sheet, params) {
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return { isDuplicate: false };

  // Check last 500 rows (for performance)
  const rowsToCheck = Math.min(500, lastRow - 1);
  const startRow = lastRow - rowsToCheck + 1;

  const recentVotes = sheet.getRange(startRow, 1, rowsToCheck, 8).getValues();
  const cutoffTime = new Date(Date.now() - (RATE_LIMIT_MINUTES * 60 * 1000));

  for (let i = recentVotes.length - 1; i >= 0; i--) {
    const row = recentVotes[i];
    const voteTime = new Date(row[0]);

    // Stop checking if we've gone past the time window
    if (voteTime < cutoffTime) break;

    // Check if same session voted on same item
    if (row[1] === params.gene_id &&
        row[2] === params.annotation_id &&
        row[4] === params.action &&
        row[7] === params.session_id) {
      return {
        isDuplicate: true,
        existingVote: row[5]
      };
    }
  }

  return { isDuplicate: false };
}

/**
 * Check if session is rate limited
 */
function isRateLimited(sheet, sessionId) {
  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return false;

  // Check last hour of votes
  const rowsToCheck = Math.min(1000, lastRow - 1);
  const startRow = lastRow - rowsToCheck + 1;

  const recentVotes = sheet.getRange(startRow, 1, rowsToCheck, 8).getValues();
  const oneHourAgo = new Date(Date.now() - (60 * 60 * 1000));

  let voteCount = 0;
  for (let i = recentVotes.length - 1; i >= 0; i--) {
    const row = recentVotes[i];
    const voteTime = new Date(row[0]);

    if (voteTime < oneHourAgo) break;

    if (row[7] === sessionId) {
      voteCount++;
    }
  }

  return voteCount >= MAX_VOTES_PER_SESSION_PER_HOUR;
}

/**
 * Create a response - can be JSON, JSONP, or image based on request
 */
function createResponse(data, callback, isImageRequest) {
  // If this is an image beacon request, return simple text (works for image src)
  if (isImageRequest || (!callback && !data)) {
    // Return simple text response that works for image beacons
    return ContentService
      .createTextOutput('OK')
      .setMimeType(ContentService.MimeType.TEXT);
  }

  const jsonString = JSON.stringify(data);

  // If callback is provided, return JSONP
  if (callback) {
    return ContentService
      .createTextOutput(callback + '(' + jsonString + ');')
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }

  // Otherwise return regular JSON with CORS headers
  return ContentService
    .createTextOutput(jsonString)
    .setMimeType(ContentService.MimeType.JSON)
    .setHeader('Access-Control-Allow-Origin', '*')
    .setHeader('Access-Control-Allow-Methods', 'GET, POST');
}

/**
 * Optional: Get vote summary for a specific gene/annotation
 * Can be called with ?action=summary&gene_id=X&annotation_id=Y
 */
function doGetSummary(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
    const gene_id = e.parameter.gene_id;
    const annotation_id = e.parameter.annotation_id;

    if (!gene_id || !annotation_id) {
      return createResponse({
        status: 'error',
        message: 'Missing gene_id or annotation_id'
      });
    }

    const data = sheet.getDataRange().getValues();
    const summary = {};

    // Skip header row
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      if (row[1] === gene_id && row[2] === annotation_id) {
        const action = row[4];
        if (!summary[action]) {
          summary[action] = { up: 0, down: 0 };
        }
        summary[action][row[5]]++;
      }
    }

    return createResponse({
      status: 'success',
      gene_id: gene_id,
      annotation_id: annotation_id,
      summary: summary
    });

  } catch (error) {
    return createResponse({
      status: 'error',
      message: error.toString()
    });
  }
}

/**
 * Test function to verify the script has access to the sheet
 */
function testConnection() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
  if (sheet) {
    console.log('Successfully connected to sheet:', SHEET_NAME);
    console.log('Number of rows:', sheet.getLastRow());
    return true;
  } else {
    console.log('Could not find sheet:', SHEET_NAME);
    return false;
  }
}
