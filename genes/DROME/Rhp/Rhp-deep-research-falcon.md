---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-10T14:55:55.201463'
end_time: '2026-09-10T15:01:00.976426'
duration_seconds: 305.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Rhp
  gene_symbol: Rhp
  uniprot_accession: Q9XYY9
  protein_description: 'SubName: Full=LD12055p {ECO:0000313|EMBL:AAX33549.1}; SubName:
    Full=Rhophilin {ECO:0000313|EMBL:AAD31273.1};'
  gene_info: Name=Rhp {ECO:0000313|EMBL:AAD31273.1, ECO:0000313|FlyBase:FBgn0026374};
    ORFNames=CG8497 {ECO:0000313|FlyBase:FBgn0026374};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the RHPN family.
  protein_domains: BRO1_dom. (IPR004328); BRO1_sf. (IPR038499); HR1_rho-bd. (IPR011072);
    HR1_rpt_sf. (IPR036274); PDZ. (IPR001478)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Rhp-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9XYY9
- **Protein Description:** SubName: Full=LD12055p {ECO:0000313|EMBL:AAX33549.1}; SubName: Full=Rhophilin {ECO:0000313|EMBL:AAD31273.1};
- **Gene Information:** Name=Rhp {ECO:0000313|EMBL:AAD31273.1, ECO:0000313|FlyBase:FBgn0026374}; ORFNames=CG8497 {ECO:0000313|FlyBase:FBgn0026374};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the RHPN family.
- **Key Domains:** BRO1_dom. (IPR004328); BRO1_sf. (IPR038499); HR1_rho-bd. (IPR011072); HR1_rpt_sf. (IPR036274); PDZ. (IPR001478)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rhp" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rhp' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rhp** (gene ID: Rhp, UniProt: Q9XYY9) in DROME.

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
- **UniProt Accession:** Q9XYY9
- **Protein Description:** SubName: Full=LD12055p {ECO:0000313|EMBL:AAX33549.1}; SubName: Full=Rhophilin {ECO:0000313|EMBL:AAD31273.1};
- **Gene Information:** Name=Rhp {ECO:0000313|EMBL:AAD31273.1, ECO:0000313|FlyBase:FBgn0026374}; ORFNames=CG8497 {ECO:0000313|FlyBase:FBgn0026374};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the RHPN family.
- **Key Domains:** BRO1_dom. (IPR004328); BRO1_sf. (IPR038499); HR1_rho-bd. (IPR011072); HR1_rpt_sf. (IPR036274); PDZ. (IPR001478)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rhp" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rhp' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rhp** (gene ID: Rhp, UniProt: Q9XYY9) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster* **Rhp** (Q9XYY9)

## Executive conclusion

The gene symbol **Rhp is ambiguous in cross-species searches, and literature is limited for this specific protein**. The requested target is the *D. melanogaster* gene **Rhp**, also **CG8497 / FBgn0026374**, encoding UniProt **Q9XYY9**, not human **RHPN1**, **RHPN2**, RHPN1-AS1, or another “Rhp”-like symbol. Indeed, an unqualified target search predominantly retrieves human RHPN1/RHPN2 disease associations rather than the fly protein, demonstrating why organism and accession constraints are essential (OpenTargets Search: -Rhp).

The strongest current annotation is that Rhp is a **non-enzymatic, multidomain rhophilin-family signaling adaptor**, probably associated with Rho-family signaling and cytoskeletal or membrane-organizing complexes. Its HR1/Rho-binding, Bro1-like, and PDZ domains support this interpretation. However, direct evidence that fly Rhp binds Rho1, controls actin, occupies a particular organelle, or participates in Hippo/STRIPAK signaling was not found. No target-specific 2023–2024 mechanistic publication was retrieved.

| Annotation question | Best-supported conclusion | Evidence type | Confidence / caveat |
|---|---|---|---|
| Identity | **Rhp** is the *Drosophila melanogaster* rhophilin-family gene **CG8497 / FBgn0026374**, encoding UniProt **Q9XYY9**; it must not be confused with human **RHPN1**, **RHPN2**, RHPN1-AS1, or unrelated “Rhp” symbols. | Identifier concordance from the supplied UniProt record; literature describes a single fly rhophilin gene, whereas target searches predominantly recover human paralogs (OpenTargets Search: -Rhp, peck2002therhoabindingprotein pages 9-10) | **High** for identifier mapping; symbol-only searches are highly ambiguous. |
| Protein class and domains | Rhp is best annotated as a **non-enzymatic, multidomain rhophilin-family signaling/adaptor protein**, with an N-terminal **HR1/Rho-binding region**, central **Bro1-like domain**, and C-terminal **PDZ domain**. The same overall architecture occurs in mammalian rhophilins (peck2002therhoabindingprotein pages 1-2) | Domain/family annotation plus conserved architecture in homologs | **High** for domain presence; **moderate** for assigning each domain’s fly-specific function because direct Rhp structure–function tests were not found. |
| Enzymatic status | No catalytic domain or catalysed reaction is established. Rhp is therefore not presently supported as an enzyme or transporter; its likely role is protein binding and assembly/regulation of signaling complexes. | Domain-based functional classification | **High** that no enzymatic reaction is established; unknown biochemical activities cannot be excluded. |
| Rho signaling | The HR1 region supports the hypothesis that fly Rhp binds **Rho-family GTPase, probably Rho1**, and acts as an effector or scaffold. Human RHPN1/RHPN2 bind RhoA in vitro, but nucleotide-state preferences and downstream consequences differ among assays and paralogs (peck2002therhoabindingprotein pages 8-9, peck2002therhoabindingprotein pages 9-10, peck2002therhoabindingprotein pages 1-2) | **Homolog-based inference**, not direct fly binding evidence | **Moderate** for pathway placement; **low-to-moderate** for precise ligand, nucleotide specificity, or regulatory direction in flies. |
| Actin phenotype | In a 2003 RNAi screen of approximately **90** actin-related genes in *Drosophila* S2 cells, Rhp depletion was classified as producing **no gross effect on lamellae**. Overall, **19/90** knockdowns produced obvious abnormal morphologies, while the authors identified 13 proteins contributing to normal lamella formation and seven involved in cytokinesis (rogers2003molecularrequirementsfor pages 3-4, rogers2003molecularrequirementsfor pages 8-9) | Direct fly-cell RNAi screening evidence | **Moderate for absence of a gross phenotype under that assay**, not evidence of no actin function: Rhp depletion was not confirmed by immunoblot, residual protein could suffice, and subtle or live-cell phenotypes could have been missed (rogers2003molecularrequirementsfor pages 8-9). |
| Embryonic requirement | A 2002 mammalian rhophilin paper states that knockout of the single *Drosophila* rhophilin gene was **embryonic lethal**, suggesting an essential developmental function (peck2002therhoabindingprotein pages 9-10) | Secondary report citing earlier screen/unpublished evidence | **Low-to-moderate**: the underlying fly experiment and allele-level data were not available in the retrieved literature, so penetrance, developmental stage, and causality cannot be independently assessed. |
| Cellular localization | No experimentally validated subcellular localization for endogenous fly Rhp was found. A cytoplasmic and/or membrane-associated signaling-complex localization is plausible from Rho-binding and PDZ-mediated scaffolding, but remains unverified. | Domain/homolog-based inference | **Low**; specific claims such as plasma membrane, endosome, cortex, junction, or nucleus would be premature. |
| Hippo/STRIPAK pathway | Mammalian RHPN1 participates in a proposed **RhoA–rhophilin–NF2/Kibra–STRIPAK** axis controlling Hippo kinase activation: active RhoA dissociates rhophilin and NF2/Kibra from STRIPAK, affecting MST/MAP4K dephosphorylation (chen2019stripakintegratesupstream pages 1-2). | **Mammalian homolog-based inference only** | **Low for fly Rhp**: no direct evidence was found that Q9XYY9 binds fly STRIPAK, Merlin/Kibra, or regulates Hippo signaling. |
| Broader actin mechanism | Human RHPN2 overexpression can disassemble stress fibers, requiring its Rho-binding, Bro1, and PDZ regions; RHPN1 lacked the same visible phenotype in that study (peck2002therhoabindingprotein pages 8-9, peck2002therhoabindingprotein pages 1-2). This supports a possible cytoskeletal adaptor role but also demonstrates paralog-specific behavior. | **Mammalian homolog-based inference**, with mutational evidence in human proteins | **Low-to-moderate for fly transfer**; these results cannot override the negative fly S2 lamella screen. |
| Applications and implementation | Current utility is principally **basic functional genomics**: Rhp can be tested as a candidate Rho-effector/scaffold in fly development, actomyosin organization, membrane trafficking, or Hippo/STRIPAK signaling using defined CRISPR alleles, rescue constructs, endogenous tagging, interaction assays, and live imaging. No validated therapeutic, diagnostic, industrial, patent, or clinical implementation specific to fly Rhp was found. | Research-gap analysis; absence of target-specific translational evidence | **High** that no established application was retrieved; proposed experiments are research recommendations, not demonstrated uses. |


*Table: Evidence-graded annotation of *Drosophila melanogaster* Rhp, distinguishing direct fly observations from hypotheses transferred from mammalian RHPN1/RHPN2. The table highlights substantial uncertainty around localization and pathway mechanism despite strong identity and domain assignments.*

## 1. Identity verification

The supplied identifiers are internally concordant:

- **Organism:** *Drosophila melanogaster* (DROME)
- **Gene:** **Rhp**
- **ORF:** **CG8497**
- **FlyBase identifier:** **FBgn0026374**
- **UniProt accession:** **Q9XYY9**
- **Protein names:** Rhophilin; LD12055p
- **Family:** RHPN/rhophilin family
- **Annotated domains:** HR1 Rho-binding region, Bro1-like domain, and PDZ domain

The literature also refers to a **single Drosophila rhophilin gene**, consistent with this target identity (peck2002therhoabindingprotein pages 9-10). Human RHPN1 and RHPN2 have related domain organization but are distinct proteins and cannot be treated as interchangeable with Q9XYY9.

## 2. Protein class and primary molecular function

### 2.1 Best-supported classification

Rhp is most plausibly a **protein-binding scaffold or Rho-associated adaptor**, not an enzyme, transporter, receptor, or structural filament protein. No catalytic domain, catalysed reaction, substrate conversion, or transported substrate has been established. Accordingly, enzyme kinetics and transporter specificity are not applicable on present evidence.

The domain architecture is informative:

- The **HR1 region** is characteristic of Rho-interacting modules and supports placement near Rho-family GTPase signaling.
- The **Bro1-like domain** likely supplies an additional protein- or membrane-complex interaction surface. Its presence alone does not establish canonical ESCRT/endosomal function.
- The **PDZ domain** is consistent with binding short peptide motifs and assembling localized signaling complexes, often near membranes.

Human Rhophilin-2 has the corresponding N-terminal Rho-binding, central Bro1-like, and C-terminal PDZ architecture, supporting evolutionary conservation of the overall scaffold design (peck2002therhoabindingprotein pages 1-2). This is structural inference, however, rather than a direct biochemical demonstration for fly Rhp.

### 2.2 Rho binding and nucleotide specificity

Mammalian RHPN1 and RHPN2 bound both GDP- and GTP-loaded RhoA in an in-vitro capture assay, but the authors noted that earlier mouse Rhophilin-1 work favored GTP-bound RhoA and that in-vivo nucleotide preference remained unresolved (peck2002therhoabindingprotein pages 8-9, peck2002therhoabindingprotein pages 9-10, peck2002therhoabindingprotein pages 1-2). Thus, the defensible fly annotation is **candidate Rho1-interacting protein**, not “proven active-Rho1-specific effector.” Direct binding of Q9XYY9 to fly Rho1, Rac, Cdc42, or another GTPase has not been established in the retrieved evidence.

## 3. Biological processes and pathways

### 3.1 Cytoskeletal regulation

The most relevant direct fly experiment is Rogers *et al.*, published **15 September 2003**, which depleted approximately **90 actin-associated or signaling proteins** in *Drosophila* S2 cells and examined spreading and lamella morphology. Rhophilin RNAi was placed in the **“no effect on lamellae”** group. Across the whole screen, 19 of approximately 90 knockdowns produced obvious abnormal morphologies; the authors ultimately identified 13 proteins contributing to normal lamella formation and seven involved in cytokinesis (rogers2003molecularrequirementsfor pages 1-2, rogers2003molecularrequirementsfor pages 3-4, rogers2003molecularrequirementsfor pages 8-9). DOI: https://doi.org/10.1083/jcb.200303023.

This negative result is narrow. It indicates that Rhp was not detectably required for **gross S2-cell lamellar morphology under that assay**, not that Rhp has no cytoskeletal function. The investigators explicitly warned that negative RNAi results may reflect incomplete depletion, sufficient residual protein, or phenotypes detectable only by live imaging; Rhp depletion was not among the targets documented as protein-level validated by immunoblot (rogers2003molecularrequirementsfor pages 3-4, rogers2003molecularrequirementsfor pages 8-9).

Mammalian RHPN2 overexpression caused actin stress-fiber loss in cultured cells, and disruption of its Rho-binding, Bro1, or PDZ regions abolished that phenotype despite retention of Rho binding by some mutants. RHPN1 did not produce the same visible phenotype, demonstrating substantial paralog-specific behavior (peck2002therhoabindingprotein pages 8-9, peck2002therhoabindingprotein pages 1-2). DOI: https://doi.org/10.1074/jbc.M203569200; online publication **6 September 2002**, issue publication **15 November 2002**. These results support—but do not prove—a possible fly role in controlling actin-complex assembly or turnover.

### 3.2 Developmental requirement

The 2002 RHPN2 paper states that knockout of the single *Drosophila* rhophilin gene was **embryonic lethal**, interpreting this as evidence for an important biological function (peck2002therhoabindingprotein pages 9-10). This is only a secondary statement in the available record; the underlying allele, penetrance, developmental arrest point, rescue evidence, and exclusion of linked mutations were not available for assessment. It should therefore be treated as **provisional evidence of essentiality**, not a fully validated mechanistic phenotype.

### 3.3 Hippo/STRIPAK signaling: plausible but unverified in flies

A mammalian study published **December 2019** identified a RhoA–rhophilin–NF2/Kibra–STRIPAK signaling axis. In that system, serum or lysophosphatidic acid activated RhoA, which bound and displaced rhophilin and NF2/Kibra from STRIPAK, promoting STRIPAK-dependent dephosphorylation of MST/MAP4K Hippo kinases. RHPN1 also suppressed anchorage-independent growth in a LATS1/2-dependent manner (chen2019stripakintegratesupstream pages 1-2, chen2019stripakintegratesupstream pages 10-11). DOI: https://doi.org/10.1038/s41556-019-0426-y.

This is an important hypothesis-generating result because Hippo, Merlin, Kibra, and STRIPAK components are conserved. Nevertheless, no retrieved experiment showed that fly Rhp binds fly Merlin, Kibra, STRIPAK, Hippo, or related kinases. Assigning Q9XYY9 directly to the fly Hippo pathway would therefore be premature.

## 4. Cellular localization

No experimentally validated localization of **endogenous Drosophila Rhp** was found. Domain architecture makes a soluble cytoplasmic protein recruited to membranes or cortical signaling complexes plausible: Rho proteins are membrane-associated, while PDZ domains commonly organize submembranous complexes. The Bro1-like domain could additionally support membrane or endosomal association. None of these possibilities establishes a specific plasma-membrane, junctional, endosomal, Golgi, nuclear, or cytoskeletal localization.

Consequently, the current location annotation should read: **intracellular signaling/adaptor protein; precise subcellular site unknown**.

## 5. Current understanding and expert assessment

The literature supports a conservative model in which Rhp receives or organizes Rho-family signals through its HR1 region and couples them, through Bro1- and PDZ-mediated interactions, to localized protein complexes. Potential outputs include actin organization, membrane traffic, or conserved growth-control signaling. The domain combination argues strongly for an adaptor function, but it does not identify the binding partners or direction of regulation in flies.

The mammalian evidence is internally cautionary. RHPN1 and RHPN2 share architecture and RhoA binding, yet only RHPN2 visibly disassembled stress fibers in the 2002 comparison (peck2002therhoabindingprotein pages 8-9, peck2002therhoabindingprotein pages 1-2). Functional transfer from a mammalian paralog to the single fly protein therefore cannot be assumed.

## 6. Recent research and evidence gaps

No 2023–2024 publication specifically resolving the function of **Rhp/CG8497/Q9XYY9** was retrieved using the accession, gene symbol, CG number, FlyBase identifier, organism, and domain combinations. Recent disease-oriented “rhophilin” literature predominantly concerns human RHPN1/RHPN2; OpenTargets results, for example, map the term to human RHPN1/RHPN2 cancer associations rather than Drosophila Q9XYY9 (OpenTargets Search: -Rhp). Such studies were excluded as direct evidence.

Major unresolved questions are:

1. Does endogenous Rhp bind fly Rho1, and is binding GTP-state selective?
2. Which proteins bind its PDZ and Bro1-like domains?
3. Is the reported embryonic lethality reproducible with defined null alleles and genomic rescue?
4. Where is endogenous Rhp localized in embryos and adult tissues?
5. Does it affect actomyosin behavior, endosomal trafficking, or Hippo/STRIPAK output under specific developmental or mechanical conditions?

## 7. Applications and real-world implementation

No therapeutic, diagnostic, industrial, clinical-trial, or patented implementation specific to fly Rhp was identified. Its present application is as a **basic-research candidate for dissecting conserved Rho-effector and scaffold biology**. The most informative implementation would combine:

- CRISPR-generated null and domain-specific alleles;
- genomic rescue to validate essentiality;
- endogenous fluorescent tagging and live imaging;
- Rho1-GTP-dependent interaction assays;
- quantitative actomyosin, cytokinesis, epithelial-junction, and trafficking phenotyping;
- proximity labeling or affinity purification–mass spectrometry;
- genetic interaction tests with Rho1, Rok, Dia, Merlin, Kibra, Hippo, and STRIPAK components.

## Final annotation

**Rhp/Q9XYY9 is a poorly characterized *Drosophila melanogaster* rhophilin-family, non-enzymatic signaling adaptor. Its HR1–Bro1–PDZ architecture supports a likely role in assembling Rho-associated intracellular signaling complexes, potentially affecting cytoskeletal or membrane-linked processes. Direct fly evidence is limited to a negative gross-lamella RNAi result and a secondary report of embryonic lethality. Precise binding specificity, pathway placement, biological output, and subcellular localization remain unestablished.**

References

1. (OpenTargets Search: -Rhp): Open Targets Query (-Rhp, 32 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (peck2002therhoabindingprotein pages 9-10): Jeremy W. Peck, Michael Oberst, Kerrie B. Bouker, Emma Bowden, and Peter D. Burbelo. The rhoa-binding protein, rhophilin-2, regulates actin cytoskeleton organization*. The Journal of Biological Chemistry, 277:43924-43932, Nov 2002. URL: https://doi.org/10.1074/jbc.m203569200, doi:10.1074/jbc.m203569200. This article has 115 citations.

3. (peck2002therhoabindingprotein pages 1-2): Jeremy W. Peck, Michael Oberst, Kerrie B. Bouker, Emma Bowden, and Peter D. Burbelo. The rhoa-binding protein, rhophilin-2, regulates actin cytoskeleton organization*. The Journal of Biological Chemistry, 277:43924-43932, Nov 2002. URL: https://doi.org/10.1074/jbc.m203569200, doi:10.1074/jbc.m203569200. This article has 115 citations.

4. (peck2002therhoabindingprotein pages 8-9): Jeremy W. Peck, Michael Oberst, Kerrie B. Bouker, Emma Bowden, and Peter D. Burbelo. The rhoa-binding protein, rhophilin-2, regulates actin cytoskeleton organization*. The Journal of Biological Chemistry, 277:43924-43932, Nov 2002. URL: https://doi.org/10.1074/jbc.m203569200, doi:10.1074/jbc.m203569200. This article has 115 citations.

5. (rogers2003molecularrequirementsfor pages 3-4): Stephen L. Rogers, Ursula Wiedemann, Nico Stuurman, and Ronald D. Vale. Molecular requirements for actin-based lamella formation in drosophila s2 cells. The Journal of Cell Biology, 162:1079-1088, Sep 2003. URL: https://doi.org/10.1083/jcb.200303023, doi:10.1083/jcb.200303023. This article has 505 citations.

6. (rogers2003molecularrequirementsfor pages 8-9): Stephen L. Rogers, Ursula Wiedemann, Nico Stuurman, and Ronald D. Vale. Molecular requirements for actin-based lamella formation in drosophila s2 cells. The Journal of Cell Biology, 162:1079-1088, Sep 2003. URL: https://doi.org/10.1083/jcb.200303023, doi:10.1083/jcb.200303023. This article has 505 citations.

7. (chen2019stripakintegratesupstream pages 1-2): Rui Chen, Ruiling Xie, Zhipeng Meng, Shenghong Ma, and Kun-Liang Guan. Stripak integrates upstream signals to initiate the hippo kinase cascade. Nature Cell Biology, 21:1565-1577, Dec 2019. URL: https://doi.org/10.1038/s41556-019-0426-y, doi:10.1038/s41556-019-0426-y. This article has 155 citations and is from a highest quality peer-reviewed journal.

8. (rogers2003molecularrequirementsfor pages 1-2): Stephen L. Rogers, Ursula Wiedemann, Nico Stuurman, and Ronald D. Vale. Molecular requirements for actin-based lamella formation in drosophila s2 cells. The Journal of Cell Biology, 162:1079-1088, Sep 2003. URL: https://doi.org/10.1083/jcb.200303023, doi:10.1083/jcb.200303023. This article has 505 citations.

9. (chen2019stripakintegratesupstream pages 10-11): Rui Chen, Ruiling Xie, Zhipeng Meng, Shenghong Ma, and Kun-Liang Guan. Stripak integrates upstream signals to initiate the hippo kinase cascade. Nature Cell Biology, 21:1565-1577, Dec 2019. URL: https://doi.org/10.1038/s41556-019-0426-y, doi:10.1038/s41556-019-0426-y. This article has 155 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Rhp-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. peck2002therhoabindingprotein pages 1-2
2. rogers2003molecularrequirementsfor pages 8-9
3. peck2002therhoabindingprotein pages 9-10
4. chen2019stripakintegratesupstream pages 1-2
5. peck2002therhoabindingprotein pages 8-9
6. rogers2003molecularrequirementsfor pages 3-4
7. rogers2003molecularrequirementsfor pages 1-2
8. chen2019stripakintegratesupstream pages 10-11
9. https://doi.org/10.1083/jcb.200303023.
10. https://doi.org/10.1074/jbc.M203569200;
11. https://doi.org/10.1038/s41556-019-0426-y.
12. https://doi.org/10.1074/jbc.m203569200,
13. https://doi.org/10.1083/jcb.200303023,
14. https://doi.org/10.1038/s41556-019-0426-y,