---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-24T02:17:50.944093'
end_time: '2026-09-24T02:26:57.159715'
duration_seconds: 546.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: SSK2
  gene_symbol: SSK2
  uniprot_accession: P53599
  protein_description: 'RecName: Full=MAP kinase kinase kinase SSK2; EC=2.7.11.25;
    AltName: Full=Suppressor of sensor kinase 2;'
  gene_info: Name=SSK2; OrderedLocusNames=YNR031C; ORFNames=N3276;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the protein kinase superfamily. STE Ser/Thr
  protein_domains: Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase_kinase. (IPR050538);
    MAPKKK_Ssk2/Ssk22. (IPR017240); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS.
    (IPR017441)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: SSK2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P53599
- **Protein Description:** RecName: Full=MAP kinase kinase kinase SSK2; EC=2.7.11.25; AltName: Full=Suppressor of sensor kinase 2;
- **Gene Information:** Name=SSK2; OrderedLocusNames=YNR031C; ORFNames=N3276;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. STE Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase_kinase. (IPR050538); MAPKKK_Ssk2/Ssk22. (IPR017240); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SSK2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SSK2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SSK2** (gene ID: SSK2, UniProt: P53599) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P53599
- **Protein Description:** RecName: Full=MAP kinase kinase kinase SSK2; EC=2.7.11.25; AltName: Full=Suppressor of sensor kinase 2;
- **Gene Information:** Name=SSK2; OrderedLocusNames=YNR031C; ORFNames=N3276;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. STE Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase_kinase. (IPR050538); MAPKKK_Ssk2/Ssk22. (IPR017240); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SSK2" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SSK2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SSK2** (gene ID: SSK2, UniProt: P53599) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Saccharomyces cerevisiae* SSK2

## Executive summary

The requested target is correctly identified as **SSK2/YNR031C**, encoding the budding-yeast MAP kinase kinase kinase **Ssk2** (UniProt **P53599**) in *Saccharomyces cerevisiae* strain S288c. Its experimentally established architecture—an extended N-terminal regulatory region and a C-terminal STE-family Ser/Thr protein-kinase domain—matches the supplied UniProt family and InterPro annotations. Papers concerning SSK2 homologs in *Candida albicans*, *Cryptococcus neoformans*, or plant-pathogenic fungi were not used as direct evidence for this protein.

Ssk2 is principally an **ATP-dependent MAP3K in the Sln1 branch of the high-osmolarity glycerol (HOG) pathway**. Hyperosmotic stress suppresses the Sln1–Ypd1 phosphorelay, allowing unphosphorylated Ssk1 to bind and activate Ssk2. Activated Ssk2 autophosphorylates and then phosphorylates the MAP2K Pbs2; Pbs2 activates Hog1, which coordinates glycerol accumulation and broader osmoadaptation. Direct biochemical evidence identifies Pbs2 as the primary established Ssk2 substrate. Ssk2 also has a spatially localized role in actin repolarization after osmotic shock and a distinct, nonredundant contribution to tunicamycin-induced ER-stress resistance.

A central interpretive qualification is that many modern experiments analyze **Ssk2 and its paralog Ssk22 together**. Consequently, Pbs2 Ser514/Thr518 site specificity is securely assigned to the **Ssk2/Ssk22 branch**, but not uniquely to Ssk2.

## 1. Identity verification

The gene symbol, locus, organism, protein class, and pathway all agree:

- **Gene:** *SSK2*; systematic locus **YNR031C**.
- **Protein:** suppressor of sensor kinase 2/Ssk2; UniProt **P53599**.
- **Organism:** *S. cerevisiae* S288c, baker’s yeast.
- **Protein class:** STE-family Ser/Thr MAP kinase kinase kinase, EC 2.7.11.25.
- **Architecture:** a large N-terminal regulatory/autoinhibitory region coupled to a C-terminal catalytic kinase domain. Direct mutational studies place Ssk1-responsive regulatory determinants in the N-terminal portion and catalytic/activation determinants near the C terminus, consistent with the supplied protein-kinase, MAP3K, and Ssk2/Ssk22-family annotations (posas1998activationofthe pages 3-5, posas1998activationofthe pages 6-8, posas1998activationofthe pages 1-2).

No conflicting *S. cerevisiae* protein bearing the same symbol was found. However, **SSK2 is not organism-unique as a name**: homologs are extensively studied in pathogenic fungi. Findings from those proteins cannot automatically be transferred to P53599.

## 2. Primary molecular function and reaction

### 2.1 Catalytic activity

Ssk2 catalyzes protein phosphorylation:

**ATP + Pbs2 protein → ADP + phospho-Pbs2 protein.**

Purified Ssk2 phosphorylated catalytically inactive Pbs2 in vitro, demonstrating a direct enzyme–substrate relationship rather than merely genetic pathway ordering. An Ssk2 **K1295N** catalytic mutant lacked detectable activity. Alkaline-phosphatase treatment inactivated Ssk2, and Ssk2 could undergo predominantly intramolecular autophosphorylation, indicating that phosphorylation is integral to its active state (posas1998activationofthe pages 3-5, posas1998activationofthe pages 6-8).

The activation-loop residue **Thr1460** is especially important: T1460A strongly reduced in-vitro activity and failed to complement osmosensitivity, whereas T1420A retained substantial activity and complementation. Thus, Thr1460 is a functionally critical activation determinant, although the evidence does not imply that it is Ssk2’s only regulatory phosphorylation site (posas1998activationofthe pages 6-8).

### 2.2 Substrate specificity

The best-established physiological downstream substrate is the MAP2K **Pbs2**. Specificity is strengthened by a docking interface in Pbs2 that binds the kinase domains of Ssk2/Ssk22. Mutation of this docking determinant reduced interaction and Hog1-pathway output, while transferring it to another MAP2K conferred recognition by Ssk2/Ssk22. This demonstrates that substrate selection depends on docking as well as kinase active-site recognition (tatebayashi2003adockingsite pages 1-2).

Later studies resolved the Pbs2 activation-loop sites. Under suitable osmostress conditions, the **Ssk2/Ssk22 pair can phosphorylate Pbs2 Ser514 and Thr518**, whereas Ste11 chiefly phosphorylates Thr518. Diphosphorylated Pbs2 can activate Hog1 without the additional osmotic enhancement required by Thr518-monophosphorylated Pbs2. Because these experiments generally combine or retain redundant Ssk2/Ssk22 activities, they do **not** prove that Ssk2 alone phosphorylates both residues under every condition (tatebayashi2023twoactivatingphosphorylation pages 1-2, tatebayashi2020osmostressenhancesactivating pages 1-2).

## 3. Pathway position and activation mechanism

### 3.1 Canonical Sln1–Ypd1–Ssk1 input

Under low-stress conditions, the Sln1 histidine kinase maintains a phosphorelay through Ypd1 to Ssk1. Phosphorylated Ssk1 is inactive toward Ssk2. Hyperosmotic stress decreases this relay, producing unphosphorylated Ssk1, which binds the N-terminal regulatory region of Ssk2 and relieves autoinhibition. Ssk2 then autophosphorylates and phosphorylates Pbs2; Pbs2 activates Hog1 (posas1998activationofthe pages 1-2, horie2008phosphorylatedssk1prevents pages 1-2).

Direct measurements support this model. Hyperosmotic shock increased Ssk2 phosphorylation by approximately **tenfold**; *ssk1Δ* prevented this increase, whereas *sln1Δ* caused constitutive Ssk2 phosphorylation. Deletion of Ssk2 residues 302–414 disrupted stress-induced phosphorylation, supporting a regulatory interaction in this region. The data support a two-step mechanism: Ssk1 binding first exposes latent Ssk2 activity, after which autophosphorylation stabilizes an active state that no longer requires persistent Ssk1 association (posas1998activationofthe pages 3-5, posas1998activationofthe pages 6-8).

Phosphorylated Ssk1 also restrains signaling by associating with unphosphorylated Ssk1, thereby preventing formation of the activating Ssk1 species or complex. This provides a mechanism by which the phosphorelay controls Ssk2 without directly phosphorylating Ssk2 (horie2008phosphorylatedssk1prevents pages 10-11).

### 3.2 Relationship to Ssk22 and Ste11

Ssk2 and **Ssk22** are substantially redundant MAP3Ks in the Sln1 branch. This redundancy explains why deletion of *SSK2* alone may yield a limited canonical HOG phenotype and why combined *ssk2Δ ssk22Δ* genotypes are commonly used. In parallel, the Sho1 branch signals through the MAP3K **Ste11**. Both branches converge on Pbs2 but differ mechanistically: Ssk2/Ssk22 can generate doubly phosphorylated Pbs2, whereas Ste11 preferentially generates Thr518-monophosphorylated Pbs2 (horie2008phosphorylatedssk1prevents pages 1-2, tatebayashi2023twoactivatingphosphorylation pages 1-2, tatebayashi2020osmostressenhancesactivating pages 1-2).

Ssk2 is not completely interchangeable with Ssk22. A strong but short-lived **Ssk1-independent Ssk2 activation route**, requiring an N-terminal segment around residues 177–240, contributes to salt resistance. In the same study Ssk22 activation remained Ssk1-dependent, indicating a genuine paralog-specific input whose upstream regulator remains incompletely defined (zhi2013ssk1pindependentactivationof pages 1-2).

## 4. Biological process and physiological output

Ssk2’s primary biological role is to transmit hyperosmotic-stress information into the HOG cascade. Activated Hog1 then coordinates osmoadaptation, including changes in transcription, translation, cell-cycle progression, metabolism, and glycerol production/retention. These broad outputs are downstream consequences; Ssk2’s precise proximal role is narrower—**activation of Pbs2 at the MAP3K tier**.

Genetic interpretation requires redundancy-aware backgrounds. Combined removal of Ssk2/Ssk22, particularly when the parallel Sho1–Ste11 branch is also disabled, causes defective Hog1 activation and osmosensitivity. Conversely, constitutive Ssk2 activity can drive inappropriate HOG output, consistent with the pathway’s need for N-terminal autoinhibition and phosphorelay control (posas1998activationofthe pages 6-8, horie2008phosphorylatedssk1prevents pages 10-11).

Ssk2 also supports post-shock actin repolarization and bud emergence. This function depends on Ssk2 catalytic activity but can be partly separable from canonical Ssk1 signaling, providing a mechanistic connection between osmotic sensing and polarized growth (horie2008phosphorylatedssk1prevents pages 10-11, walia2008thessk2mapkkk pages 1-2).

## 5. Subcellular localization

Ssk2 is an intracellular, dynamically localized signaling kinase rather than a transmembrane receptor or secreted protein. Cell-biological studies report stress-associated enrichment at the **mother–bud neck**, followed by redistribution through the **cytosol**. Associations with the polarity scaffold Spa2 and septin Shs1 connect this localization to actin recovery and bud emergence after osmotic shock (walia2008thessk2mapkkk pages 1-2).

This localized polarity function should be distinguished from downstream Hog1 nuclear translocation. The best-supported interpretation is that Ssk2 performs its kinase and cytoskeletal functions in the cytoplasm and at cortical/bud-neck signaling assemblies; evidence does not support describing Ssk2 itself as a constitutively nuclear kinase.

## 6. Recent developments, 2023–2024

### 6.1 Differential reversal of Pbs2 phosphorylation—2023

Tatebayashi and Saito, published **April 2023**, refined signal termination downstream of Ssk2/Ssk22. Four PP2C phosphatases, Ptc1–Ptc4, dephosphorylate Pbs2 asymmetrically: Ptc1 is the principal Thr518 phosphatase and acts with Nbp2, whereas Ser514 can be appreciably dephosphorylated by any of the four. This explains how the distinct phosphorylation state generated by the Ssk2/Ssk22 branch is decoded and reversed. It does not demonstrate direct dephosphorylation of Ssk2 itself. DOI: https://doi.org/10.1016/j.jbc.2023.104569 (tatebayashi2023twoactivatingphosphorylation pages 1-2).

### 6.2 Branch dynamics and MAPK crosstalk—2024

Zhang and colleagues, published **October 2024**, showed that the nominally redundant Sln1 and Sho1 branches make complementary contributions to Hog1 dynamics and signaling crosstalk. Across **0–550 mM KCl**, *ssk1Δ* cells showed stronger responses than wild type at the highest concentrations, while *sho1Δ* cells responded somewhat less; *ssk1Δ* also delayed Hog1 nuclear entry and exit. The work associates the Sln1 branch with amplitude control and the Sho1 branch with normal response duration and cross-pathway coordination. Because these experiments manipulate *SSK1* rather than *SSK2* alone, their conclusions are branch-level, not proof of an Ssk2-specific property. DOI: https://doi.org/10.1091/mbc.e24-06-0270 (zhang2024sharedandredundant pages 4-5).

Recent reviews also emphasize HOG, cell-wall-integrity, and cAMP–PKA crosstalk in industrially relevant osmotic and thermal stress. Nevertheless, direct Ssk2-specific mechanistic advances in 2023–2024 were limited; foundational studies remain the strongest evidence for Ssk2 activation and catalysis.

## 7. Additional and noncanonical functions

A 2022 study found that Ssk2 contributes to resistance against tunicamycin-induced **endoplasmic-reticulum stress**, whereas Ssk22 does not. Mutating either of two Pbs2 determinants involved in Ssk2 docking produced partial effects, but disrupting both caused strong tunicamycin sensitivity. The authors inferred that an assembled Sln1-branch/MAPK complex has a noncanonical scaffolding function in ER-stress adaptation, not simply ordinary osmotic Hog1 activation. Published **May 2022**; DOI: https://doi.org/10.1007/s10123-022-00250-z (hernandezelvira2022theyeasttwocomponenta pages 1-4).

This is important functional evidence, but it should remain secondary to Ssk2’s primary annotation as the Sln1-branch MAP3K for Pbs2.

## 8. Applications and real-world relevance

There is no established clinical or commercial implementation that directly targets or engineers *S. cerevisiae* Ssk2 as a standalone product. Its practical relevance is instead as:

1. **A model of eukaryotic stress-MAPK signaling.** The Ssk1–Ssk2–Pbs2 module provides a tractable system for studying receptor-to-MAP3K coupling, autoinhibition, docking-mediated specificity, feedback, and signal termination.
2. **A framework for industrial yeast stress biology.** Fermentation exposes yeast to osmotic pressure, temperature shifts, ethanol, nutrient limitation, and other stresses. Understanding HOG signaling can guide strain selection or engineering, although increasing Ssk2 activity alone may be counterproductive because correct timing, feedback, and branch balance are important.
3. **A comparative fungal-biology reference.** Ssk2-like MAP3Ks regulate stress adaptation and virulence in several pathogenic fungi. Those homologs may be antifungal targets, but such applications are comparative extensions and should not be presented as direct functions of P53599.
4. **A synthetic- and systems-biology component.** Branch-specific Pbs2 phosphorylation and measurable Hog1 dynamics make the pathway useful for quantitative modeling and synthetic circuit design.

## 9. Evidence assessment and remaining uncertainties

The strongest Ssk2-specific conclusions are supported by direct interaction assays, purified-kinase experiments, phosphatase treatment, catalytic mutants, activation-loop mutants, and genetics. The strongest quantitative observation is the roughly **tenfold** stress-induced increase in Ssk2 phosphorylation. Other useful quantitative contexts include weak Ste11-dependent Hog1 activation over approximately **0.8–1.6 M NaCl** when Ssk2/Ssk22 are absent and modern branch-response experiments spanning **0–550 mM KCl** (posas1998activationofthe pages 3-5, tatebayashi2020osmostressenhancesactivating pages 1-2, zhang2024sharedandredundant pages 4-5).

Important uncertainties remain:

- The exact contribution of Ssk2 versus Ssk22 to phosphorylation of Pbs2 Ser514 and Thr518 has not been fully resolved under all conditions.
- The regulator responsible for Ssk1-independent Ssk2 activation remains incompletely identified.
- Localization evidence is consistent with dynamic bud-neck/cytosolic recruitment, but a high-resolution, condition-resolved localization map is lacking.
- Several reported broad phenotypes are HOG-pathway or double-mutant effects and should not be annotated as unique direct functions of Ssk2.

The evidence hierarchy and scope are summarized below.

| Topic | Best-supported conclusion | Evidence type/scope | Key source, date, DOI |
|---|---|---|---|
| Identity and domain fit | The target is budding-yeast **Ssk2**, encoded by **SSK2/YNR031C** and corresponding to UniProt **P53599**. Its experimentally demonstrated N-terminal regulatory region and C-terminal Ser/Thr kinase region agree with classification as a STE-family MAP kinase kinase kinase in the HOG pathway. Studies of identically named proteins in *Candida*, *Cryptococcus*, and other fungi are not evidence for this protein. | **Ssk2-specific** biochemical/domain evidence; accession and locus identity supplied by UniProt context | Posas & Saito, March 1998, [10.1093/emboj/17.5.1385](https://doi.org/10.1093/emboj/17.5.1385) (posas1998activationofthe pages 6-8, posas1998activationofthe pages 1-2) |
| Catalytic reaction and substrate | Ssk2 is an ATP-dependent protein Ser/Thr kinase whose primary established downstream substrate is the MAP2K **Pbs2**: purified Ssk2 phosphorylated kinase-dead Pbs2 in vitro. Ssk2 **K1295N** lacked detectable activity, and activation-loop **Thr1460** was required for robust kinase activity and osmotic-stress complementation. | **Direct, Ssk2-specific** biochemical and genetic evidence | Posas & Saito, March 1998, [10.1093/emboj/17.5.1385](https://doi.org/10.1093/emboj/17.5.1385) (posas1998activationofthe pages 6-8) |
| Activation by Ssk1 and autophosphorylation | Hyperosmotic stress generates unphosphorylated Ssk1, which binds the Ssk2 N-terminal regulatory region, relieves autoinhibition, and permits predominantly intramolecular Ssk2 autophosphorylation. Osmotic shock increased Ssk2 phosphorylation about **tenfold**; this induction was lost in *ssk1Δ* and became constitutive in *sln1Δ*. | **Direct, Ssk2-specific** interaction, phosphorylation, biochemical, and genetic evidence | Posas & Saito, March 1998, [10.1093/emboj/17.5.1385](https://doi.org/10.1093/emboj/17.5.1385) (posas1998activationofthe pages 3-5, posas1998activationofthe pages 6-8) |
| Pbs2 docking and substrate specificity | A docking determinant in Pbs2 binds the kinase domains of Ssk2/Ssk22 and promotes selective phosphorylation and HOG-pathway activation; transferring this determinant to another MAP2K conferred recognition by Ssk2/Ssk22. | **Ssk2/Ssk22-combined**, not uniquely attributable to Ssk2 | Tatebayashi, Takekawa & Saito, July 2003, [10.1093/emboj/cdg353](https://doi.org/10.1093/emboj/cdg353) (tatebayashi2003adockingsite pages 1-2) |
| Pbs2 Ser514/Thr518 sites | Under appropriate osmostress conditions, **Ssk2/Ssk22 can phosphorylate both Pbs2 Ser514 and Thr518**, whereas Ste11 primarily phosphorylates Thr518. Diphosphorylated Pbs2 can activate Hog1 without an additional osmotic enhancement, unlike Thr518-only Pbs2. These data establish branch-level site specificity but do not prove that Ssk2 alone phosphorylates both sites. | **Ssk2/Ssk22-combined** biochemical/genetic evidence | Tatebayashi et al., February 2020, [10.15252/embj.2019103444](https://doi.org/10.15252/embj.2019103444); Tatebayashi & Saito, April 2023, [10.1016/j.jbc.2023.104569](https://doi.org/10.1016/j.jbc.2023.104569) (tatebayashi2023twoactivatingphosphorylation pages 1-2, tatebayashi2020osmostressenhancesactivating pages 1-2) |
| Localization and actin recovery | Following osmotic stress, Ssk2 was reported to concentrate at the **bud neck** and subsequently redistribute through the cytosol; associations with the polarity scaffold Spa2 and septin Shs1 support a localized role in actin repolarization and bud emergence. Localization is therefore dynamic rather than evidence for residence in a membrane-bound organelle. | **Ssk2-specific** cell-biological evidence, summarized from the actin-recovery literature | Yuzyuk & Amberg, July 2003, [10.1091/mbc.e02-11-0747](https://doi.org/10.1091/mbc.e02-11-0747) (walia2008thessk2mapkkk pages 1-2) |
| Redundancy and alternative activation | Ssk2 and Ssk22 are substantially redundant in canonical Sln1-branch osmotic signaling, so many deletion phenotypes require loss of both. However, Ssk2 can also undergo a strong, short-lived **Ssk1-independent** activation involving residues **177–240** and contributing to salt resistance; Ssk22 was reported to remain Ssk1-dependent. | Redundancy: **Ssk2/Ssk22-combined**; alternative activation: **Ssk2-specific** genetic/functional evidence | Zhi et al., February 2013, [10.1371/journal.pone.0054867](https://doi.org/10.1371/journal.pone.0054867) (zhi2013ssk1pindependentactivationof pages 1-2) |
| ER-stress role | During tunicamycin-induced ER stress, Ssk2 contributes to resistance whereas Ssk22 does not. Simultaneously disrupting the RDS-I and kinase-domain docking determinants that support Ssk2–Pbs2 binding caused strong tunicamycin sensitivity, suggesting a noncanonical requirement for an assembled signaling complex rather than ordinary osmotic output alone. | **Ssk2-specific** genetic/docking evidence for ER stress; broader complex includes SLN1-branch proteins | Hernández-Elvira et al., May 2022, [10.1007/s10123-022-00250-z](https://doi.org/10.1007/s10123-022-00250-z) (hernandezelvira2022theyeasttwocomponenta pages 1-4) |
| 2023 development: signal termination | Four PP2C phosphatases reverse Pbs2 activation: Ptc1 preferentially dephosphorylates Thr518 with Nbp2 assistance, whereas Ser514 can be dephosphorylated appreciably by Ptc1–Ptc4. This refines how output from the Ssk2/Ssk22 branch is terminated but does not identify direct phosphatase control of Ssk2 itself. | **Downstream/branch-level** evidence | Tatebayashi & Saito, April 2023, [10.1016/j.jbc.2023.104569](https://doi.org/10.1016/j.jbc.2023.104569) (tatebayashi2023twoactivatingphosphorylation pages 1-2) |
| 2024 development: branch dynamics and crosstalk | Experiments across **0–550 mM KCl** showed that the Sln1 and Sho1 branches are not merely interchangeable: Sln1-branch perturbation altered Hog1 response amplitude, transcription, and nuclear-entry/exit kinetics, while the Sho1 branch strongly influenced duration and MAPK-pathway crosstalk. Because these experiments manipulated *SSK1* or *SHO1*, they cannot be assigned specifically to Ssk2. | **Branch-level**, not Ssk2-specific | Zhang et al., October 2024, [10.1091/mbc.e24-06-0270](https://doi.org/10.1091/mbc.e24-06-0270) (zhang2024sharedandredundant pages 4-5) |


*Table: Evidence supporting functional annotation of S. cerevisiae Ssk2, with explicit separation of Ssk2-specific results from combined-paralog and branch-level findings. This distinction prevents Ssk2/Ssk22 observations from being overinterpreted as properties demonstrated uniquely for Ssk2.*

## Conclusion

The most defensible functional annotation is: **Ssk2 is a dynamically regulated cytoplasmic/bud-neck STE-family MAP3K that receives input principally from unphosphorylated Ssk1, activates itself by autophosphorylation, and directly phosphorylates the MAP2K Pbs2 to initiate Hog1-dependent osmoadaptation.** Pbs2 is its primary established physiological substrate. Ssk2 overlaps strongly with Ssk22 in canonical osmosignaling but has distinguishable roles in Ssk1-independent activation, actin recovery, and ER-stress resistance. Recent research has mainly refined downstream Pbs2 phosphoregulation and whole-branch signaling dynamics rather than changing this core annotation.

References

1. (posas1998activationofthe pages 3-5): F. Posas and H. Saito. Activation of the yeast ssk2 map kinase kinase kinase by the ssk1 two‐component response regulator. The EMBO Journal, 17:1385-1394, Mar 1998. URL: https://doi.org/10.1093/emboj/17.5.1385, doi:10.1093/emboj/17.5.1385. This article has 407 citations.

2. (posas1998activationofthe pages 6-8): F. Posas and H. Saito. Activation of the yeast ssk2 map kinase kinase kinase by the ssk1 two‐component response regulator. The EMBO Journal, 17:1385-1394, Mar 1998. URL: https://doi.org/10.1093/emboj/17.5.1385, doi:10.1093/emboj/17.5.1385. This article has 407 citations.

3. (posas1998activationofthe pages 1-2): F. Posas and H. Saito. Activation of the yeast ssk2 map kinase kinase kinase by the ssk1 two‐component response regulator. The EMBO Journal, 17:1385-1394, Mar 1998. URL: https://doi.org/10.1093/emboj/17.5.1385, doi:10.1093/emboj/17.5.1385. This article has 407 citations.

4. (tatebayashi2003adockingsite pages 1-2): K. Tatebayashi, M. Takekawa, and H. Saito. A docking site determining specificity of pbs2 mapkk for ssk2/ssk22 mapkkks in the yeast hog pathway. The EMBO Journal, 22:3624-3634, Jul 2003. URL: https://doi.org/10.1093/emboj/cdg353, doi:10.1093/emboj/cdg353. This article has 142 citations.

5. (tatebayashi2023twoactivatingphosphorylation pages 1-2): Kazuo Tatebayashi and Haruo Saito. Two activating phosphorylation sites of pbs2 map2k in the yeast hog pathway are differentially dephosphorylated by four pp2c phosphatases ptc1–ptc4. Journal of Biological Chemistry, 299:104569, Apr 2023. URL: https://doi.org/10.1016/j.jbc.2023.104569, doi:10.1016/j.jbc.2023.104569. This article has 23 citations and is from a domain leading peer-reviewed journal.

6. (tatebayashi2020osmostressenhancesactivating pages 1-2): Kazuo Tatebayashi, Katsuyoshi Yamamoto, Taichiro Tomida, Akiko Nishimura, Tomomi Takayama, Masaaki Oyama, Hiroko Kozuka‐Hata, Satomi Adachi‐Akahane, Yuji Tokunaga, and Haruo Saito. Osmostress enhances activating phosphorylation of hog1 map kinase by mono‐phosphorylated pbs2 map2k. The EMBO Journal, Feb 2020. URL: https://doi.org/10.15252/embj.2019103444, doi:10.15252/embj.2019103444. This article has 74 citations.

7. (horie2008phosphorylatedssk1prevents pages 1-2): Tetsuro Horie, Kazuo Tatebayashi, Rika Yamada, and Haruo Saito. Phosphorylated ssk1 prevents unphosphorylated ssk1 from activating the ssk2 mitogen-activated protein kinase kinase kinase in the yeast high-osmolarity glycerol osmoregulatory pathway. Sep 2008. URL: https://doi.org/10.1128/mcb.00589-08, doi:10.1128/mcb.00589-08. This article has 64 citations and is from a domain leading peer-reviewed journal.

8. (horie2008phosphorylatedssk1prevents pages 10-11): Tetsuro Horie, Kazuo Tatebayashi, Rika Yamada, and Haruo Saito. Phosphorylated ssk1 prevents unphosphorylated ssk1 from activating the ssk2 mitogen-activated protein kinase kinase kinase in the yeast high-osmolarity glycerol osmoregulatory pathway. Sep 2008. URL: https://doi.org/10.1128/mcb.00589-08, doi:10.1128/mcb.00589-08. This article has 64 citations and is from a domain leading peer-reviewed journal.

9. (zhi2013ssk1pindependentactivationof pages 1-2): Hui Zhi, Leihan Tang, Yiji Xia, and Jianhua Zhang. Ssk1p-independent activation of ssk2p plays an important role in the osmotic stress response in saccharomyces cerevisiae: alternative activation of ssk2p in osmotic stress. PLoS ONE, 8:e54867, Feb 2013. URL: https://doi.org/10.1371/journal.pone.0054867, doi:10.1371/journal.pone.0054867. This article has 21 citations and is from a peer-reviewed journal.

10. (walia2008thessk2mapkkk pages 1-2): Aditi Walia and Richard Calderone. The ssk2 mapkkk of candida albicans is required for oxidant adaptation in vitro. FEMS yeast research, 8 2:287-99, Mar 2008. URL: https://doi.org/10.1111/j.1567-1364.2007.00329.x, doi:10.1111/j.1567-1364.2007.00329.x. This article has 10 citations and is from a peer-reviewed journal.

11. (zhang2024sharedandredundant pages 4-5): Shu Zhang, Hao Wang, Emily L. Sipko, Shuang Li, Timothy A. Daugird, Wesley R. Legant, and Henrik G. Dohlman. Shared and redundant proteins coordinate signal cross-talk between mapk pathways in yeast. Molecular Biology of the Cell, Oct 2024. URL: https://doi.org/10.1091/mbc.e24-06-0270, doi:10.1091/mbc.e24-06-0270. This article has 6 citations and is from a domain leading peer-reviewed journal.

12. (hernandezelvira2022theyeasttwocomponenta pages 1-4): Mariana Hernández-Elvira, Griselda Salas-Delgado, Laura Kawasaki, Eunice Domínguez-Martin, Uriel Cruz-Martínez, Abiram E. Olivares, Francisco Torres-Quiroz, Laura Ongay-Larios, and Roberto Coria. The yeast two-component sln1 pathway and the scaffolding activity of pbs2 modulate the response to endoplasmic reticulum stress induced by tunicamycin. Unknown journal, Feb 2022. URL: https://doi.org/10.21203/rs.3.rs-1347118/v1, doi:10.21203/rs.3.rs-1347118/v1.

## Artifacts

- [Edison artifact artifact-00](SSK2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. posas1998activationofthe pages 6-8
2. tatebayashi2003adockingsite pages 1-2
3. tatebayashi2023twoactivatingphosphorylation pages 1-2
4. zhang2024sharedandredundant pages 4-5
5. hernandezelvira2022theyeasttwocomponenta pages 1-4
6. posas1998activationofthe pages 3-5
7. posas1998activationofthe pages 1-2
8. tatebayashi2020osmostressenhancesactivating pages 1-2
9. 10.1093/emboj/17.5.1385
10. 10.1093/emboj/cdg353
11. 10.15252/embj.2019103444
12. 10.1016/j.jbc.2023.104569
13. 10.1091/mbc.e02-11-0747
14. 10.1371/journal.pone.0054867
15. 10.1007/s10123-022-00250-z
16. 10.1091/mbc.e24-06-0270
17. https://doi.org/10.1016/j.jbc.2023.104569
18. https://doi.org/10.1091/mbc.e24-06-0270
19. https://doi.org/10.1007/s10123-022-00250-z
20. https://doi.org/10.1093/emboj/17.5.1385
21. https://doi.org/10.1093/emboj/cdg353
22. https://doi.org/10.15252/embj.2019103444
23. https://doi.org/10.1091/mbc.e02-11-0747
24. https://doi.org/10.1371/journal.pone.0054867
25. https://doi.org/10.1093/emboj/17.5.1385,
26. https://doi.org/10.1093/emboj/cdg353,
27. https://doi.org/10.1016/j.jbc.2023.104569,
28. https://doi.org/10.15252/embj.2019103444,
29. https://doi.org/10.1128/mcb.00589-08,
30. https://doi.org/10.1371/journal.pone.0054867,
31. https://doi.org/10.1111/j.1567-1364.2007.00329.x,
32. https://doi.org/10.1091/mbc.e24-06-0270,
33. https://doi.org/10.21203/rs.3.rs-1347118/v1,