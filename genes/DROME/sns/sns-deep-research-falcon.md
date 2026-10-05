---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T17:57:23.737835'
end_time: '2026-09-08T18:10:33.830951'
duration_seconds: 790.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: sns
  gene_symbol: sns
  uniprot_accession: Q0E9F2
  protein_description: 'SubName: Full=Sticks and stones, isoform B {ECO:0000313|EMBL:ABI31083.1};'
  gene_info: Name=sns {ECO:0000313|EMBL:ABI31083.1, ECO:0000313|FlyBase:FBgn0024189};
    Synonyms=43-49 {ECO:0000313|EMBL:ABI31083.1}, CG12495 {ECO:0000313|EMBL:ABI31083.1},
    CG13752 {ECO:0000313|EMBL:ABI31083.1}, CG13753 {ECO:0000313|EMBL:ABI31083.1},
    CG13754 {ECO:0000313|EMBL:ABI31083.1}, CG13755 {ECO:0000313|EMBL:ABI31083.1},
    CG18464 {ECO:0000313|EMBL:ABI31083.1}, CG2385 {ECO:0000313|EMBL:ABI31083.1}, CG8278
    {ECO:0000313|EMBL:ABI31083.1}, CT33230 {ECO:0000313|EMBL:ABI31083.1}, CT33232
    {ECO:0000313|EMBL:ABI31083.1}, Dmel\CG33141 {ECO:0000313|EMBL:ABI31083.1}, rost
    {ECO:0000313|EMBL:ABI31083.1}, SNS {ECO:0000313|EMBL:ABI31083.1}, SnS {ECO:0000313|EMBL:ABI31083.1},
    Sns {ECO:0000313|EMBL:ABI31083.1}, sns20 {ECO:0000313|EMBL:ABI31083.1}; ORFNames=CG33141
    {ECO:0000313|EMBL:ABI31083.1, ECO:0000313|FlyBase:FBgn0024189}, Dmel_CG33141 {ECO:0000313|EMBL:ABI31083.1};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: CD80_C2-set. (IPR013162); Cell_adhesion_signaling. (IPR051275);
    FN3_dom. (IPR003961); FN3_sf. (IPR036116); Ig-like_dom. (IPR007110)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: sns-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q0E9F2
- **Protein Description:** SubName: Full=Sticks and stones, isoform B {ECO:0000313|EMBL:ABI31083.1};
- **Gene Information:** Name=sns {ECO:0000313|EMBL:ABI31083.1, ECO:0000313|FlyBase:FBgn0024189}; Synonyms=43-49 {ECO:0000313|EMBL:ABI31083.1}, CG12495 {ECO:0000313|EMBL:ABI31083.1}, CG13752 {ECO:0000313|EMBL:ABI31083.1}, CG13753 {ECO:0000313|EMBL:ABI31083.1}, CG13754 {ECO:0000313|EMBL:ABI31083.1}, CG13755 {ECO:0000313|EMBL:ABI31083.1}, CG18464 {ECO:0000313|EMBL:ABI31083.1}, CG2385 {ECO:0000313|EMBL:ABI31083.1}, CG8278 {ECO:0000313|EMBL:ABI31083.1}, CT33230 {ECO:0000313|EMBL:ABI31083.1}, CT33232 {ECO:0000313|EMBL:ABI31083.1}, Dmel\CG33141 {ECO:0000313|EMBL:ABI31083.1}, rost {ECO:0000313|EMBL:ABI31083.1}, SNS {ECO:0000313|EMBL:ABI31083.1}, SnS {ECO:0000313|EMBL:ABI31083.1}, Sns {ECO:0000313|EMBL:ABI31083.1}, sns20 {ECO:0000313|EMBL:ABI31083.1}; ORFNames=CG33141 {ECO:0000313|EMBL:ABI31083.1, ECO:0000313|FlyBase:FBgn0024189}, Dmel_CG33141 {ECO:0000313|EMBL:ABI31083.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CD80_C2-set. (IPR013162); Cell_adhesion_signaling. (IPR051275); FN3_dom. (IPR003961); FN3_sf. (IPR036116); Ig-like_dom. (IPR007110)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sns" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sns' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sns** (gene ID: sns, UniProt: Q0E9F2) in DROME.

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
- **UniProt Accession:** Q0E9F2
- **Protein Description:** SubName: Full=Sticks and stones, isoform B {ECO:0000313|EMBL:ABI31083.1};
- **Gene Information:** Name=sns {ECO:0000313|EMBL:ABI31083.1, ECO:0000313|FlyBase:FBgn0024189}; Synonyms=43-49 {ECO:0000313|EMBL:ABI31083.1}, CG12495 {ECO:0000313|EMBL:ABI31083.1}, CG13752 {ECO:0000313|EMBL:ABI31083.1}, CG13753 {ECO:0000313|EMBL:ABI31083.1}, CG13754 {ECO:0000313|EMBL:ABI31083.1}, CG13755 {ECO:0000313|EMBL:ABI31083.1}, CG18464 {ECO:0000313|EMBL:ABI31083.1}, CG2385 {ECO:0000313|EMBL:ABI31083.1}, CG8278 {ECO:0000313|EMBL:ABI31083.1}, CT33230 {ECO:0000313|EMBL:ABI31083.1}, CT33232 {ECO:0000313|EMBL:ABI31083.1}, Dmel\CG33141 {ECO:0000313|EMBL:ABI31083.1}, rost {ECO:0000313|EMBL:ABI31083.1}, SNS {ECO:0000313|EMBL:ABI31083.1}, SnS {ECO:0000313|EMBL:ABI31083.1}, Sns {ECO:0000313|EMBL:ABI31083.1}, sns20 {ECO:0000313|EMBL:ABI31083.1}; ORFNames=CG33141 {ECO:0000313|EMBL:ABI31083.1, ECO:0000313|FlyBase:FBgn0024189}, Dmel_CG33141 {ECO:0000313|EMBL:ABI31083.1};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CD80_C2-set. (IPR013162); Cell_adhesion_signaling. (IPR051275); FN3_dom. (IPR003961); FN3_sf. (IPR036116); Ig-like_dom. (IPR007110)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sns" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sns' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sns** (gene ID: sns, UniProt: Q0E9F2) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster sns* / Sticks and stones (UniProt Q0E9F2)

## Executive conclusion

The requested identity is verified: **sns is the *Drosophila melanogaster* gene *sticks and stones***, not spermine synthase, a mammalian similarly abbreviated gene, or a protein from another organism. Its principal product is a large, single-pass immunoglobulin-superfamily (IgSF) cell-surface receptor. Its best-established primary function is to couple **heterotypic myoblast recognition and adhesion** to **localized actin remodeling**, thereby enabling fusion-competent myoblasts (FCMs) to fuse with founder cells or growing myotubes. Sns is not an enzyme, transporter, or independently established fusogen; it is an adhesion/signaling organizer acting at the plasma membrane.

A second well-supported role is as the fly Nephrin-like component of the **Sns–Kirre nephrocyte slit diaphragm**, where it contributes to the filtration-barrier architecture. The strongest mechanistic evidence remains concentrated in foundational studies from 2000–2013. Targeted searches found comparatively little 2023–2024 research centered specifically on Sns; recent work chiefly uses Sns as an established slit-diaphragm component or marker in nephrocyte and kidney-disease models.

## 1. Mandatory identity verification

### Gene, organism, and locus

Bour and colleagues isolated *sns* through a muscle-development mutant screen and mapped the responsible second-chromosome lesion to cytological region 44F1–4. Homozygous mutants and embryos carrying the allele over a deficiency deleting the locus exhibited essentially the same fusion-block phenotype, supporting classification of the tested allele as a genetic null. Sequencing of independent alleles found premature termination mutations at Sns residues 356 and 465; the historical *rost*202 mutation carries a stop at residue 367 and is therefore an *sns* allele rather than a different protein. These genetic and molecular results match the supplied *D. melanogaster* identity and explain *rost* among the listed synonyms. (bour2000drosophilasnsa pages 2-4, bour2000drosophilasnsa pages 5-6)

The cloned coding sequence predicts a **1,483-amino-acid, approximately 162-kDa protein**. It contains eight N-terminal extracellular Ig-like domains, one fibronectin type III domain, a transmembrane segment, and a long cytoplasmic region. Fourteen NXS/NXT motifs predict extensive extracellular N-glycosylation. This experimentally anchored sequence architecture agrees with the supplied UniProt/InterPro annotations for Ig-like, CD80-C2-set, FN3, and cell-adhesion/signaling domains. (bour2000drosophilasnsa pages 5-6)

The architecture is closely related to vertebrate Nephrin and to the *Drosophila* paralog Hibris. Reported Sns–Hibris amino-acid identity is approximately 48%, although Sns has the more functionally effective cytoplasmic region in embryonic fusion assays. (shelton2009theimmunoglobulinsuperfamily pages 1-2, shelton2009theimmunoglobulinsuperfamily pages 8-9)

**Isoform caveat:** Q0E9F2 is annotated as isoform B. The foundational functional studies generally interrogated the *sns* locus, endogenous protein, or transgenes and did not establish an isoform-B-specific biochemical role. The annotation below is therefore strongest at the gene/protein-family level; assigning every finding uniquely to Q0E9F2 rather than another Sns isoform would exceed the evidence.

## 2. Primary molecular function

### Cell-recognition and adhesion receptor in myoblast fusion

Embryonic somatic muscles arise when mononucleate FCMs recognize and fuse with specified founder cells and then with growing myotubes. Sns is selectively expressed in the FCM population, not in newly specified founder cells. It appears at the FCM surface shortly before fusion, becomes enriched at the plasma membrane, and clusters at discrete contact sites coincident with fusion. (bour2000drosophilasnsa pages 10-11, bour2000drosophilasnsa pages 8-10, bour2000drosophilasnsa pages 1-2)

Across the cell–cell interface, extracellular Sns engages the founder-cell IgSF receptors **Kirre/Dumbfounded (Duf)** and **Roughest (Rst)**. This asymmetric receptor distribution gives Sns a precise role: it marks the fusion-competent partner and helps establish the adhesive interface with the founder cell or myotube. Hibris can overlap partially with Sns, but genetic and rescue experiments indicate that Sns is normally the more effective FCM receptor. (shelton2009theimmunoglobulinsuperfamily pages 1-2, reissaus2007identificationandinitial pages 109-112, shelton2009theimmunoglobulinsuperfamily pages 8-9)

Sns should not be annotated as the membrane fusogen itself. Rather, it promotes the recognition, adhesion, cytoskeletal force generation, and close membrane apposition that permit a downstream fusogenic mechanism to act. This distinction is illustrated by S2R+ reconstitution experiments: Sns strongly enhanced fusion driven by the heterologous fusogen EFF-1, but EFF-1 supplied the membrane-merging activity. (shilagardi2013actinpropelledinvasivemembrane pages 1-2)

### Coupling adhesion to actin remodeling

The supported pathway is:

**Sns–Kirre/Duf or Sns–Rst trans interaction → adaptor recruitment at the fusion synapse → WASP/WIP and SCAR/WAVE–Arp2/3 activation → concentrated branched F-actin and invasive protrusions → engagement of apposed membranes and fusion.**

The Sns cytoplasmic side has been linked to D-Crk/Dock-family adaptor machinery, Solitary and actin-nucleation systems. Genetic and cell-biological evidence places Sns upstream of localized actin polymerization and directed vesicle traffic at myoblast contacts. Some individual physical links in this chain are better established than others, so it is most accurate to regard Sns as the membrane-positioning hub for a partly redundant actin-remodeling network, rather than as a simple linear receptor with one obligatory effector. (reissaus2007identificationandinitial pages 109-112)

Domain-chimera experiments comparing Sns and Hibris indicate that both extracellular and intracellular regions contribute to activity, with the Sns cytoplasmic region producing the largest improvement in fusion rescue. Sns and Hibris can also associate in cis in transfected cells: co-immunoprecipitation occurred when both were expressed in the same cells, but not after separately transfected populations were mixed before lysis. (shelton2009theimmunoglobulinsuperfamily pages 6-7, shelton2009theimmunoglobulinsuperfamily pages 8-9)

## 3. Experimental evidence and quantitative findings

### Loss-of-function phenotype

In *sns* null embryos, founder-cell specification and early differentiation are largely retained: correctly positioned founder markers, MEF2-positive myoblasts, and myosin-expressing cells remain. Nevertheless, the myoblasts fail to assemble normal multinucleate muscle fibers and accumulate as unfused cells. This separates the primary defect—fusion—from initial mesoderm specification or general myogenic differentiation. (bour2000drosophilasnsa pages 2-4)

The embryonic body wall normally produces approximately 30 muscles per hemisegment. The nearly complete absence of differentiated body-wall fibers in strong *sns* mutants therefore represents a severe system-wide failure rather than a defect in a small muscle subset. (bour2000drosophilasnsa pages 10-11)

### Quantitative fusion reconstitution

In S2R+ cells expressing EFF-1, adding Sns increased the proportion of co-expressing cells incorporated into syncytia to **86.3 ± 2.9%**, compared with approximately **12%** for EFF-1 alone. Sns was needed in only one fusion partner, consistent with an asymmetric, protrusion-generating role. RNAi against WASP, WIP, or Scar eliminated the associated F-actin foci and abolished Sns-enhanced fusion. (shilagardi2013actinpropelledinvasivemembrane pages 1-2)

Live imaging, electron microscopy, and super-resolution microscopy showed F-actin-rich, finger-like protrusions entering the partner cell. Sns and EFF-1 formed clusters along these structures, while electron-dense, ladder-like membrane segments appeared at protrusion interfaces. These observations support a mechanical model in which actin-driven invasion enlarges and stabilizes molecular engagement between apposed membranes. (shilagardi2013actinpropelledinvasivemembrane pages 1-2, shilagardi2013actinpropelledinvasivemembrane pages 9-11)

## 4. Cellular and tissue localization

### Embryonic somatic muscle

Sns is a plasma-membrane protein of FCMs. It concentrates at contacts with founder cells and nascent myotubes, i.e., at the fusion-relevant cell cortex rather than in the nucleus, extracellular matrix, or a general intracellular compartment. This is the location in which its primary developmental function is carried out. (bour2000drosophilasnsa pages 10-11, bour2000drosophilasnsa pages 1-2)

### Visceral muscle

Sns transcript and protein occur in precursors of both somatic and visceral musculature. Genetic work on visceral-muscle syncytium formation also places Sns in the recognition/fusion program, although the somatic body-wall system provides the clearest mechanistic evidence. (bour2000drosophilasnsa pages 10-11, bour2000drosophilasnsa pages 1-2)

### Nephrocytes

Sns is the Nephrin-like component of the *Drosophila* nephrocyte slit diaphragm, partnering with the Neph1-like receptor Kirre. In this setting, Sns resides at specialized plasma-membrane junctions spanning filtration slits rather than at a transient myoblast fusion synapse. The same broad molecular property—heterophilic IgSF adhesion—has therefore been adapted to a stable filtration junction. Sequence similarity to human Nephrin was already evident in the original molecular characterization, including similarity across extracellular, transmembrane, and portions of the cytoplasmic regions. (bour2000drosophilasnsa pages 5-6)

### Other reported contexts

Loss and tissue-specific rescue experiments have implicated Sns in multidendritic sensory-neuron arborization. Reported phenotypes include increased higher-order branching in one neuronal class and reduced complexity in another allele/cell context. These results suggest cell-autonomous recognition or cytoskeletal functions, but they are less extensively replicated and mechanistically developed than the muscle phenotype. (reissaus2007identificationandinitial pages 10-14, reissaus2007identificationandinitial pages 109-112)

IRM-family genetic studies also implicate Sns in sensory-organ spacing. These secondary roles are consistent with a reusable cell-recognition module but should not displace myoblast fusion and nephrocyte junction organization as the principal functional annotations.

## 5. Developmental and signaling context

Sns-positive FCM specification depends strongly on **Notch signaling**. Notch mutants show expansion of founder-cell markers and marked reduction of Sns-positive cells, indicating that Notch-dependent fate allocation generates the FCM population in which Sns subsequently functions. Conversely, Sns remains detectable in *mef2* mutants, showing that its transcription is not absolutely dependent on the core myogenic regulator MEF2. Sns itself is not a canonical Notch-pathway receptor; Notch acts upstream in cell-fate specification. (bour2000drosophilasnsa pages 8-10, bour2000drosophilasnsa pages 11-12)

Thus, two regulatory levels should be distinguished:

1. **Upstream developmental specification:** Notch and FCM transcriptional programs establish an Sns-expressing fusion-competent cell.
2. **Local membrane mechanism:** Sns recognizes Kirre/Duf or Rst across the contact and organizes adhesion-dependent actin remodeling at the fusion synapse.

## 6. Current applications and recent research

### Kidney and podocyte-disease modeling

The Sns–Kirre slit diaphragm makes *Drosophila* nephrocytes a tractable in-vivo model for mammalian podocyte junctions, filtration, polarity, and endocytosis. In current practice, Sns localization is frequently used as a structural readout: disrupted, mislocalized, or discontinuous Sns staining indicates defective slit-diaphragm assembly or maintenance. The system supports rapid tissue-specific RNAi, live-animal physiology, imaging, and genetic interaction testing.

Recent nephrocyte studies have examined polarity and phosphoinositide requirements for delivering or maintaining Sns/Kirre at the cell cortex. A 2024 *Drosophila* Dent-disease type 1 model likewise situates Sns/Kirre-positive nephrocyte diaphragms within a conserved renal model, although its principal target was ClC-c rather than Sns. Accordingly, this literature demonstrates the current real-world research utility of Sns but does not materially revise its molecular mechanism.

### Cell-fusion research

Sns remains a canonical experimental entry point for dissecting how adhesion receptors spatially organize actin forces during cell–cell fusion. The Sns/EFF-1 reconstitution system is particularly useful because it separates adhesion/protrusion-promoting activity from membrane fusogenic activity. It supports the modern view that successful cell fusion requires both a membrane-merging protein and an active mechanical program that brings fusogens into productive engagement. (shilagardi2013actinpropelledinvasivemembrane pages 1-2, shilagardi2013actinpropelledinvasivemembrane pages 9-11)

### Status of 2023–2024 evidence

Targeted searches yielded few 2023–2024 publications whose central subject was *Drosophila sns*. The latest literature mainly treats Sns as an established component or marker in broader nephrocyte, renal-disease, tissue-patterning, or fusion studies. Therefore, prioritizing recency alone would give a misleading annotation: the decisive Sns-specific evidence still comes from the original 2000 genetic characterization, 2009 interaction/domain work, and 2013 actin-protrusion experiments. No recent result identified in this search overturns that framework.

## 7. Expert interpretation and annotation confidence

The most defensible concise annotation is:

> **Sns is a Nephrin-family/IRM immunoglobulin-superfamily single-pass cell-adhesion and signaling receptor. In embryonic fusion-competent myoblasts it binds Kirre/Duf or Rst across the cell interface and organizes adaptor- and Arp2/3-dependent actin remodeling needed for myoblast fusion; in nephrocytes it forms part of the Kirre-containing slit diaphragm filtration junction.**

The evidence is **very strong** for gene identity, domain architecture, FCM-specific membrane localization, and an essential role in embryonic myoblast fusion. It is **strong** for adhesion-dependent actin remodeling and for Sns as a nephrin-like slit-diaphragm component. It is **moderate** for the exact order and universality of every intracellular adaptor interaction, because redundant actin pathways and context-dependent receptor complexes complicate a single linear model. Neuronal and sensory-patterning roles remain secondary annotations with lower mechanistic confidence.

Importantly, there is no substrate, transported solute, or catalytic reaction to assign. “Cell-adhesion/signaling receptor and fusion-site organizer” is more accurate than enzyme, transporter, structural matrix protein, or fusogen.

The following table summarizes the evidence hierarchy and major limitations.

| Annotation aspect | Best-supported conclusion | Evidence type | Representative study/date/DOI | Confidence / limitations |
|---|---|---|---|---|
| Identity and architecture | **Q0E9F2 is Drosophila melanogaster Sticks and stones (Sns)**, not mammalian spermine synthase or another similarly abbreviated protein. The cloned locus encodes a **1,483-aa, ~162-kDa Ig-superfamily single-pass membrane protein** with **8 extracellular Ig-like domains, 1 fibronectin type III domain, a transmembrane segment, and a long cytoplasmic tail**. Sequenced nonsense alleles and noncomplementation establish locus identity; *rost*202 is an *sns* allele. (bour2000drosophilasnsa pages 5-6) | Genetic mapping, allele sequencing, cDNA cloning, sequence/domain analysis | Bour et al.; June 2000; [10.1101/gad.14.12.1498](https://doi.org/10.1101/gad.14.12.1498) | **Very high.** Architecture is predicted from sequence but strongly agrees with the supplied UniProt Ig-like/FN3 annotations. The queried accession is isoform B, whereas foundational work characterized the locus and principal coding sequence rather than Q0E9F2-specific isoform biology. |
| Myoblast expression and localization | Sns is expressed on **fusion-competent myoblasts (FCMs), not founder cells**, appears shortly before fusion, is enriched at the **plasma membrane**, and clusters at discrete myoblast-contact/fusion sites. *sns* null embryos retain specified, myosin-positive myoblasts but fail to form normal multinucleate body-wall muscles, placing Sns specifically at the recognition/adhesion/fusion stage rather than initial myogenic differentiation. (bour2000drosophilasnsa pages 2-4, bour2000drosophilasnsa pages 8-10, bour2000drosophilasnsa pages 1-2) | Null-mutant phenotyping, cell-type markers, immunofluorescence/confocal localization | Bour et al.; June 2000; [10.1101/gad.14.12.1498](https://doi.org/10.1101/gad.14.12.1498) | **Very high.** Direct genetic and localization evidence. Notch is required for formation of the Sns-positive FCM population, whereas MEF2 is not required for *sns* expression; this is transcriptional context, not evidence that Sns itself is a Notch-pathway receptor. |
| Kirre/Duf–Rst adhesion and actin signaling | Extracellular Sns engages founder-cell **Kirre/Dumbfounded (Duf)** or **Roughest (Rst)** in trans, coupling recognition and adhesion to localized actin remodeling. The supported mechanistic model links Sns to D-Crk/Dock-family adaptors and WASP/SCAR–Arp2/3 machinery, producing concentrated F-actin and invasive protrusions at the fusion interface. Sns also associates in cis with its paralog Hibris; both extracellular and intracellular regions contribute, with the Sns cytoplasmic region supporting more efficient fusion signaling. (shelton2009theimmunoglobulinsuperfamily pages 1-2, reissaus2007identificationandinitial pages 109-112, shelton2009theimmunoglobulinsuperfamily pages 8-9, shelton2009theimmunoglobulinsuperfamily pages 6-7) | Cell-adhesion assays, co-immunoprecipitation, genetics, domain chimeras/rescue, cytoskeletal perturbation | Shelton et al.; April 2009; [10.1242/dev.026302](https://doi.org/10.1242/dev.026302); mechanistic synthesis supported by later actin studies | **High for adhesion and pathway placement; moderate for a simple linear receptor-to-actin chain.** Multiple partially redundant adaptors and actin nucleators operate at fusion sites, and not every proposed physical link has been demonstrated directly in vivo. |
| Quantitative S2R+ fusion reconstitution | In an S2R+ reconstitution system, co-expression of Sns with the heterologous fusogen EFF-1 placed **86.3 ± 2.9%** of co-expressing cells in syncytia, versus **~12% with EFF-1 alone**. Sns was required in only one partner and induced F-actin-rich podosome-like protrusions; RNAi against WASP, WIP, or Scar eliminated the foci and Sns-enhanced fusion. (shilagardi2013actinpropelledinvasivemembrane pages 1-2, shilagardi2013actinpropelledinvasivemembrane pages 9-11) | Quantitative cell-fusion assay, live imaging, super-resolution microscopy, electron microscopy, RNAi | Shilagardi et al.; April 2013; [10.1126/science.1234781](https://doi.org/10.1126/science.1234781) | **High for Sns-driven actin protrusion and enhancement of fusion in this assay.** EFF-1 is a heterologous fusogen, so the result demonstrates an adhesion/actin-promoting role rather than proving that Sns is itself the endogenous Drosophila fusogen. |
| Nephrocyte slit diaphragm and current application | Sns is the fly **Nephrin-like** component paired with Kirre at nephrocyte slit diaphragms, where it is used as a structural marker and experimental readout of filtration-barrier organization. This conserved architecture underlies current use of Drosophila nephrocytes in podocyte, endocytosis, polarity, and kidney-disease modeling. Structural homology to human Nephrin was evident from the original sequence analysis. (bour2000drosophilasnsa pages 5-6) | Comparative sequence inference supplemented by nephrocyte localization, knockdown, filtration, and disease-model studies | Bour et al.; June 2000; [10.1101/gad.14.12.1498](https://doi.org/10.1101/gad.14.12.1498); continuing nephrocyte-model literature through 2024 | **High for conserved Nephrin-like identity; moderate in this evidence set for precise filtration mechanism.** The foundational excerpts establish homology but do not themselves provide nephrocyte filtration measurements; recent disease studies often use Sns as a diaphragm readout rather than investigate Sns mechanism directly. |
| Secondary neuronal and sensory roles | Loss and rescue experiments implicate Sns in **dendrite morphogenesis**, including altered higher-order branching in multidendritic sensory neurons; IRM-family studies also implicate Sns in sensory-organ spacing. These likely reflect context-dependent cell-recognition or cytoskeletal functions rather than its primary embryonic-muscle role. (reissaus2007identificationandinitial pages 10-14, reissaus2007identificationandinitial pages 109-112) | Mutant morphology, neuron-specific rescue, tissue-patterning genetics | Reissaus; 2007; [10.5282/edoc.7852](https://doi.org/10.5282/edoc.7852) | **Moderate to low.** Neuronal evidence includes a dissertation and allele-dependent phenotypes; mechanisms and physiological consequences are less firmly established than myoblast fusion. |
| 2023–2024 evidence landscape | Targeted searches identified **few 2023–2024 studies centered specifically on Sns**. Recent work chiefly deploys Sns/Kirre as an established slit-diaphragm module or marker in nephrocyte disease models; no recent result located here overturns the core adhesion-to-actin model established by 2000–2013 studies. | Targeted recent-literature assessment and comparison with foundational primary studies | Evidence base dominated by Bour et al. 2000 and Shilagardi et al. 2013 (bour2000drosophilasnsa pages 1-2, shilagardi2013actinpropelledinvasivemembrane pages 1-2) | **Moderate.** This is a literature-gap conclusion, not evidence of biological inactivity. Recent papers may mention or assay Sns without making it their principal research target. |


*Table: Evidence-ranked summary of the identity, architecture, localization, mechanisms, quantitative fusion activity, and research uses of Drosophila Sns (Q0E9F2). It separates strongly established primary functions from secondary roles and areas where recent Sns-centered evidence remains limited.*

## Key source details

- Bour BA, Chakravarti M, West JM, Abmayr SM. **“Drosophila SNS, a member of the immunoglobulin superfamily that is essential for myoblast fusion.”** *Genes & Development* 14:1498–1511. Published June 2000. DOI/URL: https://doi.org/10.1101/gad.14.12.1498. This is the principal identity, architecture, expression, localization, and null-phenotype study. (bour2000drosophilasnsa pages 2-4, bour2000drosophilasnsa pages 5-6, bour2000drosophilasnsa pages 1-2)
- Shelton C, Kocherlakota KS, Zhuang S, Abmayr SM. **“The immunoglobulin superfamily member Hbs functions redundantly with Sns in interactions between founder and fusion-competent myoblasts.”** *Development* 136:1159–1168. Published April 2009; accepted January 23, 2009. DOI/URL: https://doi.org/10.1242/dev.026302. This provides genetic, cis-association, and domain-comparison evidence. (shelton2009theimmunoglobulinsuperfamily pages 1-2, shelton2009theimmunoglobulinsuperfamily pages 6-7, shelton2009theimmunoglobulinsuperfamily pages 8-9)
- Shilagardi K et al. **“Actin-propelled invasive membrane protrusions promote fusogenic protein engagement during cell-cell fusion.”** *Science* 340:359–363. Published April 2013. DOI/URL: https://doi.org/10.1126/science.1234781. This supplies the strongest quantitative reconstitution and imaging evidence for Sns-driven protrusive actin remodeling. (shilagardi2013actinpropelledinvasivemembrane pages 1-2, shilagardi2013actinpropelledinvasivemembrane pages 9-11)

References

1. (bour2000drosophilasnsa pages 2-4): Barbara A. Bour, Malabika Chakravarti, Joshua M. West, and Susan M. Abmayr. Drosophila sns, a member of the immunoglobulin superfamily that is essential for myoblast fusion. Genes & development, 14 12:1498-511, Jun 2000. URL: https://doi.org/10.1101/gad.14.12.1498, doi:10.1101/gad.14.12.1498. This article has 333 citations and is from a highest quality peer-reviewed journal.

2. (bour2000drosophilasnsa pages 5-6): Barbara A. Bour, Malabika Chakravarti, Joshua M. West, and Susan M. Abmayr. Drosophila sns, a member of the immunoglobulin superfamily that is essential for myoblast fusion. Genes & development, 14 12:1498-511, Jun 2000. URL: https://doi.org/10.1101/gad.14.12.1498, doi:10.1101/gad.14.12.1498. This article has 333 citations and is from a highest quality peer-reviewed journal.

3. (shelton2009theimmunoglobulinsuperfamily pages 1-2): Claude Shelton, Kiranmai S. Kocherlakota, Shufei Zhuang, and Susan M. Abmayr. The immunoglobulin superfamily member hbs functions redundantly with sns in interactions between founder and fusion-competent myoblasts. Development, 136:1159-1168, Apr 2009. URL: https://doi.org/10.1242/dev.026302, doi:10.1242/dev.026302. This article has 94 citations and is from a domain leading peer-reviewed journal.

4. (shelton2009theimmunoglobulinsuperfamily pages 8-9): Claude Shelton, Kiranmai S. Kocherlakota, Shufei Zhuang, and Susan M. Abmayr. The immunoglobulin superfamily member hbs functions redundantly with sns in interactions between founder and fusion-competent myoblasts. Development, 136:1159-1168, Apr 2009. URL: https://doi.org/10.1242/dev.026302, doi:10.1242/dev.026302. This article has 94 citations and is from a domain leading peer-reviewed journal.

5. (bour2000drosophilasnsa pages 10-11): Barbara A. Bour, Malabika Chakravarti, Joshua M. West, and Susan M. Abmayr. Drosophila sns, a member of the immunoglobulin superfamily that is essential for myoblast fusion. Genes & development, 14 12:1498-511, Jun 2000. URL: https://doi.org/10.1101/gad.14.12.1498, doi:10.1101/gad.14.12.1498. This article has 333 citations and is from a highest quality peer-reviewed journal.

6. (bour2000drosophilasnsa pages 8-10): Barbara A. Bour, Malabika Chakravarti, Joshua M. West, and Susan M. Abmayr. Drosophila sns, a member of the immunoglobulin superfamily that is essential for myoblast fusion. Genes & development, 14 12:1498-511, Jun 2000. URL: https://doi.org/10.1101/gad.14.12.1498, doi:10.1101/gad.14.12.1498. This article has 333 citations and is from a highest quality peer-reviewed journal.

7. (bour2000drosophilasnsa pages 1-2): Barbara A. Bour, Malabika Chakravarti, Joshua M. West, and Susan M. Abmayr. Drosophila sns, a member of the immunoglobulin superfamily that is essential for myoblast fusion. Genes & development, 14 12:1498-511, Jun 2000. URL: https://doi.org/10.1101/gad.14.12.1498, doi:10.1101/gad.14.12.1498. This article has 333 citations and is from a highest quality peer-reviewed journal.

8. (reissaus2007identificationandinitial pages 109-112): Identification and initial characterization of the gene sticks and stones as a new regulator of dendrite morphogenesis in Drosophila This article has 0 citations.

9. (shilagardi2013actinpropelledinvasivemembrane pages 1-2): Khurts Shilagardi, Shuo Li, Fengbao Luo, Faiz Marikar, Rui Duan, Peng Jin, Ji Hoon Kim, Katherine Murnen, and Elizabeth H. Chen. Actin-propelled invasive membrane protrusions promote fusogenic protein engagement during cell-cell fusion. Science, 340:359-363, Apr 2013. URL: https://doi.org/10.1126/science.1234781, doi:10.1126/science.1234781. This article has 161 citations and is from a highest quality peer-reviewed journal.

10. (shelton2009theimmunoglobulinsuperfamily pages 6-7): Claude Shelton, Kiranmai S. Kocherlakota, Shufei Zhuang, and Susan M. Abmayr. The immunoglobulin superfamily member hbs functions redundantly with sns in interactions between founder and fusion-competent myoblasts. Development, 136:1159-1168, Apr 2009. URL: https://doi.org/10.1242/dev.026302, doi:10.1242/dev.026302. This article has 94 citations and is from a domain leading peer-reviewed journal.

11. (shilagardi2013actinpropelledinvasivemembrane pages 9-11): Khurts Shilagardi, Shuo Li, Fengbao Luo, Faiz Marikar, Rui Duan, Peng Jin, Ji Hoon Kim, Katherine Murnen, and Elizabeth H. Chen. Actin-propelled invasive membrane protrusions promote fusogenic protein engagement during cell-cell fusion. Science, 340:359-363, Apr 2013. URL: https://doi.org/10.1126/science.1234781, doi:10.1126/science.1234781. This article has 161 citations and is from a highest quality peer-reviewed journal.

12. (reissaus2007identificationandinitial pages 10-14): Identification and initial characterization of the gene sticks and stones as a new regulator of dendrite morphogenesis in Drosophila This article has 0 citations.

13. (bour2000drosophilasnsa pages 11-12): Barbara A. Bour, Malabika Chakravarti, Joshua M. West, and Susan M. Abmayr. Drosophila sns, a member of the immunoglobulin superfamily that is essential for myoblast fusion. Genes & development, 14 12:1498-511, Jun 2000. URL: https://doi.org/10.1101/gad.14.12.1498, doi:10.1101/gad.14.12.1498. This article has 333 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](sns-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. bour2000drosophilasnsa pages 5-6
2. shilagardi2013actinpropelledinvasivemembrane pages 1-2
3. reissaus2007identificationandinitial pages 109-112
4. bour2000drosophilasnsa pages 2-4
5. bour2000drosophilasnsa pages 10-11
6. shelton2009theimmunoglobulinsuperfamily pages 1-2
7. shelton2009theimmunoglobulinsuperfamily pages 8-9
8. bour2000drosophilasnsa pages 8-10
9. bour2000drosophilasnsa pages 1-2
10. shelton2009theimmunoglobulinsuperfamily pages 6-7
11. shilagardi2013actinpropelledinvasivemembrane pages 9-11
12. reissaus2007identificationandinitial pages 10-14
13. bour2000drosophilasnsa pages 11-12
14. 10.1101/gad.14.12.1498
15. 10.1242/dev.026302
16. 10.1126/science.1234781
17. 10.5282/edoc.7852
18. https://doi.org/10.1101/gad.14.12.1498
19. https://doi.org/10.1242/dev.026302
20. https://doi.org/10.1126/science.1234781
21. https://doi.org/10.5282/edoc.7852
22. https://doi.org/10.1101/gad.14.12.1498.
23. https://doi.org/10.1242/dev.026302.
24. https://doi.org/10.1126/science.1234781.
25. https://doi.org/10.1101/gad.14.12.1498,
26. https://doi.org/10.1242/dev.026302,
27. https://doi.org/10.1126/science.1234781,