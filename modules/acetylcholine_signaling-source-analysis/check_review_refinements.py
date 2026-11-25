"""Audit replacement GO aspects after the VAChT MF-to-CC curation error.

Run with uv run python. This checks semantic branches, not whether a claim is
biologically justified. Unresolvable source terms are reported for review.
"""
import json
from functools import cache
from pathlib import Path
import yaml
from ai_gene_review.validation.module_validator import (
    _get_cached_adapter, load_oak_adapter_map,
)

ROOT = Path(__file__).resolve().parents[2]
ROOTS = {'GO:0003674': 'MF', 'GO:0008150': 'BP', 'GO:0005575': 'CC'}

def main():
    adapter_name = load_oak_adapter_map(ROOT / 'conf/oak_config.yaml').get('GO')
    assert adapter_name is not None, 'GO ancestry resolver unavailable'
    adapter = _get_cached_adapter(adapter_name)
    panel = json.loads((Path(__file__).parent / 'members.json').read_text())
    checked = 0
    mismatches = []
    unresolved = []
    @cache
    def aspects(curie):
        # MF activities can be part_of BP; only is_a defines ontology aspect.
        ancestors = set(adapter.ancestors(curie, predicates=['rdfs:subClassOf']))
        return {ROOTS[x] for x in ancestors | {curie} if x in ROOTS}
    for member in panel:
        org, gene = member['organism'], member['symbol']
        review = yaml.safe_load((ROOT / f'genes/{org}/{gene}/{gene}-ai-review.yaml').read_text())
        for index, row in enumerate(review.get('existing_annotations', [])):
            for replacement in row.get('review', {}).get('proposed_replacement_terms', []):
                old, new = row['term']['id'], replacement['id']
                if not old.startswith('GO:') or not new.startswith('GO:'):
                    continue
                checked += 1
                a, b = aspects(old), aspects(new)
                record = {'gene': f'{org}/{gene}', 'row': index, 'original': old, 'replacement': new}
                if not a or not b:
                    unresolved.append(record)
                elif a != b:
                    mismatches.append(dict(record, original_aspects=sorted(a), replacement_aspects=sorted(b)))
    result = {'checked_replacements': checked, 'cross_aspect_replacements': mismatches, 'unresolved': unresolved}
    out = ROOT / '.cache/module-audit-logs/acetylcholine-refinement-aspects.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(mismatches or unresolved))

if __name__ == '__main__':
    main()
