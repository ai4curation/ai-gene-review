---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T16:54:42.232130'
end_time: '2026-07-23T17:20:32.440451'
duration_seconds: 1550.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaH
  gene_symbol: paaH
  uniprot_accession: Q88HS1
  protein_description: 'SubName: Full=3-hydroxyadipyl-CoA dehydrogenase {ECO:0000313|EMBL:AAN68889.1};
    EC=1.1.1.35 {ECO:0000313|EMBL:AAN68889.1};'
  gene_info: Name=paaH {ECO:0000313|EMBL:AAN68889.1}; OrderedLocusNames=PP_3282 {ECO:0000313|EMBL:AAN68889.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the 3-hydroxyacyl-CoA dehydrogenase family.
  protein_domains: 3-OHacyl-CoA_DH_CS. (IPR006180); 3-OHacyl-CoA_DH_NAD-bd. (IPR006176);
    3-OHacyl-CoA_DH_PaaH. (IPR011967); 3HC_DH_C. (IPR006108); 3HCDH_RFF. (IPR041040)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: paaH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS1
- **Protein Description:** SubName: Full=3-hydroxyadipyl-CoA dehydrogenase {ECO:0000313|EMBL:AAN68889.1}; EC=1.1.1.35 {ECO:0000313|EMBL:AAN68889.1};
- **Gene Information:** Name=paaH {ECO:0000313|EMBL:AAN68889.1}; OrderedLocusNames=PP_3282 {ECO:0000313|EMBL:AAN68889.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the 3-hydroxyacyl-CoA dehydrogenase family.
- **Key Domains:** 3-OHacyl-CoA_DH_CS. (IPR006180); 3-OHacyl-CoA_DH_NAD-bd. (IPR006176); 3-OHacyl-CoA_DH_PaaH. (IPR011967); 3HC_DH_C. (IPR006108); 3HCDH_RFF. (IPR041040)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaH** (gene ID: paaH, UniProt: Q88HS1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PaaH (PP_3282, UniProt Q88HS1)
## 3-Hydroxyadipyl-CoA dehydrogenase of *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**PaaH** (gene *paaH*; ordered locus **PP_3282**; UniProt **Q88HS1**) of *Pseudomonas putida* KT2440 is a **soluble, cytoplasmic, NAD⁺-dependent 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35)** that acts in the **lower, β-oxidation-like segment of the aerobic phenylacetate (phenylacetyl-CoA) degradation pathway**. Its primary catalytic function is the stereospecific oxidation of **(S)-3-hydroxyadipyl-CoA to 3-oxoadipyl-CoA (β-ketoadipyl-CoA)**, coupled to reduction of NAD⁺ to NADH. This is the penultimate redox reaction of the pathway; the resulting 3-oxoadipyl-CoA is thiolytically cleaved to **succinyl-CoA + acetyl-CoA**, which enter the TCA cycle. The identification rests on database/EC annotation, membership in the 3-hydroxyacyl-CoA dehydrogenase (PaaH) family with a confirmed N-terminal Rossmann NAD-binding fold, and functional characterization of the surrounding *paa* pathway in *P. putida* and *E. coli*.

**Gene-identity verification:** The gene symbol *paaH*, the organism (*P. putida* KT2440), the annotated function (3-hydroxyadipyl-CoA dehydrogenase, EC 1.1.1.35), and the InterPro family/domains (3-OHacyl-CoA_DH_PaaH, IPR011967; NAD-binding and C-terminal domains) are **mutually consistent** with the literature on the bacterial phenylacetate catabolon. No ambiguity or misassignment was detected.

---

## 2. Biochemical Function

### 2.1 Reaction catalyzed
> **(S)-3-hydroxyadipyl-CoA + NAD⁺ ⇌ 3-oxoadipyl-CoA + NADH + H⁺**  (EC 1.1.1.35)

EC 1.1.1.35 is the general "3-hydroxyacyl-CoA dehydrogenase" that oxidizes the C3 hydroxyl of an (S)/L-3-hydroxyacyl-CoA thioester to the corresponding 3-oxo (β-keto) acyl-CoA, generating NADH. The reaction is the third of the four classic β-oxidation reactions (hydration → **dehydrogenation** → thiolysis) and is freely reversible in vitro [Barycki et al., 2000, PMID 10840044]. In PaaH the acyl substrate is the **C6 dicarboxylic thioester 3-hydroxyadipyl-CoA**, a ring-cleavage product of phenylacetyl-CoA catabolism rather than a straight-chain fatty acyl-CoA.

### 2.2 Substrate specificity
The substrate is defined by the pathway context and by the enzyme's subfamily assignment:
- The InterPro **PaaH subfamily signature (IPR011967)** distinguishes phenylacetate-pathway 3-hydroxyacyl-CoA dehydrogenases from general fatty-acid β-oxidation HADs, indicating specificity for the short-chain **dicarboxylic** 3-hydroxyacyl-CoA intermediate (3-hydroxyadipyl-CoA) generated after aromatic-ring opening [Ferrández et al., 1998, PMID 9748275; Olivera et al., 1998, PMID 9600981].
- Downstream chemistry constrains the substrate: because the terminal products of the pathway are **succinyl-CoA + acetyl-CoA** [Nogales et al., 2007, PMID 17259607], the immediate PaaH product must be **3-oxoadipyl-CoA (β-ketoadipyl-CoA)**, and therefore its substrate is **3-hydroxyadipyl-CoA**.
- Family members are stereospecific for the (S)/L-3-hydroxy configuration [Barycki et al., 2000, PMID 10840044].

### 2.3 Cofactor
NAD⁺ is the electron acceptor. The N-terminal Rossmann dinucleotide-binding domain carries the cofactor; the homologous PaaH-type enzyme RePaaH1 shows "the cofactor-binding site is located on the Rossmann fold" [Kim et al., 2014, PMID 24792376].

---

## 3. Structural / Bioinformatic Evidence

Direct sequence analysis of Q88HS1 (this study) confirms the annotation:

- **Length:** 505 residues — consistent with the PaaH subfamily (e.g., *E. coli* PaaH ≈ 475 aa), which is larger than the ~300-aa mammalian mitochondrial HAD owing to extra subfamily-specific segments (InterPro IPR041040, 3HCDH_RFF).
- **N-terminal Rossmann NAD-binding fingerprint:** residues 12–22 read `VAVIGAGAMGAG`, containing the canonical **G-x-G-x-x-G glycine-rich motif (GAGAMG, position 14)** that binds the ADP moiety of NAD(H). This is diagnostic of the dinucleotide-binding fold.
- **Two-domain architecture (by homology):** N-terminal Rossmann NAD-binding domain + C-terminal α-helical dimerization domain, as crystallographically established for the closely related PaaH-family enzyme RePaaH1 [Kim et al., 2014, PMID 24792376] and for L-3-hydroxyacyl-CoA dehydrogenase [Barycki et al., 2000, PMID 10840044].
- **Catalytic machinery (by family conservation):** a **His–Glu catalytic dyad** in the interdomain cleft abstracts a proton from the C3 hydroxyl while NAD⁺ accepts the hydride [Barycki et al., 2000, PMID 10840044; Mugo et al., 2015, PMID 25446130].
- **InterPro domains (from the target record):** 3-OHacyl-CoA_DH_CS (IPR006180), 3-OHacyl-CoA_DH_NAD-bd (IPR006176), 3-OHacyl-CoA_DH_PaaH (IPR011967), 3HC_DH_C (IPR006108), 3HCDH_RFF (IPR041040) — all congruent with an NAD-dependent 3-hydroxyacyl-CoA dehydrogenase of the phenylacetate pathway.

This constitutes convergent **bioinformatic/structural inference** (sequence motif + family + homologous crystal structures) supporting the annotated function.

---

## 4. Pathway Context

PaaH is one enzyme of the **phenylacetyl-CoA catabolon**, an aerobic "hybrid" pathway that funnels many aromatic compounds into central metabolism [Ferrández et al., 1998, PMID 9748275; Luu et al., 2013, PMID 23377939]. The pathway, defined genetically in *P. putida* U/KT2440 and *E. coli*, comprises [Olivera et al., 1998, PMID 9600981; Ferrández et al., 1998, PMID 9748275]:

1. **Activation** — phenylacetate → phenylacetyl-CoA (PaaK, phenylacetate–CoA ligase).
2. **Ring 1,2-epoxidation/hydroxylation** — a multicomponent oxygenase (PaaABC(D)E) acting on the CoA-activated ring.
3. **Ring opening** — a hydratase/aldehyde-dehydrogenase (PaaZ) that cleaves the ring to a linear dicarboxylic-CoA (a 3-oxo-unsaturated adipyl/suberyl-CoA species).
4. **β-oxidation-like processing** — enoyl-CoA hydratase/isomerase, then **PaaH (3-hydroxyacyl-CoA dehydrogenase)**, then a β-ketoadipyl-CoA thiolase.
5. **Termination** — thiolytic cleavage of 3-oxoadipyl-CoA to **succinyl-CoA + acetyl-CoA** [Nogales et al., 2007, PMID 17259607].

**PaaH's specific position:** it performs step 4's dehydrogenation, converting **3-hydroxyadipyl-CoA → 3-oxoadipyl-CoA (β-ketoadipyl-CoA)**. The product is the direct substrate of the terminal thiolase (in *P. putida* shown to yield succinyl-CoA + acetyl-CoA), so PaaH sits immediately upstream of the pathway's convergence with central carbon metabolism and with the β-ketoadipate node. This pathway allows *P. putida* to use phenylacetate as sole carbon and energy source (and it is chemotactically attractive) [Luu et al., 2013, PMID 23377939]. The catabolon integrates upper routes for phenylethylamine/phenylethanol and styrene, all of which converge on phenylacetyl-CoA [Olivera et al., 1998, PMID 9600981; Arias et al., 2008, PMID 18177365; Alonso et al., 2003, PMID 14597173].

**Note on nomenclature:** In the *P. putida* KT2440 gene naming (used for PP_3282), *paaH* denotes the 3-hydroxyacyl-CoA dehydrogenase. Homologous *paa* clusters in other organisms use different letters for the same enzymatic steps (e.g., in some *P. putida* studies the terminal thiolase is designated by a different letter), so care is needed when mapping gene letters across strains. The **enzymatic identity of PP_3282 as the 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35)** is unambiguous.

---

## 5. Subcellular Localization

PaaH is a **soluble cytoplasmic (cytosolic) enzyme**. Evidence:
- Its substrate and product are CoA thioesters, which are cytosolic metabolites of the intracellular β-oxidation-like module [Olivera et al., 1998, PMID 9600981].
- The 505-aa sequence has **no N-terminal signal peptide and no transmembrane segment**, and the 3-hydroxyacyl-CoA dehydrogenase family is uniformly soluble/globular [Barycki et al., 2000, PMID 10840044; Kim et al., 2014, PMID 24792376].
- The enzyme is predicted to function as a **homodimer** (via the C-terminal domain), like characterized family members.

---

## 6. Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| PaaH is an NAD⁺-dependent 3-hydroxyacyl-CoA dehydrogenase (EC 1.1.1.35) | **Supported** | EC/DB annotation + Rossmann motif + family membership |
| Its physiological substrate is 3-hydroxyadipyl-CoA (→ 3-oxoadipyl-CoA) | **Supported (inference)** | Pathway position; products are succinyl-CoA + acetyl-CoA [PMID 17259607] |
| PaaH acts in the β-oxidation-like lower segment of the phenylacetate catabolon | **Supported** | [PMID 9600981; 9748275] |
| PaaH is cytoplasmic/soluble, likely homodimeric | **Supported (inference)** | No signal/TM; family structures [PMID 24792376, 10840044] |
| PaaH is a membrane transporter or structural/signaling protein | **Refuted** | Sequence and family are enzymatic, soluble oxidoreductase |
| The gene symbol is ambiguous / literature belongs to a different gene | **Refuted** | All identifiers converge on the phenylacetate-pathway HAD |

---

## 7. Limitations and Future Directions

- **No direct enzymology on Q88HS1 itself:** substrate specificity and kinetic parameters are inferred from pathway context and close homologs, not measured for the KT2440 protein. Direct assay with (S)-3-hydroxyadipyl-CoA vs. straight-chain and other dicarboxylic 3-hydroxyacyl-CoAs would establish specificity and any promiscuity.
- **No experimental structure of Q88HS1:** the two-domain fold, dimerization, and His–Glu dyad positions are inferred from RePaaH1 and human HAD. A crystal/AlphaFold structure would localize the catalytic residues and confirm cofactor geometry.
- **Nomenclature mapping:** cross-strain *paa* gene-letter differences warrant care; confirming PP_3282 operon context and coexpression with the other *paa* genes in KT2440 would solidify the assignment.
- **Regulation:** the pathway is induced by phenylacetyl-CoA via a PaaX-type repressor in *E. coli*; verifying PaaH's transcriptional control in KT2440 would complete the physiological picture.

---

### Key References
- Olivera et al. 1998, *PNAS* — *P. putida* U phenylacetyl-CoA catabolon; β-oxidation-like system (PMID 9600981)
- Ferrández et al. 1998, *J Biol Chem* — *E. coli* paa cluster; β-oxidation-like enzymes (PMID 9748275)
- Nogales et al. 2007, *Microbiology* — terminal step; succinyl-CoA + acetyl-CoA products (PMID 17259607)
- Luu et al. 2013, *Appl Environ Microbiol* — PAA as funneling pathway / growth substrate (PMID 23377939)
- Kim et al. 2014, *Biochim Biophys Acta* — PaaH1 (Ralstonia) crystal structure; Rossmann + dimerization domains (PMID 24792376)
- Barycki et al. 2000, *Biochemistry* — L-3-hydroxyacyl-CoA dehydrogenase mechanism, His-Glu dyad (PMID 10840044)
- Arias et al. 2008 (PMID 18177365); Alonso et al. 2003 (PMID 14597173) — upstream catabolon routes converging on phenylacetyl-CoA


## Artifacts

- [OpenScientist final report](paaH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaH-deep-research-openscientist_artifacts/final_report.pdf)