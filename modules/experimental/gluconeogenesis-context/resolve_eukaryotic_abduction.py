#!/usr/bin/env python
"""Eukaryotic abduction: pathway known active in a tissue vs its GTEx expression.

The microbial abduction asks "genome encodes the steps?" against a growth phenotype.
The eukaryotic version asks "tissue expresses the steps?" against an independently
documented tissue function. The same abduce() primitive yields the same four outcomes,
but the eukaryotic gaps carry an extra meaning microbes lack: a pathway can be split
across organs/cell types, so a per-tissue gap may reflect non-cell-autonomy rather than
a missing enzyme.

Two scenarios, both with documented, oracle-independent activity assertions:

* Ketolysis: heart/brain/muscle/kidney oxidise ketone bodies; the liver does not.
  The engine should confirm the four and, for liver, return CONSISTENT_INACTIVE with the
  gap at OXCT1/SCOT -- the textbook molecular reason the liver exports ketones.
* Gluconeogenesis at a stringent expression bar: liver and kidney are unambiguous;
  intestinal gluconeogenesis is reported but debated, and its terminal G6PC1 sits at a
  low ~3 TPM, so at a strict threshold it surfaces as an ABDUCTION_TARGET -- exactly the
  open question in the field.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ai_gene_review.module_logic import compile_module_file, abduce, unsatisfied_steps, iter_atoms, step_id
from gtex_oracle import load_cache

MODULES = Path(__file__).parents[2]


@dataclass
class Scenario:
    name: str
    module: Path
    threshold: float
    # tissue -> (asserted_active, basis)
    assertions: dict


SCENARIOS = [
    Scenario(
        name="Ketone-body oxidation (ketolysis)",
        module=MODULES / "ketone_body_oxidation.yaml",
        threshold=1.0,
        assertions={
            "Heart_Left_Ventricle": (True, "myocardium oxidises ketone bodies as a major fuel"),
            "Brain_Cortex": (True, "brain shifts to ketone-body oxidation during prolonged fasting"),
            "Muscle_Skeletal": (True, "skeletal muscle oxidises ketone bodies"),
            "Kidney_Cortex": (True, "renal cortex oxidises ketone bodies"),
            "Liver": (False, "liver produces but does not oxidise ketone bodies (lacks SCOT/OXCT1)"),
        },
    ),
    Scenario(
        name="Gluconeogenesis at a stringent expression bar (TPM>=5)",
        module=MODULES / "gluconeogenesis_human.yaml",
        threshold=5.0,
        assertions={
            "Liver": (True, "principal gluconeogenic organ"),
            "Kidney_Cortex": (True, "renal cortex performs gluconeogenesis"),
            "Small_Intestine_Terminal_Ileum": (True, "intestinal gluconeogenesis reported (debated)"),
        },
    ),
]


def run(scenario: Scenario) -> list[tuple]:
    circuit = compile_module_file(scenario.module)
    _, matrix = load_cache()
    rows = []
    for tissue, (active, basis) in scenario.assertions.items():
        def holds(atom, _t=tissue):
            s = atom.gene_symbol
            return bool(s) and matrix.get(s, {}).get(_t, 0.0) >= scenario.threshold

        ab = abduce(circuit, holds, asserted_active=active)
        # name the specific unexpressed atoms inside each gap step (precision)
        missing_atoms = {}
        for s in unsatisfied_steps(circuit, holds):
            missing_atoms[step_id(s)] = sorted(
                a.gene_symbol for a in iter_atoms(s) if a.gene_symbol and not holds(a))
        rows.append((tissue, basis, ab, missing_atoms))
    return rows


def format_report() -> str:
    lines = []
    for sc in SCENARIOS:
        lines.append(f"################ {sc.name}  (threshold TPM>={sc.threshold}) ################")
        for tissue, basis, ab, missing in run(sc):
            lines.append(f"  [{ab.classification}] {tissue}")
            lines.append(f"      asserted active={ab.asserted_active}  ({basis})")
            lines.append(f"      engine satisfiable={ab.satisfiable}  gaps={ab.gap_steps}")
            if ab.classification == "ABDUCTION_TARGET":
                for step, miss in missing.items():
                    lines.append(f"      LEAD @ '{step}': tissue asserted active but {miss} not expressed ->")
                    for h in ab.hypotheses:
                        lines.append(f"          - {h}")
            elif ab.classification == "CONSISTENT_INACTIVE":
                for step, miss in missing.items():
                    lines.append(f"      predicted-absent because {miss} not expressed at '{step}' "
                                 f"(consistent with the known phenotype)")
        lines.append("")
    lines.append("== Reading ==")
    lines.append("  Liver ketolysis -> CONSISTENT_INACTIVE at OXCT1: the engine reproduces the textbook")
    lines.append("  reason the liver cannot consume the ketone bodies it makes (no SCOT).")
    lines.append("  Intestinal gluconeogenesis -> ABDUCTION_TARGET at the terminal G6PC1 step: a real,")
    lines.append("  literature-debated lead (low intestinal glucose-6-phosphatase), not a settled call.")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(format_report())
