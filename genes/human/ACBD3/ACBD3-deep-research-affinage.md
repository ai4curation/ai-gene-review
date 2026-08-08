---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ACBD3
affinage_run_date: 2026-06-09T22:02:38
uniprot_accession: Q9H3P7
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 34
citation_count: 34
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ACBD3 (human)

## Current model (mechanistic narrative)

ACBD3 (GCP60/PAP7) is a peripheral Golgi-membrane scaffolding protein that organizes lipid-modifying and signaling machinery on Golgi/TGN membranes and at ER–Golgi contact sites [PMID:11590181, PMID:27009356]. Its central scaffolding output is the direct recruitment of the lipid kinase PI4KB to membranes through its GOLD domain, an interaction defined structurally by NMR that both anchors PI4KB to the Golgi and stimulates its enzymatic activity to maintain Golgi PI4P homeostasis [PMID:27009356, PMID:27989622]. ACBD3 is itself targeted to the Golgi by a two-step mechanism: the Sec1/Munc-18 protein SCFD1 with the SNARE SEC22B acts upstream of an MWT374-376 motif that binds the golgins giantin and golgin-45 [PMID:38134218, PMID:11590181, PMID:28777890]. Beyond PI4KB, ACBD3 acts as an A-kinase anchoring protein, binding PKA regulatory subunits (RIα and RII via the GOLD domain) to position PKA at the Golgi and at mitochondria, where it couples cholesterol transport to hormone-stimulated steroidogenesis and where it controls cargo-triggered PKA activation governing KDEL-receptor retrograde trafficking [PMID:11731621, PMID:12943713, PMID:37044218, PMID:34493279]. ACBD3 is required for Golgi stack integrity and for FAPP2-mediated glucosylceramide transport and ER-to-Golgi ceramide/sphingolipid flux, with knockout producing enlarged, unstacked Golgi and altered sphingolipid pools [PMID:29750412, PMID:34298889]. The same membrane-coupling activity is extensively exploited by pathogens: picornavirus 3A proteins clamp ACBD3 onto replication-organelle membranes to recruit and activate PI4KB for viral PI4P synthesis, and the OSBP–VAP cholesterol-transport machinery is co-opted through ACBD3 as well [PMID:22124328, PMID:22258260, PMID:27989622, PMID:28065508, PMID:31381608, PMID:29367253]. ACBD3 also concentrates ligand-activated STING at ER–Golgi contact sites to drive ER export and type-I interferon responses [PMID:36543137], partners with Numb during mitotic Golgi fragmentation to influence asymmetric neural cell-fate specification [PMID:17418793], and modulates apoptotic signaling through a redox-sensitive Cys-463 interaction with a caspase-generated golgin-160 fragment [PMID:17711851]. Salmonella effectors SseF/SseG bind ACBD3 to position Salmonella-containing vacuoles at the Golgi [PMID:27406559], underscoring ACBD3 as a recurrently hijacked membrane-organizing hub.

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0008289 lipid binding
- **localization:** GO:0005794 Golgi apparatus, GO:0005783 endoplasmic reticulum, GO:0005829 cytosol, GO:0005739 mitochondrion
- **pathway (Reactome):** R-HSA-5653656 Vesicle-mediated transport, R-HSA-1643685 Disease, R-HSA-168256 Immune System, R-HSA-1430728 Metabolism, R-HSA-162582 Signal Transduction
- **partners:** PI4KB, GIANTIN, GOLGA1/GOLGIN-45, PRKAR1A, TBC1D22A, SCFD1, SEC22B, KDELR
- **complexes:** ACBD3:PI4KB complex, ACBD3:PI4KB:Rab11 membrane complex, golgin-45:GRASP55:TBC1D22 stacking complex, ACBD3:PKA holoenzyme (AKAP) complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2001 | Medium | GCP60 (ACBD3) was identified as a peripheral Golgi membrane protein that interacts with the C-terminal cytoplasmic domain of the integral membrane protein giantin; overexpression of the GCP60 C-terminal domain caused Golgi disassembly and blocked ER-to-Golgi protein transport. | PMID:11590181 | The Journal of biological chemistry |
| 2001 | Medium | PAP7 (ACBD3) interacts with both the mitochondrial peripheral-type benzodiazepine receptor (PBR) and the cytosolic PKA regulatory subunit RIα; overexpression of full-length PAP7 increased hCG-induced steroid production, while a dominant-negative partial PAP7 and antisense oligonucleotides inhibited hormone-stimulated cholesterol transport and steroidogenesis in MA-10 Leydig cells. | PMID:11731621 | Molecular endocrinology (Baltimore, Md.) |
| 2003 | Medium | PAP7 (ACBD3) functions as an A-kinase anchoring protein (AKAP) that localizes to the trans-Golgi apparatus and mitochondria in Leydig cells; inhibition of PAP7 expression reduced hormone-induced cholesterol transport into mitochondria and decreased steroid formation, suggesting it targets PKA to PBR-rich organelles. | PMID:12943713 | The Journal of steroid biochemistry and molecular biology |
| 2006 | Medium | GCP60 (ACBD3) preferentially interacts with a caspase-generated golgin-160 fragment (residues 140–311) and prevents its nuclear translocation; cells overexpressing GCP60 showed increased sensitivity to staurosporine-induced apoptosis. | PMID:16870622 | The Journal of biological chemistry |
| 2007 | High | A single redox-sensitive cysteine (Cys-463) in GCP60 (ACBD3) is critical for its interaction with the golgin-160 caspase fragment (residues 140–311); mutation of Cys-463 abolished interaction in vitro and disrupted Golgi retention of the fragment; oxidation by H2O2 or a nitric oxide donor restored the interaction. | PMID:17711851 | The Journal of biological chemistry |
| 2007 | High | ACBD3 associates with the Golgi in neurons and interphase progenitor cells but becomes cytosolic upon Golgi fragmentation during mitosis; ACBD3 interacts with Numb through an essential Numb domain, and cytosolic ACBD3 acts synergistically with Numb to specify neural cell fates; loss- and gain-of-function mouse mutants share phenotypic similarities linking ACBD3 to asymmetric cell division. | PMID:17418793 | Cell |
| 2011 | High | ACBD3 interacts with multiple Aichi virus non-structural proteins (2B, 2BC, 2C, 3A, 3AB) and directly with PI4KB; this ACBD3–PI4KB interaction recruits PI4KB to viral RNA replication sites, enabling PI4P synthesis essential for Aichi virus RNA replication; knockdown of ACBD3 or PI4KB suppressed replication. | PMID:22124328 | The EMBO journal |
| 2012 | High | Multiple picornavirus 3A proteins (Aichi virus, bovine kobuvirus, poliovirus, coxsackievirus B2/B3/B5, HRV14) co-purify with ACBD3; ACBD3 itself binds PI4KIIIβ in the absence of 3A; alanine-scanning mutagenesis of Aichi virus 3A identified residues that selectively abolish PI4KIIIβ co-purification without affecting ACBD3 binding; N-terminal glycines of some 3A proteins are myristoylated. | PMID:22258260 | Journal of virology |
| 2012 | Medium | ACBD3 recruits the protein phosphatase PPM1L to ER–Golgi membrane contact sites via its GOLD domain, implicating ACBD3 in ceramide trafficking regulation at the ER–Golgi interface. | PMID:22796112 | FEBS letters |
| 2013 | Medium | ACBD3 interacts with TBC1D22A and TBC1D22B (putative Rab33 GAPs) via the same binding site on ACBD3 used by PI4KB; TBC1D22A/B and PI4KB interactions with ACBD3 are mutually exclusive, suggesting a competitive regulatory mechanism for PI4KB recruitment. | PMID:23572552 | mBio |
| 2013 | Medium | ACBD3 forms a complex with Rhes and mutant huntingtin (mHtt) in the striatum; ACBD3 levels are elevated in HD striatum; ACBD3 deletion abolishes mHtt-mediated neurotoxicity, while overexpression increases it, placing ACBD3 downstream of Rhes/mHtt as a mediator of HD cytotoxicity. | PMID:24012756 | Cell reports |
| 2013 | Medium | ACBD3 interacts with poliovirus 3A proteins at viral RNA replication sites; siRNA-mediated downregulation of ACBD3 significantly increased poliovirus replication, indicating ACBD3 can negatively modulate enterovirus replication; the amino acid at position 12 of 3A influences sensitivity to this effect. | PMID:23926333 | Journal of virology |
| 2013 | Medium | ACBD3 depletion did not affect PI4KIIIβ recruitment to coxsackievirus B3 (CVB3) replication organelles and did not impair CVB3 RNA replication, demonstrating that CVB3 recruits PI4KIIIβ by an ACBD3-independent mechanism (NEGATIVE finding for CVB3). | PMID:24352456 | Journal of virology |
| 2014 | High | The viral protein/ACBD3/PI4KB complex stimulates PI4KB kinase activity in vitro; Aichi virus 3A and 3AB proteins stimulate PI4KB activity through forming a 3A(3AB)/ACBD3/PI4KB complex, enhancing PI4P synthesis at replication organelles and facilitating viral replication complex formation. | PMID:24672044 | Journal of virology |
| 2016 | High | NMR structure of the PI4KB–ACBD3 complex was determined; ACBD3 recruits PI4KB to membranes both in vitro and in vivo, and membrane recruitment of PI4KB by ACBD3 increases its enzymatic activity; ACBD3:PI4KB complex formation is essential for proper Golgi PI4P homeostasis. | PMID:27009356 | Scientific reports |
| 2016 | High | Salmonella effectors SseF and SseG interact directly with ACBD3; SseG binds ACBD3 alone, while SseF binding requires SseG; ACBD3 knockdown reduces Golgi association of Salmonella-containing vacuoles, and ACBD3-interaction-deficient SseF/SseG mutants display an intracellular replication defect. | PMID:27406559 | mBio |
| 2016 | High | Crystal structure of the ACBD3 GOLD domain revealed a unique N terminus that mediates interaction with Aichi virus 3A; hydrogen-deuterium exchange mass spectrometry mapped the PI4KIIIβ–ACBD3 and ACBD3–3A interfaces; 3A directly activates PI4KIIIβ and this is sensitized by ACBD3; rationally designed interface mutations abrogated kinase activation by ACBD3. | PMID:27989622 | Structure (London, England : 1993) |
| 2017 | High | Crystal structures of Aichi virus and bovine kobuvirus 3A proteins in complex with the ACBD3 GOLD domain showed that viral 3A proteins act as molecular harnesses to stabilize ACBD3 at target membranes; molecular dynamics simulation revealed 3A-mediated ACBD3 stabilization at lipid bilayers. | PMID:28065508 | Structure (London, England : 1993) |
| 2017 | High | ACBD3 interacts with EV71 3A protein; this interaction is required for EV71 RNA replication and plaque formation; EV71 3A redirects ACBD3 to viral replication sites; I44A or H54Y substitutions in 3A disrupt ACBD3 binding and impair replication. | PMID:28303920 | Scientific reports |
| 2017 | High | EV71 3A protein stimulates the ACBD3–PI4KB interaction; ACBD3 is required for PI4KB recruitment to EV71 RNA replication sites; EV71 infection induces PI4P production in an ACBD3- and PI4KB-dependent manner; I44A or H54Y in 3A abolish stimulation of ACBD3–PI4KB interaction. | PMID:28701404 | Journal of virology |
| 2017 | Medium | ACBD3 interacts with Golgin45 via its GOLD domain; ACBD3 co-expression increases Golgin45 Golgi targeting; ACBD3 recruits TBC1D22 (a Rab33b GAP) to a multi-protein complex containing Golgin45 and GRASP55, suggesting a scaffolding role in organizing Golgi stacking proteins. | PMID:28777890 | FEBS letters |
| 2018 | Medium | AiV non-structural proteins (2B, 2BC, 2C, 3A, 3AB) interact with ACBD3, OSBP, VAP-A/B, and SAC1; ACBD3 mediates recruitment of OSBP-VAP cholesterol transport machinery to AiV replication organelles through protein–protein interactions; silencing OSBP, VAP-A/B, or SAC1 inhibited AiV replication; cholesterol accumulates at AiV replication organelles in an OSBP-dependent manner. | PMID:29367253 | Journal of virology |
| 2019 | High | ACBD3 knockout impaired replication of representative viruses from four enterovirus and two rhinovirus species; PI4KB recruitment to replication organelles requires ACBD3; absence of ACBD3 causes 3A mis-localization to ER instead of Golgi; ACB and CAR domains of ACBD3 are dispensable, while other domains are required for 3A-mediated PI4KB recruitment. | PMID:30755512 | mBio |
| 2019 | Medium | SAXS analysis showed that the ACBD3:PI4KB complex adopts highly flexible conformations (both compact and extended), while 14-3-3:PI4KB:Rab11 has 2:1:1 stoichiometry; membrane is required for formation of the ACBD3:PI4KB:Rab11 complex at physiological concentrations. | PMID:30679637 | Scientific reports |
| 2019 | High | Crystal structures of ACBD3 GOLD domain complexed with 3A proteins from poliovirus, EV-A71, EV-D68, and rhinovirus B14 revealed convergent structural mechanisms for 3A–ACBD3 interaction; 3A–3A interactions drive assembly of ACBD3–3A heterotetramers; structure-guided mutations disrupting these interfaces impaired PI4KB recruitment and enterovirus replication. | PMID:31381608 | PLoS pathogens |
| 2019 | Medium | ACBD3 is required for FAPP2-mediated glucosylceramide transport; ACBD3 knockdown causes Golgi fragmentation, FAPP2 dispersal from trans-Golgi network, and abnormal sphingolipid metabolism; re-expression of full-length ACBD3 rescues these defects. | PMID:29750412 | Journal of molecular cell biology |
| 2021 | Medium | ACBD3 knockout cells exhibit enlarged Golgi with absence of stacks and ribbon-like formation, confirming ACBD3 role in Golgi stacking; cholesterol levels and mitochondrial structure/function are not altered in ACBD3-KO HEK293 and HeLa cells; decreased sphingomyelins with normal ceramide and sphingomyelin synthase activity reveal ACBD3 role in ceramide transport from ER to Golgi. | PMID:34298889 | International journal of molecular sciences |
| 2021 | Medium | ACBD3 directly interacts with KDEL receptor and recruits PKA to the Golgi; ACBD3 depletion causes accelerated retrograde trafficking of KDEL receptor by altering its interaction with PKA and Arf1/ArfGAP1, leading to increased Arf1-GTP-dependent tubular carrier formation; ACBD3 functions as a negative regulator of PKA activity on KDEL receptor. | PMID:34493279 | BMC biology |
| 2022 | High | The Golgi-resident ACBD3 recognizes and concentrates ligand-bound STING at specialized ER–Golgi contact sites (non-canonical ER exit sites); ACBD3 depletion impairs STING ER-to-Golgi trafficking and type-I interferon responses. | PMID:36543137 | Cell reports |
| 2023 | High | ACBD3 is recruited to the Golgi by two redundant mechanisms: (1) an MWT374-376 motif in the ACBD3 region upstream of the GOLD domain, which interacts with golgins golgin-45 and giantin; (2) interaction with SCFD1 (a Sec1/Munc-18 protein) and SEC22B (a SNARE); CRISPR-KO of SCFD1 causes ACBD3 to become cytosolic, acting upstream of golgin interactions. | PMID:38134218 | Molecular biology of the cell |
| 2023 | Medium | ACBD3 GOLD domain directly interacts with the regulatory subunit RII of PKA, recruiting PKA holoenzyme to the Golgi; forward trafficking of proteins from the ER triggers PKA activation (release of catalytic subunit from RII) at the Golgi; ACBD3 depletion reduces Golgi-localized RII and causes constitutive PKA activation and KDEL receptor retrograde transport. | PMID:37044218 | The Journal of biological chemistry |
| 2024 | Medium | ACBD3 knockdown increases labile iron levels by promoting ferritinophagy, leading to ferroptosis sensitivity; this is coupled with reduced GPX4 levels and elevated polyunsaturated fatty acid-containing glycerophospholipids; knockdown of NCOA4 or Bafilomycin A1 treatment blocked ferritinophagy and impeded ferroptosis in ACBD3-depleted cells. | PMID:38953242 | Cell biology international |
| 2025 | Medium | ACBD3 colocalizes with TBEV NS4B at ER–Golgi contact sites and promotes TBEV infection; ACBD3 depletion inhibits virus replication and causes abnormal ER transformation and reduced virion release; the proviral mechanism is independent of PI4KB recruitment, requiring the full-length ACBD3 to coordinate ER-Golgi coupling. | PMID:40207930 | Journal of virology |
| 2025 | Medium | ACBD3 promotes primary lung cancer growth by recruiting PI4KB to the Golgi, enhancing oncogenic secretion in chromosome 1q-amplified cells; conversely, in chromosome 1q-diploid cells, ACBD3 suppresses metastasis by inhibiting NOTCH signaling and reducing cell motility. | PMID:40189704 | Oncogene |

## Citations

- PMID:11590181
- PMID:11731621
- PMID:12943713
- PMID:16870622
- PMID:17418793
- PMID:17711851
- PMID:22124328
- PMID:22258260
- PMID:22796112
- PMID:23572552
- PMID:23926333
- PMID:24012756
- PMID:24352456
- PMID:24672044
- PMID:27009356
- PMID:27406559
- PMID:27989622
- PMID:28065508
- PMID:28303920
- PMID:28701404
- PMID:28777890
- PMID:29367253
- PMID:29750412
- PMID:30679637
- PMID:30755512
- PMID:31381608
- PMID:34298889
- PMID:34493279
- PMID:36543137
- PMID:37044218
- PMID:38134218
- PMID:38953242
- PMID:40189704
- PMID:40207930
