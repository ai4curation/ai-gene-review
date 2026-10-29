# LAT (human, O43561) review notes

## Provenance / process

- 2026-09-30: `just deep-research-falcon human LAT --fallback perplexity-lite` exited with code 1 and
  produced no deep-research file (in this environment falcon runs were timing out at 600 s and the
  perplexity-lite fallback reported "Provider 'perplexity' not available"). The review was done
  without a deep-research file, from the UniProt record, the GOA-cited publications
  (`just fetch-gene-pmids`) and additional primary papers fetched with `just fetch-pmid`
  (PMIDs found by PubMed esearch: 10843385, 10567557, 10204488, 27242165; plus mouse source papers
  22561606, 23793062, 16002666 traced via QuickGO for ISS/IEA/IBA rows).
- Most GOA-cited LAT papers are cached abstract-only; quotes are from abstracts.

## Biology summary

- Palmitoylated (C26/C29) single-pass type III transmembrane adaptor, no catalytic domain
  [PMID:9729044 "palmitoylation at C26 and C29 is essential for efficient partitioning into GEMs"].
- Phosphorylated by ZAP70/SYK (also reported LCK, ITK) on Y132, Y171, Y191, Y226
  [PMID:9489702 "phosphorylated by ZAP-70/Syk protein tyrosine kinases leading to recruitment of multiple signaling molecules"].
- Docking map: Y132 -> PLCG1; Y171/Y191/Y226 -> GRB2; Y171/Y191 -> GADS
  [PMID:10811803]; Y171/Y226 -> VAV1 [PMID:12186560].
- Forms TCR signalosome / microclusters; phospho-LAT + GRB2-SOS1 phase separate into liquid-like
  condensates [PMID:27056844 "pLAT microclusters are liquid-like, phase-separated structures"].
- Also scaffold in FcepsilonRI mast cell signaling [PMID:10843385] and platelet GPVI signaling
  [PMID:10567557].
- Mouse KO: block at DN stage [PMID:10204488]; human LOF: combined immunodeficiency + autoimmunity
  (IMD52) [PMID:27242165]. TRAF6 K63-ubiquitinates LAT K88 [PMID:23514740].

## Curation decisions (key points)

- Core MF: GO:0030159 signaling receptor complex adaptor activity (IBA + IDA), with parent
  GO:0035591 accepted. NEW GO:0140693 molecular condensate scaffold activity (IDA, PMID:27056844);
  comparator: condensate partners SOS1 and NCK1 carry GO:0140693 by IDA.
- 17 `protein binding` IPI rows: MODIFY -> GO:0030159 when the paper maps LAT phosphotyrosine
  docking of an SH2 effector (PLCG1, GRB2, PIK3R1, VAV1); REMOVE for kinase/phosphatase-substrate
  pairs (ZAP70, LCK, PTPN1), high-throughput screens (EGFR MaMTH, EGFR proteomics, SGTA HuRI), a
  LAT-peptide control (SLAM paper) and the NTAL/LAB paper.
- COP9 signalosome (IEA+ISS from mouse Lat, UniProt IDA PMID:22561606): the source Tespa1 paper
  describes the *TCR signalosome*; MODIFY -> GO:0036398. Likely a signalosome term-selection error
  at source; raised as a suggested question.
- Cell-cell junction (IEA from mouse, PMID:23793062 Rltpr/CD28 at immunological synapse): MODIFY ->
  immunological synapse.
- Integrin-mediated signaling pathway (IDA PMID:15100278): paper shows TCR inside-out activation of
  beta1 integrins -> MODIFY to GO:0033625 positive regulation of integrin activation.
- Inflammatory response IBA: seeded by mouse LatY136F phenotype -> MARK_AS_OVER_ANNOTATED
  (necessity/phenotype, not participation).
- Positive regulation of protein kinase activity (IEP, RAG repression microarray paper) ->
  MARK_AS_OVER_ANNOTATED.
- NEW process terms: Fc-epsilon receptor signaling pathway (PMID:10843385) and
  collagen-activated signaling pathway (PMID:10567557); LAT does work in these pathways as the
  scaffold (same role as in TCR signaling), passing the participation test.

## Deep research integration (falcon)

2026-10-01. `LAT-deep-research-falcon.md` became available after the review was completed. It was read
in full and treated as LLM-generated secondary literature. Its sources are two reviews (Shah 2021
Signal Transduct Target Ther; Fernandez-Aguilar 2023 Biology), one regional review (Moskalev 2025),
one optics review (Lee 2024) and three preprints (Rubin 2024 bioRxiv on pathway balance; Rainwater 2025
bioRxiv on DNA-PKcs; Saez bioRxiv on trafficking, since published as PMID:33572370).

Claim tally (about 25 substantive claims): 18 confirm the review, 3 add something new, 0 conflict with
the review's decisions, 4 not relevant or unsupported. One claim exposed an error in the review itself
(see below).

### Claims adopted
- **Tyrosine numbering (fixes a review error).** The report gives LAT as ~233 aa with Y132/Y171/Y191/Y226.
  Checking the UniProt sequence shows these numbers belong to the short isoform O43561-2 (233 aa, missing
  114-142). In the canonical long isoform O43561-1 (262 aa) the same residues are Y161/Y200/Y220/Y255
  (UniProt MOD_RES 161/200/220/255). The previous description said "in the long isoform", which was
  wrong. The description now gives both numberings.
- **Vesicular LAT pool and Golgi/TGN trafficking (new).** The report cited the Saez bioRxiv preprint.
  I verified this against peer-reviewed primary papers: PMID:29789604 [surface LAT phosphorylated first,
  vesicular pool recruited later], PMID:23666293 [VAMP7 required for recruitment of LAT vesicles;
  abstract-only], PMID:29440364 [Rab6/syntaxin-16 retrograde transport to Golgi-TGN], and
  PMID:33572370 [the Saez study as published in Cells 2021: "more abundantly in intracellular
  compartments"]. Changes: one description sentence added; the four papers added to `references` with
  findings; PMID:29789604 added to supported_by for core function 1.
- **Report quote as core-function context.** The report's scaffold sentence was added to
  core function 1 supported_by.

### Claims confirming the review (no change)
These claims agree with the review: non-catalytic phospho-dependent scaffold; ZAP70 phosphorylation;
docking sites (Y132 to PLCG1; GRB2/GADS at Y171/Y191/Y226; GRB2-SOS1 to Ras); C26/C29 palmitoylation
and raft targeting; immunological synapse microclusters; TCR signalosome; Ca2+/NFAT, Ras-MAPK/AP-1
outputs; LAT-null J.LAT phenotype; mouse KO thymic block; human SCID/CID with autoimmunity (IMD52).
The review's GO:0030159, GO:0035591 and GO:0140693 MF choices, and its process terms, are unaffected.
The report gives no evidence that challenges the NEW Fc-epsilon receptor or collagen-activated
signaling rows, so these stay consistent with the matching LCP2 rows.

### Claims not acted on
- **Y110 as a GRB2 site; GRAP binding.** This is plausible, but the source is the Rubin 2024 preprint
  and an AlphaFold model. It does not change any term.
- **NF-kappaB via PLCG1-DAG-PKCtheta.** LAT acts upstream as scaffold and the DAG/PKCtheta step is
  performed by other gene products. No NEW term is warranted (CLAUDE.md participation test).
- **Rubin 2024 "pathway balance" and intrinsically disordered tail with >40% functional regions.**
  These come from a preprint and are descriptive; no annotation consequence.
- **DNA-PKcs phosphorylation of S224/S241 (Rainwater 2025).** The only source is one bioRxiv
  preprint, which PubMed esearch did not find as a published paper. I raised it as a suggested
  question. UniProt lists S224/S241 (canonical numbering) as high-throughput phosphoserines, but
  this does not show which kinase acts there.
- **Transmembrane residues L11-G12-L13 "critical for surface trafficking".** Preprint-only; not used.

### Questions and experiments added
- Should LAT carry a vesicle/TGN cellular component annotation? Does vesicular LAT act as a scaffold
  itself or mainly as a reservoir? A matching experiment was added: plasma-membrane-restricted vs
  vesicle-retained LAT variants.
- Is the DNA-PKcs S224/S241 phosphorylation reproducible, and which isoform numbering does it use?

### Report errors detected
- It describes LAT as "approximately 233-amino-acid" without saying this is isoform 2. The
  UniProt canonical isoform is 262 aa.
- It credits "Yamane et al. (2026)" on SLP-76/PLCgamma1 fine-tuning to `shah2021tcellreceptor pages
  7-8`, a 2021 review that cannot report a 2026 study. This is a misattribution; I did not use it.
- It cites the Saez trafficking work only as a bioRxiv preprint, although it was published
  (PMID:33572370).
- It leans heavily on preprints (Rubin, Rainwater) for "recent developments", and these are presented
  alongside peer-reviewed findings.
