# A2FPI7 (Trichomonas vaginalis G3; TVAG_233530 / TVAG_559790) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No notes file existed before this session; this is the first entry. ProtNLM2 prediction
files were not opened and are not used as evidence.

### Identity
- UniProt A2FPI7 (TrEMBL, PE4 predicted), 129 aa, not flagged as a fragment, no isoforms.
  The entry merges two identical CDSs from two contigs of the G3 draft assembly
  (EAX93188.1 = TVAG_233530, EAX64854.1 = TVAG_559790); TrichDB also lists the newer
  model TVAGG3_0649540 (length of that model not checked here).
- The protein is a stand-alone KilA-N domain: Pfam PF04383 24-126 (1.5e-21), SMART
  SM01252 28-127, PROSITE PS51301 19-124. Nothing obviously missing: the KilA-N module is
  complete; there is simply no second domain, which is common in T. vaginalis KilA-N
  proteins (147 of 1227 are <=150 aa). The benchmark accession is the canonical product.

### Evolutionary placement (file:TRIV3/A2FPI7/A2FPI7-bioinformatics/RESULTS.md)
- PANTHER PTHR48135 ("FAMILY NOT NAMED"), subfamily SF1 ("KILA-N DOMAIN-CONTAINING
  PROTEIN"); weak match 4.5e-05 over 71-127 only. UniProt lists no PANTHER xref.
- PTHR48135: 1667 members, 1308 from T. vaginalis, otherwise bacteria (252) and viruses
  (41). It is a phage/bacterial KilA-N lineage with a huge T. vaginalis expansion.
- No reviewed/characterised KilA-N or APSES protein is in PTHR48135: Mbp1/Swi4/Res1/Res2/
  Cdc10 are PTHR43828, StuA/Efg1/Sok2/Phd1 PTHR47792, poxvirus p28 PTHR11224. No PAINT
  node; no PANTHER family review under interpro/panther/ for PTHR48135.
- Pairwise: significant similarity to phage P1 KilA (P19653) KilA-N region (z 7.4); none
  detectable to Mbp1 APSES domain 1-124 (z 1.25). The APSES link is superfamily-level only
  (Iyer et al. 2002 [PMID:11897024 "The KilA-N domain is suggested to
  be homologous to the fungal DNA-binding APSES domain."]).
- P1 KilA itself has no experimental molecular function (UniProt: lethal/plasmid
  establishment phenotype only; DNA binding there is IEA from keyword).

### Decisions
- GOA has zero annotations. The previous review proposed two NEW rows.
- GO:0003677 DNA binding: kept as NEW, now supported by Iyer et al. 2002 and the domain
  analysis rather than by the falcon report (which retrieved no contexts) or by ML
  predictions. Nothing more specific is transferred: sequence-specific/cis-regulatory
  binding and transcription regulation are APSES-subfamily properties (different PANTHER
  families).
- GO:0005634 nucleus: proposal withdrawn (removed from existing_annotations and from
  core_functions locations; validation rejects non-NEW rows that are not in GOA, and the
  claim does not meet the NEW bar). Only basis was domain -> TF -> nucleus reasoning;
  A2FPI7 is in a phage/bacteria-derived lineage, and the >1300-copy expansion suggests many
  copies may be mobile-element/viral passengers. No NLS annotated.
- Description rewritten: removed the "transcriptional regulation" framing, the ProtNLM2
  mention, and "no GO annotations in GOA" curation commentary.
- Reference fixes: the old genome-paper finding said LGT from "bacteria and viruses"; the
  abstract says bacteria. Old quotes attributed to the falcon main file actually came from
  artifact-00.md. Falcon main file kept in references, marked LOW_QUALITY, unused as support.

### Relative to review next
- No characterised ortholog or member of PTHR48135 exists. The nearest experimentally
  characterised KilA-N-fold protein is S. cerevisiae Mbp1 (P39678; APSES DNA-binding
  domain, crystal structure, MCB binding), related only at the domain-superfamily level
  (different PANTHER family PTHR43828). Mbp1 has a complete review at
  genes/yeast/MBP1/MBP1-ai-review.yaml.
- Modules: none in modules/ concern KilA-N proteins or a pathway A2FPI7 is known to be in.
