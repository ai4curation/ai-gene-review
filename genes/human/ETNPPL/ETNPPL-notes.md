# ETNPPL (Q8TBG4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ETNPPL is the closest experimentally characterised relative of the ProtNLM2
benchmark gene DROME/CG8745 (Q9VU95). This review treats ETNPPL in its own right and
does not use any ProtNLM2 output.

### Deep research

`just deep-research-falcon human ETNPPL --fallback perplexity-lite` failed: the falcon
(Edison) call returned "Failed to authenticate" (HTTP 403) and the perplexity-lite
fallback also failed. No deep-research file was produced. The review is based on
literature retrieved directly from PubMed (search "ETNPPL OR AGXT2L1", 58 hits) and
cached into `publications/`.

### Identity and family placement

- UniProt Q8TBG4, 499 aa, synonym AGXT2L1; class-III PLP-dependent aminotransferase
  fold (Pfam PF00202 Aminotran_3), PANTHER PTHR45688:SF1 "ETHANOLAMINE-PHOSPHATE
  PHOSPHO-LYASE" (from the UniProt record and `interpro/panther/PTHR45688/PTHR45688-entries.csv`).
- SF1 contains ETNPPL orthologues from human, mouse, cow, Xenopus and zebrafish. PHYKPL
  (Q8IUZ5) is in a separate subfamily, SF6. The fly gene CG8745 (Q9VU95) is in SF13
  ("ALANINE--GLYOXYLATE AMINOTRANSFERASE 2-LIKE"), a mixed subfamily, not SF1
  (entries.csv). So the SF1-specific substrate (phosphoethanolamine) should not be
  transferred to CG8745 by subfamily membership alone.
- PAINT (`PTHR45688-paint.tsv`): node PTN002904331 carries an IBD for GO:0050459
  (ethanolamine-phosphate phospho-lyase activity), seeded only by UniProtKB:Q8TBG4,
  taxon 117571 (Euteleostomi). So the curator placed the activity at the bony-vertebrate
  ETNPPL clade, not deeper. The AGXT2 node PTN002485563 (mitochondrion, GO:0008453
  alanine-glyoxylate transaminase) was not propagated to ETNPPL; ETNPPL has no IBA for
  mitochondrion or transaminase. That omission is consistent with the biochemistry
  (no transaminase activity, see below).

### Molecular function (experimental, human protein)

- Recombinant human AGXT2L1 converts phosphoethanolamine to ammonia, Pi and acetaldehyde
  [PMID:22241472 "AGXT2L1 catalyzed a similar reaction on phosphoethanolamine, converting it to ammonia, inorganic phosphate, and acetaldehyde."]
  UniProt records Km 680 uM, Vmax 1.46 umol/min/mg at pH 7.4 (ECO:0000269 PubMed:22241472).
- Lacks transaminase activity [PMID:22241472 "Unlike AGXT2, AGXT2L1 and AGXT2L2 did not act as transaminases"];
  at least 500-fold more active as lyase than aminotransferase and very selective for
  O-phosphoethanolamine [PMID:23761375].
- Kinetics: dianion-binding active site; an unusual stable Michaelis complex (400 nm
  species) during turnover; strict specificity [PMID:25327712].
- Crystal structure of human enzyme with PMP at 2.05 A (PDB 6TOR), same fold and
  active-site arrangement as Arthrobacter A1RDF1 [PMID:32254049]. A1RDF1 is a bacterial
  class-III homologue with phosphoethanolamine phospho-lyase activity [PMID:27709756]
  (shows the activity also arose/exists outside vertebrates, but A1RDF1 is not shown
  to be in SF1; no transfer claim made).
- PLP cofactor (UniProt COFACTOR ECO:0000269 PubMed:22241472); K278 Schiff-base lysine
  (by similarity).

### Biological role (in vivo, mostly mouse)

- Mouse Etnppl KO hepatocytes convert more [3H]ethanolamine to p-ETN and PE
  [PMID:39312446]; i.e. ETNPPL catabolises p-ETN in cells and diverts it from the
  Kennedy pathway. Overexpression in Huh7 cells reduces pEtn and PE synthesis
  [PMID:40154596]. KO mice have lipoprotein / cholesterol phenotypes [PMID:39312446,
  PMID:40679478] - these are downstream organismal phenotypes, not annotated.
- Etnppl is an astrocyte-specific, fasting/glucocorticoid-induced gene in mouse brain;
  KO astrocytes show no major change in FAO or O2 consumption [PMID:34048714].
- Glioma: ETNPPL reduced in transformation foci and high-grade glioma; overexpression
  reduces glioma stem cell growth [PMID:32218467]. Overexpression phenotype only; not
  annotated as a process.

### Localization

- No experimental evidence for mitochondria. UniProt "Mitochondrion" is ECO:0000305
  (curator inference); the matrix rows are ARBA (IEA) and Reactome TAS.
- Human cortex IF (peptide-competition control) and glioma cells: ETNPPL in cytoplasm
  or nucleus [PMID:32218467]. Mouse brain IHC with KO-validated monoclonal antibodies:
  predominantly nuclear, rarely cytoplasmic [PMID:36794261]. Tissue-level staining
  cannot exclude a mitochondrial pool, so mitochondrial rows are UNDECIDED rather than
  removed; nucleus added as NEW (human + mouse antibody evidence).

### Decisions

- GO:0050459 (IDA, IBA, IEA): ACCEPT, core.
- GO:0030170 PLP binding: ACCEPT.
- GO:0005515 x2 (ZC3HC1 Y2H, HuRI): REMOVE per protein-binding policy.
- GO:0005739 / GO:0005759: UNDECIDED.
- NEW GO:0046434 organophosphate catabolic process: ETNPPL itself catalyses the
  breakdown of phosphoethanolamine (participation test passes: it performs the step).
  No phosphoethanolamine-specific catabolic term exists (OLS search); proposed as new term.
- NEW GO:0005634 nucleus.
