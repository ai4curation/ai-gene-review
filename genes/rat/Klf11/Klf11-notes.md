# Klf11 (rat) review notes

- 2026-10-28: fetch-gene resolved E9PTS6 (RGD:1306646, GeneID 313994) as requested; 25 GOA rows,
  all IBA/IEA/ISO except one IEP (PMID:18406357, full text read).
- No deep-research API keys; literature synthesis written to Klf11-deep-research-manual.md.
- Key mechanistic papers are on human KLF11/TIEG2 (Urrutia lab): mSin3A recruitment via alpha-HRM
  [PMID:11438660 "represses transcription through recruitment of the mSin3A-histone deacetylase complex"],
  Smad7 repression [PMID:15300592], insulin / Pdx-1 activation [PMID:15774581, PMID:19843526].
- Decisions: core MF = GO:0001227 repressor activity (generic TF rows MODIFY to repressor plus
  activator GO:0001228, since activation of insulin/Pdx-1 promoters is documented); generic DNA
  binding rows MODIFY to GO:0000978; cellular response to endothelin kept as non-core expression
  response; NOT hemopoiesis kept (mouse KO normal hematopoiesis, PMID:15607700); G1/S transition
  UNDECIDED (source not located).
- No NEW terms proposed (GO:0001228 / GO:0045944 appear only as MODIFY replacements).
