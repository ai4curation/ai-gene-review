"""Verify ordered seed payloads and frozen evidence without altering source artifacts.

Run from repository root:
  uv run python analysis/module_audits/bacterial_groel_groes_chaperonin_folding/caulobacter-preservation.py
Optional --all-protected verifies the ignored cache-wide source snapshot as well.
"""
from pathlib import Path
import argparse, hashlib, json
from collections import Counter
import yaml

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--all-protected',type=Path)
    parser.add_argument('--output',type=Path,default=Path('analysis/module_audits/bacterial_groel_groes_chaperonin_folding/caulobacter-preservation.json'))
    args=parser.parse_args()
    folder=Path('analysis/module_audits/bacterial_groel_groes_chaperonin_folding')
    baseline=folder/'caulobacter-seed-baseline.json'
    snapshot=folder/'caulobacter-protected-baseline.json'
    members=json.loads(baseline.read_text())['members']
    evidence=json.loads(snapshot.read_text())
    result={'seed_baseline_sha256':sha(baseline),'protected_baseline_sha256':sha(snapshot),'members':[]}
    actions=Counter()
    for member in members:
        p=Path(member['review_path']);d=yaml.safe_load(p.read_text())
        assert d['id']==member['accession'] and d['taxon']==member['taxon'],p
        rows=d['existing_annotations']
        payloads=[{k:v for k,v in row.items() if k!='review'} for row in rows]
        assert payloads==member['payloads'],f'ordered payload changed: {p}'
        assert all(row['review']['action']!='PENDING' for row in rows),p
        assert not any(row.get('retired',False) for row in rows),p
        for raw,expected in member['raw_sha256'].items():
            assert sha(Path(raw))==expected,raw
        a=Counter(row['review']['action'] for row in rows);actions.update(a)
        result['members'].append({'path':str(p),'sha256':sha(p),'ordered_payloads_preserved':len(rows),'actions':dict(a),'raw_files_preserved':len(member['raw_sha256'])})
    for path,expected in evidence.items():
        assert sha(Path(path))==expected,path
    result.update(total_ordered_rows=sum(len(m['payloads']) for m in members),actions=dict(actions),new_rows=actions['NEW'],retired_rows=0,added_or_deleted_rows=0,protected_sources_preserved=len(evidence))
    if args.all_protected:
        all_evidence=json.loads(args.all_protected.read_text())
        for path,expected in all_evidence.items():
            assert sha(Path(path))==expected,path
        result['additional_source_snapshot']={'path':str(args.all_protected),'sha256':sha(args.all_protected),'files_preserved':len(all_evidence)}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
