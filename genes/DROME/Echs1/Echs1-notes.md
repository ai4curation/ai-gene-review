# Echs1 (Q0E987, Drosophila melanogaster) research notes

Drosophila melanogaster **Echs1** / CG6543 (FlyBase FBgn0033879; UniProt Q0E987, unreviewed TrEMBL). Ortholog of human ECHS1 (P30084), short-chain enoyl-CoA hydratase 1 / mitochondrial "crotonase"; EC 4.2.1.17. Gene on chromosome 2R. Encodes two isoforms (A = AAF58326.1, B = AAF58327.1).

## Identity / orthology

- UniProt entry name Q0E987_DROME, SubName "Enoyl-CoA hydratase, short chain 1, isoform A/B", with EC=4.2.1.17 and EC=4.2.1.116 assigned from EMBL records [Echs1-uniprot.txt: "EC=4.2.1.17 {ECO:0000313|EMBL:AAF58326.1, ECO:0000313|EMBL:AAF58327.1}"].
- Gene symbol `Echs1` and ORF name `CG6543`, FlyBase FBgn0033879 [Echs1-uniprot.txt GN lines]. AGR/CTD cross-reference to human gene CTD:1892 (ECHS1) [Echs1-uniprot.txt: "DR   CTD; 1892; -."].
- Domain architecture: crotonase-like fold — CDD cd06558 "crotonase-like"; Pfam PF00378 ECH_1; InterPro IPR001753 Enoyl-CoA_hydra/iso, IPR014748 Enoyl-CoA_hydra_C, IPR018376 Enoyl-CoA_hyd/isom_CS; PROSITE PS00166 ENOYL_COA_HYDRATASE; PANTHER PTHR11941:SF54 "ENOYL-COA HYDRATASE, MITOCHONDRIAL"; SUPFAM SSF52096 ClpP/crotonase [Echs1-uniprot.txt DR lines]. This is the canonical short-chain enoyl-CoA hydratase (crotonase) signature.
- The fly protein is 295 aa with an N-terminal region rich in Arg/Ser resembling a mitochondrial targeting presequence (MANIAKIFAS RAQCVLQAAA RQPQVATRFS SSS...) [Echs1-uniprot.txt SQ]. Consistent with a matrix enzyme, though the transit peptide is not experimentally annotated in this TrEMBL entry.

## Core enzymatic function (by orthology to human ECHS1)

Human ECHS1 catalyses the second step of the mitochondrial beta-oxidation spiral: reversible hydration of a 2-trans-enoyl-CoA to the corresponding (3S)-3-hydroxyacyl-CoA (EC 4.2.1.17), acting on short/medium-chain substrates (C4-C16) with highest efficiency toward crotonyl-CoA. It also hydrates branched-chain amino acid pathway intermediates (methacrylyl-CoA/acryloyl-CoA from valine; 3-methylcrotonyl-CoA from leucine; tiglyl-CoA from isoleucine).

- [PMID:26251176 "Short-chain enoyl-CoA hydratase-ECHS1-catalyses many metabolic pathways, including mitochondrial short-chain fatty acid β-oxidation and branched-chain amino acid catabolic pathways"].
- [PMID:26251176 "Human ECHS1 catalyses the hydration of five substrates via different metabolic pathways, with the highest specificity for crotonyl-CoA and the lowest specificity for tiglyl-CoA."].

The fly UniProt DR block records the corresponding GO/pathway assignments: enoyl-CoA hydratase activity (GO:0004300, ISS), 3-hydroxypropionyl-CoA dehydratase activity (GO:0043956, ISS), fatty acid beta-oxidation (GO:0006635, ISS), L-valine catabolic process (GO:0006574, IMP), and mitochondrion (GO:0005739, IDA) [Echs1-uniprot.txt DR GO lines]. Reactome links the fly gene to "Branched-chain amino acid catabolism" (R-DME-70895) and to the beta-oxidation spiral steps (R-DME-77310/77346/77348/77350/77352) [Echs1-uniprot.txt DR Reactome lines].

## GOA annotations under review (Echs1-goa.tsv)

Only two GOA annotations, both IEA:

1. **GO:0003824 catalytic activity** — IEA, GO_REF:0000002 (InterPro IPR018376). Root-level MF placeholder; correct but uninformative, subsumed by enoyl-CoA hydratase activity. Action: MARK_AS_OVER_ANNOTATED (matches human ECHS1 review handling of the same InterPro-derived term).
2. **GO:0004300 enoyl-CoA hydratase activity** — IEA, GO_REF:0000120 (ARBA:ARBA00086629 | EC:4.2.1.17). This is the defining/core molecular function, assigned from the EC number. Action: ACCEPT. Supported by ortholog biochemistry (PMID:26251176) and by functional rescue of the fly mutant by a human ECHS1 transgene (Mele et al. 2025).

(Note: the UniProt DR block lists further FlyBase GO annotations — GO:0005739 mitochondrion IDA, GO:0006574 L-valine catabolic process IMP, GO:0006635 fatty acid beta-oxidation ISS, GO:0043956 3-hydroxypropionyl-CoA dehydratase ISS — but these are NOT present in the QuickGO GOA export (Echs1-goa.tsv), so per instructions they are not added as existing_annotations. They inform the description and core_functions.)

## Drosophila functional evidence (ortholog grounding)

- **PMID:40056416** (Li et al., Cell Rep 2025; abstract-only, `full_text_available: false`): HIBCH and ECHS1 are "two Leigh syndrome genes"; their loss in cultured cells causes "abnormal mitochondrial morphology and respiratory defects." Directly in Drosophila: "Fly eyes lacking either protein exhibit age-dependent degeneration." "Elevated lysine methacrylation (Kmea) is observed in both HIBCH- and ECHS1-deficient cells and fly tissues." Mechanistically, loss of ECHS1 lets the valine-pathway intermediate methacrylyl-CoA accumulate and drive ectopic protein lysine methacrylation. This paper is the basis for the FlyBase IMP annotation to L-valine catabolic process and is a strong, organism-matched support for the fly gene's role in valine catabolism.
- **Mele et al. 2025, J Inherit Metab Dis (doi:10.1002/jimd.12840; biorxiv 2024.08.15.608013)** — NOT cached, cited from notes only: a Drosophila model of Echs1 (CG6543) deficiency; "Echs1 null larvae recapitulated human ECHS1D phenotypes including poor motor behaviour and early mortality and could be rescued by the expression of a human ECHS1 transgene," and valine dietary restriction extends survival. This establishes functional orthology (human ECHS1 rescues fly Echs1 loss) and confirms the valine-catabolism connection in the fly. Because it is not in the publications/ cache, it is used only as background here, not as verbatim supporting_text for annotations.

## Decisions summary

- Enzyme is the fly crotonase (EC 4.2.1.17); core MF = enoyl-CoA hydratase activity (GO:0004300). ACCEPT the GOA IEA for it.
- Root "catalytic activity" (GO:0003824) is over-annotated relative to the specific hydratase term. MARK_AS_OVER_ANNOTATED.
- Core BP = fatty acid beta-oxidation (GO:0006635) and L-valine catabolic process (GO:0006574) by orthology + fly genetic evidence (PMID:40056416; Mele 2025). These are captured in core_functions but NOT added to existing_annotations because they are absent from the GOA export.
- Localization: mitochondrion (matrix, by orthology); not in GOA export, so not an existing_annotation, but noted for description.
