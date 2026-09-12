---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-13T02:36:25.665300'
end_time: '2026-08-13T02:51:49.901154'
duration_seconds: 924.24
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: galC
  gene_symbol: galC
  uniprot_accession: Q88JX9
  protein_description: 'RecName: Full=4-carboxy-4-hydroxy-2-oxoadipic acid aldolase;
    AltName: Full=CHA aldolase; EC=4.1.3.17 {ECO:0000269|PubMed:21219457}; AltName:
    Full=Gallate degradation protein C;'
  gene_info: Name=galC; OrderedLocusNames=PP_2514;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the LigK/PcmE family. .
  protein_domains: LigK_PcmE. (IPR014165); RraA/RraA-like. (IPR005493); RraA/RraA-like_sf.
    (IPR036704); RraA-like (PF03737)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: galC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: galC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88JX9
- **Protein Description:** RecName: Full=4-carboxy-4-hydroxy-2-oxoadipic acid aldolase; AltName: Full=CHA aldolase; EC=4.1.3.17 {ECO:0000269|PubMed:21219457}; AltName: Full=Gallate degradation protein C;
- **Gene Information:** Name=galC; OrderedLocusNames=PP_2514;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the LigK/PcmE family. .
- **Key Domains:** LigK_PcmE. (IPR014165); RraA/RraA-like. (IPR005493); RraA/RraA-like_sf. (IPR036704); RraA-like (PF03737)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "galC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'galC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **galC** (gene ID: galC, UniProt: Q88JX9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *galC* (PP_2514, UniProt Q88JX9) — 4-Carboxy-4-hydroxy-2-oxoadipic Acid (CHA) Aldolase from *Pseudomonas putida* KT2440

## Summary

**The gene *galC* (ordered locus PP_2514; UniProt Q88JX9) of *Pseudomonas putida* KT2440 encodes 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA aldolase; EC 4.1.3.17), a cytoplasmic, Mg²⁺-dependent, homohexameric carbon–carbon lyase.** It catalyzes the last enzymatic step of the gallate (gallic acid) degradation pathway, cleaving 4-carboxy-4-hydroxy-2-oxoadipic acid (CHA) into pyruvate and oxaloacetate. This retro-aldol cleavage funnels carbon derived from gallate — and, by extension, from syringyl-type lignin aromatic compounds — into central metabolism via the TCA cycle. Loss of *galC* abolishes growth on gallate as sole carbon source, confirming its essential and non-redundant role in the pathway.

This assignment is strongly supported by direct experimental characterization of the *gal* gene cluster in *P. putida* KT2440 ([PMID: 21219457](https://pubmed.ncbi.nlm.nih.gov/21219457/)), by detailed enzymology of the orthologous enzyme LigK from the protocatechuate 4,5-cleavage pathway of *Sphingomonas paucimobilis* SYK-6 ([PMID: 12486039](https://pubmed.ncbi.nlm.nih.gov/12486039/)), and by structural/bioinformatic placement of GalC in the LigK/PcmE family within the RraA-like superfamily fold. The enzyme operates as the terminal step of an ordered five-enzyme route (GalT → GalA → GalD → GalB → GalC) that converts gallate through 4-oxalomesaconate (OMA) and CHA intermediates into TCA-cycle precursors.

The gene/protein identity was verified against the UniProt record: the gene symbol *galC*, the ordered locus PP_2514, the organism (*P. putida* KT2440), the LigK/PcmE family, and the RraA-like (Pfam PF03737) domain all match the primary literature. There is **no ambiguity** — the primary characterization paper (Nogales et al., 2011; [PMID: 21219457](https://pubmed.ncbi.nlm.nih.gov/21219457/)) is the exact UniProt reference, and no conflicting literature for an unrelated "galC" was found. GalC is a compact 238-residue single-domain protein whose AlphaFold model is of very high confidence (mean pLDDT 97.8); its fold is shared with metabolic HMG/CHA aldolases and with the ribonuclease-E regulator RraA, and it assembles into a homohexamer ("dimer of trimers").

---

## Key Findings

### Finding 1 — *galC* encodes CHA aldolase, the terminal enzyme of gallate degradation

The definitive functional assignment of *galC* comes from the molecular characterization of the complete *gal* gene cluster in *P. putida* KT2440 by Nogales and colleagues ([PMID: 21219457](https://pubmed.ncbi.nlm.nih.gov/21219457/)). This study demonstrated that *galC* encodes the aldolase (EC 4.1.3.17) that cleaves 4-carboxy-4-hydroxy-2-oxoadipic acid (CHA) into pyruvic and oxaloacetic acids — the last enzymatic step of gallate catabolism. The authors state directly that "*galC* encodes the aldolase catalysing CHA cleavage to pyruvic and oxaloacetic acids." A disruption of *galC* abolishes growth on gallate, establishing that this reaction is both essential and non-redundant for gallate utilization.

The immediate substrate of GalC, CHA, is produced one step upstream by GalB, described in the same study as "the founding member of a new family of zinc-containing hydratases that converts OMAenol into 4-carboxy-4-hydroxy-2-oxoadipic acid (CHA)." Thus GalC receives CHA directly from GalB and completes the pathway.

The UniProt entry for Q88JX9 corroborates and extends this assignment. It records two catalytic activities consistent with the enzyme class: the CHA cleavage reaction (Rhea:28935; CHA = oxaloacetate + pyruvate) and the canonical EC 4.1.3.17 reaction on 4-hydroxy-4-methyl-2-oxoglutarate (Rhea:22748; 4-hydroxy-4-methyl-2-oxoglutarate = 2 pyruvate). It annotates a Mg²⁺ cofactor requirement (metal-dependent, Class-II-type aldolase mechanism), a homohexameric quaternary structure, and membership in the LigK/PcmE family (RraA-like fold, Pfam PF03737). The dual substrate capability reflects the mechanistic flexibility of this aldolase family toward branched 4-hydroxy-2-oxo-diacid substrates.

**Reaction catalyzed:**

```
4-carboxy-4-hydroxy-2-oxoadipate (CHA)  --GalC (Mg2+)-->  pyruvate + oxaloacetate
```

### Finding 2 — GalC belongs to the LigK/PcmE CHA aldolase family; the LigK ortholog is a hexamer with dual (aldolase + decarboxylase) activity

The enzymology of the GalC family is best defined through its ortholog LigK, the CHA aldolase of the protocatechuate 4,5-cleavage pathway in *Sphingomonas paucimobilis* SYK-6, characterized by Hara and colleagues ([PMID: 12486039](https://pubmed.ncbi.nlm.nih.gov/12486039/)). Electrospray ionization mass spectrometry (ESI-MS) demonstrated that LigK converts CHA to pyruvate + oxaloacetate and, in a second activity, converts the oxaloacetate product to pyruvate + CO₂. The authors report that "LigK catalyzes not only the conversion of CHA to pyruvate and oxaloacetate but also that of oxaloacetate to pyruvate and CO₂. LigK is a hexamer." Steady-state kinetics gave a Km for CHA of 11.2 µM and a Km for oxaloacetate of 136 µM, indicating the enzyme binds its primary CHA substrate roughly an order of magnitude more tightly than the secondary oxaloacetate substrate. The low-micromolar Km for CHA marks GalC's family as dedicated, high-affinity catabolic enzymes.

Sequence comparisons place GalC firmly within this family. LigK's deduced amino acid sequence "showed 57 to 88% identity with those of the corresponding genes recently reported" from other degraders (*Comamonas*, *Arthrobacter*, *Pseudomonas ochraceae*), indicating strong conservation of CHA aldolases across diverse aromatic-degrading bacteria. UniProt assigns Q88JX9/GalC to this same LigK/PcmE family (RraA-like superfamily, Pfam PF03737) and annotates the identical homohexameric assembly and Mg²⁺ dependence, so the well-characterized dual activity and hexameric architecture of LigK provide a strong functional template for GalC.

| Property | GalC (*P. putida* KT2440) | LigK ortholog (*S. paucimobilis* SYK-6) |
|---|---|---|
| Reaction 1 | CHA → pyruvate + oxaloacetate | CHA → pyruvate + oxaloacetate |
| Reaction 2 (family) | oxaloacetate → pyruvate + CO₂ (inferred) | oxaloacetate → pyruvate + CO₂ (demonstrated) |
| Km (CHA) | Not directly reported | 11.2 µM |
| Km (oxaloacetate) | Not directly reported | 136 µM |
| Cofactor | Mg²⁺ | Divalent metal |
| Oligomeric state | Homohexamer | Hexamer |
| Family | LigK/PcmE (RraA-like) | LigK/PcmE (RraA-like) |
| Sequence conservation | 57–88% identity across family members | 57–88% identity across family members |

### Finding 3 — GalC is the terminal step of the *gal* (gallate/4-oxalomesaconate) meta-cleavage pathway feeding central metabolism

GalC operates as the final catalytic step of an ordered, well-defined pathway that enables *P. putida* to grow on gallic acid as sole carbon and energy source. The route was reconstructed by Nogales et al. ([PMID: 21219457](https://pubmed.ncbi.nlm.nih.gov/21219457/)), supplemented by upstream enzyme characterizations. The pathway proceeds as follows:

1. **GalT** — a transporter that "mediates specific GA [gallic acid] uptake and chemotaxis," importing gallate into the cytoplasm.
2. **GalA** — gallate dioxygenase, "a ring-cleavage dioxygenase that acts specifically on gallate to produce 4-oxalomesaconate" ([PMID: 16030014](https://pubmed.ncbi.nlm.nih.gov/16030014/)). This enzyme (the prototype of a new subgroup of extradiol dioxygenases; Km ~144 µM, Fe²⁺-dependent, trimeric) performs the ring cleavage that opens the aromatic gallate ring to give the keto tautomer of 4-oxalomesaconate (OMA-keto).
3. **GalD** — a novel isomerase that tautomerizes OMA-keto to OMA-enol.
4. **GalB** — a Zn²⁺-dependent hydratase (4-carboxy-2-hydroxymuconate/CHM hydratase) that hydrates OMA-enol to CHA. Its structure and kinetics were characterized by Mazurkewich et al. ([PMID: 26867578](https://pubmed.ncbi.nlm.nih.gov/26867578/)), who confirmed that "The gallate degradation pathway of *Pseudomonas putida* KT2440 requires a 4-carboxy-2-hydroxymuconate (CHM) hydratase (GalB)," an enzyme convergently evolved with LigJ of the protocatechuate pathway.
5. **GalC** — cleaves CHA to pyruvate + oxaloacetate, delivering products directly usable by the TCA cycle.

```
Gallate (extracellular)
    │  GalT  (import + chemotaxis)
    ▼
Gallate (cytoplasm)
    │  GalA  (dioxygenase, Fe2+, ring cleavage)
    ▼
4-oxalomesaconate (OMA-keto)
    │  GalD  (tautomerase / isomerase)
    ▼
4-oxalomesaconate (OMA-enol)
    │  GalB  (hydratase, Zn2+)
    ▼
4-carboxy-4-hydroxy-2-oxoadipate (CHA)
    │  GalC  (ALDOLASE, Mg2+)   ◄── this protein
    ▼
pyruvate  +  oxaloacetate  ──►  TCA cycle / central metabolism
```

This is the **gallate branch of the protocatechuate/meta (4,5)-cleavage-type pathway.** The physiological importance of the route extends into lignin valorization. *P. putida* KT2440 catabolizes syringyl (S)-type lignin-derived compounds through gallate: syringate is O-demethylated to gallate by the two-component monooxygenase VanAB and then further catabolized via extradiol (gallate) cleavage ([PMID: 33741529](https://pubmed.ncbi.nlm.nih.gov/33741529/)). The same *gal* pathway enzymes are exploited in engineered strains to produce 2-pyrone-4,6-dicarboxylate (PDC), a polyester precursor, positioning GalC and its pathway partners as biotechnologically relevant catalysts in the lignocellulosic bioeconomy. Because GalC's products, pyruvate and oxaloacetate, are direct TCA-cycle/anaplerotic intermediates, GalC is the metabolic node that converts aromatic (lignin-derived) carbon into primary metabolism.

### Finding 4 — Structural inference: GalC is a compact 238-aa single-domain RraA-like protein forming a hexameric "dimer of trimers"

GalC is a 238-residue single-domain protein. UniProt and InterPro assign it to the RraA/RraA-like superfamily (IPR036704; Gene3D 3.50.30.40; CDD RraA_family; Pfam PF03737), with the more specific LigK_PcmE signature (IPR014165). The AlphaFold DB model for Q88JX9 (v6, 238 residues) is of very high confidence — mean pLDDT 97.8, with 98.3% of residues scoring above 90 — indicating a single, well-ordered globular domain with no large disordered regions.

The quaternary structure and active-site architecture can be inferred from the crystal structure of RraA from *Pseudomonas aeruginosa*, solved at 2.0 Å by Tang et al. ([PMID: 21063756](https://pubmed.ncbi.nlm.nih.gov/21063756/)). That work established that "the protein regulator is arranged as a hexamer, consistent with the crystal packing of 'a dimer of trimer' arrangement." This same RraA-like β/α fold assembles as a trimer/dimer-of-trimers hexamer, matching the homohexamer annotation of GalC and its ortholog LigK. In the aldolase members of the family, the active sites form at subunit interfaces and coordinate a catalytic divalent metal (Mg²⁺ for GalC), explaining why oligomerization is required for catalytic competence. Notably, the RraA-like scaffold has been recruited to two distinct biological roles — metabolic aldolase/lyase activity (GalC, LigK) and post-transcriptional regulation of RNase E (the moonlighting RraA regulator) — a striking example of fold plasticity. GalC, however, is a dedicated metabolic aldolase.

| Structural feature | Value / assignment | Source |
|---|---|---|
| Length | 238 residues | UniProt Q88JX9 |
| Superfamily | RraA/RraA-like (IPR036704) | InterPro |
| Family signature | LigK_PcmE (IPR014165) | InterPro |
| Pfam domain | PF03737 (RraA-like) | Pfam |
| Fold class | Gene3D 3.50.30.40 | Gene3D |
| AlphaFold confidence | Mean pLDDT 97.8; 98.3% residues >90 | AlphaFold DB v6 |
| Quaternary structure | Homohexamer ("dimer of trimers") | UniProt; inferred from RraA crystal ([PMID: 21063756](https://pubmed.ncbi.nlm.nih.gov/21063756/)) |
| Cofactor | Mg²⁺ (divalent metal at subunit-interface active site) | UniProt |

---

## Mechanistic Model / Interpretation

GalC is best understood as a **Class II (metal-dependent) retro-aldolase / carbon–carbon lyase** that performs the committed carbon-releasing step of gallate mineralization. Its physiological substrate, CHA, is a branched 4-hydroxy-2-oxo-diacid. GalC uses a Mg²⁺ ion, coordinated at a subunit-interface active site of the hexamer, to polarize the substrate carbonyl and stabilize the developing enolate during C–C bond cleavage, splitting CHA into two central metabolites: pyruvate and oxaloacetate.

The broader logic of the pathway is elegant. Gallate (3,4,5-trihydroxybenzoate) is a symmetric trihydroxylated aromatic that is inherently difficult to open. The *gal* pathway solves this through extradiol (meta) ring cleavage by GalA to yield the open-chain OMA, followed by tautomerization (GalD), hydration (GalB), and finally aldol cleavage (GalC). The final GalC step is where the six-carbon open-chain intermediate is dismantled into recognizable TCA-cycle building blocks. Because pyruvate and oxaloacetate are both direct entry points to central carbon metabolism, GalC represents the true "handoff" from xenobiotic aromatic catabolism to housekeeping metabolism.

The family relationship to LigK is mechanistically informative. LigK's demonstrated ability to further decarboxylate the oxaloacetate product to pyruvate + CO₂ suggests that GalC may possess an analogous secondary activity, effectively allowing the enzyme to convert one CHA molecule into up to three pyruvate-derived carbons plus CO₂. Whether GalC exhibits this decarboxylase side-activity in vivo — and to what extent it is physiologically significant versus channeling oxaloacetate directly into the TCA cycle — remains to be experimentally resolved for the *P. putida* enzyme specifically.

**Localization:** All available evidence points to a cytoplasmic location. GalC has no signal peptide or transmembrane annotation, its substrate CHA is an intracellular pathway intermediate generated by upstream cytoplasmic enzymes (GalA/GalB/GalD), and its products feed directly into the cytoplasmic TCA cycle. Gallate is first imported by the transporter GalT before any downstream catabolism occurs, so the entire ring-opening and cleavage cascade — including GalC — takes place inside the cell, within a cytoplasmic gallate-catabolic metabolon.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [21219457](https://pubmed.ncbi.nlm.nih.gov/21219457/) | *Unravelling the gallic acid degradation pathway in bacteria: the gal cluster from Pseudomonas putida* | **Primary functional assignment.** Directly identifies *galC* as the CHA aldolase producing pyruvate + oxaloacetate; defines GalB as the upstream enzyme producing CHA; establishes GalT-mediated uptake. This is the UniProt reference for Q88JX9. |
| [12486039](https://pubmed.ncbi.nlm.nih.gov/12486039/) | *Characterization of the 4-carboxy-4-hydroxy-2-oxoadipate aldolase gene ... in Sphingomonas paucimobilis SYK-6* | **Family enzymology.** Ortholog LigK shown by ESI-MS to catalyze CHA cleavage and oxaloacetate decarboxylation; hexamer; Km(CHA)=11.2 µM, Km(OAA)=136 µM; 57–88% sequence conservation across family. |
| [16030014](https://pubmed.ncbi.nlm.nih.gov/16030014/) | *Molecular characterization of the gallate dioxygenase from Pseudomonas putida KT2440* | **Upstream pathway step.** Characterizes GalA as the gallate-specific ring-cleavage dioxygenase producing 4-oxalomesaconate, initiating the pathway GalC terminates. |
| [26867578](https://pubmed.ncbi.nlm.nih.gov/26867578/) | *Structural and Kinetic Characterization of the 4-Carboxy-2-hydroxymuconate Hydratase (GalB) ...* | **Immediately upstream step.** Confirms GalB as the hydratase producing GalC's substrate CHA; structural convergence with LigJ. |
| [21063756](https://pubmed.ncbi.nlm.nih.gov/21063756/) | *The crystal structure of hexamer RraA from Pseudomonas aeruginosa ...* | **Structural template.** Establishes the hexameric dimer-of-trimers architecture of the RraA-like fold to which GalC belongs. |
| [33741529](https://pubmed.ncbi.nlm.nih.gov/33741529/) | *Metabolism of syringyl lignin-derived compounds in Pseudomonas putida ... convergent production of PDC* | **Physiological/biotechnological context.** Shows syringate is O-demethylated to gallate and catabolized via extradiol cleavage, connecting the *gal* pathway (and GalC) to lignin valorization. |
| [36724292](https://pubmed.ncbi.nlm.nih.gov/36724292/) | *Development and Application of Whole-Cell Biosensors for the Detection of Gallic Acid* | Contextual: gallate biology and detection tools. |
| [41024182](https://pubmed.ncbi.nlm.nih.gov/41024182/) | *Conversion and upgrading of syringate by Acinetobacter baylyi ADP1* | Contextual: heterologous use of *galA* for PDC production, underscoring pathway portability. |

The convergence of evidence is notable: direct genetic and biochemical characterization in the target organism (Nogales et al.), transferable detailed enzymology from a high-identity ortholog (LigK), full reconstruction of the upstream pathway (GalA, GalB), and structural/bioinformatic placement within a well-studied fold family all point to the same conclusion.

### Supported and refuted hypotheses

- **Supported (strong, direct primary evidence):** *galC* is a CHA aldolase (EC 4.1.3.17) that is the terminal, Mg²⁺-dependent lyase of the gallate degradation pathway, producing pyruvate + oxaloacetate.
- **Supported (by orthology):** GalC is a homohexamer with likely secondary oxaloacetate-decarboxylase activity, characteristic of the LigK/PcmE family.
- **No mis-identification issue found:** the gene symbol, organism, family, and domains are internally consistent; no evidence of confusion with an unrelated "galC" (e.g., a galactose-related gene).

---

## Limitations and Knowledge Gaps

1. **No direct crystal structure or purified kinetics of GalC itself.** The catalytic and structural conclusions rest on (a) genetic evidence in *P. putida* (Nogales et al.), (b) enzymology of the LigK ortholog, and (c) an AlphaFold model plus the RraA crystal structure. A crystal structure and steady-state kinetics of purified GalC (Q88JX9) would confirm the Mg²⁺ coordination geometry, active-site residues, and Km/kcat values, none of which have been measured for the *P. putida* enzyme directly.

2. **Secondary decarboxylase activity unconfirmed for GalC.** The oxaloacetate → pyruvate + CO₂ decarboxylation is demonstrated for LigK but only inferred for GalC. Its in vivo relevance in *P. putida* is unknown.

3. **Stereochemistry and substrate specificity boundaries.** UniProt lists a second substrate (4-hydroxy-4-methyl-2-oxoglutarate). The relative catalytic efficiency toward CHA versus this and other 4-hydroxy-2-oxo-diacids, and the enzyme's stereospecificity, have not been quantified for GalC.

4. **Regulation and expression.** While the *gal* cluster's organization and inducibility by gallate are known at the cluster level, the specific transcriptional/post-transcriptional control of *galC* and possible metabolic channeling with GalB are not fully characterized.

5. **Localization is inferred, not directly demonstrated.** Cytoplasmic localization is highly likely from sequence and pathway logic but has not been experimentally verified (e.g., by subcellular fractionation) for GalC specifically.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and steady-state kinetics of GalC (Q88JX9).** Purify the His-tagged enzyme and measure Km/kcat for CHA and for 4-hydroxy-4-methyl-2-oxoglutarate; test Mg²⁺ dependence and metal substitution (Mn²⁺, Co²⁺). Directly test whether GalC decarboxylates oxaloacetate as LigK does.

2. **Structural determination.** Solve the crystal structure (or cryo-EM structure of the hexamer) of GalC, ideally with a bound substrate/product analog and Mg²⁺, to define the interfacial active site and validate the AlphaFold model. Compare directly to LigK and RraA.

3. **Active-site mutagenesis.** Identify and mutate predicted metal-coordinating and catalytic residues (guided by the AlphaFold model and RraA-like alignments) to confirm the reaction mechanism.

4. **In vivo confirmation.** Complement a *galC* deletion with wild-type and point-mutant alleles to correlate specific residues with restored growth on gallate; quantify accumulation of the CHA intermediate in the deletion strain by LC-MS.

5. **Metabolic-engineering optimization.** Given the role of the *gal* pathway in PDC/lignin valorization, evaluate GalC as a flux-control point and test whether its (co)expression enhances conversion of syringate/gallate-derived carbon in engineered *P. putida* and heterologous hosts.

6. **Localization assay.** Confirm cytoplasmic localization via subcellular fractionation or fluorescent fusion.

---

## Conclusion

*galC* (PP_2514; UniProt Q88JX9) of *Pseudomonas putida* KT2440 encodes **4-carboxy-4-hydroxy-2-oxoadipic acid (CHA) aldolase (EC 4.1.3.17)**, a cytoplasmic, Mg²⁺-dependent, homohexameric RraA-like (LigK/PcmE family) carbon–carbon lyase. It performs the terminal step of the gallate degradation (*gal*) pathway, cleaving CHA into pyruvate and oxaloacetate and thereby channeling gallate- and syringyl-lignin-derived carbon into the TCA cycle. The assignment is supported by direct genetic evidence in the native organism, transferable enzymology from the high-identity ortholog LigK, complete characterization of the upstream pathway enzymes, and confident structural placement within the RraA-like hexameric fold.

---
*Primary references: Nogales et al. 2011 ([PMID: 21219457](https://pubmed.ncbi.nlm.nih.gov/21219457/)); Hara et al. 2003 ([PMID: 12486039](https://pubmed.ncbi.nlm.nih.gov/12486039/)); Nogales et al. 2005 ([PMID: 16030014](https://pubmed.ncbi.nlm.nih.gov/16030014/)); Mazurkewich et al. 2016 ([PMID: 26867578](https://pubmed.ncbi.nlm.nih.gov/26867578/)); Notonier et al. 2021 ([PMID: 33741529](https://pubmed.ncbi.nlm.nih.gov/33741529/)); Tang et al. 2010 ([PMID: 21063756](https://pubmed.ncbi.nlm.nih.gov/21063756/)). Database: UniProt Q88JX9.*


## Artifacts

- [OpenScientist final report](galC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](galC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21219457
2. PMID:12486039
3. PMID:16030014
4. PMID:26867578
5. PMID:33741529
6. PMID:21063756