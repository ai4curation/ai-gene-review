# adiC (P60061) curation notes

## Sources and literature search

- No deep-research provider file was generated for this gene (no provider API keys
  in this session); no `-deep-research-*.md` file exists. The review is based on the
  UniProt Swiss-Prot record (`adiC-uniprot.txt`) and the cached primary papers
  listed below, all fetched with `just fetch-pmid`.
- Literature search (2026-11-04): the PMIDs cited in GOA and in the UniProt entry
  (12867448, 14594828, 15919996, 17099215, 19578361, 21368142, 27582465) were
  cached and read. Only PMID:19578361 has full text in the cache; the others are
  abstract-only.

## Function

- AdiC (YjdE) is the arginine:agmatine antiporter of the arginine-dependent acid
  resistance system (AR3) of E. coli. Deletion abolishes arginine-dependent acid
  resistance and arginine/agmatine exchange, without affecting AdiA decarboxylase
  [PMID:12867448 "An adiC mutant proved incapable of exchanging extracellular
  arginine for intracellular agmatine but maintained wild-type levels of arginine
  decarboxylase protein and activity."] [PMID:14594828 "Strains from which this gene
  is deleted fail to mount arginine-dependent XAR, and they cannot perform coupled
  transport of arginine and agmatine."]
- Purified AdiC reconstituted in liposomes performs strictly coupled, electrogenic
  Arg/Agm exchange; homodimer [PMID:17099215 "Purified AdiC reconstituted into
  liposomes exchanges arginine and agmatine in a strictly coupled, electrogenic
  fashion."]
- Mechanism of acid resistance: a "virtual proton pump" — AdiA decarboxylation
  consumes a cytoplasmic proton, AdiC exports agmatine and imports fresh arginine
  [PMID:19578361 "At the heart of the process is a 'virtual proton pump' in the
  inner membrane, called AdiC, that imports L-arginine from the gastric juice and
  exports its decarboxylation product agmatine."]. Each subunit of the dimer is a
  self-contained transporter (tandem WT-W293L construct, PMID:19578361).
- Structures: outward-open apo (PMID:19578361), Arg-bound N101A (PMID:21368142),
  wild-type with/without agmatine (PMID:27582465). AdiC is the main structural
  paradigm of the APC superfamily (5+5 inverted repeat, LeuT fold)
  [PMID:21368142 "AdiC, is the main APC structural paradigm"].

## Localization

- Inner (plasma) membrane, 12 TM helices, N and C termini cytoplasmic; C-terminal
  topology mapped in the global topology study PMID:15919996.

## Annotation decisions (summary)

- ACCEPT: arginine:agmatine antiporter activity (IDA, IBA); plasma membrane (IDA x2,
  IBA, IEA SubCell, ISM); cellular stress response to acidic pH (IMP).
- MODIFY to specific terms: membrane -> plasma membrane; transmembrane transporter
  activity -> arginine:agmatine antiporter activity; transmembrane transport, amino
  acid transmembrane transport and carboxylic acid transmembrane transport ->
  L-arginine transmembrane transport (GO:1903826). GO has no agmatine transport
  process term; the antiporter MF term captures the agmatine leg.
- No PAINT loss on the adiC lineage (`just paint-losses ECOLI adiC`).
- PANTHER: PTHR42770:SF18 (ARGININE_AGMATINE ANTIPORTER); AdiC is the reference
  protein of the PTHR42770 family review.
