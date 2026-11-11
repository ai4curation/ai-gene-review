# Klf9 (rat) review notes

- Fetched with `just fetch-gene rat Klf9`; UniProt Q01713 (KLF9_RAT) confirmed; 24 GOA rows (23 unique seeded).
- Only rat experimental GOA row: IEP cellular response to endothelin, PMID:18406357 (full text read).
  Klf9 rose <2-fold, delayed, sustained 4-6 h by qPCR [PMID:18406357 "The increases in expression of Klf9 and Klf10 were relatively small (maximal expression < 2-fold at 1.5–2 h) although levels remained elevated over 4–6 h"].
  Authors did not follow up Klf9 functionally. Kept as non-core (valid IEP usage, modest effect).
- Rat-protein functional data not in GOA: Imataka 1992 (PMID:1356762, abstract-only cache) shows rat BTEB
  activates multi-GC-box promoters and represses the single-GC-box CYP1A1 BTE promoter. Used to add NEW
  GO:0001227 (repressor activity, RNAPII-specific); activator activity GO:0001228 already present by ISO.
- Sin3A-interacting SID (PMID:11438660, full text) gives a mechanism for repression.
- Process terms from orthologs: embryo implantation & PR signaling (mouse KO, PMID:15117941/15917344),
  keratinocyte proliferation & cortisol response (human, PMID:22711835) kept as non-core.
  Circadian rhythm marked over-annotated: KLF9 is a clock-controlled output gene, not a clock component.
- Considered but NOT added (strict NEW bar): positive regulation of neuron projection development
  (rat antisense/overexpression, PMID:12021188, PMID:10438482), response to thyroid hormone (expression),
  oligodendrocyte differentiation (PMID:22472204). These are perturbation/expression evidence only;
  raised as suggested_questions.
- General terms (GO:0003700, GO:0000977, GO:0006355) MODIFIED to the specific terms the gene already carries.
