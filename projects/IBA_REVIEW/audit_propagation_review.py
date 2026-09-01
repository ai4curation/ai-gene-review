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
import yaml, glob, os, re, csv, sys

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
# gene -> its own MGI id, read from each gene's UniProt record
mgi={}
for _d in glob.glob('genes/*/*/'):
    _g=os.path.basename(_d.rstrip('/'))
    _f=f'{_d}{_g}-uniprot.txt'
    if os.path.exists(_f):
        _m=re.search(r'^DR   MGI; (MGI:\d+);', open(_f).read(), re.M)
        if _m: mgi[_g]=_m.group(1)
own={}
for d in sorted(glob.glob('genes/*/*/')):
    g=os.path.basename(d.rstrip('/')); s=set()
    if mgi.get(g): s.add('MGI:'+mgi[g])
    f=f'{d}{g}-uniprot.txt'
    if os.path.exists(f):
        m=re.search(r'^AC   (.+)$', open(f).read(), re.M)
        if m:
            for a in m.group(1).split(';'):
                if a.strip(): s.add('UniProtKB:'+a.strip())
    own[g]=s

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
    g=os.path.basename(os.path.dirname(f))
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
        for se in (pr.get('source_entities') or []):
            ss=se.get('source_status'); sid=se.get('source_id') or ''
            if ss not in VALID_SS: issues.append((loc,'BAD_SOURCE_STATUS',ss))
            if sid in own.get(g,set()) and ss=='CIRCULAR_OR_REDUNDANT':
                issues.append((loc,'SELF_SEED_MARKED_CIRCULAR',sid))
            lab=se.get('source_label') or ''
            m=re.match(r'^PANTHER:(PTHR\d+)$', sid)
            if m and lab and m.group(1) in fam_label and lab.strip().upper()!=fam_label[m.group(1)].upper():
                issues.append((loc,'PANTHER_LABEL_MISMATCH',f"{sid} label={lab!r} official={fam_label[m.group(1)]!r}"))
        # prose inversion check
        txt=((r.get('reason') or '')+' '+(r.get('summary') or '')+' '+
             ' '.join((se.get('comment') or '') for se in (pr.get('source_entities') or [])))
        for se in (pr.get('source_entities') or []):
            if (se.get('source_id') or '') in own.get(g,set()):
                c=(se.get('comment') or '').lower()
                bad_circular = ('circular' in c and not any(k in c for k in
                    ('not circular','rather than circular','is not circular','never circular')))
                if 'no independent' in c or 'self-supporting' in c or bad_circular:
                    issues.append((loc,'SELF_SEED_INVERTED_PROSE',se.get('source_id')))
print(f"audited {n} propagation_review blocks across {len(files)} files")
if issues:
    print(f"ISSUES ({len(issues)}):")
    for x in issues: print("  ", x)
else:
    print("no issues found")
