---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T20:02:40.979453'
end_time: '2026-09-08T20:08:23.370400'
duration_seconds: 342.39
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: NEUCR
  gene_id: mek-1
  gene_symbol: mek-1
  uniprot_accession: Q7RYZ6
  protein_description: 'RecName: Full=Serine/threonine-protein {ECO:0000256|PROSITE-ProRule:PRU10027};
    EC=2.7.11.1 {ECO:0000256|PROSITE-ProRule:PRU10027};'
  gene_info: Name=mek-1 {ECO:0000313|EMBL:EAA28074.3}; ORFNames=NCU06419 {ECO:0000313|EMBL:EAA28074.3};
  organism_full: Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 /
    DSM 1257 / FGSC 987).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915);
    Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS.
    (IPR008271)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: mek-1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q7RYZ6
- **Protein Description:** RecName: Full=Serine/threonine-protein {ECO:0000256|PROSITE-ProRule:PRU10027}; EC=2.7.11.1 {ECO:0000256|PROSITE-ProRule:PRU10027};
- **Gene Information:** Name=mek-1 {ECO:0000313|EMBL:EAA28074.3}; ORFNames=NCU06419 {ECO:0000313|EMBL:EAA28074.3};
- **Organism (full):** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mek-1" matches the protein description above**
2. **Verify the organism is correct:** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mek-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mek-1** (gene ID: mek-1, UniProt: Q7RYZ6) in NEUCR.

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
- **UniProt Accession:** Q7RYZ6
- **Protein Description:** RecName: Full=Serine/threonine-protein {ECO:0000256|PROSITE-ProRule:PRU10027}; EC=2.7.11.1 {ECO:0000256|PROSITE-ProRule:PRU10027};
- **Gene Information:** Name=mek-1 {ECO:0000313|EMBL:EAA28074.3}; ORFNames=NCU06419 {ECO:0000313|EMBL:EAA28074.3};
- **Organism (full):** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mek-1" matches the protein description above**
2. **Verify the organism is correct:** Neurospora crassa (strain ATCC 24698 / 74-OR23-1A / CBS 708.71 / DSM 1257 / FGSC 987).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mek-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mek-1** (gene ID: mek-1, UniProt: Q7RYZ6) in NEUCR.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Neurospora crassa mek-1* (Q7RYZ6; NCU06419)

## Executive conclusion

The gene symbol **mek-1 is ambiguous across biology**, but the target specified here is unambiguously the *Neurospora crassa* locus **NCU06419**, not mammalian MEK1/MAP2K1, nematode *mek-1*, or the separate *N. crassa* gene **mek-2/NCU04612**. Primary literature explicitly maps *N. crassa mek-1* to NCU06419 and classifies its product as a MAP kinase kinase (MAP2K); the association with UniProt **Q7RYZ6** and strain 74-OR23-1A derives from the UniProt record supplied in the question. The same study separately maps *mek-2* to NCU04612, confirming that these are different fungal genes. (lichius2012importanceofmap pages 3-3, lichius2012importanceofmap pages 3-4)

MEK-1 is best annotated as the central kinase in the fungal cell-wall-integrity cascade:

**MIK-1 (MAP3K) → MEK-1 (MAP2K) → MAK-1 (MAPK).**

Its principal biological role is therefore intracellular signal relay controlling cell-wall integrity, hyphal adhesion and organization, extracellular-matrix-associated morphogenesis, and sexual fruitbody development. MAK-1 is the strongly predicted physiological substrate, but the retrieved literature did not demonstrate direct MEK-1→MAK-1 phosphorylation with purified proteins or report MEK-1 kinetic constants. Likewise, direct imaging or fractionation evidence for MEK-1 localization was not found. (lichius2012importanceofmap pages 9-10, jun2019dissectingthemechanism pages 28-30)

| Annotation claim | Conclusion | Evidence type | Confidence and limitation |
|---|---|---|---|
| Target identity | **mek-1 is NCU06419** in *Neurospora crassa* and encodes a MAP kinase kinase (MAP2K). It is distinct from *N. crassa* **mek-2/NCU04612** and similarly named MEK proteins in other organisms. Q7RYZ6 is the UniProt accession specified for this locus. (lichius2012importanceofmap pages 3-3, lichius2012importanceofmap pages 3-4) | Direct locus mapping in primary literature; accession mapping from the specified UniProt record | **High** for mek-1-to-NCU06419 identity and MAP2K classification. The retrieved paper does not independently state Q7RYZ6. |
| Pathway position | MEK-1 is the middle kinase of the fungal cell-wall-integrity cascade: **MIK-1 (MAP3K) → MEK-1 (MAP2K) → MAK-1 (MAPK)**. (lichius2012importanceofmap pages 9-10, jun2019dissectingthemechanism pages 28-30) | Genetic pathway assignment and conserved MAPK-cascade architecture | **High** for cascade membership and ordering. Direct pairwise phosphorylation was not demonstrated in the retrieved passages. |
| Catalytic reaction and substrate | Domain annotation predicts an ATP-dependent protein-serine/threonine kinase reaction: **ATP + protein-OH → ADP + phosphoprotein**. MAK-1 is the probable physiological substrate based on cascade position, but no purified-protein assay directly demonstrating MEK-1 phosphorylation of MAK-1 was found. (lichius2012importanceofmap pages 3-3, jun2019dissectingthemechanism pages 28-30) | Protein-kinase-domain inference plus pathway topology | **Moderate** for the generic kinase reaction and probable MAK-1 substrate. Direct evidence is absent for substrate specificity, kinetic constants, and a reconstituted MEK-1-to-MAK-1 reaction. |
| Cellular location | MEK-1 most plausibly acts intracellularly as a cytosolic signaling kinase, potentially in dynamically assembled CWI complexes. MAK-1 exhibits cytoplasmic and cell-cortex or fusion-site dynamics, but these observations do not establish MEK-1 localization. (jun2019dissectingthemechanism pages 28-30) | Inference from soluble kinase architecture and downstream-pathway imaging | **Low to moderate**. No direct MEK-1 fluorescent-localization, fractionation, or organelle-targeting evidence was found. |
| Loss-of-function phenotype | CWI-cascade deletion analysis associates Δmek-1 with altered cell walls, impaired cell-cell adhesion, elevated autolysis, and failure to organize tightly packed protoperithecia. Development arrests in loose, abortive hyphal aggregates that are subsequently reabsorbed. (lichius2012importanceofmap pages 9-10) | Targeted gene deletion and developmental microscopy | **High** for the reported developmental and CWI phenotypes, although some conclusions apply jointly to Δmik-1, Δmek-1, and Δmak-1 rather than uniquely to MEK-1. |
| Biological role | MEK-1-dependent CWI signaling supports extracellular-matrix deposition, hyphal aggregation and adhesion, enveloping-hypha organization, and sexual fruitbody morphogenesis. Its exact mechanistic contribution to vegetative cell fusion is less directly resolved. (lichius2012importanceofmap pages 16-17, lichius2012importanceofmap pages 1-2) | Comparative phenotyping of MAPK-cascade mutants | **Moderate to high** for morphogenesis; **limited** for a MEK-1-specific cell-fusion mechanism. |
| Systems-level phosphorylation context | A 2019 phosphoproteomic study measured responses after **2 minutes** of exposure to several plant-cell-wall-related sugars and detected broad, substrate-specific phosphorylation involving MAPK and other signaling systems. This supplies environmental-signaling context rather than proof of a specific MEK-1 substrate or function. (horta2019broadsubstratespecificphosphorylation pages 1-3, horta2019broadsubstratespecificphosphorylation pages 3-4, horta2019broadsubstratespecificphosphorylation pages 4-5) | LC-MS/MS phosphoproteomics using four experimental replicates, peptide filtering, and a 1% false-discovery rate | **Moderate** as systems-level context; not a direct biochemical or genetic test of the MEK-1 catalytic target. |
| Recent 2023–2024 evidence | No retrieved 2023–2024 primary study specifically characterized Q7RYZ6/NCU06419 MEK-1. Older targeted genetics and 2019 systems biology therefore remain the principal evidence base represented here. | Literature-search result | **Search-limited negative finding**, not proof that no such publication exists. Database indexing and terminology may omit relevant work. |


*Table: Evidence-confidence summary for *Neurospora crassa* Q7RYZ6/mek-1, separating experimentally supported pathway and deletion-phenotype claims from domain-based biochemical and localization inferences.*

## 1. Identity and domain verification

The targeted organism is *Neurospora crassa*, with the requested UniProt record referring specifically to strain ATCC 24698/74-OR23-1A and its equivalent collection designations. Experimental work used deletion alleles at **NCU06419.2**, including FGSC11318 and FGSC11319, and explicitly named the deleted gene *mek-1*. The study’s wild-type comparator included FGSC2489, a 74-OR23-1-derived strain. (lichius2012importanceofmap pages 2-3, lichius2012importanceofmap pages 3-4)

The supplied InterPro assignments—protein-kinase domain, ATP-binding site, serine/threonine-kinase active site, and MAP kinase kinase family—are internally consistent with the literature’s MAP2K classification. They support an intracellular, soluble protein kinase rather than a transporter, receptor, extracellular enzyme, or structural cell-wall protein. The symbol must not be confused with *N. crassa mek-2*, the MAP2K of a different MAPK cascade, or with same-symbol proteins from animals. (lichius2012importanceofmap pages 3-3)

## 2. Molecular and enzymatic function

As an EC 2.7.11.1 serine/threonine protein kinase, the predicted net reaction is:

**ATP + protein serine/threonine–OH → ADP + phosphorylated protein.**

MEK-1 occupies the middle tier of a three-kinase module, downstream of MIK-1 and upstream of MAK-1. On the basis of this pathway topology and conserved MAPK-cascade architecture, MAK-1 is the most probable direct substrate. The precise physiological function is thus not general phosphorylation of many unrelated proteins, but activation and propagation of CWI signaling through the terminal MAP kinase MAK-1. (jun2019dissectingthemechanism pages 28-30)

This substrate assignment should nevertheless be labeled **strong inference rather than direct biochemistry**. The retrieved sources did not report a reconstituted kinase assay, phosphorylation-site mapping on MAK-1 attributable specifically to MEK-1, ATP-binding constants, catalytic efficiency, or comparisons against alternative protein substrates. Consequently, broad statements that MEK-1 has demonstrated dual-specificity toward the canonical MAPK activation motif would exceed the protein-specific evidence recovered here.

## 3. Pathway and biological processes

### Cell-wall-integrity signaling

MEK-1 belongs to the *N. crassa* CWI pathway together with MIK-1 and MAK-1. MAPK modules in *N. crassa* are organized into three broadly conserved pathways corresponding to pheromone response, cell-wall integrity, and osmoregulation. The CWI module is associated with responses to cell-wall and related stresses and with morphogenetic control. (lichius2012importanceofmap pages 2-3, lichius2012importanceofmap pages 9-10, jun2019dissectingthemechanism pages 28-30)

Deletion analysis associates the MIK-1–MEK-1–MAK-1 module with altered cell-wall properties, defective cell–cell adhesion, and increased autolysis. These phenotypes explain why a signaling kinase can produce conspicuous structural defects: MEK-1 is not itself a wall component but regulates the cellular programs that build, remodel, and stabilize fungal tissues. (lichius2012importanceofmap pages 9-10)

### Sexual fruitbody morphogenesis

A targeted comparison of all nine conserved *N. crassa* MAPK-cascade components found that all three MAPK cascades are required for sexual development, but they arrest morphogenesis at different stages. This argues against a nonspecific sickness explanation and supports pathway-specific developmental functions. (lichius2012importanceofmap pages 16-17, lichius2012importanceofmap pages 1-2)

The Δ*mek-1* CWI-pathway phenotype is especially informative. Mutant hyphae can initiate and expand ascogonial coils, but fail to organize the tightly aggregated and adherent enveloping hyphae needed to construct normal protoperithecia. Development arrests as loosely coiled, abortive aggregates, which are later reabsorbed; elevated autolysis provides a plausible explanation for that disappearance. Δ*mek-1* colonies also initiate peripheral fruitbody formation earlier than wild type in centrally inoculated cultures. (lichius2012importanceofmap pages 9-10)

Collectively, the data place MEK-1-dependent signaling in extracellular-matrix deposition, hyphal adhesion, aggregation, and envelopment during formation of fertilizable female reproductive structures. These are pathway-regulated processes, not evidence that MEK-1 itself is secreted into the extracellular matrix. (lichius2012importanceofmap pages 16-17, lichius2012importanceofmap pages 1-2)

### Cell communication and fusion

CWI signaling is connected to fungal cell communication and fusion, and the downstream MAPK MAK-1 has been reported to move from a cytoplasmic distribution during tropic growth toward the cell cortex and fusion site after cell contact. SOFT/HAM-1 has also been reported to associate with MIK-1 and MEK-1, suggesting organization of the cascade in a signaling complex. However, these observations concern pathway context and downstream-protein behavior; they do not constitute direct localization evidence for Q7RYZ6 itself. (jun2019dissectingthemechanism pages 28-30)

The safest annotation is therefore that MEK-1 contributes to morphogenetic and cell-contact signaling through the CWI cascade, while a uniquely MEK-1-specific mechanistic requirement in vegetative fusion remains less firmly established than its role in protoperithecial organization.

## 4. Cellular localization

No signal peptide, transmembrane role, or extracellular catalytic function is suggested by the supplied kinase-domain architecture. MEK-1 most plausibly operates **inside the cell**, primarily in the cytosol and in transient signaling complexes that communicate with the cortex during CWI responses.

This is a mechanistic inference, not a directly observed localization. The retrieved evidence documents cytoplasmic and cortical/fusion-site dynamics for downstream MAK-1, but no MEK-1–GFP imaging, immunolocalization, or biochemical fractionation. Accordingly, assigning MEK-1 specifically to the nucleus, plasma membrane, Spitzenkörper, septa, or another organelle would be unsupported. (jun2019dissectingthemechanism pages 28-30)

## 5. Systems-level and quantitative evidence

A 2019 phosphoproteomic study examined early signaling after transfer of *N. crassa* to several plant-cell-wall-related carbon sources. Samples were collected after only **2 minutes** of exposure, with four experimental replicates; peptide identifications were filtered at **1% false-discovery rate**, required less than 5-ppm mass error, and were retained when detected in at least two of four replicates. The dataset is available as ProteomeXchange **PXD013964**. It revealed broad, substrate-specific phosphorylation involving MAPK, cAMP, G-protein, two-component, kinase, phosphatase, and transcription-factor systems. Publication date: **1 November 2019**; DOI/URL: https://doi.org/10.3389/fmicb.2019.02317. (horta2019broadsubstratespecificphosphorylation pages 1-3, horta2019broadsubstratespecificphosphorylation pages 3-4, horta2019broadsubstratespecificphosphorylation pages 4-5)

This study is useful evidence that fungal environmental adaptation includes extremely rapid phosphorylation remodeling and provides a resource for strain engineering and pathway-hypothesis generation. It does **not**, by itself, establish a direct MEK-1 substrate or prove that the observed sugar-specific responses are mediated by the MIK-1–MEK-1–MAK-1 module. (horta2019broadsubstratespecificphosphorylation pages 1-3, horta2019broadsubstratespecificphosphorylation pages 4-5)

The principal targeted developmental study was published **10 August 2012** and analyzed deletion strains generated by homologous recombination and validated in the Neurospora Genome Knock-Out Project; the investigators additionally checked target-locus replacement by PCR. DOI/URL: https://doi.org/10.1371/journal.pone.0042565. (lichius2012importanceofmap pages 1-2, lichius2012importanceofmap pages 2-3, lichius2012importanceofmap pages 3-4)

## 6. Recent research, applications, and expert assessment

No 2023–2024 primary publication specifically characterizing Q7RYZ6/NCU06419 MEK-1 was retrieved. Therefore, there is no defensible protein-specific “latest development” from those years to report, and substituting research on human MAP2K1, nematode MEK-1, or *N. crassa* MEK-2 would violate the identity constraint. The current annotation rests principally on targeted fungal genetics and microscopy, supplemented by conserved kinase-domain architecture and systems phosphoproteomics.

Current real-world relevance is primarily **research and biotechnology**, rather than a deployed clinical or industrial application. The pathway provides: (1) a model for fungal cell-wall-integrity signaling; (2) a genetic handle for studying multicellular fungal morphogenesis, adhesion, and fusion; and (3) a potential strain-engineering node for modifying growth, tissue integrity, secretion-associated physiology, or biomass responses. The 2019 authors explicitly framed early phosphorylation networks as potential guides to engineering filamentous fungi for lignocellulosic bioprocessing, although MEK-1 itself was not validated as an engineering target. (horta2019broadsubstratespecificphosphorylation pages 1-3, horta2019broadsubstratespecificphosphorylation pages 3-4, horta2019broadsubstratespecificphosphorylation pages 4-5)

From an expert annotation perspective, the evidence hierarchy is:

1. **High confidence:** identity as NCU06419; MAP2K classification; membership in the MIK-1–MEK-1–MAK-1 CWI cascade; requirement for normal protoperithecial organization, adhesion-associated morphogenesis, and resistance to autolytic collapse.
2. **Moderate confidence:** MAK-1 as the physiological kinase substrate and intracellular/cytosolic operation, because both follow strongly from conserved cascade organization but lack protein-specific biochemical or localization validation in the retrieved studies.
3. **Unresolved:** exact phosphorylation sites and substrate motif, catalytic kinetics, direct MEK-1 interactome, stimulus-dependent MEK-1 localization, and the magnitude of its specific contribution to vegetative cell fusion.

## Final functional annotation

**Q7RYZ6/MEK-1 (NCU06419) is an intracellular fungal MAP kinase kinase and the middle component of the MIK-1–MEK-1–MAK-1 cell-wall-integrity cascade. It is predicted to use ATP to phosphorylate and activate the downstream MAP kinase MAK-1 on regulatory serine/threonine residues, thereby relaying wall- and morphogenesis-associated signals. Genetic evidence shows that MEK-1-dependent signaling is required for normal cell-wall behavior, hyphal adhesion and organization, limitation of autolysis, and assembly of tightly structured protoperithecia. Direct substrate biochemistry and direct subcellular-localization measurements for Q7RYZ6 remain important evidence gaps.**

References

1. (lichius2012importanceofmap pages 3-3): Alexander Lichius, Kathryn M. Lord, Chris E. Jeffree, Radek Oborny, Patid Boonyarungsrit, and Nick D. Read. Importance of map kinases during protoperithecial morphogenesis in neurospora crassa. PLoS ONE, 7:e42565, Aug 2012. URL: https://doi.org/10.1371/journal.pone.0042565, doi:10.1371/journal.pone.0042565. This article has 51 citations and is from a peer-reviewed journal.

2. (lichius2012importanceofmap pages 3-4): Alexander Lichius, Kathryn M. Lord, Chris E. Jeffree, Radek Oborny, Patid Boonyarungsrit, and Nick D. Read. Importance of map kinases during protoperithecial morphogenesis in neurospora crassa. PLoS ONE, 7:e42565, Aug 2012. URL: https://doi.org/10.1371/journal.pone.0042565, doi:10.1371/journal.pone.0042565. This article has 51 citations and is from a peer-reviewed journal.

3. (lichius2012importanceofmap pages 9-10): Alexander Lichius, Kathryn M. Lord, Chris E. Jeffree, Radek Oborny, Patid Boonyarungsrit, and Nick D. Read. Importance of map kinases during protoperithecial morphogenesis in neurospora crassa. PLoS ONE, 7:e42565, Aug 2012. URL: https://doi.org/10.1371/journal.pone.0042565, doi:10.1371/journal.pone.0042565. This article has 51 citations and is from a peer-reviewed journal.

4. (jun2019dissectingthemechanism pages 28-30): D Jun. Dissecting the mechanism of cell fusion and secretion in neurospora crassa. Unknown journal, 2019.

5. (lichius2012importanceofmap pages 16-17): Alexander Lichius, Kathryn M. Lord, Chris E. Jeffree, Radek Oborny, Patid Boonyarungsrit, and Nick D. Read. Importance of map kinases during protoperithecial morphogenesis in neurospora crassa. PLoS ONE, 7:e42565, Aug 2012. URL: https://doi.org/10.1371/journal.pone.0042565, doi:10.1371/journal.pone.0042565. This article has 51 citations and is from a peer-reviewed journal.

6. (lichius2012importanceofmap pages 1-2): Alexander Lichius, Kathryn M. Lord, Chris E. Jeffree, Radek Oborny, Patid Boonyarungsrit, and Nick D. Read. Importance of map kinases during protoperithecial morphogenesis in neurospora crassa. PLoS ONE, 7:e42565, Aug 2012. URL: https://doi.org/10.1371/journal.pone.0042565, doi:10.1371/journal.pone.0042565. This article has 51 citations and is from a peer-reviewed journal.

7. (horta2019broadsubstratespecificphosphorylation pages 1-3): MAC Horta, N Thieme, and Y Gao. Broad substrate-specific phosphorylation events are associated with the initial stage. Unknown journal, 2019.

8. (horta2019broadsubstratespecificphosphorylation pages 3-4): MAC Horta, N Thieme, and Y Gao. Broad substrate-specific phosphorylation events are associated with the initial stage. Unknown journal, 2019.

9. (horta2019broadsubstratespecificphosphorylation pages 4-5): MAC Horta, N Thieme, and Y Gao. Broad substrate-specific phosphorylation events are associated with the initial stage. Unknown journal, 2019.

10. (lichius2012importanceofmap pages 2-3): Alexander Lichius, Kathryn M. Lord, Chris E. Jeffree, Radek Oborny, Patid Boonyarungsrit, and Nick D. Read. Importance of map kinases during protoperithecial morphogenesis in neurospora crassa. PLoS ONE, 7:e42565, Aug 2012. URL: https://doi.org/10.1371/journal.pone.0042565, doi:10.1371/journal.pone.0042565. This article has 51 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](mek-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. jun2019dissectingthemechanism pages 28-30
2. lichius2012importanceofmap pages 9-10
3. lichius2012importanceofmap pages 3-3
4. lichius2012importanceofmap pages 3-4
5. lichius2012importanceofmap pages 16-17
6. lichius2012importanceofmap pages 1-2
7. horta2019broadsubstratespecificphosphorylation pages 1-3
8. horta2019broadsubstratespecificphosphorylation pages 3-4
9. horta2019broadsubstratespecificphosphorylation pages 4-5
10. lichius2012importanceofmap pages 2-3
11. https://doi.org/10.3389/fmicb.2019.02317.
12. https://doi.org/10.1371/journal.pone.0042565.
13. https://doi.org/10.1371/journal.pone.0042565,