# B8BAB0 (OsI_29064) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened or used. No notes file
existed before this session; this is the first entry.

### Identity (gene model)

- B8BAB0 is the indica (cv. 93-11, BGI annotation OsI_29064 / BGIOSGA028580,
  chromosome 8) gene model of rice OsBURP12. Its japonica allele is Q6ZA27 (BURP12,
  Os08g0380100, 627 aa, Swiss-Prot). Global alignment: 95.6% identity over 594 aligned
  pairs [file:ORYSI/B8BAB0/B8BAB0-bioinformatics/RESULTS-rereview.md].
- B8BAB0 is NOT a fragment by length (623 vs 627 aa), but it is an alternative gene
  model with two differences from Q6ZA27:
  1. ~31 residues missing from the N-terminal propeptide region (one FTNYG repeat unit
     of Q6ZA27 is absent);
  2. a divergent 42-residue C-terminal tail after residue 581 replaces the Q6ZA27
     C-terminus, so B8BAB0 lacks the fourth CH motif of the BURP domain (3 CH vs 4 in
     Q6ZA27, tomato GP1 and Arabidopsis PGL2). Likely a gene-model artefact; not tested
     against indica transcript evidence.
- UniProt record: unreviewed, PE 4 (predicted), signal peptide 1-21 (SignalP), BURP
  domain 384-595 (PROSITE PS51277), PANTHER PTHR31458:SF2 [file:ORYSI/B8BAB0/B8BAB0-uniprot.txt].
- GOA: no annotations at all for B8BAB0 (and none for the japonica allele Q6ZA27 in
  QuickGO, checked 2026-10-20).

### Evolutionary placement

PANTHER 19 tree (proxy leaf Q6ZA27), see RESULTS-rereview.md:
- closest paralog OsBURP16 (Q7XES5), split at grass duplication PTN000779097;
- then OsBURP14 (SF4) at commelinid duplication PTN002050022;
- tomato GP1 (PG1 beta subunit) and Arabidopsis PGL1-3 only at the Mesangiosperma
  node PTN004827825. No eudicot one-to-one ortholog.
- The family's only PAINT IBD (PTN004827911: plant-type cell wall, plant-type cell
  wall modification, cell wall modification involved in multidimensional cell growth;
  seed AT1G70370/PGL3) sits on the Brassicaceae SF10 node. B8BAB0's clade is outside
  it, so the curators did not extend these terms to grass PG1beta-like proteins. I
  treat that as a deliberate decision and do not transfer them.

### Literature

- Ding et al. 2009 [PMID:19363683] identified 17 rice BURP genes (OsBURP01-17); abstract
  only in cache. UniProt Q6ZA27 cites it for OsBURP12 expression in stems, leaves,
  shoot and panicles.
- Liu et al. 2014 [PMID:24237159 "The PG1β-like subfamily consists of three members, OsBURP02, OsBURP14 and OsBURP16."]
  Under the Ding numbering OsBURP12 is not listed as PG1beta-like, although PANTHER
  places Q6ZA27/B8BAB0 in the same subfamily as OsBURP16 and B8BAB0 has the PG1beta
  FxxY repeat region. Numbering discrepancies between Ding 2009 and UniProt gene names
  are possible (UniProt BURP2, Q6I5W0, is in a different PANTHER family, PTHR31236), so I
  record this as unresolved rather than as a contradiction.
- OsBURP16 overexpression: [PMID:24237159 "Transgenic rice showed enhanced PG activity and reduced pectin content."]
- OsEIL2 activates OsBURP14 and OsBURP16 [PMID:32005373 "OsEIL2 binds directly to the promoter of OsBURP14
and OsBURP16 and activates their transcript levels."]. B8BAB0/OsBURP12 is not
  mentioned.
- Tomato PG1 beta subunit [PMID:1392611 "a cell wall protein that associates with,
and apparently regulates, the catalytic PG2 polypeptides"]; mature protein made of
  the FTNYGxxGNGGxxx repeat.
- AtPGL3 (SF10) is in the cell wall and its BURP domain is needed for function
  [PMID:26106400].
- No paper studies B8BAB0 or OsBURP12 function. The falcon deep-research report adds
  no gene-specific data; its claims are about OsBURP16/OsBURP14 and the family.

### Changes from the previous draft

- Previous draft quoted text not present in the UniProt record or the deep-research
  file (non-verbatim quotes); replaced with verbatim quotes.
- Removed the core-function MF GO:0030234 enzyme regulator activity and BP
  GO:0071555 cell wall organization: no grass member has a demonstrated activity,
  and PAINT did not propagate any MF/BP to this clade. Location reduced to
  extracellular region (signal peptide + family); cell wall left as a question.
- Description rewritten to record the gene-model identity and paralog relationships.

### Relative to review next

OsBURP16 (Q7XES5, ORYSJ), nearest experimentally studied paralog (grass duplication
PTN000779097). The ortholog/allele OsBURP12 (Q6ZA27) has only expression data. No
review for either exists in the repo.
