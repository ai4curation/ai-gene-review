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
