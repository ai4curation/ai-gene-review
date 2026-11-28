# MDM2 (Q00987) review notes

- `just fetch-gene human MDM2` seeded 410 existing GOA annotations.
  The largest cluster is 204 `GO:0005515 protein binding` rows from
  interaction curation; these need to remain as distinct rows but can share
  the same policy decision on bare protein binding.
- PTHR46858 contains one reviewed human Swiss-Prot member in this checkout:
  MDM2 in `PTHR46858:SF13`.
- `just fetch-panther-paint PTHR46858` returned 16 node-level PAINT rows.
  The two IRD rows in the local PAINT table are on `PTN002676268`, which is
  the MDM4 branch, not the human MDM2 subfamily path. The standard
  `just paint-losses human MDM2` check hung while downloading the PANTHER tree
  from the remote tree API and was interrupted.
- Perplexity deep research was attempted through `just deep-research human
  MDM2 --provider perplexity`, but this runtime only exposes the `claude_code`
  provider and the Perplexity run failed before writing a provider file.
- Core catalytic evidence: Honda et al. showed p53 polyubiquitination in the
  presence of E1, UbcH5, and MDM2 and identified MDM2 as a ubiquitin ligase E3
  [PMID:9450543]. Fang et al. showed that Mdm2 is a RING-dependent ubiquitin
  protein ligase for p53 and also mediates its own ubiquitination in a
  RING-dependent manner [PMID:10722742].
- PTHR46858 PAINT places `ubiquitin protein ligase activity`,
  `ubiquitin-dependent protein catabolic process`, and `positive regulation of
  mitotic cell cycle` at `PTN008712296`, with human MDM2 and mouse Mdm2 among
  the seeds.
- MDM2 is nuclear, nucleoplasmic, nucleolar, and cytoplasmic in the curated
  record. Nucleus, nucleoplasm, nucleolus, and cytoplasm are all supported by
  UniProt and by direct localization rows. Cytosol rows from HPA/Reactome need
  exact source support rather than substituting the broader cytoplasm term.
- The GOA file contains many Ensembl Compara rows transferred through rat
  Mdm2-like records. Treat these as suspect unless the local MDM2 literature
  directly supports the exact stress, synapse, or receptor-context term.
