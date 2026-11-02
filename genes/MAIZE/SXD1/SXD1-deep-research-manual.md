# SXD1 (Zea mays, Q94FY8) - manual literature synthesis

No deep-research API provider was available for this session. This file is a manual
literature synthesis prepared from cached publications (publications/PMID_*.md) and
PubMed searches (query: `(sxd1 OR "sucrose export defective") AND maize`, 11 hits).

## Identity

- UniProt Q94FY8 (TOCC_MAIZE), Tocopherol cyclase, chloroplastic, EC 5.5.1.24; 474 aa with a
  predicted 65-aa chloroplast transit peptide (UniProt, ECO:0000255).
- Gene: Sucrose export defective1 (Sxd1); Zm00001eb237270 / Zm00001d015985; chromosome 5.
  UniProt cross-references NCBI GeneID 541877.
- Family: Pfam PF14249 Tocopherol_cycl; InterPro IPR025893; PANTHER PTHR35309:SF2
  (TOCOPHEROL CYCLASE, CHLOROPLASTIC). Orthologous to Arabidopsis VTE1 (At4g32770) and
  Synechocystis slr1737.

## Gene cloning and localization (Provencher et al. 2001)

- The Sxd1 gene was cloned and "shown to encode a novel protein conserved between plants and
  cyanobacteria" [PMID:11340186].
- "The SXD1 protein was localized to chloroplasts, in both bundle sheath and mesophyll cells."
  [PMID:11340186]
- Expression: "the gene was transcribed in all green tissues, with highest levels in maturing
  leaf blades" [PMID:11340186].
- Mutant phenotype: sugars trapped in anthocyanin-accumulating leaf regions "due to plasmodesmal
  occlusion at the bundle sheath-vascular parenchyma boundary of the minor veins"; at that time
  the authors proposed a chloroplast-to-nucleus signaling model [PMID:11340186]. This model
  predates identification of the biochemical activity.

## Biochemical function (Sattler et al. 2003)

- "Mutations in the VTE1, SXD1, or slr1737 genes resulted in both tocopherol deficiency and the
  accumulation of 2,3-dimethyl-6-phytyl-1,4-benzoquinone (DMPBQ), a TC substrate." [PMID:12913173]
- "Recombinant SXD1 and VTE1 proteins are able to convert DMPBQ to gamma-tocopherol in vitro."
  [PMID:12913173]
- "expression of maize SXD1 in a Synechocystis sp. PCC6803 slr1737 knockout mutant restored
  tocopherol synthesis" [PMID:12913173] - cross-kingdom complementation.
- A conserved 30-aa C-terminal domain specific to plant TCs is proposed to be necessary for
  activity in plants [PMID:12913173].
- The abstract speculates that tocopherols/breakdown products or the accumulating DMPBQ affect
  signaling required for sucrose export [PMID:12913173]. (Abstract-only in cache.)

## Ortholog evidence (Arabidopsis VTE1)

- vte1 mutants "lacked all four tocopherol forms and were deficient in tocopherol cyclase
  activity"; recombinant VTE1 has "high tocopherol cyclase and tocotrienol cyclase activity"
  [PMID:12213958].
- VTE1 is a plastoglobule protein: proteomics showed "specific plastoglobule association of ...
  the tocopherol cyclase (VTE1)", and plastoglobules are a site of vitamin E accumulation
  [PMID:16414959, abstract only].

## Physiological consequence of loss of SXD1 (Ma et al. 2008; full text)

- "Sxd1 encodes tocopherol cyclase, an enzyme functioning in tocopherol (vitamin E)
  biosynthesis, and sxd1 mutants lack tocopherols" [PMID:17924136].
- Tocopherols were "none detected" in sxd1-1 leaves (Table 4) [PMID:17924136].
- "Absence of tocopherols results in callose deposition over the plasmodesmata at the bundle
  sheath-vascular parenchyma cell interface of leaf minor veins" which "prevents sucrose from
  moving into the vein" [PMID:17924136].
- "It is not known how lack of tocopherols causes callose deposition." [PMID:17924136]
- tdy1 has wild-type tocopherol levels; tdy1 and sxd1 act in independent genetic pathways
  (additive double mutant) [PMID:17924136].
- Conservation of the phenotype: RNAi suppression of tocopherol cyclase in potato causes callose
  deposition and carbohydrate accumulation [PMID:15247386], and Arabidopsis vte mutants show it
  under low temperature (cited in PMID:17924136).

## Interpretation

SXD1 is the plastid tocopherol cyclase. The sucrose-export/callose/plasmodesmata phenotype is a
downstream, indirect consequence of tocopherol deficiency (mechanism unknown), not a direct
activity of SXD1 in carbohydrate transport or plasmodesma regulation.
