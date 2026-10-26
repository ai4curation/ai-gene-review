# FY (At5g13480, UniProt Q6NLV4) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: Q6NLV4 FY_ARATH, At5g13480.
- Deep research (falcon) failed (HTTP 429).
- FY = Pfs2p/WDR33 ortholog [PMID:12809608 "FY belongs to a highly conserved group of eukaryotic proteins represented in Saccharomyces cerevisiae by the RNA 3' end-processing factor, Pfs2p."]
- Stable CPSF association; transient FCA [PMID:19439664 "AtCPSF100 and AtCPSF160, but not FCA, are stably associated with FY in vivo and form a range of different-sized complexes."]
- Null alleles embryo lethal; PPLPP motifs bind FCA [PMID:16033802 "The FY C-terminal domain binds FCA and in vitro assays demonstrate a requirement for both C-terminal FY-PPLPP repeats during this interaction."]
- SDG26 links FY to FLD complex [PMID:32541063 "SDG26 interacts with the RNA 3' processing factor FY (WDR33), thus linking activities for proximal polyadenylation of the antisense transcripts to FLD/LD/SDG26-associated H3K4 demethylation."]

## Decisions
- CPSF complex (IBA) and mRNA 3'-end processing (IEA) accepted as core.
- Six bare protein-binding rows removed (CPSF membership captured by GO:0005847).
- CRL4 complex (DDB1 interaction of DWD protein) kept as non-core: no functional evidence.
- NEW: mRNA alternative polyadenylation (GO:0110104).
- No MF assigned in core_functions: direct RNA (PAS) binding by plant FY has not been demonstrated.


## 2026-10-26 autonomous-flowering RNA-factor audit

All rows were reviewed, preserving original terms, evidence, references, qualifiers, NOT flags and supporting entities. Falcon/fallback research and gene-publication retrieval ran concurrently under the parent workflow; provider attempts failed and logs remain under `.cache/module-audit-logs/autonomous-flowering-fetch/`. No provider report was fabricated. Primary source caches and curated UniProt evidence were inspected independently. Annotation-reviewer consultation with the chromatin-panel reviewer agreed that nuclear predominance is not organelle exclusion, broad RNP membership does not require PABP identity, and FPA termination reinterpretations are locus-specific.

The authoritative PAINT inspection is reproducible in `genes/ARATH/FCA/FCA-bioinformatics/`. It uses exact existing PTNs and is not a reconstructed family phylogeny. The failed full-family download was not used; only its incomplete .part file was removed after disk exhaustion. Current source retrieval is recorded honestly: PMID18223036 refreshed complete; PMID19439664 cache abstract-only but full web text inspected; 16820865 and19561057 recovered normally; optional16753815 fetch returned429 and was not used to support a new claim.

- Refreshed PMID:18223036 contains complete Results/Methods. Fig4A explicitly retrieves FY with DDB1b together with CUL4. Retain CRL4-complex association as contextual non-core; Fig4B CUL4 bait and AKIN10 degradation are PRL1 experiments and do not demonstrate FY substrate selection.
- PMID:19439664 cache remains abstract-only after normal PMC fallbacks. Complete online PMC text inspected at https://pmc.ncbi.nlm.nih.gov/articles/PMC2689023/ (2026-10-26). Native stable FY/CPSF100/CPSF160 assemblies are supported; FCA was not stably co-purified. Do not claim the cached file contains the complete paper.
- Exact PTN000519834 CPSF IBD independently matches native complex purification. No direct plant FY RNA-binding/nuclease activity is added from WDR33 analogy. Existing NEW APA retained.
