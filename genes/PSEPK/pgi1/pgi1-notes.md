# pgi1 (Glucose-6-phosphate isomerase 1) — Pseudomonas putida KT2440

UniProt: Q88LW9 (G6PI1_PSEPK); locus PP_1808; 554 aa; EC 5.3.1.9.
Evidence level: PE 3 (Inferred from homology). All UniProt functional annotation is propagated from HAMAP-Rule MF_00473; no gene-specific experimental papers found for this locus.

## FUNCTION
Pgi catalyzes the reversible aldose-ketose isomerization of glucose-6-phosphate and fructose-6-phosphate, interconverting the two hexose-phosphate pools.

- [UniProt "Catalyzes the reversible isomerization of glucose-6-phosphate to fructose-6-phosphate."]
- [UniProt "RecName: Full=Glucose-6-phosphate isomerase 1"]
- [UniProt "AltName: Full=Phosphoglucose isomerase 1"]
- [UniProt "AltName: Full=Phosphohexose isomerase 1"]

## CATALYTIC ACTIVITY
Reaction: alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate (RHEA:11816), EC 5.3.1.9.

- [UniProt "Reaction=alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate;"]
- [UniProt "EC=5.3.1.9"]

Three predicted catalytic active-site residues (proton-relay isomerization mechanism): His/Glu/Lys-type residues at positions 359 (proton donor), 390, 518.
- [UniProt "ACT_SITE        359"]
- [UniProt "/note=\"Proton donor\""]

## PATHWAY
UniProt assigns Pgi to two carbohydrate pathways by homology:
- Gluconeogenesis (Carbohydrate biosynthesis).
  - [UniProt "Carbohydrate biosynthesis; gluconeogenesis."]
- Glycolysis (EMP), G3P + DHAP from D-glucose, step 2/4.
  - [UniProt "Carbohydrate degradation; glycolysis; D-glyceraldehyde 3-phosphate and glycerone phosphate from D-glucose: step 2/4."]

### Pathway context in P. putida KT2440 (important caveat)
P. putida KT2440 does NOT use the Embden-Meyerhof-Parnas (EMP/glycolysis) pathway for glucose catabolism. Glucose is degraded almost exclusively via the Entner-Doudoroff (ED) pathway (and the cyclic EDEMP variant); the EMP-specific enzyme 6-phosphofructokinase (Pfk) is essentially absent/non-functional, so net glycolytic flux from glucose through fructose-6-phosphate to fructose-1,6-bisphosphate does not occur. The genome paper describes KT2440 as metabolically versatile but lacking a complete EMP route.
- [PMID:12534463 "Complete genome sequence and comparative analysis of the metabolically versatile Pseudomonas putida KT2440"]

Consequently, in KT2440 the physiologically relevant direction of Pgi is gluconeogenic / anabolic: converting fructose-6-phosphate (generated from ED-pathway triose/hexose intermediates) into glucose-6-phosphate to supply hexose-phosphate-derived biosynthesis (e.g. LPS, peptidoglycan, glycogen precursors, and the EDEMP recycling node). Pgi connects the fructose-6-phosphate and glucose-6-phosphate pools and feeds the oxidative pentose-phosphate / G6P branch.

The generic "glycolytic process" (GO:0006096) BP term is a HAMAP/UniRule homology transfer reflecting the canonical role of Pgi in the EMP pathway of organisms that run glycolysis. It is not an accurate representation of the in vivo physiological role of this enzyme in KT2440, which routes glucose through ED rather than EMP. It should be treated as an over-annotation (true at the generic enzyme-class level, but not the relevant biology for this organism).

## SUBCELLULAR LOCATION
Cytoplasm (soluble enzyme acting on phosphorylated sugar intermediates).
- [UniProt "SUBCELLULAR LOCATION: Cytoplasm"]

## FAMILY / DOMAINS
Belongs to the GPI family (COG0166; Pfam PF00342 PGI; SIS domains; HAMAP MF_00473). Substrate-binding involves the phosphosugar (carbohydrate derivative / monosaccharide binding).
- [UniProt "Belongs to the GPI family."]
- [UniProt "Pfam; PF00342; PGI"]

## CURATION SUMMARY (per annotation)
- GO:0004347 glucose-6-phosphate isomerase activity (MF) — ACCEPT; exact core catalytic function, matches EC 5.3.1.9 and UniProt name.
- GO:0006094 gluconeogenesis (BP) — ACCEPT; physiologically relevant anabolic role in KT2440; UniProt pathway.
- GO:0051156 glucose 6-phosphate metabolic process (BP) — ACCEPT; specific and accurate (Pgi produces/consumes G6P).
- GO:0006096 glycolytic process (BP) — MARK_AS_OVER_ANNOTATED; KT2440 uses ED not EMP; homology transfer, not in-vivo glycolytic flux.
- GO:0005737 cytoplasm (CC) — ACCEPT; soluble cytoplasmic enzyme.
- GO:0005829 cytosol (CC) — ACCEPT (more specific CC); consistent with cytoplasm.
- GO:0048029 monosaccharide binding (MF) — KEEP_AS_NON_CORE; substrate (G6P/F6P) binding; subsumed by catalytic activity, generic.
- GO:0097367 carbohydrate derivative binding (MF) — MARK_AS_OVER_ANNOTATED; very broad binding parent, uninformative when catalytic MF present.
- GO:1901135 carbohydrate derivative metabolic process (BP) — MARK_AS_OVER_ANNOTATED; broad parent of glucose-6-phosphate metabolic process.
