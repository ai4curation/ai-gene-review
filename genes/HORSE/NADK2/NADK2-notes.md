# NADK2 (horse, Equus caballus) — notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Target: UniProtKB A0A3Q2GYY5 (TrEMBL, unreviewed, 560 aa; Ensembl
ENSECAT00000031483.2 / ENSECAG00000019847; VGNC:20544 NADK2). Folder created
with `just fetch-gene HORSE A0A3Q2GYY5 --alias NADK2`; stub id confirmed as
A0A3Q2GYY5. No previous review existed. ProtNLM2 outputs were not consulted.

### Deep research

`just deep-research-falcon HORSE NADK2 --fallback perplexity-lite` failed:
falcon "Exception: Failed to authenticate"; perplexity-lite fallback HTTP 401
(insufficient quota). No deep-research file was produced. The review relies on
the cached primary literature on human NADK2 (PMID:23212377 full text,
PMID:24847004 abstract), the completed human review
(genes/human/NADK2/NADK2-ai-review.yaml), PAINT data for PTHR13158 and my own
sequence analysis. There is no horse-specific experimental literature on NADK2.

### Identity / gene model

See NADK2-bioinformatics/RESULTS.md. A0A3Q2GYY5 is one of four horse NADK2
TrEMBL models (A0A3Q2GYY5 560 aa, F7DCV0 538 aa, A0A3Q2H586 411 aa,
A0A3Q2GS26 510 aa); there is no reviewed horse entry. Against human Q4G0N4
(442 aa) it is 96.8% identical over the aligned region, with:
- a 96-aa N-terminal extension (residues 1..96) absent from human and mouse,
  overlapping the MobiDB-lite disordered regions; the human-equivalent start
  Met is horse M97. Probably an upstream in-frame ATG in the gene model; if real
  it would bury the mitochondrial transit peptide, so I do not treat it as the
  native N-terminus.
- a 22-aa internal insertion after human position 287 that matches the segment
  present in canonical mouse NADK2 Q8C5H8, i.e. a conserved alternative exon.
- all catalytic motifs conserved: GGDG (horse 253), NE/D (horse 370), and the
  NADK2-specific Ser/Lys/Trp NAD-site substitutions (human S306/K317/W319 →
  horse S424/K435/W437) [PMID:23212377 "In the structure of the C5orf33
  protein, although the GGDG motif and NE/D short motif were completely
  conserved, the Asp, Thr and Tyr residues were not, corresponding instead to
  Ser-306, Lys-317 and Trp-319"].
Not a fragment; an alternative gene model of the full-length enzyme.

### Evolutionary grounding

UniProt places A0A3Q2GYY5 in PANTHER PTHR13158:SF5 "NAD KINASE 2,
MITOCHONDRIAL", the same subfamily as human Q4G0N4 and mouse Q8C5H8 (both carry
PTHR13158:SF5). PAINT (interpro/panther/PTHR13158/PTHR13158-paint.tsv):
- PTN004406956 GO:0003951 NAD+ kinase activity, seeds MGI:1915896 + Q4G0N4
- PTN004406956 GO:0019674 NAD+ metabolic process, seed Q4G0N4
- PTN000994636 GO:0005739 mitochondrion, seeds MGI:1915896 + Q4G0N4, taxon:2759
The PAINT curators propagated catalytic activity, NAD+ metabolism and
mitochondrion; they did not propagate homodimerization. Horse is in the
subfamily, so the catalytic and localisation transfers are well grounded.

Human NADK2 experimental basis: purified protein forms NADP+ from NAD+ using ATP
or polyphosphate [PMID:23212377 "we detected the formation of NADP+ from NAD+ and
of ADP from ATP"]; localised to mitochondria by fractionation [PMID:23212377
"C5orf33 protein was localized in the mitochondrial fraction but not in the
cytosolic fraction"]; patient loss of function lowers mitochondrial NADP(H)
[PMID:24847004 "NADK2 encodes the mitochondrial NAD kinase, which is crucial for
NADP biosynthesis evidenced by decreased mitochondrial NADP(H) levels in patient
fibroblasts"].

### Decisions

- NAD+ kinase activity (IBA, IEA): ACCEPT, core.
- mitochondrion (IBA, IEA): ACCEPT; mitochondrial matrix (IEA ARBA): ACCEPT
  (soluble enzyme with a cleavable transit peptide; Reactome places human NADK2
  reaction in the matrix).
- NAD+ metabolic process (IBA, IEA): MODIFY to NADP+ biosynthetic process
  GO:0006741 (an is_a descendant per OLS hierarchicalAncestors); the enzyme
  itself catalyses the NAD+ → NADP+ step.
- protein homodimerization activity (IEA, Ensembl Compara from human): KEEP_AS_NON_CORE;
  the human SUBUNIT line is a curator inference (ECO:0000305) from PMID:23212377,
  and PAINT did not propagate it.
- No downstream process terms (DECR1-dependent PUFA oxidation, lysine
  degradation, proline biosynthesis) added: those steps are performed by other
  NADPH-dependent enzymes; NADK2 supplies a cofactor.

### Relative

Closest characterised relative by phylogeny: human NADK2 Q4G0N4 (same
PTHR13158:SF5, PAINT seed). Complete review exists at
genes/human/NADK2/NADK2-ai-review.yaml (no PENDING actions). Mouse Nadk2
(Q8C5H8, MGI:1915896) is the other PAINT seed; no mouse review in repo.

Module: modules/nadp_synthesis_and_nr_salvage.yaml (NADP+ synthesis by NADK/NADK2).
