# AFAP1L2: paired human–horse review notes

## Biological evidence

The primary XB130 study establishes a signaling adaptor that activates Src and links EGF to downstream signaling and gene expression. It reports interaction motifs, kinase activation, knockdown effects and transcriptional reporters. The evidence supports specific kinase/adaptor roles rather than generic binding.

- [PMID:17412687: XB130, a novel adaptor protein for signal transduction.](https://pubmed.ncbi.nlm.nih.gov/17412687/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The full human818-residue sequence aligns to the horse850-residue model at88.6% identity. This supports the conserved adaptor mechanism and broad downstream cytokine/signaling claims. The cached abstract establishes IL-8; the separate DOI-linked full-paper excerpt documents the IL-6 result. Neither the Edison narrative nor ARBA is used as independent validation.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/AFAP1L2/AFAP1L2-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

The source excerpt file preserves the IL-6 sentence and full-paper URL because the publication cache is abstract-only. Consider tissue/condition-specific assays before treating cytokine phenotypes as universal horse physiology.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research-falcon HORSE AFAP1L2 --fallback perplexity-lite` failed (falcon "Failed to authenticate"; perplexity-lite HTTP 401 insufficient quota). No deep-research file was created. Literature was gathered by a PubMed search (XB130/AFAP1L2 in title/abstract) and the key primary papers were cached with `just fetch-pmid`: PMID:19060924 (abstract), PMID:21084565 (abstract), PMID:22496359 (abstract), PMID:27462298 (full text), PMID:34470464 (full text), PMID:26446840 (full text), alongside the existing PMID:17412687 (abstract).

### Identity / gene model

New script `AFAP1L2-bioinformatics/compare_sequences_rereview.py` (outputs `RESULTS-rereview.md`, `results-rereview.json`; earlier RESULTS.md left untouched). UniProt has ten unreviewed horse AFAP1L2 TrEMBL entries (748-943 aa), all PTHR14338:SF4, each an Ensembl transcript model of one gene (ENSECAG00000014979 for this one); none is reviewed, so there is no reviewed canonical horse product to fall back to. A0A9L0RQI4 (850 aa, ENSECAT00000130227.1) is one alternative transcript model, not a fragment: all 818 human Q8N4X5 residues pair (88.5% identity) with no human residue missing. Differences from human canonical: (1) an alternative N-terminus, MRSTMWVLLANTATSN... in place of human MERYK..., adding 11 residues (shared with model A0A3Q2GZU2, consistent with an alternative first exon); (2) a 20-residue insertion (DEQTEVQRGEGTCPRSHSKE) after human position 652, at the start of the coiled coil, absent from human canonical, mouse Q5DTU0 and most other horse models (a likely cassette exon). All characterized features are retained: Tyr54 p85-binding phosphosite (horse Tyr65), PH1 95/97, PH2 93/95 identical, coiled coil, and the C-terminal 63-residue actin/lamellipodium-targeting segment (57/63 identical; terminal AKEWEKKGAS identical). Whether the insertion changes multimerization is unknown.

### Evolutionary grounding

A0A9L0RQI4 is in PANTHER PTHR14338:SF4 (AFAP1L2), the same subfamily as human Q8N4X5, mouse Q5DTU0 and rat PI3KAP; AFAP1 and AFAP1L1 are separate subfamilies (PAINT node PTN002682780 carries actin filament/adaptor terms for the AFAP1 branch, which were not transferred). PAINT places GO:0030296 protein tyrosine kinase activator activity plus four process terms (inflammatory response, regulation of mitotic cell cycle, positive regulation of EGFR signalling, positive regulation of DNA-templated transcription) at PTN002682769 (taxon 117571), and cytosol at PTN001023816 (taxon 33511), all seeded by human Q8N4X5. QuickGO shows rat and mouse members carrying these IBAs; the horse benchmark model carries none, consistent with it not being the PANTHER tree leaf for the horse gene. The family review `interpro/panther/PTHR14338/PTHR14338-review.yaml` lists A0A9L0RQI4 as an SF4 representative: no disagreement on subfamily placement.

### Changes vs previous version

- GO:0005737 cytoplasm (IEA): ACCEPT kept; support rewritten to cite the human experimental location (UniProt ECO:0000269 from PMID:17412687), PMID:21084565 [“XB130 is a newly described cytosolic adaptor protein and tyrosine kinase substrate”] and SF4 membership, replacing the c-Src activation quote that did not address location.
- NEW GO:0030296 protein tyrosine kinase activator activity (IBA, PTN002682769) and NEW GO:0005829 cytosol (IBA, PTN001023816): the PAINT-inherited terms this model missed.
- NEW GO:0036312 phosphatidylinositol 3-kinase regulatory subunit binding (ISS) [PMID:19060924 “We identified tyrosine 54 of XB130 as the major target of RET/PTC-mediated phosphorylation and a critical binding site for the SH2 domains of p85alpha.”; rat PMID:22496359 “a mutant Y72F incapable of binding to p85 PI3K did not show this response”]. Not an annotation in any species yet, so not a PAINT omission.
- NEW GO:0051015 actin filament binding (ISS) [PMID:27462298 “PI3KAP/XB130 bound to actin filaments through amino acid residues 830–840”] and NEW GO:0030027 lamellipodium (ISS) [PMID:21084565 “In stimulated cells, XB130 localized to the lamellipodial F-actin meshwork.”].
- Not added: the four PAINT process terms. Their human basis is siRNA/overexpression readouts (IL-8/IL-6, cell-cycle profiles, EGF-Akt, SRE/AP-1 reporters) and inflammatory response is an organismal-level outcome; per the NEW-bar rules they are not proposed for horse. Knockout thyroid phenotypes (PMID:34470464) are context only.
- Description and core functions rewritten: (1) Src activator in cytosol; (2) phosphotyrosine-dependent p85 PI3K adaptor; (3) actin filament binding/crosslinking at lamellipodia.

### Relative

Human AFAP1L2 (Q8N4X5), ortholog in the same PANTHER subfamily and the PAINT seed for PTN002682769; `genes/human/AFAP1L2/AFAP1L2-ai-review.yaml` exists with all 18 GOA rows reviewed. Suggestion for that review (not edited here): it could add the p85-binding and actin filament binding MFs supported by PMID:19060924 and PMID:27462298. No module includes AFAP1L2; nearest context modules are `modules/integrin_fak_src_signaling.yaml` and `modules/pi3k_akt_mtor.yaml`.

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The HORSE40 re-review (PR #5303) proposed NEW IBA rows for GO:0030296 protein tyrosine kinase activator
activity and GO:0005829 cytosol on A0A9L0RQI4, because GOA did not propagate the PAINT IBAs to this
transcript model. QuickGO shows that another horse AFAP1L2 product, A0A3Q2HBW2 (943 aa), carries both
terms by IBA and IEA. GOA propagates gene-level annotations to one representative product per gene, so
these rows filled a convention rather than a curation gap. They were withdrawn under the rule applied
across the ProtNLM2 re-review cohorts. The core functions keep their own PAINT and literature support,
and the gene-level function is unchanged.

## 2026-10-23 — Which form of the representative-product rule applies here (PR #5310 review)

Two forms of the rule are in use across the ProtNLM2 re-review cohorts:

1. Withdraw a NEW row when GOA already carries the same term on another product of the same gene. Applied
   here to GO:0030296 and GO:0005829, which GOA carries on A0A3Q2HBW2.
2. Move a gene-level NEW proposal to a reviewed representative product. Applied to DYNLT2B, where the
   canonical product `DYNLT2B__A0A9L0S9P8` has its own review folder.

The three remaining NEW rows here are GO:0036312 PI3K regulatory subunit binding, GO:0051015 actin filament
binding and GO:0030027 lamellipodium. They are ISS transfers from human and rodent AFAP1L2 and appear in no
species' GOA, so form 1 does not apply. Form 2 would require a review of A0A3Q2HBW2, which does not exist in
the repo. The proposals therefore stay on this benchmark accession until a representative-product review
is created. They describe the horse gene, not something specific to this transcript model.

Core functions keep GO:0030296 and GO:0005829 with their own PAINT and literature support. This is the
convention accepted in PRs #5305 (MESK2) and #5308 (FTSH12): a core function may name a gene-level term
that GOA carries on another product, provided its supported_by does not rest on the withdrawn row.
