# ADAT2 notes

## 2026-11-21

Deep research provider execution was unavailable in this sparse ADAT worktree, so this review was
completed from cached UniProt/GOA/PANTHER/Reactome data plus the fetched primary papers.

Torres et al. establish the human ADAT2:ADAT3 enzyme as the precursor-tRNA A34-to-I34 editing
complex: the paper identifies the "human genes encoding for hetADAT", shows that the subunits
"co-localize in nucleus in an ADAT2-dependent manner", and assays A34 editing on a precursor
tRNAVal(AAC) substrate [PMID:25916855].

The 2025 ADAT3 disease paper confirms that ADAT2 supplies the catalytic site while ADAT3 is the
required substrate-recognition partner: it describes ADAT2/ADAT3 as a complex that edits A34 to
I34 at the wobble position and shows that ADAT3 variants impair complex activity
[PMID:40120092]. Its mouse radial-migration phenotype supports a downstream consequence of
reduced tRNA I34-dependent translation, but not direct execution of neuron migration by ADAT2.

PAINT places `GO:0052717` and `GO:0002100` at `PANTHER:PTN000118390` in the eukaryotic ADAT2/TAD2
clade. `just paint-losses human ADAT2` reported no IRD or IKR on the human ADAT2 lineage.
