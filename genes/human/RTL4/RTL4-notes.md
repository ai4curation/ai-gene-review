# RTL4 / SIRH11 / ZCCHC16 (Q6ZR62) notes

X-linked domesticated sushi-ichi Gag gene; C-terminal CCHC knuckle (res 278-295), no catalytic domains; predicted nucleic-acid binder [PMID:16093683].
Brain gene via noradrenergic system (mouse ortholog) [PMID:26402067]. Human disease: rare complete knockout of ZCCHC16 in autism cases only [PMID:23352160 "4 genes with rare complete knockouts (PTH2R, MECP2, VSIG1 and ZCCHC16) observed in cases only"]; reviewed as ASD causative [PMID:39769499 "a causative gene in autism spectrum disorder"].
HuRI AGR2 interaction (single Y2H) -> REMOVE (protein-binding policy).
Calls: nucleic acid binding ACCEPT; zinc ion binding ACCEPT; protein binding REMOVE.
No human-specific OpenScientist file (family report is in mouse/Rtl4).

## Deep research integration (OpenScientist, 2026-10-24)

A human RTL4 OpenScientist report has now arrived (RTL4-deep-research-openscientist.md). Checked against cached sources; no contradiction with the review calls.

- Synonym: UniProt Q6ZR62 lists "Synonyms=MAR3, MART4"; the description said MAR4. Corrected to MAR3/MART4 (the report has MAR3).
- NA-specific microdialysis deficit in mouse KO [PMID:26402067 "the recovery rate of noradrenaline (NA) was reduced compared with dopamine (DA) after perfusion of high potassium-containing artificial cerebrospinal fluid in knockout (KO) mice"]. Added to core function support.
- Microglial, noradrenaline-responsive expression from the Rtl4-Venus knock-in, summarized in [PMID:42511665 "Analyses using KI mice expressing a SIRH11/RTL4-Venus fusion protein from the endogenous Sirh11/Rtl4 locus revealed that SIRH11/RTL4 is predominantly expressed in the hypothalamus, midbrain, and amygdala"]; the same review proposes nucleic-acid (DAMP) clearance through the "conserved C-terminal CCHC RNA-binding motif". Added as extra support on the nucleic acid binding row (a hypothesis, so the general term stays).
- The report's EV/multivesicular-body secretion route is inferred from Arc [PMID:29328916, PMID:39178227] and not shown for RTL4; not used for annotation.
- The report's Human Protein Atlas expression numbers were not checked against a primary source and are not used.

No action changes. Cross-species: the mouse Rtl4 review carries extracellular region, cognition and norepinephrine metabolic process; human GOA has none of these and I did not add NEW terms. A curator may wish to consider whether ISO transfer to human is wanted.
