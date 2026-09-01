"""Audit propagation_review blocks against the rules in projects/IBA_REVIEW.md.

Checks each block for:
  * enum values that exist in the schema (root_cause / failure_modes / source_status)
  * NO_FAILURE_* paired with failure_modes (naming a failure while declaring none)
  * MODIFY carrying a NO_FAILURE_* root cause (proposing a replacement IS term scoping)
  * a self-seed source marked CIRCULAR_OR_REDUNDANT, or described with the inverted
    "adds no independent evidence" prose -- finding 1 of
    projects/IBA_REVIEW/propagation-review-audit.md
  * PANTHER family labels that disagree with interpro/panther/panther.obo

Usage:  python3 projects/IBA_REVIEW/audit_propagation_review.py [glob ...]
Defaults to genes/mouse/*/*-ai-review.yaml; pass globs to audit other organisms,
e.g. the ISO backlog:  ... audit_propagation_review.py 'genes/human/*/*-ai-review.yaml'
"""
import yaml, glob, os, re, csv

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
PATTERNS = sys.argv[1:] or ['genes/mouse/*/*-ai-review.yaml']

# Model-organism database cross-references that appear as self-seed ids in WITH/FROM.
# The DR line name and the id prefix used in GOA differ for several of these.
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
files=[f for pat in PATTERNS for f in sorted(glob.glob(pat))]
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
        # Third arm of the same consistency rule: a DEFECT root cause sitting under an
        # action that accepts the annotation. Usually a stale block left behind when the
        # action was softened, so the machine-readable field contradicts the prose.
        DEFECT_RC = {'SOURCE_BAD','SOURCE_STALE_OR_MISSING','SOURCE_WEAK_OR_INFERRED',
                     'EVIDENCE_CIRCULAR_OR_REDUNDANT','PROPAGATION_BAD','TERM_SCOPING_PROBLEM'}
        if act in ('ACCEPT','KEEP_AS_NON_CORE') and rc in DEFECT_RC:
            issues.append((loc,'DEFECT_ROOT_CAUSE_UNDER_ACCEPTING_ACTION',f"{act}+{rc}"))
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

pair_arg = None
for _i, _a in enumerate(sys.argv):
    if _a == '--pair' and _i + 1 < len(sys.argv):
        pair_arg = sys.argv[_i + 1]
if pair_arg:
    _names = pair_arg.split(',')
    _paths = [f for f in files if os.path.basename(os.path.dirname(f)) in _names]
    _combos = [(_paths[i], _paths[j]) for i in range(len(_paths)) for j in range(i + 1, len(_paths))]
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

print(f"audited {n} propagation_review blocks across {len(files)} files")
if issues:
    print(f"ISSUES ({len(issues)}):")
    for x in issues: print("  ", x)
else:
    print("no issues found")
