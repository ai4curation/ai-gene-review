# O61358 notes

## 2026-11-23

- Started the ONCVO beta-tubulin review with UniProt `O61358`, a 448 aa
  full-length *O. volvulus* beta-tubulin sequence in PANTHER `PTHR11588`.
  UniProt traces the entry to EMBL `AF019885` / protein `AAC13548.1` from the
  Geary et al. filarial cDNA study [PMID:9576511 Cloning and characterization
  of cDNAs encoding beta-tubulin from Dirofilaria immitis and Onchocerca
  volvulus., "We cloned and characterized cDNAs encoding beta-tubulin from 2
  filariae, Dirofilaria immitis and Onchocerca volvulus"].
- `just paint-losses ONCVO O61358` reported that `O61358` is in PANTHER
  `PTHR11588` but not as a leaf of the cached PAINT tree, and found no IRD or
  IKR loss on the gene lineage.
- Live UniProt release 2026_04 has many duplicate or partial *O. volvulus*
  beta-tubulin candidates in `PTHR11588`. I chose `O61358` before the current
  A0A8R1*/A0A2K6* genome-model duplicates because it is a full-length PE2 cDNA
  record tied directly to PMID:9576511; the companion `O61359` record is marked
  as a genomic-DNA fragment.
- O61358 has nine GOA rows. Seven are automated beta-tubulin rows for GTPase
  activity, GTP binding, structural constituent of cytoskeleton, microtubule,
  cytoskeleton, microtubule-based process and microtubule cytoskeleton
  organization. These mirror the accepted or too-general calls in the merged
  `BRUMA/bma-ben-1` review and are supported by the local UniProt domain
  architecture.
- The two EnsemblMetazoa behavior rows, chemosensory behavior and egg-laying
  behavior, are transferred from the *C. elegans* BEN-1 product. I marked both
  over-annotated for this parasite beta-tubulin: the direct evidence for O61358
  is the conserved beta-tubulin sequence, not an *O. volvulus* sensory or
  egg-laying circuit assay.
- Geary et al. reported that all four filarial beta-tubulins considered in
  their comparison encoded Phe at the codon-200 site associated with
  benzimidazole resistance [PMID:9576511 Cloning and characterization of cDNAs
  encoding beta-tubulin from Dirofilaria immitis and Onchocerca volvulus., "All
  4 filarial beta-tubulins are predicted to encode phe at this position"].
  That residue is consistent with a benzimidazole-sensitive beta-tubulin
  sequence, so the remaining gap is not O61358's local codon 200 but whether
  this cloned isotype is a drug-engaged target in adult *O. volvulus*.
