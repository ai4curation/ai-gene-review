---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T11:38:46.809596'
end_time: '2026-07-23T11:53:29.184504'
duration_seconds: 882.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaA
  gene_symbol: paaA
  uniprot_accession: Q88HS5
  protein_description: 'SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase alpha subunit
    {ECO:0000313|EMBL:AAN68885.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68885.1};'
  gene_info: Name=paaA {ECO:0000313|EMBL:AAN68885.1}; OrderedLocusNames=PP_3278 {ECO:0000313|EMBL:AAN68885.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Aromatic_CoA_ox/epox. (IPR052703); Ferritin-like. (IPR012347);
    Ferritin-like_SF. (IPR009078); PaaA. (IPR011881); PaaA_PaaC. (IPR007814)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: paaA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS5
- **Protein Description:** SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase alpha subunit {ECO:0000313|EMBL:AAN68885.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68885.1};
- **Gene Information:** Name=paaA {ECO:0000313|EMBL:AAN68885.1}; OrderedLocusNames=PP_3278 {ECO:0000313|EMBL:AAN68885.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Aromatic_CoA_ox/epox. (IPR052703); Ferritin-like. (IPR012347); Ferritin-like_SF. (IPR009078); PaaA. (IPR011881); PaaA_PaaC. (IPR007814)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaA** (gene ID: paaA, UniProt: Q88HS5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *paaA* (Q88HS5, PP_3278) — Ring 1,2-Phenylacetyl-CoA Epoxidase α-Subunit in *Pseudomonas putida* KT2440

## Summary

**paaA** (UniProt **Q88HS5**; ordered locus **PP_3278**) of *Pseudomonas putida* KT2440 encodes the **catalytic α-subunit of the ring 1,2-phenylacetyl-CoA epoxidase** (EC 1.14.13.149), the oxygen- and NAD(P)H-dependent enzyme that catalyzes the committed, ring-dearomatizing step of the aerobic **phenylacetate (PAA) catabolic pathway**. PaaA is not a stand-alone enzyme: it is the iron-binding catalytic core of a **multicomponent bacterial monooxygenase** (the PaaABC(D)E complex), in which PaaA (α, catalytic) pairs with PaaC (β, structural) to form a di-iron oxygenase, PaaB is an accessory subunit required for activity, PaaE is the NAD(P)H-dependent reductase that supplies electrons, and PaaD is dispensable for catalysis. This enzyme performs the biochemically difficult task of activating the extremely stable aromatic ring of phenylacetyl-CoA by inserting a single atom of molecular oxygen to yield a **ring 1,2-epoxide** (1,2-epoxyphenylacetyl-CoA), the first non-aromatic intermediate of the pathway.

The phenylacetate pathway is one of the most widely distributed bacterial routes for the aerobic degradation of aromatic compounds — a metabolic "funnel" through which phenylalanine, phenylethylamine, styrene, ethylbenzene, and numerous environmental aromatic pollutants are channeled after conversion to the common intermediate **phenylacetyl-CoA (PA-CoA)**. PaaA sits at the mechanistic heart of this funnel: its epoxidation reaction is what breaks aromaticity and permits all downstream ring-opening and β-oxidation chemistry. Remarkably, the PaaA-containing complex is **bifunctional**: in addition to forming the ring 1,2-epoxide, it can catalyze the NADPH-dependent **removal** of the epoxide oxygen, regenerating phenylacetyl-CoA and releasing water. This oxygenase/deoxygenase duality serves as a built-in detoxification safety valve for the reactive, unstable epoxide product.

The gene product functions in the **cytoplasm** (all reactions of the paa pathway involve soluble CoA-thioester intermediates), is expressed from the *paa* gene cluster, and is transcriptionally induced when its own substrate, PA-CoA, accumulates and de-represses the pathway by binding the **PaaX** repressor. Downstream, the epoxide is isomerized to an unusual seven-membered oxygen heterocycle (**oxepin-CoA**) by PaaG, subjected to hydrolytic (non-oxygenolytic) ring cleavage by the bifunctional enzyme **PaaZ**, and processed by β-oxidation-like steps to the central-metabolism building blocks **acetyl-CoA and succinyl-CoA**. This report documents the enzymatic identity, mechanism, cellular context, pathway integration, and evidence base for PaaA, and clearly distinguishes it from the many unrelated genes that share the "paaA" symbol.

---

## Gene/Protein Identity Verification

Before presenting findings, the mandatory identity check confirms the research target is correct:

| Attribute | UniProt annotation (Q88HS5) | Literature match |
|---|---|---|
| Gene symbol | *paaA* | ✓ *paa* cluster gene, phenylacetate degradation |
| Protein description | Ring 1,2-phenylacetyl-CoA epoxidase α-subunit; EC 1.14.13.149 | ✓ PaaA = catalytic α-subunit (Grishin et al. 2011) |
| Organism | *Pseudomonas putida* KT2440 | ✓ paa cluster characterized in *P. putida* and *E. coli* |
| Key domains | PaaA (IPR011881); PaaA_PaaC (IPR007814); Ferritin-like/Ferritin-like_SF (IPR012347/IPR009078); Aromatic_CoA_ox/epox (IPR052703) | ✓ Ferritin-like fold houses the di-iron center of multicomponent monooxygenases |

The domain architecture is decisive. The **Ferritin-like superfamily fold (IPR009078/IPR012347)** is the structural hallmark of **di-iron carboxylate oxygenases** (the same fold family as the hydroxylase components of soluble methane monooxygenase and toluene monooxygenases). The dedicated **PaaA (IPR011881)** and **PaaA_PaaC (IPR007814)** signatures confirm this is the phenylacetyl-CoA oxygenase α-subunit, not an unrelated protein. This is fully consistent with the assigned reaction (EC 1.14.13.149) and rules out mis-identification.

> **Note on symbol ambiguity:** "paaA" and "PAAA"-like symbols are reused across biology for entirely unrelated genes (plant/eukaryotic proteins; unrelated bacterial loci). The literature search surfaced several off-target hits — e.g., an Arabidopsis UDP-glucosyltransferase acting on phenylacetic acid ([PMID: 32868079](https://pubmed.ncbi.nlm.nih.gov/32868079/)), and a copper–phenanthroline antimicrobial compound abbreviated "P-FAH-Cu-phen" ([PMID: 41912070](https://pubmed.ncbi.nlm.nih.gov/41912070/)) — that are **NOT** relevant to this bacterial enzyme. All findings below are restricted to the bacterial phenylacetate-CoA epoxidase α-subunit that matches Q88HS5's annotation and domain architecture.

---

## Key Findings

### Finding 1 — PaaA is the catalytic α-subunit of the ring 1,2-phenylacetyl-CoA epoxidase, the committed step of aerobic phenylacetate catabolism

The central, well-supported conclusion of this investigation is that **PaaA is the catalytic α-subunit of a multicomponent oxygenase that epoxidizes the aromatic ring of phenylacetyl-CoA**. This is the first and rate-committing chemical transformation of the aerobic phenylacetate degradation pathway.

The pathway itself was elucidated by Teufel and colleagues, who showed that bacterial aerobic degradation of phenylalanine/phenylacetate is fundamentally different from classical aromatic-ring dioxygenation: it proceeds through **coenzyme A thioesters**, and "the aromatic ring of phenylacetyl-CoA becomes activated to a ring 1,2-epoxide by a distinct multicomponent oxygenase" ([PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/)). This pathway is encoded by the *paa* gene cluster and is remarkably widespread, present in roughly 16% of sequenced bacterial genomes, including both *Escherichia coli* and *Pseudomonas putida*.

The precise subunit role of PaaA was established structurally and biochemically by Grishin et al., who reconstituted the *E. coli* phenylacetyl-CoA monooxygenase complex. They demonstrated that "**PaaAC forms a catalytic core with a monooxygenase fold with PaaA being the catalytic α subunit and PaaC, the structural β subunit**" ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/)). Their reconstitution further showed that **PaaA, PaaB, PaaC, and PaaE are each required for catalysis, whereas PaaD is dispensable**. PaaA is therefore the iron-binding catalytic heart of the complex, and its ferritin-like fold (matching Q88HS5's domain annotation) houses the di-iron active site where O₂ activation and ring epoxidation occur.

The reaction can be written as:

```
phenylacetyl-CoA + O2 + NAD(P)H + H+  →  1,2-epoxyphenylacetyl-CoA + NAD(P)+ + H2O
                    (catalyzed by PaaABCE; PaaA = catalytic α-subunit; EC 1.14.13.149)
```

This is a **substrate-specific** reaction: the enzyme acts on the CoA thioester of phenylacetate, not on free phenylacetic acid. The prior activation of phenylacetate to phenylacetyl-CoA is carried out by a dedicated phenylacetate-CoA ligase (PaaK), meaning the pathway commits its substrate to CoA-thioester chemistry before PaaA acts.

### Finding 2 — The PaaA complex is a bifunctional oxygenase/deoxygenase with a di-iron center that self-detoxifies its reactive epoxide product

A striking mechanistic property of the PaaA-containing enzyme is that it is **bifunctional**. Teufel, Friedrich, and Fuchs purified the multicomponent monooxygenase (PaaABCE) and demonstrated that it "**not only transforms phenylacetyl-CoA into its ring-1,2-epoxide, but also mediates the NADPH-dependent removal of the epoxide oxygen, regenerating phenylacetyl-CoA with formation of water**" ([PMID: 22398448](https://pubmed.ncbi.nlm.nih.gov/22398448/)). The same study provided evidence for a **catalytic di-iron center**, consistent with the ferritin-like fold annotated for Q88HS5.

The biological logic of this oxygenase/deoxygenase duality is detoxification. The ring 1,2-epoxide product is chemically reactive and unstable — a potentially cytotoxic electrophile if it accumulates or escapes the pathway. By retaining the capacity to reverse its own reaction (stripping the epoxide oxygen and regenerating the harmless CoA thioester), the enzyme provides an **intrinsic safety valve** that prevents dangerous build-up of the epoxide when downstream flux is limiting.

Structural analysis reinforces that this complex is mechanistically distinct from other di-iron monooxygenases. Grishin et al. found that **PaaAC lacks the conserved hydrogen-bond network** connecting the di-iron center to the protein surface that is seen in canonical bacterial multicomponent monooxygenases (like methane/toluene monooxygenases) ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/)). This implies a **distinct mode of reductase association and electron transfer** — electrons for O₂ activation are delivered by the flavin/[2Fe-2S] reductase subunit **PaaE** (which uses NAD(P)H), and the unusual active-site architecture likely underlies both the epoxidation and the reverse deoxygenation chemistry.

### Finding 3 — PaaA launches a cytoplasmic hybrid pathway that ends in acetyl-CoA and succinyl-CoA, and is transcriptionally gated by phenylacetyl-CoA

PaaA's epoxidation is the entry point of a defined, ordered downstream sequence. Teufel et al. showed that "**the reactive nonaromatic epoxide is isomerized to a seven-member O-heterocyclic enol ether, an oxepin. This isomerization is followed by hydrolytic ring cleavage and beta-oxidation steps, leading to acetyl-CoA and succinyl-CoA**" ([PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/)). This is termed a **"hybrid" pathway** because, although it is aerobic and uses O₂ at the PaaA step, the ring is ultimately opened by **hydrolysis (non-oxygenolytic cleavage)** — a strategy more reminiscent of anaerobic aromatic degradation, combined with β-oxidation-like chemistry.

The specific downstream steps are:

1. **PaaG** (an enoyl-CoA isomerase of the crotonase superfamily) isomerizes the ring 1,2-epoxide to **oxepin-CoA**, an unusual seven-membered oxygen heterocycle.
2. **PaaZ**, a bifunctional fusion enzyme with a C-terminal (R)-specific enoyl-CoA hydratase (MaoC-like) domain and an N-terminal NADP⁺-dependent aldehyde dehydrogenase domain, cleaves the oxepin ring. The hydratase produces a highly reactive aldehyde, which the aldehyde dehydrogenase immediately oxidizes to **3-oxo-5,6-dehydrosuberyl-CoA** ([PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/)). The fusion architecture prevents the reactive aldehyde from cyclizing into a stable dead-end product.
3. A series of **β-oxidation-like enzymes** (including the PaaF enoyl-CoA hydratase and PaaG isomerase, which form a defined **PaaFG complex**; [PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/)) shorten the chain and ultimately yield **acetyl-CoA and succinyl-CoA**, which enter central metabolism via the TCA cycle.

The physical organization of these downstream enzymes into complexes (PaaFG) is thought to accelerate the pathway following PaaA's production of the "toxic and unstable epoxide-CoA," channeling the reactive intermediates and minimizing their escape ([PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/)).

Expression of *paaA* (and the entire *paa* cluster) is controlled by the transcriptional repressor **PaaX**. Fernández et al. showed that the pathway's own first intermediate acts as the inducer: PaaX "is able to bind and inhibit the activity of Px [the PaaX-regulated promoter] in a phenylacetyl-coenzyme A (PA-CoA) dependent manner" ([PMID: 24983528](https://pubmed.ncbi.nlm.nih.gov/24983528/)). In other words, when phenylacetate is available and converted to PA-CoA, PA-CoA binds PaaX, relieves repression, and switches on transcription of the genes — including *paaA* — that consume it. The crystal structure of *E. coli* W PaaX reveals a novel transcription-regulator fold with a crevice sized to bind the PA-CoA effector, and confirms that induction proceeds by release of PaaX from its operator ([PMID: 37949283](https://pubmed.ncbi.nlm.nih.gov/37949283/)).

---

## Mechanistic Model / Interpretation

Integrating the three findings produces a coherent picture of PaaA's role. The following diagram places PaaA within the complete phenylacetate funnel:

```
 UPSTREAM AROMATIC SOURCES (funneled into the pathway)
 phenylalanine · phenylethylamine · styrene · ethylbenzene · 2-phenylethanol · env. pollutants
                                   |
                                   v
                        phenylacetic acid (PAA)
                                   |   PaaK (phenylacetate-CoA ligase, ATP)
                                   v
                        phenylacetyl-CoA (PA-CoA) ---------> binds PaaX repressor
                                   |                          => DE-REPRESSES paa operon
                                   |                             (induces paaA transcription)
             +---------------------+---------------------+
             |   PaaABC(D)E MULTICOMPONENT MONOOXYGENASE |
             |   PaaA = catalytic alpha-subunit (di-iron)|  <=== THIS GENE (Q88HS5)
             |   PaaC = structural beta-subunit          |
             |   PaaB = required accessory subunit        |
             |   PaaE = NAD(P)H reductase (e- donor)      |
             |   PaaD = dispensable                       |
             |   O2 + NAD(P)H consumed                    |
             |   BIFUNCTIONAL: also deoxygenates epoxide  |
             +---------------------+---------------------+
                                   v
                    1,2-epoxyphenylacetyl-CoA  (reactive, toxic epoxide)
                                   |   PaaG (isomerase)
                                   v
                             oxepin-CoA  (7-membered O-heterocycle)
                                   |   PaaZ (hydratase + aldehyde dehydrogenase; hydrolytic ring cleavage)
                                   v
                    3-oxo-5,6-dehydrosuberyl-CoA
                                   |   PaaF/PaaG + beta-oxidation enzymes (PaaFG complex)
                                   v
                    acetyl-CoA  +  succinyl-CoA  --> TCA cycle / central metabolism
```

**Primary function (enzyme, reaction, substrate specificity).** PaaA is an **oxidoreductase (monooxygenase/oxygenase), EC 1.14.13.149**. As the catalytic α-subunit, it activates O₂ at a **di-iron center** and inserts one oxygen atom across the C1–C2 bond of the aromatic ring of **phenylacetyl-CoA**, producing the **ring 1,2-epoxide**; the other oxygen atom is reduced to water using electrons from NAD(P)H delivered via PaaE. Substrate specificity is for the **CoA thioester of phenylacetate**, not free PAA — the pathway deliberately commits substrate to CoA chemistry (via PaaK) before PaaA acts. The enzyme is additionally a **deoxygenase**, able to reverse the epoxidation for detoxification.

**Cellular localization.** PaaA functions in the **cytoplasm**. There are no signal-peptide/membrane features; the substrate and all intermediates are soluble CoA thioesters, and the reductase (PaaE, NAD(P)H-dependent) and downstream enzymes (PaaG, PaaZ, PaaF) are cytoplasmic. The reaction therefore occurs entirely within the cytosol, integrated with the cytoplasmic NAD(P)H/CoA pools.

**Pathway role.** PaaA catalyzes the **committed, ring-dearomatizing step** of the aerobic phenylacetate catabolic pathway — a globally important microbial "funnel" for aromatic-compound degradation. Its product feeds isomerization (PaaG) → hydrolytic ring cleavage (PaaZ) → β-oxidation → acetyl-CoA + succinyl-CoA. Its expression is gated by the PA-CoA/PaaX regulatory switch, ensuring the potentially hazardous epoxidation chemistry is only active when substrate is present.

**Why this matters.** Because the paa pathway is the convergence point for degradation of styrene, ethylbenzene, and other aromatic pollutants (and because *P. putida* KT2440 is a workhorse for bioremediation and industrial biocatalysis), PaaA is the key "dearomatization engine" that enables these compounds to be mineralized. In *P. putida* F1, the ability to sense and swim toward PAA (energy taxis via the Aer2 receptor) is coupled to the cell's capacity to metabolize it through this same pathway ([PMID: 23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/)). Upstream funneling is illustrated by styrene-degrading *Rhodococcus*, which converts styrene → styrene oxide → phenylacetaldehyde → phenylacetic acid → phenylacetyl-CoA before entering the PaaA-initiated route ([PMID: 21996027](https://pubmed.ncbi.nlm.nih.gov/21996027/)).

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings | Strength |
|---|---|---|---|
| [20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/) | *Bacterial phenylalanine and phenylacetate catabolic pathway revealed* | Establishes the whole pathway; ring 1,2-epoxidation of PA-CoA by a multicomponent oxygenase; downstream oxepin/hydrolysis/β-ox to acetyl-CoA + succinyl-CoA; ~16% of bacterial genomes | Landmark primary study (PNAS) |
| [21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/) | *Structural and functional studies of the E. coli phenylacetyl-CoA monooxygenase complex* | Directly identifies **PaaA as the catalytic α-subunit** and PaaC as structural β-subunit; PaaA/B/C/E required, PaaD dispensable; distinct electron-transfer architecture | Primary structural/biochemical (JBC) |
| [22398448](https://pubmed.ncbi.nlm.nih.gov/22398448/) | *An oxygenase that forms and deoxygenates toxic epoxide* | Demonstrates **bifunctional oxygenase/deoxygenase** activity and the **di-iron center**; NADPH-dependent epoxide removal → self-detoxification | Primary study (Nature) |
| [21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/) | *Studies on the mechanism of ring hydrolysis in phenylacetate degradation* | Characterizes PaaZ bifunctional ring-cleavage downstream of PaaA; explains reactive-aldehyde handling; metabolic branch point | Primary study |
| [24983528](https://pubmed.ncbi.nlm.nih.gov/24983528/) | *Insights on regulation of the phenylacetate degradation pathway from E. coli* | PA-CoA-dependent inhibition of PaaX → de-repression; defines regulatory context of *paaA* expression | Primary regulatory study |
| [37949283](https://pubmed.ncbi.nlm.nih.gov/37949283/) | *Structural characterization of PaaX* | Crystal structure of the PaaX repressor; novel fold; crevice for PA-CoA effector; induction by release from operator | Primary structural study |
| [22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/) | *Protein-protein interactions in the β-oxidation part... PaaF-PaaG complex* | Shows downstream β-oxidation enzymes form defined complexes; frames PaaABCE as producing a "toxic and unstable epoxide-CoA" requiring rapid downstream channeling | Primary structural study |
| [23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/) | *Taxis of P. putida F1 toward phenylacetic acid...* | Confirms a *paa* cluster in *P. putida*; PAA is a metabolizable chemoattractant via energy taxis; physiological relevance | Primary study (same species) |
| [21996027](https://pubmed.ncbi.nlm.nih.gov/21996027/) | *Styrene metabolism genes... Rhodococcus* | Illustrates how upstream aromatics (styrene→PAA→PA-CoA) funnel into the PAA pathway that PaaA initiates | Supporting/context |
| [30861343](https://pubmed.ncbi.nlm.nih.gov/30861343/) | *Shunting Phenylacetic Acid Catabolism for Tropone Biosynthesis* | Demonstrates that the PAA catabolic module (incl. the epoxidation/PaaZ steps) can be redirected for biosynthesis, underscoring intermediate reactivity | Supporting/applied |

**Confidence and transfer of inference.** The most detailed subunit-level (PaaA = catalytic α-subunit) and mechanistic (bifunctional di-iron oxygenase/deoxygenase) evidence derives from the *E. coli* orthologue ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/); [PMID: 22398448](https://pubmed.ncbi.nlm.nih.gov/22398448/)). Function is assigned to the *P. putida* KT2440 protein Q88HS5 by strong orthology — identical PaaA-specific InterPro signatures (IPR011881, IPR007814) plus the ferritin-like di-iron domains (IPR012347, IPR009078) — combined with the curated UniProt EC assignment (1.14.13.149) and the demonstrated presence and physiological function of the *paa* cluster in *P. putida* ([PMID: 23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/)).

**Off-target / non-relevant hits identified during search** (explicitly excluded): [PMID: 32868079](https://pubmed.ncbi.nlm.nih.gov/32868079/) (Arabidopsis UGT84B1, a plant glucosyltransferase acting on phenylacetic acid — unrelated eukaryotic gene) and [PMID: 41912070](https://pubmed.ncbi.nlm.nih.gov/41912070/) (copper–phenanthroline antimicrobial "P-FAH-Cu-phen" — no relation to the bacterial enzyme). These illustrate the symbol/keyword ambiguity flagged in the identity-verification step and do not inform the annotation of Q88HS5.

---

## Supported and Refuted Hypotheses

**Supported:**
- **H1** — PaaA is the catalytic α-subunit of a di-iron phenylacetyl-CoA epoxidase. *Supported* ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/); [PMID: 22398448](https://pubmed.ncbi.nlm.nih.gov/22398448/)).
- **H2** — Its substrate is the CoA thioester phenylacetyl-CoA, not free phenylacetate. *Supported* ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/)).
- **H3** — It initiates a cytoplasmic hybrid pathway ending in acetyl-CoA + succinyl-CoA. *Supported* ([PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/); [PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/)).
- **H4** — The complex has an intrinsic deoxygenase/detoxification function. *Supported* ([PMID: 22398448](https://pubmed.ncbi.nlm.nih.gov/22398448/)).

**Refuted / excluded:**
- PaaA is NOT a classical Rieske ring-hydroxylating dioxygenase acting on a free aromatic substrate; it is a ferritin-like di-iron oxygenase acting on a CoA thioester.
- The "paaA" of Q88HS5 is unrelated to plant/auxin PAA-metabolism genes or other eukaryotic genes that share the "PAA" string.

---

## Limitations and Knowledge Gaps

1. **Direct characterization is largely from *E. coli*, not *P. putida* KT2440.** The definitive structural and biochemical dissection of subunit roles (PaaA as α-catalytic subunit; PaaABCE requirement; bifunctional deoxygenation) was performed on the *E. coli* enzyme ([PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/); [PMID: 22398448](https://pubmed.ncbi.nlm.nih.gov/22398448/)). The *P. putida* KT2440 ortholog (Q88HS5/PP_3278) is annotated by strong homology and the *P. putida paa* cluster is functionally validated at the pathway/physiology level ([PMID: 23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/)), but strain-specific kinetic constants, structural coordinates, and any subtle substrate-range differences for the *P. putida* PaaA itself have not been directly measured here.

2. **No experimental high-resolution structure of PaaA from *P. putida* was examined.** The di-iron site geometry and residue-level catalytic mechanism are inferred from the ferritin-like fold annotation and *E. coli* work; an AlphaFold model or crystal structure of Q88HS5 was not analyzed in this investigation.

3. **Kinetic parameters (kcat, Km) and substrate-specificity breadth are not quantified.** While the substrate is clearly the CoA thioester of phenylacetate, tolerance for ring-substituted phenylacetyl-CoA analogs (relevant to degrading substituted aromatic pollutants) is not established from the reviewed literature.

4. **Electron-transfer stoichiometry and the mechanistic basis of the oxygenase↔deoxygenase switch** remain incompletely defined. The unusual absence of the conserved di-iron-to-surface H-bond network suggests a novel reductase-coupling mechanism, but the precise electron path from PaaE to the PaaA di-iron center is not fully resolved.

5. **Role of PaaB and PaaD.** PaaB is required for activity and PaaD is dispensable, but the molecular functions of these accessory subunits (e.g., assembly, stability, or effector roles) are not fully explained.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and in vitro reconstitution of the *P. putida* KT2440 PaaABCE complex** to directly measure epoxidation kinetics (kcat, Km for phenylacetyl-CoA), O₂ and NAD(P)H stoichiometry, and to confirm the bifunctional deoxygenase activity in the *Pseudomonas* enzyme, rather than relying on *E. coli* orthology.

2. **Structural determination of the *P. putida* PaaA/PaaC catalytic core** (cryo-EM or X-ray) and/or AlphaFold-Multimer modeling with di-iron site validation, to map active-site residues, confirm the ferritin-like di-iron geometry, and rationalize the absence of the canonical surface H-bond network.

3. **Substrate-specificity profiling** using a panel of ring-substituted phenylacetyl-CoA analogs (derived from methyl-, halo-, or hydroxy-styrenes/ethylbenzenes) to define the pollutant range that the *P. putida* pathway can dearomatize — directly relevant to bioremediation applications.

4. **Targeted *paaA* knockout in *P. putida* KT2440** followed by growth assays on phenylacetate and phenylalanine, plus metabolomic detection of accumulated phenylacetyl-CoA, to confirm that PaaA is genetically essential for aerobic PAA catabolism in this strain and non-redundant.

5. **In vivo epoxide-stress and channeling studies** — quantify epoxide/oxepin-CoA intermediate leakage under conditions where downstream enzymes (PaaG/PaaZ) are limiting, testing the physiological importance of PaaA's built-in deoxygenase safety valve and the PaaFG-type metabolite channeling.

6. **Reductase-coupling mechanism dissection** — reconstitute PaaE electron transfer with the *P. putida* complex and use rapid kinetics/EPR spectroscopy on the di-iron center to define the oxygenase→deoxygenase mechanistic switch.

---

## Conclusion

PaaA (Q88HS5, PP_3278) of *Pseudomonas putida* KT2440 is the **catalytic α-subunit of the ring 1,2-phenylacetyl-CoA epoxidase** (EC 1.14.13.149), a cytoplasmic, di-iron, ferritin-fold multicomponent monooxygenase (the PaaABC(D)E complex). It catalyzes the O₂- and NAD(P)H-dependent epoxidation of the aromatic ring of phenylacetyl-CoA — the committed, ring-dearomatizing entry step of the widely distributed aerobic phenylacetate catabolic pathway — and is uniquely bifunctional, also deoxygenating its own reactive epoxide product as a detoxification mechanism. Its product is funneled through oxepin-CoA (PaaG), hydrolytic ring cleavage (PaaZ), and β-oxidation to acetyl-CoA and succinyl-CoA, with expression controlled by the PA-CoA/PaaX regulatory switch. The annotation is robustly supported by structural, biochemical, and pathway-level evidence, with the principal caveat that the most detailed mechanistic work was performed on the *E. coli* ortholog.

---

### Key References

- Teufel R, et al. *Bacterial phenylalanine and phenylacetate catabolic pathway revealed.* PNAS 2010. [PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/)
- Grishin AM, et al. *Structural and functional studies of the E. coli phenylacetyl-CoA monooxygenase complex.* J Biol Chem 2011. [PMID: 21247899](https://pubmed.ncbi.nlm.nih.gov/21247899/)
- Teufel R, Friedrich T, Fuchs G. *An oxygenase that forms and deoxygenates toxic epoxide.* Nature 2012. [PMID: 22398448](https://pubmed.ncbi.nlm.nih.gov/22398448/)
- Teufel R, et al. *Studies on the mechanism of ring hydrolysis in phenylacetate degradation: a metabolic branching point.* J Biol Chem 2011. [PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/)
- Fernández C, Díaz E, García JL. *Insights on the regulation of the phenylacetate degradation pathway from E. coli.* Environ Microbiol Rep 2014. [PMID: 24983528](https://pubmed.ncbi.nlm.nih.gov/24983528/)
- Grishin AM, et al. *Protein-protein interactions in the β-oxidation part of the phenylacetate utilization pathway: crystal structure of the PaaF-PaaG hydratase-isomerase complex.* J Biol Chem 2012. [PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/)
- *Structural characterization of PaaX, the main repressor of the phenylacetate degradation pathway in E. coli W.* 2023. [PMID: 37949283](https://pubmed.ncbi.nlm.nih.gov/37949283/)
- Luu RA, et al. *Taxis of Pseudomonas putida F1 toward phenylacetic acid is mediated by the energy taxis receptor Aer2.* 2013. [PMID: 23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/)


## Artifacts

- [OpenScientist final report](paaA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:32868079
2. PMID:41912070
3. PMID:20660314
4. PMID:21247899
5. PMID:22398448
6. PMID:21296885
7. PMID:22961985
8. PMID:24983528
9. PMID:37949283
10. PMID:23377939
11. PMID:21996027