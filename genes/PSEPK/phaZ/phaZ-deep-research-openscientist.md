---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T03:35:31.964691'
end_time: '2026-08-13T04:01:04.981562'
duration_seconds: 1533.02
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: phaZ
  gene_symbol: phaB
  uniprot_accession: Q88D24
  protein_description: 'SubName: Full=Poly(3-hydroxyalkanoate) depolymerase {ECO:0000313|EMBL:AAN70570.1};
    EC=3.1.1.- {ECO:0000313|EMBL:AAN70570.1};'
  gene_info: Name=phaB {ECO:0000313|EMBL:AAN70570.1}; OrderedLocusNames=PP_5004 {ECO:0000313|EMBL:AAN70570.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: AB_hydrolase. (IPR050471); AB_hydrolase_1. (IPR000073); AB_hydrolase_fold.
    (IPR029058); PHA_depoly_arom. (IPR011942); Abhydrolase_1 (PF00561)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: phaZ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: phaZ-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88D24
- **Protein Description:** SubName: Full=Poly(3-hydroxyalkanoate) depolymerase {ECO:0000313|EMBL:AAN70570.1}; EC=3.1.1.- {ECO:0000313|EMBL:AAN70570.1};
- **Gene Information:** Name=phaB {ECO:0000313|EMBL:AAN70570.1}; OrderedLocusNames=PP_5004 {ECO:0000313|EMBL:AAN70570.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AB_hydrolase. (IPR050471); AB_hydrolase_1. (IPR000073); AB_hydrolase_fold. (IPR029058); PHA_depoly_arom. (IPR011942); Abhydrolase_1 (PF00561)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "phaB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'phaB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **phaB** (gene ID: phaZ, UniProt: Q88D24) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *phaZ* (PP_5004, UniProt Q88D24) in *Pseudomonas putida* KT2440

## Summary

The gene submitted for annotation under the symbol **"phaB"** (UniProt accession **Q88D24**, ordered locus **PP_5004**) in *Pseudomonas putida* KT2440 does **not** encode a PhaB acetoacetyl-CoA reductase. Instead, it is the **intracellular medium-chain-length polyhydroxyalkanoate (mcl-PHA) depolymerase**, correctly designated **phaZ**. The UniProt "SubName" already flags this ("Poly(3-hydroxyalkanoate) depolymerase; EC=3.1.1.-"), and the experimental literature is unambiguous: PP_5004/Q88D24 is the *P. putida* PhaZ enzyme. The gene name "phaB" carried by the EMBL record AAN70570.1 is a legacy/ambiguous locus label and should not be confused with the reductase PhaB of the classical *phbCAB* short-chain-length PHA operons of organisms such as *Ralstonia eutropha*. All functional statements below apply to the α/β-hydrolase depolymerase, consistent with the annotated domains (AB_hydrolase_1 PF00561; AB_hydrolase_fold IPR029058; PHA_depoly_arom IPR011942).

**Primary function.** PhaZ is a **serine hydrolase (α/β-hydrolase fold) that specifically hydrolyzes intracellular mcl-PHA polyester** — for example poly-3-hydroxyoctanoate and copolymers bearing both aliphatic and aromatic side chains — releasing **(R)-3-hydroxyalkanoic acid monomers and oligomers**. This activity was demonstrated biochemically by purifying the enzyme after heterologous overexpression, where it was inhibited by the serine-hydrolase inhibitor PMSF. Structurally, PhaZ is built from a core α/β-hydrolase domain capped by a **lipase-like "lid" domain** that is essential for activity on the water-insoluble polyester substrate — a feature that distinguishes intracellular from extracellular PHA depolymerases.

**Localization and pathway.** PhaZ acts at the **surface of cytoplasmic PHA storage granules ("carbonosomes")**, where it operates alongside the PHA synthases PhaC1/PhaC2 to drive a continuous **PHA turnover cycle**. When exogenous carbon becomes limiting, PhaZ mobilizes the stored polyester, feeding (R)-3-hydroxyacids back into β-oxidation as carbon and energy sources. The *phaZ* gene is embedded in the **phaC1ZC2D operon**, transcribed from the P<sub>C1</sub> promoter and activated by the carbon-source–dependent TetR-family regulator **PhaD**, so that synthesis and mobilization machinery are expressed together to keep the storage cycle balanced with metabolic demand.

---

## Gene/Protein Identity Verification (MANDATORY)

The research target was supplied with gene name **"phaB"** and gene ID "phaZ." These reflect a **naming inconsistency in the source records**, not two different proteins. Verification steps and conclusions:

- **Gene symbol vs. protein description:** The UniProt SubName for Q88D24 is "Poly(3-hydroxyalkanoate) depolymerase; EC 3.1.1.-" — a hydrolase, matching the *phaZ* depolymerase, **not** a PhaB acetoacetyl-CoA reductase (EC 1.1.1.36, an oxidoreductase). The "phaB" label originates from the EMBL entry AAN70570.1 and is best treated as a locus alias.
- **Organism:** Confirmed *Pseudomonas putida* KT2440 (PP_5004). The characterized enzyme (from strain KT2442) is from a rifampicin-resistant derivative with an essentially identical genome; the two are equivalent.
- **Domains:** The annotated PF00561 (Abhydrolase_1), IPR029058 (AB_hydrolase_fold), and IPR011942 (**PHA_depoly_arom** — PHA depolymerase, aromatic) align precisely with the depolymerase function and its ability to act on aromatic-monomer mcl-PHA.

**Conclusion of verification:** PP_5004/Q88D24 should be annotated as **phaZ, the intracellular mcl-PHA depolymerase**. The symbol "phaB" is a misleading legacy name and should be deprecated in favor of *phaZ* to avoid confusion with reductase-type PhaB proteins. Literature for this specific protein is abundant and directly on-target, so the research proceeded with confidence.

---

## Key Findings

### Finding 1 — PP_5004/Q88D24 is a specific intracellular mcl-PHA depolymerase (a serine hydrolase), *not* an acetoacetyl-CoA reductase

The single most decisive piece of evidence comes from de Eugenio et al. (2007), who overexpressed the *phaZ* gene of *P. putida* KT2442 in *Escherichia coli*, purified the product, and characterized its enzymology directly. They showed that **PhaZ is an intracellular depolymerase located in PHA granules that specifically hydrolyzes mcl-PHAs containing aliphatic and aromatic monomers**, and that it **behaves as a serine hydrolase inhibited by phenylmethylsulfonyl fluoride (PMSF)** ([PMID: 17170116](https://pubmed.ncbi.nlm.nih.gov/17170116/)). This is a precise, low-throughput biochemical study — exactly the class of evidence prioritized for functional annotation — and it establishes both the catalyzed reaction (ester hydrolysis of the polyester backbone) and the mechanistic class (serine hydrolase with a nucleophilic active-site serine, consistent with the α/β-hydrolase fold).

A critical identity note: the characterized enzyme is from strain **KT2442**, which is a spontaneous rifampicin-resistant derivative of **KT2440**. The two strains share essentially identical genomes, so the KT2442 *phaZ* gene product is functionally equivalent to KT2440 **PP_5004/Q88D24**. The substrate specificity is *medium*-chain-length (C6–C14 hydroxyacid side chains), which matches *P. putida*'s status as the paradigm mcl-PHA–accumulating organism and rules out the short-chain-length metabolism associated with a genuine PhaB reductase.

### Finding 2 — PhaZ is granule-bound: it localizes to the surface of cytoplasmic PHA granules (carbonosomes)

PhaZ carries out its function **at the surface of intracellular PHA granules**, not in the bulk cytoplasm or extracellularly. de Eugenio et al. (2007) explicitly state that "PhaZ is an intracellular depolymerase that is located in PHA granules" ([PMID: 17170116](https://pubmed.ncbi.nlm.nih.gov/17170116/)). This subcellular assignment is independently corroborated by granule-proteome and enzyme-activity studies of PHA granules isolated from *Pseudomonas*: **isolated PHA granules displayed both PhaC and PhaZ activities**, physically associating the depolymerase with the granule body ([PMID: 19267463](https://pubmed.ncbi.nlm.nih.gov/19267463/); see also [PMID: 20937103](https://pubmed.ncbi.nlm.nih.gov/20937103/)).

The granule ("carbonosome") is a supramolecular assembly of the polyester core coated by a proteinaceous surface layer that includes the synthases (PhaC1/PhaC2), the depolymerase (PhaZ), and structural phasins (PhaF, PhaI). Because the substrate is a solvated, amorphous polyester sequestered inside the granule, PhaZ must operate at the polymer–protein interface, which is consistent with the requirement for a lid domain (Finding 4).

### Finding 3 — PhaZ mobilizes stored PHA, releasing (R)-3-hydroxyalkanoic acids and closing the PHA turnover cycle

Genetic and physiological studies define the *in vivo* consequence of PhaZ activity. de Eugenio et al. (2010) constructed *phaC1* and *phaZ* knockout mutants of KT2442 and showed that **"under starvation conditions, PHA depolymerase (PhaZ) degrades PHA and releases R-hydroxyalkanoic acids, which can be used as carbon and energy sources,"** and that **"the coordination of PHA synthesis and mobilization pathways configures a functional PHA turnover cycle in *P. putida* KT2442"** ([PMID: 19788655](https://pubmed.ncbi.nlm.nih.gov/19788655/)). PhaZ is therefore the **degradative/mobilization arm** of a cycle in which PhaC continuously polymerizes (R)-3-hydroxyacyl-CoA into polyester while PhaZ continuously depolymerizes it back to monomers.

The direction and magnitude of PhaZ's effect are confirmed by loss- and gain-of-function experiments:

| Manipulation | Effect on mcl-PHA | Source |
|---|---|---|
| *phaZ* knockout (strain KTMQ01) | mcl-PHA content rises from ~66 to ~86 wt% on octanoate | [PMID: 19103481](https://pubmed.ncbi.nlm.nih.gov/19103481/) |
| *phaZ* overexpression (+ *fadL*, *fadD*) | Extracellular mcl-3-hydroxyacid (3HHx/3HO) secretion, up to ~5.8 g/L in fed-batch | [PMID: 18422622](https://pubmed.ncbi.nlm.nih.gov/18422622/) |

The knockout data ("accumulated 86 wt% medium-chain-length PHA … compared with … KT2442 which produced only 66 wt%", [PMID: 19103481](https://pubmed.ncbi.nlm.nih.gov/19103481/)) prove PhaZ mediates ongoing PHA degradation *in vivo*: remove it, and polymer accumulates. Conversely, driving PhaZ (together with fatty-acid import/activation) redirects the cycle toward secretion of **enantiomerically pure (R)-3-hydroxyalkanoic acids**, a biotechnological demonstration that the reaction product is the monomeric hydroxyacid.

### Finding 4 — PhaZ adopts an α/β-hydrolase fold with a lipase-like lid domain that is essential for mcl-PHA activity

The structural basis of catalysis is an **α/β-hydrolase fold with a buried catalytic triad**, capped by a **lid domain** analogous to those of lipases. de Eugenio et al. (2007) first modeled this architecture ([PMID: 17170116](https://pubmed.ncbi.nlm.nih.gov/17170116/)), consistent with the InterPro/Pfam annotation (IPR029058 AB_hydrolase_fold; PF00561 Abhydrolase_1; IPR011942 PHA_depoly_arom). A dedicated 2025 study (de Eugenio et al.) then dissected the lid experimentally, showing that PhaZ<sub>KT</sub> **"consists of an α/β-hydrolase fold with a lid domain, similar to lipases and other enzymes acting on lipid substrates, in contrast to extracellular PHA depolymerases, which generally lack this lid structure"** ([PMID: 41055782](https://pubmed.ncbi.nlm.nih.gov/41055782/)).

Crucially, targeted mutagenesis established the lid's functional importance: **"Targeted deletions within or near the lid completely abolished enzyme activity, highlighting its critical structural and functional importance"** ([PMID: 41055782](https://pubmed.ncbi.nlm.nih.gov/41055782/)). A point mutant at the lid hinge (**S184F**) *increased* generic esterase activity on the soluble model substrate p-nitrophenyl ester while *reducing* mcl-PHA depolymerase activity — demonstrating that the lid governs recognition and processing of the bulky, hydrophobic polyester rather than simple ester hydrolysis. This is the mechanistic hallmark distinguishing intracellular mcl-PHA depolymerases from lidless extracellular PHA depolymerases and from ordinary esterases.

### Finding 5 — *phaZ* is co-transcribed in the phaC1ZC2D operon and activated by the carbon-source–dependent regulator PhaD

At the genetic level, *phaZ* (PP_5004) sits in the *pha* gene cluster between the two synthase genes *phaC1* (PP_5003) and *phaC2* (PP_5005), followed by the regulator *phaD*. de Eugenio et al. (2010) mapped five promoters across the cluster (P<sub>C1</sub>, P<sub>Z</sub>, P<sub>C2</sub>, P<sub>F</sub>, P<sub>I</sub>) and showed that **"P<sub>C1</sub> and P<sub>I</sub> are the most active promoters of the pha cluster allowing the transcription of phaC1ZC2D and phaIF operons"** ([PMID: 20406286](https://pubmed.ncbi.nlm.nih.gov/20406286/)). Thus *phaZ* is normally expressed as part of the **phaC1ZC2D polycistron**, guaranteeing that depolymerase and synthase machinery appear together.

Expression is controlled by **PhaD, a TetR-family transcriptional regulator that "behaves as a carbon source-dependent activator of the pha cluster"** ([PMID: 20406286](https://pubmed.ncbi.nlm.nih.gov/20406286/)). PhaD binds operators at P<sub>C1</sub> (OPRc1, 25 bp) and P<sub>I</sub> (OPRi, 29 bp); its predicted effector is a CoA-thioester metabolite of the PHA pathway (e.g., 3-hydroxyacyl-CoA), coupling *pha* gene expression to the flux of PHA precursors. This regulatory wiring explains why the cell **simultaneously** produces synthase and depolymerase, sustaining turnover rather than one-way accumulation. A later interactome study additionally links the phasin **PhaF** to PhaD, hinting at an extra layer of regulation over the *pha* promoters ([PMID: 32705785](https://pubmed.ncbi.nlm.nih.gov/32705785/)).

### Finding 6 — PhaZ activity within the carbonosome balances carbon/energy storage with metabolic demand and influences cell physiology

The authoritative review by Prieto et al. (2016) synthesizes the physiological role: PHA granules/carbonosomes are **"supramolecular complexes of biopolyester and proteins that are essential for granule segregation during cell division, and for the functioning of the PHA metabolic route as a continuous cycle,"** and **"the simultaneous activities of PHA synthase and depolymerase ensure the carbon flow to the transient demand for metabolic intermediates to balance the storage and use of carbon and energy"** ([PMID: 25556983](https://pubmed.ncbi.nlm.nih.gov/25556983/)). PhaZ is the depolymerase in that balance. Beyond metabolism, the PHA cycle also shapes bacterial cell number and size, so PhaZ activity has downstream physiological consequences (though the annotation focus remains its direct catalytic role). Jendrossek & Pfeiffer (2014) place *P. putida* as the mcl-PHA representative in the broader carbonosome surface-layer framework ([PMID: 24329995](https://pubmed.ncbi.nlm.nih.gov/24329995/)).

---

## Mechanistic Model / Interpretation

PhaZ is the **catabolic engine of the PHA storage cycle** in *P. putida* KT2440. The overall picture integrates enzymology, structure, localization, and regulation into a single coherent narrative:

```
   Fatty acids / carbon source
             │  (β-oxidation)
             ▼
   (R)-3-hydroxyacyl-CoA  ──────────────┐
             │  PhaC1/PhaC2 (synthase)   │  ANABOLIC arm
             ▼                            │
   ┌─────────────────────────────────────┴───────────┐
   │        PHA GRANULE / CARBONOSOME (cytoplasm)     │
   │   mcl-PHA polyester core (e.g. PHO)              │
   │   surface layer: PhaC, PhaZ, phasins PhaF/PhaI   │
   └─────────────────────────────────────┬───────────┘
             ▲                            │
             │  PhaZ (depolymerase)       │  CATABOLIC arm
             │  α/β-hydrolase + LID       │
   (R)-3-hydroxyalkanoic acids ◄──────────┘
             │  (re-activated → β-oxidation,
             ▼   carbon + energy)
        Central metabolism / growth

   Regulation:  P_C1 promoter → phaC1-Z-C2-D operon
                PhaD (TetR-like) activator, effector = 3-OH-acyl-CoA
```

Key mechanistic points:

1. **Reaction.** PhaZ catalyzes hydrolytic cleavage of the ester bonds of the mcl-PHA polyester (EC 3.1.1.-), yielding (R)-3-hydroxyalkanoic acid monomers/oligomers. Catalysis proceeds via an active-site serine nucleophile (α/β-hydrolase catalytic triad), evidenced by PMSF inhibition.

2. **Substrate specificity.** The enzyme is specific for **medium-chain-length** PHA (C6–C14 side chains) and tolerates both aliphatic and aromatic monomers. It is a genus-specific (Pseudomonas) intracellular depolymerase, distinct from short-chain-length (PHB) depolymerases and from lidless extracellular depolymerases.

3. **Structure–function.** The **lid domain** is the determinant of polyester (versus simple ester) activity: lid deletions abolish activity, and lid-hinge mutation (S184F) trades polyester depolymerase activity for generic esterase activity. This mirrors interfacial activation seen in lipases acting on aggregated lipid substrates.

4. **Localization.** All of this happens at the **carbonosome surface** in the cytoplasm — PhaZ is granule-bound, positioned at the polymer–water interface.

5. **Physiology & regulation.** Because *phaZ* is co-transcribed with the synthases under PhaD control, cells run synthesis and degradation **simultaneously**, buffering carbon and energy supply against fluctuating demand. This is why *phaZ* deletion raises steady-state PHA (66→86 wt%) and *phaZ* overexpression drives net monomer secretion.

---

## Evidence Base

| PMID | Study (type) | How it supports the annotation |
|---|---|---|
| [17170116](https://pubmed.ncbi.nlm.nih.gov/17170116/) | de Eugenio et al. 2007, *J Biol Chem* — purified-enzyme biochemistry | **Core identity evidence.** PhaZ = intracellular mcl-PHA depolymerase, serine hydrolase (PMSF-inhibited), granule-localized; specifies substrate (aliphatic + aromatic mcl-PHA). |
| [19788655](https://pubmed.ncbi.nlm.nih.gov/19788655/) | de Eugenio et al. 2010, *Environ Microbiol* — knockout/physiology | Defines PhaZ as the mobilization arm; degrades PHA under starvation → (R)-hydroxyacids; establishes the PHA turnover cycle. |
| [19103481](https://pubmed.ncbi.nlm.nih.gov/19103481/) | Cai et al. 2009 — *phaZ* knockout | Loss-of-function: PHA rises 66→86 wt%, proving *in vivo* degradative role. |
| [18422622](https://pubmed.ncbi.nlm.nih.gov/18422622/) | Yuan et al. 2008 — overexpression | Gain-of-function: PhaZ drives extracellular mcl-3-hydroxyacid production; confirms monomeric product. |
| [41055782](https://pubmed.ncbi.nlm.nih.gov/41055782/) | de Eugenio et al. 2025 — structure/mutagenesis | α/β-hydrolase + essential lid; lid deletions abolish activity; S184F shifts specificity. |
| [20406286](https://pubmed.ncbi.nlm.nih.gov/20406286/) | de Eugenio et al. 2010 — promoter mapping | *phaZ* is in the phaC1ZC2D operon (P<sub>C1</sub>); PhaD is a carbon-source-dependent activator. |
| [25556983](https://pubmed.ncbi.nlm.nih.gov/25556983/) | Prieto et al. 2016, *Environ Microbiol* — authoritative review | Places PhaZ in the carbonosome; synthase+depolymerase balance carbon/energy. |
| [19267463](https://pubmed.ncbi.nlm.nih.gov/19267463/) | Ren et al. 2009 — granule activities | Isolated granules show both PhaC and PhaZ activities (localization). |
| [20937103](https://pubmed.ncbi.nlm.nih.gov/20937103/) | Ren et al. 2010 — *P. putida* U enzymology | PhaC and PhaZ concomitantly active → parallel synthesis/degradation. |
| [24329995](https://pubmed.ncbi.nlm.nih.gov/24329995/) | Jendrossek & Pfeiffer 2014 — carbonosome review | Framework for granule formation; *P. putida* as mcl-PHA representative. |
| [32705785](https://pubmed.ncbi.nlm.nih.gov/32705785/) | Maestro et al. 2020 — PhaF interactome | Links phasin PhaF to PhaD, extending regulatory context of the *phaZ* operon. |
| [23457638](https://pubmed.ncbi.nlm.nih.gov/23457638/) / [21219460](https://pubmed.ncbi.nlm.nih.gov/21219460/) | PhaF structure / granule segregation | Context on the granule surface layer where PhaZ operates. |

**Convergence.** Across biochemistry (17170116), genetics (19788655, 19103481, 18422622), structure (41055782), regulation (20406286), and reviews (25556983, 24329995), the evidence converges without contradiction on a single function: an intracellular, granule-bound, mcl-PHA-specific serine-hydrolase depolymerase.

---

## Limitations and Knowledge Gaps

1. **No experimental 3D structure of PP_5004 itself.** The α/β-hydrolase-plus-lid architecture rests on homology modeling plus mutagenesis ([PMID: 17170116](https://pubmed.ncbi.nlm.nih.gov/17170116/); [PMID: 41055782](https://pubmed.ncbi.nlm.nih.gov/41055782/)). A crystal or cryo-EM structure with a bound substrate analog would confirm the catalytic triad geometry, the oxyanion hole, and the exact lid conformational change.

2. **Precise catalytic residues not enumerated here.** The serine-hydrolase mechanism is established (PMSF inhibition), but the exact Ser–His–Asp/Glu triad positions in PP_5004 have not been individually mutated and reported in the reviewed evidence set.

3. **Product distribution.** *In vivo* data show release of (R)-3-hydroxyacid monomers; the balance of monomer vs. oligomer release, processivity/exo- vs. endo-cleavage, and whether a second downstream hydrolase (oligomer hydrolase) participates are not fully resolved for KT2440.

4. **Effector identity of PhaD.** The activating effector is *predicted* to be a 3-hydroxyacyl-CoA; direct binding/structural confirmation for the KT2440 system was not part of the reviewed evidence.

5. **Strain transferability.** Most enzymology is from KT2442; while genomically equivalent, formal confirmation with the KT2440 PP_5004 ORF strengthens the annotation.

6. **Quantitative kinetics.** Michaelis–Menten parameters (k_cat, K_M) against defined mcl-PHA substrates of varying chain length were not tabulated in the reviewed sources, limiting quantitative substrate-specificity statements.

---

## Proposed Follow-up Experiments / Actions

1. **Solve the PhaZ structure.** Crystallize (or cryo-EM) recombinant PP_5004 PhaZ, ideally as a covalent complex with a serine-trapping inhibitor or a soluble hydroxyacyl-ester analog, to visualize the catalytic triad, oxyanion hole, and lid open/closed states.

2. **Alanine-scan the catalytic triad and oxyanion hole.** Mutate the predicted Ser/His/Asp(Glu) residues individually and assay mcl-PHA depolymerase vs. p-nitrophenyl-ester activity to formally assign the mechanism in PP_5004 (complementing the S184F lid result).

3. **Full kinetic characterization.** Measure k_cat/K_M against a panel of defined mcl-PHAs (C6–C14, aliphatic and aromatic monomers) and amorphous vs. semicrystalline granules to quantify substrate specificity and interfacial activation.

4. **Product analysis.** Use LC–MS/NMR time courses on purified enzyme + isolated granules to determine monomer:oligomer ratios and endo- vs. exo-cleavage mode; test whether a downstream oligomer hydrolase is required for complete turnover.

5. **Confirm PhaD effector.** Perform ITC/EMSA of purified PhaD with candidate 3-hydroxyacyl-CoA effectors to validate the carbon-source-sensing mechanism controlling the phaC1ZC2D operon.

6. **KT2440-native validation.** Re-express and characterize the exact PP_5004 ORF, and construct clean in-frame *phaZ* deletions/complementations in KT2440 to reconfirm the 66→86 wt% accumulation phenotype in the reference strain.

7. **Annotation correction.** Submit a curation request to update UniProt/EMBL to preferentially name the gene *phaZ* (retaining "phaB" only as an alias), reducing the risk of confusion with acetoacetyl-CoA reductase.


## Artifacts

- [OpenScientist final report](phaZ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](phaZ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:17170116
2. PMID:19267463
3. PMID:20937103
4. PMID:19788655
5. PMID:19103481
6. PMID:18422622
7. PMID:41055782
8. PMID:20406286
9. PMID:32705785
10. PMID:25556983
11. PMID:24329995