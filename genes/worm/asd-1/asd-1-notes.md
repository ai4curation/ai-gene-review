# asd-1 review notes

## Session 2026-10-28

- `just fetch-gene worm asd-1` timed out twice on the UniProt gene-name search. Fetched by accession
  instead: `just fetch-gene worm G5EEW7 --alias asd-1`. The entry is G5EEW7 (TrEMBL, asd-1/R74.5,
  NCBITaxon:6239), with 13 GOA rows.
- No deep-research API keys, so I wrote the literature synthesis by hand in
  `asd-1-deep-research-manual.md`.
- Papers read: PMID:23468662 (full text; ASD-1 EMSA on unc-32 intron 7b, PY-NLS deletion), PMID:29121637
  (full text; RNA-seq), PMID:26430555 (full text; review). Abstract-only: 17060915, 17923701, 25132178,
  25183497, 14704431.

### Decisions

- Regulation of alternative mRNA splicing (IBA, IEA): ACCEPT. This is the core process. ASD-1 binds the
  cis element itself [PMID:23468662 "demonstrating direct and specific binding of ASD-1 and FOX-1 to the UGCAUG stretch"].
- Nucleic acid binding, RNA binding (IEA) and mRNA binding (IBA): MODIFY to GO:0097157 pre-mRNA intronic
  binding. In GO, pre-mRNA binding is not under mRNA binding, so the move from mRNA binding is lateral.
  Added GO:0097157 as a NEW IDA row from PMID:23468662. This is an MF refinement, not a process term.
- Single-stranded RNA binding (IDA, NMR structure): ACCEPT.
- Protein binding (two IPI rows with SUP-12): REMOVE under the protein-binding policy. The interaction is
  real but occurs on co-bound RNA [PMID:26430555 "there is no simple contribution of binding cooperativity"].
- Nucleus (IBA, IEA): ACCEPT, with ASD-1-specific NLS evidence.
- Cytoplasm (IBA): KEEP_AS_NON_CORE. It reflects mammalian cytoplasmic RBFOX isoforms. No ASD-1 data
  either way.
- Nervous system development (IBA, IEA): MARK_AS_OVER_ANNOTATED. ASD-1's neuronal role is splicing
  regulation in differentiated neurons, not development.
- No NEW process terms were proposed. The egg-laying and sex myoblast migration phenotypes are
  necessity evidence acting through the EGL-15 isoform, and do not show that ASD-1 takes part in those
  processes.
