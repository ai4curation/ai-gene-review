# Rgn (Regucalcin) Research Notes

## Core Enzymatic Function

Regucalcin/SMP30 is the lactone-hydrolyzing enzyme gluconolactonase (GNL) in the liver responsible for L-ascorbic acid (vitamin C) biosynthesis [PMID:16585534 "SMP30 purified from the rat liver had lactonase activity toward various aldonolactones, such as d- and l-glucono-δ-lactone, d- and l-gulono-γ-lactone, and d- and l-galactono-γ-lactone, with a requirement for Zn2+ or Mn2+ as a cofactor"]. The lactonase reaction with l-gulono-γ-lactone is the penultimate step in vitamin C biosynthesis [PMID:16585534 "The lactonase reaction with l-gulono-γ-lactone is the penultimate step in l-ascorbic acid (AA) biosynthesis"]. SMP30 knockout mice developed scurvy when fed vitamin C-deficient diet, confirming its essential role in vitamin C synthesis [PMID:16585534 "These knockout mice (n = 6), fed a vitamin C-deficient diet, did not thrive; i.e., they displayed symptoms of scurvy such as bone fracture and rachitic rosary and then died by 135 days"].

## Calcium Binding and Regulation

Regucalcin was originally discovered as a calcium-binding protein in 1978 [PMID:699201], though it lacks the typical EF-hand Ca2+-binding motif. It increases Ca2+-ATPase activity in heart mitochondria [PMID:16786169 "The addition of regucalcin (10^-11-10^-8 M) in the enzyme reaction mixture caused a significant increase in Ca2+-ATPase activity in heart mitochondria"]. This regulation of Ca2+-ATPase activity is important for maintaining calcium homeostasis [PMID:16786169 "regucalcin has an activating effect on Ca2+-ATPase in rat heart mitochondria, suggesting its role in the regulation of heart mitochondrial function"].

## Developmental Expression

Regucalcin expression is coordinately upregulated with tissue maturation and gradually downregulated with aging [PMID:8794449]. In liver, peak expression occurs in 5-day-old neonates with a second increase from day 7-10, then decreases in adults to about 1/3 of neonatal levels [PMID:8794449 from UniProt]. In kidney, expression increases from day 21, peaks at day 35, and remains high until 3 months.

## Cellular Functions Beyond Vitamin C Synthesis

### Regulation of Macromolecule Biosynthesis
- Inhibits aminoacyl-tRNA synthetase activity, negatively regulating protein synthesis [PMID:2280766]
- Suppresses enhanced DNA synthesis in proliferating hepatoma cells [PMID:11500948]
- Suppresses enhanced RNA synthesis in regenerating liver [PMID:12397604]

### Anti-apoptotic Effects
- Overexpression suppresses apoptosis in hepatoma cells induced by sulforaphane [PMID:15806309]
- Suppresses apoptosis in kidney proximal tubular epithelial cells [PMID:16167335]
- Inhibits Ca2+-activated DNA fragmentation in liver nuclei [PMID:2001740]

### Metabolic Regulation
- Enhances glucose utilization and lipid production in hepatoma cells [PMID:16817230]
- Increases fatty acid biosynthesis and triglyceride biosynthesis [PMID:16817230]
- Involved in intracellular calcium homeostasis and calcium-mediated signaling [PMID:16786169]

### Tissue-Specific Functions
- In bone: negatively regulates bone development [PMID:12239582, PMID:11129957]
- In testis: negatively regulates flagellated sperm motility but is required for spermatogenesis [PMID:23615721]
- In liver: essential for liver regeneration [PMID:7759556]
- In kidney: involved in epithelial cell proliferation control [PMID:16142398]

### Other Enzymatic Activities
- Increases calcium-independent proteolytic activity [PMID:1513338]
- Inhibits nitric oxide synthase activity in brain cytosol [PMID:12686401]

## Subcellular Localization

Regucalcin is found in:
- Cytoplasm (confirmed by multiple sources)
- Nucleus (ISS evidence)
- Mitochondria (especially in heart, where it regulates Ca2+-ATPase) [PMID:16786169]

## Clinical Significance

The protein is also known as Senescence Marker Protein 30 (SMP30) because its expression decreases with aging. Given its role in vitamin C synthesis and multiple regulatory functions, reduced expression with age may contribute to age-related dysfunction in calcium homeostasis, oxidative stress management, and metabolic regulation.
## Re-review 2026-10-10

GOA refresh changes (large turnover):
- 14 new rows seeded: gluconolactonase activity ISO (mouse MGI:108024; human Q15493) and ISS (mouse Q64374); calcium ion binding ISO (human); nucleus IBA and ISO (mouse); cytoplasm IBA, IEA (GO_REF:0000044) and ISO (mouse); zinc ion binding ISO (human); L-ascorbic acid biosynthetic process ISO (mouse); regulation of calcium-mediated signaling IBA (PTN004208435); GO:0017148 negative regulation of translation IDA (PMID:2280766); GO:0045732 positive regulation of protein catabolic process IDA (PMID:1513338).
- 14 rows retired, mostly older ISO (GO_REF:0000096), IEA (GO_REF:0000043/0000120) and two IBA rows, plus the IDA rows for GO:0010558 (now GO:0017148) and obsolete GO:1903052 (now GO:0045732). Retired rows kept with a note.

Decisions:
- Validator error "action=NEW exists in GOA: GO:0017148": the NEW row was folded into the seeded IDA row (ACCEPT) and deleted [PMID:2280766 "the protein caused a remarkable decrease in hepatic protein synthesis"]. Caveat recorded: single-lab in vitro addition of purified protein; direct versus Ca2+-mediated mechanism unresolved.
- NEW GO:0005739 mitochondrion withdrawn: the only support was activation of mitochondrial Ca2+-ATPase by added regucalcin [PMID:16786169 "Regucalcin increases Ca2+-ATPase activity in the heart mitochondria of normal and regucalcin transgenic rats."], which does not show localization. Moved to suggested_questions; mitochondrion removed from the Ca2+-ATPase core function's locations.
- NEW GO:0004857 enzyme inhibitor activity withdrawn: it is a descendant of GO:0030234 enzyme regulator activity, which the gene already carries, and the mechanism is unresolved. Moved to suggested_questions.
- GO:0030234 enzyme regulator activity (IEA): MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE (generic, not overreaching; regucalcin is reported to activate Ca2+-ATPases and suppress other enzymes).
- GO:0045732 (IDA, PMID:1513338): KEEP_AS_NON_CORE (in vitro proteinase activation).
- All other PENDING rows ACCEPT, consistent with existing rows for the same terms.
- Added supported_by (UniProt CC lines or deep-research text) to 7 live rows and the retired rows that lacked it.
- core_functions: six entries became five. The two entries that used the withdrawn enzyme inhibitor activity (translation suppression; DNA/RNA synthesis suppression) were merged into one entry with no molecular_function and with verbatim quotes in place of the previous paraphrases.

Open questions:
- Is regucalcin mitochondrial? Does it inhibit enzymes directly?
- Many regulatory annotations (translation, DNA/RNA synthesis, apoptosis, NO synthesis) rest on one laboratory's in vitro and cell-line work; independent confirmation would strengthen them.

Review follow-up 2026-10-17: In response to PR #4622 review: (1) GO:0007283 and GO:1901318 (PMID:23615721) no longer quote the author list; they now quote [PMID:23615721 "Tg-RGN animals displayed an altered morphology of epididymis and lower sperm counts and motility"] and "suggest a role for RGN in sperm maturation". (2) The calcium ion binding core function now cites the UniProt cofactor line instead of the PMID:699201 title. (3) Title-only quotes on 13 rows were replaced by evidential abstract sentences (PMID:16786169, 2280766, 12239582, 16817230, 8794449, 16167335, 7759556, 9546611); PMID:699201 (no abstract) and the PMID:11129957 row (where the title documents the mismatch) keep their titles. (4) GO:0032781 positive regulation of ATP-dependent activity moved MODIFY (to the MF GO:0060590, cross-aspect) -> ACCEPT, and the Ca2+-ATPase core function no longer asserts GO:0060590; the effect is abolished by ruthenium red, lanthanum and digitonin [PMID:16786169 "The effect of regucalcin in increasing mitochondrial Ca2+-ATPase activity was not observed in the presence of ruthenium red"], so direct ATPase regulator activity is unproven and is raised as a suggested question. This makes the KEEP_AS_NON_CORE call on the generic GO:0030234 consistent with the core functions.
