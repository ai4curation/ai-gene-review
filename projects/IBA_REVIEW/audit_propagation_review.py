"""Audit propagation_review blocks against the rules in projects/IBA_REVIEW.md.

Checks each block for:
  * enum values that exist in the schema (root_cause / failure_modes / source_status)
  * NO_FAILURE_* paired with failure_modes (naming a failure while declaring none)
  * MODIFY carrying a NO_FAILURE_* root cause (proposing a replacement IS term scoping)
  * a self-seed source marked CIRCULAR_OR_REDUNDANT, or described with the inverted
    "adds no independent evidence" prose -- finding 1 of
    projects/IBA_REVIEW/propagation-review-audit.md
  * PANTHER family labels that disagree with interpro/panther/panther.obo

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
            pair = argv[i + 1]; i += 2; continue
        if tok.startswith('--pair='):
            pair = tok[len('--pair='):]; i += 1; continue
        if tok == '--strict':
            strict = True; i += 1; continue
        # Anything else that LOOKS like a flag is a typo, not a glob. Falling through
        # to globs is only caught by the zero-inputs guard when no real glob is also
        # passed; with one, '--pairs A,B <glob>' or '--strct <glob>' audits every file
        # and exits 0 having done neither thing the caller asked for -- and a mistyped
        # --strict silently turns a CI gate back into a report while still going green.
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
if _selftest_failures:
    print("SELF-TEST FAILED - self-seed detection is not working:")
    for _f in _selftest_failures:
        print("   ", _f)
    raise SystemExit(2)

# valid PANTHER family labels
fam_label={}
try:
    cur=None
    for line in open('interpro/panther/panther.obo'):
        line=line.rstrip('\n')
        if line.startswith('id: PANTHER:'): cur=line.split('id: ')[1]
        elif line.startswith('name: ') and cur: fam_label[cur]=line[6:]; cur=None
except Exception: pass

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
    d=yaml.safe_load(open(f))
    for i,a in enumerate(d.get('existing_annotations') or []):
        r=a.get('review') or {}
        pr=r.get('propagation_review')
        if not pr: continue
        n+=1
        loc=f"{g}[{i}] {(a.get('term') or {}).get('id')}"
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
            m=re.match(r'^PANTHER:(PTHR\d+(?::SF\d+)?)$', sid)
            if m and lab and m.group(1) in fam_label and lab.strip().upper()!=fam_label[m.group(1)].upper():
                issues.append((loc,'PANTHER_LABEL_MISMATCH',f"{sid} label={lab!r} official={fam_label[m.group(1)]!r}"))
        # prose inversion check
        txt=((r.get('reason') or '')+' '+(r.get('summary') or '')+' '+
             ' '.join((se.get('comment') or '') for se in (pr.get('source_entities') or [])))
        for se in (pr.get('source_entities') or []):
            if (se.get('source_id') or '') in own_ids:
                c=(se.get('comment') or '').lower()
                bad_circular = ('circular' in c and not any(k in c for k in
                    ('not circular','rather than circular','is not circular','never circular')))
                if 'no independent' in c or 'self-supporting' in c or bad_circular:
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
    ga = os.path.basename(os.path.dirname(fa)); gb = os.path.basename(os.path.dirname(fb))
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
