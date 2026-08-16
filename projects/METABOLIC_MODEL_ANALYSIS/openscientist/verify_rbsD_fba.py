#!/usr/bin/env python3
"""Independent replication of the OpenScientist rbsD / iML1515 COBRApy run.

The OpenScientist report (rbsD-fba-openscientist.md) states growth rates but its
executed-code artifacts were not returned with the job, so nothing in that report
is locally checkable. This script re-runs the same experiment from scratch so the
numbers can be confirmed or refuted.

Run with a throwaway environment (cobra is deliberately not a repo dependency):

    uv venv /tmp/cobra-venv
    uv pip install --python /tmp/cobra-venv/bin/python cobra
    /tmp/cobra-venv/bin/python projects/METABOLIC_MODEL_ANALYSIS/openscientist/verify_rbsD_fba.py
"""

from __future__ import annotations

import hashlib
import json
import urllib.request
from pathlib import Path

import cobra
from cobra import Metabolite, Reaction

MODEL_URL = "http://bigg.ucsd.edu/static/models/iML1515.json"
CACHE = Path("/tmp/iML1515.json")

INORGANIC_OPEN = None  # keep the model's distributed default medium for inorganics


def fetch_model() -> Path:
    if not CACHE.exists():
        urllib.request.urlretrieve(MODEL_URL, CACHE)
    raw = CACHE.read_bytes()
    print(f"model bytes : {len(raw)}")
    print(f"md5         : {hashlib.md5(raw).hexdigest()}")
    print(f"sha256      : {hashlib.sha256(raw).hexdigest()}")
    return CACHE


def set_medium(model: cobra.Model, carbon: str) -> None:
    """Open exactly one carbon exchange at lb=-10; close the other two."""
    for ex in ("EX_glc__D_e", "EX_rib__D_e"):
        model.reactions.get_by_id(ex).lower_bound = 0.0
    if carbon is not None:
        model.reactions.get_by_id(carbon).lower_bound = -10.0


def growth(model: cobra.Model) -> float:
    sol = model.optimize()
    return 0.0 if sol.status != "optimal" else float(sol.objective_value)


def ko_growth(model: cobra.Model, gene: str) -> float:
    with model:
        model.genes.get_by_id(gene).knock_out()
        return growth(model)


def reannotate(model: cobra.Model) -> cobra.Model:
    """rbsD as D-ribose pyranase (EC 5.4.99.62) obligatorily upstream of ribokinase."""
    m = model.copy()

    furan = Metabolite("rib__D_furan_c", formula="C5H10O5",
                       name="beta-D-ribofuranose", compartment="c")
    pyranase = Reaction("RBSD_pyranase", name="D-ribose pyranase (EC 5.4.99.62)",
                        lower_bound=-1000.0, upper_bound=1000.0)
    pyranase.add_metabolites({m.metabolites.get_by_id("rib__D_c"): -1.0, furan: 1.0})
    m.add_reactions([pyranase])
    pyranase.gene_reaction_rule = "b3748"

    # ribokinase now consumes the furanose anomer only
    rbk = m.reactions.get_by_id("RBK")
    rbk.add_metabolites({m.metabolites.get_by_id("rib__D_c"): 1.0, furan: -1.0})

    # rbsD is not a transporter subunit
    ribabc = m.reactions.get_by_id("RIBabcpp")
    ribabc.gene_reaction_rule = ribabc.gene_reaction_rule.replace(
        "(b3750 and b3751 and b3749 and b3748)", "(b3750 and b3751 and b3749)")
    return m


def main() -> None:
    path = fetch_model()
    model = cobra.io.load_json_model(str(path))
    print(f"cobra       : {cobra.__version__}")
    print(f"solver      : {model.solver.interface.__name__}")
    print(f"model       : {len(model.reactions)} rxns, "
          f"{len(model.metabolites)} mets, {len(model.genes)} genes\n")

    print("b3748 GPRs (published):")
    for rxn in model.genes.get_by_id("b3748").reactions:
        print(f"  {rxn.id}: {rxn.gene_reaction_rule}")
    print(f"RBK: {model.reactions.get_by_id('RBK').reaction} "
          f"| GPR {model.reactions.get_by_id('RBK').gene_reaction_rule}\n")

    with model:
        set_medium(model, "EX_glc__D_e")
        print(f"glucose baseline WT      : {growth(model):.6f}")

    with model:
        set_medium(model, None)
        print(f"no-carbon control        : {growth(model):.6f}")

    with model:
        set_medium(model, "EX_rib__D_e")
        wt_pub = growth(model)
        ko_pub = ko_growth(model, "b3748")
        print(f"(a) published  WT        : {wt_pub:.6f}")
        print(f"(a) published  b3748 KO  : {ko_pub:.6f}   KO/WT = {ko_pub / wt_pub:.3f}")

    m2 = reannotate(model)
    print(f"\nreannotated RBK          : {m2.reactions.get_by_id('RBK').reaction}")
    print(f"reannotated RIBabcpp GPR : {m2.reactions.get_by_id('RIBabcpp').gene_reaction_rule}")
    with m2:
        set_medium(m2, "EX_rib__D_e")
        wt_re = growth(m2)
        ko_re = ko_growth(m2, "b3748")
        print(f"(b) reannotated WT       : {wt_re:.6f}")
        print(f"(b) reannotated b3748 KO : {ko_re:.6f}   KO/WT = {ko_re / wt_re:.3f}")

    # ALT 1 from the report: pyranase present but ribokinase still accepts rib__D_c
    m3 = reannotate(model)
    rbk = m3.reactions.get_by_id("RBK")
    rbk.add_metabolites({m3.metabolites.get_by_id("rib__D_c"): -1.0,
                         m3.metabolites.get_by_id("rib__D_furan_c"): 1.0})
    with m3:
        set_medium(m3, "EX_rib__D_e")
        wt_a1 = growth(m3)
        ko_a1 = ko_growth(m3, "b3748")
        print(f"ALT1 (RBK anomer-agnostic) WT/KO : {wt_a1:.6f} / {ko_a1:.6f} "
              f"  KO/WT = {ko_a1 / wt_a1:.3f}")


if __name__ == "__main__":
    main()
