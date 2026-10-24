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
