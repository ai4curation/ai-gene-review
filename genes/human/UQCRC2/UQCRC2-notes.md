# UQCRC2 (P22695) — review notes

## Identity
- UniProtKB:P22695, HGNC:12586, GeneID 7385, chr 16p12.
- Names: Cytochrome b-c1 complex subunit 2, mitochondrial; Complex III subunit 2; Core protein II; Ubiquinol-cytochrome-c reductase complex core protein 2 (QCR2).
- 453 aa precursor; N-terminal transit peptide (1..14) cleaved; mature chain 15..453.

## Core biology (verified)
- One of the **two large "core" subunits (UQCRC1/core 1 and UQCRC2/core 2)** of mitochondrial respiratory **Complex III** (cytochrome bc1 / ubiquinol–cytochrome c reductase, CIII) of the electron transport chain. CIII is an 11-subunit obligate dimer in the inner membrane.
- Complex III transfers electrons from ubiquinol to cytochrome c and pumps protons (protonmotive Q cycle): the catalytic redox centres reside in **cytochrome b (MT-CYB), the Rieske Fe-S protein UQCRFS1, and cytochrome c1 (CYC1)** — NOT in the core proteins. UQCRC2 is a **non-catalytic structural subunit** required for assembly/stability of the complex. [file:human/UQCRC2/UQCRC2-uniprot.txt "The cytochrome b-c1 complex catalyzes electron transfer from ubiquinol to cytochrome c, linking this redox reaction to translocation of protons across the mitochondrial inner membrane"]
- Location: mitochondrial inner membrane, peripheral membrane protein on the matrix side. [file:human/UQCRC2/UQCRC2-uniprot.txt "Mitochondrion inner membrane"]
- CIII forms supercomplexes/respirasomes with CI and CIV (SCI1III2IV1, megacomplex MCI2III2IV2). [PMID:28844695]

## M16 peptidase fold — pseudo-peptidase
- UQCRC1/UQCRC2 belong to the **peptidase M16 family (UQCRC2/QCR2 subfamily)** and are structurally homologous to the two mitochondrial-processing peptidase (MPP) subunits (α-MPP/β-MPP). [file:human/UQCRC2/UQCRC2-uniprot.txt "Belongs to the peptidase M16 family. UQCRC2/QCR2 subfamily."]
- **UQCRC2 has lost the catalytic M16 inverted zinc-binding motif (HXXEH).** A scan of the mature sequence finds no HXXEH; the closest match (HVIEN at ~172) has N (not H) at the final position and lacks the downstream catalytic His. So the InterPro/PROSITE-derived IEA terms *metalloendopeptidase activity* (GO:0004222), *proteolysis* (GO:0006508), and *metal ion binding* (GO:0046872) reflect the **fold**, not a demonstrated catalytic activity in human. UniProt hedges: catalytic MPP properties "seem to have [been] preserved (By similarity)" and UQCRC2 "May be involved in the in situ processing of UQCRFS1 ... (Probable)". [file:human/UQCRC2/UQCRC2-uniprot.txt "May be involved in the in situ processing of UQCRFS1 into the mature Rieske protein and its mitochondrial targeting sequence (MTS)/subunit 9 when incorporated into complex III"]
- PAN-GO/GO_Central assigns UQCRC2 only *mitochondrion* + *respiratory chain complex III* (IBA) — no catalytic MF — consistent with a structural role. Reactome R-HSA-9906017 lists UQCRC1/UQCRC2 only as **possible** candidates for the UQCRFS1-cleaving peptidase ("as hinted at in the cattle model").
- Curation call: mark the catalytic InterPro IEAs as over-annotations (fold-based), do NOT assign a catalytic MF in core_functions; MF is minimal/structural.

## Disease
- Biallelic UQCRC2 variants cause **Mitochondrial complex III deficiency, nuclear type 5 (MC3DN5; MIM 615160)** — neonatal-onset recurrent metabolic decompensation, encephalopathy, lactic acidosis, hypoglycemia, liver/renal involvement. [file:human/UQCRC2/UQCRC2-uniprot.txt "Mitochondrial complex III deficiency, nuclear type 5 (MC3DN5)"]; original report PMID:23281071 (R183W), not cached (abstract-only).

## Annotation-by-annotation curation summary
- **CC mitochondrion / mitochondrial inner membrane / respiratory chain complex III** (multiple IBA/IEA/IDA/ISS/TAS/HTP/HDA): all ACCEPT (well supported; CIII inner-membrane subunit). Inner membrane + CIII are the informative/core CC terms; bare `mitochondrion` kept as accurate-but-general.
- **BP mitochondrial electron transport, ubiquinol to cytochrome c (GO:0006122)** NAS: ACCEPT — this is the core process CIII performs; UQCRC2 is a required structural subunit.
- **BP oxidative phosphorylation / aerobic respiration / cellular respiration**: ACCEPT (accurate high-level respiration processes; keep the most specific, GO:0006122, as core).
- **MF metalloendopeptidase activity (GO:0004222)** IEA InterPro: MARK_AS_OVER_ANNOTATED — fold-based; catalytic zinc motif lost in human UQCRC2; no experimental peptidase activity demonstrated.
- **MF metal ion binding (GO:0046872)** IEA InterPro: MARK_AS_OVER_ANNOTATED — same reason (predicted zinc-binding of M16 fold; catalytic site degenerate).
- **BP proteolysis (GO:0006508)** IEA InterPro: MARK_AS_OVER_ANNOTATED — depends on the (unproven) peptidase activity.
- **MF protein binding (GO:0005515)** IPI ×6 references (IntAct/UniProt interactome + mitolamban): MARK_AS_OVER_ANNOTATED per curation policy (bare `protein binding` uninformative; many are high-throughput/PDZ-domain interactome hits of unclear physiological relevance). The mitolamban (P0DP99) and RAB5IF (Q9BUV8) interactions are biologically plausible CIII-assembly-related but the term itself is uninformative.

## Core functions (final)
- MF: none catalytic. UQCRC2 acts as a **structural subunit** of CIII — no GOA MF term captures this well (GOA MF terms are the over-annotated M16/binding IEAs). Leave core_functions MF empty (do not invent structural molecule activity, which is not in GOA); represent role via BP + CC + in_complex.
- BP: GO:0006122 mitochondrial electron transport, ubiquinol to cytochrome c.
- CC: located_in GO:0005743 mitochondrial inner membrane; in_complex GO:0045275 respiratory chain complex III.
</content>
</invoke>
