# Mki67 (mouse) review notes

## Session 1 (2026-10-28)

- fetch-gene resolved E9PVX6 (KI67_MOUSE, Swiss-Prot, MGI:106035, GeneID 17345); 53 GOA rows.
- No deep-research API keys; literature synthesis in `Mki67-deep-research-manual.md`.
- Additional papers cached for function: PMID:27362226 (Cuylen 2016, surfactant; includes
  mouse ES cells), PMID:32879492 (Cuylen-Haering 2020, clustering), PMID:24867636
  (Booth 2014, perichromosomal layer, PP1), PMID:39003739 (Sanz-Flores 2024, abstract only).
- PMID:20097747, which the batch task flagged as a key experimental paper, is a rat
  myocardial-infarction study that uses Ki-67 only as a cycling-cell marker
  [PMID:20097747 "Cycling cells were identified with an antibody against nuclear transcription factor Ki-67."].
  It says nothing about Ki-67 function and is not attached to any GOA row.

### Key decisions

- ~20 MGI rows come from marker usage (anti-Ki-67 IHC in papers about other genes).
  Nucleus/nucleolus location rows are true and kept (ACCEPT).
- Proliferation process rows (`cell population proliferation`, `epithelial cell
  proliferation`, `hepatocyte proliferation`, `cholangiocyte proliferation`) are read-outs
  of the perturbed gene's phenotype, not Ki-67 participation, and are contradicted by
  Sobecki 2016 [PMID:26949251 "Ki-67 mutant mice developed normally and cells lacking Ki-67 proliferated efficiently."].
  Most are abstract-only, so per project rules they are MARK_AS_OVER_ANNOTATED (not
  REMOVE), each with a source_defects entry to MGI.
- NOT involved_in cell population proliferation (UniProt IMP, PMID:26949251) accepted.
- `regulation of chromatin organization` (IMP) refined to `regulation of heterochromatin
  organization` (GO:0120261, is_a GO:1902275, checked with OAK).
- `meiotic cell cycle` rows rest on expression/localisation in meiocytes; mutant mice are
  fertile; marked over-annotated.
- `regulation of mitotic nuclear division` (IBA/ISO/ISS): Ki-67 is not shown to set the
  rate or frequency of mitosis; over-annotated.
- `cytoplasm` IDA from a beta-catenin paper (abstract only): UNDECIDED.
- Core MF: no GO term for the surfactant/steric-barrier role; proposed as a new term.
  `molecular condensate scaffold activity` kept for the RNA-dependent condensate
  formed at mitotic exit (by similarity to human).
