/**
 * Deterministic trust gate for GitHub-sourced text.
 *
 * Used by `untrusted-comment-guard.yml` to decide whether a comment came from
 * someone we trust, and — if not — whether it carries content that should be
 * hidden before an agentic workflow can pick it up. No model is involved; this
 * is a plain allowlist + pattern check so it cannot itself be talked out of a
 * decision by the text it is inspecting.
 *
 * Trust is: a repo controller (.github/ai-controllers.json), a repository
 * collaborator with triage-or-better permission, or one of our own bots.
 */

const fs = require("fs");

const TRUSTED_PERMISSIONS = new Set(["admin", "maintain", "write", "triage"]);

// Deliberately NOT a list of bare names. A comment author that is a GitHub App
// always appears as "<slug>[bot]", so the "[bot]" suffix is the only reliable
// signal. Listing bare logins such as "claude" would hand automatic trust to
// whoever registers that username.
const BOT_LOGIN_SUFFIX = "[bot]";

const RISKY_COMMENT_PATTERNS = [
  {
    reason: "github_user_attachment",
    pattern: /https?:\/\/github\.com\/user-attachments\/files\/\d+\/[^\s)\]>"']+/i,
  },
  {
    reason: "archive_attachment",
    pattern:
      /(?:^|[^\w])[\w./:%?=&-]+\.(?:zip|7z|rar|tar\.gz|tgz|tar|gz|bz2|xz)(?:[?#][^\s)\]>"']*)?(?:[\s)\]>"']|$)/i,
  },
  {
    reason: "executable_or_script_attachment",
    // JavaScript is executable in browser and Node contexts. Python paths are
    // intentionally not matched here so ordinary repo-script references are not
    // hidden unless they also include an attachment/archive or agent trigger.
    pattern:
      /(?:^|[^\w])[\w./:%?=&-]+\.(?:exe|msi|dmg|pkg|apk|jar|sh|bash|zsh|ps1|bat|cmd|js|vbs|scr)(?:[?#][^\s)\]>"']*)?(?:[\s)\]>"']|$)/i,
  },
  {
    reason: "agent_trigger",
    // The phrases that actually dispatch an agent in this repo.
    pattern:
      /(?:^|\s)(?:@claude\b|@(?:ai4c-agent|dragon-ai-agent)\s+please\b|\/review\b)/i,
  },
];

function normalizeLogin(login) {
  return String(login || "").trim().toLowerCase();
}

function loadControllers(controllersPath = ".github/ai-controllers.json") {
  try {
    const controllers = JSON.parse(fs.readFileSync(controllersPath, "utf8"));
    if (!Array.isArray(controllers)) {
      throw new Error("expected a JSON array of GitHub logins");
    }
    return controllers.map(normalizeLogin).filter(Boolean);
  } catch (error) {
    console.log(`Failed to load ${controllersPath}: ${error.message}`);
    return ["cmungall"];
  }
}

function isBotLogin(login, extraBotLogins = []) {
  if (!login) {
    return false;
  }
  const normalized = normalizeLogin(login);
  if (normalized.endsWith(BOT_LOGIN_SUFFIX)) {
    return true;
  }
  // extraBotLogins is an explicit, caller-supplied override; it is not populated
  // with bare names by default.
  return extraBotLogins.map(normalizeLogin).includes(normalized);
}

async function isTrustedLogin({
  github,
  owner,
  repo,
  login,
  controllers = [],
  permissionCache = new Map(),
}) {
  // A missing login is NOT trusted. This is a trust gate: the safe default for
  // an author we cannot identify is untrusted, and the caller's risk classifier
  // decides whether anything actually happens.
  if (!login) {
    return false;
  }
  if (isBotLogin(login)) {
    return true;
  }
  const loginKey = normalizeLogin(login);
  const controllerSet =
    controllers instanceof Set
      ? controllers
      : new Set(controllers.map(normalizeLogin));
  if (controllerSet.has(loginKey)) {
    return true;
  }
  if (permissionCache.has(loginKey)) {
    return permissionCache.get(loginKey);
  }

  try {
    const response = await github.rest.repos.getCollaboratorPermissionLevel({
      owner,
      repo,
      username: login,
    });
    const trusted = TRUSTED_PERMISSIONS.has(response.data.permission);
    permissionCache.set(loginKey, trusted);
    return trusted;
  } catch (error) {
    console.log(`Treating ${login} as untrusted: ${error.message}`);
    permissionCache.set(loginKey, false);
    return false;
  }
}

function classifyCommentRisk(body) {
  const text = String(body || "");
  const reasons = RISKY_COMMENT_PATTERNS.filter(({ pattern }) =>
    pattern.test(text),
  ).map(({ reason }) => reason);

  return {
    shouldMinimize: reasons.length > 0,
    classifier: "SPAM",
    reasons,
  };
}

async function minimizeComment({ github, subjectId, classifier = "SPAM" }) {
  const mutation = `
    mutation($subjectId: ID!, $classifier: ReportedContentClassifiers!) {
      minimizeComment(input: {subjectId: $subjectId, classifier: $classifier}) {
        minimizedComment {
          isMinimized
          minimizedReason
        }
      }
    }
  `;
  return github.graphql(mutation, { subjectId, classifier });
}

module.exports = {
  classifyCommentRisk,
  isBotLogin,
  isTrustedLogin,
  loadControllers,
  minimizeComment,
  normalizeLogin,
  TRUSTED_PERMISSIONS,
};
