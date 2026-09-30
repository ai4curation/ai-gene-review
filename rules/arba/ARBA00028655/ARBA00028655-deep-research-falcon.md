---
title: ARBA00028655 (GO:0006661 phosphatidylinositol biosynthetic process) rule research
keywords:
- ARBA00028655
- GO:0006661
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T06:25:00.594947'
end_time: '2026-08-15T06:38:10.181972'
duration_seconds: 789.59
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: ARBA00028655-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Research request: is GO:0006661 "phosphatidylinositol biosynthetic process" the correct GO Biological Process term for these enzyme families?

I am evaluating a UniProt ARBA automatic-annotation rule (ARBA00028655) that assigns
**GO:0006661 "phosphatidylinositol biosynthetic process"** to proteins matching any of 25
alternative condition sets. Please research the biochemistry and answer precisely, with
citations to primary literature and reviews.

## Background definitions I need adjudicated

1. In the strict biochemical sense, which reaction(s) constitute *de novo* **phosphatidylinositol (PI)
   biosynthesis** in eukaryotes? Please describe the CDP-DAG pathway
   (CDS1/CDS2 → CDP-diacylglycerol; PIS/CDIPT, EC 2.7.8.11, CDP-diacylglycerol--inositol
   3-phosphatidyltransferase) and where it occurs (ER / PI-synthase-containing mobile
   membrane compartment). Which enzymes are the *only* ones that actually form the
   PI molecule itself?

2. **Phosphoinositide kinases** — PI3K class I/II/III (PIK3CA/PIK3CB/PIK3CG, PIK3C2A/B/G,
   PIK3C3/VPS34), PI4K (PI4KB), PIP5K (PIP5K1A/B/C, its3 in fission yeast), PIP4K
   (PIP4K2A/B/C). Do these enzymes synthesize *phosphatidylinositol*, or do they
   *phosphorylate pre-existing PI / PIPs* to make phosphatidylinositol **phosphates**
   (PI3P, PI4P, PI(4,5)P2, PI(3,4,5)P3)? Is it biochemically accurate to describe them as
   participating in "phosphatidylinositol biosynthetic process", or should they be described by
   terms such as "phosphatidylinositol phosphorylation" / "phosphatidylinositol-mediated
   signaling" / "phosphatidylinositol phosphate biosynthetic process"?

3. **Phosphoinositide phosphatases** — myotubularins (MTM1, MTMR1-4; PTP-like /
   Tyrosine-specific protein phosphatase domain IPR000387 + myotubularin phosphatase domain
   IPR010569), SAC-domain phosphatases (SACM1L/Sac1, synaptojanin SYNJ1/2; SAC domain
   IPR002013), and inositol polyphosphate 5-phosphatases (INPP5D/SHIP1). What reactions do
   they catalyse? MTM1/MTMR2 dephosphorylate PI3P and PI(3,5)P2 — does the product
   (phosphatidylinositol) mean these should be considered part of "phosphatidylinositol
   biosynthetic process", or are they conventionally regarded as phosphoinositide turnover /
   dephosphorylation / catabolic enzymes? What is the standard GO/curatorial treatment?

4. **GPI-anchor biosynthesis enzymes** — PIGL (N-acetylglucosaminyl-phosphatidylinositol
   de-N-acetylase), PIGN/PIGO/PIGG (GPI ethanolamine phosphate transferases), PGAP5/MPPE1
   (metallophosphoesterase), and **DPM1 (dolichol-phosphate mannose synthase subunit 1)**.
   These act *downstream* of PI, using PI as an acceptor substrate. Do any of them
   participate in the synthesis of the PI molecule? Is DPM1 (which makes
   dolichol-phosphate-mannose, a mannosyl donor for GPI anchoring and protein N-/O-/C-
   mannosylation) involved in phosphatidylinositol biosynthesis in any sense? Please be
   explicit about whether annotating DPM1 to GO:0006661 is supportable.

5. **UVRAG** — is it a phosphoinositide-metabolising enzyme, or a regulatory subunit of the
   PI3KC3/Beclin-1 complex? What is the appropriate way to describe its relationship to
   PI3P production?

6. **PI3K regulatory subunits** (PIK3R1/p85 alpha) — do they have catalytic activity?

## Specific question about the GO ontology

7. In the Gene Ontology, how is **GO:0006661 phosphatidylinositol biosynthetic process**
   defined, and how does it relate to:
   - GO:0046488 phosphatidylinositol metabolic process
   - GO:0046854 phosphatidylinositol phosphorylation
   - GO:0046474 glycerophospholipid biosynthetic process
   - GO:0006506 GPI anchor biosynthetic process
   - GO:0048015 phosphatidylinositol-mediated signaling
   Are phosphatidylinositol *phosphates* (phosphoinositides) considered "phosphatidylinositol"
   for the purposes of this term? Is there a distinct term for phosphatidylinositol-phosphate
   biosynthesis? Has the GO consortium discussed over-annotation of PI kinases/phosphatases to
   GO:0006661?

## Taxonomic questions

8. Is the CDP-DAG → PI route (PIS/CDIPT) conserved across eukaryotes, and is it present in
   fission yeast *Schizosaccharomyces pombe*? Which *S. pombe* gene encodes PI synthase?
   Does *S. pombe* dpm1 (SPAC31G5.16c) have any role in PI synthesis?

9. Is PI synthase activity present in bacteria/archaea (e.g. *Mycobacterium* PgsA1) —
   i.e. is a "Eukaryota" restriction appropriate?

## Deliverable

Please give a per-family verdict table: family → actual reaction → whether "phosphatidylinositol
biosynthetic process" (GO:0006661) is a correct, over-broad, or outright incorrect description,
and the better GO term if any. Cite primary literature (PMIDs) and authoritative reviews.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Research request: is GO:0006661 "phosphatidylinositol biosynthetic process" the correct GO Biological Process term for these enzyme families?

I am evaluating a UniProt ARBA automatic-annotation rule (ARBA00028655) that assigns
**GO:0006661 "phosphatidylinositol biosynthetic process"** to proteins matching any of 25
alternative condition sets. Please research the biochemistry and answer precisely, with
citations to primary literature and reviews.

## Background definitions I need adjudicated

1. In the strict biochemical sense, which reaction(s) constitute *de novo* **phosphatidylinositol (PI)
   biosynthesis** in eukaryotes? Please describe the CDP-DAG pathway
   (CDS1/CDS2 → CDP-diacylglycerol; PIS/CDIPT, EC 2.7.8.11, CDP-diacylglycerol--inositol
   3-phosphatidyltransferase) and where it occurs (ER / PI-synthase-containing mobile
   membrane compartment). Which enzymes are the *only* ones that actually form the
   PI molecule itself?

2. **Phosphoinositide kinases** — PI3K class I/II/III (PIK3CA/PIK3CB/PIK3CG, PIK3C2A/B/G,
   PIK3C3/VPS34), PI4K (PI4KB), PIP5K (PIP5K1A/B/C, its3 in fission yeast), PIP4K
   (PIP4K2A/B/C). Do these enzymes synthesize *phosphatidylinositol*, or do they
   *phosphorylate pre-existing PI / PIPs* to make phosphatidylinositol **phosphates**
   (PI3P, PI4P, PI(4,5)P2, PI(3,4,5)P3)? Is it biochemically accurate to describe them as
   participating in "phosphatidylinositol biosynthetic process", or should they be described by
   terms such as "phosphatidylinositol phosphorylation" / "phosphatidylinositol-mediated
   signaling" / "phosphatidylinositol phosphate biosynthetic process"?

3. **Phosphoinositide phosphatases** — myotubularins (MTM1, MTMR1-4; PTP-like /
   Tyrosine-specific protein phosphatase domain IPR000387 + myotubularin phosphatase domain
   IPR010569), SAC-domain phosphatases (SACM1L/Sac1, synaptojanin SYNJ1/2; SAC domain
   IPR002013), and inositol polyphosphate 5-phosphatases (INPP5D/SHIP1). What reactions do
   they catalyse? MTM1/MTMR2 dephosphorylate PI3P and PI(3,5)P2 — does the product
   (phosphatidylinositol) mean these should be considered part of "phosphatidylinositol
   biosynthetic process", or are they conventionally regarded as phosphoinositide turnover /
   dephosphorylation / catabolic enzymes? What is the standard GO/curatorial treatment?

4. **GPI-anchor biosynthesis enzymes** — PIGL (N-acetylglucosaminyl-phosphatidylinositol
   de-N-acetylase), PIGN/PIGO/PIGG (GPI ethanolamine phosphate transferases), PGAP5/MPPE1
   (metallophosphoesterase), and **DPM1 (dolichol-phosphate mannose synthase subunit 1)**.
   These act *downstream* of PI, using PI as an acceptor substrate. Do any of them
   participate in the synthesis of the PI molecule? Is DPM1 (which makes
   dolichol-phosphate-mannose, a mannosyl donor for GPI anchoring and protein N-/O-/C-
   mannosylation) involved in phosphatidylinositol biosynthesis in any sense? Please be
   explicit about whether annotating DPM1 to GO:0006661 is supportable.

5. **UVRAG** — is it a phosphoinositide-metabolising enzyme, or a regulatory subunit of the
   PI3KC3/Beclin-1 complex? What is the appropriate way to describe its relationship to
   PI3P production?

6. **PI3K regulatory subunits** (PIK3R1/p85 alpha) — do they have catalytic activity?

## Specific question about the GO ontology

7. In the Gene Ontology, how is **GO:0006661 phosphatidylinositol biosynthetic process**
   defined, and how does it relate to:
   - GO:0046488 phosphatidylinositol metabolic process
   - GO:0046854 phosphatidylinositol phosphorylation
   - GO:0046474 glycerophospholipid biosynthetic process
   - GO:0006506 GPI anchor biosynthetic process
   - GO:0048015 phosphatidylinositol-mediated signaling
   Are phosphatidylinositol *phosphates* (phosphoinositides) considered "phosphatidylinositol"
   for the purposes of this term? Is there a distinct term for phosphatidylinositol-phosphate
   biosynthesis? Has the GO consortium discussed over-annotation of PI kinases/phosphatases to
   GO:0006661?

## Taxonomic questions

8. Is the CDP-DAG → PI route (PIS/CDIPT) conserved across eukaryotes, and is it present in
   fission yeast *Schizosaccharomyces pombe*? Which *S. pombe* gene encodes PI synthase?
   Does *S. pombe* dpm1 (SPAC31G5.16c) have any role in PI synthesis?

9. Is PI synthase activity present in bacteria/archaea (e.g. *Mycobacterium* PgsA1) —
   i.e. is a "Eukaryota" restriction appropriate?

## Deliverable

Please give a per-family verdict table: family → actual reaction → whether "phosphatidylinositol
biosynthetic process" (GO:0006661) is a correct, over-broad, or outright incorrect description,
and the better GO term if any. Cite primary literature (PMIDs) and authoritative reviews.

# Research report: suitability of GO:0006661 for ARBA00028655 families

## Executive conclusion

**No—GO:0006661 is not a biochemically correct blanket annotation for the listed families.** In strict pathway terms, de novo phosphatidylinositol (PI) synthesis is the CDP-diacylglycerol route: ER-localized CDS1/CDS2 produce CDP-DAG from phosphatidic acid and CTP, and phosphatidylinositol synthase, CDIPT/PIS (EC 2.7.8.11), transfers phosphatidyl to myo-inositol to form PI. **PIS/CDIPT is the enzyme that directly creates the PI molecule; CDS1/2 are upstream precursor-supplying enzymes and are reasonably included in the biosynthetic process.** (blunsom2020cdpdiacylglycerolsynthases(cds) pages 1-2, blunsom2020cdpdiacylglycerolsynthases(cds) pages 3-5, dickson2019understandingphosphoinositidesrare pages 1-3)

By contrast, PI/PIP kinases phosphorylate existing PI or phosphoinositides; phosphoinositide phosphatases remove those phosphates; GPI enzymes modify PI-containing GPI intermediates; DPM1 makes dolichol-phosphate-mannose; and UVRAG and PIK3R1/p85 are noncatalytic regulators. Assigning GO:0006661 directly to these proteins conflates **PI synthesis** with **phosphoinositide turnover, signaling, or downstream GPI-anchor synthesis**.

## 1. Strict biochemical meaning of PI biosynthesis

The eukaryotic pathway is:

1. **CDS1/CDS2:** phosphatidic acid + CTP → CDP-diacylglycerol + PPi.
2. **CDIPT/PIS:** CDP-diacylglycerol + myo-inositol → phosphatidylinositol + CMP.

Mammalian CDS1 and CDS2 are integral ER proteins; CDS2 appears especially important for replenishing PI during phospholipase-C signaling. PI synthesis occurs principally in the ER. A highly mobile, ER-derived PIS-containing membrane compartment has also been reported and proposed to synthesize and/or deliver PI to other membranes. PI accounts for approximately **10–20 mol% of mammalian phospholipids**, whereas its seven reversibly phosphorylated derivatives are substantially less abundant and function as compartmental signaling lipids. (blunsom2020cdpdiacylglycerolsynthases(cds) pages 1-2, blunsom2020cdpdiacylglycerolsynthases(cds) pages 3-5, dickson2019understandingphosphoinositidesrare pages 1-3)

Thus, under a narrow “which enzyme makes PI?” test, **CDIPT/PIS alone catalyzes the direct PI-forming reaction**. Under the broader biological-process interpretation used by GO, CDS1/CDS2 can properly be participants because they supply the CDP-DAG precursor in the same de novo pathway. CDS enzymes are not uniquely dedicated to PI in every organism or compartment, however: CDP-DAG can also feed phosphatidylglycerol/cardiolipin pathways. (blunsom2020cdpdiacylglycerolsynthases(cds) pages 1-2, blunsom2020cdpdiacylglycerolsynthases(cds) pages 3-5)

## 2. PI kinases make phosphoinositides, not PI

Phosphoinositides are reversibly phosphorylated derivatives of PI. Kinases add phosphate to the 3-, 4-, or 5-hydroxyl of the inositol headgroup, producing seven possible phosphorylated species; phosphatases reverse those transformations. This is chemically and conceptually distinct from assembling PI from CDP-DAG and inositol. (dickson2019understandingphosphoinositidesrare pages 1-3)

* **Class-I PI3Ks**—including PIK3CA/p110α, PIK3CB/p110β and PIK3CG/p110γ—principally produce PI(3,4,5)P3 from PI(4,5)P2 in receptor signaling.
* **Class-II PI3Ks** PIK3C2A/B/G generate PI3P and, context-dependently, PI(3,4)P2.
* **Class-III PIK3C3/VPS34** phosphorylates PI to PI3P in autophagic and endosomal complexes.
* **PI4KB** phosphorylates PI to PI4P, predominantly at the trans-Golgi.
* **PIP5K1A/B/C**, and fission-yeast Its3, phosphorylate PI4P to PI(4,5)P2.
* **PIP4K2A/B/C** phosphorylate PI5P to PI(4,5)P2.

For example, PI4P followed by PI(4,5)P2 is generated by sequential PI4K and type-I PIP5K activity; PIP4Ks instead use PI5P. These are appropriately described by **phosphatidylinositol phosphorylation**, a specific phosphatidylinositol-phosphate biosynthetic term where available, and often **phosphatidylinositol-mediated signaling**—not PI biosynthesis. (dickson2019understandingphosphoinositidesrare pages 3-5, dickson2019understandingphosphoinositidesrare pages 1-3, fox2020classiapi3k pages 1-3)

## 3. Phosphatases: PI as a product does not make the reaction de novo PI biosynthesis

MTM1 and catalytically active MTMR proteins are phosphoinositide 3-phosphatases. MTM1/MTMR2 use PI3P and PI(3,5)P2 as substrates, yielding PI and PI5P, respectively. Loss of MTM1 or MTMR2 causes excess PI3P on distinct endosomal populations, which is why the family is conventionally classified in endosomal phosphoinositide degradation/homeostasis rather than bulk PI synthesis. (cao2008sequentialactionsof pages 1-2, dickson2019understandingphosphoinositidesrare pages 3-5)

Likewise, ER SACM1L/Sac1 hydrolyzes PI4P to PI; synaptojanins remove the 5-phosphate from PI(4,5)P2 and related substrates and also contain a SAC domain; and INPP5D/SHIP1 converts PI(3,4,5)P3 to PI(3,4)P2. These reactions are **phosphoinositide dephosphorylation/turnover**. A terminal product being PI does not convert a salvage or catabolic reaction into the canonical biosynthetic pathway. GO annotation should normally represent the enzyme’s mechanistic process—dephosphorylation, phosphoinositide catabolism/homeostasis, and signaling—rather than GO:0006661. (dickson2019understandingphosphoinositidesrare pages 3-5)

## 4. GPI-anchor enzymes and DPM1 are downstream of PI

GPI synthesis begins by modifying pre-existing PI. PIGL converts GlcNAc-PI to GlcN-PI. PIGN, PIGG and PIGO add ethanolamine phosphate to mannose residues of GPI intermediates. PGAP5/MPPE1 subsequently removes ethanolamine phosphate from Man2 during GPI remodeling and ER export. None produces the PI lipid moiety. The correct umbrella process is **GO:0006506 GPI anchor biosynthetic process**, with a remodeling term for PGAP5 where available. (murakami2024gpianchorand pages 1-2, kinoshita2020biosynthesisandbiology pages 7-7, kinoshita2020biosynthesisandbiology pages 4-5)

DPM1 is even more clearly outside PI biosynthesis. The DPM1-containing dolichol-phosphate-mannose synthase catalyzes:

**GDP-mannose + dolichol-phosphate → GDP + dolichol-phosphate-mannose.**

Dol-P-Man donates mannose to GPI precursors and to N-, O- and C-mannosylation pathways. Human DPM1 deficiency reduced Dol-P-Man synthase activity to approximately **6% of normal** in one foundational patient study and impaired both N-glycosylation and GPI-anchored-protein production. This demonstrates biological coupling to GPI formation, not synthesis of PI. **Annotating DPM1 to GO:0006661 is not supportable.** Appropriate descriptions are dolichol-phosphate-mannose biosynthesis, glycosylation, and—by pathway participation—GPI-anchor biosynthesis. (banerjee2017dolicholphosphatemannose pages 1-3, welti2013regulationofdolichollinked pages 1-2, banerjee2017dolicholphosphatemannose pages 3-4, imbach2000deficiencyofdolicholphosphatemannose pages 5-6)

## 5. UVRAG and PIK3R1/p85 are noncatalytic

UVRAG is a mutually exclusive, Beclin-1-binding subunit of the UVRAG-containing VPS34 complex II, involved especially in endolysosomal trafficking and later autophagic maturation. **VPS34 is the catalytic lipid kinase and major producer of PI3P; UVRAG is a targeting/regulatory component, not a phosphoinositide-metabolizing enzyme.** Its relationship to PI3P should therefore be described as regulation or localization of VPS34-dependent PI3P production. (wu2018targetingthepotent pages 1-2, itakura2008beclin1forms pages 1-2)

PIK3R1 encodes p85α and shorter regulatory isoforms. Class-IA PI3Ks are obligate p110–p85 heterodimers: p110 is catalytic, while p85 stabilizes p110, restrains its basal activity, binds phosphotyrosine-containing receptors/adaptors, and recruits the catalytic subunit to membrane substrate. **p85 has no PI/PIP lipid-kinase catalytic activity.** GO:0006661 is therefore incorrect; regulation of PI3K activity and PI-mediated signaling are appropriate. (fox2020classiapi3k pages 1-3)

## 6. Per-family verdict

The decisive reaction-level assessment is summarized below.

| Family / proteins | Actual substrate → product or role | Relationship to PI | Verdict for GO:0006661 “phosphatidylinositol biosynthetic process” | Better GO biological-process wording |
|---|---|---|---|---|
| **CDS1 / CDS2** | **Phosphatidic acid + CTP → CDP-diacylglycerol + PPi** at ER; supplies committed precursor for PI synthesis (blunsom2020cdpdiacylglycerolsynthases(cds) pages 1-2, blunsom2020cdpdiacylglycerolsynthases(cds) pages 3-5) | Upstream **precursor-forming** step in de novo PI synthesis; does **not** itself form PI molecule | **Correct** (broadly supportable as part of PI biosynthesis) | phosphatidylinositol biosynthetic process; more specific reaction-level wording: **CDP-diacylglycerol biosynthetic process** / phosphatidylinositol precursor biosynthesis |
| **CDIPT / PIS (PI synthase)** | **CDP-diacylglycerol + myo-inositol → phosphatidylinositol + CMP**; direct PI-forming enzyme, classically at ER and PI-synthase-containing mobile compartments (dickson2019understandingphosphoinositidesrare pages 1-3) | **Directly forms PI molecule itself** | **Correct** | phosphatidylinositol biosynthetic process |
| **PI3K class I** (**PIK3CA/CB/CG**) | Phosphorylate pre-existing phosphoinositides at D3; class I chiefly **PI(4,5)P2 → PI(3,4,5)P3** (class review substrate scope includes PI/PI4P/PIP2, but signaling output is PIP3) (fox2020classiapi3k pages 1-3, tsay2023theroleof pages 1-2) | Do **not** synthesize PI; make **phosphorylated PI species** | **Outright incorrect** | **phosphatidylinositol phosphorylation**; phosphatidylinositol-mediated signaling; phosphatidylinositol phosphate biosynthetic process |
| **PI3K class II** (**PIK3C2A/B/G**) | D3 phosphorylation of phosphoinositides; can generate **PI3P** (and in some contexts PI(3,4)P2) from pre-existing lipids (dickson2019understandingphosphoinositidesrare pages 3-5, fox2020classiapi3k pages 1-3) | Do **not** synthesize PI; make **PI3P / other PIPs** | **Outright incorrect** | phosphatidylinositol phosphorylation; phosphatidylinositol phosphate biosynthetic process |
| **PI3K class III / VPS34** (**PIK3C3**) | **PI → PI3P** in VPS34 complexes involved in autophagy/endosomal sorting (dickson2019understandingphosphoinositidesrare pages 3-5, wu2018targetingthepotent pages 1-2, itakura2008beclin1forms pages 1-2) | Converts existing PI into **PI3P**; does not make PI | **Outright incorrect** | phosphatidylinositol phosphorylation; phosphatidylinositol 3-phosphate biosynthetic process; autophagy / endosomal sorting |
| **PI4KB** | **PI → PI4P** at trans-Golgi (dickson2019understandingphosphoinositidesrare pages 1-3, dickson2019understandingphosphoinositidesrare pages 3-5) | Uses pre-existing PI as substrate; forms **PI4P**, not PI | **Outright incorrect** | phosphatidylinositol phosphorylation; phosphatidylinositol 4-phosphate biosynthetic process |
| **PIP5K1A/B/C; S. pombe its3** | **PI4P → PI(4,5)P2** via 5-phosphorylation (type I PIP5Ks) (dickson2019understandingphosphoinositidesrare pages 3-5) | Act on **PI4P**, not on de novo PI synthesis | **Outright incorrect** | phosphatidylinositol phosphorylation; phosphatidylinositol-4-phosphate 5-kinase pathway / PI(4,5)P2 biosynthetic process |
| **PIP4K2A/B/C** | **PI5P → PI(4,5)P2** via 4-phosphorylation (type II PIP4Ks) (dickson2019understandingphosphoinositidesrare pages 3-5) | Act on **PI5P**, a phosphorylated PI; do not synthesize PI | **Outright incorrect** | phosphatidylinositol phosphorylation; phosphatidylinositol phosphate biosynthetic process |
| **MTM1 / MTMR1-4 (myotubularins)** | 3-phosphatases acting on **PI3P and/or PI(3,5)P2 → PI or PI5P**; classical phosphoinositide phosphatases regulating endosomal PI(3)P homeostasis (cao2008sequentialactionsof pages 1-2, dickson2019understandingphosphoinositidesrare pages 3-5) | Can yield PI as a **dephosphorylation product**, but conventionally are **turnover / phosphatase** enzymes, not PI biosynthetic enzymes | **Outright incorrect** | phosphatidylinositol dephosphorylation; phosphoinositide phosphatase activity; phosphatidylinositol phosphate catabolic process |
| **SACM1L / Sac1** | **PI4P → PI** (ER/Golgi-associated 4-phosphatase) (dickson2019understandingphosphoinositidesrare pages 3-5) | Produces PI by **dephosphorylation of PI4P**; standard role is phosphoinositide turnover/homeostasis | **Outright incorrect** | phosphatidylinositol dephosphorylation; phosphatidylinositol 4-phosphate catabolic process |
| **SYNJ1 / SYNJ2 (synaptojanins)** | 5-phosphatases acting on **PI(4,5)P2 → PI4P** and related PIPs; synaptojanins also carry Sac domains (dickson2019understandingphosphoinositidesrare pages 3-5) | Catabolize higher phosphoinositides; do not synthesize PI | **Outright incorrect** | phosphatidylinositol dephosphorylation; phosphoinositide catabolic process; phosphatidylinositol-mediated signaling |
| **INPP5D / SHIP1** | **PI(3,4,5)P3 → PI(3,4)P2** (5-phosphatase) (dickson2019understandingphosphoinositidesrare pages 3-5) | Turns over signaling phosphoinositides; no PI synthesis | **Outright incorrect** | phosphatidylinositol dephosphorylation; phosphatidylinositol-mediated signaling |
| **PIGL** | **GlcNAc-PI → GlcN-PI** (de-N-acetylation in GPI-anchor biosynthesis) (murakami2024gpianchorand pages 1-2, kinoshita2020biosynthesisandbiology pages 7-7) | Uses PI-containing **GPI intermediate** downstream of PI synthesis; does not make PI | **Outright incorrect** | GPI anchor biosynthetic process |
| **PIGN / PIGO / PIGG** | Transfer ethanolamine phosphate onto mannoses of GPI intermediates (GPI-ET enzymes) (murakami2024gpianchorand pages 1-2, kinoshita2020biosynthesisandbiology pages 7-7, kinoshita2020biosynthesisandbiology pages 4-5) | Modify **GPI anchor precursors** that already contain PI; no PI synthesis | **Outright incorrect** | GPI anchor biosynthetic process |
| **PGAP5 / MPPE1** | Removes ethanolamine phosphate from Man2 after GPI attachment; GPI remodeling phosphodiesterase (murakami2024gpianchorand pages 1-2, kinoshita2020biosynthesisandbiology pages 7-7) | Acts on mature/late **GPI anchor**, not PI synthesis | **Outright incorrect** | GPI anchor remodeling / GPI anchor biosynthetic process |
| **DPM1** | **GDP-mannose + dolichol-P → Dol-P-Man**; mannose donor supply for GPI anchor biosynthesis and N-/O-/C-mannosylation (banerjee2017dolicholphosphatemannose pages 1-3, welti2013regulationofdolichollinked pages 1-2, banerjee2017dolicholphosphatemannose pages 3-4, imbach2000deficiencyofdolicholphosphatemannose pages 5-6) | No biochemical role in making PI molecule; only indirectly supports pathways that later use PI-containing GPI intermediates | **Outright incorrect** | dolichol-phosphate-mannose biosynthetic process; protein glycosylation; GPI anchor biosynthetic process |
| **UVRAG** | **Noncatalytic regulatory/scaffolding subunit** of Beclin1–VPS34 **complex II**; promotes VPS34-dependent endolysosomal trafficking (wu2018targetingthepotent pages 1-2, itakura2008beclin1forms pages 1-2) | Regulates **PI3P production by VPS34** but is **not** a phosphoinositide-metabolizing enzyme and does not make PI | **Outright incorrect** | regulation of phosphatidylinositol 3-kinase complex / autophagy / endosomal transport |
| **PIK3R1 / p85α** | **Noncatalytic regulatory subunit** of class IA PI3K; stabilizes and inhibits p110 catalytic subunit, recruits holoenzyme to activated receptors (fox2020classiapi3k pages 1-3) | No catalytic PI synthesis; only regulates enzymes that make **PIP3** from PIP2 | **Outright incorrect** | regulation of phosphatidylinositol 3-kinase activity; phosphatidylinositol-mediated signaling |


*Table: This table adjudicates whether each enzyme family actually participates in phosphatidylinositol biosynthesis versus phosphoinositide phosphorylation, dephosphorylation, signaling, or GPI-anchor metabolism. It is useful for deciding which ARBA families are appropriately annotated to GO:0006661 and which are over-broad or incorrect.*

In this table, “outright incorrect” means that the protein’s established molecular function lies in a chemically different process, not merely that a more specific child term is preferable. Only CDS1/CDS2 and CDIPT/PIS warrant GO:0006661 among the assessed catalytic families; CDIPT/PIS is the only direct PI-forming enzyme.

## 7. GO ontology interpretation

GO:0006661, **phosphatidylinositol biosynthetic process**, denotes the chemical reactions and pathways resulting in formation of phosphatidylinositol. Its logical placement is within **GO:0046488 phosphatidylinositol metabolic process** and **GO:0046474 glycerophospholipid biosynthetic process**. The other requested terms represent distinct biology:

* **GO:0046854 phosphatidylinositol phosphorylation:** phosphate addition to PI or a PI phosphate—the appropriate mechanistic process for PI3K, PI4K, PIP5K and PIP4K reactions.
* **GO:0006506 GPI anchor biosynthetic process:** construction of a glycan-phospholipid anchor using PI as the lipid substrate.
* **GO:0048015 phosphatidylinositol-mediated signaling:** signaling in which PI-derived lipids function as mediators.

Phosphoinositides are structurally PI derivatives and may colloquially be called “phosphatidylinositols,” but this does **not** make their synthesis synonymous with biosynthesis of the unphosphorylated parent lipid. The ontology’s separate phosphorylation, signaling, and GPI terms are strong evidence that GO:0006661 should not be used as a generic parent for every reaction involving a PI-containing molecule. The biologically appropriate formulation for kinase products is a specific PI3P, PI4P, PI(4,5)P2 or PI(3,4,5)P3 biosynthetic process where such a term exists, otherwise GO:0046854.

I found no retrievable, authoritative GO Consortium issue or publication explicitly documenting a discussion of **ARBA00028655** or a named campaign against PI-kinase/phosphatase over-annotation to GO:0006661. Therefore, it would be unsafe to claim formal Consortium adjudication. The biochemical and ontology-structure evidence nevertheless strongly indicates that such annotations are over-extensions.

## 8. Taxonomic conclusions

The CDP-DAG/PIS route is broadly conserved across eukaryotes, including fungi. In *Schizosaccharomyces pombe*, the PI-synthase ortholog is conventionally designated **pis1/PIS**; it should not be confused with **its3**, which encodes a PI4P 5-kinase producing PI(4,5)P2. The *S. pombe* locus **SPAC31G5.16c (dpm1)** encodes dolichol-phosphate-mannose synthase: its role is Dol-P-Man production for glycosylation/GPI pathways, not PI formation. CDS and TAM41 homologs are also documented in *S. pombe*, supplying CDP-DAG in ER and mitochondrial phospholipid pathways, respectively. (blunsom2020cdpdiacylglycerolsynthases(cds) pages 3-5, banerjee2017dolicholphosphatemannose pages 1-3, welti2013regulationofdolichollinked pages 1-2)

PI synthesis is not eukaryote-exclusive. Inositol phospholipids and PI/PI-phosphate synthases occur in several bacterial lineages and in archaea with inositol-containing ether lipids. Mycobacteria synthesize PI and use it to construct phosphatidylinositol mannosides, lipomannan and lipoarabinomannan. Their enzyme often called **PgsA/PgsA1** is more precisely a CDP-diacylglycerol–inositol-phosphate phosphatidyltransferase: it produces phosphatidylinositol phosphate, which is then dephosphorylated to PI. CDS-family enzymes themselves occur across all three domains of life. Consequently, a blanket **Eukaryota-only taxon restriction on GO:0006661 would be biologically wrong**, although individual ortholog rules can legitimately be taxonomically restricted according to the family and reaction represented. (blunsom2020cdpdiacylglycerolsynthases(cds) pages 1-2, blunsom2020cdpdiacylglycerolsynthases(cds) pages 3-5)

## Final recommendation for ARBA00028655

Retain GO:0006661 only for condition sets that identify **CDIPT/PIS** or demonstrably identify an upstream enzyme in the bona fide de novo PI pathway, principally **ER CDS1/CDS2**. Remove or replace GO:0006661 for all PI/PIP kinases, phosphoinositide phosphatases, GPI-processing proteins, DPM1, UVRAG and PI3K regulatory subunits. In particular, **DPM1 → GO:0006661 should be treated as an erroneous annotation, not merely an imprecise one**.

### Principal recent and authoritative sources

* Murakami Y, Kinoshita T. “GPI Anchor and Its Deficiency.” *Trends in Glycoscience and Glycotechnology* 36:E1–E5. **January 2024**. https://doi.org/10.4052/tigg.2331.1e (murakami2024gpianchorand pages 1-2)
* Blunsom NJ, Cockcroft S. “CDP-Diacylglycerol Synthases: Gateway to Phosphatidylinositol and Cardiolipin Synthesis.” *Frontiers in Cell and Developmental Biology* 8:63. **7 February 2020**. https://doi.org/10.3389/fcell.2020.00063 (blunsom2020cdpdiacylglycerolsynthases(cds) pages 1-2)
* Kinoshita T. “Biosynthesis and biology of mammalian GPI-anchored proteins.” *Open Biology* 10:190290. **March 2020**. https://doi.org/10.1098/rsob.190290 (kinoshita2020biosynthesisandbiology pages 7-7)
* Fox M, Mott HR, Owen D. “Class IA PI3K regulatory subunits: p110-independent roles and structures.” *Biochemical Society Transactions* 48:1397–1417. **17 July 2020**. https://doi.org/10.1042/BST20190845 (fox2020classiapi3k pages 1-3)
* Dickson EJ, Hille B. “Understanding phosphoinositides: rare, dynamic, and essential membrane phospholipids.” *Biochemical Journal* 476:1–23. **7 January 2019**. https://doi.org/10.1042/BCJ20180022 (dickson2019understandingphosphoinositidesrare pages 1-3)
* Wu S et al. “Targeting the potent Beclin 1–UVRAG coiled-coil interaction…” *PNAS*. **June 2018**. https://doi.org/10.1073/pnas.1721173115 (wu2018targetingthepotent pages 1-2)
* Banerjee DK et al. “Dolichol phosphate mannose synthase…” *Glycoconjugate Journal* 34:467–479. **June 2017**. https://doi.org/10.1007/s10719-017-9777-4 (banerjee2017dolicholphosphatemannose pages 1-3)
* Cao C et al. “Sequential Actions of Myotubularin Lipid Phosphatases…” *Molecular Biology of the Cell* 19:3334–3346. **August 2008**. https://doi.org/10.1091/mbc.E08-04-0367 (cao2008sequentialactionsof pages 1-2)

References

1. (blunsom2020cdpdiacylglycerolsynthases(cds) pages 1-2): Nicholas J. Blunsom and Shamshad Cockcroft. Cdp-diacylglycerol synthases (cds): gateway to phosphatidylinositol and cardiolipin synthesis. Frontiers in Cell and Developmental Biology, Feb 2020. URL: https://doi.org/10.3389/fcell.2020.00063, doi:10.3389/fcell.2020.00063. This article has 142 citations.

2. (blunsom2020cdpdiacylglycerolsynthases(cds) pages 3-5): Nicholas J. Blunsom and Shamshad Cockcroft. Cdp-diacylglycerol synthases (cds): gateway to phosphatidylinositol and cardiolipin synthesis. Frontiers in Cell and Developmental Biology, Feb 2020. URL: https://doi.org/10.3389/fcell.2020.00063, doi:10.3389/fcell.2020.00063. This article has 142 citations.

3. (dickson2019understandingphosphoinositidesrare pages 1-3): Eamonn J. Dickson and Bertil Hille. Understanding phosphoinositides: rare, dynamic, and essential membrane phospholipids. The Biochemical journal, 476 1:1-23, Jan 2019. URL: https://doi.org/10.1042/bcj20180022, doi:10.1042/bcj20180022. This article has 316 citations.

4. (dickson2019understandingphosphoinositidesrare pages 3-5): Eamonn J. Dickson and Bertil Hille. Understanding phosphoinositides: rare, dynamic, and essential membrane phospholipids. The Biochemical journal, 476 1:1-23, Jan 2019. URL: https://doi.org/10.1042/bcj20180022, doi:10.1042/bcj20180022. This article has 316 citations.

5. (fox2020classiapi3k pages 1-3): Millie Fox, Helen R. Mott, and Darerca Owen. Class ia pi3k regulatory subunits: p110-independent roles and structures. Biochemical Society Transactions, 48:1397-1417, Jul 2020. URL: https://doi.org/10.1042/bst20190845, doi:10.1042/bst20190845. This article has 106 citations and is from a peer-reviewed journal.

6. (cao2008sequentialactionsof pages 1-2): Canhong Cao, Jonathan M. Backer, Jocelyn Laporte, Edward J. Bedrick, and Angela Wandinger-Ness. Sequential actions of myotubularin lipid phosphatases regulate endosomal pi(3)p and growth factor receptor trafficking. Molecular biology of the cell, 19 8:3334-46, Aug 2008. URL: https://doi.org/10.1091/mbc.e08-04-0367, doi:10.1091/mbc.e08-04-0367. This article has 157 citations and is from a domain leading peer-reviewed journal.

7. (murakami2024gpianchorand pages 1-2): Yoshiko Murakami and Taroh Kinoshita. Gpi anchor and its deficiency. Trends in Glycoscience and Glycotechnology, 36:E1-E5, Jan 2024. URL: https://doi.org/10.4052/tigg.2331.1e, doi:10.4052/tigg.2331.1e. This article has 1 citations and is from a peer-reviewed journal.

8. (kinoshita2020biosynthesisandbiology pages 7-7): Taroh Kinoshita. Biosynthesis and biology of mammalian gpi-anchored proteins. Open Biology, Mar 2020. URL: https://doi.org/10.1098/rsob.190290, doi:10.1098/rsob.190290. This article has 397 citations and is from a peer-reviewed journal.

9. (kinoshita2020biosynthesisandbiology pages 4-5): Taroh Kinoshita. Biosynthesis and biology of mammalian gpi-anchored proteins. Open Biology, Mar 2020. URL: https://doi.org/10.1098/rsob.190290, doi:10.1098/rsob.190290. This article has 397 citations and is from a peer-reviewed journal.

10. (banerjee2017dolicholphosphatemannose pages 1-3): Dipak K. Banerjee, Zhenbo Zhang, Krishna Baksi, and Jesús E. Serrano-Negrón. Dolichol phosphate mannose synthase: a glycosyltransferase with unity in molecular diversities. Glycoconjugate Journal, 34:467-479, Jun 2017. URL: https://doi.org/10.1007/s10719-017-9777-4, doi:10.1007/s10719-017-9777-4. This article has 25 citations and is from a peer-reviewed journal.

11. (welti2013regulationofdolichollinked pages 1-2): Michael Welti. Regulation of dolichol-linked glycosylation. Glycoconjugate Journal, 30:51-56, Jun 2013. URL: https://doi.org/10.1007/s10719-012-9417-y, doi:10.1007/s10719-012-9417-y. This article has 61 citations and is from a peer-reviewed journal.

12. (banerjee2017dolicholphosphatemannose pages 3-4): Dipak K. Banerjee, Zhenbo Zhang, Krishna Baksi, and Jesús E. Serrano-Negrón. Dolichol phosphate mannose synthase: a glycosyltransferase with unity in molecular diversities. Glycoconjugate Journal, 34:467-479, Jun 2017. URL: https://doi.org/10.1007/s10719-017-9777-4, doi:10.1007/s10719-017-9777-4. This article has 25 citations and is from a peer-reviewed journal.

13. (imbach2000deficiencyofdolicholphosphatemannose pages 5-6): Timo Imbach, Barbara Schenk, Els Schollen, Patricie Burda, Andreas Stutz, Stephanie Grünewald, Nicola M. Bailie, Mary D. King, Jaak Jaeken, Gert Matthijs, Eric G. Berger, Markus Aebi, and Thierry Hennet. Deficiency of dolichol-phosphate-mannose synthase-1 causes congenital disorder of glycosylation type ie. The Journal of clinical investigation, 105 2:233-9, Jan 2000. URL: https://doi.org/10.1172/jci8691, doi:10.1172/jci8691. This article has 199 citations.

14. (wu2018targetingthepotent pages 1-2): Shuai Wu, Yunjiao He, Xianxiu Qiu, Wenchao Yang, Wenchao Liu, Xiaohua Li, Yan Li, Han-Ming Shen, Renxiao Wang, Zhenyu Yue, and Yanxiang Zhao. Targeting the potent beclin 1–uvrag coiled-coil interaction with designed peptides enhances autophagy and endolysosomal trafficking. Proceedings of the National Academy of Sciences of the United States of America, 115:E5669-E5678, Jun 2018. URL: https://doi.org/10.1073/pnas.1721173115, doi:10.1073/pnas.1721173115. This article has 75 citations and is from a highest quality peer-reviewed journal.

15. (itakura2008beclin1forms pages 1-2): Eisuke Itakura, Chieko Kishi, Kinji Inoue, and Noboru Mizushima. Beclin 1 forms two distinct phosphatidylinositol 3-kinase complexes with mammalian atg14 and uvrag. Molecular biology of the cell, 19 12:5360-72, Dec 2008. URL: https://doi.org/10.1091/mbc.e08-01-0080, doi:10.1091/mbc.e08-01-0080. This article has 1541 citations and is from a domain leading peer-reviewed journal.

16. (tsay2023theroleof pages 1-2): Ariel Tsay and Jen-Chywan Wang. The role of pik3r1 in metabolic function and insulin sensitivity. International Journal of Molecular Sciences, 24:12665, Aug 2023. URL: https://doi.org/10.3390/ijms241612665, doi:10.3390/ijms241612665. This article has 118 citations.

## Artifacts

- [Edison artifact artifact-00](ARBA00028655-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. dickson2019understandingphosphoinositidesrare pages 1-3
2. dickson2019understandingphosphoinositidesrare pages 3-5
3. murakami2024gpianchorand pages 1-2
4. kinoshita2020biosynthesisandbiology pages 7-7
5. wu2018targetingthepotent pages 1-2
6. banerjee2017dolicholphosphatemannose pages 1-3
7. cao2008sequentialactionsof pages 1-2
8. kinoshita2020biosynthesisandbiology pages 4-5
9. welti2013regulationofdolichollinked pages 1-2
10. banerjee2017dolicholphosphatemannose pages 3-4
11. imbach2000deficiencyofdolicholphosphatemannose pages 5-6
12. tsay2023theroleof pages 1-2
13. https://doi.org/10.4052/tigg.2331.1e
14. https://doi.org/10.3389/fcell.2020.00063
15. https://doi.org/10.1098/rsob.190290
16. https://doi.org/10.1042/BST20190845
17. https://doi.org/10.1042/BCJ20180022
18. https://doi.org/10.1073/pnas.1721173115
19. https://doi.org/10.1007/s10719-017-9777-4
20. https://doi.org/10.1091/mbc.E08-04-0367
21. https://doi.org/10.3389/fcell.2020.00063,
22. https://doi.org/10.1042/bcj20180022,
23. https://doi.org/10.1042/bst20190845,
24. https://doi.org/10.1091/mbc.e08-04-0367,
25. https://doi.org/10.4052/tigg.2331.1e,
26. https://doi.org/10.1098/rsob.190290,
27. https://doi.org/10.1007/s10719-017-9777-4,
28. https://doi.org/10.1007/s10719-012-9417-y,
29. https://doi.org/10.1172/jci8691,
30. https://doi.org/10.1073/pnas.1721173115,
31. https://doi.org/10.1091/mbc.e08-01-0080,
32. https://doi.org/10.3390/ijms241612665,