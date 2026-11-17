"""Apply bounded, reviewed evidence/prose changes; refuse to overwrite a release."""

import json
import re
from pathlib import Path


A = Path(__file__).resolve().parent
ROOT = A.parents[4]
assert not (A / "handoff.json").exists()
BASE = json.loads((A / "baseline.json").read_text())


def replace_field(path, field, value):
    path = ROOT / path
    text = path.read_text()
    pattern = rf"(?m)^{field}:.*(?:\n[ \t].*)*"
    new, count = re.subn(pattern, field + ": " + value, text, count=1)
    assert count == 1, path
    path.write_text(new)


replace_field(
    "genes/ECOLI/lptM/lptM-ai-review.yaml",
    "description",
    "LptM (formerly YifL) is an Escherichia coli outer-membrane lipoprotein that associates with LptD and LptE. It stabilizes a translocon conformation favorable for LptD disulfide maturation and efficient release from the BAM assembly machinery. In the mature translocon, its lipidated N-terminal region contacts the LptD lateral gate and promotes conformational changes that facilitate LPS access. Its contribution becomes especially important when oxidative folding or Lpt-bridge function is perturbed.",
)
replace_field(
    "genes/ECOLI/yedD/yedD-ai-review.yaml",
    "description",
    "YedD, renamed LptY, is an Escherichia coli outer-membrane lipoprotein associated with the LptDE LPS translocon. It binds and stabilizes the periplasmic beta-taco domain of LptD and its connection to the transenvelope Lpt bridge. LptY and LptM occupy different regions of LptD and can associate independently. LptY supports translocon function especially when LptD oxidative maturation or bridge connectivity is perturbed.",
)
replace_field(
    "genes/NEIMB/lptE/lptE-ai-review.yaml",
    "description",
    "LptE is an outer-membrane lipoprotein that associates with LptD and supports its biogenesis or stability in Neisseria meningitidis. The MC58 protein is identical across its full 159 residues to H44/76 LptE. In H44/76-derived strains, lptE deletion reduces LptD abundance and complementation restores it, while surface LPS transport remains detectable.",
)
path = ROOT / "genes/ECOLI/lptE/lptE-ai-review.yaml"
text = path.read_text()
old = "Whereas LptY binds and stabilizes the periplasmic LptD β-taco domain that\n      functions as LPS receptor, LptM intercalates the lateral gate of the β-barrel domain,\n      promoting its opening and access by LPS."
before, core = text.split("core_functions:", 1)
assert core.count(old) == 1
text = (
    before
    + "core_functions:"
    + core.replace(
        old, "with an internal lumen partially occluded by the lipoprotein LptE"
    )
)
path.write_text(text)
identity_counts = {}
for org, gene in [("NEIMB", "lptE"), ("NEIMB", "lptH")]:
    path = ROOT / f"genes/{org}/{gene}/{gene}-ai-review.yaml"
    text = path.read_text()
    old = "Sequence identity supports protein-role transfer in a matched biological context."
    identity_counts[f"{org}/{gene}"] = text.count(old)
    assert text.count(old) > 0
    path.write_text(
        text.replace(
            old, "All three matches are exact and unique among 2,423 translated CDSs."
        )
    )
path = ROOT / "genes/NEIMH/lptD/lptD-ai-review.yaml"
text = path.read_text()
old = "supporting_text: Thus, Imp functions in LPS transport to the outer leaflet of the OM."
assert old in text
text = text.replace(
    old,
    "supporting_text: Imp itself is an OMP, as shown by its presence in purified Neisserial (this study) and E. coli ( 6 ) OMs",
    1,
)
path.write_text(text)
for org, gene in BASE["genes"]:
    path = ROOT / f"genes/{org}/{gene}/{gene}-notes.md"
    text = path.read_text()
    if org == "PSEPK":
        old = f".cache/module-audit-logs/lps-20261107/psepk-consultation/falcon-{gene}.log"
        new = f"analysis/module_audits/bacterial_lps_transport/psepk-consultation/provider-attempts/falcon-{gene}.log"
        assert old in text and (ROOT / new).exists()
        text = text.replace(old, new)
        note = "Corrected the historical Falcon failure pointer to the already committed durable provider-attempt log. The failed attempt and all annotation decisions remain unchanged."
    elif org == "ECOLI" and gene == "lptE":
        note = "Replaced an off-target LptM/LptY quote on the LptE core with PMID41285762’s explicit LptE luminal-occlusion clause. Existing independent LPS-binding and native transport support remains. No annotation action or core functional assertion changed."
    elif org == "NEIMH":
        note = "The outer-membrane ACCEPT now quotes PMID15192148’s explicit observation of Imp in purified Neisserial outer membranes, rather than its transport conclusion. Its membrane-separation difficulties concern tracking LPS through fractions; the authors still explicitly report Imp in purified OMs. No action changed."
    elif org == "NEIMB":
        note = (
            "Replaced methodological identity boilerplate with the reproducible exact-and-unique CDS-match finding. The 159-residue LptE/role-specific identity bridge transfers protein identity, not the native strain of the experiment. H44/76 assays remain distinct from MC58 inference. The LptE summary now states positive biology; accessory/non-obligatory scope remains in the review reasons."
            if gene == "lptE"
            else "Replaced methodological identity boilerplate with the reproducible exact-and-unique CDS-match finding. This supports the strain bridge, not an independent MC58 experiment; the native H44/76 evidence and assay limitations remain unchanged."
        )
    else:
        note = "Recast the description as positive mechanistic biology. The review reasons retain the bounds on autonomous activity and lineage-wide essentiality; no catalytic activity, universal requirement or annotation action was added."
    path.write_text(text + "\n\n## PR6190 evidence/prose follow-up\n\n" + note + "\n")
replace_field(
    "interpro/panther/PTHR33529/PTHR33529-review.yaml",
    "summary",
    "LptF and LptG are paralogous membrane subunits of LptB2FG lipid-extraction assemblies. In characterized LPS transporters, each supplies six transmembrane helices and a periplasmic beta-jellyroll domain. Their membrane domains form a cavity that accepts LPS laterally, while ATP hydrolysis by the cytoplasmic LptB dimer drives extraction toward the LptC/LptA bridge. The two paralogs contribute distinct parts of this machinery. Escherichia coli LptF and LptG were formerly YjgP and YjgQ; the PANTHER family retains the Slr0882 designation.",
)
replace_field(
    "interpro/panther/PTHR30189/PTHR30189-review.yaml",
    "summary",
    "LptD (Imp/OstA) forms the outer-membrane insertion component of characterized LPS transport systems. Its N-terminal periplasmic beta-jellyroll domain receives the LptA bridge, and its C-terminal 26-stranded beta-barrel provides a lateral exit into the outer leaflet. In Escherichia coli, the lipoprotein LptE occupies part of the barrel lumen and supports translocon assembly and LPS insertion. Meningococcal LptD also supports surface LPS delivery, with LptE promoting LptD abundance and biogenesis under the tested conditions.",
)
family_path = ROOT / "interpro/panther/PTHR45772/PTHR45772-review.yaml"
text = family_path.read_text()
old = BASE["documents"][str(family_path.relative_to(ROOT))]["term_assessments"][0][
    "scope_reason"
]
new = "Positive LPS-export motors P0A9V1 and Q88P99 lie in SF10. The actual amino-acid IBD node PTN000656921 contains only SF7/SF11 and excludes SF10; that topological boundary is retained, but it is not a positive LPS grant to every remaining SF10 member. SF10 also includes Q9X0E4 and Q9RSJ0 in non-LPS-producing contexts, plus A0A1Y1IFB9 and B9TJQ6 with unresolved cargo/provenance. Their uncertainty cannot be represented as negative member_exceptions, whose schema meaning is that the term does not hold. SUBFAMILY_ONLY would affirm the term is safe throughout SF10 except explicitly justified negatives; the available evidence does not establish that universal positive scope. Keep UNRESOLVED, preserve the named positive motors and actual between-clade boundary, and require source-qualified LptB chemistry, LPS/LOS context and compatible partners. No ancestral loss or universal secondary-activity exclusion is inferred."
pattern = r"(?m)^  scope_reason: The reviewed E\. coli.*(?:\n    .*)*"
text, count = re.subn(pattern, "  scope_reason: " + new, text, count=1)
assert count == 1
family_path.write_text(text)
(A / "identity-replacements.json").write_text(
    json.dumps(identity_counts, indent=2) + "\n"
)
# A live bounded assessment ledger records useful topology without a false scope grant.
snapshot = json.loads(
    (
        ROOT
        / "analysis/module_audits/bacterial_lps_transport/family-consultation/tree-snapshot.json"
    ).read_text()
)["PTHR45772"]
inside = snapshot["under"]["PTN000656921"]
assert {snapshot["leaves"][node]["subfamily"] for node in inside} == {
    "PTHR45772:SF7",
    "PTHR45772:SF11",
}
sf10 = {
    node: row
    for node, row in snapshot["leaves"].items()
    if row["subfamily"] == "PTHR45772:SF10"
}
(A / "scope-boundaries.json").write_text(
    json.dumps(
        {
            "term": "GO:0015920",
            "current_scope": "UNRESOLVED",
            "positive_members": ["P0A9V1", "Q88P99"],
            "positive_member_basis": "Characterized E. coli LptB and curated matched KT2440 motor; no universal cargo inference.",
            "amino_acid_node": {
                "id": "PANTHER:PTN000656921",
                "leaf_ids": inside,
                "subfamilies": ["PTHR45772:SF7", "PTHR45772:SF11"],
                "excludes_sf10": True,
                "judgment": "Verified topological separation, not a new negative LPS assay or ancestral loss.",
            },
            "sf10_leaves": sf10,
            "unadjudicated_cargo_or_provenance": [
                "Q9X0E4",
                "Q9RSJ0",
                "A0A1Y1IFB9",
                "B9TJQ6",
            ],
            "member_exception_decision": "Do not encode uncertainty as the negative assertion that GO0015920 does not hold.",
        },
        indent=2,
    )
    + "\n"
)
