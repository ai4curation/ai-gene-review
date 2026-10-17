# RUBCNL review notes

## Scope

RUBCNL/PACER is reviewed in the PN class III PI3K complex 2/autophagosome maturation branch. PN entries without PMIDs were used as context only. The main curation question is whether RUBCNL should be represented only by autophagosome maturation/fusion process terms, or also by a more specific adaptor/PI3KC3-C2-associated complex context.

## Evidence synthesis

RUBCNL is a positive late-autophagy regulator. The discovery abstract reports that Pacer "positively regulates autophagosome maturation", "stimulate[s] Vps34 kinase activity", and "recruits PI3KC3 and HOPS complexes" by "anchoring to the autophagosomal SNARE Stx17" [PMID:28306502, "positively regulates autophagosome maturation"; PMID:28306502, "stimulate Vps34 kinase activity"; PMID:28306502, "recruits PI3KC3 and HOPS complexes"; PMID:28306502, "anchoring to the autophagosomal SNARE Stx17"]. This supports autophagosome maturation, autophagosome-lysosome fusion, autophagosome-endosome fusion, and an adaptor/recruitment interpretation for the generic protein-binding annotations.

The mTORC1/GSK3-TIP60 paper supports regulation of the same late maturation role. Its abstract states that signaling pathways "modulate autophagosome maturation through Pacer", that mTORC1 phosphorylation can "disrupt the association of Pacer with Stx17 and the HOPS complex", and that TIP60-mediated acetylation "facilitates HOPS complex recruitment" and is "required for autophagosome maturation and lipid droplet clearance" [PMID:30704899, "modulate autophagosome maturation through Pacer"; PMID:30704899, "disrupt the association of Pacer with Stx17 and the HOPS complex"; PMID:30704899, "facilitates HOPS complex recruitment"; PMID:30704899, "required for autophagosome maturation and lipid droplet clearance"]. This supports retaining autophagosome maturation as core and treating lipid metabolic process regulation as non-core downstream physiology.

UniProt summarizes the same mechanism: RUBCNL "promotes autophagosome maturation", acts by "facilitating the biogenesis of phosphatidylinositol 3-phosphate", and "promotes the recruitment of PI3K/PI3KC3 and HOPS complexes" [file:human/RUBCNL/RUBCNL-uniprot.txt, "promotes autophagosome maturation"; file:human/RUBCNL/RUBCNL-uniprot.txt, "facilitating the biogenesis of phosphatidylinositol 3-phosphate"; file:human/RUBCNL/RUBCNL-uniprot.txt, "promotes the recruitment of PI3K/PI3KC3 and HOPS complexes"]. It also reports direct interaction with UVRAG and STX17 and autophagosome-membrane localization [file:human/RUBCNL/RUBCNL-uniprot.txt, "Interacts with UVRAG"; file:human/RUBCNL/RUBCNL-uniprot.txt, "Interacts with STX17"; file:human/RUBCNL/RUBCNL-uniprot.txt, "autophagosome membrane"].

The phosphoinositide-binding annotations are supported. UniProt says RUBCNL binds "phosphatidylinositol 3-phosphate", "phosphatidylinositol-4-phosphate", and "phosphatidylinositol-5-phosphate" [file:human/RUBCNL/RUBCNL-uniprot.txt, "phosphatidylinositol 3-phosphate"; file:human/RUBCNL/RUBCNL-uniprot.txt, "phosphatidylinositol-4-phosphate"; file:human/RUBCNL/RUBCNL-uniprot.txt, "phosphatidylinositol-5-phosphate"]. The generic inherited `phosphatidylinositol phosphate binding` row is true but less specific than the IDA-supported lipid-binding terms.

Generic `protein binding` rows are over-annotations. The useful molecular-function interpretation is protein-macromolecule adaptor activity or recruitment activity: RUBCNL links STX17-positive autophagosomes with UVRAG/PI3KC3 and HOPS machinery during late autophagosome maturation.

## Falcon

Falcon deep research was run for RUBCNL on 2026-06-02 but timed out after 600 seconds, and no `RUBCNL-deep-research-falcon.md` report was produced. This review therefore uses the local GOA, UniProt, cached publication files, and the additional notes above.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording framed RUBCNL in the Proteostasis Network context as an autophagosome-maturation adaptor/recruitment factor associated with PI3KC3-C2 and HOPS, not as generic protein binding.

## 2026-10-10 GOA refresh (PTHR45971 family pass)

- GOA now carries five GO:0005515 IPI rows. Policy: protein binding is never MARK_AS_OVER_ANNOTATED.
  - STX17 (P56962; PMID:28306502 and PMID:30704899) and UVRAG (Q9P2Y5; PMID:28306502): MODIFY to
    GO:0030674 protein-macromolecule adaptor activity (STX17 rows also list GO:0019905 syntaxin binding).
    UniProt: "Interacts with UVRAG; the interaction is direct and promotes association with the
    PI3K/PI3KC3 and HOPS complexes" [file:human/RUBCNL/RUBCNL-uniprot.txt].
  - MTOR (P42345) and KAT5 (Q92993) (PMID:30704899): REMOVE. These are kinase/acetyltransferase
    substrate interactions [PMID:30704899, "mTORC1 phosphorylates Pacer at serine157 to disrupt the
    association of Pacer with Stx17 and the HOPS complex"]; there is no informative PACER MF to substitute.
- Added propagation_review to the GO:1901981 IBA MODIFY (PTN002915557 is seeded only by RUBCNL).
- Additional literature not yet reflected in GOA: RH-domain binding to phospho-Ser72 RAB7A and a role in
  Parkin-dependent mitophagy [PMID:38728007, "Pacer knockout reduces Parkin mitophagy with little
  effect on bulk autophagy or Parkin-independent mitophagy"]; negative regulation of RIPK1-dependent
  apoptosis/necroptosis in MSCs [PMID:38873940]. Not added as NEW in this pass (single studies);
  candidate future annotations.
- Correction: the PACER discovery paper is Cheng et al. 2017 Mol Cell (PMID:28306502), not Nat Cell Biol.
- The PI3P-binding region of PACER is not established from accessible text; the RH domain's verified
  ligand is phospho-RAB7A.
