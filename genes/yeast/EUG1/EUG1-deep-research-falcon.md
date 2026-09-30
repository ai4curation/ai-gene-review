---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-08T14:42:10.656064'
end_time: '2026-08-08T14:50:48.693139'
duration_seconds: 518.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: EUG1
  gene_symbol: EUG1
  uniprot_accession: P32474
  protein_description: 'RecName: Full=Protein disulfide-isomerase EUG1; Short=PDI;
    EC=5.3.4.1; AltName: Full=Endoplasmic reticulum protein EUG1; Flags: Precursor;'
  gene_info: Name=EUG1; OrderedLocusNames=YDR518W; ORFNames=D9719.23;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the protein disulfide isomerase family.
  protein_domains: Prot_disulphide_isomerase. (IPR005792); Thioredoxin-like_sf. (IPR036249);
    Thioredoxin_domain. (IPR013766); Thioredoxin (PF00085); Thioredoxin_6 (PF13848)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: EUG1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P32474
- **Protein Description:** RecName: Full=Protein disulfide-isomerase EUG1; Short=PDI; EC=5.3.4.1; AltName: Full=Endoplasmic reticulum protein EUG1; Flags: Precursor;
- **Gene Information:** Name=EUG1; OrderedLocusNames=YDR518W; ORFNames=D9719.23;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein disulfide isomerase family.
- **Key Domains:** Prot_disulphide_isomerase. (IPR005792); Thioredoxin-like_sf. (IPR036249); Thioredoxin_domain. (IPR013766); Thioredoxin (PF00085); Thioredoxin_6 (PF13848)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EUG1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EUG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EUG1** (gene ID: EUG1, UniProt: P32474) in yeast.

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
- **UniProt Accession:** P32474
- **Protein Description:** RecName: Full=Protein disulfide-isomerase EUG1; Short=PDI; EC=5.3.4.1; AltName: Full=Endoplasmic reticulum protein EUG1; Flags: Precursor;
- **Gene Information:** Name=EUG1; OrderedLocusNames=YDR518W; ORFNames=D9719.23;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein disulfide isomerase family.
- **Key Domains:** Prot_disulphide_isomerase. (IPR005792); Thioredoxin-like_sf. (IPR036249); Thioredoxin_domain. (IPR013766); Thioredoxin (PF00085); Thioredoxin_6 (PF13848)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EUG1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EUG1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EUG1** (gene ID: EUG1, UniProt: P32474) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Saccharomyces cerevisiae* **EUG1** (YDR518W; UniProt P32474)

## Executive conclusion

The requested target is correctly identified: **EUG1/YDR518W** from *Saccharomyces cerevisiae* is an endoplasmic-reticulum (ER) protein of the protein-disulfide-isomerase (PDI) family. The literature specifically associates YDR518W with two thioredoxin-like **CXXS** motifs—CLHS and CIHS, centered at residues 62 and 405—consistent with the supplied UniProt P32474 identity and InterPro/Pfam thioredoxin/PDI-domain assignments. No evidence from a similarly named gene in another organism was used. (nørgaard2001functionaldifferencesin pages 1-2, hacioglu2010therolesof pages 3-4)

The best-supported primary function is **thiol–disulfide rearrangement during folding of proteins in the ER lumen**. Eug1p is unusual among classical PDIs because each catalytic motif contains only one cysteine. It therefore cannot efficiently form the intramolecular active-site disulfide required to donate an oxidizing equivalent. Native Eug1p is consequently better interpreted as a **disulfide-shuffling/isomerase-like auxiliary folding factor with poor intrinsic oxidase capacity**, rather than as the principal enzyme introducing new disulfides. Pdi1p remains the dominant, essential ER PDI. (nørgaard2001functionaldifferencesin pages 2-2, nørgaard2001functionaldifferencesin pages 7-8, nørgaard2001functionaldifferencesin pages 4-5)

## Evidence summary

| Annotation question | Best-supported conclusion | Direct evidence / quantitative result | Evidence strength | Key citation (author/year/DOI URL) |
|---|---|---|---|---|
| Identity: is this the correct EUG1? | Yes. The literature matches **Saccharomyces cerevisiae EUG1 / YDR518W**, a **PDI-family ER protein** with **two thioredoxin-like active sites of the CXXS type**, consistent with UniProt P32474. | Primary literature on yeast PDI homologues explicitly places **EUG1** among the nonessential S. cerevisiae PDI-family genes and notes its **two CXXS motifs**; a later study tabulates **YDR518W EUG1** with motifs at **positions 62 and 405**. (nørgaard2001functionaldifferencesin pages 1-2, hacioglu2010therolesof pages 3-4) | **Strong** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553; Hacioglu et al. 2010, https://doi.org/10.1016/j.mad.2010.09.006 |
| Localization: where does Eug1p function? | Eug1p is best supported as a **soluble lumenal endoplasmic reticulum (ER) protein**. | Reviews of yeast PDI homologues state that **all are ER lumenal proteins except Eps1**, and PDI-family members are identified by **signal sequence plus ER retention signal (K/H)DEL**. Foundational work cited in these papers originally identified EUG1 as an ER protein. (nørgaard2001functionaldifferencesin pages 1-2, nørgaard2001functionaldifferencesin pages 2-3) | **Moderate to strong** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553 |
| Catalytic chemistry / active-site constraint | Eug1p is a **thiol-disulfide isomerase–like/shuffling** PDI-family protein with **limited oxidase capacity** because its active sites are **CXXS, not CXXC**. | Nørgaard et al. state Eug1p has **one cysteine residue in each active site**, rendering it **incapable of forming the internal disulfide bond required for oxidation**, but suited for shuffling reactions; overexpression of **CXXC-converted EUG1** rescues strains that native EUG1 cannot. Laboissière et al. independently showed the same principle in PDI: **CGHS (“shufflease”)** supports growth, whereas **SGHC** does not. (nørgaard2001functionaldifferencesin pages 4-5, nørgaard2001functionaldifferencesin pages 7-8, laboissiere1995theessentialfunction pages 2-3, laboissiere1995theessentialfunction pages 1-1) | **Strong** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553; Laboissière et al. 1995, https://doi.org/10.1074/jbc.270.47.28006 |
| What reaction is catalyzed? | The most defensible annotation is **rearrangement/isomerization of disulfide bonds in ER client proteins**, rather than efficient net oxidation of dithiols. | Direct Eug1p-specific biochemical kinetics were not recovered here, but in vivo genetics show native EUG1 behaves as a **CXXS-dependent shuffler/reductase-like PDI homolog** whose function improves when active sites are converted to **CXXC**. Family-level assays in related PDI constructs support the mechanistic interpretation. (nørgaard2001functionaldifferencesin pages 4-5, laboissiere1995theessentialfunction pages 2-3) | **Moderate** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553; Laboissière et al. 1995, https://doi.org/10.1074/jbc.270.47.28006 |
| Physiological substrate evidence: does Eug1p act on CPY? | **CPY/proCPY is supported as an informative in vivo substrate/reporters system**, but not as a uniquely specific physiological substrate of Eug1p. | In **Δpdi1 [EUG1]** strains, **proCPY maturation is almost arrested** with accumulation of the **ER p1 form**; the **steady-state proCPY pool is partially reduced**, indicating compromised oxidation when Eug1p substitutes for Pdi1p. This shows Eug1p can engage the CPY folding pathway but does so inefficiently on its own. (nørgaard2001functionaldifferencesin pages 6-7, nørgaard2001functionaldifferencesin pages 7-8) | **Strong for CPY pathway involvement; weak for specificity** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553 |
| Substrate specificity: what proteins does Eug1p prefer? | **No well-defined Eug1p-specific substrate repertoire is established** from the retrieved literature. | Available evidence is from complementation and CPY reporter assays rather than substrate-trapping or direct substrate panels. Reviews discuss PDI-family substrate selectivity broadly, but not a specific Eug1p client spectrum. (nørgaard2001functionaldifferencesin pages 1-2, xiao2004thecontributionsof pages 1-2) | **Limited / unresolved** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553; Xiao et al. 2004, https://doi.org/10.1074/jbc.M409210200 |
| Genetic essentiality and redundancy | **EUG1 is nonessential** and functionally redundant only in part; it cannot replace all essential Pdi1p functions by itself. | Deletion of **EUG1** caused **no obvious growth defect** under standard conditions, but **overexpression of EUG1** rescued **pdi1Δ** only when **MPD1 and MPD2** were present. By contrast, **MPD1** alone could rescue all tested deletion combinations. (nørgaard2001functionaldifferencesin pages 4-5, nørgaard2001functionaldifferencesin pages 5-6, nørgaard2001functionaldifferencesin pages 1-2) | **Strong** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553 |
| Quantitative expression context | EUG1 is normally expressed at a **much lower level than PDI1**, which likely contributes to its limited standalone capacity. | Promoter-lacZ data showed **EUG1 reporter activity ~1.173 Miller units** versus **PDI1 ~26.28 Miller units**; thus EUG1 promoter output was about **4–5% of PDI1** in that assay. (nørgaard2001functionaldifferencesin pages 5-6) | **Strong** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553 |
| Relationship to Ero1 oxidative folding pathway | Eug1p function is genetically linked to the canonical **Ero1-dependent ER oxidative folding pathway**, not an independent oxidation route. | In a **pdi1-deleted ero1-1** background, **none of the homologues** rescued viability when expressed from the **PDI1 promoter**; authors concluded the simplest explanation is that **Ero1p transfers oxidizing equivalents to the homologues** as well. For Eug1p specifically, its inability to oxidize on its own is consistent with this dependency. (nørgaard2001functionaldifferencesin pages 5-6, nørgaard2001functionaldifferencesin pages 7-8, xiao2004thecontributionsof pages 1-2) | **Moderate to strong** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553; Xiao et al. 2004, https://doi.org/10.1074/jbc.M409210200 |
| UPR / ER-stress pathway placement | EUG1 is a **transcriptional target of the yeast unfolded protein response (UPR)** downstream of **Ire1/Hac1** and participates in ER proteostasis capacity. | Classic UPR literature lists **EUG1** among genes induced by Hac1p, and Schröder et al. report that activation of **ER chaperone genes EUG1 and SCJ1 is completely abolished** in the tested IRE1/HAC1-independent context, implying their normal ER-stress induction depends on the canonical pathway. A 2023 review summarizes UPR-driven induction of ER folding/modification genes for applied engineering. (schroder2003ire1‐andhac1‐independent pages 1-2, ishiwatakimata2023fundamentalandapplicative pages 1-3) | **Moderate** | Cox et al. 1996, https://doi.org/10.1016/S0092-8674(00)81360-4; Schröder et al. 2003, https://doi.org/10.1046/j.1365-2958.2003.03585.x; Ishiwata-Kimata & Kimata 2023, https://doi.org/10.3390/jof9100989 |
| Aging phenotype | EUG1 contributes modestly to replicative lifespan maintenance, but this is likely secondary to its ER proteostasis role rather than its primary annotation. | Deletion of **EUG1** decreased replicative lifespan by **13%** in one study; authors note Eug1 may act as a **chaperone** in addition to thiol-disulfide isomerase activity. (hacioglu2010therolesof pages 3-4) | **Moderate** | Hacioglu et al. 2010, https://doi.org/10.1016/j.mad.2010.09.006 |
| Current applications / real-world implementation | There is **no strong evidence for EUG1-specific industrial or biomedical deployment**. Its main current relevance is as part of the **yeast ER folding/UPR network** that informs strain engineering for protein secretion. | Recent review literature (2023) emphasizes **UPR engineering** and ER expansion to improve secretion and lipid/terpenoid production in yeasts, but does **not identify EUG1 alone** as a validated engineering lever. Thus any application claim should remain network-level, not gene-specific. (ishiwatakimata2023fundamentalandapplicative pages 10-12, ishiwatakimata2023fundamentalandapplicative pages 1-3) | **Moderate for network relevance; weak for EUG1-specific application** | Ishiwata-Kimata & Kimata 2023, https://doi.org/10.3390/jof9100989 |
| Knowledge gaps | Key unresolved points are **direct native substrates**, **quantitative Eug1p enzymology in vivo**, **structural basis of client selection**, and **whether recent (2023–2024) EUG1-specific advances exist**. | Searches recovered foundational studies and recent UPR reviews, but **no 2023–2024 Eug1-specific mechanistic paper**. Existing data are dominated by genetics and reporter substrates such as CPY rather than direct client mapping. (nørgaard2001functionaldifferencesin pages 1-2, ishiwatakimata2023fundamentalandapplicative pages 1-3, ishiwatakimata2023fundamentalandapplicative pages 10-12) | **Strong as an assessment of the evidence landscape** | Nørgaard et al. 2001, https://doi.org/10.1083/jcb.152.3.553; Ishiwata-Kimata & Kimata 2023, https://doi.org/10.3390/jof9100989 |


*Table: This table summarizes the strongest available evidence for the identity, function, pathway context, and limitations of functional annotation for yeast EUG1/YDR518W/P32474. It is weighted toward direct experimental evidence and explicitly distinguishes established conclusions from unresolved questions.*

## 1. Identity, family, and architecture

EUG1 is one of five recognizable PDI-family genes in budding yeast: **PDI1, EUG1, MPD1, MPD2,** and **EPS1**. Unlike essential **PDI1**, EUG1 and the other homologues are individually nonessential under standard laboratory conditions. Eug1p shares approximately 40% sequence identity with Pdi1p and contains two thioredoxin-like catalytic domains, aligning well with the supplied PDI, thioredoxin-domain, and thioredoxin-like-superfamily annotations. (nørgaard2001functionaldifferencesin pages 2-2, nørgaard2001functionaldifferencesin pages 1-2, nørgaard2001functionaldifferencesin pages 3-4)

The decisive biochemical distinction is its two monothiol active-site sequences, reported as **WCLHSQ** and **WCIHSK**, rather than the canonical Pdi1p **CGHC** dithiol motifs. Later proteome-level annotation places the corresponding CXXS motifs at residues 62 and 405. These matching locus, motif, family, and organism data make misidentification unlikely. (hacioglu2010therolesof pages 3-4, laboissiere1995theessentialfunction pages 1-1)

## 2. Cellular localization

Eug1p is a **soluble ER-lumenal protein**. Yeast PDI-family soluble ER proteins are characterized by an N-terminal secretory-pathway targeting signal and a C-terminal ER retrieval/retention signal of the (K/H)DEL class; Eps1p is the notable membrane-associated member of the family. Thus Eug1p acts where secretory and membrane proteins fold—inside the ER lumen—rather than in the cytosol, nucleus, mitochondrion, or extracellular space. (nørgaard2001functionaldifferencesin pages 1-2, nørgaard2001functionaldifferencesin pages 2-3)

This localization is functionally coherent: nascent secretory proteins enter the yeast ER, where chaperones and redox enzymes promote folding before clients can leave for the Golgi. A 2023 authoritative review describes the yeast ER as nuclear and cortical ER and emphasizes its role in folding and assembling secretory and transmembrane proteins. (ishiwatakimata2023fundamentalandapplicative pages 1-3)

## 3. Catalytic reaction and mechanism

### Reaction

For a substrate protein containing incorrectly paired disulfides, the appropriate functional reaction is:

**protein-S–S-protein (non-native) ⇌ protein-S–S-protein (alternative/native pairing)**

This is thiol–disulfide exchange with no required net change in the number of substrate disulfides. The enzyme can transiently form a mixed disulfide through its active-site cysteine, allowing an incorrect substrate disulfide to be broken and rearranged.

Canonical CXXC PDIs can additionally oxidize two substrate thiols:

**protein-(SH)₂ + PDI(S–S) → protein-S–S + PDI(SH)₂.**

Native Eug1p is poorly equipped for this second reaction because CXXS sites cannot form the internal active-site disulfide used to transfer oxidizing equivalents. Nørgaard and colleagues therefore described Eug1p as incapable of independent oxidation but suited to “shuffling” reactions. (nørgaard2001functionaldifferencesin pages 7-8)

### Active-site evidence

Replacing Eug1p’s CXXS motifs with CXXC motifs converted it into a much more Pdi1-like enzyme genetically: the CXXC-converted Eug1p rescued combined loss of PDI1 and the other homologues, whereas native EUG1 required endogenous CXXC-containing Mpd1p and Mpd2p. Conversely, converting Pdi1p to CXXS restricted its rescue capacity. This reciprocal mutagenesis is strong evidence that the second active-site cysteine controls oxidative capacity. (nørgaard2001functionaldifferencesin pages 4-5)

Mechanistic experiments on matched CXXS PDI constructs reinforce this interpretation. A CGHS “shufflease” retained efficient disulfide-isomerization activity but had negligible dithiol-oxidation and disulfide-reduction activity; assays used scrambled RNase A for isomerization, reduced RNase A for oxidation, and insulin for reduction. These experiments were performed on mutant PDI rather than purified Eug1p, so they support the CXXS mechanism but should not be mistaken for Eug1p-specific kinetic measurements. (laboissiere1995theessentialfunction pages 2-3, laboissiere1995theessentialfunction pages 1-2)

## 4. Substrate specificity

A defined Eug1p-specific substrate repertoire has **not** been established. The strongest in vivo client evidence involves **carboxypeptidase Y (CPY/proCPY)**, a disulfide-containing vacuolar protein that folds in the ER and serves as a reporter of secretory-pathway folding. When EUG1 overexpression substituted for PDI1, proCPY maturation was almost arrested, the ER p1 form accumulated, and part of the proCPY pool remained reduced. Eug1p therefore recognizes or participates in the CPY folding pathway but cannot efficiently supply all required oxidation and isomerization by itself. (nørgaard2001functionaldifferencesin pages 6-7)

This does not demonstrate selective binding to CPY. In fact, deletion of the auxiliary homologues had little effect on CPY maturation when normal Pdi1p remained present, implying that Eug1p makes a minor or condition-dependent contribution under basal conditions. Its physiological specificity is thus best described as **unresolved, probably overlapping with ER disulfide-containing client proteins rather than confined to one substrate**. (nørgaard2001functionaldifferencesin pages 6-7)

EUG1 was also dispensable for degradation of the tested ER-associated degradation substrate CPY*: eliminating the auxiliary PDI homologues did not significantly reduce CPY* degradation. Eug1p should therefore not be annotated as a dedicated ERAD receptor or obligatory ERAD enzyme. (nørgaard2001functionaldifferencesin pages 7-8)

## 5. Biological processes and pathway placement

### Oxidative protein folding

Eug1p functions within the **ER oxidative-folding network**, alongside Pdi1p, Mpd1p, Mpd2p, Eps1p, and the ER oxidase Ero1p. Ero1p generates oxidizing equivalents that are passed through PDI-family proteins to substrates. In an *ero1-1 pdi1Δ* background, none of the PDI homologues rescued viability, arguing against an independent Eug1p oxidation pathway. For Eug1p, which lacks a native CXXC disulfide, productive function is especially dependent on cooperation with CXXC-containing homologues and the broader Ero1 pathway. (nørgaard2001functionaldifferencesin pages 7-8, nørgaard2001functionaldifferencesin pages 5-6, xiao2004thecontributionsof pages 1-2)

### Unfolded protein response

EUG1 is part of the ER-proteostasis program induced by the yeast **unfolded protein response (UPR)**. ER stress activates the ER transmembrane kinase/RNase Ire1, which splices **HAC1** mRNA; translated Hac1 then induces genes encoding ER chaperones and protein-modification enzymes. Classic studies identify EUG1 as an ER-chaperone/PDI-like UPR target, placing it downstream of the canonical Ire1–Hac1 signaling axis. (schroder2003ire1‐andhac1‐independent pages 1-2, ishiwatakimata2023fundamentalandapplicative pages 1-3)

This is regulatory pathway membership, not evidence that Eug1p itself is a signaling molecule. Eug1p is an **effector enzyme/folding factor induced by the pathway**, whereas Ire1 and Hac1 perform sensing and transcriptional signaling.

## 6. Genetic evidence, redundancy, and quantitative findings

Several quantitative observations define Eug1p’s role:

- **Nonessentiality:** deleting EUG1 caused no obvious growth defect under standard conditions, even in combinations where PDI1 remained intact. (nørgaard2001functionaldifferencesin pages 4-5, nørgaard2001functionaldifferencesin pages 3-4)
- **Low basal expression:** an EUG1-promoter reporter yielded **1.173 ± 0.056 Miller units**, versus **26.28 ± 2.34** for PDI1—approximately 4–5% of PDI1 reporter output. (nørgaard2001functionaldifferencesin pages 5-6)
- **Incomplete Pdi1 replacement:** a *pdi1Δ* strain rescued by EUG1 grew at approximately **0.3 h⁻¹**, compared with about **0.7 h⁻¹** for wild type. (nørgaard2001functionaldifferencesin pages 4-5)
- **CPY folding:** proCPY maturation had a half-time of **5–10 min** with PDI1; with EUG1 replacing PDI1, maturation was described as almost arrested with accumulation of ER-localized p1 proCPY. (nørgaard2001functionaldifferencesin pages 6-7)
- **Dependence on other PDIs:** native EUG1 rescued *pdi1Δ* only when both MPD1 and MPD2 were available, whereas the CXXC-engineered Eug1p rescued all tested PDI-family deletion combinations. (nørgaard2001functionaldifferencesin pages 4-5)
- **Replicative aging:** one study reported a **13% reduction in replicative lifespan** after EUG1 deletion. This supports a modest contribution to long-term proteostasis but is a secondary phenotype, not the basis of the primary annotation. (hacioglu2010therolesof pages 3-4)

Together, these results indicate that Eug1p is an **auxiliary, low-abundance ER folding catalyst**. Its apparent ability to suppress PDI1 loss under overexpression should not be interpreted as normal functional equivalence to Pdi1p.

## 7. Current understanding and expert interpretation

The most defensible expert interpretation is that yeast divided ER redox work among noninterchangeable PDI-family members. Pdi1p supplies the major essential oxidative-folding capacity; Eug1p’s unusual CXXS motifs bias it toward disulfide rearrangement and perhaps chaperone-like assistance. The requirement for CXXC-containing partners when EUG1 replaces PDI1 demonstrates that **net disulfide oxidation remains essential even when shuffling activity is present**. (nørgaard2001functionaldifferencesin pages 1-2, nørgaard2001functionaldifferencesin pages 7-8)

There is an important historical nuance. Earlier complementation experiments with CXXS PDI variants suggested that disulfide isomerization might be PDI’s essential function. Later deletion and CPY-folding studies showed that efficient ER folding requires both oxidation and isomerization and that auxiliary homologues can mask defects. Thus the current balanced model is not “Eug1p alone performs the essential PDI reaction,” but rather “Eug1p supplies a specialized component of a cooperative redox network.” (xiao2004thecontributionsof pages 1-2, laboissiere1995theessentialfunction pages 2-3)

## 8. Recent developments (2023–2024) and applications

The search identified **no 2023–2024 primary mechanistic study specifically resolving Eug1p structure, kinetics, or native clients**. The gene-specific evidence base remains dominated by foundational work from 1992–2010. This is itself an important limitation: recent general PDI or fungal-UPR discoveries should not be attributed automatically to EUG1.

The relevant recent development is network-level. A review published **5 October 2023** describes contemporary engineering of yeast UPR and ER capacity for recombinant protein production. Artificial Hac1 expression can expand the ER and, in some contexts, increase secretion of heterologous proteins or production of triglycerides and terpenoids. In *S. cerevisiae*, reported secretion gains for α-amylase and xylanase were moderate, while excessive constitutive Hac1 activity can severely retard growth. (ishiwatakimata2023fundamentalandapplicative pages 1-3, ishiwatakimata2023fundamentalandapplicative pages 10-12)

EUG1 is relevant to these applications as one Hac1-responsive ER folding factor, but there is **no strong evidence that EUG1 overexpression alone is a validated industrial intervention**. Its poor intrinsic oxidase capacity and dependence on CXXC partners suggest that rational engineering would likely require balancing Eug1p with Ero1/Pdi1-family oxidation capacity rather than increasing EUG1 in isolation.

## 9. Recommended functional annotation

**Molecular function:** ER-lumenal PDI-family thiol–disulfide oxidoreductase, principally supporting rearrangement/isomerization of non-native protein disulfide bonds; limited intrinsic oxidase activity owing to two CXXS active sites.

**Biological process:** folding and oxidative maturation of secretory-pathway proteins; ER proteostasis and adaptation to ER stress.

**Cellular component:** endoplasmic-reticulum lumen.

**Pathway:** Ero1/PDI-dependent oxidative protein folding; downstream effector of the Ire1–Hac1 unfolded-protein response.

**Substrates:** disulfide-containing ER client proteins. CPY/proCPY is experimentally supported as a reporter/client pathway, but no Eug1p-selective physiological substrate set is established.

**Confidence:** high for identity, family, ER localization, nonessentiality, CXXS architecture, and auxiliary oxidative-folding role; moderate for predominant isomerase/shuffling activity; low for precise native substrate specificity and EUG1-specific industrial applications.

## Key sources and publication dates

1. Nørgaard P. et al. “Functional Differences in Yeast Protein Disulfide Isomerases.” *Journal of Cell Biology*, **5 February 2001**. https://doi.org/10.1083/jcb.152.3.553 (nørgaard2001functionaldifferencesin pages 1-2)
2. Xiao R. et al. “The Contributions of Protein Disulfide Isomerase and Its Homologues to Oxidative Protein Folding in the Yeast Endoplasmic Reticulum.” *Journal of Biological Chemistry*, **26 November 2004**. https://doi.org/10.1074/jbc.M409210200 (xiao2004thecontributionsof pages 1-2)
3. Laboissière M.C.A. et al. “The Essential Function of Protein-disulfide Isomerase Is to Unscramble Non-native Disulfide Bonds.” *Journal of Biological Chemistry*, **24 November 1995**. https://doi.org/10.1074/jbc.270.47.28006 (laboissiere1995theessentialfunction pages 1-1)
4. Hacioglu E. et al. “The Roles of Thiol Oxidoreductases in Yeast Replicative Aging.” *Mechanisms of Ageing and Development*, **November 2010**. https://doi.org/10.1016/j.mad.2010.09.006 (hacioglu2010therolesof pages 3-4)
5. Schröder M. et al. “IRE1- and HAC1-independent Transcriptional Regulation in the Unfolded Protein Response of Yeast.” *Molecular Microbiology*, **August 2003**. https://doi.org/10.1046/j.1365-2958.2003.03585.x (schroder2003ire1‐andhac1‐independent pages 1-2)
6. Ishiwata-Kimata Y., Kimata Y. “Fundamental and Applicative Aspects of the Unfolded Protein Response in Yeasts.” *Journal of Fungi*, **5 October 2023**. https://doi.org/10.3390/jof9100989 (ishiwatakimata2023fundamentalandapplicative pages 1-3)

References

1. (nørgaard2001functionaldifferencesin pages 1-2): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

2. (hacioglu2010therolesof pages 3-4): Elise Hacioglu, Isil Esmer, Dmitri E. Fomenko, Vadim N. Gladyshev, and Ahmet Koc. The roles of thiol oxidoreductases in yeast replicative aging. Mechanisms of Ageing and Development, 131:692-699, Nov 2010. URL: https://doi.org/10.1016/j.mad.2010.09.006, doi:10.1016/j.mad.2010.09.006. This article has 15 citations and is from a peer-reviewed journal.

3. (nørgaard2001functionaldifferencesin pages 2-2): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

4. (nørgaard2001functionaldifferencesin pages 7-8): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

5. (nørgaard2001functionaldifferencesin pages 4-5): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

6. (nørgaard2001functionaldifferencesin pages 2-3): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

7. (laboissiere1995theessentialfunction pages 2-3): Martha C.A. Laboissière, Stephen L. Sturley, and Ronald T. Raines. The essential function of protein-disulfide isomerase is to unscramble non-native disulfide bonds (*). The Journal of Biological Chemistry, 270:28006-28009, Nov 1995. URL: https://doi.org/10.1074/jbc.270.47.28006, doi:10.1074/jbc.270.47.28006. This article has 284 citations.

8. (laboissiere1995theessentialfunction pages 1-1): Martha C.A. Laboissière, Stephen L. Sturley, and Ronald T. Raines. The essential function of protein-disulfide isomerase is to unscramble non-native disulfide bonds (*). The Journal of Biological Chemistry, 270:28006-28009, Nov 1995. URL: https://doi.org/10.1074/jbc.270.47.28006, doi:10.1074/jbc.270.47.28006. This article has 284 citations.

9. (nørgaard2001functionaldifferencesin pages 6-7): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

10. (xiao2004thecontributionsof pages 1-2): Ruoyu Xiao, Bonney Wilkinson, Anton Solovyov, Jakob R. Winther, Arne Holmgren, Johanna Lundström-Ljung, and Hiram F. Gilbert. The contributions of protein disulfide isomerase and its homologues to oxidative protein folding in the yeast endoplasmic reticulum*. Journal of Biological Chemistry, 279:49780-49786, Nov 2004. URL: https://doi.org/10.1074/jbc.m409210200, doi:10.1074/jbc.m409210200. This article has 90 citations and is from a domain leading peer-reviewed journal.

11. (nørgaard2001functionaldifferencesin pages 5-6): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

12. (schroder2003ire1‐andhac1‐independent pages 1-2): Martin Schröder, Robert Clark, and Randal J. Kaufman. Ire1‐ and hac1‐independent transcriptional regulation in the unfolded protein response of yeast. Molecular Microbiology, 49:591-606, Aug 2003. URL: https://doi.org/10.1046/j.1365-2958.2003.03585.x, doi:10.1046/j.1365-2958.2003.03585.x. This article has 77 citations and is from a domain leading peer-reviewed journal.

13. (ishiwatakimata2023fundamentalandapplicative pages 1-3): Yuki Ishiwata-Kimata and Yukio Kimata. Fundamental and applicative aspects of the unfolded protein response in yeasts. Journal of Fungi, 9:989, Oct 2023. URL: https://doi.org/10.3390/jof9100989, doi:10.3390/jof9100989. This article has 23 citations.

14. (ishiwatakimata2023fundamentalandapplicative pages 10-12): Yuki Ishiwata-Kimata and Yukio Kimata. Fundamental and applicative aspects of the unfolded protein response in yeasts. Journal of Fungi, 9:989, Oct 2023. URL: https://doi.org/10.3390/jof9100989, doi:10.3390/jof9100989. This article has 23 citations.

15. (nørgaard2001functionaldifferencesin pages 3-4): Per Nørgaard, Vibeke Westphal, Christine Tachibana, Lene Alsøe, Bjørn Holst, and Jakob R. Winther. Functional differences in yeast protein disulfide isomerases. The Journal of Cell Biology, 152:553-562, Feb 2001. URL: https://doi.org/10.1083/jcb.152.3.553, doi:10.1083/jcb.152.3.553. This article has 169 citations.

16. (laboissiere1995theessentialfunction pages 1-2): Martha C.A. Laboissière, Stephen L. Sturley, and Ronald T. Raines. The essential function of protein-disulfide isomerase is to unscramble non-native disulfide bonds (*). The Journal of Biological Chemistry, 270:28006-28009, Nov 1995. URL: https://doi.org/10.1074/jbc.270.47.28006, doi:10.1074/jbc.270.47.28006. This article has 284 citations.

## Artifacts

- [Edison artifact artifact-00](EUG1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. hacioglu2010therolesof pages 3-4
2. ishiwatakimata2023fundamentalandapplicative pages 1-3
3. xiao2004thecontributionsof pages 1-2
4. laboissiere1995theessentialfunction pages 1-1
5. laboissiere1995theessentialfunction pages 2-3
6. ishiwatakimata2023fundamentalandapplicative pages 10-12
7. laboissiere1995theessentialfunction pages 1-2
8. EUG1
9. https://doi.org/10.1083/jcb.152.3.553;
10. https://doi.org/10.1016/j.mad.2010.09.006
11. https://doi.org/10.1083/jcb.152.3.553
12. https://doi.org/10.1074/jbc.270.47.28006
13. https://doi.org/10.1074/jbc.M409210200
14. https://doi.org/10.1016/S0092-8674(00
15. https://doi.org/10.1046/j.1365-2958.2003.03585.x;
16. https://doi.org/10.3390/jof9100989
17. https://doi.org/10.1046/j.1365-2958.2003.03585.x
18. https://doi.org/10.1083/jcb.152.3.553,
19. https://doi.org/10.1016/j.mad.2010.09.006,
20. https://doi.org/10.1074/jbc.270.47.28006,
21. https://doi.org/10.1074/jbc.m409210200,
22. https://doi.org/10.1046/j.1365-2958.2003.03585.x,
23. https://doi.org/10.3390/jof9100989,