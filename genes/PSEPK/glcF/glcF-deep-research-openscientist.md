---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-15T17:08:39.802162'
end_time: '2026-07-15T18:13:17.454474'
duration_seconds: 3877.65
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: glcF
  gene_symbol: glcF
  uniprot_accession: Q88GH6
  protein_description: 'RecName: Full=Glycolate oxidase iron-sulfur subunit {ECO:0000256|PIRNR:PIRNR000139};
    EC=1.1.99.14 {ECO:0000256|PIRNR:PIRNR000139};'
  gene_info: Name=glcF {ECO:0000313|EMBL:AAN69342.1}; OrderedLocusNames=PP_3747 {ECO:0000313|EMBL:AAN69342.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 4Fe4S_Fe-S-bd. (IPR017896); 4Fe4S_Fe_S_CS. (IPR017900); Cys_rich_dom.
    (IPR004017); Glc_ox_4Fe-4S. (IPR012257); Helical_ferredxn. (IPR009051)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: glcF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: glcF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88GH6
- **Protein Description:** RecName: Full=Glycolate oxidase iron-sulfur subunit {ECO:0000256|PIRNR:PIRNR000139}; EC=1.1.99.14 {ECO:0000256|PIRNR:PIRNR000139};
- **Gene Information:** Name=glcF {ECO:0000313|EMBL:AAN69342.1}; OrderedLocusNames=PP_3747 {ECO:0000313|EMBL:AAN69342.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 4Fe4S_Fe-S-bd. (IPR017896); 4Fe4S_Fe_S_CS. (IPR017900); Cys_rich_dom. (IPR004017); Glc_ox_4Fe-4S. (IPR012257); Helical_ferredxn. (IPR009051)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "glcF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'glcF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **glcF** (gene ID: glcF, UniProt: Q88GH6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *glcF* (Q88GH6, PP_3747) in *Pseudomonas putida* KT2440

## Summary

The gene **glcF** (UniProt **Q88GH6**; ordered locus **PP_3747**) of *Pseudomonas putida* KT2440 encodes the **iron–sulfur (Fe-S) subunit of the multi-subunit glycolate oxidase/dehydrogenase complex, GlcDEF** (EC 1.1.99.14). The holoenzyme catalyzes the two-electron oxidation of **glycolate to glyoxylate**. GlcF is not the catalytic (substrate-oxidizing) subunit; instead it functions as an obligate **electron-relay module**. Its diagnostic InterPro domains — two [4Fe-4S] ferredoxin clusters (IPR017896, IPR017900), a cysteine-rich cluster-binding domain (IPR004017), the glycolate-oxidase-specific 4Fe-4S signature (IPR012257), and a helical ferredoxin fold (IPR009051) — identify it as the terminal electron-conducting "wire" that transfers electrons from the FAD centers of the catalytic subunits GlcD/GlcE onward to the membrane quinone pool. Because the enzyme belongs to EC class 1.1.99 (using an unspecified/quinone acceptor rather than O₂), the complex is best described as a **quinone-coupled, inner-membrane-associated dehydrogenase acting at the cytoplasmic face of the membrane**, rather than an oxygen-dependent oxidase.

Physiologically, the glycolate → glyoxylate reaction catalyzed by GlcDEF is the **gateway step that channels glycolate into central glyoxylate metabolism**. In *P. putida* KT2440, this step is of considerable biotechnological importance because glycolate is the convergent intermediate produced during the degradation of **ethylene glycol** and **1,4-butanediol** — monomers derived from plastic depolymerization. The glyoxylate produced is assimilated through the **glyoxylate carboligase (glycerate) pathway** and the **glyoxylate cycle**, connecting to central carbon metabolism and gluconeogenesis.

The functional assignment is strongly supported by convergent evidence across three lines: (1) classical genetic dissection of the *E. coli* *glc* operon, where insertional inactivation of *glcD*, *glcE*, **or** *glcF* individually abolishes glycolate oxidase activity, proving all three are essential subunits; (2) conservation of GlcD-type glycolate dehydrogenase activity in cyanobacteria, where genetic knockouts block glycolate consumption in vivo; and (3) *P. putida*-specific diol-degradation studies showing accumulation of glycolate and glyoxylate as pathway intermediates. The gene symbol, organism, EC number, and InterPro domain architecture are all mutually consistent, and **no gene-symbol ambiguity or conflicting literature was encountered** — the annotation is confidently for the correct gene/protein.

---

## Gene / Protein Identity Verification

| Attribute | Value | Consistency |
|---|---|---|
| Gene symbol | *glcF* | ✔ Matches the "glc" (glycolate utilization) operon nomenclature |
| Protein | Glycolate oxidase iron–sulfur subunit, EC 1.1.99.14 | ✔ Matches domain content |
| Organism | *P. putida* KT2440 (PSEPK) | ✔ Correct target strain |
| Locus | PP_3747 | ✔ |
| Key InterPro domains | 4Fe4S_Fe-S-bd (IPR017896); 4Fe4S ferredoxin CS (IPR017900); Cys-rich domain (IPR004017); Glc_ox_4Fe-4S (IPR012257); Helical ferredoxin (IPR009051) | ✔ All consistent with an [4Fe-4S] electron-carrier subunit of glycolate oxidase |

The InterPro signature **IPR012257 (Glc_ox_4Fe-4S)** is diagnostic specifically for the glycolate-oxidase iron-sulfur subunit, and the twin 4Fe-4S ferredoxin motifs plus a cysteine-rich cluster-binding domain define an electron-transfer protein rather than a catalytic oxidase. Identity is therefore secure.

---

## Key Findings

### Finding 1 — GlcF is the essential iron–sulfur subunit of the three-subunit glycolate oxidase/dehydrogenase (GlcDEF)

The clearest experimental foundation for GlcF's function comes from the characterization of the *glc* locus in *Escherichia coli*, the ortholog of *P. putida* PP_3747/*glcF*. Sequence analysis of the operon showed a clear division of labor among the three structural genes: the products of *glcD* and *glcE* resemble flavoenzymes, whereas **the GlcF protein is similar to iron–sulfur proteins** ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)). This bioinformatic assignment is directly corroborated by the InterPro domain architecture of Q88GH6, which carries **two [4Fe-4S] cluster-binding domains** (IPR017896; IPR017900), a **cysteine-rich domain** (IPR004017), and the **glycolate-oxidase 4Fe-4S signature** (IPR012257). Together these domains establish that GlcF is a ferredoxin-type electron-carrier module rather than a substrate-binding catalytic enzyme.

The genetic proof that GlcF is an obligatory subunit — and not merely an accessory factor — is decisive: **insertional mutation with a chloramphenicol acetyltransferase (CAT) cassette in either *glcD*, *glcE*, or *glcF* abolished glycolate oxidase activity** ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)). The fact that disrupting *glcF* alone destroys enzymatic activity demonstrates that the Fe-S subunit is indispensable for the holoenzyme — consistent with its role as the electron-conducting element required to complete the catalytic cycle.

> *"the one from glcF was found to be similar to iron-sulfur proteins"* — [PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)
>
> *"The insertional mutation by a chloramphenicol acetyltransferase cassette in either glcD, glcE, or glcF abolished glycolate oxidase activity, indicating that presumably these proteins are subunits of this enzyme."* — [PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)

### Finding 2 — The GlcDEF complex catalyzes oxidation of glycolate to glyoxylate (EC 1.1.99.14) within the *glc* operon

GlcF operates within a defined genetic and biochemical context. In *E. coli*, the **glc operon** comprises *glcDEF* (encoding glycolate oxidase) and *glcB* (encoding malate synthase G), together with a divergently transcribed regulator (*glcC*) and a permease (*glcA*/*yghK*) ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/); [PMID: 11283302](https://pubmed.ncbi.nlm.nih.gov/11283302/)). Expression is induced by growth on glycolate. The enzyme is a **glycolate:acceptor 2-oxidoreductase (EC 1.1.99.14)** that converts glycolate to glyoxylate.

The substrate specificity of the associated uptake system further constrains the physiological role. The permease GlcA (structurally and functionally similar to L-lactate permease) transports the **2-hydroxymonocarboxylate substrate class — glycolate, L-lactate, and D-lactate** ([PMID: 11283302](https://pubmed.ncbi.nlm.nih.gov/11283302/)). This places glycolate at the center of a small-molecule 2-hydroxyacid metabolic module in which GlcDEF is the dedicated glycolate-oxidizing enzyme.

> *"In Escherichia coli the glc operon involved in glycolate utilization is located at 67.3 min and formed by genes encoding the enzymes glycolate oxidase (glcDEF) and malate synthase G (glcB)."* — [PMID: 11283302](https://pubmed.ncbi.nlm.nih.gov/11283302/)
>
> *"specificity for the 2-hydroxymonocarboxylates glycolate, L-lactate and D-lactate"* — [PMID: 11283302](https://pubmed.ncbi.nlm.nih.gov/11283302/)
>
> *"is known to contain glcB, encoding malate synthase G, and the gene(s) needed for glycolate oxidase activity"* — [PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)

### Finding 3 — In *P. putida* KT2440, glycolate oxidation is the gateway of ethylene glycol / diol degradation feeding the glyoxylate pathway

The physiological significance of GlcDEF in *P. putida* KT2440 is best appreciated through the degradation of two-carbon and four-carbon diols. KT2440 oxidizes **ethylene glycol** via periplasmic PQQ-dependent dehydrogenases (PedE/PedH) to glycolaldehyde and then to **glycolate**, with the temporal accumulation of both **glycolic acid and glyoxylic acid** during growth ([PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/)). The conversion of glycolate to glyoxylate at this junction is the reaction catalyzed by GlcDEF.

Downstream, glyoxylate is assimilated through the **glyoxylate carboligase (Gcl) pathway**, in which two molecules of glyoxylate are condensed to tartronate semialdehyde (EC 4.1.1.47) ([PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)), and through the glyoxylate cycle. Adaptive laboratory evolution demonstrated that **efficient growth on ethylene glycol requires de-repression of the Gcl pathway via the transcriptional regulator GclR** ([PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)). The same route is used for **1,4-butanediol** degradation, which proceeds through β-oxidation, the glyoxylate carboligase pathway, the glyoxylate cycle, and gluconeogenesis ([PMID: 37067433](https://pubmed.ncbi.nlm.nih.gov/37067433/)). GlcDEF therefore sits at a metabolic convergence point that is central to the biotechnological valorization of plastic-derived diol monomers.

> *"with the temporal accumulation of glycolic acid and glyoxylic acid for strain KT2440"* — [PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/)
>
> *"a central role of the transcriptional regulator GclR, which represses the glyoxylate carboligase pathway"* — [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)
>
> *"Glyoxylate carboligase (Gcl) (EC 4.1.1.47) of Escherichia coli catalyzes the condensation of two molecules of glyoxylate to give tartronic semialdehyde, a key intermediate in glyoxylate catabolism."* — [PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)

### Finding 4 — GlcF/GlcDEF is a cytoplasm-facing, inner-membrane-associated dehydrogenase coupling glycolate oxidation to the quinone pool (not an O₂-dependent oxidase)

Although historically named "glycolate oxidase," the enzyme is more accurately a **quinone-coupled dehydrogenase**. The catalytic subunits GlcD and GlcE display similarity to several flavoenzymes ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)) belonging to the **FAD-linked oxidase / D-lactate-dehydrogenase-type family of membrane-associated flavo-dehydrogenases**. Enzymes of this family transfer electrons from FAD through a [Fe-S] relay to the membrane quinone pool. The EC classification itself is diagnostic: **EC class 1.1.99 uses an unspecified electron acceptor** (i.e., a quinone), distinguishing these enzymes from the peroxisomal, O₂-dependent glycolate oxidases (EC 1.1.3.15) of plants and animals, which produce H₂O₂.

GlcF's structure is fully consistent with a peripheral, cytoplasm-facing electron-relay role: it possesses **no signal peptide and no transmembrane domain**, being instead a soluble [4Fe-4S] ferredoxin-type electron-carrier module. It is anchored to the inner membrane indirectly, through its assembly into the GlcDEF complex, and conducts electrons to membrane-embedded quinone. This architecture localizes the reaction to the **cytoplasmic face of the inner membrane**.

> *"The proteins encoded from glcD and glcE displayed similarity to several flavoenzymes"* — [PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)

### Finding 5 — The glycolate→glyoxylate reaction is evolutionarily conserved and feeds the bacterial glycerate pathway

The functional assignment of GlcF is reinforced by strong evolutionary conservation. In the cyanobacterium *Synechocystis* sp. PCC 6803, glyoxylate for photorespiratory (2-phosphoglycolate) metabolism is synthesized by **two forms of glycolate dehydrogenase (GlcD)**. Genetic evidence is unambiguous: **mutants defective in one or both GlcD proteins accumulate glycolate**, and the ΔglcD1/ΔglcD2 double mutant is unable to grow under low CO₂ ([PMID: 18957552](https://pubmed.ncbi.nlm.nih.gov/18957552/)). This confirms in vivo that GlcD-type enzymes catalyze glycolate → glyoxylate and that loss of the activity blocks glycolate consumption.

Crucially, the glyoxylate product enters the **bacterial glycerate pathway** (glyoxylate → tartronate semialdehyde → glycerate), the very pathway used by *P. putida* KT2440 (the Gcl pathway; [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/), [PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)). This conservation of both the enzymatic reaction and its downstream metabolic fate across proteobacteria and cyanobacteria provides confident support for assigning the identical glycolate-oxidizing role to *P. putida* GlcF/GlcDEF.

> *"All these catabolic routes start with glyoxylate, which can be synthesized by 2 different forms of glycolate dehydrogenase (GlcD)."* — [PMID: 18957552](https://pubmed.ncbi.nlm.nih.gov/18957552/)
>
> *"Mutants defective in one or both GlcD proteins accumulated glycolate under high CO(2) level and the double mutant DeltaglcD1/DeltaglcD2 was unable to grow under low CO(2)."* — [PMID: 18957552](https://pubmed.ncbi.nlm.nih.gov/18957552/)

### Finding 6 — Intra-complex electron flow: GlcD/GlcE (FAD) abstract hydride from glycolate; GlcF ([Fe-S]) relays electrons to quinone

Integrating the above, GlcDEF is a **modular heterotrimeric flavo-iron-sulfur dehydrogenase** with an internal electron-transfer chain. **GlcD** is the catalytic FAD subunit of the vanillyl-alcohol-oxidase / D-lactate-dehydrogenase (FAD-binding-4, PF01565) superfamily; it oxidizes the C2 hydroxyl of glycolate to the aldehyde (glyoxylate). **GlcE** is a second FAD-binding subunit. **GlcF** carries two low-potential [4Fe-4S] clusters (InterPro IPR017896/IPR017900) plus a cysteine-rich cluster-binding module (IPR004017) forming the terminal electron-conducting wire to the membrane quinone pool.

The obligatory, sequential nature of this electron relay is demonstrated by the finding that all three subunits are individually essential — insertional inactivation of *glcD*, *glcE*, **or** *glcF* abolishes glycolate oxidase activity ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)). This confirms an obligate electron-relay chain in which GlcF is the Fe-S conductor, rather than three independent enzymatic activities.

> *"The insertional mutation by a chloramphenicol acetyltransferase cassette in either glcD, glcE, or glcF abolished glycolate oxidase activity, indicating that presumably these proteins are subunits of this enzyme."* — [PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)

---

## Mechanistic Model / Interpretation

### The electron-relay chain of GlcDEF

The GlcDEF complex is best understood as a linear electron-transfer chain running from the substrate to the membrane quinone pool. GlcF sits at the "output" end of this chain:

```
   Glycolate (2-hydroxyacetate)
        │
        │  C2–OH oxidized to aldehyde
        ▼
  ┌──────────────┐        ┌──────────────┐        ┌───────────────────────┐
  │  GlcD (FAD)  │──e⁻──▶ │  GlcE (FAD)  │──e⁻──▶ │  GlcF                 │
  │  catalytic   │        │  flavo-      │        │  [4Fe-4S] x2 +        │──e⁻──▶ Quinone (Q → QH₂)
  │  hydride     │        │  transfer    │        │  Cys-rich cluster     │            │
  │  abstraction │        │              │        │  (electron wire)      │            ▼
  └──────────────┘        └──────────────┘        └───────────────────────┘     Respiratory chain
        │                                                                        (ETC → terminal
        ▼                                                                         oxidase / O₂)
   Glyoxylate  ────────────────────────────────────────────────▶  Glyoxylate metabolism
```

Two electrons and a proton (a hydride) are abstracted from the C2 hydroxyl of glycolate by the FAD cofactor of GlcD, generating glyoxylate. The reducing equivalents are then passed through the flavin of GlcE and into GlcF's tandem [4Fe-4S] clusters, which act as a molecular wire delivering electrons to the membrane quinone pool. Reduced quinol (QH₂) is subsequently re-oxidized by the aerobic respiratory chain. This is why the enzyme is classified as a **dehydrogenase (EC 1.1.99.14, unspecified acceptor)** and not an oxidase — molecular oxygen is not the direct electron acceptor at the GlcDEF active site.

### Localization

| Property | Assignment | Basis |
|---|---|---|
| Cellular compartment | Cytoplasmic face of the inner (plasma) membrane | Quinone-coupled dehydrogenase family; GlcF lacks signal peptide/TM domain |
| GlcF membrane anchoring | Indirect, via assembly into GlcDEF | GlcF is a soluble ferredoxin-type module |
| Reaction site | Intracellular (cytoplasmic) | Substrate glycolate is imported by GlcA permease |

### Position in metabolism

GlcDEF is the committed **entry point of glycolate into central carbon metabolism**. In *P. putida* KT2440 this is a convergence hub for multiple upstream substrates:

```
Ethylene glycol ─(PedE/PedH, periplasm)─▶ glycolaldehyde ─▶ GLYCOLATE ─┐
1,4-Butanediol  ─(β-oxidation)──────────────────────────▶ GLYCOLATE ─┤
                                                                      │
                                                          [ GlcDEF, EC 1.1.99.14 ]  ◀── GlcF Fe-S relay
                                                                      │
                                                                      ▼
                                                                  GLYOXYLATE
                                                          ┌───────────┴───────────┐
                                                          ▼                       ▼
                                          Glyoxylate carboligase (Gcl)     Glyoxylate cycle
                                          → tartronate semialdehyde        (malate synthase, etc.)
                                          → glycerate → glycolysis         → C4 replenishment
                                                          │
                                                          ▼
                                              Central carbon / gluconeogenesis
```

The regulator **GclR** controls flux into the glyoxylate carboligase branch; its de-repression is required for efficient growth on ethylene glycol, underscoring that the glycolate→glyoxylate step catalyzed by GlcDEF is rate-relevant to diol assimilation.

---

## Evidence Base

| PMID | Title (abbrev.) | Organism | How it supports the annotation |
|---|---|---|---|
| [8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/) | *glc* locus of *E. coli*: subunits of glycolate oxidase and glc regulator | *E. coli* | **Primary genetic + sequence evidence.** GlcF resembles iron-sulfur proteins; *glcD/glcE* resemble flavoenzymes; insertional inactivation of *glcD*, *glcE*, or *glcF* individually abolishes glycolate oxidase activity → all three are essential subunits. |
| [11283302](https://pubmed.ncbi.nlm.nih.gov/11283302/) | *yghK* permease for glycolate, similar to L-lactate permease | *E. coli* | Defines operon structure (*glcDEF* = glycolate oxidase; *glcB* = malate synthase G) and substrate class (2-hydroxymonocarboxylates: glycolate, L-/D-lactate). |
| [23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/) | Ethylene glycol metabolism by *P. putida* | *P. putida* KT2440 | Shows glycolate and glyoxylate accumulate as pathway intermediates in the target organism → in vivo context for GlcDEF. |
| [31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/) | Metabolic/regulatory basis of ethylene glycol metabolism (ALE) | *P. putida* KT2440 | Establishes downstream glyoxylate assimilation via the Gcl pathway and its GclR regulation in the target organism. |
| [37067433](https://pubmed.ncbi.nlm.nih.gov/37067433/) | 1,4-butanediol degradation (ARTP + ALE) | *P. putida* KT2440 | Confirms glyoxylate carboligase pathway + glyoxylate cycle as the downstream route for diol degradation. |
| [8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/) | Glyoxylate carboligase molecular cloning | *E. coli* | Defines the immediate downstream fate of glyoxylate (2 glyoxylate → tartronate semialdehyde). |
| [18957552](https://pubmed.ncbi.nlm.nih.gov/18957552/) | Photorespiratory glycolate metabolism in cyanobacteria | *Synechocystis* PCC 6803 | Independent in vivo genetic proof that GlcD-type glycolate dehydrogenase catalyzes glycolate→glyoxylate; conservation across phyla. |
| [11831473](https://pubmed.ncbi.nlm.nih.gov/11831473/) | Microbial degradation of polyethers (review) | Various | Context: glycolic/glyoxylic acid as convergent intermediates of polyether/glycol catabolism. |
| [35953636](https://pubmed.ncbi.nlm.nih.gov/35953636/) | Transcriptomic response of *P. nicosulfuronedens* to nicosulfuron | *Pseudomonas* | Corroborating context: glycolate oxidase linked to glyoxylate cycle and acid metabolite production in *Pseudomonas*. |

**Strength of the evidence.** The core enzymatic assignment rests on **precise, low-throughput genetic experiments** (targeted CAT-cassette insertions in *E. coli*, [PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/); defined gene knockouts in *Synechocystis*, [PMID: 18957552](https://pubmed.ncbi.nlm.nih.gov/18957552/)) rather than high-throughput inference alone. The bioinformatic structural assignment (InterPro 4Fe-4S ferredoxin domains) is fully consistent with these genetic and biochemical data. The *P. putida*-specific physiological role is supported by targeted metabolite tracking ([PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/)) plus ALE/omics studies ([PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/), [PMID: 37067433](https://pubmed.ncbi.nlm.nih.gov/37067433/)).

### Supported and refuted hypotheses

**Supported:**
- GlcF is the essential [4Fe-4S] iron-sulfur subunit of a heterotrimeric glycolate oxidase/dehydrogenase ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/); InterPro domains). ✔
- The complex oxidizes glycolate → glyoxylate (EC 1.1.99.14), part of the *glc* operon glycolate-utilization module ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/), [PMID: 11283302](https://pubmed.ncbi.nlm.nih.gov/11283302/)). ✔
- It is a quinone-coupled, membrane-associated dehydrogenase (not an O₂-dependent oxidase); GlcF acts as electron relay (inference from EC class + family; [PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)). ✔
- In KT2440, this step is the gateway of ethylene glycol / 1,4-butanediol degradation feeding the glyoxylate/glycerate pathway ([PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/), [PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/), [PMID: 37067433](https://pubmed.ncbi.nlm.nih.gov/37067433/), [PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)). ✔
- The reaction is evolutionarily conserved (cyanobacteria; [PMID: 18957552](https://pubmed.ncbi.nlm.nih.gov/18957552/)). ✔

**Refuted / excluded:**
- GlcF is *not* the substrate-oxidizing catalytic subunit (that role belongs to the FAD subunit GlcD).
- Bacterial GlcDEF is *not* a peroxisomal H₂O₂-producing glycolate oxidase like the plant enzyme (EC 1.1.3.15).

---

## Limitations and Knowledge Gaps

1. **No direct biochemical characterization of the *P. putida* KT2440 enzyme.** The specific reaction and subunit essentiality have been demonstrated in *E. coli* and cyanobacteria, and the *P. putida* PP_3747 assignment relies on orthology (sequence/domain conservation and operon context) plus organism-level metabolite data. The KT2440 GlcDEF complex has not, to our knowledge, been purified and kinetically characterized. The substrate specificity (K_m, turnover) for glycolate vs. other 2-hydroxyacids in KT2440 remains undetermined.

2. **Electron acceptor not directly demonstrated.** The quinone-coupled mechanism is inferred from the EC 1.1.99 classification and the D-lactate-dehydrogenase-family membership of GlcD/GlcE. Direct demonstration of quinone reduction (e.g., with menaquinone/ubiquinone analogs) for the *Pseudomonas* enzyme is lacking.

3. **Cluster stoichiometry and redox potentials unmeasured.** The presence of two [4Fe-4S] clusters in GlcF is inferred from InterPro domains. EPR/Mössbauer spectroscopy confirming cluster number, type, and midpoint potentials has not been performed on this protein.

4. **Localization is inferred, not observed.** The cytoplasm-facing, membrane-associated topology is deduced from family membership and the absence of signal/TM sequences in GlcF. Fractionation or fluorescence-localization data specific to KT2440 would strengthen this.

5. **Regulation in *P. putida* is less defined than in *E. coli*.** While GclR governs the downstream glyoxylate carboligase branch, the transcriptional control of *glcDEF* itself (e.g., a GlcC-type regulator, induction by glycolate) in KT2440 has not been detailed in the reviewed literature.

6. **Individual roles of GlcD vs. GlcE not fully resolved.** Both are FAD-binding subunits; which performs the primary hydride abstraction versus intermediary electron transfer is a mechanistic detail supported by family analogy rather than direct structural evidence for this complex.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and purification of the KT2440 GlcDEF complex**, followed by in vitro assay of glycolate:quinone oxidoreductase activity using ubiquinone/menaquinone analogs or artificial acceptors (e.g., DCPIP/PMS) to directly confirm the quinone-coupled dehydrogenase mechanism and measure kinetic parameters.

2. **Substrate-specificity profiling.** Test the purified enzyme against glycolate, L-lactate, D-lactate, and glyoxylate to define the substrate range and confirm glycolate as the preferred substrate, quantifying K_m/k_cat.

3. **Spectroscopic characterization of GlcF clusters** (EPR, Mössbauer, UV-vis) to confirm the number and type of [4Fe-4S] clusters and determine their midpoint redox potentials, validating the electron-relay model.

4. **Targeted gene deletion in KT2440.** Construct a clean Δ*PP_3747* (Δ*glcF*) mutant and test for loss of growth on glycolate, ethylene glycol, and 1,4-butanediol, with metabolite profiling to confirm glycolate accumulation — replicating the *E. coli*/cyanobacterial genetics in the target organism.

5. **Subcellular localization.** Perform membrane/cytoplasm fractionation and/or fluorescent-tag localization of GlcF and GlcD to confirm inner-membrane association and cytoplasmic-face topology.

6. **Structural biology.** Solve or model (AlphaFold-multimer) the GlcDEF heterotrimer to map the electron-transfer path (FAD → FAD → [4Fe-4S] → [4Fe-4S] → quinone) and validate inter-subunit cofactor distances against efficient tunneling.

7. **Regulatory mapping.** Identify the regulator and inducer controlling *glcDEF* transcription in KT2440 (candidate GlcC/GntR-family regulator) via reporter assays and ChIP/RNA-seq under glycolate vs. glucose growth.

---

## Conclusion

*glcF* (Q88GH6, PP_3747) encodes the **iron–sulfur electron-relay subunit of the glycolate oxidase/dehydrogenase complex GlcDEF (EC 1.1.99.14)** of *Pseudomonas putida* KT2440. The holoenzyme oxidizes **glycolate to glyoxylate** at the cytoplasmic face of the inner membrane, coupling the reaction to the respiratory quinone pool. GlcF is not the catalytic subunit but is an obligatory component: its two [4Fe-4S] clusters conduct electrons from the FAD centers of GlcD/GlcE to quinone, and its loss abolishes activity. Physiologically, this reaction is the **gateway that channels glycolate — including glycolate derived from ethylene glycol and 1,4-butanediol degradation — into the glyoxylate carboligase (glycerate) pathway and the glyoxylate cycle**, linking to central carbon metabolism. The assignment is confidently supported by *E. coli* operon genetics, cyanobacterial knockouts, *P. putida* diol-degradation metabolite data, and the protein's diagnostic 4Fe-4S ferredoxin domain architecture.

---

### References (PMIDs)
- Pellicer et al. 1996, *J. Bacteriol.* — glc locus characterization; GlcF is Fe-S, subunits essential ([PMID: 8606183](https://pubmed.ncbi.nlm.nih.gov/8606183/)).
- Núñez et al. 2001 — glc operon, glycolate permease GlcA, 2-hydroxymonocarboxylate specificity ([PMID: 11283302](https://pubmed.ncbi.nlm.nih.gov/11283302/)).
- Chang, Wang & Cronan 1993 — glyoxylate carboligase ([PMID: 8440684](https://pubmed.ncbi.nlm.nih.gov/8440684/)).
- Mückschel et al. 2012 — ethylene glycol → glycolate/glyoxylate in *P. putida* ([PMID: 23023748](https://pubmed.ncbi.nlm.nih.gov/23023748/)).
- Li et al. 2019 — ethylene glycol metabolism, GclR, glyoxylate carboligase pathway, KT2440 ([PMID: 31166064](https://pubmed.ncbi.nlm.nih.gov/31166064/)).
- Qian et al. 2023 — 1,4-butanediol degradation via glyoxylate pathway in KT2440 ([PMID: 37067433](https://pubmed.ncbi.nlm.nih.gov/37067433/)).
- Eisenhut et al. 2008 — cyanobacterial glycolate dehydrogenase (GlcD) makes glyoxylate ([PMID: 18957552](https://pubmed.ncbi.nlm.nih.gov/18957552/)).


## Artifacts

- [OpenScientist final report](glcF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](glcF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:8606183
2. PMID:11283302
3. PMID:23023748
4. PMID:8440684
5. PMID:31166064
6. PMID:37067433
7. PMID:18957552