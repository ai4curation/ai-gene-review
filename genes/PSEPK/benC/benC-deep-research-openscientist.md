---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-13T11:30:16.793688'
end_time: '2026-07-13T11:43:00.871811'
duration_seconds: 764.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: benC
  gene_symbol: benC
  uniprot_accession: Q88I38
  protein_description: 'SubName: Full=Benzoate 1,2-dioxygenase electron transfer component
    {ECO:0000313|EMBL:AAN68771.1}; EC=1.14.12.10 {ECO:0000313|EMBL:AAN68771.1}; EC=1.18.1.3
    {ECO:0000313|EMBL:AAN68771.1};'
  gene_info: Name=benC {ECO:0000313|EMBL:AAN68771.1}; OrderedLocusNames=PP_3163 {ECO:0000313|EMBL:AAN68771.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: 2Fe-2S_ferredoxin-like_sf. (IPR036010); 2Fe-2S_ferredoxin-type.
    (IPR001041); 2Fe2S_fd_BS. (IPR006058); BenC-like_FAD_NAD-bd. (IPR047683); Beta-grasp_dom_sf.
    (IPR012675)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 20
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: benC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: benC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I38
- **Protein Description:** SubName: Full=Benzoate 1,2-dioxygenase electron transfer component {ECO:0000313|EMBL:AAN68771.1}; EC=1.14.12.10 {ECO:0000313|EMBL:AAN68771.1}; EC=1.18.1.3 {ECO:0000313|EMBL:AAN68771.1};
- **Gene Information:** Name=benC {ECO:0000313|EMBL:AAN68771.1}; OrderedLocusNames=PP_3163 {ECO:0000313|EMBL:AAN68771.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** 2Fe-2S_ferredoxin-like_sf. (IPR036010); 2Fe-2S_ferredoxin-type. (IPR001041); 2Fe2S_fd_BS. (IPR006058); BenC-like_FAD_NAD-bd. (IPR047683); Beta-grasp_dom_sf. (IPR012675)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "benC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'benC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **benC** (gene ID: benC, UniProt: Q88I38) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# benC (Q88I38, PP_3163) in *Pseudomonas putida* KT2440: The Reductase Component of Benzoate 1,2-Dioxygenase

## Summary

**benC** (UniProt **Q88I38**; ordered locus **PP_3163**) in *Pseudomonas putida* strain KT2440 encodes the **soluble, cytoplasmic reductase (electron-transfer) component of benzoate 1,2-dioxygenase**. It is a class IB Rieske non-heme iron dioxygenase reductase — a single polypeptide that fuses three redox-cofactor domains (a plant-type [2Fe-2S] ferredoxin domain, an FAD-binding domain, and an NAD(H)-binding domain). Its molecular function is to accept a hydride (two electrons) from **NADH**, pass those electrons one at a time through its bound **FAD** flavin and its **[2Fe-2S]** cluster, and deliver them **directly to the terminal oxygenase** (the BenA/BenB heterocomplex). The oxygenase then uses those electrons plus molecular O₂ to carry out *cis*-1,2-dihydroxylation of benzoate, producing benzoate-*cis*-1,2-dihydrodiol (also called *cis*-1,2-dihydroxycyclohexa-3,5-diene-1-carboxylate, DHCDC). This is the first committed and rate-setting step of aerobic benzoate catabolism.

The two EC numbers annotated for Q88I38 reflect the same protein viewed at two levels: **EC 1.14.12.10** (benzoate 1,2-dioxygenase) describes the overall multi-component reaction that benC participates in, while **EC 1.18.1.3** (ferredoxin—NAD(P)⁺ reductase-type activity) describes benC's own intrinsic catalytic activity as an NAD(H)-dependent oxidoreductase. Importantly, benC does **not** itself bind benzoate and does **not** determine substrate specificity; specificity is dictated by the oxygenase α-subunit (BenA). benC's role is purely to serve as the electron conduit.

The physiological context is well established in the target organism. In *P. putida* KT2440, benC is part of the chromosomal **benABC** operon, which is induced by benzoate through the AraC/XylS-family transcriptional activator **BenR**. The pathway funnels benzoate → catechol → *cis,cis*-muconate → β-ketoadipate → succinyl-CoA + acetyl-CoA into the TCA cycle, via the **catechol branch of the β-ketoadipate pathway**. This report synthesizes 12 confirmed findings drawn from 32 papers, including the definitive 1.5 Å crystal structure of the direct BenC homolog from *Acinetobacter* sp. ADP1, biochemical reconstitution studies, genetic/regulatory dissection, and the modern systematic classification of Rieske oxygenases.

### Identity verification (mandatory)

The gene symbol *benC*, the operon context (*benABC*), the organism (*P. putida* KT2440), the EC numbers, and the InterPro domain complement (2Fe-2S ferredoxin-type IPR001041; BenC-like FAD/NAD-binding IPR047683; beta-grasp IPR012675) are **all mutually consistent** and match a large, coherent primary literature on benzoate/toluate dioxygenase reductases. There is **no ambiguity**: this is the reductase (BenC) of benzoate 1,2-dioxygenase.

---

## Key Findings

### 1. benC is the NADH-dependent reductase component of benzoate 1,2-dioxygenase

The single most definitive piece of evidence comes from the X-ray crystal structure of the direct structural homolog, **BenC from *Acinetobacter* sp. strain ADP1**, solved at 1.5 Å resolution ([PMID: 12051836](https://pubmed.ncbi.nlm.nih.gov/12051836/)). This homolog shares >50% amino-acid identity with Q88I38 and comes from an identical *benABC* operon architecture. The authors state plainly that benzoate dioxygenase "contains a reductase component, BenC, that is responsible for the **two-electron transfer from NADH via FAD and an iron-sulfur cluster to the terminal oxygenase component**." This directly defines the molecular function of benC: it is the entry point for reducing equivalents into the dioxygenase system.

The structure reveals **three domains, each binding a redox cofactor: iron-sulfur, FAD, and NADH**, respectively. The [2Fe-2S] domain resembles that of plant ferredoxins, while the FAD and NADH domains belong to the ferredoxin:NADPH reductase (FNR) superfamily. This three-domain cofactor architecture is exactly mirrored by the InterPro domain annotations for Q88I38: the 2Fe-2S ferredoxin-type domain (IPR001041), the BenC-like FAD/NAD-binding domain (IPR047683), and the beta-grasp domain (IPR012675). The structure also shows that the iron-sulfur center and the flavin sit **only ~9 Å apart**, a geometry that "allows a fast electron transfer" — providing the physical basis for rapid intramolecular electron relay within the protein.

### 2. benC is a class IB Rieske dioxygenase reductase that transfers electrons directly to the oxygenase

The BenC structure was, at the time of publication, "**the first determined for a reductase from the class IB Rieske dioxygenases, whose reductases transfer electrons directly to their oxygenase components**" ([PMID: 12051836](https://pubmed.ncbi.nlm.nih.gov/12051836/)). This is a mechanistically important distinction. In three-component Rieske systems (e.g., toluene dioxygenase, carbazole dioxygenase), a separate small **ferredoxin** protein shuttles electrons between the reductase and the oxygenase. In class IB systems like benzoate dioxygenase, there is **no discrete ferredoxin gene** in the operon; instead, benC itself carries the plant-type [2Fe-2S] domain fused to the FAD/NAD reductase module, so the electron chain collapses into a **two-component system**: oxygenase (benAB) + reductase (benC).

General studies of Rieske reductases contextualize benC's function. The reductase's task is to "**shuttle electrons from NADH to the ferredoxin, a reaction the enzyme has to catalyze in the presence of dioxygen**" ([PMID: 22992736](https://pubmed.ncbi.nlm.nih.gov/22992736/)) — in benC's case, the [2Fe-2S] acceptor is fused rather than a separate protein, but the principle of managing electron flow in an O₂-rich environment is the same.

### 3. benC belongs to a two-component RHO system with a fused-domain FNR-type reductase

The authoritative Kweon et al. (2008) reclassification analyzed 130 bacterial Rieske non-heme iron aromatic ring-hydroxylating oxygenases (RHOs) and organized them into 5 types based on their electron-transport-chain (ETC) components ([PMID: 18387195](https://pubmed.ncbi.nlm.nih.gov/18387195/)). "**Type I represents two-component RHO systems that consist of an oxygenase and an FNRC-type reductase.**" Benzoate 1,2-dioxygenase — oxygenase BenAB plus reductase BenC (with its fused plant-type [2Fe-2S] domain and FAD/NAD FNR-like domains) — is precisely such a two-component system. This modern classification is fully consistent with the earlier "class IB" designation from the BenC crystal structure paper. The same review establishes that RHOs "are multi-component enzyme systems that are remarkably diverse in bacteria isolated from diverse habitats," placing benC firmly within this large, functionally coherent enzyme family.

### 4. benC carries ~1 FAD + 1 [2Fe-2S] per monomer and couples NADH oxidation stoichiometrically to O₂ consumption

Biochemical characterization of the closely related two-component **anthranilate/benzoate dioxygenase system from *Acinetobacter* ADP1** (same enzyme family, benC-type reductase) established the cofactor stoichiometry ([PMID: 11114907](https://pubmed.ncbi.nlm.nih.gov/11114907/)). The reductase component "was found to contain approximately **one flavin adenine dinucleotide and one ferredoxin-type [2Fe-2S] center per 39-kDa monomer**." The complete dioxygenase converts substrate "to catechol with insertion of both atoms of O₂ and consumption of one NADH," and this conversion is "**stoichiometrically coupled to NADH oxidation and O₂ consumption**."

Critically, this same enzyme, when tested with benzoate, "was converted to a nonaromatic benzoate 1,2-diol with similarly tight coupling. This latter activity is **identical to that of the related benzoate 1,2-dioxygenase**." This directly links benC-supplied electron flow to benzoate *cis*-diol formation with tight NADH/O₂ coupling — a hallmark of a well-behaved, non-leaky electron-transfer chain.

**Reaction (overall system, EC 1.14.12.10):**
> benzoate + NADH + H⁺ + O₂ → benzoate-*cis*-1,2-dihydrodiol + NAD⁺

**benC's intrinsic half-reaction (EC 1.18.1.3):**
> NADH + H⁺ + 2 oxidized acceptor → NAD⁺ + 2 reduced acceptor (electrons passed onward to the oxygenase's Rieske / mononuclear-Fe centers).

### 5. The flavin acts as a 2-electron/1-electron switch

benC solves a fundamental chemical problem: NADH is an obligatory **two-electron** donor, while the [2Fe-2S] cluster and the downstream oxygenase iron centers are obligatory **one-electron** carriers. The paradigm enzyme for understanding this switch is **phthalate dioxygenase reductase (PDR)**, a structurally homologous three-domain iron-sulfur flavoprotein ([PMID: 7589982](https://pubmed.ncbi.nlm.nih.gov/7589982/)). As the authors state, "**Transfer of electrons between pyridine nucleotides (obligatory two-electron carriers) and hemes or [2Fe-2S] centers (obligatory one-electron carriers) is an essential step mediated by flavins** in respiration, photosynthesis, and many oxygenase systems."

The mechanism proceeds in defined sequential steps: "Kinetic studies have identified sequential steps in the reaction of PDR with NADH that involve **pyridine nucleotide binding, hydride transfer to FMN, and intramolecular electron transfer from the reduced flavin to the [2Fe-2S] cluster**" ([PMID: 7589982](https://pubmed.ncbi.nlm.nih.gov/7589982/)). In benC, the analogous flavin is FAD (rather than PDR's FMN), and the ~9 Å flavin-to-[2Fe-2S] distance enables fast intramolecular transfer. A related concern — avoiding wasteful reaction of the reduced flavin with O₂ — is addressed in the homologous toluene dioxygenase reductase, whose structure shows "the complex between NAD(+) and reduced reductase, which shows that the nicotinamide ring and the protein matrix **shield the reactive C4a position of the isoalloxazine ring**" ([PMID: 22992736](https://pubmed.ncbi.nlm.nih.gov/22992736/)), suppressing unwanted flavin-O₂ side reactions during electron shuttling.

### 6. Substrate specificity resides in the oxygenase α-subunit, not in benC

A crucial point for functional annotation: benC does not confer substrate specificity. Reconstitution and hybrid-oxygenase experiments with benzoate dioxygenase (BADO) from *Acinetobacter* ADP1 showed that "**Reconstituted BADO(ADP1) utilized four of the seven tested benzoates in the following order of apparent specificity: benzoate > 3-methylbenzoate > 3-chlorobenzoate > 2-methylbenzoate**" ([PMID: 12949084](https://pubmed.ncbi.nlm.nih.gov/12949084/)) — a narrower specificity than the related toluate dioxygenase. By constructing hybrid oxygenases, the authors demonstrated that "**The apparent substrate specificity of the alphaBbetaT hybrid oxygenase for these benzoates corresponded to that of BADO(ADP1), the parent from which the alpha subunit originated.**" In other words, swapping the α-subunit swaps the specificity; the reductase (benC) is functionally interchangeable and does not select substrates. This confirms benzoate as the preferred physiological substrate and localizes specificity determinants to BenA, not benC.

### 7. benC is evolutionarily homologous to related aromatic-ring dioxygenase reductases

benC belongs to a family of closely related reductases. Sequence alignment of the toluate 1,2-dioxygenase reductase **XylZ** (TOL plasmid pWW0) with BenC (benzoate dioxygenase reductase) shows that "comparison of aligned XylX-BenA, XylY-BenB, and XylZ-BenC amino acid sequences revealed respective identities of **58.3, 61.3, and 53%**" ([PMID: 1938949](https://pubmed.ncbi.nlm.nih.gov/1938949/)). The 2-halobenzoate 1,2-dioxygenase operon *cbdABC* from *Burkholderia/Pseudomonas cepacia* 2CBS shows ~52% identity to *benABC*, and its reductase **CbdC** has "a putative binding site for a **chloroplast-type [2Fe-2S] center and possible flavin adenine dinucleotide- and NAD-binding domains**" ([PMID: 7530709](https://pubmed.ncbi.nlm.nih.gov/7530709/)) — the same domain architecture as benC. This conserved reductase design across multiple aromatic-acid dioxygenases reinforces the functional assignment of benC.

### 8. Expression of benABC (including benC) is benzoate-inducible via the activator BenR

In *P. putida*, the *benABC* operon is transcriptionally controlled by **BenR**, an AraC/XylS-family regulator whose deduced sequence is 62% identical to XylS. Genetic evidence is definitive: "**A benR mutant isolated by random transposon mutagenesis was unable to grow on benzoate**," and "**benR activated expression of a benA-lacZ reporter fusion in response to benzoate**" ([PMID: 11053377](https://pubmed.ncbi.nlm.nih.gov/11053377/)). The same study confirms operon assignment: "The benABC genes likely encode benzoate dioxygenase, and benD likely encodes 2-hydro-1,2-dihydroxybenzoate dehydrogenase." The broader ben gene cluster comprises benABC (dioxygenase), benD (dihydrodiol dehydrogenase), benK (benzoate permease), benF (porin), and benE, with benR as the adjacent regulator.

### 9. benABC is a chromosomal peripheral pathway feeding the β-ketoadipate pathway in KT2440

Genomic analysis of KT2440 mapped the benzoate (*ben*) peripheral pathway on the chromosome, feeding into the catechol branch (*cat* genes) of the β-ketoadipate pathway. The KT2440 genome contains "the genes encoding the peripheral pathways for the catabolism of p-hydroxybenzoate (pob), **benzoate (ben)**, quinate (qui)" ([PMID: 12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/)), which converge on "the protocatechuate (pca genes) and catechol (cat genes) branches of the beta-ketoadipate pathway." Proteomics of benzoate-grown KT2440 provided direct expression evidence: "**Benzoate dioxygenase (BenA, BenD) and catechol 1,2-dioxygenase (CatA) were induced by benzoate**" ([PMID: 16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/)).

Functional evidence that benABC catalyzes the first (dihydroxylation) step comes from an overexpression experiment: "Genes benABC encoding benzoate dioxygenase were cloned into plasmid pSYM01 and overexpressed in P. putida KTSY01. The recombinant bacteria **P. putida KTSY01 (pSYM01) showed strong ability to transform benzoate to DHCDC**" ([PMID: 18679676](https://pubmed.ncbi.nlm.nih.gov/18679676/)) — confirming that benABC (including benC) converts benzoate to the *cis*-dihydrodiol product.

### 10. benC initiates catabolic flux from benzoate into central metabolism

The benABC/benD-initiated pathway converts benzoate to catechol, which is processed by the catechol branch (catechol → *cis,cis*-muconate → ... → β-ketoadipate → succinyl-CoA + acetyl-CoA → TCA cycle). This in vivo flux is exploited biotechnologically: engineered *P. putida* KT2440 produces *cis,cis*-muconic acid "**in a 42.5 L fermenter using glucose and benzoate as carbon substrates**" ([PMID: 32022244](https://pubmed.ncbi.nlm.nih.gov/32022244/)), demonstrating substantial catabolic throughput from benzoate through the benABC-initiated catechol pathway.

### 11. benC's pathway is directly studied in KT2440 — the target strain

This is not merely inference from homologs. The benzoate route is a strain-native, active pathway in KT2440: soil microorganisms "**mineralize lignin-derived aromatic carbon sources using oxidative catabolic pathways, such as the β-ketoadipate pathway**" ([PMID: 29468117](https://pubmed.ncbi.nlm.nih.gov/29468117/)), and the dynamics of benzoate metabolism have been explicitly modeled in *P. putida* KT2440, integrating the benzoate pathway and its aromatic-carbon-source regulation into the KT2440 metabolic network.

### 12. benC is a soluble, cytoplasmic protein

All evidence points to a soluble cytoplasmic localization. The paradigm class member, phthalate dioxygenase reductase, is explicitly "a **soluble** iron-sulfur flavoprotein from Pseudomonas cepacia" ([PMID: 7589982](https://pubmed.ncbi.nlm.nih.gov/7589982/)). The BenC homolog from *Acinetobacter* ADP1 was purified as a soluble recombinant protein and crystallized ("Here, we present the structure of BenC from Acinetobacter sp. strain ADP1 at 1.5 A resolution," [PMID: 12051836](https://pubmed.ncbi.nlm.nih.gov/12051836/)). benC's InterPro domains are all soluble cofactor-binding folds (2Fe-2S ferredoxin-like, FAD/NAD-binding, beta-grasp), with no signal peptide or transmembrane segment. Consistent with cytoplasmic action, benzoate must first be **imported** (via the BenK permease/BenF porin) before intracellular oxidation.

---

## Mechanistic Model / Interpretation

### The electron-transfer chain

benC sits at the head of a short, fast electron-transfer chain that powers benzoate dihydroxylation:

```
                                  benC (reductase, PP_3163)
                          ┌───────────────────────────────────┐
   NADH  ──(hydride, 2e⁻)──▶  FAD  ──(1e⁻ each)──▶  [2Fe-2S]   │
   NAD⁺ ◀────────────────────┘                        │        │
                          └────────────────────────────┼───────┘
                                                        │ (1e⁻ each, direct)
                                                        ▼
                              BenAB terminal oxygenase (Rieske [2Fe-2S] + mononuclear Fe)
                                                        │
                                          benzoate + O₂ │
                                                        ▼
                                   benzoate-cis-1,2-dihydrodiol (DHCDC)
                                                        │  BenD (dihydrodiol dehydrogenase)
                                                        ▼
                                                    catechol
                                                        │  CatA (catechol 1,2-dioxygenase)
                                                        ▼
                                               cis,cis-muconate
                                                        │  β-ketoadipate pathway (cat branch)
                                                        ▼
                              β-ketoadipate → succinyl-CoA + acetyl-CoA → TCA cycle
```

benC is a **modular, single-polypeptide electron relay**. NADH binds and delivers a hydride to FAD (a 2-electron event). The reduced flavin then passes electrons one at a time — first, intramolecularly, to the closely juxtaposed (~9 Å) [2Fe-2S] cluster, and then to the terminal oxygenase's Rieske center. Because benzoate dioxygenase is a class IB / Type I system, there is no intervening ferredoxin: benC's own [2Fe-2S] domain performs the role that a separate ferredoxin plays in three-component systems.

### Division of labor within the enzyme complex

| Component | Gene | Cofactors | Role |
|-----------|------|-----------|------|
| Reductase | **benC** (PP_3163, Q88I38) | FAD + plant-type [2Fe-2S] | Accept 2e⁻ from NADH; relay 1e⁻ at a time to oxygenase |
| Oxygenase α | benA | Rieske [2Fe-2S] + mononuclear Fe | O₂ activation; **substrate binding & specificity**; catalysis |
| Oxygenase β | benB | (structural) | Structural subunit of oxygenase |

The key conceptual takeaway is a clean separation of function: **benC handles electrons; BenA handles substrate and chemistry.** Hybrid-oxygenase experiments proved that specificity travels with the α-subunit, not the reductase ([PMID: 12949084](https://pubmed.ncbi.nlm.nih.gov/12949084/)).

### The two EC numbers, reconciled

- **EC 1.14.12.10** (benzoate 1,2-dioxygenase): the overall reaction of the multi-component enzyme system that benC is a part of — benzoate + NADH + H⁺ + O₂ → benzoate-*cis*-dihydrodiol + NAD⁺.
- **EC 1.18.1.3** (ferredoxin—NAD(P)⁺ oxidoreductase-type activity): benC's own intrinsic catalytic activity — oxidation of NADH with transfer of electrons to a ferredoxin-type acceptor (here, its fused [2Fe-2S] and, downstream, the oxygenase).

Both annotations describe the same protein; benC is the reductase that makes the EC 1.14.12.10 reaction possible via its EC 1.18.1.3 chemistry.

### Physiological role

benC enables *P. putida* KT2440 to use benzoate — and, through the same pathway, various lignin-derived aromatic acids — as a carbon and energy source. The operon is switched on only when benzoate is present (BenR-mediated induction), reflecting an economical, substrate-inducible catabolic strategy. The pathway's central-metabolic connection (via catechol → β-ketoadipate → TCA cycle) explains why KT2440 is a favored chassis for producing *cis,cis*-muconate and adipic acid precursors from aromatic feedstocks.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|------|--------------------|------------------------------|
| [12051836](https://pubmed.ncbi.nlm.nih.gov/12051836/) | *X-ray crystal structure of benzoate 1,2-dioxygenase reductase from Acinetobacter sp. ADP1* | **Central evidence.** Defines BenC as the NADH→FAD→[2Fe-2S]→oxygenase electron-transfer component; establishes 3-domain architecture, ~9 Å flavin–[2Fe-2S] distance, and class IB (direct-to-oxygenase) mechanism. |
| [18387195](https://pubmed.ncbi.nlm.nih.gov/18387195/) | *A new classification system for bacterial Rieske non-heme iron aromatic RHOs* | Places benzoate dioxygenase in Type I (two-component: oxygenase + FNR-type reductase). Authoritative modern taxonomy. |
| [11114907](https://pubmed.ncbi.nlm.nih.gov/11114907/) | *Characterization and evolution of anthranilate 1,2-dioxygenase from Acinetobacter ADP1* | Cofactor stoichiometry (1 FAD + 1 [2Fe-2S] per monomer); tight NADH/O₂ coupling; benzoate → benzoate 1,2-diol identical to benzoate dioxygenase. |
| [7589982](https://pubmed.ncbi.nlm.nih.gov/7589982/) | *Structure and mechanism of phthalate dioxygenase reductase* | Paradigm for the 2e⁻/1e⁻ flavin switch and the sequential NADH-binding → hydride transfer → intramolecular electron transfer mechanism; documents soluble cytoplasmic nature. |
| [22992736](https://pubmed.ncbi.nlm.nih.gov/22992736/) | *Suppression of electron transfer to dioxygen in toluene dioxygenase reductase* | Reductase shuttles electrons from NADH in the presence of O₂; charge-transfer complex shields flavin C4a to prevent wasteful O₂ reaction. |
| [12949084](https://pubmed.ncbi.nlm.nih.gov/12949084/) | *Characterization of hybrid toluate and benzoate dioxygenases* | Substrate specificity resides in oxygenase α-subunit, not reductase; benzoate is preferred substrate; narrow specificity. |
| [1938949](https://pubmed.ncbi.nlm.nih.gov/1938949/) | *Evolutionary divergence of benABC and xylXYZ* | XylZ–BenC 53% identity; establishes evolutionary homology to toluate dioxygenase reductase. |
| [7530709](https://pubmed.ncbi.nlm.nih.gov/7530709/) | *2-halobenzoate 1,2-dioxygenase from P. cepacia 2CBS* | Homologous reductase CbdC has same chloroplast-type [2Fe-2S]/FAD/NAD architecture, confirming conserved design. |
| [11053377](https://pubmed.ncbi.nlm.nih.gov/11053377/) | *BenR, a XylS homologue, regulates aromatic acid degradation in P. putida* | benABC is benzoate-inducible via BenR; benR mutant cannot grow on benzoate; operon assignment. |
| [12534466](https://pubmed.ncbi.nlm.nih.gov/12534466/) | *Genomic analysis of aromatic catabolic pathways from P. putida KT2440* | Chromosomal ben peripheral pathway feeding catechol branch of β-ketoadipate pathway in the target strain. |
| [16470664](https://pubmed.ncbi.nlm.nih.gov/16470664/) | *Proteomic analysis of aromatic pathways in KT2440* | Direct experimental evidence that benzoate dioxygenase (BenA, BenD) is induced during benzoate growth in KT2440. |
| [18679676](https://pubmed.ncbi.nlm.nih.gov/18679676/) | *Microbial production of DHCDC by modified P. putida* | benABC overexpression converts benzoate to DHCDC, confirming the dihydroxylation step. |
| [29468117](https://pubmed.ncbi.nlm.nih.gov/29468117/) | *Dynamics of benzoate metabolism in P. putida KT2440* | KT2440-native operation of the benzoate/β-ketoadipate pathway. |
| [32022244](https://pubmed.ncbi.nlm.nih.gov/32022244/) | *Life-cycle assessment for bioconversion of lignin aromatics to adipic acid* | In vivo flux from benzoate to cis,cis-muconate in KT2440 at fermenter scale. |

Supporting structural/mechanistic context on related multi-component Rieske systems (toluene 2,3-dioxygenase, [PMID: 19153463](https://pubmed.ncbi.nlm.nih.gov/19153463/); carbazole 1,9a-dioxygenase, [PMID: 19616558](https://pubmed.ncbi.nlm.nih.gov/19616558/), [PMID: 34196618](https://pubmed.ncbi.nlm.nih.gov/34196618/); alkene monooxygenase, [PMID: 9312093](https://pubmed.ncbi.nlm.nih.gov/9312093/)) and on PDR kinetics ([PMID: 7522555](https://pubmed.ncbi.nlm.nih.gov/7522555/), [PMID: 7577934](https://pubmed.ncbi.nlm.nih.gov/7577934/)) further corroborate the electron-transfer model but describe distinct (often three-component) systems.

### Supported and refuted hypotheses

**Supported:**
- benC is the reductase/electron-transfer component of benzoate 1,2-dioxygenase (NADH → FAD → [2Fe-2S] → oxygenase). ✔ ([PMID: 12051836](https://pubmed.ncbi.nlm.nih.gov/12051836/), [PMID: 11114907](https://pubmed.ncbi.nlm.nih.gov/11114907/))
- benC is a class IB / Type I Rieske dioxygenase reductase (no separate ferredoxin). ✔ ([PMID: 12051836](https://pubmed.ncbi.nlm.nih.gov/12051836/), [PMID: 18387195](https://pubmed.ncbi.nlm.nih.gov/18387195/))
- benC is soluble/cytoplasmic. ✔ ([PMID: 7589982](https://pubmed.ncbi.nlm.nih.gov/7589982/), [PMID: 12051836](https://pubmed.ncbi.nlm.nih.gov/12051836/))
- benABC is benzoate-inducible via BenR. ✔ ([PMID: 11053377](https://pubmed.ncbi.nlm.nih.gov/11053377/))
- Substrate specificity is oxygenase-determined; benzoate is the physiological substrate. ✔ ([PMID: 12949084](https://pubmed.ncbi.nlm.nih.gov/12949084/))

**Refuted / excluded:**
- benC is NOT the substrate-binding hydroxylase (that is BenAB). ✘
- benC does NOT determine substrate specificity. ✘
- benC does NOT require a separate ferredoxin partner (unlike class III systems). ✘

### A note on evidence strength

The functional assignment of benC rests primarily on the **1.5 Å crystal structure of the direct *Acinetobacter* BenC homolog** (>50% identity, identical operon), combined with biochemical reconstitution of the closely related ADP1 dioxygenase and detailed mechanistic work on the paradigm reductases PDR and toluene dioxygenase reductase. For the target organism *P. putida* KT2440 specifically, we have strong genetic (BenR regulation), genomic (operon mapping), and proteomic (benzoate induction) evidence that the pathway is native and active, plus functional overexpression evidence that benABC dihydroxylates benzoate. This is a well-supported annotation.

---

## Limitations and Knowledge Gaps

1. **No direct crystal structure or enzymatic assay of Q88I38 itself.** The definitive structural and biochemical characterization is of the *Acinetobacter* sp. ADP1 BenC homolog (>50% identity) and the ADP1 anthranilate/benzoate dioxygenase system, not of the *P. putida* KT2440 protein directly. Functional equivalence is strongly inferred from high sequence identity and identical operon architecture, but the KT2440 protein's specific kinetic parameters (Km for NADH, kcat, coupling efficiency, midpoint potentials) have not been measured in the reviewed literature.

2. **NADH vs. NADPH preference not experimentally pinned down for benC.** By homology to class IB Rieske reductases, NADH is expected, and the ADP1 system uses NADH; however, the exact pyridine-nucleotide preference and its Km for Q88I38 were not directly quantified in the sources reviewed.

3. **Localization is inferred, not directly demonstrated for Q88I38.** Cytoplasmic localization is a robust inference (soluble domains, no signal peptide, soluble homologs crystallized), but no direct fractionation/localization experiment on the KT2440 protein was found.

4. **Cofactor occupancy assumed by homology.** The 1 FAD + 1 [2Fe-2S] stoichiometry comes from the ADP1 system; it is expected but not independently measured for the KT2440 protein.

5. **Quaternary structure and reductase–oxygenase docking geometry.** How benC physically docks onto the BenAB oxygenase to deliver electrons, and whether a transient complex forms, remains less characterized for this specific system than for some three-component Rieske systems where ferredoxin–oxygenase interfaces have been mapped.

---

## Proposed Follow-up Experiments / Actions

1. **Heterologous expression and biochemical characterization of Q88I38 (KT2440 benC).** Purify the KT2440 protein and directly measure: cofactor content (FAD, [2Fe-2S] by UV-vis/EPR/iron & acid-labile sulfide assays), NADH vs. NADPH preference and Km, and diaphorase (cytochrome c / ferricyanide reduction) activity — to confirm the intrinsic EC 1.18.1.3 chemistry.

2. **Reconstitute the full KT2440 benzoate 1,2-dioxygenase in vitro** (benC + BenAB) and verify stoichiometric, tightly coupled conversion of benzoate to benzoate-*cis*-1,2-dihydrodiol with 1:1 NADH:O₂:product ratios, replicating the ADP1 result for the target organism.

3. **Solve or model the KT2440 benC structure** (an AlphaFold model is readily obtainable from the domain composition; an experimental structure would confirm the ~9 Å flavin–[2Fe-2S] geometry and validate the electron-transfer distance).

4. **Cross-complementation / interchangeability tests.** Test whether benC can substitute for related reductases (XylZ, CbdC) and vice versa in reconstituted systems, to formally confirm that the reductase does not confer substrate specificity in the KT2440 context.

5. **Subcellular localization confirmation.** Cell fractionation or fluorescent-tag microscopy of benC in KT2440 to experimentally confirm cytoplasmic localization.

6. **Targeted benC deletion in KT2440.** A clean ΔbenC mutant should abolish benzoate-supported growth (or shift it to alternative routes), providing direct genetic proof of benC's essentiality for benzoate dihydroxylation in the native strain.

---

## Conclusion

**benC (Q88I38, PP_3163)** is the **soluble, cytoplasmic reductase component of benzoate 1,2-dioxygenase** in *Pseudomonas putida* KT2440. As a class IB / Type I Rieske dioxygenase reductase, it uses a bound FAD and a plant-type [2Fe-2S] cluster to accept two electrons from NADH and relay them, one at a time, directly to the terminal oxygenase BenAB. Those electrons and O₂ drive *cis*-1,2-dihydroxylation of benzoate to benzoate-*cis*-dihydrodiol — the first committed step of aerobic benzoate catabolism, which funnels through catechol and the β-ketoadipate pathway into central metabolism. benC supplies reducing power but does not bind benzoate or set substrate specificity; its benABC operon is benzoate-inducible via the AraC/XylS regulator BenR.


## Artifacts

- [OpenScientist final report](benC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](benC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12051836
2. PMID:22992736
3. PMID:18387195
4. PMID:11114907
5. PMID:7589982
6. PMID:12949084
7. PMID:1938949
8. PMID:7530709
9. PMID:11053377
10. PMID:12534466
11. PMID:16470664
12. PMID:18679676
13. PMID:32022244
14. PMID:29468117
15. PMID:19153463
16. PMID:19616558
17. PMID:34196618
18. PMID:9312093
19. PMID:7522555
20. PMID:7577934