# CDC37L1 (Hsp90 co-chaperone Cdc37-like 1, "Harc") review notes

UniProt: Q7L3B6 (CD37L_HUMAN). Gene symbol CDC37L1; synonyms CDC37B, HARC (Hsp90-Associating Relative of Cdc37). 337 aa. HGNC:17179. Chromosome 9.

## Identity and family
- RecName: "Hsp90 co-chaperone Cdc37-like 1"; AltName "Hsp90-associating relative of Cdc37" [file:human/CDC37L1/CDC37L1-uniprot.txt].
- Belongs to the CDC37 family (UniProt SIMILARITY; SUPFAM SSF101391 "Hsp90 co-chaperone CDC37"; Pfam PF08565 CDC37_M; InterPro IPR004918 Cdc37, IPR013874 Cdc37_Hsp90-bd; PANTHER PTHR12800:SF2 "HSP90 CO-CHAPERONE CDC37-LIKE 1") [file:human/CDC37L1/CDC37L1-uniprot.txt].
- Paralog of CDC37, the canonical kinase-specific Hsp90 co-chaperone.

## Function (UniProt)
- FUNCTION: "Co-chaperone that binds to numerous proteins and promotes their interaction with Hsp70 and Hsp90." (ECO:0000250, by similarity) [file:human/CDC37L1/CDC37L1-uniprot.txt].
- SUBUNIT: "Self-associates. Forms complexes with Hsp70 and Hsp90. Interacts with CDC37, FKBP4, PPID and STIP1." (ECO:0000269|PubMed:11413142, PubMed:15850399, PubMed:18052042) [file:human/CDC37L1/CDC37L1-uniprot.txt].
- INTERACTION (IntAct): binds HSP90AA1 (P07900), HSP90AB1 (P08238, Q6PK50), STIP1 (P31948), BRK1 (Q8WUW1) [file:human/CDC37L1/CDC37L1-uniprot.txt].

## Primary literature (in UniProt, not cached locally)
- PMID:11413142 (Scholz et al., 2001, J Biol Chem): original identification/characterization of Harc; interaction with FKBP4, HSP70, HSP90, PPID and STIP1; subcellular location (cytoplasm); tissue specificity; phosphorylation. Defines Harc as a novel Hsp90-associating relative of Cdc37.
- PMID:15850399 (Roiniotis et al., 2005, Biochemistry): "Domain-mediated dimerization of the Hsp90 cochaperones Harc and Cdc37." Self-association and interaction with CDC37 and HSP90.
- PMID:18052042 (Cartledge et al., 2007, Biochemistry): C-terminal domain of Harc required for binding HSP70 and Hop (STIP1) and response to heat shock.

## Domain architecture (UniProt feature table) [file:human/CDC37L1/CDC37L1-uniprot.txt]
- REGION 2..171 Self-association.
- REGION 147..277 Self-association and interaction with Hsp90.
- REGION 267..337 Interaction with Hsp70.
- REGION 278..337 Required for interaction with STIP1 (Hop).
- COILED 84..122.
- Phosphoserine at S32 (PMID:18669648, PMID:19690332) and S88 (PMID:23186163) — large-scale phosphoproteomics; mitotic / TCR signaling contexts.

## Subcellular location and tissue
- Cytoplasm (PubMed:11413142); IDA cytosol (HPA, GO_REF:0000052) [file:human/CDC37L1/CDC37L1-goa.tsv].
- Tissue: brain, heart, kidney, liver, placenta, skeletal muscle (PubMed:11413142); HPA "Tissue enhanced (skeletal)".

## GOA annotations reviewed [file:human/CDC37L1/CDC37L1-goa.tsv]
- IBA (GO_REF:0000033, PANTHER PTN000980613): cytoplasm GO:0005737; protein folding GO:0006457; heat shock protein binding GO:0031072; protein stabilization GO:0050821; protein-folding chaperone binding GO:0051087. (UniProt DR also lists IBA GO:0051082 unfolded protein binding, but this is not in the GOA TSV.)
- IEA cytoplasm GO:0005737 (GO_REF:0000120).
- IDA cytosol GO:0005829 (HPA, GO_REF:0000052).
- IPI protein binding GO:0005515 from high-throughput interactome/proteomics screens:
  - PMID:21988832 (human liver interactome) WITH HSP90AB1 (P08238).
  - PMID:25036637 (Taipale chaperone interaction network) WITH HSP90AA1 (P07900), HSP90AB1 (P08238, Q6PK50), STIP1 (P31948). This is the most biologically relevant: it maps CDC37L1 into the Hsp90 co-chaperone module of the chaperome.
  - PMID:25416956 (Rolland human interactome Y2H) WITH HSP90AB1 (P08238).
  - PMID:32814053 (Haenig neurodegeneration interactome) WITH BRK1 (Q8WUW1).
  - PMID:33961781 (Huttlin BioPlex) WITH HSP90AA1 (P07900), HSP90AB1 (P08238).
  - PMID:40205054 (Schaffer multimodal cell maps) WITH HSP90AB1 (P08238).
  These cached papers are genome-scale screens; none discuss CDC37L1 mechanistically in body text, but the WITH partners (HSP90AA1/AB1, STIP1) are consistent with the co-chaperone role.
- TAS (Reactome:R-HSA-481009 "Exocytosis of platelet dense granule content"): extracellular region GO:0005576; platelet dense granule lumen GO:0031089. CDC37L1 was detected in platelet releasate / dense granule proteomics; this is a localization annotation from platelet biology, not its core chaperone function. Keep as non-core (curated TAS, plausible localization) rather than removing.

## Interpretation / review decisions
- Core function: HSP90/HSP70 co-chaperone — adaptor that binds Hsp90 (and Hsp70/Hop) and promotes client (notably protein kinase) folding/maturation, paralogous to CDC37.
- Specific binding terms supported: heat shock protein binding (GO:0031072), protein-folding chaperone binding (GO:0051087), Hsp90 protein binding (GO:0051879). The bare "protein binding" GO:0005515 IPI annotations are uninformative; where the WITH partner is HSP90 these are better captured by GO:0051879 Hsp90 protein binding, but per curation guidelines the redundant bare-protein-binding rows are marked over-annotated (the specific HSP90 binding is already covered by the IBA heat shock protein binding term).
- Note: GO:0003767 "co-chaperone activity", GO:0061077 "chaperone-mediated protein folding", and GO:0051085 are OBSOLETE — do not use.
- Annotations such as protein folding (GO:0006457) and protein stabilization (GO:0050821) are reasonable BP outcomes of the co-chaperone role (kept as non-core since CDC37L1's direct molecular role is co-chaperone binding/adaptor, with folding/stabilization being downstream of the Hsp90 machine).
