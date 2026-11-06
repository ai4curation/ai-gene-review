"""Read-only checks for PTHR42803 evidence and released-file preservation.

Run with `uv run python <this-file>` from the repository root. Uses existing
caches only: no fetching, member-index building, or curated-file mutation.
"""
from pathlib import Path
import gzip
import hashlib
import json
import re
import yaml
from ai_gene_review.etl.panther_families import load_member_index, load_member_index_alternates
from ai_gene_review.validation.module_validator import FamilyMemberUse, validate_family_members

ROOT = Path(__file__).resolve().parents[4]
CACHE = ROOT / '.cache/module-audit-logs/beta-oxidation-20261106/pao1-family'
review_path = ROOT / 'interpro/panther/PTHR42803/PTHR42803-review.yaml'
doc = yaml.safe_load(review_path.read_text())
proof = yaml.safe_load((Path(__file__).parent / 'lineage-proof.yaml').read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
quotes = []

def walk(value):
    if isinstance(value, dict):
        if 'reference_id' in value and 'supporting_text' in value:
            ref, quote = value['reference_id'], value['supporting_text']
            path = ROOT / ('publications/' + ref.replace(':', '_') + '.md' if ref.startswith('PMID:') else ref.removeprefix('file:'))
            assert norm(quote) in norm(path.read_text()), ref
            quotes.append({'reference_id': ref, 'verified': True})
        for child in value.values(): walk(child)
    elif isinstance(value, list):
        for child in value: walk(child)
walk(doc)
titles = 0
for ref in doc['references']:
    if ref['id'].startswith('PMID:'):
        text = (ROOT / 'publications' / (ref['id'].replace(':', '_')+'.md')).read_text()
        metadata = yaml.safe_load(text.split('\n---\n')[0].removeprefix('---\n'))
        assert ref['title'] == metadata['title']
        titles += 1
obo = (ROOT / 'interpro/panther/panther.obo').read_text()
assert f"id: {doc['family_id']}\nname: {doc['family_name']}\n" in obo
uses = []
for sub in doc['subfamilies']:
    assert f"id: {sub['subfamily_id']}\nname: {sub['label']}\n" in obo
    uses.append(FamilyMemberUse(path='subfamilies.'+sub['subfamily_id'], declared_family_curies=frozenset([sub['subfamily_id']]), representative_accessions=frozenset(m['id'].removeprefix('UniProtKB:') for m in sub['representative_members']), ancestral_node_curies=frozenset()))
index_path = ROOT / '.cache/panther/panther-members-19.0.tsv'
errors, warnings = validate_family_members(uses, load_member_index(index_path), alternates=load_member_index_alternates(index_path))
assert not errors, errors
for path, expected in proof['original_files'].items():
    assert sha(ROOT/path) == expected, path
assert not (review_path.parent / 'PTHR42803-paint.tsv').exists()
# Check exact tree leaf-to-accession correspondence without inventing clade functions.
tree_path = ROOT / '.cache/panther_trees/PTHR42803.json.gz'
assert sha(tree_path) == proof['tree']['compact_cache_sha256']
with gzip.open(tree_path, 'rt') as handle: tree = json.load(handle)
for node, member in proof['tree']['exact_members'].items():
    assert tree['leaves'][node] == member
assert set(tree['under'][proof['tree']['common_pseudomonas_clade']['node']]) == set(proof['tree']['common_pseudomonas_clade']['members'])
assert proof['PAINT']['annotation_rows'] == 0 and doc['node_assessments'] == []
# The normal fetch and independent IBD intersection are recorded with exact input hashes.
for source in proof['PAINT']['sources']:
    path = ROOT / '.cache/panther' / source['url'].rsplit('/',1)[1]
    assert sha(path) == source['sha256'], str(path)
from ai_gene_review.etl.panther_paint import open_text, parse_ibd_gaf, treegrafter_family_nodes
with open_text(ROOT / '.cache/panther/PAINT_TreeGrafter_Annotations_TOTAL.txt.gz') as handle:
    nodes = treegrafter_family_nodes(handle)['PTHR42803']
with open_text(ROOT / '.cache/panther/IBD.gaf') as handle:
    ibd = parse_ibd_gaf(handle)
assert sorted(nodes) == proof['PAINT']['resolved_nodes']
assert not set(nodes).intersection(ibd)
baseline = json.loads((CACHE/'baseline.json').read_text())
for category in ['original_family_files', 'frozen_gene_files']:
    for path, expected in baseline[category].items():
        assert sha(ROOT/path) == expected, path
print(json.dumps({'status':'PASS','quotes_checked':len(quotes),'titles_checked':titles,'official_labels_checked':2,'representatives_checked':sum(len(u.representative_accessions) for u in uses),'membership_errors':errors,'membership_warnings':warnings,'tree_members_checked':len(proof['tree']['exact_members']),'PAINT_nodes_checked':len(nodes),'PAINT_assertions':0,'original_family_files_preserved':len(baseline['original_family_files']),'released_gene_files_preserved':len(baseline['frozen_gene_files']),'baseline_sha256':sha(CACHE/'baseline.json'),'quotes':quotes},indent=2))
