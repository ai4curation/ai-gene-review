# LIH1 (YJR107W) — curation notes

## Deep-research provenance note (2026-07-05)

Automated deep research could not be generated for LIH1. `just deep-research-falcon`
(falcon provider) timed out twice at 600 s (exit 143/144), and the `perplexity-lite`
fallback returned HTTP 401 (insufficient_quota — API billing exhausted). Per project
policy I did NOT fabricate a `-deep-research-{provider}.md` file. This review is therefore
grounded directly in: (1) the UniProt record (P47145), (2) the QuickGO GOA export
(LIH1-goa.tsv), (3) the full text of the sole primary reference PMID:26580812 (fetched to
publications/, verified by grep), and (4) inline domain/catalytic-triad analysis of the
deposited sequence (below). This is a genuinely dark gene, so the literature is thin and
these sources are, in fact, essentially the entire evidence base.

UniProt: P47145 (LIH1_YEAST). SGD: S000003868. Systematic: YJR107W. ORF: J1983.
Length 328 aa; 37.2 kDa. Reference proteome (S288c). PE=1 (Evidence at protein level —
but see caveat below: this is a UniProt "protein level" that rests on peptide detection,
not on a functional assay).

## Bottom line (dark gene)

LIH1 ("Lipase homolog 1") is a **putative** lipase. Its "lipase" identity is an inference
from sequence homology and domain architecture, NOT from any biochemical characterization of
the LIH1 protein itself. There is:
- NO demonstrated enzymatic activity for LIH1.
- NO known natural substrate.
- NO reported subcellular localization (SGD MF/BP/CC are ND).
- NO reported loss-of-function phenotype (BioGRID-ORCS: 0 hits in 10 CRISPR screens; the
  gene is non-essential and no strong phenotype is on record).
- NO experimental paper that characterizes LIH1 as an enzyme.

This is a genuine biology knowledge gap (the unknome): the fold and catalytic machinery are
present, but what the protein does, where, and why is unknown.

## Identity / domain reasoning (from LIH1-uniprot.txt, verified inline)

- Family: AB hydrolase superfamily, Lipase family (UniProt SIMILARITY, ECO:0000305).
- Pfam PF01764 (Lipase_3); CDD cd00519 (Lipase_3); InterPro IPR002921 (Fungal lipase-type),
  IPR029058 (AB hydrolase fold), IPR051299 (AB_hydrolase_lip/est); Gene3D 3.40.50.1820
  (alpha/beta hydrolase); PROSITE PS00120 (LIPASE_SER).
- ESTHER classification: yeast-yj77, family "Lipase_3".
- PANTHER: PTHR46640 / PTHR46640:SF3 "LIPASE LIH1-RELATED".
- Catalytic triad (by similarity to O59952, a fungal/Rhizomucor-type lipase):
  - ACT_SITE Ser181 (Nucleophile) — verified in sequence: sits in the canonical pentapeptide
    **GHSLG** (residues 179–183; I recomputed from the UniProt sequence: positions 179–183 =
    G-H-S181-L-G). This is the classic filamentous-fungal lipase / α/β-hydrolase catalytic
    serine motif GHS[LFM]G.
  - ACT_SITE Asp253 (charge relay) — verified: context HTG-**D253**-YIP.
  - ACT_SITE His315 (charge relay) — verified: context VYE-**H315**-RAY.
  - => The catalytic triad Ser-Asp-His is INTACT. LIH1 is NOT an obvious pseudoenzyme
    (catalytic residues are conserved), so a fold-level catalytic annotation is defensible;
    but "intact triad" is necessary, not sufficient, for TAG-lipase activity.
- Sequence version 2 (2011) revised residues 14 and 66 vs the original 1996 chromosome-X
  sequence (CONFLICTs at 14 P->L and 66 G->P in Ref.1) — a common early-yeast-genome artifact.

## Literature (verified against cached full text)

1. PMID:26580812 — Meunchan et al. 2015, PLoS ONE, "Comprehensive Analysis of a Yeast Lipase
   Family in the Yarrowia Clade." **This is the sole source cited by UniProt for the LIH1
   name and the EC=3.1.1.3 designation, and both are ECO:0000303 / ECO:0000305 (author
   statement / curator inference), NOT experimental.**
   - The paper is about the *Yarrowia* clade LIP gene family. S. cerevisiae is only mentioned
     as an outgroup context. The ONLY statement about LIH1 (verbatim):
     > "A putative lipase was also identified in Sacharomycetaceae. This putative lipase in
     > Saccharomyces cerevisiae, called Lih1 and encoded by YJR107W, shares 26% identity and
     > 44% similarity with YlLip2, its closest relative in Y. lipolytica. Lih1 and its
     > counterparts in other Hemiascomycetes may derive from a common LIP ancestor."
   - i.e. LIH1 is named by homology to Y. lipolytica Lip2 (only 26% identity). It was NOT
     expressed, assayed, or biochemically characterized in this study.
   - The catalytic-triad / GHS[LFM]G statement in the paper describes the *Yarrowia* LIP
     family proteins collectively (verbatim: "All the proteins in this region harbored the
     conserved serine, aspartic acid, and histidine catalytic triad characteristic of the
     α/β hydrolase with the catalytic nucleophile serine located in the highly conserved
     pentapeptide GHS[LFM]G ... This finding confirms that all of these genes encode
     lipases.") — this is a family/fold-level bioinformatic argument, consistent with LIH1
     retaining the triad, but does not itself test LIH1.

2. PMID:8641269 — Galibert et al. 1996, EMBO J — complete sequence of chromosome X. Genomic
   sequencing only; establishes the ORF (YJR107W). Not functional. Abstract-only cached.

3. PMID:24374639 — Engel et al. 2014, G3 — S. cerevisiae reference genome reannotation.
   Source of the 2011 sequence revision. Not functional.

## GO annotation assessment (GOA, LIH1-goa.tsv)

- GO:0004806 triacylglycerol lipase activity | IEA | GO_REF:0000120 (RHEA:12044 | EC:3.1.1.3).
  This is an electronic EC->GO mapping. The EC number itself (3.1.1.3) is a curator inference
  (ECO:0000305) from homology, not measured. Asserting the *specific TAG substrate* is an
  over-annotation for a protein with only 26% identity to the nearest characterized lipase and
  no biochemical data. The intact triad supports at most a general fold-level activity.
  -> MODIFY / generalize toward lipase activity (GO:0016298) or carboxylic ester hydrolase
     activity (GO:0052689). Keep non-core.
- GO:0006629 lipid metabolic process | IEA | GO_REF:0000002 (InterPro:IPR002921). Broad,
  domain-based; consistent with the fold. Defensible as a general, non-core BP.
- GO:0005575 cellular_component (root) | ND | GO_REF:0000015. Root/ND placeholder — no CC
  known. Keep as-is (accurately records "unknown location").
- GO:0008150 biological_process (root) | ND | GO_REF:0000015. Root/ND placeholder — no BP
  known experimentally. Keep as-is.

## GO term hierarchy (verified via OLS)

- GO:0052689 carboxylic ester hydrolase activity — "Catalysis of the hydrolysis of a
  carboxylic ester bond." (most general; matches AB hydrolase fold)
- GO:0016298 lipase activity — "Catalysis of the hydrolysis of a lipid."
- GO:0004806 triacylglycerol lipase activity — "a triacylglycerol + H2O = a diacylglycerol +
  a fatty acid + H+." (specific substrate; the EC-mapped IEA term)

## KNOWN vs NOT-known

KNOWN (bioinformatic / sequence-level):
- Belongs to the fungal Lipase_3 / AB-hydrolase family (multiple orthogonal signatures).
- Retains an intact, canonically-positioned Ser181–Asp253–His315 catalytic triad and the
  GHSLG nucleophile-elbow pentapeptide.
- Encoded on chr X, YJR107W; 328 aa; expressed at the protein level (peptide evidence).
- Non-essential (no CRISPR-screen hits; a viable deletion is expected for a lone S. cerevisiae
  lipase homolog).

NOT known (the real gaps):
- Actual catalytic activity of the LIH1 protein (never assayed).
- Natural / physiological substrate (TAG? di-/mono-acylglycerol? other ester? unknown).
- Whether it is catalytically active at all in vivo, or a vestigial homolog.
- Subcellular localization (secreted? intracellular? membrane-associated? unknown).
- Biological process / physiological role (lipid catabolism is a fold-level guess, unverified).
- Loss-of-function phenotype / conditions under which it matters.
- Regulation / expression conditions.
