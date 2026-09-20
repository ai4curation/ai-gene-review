#!/usr/bin/env python3
"""Verify that `supporting_text` on `file:` references is verbatim.

The reference validator checks `supporting_text` only for `PMID:` references. Quotes
attributed to `file:` references (deep-research reports, UniProt records, GOA tables)
have never been checked, and paraphrase presented as quotation has accumulated there.

Run:  uv run --no-dev python scripts/check_file_supporting_text.py

Notes on false positives: UniProt `.txt` records carry two-letter line-prefix codes
(DE, CC, FT...) that break naive substring matching, so those are stripped first.
Remaining mismatches still include benign cases (smart quotes, ellipses, quotes
stitched across non-contiguous lines). The unambiguous subset is the one reported
separately: quotes that begin with a narration word such as "Falcon report
summarizes", which cannot be verbatim source text by construction.
"""

import yaml, glob, os, re, json
from collections import Counter

def strip_prefix(txt):
    return "\n".join(re.sub(r'^[A-Z]{2}(   |\s{3})', '', ln) for ln in txt.splitlines())
def norm(s): return re.sub(r'\s+', ' ', s or '').strip().lower()

def walk(o, out):
    if isinstance(o, dict):
        if 'reference_id' in o and 'supporting_text' in o: out.append((o['reference_id'], o['supporting_text']))
        for v in o.values(): walk(v, out)
    elif isinstance(o, list):
        for v in o: walk(v, out)

cache={}
def body(p):
    if p not in cache:
        try:
            t=open(p,encoding='utf-8',errors='replace').read()
            if p.endswith('.txt'): t=strip_prefix(t)
            cache[p]=norm(t)
        except Exception: cache[p]=None
    return cache[p]

bad=[]; checked=Counter(); badc=Counter(); unresolved=[]; unreadable=[]
for f in sorted(glob.glob('genes/*/*/*-ai-review.yaml')):
    try: d=yaml.safe_load(open(f,encoding='utf-8'))
    except Exception: continue
    pairs=[]; walk(d,pairs)
    for rid,txt in pairs:
        if not isinstance(rid,str) or not rid.startswith('file:'): continue
        p=rid[5:]; real=next((c for c in (p,os.path.join('genes',p)) if os.path.exists(c)),None)
        if real is None:
            # A file: reference whose path does not resolve is its own defect, and silently
            # skipping it also inflates the apparent coverage: the quote is neither checked
            # nor counted, so "N checked" reads as if it were the whole population.
            unresolved.append((f,rid)); continue
        kind = 'uniprot' if real.endswith('-uniprot.txt') else ('deep-research' if 'deep-research' in real else ('goa' if real.endswith('.tsv') else 'other-md'))
        b=body(real)
        if b is None:
            # Resolvable but unreadable. Counting it as checked would inflate coverage the
            # same way an unresolvable path does, just one level down: nothing was compared.
            unreadable.append((f,rid)); continue
        checked[kind]+=1
        if norm(txt) not in b:
            badc[kind]+=1; bad.append((f,rid,kind,(txt or '')[:100]))
print('checked by type:',dict(checked))
print('UNRESOLVED file: paths (path does not exist; not compared, not counted above):',len(unresolved))
for f,rid in unresolved[:10]: print('   ',f,rid)
print('UNREADABLE file: paths (path exists but could not be read; likewise not counted):',len(unreadable))
for f,rid in unreadable[:10]: print('   ',f,rid)
print('MISMATCH by type:',dict(badc))
print()
print('=== deep-research mismatches: how many are narrated paraphrase? ===')
dr=[b for b in bad if b[2]=='deep-research']
pat=re.compile(r'^(falcon|the falcon|deep research|this file|the file|synthesis|research)\b', re.I)
narr=[b for b in dr if pat.match((b[3] or '').strip())]
print(f'  deep-research mismatches: {len(dr)}; starting with a narration word: {len(narr)}')
for b in narr[:10]: print('   ',b[0].split("/")[2],'|',b[3][:85])
# Self-describing report: the mismatches plus the two populations that were NOT
# compared, so a reader cannot mistake "checked" for "every file: quote in the repo".
json.dump({'checked_by_type': dict(checked),
           'mismatches_by_type': dict(badc),
           'unresolved_paths': unresolved,
           'unreadable_paths': unreadable,
           'mismatches': bad},
          open('reports/file_supporting_text_mismatches.json','w'), indent=1)
