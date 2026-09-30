"""Audit propagation_review blocks against the rules in projects/IBA_REVIEW.md.

Checks each block for:
  * enum values that exist in the schema (root_cause / failure_modes / source_status)
  * NO_FAILURE_* paired with failure_modes (naming a failure while declaring none)
  * MODIFY carrying a NO_FAILURE_* root cause (proposing a replacement IS term scoping)
  * a self-seed source marked CIRCULAR_OR_REDUNDANT, or described with the inverted
    "adds no independent evidence" prose -- finding 1 of
    projects/IBA_REVIEW/propagation-review-audit.md
  * PANTHER family labels that disagree with interpro/panther/panther.obo.
    Read a hit as LABEL HYGIENE first, not as a hallucinated id: the common case is a
    truncated or embellished name for a correct family (dropping a trailing
    'SUBUNIT A', appending '(SF0)'), and the fix is to copy the official name
    verbatim. Only when the label names a DIFFERENT PROTEIN is it the hazard
    CLAUDE.md singles out -- and there the fix is the id, never the label.

Usage:  python3 projects/IBA_REVIEW/audit_propagation_review.py [glob ...] [--pair A,B] [--strict]
Defaults to genes/mouse/*/*-ai-review.yaml; pass globs to audit other organisms,
e.g. the ISO backlog:  ... audit_propagation_review.py 'genes/human/*/*-ai-review.yaml'

--pair compares two PARALOGS for rows adjudicated differently on the same
(term, evidence_type, reference). It is opt-in because unrelated genes legitimately
differ. It may be used with or without a glob; without one the mouse default applies:
    ... audit_propagation_review.py --pair Mapk1,Mapk3
--strict makes findings exit 1 (default: findings exit 0, this is a report tool).
Exits 2 for failures of the RUN itself: the self-test failing, no input files
matching, or a --pair that cannot be compared.
"""
import yaml, glob, os, re

VALID_RC={'NO_FAILURE_CORE','NO_FAILURE_NON_CORE','SOURCE_BAD','SOURCE_STALE_OR_MISSING',
 'SOURCE_WEAK_OR_INFERRED','EVIDENCE_CIRCULAR_OR_REDUNDANT','PROPAGATION_BAD',
 'TERM_SCOPING_PROBLEM','UNRESOLVED'}
VALID_FM={'WRONG_ORTHOLOG_OR_PARALOG','FUNCTIONAL_DIVERGENCE','PSEUDO_OR_SUBACTIVITY_LOSS',
 'CONTEXT_OR_TISSUE_MISMATCH','LINEAGE_OR_TAXON_MISMATCH','COMPARTMENT_OR_COMPLEX_MISMATCH',
 'REGULATORY_SIGN_INVERSION','ROLE_CONFLATION','GRANULARITY_MISMATCH','SOURCE_MISCITATION',
 'SOURCE_EVIDENCE_WEAK','CIRCULAR_PROPAGATION'}
VALID_SS={'SUPPORTS_TRANSFER','SUPPORTS_SOURCE_BUT_NOT_TARGET','SOURCE_BAD','SOURCE_STALE_OR_MISSING',
 'SOURCE_WEAK_OR_INFERRED','CIRCULAR_OR_REDUNDANT','NOT_RELEVANT','UNRESOLVED'}

# self-seed map: gene -> set of own ids
import sys

def _require_pair_value(val):
    """Reject an empty --pair value instead of letting it disable the comparison.

    '--pair=' and '--pair ""' both yield '', which is falsy -- so BOTH the pre-audit
    validation and the comparison block are skipped, and the run reports clean having
    silently ignored the flag. The realistic path is a CI wrapper invoking
    --pair "$PAIR_GENES" with the variable unset, which is exactly the case --strict
    exists to make trustworthy.
    """
    if not val.strip():
        print("--pair: empty value. Give two genes, e.g. --pair Mapk1,Mapk3 "
              "(or --pair mouse/Mapk1,mouse/Mapk3).")
        raise SystemExit(2)
    return val


def _parse_argv(argv):
    """Split argv into (file globs, --pair value).

    --pair and its value must be removed BEFORE the glob default is chosen: leaving
    them in makes argv truthy, suppresses the default glob, and globs '--pair' and
    'Mapk1,Mapk3' to nothing -- so the run audits zero files and reports clean. A
    vacuous pass, which is the failure mode this script exists to prevent.
    """
    globs, pair, strict, i = [], None, False, 0
    while i < len(argv):
        tok = argv[i]
        if tok == '--pair' and i + 1 < len(argv):
            pair = _require_pair_value(argv[i + 1]); i += 2; continue
        if tok.startswith('--pair='):
            pair = _require_pair_value(tok[len('--pair='):]); i += 1; continue
        if tok == '--strict':
            strict = True; i += 1; continue
        # Anything else that LOOKS like a flag is a typo, not a glob. Falling through
        # to globs is only caught by the zero-inputs guard when no real glob is also
        # passed; with one, '--pairs A,B <glob>' or '--strct <glob>' audits every file
        # and exits 0 having done neither thing the caller asked for -- and a mistyped
        # --strict silently turns a CI gate back into a report while still going green.
        if tok == '--pair':
            # Recognized, but last in argv so the two-token branch above declined it.
            # Saying "unrecognized" would send the reader off checking their spelling.
            print("--pair requires a value, e.g. --pair Mapk1,Mapk3 "
                  "(or --pair mouse/Mapk1,mouse/Mapk3).")
            raise SystemExit(2)
        if tok.startswith('-'):
            print(f"unrecognized flag {tok!r}. Accepted: --pair A,B (or --pair=A,B), --strict.")
            print("  Everything else is treated as a file glob; flags are not.")
            raise SystemExit(2)
        globs.append(tok); i += 1
    return globs, pair, strict

_GLOBS, PAIR_ARG, STRICT = _parse_argv(sys.argv[1:])
PATTERNS = _GLOBS or ['genes/mouse/*/*-ai-review.yaml']

# Model-organism database cross-references that appear as self-seed ids in WITH/FROM.
# Each entry is (GOA id prefix, which ';'-separated DR field holds the id GOA cites).
# Two traps here, both of which have silently broken this check before:
#   * MGI's DR value ALREADY carries the "MGI:" prefix and GOA doubles it, so the
#     corpus writes MGI:MGI:1346858 (1012 occurrences). Always prepend.
#   * WormBase's first DR field is the TRANSCRIPT id (T01C8.1a); GOA cites the
#     WBGene id, which is the third field.
MOD_XREFS = {
    'MGI':        ('MGI', 0),
    'RGD':        ('RGD', 0),
    'SGD':        ('SGD', 0),
    'FlyBase':    ('FB', 0),
    'WormBase':   ('WB', 2),
    'ZFIN':       ('ZFIN', 0),
    'TAIR':       ('TAIR', 0),
    'dictyBase':  ('dictyBase', 0),
    'PomBase':    ('PomBase', 0),
    'CGD':        ('CGD', 0),
}
# (organism, gene) -> the set of identifiers that denote the review target itself.
# Keyed by organism as well as gene because directory basenames collide across species
# (mouse and rat share Akt1, Casp3, Egfr, Ghr, Hspa8, Mapk1, Slc5a1, ...).
own={}
for d in sorted(glob.glob('genes/*/*/')):
    parts=d.rstrip('/').split(os.sep)
    org, g = parts[-2], parts[-1]
    ids=set()
    f=f'{d}{g}-uniprot.txt'
    if os.path.exists(f):
        txt=open(f).read()
        for dr_name, (id_prefix, field_idx) in MOD_XREFS.items():
            for m in re.finditer(rf'^DR   {re.escape(dr_name)}; (.+)$', txt, re.M):
                fields=[x.strip() for x in m.group(1).split(';')]
                if field_idx >= len(fields): continue
                val=fields[field_idx].rstrip('.').strip()
                if not val: continue
                # Always prepend the GOA prefix. Do NOT skip when the value already
                # starts with it: MGI is exactly that case and GOA doubles it.
                ids.add(f'{id_prefix}:{val}')
        m=re.search(r'^AC   (.+)$', txt, re.M)
        if m:
            for a in m.group(1).split(';'):
                if a.strip(): ids.add('UniProtKB:'+a.strip())
    own[(org,g)]=ids

# Self-test: the two id conventions that have silently broken self-seed detection
# before. If these stop holding, SELF_SEED_* can never fire and the audit passes
# vacuously on the affected organism -- which is worse than failing loudly.
_selftest_failures = []
# Guard the guards: if `own` is empty (run from the wrong cwd, so glob matched nothing)
# every conditional check below is skipped and SELF_SEED_* passes vacuously -- the exact
# failure shape this self-test exists to prevent.
if not any(own.values()):
    # `own` gets a key for every gene directory, including ones with no -uniprot.txt,
    # so a non-empty dict does NOT mean any identifier was parsed. Check the values.
    _selftest_failures.append(
        "no self-identifiers parsed from any gene directory - wrong cwd, partial "
        "checkout, or the UniProt DR format changed?")
if ('mouse', 'Mapk1') in own and 'MGI:MGI:1346858' not in own[('mouse', 'Mapk1')]:
    _selftest_failures.append(
        "MGI self-seed ids must carry the doubled prefix (MGI:MGI:...) as GOA writes them")
if ('worm', 'aak-2') in own and 'WB:WBGene00020142' not in own[('worm', 'aak-2')]:
    _selftest_failures.append(
        "WormBase self-seed ids must be the WBGene id, not the transcript id")
# valid PANTHER family labels. Loaded BEFORE the self-test so the anchor below can
# prove it actually loaded: a bare `except: pass` here previously meant a missing or
# renamed panther.obo left fam_label empty and PANTHER_LABEL_MISMATCH passing vacuously.
fam_label={}
try:
    cur=None
    for line in open('interpro/panther/panther.obo'):
        line=line.rstrip('\n')
        if line.startswith('id: PANTHER:'): cur=line.split('id: ')[1]
        elif line.startswith('name: ') and cur: fam_label[cur]=line[6:]; cur=None
except Exception as _e:
    _selftest_failures.append(f"could not read interpro/panther/panther.obo: {_e!r}")

# PANTHER anchors. fam_label is keyed WITH the 'PANTHER:' prefix, and the lookup used
# the bare id for eight rounds -- so the rule never fired once and reported clean the
# whole time. Two separate assertions, because they fail for different reasons and a
# single one would report the wrong cause:
#   * shape: ANY prefixed key at all. Catches the file not loading and the key
#     convention changing -- the two ways this check goes silent.
#   * anchor: one known family. Catches a subtler parse break that still yields
#     plausible keys. PANTHER may legitimately retire or merge PTHR46861 in a future
#     release, in which case ONLY this second line fires and the shape line passes,
#     which is the signal to re-point the anchor rather than to hunt a parser bug.
if not any(k.startswith('PANTHER:PTHR') for k in fam_label):
    _selftest_failures.append(
        "PANTHER family labels must be keyed with the 'PANTHER:' prefix as panther.obo "
        "writes them - no such key exists, so PANTHER_LABEL_MISMATCH cannot fire")
elif 'PANTHER:PTHR46861' not in fam_label:
    _selftest_failures.append(
        "PANTHER anchor PTHR46861 is missing while other prefixed keys loaded - the "
        "family was likely retired or merged upstream; re-point the anchor")

# The three framings CLAUDE.md forbids about a self-seed source. All three were
# once bare substring tests -- a list of phrasings someone had happened to see, not
# a match on the grammar -- so a curator DISCLAIMING the framing was flagged as
# committing it. Five of seven live hits were disclaimers.
#
# Checked PER OCCURRENCE, not per comment: one clause may disclaim circularity while
# another asserts "adds no independent support". ACRV1 does exactly that, and a
# whole-comment test would let its disclaimer suppress its assertion.
_FLAGGED_FRAMING = re.compile(r'circular|self-supporting|no independent', re.I)
_NEG_CUE = re.compile(r'\bnot\b|\bnon\b|\bnever\b|\brather\s+than\b|\bavoids?\b', re.I)

def _asserts_inverted_framing(c):
    """True if c ASSERTS one of the forbidden framings rather than disclaiming it."""
    for m in _FLAGGED_FRAMING.finditer(c):
        # Look back only within the same clause: splitting on .;: stops an unrelated
        # earlier negation from suppressing a later assertion.
        pre = re.split(r'[.;:,]', c[max(0, m.start() - 45):m.start()])[-1]
        if not _NEG_CUE.search(pre):
            return True
    return False

# Self-test the predicate rather than trusting it: the failure direction here is a
# FALSE POSITIVE, which does not announce itself the way a crash would.
for _s, _want in (
        # Disclaimers -- must NOT be flagged.
        ("not a circular transfer", False), ("not a circular chain", False),
        ("rather than a circular inference", False), ("makes this non-circular", False),
        ("strengthens the transfer rather than making it circular", False),
        ("grounded rather than circular", False), ("never circular", False),
        ("expected rather than self-supporting", False),
        # Assertions -- must still be flagged.
        ("this source is circular and adds nothing", True),
        ("a circular propagation with no experimental grounding", True),
        ("the propagation adds no independent evidence", True),
        ("that item is self-supporting", True),
        # Both in one comment: the disclaimer must not suppress the assertion.
        ("rather than a circular inference, so it is not a defect; "
         "it simply adds no independent support", True),
        # A cue in a PRECEDING comma-clause must not reach across it. Without ','
        # in the split set this reads as a disclaimer and the assertion is lost --
        # a false negative, the worse direction.
        ("this donor is not the closest ortholog, and the chain is circular", True)):
    if _asserts_inverted_framing(_s) != _want:
        _selftest_failures.append(
            f"inverted-framing predicate is wrong for {_s!r} "
            f"(expected flagged={_want}) - SELF_SEED_INVERTED_PROSE will misreport")


# ---------------------------------------------------------------------------
# MANGLED_PROSE: punctuation damage from bulk string substitution.
#
# Written after a sed-style rewrite of 8 source_entities comments consumed the
# opening "(" of a trailing "(ACC)" while leaving the ")", producing sentences like
# "...appears in no cached record under a name)." and, worse, "...under a name, )."
# -- a hole where an accession had been. Nothing in the schema or the validator sees
# this: the YAML parses, the enums are legal, and inside a folded scalar the damage
# does not even land on one line, so a line-wise grep misses it too. It has to be
# checked on the JOINED value.
#
# SCOPE is an ALLOWLIST, and it covers every author-written prose field rather than
# only the ones the original damage landed in -- restricting it to {comment, reason,
# summary, review_notes} would repeat the mistake of the sweep scoped to `comment:`
# that missed `reason:`, which describes where a defect occurred rather than where one
# could. So `description` (GeneReview, CoreFunction, ProposedOntologyTerm) and
# `findings[].statement` are in.
#
# What stays OUT is machine-sourced text, and that exemption is load-bearing rather
# than theoretical. supporting_text is verbatim publication quotation, legitimately
# unbalanced ~10 times in genes/mouse alone ("(LCAD-/-) develop hepatic steatosis",
# "emerges from 1) ..."); `name` carries machine-extracted isoform names whose UniProt
# evidence tags are themselves truncated at a comma; titles carry "system xc()". A
# denylist would fire on all of those on its first run. An allowlist also means a new
# machine-sourced field cannot start false-positiving later.
#
# HONEST LIMIT, stated because the temptation is to call this a guard for the class:
# it catches the UNBALANCED and EMPTY-SLOT shapes, which was 5 of the 8 comments that
# prompted it. The other 3 were the mirror artifact -- a new sentence prepended while
# the original trailing parenthetical was left in place -- which is balanced, reads as
# ordinary prose, and is only detectable as duplication. This rule does not catch that,
# and no attempt at a duplication heuristic survived contact with prose that names an
# accession twice for good reason.
#
# A second limit, found the hard way: the two genes/human values this rule reports
# (IL36RN core_functions[0].description, EMC1 references[17].findings[0].statement)
# look intact in the FILE and are damaged only in the PARSED value -- see
# YAML_COMMENT_TRUNCATION below. This rule catches them incidentally, because the lost
# text happened to contain a closing paren. It is not a detector for that class.
_PROSE_FIELDS = {'comment', 'reason', 'summary', 'review_notes',
                 'description', 'statement'}
# A delimiter immediately before ")" is the signature of a consumed slot ("name, )"),
# as is a wholly empty "()" -- both balance, so the depth scan alone misses them.
_EMPTY_SLOT = re.compile(r'\(\s*[,;]?\s*\)|[,;]\s*\)')

def _mangled_prose(s):
    """Return the offending index if s shows punctuation damage, else None.

    A position rather than a bool, so the finding can quote the damage. Reporting the
    tail instead (the first version did) shows clean prose for the EMPTY-SLOT shape,
    whose damage sits mid-string -- and that is the very shape the depth scan alone
    also misses, so the one case where the payload is uninformative was the one case
    that most needed it.
    """
    depth = 0
    for i, ch in enumerate(s):
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            # Order matters, not just the count: "a) (b" balances but is still wrong.
            if depth < 0:
                return i
    m = _EMPTY_SLOT.search(s)
    if m:
        return m.start()
    if depth != 0:
        # Unclosed: point at the last "(" that never closed rather than at the end.
        return s.rfind('(')
    return None

def _damage_window(s, pos, span=35):
    """The text around pos, so a MANGLED_PROSE finding carries its own evidence."""
    lo, hi = max(0, pos - span), min(len(s), pos + span)
    return ('...' if lo else '') + s[lo:hi] + ('...' if hi < len(s) else '')

def _walk_prose(o, path, key=None):
    """Yield (path, value) for every author-written prose scalar in a review doc."""
    if isinstance(o, dict):
        for k, v in o.items():
            yield from _walk_prose(v, f"{path}.{k}", k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _walk_prose(v, f"{path}[{i}]", key)
    elif isinstance(o, str) and key in _PROSE_FIELDS:
        yield path, o

# Self-test, same reasoning as the predicate above: the corpus is clean, so this rule
# reports success by finding nothing, and a broken version is indistinguishable from a
# healthy corpus. The first four cases are the exact strings this was written for.
for _s, _want in (
        ("appears in no cached record under a name).", True),
        ("in no local entries index or cached record under a name, ).", True),
        ("Anti-apoptotic donor (asserted from external knowledge, ).", True),
        ("under a name); same role and sign as the target.", True),
        ("a) (b", True),                      # balances by count, still damaged
        ("the empty pair () is a hole too", True),
        ("(a", True), ("a)", True),
        # Must NOT fire on ordinary prose.
        ("Rodent donor, corroborated through the cross-reference (Q07813).", False),
        ("nested (a (b) c) d", False),
        ("no brackets at all", False),
        ("SF4 PROTEIN SLIT, but also worm glp-1 (P13508) and zebrafish notch1a (P46530)", False)):
    if (_mangled_prose(_s) is not None) != _want:
        _selftest_failures.append(
            f"mangled-prose predicate is wrong for {_s!r} "
            f"(expected flagged={_want}) - MANGLED_PROSE will misreport")

# The window must actually contain the damage. Without this the payload can regress to
# showing clean prose while every case above still passes -- the exact defect that was
# reported against the first version, and one a boolean self-test cannot see.
for _s, _must_contain in (
        # Mid-string empty slot with a long clean tail: the shape the tail payload lost.
        ("Anti-apoptotic donor (asserted from external knowledge, ). "
         "It is flagged NOT_RELEVANT because it contributes no support for the "
         "positive-regulation term, and is named only as node-composition evidence.", ", )"),
        ("appears in no cached record under a name).", "name)"),
        ("the empty pair () is a hole too", "()")):
    _pos = _mangled_prose(_s)
    if _pos is None or _must_contain not in _damage_window(_s, _pos):
        _selftest_failures.append(
            f"mangled-prose window does not show the damage {_must_contain!r} "
            f"for {_s[:60]!r} - MANGLED_PROSE findings would carry no evidence")


# ---------------------------------------------------------------------------
# YAML_COMMENT_TRUNCATION: text silently discarded by the YAML parser.
#
# In a PLAIN (unquoted) scalar, " #" starts a comment. So a reason written as
#     reason: ... over-general term when more specific MFs are available; PR #758 review
# is stored as "...are available; PR" -- everything from " #" is dropped at parse time.
# The file looks complete, `git diff` looks complete, and a grep over the raw text finds
# the full sentence. Only the parsed value is short, which is what every consumer sees:
# the validator, the renderer, the auditor, and any downstream tool.
#
# The plain scalar has a second, opposite failure with the same shape: ": " inside one is
# a PARSE ERROR, not a truncation. Writing "...does not weaken this one: the IEA and ISO
# rows..." into a plain multi-line `reason` raised
#     yaml.scanner.ScannerError: mapping values are not allowed here
# So the same field punishes " #" silently and ": " loudly, and only the loud half is
# self-reporting. A folded ">-" block is immune to both; a plain scalar is the risk.
# This rule detects only the silent half -- the loud half needs no detector, since
# nothing that fails to parse gets committed past validation.
#
# This is why the two genes/human values MANGLED_PROSE reports look intact when checked
# with grep. Both are real -- EMC1 references[17].findings[0].statement parses to 122
# characters from a 357-character line, losing 235 -- but the mechanism is the parser,
# not the author, and stating them as "truncations" without saying so invites exactly
# the raw-text check that appears to refute them. They are the same defect as the ATG14
# and LEMD2 rows below.
#
# MANGLED_PROSE catches 2 of the 13, and only by luck: the discarded text happened to
# begin right after an unclosed "(" ("(OMIM", "(PR"). A truncation that leaves the
# parens balanced -- which is 11 of 13, including every ATG14 row, where a whole
# "[GO issue #29437] Same defect as ..." clause is lost -- is invisible to it. Hence a
# separate rule keyed on the mechanism rather than on the symptom.
#
# The " #" must be on the SAME LINE as the scalar's text. A comment on its own line
# after a value is ordinary YAML and discards nothing; an earlier version that searched
# whitespace-normalised text conflated the two and reported 814 hits instead of 13.
# The floor exists because the match is a TAIL SEARCH: a very short value gives a very
# short pattern, which both scans slowly and coincides with unrelated text. 12 is where
# that stops being a real risk; the corpus result is identical at 12 and at 20, so this
# is coverage bought for nothing rather than a threshold tuned to a number. Values
# shorter than this are simply not judged -- worth knowing, since a `label:` cut to 8
# characters has lost proportionally far more than EMC1's 357-character statement did.
_TRUNCATION_MIN_LEN = 12
# A non-space, non-"#" character, then horizontal space, then "#": the shape of an
# inline comment. A "#" at the start of a line (a standalone comment) never matches.
_INLINE_HASH = re.compile(r'[^\s#][ \t]+#')

def _yaml_comment_truncations(raw, doc):
    """Yield (path, lost_text) for plain scalars the parser cut at an inline '#'.

    Note it cannot distinguish "the parser ate the author's text" from "the author
    wrote a trailing comment" -- in YAML those are the same construct. That is not a
    real gap: a trailing comment inside a curation record is itself content the schema
    will never see, so reporting it is right either way. (Swept for it: no
    `value  # note` form exists anywhere in the corpus today, so this is latent.)
    """
    # File-level pre-check. The per-value work below is a finditer over the whole raw
    # text, which is far too slow to run for every scalar in every file; almost no file
    # contains an inline "#" at all, so one cheap scan skips the vast majority outright.
    if not _INLINE_HASH.search(raw):
        return
    for _path, _value in _walk_all_scalars(doc, ''):
        if len(_value) < _TRUNCATION_MIN_LEN:
            continue
        # Match the value's tail in the raw text, allowing YAML line-folding inside it,
        # then require a "#" after horizontal space only -- never across a newline.
        # Requiring same-line is what structurally excludes block scalars (where "#" is
        # literal and nothing is lost) and standalone comment lines after a value.
        # A clip-style "|" block keeps its trailing newline, so its tail ends with one.
        # The "#" test below would then match an INDENTED comment on the following line
        # and report a truncation where nothing was lost. (No live instance today -- every
        # indented comment in the corpus follows a folded or plain scalar -- but 717 clip
        # blocks and 20 files with indented comments both exist, so the ingredients do.)
        if _value.endswith('\n'):
            continue
        _tail = re.escape(_value[-25:]).replace(r'\ ', r'\s+')
        _all = list(re.finditer(_tail, raw))
        _cut = [_m for _m in _all if re.match(r'[ \t]+#', raw[_m.end():])]
        if not _cut:
            continue
        # The search is over the whole file, not anchored to this value's own offset, so
        # an identical tail occurring more than once needs care. Two separate questions:
        #
        #   IS this value cut?  Certain only when EVERY occurrence of the tail is cut.
        #     If some occurrence is not, this value might be the intact one and the
        #     finding would be a false positive borrowed from its twin -- so skip. That
        #     trades a false negative for a false positive, the right direction for a
        #     rule whose output sends a maintainer looking.
        #
        #   WHAT did it lose?  Answerable only when every occurrence lost the same text.
        #     ATG14 is the live case and it is genuinely mixed: eight `reason` values
        #     share the tail "e-review against GO issue", all eight are cut, but the
        #     lost text has TWO variants ("...Same defect as..." and "...The cited
        #     evidence describes..."). The defect is certain; the attribution is not.
        #     Suppressing the finding on that basis would lose eight real truncations to
        #     protect a payload, so report the finding and say the payload is ambiguous.
        if len(_cut) != len(_all):
            continue
        _lost = {raw[_m.end():].split('\n', 1)[0] for _m in _cut}
        yield _path, (_lost.pop() if len(_lost) == 1 else
                      f"<{len(_lost)} variants at {len(_all)} identical tails, "
                      f"e.g. {sorted(_lost)[0][:40]!r}>")

def _walk_all_scalars(o, path):
    """Every string scalar, machine-sourced included: the parser cuts them all."""
    if isinstance(o, dict):
        for k, v in o.items():
            yield from _walk_all_scalars(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _walk_all_scalars(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o

# Self-test on real YAML, because the whole point is what the PARSER does -- asserting
# against hand-written expectations would just re-encode my belief about YAML.
_tt_doc = ("description: over-general term; PR #758 review feedback.\n"
           "quoted: \"a quoted # stays whole\"\n"
           "folded: >-\n  a folded scalar with no hash\n"
           "# a standalone comment line discards nothing\n"
           "after_comment: this value is intact and long enough to test\n")
_tt_hits = dict(_yaml_comment_truncations(_tt_doc, yaml.safe_load(_tt_doc)))
if '.description' not in _tt_hits:
    _selftest_failures.append(
        "YAML_COMMENT_TRUNCATION misses an inline '#' in a plain scalar - the rule cannot fire")
if [k for k in _tt_hits if k != '.description']:
    _selftest_failures.append(
        f"YAML_COMMENT_TRUNCATION fires on undamaged values {sorted(_tt_hits)} - "
        "a standalone comment line or a quoted '#' is not a truncation")

# A clip "|" block followed by an INDENTED comment: nothing is lost, so nothing is
# reported. The _tt_doc arm above only covers a comment at column 0, which is safe for a
# different reason (no leading horizontal space before the "#"), so it does not reach this.
# NOTE the first line: without a genuine inline "#" somewhere, _INLINE_HASH fails and the
# function returns before reaching any value, so the assertion below would hold no matter
# what the rule did. A first version of this arm omitted it and passed vacuously.
_tt_clip = ("z: a plain scalar that is truncated here # lost\n"
            "a:\n  b: |\n    text here that is long enough to test\n  # an indented comment\n")
_tt_clip_hits = dict(_yaml_comment_truncations(_tt_clip, yaml.safe_load(_tt_clip)))
if '.z' not in _tt_clip_hits:
    _selftest_failures.append(
        "YAML_COMMENT_TRUNCATION self-test input reaches no value - the inline-'#' gate "
        "rejected it, so the clip-block assertion below cannot fail")
if '.a.b' in _tt_clip_hits:
    _selftest_failures.append(
        "YAML_COMMENT_TRUNCATION reports a clip '|' block followed by an indented comment - "
        "the block's trailing newline is not a truncation and nothing was lost")

# The duplicate-tail arms, each on real YAML. These decide whether a finding appears at
# all, so a silent regression here is a false positive or eight lost real defects.
# (a) Two identical tails, one cut and one intact: the intact value must NOT be reported
#     on its twin's evidence, and the cut one is given up along with it.
_tt_amb = ("a: the same trailing words appear twice here\n"
           "b: the same trailing words appear twice here # lost text\n")
if dict(_yaml_comment_truncations(_tt_amb, yaml.safe_load(_tt_amb))):
    _selftest_failures.append(
        "YAML_COMMENT_TRUNCATION reports a duplicated tail where one occurrence is "
        "intact - it cannot tell which value is cut, so this is a false positive")
# (b) Two identical tails, both cut, differing lost text: the finding must still appear
#     (the truncation is certain) with the payload marked ambiguous (which text is not).
_tt_two = ("a: the same trailing words appear twice here # lost ONE\n"
           "b: the same trailing words appear twice here # lost TWO\n")
_tt_two_hits = dict(_yaml_comment_truncations(_tt_two, yaml.safe_load(_tt_two)))
if sorted(_tt_two_hits) != ['.a', '.b']:
    _selftest_failures.append(
        f"YAML_COMMENT_TRUNCATION lost a certain truncation to an ambiguous payload "
        f"(reported {sorted(_tt_two_hits)}, expected both) - this is the ATG14 case")
elif not all('variants' in _v for _v in _tt_two_hits.values()):
    _selftest_failures.append(
        f"YAML_COMMENT_TRUNCATION quotes one variant as if it were the value's own "
        f"lost text ({_tt_two_hits}) - the payload must say it is ambiguous")

if _selftest_failures:
    print("SELF-TEST FAILED - a detection rule cannot fire:")
    for _f in _selftest_failures:
        print("   ", _f)
    raise SystemExit(2)


issues=[]; n=0
# Dedupe across patterns: overlapping globs would otherwise audit a file twice and
# inflate the "across N files" headline.
files=sorted({f for pat in PATTERNS for f in glob.glob(pat)})

def _org_gene(path):
    _p = os.path.dirname(path).split(os.sep)
    return (_p[-2], _p[-1])

# ZERO INPUTS IS AN ERROR, NOT A PASS. Every entry point that can silently audit
# nothing has produced a false "clean" in this tool's history: a mistyped glob, a
# --pair whose value was omitted (so the flag itself became a glob), the --pair=X
# equals-form, a typo'd flag name. The self-test above cannot catch these -- it globs
# genes/*/*/ independently of PATTERNS -- so the check belongs here.
if not files:
    print("NO INPUT FILES MATCHED - refusing to report a clean audit.")
    print("  patterns:", PATTERNS)
    print("  (a mistyped glob, or --pair given without a value, lands here)")
    raise SystemExit(2)

# Validate --pair BEFORE the audit runs. Checking it afterwards means a typo in an
# unrelated flag throws away a completed, perfectly valid report.
PAIR_PATHS = None
if PAIR_ARG:
    # Accept either "Gene" or "organism/Gene". The bare form is ambiguous across
    # organisms -- genes/mouse and genes/rat share Akt1, Casp3, Egfr, Ghr, Hspa8,
    # Mapk1, Slc5a1 -- and pairing mouse Casp3 against rat Casp3 compares ORTHOLOGS
    # ACROSS SPECIES, which is exactly the noise --pair being opt-in exists to avoid.
    _names = [nm.strip() for nm in PAIR_ARG.split(',') if nm.strip()]
    def _matches(path, name):
        org, gene = _org_gene(path)
        return f'{org}/{gene}' == name if '/' in name else gene == name
    PAIR_PATHS = [f for f in files if any(_matches(f, nm) for nm in _names)]
    _missing = [nm for nm in _names if not any(_matches(f, nm) for f in files)]
    if _missing:
        print(f"--pair: no file matched {_missing} in the audited set - nothing compared.")
        print("  audited patterns:", PATTERNS)
        raise SystemExit(2)
    _orgs = {_org_gene(f) for f in PAIR_PATHS}
    if len(_orgs) < 2:
        # One distinct gene (--pair X, or --pair X,X) compares nothing.
        print(f"--pair: {PAIR_ARG!r} resolves to fewer than two distinct genes "
              f"({sorted(_orgs)}) - nothing to compare.")
        raise SystemExit(2)
    # Check each BARE name independently. An earlier version asked whether every
    # matched path shared one gene name, which only caught --pair X,X: with two
    # distinct colliding names (--pair Casp3,Ghr over a mouse+rat glob) the gene set
    # has size 2, the guard passed, and the combinations included mouse Casp3 vs rat
    # Casp3. Per-name is the right granularity and subsumes the same-gene case.
    for _nm in _names:
        if '/' in _nm:
            continue  # already disambiguated by the caller
        _nm_orgs = sorted({o for o, g in _orgs if g == _nm})
        if len(_nm_orgs) > 1:
            print(f"--pair: bare name {_nm!r} matched {len(_nm_orgs)} organisms "
                  f"({_nm_orgs}). Comparing those pairs orthologs across species, "
                  f"not paralogs.")
            print(f"  Disambiguate with the organism/Gene form, "
                  f"e.g. --pair {_nm_orgs[0]}/{_nm},...")
            raise SystemExit(2)

for f in files:
    _parts=os.path.dirname(f).split(os.sep)
    org, g = _parts[-2], _parts[-1]
    own_ids = own.get((org,g), set())
    with open(f) as _fh:
        _raw = _fh.read()
    d=yaml.safe_load(_raw)
    # Whole-document, not per-propagation_review-block: the substitution that motivated
    # this also rewrote `reason`, and a review with no propagation_review at all is just
    # as capable of carrying the damage.
    _ann_terms = {_j: ((_a.get('term') or {}).get('id'))
                  for _j, _a in enumerate(d.get('existing_annotations') or [])}
    for _tpath, _lost in _yaml_comment_truncations(_raw, d):
        _ti = re.match(r'\.existing_annotations\[(\d+)\]', _tpath)
        _tloc = (f"{org}/{g}[{_ti.group(1)}] {_ann_terms.get(int(_ti.group(1))) or '?'}"
                 if _ti else f"{org}/{g}")
        issues.append((_tloc, 'YAML_COMMENT_TRUNCATION', f"{_tpath}: lost {_lost[:60]!r}"))
    for _path, _txt in _walk_prose(d, ''):
        _pos = _mangled_prose(_txt)
        if _pos is not None:
            # Key the same way every other rule does -- "org/gene[i] TERM" -- so the
            # "across N rows" denominator keeps meaning annotation rows. Keying on the
            # dotted path would let one annotation contribute two rows to the headline
            # when it also trips another rule. The path is more useful for LOCATING the
            # damage, so it moves into the payload rather than being dropped.
            _i = re.match(r'\.existing_annotations\[(\d+)\]', _path)
            # `or '?'` on the lookup, not just a dict default: _ann_terms stores None
            # for an annotation with no `term`, and the index always exists, so the
            # default could never fire and such a row would report "mouse/Foo[3] None".
            _loc = (f"{org}/{g}[{_i.group(1)}] {_ann_terms.get(int(_i.group(1))) or '?'}"
                    if _i else f"{org}/{g}")
            issues.append((_loc, 'MANGLED_PROSE',
                           f"{_path}: {_damage_window(_txt, _pos)}"))
    for i,a in enumerate(d.get('existing_annotations') or []):
        r=a.get('review') or {}
        pr=r.get('propagation_review')
        if not pr: continue
        n+=1
        # Key by organism/gene, not the bare basename. The dedupe collapses on the
        # full tuple, so mouse Casp3[12] and rat Casp3[12] emitting the same issue
        # would otherwise merge into one finding -- an UNDERCOUNT, and the third
        # place this same bare-basename keying has had to be fixed (after `own` and
        # `_paths`). Latent until the ISO run populates the colliding genes.
        loc=f"{org}/{g}[{i}] {(a.get('term') or {}).get('id')}"
        rc=pr.get('root_cause'); fms=pr.get('failure_modes') or []; act=r.get('action')
        if rc not in VALID_RC: issues.append((loc,'BAD_ROOT_CAUSE',rc))
        for m in fms:
            if m not in VALID_FM: issues.append((loc,'BAD_FAILURE_MODE',m))
        if rc and rc.startswith('NO_FAILURE') and fms:
            issues.append((loc,'NO_FAILURE_WITH_MODES',f"{rc}+{fms}"))
        if act=='MODIFY' and rc and rc.startswith('NO_FAILURE'):
            issues.append((loc,'MODIFY_WITH_NO_FAILURE',rc))
        # Third arm: a root cause that says the TRANSFER ITSELF failed, sitting under an
        # action that accepts the annotation. Deliberately narrow. TERM_SCOPING_PROBLEM is
        # excluded because it is routinely coherent with KEEP_AS_NON_CORE -- the term is
        # over-scoped but the annotation is still worth keeping (e.g. human IDO1
        # GO:0034354, which contributes only the pathway's entry step). The three below
        # assert the propagation or its source is wrong, which accepting contradicts.
        # ...and gated further: fire only when NOTHING IN THE BLOCK SUBSTANTIATES the
        # claimed failure, i.e. every source_entity (if any) says SUPPORTS_TRANSFER. A
        # block that accepts the term while recording a genuinely faulted source is a
        # coherent stance about two different objects -- the action adjudicates the TERM,
        # these root causes adjudicate the PROVENANCE. Human LMTK2 GO:0070853 (ACCEPT +
        # SOURCE_BAD, flagging a homonym accession) and ADIRF (ACCEPT +
        # EVIDENCE_CIRCULAR_OR_REDUNDANT, "correct term, zero added information") are
        # both deliberate and correct. The Mapk1 block this rule was written for had NO
        # source_entities at all, so nothing backed its PROPAGATION_BAD claim.
        CONTRADICTORY_RC = {'PROPAGATION_BAD','SOURCE_BAD','EVIDENCE_CIRCULAR_OR_REDUNDANT'}
        # An ABSENT source_status is not an endorsement. ~14% of source entities corpus-wide
        # carry no status (3354 status lines against 3902 source_id lines), so defaulting a
        # missing one to SUPPORTS_TRANSFER would make this arm fire on blocks that simply
        # never recorded a judgement. Fire only when there are no sources at all (the Mapk1
        # case: nothing whatsoever backs the claimed failure) or when every source
        # EXPLICITLY says SUPPORTS_TRANSFER.
        _srcs = pr.get('source_entities') or []
        _unsubstantiated = (not _srcs) or all(
            se.get('source_status') == 'SUPPORTS_TRANSFER' for se in _srcs)
        if act in ('ACCEPT','KEEP_AS_NON_CORE') and rc in CONTRADICTORY_RC and _unsubstantiated:
            issues.append((loc,'DEFECT_ROOT_CAUSE_UNDER_ACCEPTING_ACTION',f"{act}+{rc}"))
        # Fourth arm: the inverse -- a corrective action declaring no failure at all.
        if act in ('REMOVE','MARK_AS_OVER_ANNOTATED') and rc and rc.startswith('NO_FAILURE'):
            issues.append((loc,'CORRECTIVE_ACTION_WITH_NO_FAILURE',f"{act}+{rc}"))
        for se in (pr.get('source_entities') or []):
            ss=se.get('source_status'); sid=se.get('source_id') or ''
            # source_status is OPTIONAL in the schema; only flag values that are present
            # but not legal enum members.
            if ss is not None and ss not in VALID_SS:
                issues.append((loc,'BAD_SOURCE_STATUS',ss))
            if sid in own_ids and ss=='CIRCULAR_OR_REDUNDANT':
                issues.append((loc,'SELF_SEED_MARKED_CIRCULAR',sid))
            lab=se.get('source_label') or ''
            # Look up with group(0), NOT group(1): panther.obo writes
            # "id: PANTHER:PTHR10000", so fam_label is keyed WITH the prefix while
            # group(1) drops it. Keying on the bare id made the membership test
            # always False, the and-chain short-circuit silently, and this rule
            # never fire once since the script was checked in.
            m=re.match(r'^PANTHER:(PTHR\d+(?::SF\d+)?)$', sid)
            if m and lab and m.group(0) in fam_label and lab.strip().upper()!=fam_label[m.group(0)].upper():
                issues.append((loc,'PANTHER_LABEL_MISMATCH',f"{sid} label={lab!r} official={fam_label[m.group(0)]!r}"))
        # prose inversion check -- per source comment, not a concatenated blob:
        # the finding has to name WHICH source carries the inverted framing.
        for se in (pr.get('source_entities') or []):
            if (se.get('source_id') or '') in own_ids:
                c=(se.get('comment') or '').lower()
                if _asserts_inverted_framing(c):
                    issues.append((loc,'SELF_SEED_INVERTED_PROSE',se.get('source_id')))
# ---------------------------------------------------------------------------
# Cross-gene consistency: the same (term, evidence_type, reference) reviewed with
# different actions in two files is usually an artifact of the two reviews being
# written independently, not a biological judgement. Run with --pair A,B to compare
# a specific paralog pair, e.g. --pair Mapk1,Mapk3. This is opt-in: it is only a
# defect signal for true paralogs, where the same term/evidence/reference ought to
# get the same call. Two agents reviewing sister genes independently is exactly how
# such divergences arise, and no other rule here catches them.
def action_map(path):
    d = yaml.safe_load(open(path))
    m = {}
    for a in (d.get('existing_annotations') or []):
        k = ((a.get('term') or {}).get('id'), a.get('evidence_type'), a.get('original_reference_id'))
        m.setdefault(k, set()).add((a.get('review') or {}).get('action'))
    return m

pair_arg = PAIR_ARG
if pair_arg:
    _paths = PAIR_PATHS  # already validated above, before the audit ran
    _combos = [(_paths[i], _paths[j]) for i in range(len(_paths)) for j in range(i + 1, len(_paths))]
    # Unreachable as written: the validation above requires >=2 distinct (organism,
    # gene) in PAIR_PATHS, so there is always >=1 combination. Kept as a backstop in
    # case that validation is later relaxed -- but it is NOT the live guard, and
    # editing it will not change any behaviour. The real checks are with PAIR_PATHS.
    if not _combos:  # pragma: no cover - see above
        print(f"--pair: {pair_arg!r} produced no comparable pair - nothing compared.")
        raise SystemExit(2)
else:
    # No automatic pairing. Two unrelated genes sharing a term legitimately get
    # different actions (Src vs Syk, Myc vs Stat1 ...), so an unguided sweep emits
    # noise rather than defects. The check only means something for genuine
    # paralogs, which the caller has to name.
    _combos = []

cross = []
for fa, fb in _combos:
    ma, mb = action_map(fa), action_map(fb)
    # organism/gene: an explicit --pair mouse/Casp3,rat/Casp3 is permitted (the
    # caller disambiguated deliberately), and 'Casp3 vs Casp3' would be useless.
    ga = '/'.join(_org_gene(fa)); gb = '/'.join(_org_gene(fb))
    for k in sorted(set(ma) & set(mb)):
        if ma[k] != mb[k]:
            cross.append((f"{ga} vs {gb}", k[0], k[1], sorted(ma[k]), sorted(mb[k])))
if cross:
    print(f"\nCROSS-GENE ACTION DIVERGENCES ({len(cross)}):")
    for c in cross:
        print(f"   {c[0]}  {c[1]} {c[2]}: {c[3]} vs {c[4]}")

# Collapse only EXACT duplicates. Keying on (loc, issue_type) would discard the payload
# when a per-value rule fires twice on one row -- BAD_FAILURE_MODE, BAD_SOURCE_STATUS,
# SELF_SEED_MARKED_CIRCULAR, SELF_SEED_INVERTED_PROSE and PANTHER_LABEL_MISMATCH are all
# emitted per source or per value, so a block with two offending sources would report
# one. That is an undercount, which is the failure direction that matters here.
# The overlapping arms are NOT collapsed (they emit different issue_type strings); the
# "across N rows" figure below is what keeps the headline from overstating.
_seen=set(); _dedup=[]
for _i in issues:
    _k=tuple(_i)
    if _k in _seen: continue
    _seen.add(_k); _dedup.append(_i)
_rows={_i[0] for _i in _dedup}
issues=_dedup

print(f"audited {n} propagation_review blocks across {len(files)} files")
if issues:
    print(f"ISSUES ({len(issues)} across {len(_rows)} rows):")
    for x in issues: print("  ", x)
else:
    print("no issues found")

# Exit code semantics. By default this is a report tool and findings exit 0. Under
# --strict, findings (and cross-gene divergences) exit 1, so a CI job's green means
# "clean" rather than merely "ran" -- reading the exit code is otherwise the natural
# mistake once this is wired into the ISO backlog run. Note 2 is already taken by the
# self-test and the zero-input/bad---pair guards, which are failures of the RUN, not
# findings about the corpus.
if STRICT and (issues or cross):
    raise SystemExit(1)
