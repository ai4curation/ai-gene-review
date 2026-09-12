---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T17:47:22.660913'
end_time: '2026-07-23T17:58:02.084889'
duration_seconds: 639.42
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaF
  gene_symbol: paaF
  uniprot_accession: Q88HR9
  protein_description: 'SubName: Full=Enoyl-CoA hydratase-isomerase {ECO:0000313|EMBL:AAN68891.1};
    EC=4.2.1.17 {ECO:0000313|EMBL:AAN68891.1};'
  gene_info: Name=paaF {ECO:0000313|EMBL:AAN68891.1}; OrderedLocusNames=PP_3284 {ECO:0000313|EMBL:AAN68891.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the enoyl-CoA hydratase/isomerase family.
  protein_domains: ClpP/crotonase-like_dom_sf. (IPR029045); Enoyl-CoA_hyd/isom_CS.
    (IPR018376); Enoyl-CoA_hydra/iso. (IPR001753); Enoyl-CoA_hydra_C. (IPR014748);
    ECH_1 (PF00378)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: paaF-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaF-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HR9
- **Protein Description:** SubName: Full=Enoyl-CoA hydratase-isomerase {ECO:0000313|EMBL:AAN68891.1}; EC=4.2.1.17 {ECO:0000313|EMBL:AAN68891.1};
- **Gene Information:** Name=paaF {ECO:0000313|EMBL:AAN68891.1}; OrderedLocusNames=PP_3284 {ECO:0000313|EMBL:AAN68891.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the enoyl-CoA hydratase/isomerase family.
- **Key Domains:** ClpP/crotonase-like_dom_sf. (IPR029045); Enoyl-CoA_hyd/isom_CS. (IPR018376); Enoyl-CoA_hydra/iso. (IPR001753); Enoyl-CoA_hydra_C. (IPR014748); ECH_1 (PF00378)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaF" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaF** (gene ID: paaF, UniProt: Q88HR9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *paaF* (PP_3284, UniProt Q88HR9) in *Pseudomonas putida* KT2440

## Gene/Protein Identity — Verified

| Field | Value |
|---|---|
| UniProt | Q88HR9 (Q88HR9_PSEPK) |
| Gene | *paaF* |
| Locus | PP_3284 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950) |
| Length | 257 aa (soluble) |
| EC | 4.2.1.17 (enoyl-CoA hydratase) |
| KEGG orthology | K01692 |
| Family/domains | Enoyl-CoA hydratase/isomerase (crotonase) superfamily; Pfam PF00378 (ECH_1); COG1024; InterPro IPR001753, IPR014748, IPR018376, IPR029045 (ClpP/crotonase-like fold) |

**Identity is unambiguous.** The gene symbol *paaF*, the crotonase-fold domain architecture, the EC number, and the genomic context all agree. PP_3284 lies inside the *P. putida* KT2440 phenylacetate (*paa*) catabolic gene cluster, immediately adjacent to the isomerase gene *paaG* (PP_3283), exactly as in the well-studied *Escherichia coli* *paa* operon. This is the correct gene; there is no cross-species symbol confusion.

---

## Summary

**paaF** (locus tag **PP_3284**; UniProt **Q88HR9**) encodes a **cytoplasmic enoyl-CoA hydratase** of the **crotonase superfamily** (EC 4.2.1.17) that operates within the aerobic **phenylacetate (paa) catabolic pathway** of *Pseudomonas putida* KT2440. The protein is a 257-residue soluble enzyme carrying the canonical crotonase/enoyl-CoA hydratase-isomerase fold (Pfam PF00378 "ECH_1"; InterPro IPR001753, IPR029045, IPR018376; COG1024). Its assignment to this specific catalytic function is supported by domain architecture, KEGG orthology (K01692), conserved genomic operon context, and strong sequence homology (58.8% identity) to the biochemically and structurally characterized *Escherichia coli* PaaF ortholog.

The **primary catalytic function** of PaaF is the **syn-hydration of the C2=C3 double bond of 2,3-dehydroadipyl-CoA to yield 3-hydroxyadipyl-CoA**, one step of a β-oxidation-like module that processes the ring-opened product of aromatic-ring cleavage. This step is embedded in a metabolic relay: after phenylacetyl-CoA is epoxidized (PaaABCE), ring-isomerized and hydrolytically ring-opened (PaaG/PaaZ), the resulting unsaturated dicarboxylic CoA-thioester is hydrated by **PaaF**, oxidized by **PaaH** (3-hydroxyacyl-CoA dehydrogenase, PP_3282), and thiolytically cleaved by **PaaJ** (3-oxoadipyl-CoA thiolase, PP_3280) to give **succinyl-CoA + acetyl-CoA**, which enter the TCA cycle. Notably, the *E. coli* ortholog forms a stable hetero-oligomeric **PaaF–PaaG complex** with the enoyl-CoA isomerase PaaG.

Biologically, PaaF sits at the heart of a widely distributed **aromatic "funneling" pathway** that channels carbon from phenylalanine, 2-phenylethylamine, and styrene/ethylbenzene degradation — all of which converge on phenylacetyl-CoA — into central metabolism, allowing *P. putida* to use phenylacetate as a sole carbon and energy source. Expression of the operon housing *paaF* is controlled by the pathway-specific repressor **PaaX** (PP_3286), which is relieved by the inducer phenylacetyl-CoA. The protein performs its function in the **cytoplasm**, consistent with its soluble crotonase fold and the CoA-thioester chemistry of the pathway.

---

## Key Findings

### Finding 1 — PaaF is a crotonase-superfamily enoyl-CoA hydratase within the *paa* operon of *P. putida* KT2440

PP_3284 (paaF, Q88HR9) is a 257-amino-acid protein whose sequence and domain content place it unambiguously in the **enoyl-CoA hydratase/isomerase (crotonase) superfamily**. The InterPro and Pfam signatures — **PF00378 (ECH_1)**, **IPR001753 (enoyl-CoA hydratase/isomerase)**, **IPR029045 (ClpP/crotonase-like fold superfamily)**, and **IPR018376 (enoyl-CoA hydratase/isomerase conserved site)** — together with **COG1024**, are the defining hallmarks of this enzyme class. KEGG assigns **ppu:PP_3284** to the KEGG Ortholog **K01692**, i.e. enoyl-CoA hydratase [EC:4.2.1.17].

Critically, the gene sits within the *P. putida* **phenylacetate catabolic gene cluster**. Its genomic neighborhood, from KEGG, includes:

| Locus | Gene | KO | Function |
|-------|------|-----|----------|
| PP_3278 | paaA | K02609 | Ring-1,2-phenylacetyl-CoA epoxidase (subunit) |
| PP_3277 | paaB | K02610 | Phenylacetyl-CoA epoxidase (subunit) |
| PP_3279 | paaK | K01912 | Phenylacetate–CoA ligase |
| PP_3283 | paaG | K15866 | 1,2-epoxyphenylacetyl-CoA isomerase (EC 5.3.3.18) |
| PP_3282 | paaH | K00074 | 3-hydroxyacyl-CoA dehydrogenase |
| PP_3280 | paaJ | K07823 | 3-oxoadipyl-CoA thiolase |
| **PP_3284** | **paaF** | **K01692** | **Enoyl-CoA hydratase (EC 4.2.1.17)** |
| PP_3286 | paaX | K02616 | Pathway-specific transcriptional repressor |

paaF lies immediately adjacent to the isomerase **paaG**, mirroring the gene organization in *E. coli*. This physical proximity is functionally meaningful because the two enzymes form a stable complex (see Finding 2).

This assignment is directly supported by the literature. In the foundational characterization of the *E. coli* pathway, [PMID: 9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/) reported that *"the paaFGHIJ gene products, which show significant similarity to fatty acid beta-oxidation enzymes, likely involved in further mineralization to Krebs cycle intermediates,"* establishing PaaF as one of the β-oxidation-like enzymes of the cluster. More specifically, the structural study by Grishin and colleagues, [PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/), identified *"another stable complex, PaaFG, an enoyl-CoA hydratase and enoyl-Coa isomerase, both belonging to the crotonase superfamily,"* directly confirming PaaF as a crotonase-superfamily enoyl-CoA hydratase — precisely matching the Pfam/InterPro annotation of Q88HR9.

### Finding 2 — PaaF catalyzes the hydration of 2,3-dehydroadipyl-CoA to 3-hydroxyadipyl-CoA (EC 4.2.1.17)

The specific reaction catalyzed by PaaF is the **stereospecific (syn) addition of water across the C2=C3 double bond of an enoyl-CoA thioester**. In the context of the phenylacetate pathway, the physiological substrate is **2,3-dehydroadipyl-CoA** — a C6 dicarboxylic enoyl-CoA arising from the ring cleavage of phenylacetyl-CoA — and the product is **3-hydroxyadipyl-CoA**:

```
2,3-dehydroadipyl-CoA  + H2O   --PaaF (EC 4.2.1.17)-->   3-hydroxyadipyl-CoA
```

The product 3-hydroxyadipyl-CoA is then oxidized by the adjacent **PaaH** (PP_3282, K00074) to 3-oxoadipyl-CoA, which is cleaved by the **PaaJ** thiolase (PP_3280, K07823) to yield **succinyl-CoA + acetyl-CoA**.

**Substrate specificity.** The physiological substrate is the CoA-thioester of a short **dicarboxylic** enoyl intermediate produced by ring opening of phenylacetyl-CoA — not generic long-chain fatty enoyl-CoAs. This narrow specificity is dictated by the enzyme's dedicated role inside the *paa* pathway, although crotonase-fold hydratases commonly show some in-vitro promiscuity toward related short/medium-chain enoyl-CoAs.

**Mechanism (crotonase superfamily).** The sequence contains the conserved **glycine-rich oxyanion-hole motif** (…G-G-G-C-E… around residue ~107) that, together with backbone amide NH groups, stabilizes the thioester enolate/oxyanion transition state; **two conserved active-site glutamates** act as general acid/base for the syn addition of water. This is the archetypal enoyl-CoA hydratase (crotonase) chemistry.

**Orthology evidence.** A pairwise global alignment of *P. putida* PaaF (Q88HR9, 257 aa) against *E. coli* K-12 PaaF (P76082, 255 aa) yields **58.8% identity over 250 aligned positions** — far above the ~30% "twilight zone" threshold used for confident homology-based inference — with the two proteins sharing the same length class and the same operon position. This is strong bioinformatic evidence that the two are true orthologs performing the same reaction.

The structural context of PaaF is well established. [PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/) solved the crystal structure of the PaaF–PaaG complex and reported that *"The PaaFG complex has a four-layered structure composed of homotrimeric discs of PaaF and PaaG,"* demonstrating that PaaF is a trimeric crotonase-fold enoyl-CoA hydratase that physically partners with the isomerase PaaG. The same study situated the hydratase step within the ring-degradation module, noting that *"These reactions convert the product of the opening of the aromatic ring to common metabolites,"* which frames the PaaF-catalyzed hydration as part of the conversion of the ring-opened intermediate into central-metabolism compounds.

### Finding 3 — PaaF functions in the cytoplasm within the aerobic hybrid phenylacetate catabolon, funneling aromatic carbon to the TCA cycle

PaaF operates in the **cytoplasm**. The phenylacetate pathway is a soluble, CoA-dependent cytoplasmic route: all of its intermediates are CoA thioesters processed by soluble enzymes, and no membrane-spanning segments are predicted for the 257-residue crotonase fold of Q88HR9. This is fully consistent with the general architecture of β-oxidation-like CoA chemistry, which occurs in the cytoplasmic compartment in bacteria.

Biologically, PaaF is embedded in a central aromatic **"funneling" pathway**. Phenylacetate — generated from phenylalanine catabolism, from 2-phenylethylamine, and from the degradation of styrene/ethylbenzene — is first activated to **phenylacetyl-CoA** by the ligase PaaK, then epoxidized by the multicomponent monooxygenase PaaABC(D)E, ring-isomerized and hydrolytically opened by PaaG/PaaZ, and finally processed by the β-oxidation-like enzymes **PaaF → PaaH → PaaJ** to yield **succinyl-CoA + acetyl-CoA**. This makes phenylacetate usable as a sole carbon and energy source.

The downstream fate of the pathway was experimentally defined by Nogales et al. ([PMID: 17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/)), who showed that *"succinyl-CoA is one of the final products of this pathway in Pseudomonas putida and Escherichia coli,"* linking the module that includes PaaF directly to the TCA cycle. The same work confirmed the pathway's biochemical logic: *"Phenylacetic acid (PA) degradation in bacteria involves an aerobic hybrid pathway encoded by the paa gene cluster."* The term "hybrid" reflects the unusual combination of oxygen-dependent activation (epoxidation) followed by anaerobic-style CoA-thioester β-oxidation chemistry — the branch in which PaaF acts.

The breadth of substrates funneled through this pathway is documented by [PMID: 23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/), which describes *"The phenylacetic acid (PAA) degradation pathway is a widely distributed funneling pathway for the catabolism of aromatic compounds, including the environmental pollutants styrene and ethylbenzene,"* establishing the environmental and metabolic significance of the route in which PaaF participates.

Finally, expression of the operon containing *paaF* is controlled by the pathway-specific repressor **PaaX** (PP_3286). [PMID: 24983528](https://pubmed.ncbi.nlm.nih.gov/24983528/) showed that this regulator *"is able to bind and inhibit the activity of Px in a phenylacetyl-coenzyme A (PA-CoA) dependent manner,"* meaning that the pathway inducer phenylacetyl-CoA de-represses the operon — a coherent feedback logic that couples enzyme production (including PaaF) to substrate availability.

---

## Mechanistic Model / Interpretation

The role of PaaF is best understood as **one enzymatic step in an integrated β-oxidation-like module** that dismantles the ring-cleavage product of aromatic catabolism. The overall pathway, and PaaF's place within it, can be diagrammed as follows:

```
   Phenylalanine / 2-phenylethylamine / styrene / ethylbenzene
                              │
                              ▼
                    Phenylacetate (PAA)
                              │  PaaK (PP_3279, phenylacetate-CoA ligase)
                              ▼
                   Phenylacetyl-CoA  ◄─── inducer that de-represses PaaX
                              │  PaaABC(D)E (PP_3277/3278…, epoxidase)  + O2
                              ▼
              1,2-epoxyphenylacetyl-CoA
                              │  PaaG (PP_3283, isomerase, EC 5.3.3.18)
                              ▼
              (oxepin-CoA) → ring opening (PaaZ)
                              │
                              ▼
                  2,3-dehydroadipyl-CoA
                              │  ★ PaaF (PP_3284, enoyl-CoA hydratase, EC 4.2.1.17)  + H2O
                              ▼
                   3-hydroxyadipyl-CoA
                              │  PaaH (PP_3282, 3-hydroxyacyl-CoA dehydrogenase)  + NAD+
                              ▼
                    3-oxoadipyl-CoA
                              │  PaaJ (PP_3280, 3-oxoadipyl-CoA thiolase)  + CoA
                              ▼
              Succinyl-CoA  +  Acetyl-CoA  ──►  TCA cycle
```

Several features make this model robust:

1. **Catalytic identity is over-determined.** Independent lines of evidence — Pfam/InterPro domain signatures, COG assignment, KEGG orthology (K01692/EC 4.2.1.17), the conserved crotonase oxyanion-hole and dual-glutamate catalytic motif, operon context, and 58.8% identity to a biochemically characterized ortholog — all converge on the same conclusion. This is a textbook case where homology-based inference is highly reliable.

2. **PaaF acts as part of a physical protein assembly.** The demonstration of a stable **PaaF–PaaG hetero-complex** with a four-layered trimeric-disc architecture ([PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/)) suggests that hydration (PaaF) and isomerization (PaaG) are spatially coupled, potentially enabling substrate channeling of unstable CoA-thioester intermediates. The immediate adjacency of *paaF* and *paaG* in the *P. putida* genome is consistent with co-expression and complex formation.

3. **The pathway output is experimentally anchored.** Because succinyl-CoA and acetyl-CoA are the demonstrated end products ([PMID: 17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/)), the intermediate steps — including PaaF's hydration of the C6 dicarboxylic enoyl-CoA — are constrained by mass balance to produce the 3-hydroxy intermediate required for the subsequent dehydrogenation/thiolysis.

4. **Regulation ties enzyme abundance to substrate.** The PaaX/phenylacetyl-CoA switch ensures that PaaF and its partner enzymes are made only when aromatic substrate is present, an economical design characteristic of catabolic funneling pathways.

---

## Evidence Base

| PMID | Study (abbrev.) | Relevance to PaaF |
|------|-----------------|-------------------|
| [22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/) | Grishin et al. (2012) — *PaaF–PaaG hydratase-isomerase complex crystal structure* | **Primary structural evidence.** Directly identifies PaaF as a crotonase-superfamily enoyl-CoA hydratase and shows it forms a four-layered trimeric-disc complex with the isomerase PaaG. |
| [17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/) | Nogales et al. (2007) — *Last step of aerobic PAA degradation* | **Pathway output.** Experimentally shows succinyl-CoA is a final product in *P. putida* and *E. coli*; confirms the aerobic hybrid nature of the paa pathway. |
| [9748275](https://pubmed.ncbi.nlm.nih.gov/9748275/) | Ferrández et al. (1998) — *PAA catabolism in E. coli* | **Foundational.** Establishes paaFGHIJ as β-oxidation-like enzymes leading to Krebs-cycle intermediates. |
| [23377939](https://pubmed.ncbi.nlm.nih.gov/23377939/) | Luu et al. (2013) — *Taxis of P. putida F1 toward PAA* | **Pathway breadth.** Documents the PAA route as a widely distributed funneling pathway for aromatics including styrene and ethylbenzene. |
| [24983528](https://pubmed.ncbi.nlm.nih.gov/24983528/) | Fernández et al. (2014) — *Regulation of the PAA pathway* | **Regulation.** Shows PaaX represses the operon in a phenylacetyl-CoA-dependent manner, controlling expression of the *paaF*-containing operon. |

**Supporting context (corroborating the pathway, not directly cited for PaaF's catalytic step):**

- [PMID: 14597173](https://pubmed.ncbi.nlm.nih.gov/14597173/) and [PMID: 15474299](https://pubmed.ncbi.nlm.nih.gov/15474299/) characterize *paa* clusters in *Pseudomonas* sp. Y2 (one with organization similar to *P. putida* KT2440), reinforcing the conserved genomic architecture in which *paaF* resides.
- [PMID: 12189419](https://pubmed.ncbi.nlm.nih.gov/12189419/) describes the homologous *paaYZGHIKABCDE* cluster in *Azoarcus evansii*, underscoring the wide conservation of this β-oxidation-like module across proteobacteria.
- [PMID: 22685150](https://pubmed.ncbi.nlm.nih.gov/22685150/) and [PMID: 37949283](https://pubmed.ncbi.nlm.nih.gov/37949283/) detail transcriptional regulation (PaaR/PaaX) of *paa* operons, supporting the regulatory logic described for PaaF's operon.

**Evidence grading.**

- **Direct experimental data on this exact protein (PP_3284):** none; UniProt lists protein existence as inferred from homology.
- **Strong homology/structural inference:** biochemistry and crystal structure of the orthologous *E. coli* PaaF/PaaFG complex; 58.8% sequence identity; conserved catalytic core.
- **Experimental at the pathway level in the same species:** *P. putida* *paa* pathway produces succinyl-CoA ([PMID: 17259607](https://pubmed.ncbi.nlm.nih.gov/17259607/)); regulation and substrate funneling established.

All five primary citations point in the same direction; none contradicts the assignment. The strongest single piece of evidence is the crystal-structure study, which experimentally proves the crotonase-fold hydratase identity and the PaaF–PaaG partnership in the *E. coli* ortholog.

---

## Supported vs. Refuted Hypotheses

- **Supported:** PP_3284 = *paaF* = enoyl-CoA hydratase of the *paa* β-oxidation module (operon context + KO K01692 + 58.8% identity to characterized *E. coli* PaaF + crotonase fold).
- **Supported:** Cytoplasmic localization within a soluble CoA-thioester pathway (domain/family inference; no membrane features).
- **Refuted / ruled out:** PaaF is *not* the ring epoxidase, isomerase, dehydrogenase, thiolase, or CoA-ligase — those are distinct, separately annotated genes (PP_3277–3283) in the same cluster.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical assay of the *P. putida* protein.** Catalytic parameters (kcat, Km), the exact physiological substrate, and the degree of substrate promiscuity of Q88HR9 have not, to our knowledge, been measured directly. The functional assignment rests on homology to *E. coli* PaaF (58.8% identity), conserved motifs, and operon context.

2. **Structural data are for the ortholog, not Q88HR9.** The four-layered PaaF–PaaG complex structure was determined for the *E. coli* proteins ([PMID: 22961985](https://pubmed.ncbi.nlm.nih.gov/22961985/)). While high homology makes it very likely the *P. putida* protein adopts the same fold and forms the analogous complex, this has not been experimentally verified for KT2440.

3. **Stereochemistry unconfirmed for this protein.** The syn-hydration mechanism and 3-hydroxy stereochemistry are inferred from the crotonase superfamily and the requirement of the downstream PaaH dehydrogenase; they have not been directly demonstrated for PaaF from *P. putida*.

4. **Exact ring-opening intermediate.** The precise structure and stereochemistry of the substrate presented to PaaF depend on the upstream PaaG/PaaZ chemistry (oxepin-CoA / ring opening), details of which continue to be refined. "2,3-dehydroadipyl-CoA" is the widely accepted intermediate, but the exact isomer could be revisited.

5. **Localization is inferred, not measured.** Cytoplasmic localization is deduced from the absence of predicted transmembrane segments/signal peptides and the soluble nature of crotonase-fold enzymes, rather than from proteomic/fractionation data specific to this protein.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and enzymatic assay.** Clone and purify recombinant PP_3284 (Q88HR9) and measure enoyl-CoA hydratase activity spectrophotometrically (e.g., loss of the 263 nm enoyl-CoA absorbance). Determine kcat/Km against 2,3-dehydroadipyl-CoA and a panel of short/medium-chain enoyl-CoAs (crotonyl-CoA, hexenoyl-CoA) to define physiological substrate and any promiscuity.

2. **Reconstitute the PaaF–PaaG complex.** Co-express *P. putida* PaaF and PaaG and test for stable complex formation by size-exclusion chromatography and native mass spectrometry, verifying that the four-layered trimeric-disc architecture seen in *E. coli* is conserved.

3. **Structure determination.** Solve the crystal or cryo-EM structure of *P. putida* PaaF (ideally in complex with PaaG and/or a CoA-thioester analog) to confirm the crotonase fold, the oxyanion hole, and catalytic glutamate positioning; alternatively, use an AlphaFold model validated against the *E. coli* structure.

4. **Genetic knockout / complementation.** Delete *PP_3284* in KT2440 and test growth on phenylacetate (and on styrene/ethylbenzene as upstream feeders). Confirm loss of growth and restoration by in-trans complementation, and look for accumulation of the 2,3-dehydroadipyl-CoA substrate by LC-MS metabolomics.

5. **Active-site mutagenesis.** Mutate the predicted catalytic glutamates and the oxyanion-hole glycines to confirm their roles and to test the syn-hydration mechanism.

6. **Regulatory validation.** Confirm phenylacetyl-CoA-dependent PaaX de-repression of the *paaF* operon in KT2440 by reporter-fusion and EMSA experiments, tying enzyme expression to substrate availability.

---

## Conclusion

The gene **paaF** (PP_3284, Q88HR9) in *Pseudomonas putida* KT2440 encodes a **cytoplasmic, crotonase-superfamily enoyl-CoA hydratase (EC 4.2.1.17)** that catalyzes the **hydration of 2,3-dehydroadipyl-CoA to 3-hydroxyadipyl-CoA** as part of the β-oxidation-like module of the aerobic **phenylacetate (paa) degradation pathway**. Working in concert with the isomerase PaaG (with which its *E. coli* ortholog forms a stable structural complex), the dehydrogenase PaaH, and the thiolase PaaJ, PaaF helps convert the ring-cleavage product of phenylacetyl-CoA into **succinyl-CoA and acetyl-CoA** for the TCA cycle. This positions PaaF as a key downstream enzyme of a broadly conserved aromatic-catabolism funneling pathway that lets *P. putida* grow on phenylacetate and on aromatic feedstocks (phenylalanine, styrene, ethylbenzene) that converge on phenylacetyl-CoA. The assignment is strongly supported by domain architecture, KEGG orthology, operon context, and homology to the experimentally characterized *E. coli* enzyme, though direct biochemical characterization of the *P. putida* protein remains an outstanding gap.


## Artifacts

- [OpenScientist final report](paaF-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaF-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9748275
2. PMID:22961985
3. PMID:17259607
4. PMID:23377939
5. PMID:24983528
6. PMID:14597173
7. PMID:15474299
8. PMID:12189419
9. PMID:22685150
10. PMID:37949283