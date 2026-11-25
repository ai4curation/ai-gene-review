"""Bounded consistency corrections after the initial frozen family release."""

import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PARENT = HERE.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if (HERE / "changes.json").exists():
        raise RuntimeError("Correction already applied")
    frozen = json.loads((PARENT / "handoff.json").read_text())
    for path, h in frozen["files"].items():
        assert sha(ROOT / path) == h, path
    changes = []
    for family in ["PTHR43023", "PTHR30188", "PTHR33371"]:
        path = ROOT / f"interpro/panther/{family}/{family}-review.yaml"
        before = yaml.safe_load(path.read_text())
        document = yaml.safe_load(path.read_text())
        old_hash = sha(path)
        if family == "PTHR43023":
            term = next(
                t
                for t in document["term_assessments"]
                if t["assessed_term"]["id"] == "GO:0043190"
            )
            term["scope_reason"] = (
                "The conserved ABC nucleotide-binding architecture supports participation in an ABC transporter complex. Characterized members work with MlaE, YrbE or TGD1 partners, but those specific permeases and MCE-associated architecture are not asserted for every additional or source-disputed ABC member. Exact partners and cargo require member-specific evidence; the substrate-neutral ABC-complex term does not license a complete Mla system."
            )
            sub = next(
                s for s in document["subfamilies"] if s["subfamily_id"].endswith(":SF6")
            )
            sub["description"] = (
                "SF6 includes enterobacterial MlaF, the Pseudomonas and Bordetella targets, mycobacterial Mkl/MceG and actinobacterial relatives such as SCO2422. Thus it combines characterized Mla phospholipid transport ATPases with a shared ATPase of fatty-acid/cholesterol uptake systems. This verifies classification while leaving universal cargo, secondary activities and compatible Mla partners unresolved; no substrate-loss exception is inferred solely from another positive role."
            )
        elif family == "PTHR30188":
            document["coherence_reason"] = (
                "The shared membrane-permease architecture supports comparison among bacterial MlaE, mycobacterial YrbE and plant TGD1. Positive fatty-acid/cholesterol uptake by YrbE does not establish phospholipid-negative chemistry. Plant chloroplast localization is independently supported and its original plasma-membrane IRD remains intact. SF4 mixes these roles, SF13 contains YrbE partners and SF14 includes Brassica proteins, so substrate and compartment judgments cannot be reduced to an exclusive subfamily list."
            )
            sub = next(
                s
                for s in document["subfamilies"]
                if s["subfamily_id"].endswith(":SF13")
            )
            sub["divergence_description"] = (
                "These are the permease partners of mycobacterial Mce uptake systems, with positive fatty-acid/cholesterol routes and corresponding partners rather than independently demonstrated Mla phospholipid cycling. That contextual difference prevents using them as verified Mla realizers; it does not demonstrate absence of secondary phospholipid transport or justify a substrate-loss node. SF4 contains the paired YrbE proteins alongside MlaE and TGD1."
            )
            term = next(
                t
                for t in document["term_assessments"]
                if t["assessed_term"]["id"] == "GO:0006869"
            )
            term["scope_reason"] = (
                "The substrate-neutral process is consistent with positively characterized Mla phospholipid handling, mycobacterial fatty-acid/cholesterol uptake and plant TGD lipid import, together with conserved permease architecture. It retains those positive lipid roles without requiring a negative phospholipid assertion or licensing exact cargo/partners for every member."
            )
        else:
            document["coherence_reason"] = (
                "The shared MCE architecture links MlaD phospholipid-binding rings with differentiated mycobacterial lipid-import assemblies. SF4 contains both MlaD and Mce1D/Mce2D/Mce3D/Mce4D, while other subfamilies follow operon positions. Positive alternate cargo and extended cell-wall architecture do not show loss of all phospholipid activity or erase membrane anchoring. The separate inherited host-entry node judgment is retained outside this bounded Mla-role audit; no new host-entry exclusion is inferred here."
            )
            for sub in document["subfamilies"]:
                if not sub["subfamily_id"].endswith(":SF4"):
                    sub["divergence_description"] = (
                        "This mycobacterial operon-position group belongs to differentiated Mce lipid-import assemblies rather than an independently demonstrated complete Mla panel. Fatty-acid/cholesterol roles and envelope-spanning architecture support that context distinction; they do not establish a target-negative phospholipid assay or a secondary-function loss. Host-entry participation is a separate question and is not resolved from substrate or operon position alone."
                    )
            term = next(
                t
                for t in document["term_assessments"]
                if t["assessed_term"]["id"] == "GO:0006869"
            )
            term["scope_reason"] = (
                "The substrate-neutral process accommodates positive phospholipid handling in the Mla clade and fatty-acid/cholesterol uptake in characterized mycobacterial Mce systems. It preserves these positive lipid roles without requiring a phospholipid-negative judgment or defining a pruning boundary."
            )
        path.write_text(
            yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=100)
        )
        changes.append(
            {
                "path": str(path.relative_to(ROOT)),
                "before_sha256": old_hash,
                "after_sha256": sha(path),
                "before": before,
                "after": document,
            }
        )
    (HERE / "changes.json").write_text(json.dumps(changes, indent=2) + "\n")
    (HERE / "prior-release.json").write_text(
        json.dumps(
            {
                "path": str((PARENT / "handoff.json").relative_to(ROOT)),
                "sha256": sha(PARENT / "handoff.json"),
            },
            indent=2,
        )
        + "\n"
    )
    print(
        "Corrected three family prose documents; all enums, PAINT and evidence unchanged"
    )


if __name__ == "__main__":
    main()
