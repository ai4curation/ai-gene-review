# prpC (PA0795, Q9I5E3) review notes

## Literature

Searches 2026-11-05: PubMed MCP search failing (API errors); web search
"Pseudomonas aeruginosa methylcitrate synthase PrpC PA0795" found the Dolan et al. 2022
mBio paper (DOI 10.1128/mbio.02541-22 = PMID:36377867, PMC9765439, full text cached) and
PDB 6S6F/6S87 (PrpC apo and oxaloacetate-bound).

1. Mitchell et al. 1995 [PMID:7626013]. Abstract only (PMC1135760 is a scanned PDF; the
   PMC full-text call returned no text). Two native citrate synthases purified from
   P. aeruginosa: CSI, a hexamer of 42-kDa subunits, and CSII, a dimer of 36.5-kDa
   subunits [PMID:7626013 "showed that CSI is a hexamer and CSII is a dimer"]. No gene is
   identified [PMID:7626013 "It is suggested that the CS isoenzymes are products of
   different structural genes."]. The paper predates the PAO1 genome (2000).
   PseudoCAP annotated the same IDA rows (GO:0036440, GO:0006099) to both gltA (P14165)
   and prpC (Q9I5E3) (`.cache/paint/pseudocap.tsv`).
2. Dolan et al. 2022 [PMID:36377867], full text cached. Purified PrpC has both citrate
   synthase and 2-methylcitrate synthase activity [PMID:36377867 "Purified PrpCPa exhibits
   both citrate synthase activity (with acetyl-CoA as a substrate) and 2-methylcitrate
   synthase activity (with propionyl-CoA as a substrate)."], with roughly comparable
   activity toward both acyl-CoAs and higher Vmax with propionyl-CoA. PrpC is a homodimer
   [PMID:36377867 "PrpCPa is a homodimer."], GltA a hexamer; monomer mass about 41 kDa.
   ΔprpC cannot grow on propionate [PMID:36377867 "The 2-methylcitrate synthase mutant
   (ΔprpC) was unable to grow on propionate as a sole carbon source but displayed no
   detectable growth deficit on any of the other tested carbon sources."]. Basal PrpC
   rescues ΔgltA, and a ΔgltA ΔprpC double mutant could not be made [PMID:36377867
   "Consistent with this, and despite repeated attempts at doing so, we were unable to
   make a ΔgltA ΔprpC double mutant."].

Interpretation: CSII of the 1995 paper (dimer, ~37-41 kDa subunit) matches PrpC, and CSI
(hexamer) matches GltA, so PseudoCAP's attribution is very likely right in substance, but
the 1995 paper itself cannot tie either enzyme to a gene. PrpC's citrate synthase
activity is a genuine secondary activity: comparable kcat with acetyl-CoA, and enough
in vivo to keep a gltA mutant alive. Its main role is 2-methylcitrate synthesis in the
2-methylcitrate cycle (propionate catabolism).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000201223 | GO:0036440 citrate synthase activity | 19 | 270 (123 taxa) | GO:0036440, IDA, PMID:7626013 (PseudoCAP) | SOUND (gene identity inferred) | Purified CSII matches PrpC (dimer, ~41-kDa subunit) and purified recombinant PrpC has CS activity (PMID:36377867, full text). The 1995 paper does not identify the gene, so a SUSPECTED CHECK defect asks PseudoCAP to add/repoint to PMID:36377867. | E. coli PrpC (P31660), S. typhimurium PrpC (Q56063), yeast CIT1/CIT2/CIT3, S. pombe cit1, human/mouse/rat CS, Arabidopsis CSY4, Drosophila kdn, Dictyostelium and others | Yes; dozens of experimentally characterised citrate synthases. No GO_CENTRAL defect. |
| PTN000201223 | GO:0006099 tricarboxylic acid cycle | 4 | 270 (123 taxa) | GO:0006099, IDA, PMID:7626013 (PseudoCAP) | SOUND in substance (gene identity inferred; participation conditional) | PrpC supplies citrate in vivo when GltA is absent (ΔgltA ΔprpC not obtainable), so it can take part in the TCA cycle, but GltA is the TCA-cycle enzyme in wild type. The same CHECK defect applies. | yeast CIT1 (S000005284), CIT3 (S000006205), S. pombe cit1 (SPAC6C3.04) | Yes, on the mitochondrial citrate synthases. The term is right for the eukaryotic CS members; for the bacterial PrpC subclade it is a backup role. Not filed as a GO_CENTRAL defect (raised as a question). |

## Annotation decisions

- GO:0050440 2-methylcitrate synthase (IBA, IEA): ACCEPT; core.
- GO:0019543 propionate catabolic process IBA: ACCEPT; ΔprpC cannot grow on propionate.
- GO:0036440 citrate synthase (IBA, IDA, IEA): KEEP_AS_NON_CORE (genuine secondary activity).
- GO:0006099 TCA cycle (IBA, IDA, IEA): KEEP_AS_NON_CORE (backup in vivo role).
- GO:0005975 carbohydrate metabolic process IBA: MARK_AS_OVER_ANNOTATED.
- GO:0046912 IEA: TOO_GENERAL (GO:0050440 is_a GO:0046912).
- GO:0005737 cytoplasm IEA: ACCEPT (soluble enzyme, no signal peptide or TM).
