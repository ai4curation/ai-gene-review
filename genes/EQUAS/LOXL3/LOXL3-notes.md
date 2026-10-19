# LOXL3 (donkey, A0A9L0K7N3) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry, 824 aa, "Lysyl oxidase homolog" (UniRule RU367046). A human LOXL3 review exists in this repository (genes/human/LOXL3/LOXL3-ai-review.yaml) and was used for consistency.

## Identity and sequence
- PANTHER PTHR45817:SF2 (LYSYL OXIDASE HOMOLOG 3); four SRCR domains and the C-terminal lysyl oxidase domain [file:EQUAS/LOXL3/LOXL3-uniprot.txt "DR   PANTHER; PTHR45817:SF2; LYSYL OXIDASE HOMOLOG 3; 1."].
- 95.62% identity to human P58215 over the whole human length; copper-binding His and LTQ Lys/Tyr conserved; donkey 52-residue N-terminal extension places the human signal-peptide segment internally [file:EQUAS/LOXL3/LOXL3-bioinformatics/RESULTS.md "Human Met1 aligns to donkey Met53"].

## Function (human ortholog)
- Copper-dependent amine oxidase of the LOX family; human LOXL3 and LOXL3-sv1 oxidize elastin and collagen [PMID:17018530 "The recombinant LOXL3-sv1 protein showed a beta-aminopropionitrile-inhibitable amine oxidase activity toward elastin and collagen with substrate specificity."].
- Domain architecture with copper-binding sequence and LTQ residues; recombinant protein secreted [PMID:11284725 "Recombinant LOXL3, expressed in HT-1080 cells, was secreted into the culture medium but was not detected by immunofluorescence staining in nuclei."].
- Collagen I oxidation by LOXL3-sv2 [PMID:28112368 "The recombinant LOXL3-sv2 protein showed a β-aminopropionitrile-inhibitable amine oxidase activity toward collagen type I."].
- Nuclear Loxl3 deacetylates Stat3 via its SRCR repeats; Loxl3-/- naive CD4+ T cells show enhanced Th17/Treg differentiation [PMID:28065600 "LOX-like 3 (Loxl3) associates with Stat3"; "In Loxl3-/- mice, Stat3 is constitutively acetylated"].

## Annotation decisions (consistent with human LOXL3 review)
- protein-lysine 6-oxidase activity, copper ion binding, extracellular region, collagen fibril organization: ACCEPT.
- oxidoreductase activity acting on CH-NH2 group, oxygen as acceptor: TOO_GENERAL (entailed by protein-lysine 6-oxidase activity).
- nucleus, cytoplasm, inflammatory response, negative regulation of Th17 lineage commitment, tissue development, animal organ development: KEEP_AS_NON_CORE.
- elastic fiber: MARK_AS_OVER_ANNOTATED (substrate relationship, not established residence).
- membrane (InterPro SRCR mapping): REMOVE (soluble secreted protein; SRCR domains are not membrane anchors).

## ProtNLM2
- GO:0018057 peptidyl-lysine oxidation: not in donkey GOA; correct (the enzyme performs this protein modification) -> COR.
- No non-GO ProtNLM2 rows for this accession.
