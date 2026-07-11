# GLB1 (human) — curation notes

UniProtKB: P16278 (BGAL_HUMAN). HGNC:4298. EC 3.2.1.23. Glycosyl hydrolase family 35 (CAZy GH35).

## Core biology (grounded in UniProt + cached publications; falcon deep research unavailable, HTTP 402)

GLB1 encodes **lysosomal acid beta-galactosidase (β-Gal)**, an exoglycosidase that
hydrolyses **terminal non-reducing β-D-galactose residues** from a broad range of
substrates.

- UniProt CATALYTIC ACTIVITY: "Hydrolysis of terminal non-reducing beta-D-galactose
  residues in beta-D-galactosides.; EC=3.2.1.23" [file:human/GLB1/GLB1-uniprot.txt].
- UniProt FUNCTION [Isoform 1]: "Cleaves beta-linked terminal galactosyl residues from
  gangliosides, glycoproteins, and glycosaminoglycans." [file:human/GLB1/GLB1-uniprot.txt].
- pH optimum 4.5–5.5 (acid hydrolase) [file:human/GLB1/GLB1-uniprot.txt].

Two disease-relevant catabolic roles:
1. **Ganglioside/glycosphingolipid catabolism** — removes the terminal galactose of GM1
   ganglioside (→ GM2) and of its asialo derivative GA1 (→ GA2). Deficiency → lysosomal
   accumulation of GM1 and GA1 [PMID:31720227 "removes β-linked galactose from the
   non-reducing end of glycans... leads to the lysosomal accumulation of GM1 and its
   asialo derivative GA1"]. Also acts (with sap-B) on lactosylceramide/GM1 in vitro
   [PMID:8200356].
2. **Keratan sulfate / glycosaminoglycan and glycoprotein catabolism** — GM1
   gangliosidosis / Morquio B accumulate keratan sulfate and β-galactose-terminated
   N-/O-linked glycans. GLB1 deficiency is a "broad oligosaccharidosis" [PMID:31720227].

## Structure / mechanism
- Crystal structure (homodimer): catalytic **TIM barrel** + β-domain 1 + β-domain 2; "β-Gal
  is an exoglycosidase that catalyzes the hydrolysis of terminal β-linked galactose
  residues" [PMID:22128166]. Active site: proton donor Glu188, nucleophile Glu268
  (UniProt ACT_SITE). Binds galactose product; homodimer [PMID:22128166].

## Lysosomal multienzyme complex
- GLB1 forms a lysosomal complex with **protective protein/cathepsin A (PPCA/CTSA),
  α-neuraminidase (NEU1)** and GALNS; PPCA stabilises β-Gal multimers
  [PMID:15714521 "GLB1 forms a complex with protective protein cathepsin A (PPCA), alpha
  neuraminidase (NEU1), and galactosamine 6-sulphate sulfatase (GALNS) inside lysosomes"].
  Loss of PPCA (galactosialidosis) → combined β-Gal/NEU1 deficiency; PPCA restores
  high-MW β-Gal multimers [PMID:3084261].

## Localisation
- Lysosome (isoform 1). Synthesised as precursor in RER → Golgi → mature high-MW multimer
  in lysosome [PMID:3084261]. UniProt SUBCELLULAR LOCATION [Isoform 1]: Lysosome
  [PMID:2511208, PMID:3084261].

## Isoform 2 (EBP / elastin-binding protein / S-Gal)
- Alternatively spliced, **catalytically inactive** (~67 kDa); functions in elastic-fibre
  assembly (elastogenesis) as a recycling chaperone for tropoelastin; localises to
  perinuclear cytoplasm / cell surface, NOT lysosome [UniProt FUNCTION [Isoform 2],
  SUBCELLULAR LOCATION [Isoform 2]; PMID:2511208]. The perinuclear-region (GO:0048471) and
  cytoplasm (GO:0005737) CC annotations pertain to this non-catalytic isoform.

## Disease
- Allelic disorders, all autosomal recessive lysosomal storage diseases:
  GM1-gangliosidosis types 1/2/3 (MIM 230500/230600/230650) and Mucopolysaccharidosis
  type IVB / Morquio B (MIM 253010) [UniProt DISEASE].

## Annotation-review judgement calls
- **PMID:11927518** (atherosclerosis / endothelial senescence): measures
  **senescence-associated β-gal (SA-β-gal) histochemical staining**, a phenotypic readout
  of lysosomal β-Gal activity at pH 6, not a biochemical characterisation of the GLB1
  enzyme's substrate specificity. The IDA "beta-galactosidase activity", "carbohydrate
  metabolic process", and "cytoplasm" annotations from this paper are over-annotations /
  peripheral (SA-β-gal signal is lysosomal, not cytoplasmic). Kept but marked
  over-annotated; not core.
- **protein binding (GO:0005515) IPIs**: PMID:32296183 (HuRI binary interactome — GOLM1,
  SLC10A6, SLC30A2, SLC7A1; membrane transporters, likely non-physiological Y2H hits);
  PMID:15498789 (NGX6 paper — GLB1 not the subject). Bare `protein binding`, uninformative.
  Per policy: MARK_AS_OVER_ANNOTATED, not REMOVE.
- **GO:0042803 protein homodimerization activity** IPI PMID:22128166: real — the crystal
  structure shows a homodimer. ACCEPT (non-core).
- Exosome / granule / extracellular-region CC terms (HDA proteomics + Reactome
  neutrophil-degranulation): GLB1 is a soluble lysosomal enzyme detected in these
  proteomic/secretory contexts but its site of action is the lysosome. Kept as non-core.
- IEA `response to cortisone` (GO:0051413) and `response to Thyroglobulin triiodothyronine`
  (GO:1904016): rat-ortholog electronic transfers (GO_REF:0000107), no human evidence,
  not molecular function of the enzyme. Marked over-annotated.
