---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T06:41:00.881235'
end_time: '2026-07-23T06:52:15.076037'
duration_seconds: 674.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: prpD
  gene_symbol: prpD
  uniprot_accession: Q88KF2
  protein_description: 'RecName: Full=2-methylcitrate dehydratase {ECO:0000256|ARBA:ARBA00017240};
    EC=4.2.1.79 {ECO:0000256|ARBA:ARBA00013124};'
  gene_info: Name=prpD {ECO:0000313|EMBL:AAN67951.1}; OrderedLocusNames=PP_2338 {ECO:0000313|EMBL:AAN67951.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the PrpD family.
  protein_domains: 2Me_IsoCit_deHydtase_PrpD. (IPR012705); MmgE/PrpD_sf. (IPR036148);
    MmgE/PrpD_sf_1. (IPR042183); MmgE/PrpD_sf_2. (IPR042188); MmgE_PrpD. (IPR005656)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: prpD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: prpD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KF2
- **Protein Description:** RecName: Full=2-methylcitrate dehydratase {ECO:0000256|ARBA:ARBA00017240}; EC=4.2.1.79 {ECO:0000256|ARBA:ARBA00013124};
- **Gene Information:** Name=prpD {ECO:0000313|EMBL:AAN67951.1}; OrderedLocusNames=PP_2338 {ECO:0000313|EMBL:AAN67951.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the PrpD family.
- **Key Domains:** 2Me_IsoCit_deHydtase_PrpD. (IPR012705); MmgE/PrpD_sf. (IPR036148); MmgE/PrpD_sf_1. (IPR042183); MmgE/PrpD_sf_2. (IPR042188); MmgE_PrpD. (IPR005656)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "prpD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'prpD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **prpD** (gene ID: prpD, UniProt: Q88KF2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *prpD* (Q88KF2 / PP_2338) — 2-Methylcitrate Dehydratase of *Pseudomonas putida* KT2440

## Summary

The gene **prpD** (locus tag **PP_2338**; UniProt **Q88KF2**) of *Pseudomonas putida* strain KT2440 encodes **2-methylcitrate dehydratase (EC 4.2.1.79)**, an enzyme of central carbon-catabolic metabolism. Its primary and well-defined biochemical function is to catalyze the **dehydration of (2S,3S)-2-methylcitrate to 2-methyl-*cis*-aconitate with release of water** — the third enzymatic step of the **2-methylcitric acid cycle (2-MCC)**. This cycle is the principal route by which many bacteria oxidize **propionate**, via its activated form **propionyl-CoA**, to the central metabolites **pyruvate and succinate**, thereby allowing propionate to serve as a sole carbon and energy source while simultaneously **detoxifying propionyl-CoA and 2-methylcitrate**, both of which are growth-inhibitory when they accumulate.

PrpD belongs to the **MmgE/PrpD protein family** (InterPro IPR005656, IPR012705; superfamily IPR036148/IPR042183/IPR042188), an all-α-helical fold that is **structurally and mechanistically distinct from the iron–sulfur aconitase superfamily**. Direct biochemical characterization of high-identity orthologs (chiefly *Salmonella enterica* PrpD) established that the purified enzyme **contains no iron–sulfur center, requires no metal cations or reducing agents, and performs only the dehydration half-reaction** — the subsequent hydration of 2-methyl-*cis*-aconitate to 2-methylisocitrate is carried out by a separate aconitase. The *P. putida* KT2440 protein itself has not been directly assayed, but its function is confidently transferred from these orthologs: PP_2338 is **~60% identical** to characterized *E. coli* PrpD and sits within a **complete, contiguous 2-MCC gene cluster** (PP_2334–PP_2339) in the KT2440 genome.

The gene product is a **soluble, cytoplasmic enzyme**. Bioinformatic analysis of the 494-residue Q88KF2 sequence found no signal peptide and no transmembrane segment (maximum Kyte–Doolittle windowed hydropathy 1.42, below the 1.6 membrane-helix threshold; overall GRAVY −0.145), consistent with a globular protein acting in the bacterial cytosol on soluble organic-acid substrates. One important database caveat: the UniProt record for Q88KF2 carries an **electronically inferred "2Fe-2S cluster binding" annotation (GO:0051537, IEA)** that **directly contradicts** the experimental demonstration that PrpD is cofactor-free; this annotation should be regarded as an artifact of automated InterPro-to-GO mapping.

---

## Gene/Protein Identity Verification

Before presenting the findings, the identity of the research target was confirmed against the supplied UniProt context:

- **UniProt:** Q88KF2 — RecName 2-methylcitrate dehydratase; EC 4.2.1.79
- **Gene / locus:** *prpD* / PP_2338
- **Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
- **Family / domains:** PrpD family; MmgE/PrpD (IPR005656), 2Me_IsoCit_deHydtase_PrpD (IPR012705), MmgE/PrpD superfamily (IPR036148/IPR042183/IPR042188)

The gene symbol **prpD matches the protein description** (2-methylcitrate dehydratase), the organism is correctly *P. putida* KT2440, and the protein family/domains **align with the literature** on the PrpD 2-methylcitrate dehydratase. No conflicting-identity problem was encountered: all retrieved literature concerns *prpD* as the 2-MCC dehydratase, differing only in organism. The assignment for the KT2440 protein rests on strong orthology rather than a direct assay (see Limitations).

---

## Key Findings

### F001 — PrpD is 2-methylcitrate dehydratase (EC 4.2.1.79) in the 2-methylcitrate cycle of propionate catabolism

The defining function of *prpD* was established by direct in vitro enzymology on the ortholog from *Salmonella enterica*, which is closely related to *P. putida* Q88KF2/PP_2338. Purified PrpD catalyzes the **dehydration of (2S,3S)-2-methylcitrate to 2-methyl-*cis*-aconitate**. As stated in the foundational study, *"the prpD gene of the prpBCDE operon of this bacterium encodes a protein with 2-methylcitrate dehydratase enzyme activity"* ([PMID: 11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/)).

This activity is one of four coordinated enzymatic steps encoded by the canonical *prp* operon. The operon *"usually comprises prpB, prpC, prpD and prpE genes, encoding 2-methylisocitrate (2-MIC) lyase, 2-methylcitrate (2-MC) synthase, 2-MC dehydratase and propionyl-CoA synthetase, respectively, which constitute the pathway 2-methylcitrate cycle (2-MCC) well-known for microbial propionate metabolism"* ([PMID: 42271202](https://pubmed.ncbi.nlm.nih.gov/42271202/)). Together, these enzymes convert propionate to pyruvate and succinate. The complete cycle has been reconstituted in vitro from homogeneous PrpE (propionyl-CoA synthetase), PrpC (2-methylcitrate synthase), PrpD (2-methylcitrate dehydratase), aconitase (AcnA), and PrpB (2-methylisocitrate lyase), providing a fully validated biochemical framework for PrpD's role.

Isotope-labeling studies in *Salmonella typhimurium* independently confirmed the pathway topology: *"The reactions are catalyzed by propionyl coenzyme A (propionyl-CoA) synthetase (PrpE), 2-methylcitrate synthase (PrpC), 2-methylcitrate dehydratase (probably PrpD), 2-methylisocitrate hydratase (probably PrpD), and 2-methylisocitrate lyase (PrpB)"*, and demonstrated that *"the alpha-carbon of propionate is oxidized to yield pyruvate"* ([PMID: 10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/)).

### F002 — PrpD is an iron–sulfur-independent, cofactor-free dehydratase distinct from aconitase-type hydratases

A crucial mechanistic finding is that PrpD is **not** an iron–sulfur enzyme, distinguishing it sharply from the aconitase superfamily that catalyzes analogous dehydration/hydration chemistry in the TCA cycle. Homogeneous PrpD *"did not contain an iron-sulfur center, displayed no requirements for metal cations or reducing agents for activity, and did not catalyze the hydration of 2-methyl-cis-aconitate to 2-methylisocitrate"* ([PMID: 11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/)). This establishes two points: (i) PrpD is a **cofactor-independent** dehydratase, and (ii) it catalyzes **only the dehydration half-reaction**, with the subsequent rehydration to 2-methylisocitrate carried out by a distinct aconitase.

The mechanistic distinctiveness of the PrpD class is underscored by the existence of an alternative enzymatic solution to the same metabolic step. In some organisms, *"two genes, acnD and prpF replace prpD, which encodes 2-methylcitrate dehydratase"* ([PMID: 29145506](https://pubmed.ncbi.nlm.nih.gov/29145506/)). In this AcnD/PrpF system, a dedicated 2-methylcitrate dehydratase (AcnD) produces 2-methyl-*trans*-aconitate, and PrpF isomerizes it to the *cis* isomer needed downstream — a division of labor that highlights PrpD as a discrete, self-contained dehydratase class within the MmgE/PrpD family (InterPro IPR005656, IPR012705), an all-α-helical fold unrelated to the [4Fe-4S] aconitase superfamily.

### F003 — Physiological role: PrpD enables propionate detoxification/utilization and acts in the cytoplasm

Functionally, the 2-MCC — and therefore PrpD — serves a dual purpose: **catabolic** (harvesting carbon and energy from propionate) and **protective** (removing toxic intermediates). *"The methylcitrate cycle metabolizes propionyl-CoA, a toxic metabolite, into pyruvate"* ([PMID: 30933666](https://pubmed.ncbi.nlm.nih.gov/30933666/)). When the cycle is impaired, not only does propionyl-CoA accumulate, but so does **2-methylcitrate**, which is itself toxic: in *Salmonella*, *"a target of the 2-MC isomer produced by GltA (2-MC(GltA)) is fructose-1,6-bisphosphatase (FBPase), a key enzyme in gluconeogenesis"* ([PMID: 19948794](https://pubmed.ncbi.nlm.nih.gov/19948794/)). Because PrpD consumes 2-methylcitrate, its activity is important both for completing propionate oxidation and for preventing the buildup of a gluconeogenesis-blocking inhibitor.

The expression of *prpD* is tightly linked to propionate availability. In *Corynebacterium glutamicum*, *"the specific 2-methylcitrate synthase activity increased about 50-fold when propionate was provided as the sole carbon source"* ([PMID: 11976302](https://pubmed.ncbi.nlm.nih.gov/11976302/)), reflecting coordinate propionate-inducible expression of the *prp* genes including *prpD*. This inducible, catabolic behavior is consistent across diverse taxa (*Corynebacterium*, *Acetobacter*, *Mycobacterium*, and the fungus *Magnaporthe oryzae*), and in *Mycobacterium tuberculosis* the dedicated transcription factor PrpR directly activates the *prpDC* genes in response to propionate ([PMID: 22916289](https://pubmed.ncbi.nlm.nih.gov/22916289/)).

Regarding **localization**, PrpD is a soluble metabolic enzyme with no signal peptide and no transmembrane region; its substrates (2-methylcitrate, 2-methyl-*cis*-aconitate) are soluble cytosolic organic acids. It therefore carries out its function in the **bacterial cytoplasm**.

### F004 — PP_2338 sits in a complete 2-MCC gene cluster and is ~60% identical to characterized *E. coli* PrpD

Genome annotation and sequence analysis firmly anchor the functional assignment to the KT2440 protein. PP_2338 (*prpD*; KEGG orthology K01720; EC 4.2.1.79; genomic position 2,668,149–2,669,633; 494 aa / 54.9 kDa) lies within a **contiguous 2-MCC gene cluster**:

| Locus | Gene | Product |
|-------|------|---------|
| PP_2334 | *prpB*/*mmgF* | 2-methylisocitrate lyase |
| PP_2335 | *prpC* | 2-methylcitrate synthase |
| PP_2336 | *acnA-II* | aconitate hydratase |
| PP_2337 | *prpF* | aconitate isomerase |
| **PP_2338** | ***prpD*** | **2-methylcitrate dehydratase** |
| PP_2339 | *acnB* | bifunctional aconitate hydratase 2 / 2-methylisocitrate dehydratase |

A Needleman–Wunsch global alignment gives **59.7% amino-acid identity (302/506)** between Q88KF2 and biochemically characterized *E. coli* PrpD (P77243). UniProt further records the exact catalyzed reaction (Rhea:17725; ChEBI 57872 → 58853 + H₂O), the pathway assignment "propanoate degradation" (UniPathway UPA00946), orthology group COG2079, and the PrpD-specific hidden-Markov models TIGR02330 / PRK09425. The experimental function of the ortholog — *"the prpD gene ... encodes a protein with 2-methylcitrate dehydratase enzyme activity"* ([PMID: 11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/)) — is thus transferred to the KT2440 protein with high confidence given the strong sequence conservation and complete pathway context.

### F005 — Database caveat: the automated "2Fe-2S cluster binding" GO term on Q88KF2 conflicts with experimental evidence

The UniProt entry for Q88KF2 carries an electronically inferred annotation, **GO:0051537 "2 iron, 2 sulfur cluster binding" (evidence code IEA, propagated from InterPro)**. This is **inconsistent with the direct biochemical evidence**: homogeneous PrpD *"did not contain an iron-sulfur center, displayed no requirements for metal cations or reducing agents for activity"* ([PMID: 11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/)). The most parsimonious explanation is that the automated InterPro-to-GO mapping erroneously associated the MmgE/PrpD fold with iron–sulfur chemistry — probably by analogy to aconitases, which perform related dehydration chemistry but belong to a completely different, Fe–S-dependent superfamily. Users of the annotation should **prefer the experimental cofactor-free assignment** over the automated GO term.

### F006 — Bioinformatic sequence analysis supports cytoplasmic localization

A Kyte–Doolittle hydropathy analysis (window = 19) of the 494-residue Q88KF2 sequence found **zero windows exceeding the 1.6 transmembrane-helix threshold** (maximum windowed hydropathy = 1.42) and an overall **negative GRAVY of −0.145**, both hallmarks of a soluble globular protein rather than a membrane protein. The N-terminus (MSANVDLNDRPDYDRVLQTL…) is hydrophilic and charged, lacking the hydrophobic h-region characteristic of Sec/Tat signal peptides. Combined with the soluble, cytosolic nature of its substrates, these features independently corroborate that PrpD functions in the **cytoplasm**.

---

## Mechanistic Model / Interpretation

PrpD is the **third catalytic step** of the 2-methylcitric acid cycle, the pathway that funnels propionate into central metabolism. The cycle can be depicted as follows:

```
   Propionate
       │  PrpE (propionyl-CoA synthetase)  [+ATP, +CoA]
       ▼
   Propionyl-CoA  ──────────────► (TOXIC if accumulated)
       │  PrpC (2-methylcitrate synthase)  [+ oxaloacetate]
       ▼
   (2S,3S)-2-Methylcitrate  ────► (TOXIC; inhibits FBPase / gluconeogenesis)
       │
       │  ┌────────────────────────────────────────────┐
       │  │  *** PrpD — 2-methylcitrate dehydratase ***  │
       │  │  EC 4.2.1.79    (−H2O)                       │  <=== PP_2338 / Q88KF2
       ▼  └────────────────────────────────────────────┘
   2-Methyl-cis-aconitate
       │  Aconitase (AcnA / AcnB)  [+H2O]   ← NOT catalyzed by PrpD
       ▼
   (2R,3S)-2-Methylisocitrate
       │  PrpB (2-methylisocitrate lyase)
       ▼
   Pyruvate  +  Succinate  ───────► central metabolism (TCA cycle, gluconeogenesis)
```

Several features of this model deserve emphasis:

1. **PrpD performs only the dehydration.** Unlike the bifunctional aconitase of the TCA cycle, which both dehydrates citrate and rehydrates *cis*-aconitate, PrpD catalyzes solely the removal of water from 2-methylcitrate. The reverse hydration to 2-methylisocitrate is delegated to a separate aconitase (AcnA/AcnB), explaining why the KT2440 gene cluster contains two aconitase genes (PP_2336, PP_2339) alongside *prpD*.

2. **Cofactor-free chemistry.** The MmgE/PrpD family achieves β-elimination of water **without** an Fe–S cluster or metal cofactor — a distinctive feature that separates it from aconitase-type hydratases and refutes the automated 2Fe-2S annotation. This has implications for enzyme stability (no oxygen-sensitive cluster) and for evolutionary interpretation (convergent metabolic solution to the same reaction).

3. **Redundant enzymatic solutions exist.** The AcnD + PrpF system in organisms such as *Shewanella oneidensis* replaces PrpD, producing 2-methyl-*trans*-aconitate that PrpF isomerizes to the *cis* form. *P. putida* KT2440 is notable for encoding *both* a *prpD* (PP_2338) **and** a *prpF* (PP_2337) in the same cluster, which may reflect a hybrid or backup arrangement worth experimental dissection.

4. **Dual physiological logic.** The pathway is simultaneously a **carbon-acquisition** route (propionate → pyruvate + succinate) and a **detoxification** route (clearing propionyl-CoA and the FBPase-inhibiting 2-methylcitrate). PrpD sits at the exact node where the toxic 2-methylcitrate is consumed, making it pivotal to both functions.

Overall, the evidence — direct enzymology on high-identity orthologs, complete pathway gene context, strong sequence conservation, and consistent bioinformatic localization signals — converges on a confident functional assignment for the KT2440 protein.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/) | *In vitro conversion of propionate to pyruvate by Salmonella enterica enzymes* | **Primary experimental basis.** Assigns 2-methylcitrate dehydratase activity to PrpD; shows it is cofactor-free and Fe–S-free, catalyzing only dehydration. Supports F001, F002, F004, F005. |
| [10482501](https://pubmed.ncbi.nlm.nih.gov/10482501/) | *Salmonella typhimurium LT2 catabolizes propionate via the 2-MCC* | ¹³C-labeling defines pathway topology and PrpD's step; PrpC purified and confirmed. Supports F001. |
| [42271202](https://pubmed.ncbi.nlm.nih.gov/42271202/) | *Functions of the prp operon in acetic acid bacteria* | Confirms *prpD* encodes 2-MC dehydratase within the 2-MCC operon. Supports F001. |
| [29145506](https://pubmed.ncbi.nlm.nih.gov/29145506/) | *PrpF of Shewanella oneidensis MR-1* | Shows AcnD+PrpF can replace PrpD, underscoring PrpD as a distinct dehydratase class. Supports F002. |
| [30933666](https://pubmed.ncbi.nlm.nih.gov/30933666/) | *Methylcitrate cycle in rice blast fungus* | States the cycle detoxifies propionyl-CoA to pyruvate. Supports F003. |
| [19948794](https://pubmed.ncbi.nlm.nih.gov/19948794/) | *In Salmonella enterica, 2-methylcitrate blocks gluconeogenesis* | Shows 2-methylcitrate inhibits FBPase, making PrpD-mediated turnover physiologically important. Supports F003. |
| [11976302](https://pubmed.ncbi.nlm.nih.gov/11976302/) | *Two prpDBC clusters in Corynebacterium glutamicum* | ~50-fold induction of 2-MCC activity by propionate; inducible catabolic role. Supports F003. |
| [22916289](https://pubmed.ncbi.nlm.nih.gov/22916289/) | *PrpR transcription factor in M. tuberculosis* | Establishes propionate-responsive transcriptional activation of *prpDC*. Contextual support for F003. |
| [18295882](https://pubmed.ncbi.nlm.nih.gov/18295882/) | *Cloning vectors for recombinant protein purification* | Documents purification of *S. enterica* PrpD and *S. oneidensis* PrpF for the 2-MCC. Methodological support. |

**Consistency across the literature.** All primary and secondary sources agree on the enzymatic identity of PrpD as 2-methylcitrate dehydratase within the 2-MCC. No paper contradicts this assignment. The only conflicting piece of information is the **automated GO annotation** on the UniProt record itself (F005), which is refuted by the primary experimental literature.

**A note on organism scope.** The direct enzymological characterization was performed on *Salmonella enterica* and *E. coli* PrpD, not on the *P. putida* KT2440 protein. However, the ~60% identity, identical EC/Rhea reaction annotation, conserved TIGR02330/PRK09425 signatures, and complete co-localized 2-MCC gene cluster make transfer of function to PP_2338 robust. Studies in *Mycobacterium*, *Corynebacterium*, *Acetobacter*, and eukaryotes (*Toxoplasma*, *Magnaporthe*) further demonstrate the deep conservation of PrpD's role across the tree of life.

---

## Limitations and Knowledge Gaps

1. **No direct assay of the KT2440 protein.** The functional assignment for Q88KF2/PP_2338 rests on orthology (chiefly to *Salmonella* and *E. coli* PrpD), not on direct biochemical characterization of the *P. putida* enzyme. While the inference is strong, kinetic parameters (kcat, Km for 2-methylcitrate), stereospecificity, and substrate range specific to the KT2440 enzyme are unmeasured.

2. **Co-occurrence of *prpD* and *prpF* in KT2440.** The KT2440 cluster encodes both PrpD (PP_2338) and PrpF (PP_2337, aconitate isomerase), plus two aconitases. The functional interplay — whether PrpD and an AcnD-like system operate redundantly or under different conditions — has not been resolved experimentally in *P. putida*.

3. **Localization is inferred, not observed.** Cytoplasmic localization is supported by sequence-based predictions (no signal peptide, no TM segment, negative GRAVY) and substrate chemistry, but has not been confirmed by fractionation, fluorescence tagging, or proteomics for this specific protein.

4. **Structural data.** No experimental 3D structure of the *P. putida* PrpD is cited here; mechanistic details of cofactor-free dehydration in the MmgE/PrpD fold remain to be examined for this ortholog (though the family fold is defined by InterPro IPR036148 and related superfamily entries).

5. **The persistent 2Fe-2S annotation.** The erroneous GO:0051537 IEA annotation remains in the database and could mislead downstream automated analyses; it warrants correction/flagging.

---

## Proposed Follow-up Experiments / Actions

1. **Directly assay recombinant PP_2338.** Overexpress and purify His-tagged Q88KF2 (using vectors analogous to pTEV/pKLD, [PMID: 18295882](https://pubmed.ncbi.nlm.nih.gov/18295882/)) and measure 2-methylcitrate dehydratase activity, kinetic constants, and confirm the absence of an Fe–S cluster (UV-vis/EPR), directly validating the ortholog-based assignment.

2. **Genetic knockout in KT2440.** Construct a Δ*prpD* (PP_2338) mutant and test growth on propionate as sole carbon source; assay for 2-methylcitrate accumulation. Complementation should restore growth. This tests the physiological necessity of PrpD and its redundancy with any PrpF/AcnD system.

3. **Dissect PrpD vs PrpF/aconitase division of labor.** Systematically delete PP_2337 (*prpF*), PP_2336, and PP_2339 individually and in combination with Δ*prpD* to define which enzymes carry the dehydration/isomerization/hydration steps in *P. putida*.

4. **Confirm subcellular localization.** Use cell fractionation or a fluorescent-protein fusion to verify cytoplasmic localization empirically.

5. **Correct the database annotation.** Submit evidence (via UniProt/GO) to flag or remove the electronically inferred GO:0051537 "2Fe-2S cluster binding" term for Q88KF2, citing the experimental cofactor-free characterization ([PMID: 11294638](https://pubmed.ncbi.nlm.nih.gov/11294638/)).

6. **Structural characterization.** Determine or model (AlphaFold) the 3D structure to examine the all-α-helical MmgE/PrpD fold and identify catalytic residues responsible for cofactor-free β-elimination.

---

## Conclusion

*prpD* (Q88KF2 / PP_2338) of *Pseudomonas putida* KT2440 encodes the **2-methylcitrate dehydratase (EC 4.2.1.79)** of the 2-methylcitric acid cycle. It catalyzes the cytoplasmic, cofactor-independent dehydration of (2S,3S)-2-methylcitrate to 2-methyl-*cis*-aconitate — the committed dehydration step that enables propionate to be oxidized to pyruvate and succinate while detoxifying propionyl-CoA and 2-methylcitrate. This assignment, though not yet verified by direct assay of the KT2440 protein itself, is firmly supported by direct enzymology on high-identity orthologs, complete conserved pathway gene context, and consistent bioinformatic evidence for a soluble cytoplasmic enzyme of the MmgE/PrpD family.


## Artifacts

- [OpenScientist final report](prpD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](prpD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11294638
2. PMID:42271202
3. PMID:10482501
4. PMID:29145506
5. PMID:30933666
6. PMID:19948794
7. PMID:11976302
8. PMID:22916289
9. PMID:18295882