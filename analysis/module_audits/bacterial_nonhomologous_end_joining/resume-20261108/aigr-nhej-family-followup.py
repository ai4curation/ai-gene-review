from pathlib import Path
import yaml

p = Path("interpro/panther/PTHR42705/PTHR42705-review.yaml")
d = yaml.safe_load(p.read_text())
for a in d["term_assessments"]:
    if a["assessed_term"]["id"] == "GO:0003887":
        a["scope"] = "UNRESOLVED"
        a.pop("applicable_subfamilies", None)
        a["scope_reason"] = (
            "DNA polymerization is positively supported in the named bacterial SF2 POL/LIG proteins across three phyla. The sampled SF2 also contains nonbacterial members whose domain architecture was not assessed, so the evidence does not yet justify a machine-level grant to every SF2 member. This is incomplete scope justification, not a demonstrated counterexample or loss. The module uses independently supported, POL-qualified exemplars; its qualifier does not retroactively narrow a family-wide or subfamily-wide grant."
        )
reasons = {
    "GO:0003887": "PTN001627042 spans both the fused-LigD SF2 exemplars and the ATP-dependent-ligase SF3 clade in the inspected tree. Polymerase activity is established in the named SF2 proteins. SF3 POL architecture has not been independently adjudicated, so the full descendant scope is unresolved; a classification label alone is insufficient to manufacture a negative assertion or loss node.",
    "GO:0006269": "The H37Rv seed has measured DNA-dependent synthesis of unprimed oligoribonucleotides. GO includes damage-repair priming; neither a single experimental seed nor the repair role makes the assertion suspect. The broader tree also spans SF3 ligases and nonbacterial leaves whose primase architecture/capacity has not been independently assessed. This unresolved whole-node scope does not contradict inherited capacity in the supported SF2 targets, and native physiological use remains distinct from biochemical capacity.",
    "GO:0006303": "The mycobacterial seed and other characterized bacterial SF2 proteins participate in Ku-associated end joining. The broad node also spans SF3 ligases and nonbacterial leaves for which cognate repair-partner and pathway participation evidence was not inspected. Lack of a POL domain, if established, would not itself exclude NHEJ participation through ligation. Whole-node process scope therefore remains unresolved without asserting that those descendants lack NHEJ or that the curator chose a wrong node.",
}
for n in d["node_assessments"]:
    if n["asserted_term"]["id"] in reasons:
        n["assessment_reason"] = reasons[n["asserted_term"]["id"]]
    if n["asserted_term"]["id"] == "GO:0006303":
        n["supported_by"] = [
            {
                "reference_id": "PMID:16023671",
                "supporting_text": "A prokaryotic non-homologous end-joining (NHEJ) system for the repair of DNA double-strand breaks (DSBs), composed of a Ku homodimer (Mt-Ku) and a multidomain multifunctional ATP-dependent DNA ligase (Mt-Lig)",
            }
        ]
d["notes"] += (
    " These reconstructed scope distinctions are based on the retained tree exports and primary evidence. No universal processing grant follows from the positive exemplar panel."
)
p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
p = Path("modules/bacterial_nonhomologous_end_joining.yaml")
s = p.read_text()
replacements = {
    "The2026": "The 2026",
    "the2026": "the 2026",
    "Strain168": "Strain 168",
    "the3-primehydroxyl": "the 3-prime hydroxyl",
    "2026CDC1551LigD": "2026 CDC1551 LigD",
    "truncatedBacillusKu": "truncated Bacillus Ku",
    "nativeoccupancy": "native occupancy",
    "nativeKT2440/PA14": "native KT2440/PA14",
    "PAO1biochemistry": "PAO1 biochemistry",
}
for a, b in replacements.items():
    s = s.replace(a, b)
p.write_text(s)
