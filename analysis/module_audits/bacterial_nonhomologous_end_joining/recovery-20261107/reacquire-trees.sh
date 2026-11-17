env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/Users/cjm/worktrees/aigr-nhej-audit-recovery/src /Users/cjm/orca/workspaces/ai-gene-review/aigr-modules-taxon/.venv/bin/python -P - <<'PY'
from pathlib import Path
import requests,json,gzip,hashlib,datetime
from ai_gene_review.etl.panther_trees import compact_tree,leaf_nodes_for,ancestors_of,TREE_URL
out=Path('analysis/module_audits/bacterial_nonhomologous_end_joining/tree-evidence-20261107');out.mkdir(exist_ok=False)
for fam,members in {'PTHR41251':['Q88HU8','Q9I1W5','P9WKD9','O34859'],'PTHR42705':['Q88HU3','Q9I1X7','P9WNV3','O34398','P9WNV2']}.items():
 r=requests.get(TREE_URL,params={'family':fam},timeout=35);r.raise_for_status();raw=r.content;tree=compact_tree(r.json());(out/(fam+'-treeinfo.json.gz')).write_bytes(gzip.compress(raw,mtime=0));(out/(fam+'-compact.json')).write_text(json.dumps(tree,sort_keys=True)+'\n');receipt={'url':r.url,'reacquired_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'raw_sha256':hashlib.sha256(raw).hexdigest(),'leaf_count':len(tree['leaves']),'members':{},'scope':'Tree paths only; join exact PAINT IBD rows and experimental evidence before judging claims.'}
 for acc in members:
  leaves=leaf_nodes_for(tree,acc);receipt['members'][acc]={'leaves':leaves,'paths':{leaf:sorted(ancestors_of(tree,leaf)) for leaf in leaves},'leaf_metadata':{leaf:tree['leaves'][leaf] for leaf in leaves}}
 (out/(fam+'-receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n');print(fam,len(tree['leaves']),{a:len(v['leaves']) for a,v in receipt['members'].items()},flush=True)
PY
