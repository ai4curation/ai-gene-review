# SLC2A9 (GLUT9 / URATv1), UniProt Q9NRM0 — curation notes

## Summary of synthesized function

SLC2A9/GLUT9 is a class II member of the SLC2 (GLUT) facilitative transporter family
(major facilitator superfamily, 12 TM helices) whose principal, physiologically
relevant function is **urate transport**, not sugar transport. It is a
**high-capacity, Na+-independent, voltage-driven urate uniporter** that drives renal
urate handling and sets serum urate levels in humans.

- **Core molecular function:** urate transmembrane transporter activity (GO:0015143).
  Directly demonstrated by radiotracer flux in Xenopus oocytes and mammalian cells
  (PMID:18327257, PMID:18701466, PMID:18842065; confirmed PMID:36749388).
  Km ~365 µM–900 µM for urate [PMID:18701466 "GLUT9-expressed Xenopus oocytes mediated saturable urate transport (K(m): 365+/-42 microm)"; UniProt KM=900 uM / 433 uM].
- **Transport mode:** facilitative uniport, Na+-independent, electrogenic/voltage-driven
  (negative→positive potential favours urate efflux) [PMID:18701466 "The transport was Na(+)-independent and enhanced at high concentrations of extracellular potassium favoring negative to positive potential direction"]. The authors proposed renaming it URATv1 (voltage-driven urate transporter 1).
- **NOT a proton symporter / active transporter.** The original 2000 cloning paper placed it in the "facilitative glucose transporter family" by homology [PMID:10860667 "Several lines of evidence suggest the existence of additional members of the mammalian facilitative glucose transporter family"]. The old GOA row GO:0005351 carbohydrate:proton symporter activity (NAS) and its inter-ontology IEA consequence GO:1902600 proton transmembrane transport are **wrong-mode** for a facilitative GLUT and contradicted by the mechanism actually reported.

## Sugar transport is residual/secondary and disputed

- Urate is transported 45–60× faster than glucose [PMID:18842065 "urate is transported by SLC2A9 at rates 45- to 60-fold faster than glucose"].
- GLUT9 has low-affinity deoxyglucose transport [PMID:14739288 "GLUT9 appears to be a functional isoform with low affinity for deoxyglucose"]. Fructose and glucose transporter activity was reported by IDA (PMID:18842065).
- UniProt FUNCTION: "May have a residual high-affinity, low-capacity glucose and fructose transporter activity". UniProt CAUTION: "another group could not confirm transporter activity for glucose or fructose (PubMed:28083649)".
- Does NOT transport galactose (UniProt, PMID:28083649) and does NOT transport vitamin C/ascorbate [PMID:36749388 "neither URAT1, GLUT9, nor ABCG2 could transport vitamin C"].
- Conclusion: glucose/fructose transporter activity is a genuine but minor, inherited GLUT-family secondary activity of uncertain physiological relevance → KEEP_AS_NON_CORE (not the gene's core).

## Localization / isoforms (vectorial renal urate reabsorption)

Two splice variants differing only in the N-terminus:
- **Isoform 1 (Q9NRM0-1; SLC2A9-L, SLC2A9a, GLUT9):** 540 aa; **basolateral** membrane of proximal tubule cells [PMID:14739288; PMID:24409316 "SLC2A9-L was expressed at the basolateral membrane of proximal tubules, which were positive for LTL"]. Likely responsible for urate reabsorption (urate exit to blood) [PMID:24409316].
- **Isoform 2 (Q9NRM0-2; SLC2A9-S, SLC2A9b, GLUT9ΔN):** 512 aa; **apical** membrane of collecting ducts / polarized renal cells [PMID:24409316 "SLC2A9-S was expressed at the apical membrane of collecting ducts, which were stained with DBA"].
- Model: urate reabsorbed from urine via apical URAT1 (SLC22A12) and exits basolaterally via GLUT9 [PMID:18701466 "urate is taken up via apically located URAT1 and exits the cell via basolaterally located GLUT9"].
- Plasma membrane localization confirmed by subcellular fractionation of human kidney [PMID:14739288 "subcellular fractionation of human kidney revealed the GLUT9 protein in plasma membranes"].

## Disease / genetics

- GWAS: common SLC2A9 variants are among the strongest determinants of serum urate and gout risk [PMID:18834626; PMID:19503597 "the common variants associated with serum uric acid levels fall in the following nine regions: SLC2A9 (p = 5.2x10(-201))"; PMID:20053405; pronounced sex-specific effects, UniProt POLYMORPHISM].
- Loss-of-function SLC2A9 variants cause renal hypouricemia type 2 (RHUC2, MIM:612076) with high urinary urate excretion (UniProt DISEASE; PMID:18701466 and multiple RHUC2 reports in UniProt).

## GO review decisions (high level)

- **Core:** GO:0015143 urate transmembrane transporter activity (ACCEPT), GO:0015747 urate transport (ACCEPT), plasma-membrane localizations (ACCEPT), basolateral/apical PM (ACCEPT, isoform-tagged).
- **Wrong-mode:** GO:0005351 carbohydrate:proton symporter activity → MODIFY to GO:0055056 (facilitative); GO:1902600 proton transmembrane transport → REMOVE (wrong-mode IEA consequence; GLUT9 does not transport protons).
- **Non-core sugar activity:** fructose/glucose MF+BP IDA/IBA/IEA rows → KEEP_AS_NON_CORE; dehydroascorbic acid transport IBA → KEEP_AS_NON_CORE (family-inherited, no GLUT9-specific evidence; note GLUT9 does not transport reduced vitamin C).
- **Root/too-general:** GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport → TOO_GENERAL (entailed by the specific urate activity). GO:0016020 membrane → MODIFY to GO:0005886 plasma membrane.
- **Systemic urate phenotype (GWAS IMP):** GO:0046415 urate metabolic process → KEEP_AS_NON_CORE (metabolic branch; GLUT9 influences systemic urate *levels* via transport but does not chemically metabolize urate; no "urate homeostasis" GO term exists — flagged as a question).

## Ontology gap noted
No GO term for "urate homeostasis" (the systemic-level phenotype captured by the GWAS IMP rows); urate transport (GO:0015747) and urate metabolic process (GO:0046415) sit in different branches (transport/localization vs metabolism). Flagged in suggested_questions.
