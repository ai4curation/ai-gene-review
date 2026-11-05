"""Exhaustive exact-product coverage checks for six native regeneration chains.

A present product denotes an expressed, functional capability under the module's
chemical conditions. This is not a prediction of growth, stress survival, native
pathway predominance, or the absence of unmodeled alternative donors.
"""

import itertools
import json
from pathlib import Path

import yaml

from ai_gene_review.module_logic import compile_module, is_satisfied

ROOT = Path(__file__).resolve().parents[2]
SLUG = "bacterial_alkyl_hydroperoxide_reductase"
doc = yaml.safe_load((ROOT / "modules" / f"{SLUG}.yaml").read_text())
variants = doc["module"]["variant_sets"][0]["variants"]
EXPECTED = {
    "ecoli_ahpc_ahpf": {"P0AE08", "P35340"},
    "salty_ahpc_ahpf": {"P0A251", "P19480"},
    "bacsu_ahpc_ahpf": {"P80239", "P42974"},
    "helpy_thioredoxin_ahpc": {"P21762", "P66928", "P56431"},
    "myctu_thioredoxin_ahpc": {"P9WQB7", "P9WG67", "P9WHH1"},
    "myctu_lipoyl_ahpc": {"P9WQB7", "P9WQB5", "P9WIS7", "P9WHH9"},
}
assert len(variants) == len(EXPECTED)
requirements = {}
for variant in variants:
    members = set()
    for annoton in variant["annotons"]:
        participant = annoton["participant"]
        assert participant["selector_type"] == "GENE_PRODUCT"
        accession = participant["gene_product"]["term"]["id"].removeprefix("UniProtKB:")
        requirements[annoton["id"]] = accession
        members.add(accession)
    assert members == EXPECTED[variant["id"]], variant["id"]

circuit = compile_module(doc)
all_accessions = sorted(set.union(*EXPECTED.values()))
assert len(all_accessions) == 15
cases = 0
positive = 0
for size in range(len(all_accessions) + 1):
    for combination in itertools.combinations(all_accessions, size):
        present = set(combination)
        expected = any(route <= present for route in EXPECTED.values())
        observed = is_satisfied(circuit, lambda atom: requirements[atom.node_id] in present)
        assert observed == expected, (sorted(present), observed, expected)
        cases += 1
        positive += observed
assert cases == 32768
print(json.dumps({"cases": cases, "passed": cases, "satisfying_sets": positive,
                  "native_routes": {k: sorted(v) for k, v in EXPECTED.items()},
                  "limits": __doc__}, indent=2))
