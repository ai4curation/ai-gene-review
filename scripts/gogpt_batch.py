#!/usr/bin/env python3
"""Batch GO-GPT predictions — loads model once, clears memory between genes."""
import csv
import gc
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable

import yaml

REPO = Path(os.environ.get("AIGR_DIR", Path(__file__).resolve().parents[1]))
MODEL_DIR = Path(os.path.expanduser('~/repos/BioReason-Pro/models/gogpt'))
sys.path.insert(0, str(Path.home() / 'repos/BioReason-Pro/gogpt/src'))

GENERIC_TERMS = {
    'GO:0003674', 'GO:0008150', 'GO:0005575',
    'GO:0005488', 'GO:0009987', 'GO:0008152',
    'GO:0044237', 'GO:0071704', 'GO:0044238',
    'GO:0006807', 'GO:0044260', 'GO:0043170',
    'GO:0097159', 'GO:1901363',
}

ORG_MAP = {
    'human': 'Homo sapiens',
    'mouse': 'Mus musculus',
    'rat': 'Rattus norvegicus',
    'yeast': 'Saccharomyces cerevisiae (strain ATCC 204508 / S288c)',
    'worm': 'Caenorhabditis elegans',
    'DROME': 'Drosophila melanogaster',
    'ARATH': 'Arabidopsis thaliana',
    'PSEPK': 'Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)',
    'ECOLI': 'Escherichia coli (strain K12)',
}

GO_NAMESPACE_TO_ASPECT = {
    "molecular_function": "MF",
    "biological_process": "BP",
    "cellular_component": "CC",
}
LOCAL_GO_ADAPTER = "sqlite:obo:go"
AspectResolver = Callable[[str], str | None]


def extract_sequence(uniprot_file):
    lines = uniprot_file.read_text().splitlines()
    in_seq = False
    seq = []
    for line in lines:
        if line.startswith('SQ'):
            in_seq = True
            continue
        if in_seq:
            if line.startswith('//'):
                break
            seq.append(line.strip().replace(' ', ''))
    return ''.join(seq)


class GoAspectResolutionError(RuntimeError):
    """Raised when a GO-valued NEW term cannot be assigned safely to an aspect."""


class LocalGoAspectResolver:
    """Resolve GO aspects once from the repository-standard local OAK snapshot."""

    def __init__(self, adapter: Any | None = None):
        self._adapter = adapter
        self._cache: dict[str, str | None] = {}

    def _get_adapter(self) -> Any:
        if self._adapter is None:
            from oaklib import get_adapter

            self._adapter = get_adapter(LOCAL_GO_ADAPTER)
        return self._adapter

    def resolve(self, go_id: str) -> str:
        """Return MF/BP/CC, following one authoritative obsolete replacement."""
        if not go_id.startswith("GO:"):
            raise GoAspectResolutionError(f"Not a GO identifier: {go_id}")
        aspect = self._resolve(go_id, ())
        if aspect is None:
            raise GoAspectResolutionError(f"Unable to resolve GO aspect for {go_id}")
        return aspect

    def _resolve(self, go_id: str, path: tuple[str, ...]) -> str | None:
        if go_id in self._cache:
            return self._cache[go_id]
        if go_id in path:
            cycle = " -> ".join((*path, go_id))
            raise GoAspectResolutionError(
                f"GO replacement cycle while resolving aspect: {cycle}"
            )

        try:
            statements = list(
                self._get_adapter().entities_metadata_statements(
                    [go_id],
                    predicates=["oio:hasOBONamespace", "IAO:0100001"],
                    include_nested_metadata=True,
                )
            )
        except Exception as error:
            raise GoAspectResolutionError(
                f"Unable to query local GO metadata for {go_id}: {error}"
            ) from error

        namespaces: set[str] = set()
        replacements: set[str] = set()
        for subject, predicate, value, *_ in statements:
            if subject != go_id:
                continue
            if predicate == "oio:hasOBONamespace":
                namespaces.add(str(value))
            elif predicate == "IAO:0100001" and str(value).startswith("GO:"):
                replacements.add(str(value))

        aspects = {
            aspect
            for namespace in namespaces
            if (aspect := GO_NAMESPACE_TO_ASPECT.get(namespace))
        }
        if len(aspects) > 1:
            raise GoAspectResolutionError(
                f"Conflicting GO aspects found for {go_id}: {sorted(aspects)}"
            )
        if aspects:
            aspect = next(iter(aspects))
            self._cache[go_id] = aspect
            return aspect

        if len(replacements) > 1:
            raise GoAspectResolutionError(
                f"Multiple authoritative GO replacements found for {go_id}: "
                f"{sorted(replacements)}"
            )
        if not replacements:
            self._cache[go_id] = None
            return None

        replacement = next(iter(replacements))
        aspect = self._resolve(replacement, (*path, go_id))
        self._cache[go_id] = aspect
        return aspect


def load_review_terms(
    review_file,
    goa_file,
    aspect_resolver: AspectResolver | None = None,
):
    """Load retained/replacement/new and core terms partitioned by GO aspect."""
    with open(review_file) as f:
        review = yaml.safe_load(f)

    aspect_by_id = {}
    if goa_file.exists():
        with goa_file.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                aspect = {
                    "molecular_function": "MF",
                    "biological_process": "BP",
                    "cellular_component": "CC",
                }.get(row.get("GO ASPECT", ""))
                if aspect:
                    aspect_by_id[row.get("GO TERM", "")] = aspect

    terms: dict[str, set[str]] = {"MF": set(), "BP": set(), "CC": set()}
    for ann in review.get('existing_annotations', []):
        if ann.get("negated") is True:
            continue
        t = ann.get('term', {})
        go_id = t.get('id', '')
        aspect = aspect_by_id.get(go_id)
        action = (ann.get("review") or {}).get("action", "")
        if action == "NEW" and go_id.startswith("GO:"):
            if aspect_resolver is None:
                aspect_resolver = LocalGoAspectResolver().resolve
            try:
                new_aspect = aspect_resolver(go_id)
            except GoAspectResolutionError:
                raise
            except Exception as error:
                raise GoAspectResolutionError(
                    f"Unable to resolve GO aspect for NEW term {go_id}: {error}"
                ) from error
            if new_aspect not in terms:
                raise GoAspectResolutionError(
                    f"Unable to resolve GO aspect for NEW term {go_id}"
                )
            terms[new_aspect].add(go_id)
        elif action == "MODIFY" and aspect:
            for replacement in (ann.get("review") or {}).get(
                "proposed_replacement_terms", []
            ):
                replacement_id = replacement.get("id", "")
                if replacement_id.startswith("GO:"):
                    terms[aspect].add(replacement_id)
        elif action in {"", "ACCEPT", "KEEP_AS_NON_CORE", "UNDECIDED", "PENDING"}:
            if aspect and go_id.startswith("GO:"):
                terms[aspect].add(go_id)
    for cf in review.get('core_functions', []):
        for slot in ("molecular_function", "contributes_to_molecular_function"):
            mf = cf.get(slot, {})
            if mf and mf.get('id', '').startswith('GO:'):
                terms['MF'].add(mf['id'])
        for bp in cf.get('directly_involved_in', []):
            if bp.get('id', '').startswith('GO:'):
                terms['BP'].add(bp['id'])
        complex_term = cf.get("in_complex", {})
        if complex_term and complex_term.get("id", "").startswith("GO:"):
            terms["CC"].add(complex_term["id"])
        for location in cf.get("locations", []):
            if location.get("id", "").startswith("GO:"):
                terms["CC"].add(location["id"])
    return terms

def main():
    import torch  # type: ignore[import-not-found]
    from gogpt.inference import (  # type: ignore[import-not-found]
        GOGPTPredictor,
        GOTokenizerJSON,
        OrganismMapperJSON,
    )
    from transformers import AutoTokenizer  # type: ignore[import-not-found]
    
    print("Loading GO-GPT model...", flush=True)
    predictor = object.__new__(GOGPTPredictor)
    predictor.device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    predictor.verbose = False
    predictor.config_path = str(MODEL_DIR / 'config.yaml')
    predictor._embed_model_path = 'facebook/esm2_t36_3B_UR50D'
    with open(MODEL_DIR / 'tokenizer_info.json') as f:
        predictor.tokenizer_info = json.load(f)
    predictor.go_tokenizer = GOTokenizerJSON.from_json(MODEL_DIR / 'go_tokenizer.json')
    predictor.organism_mapper = OrganismMapperJSON.from_json(MODEL_DIR / 'organism_mapper.json')
    predictor.protein_tokenizer = AutoTokenizer.from_pretrained('facebook/esm2_t36_3B_UR50D')
    predictor._load_model(str(MODEL_DIR / 'model.ckpt'))
    print(f"Model loaded on {predictor.device}", flush=True)
    
    genes = []
    for review_file in sorted(REPO.glob('genes/**/*-ai-review.yaml')):
        gene_dir = review_file.parent
        gene = gene_dir.name
        org = gene_dir.parent.name
        uniprot = gene_dir / f'{gene}-uniprot.txt'
        if uniprot.exists():
            genes.append((org, gene, uniprot, review_file))
    
    print(f"Found {len(genes)} genes to process", flush=True)
    
    results = []
    go_aspect_resolver = LocalGoAspectResolver()
    for i, (org, gene, uniprot, review_file) in enumerate(genes):
        try:
            seq = extract_sequence(uniprot)
            if not seq or len(seq) < 10:
                continue
            if len(seq) > 2000:
                seq = seq[:2000]
            
            org_name = ORG_MAP.get(org, org)
            if org_name == org:
                for name in predictor.organism_mapper.organism_to_idx:
                    if org.lower() in name.lower():
                        org_name = name
                        break
            
            with torch.no_grad():
                preds = predictor.predict(sequence=seq, organism=org_name)
            
            review_terms = load_review_terms(
                review_file,
                review_file.parent / f"{gene}-goa.tsv",
                aspect_resolver=go_aspect_resolver.resolve,
            )
            
            for aspect in ['MF', 'BP', 'CC']:
                pred_set = set(preds.get(aspect, [])) - GENERIC_TERMS
                rev_set = review_terms.get(aspect, set())
                overlap = pred_set & rev_set
                results.append({
                    'organism': org, 'gene': gene, 'aspect': aspect,
                    'predicted': len(pred_set), 'reviewed': len(rev_set),
                    'overlap': len(overlap), 'overlap_terms': list(overlap),
                    'pred_only': list(pred_set - rev_set),
                    'rev_only': list(rev_set - pred_set),
                })
            
            # Memory cleanup every gene
            if hasattr(torch.mps, 'empty_cache'):
                torch.mps.empty_cache()
            gc.collect()
            
            if (i + 1) % 10 == 0:
                print(f"  [{i+1}/{len(genes)}] {org}/{gene} done", flush=True)
                # Save intermediate results every 50
                if (i + 1) % 50 == 0:
                    out = REPO / 'reports' / 'gogpt-comparison.json'
                    out.parent.mkdir(exist_ok=True)
                    with open(out, 'w') as f:
                        json.dump(results, f, indent=2)
        
        except GoAspectResolutionError:
            raise
        except Exception as e:
            print(f"  ERROR {org}/{gene}: {e}", flush=True)
            if hasattr(torch.mps, 'empty_cache'):
                torch.mps.empty_cache()
            gc.collect()
    
    out = REPO / 'reports' / 'gogpt-comparison.json'
    out.parent.mkdir(exist_ok=True)
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    
    total_overlap = sum(r['overlap'] for r in results)
    total_pred = sum(r['predicted'] for r in results)
    total_rev = sum(r['reviewed'] for r in results)
    genes_done = len(set((r['organism'], r['gene']) for r in results))
    
    print("\n=== SUMMARY ===")
    print(f"Genes processed: {genes_done}")
    print(f"Total predicted (specific): {total_pred}")
    print(f"Total in reviews: {total_rev}")
    print(f"Exact overlap: {total_overlap}")
    print(f"Overlap rate: {total_overlap*100/max(total_rev,1):.1f}% of review terms predicted")
    print(f"Results saved to {out}")

if __name__ == '__main__':
    main()
