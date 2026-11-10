# darA receptor review notes

## 2026-11-04 — cyclic di-AMP receptor audit

The 2024 suppressor study (PMID:38832794) updates physiology but does not establish a direct transport/enzyme partner. No NEW process term is inferred from necessity or compensatory mutations. Cytoplasm EXP and IEA actions are consistent. The existing experimental citation PMID:31061098 was also retained.

Falcon deep research was attempted using `just deep-research-falcon BACSU darA` and failed with HTTP 403 authentication failure. This is manual primary-source research, not a provider-generated report. The original machine annotation payloads and raw UniProt/GOA files are retained. No NEW annotation rows were added in the initial pass; the follow-up below records the final recommendation.

- [PMID:25433025](https://pubmed.ncbi.nlm.nih.gov/25433025/): DarA forms a trimer with three cyclic di-AMP binding pockets. "DarA is a homotrimer that binds three molecules of c-di-AMP, each in a pocket located between two subunits."
- [PMID:38832794](https://pubmed.ncbi.nlm.nih.gov/38832794/): Suppressor phenotypes link DarA to osmotic, potassium and amino-acid homeostasis without identifying a direct molecular target. "Suppressor screens with darA mutants reveal compensatory mechanisms involving the accumulation of osmoprotectants, particularly potassium and citrulline."

Module membership: `MODULE:bacterial_c_di_amp_signaling`, receptor arm. No unsupported top-level association slot is used.

## 2026-11-04 — PR #5997 review follow-up

Added NEW GO:0180001 (IDA; PMID:25433025) for direct cyclic di-AMP recognition. Removed the duplicated identical UniProt localization support entry from the two cytoplasm reviews; both original machine rows remain intact and ACCEPT. The 2024 suppressor phenotypes still do not establish a direct downstream target.
