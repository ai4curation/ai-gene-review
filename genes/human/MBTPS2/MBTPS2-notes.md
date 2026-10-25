# MBTPS2 (S2P) review notes

## Provenance / process

- 2026-10-18: Falcon deep research was attempted once in this session (for MBTPS1) and failed at
  authentication ("Exception: Failed to authenticate"; key unauthorised / 403). Not retried for
  MBTPS2. No `-deep-research-*.md` file exists; notes compiled manually from cached publications
  (mostly abstract-only), UniProt and Reactome.

## Identity and structure

- 519 aa polytopic membrane protein; N and C termini cytosolic; "Belongs to the peptidase M50A
  family" (UniProt; MEROPS M50.001; PANTHER PTHR13325:SF3).
- Zinc metalloprotease with HEIGH motif within a hydrophobic segment and Asp467 as third zinc ligand
  [PMID:10419520 "The HEIGH sequence of S2P, which contains two potential zinc-coordinating residues,
  is contained within a long hydrophobic segment."; "Aspartic acid 467, located approximately 300
  residues away from the HEIGH sequence, appears to provide the third coordinating residue for the
  active site zinc."].
- Cloned by complementation of CHO M19 cells [PMID:9659902 "S2P defines a new family of polytopic
  membrane proteins that contain an HEXXH sequence characteristic of zinc metalloproteases.
  Mutation of the putative zinc-binding residues abolishes S2P activity."].

## Mechanism

- Second, sterol-independent cleavage of SREBP within TM1 after S1P [PMID:8674110 "The second, not
  regulated by sterols, occurs within the first transmembrane domain."]; cleaves Leu-Cys bond; needs
  Asn-Pro helix-breaking motif in the substrate TM [PMID:10805775 "The studies reveal a requirement
  for an asparagine-proline sequence in the middle third of the transmembrane segment."].
- Substrate must first be trimmed by S1P (S2P acts on short-lumenal-domain intermediates).
- ATF6 second cleavage; S2P-null cells fail to induce GRP78 [PMID:11163209 "Cells lacking S2P failed
  to induce GRP78, an ATF6 target, in response to ER stress."].
- Also OASIS/CREB3L1, CREB3L2, CREB3L3 (Reactome R-HSA-8874201) [PMID:16417584].
- Site of action: Golgi (Reactome; UniProt Golgi membrane by similarity/inference from PMID:16417584).

## Disease

- IFAP syndrome (X-linked) [PMID:19361614 "missense mutations exchanging highly conserved amino acids
  of membrane-bound transcription factor protease, site 2 (MBTPS2) are associated with this
  phenotype"]; severity correlates with residual activity.
- KFSD-X, X-linked Olmsted syndrome, and X-linked osteogenesis imperfecta type XIX [PMID:27380894
  "Mutant S2P has normal stability, but impaired functioning in regulated intramembrane proteolysis
  (RIP) of OASIS, ATF6 and SREBP transcription factors, consistent with decreased proband secretion
  of type I collagen."].
- S2P is not needed for lysosomal enzyme trafficking (contrast with S1P/GNPTAB) [PMID:30046013].

## Curation decisions summary

- Core MF: metalloendopeptidase activity (GO:0004222) — ACCEPT all four rows.
- Core BP: membrane protein intracellular domain proteolysis (GO:0031293) (ACCEPT IBA, IGI);
  ATF6-mediated UPR (ACCEPT); positive regulation of cholesterol biosynthetic process (ACCEPT IDA;
  "regulation of" TAS and "cholesterol metabolic process" TAS -> MODIFY to GO:0045542).
- `proteolysis` IEA -> MODIFY to GO:0031293. `protein maturation` rows -> MODIFY to GO:0016485.
- `response to ER stress` -> MODIFY to GO:0036500.
- `transcription regulator activator activity` (IGI) -> MODIFY to GO:0004222: S2P is an enzyme
  whose product is an active transcription factor; GO represents that as the catalytic activity.
- `positive regulation of transcription by RNA pol II` (IGI) -> MARK_AS_OVER_ANNOTATED (two steps
  removed, executed by released SREBP/ATF6 fragments).
- Locations: Golgi membrane ACCEPT; cytoplasm (IBA/IDA/IEA) and membrane -> MODIFY to Golgi membrane.
- bone maturation (IMP, OI19) -> KEEP_AS_NON_CORE.
- regulation of response to ER stress (IBA, deep node with Arabidopsis S2P) -> KEEP_AS_NON_CORE.
