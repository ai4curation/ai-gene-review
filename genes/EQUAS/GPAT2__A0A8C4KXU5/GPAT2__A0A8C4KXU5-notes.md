# GPAT2 (donkey, A0A8C4KXU5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full review of the 800-residue donkey GPAT2 entry A0A8C4KXU5 (Ensembl ENSEASP00005003122.2, gene
ENSEASG00005002382.2), the full-length model of the same gene as the 718-residue entry A0A9L0ILJ0 reviewed
in `genes/EQUAS/GPAT2/`. ProtNLM2 output was not opened or used.

### Setup and deep research

- `just fetch-gene EQUAS A0A8C4KXU5 --alias GPAT2__A0A8C4KXU5`: 14 GOA rows, all IEA (Ensembl Compara
  GO_REF:0000107, TreeGrafter GO_REF:0000118, combined GO_REF:0000120, InterPro2GO, UniProt SubCell).
- `just deep-research-falcon EQUAS GPAT2__A0A8C4KXU5 --fallback perplexity-lite` failed: falcon
  "Failed to authenticate"; perplexity-lite HTTP 401 insufficient quota. No deep-research file exists.
  The review relies on the cached mouse primary papers below, read directly.

### Evolutionary grounding

- A0A8C4KXU5, mouse Q14DK4, human Q6NUI2 and rat D3ZI76 are all PANTHER PTHR12563:SF15 (GPAT2,
  mitochondrial); GPAT1/GPAM (mouse Q61586, human Q9HCL2) is SF16
  (`interpro/panther/PTHR12563/PTHR12563-entries.csv`).
- Cached PAINT (`PTHR12563-paint.tsv`): GPAT1/GPAT2 node PTN000970957 (taxon:6072) carries GO:0004366,
  GO:0005739, GO:0006650, GO:0019432. No node carries GO:0034587 piRNA processing or GO:0003841 AGPAT
  activity. GO:0006631 fatty acid metabolic process is only on bacterial PlsB node PTN000285870.
- QuickGO for mouse Q14DK4: GPAT activity IDA/EXP; AGPAT activity IDA (PMID:22905194); PA biosynthesis IMP
  (PMID:22905194); piRNA processing IMP (PMID:23611983); mitochondrion IDA; mitochondrial outer membrane
  ISS/ISO. IBAs on mouse match the PAINT node terms only.
- Own analysis (`GPAT2__A0A8C4KXU5-bioinformatics/RESULTS.md`): 83.75% identity to mouse over 99.88% of
  its length (one unpaired mouse residue, 363); HXXXXD = HKSLLD at 205-210; both mouse TM segments align
  gap-free. Similar for human (88.04%) and rat (84.5%).

### Literature (mouse Gpat2; nothing on donkey)

- [PMID:17689486 "When Cos-7 cells were transiently transfected with GPAT2, NEM-sensitive GPAT activity
  increased 30%."] and ["Confocal microscopy confirmed a mitochondrial location."] (abstract only).
- [PMID:22905194 "GPAT2 overexpression significantly increased both GPAT and AGPAT activities only when
  arachidonoyl-CoA was used as a substrate"]; the authors hedge on AGPAT: ["These findings suggest that
  the increase in PA may be due to an AGPAT activity for this heterologously-expressed protein, but we
  cannot exclude the possibility that the protein has dual enzymatic activities."]
- [PMID:22285183 "These results suggest that the GPAT2 protein has two transmembrane segments and that
  the N-terminal and C-terminal regions of this protein face the cytoplasm."]
- [PMID:23611983 "These data clearly show that GPAT2 plays a critical role in primary processing during
  piRNA production."] and ["These data suggest that the acyltransferase activity of GPAT2 is dispensable
  for the biogenesis of piRNA."]

### Decisions

- GPAT activity: ACCEPT (core). PA biosynthetic process: ACCEPT (most specific catalytic process term).
- AGPAT activity: KEEP_AS_NON_CORE; crude-membrane activity in overexpressing cells, authors hedge, PAINT
  did not propagate it. Not removed because it rests on a curated mouse IDA.
- piRNA processing: ACCEPT. PAINT absence is read as a decision that it is not ancestral to GPAT1+GPAT2;
  the transfer stays within SF15, and the catalytic-motif-independent requirement plus MILI binding at the
  site of processing meet the participation (scaffold) bar. Single study, mouse GS cells.
- mitochondrion / mitochondrial membrane / membrane: MODIFY to GO:0005741 mitochondrial outer membrane.
- TAG biosynthesis, glycerol-3-phosphate metabolic process: KEEP_AS_NON_CORE. Fatty acid metabolic process:
  MARK_AS_OVER_ANNOTATED. lipid metabolic process, phospholipid biosynthetic process, acyltransferase
  activity (two rows): TOO_GENERAL.
- Everything above is inferred for donkey from mouse experiments plus subfamily membership; no donkey
  GPAT2 function has been measured.
