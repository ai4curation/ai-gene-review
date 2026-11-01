# fabY (PA5174, Q9HU15) notes

Deep research (`just deep-research`) was not available in this session (no provider API keys),
so no `-deep-research-<provider>.md` file exists. Literature was researched directly: the
cached publications, PubMed searches ("FabY Pseudomonas aeruginosa PA5174", "FabY
beta-ketoacyl synthase Pseudomonas"; only PMID:22753059 and PMID:22753057 are returned), and
the PMC full text of PMID:22753059, which was upgraded in the publications cache from abstract
to full text (PMC3457228) for this review. The GONUTS wiki page
(https://gowiki.tamu.edu/wiki/index.php/PMID:22753059) returned only a maintenance notice
("site temporarily offline"), so the CACAO students' own evidence notes could not be read.

## Identity

- 634-aa KASI/II-family (KS3 domain) condensing enzyme; active-site Cys281 (UniProt FT).
- FabY class defined by Yuan et al. 2012: "We propose distinguishing β-ketoacyl-ACP synthases
  with KASI/II domains and a preference for short-chain acyl-CoA acceptor substrates as the new
  FabY class of condensing enzymes" [PMID:22753059].
- Restricted distribution: "FabY is also more narrowly distributed at the species level"
  [PMID:22753059] (P. aeruginosa, P. fulva, P. mendocina, Azotobacter vinelandii).
- Crystal structure 4CW4 (1.35 A), homodimer; FabY is a "noncanonical fatty acid biosynthesis
  starter enzyme" whose insertions resemble fungal FAS scaffolding [PMID:25456814, abstract only].

## Function (PMID:22753059, full text)

- Genetic: P. aeruginosa cosmids rescuing a FabH-depleted E. coli all began just upstream of
  PA5174; "PA5174 is thus by itself sufficient to complement FabH and restore initiation of FAS";
  plasmid PA5174 allowed deletion of E. coli fabH: "Growth analysis confirmed complete
  fabH-PA5174 cross complementation" (Fig. 3).
- Deleting all four KASIII homologs (PA3333, PA3286, PqsC, PqsD) had no growth phenotype (Fig. 2C).
- ΔPA5174: "doubling time increased from 19 to 62 min in the absence of PA5174" (Fig. 4A);
  [3H]acetate labeling: "the larger decrease in the rate of label incorporation for FAS in
  comparison to RNA indicates particular attenuation specific to FAS" (Fig. 4B).
- Enzymology (Fig. 8): "the specific activities of PA5174 and E. coli FabH with malonyl-ACP and
  acetyl-CoA as substrates were 13.4 and 7.4 pmol/min/ng under the same assay conditions";
  product reduced by FabG/FabA/FabI to butyryl-ACP; "The lack of additional bands indicates that
  PA5174 cannot efficiently carry out the next round of condensation for chain elongation using
  acyl-ACP as a substrate"; "PA5174 utilized short-chain acyl-CoA as substrates, including
  acetyl-CoA, butyryl-CoA, and hexanoyl-CoA, but did not use any of the longer-chain acyl-CoA
  substrates".
- Downstream phenotypes of ΔPA5174 (all consequences of reduced acyl-ACP supply):
  - rhl QS: "The amount of acyl-HSL in the ΔPA5174 strain was nearly undetectable in comparison
    to that in the wild type" (Fig. 5A, TLC + C. violaceum overlay); rhamnolipid and swarming loss.
  - las: "The ΔPA5174 mutant apparently can synthesize 3-oxo-acyl-HSL to wild-type levels in LB
    liquid culture after 24 h of incubation despite the FAS defect" (Fig. 6A); elastase lost.
  - PQS: "The PQS level was reduced to a trace in the supernatant extract when PA5174 was
    deleted" (Fig. 6C); pyocyanin lost.
  - Siderophore: CAS plate, "the ΔPA5174 strain did not produce a zone, indicating a lack of
    relative siderophore production" (Fig. 7). Authors' rationale: "Since pyoverdine is
    coregulated by QS systems (79) and is assembled on a myristate fatty acid residue (21, 34)".
  - Authors' interpretation: "The progression of QS in the ΔFabY mutant is likely delayed by the
    lack of fatty acid precursors".

## Bypass (PMID:22753057, abstract)

Exogenous ≥C8 fatty acids rescue ΔfabY via the KASIII enzyme PA3286, which condenses C8-CoA with
malonyl-ACP; "PA3286 in P. aeruginosa PAO1 intercepts C(8)-CoA by condensation with malonyl-ACP"
[PMID:22753057].

## Lipid A (PMID:24145528, full text)

- "The majority of lipid A species in the Δ fabY mutant lacked a single secondary lauroyl group,
  resulting in hypoacylated lipid A." [PMID:24145528]
- Mechanism proposed is indirect precursor limitation: "It is likely that decreased flux of the
  FAS pathway in the Δ fabY strain limits cellular pools of the C 12:0 -ACP donor available for
  the secondary acyl transferases." and the authors "cannot rule out differences in gene
  regulation" [PMID:24145528]. Lipid A acyltransferases (PA0011, PA3242 LpxL-like) perform the step.

## CACAO assessment summary

| Term | Evidence | Verdict |
|---|---|---|
| GO:0033818 KASIII activity | IDA PMID:22753059 | Matches Fig. 8; ACCEPT |
| GO:0006633 FA biosynthesis | IMP PMID:22753059 | Matches Fig. 4; ACCEPT |
| GO:0009372 quorum sensing | IMP PMID:22753059 | Phenotype-as-process (precursor supply); over-annotated |
| GO:0019290 siderophore biosynthesis | IMP PMID:22753059 | Phenotype-as-process, CAS secretion plate only; over-annotated |
| GO:0009245 lipid A biosynthesis | IMP PMID:24145528 | Phenotype-as-process (acyl-ACP pool limitation); over-annotated |

Pattern: one well-characterised metabolic enzyme whose knockout has pleiotropic downstream
metabolite phenotypes; each downstream product pathway became a BP annotation. This is the
"phenotype read as process" failure, in a metabolic-precursor variant (necessity via substrate
supply, not participation).
