# SLC2A2 (GLUT2, P11168) — curation notes

## Identity and family
- Solute carrier family 2, facilitated glucose transporter member 2 (GLUT2). HGNC:11006. 524 aa, 12 TM helices (UniProt P11168 topology).
- Major facilitator superfamily (MFS), Sugar transporter (TC 2.A.1.1) family, Glucose transporter subfamily (Class I GLUTs: GLUT1-4). PANTHER PTHR23503:SF27. [UniProt P11168 SIMILARITY; DR CDD cd17431 MFS_GLUT_Class1]
- **Facilitative (uniporter) transporter — facilitated diffusion, energy-independent, NOT Na+-coupled.** UniProt RecName "facilitated glucose transporter member 2"; FUNCTION "Facilitative hexose transporter". Distinguish from the apical SGLT1 (SLC5A1) Na+/glucose symporter.

## Transport function (substrates)
- **Glucose, fructose, galactose** — classic hexose substrates, demonstrated in Xenopus oocytes. [PMID:8457197 "GLUT2 mediates the transport of fructose and galactose"; low-affinity/high-capacity; Km(deoxyglucose)=11.2 mM, Km(galactose)=85.5 mM, Km(fructose)=66.7 mM per UniProt kinetics]
- Reconfirmed glucose + fructose transport in oocytes. [PMID:28083649 "In assessing whether human GLUT2, GLUT5, GLUT7, and GLUT9 are indeed fructose transporters, we expressed these proteins in Xenopus laevis oocytes"; p.I322V reduces fructose transport]
- Glucose + fructose transport inhibited by flavonoids (quercetin, EGCG, apigenin). [PMID:29548810 "GLUT2-mediated glucose and fructose transport were inhibited by quercetin, (-)-epigallocatechin gallate (EGCG) and apigenin"]
- **Dehydroascorbic acid (DHA, oxidized vitamin C)** — genuine secondary substrate, Km=3.23 mM. [PMID:23396969 "Only GLUT2 and GLUT8, known to be expressed in intestines, transported DHA with apparent transport affinities (Km) of 2.33 and 3.23 mm"]
- **Urate** — newly demonstrated (2025) bidirectional urate transport; GWAS-linked to serum urate. Km(urate)=4.6 mM. [PMID:40209957 "The present study revealed that GLUT2 is a bi-directional urate transporter"; urate uptake into GLUT2-expressing 293A cells inhibited by GLUT2 inhibitors; efflux also demonstrated]
- Also listed: glucosamine (DrugBank DB01296, not independently reviewed here).
- **Bidirectional**: UniProt FUNCTION "Likely mediates the bidirectional transfer of glucose across the plasma membrane of hepatocytes" — exports glucose from hepatocytes (gluconeogenesis/glycogenolysis) and imports in intestine/kidney/β-cell.

## Localization
- **Plasma membrane** — core location. Direct evidence: [PMID:28083649 subcellular location]; [PMID:40209957]; HPA immunofluorescence (GO_REF:0000052); multiple Reactome/TAS rows.
- In polarized epithelia (enterocytes, renal proximal tubule), GLUT2 is **basolateral** (textbook; pairs with apical SGLT1 for transcellular sugar absorption — UniProt FUNCTION "May also participate with the Na(+)/glucose cotransporter in the transcellular transport of glucose in the small intestine and kidney").
- Apical/brush-border GLUT2: a conditional, debated phenomenon (Kellett "apical GLUT2" hypothesis — transient recruitment under high luminal glucose). Not the canonical steady-state location; GOA brush-border and apical-PM rows are IBA/ortholog over-propagation of this conditional/non-core location. Judged MARK_AS_OVER_ANNOTATED.
- "cytoplasm" (IEA, mouse ortholog) and "cell-cell junction" (IEA, mouse ortholog) are not established GLUT2 locations — over-annotation of an integral PM protein.

## Physiology / disease
- Expressed in liver, pancreatic β-cells, basolateral intestine and kidney. [UniProt TISSUE SPECIFICITY; HPA "Tissue enriched (liver)"]
- Rodent β-cell glucose sensor (part of glucose-stimulated insulin secretion); in humans GLUT1/GLUT3 carry more of the β-cell glucose uptake, so the rodent-derived "positive regulation of insulin secretion" IEA is a downstream/indirect physiological role, not GLUT2's molecular core. GLUT2 transports the glucose; the insulin-secretion machinery (glucokinase, K_ATP, exocytosis) performs the regulation. [UniProt FUNCTION "may comprise part of the glucose-sensing mechanism of beta cells (PubMed:8027028)"]
- **Fanconi-Bickel syndrome** (FBS, MIM:227810): autosomal recessive; hepatorenal glycogen accumulation, proximal renal tubular dysfunction, impaired glucose/galactose utilization. FBS variants: p.L389P, p.V423E, p.P417L. [UniProt DISEASE; PMID:10987651; PMID:11044475]
- NIDDM variant p.V197I abolishes transport activity in oocytes. [PMID:8027028 "the highly conservative valine 197-->isoleucine amino acid change abolished transport activity of the Glut2 transporter expressed in Xenopus oocytes"]

## Review decisions summary
- Core MF: D-glucose / fructose / galactose / dehydroascorbic-acid transmembrane transporter activities (all IDA-supported). NEW urate transmembrane transporter activity (GO:0015143) from PMID:40209957.
- Core BP: the matching transmembrane transport processes + D-glucose import across PM; NEW urate transport (GO:0015747).
- TOO_GENERAL: hexose transmembrane transporter activity, transmembrane transporter activity, transmembrane transport (all entailed by accepted specific terms).
- MODIFY: membrane -> plasma membrane (both rows).
- MARK_AS_OVER_ANNOTATED: cytoplasm, cell-cell junction, brush border, apical plasma membrane, carbohydrate metabolic process.
- KEEP_AS_NON_CORE: positive regulation of insulin secretion involved in cellular response to glucose stimulus (indirect physiological role, rodent-derived IEA).
