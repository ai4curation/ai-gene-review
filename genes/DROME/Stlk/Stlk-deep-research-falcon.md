---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T13:08:39.215307'
end_time: '2026-10-09T13:16:26.701184'
duration_seconds: 467.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Stlk
  gene_symbol: Stlk
  uniprot_accession: P83098
  protein_description: 'RecName: Full=STE20-related kinase adapter protein stlk {ECO:0000305};
    Short=STRAD {ECO:0000305}; AltName: Full=Ste20-like kinase {ECO:0000312|FlyBase:FBgn0046692};'
  gene_info: Name=Stlk {ECO:0000312|FlyBase:FBgn0046692}; Synonyms=STRADalpha {ECO:0000312|FlyBase:FBgn0046692};
    ORFNames=CG40293 {ECO:0000312|FlyBase:FBgn0046692};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the protein kinase superfamily. STE Ser/Thr
  protein_domains: Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719);
    STRAD_A/B-like. (IPR047173); Pkinase (PF00069)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Stlk-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P83098
- **Protein Description:** RecName: Full=STE20-related kinase adapter protein stlk {ECO:0000305}; Short=STRAD {ECO:0000305}; AltName: Full=Ste20-like kinase {ECO:0000312|FlyBase:FBgn0046692};
- **Gene Information:** Name=Stlk {ECO:0000312|FlyBase:FBgn0046692}; Synonyms=STRADalpha {ECO:0000312|FlyBase:FBgn0046692}; ORFNames=CG40293 {ECO:0000312|FlyBase:FBgn0046692};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the protein kinase superfamily. STE Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); STRAD_A/B-like. (IPR047173); Pkinase (PF00069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Stlk" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Stlk' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Stlk** (gene ID: Stlk, UniProt: P83098) in DROME.

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
- **UniProt Accession:** P83098
- **Protein Description:** RecName: Full=STE20-related kinase adapter protein stlk {ECO:0000305}; Short=STRAD {ECO:0000305}; AltName: Full=Ste20-like kinase {ECO:0000312|FlyBase:FBgn0046692};
- **Gene Information:** Name=Stlk {ECO:0000312|FlyBase:FBgn0046692}; Synonyms=STRADalpha {ECO:0000312|FlyBase:FBgn0046692}; ORFNames=CG40293 {ECO:0000312|FlyBase:FBgn0046692};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the protein kinase superfamily. STE Ser/Thr
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); STRAD_A/B-like. (IPR047173); Pkinase (PF00069)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Stlk" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Stlk' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Stlk** (gene ID: Stlk, UniProt: P83098) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* Stlk (UniProt P83098)

## Identity and scope

**The gene symbol ‘Stlk’ is ambiguous or literature is limited for this specific protein.** Here, Stlk means the *D. melanogaster* protein identified in the supplied UniProt record as P83098, also named STRAD/STRADalpha and associated with CG40293 and FlyBase FBgn0046692. The retrieved fly literature independently uses **Stlk** for a kinase-family *pseudokinase* and an LKB1 cofactor; it distinguishes Stlk from **LKB1**, the catalytically active kinase. The papers did not independently provide a P83098-to-CG40293 cross-reference, so that precise identifier mapping rests on the UniProt information supplied in the question. Neither mammalian STRADα experiments nor studies of other Ste20 kinases should be presented as direct evidence about fly Stlk. (borkowsky2023phosphorylationoflkb1 pages 7-8, thiele2016subcellularlocalizationof pages 14-18, zheng2015identificationofhappyhourmap4k pages 3-4)

**Best-supported primary function:** Stlk is a **STRAD-like, kinase-fold regulatory adaptor for LKB1 signaling**, rather than an established phosphotransferase. Its annotated protein-kinase/STE-related and STRAD-like domains are compatible with this interpretation. Fly-focused sequence analysis reported that Stlk lacks residues required for kinase activity, and a 2015 *Drosophila* Ste20-family screen explicitly called it a pseudokinase and *excluded* it from the screen of candidate active kinases. No purified-fly-Stlk catalytic assay establishing either an enzymatic reaction or a substrate specificity was identified. Thus, no phosphorylation reaction or protein substrate should be assigned to Stlk itself. (thiele2016subcellularlocalizationof pages 14-18, zheng2015identificationofhappyhourmap4k pages 3-4)

The evidence and its limits can be summarized as follows. (borkowsky2023phosphorylationoflkb1 pages 7-8, thiele2016subcellularlocalizationof pages 14-18, borkowsky2023phosphorylationoflkb1 pages 8-10, zeqiraj2009atpandmo25α pages 1-2)

| Claim | Experimental evidence in fly | Limits / inference |
|---|---|---|
| **Stlk is a kinase-fold pseudokinase rather than an active Ste20 kinase.** | A 2015 *Drosophila* Ste20-family study classified Stlk as a pseudokinase and excluded it from a screen of catalytically active Ste20 kinases. A fly-focused analysis reported that the *Drosophila* STRAD homolog lacks key residues required for kinase activity (zheng2015identificationofhappyhourmap4k pages 3-4, thiele2016subcellularlocalizationof pages 14-18). | The assignment is supported by family classification and sequence, but no direct catalytic assay of purified fly Stlk was identified. The papers did not state the exact P83098/CG40293 cross-reference. |
| **Stlk associates with the LKB1–Mo25 regulatory complex.** | In 2023, *Drosophila* S2R+ cells were cotransfected with Stlk-Myc, Mo25-HA, and GFP-LKB1. GFP-LKB1 immunoprecipitation followed by immunoblotting tested association with the tagged cofactors in fly-derived cells (borkowsky2023phosphorylationoflkb1 pages 8-10). | The experiment used tagged, overexpressed proteins rather than endogenous Stlk. It supports association under these conditions but does not establish direct binding or the stoichiometry of a native complex. |
| **LKB1 T353 phosphorylation is not required for detectable Stlk/Mo25 association.** | Co-immunoprecipitation detected no difference in Stlk/Mo25 binding between wild-type LKB1 and phosphorylation-deficient LKB1-T353A. T353 was also predicted to lie outside the cofactor interface (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 8-10). | This negative result applies to one LKB1 substitution and assay context. It neither defines the complete Stlk-binding interface nor excludes small affinity changes. |
| **Stlk participates as a cofactor in an LKB1-to-AMPK assay system.** | A 2023 in-vitro assay combined LKB1 variants, Stlk, and recombinant GST-AMPK residues 108–280; the study described Stlk as an LKB1 cofactor (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 8-10). | The assay evaluated LKB1 activity toward AMPK. It does not show that Stlk phosphorylates AMPK, establish Stlk catalytic activity, or isolate Stlk's quantitative contribution. |
| **The likely primary molecular role is allosteric or adaptor regulation of LKB1.** | Fly co-immunoprecipitation and inclusion of Stlk in the kinase assay support a cofactor role (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 8-10). | Mechanistic detail is inferred mainly from human STRADα. Structural experiments showed ATP binding, MO25-dependent stabilization of a closed kinase-like conformation, and LKB1 activation despite undetectable STRADα phosphotransferase activity; conservation of this complete mechanism in fly Stlk remains untested (zeqiraj2009atpandmo25α pages 1-2, zeqiraj2009atpandmo25α pages 5-6). |
| **Stlk is provisionally linked to the LKB1–AMPK pathway and downstream mTOR/growth regulation.** | The 2023 fly study included Stlk in LKB1 biochemical assays and showed that altered LKB1 regulation changes AMPK phosphorylation, S6K/mTOR signaling, proliferation, and body size (borkowsky2023phosphorylationoflkb1 pages 1-2, borkowsky2023phosphorylationoflkb1 pages 5-7). | The organismal phenotypes arose from LKB1 knock-in alleles, not Stlk mutation or depletion. They establish pathway context but cannot be attributed specifically to Stlk. |
| **Endogenous subcellular localization of fly Stlk is unresolved.** | No direct endogenous *Drosophila* Stlk localization experiment was identified. Earlier fly-focused work stated that the Stlk homolog had not yet been investigated (thiele2016subcellularlocalizationof pages 14-18). | Cytoplasmic relocalization and nucleocytoplasmic shuttling are established principally for mammalian LKB1–STRAD complexes and are not demonstrated localization results for fly Stlk (trelford2024lkb1biologyassessing pages 2-4). |
| **A fly Stlk loss-of-function phenotype remains unestablished in the retrieved literature.** | No Stlk-null, RNAi-knockdown, rescue, or endogenous allelic phenotype was identified in the retrieved fly studies. | No defensible Stlk-specific statistics are available for viability, polarity, AMPK activity, cell size, or development. Reported proliferation values of 0.9%, 1.2%, and 1.4% concern LKB1 alleles rather than Stlk (borkowsky2023phosphorylationoflkb1 pages 5-7). |


*Table: This table separates direct Drosophila Stlk evidence from pathway context and mammalian STRADα-based inference. It highlights support for an LKB1-associated pseudokinase role and major gaps in endogenous localization, catalytic testing, and fly loss-of-function genetics.*

## Molecular mechanism and pathway

The most informative **direct experiment on fly Stlk** is Borkowsky and colleagues’ 2023 study. In *Drosophila*-derived S2R+ cells, the authors expressed tagged Stlk-Myc and Mo25-HA alongside GFP-tagged LKB1, immunoprecipitated GFP-LKB1, and examined cofactor association by immunoblotting. They describe Stlk and Mo25 as LKB1 cofactors and report **no detectable difference in their association** between wild-type LKB1 and the phosphorylation-deficient LKB1-T353A variant. This supports Stlk’s association with an LKB1-containing complex *under tagged-expression conditions*, but does not establish direct Stlk–LKB1 binding, native complex stoichiometry, or an endogenous interaction in fly tissues. (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 8-10)

The same study included Stlk with LKB1 variants in an **in-vitro kinase assay using recombinant GST-AMPK residues 108–280**. This places Stlk in a biochemical assay of the **LKB1 → AMPK** pathway; **LKB1, not Stlk, is the kinase being assayed against AMPK**. Because the reported comparison concerns LKB1 variants rather than an assay with and without Stlk, it does not measure how much Stlk independently increases LKB1 activity or show that Stlk phosphorylates AMPK. (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 5-7)

The mechanistic model is stronger in **human STRADα**, and should be applied to fly Stlk only as a conservation-based inference. Structural and biochemical experiments show that human STRADα binds ATP and MO25α, adopts a closed kinase-like conformation despite lacking detectable phosphorylation activity against tested substrates, and helps activate LKB1 in a regulatory complex. The MO25–STRAD interface and ATP-dependent conformation provide a plausible explanation for why a kinase-like *adaptor* can regulate a kinase without itself catalyzing phosphorylation. A 2024 review likewise describes STRAD-dependent allosteric activation and relocalization of mammalian LKB1. These sources do **not** demonstrate the complete ATP-binding, MO25-binding, or allosteric mechanism for P83098 itself. (zeqiraj2009atpandmo25α pages 1-2, zeqiraj2009atpandmo25α pages 5-6, trelford2024lkb1biologyassessing pages 2-4)

**Biological-process assignment should therefore be qualified:** Stlk is experimentally connected to the fly LKB1–Mo25/AMPK biochemical system, making regulation of energy-responsive AMPK signaling its most defensible pathway annotation. In 2023, fly **LKB1** T353 knock-in experiments linked changed LKB1 regulation to AMPK phosphorylation, S6K/mTOR signaling and growth. Those outcomes provide context for Stlk’s likely pathway role, **not evidence that Stlk mutation causes them**. For example, the reported percentages of proliferating wing-disc clone cells—**0.9%** for LKB1-T353A, **1.2%** for wild type and **1.4%** for LKB1-T353D—compare *LKB1 alleles*, not Stlk alleles. No Stlk-specific growth-effect estimate is warranted. (borkowsky2023phosphorylationoflkb1 pages 1-2, borkowsky2023phosphorylationoflkb1 pages 5-7)

Stlk’s Ste20-related name must also **not** be read as evidence that it catalyzes a Hippo-pathway phosphorylation. The 2015 screen that identified the active Ste20-family Hippo regulator Happyhour omitted pseudokinase Stlk; its phosphorylation results therefore cannot be transferred to Stlk. (zheng2015identificationofhappyhourmap4k pages 3-4)

## Where Stlk acts

**Endogenous subcellular localization of fly Stlk remains unresolved in the retrieved studies.** The fly-cell association assay establishes that tagged Stlk can participate in an LKB1-containing complex in cell lysates, but does not identify whether endogenous Stlk acts predominantly in the cytosol, at membranes, or elsewhere. A fly-focused 2016 analysis explicitly noted that the *Drosophila* STRAD homolog had not then been directly investigated; its discussion of STRAD-mediated nuclear export referred to mammalian experiments. Subsequent mammalian reviews describe STRAD-dependent cytoplasmic localization of LKB1, but that is a hypothesis for fly Stlk’s localization and regulatory role, **not a demonstrated P83098 localization**. Similarly, experiments locating fly **LKB1** at membranes cannot locate Stlk by proxy. (thiele2016subcellularlocalizationof pages 14-18, borkowsky2023phosphorylationoflkb1 pages 8-10, trelford2024lkb1biologyassessing pages 2-4, borkowsky2023phosphorylationoflkb1 pages 2-4)

## State of research and use

The **2023 primary fly study** advances Stlk annotation from sequence-based prediction to an experimentally examined LKB1-cofactor association, while the **2024 authoritative review** refines the general STRAD–LKB1 mechanism chiefly through mammalian evidence. In the retrieved literature, practical implementation is research use of tagged fly Stlk in S2R+ co-immunoprecipitation and inclusion of Stlk in LKB1–AMPK kinase assays. No Stlk-directed clinical application, fly Stlk loss-of-function/rescue analysis, Stlk-specific physiological statistic, or validated endogenous localization was identified. The priority for a more definitive annotation is to test fly Stlk directly for catalytic activity and nucleotide/Mo25 binding, then assess endogenous localization and the consequences of Stlk-specific perturbation for LKB1–AMPK signaling. (borkowsky2023phosphorylationoflkb1 pages 7-8, borkowsky2023phosphorylationoflkb1 pages 8-10, trelford2024lkb1biologyassessing pages 2-4, zeqiraj2009atpandmo25α pages 1-2)

### Principal sources

- **Borkowsky S, et al.** “Phosphorylation of LKB1 by PDK1 Inhibits Cell Proliferation and Organ Growth by Decreased Activation of AMPK.” *Cells*, **published 6 March 2023**. Fly Stlk co-immunoprecipitation and LKB1/AMPK assay: https://doi.org/10.3390/cells12050812. (borkowsky2023phosphorylationoflkb1 pages 1-2, borkowsky2023phosphorylationoflkb1 pages 8-10)
- **Trelford CB, Shepherd TG.** “LKB1 biology: assessing the therapeutic relevancy of LKB1 inhibitors.” *Cell Communication and Signaling*, **June 2024**. Review of predominantly mammalian STRAD–MO25–LKB1 regulation: https://doi.org/10.1186/s12964-024-01689-5. (trelford2024lkb1biologyassessing pages 2-4)
- **Zeqiraj E, et al.** “ATP and MO25α Regulate the Conformational State of the STRADα Pseudokinase and Activation of the LKB1 Tumour Suppressor.” *PLoS Biology*, **published 9 June 2009**. Human-protein structural and biochemical mechanism: https://doi.org/10.1371/journal.pbio.1000126. (zeqiraj2009atpandmo25α pages 1-2, zeqiraj2009atpandmo25α pages 5-6)
- **Zheng Y, et al.** “Identification of Happyhour/MAP4K as Alternative Hpo/Mst-like Kinases in the Hippo Kinase Cascade.” *Developmental Cell*, **28 September 2015**. Fly Ste20-family screen identifying Stlk as the excluded pseudokinase: https://doi.org/10.1016/j.devcel.2015.08.014. (zheng2015identificationofhappyhourmap4k pages 3-4)
- **Thiele CVS.** *Subcellular localization of LKB1 and characterization of its interactions with the membrane skeleton in Drosophila melanogaster*, **2016**. Fly-focused analysis distinguishing the uncharacterized Stlk homolog from LKB1; a dissertation rather than Stlk-specific primary characterization: https://doi.org/10.5283/epub.31340. (thiele2016subcellularlocalizationof pages 14-18)

References

1. (borkowsky2023phosphorylationoflkb1 pages 7-8): Sarah Borkowsky, Maximilian Gass, Azadeh Alavizargar, Johannes Hanewinkel, Ina Hallstein, Pavel I. Nedvetsky, Andreas Heuer, and Michael Peter Rolf Krahn. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. Text, Mar 2023. URL: https://doi.org/10.17879/90089628698, doi:10.17879/90089628698. This article has 13 citations and is from a peer-reviewed journal.

2. (thiele2016subcellularlocalizationof pages 14-18): Christian Volker Steffen Thiele. Subcellular localization of lkb1 and characterization of its interactions with the membrane skeleton in drosophila melanogaster. Text, Jan 2016. URL: https://doi.org/10.5283/epub.31340, doi:10.5283/epub.31340. This article has 0 citations and is from a peer-reviewed journal.

3. (zheng2015identificationofhappyhourmap4k pages 3-4): Yonggang Zheng, Wei Wang, Bo Liu, Hua Deng, Eliza Uster, and Duojia Pan. Identification of happyhour/map4k as alternative hpo/mst-like kinases in the hippo kinase cascade. Developmental cell, 34 6:642-55, Sep 2015. URL: https://doi.org/10.1016/j.devcel.2015.08.014, doi:10.1016/j.devcel.2015.08.014. This article has 281 citations and is from a highest quality peer-reviewed journal.

4. (borkowsky2023phosphorylationoflkb1 pages 8-10): Sarah Borkowsky, Maximilian Gass, Azadeh Alavizargar, Johannes Hanewinkel, Ina Hallstein, Pavel I. Nedvetsky, Andreas Heuer, and Michael Peter Rolf Krahn. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. Text, Mar 2023. URL: https://doi.org/10.17879/90089628698, doi:10.17879/90089628698. This article has 13 citations and is from a peer-reviewed journal.

5. (zeqiraj2009atpandmo25α pages 1-2): Elton Zeqiraj, Beatrice Maria Filippi, Simon Goldie, Iva Navratilova, Jérôme Boudeau, Maria Deak, Dario R. Alessi, and Daan M. F. van Aalten. Atp and mo25α regulate the conformational state of the stradα pseudokinase and activation of the lkb1 tumour suppressor. PLoS Biology, 7:e1000126, Jun 2009. URL: https://doi.org/10.1371/journal.pbio.1000126, doi:10.1371/journal.pbio.1000126. This article has 177 citations and is from a highest quality peer-reviewed journal.

6. (zeqiraj2009atpandmo25α pages 5-6): Elton Zeqiraj, Beatrice Maria Filippi, Simon Goldie, Iva Navratilova, Jérôme Boudeau, Maria Deak, Dario R. Alessi, and Daan M. F. van Aalten. Atp and mo25α regulate the conformational state of the stradα pseudokinase and activation of the lkb1 tumour suppressor. PLoS Biology, 7:e1000126, Jun 2009. URL: https://doi.org/10.1371/journal.pbio.1000126, doi:10.1371/journal.pbio.1000126. This article has 177 citations and is from a highest quality peer-reviewed journal.

7. (borkowsky2023phosphorylationoflkb1 pages 1-2): Sarah Borkowsky, Maximilian Gass, Azadeh Alavizargar, Johannes Hanewinkel, Ina Hallstein, Pavel I. Nedvetsky, Andreas Heuer, and Michael Peter Rolf Krahn. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. Text, Mar 2023. URL: https://doi.org/10.17879/90089628698, doi:10.17879/90089628698. This article has 13 citations and is from a peer-reviewed journal.

8. (borkowsky2023phosphorylationoflkb1 pages 5-7): Sarah Borkowsky, Maximilian Gass, Azadeh Alavizargar, Johannes Hanewinkel, Ina Hallstein, Pavel I. Nedvetsky, Andreas Heuer, and Michael Peter Rolf Krahn. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. Text, Mar 2023. URL: https://doi.org/10.17879/90089628698, doi:10.17879/90089628698. This article has 13 citations and is from a peer-reviewed journal.

9. (trelford2024lkb1biologyassessing pages 2-4): Charles B. Trelford and Trevor G. Shepherd. Lkb1 biology: assessing the therapeutic relevancy of lkb1 inhibitors. Cell Communication and Signaling : CCS, Jun 2024. URL: https://doi.org/10.1186/s12964-024-01689-5, doi:10.1186/s12964-024-01689-5. This article has 32 citations.

10. (borkowsky2023phosphorylationoflkb1 pages 2-4): Sarah Borkowsky, Maximilian Gass, Azadeh Alavizargar, Johannes Hanewinkel, Ina Hallstein, Pavel I. Nedvetsky, Andreas Heuer, and Michael Peter Rolf Krahn. Phosphorylation of lkb1 by pdk1 inhibits cell proliferation and organ growth by decreased activation of ampk. Text, Mar 2023. URL: https://doi.org/10.17879/90089628698, doi:10.17879/90089628698. This article has 13 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Stlk-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. thiele2016subcellularlocalizationof pages 14-18
2. https://doi.org/10.3390/cells12050812.
3. https://doi.org/10.1186/s12964-024-01689-5.
4. https://doi.org/10.1371/journal.pbio.1000126.
5. https://doi.org/10.1016/j.devcel.2015.08.014.
6. https://doi.org/10.5283/epub.31340.
7. https://doi.org/10.17879/90089628698,
8. https://doi.org/10.5283/epub.31340,
9. https://doi.org/10.1016/j.devcel.2015.08.014,
10. https://doi.org/10.1371/journal.pbio.1000126,
11. https://doi.org/10.1186/s12964-024-01689-5,