# Su(H) (Suppressor of Hairless) — curation notes (DROME, P28159)

Directory named by UniProt accession because the symbol contains parentheses; `gene_symbol: Su(H)`
is recorded in the review.

## Session 2026-09-30 (Notch signaling module)

Deep research: `P28159-deep-research-falcon.md` produced (falcon).

### Key findings
- Su(H) binds E(spl)-C m5/m8 regulatory sequences and these sites are required for activation
  [PMID:7590238].
- Dual function: activator with NICD, repressor without signal [PMID:12154126 "functions as an
  activator during Notch (N) pathway signaling, but can act as a repressor in the absence of
  signaling"]; Hairless recruits Groucho and dCtBP [PMID:12154126].
- Su(H) C-terminal domain binds Hairless; Notch and Hairless compete for Su(H) [PMID:21737682].
- Notch-independent roles: direct repression of sim [PMID:10673509 "repression of sim transcription
  by Su(H) is direct and independent of Notch activity"]; SOP development [PMID:12642500].
- Cytoplasmic Su(H) in socket cells; nuclear in disc cells [PMID:8674407].

### Decisions
- Core MF: GO:0001228 activator (in GO:1990433) and GO:0001227 repressor (in GO:0090571).
- NEW: GO:0007221 (IDA, PMID:7590238).
- GO:0005515 rows: Notch/Notch1 partners -> MODIFY to GO:0001223 transcription coactivator
  binding; Insensitive/Ebi/SMRTER -> MODIFY to GO:0001222 transcription corepressor binding; human
  TBP (SCA17 model) -> REMOVE.
- GO:0061629 (partner lilli/FBgn0041111, AFF4 ortholog, not a DNA-binding TF) -> MODIFY to
  GO:0001223; flagged in suggested_questions.
- GO:0003677 -> GO:0000978; GO:0003700 -> GO:0000981; GO:0032991 -> GO:1990433.

### PANTHER
UniProt DR PANTHER: PTHR10665 ("RECOMBINING BINDING PROTEIN SUPPRESSOR OF HAIRLESS"), no subfamily
line. IBA GO:0005634, GO:0000981, GO:0000978 <- PANTHER:PTN000071433.
