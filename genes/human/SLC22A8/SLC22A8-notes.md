# SLC22A8 (OAT3, hOAT3) — curation notes

UniProt: Q8TCC7 · HGNC:10972 · Organic anion transporter 3 · MFS superfamily (TC 2.A.1.19.34)

## Summary of function

SLC22A8/OAT3 is the principal **basolateral organic anion uptake transporter** of the
renal proximal tubule, and the first (blood-to-cell) step of renal organic anion secretion.
It is a **tertiary-active organic anion/dicarboxylate antiporter**: it exchanges extracellular
organic anion uptake for efflux of intracellular dicarboxylate (chiefly 2-oxoglutarate/
alpha-ketoglutarate or glutarate). The outwardly directed dicarboxylate gradient is maintained
by Na(+)-dicarboxylate cotransporters (NaDC3/SLC13A3) that use the inward Na(+) gradient set by
the Na(+)/K(+)-ATPase; OAT3 itself is thus coupled to the Na(+) gradient only indirectly and is
not a Na(+)- or proton-symporter [UniProtKB:Q8TCC7 CC:FUNCTION, "organic anion/dicarboxylate exchanger that couples organic anion uptake indirectly to the sodium gradient"].

- Mechanism / exchanger: "Human organic anion transporter 3 (hOAT3) can operate as an exchanger and mediate secretory urate flux" [PMID:14586168 title]. UniProt records the explicit exchange reactions, e.g. urate(in) + 2-oxoglutarate(out) and estrone-3-sulfate(out) + glutarate(in) [UniProtKB:Q8TCC7 CATALYTIC ACTIVITY, Rhea:72403/72151].
- Broad substrate range (endogenous): urate/uric acid, estrone-3-sulfate (E1S), DHEA-sulfate, cortisol, prostaglandins E2/F2alpha, cAMP, the tryptophan metabolites kynurenate and xanthurenate, uremic toxins (indoxyl sulfate, indole-acetate, hippurate, CMPF), and biopterins (BH4, BH2, sepiapterin) [UniProtKB:Q8TCC7 CC:FUNCTION].
- Broad substrate range (xenobiotic/drug): methotrexate, NSAIDs, beta-lactam antibiotics (benzylpenicillin, cephalosporins), loop/thiazide diuretics, antivirals (acyclovir, zidovudine), statins (pravastatin, pitavastatin), fexofenadine, cimetidine, PAH, 2,4-D, ochratoxin A [UniProtKB:Q8TCC7 CC:FUNCTION; DrugBank cross-references].
- Prostaglandins: "PGE(2) and PGF(2 alpha) transport in the basolateral membrane of the proximal tubule is mediated by multiple pathways including hOAT1, hOAT2, hOAT3, and hOCT2" [PMID:11907186 abstract]; K_m(PGE2 by hOAT3) = 345 nM.
- Biopterins: "Both OAT1 and OAT3 ... OAT1 and OAT3 preferred BH2 and sepiapterin" and the transporters are "crucial biopterin transporters involved in bodily distribution of tetrahydrobiopterin and exclusion of its excess" [PMID:28534121].
- Uremic toxins: OAT3 contributes to renal uptake of indoxyl sulfate, indole-acetate, hippurate and CMPF [PMID:14675047 title + UniProtKB:Q8TCC7 CC:FUNCTION; CATALYTIC ACTIVITY Rhea:75987/75983/75991/75995].

## Location

- Basolateral membrane of proximal tubular cells: "Localizes to the basolateral membrane of the proximal tubular cells" [UniProtKB:Q8TCC7 CC:SUBCELLULAR LOCATION]; "Basolateral cell membrane". Directly shown by immunolocalization (PMID:11306713, PMID:11912245, PMID:27053689) and by ISS from rat Oat3 (PMID:18619525).
- Also at the choroid plexus (brush-border of choroid epithelium) and brain-capillary endothelium (blood–brain barrier, abluminal and possibly luminal), where it clears organic anions from CSF/brain to blood [UniProtKB:Q8TCC7 CC:SUBCELLULAR LOCATION note; PMID:26590417 NAS].
- Retinal pigment epithelium: both apical and basolateral membranes by quantitative proteomics (PMID:31791063). Apical localization is tissue-specific; the core renal location is basolateral.
- Detected in urinary exosomes by proteomics (HDA, PMID:19056867) — consistent with a shed plasma-membrane protein; not a functional site.

## Tissue specificity

"Strongly expressed in kidney ... Weaker expression in brain and skeletal muscle ... Expressed in adrenal glands" [UniProtKB:Q8TCC7 CC:TISSUE SPECIFICITY]; HPA group-enriched in choroid plexus and kidney.

## Physiological roles (participation vs necessity)

OAT3 *performs* organic anion transmembrane transport (it is the transporter). Higher-level
processes it is *necessary* for but does not itself execute the chemistry of — renal secretion,
systemic drug disposition, urate homeostasis, blood–brain-barrier clearance — are therefore
non-core context, not the molecular function. Loss-of-function variants (R149S, I260R complete
loss; R277W, I305F reduced) alter drug pharmacokinetics (PMID:16291576, PMID:12811365 pravastatin).

## GO term / ontology notes

The obvious grouping MF terms are **obsolete** and must not be used in `core_functions`
(verified via QuickGO 2026-11-15):
- GO:0008514 "organic anion transmembrane transporter activity" — OBSOLETE
- GO:0015347 "sodium-independent organic anion transmembrane transporter activity" — OBSOLETE
- GO:0015301 "anion:anion antiporter activity" — OBSOLETE
- GO:0015711 "organic anion transport" (BP) — OBSOLETE

Non-obsolete terms used instead:
- **GO:0015297 antiporter activity** (MF; is_a GO:0015291 secondary active transmembrane transporter activity) — the accurate, present mechanism term for the organic-anion:dicarboxylate exchange. Core.
- **GO:0042910 xenobiotic transmembrane transporter activity** (MF, present IDA) — drug/toxin elimination. Core.
- **GO:0015143 urate transmembrane transporter activity** (MF, non-obsolete) — proposed NEW row; urate secretion is a defining, well-supported OAT3 function absent from GOA.
- **GO:0015132 prostaglandin transmembrane transporter activity** / GO:0015732 prostaglandin transport — genuine but minor substrate class (non-core).
- **GO:0042908 xenobiotic transport** (BP, present) — non-core process consequence.

GO:0005452 "solute:**inorganic** anion antiporter activity" (IDA, PMID:15037815) is an inaccurate
term for OAT3: the counter-substrate it exchanges is the **organic** dicarboxylate
2-oxoglutarate/glutarate, not an inorganic anion. MODIFY (generalize) to the supported parent
GO:0015297 antiporter activity, which OAT3 already carries (IEA from mouse Oat3 O88909).

No non-obsolete MF covers the *broad* organic-anion:dicarboxylate exchange as a substrate-class
function; proposing "organic anion:dicarboxylate antiporter activity" (parent GO:0015297) to fill
the gap left by the obsoletions (mirrors the SLCO2B1 steroid-sulfate proposal).

## Key references (abstract-only unless noted)

- PMID:14586168 (NOT cached) — OAT3 operates as an exchanger, secretory urate flux. Mechanism basis; relied on via UniProt ECO:0000269 statements.
- PMID:11907186 — prostaglandin transport, basolateral proximal tubule.
- PMID:14675047 — uremic toxin transport.
- PMID:11669456 — ochratoxin A transport (xenobiotic).
- PMID:22108572 / PMID:23832370 — kynurenate / xanthurenate transport.
- PMID:28534121 (full text) — biopterin transport.
- PMID:26377792 — OAT2 vs OAT1/3; E1S pH/Cl-dependence.
- PMID:27053689 / PMID:31791063 / PMID:18619525 — localization (nephron, RPE, BBB).
</content>
