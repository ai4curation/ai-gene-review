# Z-ISO (Arabidopsis thaliana, At1g10830, UniProt Q9SAC0) — review notes

## Identity

- UniProt Q9SAC0, ZCIS_ARATH, "15-cis-zeta-carotene isomerase, chloroplastic", EC 5.2.1.12,
  gene Name=Z-ISO; OrderedLocusNames=At1g10830 [file:ARATH/Z-ISO/Z-ISO-uniprot.txt].
- 367 aa precursor with a predicted N-terminal chloroplast transit peptide (1-58) and six
  predicted transmembrane helices (multi-pass membrane protein) [file:ARATH/Z-ISO/Z-ISO-uniprot.txt].
- Domain: NnrU (Pfam PF07298; InterPro IPR009915). PANTHER family PTHR35988 / subfamily
  PTHR35988:SF2 "15-CIS-ZETA-CAROTENE ISOMERASE, CHLOROPLASTIC" [file:ARATH/Z-ISO/Z-ISO-uniprot.txt].
- Two alternative-splicing isoforms; isoform 1 (Q9SAC0-1) is the major, active form; isoform 2
  (Q9SAC0-2, VSP_041999/VSP_042000) has an altered/truncated C-terminus and is reported inactive
  in the heterologous assay [file:ARATH/Z-ISO/Z-ISO-deep-research-falcon.md "one fewer predicted
  membrane span and lacks detectable activity in the heterologous assay"].

## Function (what it does)

- Z-ISO catalyses the cis-to-trans isomerization of the central 15-cis (15-15') double bond of
  9,9',15-tri-cis-zeta-carotene to give 9,9'-di-cis-zeta-carotene (Rhea:30967, ChEBI:48717 ->
  ChEBI:48716; EC 5.2.1.12) [file:ARATH/Z-ISO/Z-ISO-uniprot.txt "Reaction=9,9',15-tri-cis-zeta-carotene
  = 9,9'-di-cis-zeta-carotene;"]. Note: I verified the ChEBI labels via OLS — CHEBI:48717 =
  9,9',15-tri-cis-zeta-carotene (substrate), CHEBI:48716 = 9,9'-di-cis-zeta-carotene (product).
- Directly proven experimentally in the identification paper: functional expression in E. coli
  [PMID:20335404 "15-cis double bond in 9,15,9'-tri-cis-zeta-carotene, proving that Z-ISO encoded"]
  (abstract-only cache; full_text_available: false). This is the source of the IDA GO:0090471 row.
- Pathway position: acts between the two plastid poly-cis desaturases PDS and ZDS. PDS makes
  9,9',15-tri-cis-zeta-carotene; Z-ISO isomerizes its 15-cis bond so that ZDS can act; ZDS then
  makes prolycopene and CRTISO makes all-trans-lycopene
  [file:modules/carotene_backbone_biosynthesis.yaml, ziso_step; connections PDS->Z-ISO->ZDS].
- Physiological importance: essential for light-independent ("dark") carotenoid synthesis and
  improves efficiency in the light; light can only partially photoisomerize the 15-cis bond
  [PMID:20335404 "Z-ISO was found to be important for both light-exposed and" (dark) tissues].
  Disruption phenotype: "Lacks carotenoids in the dark and exhibits delayed greening when exposed
  to light" [file:ARATH/Z-ISO/Z-ISO-uniprot.txt].

## Cofactor / mechanism

- Beltrán et al. 2015 (Nat Chem Biol) showed plant Z-ISO is a bona fide, independently acting
  enzyme and integral membrane protein whose isomerization depends on a ferrous heme b cofactor
  with redox-regulated axial-ligand switching [PMID:26075523 "Z-ISO is a bona fide enzyme and
  integral membrane protein"; "isomerization depends upon a ferrous heme b cofactor that undergoes"
  redox-regulated ligand switching]. IMPORTANT CAVEAT: the decisive biochemistry used protein
  "isolated Z-ISO from Zea mays" [PMID:26075523]; transfer to Arabidopsis Q9SAC0 rests on
  orthology/conservation. The deep-research report agrees the Arabidopsis protein itself has not
  been characterized to that depth [file:ARATH/Z-ISO/Z-ISO-deep-research-falcon.md].
- This supports: (a) the integral chloroplast-membrane location (GO:0031969), and (b) a heme
  binding molecular function (GO:0020037), which is not in GOA and is proposed here as NEW by
  orthology to maize Z-ISO plus cross-lineage conservation.

## Localization

- UniProt: "Plastid, chloroplast membrane; Multi-pass membrane protein" (ECO:0000305)
  [file:ARATH/Z-ISO/Z-ISO-uniprot.txt]. GOA carries GO:0009507 chloroplast (HDA from the van Wijk
  chloroplast-proteome study PMID:18431481, and ISM from AtSubP GO_REF:0000122) and GO:0031969
  chloroplast membrane (IEA from UniProt SubCell GO_REF:0000044).
- PMID:18431481 is full_text_available: true but the cached body does not name At1g10830/Q9SAC0 in
  a grep; the gene-level datum is in the large-scale proteomics supplementary data. The HDA
  chloroplast call is consistent with the transit peptide, the plastid-restricted pathway, and
  UniProt, so ACCEPT and support from the UniProt subcellular line rather than a body quote.
- Exact plastid sub-membrane (envelope vs thylakoid) is unresolved
  [file:ARATH/Z-ISO/Z-ISO-deep-research-falcon.md "The most defensible annotation is therefore
  chloroplast/plastid integral membrane, without assigning a unique membrane compartment"].

## Annotation-by-annotation decisions

1. GO:0009507 chloroplast (HDA, PMID:18431481, located_in) -> ACCEPT. Correct organelle; proteomics
   + transit peptide + plastid pathway all agree.
2. GO:0009507 chloroplast (ISM, GO_REF:0000122, located_in) -> ACCEPT. AtSubP sequence prediction,
   duplicate of the same correct location.
3. GO:0016120 carotene biosynthetic process (IMP, PMID:20335404, acts_upstream_of_or_within) ->
   ACCEPT (core process). Z-ISO performs a catalytic step of the carotene backbone route; mutant
   lacks carotenoids in the dark. Zeta-carotene, its substrate and product, is a carotene.
4. GO:0031969 chloroplast membrane (IEA, GO_REF:0000044, located_in) -> ACCEPT (core location).
   UniProt multi-pass membrane protein; Beltrán integral membrane protein.
5. GO:0090471 9,15,9'-tri-cis-zeta-carotene isomerase activity (IDA, PMID:20335404, enables) ->
   ACCEPT (core MF). Directly demonstrated by E. coli functional expression.
6. GO:0090471 same (IEA, GO_REF:0000120 Rhea/EC mapping, enables) -> ACCEPT. Automated EC 5.2.1.12
   / Rhea:30967 mapping that coincides with the experimental IDA; duplicates are fine.

## NEW proposals (conservative)

- GO:0016117 carotenoid biosynthetic process (NEW, involved_in). Participation test passed: Z-ISO
  catalyses a committed step of the pathway that produces carotenoids. Comparator check passed:
  the sibling pathway enzyme CRTISO carries GO:0016117 (IEA/TAS) and the carotene backbone module
  uses GO:0016117 as the module-level process. Not redundant with the existing GO:0016120: in the
  current ontology GO:0016120 carotene biosynthetic process is NOT a descendant of GO:0016117
  carotenoid biosynthetic process (verified; also stated in the module knowledge_gaps), so a
  GO:0016117 query otherwise under-retrieves Z-ISO.
- GO:0020037 heme binding (NEW, enables/MF). Z-ISO requires a ferrous heme b cofactor
  [PMID:26075523]. Direct molecular function of the protein (cofactor binding). Evidence is maize
  Z-ISO transferred by orthology; flagged in reference_review.

Rejected as over-annotation / not asserted:
- Did NOT propose GO:1901177 lycopene biosynthetic process: Z-ISO's direct product is a
  zeta-carotene, two enzymatic steps upstream of lycopene; GO:0016120 already captures the
  carotene-level process and GO:0016117 the carotenoid-level process, so a lycopene-specific term
  would over-reach the direct product. Raised instead as context only.
- Did NOT add a separate "denitrification"/NnrU functional term despite the NnrU ancestry
  [PMID:20335404]: the ancestry is evolutionary, and bacterial NnrU proteins tested lack
  carotenoid-isomerase activity [file:ARATH/Z-ISO/Z-ISO-deep-research-falcon.md].

## Validation

- `just validate ARATH Z-ISO` run after editing; see final report.
