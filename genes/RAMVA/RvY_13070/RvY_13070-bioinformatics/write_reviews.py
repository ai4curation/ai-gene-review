"""Write reviews for the SOD paralogs based on bioinformatic verdicts.

Verdicts from RESULTS.md:
- LIKELY_FUNCTIONAL: All residues + both PROSITE patterns OK
- IMPAIRED: All residues OK but PROSITE PS00087 fails
- HIGHLY_DEGRADED: Most residues missing, fails PROSITE + Pfam (RvY_01767)
- CHAPERONE: Cu chaperone, not a SOD (RvY_15948)
"""
from pathlib import Path

PARALOG_DATA = {
    # gene: (accession, length, verdict, details)
    "RvY_00650": (
        "A0A1D1UDY8", 292, "IMPAIRED",
        "292 aa with N-terminal extension; all 4 Cu His preserved by sequence but PROSITE PS00087 fails",
    ),
    "RvY_00651": (
        "A0A1D1UKR0", 154, "FUNCTIONAL",
        "154 aa, 66% identity to human SOD1 (highest of paralogs); all PROSITE patterns and residues match",
    ),
    "RvY_01767": (
        "A0A1D1USM4", 230, "HIGHLY_DEGRADED",
        "230 aa, 27% identity to human SOD1; only 2/4 Cu, 0/4 Zn, 0/2 SS preserved; not in Pfam SODC; both PROSITE patterns fail",
    ),
    "RvY_03754": (
        "A0A1D1UP68", 156, "FUNCTIONAL",
        "156 aa, 63% identity to human SOD1; all residues and PROSITE patterns match canonical CuZnSOD",
    ),
    "RvY_03757": (
        "A0A1D1UP59", 193, "IMPAIRED",
        "193 aa (172 mature); all 4 Cu His preserved by sequence but PROSITE PS00087 fails",
    ),
    "RvY_09480": (
        "A0A1D1VEY6", 317, "FUNCTIONAL",
        "317 aa with N-terminal extension; all residues and PROSITE patterns match canonical CuZnSOD",
    ),
    "RvY_10893": (
        "A0A1D1VE88", 185, "FUNCTIONAL",
        "185 aa (166 mature); all residues and PROSITE patterns match canonical CuZnSOD",
    ),
    "RvY_17310": (
        "A0A1D1W3Y1", 475, "IMPAIRED",
        "475 aa (455 mature) - 3x larger than canonical CuZnSOD; SOD domain in C-terminus; all 4 Cu His preserved by sequence but PROSITE PS00087 fails",
    ),
    "RvY_15948": (
        "A0A1D1VWP9", 305, "CHAPERONE",
        "305 aa; UniProt classifies as 'Superoxide dismutase copper/zinc binding domain-containing protein'; H46→A and H48→C substitutions consistent with copper chaperone (CCS) function rather than SOD activity",
    ),
}


DESCRIPTIONS = {
    "FUNCTIONAL": (
        "Putative Cu/Zn superoxide dismutase paralog from R. varieornatus, "
        "one of approximately 10 CuZnSOD-family proteins encoded by this "
        "extremotolerant tardigrade. Bioinformatic analysis "
        "(file:RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md) shows that "
        "all four canonical Cu-binding histidines, all four Zn-binding residues, "
        "and both intrachain disulfide cysteines are preserved at the sequence "
        "level. The protein matches both PROSITE Cu/Zn SOD signatures (PS00087 "
        "for the N-terminal Cu coordination loop and PS00332 for the C-terminal "
        "disulfide region), as well as the Pfam SODC family (PF00080). This is "
        "consistent with canonical Cu/Zn superoxide dismutase activity, although "
        "biochemical confirmation has not been published for this specific "
        "paralog. {details}"
    ),
    "IMPAIRED": (
        "Cu/Zn superoxide dismutase family paralog from R. varieornatus with "
        "evidence of catalytic impairment. Bioinformatic analysis "
        "(file:RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md) shows that "
        "while all four Cu-binding histidines are preserved at the residue level, "
        "the protein FAILS to match PROSITE PS00087 - the N-terminal H-x-H Cu "
        "coordination signature. PS00087 requires not just the catalytic "
        "histidines but also specific flanking residues that maintain the "
        "structural geometry of the Cu site loop. By analogy with the related "
        "paralog RvSOD15 (Sim & Inoue 2023, PMID:37358501), where restoring "
        "a missing histidine via V87H mutagenesis did NOT restore activity due "
        "to a flexible loop with non-canonical context, this paralog likely "
        "has impaired or absent canonical SOD activity despite retaining the "
        "catalytic residues. {details}"
    ),
    "HIGHLY_DEGRADED": (
        "Heavily degraded Cu/Zn superoxide dismutase family paralog from "
        "R. varieornatus. Bioinformatic analysis "
        "(file:RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md) shows this "
        "protein has only 27% identity to human SOD1, retains only 2 of 4 Cu "
        "ligands, 0 of 4 Zn ligands, and 0 of 2 disulfide cysteines. It also "
        "fails BOTH PROSITE Cu/Zn SOD signatures and is NOT a member of the "
        "Pfam SODC family (PF00080). This is most likely either a true "
        "pseudogene (if not expressed) or has undergone radical "
        "neofunctionalization. Standard SOD-related GO annotations are not "
        "appropriate for this protein. {details}"
    ),
    "CHAPERONE": (
        "Copper chaperone for Cu/Zn superoxide dismutase (CCS homolog) from "
        "R. varieornatus, NOT a superoxide dismutase. UniProt already classifies "
        "this protein as 'Superoxide dismutase copper/zinc binding domain-containing "
        "protein.' CCS proteins have a SOD-like fold but lack canonical Cu "
        "ligands because their function is to deliver copper to SOD enzymes "
        "rather than catalyze superoxide dismutation. Bioinformatic analysis "
        "(file:RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md) confirms "
        "that the H46 → A and H48 → C substitutions at the canonical Cu site "
        "are consistent with chaperone function. The protein matches Pfam SODC "
        "but does not match either PROSITE Cu/Zn SOD signature. {details}"
    ),
}


def make_review_yaml(gene: str, accession: str, length: int, verdict: str, details: str) -> str:
    description = DESCRIPTIONS[verdict].format(details=details)

    if verdict == "FUNCTIONAL":
        sod_action = "ACCEPT"
        sod_summary = (
            "All catalytic residues (4 Cu His, 4 Zn ligands, 2 disulfide Cys) "
            "are preserved at the sequence level. PROSITE PS00087 (N-terminal "
            "Cu coordination signature) and PS00332 (C-terminal disulfide "
            "signature) both match. The protein is in Pfam family PF00080 "
            "(Sod_Cu). Canonical SOD activity is plausible based on sequence "
            "and motif analysis, though biochemical data are lacking for this "
            "specific paralog. ACCEPT with the caveat that confidence is "
            "limited to sequence-level inference."
        )
        sod_reason = "All sequence-level criteria for canonical CuZnSOD are met."
        cu_action = "ACCEPT"
        bp_action = "ACCEPT"
    elif verdict == "IMPAIRED":
        sod_action = "MARK_AS_OVER_ANNOTATED"
        sod_summary = (
            "All four Cu-binding histidines are preserved at the residue level, "
            "but PROSITE PS00087 (the N-terminal Cu coordination signature) "
            "FAILS to match. PS00087 requires both the H-x-H motif AND specific "
            "flanking residues that maintain the structural context. This "
            "indicates divergence at the Cu site beyond just the catalytic "
            "residues themselves. By analogy with Sim & Inoue (PMID:37358501), "
            "where the V87H rescue mutant of RvSOD15 failed to restore activity "
            "due to a flexible loop with non-canonical context, this paralog "
            "likely has impaired catalytic function. The IEA annotation from "
            "Pfam family assignment is therefore probably incorrect."
        )
        sod_reason = (
            "PROSITE PS00087 failure indicates the canonical N-terminal Cu "
            "coordination structure is not intact, even though the catalytic "
            "histidines themselves are present. Without biochemical confirmation, "
            "the IEA SOD activity annotation should be marked as over-annotated."
        )
        cu_action = "ACCEPT"  # Cu binding still likely
        bp_action = "MARK_AS_OVER_ANNOTATED"
    elif verdict == "HIGHLY_DEGRADED":
        sod_action = "REMOVE"
        sod_summary = (
            "This protein has only 2 of 4 Cu ligands, 0 of 4 Zn ligands, and "
            "0 of 2 disulfide cysteines preserved. It fails BOTH PROSITE Cu/Zn "
            "SOD signatures and is NOT in the Pfam SODC family (PF00080). Only "
            "27% identity to human SOD1. This is too divergent to retain "
            "canonical SOD activity and the IEA annotation appears to be "
            "based on weak sequence remnants. Annotation should be removed."
        )
        sod_reason = (
            "Catastrophic loss of catalytic residues, both PROSITE patterns "
            "fail, and the protein is not in the Pfam SODC family. There is "
            "no sequence-level support for SOD activity."
        )
        cu_action = "REMOVE"
        bp_action = "REMOVE"
    elif verdict == "CHAPERONE":
        sod_action = "REMOVE"
        sod_summary = (
            "This protein is the copper chaperone for SOD (CCS), NOT a "
            "superoxide dismutase. UniProt already names it 'Superoxide "
            "dismutase copper/zinc binding domain-containing protein.' CCS "
            "proteins have a SOD-like fold (hence the Pfam SODC match) but "
            "function as copper delivery factors, not as enzymes. The H46 → A "
            "and H48 → C substitutions are inconsistent with SOD activity but "
            "consistent with copper coordination for transfer. The annotation "
            "should be SOD copper chaperone activity (GO:0016531), not SOD."
        )
        sod_reason = (
            "The protein is a copper chaperone, not a SOD. UniProt's own "
            "naming reflects this. Canonical Cu binding histidines are absent."
        )
        cu_action = "MODIFY"  # Replace with chaperone activity
        bp_action = "REMOVE"

    yaml = f"""id: {accession}
gene_symbol: {gene}
product_type: PROTEIN
status: IN_PROGRESS
taxon:
  id: NCBITaxon:947166
  label: Ramazzottius varieornatus
description: >-
  {description}
existing_annotations:
- term:
    id: GO:0004784
    label: superoxide dismutase activity
  evidence_type: IEA
  original_reference_id: GO_REF:0000120
  review:
    summary: >-
      {sod_summary}
    action: {sod_action}
    reason: >-
      {sod_reason}
    supported_by:
      - reference_id: file:RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md
        supporting_text: >-
          {gene} | {accession} | bioinformatic verdict: {verdict}
- term:
    id: GO:0005507
    label: copper ion binding
  evidence_type: IEA
  original_reference_id: GO_REF:0000002
  review:
    summary: >-
      {"All four canonical Cu-binding histidines are preserved at the sequence level. Copper binding is likely." if cu_action == "ACCEPT" else "Cu binding residues are not preserved in their canonical positions."}
    action: {cu_action}
"""
    if cu_action == "MODIFY":
        yaml += """    proposed_replacement_terms:
      - id: GO:0016531
        label: copper chaperone activity
"""
    yaml += f"""- term:
    id: GO:0006801
    label: superoxide metabolic process
  evidence_type: IEA
  original_reference_id: GO_REF:0000002
  review:
    summary: >-
      {"Inferred from SOD activity. Same caveats as the MF annotation." if bp_action == "MARK_AS_OVER_ANNOTATED" else "Inferred from SOD activity annotation." if bp_action == "ACCEPT" else "Not applicable - this protein is not a functional SOD."}
    action: {bp_action}
- term:
    id: GO:0019430
    label: removal of superoxide radicals
  evidence_type: IEA
  original_reference_id: GO_REF:0000108
  review:
    summary: >-
      {"Inferred from SOD activity. Same caveats as the MF annotation." if bp_action == "MARK_AS_OVER_ANNOTATED" else "Inferred from SOD activity annotation." if bp_action == "ACCEPT" else "Not applicable - this protein is not a functional SOD."}
    action: {bp_action}
- term:
    id: GO:0046872
    label: metal ion binding
  evidence_type: IEA
  original_reference_id: GO_REF:0000002
  review:
    summary: >-
      Parent term of the more specific Cu/Zn binding annotations. {"Both Cu and Zn binding are likely." if cu_action != "REMOVE" else "Metal binding may still occur but cannot be assumed."}
    action: KEEP_AS_NON_CORE
references:
- id: GO_REF:0000002
  title: Gene Ontology annotation through association of InterPro records with GO
    terms
  findings: []
- id: GO_REF:0000108
  title: Automatic assignment of GO terms using logical inference, based on on inter-ontology
    links
  findings: []
- id: GO_REF:0000120
  title: Combined Automated Annotation using Multiple IEA Methods
  findings: []
- id: file:RAMVA/RvY_13070/RvY_13070-bioinformatics/RESULTS.md
  title: Bioinformatics analysis of Cu/Zn SOD paralogs in R. varieornatus
  findings:
  - statement: "Bioinformatic verdict for {gene}: {verdict}. {details}"
"""
    return yaml


def main():
    base = Path("/Users/cjm/repos/ai-gene-review/genes/RAMVA")
    for gene, (acc, length, verdict, details) in PARALOG_DATA.items():
        if gene == "RvY_00651":
            # Already manually written
            continue
        out = base / gene / f"{gene}-ai-review.yaml"
        yaml = make_review_yaml(gene, acc, length, verdict, details)
        out.write_text(yaml)
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
