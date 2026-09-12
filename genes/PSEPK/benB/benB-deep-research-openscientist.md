---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-13T11:32:04.180862'
end_time: '2026-07-13T11:46:19.002345'
duration_seconds: 854.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: benB
  gene_symbol: benB
  uniprot_accession: Q88I39
  protein_description: 'SubName: Full=Benzoate 1,2-dioxygenase subunit beta {ECO:0000313|EMBL:AAN68770.1};
    EC=1.14.12.10 {ECO:0000313|EMBL:AAN68770.1};'
  gene_info: Name=benB {ECO:0000313|EMBL:AAN68770.1}; OrderedLocusNames=PP_3162 {ECO:0000313|EMBL:AAN68770.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the bacterial ring-hydroxylating dioxygenase
  protein_domains: Benzo_1-2-diOase_ssu. (IPR017641); NTF2-like_dom_sf. (IPR032710);
    Rng_hydr_dOase-bsu. (IPR000391); Ring_hydroxyl_B (PF00866)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: benB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: benB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I39
- **Protein Description:** SubName: Full=Benzoate 1,2-dioxygenase subunit beta {ECO:0000313|EMBL:AAN68770.1}; EC=1.14.12.10 {ECO:0000313|EMBL:AAN68770.1};
- **Gene Information:** Name=benB {ECO:0000313|EMBL:AAN68770.1}; OrderedLocusNames=PP_3162 {ECO:0000313|EMBL:AAN68770.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the bacterial ring-hydroxylating dioxygenase
- **Key Domains:** Benzo_1-2-diOase_ssu. (IPR017641); NTF2-like_dom_sf. (IPR032710); Rng_hydr_dOase-bsu. (IPR000391); Ring_hydroxyl_B (PF00866)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "benB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'benB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **benB** (gene ID: benB, UniProt: Q88I39) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# benB (PP_3162, UniProt Q88I39): The β Subunit of Benzoate 1,2-Dioxygenase in *Pseudomonas putida* KT2440

## Summary

**benB** (locus **PP_3162**; UniProt **Q88I39**) of *Pseudomonas putida* KT2440 encodes the **β (small/beta) subunit of the terminal oxygenase component of benzoate 1,2-dioxygenase** (EC 1.14.12.10). This is a well-supported, unambiguous identification: the UniProt record, the historical biochemistry of the *ben* gene cluster, and the genome annotation of the *benABCDK* operon all converge on the same conclusion. The gene symbol *benB* is **not** ambiguous in this context — the organism, protein family (bacterial ring-hydroxylating dioxygenase, RHO), and Pfam/InterPro domain architecture (PF00866 Ring_hydroxyl_B; IPR017641 benzoate 1,2-dioxygenase small subunit; IPR032710 NTF2-like fold) all match the primary literature on the benzoate degradation pathway.

The primary function of the *benB* product is **structural, not catalytic**. Benzoate 1,2-dioxygenase catalyzes the **first, committed step of aerobic benzoate catabolism**: the *cis*-dihydroxylation of benzoate to **benzoate *cis*-1,2-dihydrodiol** (1,2-dihydroxycyclohexa-3,5-diene-1-carboxylate), incorporating both atoms of molecular O₂ into the substrate using NADH-derived electrons. The catalytically active terminal oxygenase is an **α₃β₃ heterohexamer** built from three copies of the α subunit (BenA) and three copies of the β subunit (BenB). All catalytic machinery — the Rieske [2Fe-2S] cluster, the mononuclear non-heme Fe(II) center, and the substrate-binding pocket that governs specificity — resides in the **α subunit (BenA)**. BenB carries **no metal center and no catalytic residues**; it adopts an NTF2-like soluble fold and functions to **stabilize the oligomeric assembly and provide the inter-subunit interface** required for a stable, active oxygenase.

Functionally, BenB operates as part of a **soluble, cytoplasmic**, multi-component electron-transport system in which the FAD/[2Fe-2S] reductase **BenC** delivers NADH-derived electrons to the **BenAB oxygenase**. The *cis*-dihydrodiol product is then oxidized by the dehydrogenase **BenD** to **catechol**, which enters the **catechol branch of the β-ketoadipate (ortho-cleavage) pathway**, ultimately feeding the TCA cycle. The *benABCDK* operon is **induced by benzoate** through the AraC/XylS-family transcriptional activator **BenR** and is subject to **carbon catabolite repression** mediated by the translational repressor **Crc**. In sum, BenB is the non-catalytic scaffolding subunit that, together with the catalytic BenA subunit, initiates the aerobic degradation of benzoate — a keystone reaction in the funneling of aromatic compounds (including many lignin-derived and xenobiotic aromatics) into central metabolism.

---

## Key Findings

### Finding 1 — benB encodes the β (small) subunit of the benzoate 1,2-dioxygenase terminal oxygenase, initiating aerobic benzoate catabolism

The identity of *benB* is firmly established. The UniProt record for Q88I39 describes it as "Benzoate 1,2-dioxygenase subunit beta," EC 1.14.12.10, gene *benB*, locus PP_3162, in *P. putida* KT2440. Its domain architecture — Pfam PF00866 (Ring_hydroxyl_B) and InterPro IPR017641 (benzoate 1,2-dioxygenase small subunit) — places it unambiguously in the β-subunit family of bacterial ring-hydroxylating dioxygenases.

The foundational biochemical characterization comes from Neidle et al. (1987), who cloned the *benABCD* genes from *Acinetobacter calcoaceticus* and showed they encode "both a benzoate 1,2-dioxygenase system, composed of NADH-cytochrome c reductase and terminal oxygenase components, and a cis-diol dehydrogenase." Critically, they demonstrated that "the dioxygenase system appears to be encoded by three genes, *benABC*, whose products, 53-, 19-, and 38-kilodalton proteins, correspond in size to those of components in other bacterial dioxygenases" [PMID: 2824437](https://pubmed.ncbi.nlm.nih.gov/2824437/). The **19-kDa protein is BenB — the small/β subunit** of the terminal oxygenase.

The reaction itself was directly demonstrated in *P. putida* by Sun et al. (2008), who cloned *benABC* into a plasmid and overexpressed it: "The recombinant bacteria *P. putida* KTSY01 (pSYM01) showed strong ability to transform benzoate to DHCDC" [PMID: 18679676](https://pubmed.ncbi.nlm.nih.gov/18679676/). DHCDC (*cis*-1,2-dihydroxy-cyclohexa-3,5-diene-1-carboxylate) is the *cis*-dihydrodiol product of the EC 1.14.12.10 reaction. The net reaction catalyzed by the BenAB oxygenase is:

> **benzoate + NADH + H⁺ + O₂ → benzoate *cis*-1,2-dihydrodiol + NAD⁺**

This is the first, committed, and rate-defining step of aerobic benzoate catabolism.

### Finding 2 — The terminal oxygenase is an α₃β₃ heterohexamer; catalysis resides in BenA, making BenB a structural subunit

Crystallographic and biochemical studies of the naphthalene-dioxygenase family of Rieske oxygenases — the structural class to which benzoate dioxygenase belongs — establish that the terminal oxygenase is an **α₃β₃ hexamer**. Parales (2003) reports that "the crystal structure of the oxygenase component revealed the enzyme to be an alpha(3)beta(3) hexamer and identified the amino acids located near the active site" [PMID: 12695887](https://pubmed.ncbi.nlm.nih.gov/12695887/), and Parales et al. (2005) confirmed the same α₃β₃ subunit composition for the closely related nitrobenzene and 2-nitrotoluene dioxygenases [PMID: 16000792](https://pubmed.ncbi.nlm.nih.gov/16000792/).

The division of labor between subunits is decisive. Bagnéris et al. (2005) state plainly that "the catalytic iron-sulfur proteins of these enzymes consist of two dissimilar subunits, alpha and beta; **the alpha subunit contains a [2Fe-2S] cluster involved in electron transfer, the catalytic nonheme iron center, and is also responsible for substrate specificity**" [PMID: 15746362](https://pubmed.ncbi.nlm.nih.gov/15746362/). By this logic the β subunit — BenB — carries **no metal center and does not determine substrate specificity**. Consistent with a non-catalytic role, BenB adopts an **NTF2-like fold** (IPR032710), a soluble domain commonly serving structural/scaffolding functions.

The structural role of β subunits is further underscored by carbazole 1,9a-dioxygenase, an unusual α₃-only oxygenase that lacks structural β subunits. Nojiri et al. (2005) found it must compensate with specialized interfacial loops that are "indispensable for stable alpha3 interactions without structural beta subunits" [PMID: 16005887](https://pubmed.ncbi.nlm.nih.gov/16005887/) — direct evidence that, in enzymes like benzoate dioxygenase, the β subunit normally provides the inter-subunit stabilization required for a stable hexamer.

Finally, BenB's assignment as the β subunit is corroborated by homology. Harayama et al. (1991) aligned the chromosomal *ben* genes against the plasmid-borne *xyl* genes of the TOL pathway and found that "comparison of aligned XylX-BenA, XylY-BenB, and XylZ-BenC amino acid sequences revealed respective identities of 58.3, **61.3**, and 53%" [PMID: 1938949](https://pubmed.ncbi.nlm.nih.gov/1938949/). BenB is thus 61.3% identical to XylY, the β subunit of the homologous toluate 1,2-dioxygenase.

### Finding 3 — Benzoate dioxygenase is a multi-component electron-transport system; the BenC reductase feeds electrons to the BenAB oxygenase

The complete enzyme is not a single protein but a multi-component system. As Neidle et al. (1987) established, *benABCD* encodes a benzoate 1,2-dioxygenase system "composed of NADH-cytochrome c reductase and terminal oxygenase components" [PMID: 2824437](https://pubmed.ncbi.nlm.nih.gov/2824437/). The **reductase component (BenC)** couples oxidation of NADH to electron transfer into the oxygenase. Its cofactor content is defined by homology to the well-characterized 2-halobenzoate 1,2-dioxygenase reductase CbdC, in which "a putative binding site for a chloroplast-type [2Fe-2S] center and possible flavin adenine dinucleotide- and NAD-binding domains were identified" [PMID: 7530709](https://pubmed.ncbi.nlm.nih.gov/7530709/); CbdC shows 52% identity to *benABC*.

Electrons therefore flow: **NADH → BenC (FAD → [2Fe-2S]) → BenA Rieske [2Fe-2S] → BenA mononuclear Fe(II) → O₂ activation → cis-dihydroxylation of benzoate**. BenB plays no role in this electron-transfer chain; it stabilizes the oxygenase within which the chemistry occurs.

### Finding 4 — The product feeds the β-ketoadipate pathway via BenD → catechol; the operon is benzoate-inducible via BenR

The *cis*-dihydrodiol product of BenAB does not accumulate — it is oxidized by the *cis*-diol dehydrogenase **BenD** to **catechol**. Kitagawa et al. (2001) demonstrated the full route in a heterologous host: "*Escherichia coli* cells containing RHA1 *benABCD* transformed benzoate to catechol via 2-hydro-1,2-dihydroxybenzoate" [PMID: 11673430](https://pubmed.ncbi.nlm.nih.gov/11673430/). Neidle et al. (1987) similarly showed that "the product of the *A. calcoaceticus benD* gene, when present in *E. coli* enables this organism to convert the cis-diol intermediate to catechol," and that "the *ben* genes are clustered on the ... chromosome with independently regulated genes needed for the dissimilation of catechol" [PMID: 2824437](https://pubmed.ncbi.nlm.nih.gov/2824437/).

Catechol is the entry metabolite of the **catechol branch of the β-ketoadipate (ortho-cleavage) pathway**, which converts catechol through *cis,cis*-muconate and β-ketoadipate to the TCA-cycle intermediates succinyl-CoA and acetyl-CoA. Transcriptionally, the *ben* operon is benzoate-inducible: Li et al. (2010) showed that "the BenR protein functions as a transcriptional activator of the ben operon" [PMID: 20137101](https://pubmed.ncbi.nlm.nih.gov/20137101/).

### Finding 5 — Benzoate dioxygenase is soluble and cytoplasmic, with narrow substrate specificity for benzoate

Rieske ring-hydroxylating dioxygenases of this family are **soluble proteins** purified from cytoplasmic extracts and crystallized as α₃β₃ hexamers [PMID: 12695887](https://pubmed.ncbi.nlm.nih.gov/12695887/); [PMID: 16000792](https://pubmed.ncbi.nlm.nih.gov/16000792/). Neither BenA nor BenB carries a signal peptide or membrane-anchoring domain (BenB's NTF2-like fold is a soluble domain, IPR032710), consistent with a **cytoplasmic site of catalysis**.

Substrate specificity in this enzyme class is a property of the **α subunit's active-site pocket** [PMID: 15746362](https://pubmed.ncbi.nlm.nih.gov/15746362/) — not of BenB. The chromosomal Ben system is **narrow and benzoate-specific**, in explicit contrast to its plasmid-borne homolog: Harayama et al. (1991) note that "the xylXYZ DNA region is carried on the TOL pWW0 plasmid in *Pseudomonas putida* and encodes a benzoate dioxygenase with **broad substrate specificity**" toward methyl-substituted benzoates (toluates) [PMID: 1938949](https://pubmed.ncbi.nlm.nih.gov/1938949/). This contrast frames BenAB as the dedicated benzoate-degrading enzyme, while the toluate dioxygenase (XylXYZ) handles the wider range of substituted benzoates in the TOL pathway.

### Finding 6 — The KT2440 benABCDK cluster (PP_3161–PP_3165) genome-verifies benB as the β subunit, upstream of catA

Direct UniProt/genome verification of *P. putida* KT2440 (taxid 160488) locks in the operon organization:

| Locus | Gene | Product | Length | UniProt |
|-------|------|---------|--------|---------|
| PP_3161 | *benA* | Benzoate 1,2-dioxygenase subunit **α** | 452 aa | Q88I40 |
| **PP_3162** | ***benB*** | **Benzoate 1,2-dioxygenase subunit β (TARGET)** | **161 aa** | **Q88I39** |
| PP_3163 | *benC* | Benzoate 1,2-dioxygenase electron-transfer component (reductase) | 336 aa | Q88I38 |
| PP_3164 | *benD* | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase | 253 aa | Q88I37 |
| PP_3165 | *benK* | Benzoate MFS transporter | 442 aa | Q88I36 |
| PP_3166 | *catA-II* | Catechol 1,2-dioxygenase | 304 aa | Q88I35 |

The three oxygenase-system subunit sizes (α 452 / β 161 / reductase 336 residues) match the historically reported 53 / 19 / 38 kDa proteins of *benABC* [PMID: 2824437](https://pubmed.ncbi.nlm.nih.gov/2824437/). UniProt classifies Q88I39 in the "bacterial ring-hydroxylating dioxygenase beta subunit family," with keywords Aromatic-hydrocarbons-catabolism, Dioxygenase, and Oxidoreductase. The immediate downstream location of *catA-II* (catechol 1,2-dioxygenase) reflects the metabolic logic of the operon: benzoate is converted to catechol and then ortho-cleaved in a spatially co-located gene neighborhood.

### Finding 7 — In P. putida, benABCD is benzoate-induced via BenR and carbon-catabolite-repressed via Crc

The regulatory control of the *benB*-containing operon is exceptionally well characterized in *P. putida* specifically. Cowles, Nichols & Harwood (2000) established the core regulatory logic: "*P. putida* converts benzoate to catechol using two enzymes that are encoded on the chromosome and whose expression is induced by benzoate"; "the *benABC* genes likely encode benzoate dioxygenase, and *benD* likely encodes 2-hydro-1,2-dihydroxybenzoate dehydrogenase. *benK* and *benF* were assigned functions as a benzoate permease and porin" [PMID: 11053377](https://pubmed.ncbi.nlm.nih.gov/11053377/). They demonstrated direct promoter activation — "*benR* activated expression of a *benA-lacZ* reporter fusion in response to benzoate" — and showed BenR has "high similarity (62% identity) to the sequence of XylS, a member of the AraC family of regulators."

Layered on top of this induction is **carbon catabolite repression** by the translational repressor Crc. Moreno & Rojo (2008) showed that "Crc directly inhibits the expression of the peripheral genes that transform benzoate into catechol (the *ben* genes)... Crc significantly reduced *benABCD* mRNA levels" and that it acts "by reducing the translation of *benR* mRNA" [PMID: 18156252](https://pubmed.ncbi.nlm.nih.gov/18156252/). Hernández-Arranz et al. (2013) then demonstrated a **multi-tier strategy**: Crc "inhibits the induction of both pathways by limiting not only the translation of their transcriptional activators, but also that of genes coding for the first enzyme in each pathway" and "may also inhibit the translation of a gene involved in benzoate uptake" [PMID: 22925411](https://pubmed.ncbi.nlm.nih.gov/22925411/). Together these findings show that expression of *benB* is turned on only when benzoate is present **and** preferred carbon sources (e.g., organic acids, amino acids) are absent.

---

## Mechanistic Model / Interpretation

### The benzoate 1,2-dioxygenase reaction and BenB's place in it

Benzoate 1,2-dioxygenase is a multi-component Rieske non-heme iron oxygenase system. Electrons from NADH are shuttled through the reductase to the terminal oxygenase, where the actual O₂-dependent chemistry takes place. BenB is one of the two subunit types (α = BenA, β = BenB) that build the oxygenase.

```
      NADH + H+                       O2
          |                            |
          v                            v
   +-------------+   e-    +-----------------------------+
   | BenC        |-------->|  BenAB terminal oxygenase   |
   | reductase   | Rieske  |  (alpha3-beta3 hexamer)     |
   | FAD/[2Fe-2S]|         |                             |
   +-------------+         |  BenA (alpha): Rieske       |
          |                |    [2Fe-2S] + mononuclear   |
        NAD+               |    Fe(II) + substrate pocket|--> benzoate cis-1,2-dihydrodiol
                           |  BenB (beta): NTF2-like     |
                           |    STRUCTURAL scaffold,     |
                           |    no metal, no catalysis   |
                           +-----------------------------+

  benzoate + NADH + H+ + O2  --->  benzoate cis-1,2-dihydrodiol + NAD+
```

BenB does not touch the substrate, bind a cofactor, or transfer an electron. Its role is architectural: three αβ protomers assemble into the mushroom-shaped α₃β₃ hexamer, and the β subunits provide inter-subunit contacts that hold this assembly together in a catalytically competent state. The carbazole dioxygenase precedent [PMID: 16005887](https://pubmed.ncbi.nlm.nih.gov/16005887/) — where the absence of β subunits demands compensatory structural loops — is the clearest experimental argument that this stabilizing role is real and necessary.

### The full catabolic pathway

```
 benzoate
    | BenAB oxygenase (+ BenC reductase, NADH, O2)   <-- benB acts HERE (structural subunit)
    v
 benzoate cis-1,2-dihydrodiol
    | BenD (cis-diol dehydrogenase, NAD+)
    v
 catechol
    | CatA (catechol 1,2-dioxygenase; PP_3166 catA-II)  ortho / intradiol cleavage
    v
 cis,cis-muconate
    |  (beta-ketoadipate pathway: CatBC ...)
    v
 beta-ketoadipate --> succinyl-CoA + acetyl-CoA --> TCA cycle
```

### Regulatory logic

```
   benzoate present? --YES--> BenR (AraC/XylS activator) --activates--> P(benABCDK)
                                                                              |
   preferred carbon source present? --YES--> Crc represses (translational)   |
        - inhibits benR mRNA translation                                     |
        - inhibits benABCD structural-gene mRNA translation        ----------+
        - inhibits benK (uptake) mRNA translation
   Net: benB expressed ONLY when benzoate present AND no preferred substrate available
```

This dual control ensures that the metabolically costly machinery for aromatic degradation — including the BenB scaffold — is deployed only when benzoate is available and better carbon sources are exhausted, a hallmark of *P. putida*'s finely tuned carbon-source hierarchy.

### Localization

All available evidence indicates BenB (and the whole BenAB oxygenase) functions in the **cytoplasm**: the enzyme is soluble, purified from cytoplasmic extracts across the RHO family, and neither BenA nor BenB bears a signal peptide or transmembrane segment. Benzoate is imported by the MFS transporter BenK (and a porin), so catabolism proceeds intracellularly.

---

## Evidence Base

| PMID | Paper (abbreviated) | How it supports the findings |
|------|---------------------|------------------------------|
| [2824437](https://pubmed.ncbi.nlm.nih.gov/2824437/) | Neidle et al. 1987 — cloning of *A. calcoaceticus benABCD* | Establishes *benABC* = benzoate 1,2-dioxygenase (53/19/38 kDa; BenB = 19 kDa β subunit); BenD converts cis-diol → catechol; multi-component reductase + oxygenase system |
| [18679676](https://pubmed.ncbi.nlm.nih.gov/18679676/) | Sun et al. 2008 — DHCDC production in *P. putida* | Direct demonstration in *P. putida* that *benABC* converts benzoate to its *cis*-1,2-dihydrodiol (EC 1.14.12.10 reaction) |
| [1938949](https://pubmed.ncbi.nlm.nih.gov/1938949/) | Harayama et al. 1991 — *benABC* vs *xylXYZ* | BenB = β subunit, 61.3% identical to XylY; contrasts narrow benzoate specificity (Ben) vs broad toluate specificity (Xyl) |
| [15746362](https://pubmed.ncbi.nlm.nih.gov/15746362/) | Bagnéris et al. 2005 — benzene/toluene dioxygenases | α subunit holds [2Fe-2S], mononuclear Fe, and substrate specificity → β subunit (BenB) is non-catalytic |
| [12695887](https://pubmed.ncbi.nlm.nih.gov/12695887/) | Parales 2003 — active-site residues in NDO | α₃β₃ hexameric architecture; soluble enzyme |
| [16000792](https://pubmed.ncbi.nlm.nih.gov/16000792/) | Parales et al. 2005 — nitrobenzene/2NT dioxygenases | Confirms α₃β₃ oxygenase composition and reductase/ferredoxin cofactor content in the family |
| [16005887](https://pubmed.ncbi.nlm.nih.gov/16005887/) | Nojiri et al. 2005 — carbazole 1,9a-dioxygenase | α₃-only enzyme needs special loops "indispensable for stable alpha3 interactions without structural beta subunits" → proves β subunit's structural role |
| [7530709](https://pubmed.ncbi.nlm.nih.gov/7530709/) | Haak et al. 1995 — 2-halobenzoate dioxygenase | Reductase (BenC homolog CbdC) contains FAD + [2Fe-2S]; defines the electron-transfer partner |
| [11673430](https://pubmed.ncbi.nlm.nih.gov/11673430/) | Kitagawa et al. 2001 — RHA1 *benABCD* | Full route benzoate → cis-dihydrodiol → catechol reconstituted in *E. coli* |
| [20137101](https://pubmed.ncbi.nlm.nih.gov/20137101/) | Li et al. 2010 — β-ketoadipate pathway in *P. stutzeri* | BenR is a transcriptional activator of the *ben* operon |
| [11053377](https://pubmed.ncbi.nlm.nih.gov/11053377/) | Cowles, Nichols & Harwood 2000 — BenR in *P. putida* | Primary *P. putida* study: *benABC* = benzoate dioxygenase; benzoate-induced, BenR (XylS/AraC-family) activation |
| [18156252](https://pubmed.ncbi.nlm.nih.gov/18156252/) | Moreno & Rojo 2008 — Crc target in benzoate pathway | Crc represses *benABCD* mRNA via *benR* translation (catabolite repression) |
| [22925411](https://pubmed.ncbi.nlm.nih.gov/22925411/) | Hernández-Arranz et al. 2013 — Crc multi-tier control | Crc inhibits translation of the activator *and* the structural genes *and* the uptake gene |

**Convergence of evidence:** The identification of BenB as a structural β subunit rests on three mutually reinforcing lines: (1) direct biochemistry of the *ben* cluster showing a 19-kDa β subunit [PMID: 2824437]; (2) structural biology of the entire RHO family placing all catalytic function in the α subunit and assigning the β subunit a stabilizing role [PMID: 15746362, 12695887, 16005887]; and (3) genome verification of the KT2440 operon with subunit sizes matching the historical proteins (Finding 6). No evidence in the reviewed literature contradicts the structural (non-catalytic) role of BenB.

---

## Limitations and Knowledge Gaps

1. **No BenB-specific experimental structure or mutagenesis.** There is no published crystal structure of the *P. putida* KT2440 benzoate dioxygenase itself, and no dedicated BenB knockout/point-mutation study isolating its structural contribution. BenB's role is inferred from close homologs (naphthalene, nitrobenzene, biphenyl, toluate dioxygenases) rather than from the KT2440 enzyme directly. The inference is strong (61.3% identity to XylY; conserved α₃β₃ architecture across the family) but remains homology-based.

2. **Direct kinetics for the KT2440 enzyme are lacking.** Substrate-specificity and turnover parameters (K_m, k_cat) for the purified KT2440 BenABC system have not been reported in the reviewed literature; the narrow-specificity conclusion derives from comparative genetics with the TOL/Xyl system rather than side-by-side kinetics of the chromosomal enzyme.

3. **Cofactor content of BenC not directly measured for KT2440.** The FAD + [2Fe-2S] assignment for BenC rests on homology to CbdC (52% identity) [PMID: 7530709], not on direct spectroscopy of the KT2440 reductase.

4. **Localization is inferred, not imaged.** The cytoplasmic assignment follows from solubility, cofactor logic, and absence of targeting signals, but has not been demonstrated by fractionation or microscopy for this specific protein.

5. **Possible functional interplay with other aromatic pathways.** *P. putida* KT2440 encodes multiple aromatic-degradation modules (e.g., the *lig* operons, protocatechuate branch). How benzoate flux via BenAB integrates with these under mixed-substrate conditions is only partly understood.

---

## Proposed Follow-up Experiments / Actions

1. **Solve or model the KT2440 BenAB oxygenase structure.** An experimental cryo-EM/crystal structure — or, at minimum, an AlphaFold-Multimer α₃β₃ model validated against family templates — would directly confirm BenB's inter-subunit contacts and NTF2-like fold and localize the α/β interface. (Phenix `phenix.superpose_pdbs` / `phenix.molprobity` could validate any model against solved homologs such as naphthalene dioxygenase.)

2. **Targeted *benB* mutagenesis.** Construct a clean *benB* deletion and interface point mutants in KT2440; assay benzoate dioxygenase activity and oxygenase assembly (size-exclusion/native-PAGE) to quantify BenB's contribution to hexamer stability and catalysis — the missing direct test of the structural-subunit hypothesis.

3. **Reconstitute and kinetically characterize the purified KT2440 BenABC system.** Measure K_m/k_cat for benzoate and a panel of substituted benzoates to define substrate specificity directly and contrast quantitatively with toluate dioxygenase (XylXYZ).

4. **Spectroscopic cofactor confirmation of BenC.** Purify BenC and confirm FAD and [2Fe-2S] content by UV-vis/EPR, and reconstitute the full electron-transfer chain in vitro.

5. **Localization confirmation.** Use cell fractionation and/or a fluorescent fusion to confirm cytoplasmic localization of BenAB.

6. **Systems-level flux analysis.** Under mixed carbon sources, use transcriptomics/proteomics to map how Crc-mediated repression tunes BenB (and operon) expression, integrating benzoate catabolism with competing aromatic pathways — relevant to lignin-valorization and bioremediation applications of KT2440.

---

## Conclusion

The gene symbol *benB* is **not ambiguous** in *Pseudomonas putida* KT2440: all evidence converges on **PP_3162 / Q88I39 encoding the β (small) subunit of benzoate 1,2-dioxygenase**. Its function is **structural** — it is a non-catalytic, NTF2-like scaffolding subunit that, in three copies alongside three copies of the catalytic α subunit BenA, forms the α₃β₃ terminal oxygenase. Fueled by NADH via the BenC reductase, this soluble cytoplasmic enzyme catalyzes the first committed step of aerobic benzoate catabolism — the *cis*-dihydroxylation of benzoate to benzoate *cis*-1,2-dihydrodiol — which is oxidized by BenD to catechol and channeled through the β-ketoadipate pathway to the TCA cycle. Expression of *benB* is benzoate-induced (BenR) and carbon-catabolite-repressed (Crc). BenB itself contributes no metal center, catalytic residue, or substrate-specificity determinant; its role is to stabilize the active oligomeric oxygenase.


## Artifacts

- [OpenScientist final report](benB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](benB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:2824437
2. PMID:18679676
3. PMID:12695887
4. PMID:16000792
5. PMID:15746362
6. PMID:16005887
7. PMID:1938949
8. PMID:7530709
9. PMID:11673430
10. PMID:20137101
11. PMID:11053377
12. PMID:18156252
13. PMID:22925411