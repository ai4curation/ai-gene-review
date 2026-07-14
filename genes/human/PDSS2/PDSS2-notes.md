# PDSS2 (Q86YH6) review notes

Human PDSS2 = "All trans-polyprenyl-diphosphate synthase PDSS2" / decaprenyl-diphosphate
synthase subunit 2 (a.k.a. DLP1, hDLP1, C6orf210). HGNC:23041. Gene on chr 6q21.

## Core biology (from UniProt Q86YH6)

- **Function / catalytic activity.** PDSS2 is one subunit of a heterotetrameric
  trans-prenyltransferase. The complex condenses (2E,6E)-farnesyl diphosphate (FPP),
  which acts as the primer, with isopentenyl diphosphate (IPP) units to build the
  all-trans decaprenyl (C50) side chain of ubiquinone (coenzyme Q10). It is the first
  committed step of the CoQ10 side-chain assembly.
  - UniProt FUNCTION: "Heterotetrameric enzyme that catalyzes the condensation of
    farnesyl diphosphate (FPP), which acts as a primer, and isopentenyl diphosphate
    (IPP) to produce prenyl diphosphates of varying chain lengths and participates in
    the determination of the side chain of ubiquinone" [file:human/PDSS2/PDSS2-uniprot.txt].
  - UniProt CATALYTIC ACTIVITY: "7 isopentenyl diphosphate + (2E,6E)-farnesyl
    diphosphate = all-trans-decaprenyl diphosphate + 7 diphosphate" ; EC=2.5.1.91 ;
    Rhea:RHEA:27802 ; evidence ECO:0000269|PubMed:16262699
    [file:human/PDSS2/PDSS2-uniprot.txt]. This is exactly GO:0097269
    "all-trans-decaprenyl-diphosphate synthase activity" (OLS definition: "7
    isopentenyl diphosphate + (2E,6E)-farnesyl diphosphate = all-trans-decaprenyl
    diphosphate + 7 diphosphate").
  - A second, "by similarity" catalytic activity to all-trans-nonaprenyl diphosphate
    (Q9 chain) is annotated by similarity to the mouse ortholog Q33DR3
    [file:human/PDSS2/PDSS2-uniprot.txt]; humans predominantly make Q10.

- **Subunit / complex.** UniProt SUBUNIT: "Heterotetramer composed of 2 PDSS1/DPS1
  and 2 PDSS2/DLP1 subunits" (ECO:0000269|PubMed:16262699)
  [file:human/PDSS2/PDSS2-uniprot.txt]. The functional enzyme is the PDSS1:PDSS2
  2:2 heterotetramer; neither subunit is catalytically active alone. This is
  GO:0032478 "heterotetrameric polyprenyl diphosphate synthase complex" (OLS def:
  "a heterotetrameric complex ... In S. pombe it is a heterotetramer of Dlp1 and
  Dps1"). The PDSS2 IPI "protein binding" annotation (WITH UniProtKB:Q5T2R2 = PDSS1)
  is simply this heterodimeric partnership, so the informative representation is the
  named complex, not bare "protein binding".

- **Primary evidence (PMID:16262699, Saiki et al. 2005, FEBS J).** Abstract-only in
  our cache (`full_text_available: false`). Abstract shows: mammalian long-chain
  trans-prenyl diphosphate synthases "are heterotetramers composed of newly
  characterized hDPS1 (mSPS1) and hDLP1 (mDLP1)"; co-expression of hDPS1 and hDLP1 in
  E. coli produced Q10 and "an in vitro activity of solanesyl or decaprenyl
  diphosphate synthase was verified"; gel filtration indicates "they consist of
  heterotetramers"; and heterologous mSPS1+hDLP1 / hDPS1+mDLP1 combinations gave both
  Q9 and Q10, "indicating both components are involved in determining the ubiquinone
  side chain" [PMID:16262699]. hDLP1 = PDSS2. So PDSS2 both is a complex subunit and
  is required for chain-length determination, but the catalytic activity is a
  complex-level property (hence GOA uses `contributes_to` for the MF and `part_of`
  for the complex).

- **Pathway.** UniProt PATHWAY: "Cofactor biosynthesis; ubiquinone biosynthesis"
  (ECO:0000269|PubMed:16262699) [file:human/PDSS2/PDSS2-uniprot.txt]. BP =
  GO:0006744 ubiquinone biosynthetic process. isoprenoid biosynthetic process
  (GO:0008299) is a true but more general parent process.

- **Localization.** UniProt SUBCELLULAR LOCATION: "Mitochondrion"
  (ECO:0000269|PubMed:34800366) [file:human/PDSS2/PDSS2-uniprot.txt]. Reactome places
  the reaction in the mitochondrial matrix (GO:0005759). The N-terminal sequence
  (MNFRQLLLHLPRYLGASGSPRRLWWSPS...) is consistent with a mitochondrial-targeting
  presequence. Substrates FPP/IPP are made in the cytosol and imported (Reactome:
  "IPPP and FPP are provided by cytosolic cholesterol biosynthesis. However, the
  means of transport of FPP and IPPP into mitochondria is unknown"
  [reactome/R-HSA-2162253]). A single-antibody HPA IDA to cytosol (GO:0005829)
  conflicts with the mitochondrial matrix consensus and is treated as an
  over-annotation (not removed — it is IDA).

- **Disease.** UniProt DISEASE: "Coenzyme Q10 deficiency, primary, 3 (COQ10D3)
  [MIM:614652]: A fatal encephalomyopathic form of coenzyme Q10 deficiency with
  nephrotic syndrome" (ECO:0000269|PubMed:17186472)
  [file:human/PDSS2/PDSS2-uniprot.txt]. The reported patient (Leigh syndrome with
  nephropathy) is the S382L variant (VAR_055398, PMID:17186472). The disease
  underscores the essential role of the PDSS1/PDSS2 enzyme in CoQ10 biosynthesis.
  PMID:17186472 is NOT cached locally (abstract not read); disease role stated only
  from the UniProt DISEASE block.

- **Family.** UniProt SIMILARITY: "Belongs to the FPP/GGPP synthase family"; Pfam
  PF00348 polyprenyl_synt; InterPro IPR000092. PANTHER subfamily PTHR12001:SF55 "ALL
  TRANS-POLYPRENYL-DIPHOSPHATE SYNTHASE PDSS2".

## Peripheral / weaker annotations

- **cerebellum development (GO:0021549).** UniProt FUNCTION: "May play a role during
  cerebellar development (By similarity)" [file:human/PDSS2/PDSS2-uniprot.txt]. This
  is a By-similarity / ISS + Ensembl-Compara transfer from the mouse ortholog
  (Q33DR3), not a demonstrated human function; the phenotype is plausibly downstream
  of CoQ10 deficiency rather than a distinct molecular role. Kept as non-core.
- **regulation of mitochondrial respiratory chain (By similarity).** UniProt
  FUNCTION: "May regulate mitochondrial respiratory chain function (By similarity)"
  [file:human/PDSS2/PDSS2-uniprot.txt]. Consistent with CoQ10 being an electron
  carrier of the respiratory chain; downstream consequence, not a separate MF.
- **lipid metabolic process (GO:0006629, ARBA IEA).** True but very general (a broad
  ancestor of isoprenoid/ubiquinone biosynthesis); over-annotation relative to the
  specific ubiquinone biosynthetic process term.
- **cytosol (GO:0005829, HPA IDA).** See localization note; conflicts with
  mitochondrial consensus; marked over-annotated.

## Core-function summary

- MF (complex-level, PDSS2 contributes): GO:0097269 all-trans-decaprenyl-diphosphate
  synthase activity.
- Complex: GO:0032478 heterotetrameric polyprenyl diphosphate synthase complex
  (2x PDSS1 + 2x PDSS2).
- BP: GO:0006744 ubiquinone biosynthetic process.
- Location: GO:0005759 mitochondrial matrix (mitochondrion, GO:0005739).
