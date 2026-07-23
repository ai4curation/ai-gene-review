---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T14:57:10.089418'
end_time: '2026-07-23T15:43:12.255388'
duration_seconds: 2762.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaZ
  gene_symbol: paaZ
  uniprot_accession: Q88HT3
  protein_description: 'SubName: Full=Oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA
    semialdehyde dehydrogenase {ECO:0000313|EMBL:AAN68877.1}; EC=1.2.1.91 {ECO:0000313|EMBL:AAN68877.1};
    EC=3.3.2.12 {ECO:0000313|EMBL:AAN68877.1};'
  gene_info: Name=paaZ {ECO:0000313|EMBL:AAN68877.1}; OrderedLocusNames=PP_3270 {ECO:0000313|EMBL:AAN68877.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_N.
    (IPR016162); Aldehyde_DH_dom. (IPR015590); HotDog_dom_sf. (IPR029069)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: paaZ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaZ-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HT3
- **Protein Description:** SubName: Full=Oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase {ECO:0000313|EMBL:AAN68877.1}; EC=1.2.1.91 {ECO:0000313|EMBL:AAN68877.1}; EC=3.3.2.12 {ECO:0000313|EMBL:AAN68877.1};
- **Gene Information:** Name=paaZ {ECO:0000313|EMBL:AAN68877.1}; OrderedLocusNames=PP_3270 {ECO:0000313|EMBL:AAN68877.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590); HotDog_dom_sf. (IPR029069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaZ" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaZ' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaZ** (gene ID: paaZ, UniProt: Q88HT3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **paaZ** (Q88HT3 / PP_3270) in *Pseudomonas putida* KT2440

## Summary

**paaZ** (UniProt **Q88HT3**; ordered locus **PP_3270**) of *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) encodes a **soluble, cytoplasmic, bifunctional enzyme** that catalyzes the pivotal ring-cleavage step of the **aerobic phenylacetate (Paa) degradation pathway**. The protein is a natural **fusion of two catalytic domains**: a C-terminal (R)-specific enoyl-CoA hydratase domain (of the MaoC/HotDog fold) that hydrolytically opens the seven-membered **oxepin-CoA** ring (**EC 3.3.2.12**, oxepin-CoA hydrolase), and an N-terminal **NADP⁺-dependent aldehyde dehydrogenase** domain (of the Ald_DH/histidinol_DH fold) that immediately oxidizes the resulting reactive aldehyde to **3-oxo-5,6-dehydrosuberyl-CoA** (**EC 1.2.1.91**). These two activities and their domain assignments match the UniProt description and InterPro domain complement precisely, confirming that the gene symbol, organism, and domain architecture are all internally consistent — **this is the correct gene**, and it is unambiguous.

The PaaZ reaction sits at the **branch point** between an unstable, chemically reactive intermediate and productive catabolism. The oxepin-CoA ring, generated upstream by a multicomponent oxygenase (PaaABC(D)E) that epoxidizes phenylacetyl-CoA plus an isomerase that converts the epoxide, is opened by PaaZ to yield a highly reactive aldehyde. If this aldehyde is not oxidized instantly it cyclizes into a stable dead-end product; the physical fusion of the hydratase and dehydrogenase activities in a single polypeptide — and the enzyme's higher-order **trimer-of-dimers** architecture with **substrate channeling** — ensures the aldehyde is captured and oxidized before it can escape. The 3-oxo-5,6-dehydrosuberyl-CoA product is then processed by β-oxidation-like reactions, ultimately yielding **acetyl-CoA and succinyl-CoA**, which feed central metabolism.

Biologically, *paaZ* is embedded in the *paa* catabolic gene cluster, is induced in response to the true inducer **phenylacetyl-CoA** (via the PaaX repressor), and enables *P. putida* to grow on phenylacetate and on the many aromatic compounds (phenylalanine, 2-phenylethylamine, styrene, ethylbenzene) that funnel through phenylacetyl-CoA. This same machinery has been co-opted biotechnologically for medium-chain dicarboxylate (e.g., adipate) metabolism, underscoring the pathway's chemical logic and plasticity.

---

## Gene/Protein Identity Verification

| Attribute | Value | Consistent with literature? |
|---|---|---|
| UniProt accession | Q88HT3 | ✔ |
| Gene symbol | *paaZ* | ✔ (assigned to the ring-cleavage step across taxa) |
| Locus | PP_3270 | ✔ |
| Organism | *P. putida* KT2440 | ✔ (pathway characterized in *P. putida* and *E. coli*) |
| EC numbers | 3.3.2.12 + 1.2.1.91 | ✔ (both directly demonstrated biochemically) |
| Domains | Ald_DH N/C (IPR016161/2/3, IPR015590) + HotDog/MaoC (IPR029069) | ✔ (dehydrogenase + hydratase fusion) |

**Verification result: CONFIRMED and unambiguous.** All evidence converges on a single, well-characterized bifunctional enzyme of the aerobic phenylacetate pathway. There is no symbol clash with an unrelated gene.

---

## Key Findings

### Finding 1 — PaaZ is a bifunctional oxepin-CoA hydrolase / aldehyde dehydrogenase

PaaZ is not a single-activity enzyme but a **fusion protein** combining two chemically distinct catalytic modules on one polypeptide chain. Biochemical characterization by Teufel and colleagues established that the **C-terminal (R)-specific enoyl-CoA hydratase domain** — historically annotated as "MaoC" — performs the ring-opening chemistry: it hydrolytically cleaves the oxepin-CoA ring to generate a **highly reactive aldehyde** intermediate. The **N-terminal NADP⁺-dependent aldehyde dehydrogenase domain** then oxidizes that aldehyde to **3-oxo-5,6-dehydrosuberyl-CoA** ([PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/)).

These two activities correspond exactly to the two EC numbers annotated in UniProt for Q88HT3: **EC 3.3.2.12** (oxepin-CoA hydrolase) and **EC 1.2.1.91** (3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase). The domain assignments are also fully consistent with the InterPro complement listed in the target record — the aldehyde dehydrogenase N- and C-terminal domains (IPR016162, IPR016163, IPR015590), the shared aldehyde/histidinol DH superfamily fold (IPR016161), and the HotDog domain superfamily (IPR029069) that houses the MaoC-like hydratase. As the authors state verbatim: *"The enzyme consists of a C-terminal (R)-specific enoyl-CoA hydratase domain (formerly MaoC) that cleaves the ring and produces a highly reactive aldehyde and an N-terminal NADP(+)-dependent aldehyde dehydrogenase domain that oxidizes the aldehyde to 3-oxo-5,6-dehydrosuberyl-CoA"* ([PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/)).

This finding establishes the **primary molecular function** of the gene product: an enzyme catalyzing two sequential reactions — hydrolytic ring opening followed by NADP⁺-dependent aldehyde oxidation — with the CoA-thioester substrate providing the anchoring handle for both active sites. The **NADP⁺** (rather than NAD⁺) dependence distinguishes the fused PaaZ arrangement from the alternative seen in some bacteria that use a stand-alone NAD⁺-dependent aldehyde dehydrogenase plus a separate hydratase.

### Finding 2 — PaaZ acts at the ring-cleavage branch point of the aerobic phenylacetate pathway

The broader pathway context was elucidated by Teufel et al. (2010), who defined a fundamentally **novel aerobic catabolic route** distinct from classical ring-hydroxylating dioxygenase pathways. In this route, phenylacetate is first activated to **phenylacetyl-CoA**; the aromatic ring is then epoxidized to a **ring 1,2-epoxide** by a distinct multicomponent oxygenase (PaaABC(D)E); the reactive epoxide is isomerized to a **seven-membered O-heterocyclic enol ether (an oxepin)**; and this oxepin undergoes **hydrolytic ring cleavage and β-oxidation**, ultimately producing **acetyl-CoA and succinyl-CoA** ([PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/)). PaaZ performs the hydrolytic ring-cleavage-plus-oxidation node of this sequence. In the authors' words: *"the aromatic ring of phenylacetyl-CoA becomes activated to a ring 1,2-epoxide by a distinct multicomponent oxygenase. The reactive nonaromatic epoxide is isomerized to a seven-member O-heterocyclic enol ether, an oxepin. This isomerization is followed by hydrolytic ring cleavage and beta-oxidation steps, leading to acetyl-CoA and succinyl-CoA"* ([PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/)).

Crucially, PaaZ sits at a **metabolic branch point** because the aldehyde it generates is chemically labile. Teufel et al. (2011) demonstrated that *"If not oxidized immediately, the reactive aldehyde condenses intramolecularly to a stable cyclic derivative that is largely prevented by PaaZ fusion in vivo"* ([PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/)). This provides the **physiological rationale** for why the two activities are fused into one protein: the fusion minimizes escape of the reactive intermediate into a dead-end cyclic product — a chemistry that, in other bacteria, is exploited to make tropone/tropolone natural products. PaaZ therefore functions not merely as a catalyst but as a **committed channeling device** that steers a reactive intermediate toward productive catabolism.

The downstream fate of the PaaZ product in *P. putida* was defined by Nogales et al. (2007), who characterized the final steps and confirmed that *"succinyl-CoA is one of the final products of this pathway in Pseudomonas putida and Escherichia coli"* ([PMID: 17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/)). Thus the 3-oxo-5,6-dehydrosuberyl-CoA generated by PaaZ is processed through β-oxidation-like steps to acetyl-CoA and succinyl-CoA, which enter the TCA cycle.

### Finding 3 — PaaZ forms a trilobed trimer-of-dimers and channels its intermediate by electrostatic pivoting

The structural basis for PaaZ's channeling function was resolved by cryo-electron microscopy. Sathyanarayanan et al. (2019) determined structures of PaaZ with and without ligands and showed that **three domain-swapped dimers assemble into a trilobed hexamer** (a trimer of dimers): *"The structures reveal that three domain-swapped dimers of the enzyme form a trilobed structure"* ([PMID: 31511507](https://pubmed.ncbi.nlm.nih.gov/31511507/)). This higher-order architecture spatially organizes the hydratase and dehydrogenase active sites within each functional unit.

Integrating the structures with small-angle X-ray scattering (SAXS), computation, site-directed mutagenesis, and microbial growth assays, the authors proposed a striking **substrate-channeling mechanism**. Rather than a conventional enclosed hydrophobic tunnel, PaaZ transfers its labile intermediate between the two active sites by **electrostatic pivoting of the CoA moiety**: *"the key intermediate is transferred from one active site to the other by a mechanism of electrostatic pivoting of the CoA moiety, mediated by a set of conserved positively charged residues"* ([PMID: 31511507](https://pubmed.ncbi.nlm.nih.gov/31511507/)). The CoA arm acts as a molecular tether that swings the reactive aldehyde from the ring-opening (hydratase) site to the oxidation (dehydrogenase) site, guided by conserved basic residues. This mechanism directly explains, at atomic resolution, the physiological observation from Finding 2 — the fusion and channeling together suppress formation of the dead-end cyclic product.

### Finding 4 — *paaZ* is encoded in the *paa* catabolic cluster, induced by phenylacetyl-CoA, and physiologically enables aromatic catabolism

The genetic and regulatory context of *paaZ* was established in *E. coli* by Ferrández et al. (1998) and extends to *P. putida* by homology and pathway conservation. In *E. coli* the *paa* cluster is organized as *paaZ*, *paaABCDEFGHIJK*, and *paaXY*; *paaZ* is transcribed from its own promoter (Pz), and PaaZ *"appears to catalyze the third enzymatic step"* of the aerobic hybrid pathway ([PMID: 9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/)). Regulation is exerted by the **PaaX repressor**, which responds to the CoA-thioester intermediate rather than to free phenylacetate: *"As PA-CoA is the true inducer, PaaX becomes the first regulator of an aromatic catabolic pathway that responds to a CoA derivative"* ([PMID: 9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/)). This means *paaZ* expression is switched on precisely when the substrate for the pathway (phenylacetyl-CoA) accumulates. The homologous cluster and organization occur in *P. putida* and other proteobacteria such as *Azoarcus evansii* ([PMID: 12189419](https://pubmed.ncbi.nlm.nih.gov/12189419/)).

Physiologically, the *paa* pathway is a **funneling hub**: diverse aromatic compounds — phenylalanine, 2-phenylethylamine, styrene, and ethylbenzene — are catabolized to the common intermediate phenylacetyl-CoA, which the pathway (including PaaZ) then degrades. In *P. putida* this supports growth on phenylacetate as a sole carbon and energy source and even underlies **chemotaxis toward phenylacetate** (mediated by the energy-taxis receptor Aer2 in *P. putida* F1) ([PMID: 23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/)). The same *paa*/β-oxidation machinery was more recently **co-opted for medium-chain dicarboxylate (adipate) metabolism** in engineered *P. putida* KT2440, where the *paa* cluster plays a central role in enabling growth on adipate, suberate, and sebacate ([PMID: 33965615](https://pubmed.ncbi.nlm.nih.gov/33965615/)). This highlights both the native role and the biotechnological versatility of the pathway in which *paaZ* participates.

---

## Mechanistic Model / Interpretation

PaaZ is best understood as a **two-active-site molecular assembly line** that converts a chemically dangerous intermediate into a stable, catabolizable thioester. The following diagram places PaaZ within the aerobic phenylacetate (Paa) pathway:

```
  Aromatic funnel substrates
  (phenylalanine, 2-phenylethylamine,
   styrene, ethylbenzene, phenylacetate)
                │
                ▼
       Phenylacetyl-CoA  ◄─── PaaX / PA-CoA regulation (true inducer)
                │
                │  PaaABC(D)E  (multicomponent ring 1,2-epoxidase/oxygenase)
                ▼
       1,2-epoxyphenylacetyl-CoA
                │
                │  PaaG  (isomerase)
                ▼
          Oxepin-CoA  (7-membered O-heterocyclic enol ether)
                │
   ┌────────────┴──────────────────────────────────────────┐
   │                    P a a Z   (fusion)                   │
   │                                                         │
   │  C-terminal MaoC/HotDog (R)-hydratase                   │
   │   → hydrolytic ring opening (EC 3.3.2.12)               │
   │        │  reactive aldehyde                             │
   │        │  ↳ electrostatic pivoting of CoA moiety        │
   │        ▼  (conserved + charged residues; no tunnel)     │
   │  N-terminal NADP+-dependent aldehyde dehydrogenase      │
   │   → oxidation (EC 1.2.1.91)                             │
   └────────────┬──────────────────────────────────────────┘
                ▼
     3-oxo-5,6-dehydrosuberyl-CoA
                │
                │  β-oxidation-like steps (PaaF/PaaG/PaaH/PaaJ)
                ▼
      Acetyl-CoA  +  Succinyl-CoA  →  TCA cycle

        (branch: if aldehyde escapes → stable cyclic dead-end
         product → tropone/tropolone natural products in some taxa)
```

The central chemical problem the pathway must solve is that the oxepin-CoA ring, once opened, yields an aldehyde that will spontaneously cyclize into a stable, non-metabolizable dead end. Evolution's solution is elegant on three nested levels:

1. **Domain fusion** — placing the ring-opening hydratase and the aldehyde-oxidizing dehydrogenase on a single polypeptide keeps the two catalytic events tightly coupled in time and space (Finding 1, [PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/)).
2. **Quaternary organization** — assembling three domain-swapped dimers into a trilobed hexamer creates the geometric framework in which the two active sites of a functional unit are correctly juxtaposed (Finding 3, [PMID: 31511507](https://pubmed.ncbi.nlm.nih.gov/31511507/)).
3. **Electrostatic channeling** — using the CoA arm as a charged lever, the enzyme swings the reactive aldehyde from the hydratase site to the dehydrogenase site guided by conserved positive residues, rather than relying on a sealed hydrophobic tunnel (Finding 3, [PMID: 31511507](https://pubmed.ncbi.nlm.nih.gov/31511507/)).

Together these features suppress the dead-end cyclic derivative in vivo and channel carbon into β-oxidation. The table below summarizes the two reactions and their attributes.

| Attribute | Ring-opening activity | Oxidation activity |
|---|---|---|
| Domain | C-terminal MaoC / HotDog (R)-hydratase | N-terminal Ald_DH (aldehyde dehydrogenase) |
| EC number | 3.3.2.12 (oxepin-CoA hydrolase) | 1.2.1.91 |
| Substrate | Oxepin-CoA | Reactive ring-opened aldehyde |
| Product | Reactive aldehyde (ring-opened) | 3-oxo-5,6-dehydrosuberyl-CoA |
| Cofactor | None (hydrolytic) | NADP⁺ |
| InterPro fold | HotDog domain superfamily (IPR029069) | Ald_DH/histidinol_DH (IPR016161/2/3, IPR015590) |

**Localization.** No secretion signal, membrane-spanning region, or lipid anchor is implied by the domain architecture; all substrates are soluble CoA thioesters and the cofactor is soluble NADP⁺. Consistent with the entire Paa pathway operating on cytoplasmic CoA-activated intermediates, PaaZ carries out its function in the **cytoplasm** as a soluble oligomeric enzyme.

**Pathway role summary.** PaaZ catalyzes the committed conversion that transforms a ring-opened but still reactive species into a stable β-oxidation substrate. It is the linchpin connecting the oxygenase/isomerase "upper" segment of the pathway (ring activation and oxepin formation) to the "lower" segment (β-oxidation to acetyl-CoA and succinyl-CoA).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to this report |
|---|---|---|
| [21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/) | *Studies on the mechanism of ring hydrolysis in phenylacetate degradation: a metabolic branching point* | Primary biochemical characterization defining PaaZ's two catalytic domains, the two reactions (EC 3.3.2.12 and EC 1.2.1.91), the product 3-oxo-5,6-dehydrosuberyl-CoA, and the rationale for the fusion (preventing a dead-end cyclic aldehyde). Basis for Findings 1 and 2. |
| [20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/) | *Bacterial phenylalanine and phenylacetate catabolic pathway revealed* | Landmark elucidation of the full aerobic phenylacetate pathway (epoxidation → oxepin → hydrolytic ring cleavage → β-oxidation → acetyl-CoA + succinyl-CoA) in *E. coli* and *P. putida*, placing PaaZ's step in context. Basis for Finding 2. |
| [31511507](https://pubmed.ncbi.nlm.nih.gov/31511507/) | *Molecular basis for metabolite channeling in a ring opening enzyme of the phenylacetate degradation pathway* | Cryo-EM/SAXS/mutagenesis study revealing the trilobed trimer-of-dimers architecture and the electrostatic-pivoting channeling mechanism. Basis for Finding 3. |
| [17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/) | *Characterization of the last step of the aerobic phenylacetic acid degradation pathway* | Establishes succinyl-CoA as a final product of the pathway in *P. putida* and *E. coli*, defining the downstream fate of PaaZ's product. Supports Finding 2. |
| [9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/) | *Catabolism of phenylacetic acid in E. coli: a new aerobic hybrid pathway* | Defines the *paa* gene cluster organization, assigns PaaZ to the third enzymatic step, and establishes PaaX/phenylacetyl-CoA regulation. Basis for Finding 4. |
| [23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/) | *Taxis of P. putida F1 toward phenylacetic acid (Aer2)* | Demonstrates the physiological importance of PAA catabolism in *P. putida*, including chemotaxis via energy taxis. Supports Finding 4. |
| [33965615](https://pubmed.ncbi.nlm.nih.gov/33965615/) | *Engineering adipic acid metabolism in P. putida* | Shows the *paa* cluster's central role when the pathway is co-opted for medium-chain dicarboxylate (adipate) metabolism. Supports Finding 4. |
| [22582071](https://pubmed.ncbi.nlm.nih.gov/22582071/) | *Epoxy Coenzyme A Thioester pathways for degradation of aromatic compounds* | Review contextualizing the epoxide/oxepin CoA-thioester strategy of aerobic aromatic degradation (benzoate and phenylacetate). Supports the pathway framework. |
| [12189419](https://pubmed.ncbi.nlm.nih.gov/12189419/) | *Aerobic metabolism of phenylacetic acids in Azoarcus evansii* | Independent characterization of a conserved *paa* cluster (paaYZGHIKABCDE) and pathway in another proteobacterium, supporting the generality of the pathway. |
| [28153386](https://pubmed.ncbi.nlm.nih.gov/28153386/) | *Phenylacetaldehyde dehydrogenase from P. putida S12 styrene pathway* | Related aldehyde dehydrogenase in an upstream funneling route (styrene → phenylacetate), illustrating how aromatics feed into phenylacetyl-CoA. Contextual. |
| [12906358](https://pubmed.ncbi.nlm.nih.gov/12906358/) | *Design of catabolic cassettes for styrene biodegradation* | Demonstrates that styrene degradation funnels into phenylacetate/PAA metabolism, supporting the funneling role of the pathway. Contextual. |

**Consistency with UniProt/InterPro annotation.** The literature-derived functions align exactly with the target record: the two EC numbers (3.3.2.12 and 1.2.1.91), the bifunctional "oxepin-CoA hydrolase / 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase" description, the gene name *paaZ*, the locus PP_3270, and the InterPro domains (aldehyde dehydrogenase N/C domains and the HotDog superfamily that houses the MaoC hydratase). All verification criteria are satisfied.

---

## Supported and Refuted Hypotheses

**Supported:**
- PaaZ (Q88HT3/PP_3270) is a bifunctional oxepin-CoA hydrolase (EC 3.3.2.12) + NADP⁺-dependent aldehyde dehydrogenase (EC 1.2.1.91). ✔ ([PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/))
- Its substrate is the pathway-specific oxepin-CoA; its product is 3-oxo-5,6-dehydrosuberyl-CoA. ✔ ([PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/), [PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/))
- It performs the ring-cleavage (third) step of the aerobic *paa* pathway, upstream of β-oxidation to succinyl-CoA/acetyl-CoA. ✔ ([PMID: 9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/), [PMID: 17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/))
- It is a cytoplasmic trimer-of-dimers that channels its intermediate via electrostatic pivoting. ✔ ([PMID: 31511507](https://pubmed.ncbi.nlm.nih.gov/31511507/))
- The fusion prevents accumulation of a toxic cyclic dead-end product. ✔ ([PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/))

**Refuted / ruled out:**
- PaaZ is **not** an oxygenolytic ring-cleavage enzyme; ring opening is **hydrolytic** (non-oxygenolytic). ([PMID: 20660314](https://pubmed.ncbi.nlm.nih.gov/20660314/), [PMID: 21296885](https://pubmed.ncbi.nlm.nih.gov/21296885/))
- The gene symbol is **not** ambiguous here; all evidence converges on a single, well-defined enzyme.

---

## Limitations and Knowledge Gaps

1. **Direct enzymology on the *P. putida* KT2440 ortholog is limited.** The definitive biochemical (Teufel et al.) and structural (Sathyanarayanan et al.) work was performed largely on PaaZ orthologs (notably from *E. coli* and related systems). Function is assigned to Q88HT3 by strong sequence/domain homology, identical EC annotations, and conserved pathway organization rather than by direct kinetic characterization of the KT2440 protein itself. Strain-specific kinetic parameters (kcat, Km for oxepin-CoA) were not located.

2. **Cofactor specificity nuance.** The dehydrogenase domain is NADP⁺-dependent; the strictness of NADP⁺ vs. NAD⁺ preference and its regulatory implications for the KT2440 enzyme are not experimentally quantified here.

3. **Localization is inferred, not measured.** The cytoplasmic assignment follows logically from the soluble CoA-thioester substrates and the absence of targeting/membrane domains, but no direct fractionation or imaging evidence for Q88HT3 was examined.

4. **Regulatory details in *P. putida*.** PaaX/phenylacetyl-CoA regulation is best characterized in *E. coli*. The precise promoter architecture and operon boundaries around PP_3270 in KT2440 were not directly verified.

5. **Channeling residue conservation.** The electrostatic-pivoting mechanism was demonstrated for a specific ortholog; residue-level validation in the KT2440 sequence would confirm identical implementation.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biochemical characterization of Q88HT3.** Heterologously express and purify the KT2440 PaaZ; measure steady-state kinetics for oxepin-CoA hydrolysis and aldehyde oxidation, confirm the NADP⁺ preference, and verify the 3-oxo-5,6-dehydrosuberyl-CoA product by LC-MS.

2. **Genetic knockout / complementation in KT2440.** Delete PP_3270 and test loss of growth on phenylacetate (and on funneling substrates such as phenylalanine, 2-phenylethylamine, styrene); complement in trans. Assess accumulation of the predicted dead-end cyclic aldehyde derivative in the mutant by metabolomics.

3. **Localization confirmation.** Use cell fractionation and/or a fluorescent fusion to confirm cytoplasmic localization of PP_3270.

4. **Structural validation.** Solve or predict (AlphaFold/cryo-EM) the KT2440 PaaZ structure, confirm the trilobed trimer-of-dimers assembly, and test key conserved basic residues implicated in electrostatic CoA pivoting via site-directed mutagenesis and channeling assays.

5. **Regulatory mapping.** Define the *paaZ* (PP_3270) promoter and PaaX binding site in KT2440; confirm induction by phenylacetyl-CoA using reporter fusions.

6. **Applied metabolic engineering.** Given the demonstrated co-option of the *paa* cluster for adipate/dicarboxylate metabolism, systematically test PaaZ variants for expanded substrate scope toward plastic-monomer dicarboxylates, informing bio-upcycling strain design.

---

*Report generated for target gene paaZ (UniProt Q88HT3, locus PP_3270) in* Pseudomonas putida *KT2440. All functional claims are attributed to the primary and review literature cited above; annotation-database attributes (EC numbers, InterPro domains) were cross-checked against and found consistent with the experimental literature.*


## Artifacts

- [OpenScientist final report](paaZ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaZ-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:21296885
2. PMID:20660314
3. PMID:17259607
4. PMID:31511507
5. PMID:9748275
6. PMID:12189419
7. PMID:23377939
8. PMID:33965615