---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T20:34:53.296533'
end_time: '2026-10-09T20:45:03.219640'
duration_seconds: 609.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Tcs3
  gene_symbol: Tcs3
  uniprot_accession: Q9VV41
  protein_description: 'RecName: Full=Probable tRNA N6-adenosine threonylcarbamoyltransferase
    {ECO:0000255|HAMAP-Rule:MF_03180}; EC=2.3.1.234 {ECO:0000255|HAMAP-Rule:MF_03180};
    AltName: Full=N6-L-threonylcarbamoyladenine synthase; Short=t(6)A synthase; AltName:
    Full=t(6)A37 threonylcarbamoyladenosine biosynthesis protein Tcs3 {ECO:0000255|HAMAP-Rule:MF_03180};
    AltName: Full=tRNA threonylcarbamoyladenosine biosynthesis protein Tcs3 {ECO:0000255|HAMAP-Rule:MF_03180};'
  gene_info: Name=Tcs3 {ECO:0000312|FlyBase:FBgn0283681}; ORFNames=CG4933 {ECO:0000312|FlyBase:FBgn0283681};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the KAE1 / TsaD family. {ECO:0000255|HAMAP-
  protein_domains: ATPase_NBD. (IPR043129); Gcp-like_dom. (IPR000905); KAE1/TsaD.
    (IPR017861); Kae1_archaea_euk. (IPR034680); Peptidase_M22_CS. (IPR017860)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: Tcs3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: Tcs3-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000027 I have extracted Figure 3 panels B and
    C from page 5 of the document. Panel B shows the primer extension analysis for
    tRNA-Met[CAU]'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VV41
- **Protein Description:** RecName: Full=Probable tRNA N6-adenosine threonylcarbamoyltransferase {ECO:0000255|HAMAP-Rule:MF_03180}; EC=2.3.1.234 {ECO:0000255|HAMAP-Rule:MF_03180}; AltName: Full=N6-L-threonylcarbamoyladenine synthase; Short=t(6)A synthase; AltName: Full=t(6)A37 threonylcarbamoyladenosine biosynthesis protein Tcs3 {ECO:0000255|HAMAP-Rule:MF_03180}; AltName: Full=tRNA threonylcarbamoyladenosine biosynthesis protein Tcs3 {ECO:0000255|HAMAP-Rule:MF_03180};
- **Gene Information:** Name=Tcs3 {ECO:0000312|FlyBase:FBgn0283681}; ORFNames=CG4933 {ECO:0000312|FlyBase:FBgn0283681};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the KAE1 / TsaD family. {ECO:0000255|HAMAP-
- **Key Domains:** ATPase_NBD. (IPR043129); Gcp-like_dom. (IPR000905); KAE1/TsaD. (IPR017861); Kae1_archaea_euk. (IPR034680); Peptidase_M22_CS. (IPR017860)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Tcs3" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Tcs3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Tcs3** (gene ID: Tcs3, UniProt: Q9VV41) in DROME.

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
- **UniProt Accession:** Q9VV41
- **Protein Description:** RecName: Full=Probable tRNA N6-adenosine threonylcarbamoyltransferase {ECO:0000255|HAMAP-Rule:MF_03180}; EC=2.3.1.234 {ECO:0000255|HAMAP-Rule:MF_03180}; AltName: Full=N6-L-threonylcarbamoyladenine synthase; Short=t(6)A synthase; AltName: Full=t(6)A37 threonylcarbamoyladenosine biosynthesis protein Tcs3 {ECO:0000255|HAMAP-Rule:MF_03180}; AltName: Full=tRNA threonylcarbamoyladenosine biosynthesis protein Tcs3 {ECO:0000255|HAMAP-Rule:MF_03180};
- **Gene Information:** Name=Tcs3 {ECO:0000312|FlyBase:FBgn0283681}; ORFNames=CG4933 {ECO:0000312|FlyBase:FBgn0283681};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the KAE1 / TsaD family. {ECO:0000255|HAMAP-
- **Key Domains:** ATPase_NBD. (IPR043129); Gcp-like_dom. (IPR000905); KAE1/TsaD. (IPR017861); Kae1_archaea_euk. (IPR034680); Peptidase_M22_CS. (IPR017860)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Tcs3" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Tcs3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Tcs3** (gene ID: Tcs3, UniProt: Q9VV41) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation of *Drosophila melanogaster* Tcs3

## Identity and evidence standard

The target is **Tcs3, also called Kae1, encoded by *D. melanogaster* CG4933**. UniProt accession **Q9VV41** is the identifier supplied in the question; the retrieved experimental papers identify the protein by CG4933/Tcs3/Kae1 rather than printing that accession. Rojas-Benítez and colleagues explicitly proposed the name *tcs3* for CG4933 and identified its predicted 347-amino-acid product as a Kae1/YgjD-family protein. Independently, Lin and colleagues mapped multiple fly *kae1* mutant alleles to CG4933 and rescued their phenotypes with CG4933 transgenes. These observations support the supplied KAE1/TsaD-family assignment, rather than a same-named protein in another organism. The related mitochondrial protein Qri7, annotated as CG14231 in the fly study, is **not** Tcs3. (rojasbenitez2015thelevelsof pages 2-3, rojasbenitez2015thelevelsof pages 3-5, lin2015anextensiveallelic pages 2-3, lin2015anextensiveallelic pages 5-7)

## Primary molecular function and substrate specificity

**Tcs3 is the catalytic Kae1-family component of the tRNA threonylcarbamoyladenosine (t⁶A) biosynthesis pathway.** t⁶A is an N⁶-threonylcarbamoyl modification of adenosine **37**, immediately beside the anticodon, in most tRNAs that decode codons beginning with A; this class includes initiator tRNA^Met. The modification helps stabilize productive codon–anticodon interactions. In the conserved two-step pathway, Sua5/YRDC first makes **L-threonylcarbamoyladenylate (TC-AMP)** from L-threonine, bicarbonate/CO₂ and ATP. Kae1 then transfers the threonylcarbamoyl group from TC-AMP to the **N⁶ atom of tRNA A37**, forming t⁶A. Thus the substrate is an appropriate **tRNA bearing A37**, together with TC-AMP—not a free adenine base. This precise transfer chemistry is established for homologous systems and is the strong mechanistic inference for fly Tcs3; the retrieved fly studies did **not** purify Tcs3 and directly measure its catalytic turnover or a complete fly-specific substrate range. The user-supplied UniProt record assigns EC **2.3.1.234**. (lin2015anextensiveallelic pages 1-2, zheng2024molecularbasisof pages 1-2, wang2022commonalityanddiversity pages 1-2)

Fly experiments establish function on specific tRNAs. A modification-sensitive hybridization assay found less t⁶A-associated signal on **initiator tRNA^Met** in *tcs3* mutants. An independent primer-extension study found reduced A37 modification on **tRNA-Met[CAU] and tRNA-Ile[AAU]** in strong *kae1* mutants, with restoration by a CG4933 genomic transgene. These results identify experimentally supported substrates, but do not establish that every fly ANN-decoding tRNA is modified with equal efficiency. Comparative eukaryotic assays implicate anticodon-loop and D-stem features in substrate recognition; the quantitative preferences of purified **fly** Tcs3 remain unmeasured in the retrieved studies. (rojasbenitez2015thelevelsof pages 3-5, lin2015anextensiveallelic pages 5-7, lin2015anextensiveallelic media c58bedc0, wang2022commonalityanddiversity pages 1-2)

## Pathway, partners and site of action

Tcs3 acts in the **KEOPS/EKC tRNA-modification machinery**, rather than as a stand-alone mitochondrial Qri7 enzyme. Fly studies identify the conserved components Kae1/Tcs3 (**CG4933**), Bud32/Prpk (**CG10673**) and Pcc1 (**CG42498**); a 2013 fly analysis reported no conserved fly Cgi121 ortholog. Fly Kae1, Bud32 and the upstream Sua5 factor each complement corresponding yeast pathway mutants; combining fly Kae1 with Bud32 gave particularly strong recovery of yeast growth and t⁶A-modified tRNA. These findings support conserved pathway participation, although complementation does not itself prove that every proposed partner physically associates with Tcs3 inside fly cells. The KEOPS name retains an historical “endopeptidase” reference; **tRNA modification, not protein cleavage, is the experimentally supported primary function here**. (rojasbenitez2013thedrosophilaekckeopscomplex pages 2-3, lin2015anextensiveallelic pages 5-7, lin2015anextensiveallelic pages 1-2)

The **best-supported functional compartment is the cytosolic/cytoplasmic tRNA-modification pathway**, because the fly experiments implicate KEOPS and initiator and elongator tRNAs used for cytoplasmic translation. However, the retrieved fly studies do **not** directly image endogenous Tcs3 or establish its precise cytoplasm-versus-nucleus distribution. The mitochondrial t⁶A pathway should not be assigned to Tcs3 on this evidence: CG14231/Qri7 is the distinct proposed mitochondrial paralog. Lin and colleagues suggested that this pathway *might* account for t⁶A remaining in strong Tcs3/Kae1 mutants, but did not experimentally establish that explanation. (rojasbenitez2015thelevelsof pages 3-5, lin2015anextensiveallelic pages 5-7, thiaville2014diversityofthe pages 3-5, wang2022commonalityanddiversity pages 1-2)

## Strength of the fly evidence and physiological interpretation

Two complementary 2015 studies make the annotation more than a sequence-based prediction. Fly CG4933 mutant phenotypes were rescued by gene expression or genomic transgenes; modification-sensitive assays showed reduced t⁶A; and fly Kae1 restored pathway function in yeast. In Lin and colleagues’ **LC–MS/MS measurements of total tRNA**, a weak hemizygous allele had approximately **10% less t⁶A**, whereas strong/null hemizygous conditions had approximately **40% less** than controls. The genomic transgene restored the signal. The strong-mutant decrease did not progress further in long-lived 12- or 18-day larvae, so residual bulk t⁶A cannot simply be assumed to reflect progressively disappearing maternal stores. Figure 3B–C directly presents the tRNA-specific primer-extension and bulk mass-spectrometry results. (rojasbenitez2015thelevelsof pages 3-5, lin2015anextensiveallelic pages 5-7, lin2015anextensiveallelic media c58bedc0)

The biochemical role offers a focused explanation for growth effects: impaired modification of translation-relevant tRNAs limits protein synthesis. *tcs3* mutants had reduced polysome fractions and reduced S6K phosphorylation, while Tcs3 overexpression increased modified initiator tRNA, S6K phosphorylation and tissue growth. Importantly, activating TORC1 through Rheb **did not rescue** growth of *tcs3* mutants despite increasing TORC1 activity. TOR changes therefore should not be described as Tcs3’s primary enzymatic pathway or as a sufficient explanation for its growth phenotype; defective tRNA-dependent translation remains central. An independent allelic study found proliferating imaginal tissues especially sensitive to *kae1* loss, whereas some nonproliferating tissues were less affected. These are consequences of the t⁶A pathway, not evidence of a separate primary catalytic activity. (rojasbenitez2015thelevelsof pages 5-6, lin2015anextensiveallelic pages 10-11, lin2015anextensiveallelic pages 1-2)

| Topic | Direct evidence in *D. melanogaster* | Conserved-mechanism inference / limitation | Evidence grade |
|---|---|---|---|
| Identity and family | CG4933 was identified as the fly ortholog of yeast Kae1/Tcs3; it encodes a predicted 347-aa Kae1/YgjD-family protein. Independent CG4933 mutations, non-complementation, and genomic/cDNA rescue establish the locus–phenotype assignment (rojasbenitez2015thelevelsof pages 2-3, lin2015anextensiveallelic pages 3-5, lin2015anextensiveallelic pages 2-3, rojasbenitez2015thelevelsof pages 3-5). | UniProt accession **Q9VV41** is supplied by the target record but is not stated in the cited papers. KAE1/TsaD-family and ATPase/Gcp-like annotations are consistent with conserved homologs (lin2015anextensiveallelic pages 1-2, zheng2024molecularbasisof pages 1-2). | **High** for CG4933 = Tcs3/Kae1 and family; **database-supported** for the accession/domain mapping. |
| Biochemical reaction and substrates | Fly Tcs3/Kae1 is required for normal t6A at A37: loss reduces modification of initiator tRNA-Met and elongator tRNA-Ile[AAU]; fly Kae1 restores t6A in yeast mutants. These experiments establish pathway participation but are not a purified-fly-enzyme reaction assay (lin2015anextensiveallelic pages 5-7, rojasbenitez2015thelevelsof pages 3-5). | Conserved Kae1 catalysis transfers the threonylcarbamoyl group from Sua5-generated TC-AMP to the N6 atom of A37 in ANN-decoding tRNAs. This exact chemistry is established with homologous systems and inferred for fly Tcs3 (zheng2024molecularbasisof pages 1-2). | **High** for fly t6A-pathway function and tested tRNAs; **strong evolutionary/biochemical inference** for exact reaction chemistry. |
| Genetic and quantitative fly evidence | CG4933 transgenes rescue lethality, melanotic masses, and t6A loss. LC–MS/MS found about **10%** lower total t6A in a weak allele and about **40%** lower levels in strong/null hemizygotes; primer extension independently showed reduced A37 modification (lin2015anextensiveallelic pages 5-7, lin2015anextensiveallelic media c58bedc0). Tcs3 loss reduces polysomes and growth, whereas overexpression increases t6A, S6K phosphorylation, cell size, and tissue growth (rojasbenitez2015thelevelsof pages 3-5, rojasbenitez2015thelevelsof pages 5-6). | TOR changes track t6A/translation status, but failure of Rheb-driven TORC1 activation to rescue growth argues that defective translation is not merely downstream of reduced TOR activity (rojasbenitez2015thelevelsof pages 5-6). | **High**, based on allelic series, rescue, two biochemical assays, and physiological perturbations. |
| Cellular location and mitochondrial distinction | No Tcs3-protein localization experiment was located. Its modification of cytoplasmic initiator and elongator tRNAs and KEOPS role support a cytosolic/nucleocytosolic assignment, but this remains inferred. CG14231/Qri7 is a distinct predicted mitochondrial Kae1-family paralog and may contribute residual t6A in Tcs3-null larvae (lin2015anextensiveallelic pages 5-7, lin2015anextensiveallelic pages 2-3). | Mitochondria generally use Qri7/OSGEPL1 rather than cytosolic KEOPS Kae1; residual fly t6A was proposed, not experimentally proven, to derive from CG14231 (thiaville2014diversityofthe pages 3-5, lin2015anextensiveallelic pages 5-7). | **Moderate** for cytosolic assignment; **high** for paralog distinction; **hypothesis** for Qri7 causing residual t6A. |
| KEOPS architecture and 2024 mechanism | Fly studies identify Kae1/CG4933, Bud32/Prpk/CG10673, and Pcc1/CG42498 as conserved KEOPS components; no fly Cgi121 ortholog was identified in the cited analysis. Fly Kae1 plus Bud32 gives especially strong yeast complementation (rojasbenitez2013thedrosophilaekckeopscomplex pages 2-3, lin2015anextensiveallelic pages 5-7). | 2024 cryo-EM/biochemistry in other eukaryotes shows tRNA engagement across KEOPS, CCA-tail capture by Cgi121 where present, A37 exposure to Kae1, and tRNA-stimulated Bud32 ATP hydrolysis coupled to catalysis. These mechanistic details are not directly demonstrated for fly Tcs3 (zheng2024molecularbasisof pages 14-15, chuquimarca2024structuresofkeops pages 11-11, zheng2024molecularbasisof pages 14-14). | **High** for the conserved general mechanism; **moderate inference** when transferred specifically to the reduced fly complex. |


*Table: This table separates direct Drosophila evidence for CG4933/Tcs3/Kae1 from mechanistic conclusions inferred from homologous KEOPS systems. It also highlights unresolved accession, localization, and mitochondrial-residual-t6A questions.*

## Developments in 2023–2024 and research use

Recent work improves the **conserved mechanistic model**, not the direct experimental annotation of fly Tcs3. Zheng and colleagues’ *Arabidopsis* KEOPS structural and biochemical study, accepted **1 March 2024**, showed that KAE1-centered catalysis is supported by assembly with other KEOPS subunits, tRNA binding and Bud32 ATP hydrolysis; its measured binding affinity for one tested tRNA, tRNA-Arg[CCU], was approximately **18 µM**. A separate **December 2024** KEOPS–tRNA cryo-EM study identified extended tRNA contacts and a conformational arrangement that can expose A37 to Kae1. These results clarify plausible roles for conserved Tcs3 interfaces, but the plant and other eukaryotic complexes must **not** be assumed to have exactly the fly subunit composition or measured substrate affinities. A **2022** comparative study similarly showed species-dependent substrate-recognition rules; its mention of fly initiator tRNA sequence is comparative, not a purified fly-Tcs3 assay. (zheng2024molecularbasisof pages 14-15, chuquimarca2024structuresofkeops pages 11-11, zheng2024molecularbasisof pages 14-14, zheng2024molecularbasisof pages 1-1, wang2022commonalityanddiversity pages 5-7)

The established real-world use of fly *tcs3* is as a **genetic model** for testing how tRNA modification affects translation, growth and development: allelic series, genomic rescue, tRNA-specific assays and LC–MS/MS permit the causal pathway to be interrogated. The retrieved 2023–2024 studies did not supply a new direct fly-Tcs3 reaction assay, definitive cellular imaging or a clinical implementation. Accordingly, the strongest current annotation remains **KEOPS-associated tRNA A37 N⁶-threonylcarbamoyltransferase**, experimentally required for t⁶A formation in flies, with its exact reaction and likely cytosolic site supported additionally by conserved biochemistry and pathway context. (rojasbenitez2015thelevelsof pages 3-5, lin2015anextensiveallelic pages 5-7, zheng2024molecularbasisof pages 1-2, chuquimarca2024structuresofkeops pages 11-11)

### Principal sources

- Rojas-Benítez D *et al.* **24 July 2015**. “The levels of a universally conserved tRNA modification regulate cell growth.” *Journal of Biological Chemistry* **290**:18699–18707. https://doi.org/10.1074/jbc.M115.665406. (rojasbenitez2015thelevelsof pages 2-3, rojasbenitez2015thelevelsof pages 3-5, rojasbenitez2015thelevelsof pages 5-6)
- Lin C-J *et al.* **2015**. “An extensive allelic series of *Drosophila kae1* mutants reveals diverse and tissue-specific requirements for t6A biogenesis.” *RNA* **21**:2103–2118. https://doi.org/10.1261/rna.053934.115. (lin2015anextensiveallelic pages 1-2, lin2015anextensiveallelic pages 5-7, lin2015anextensiveallelic media c58bedc0)
- Thiaville PC *et al.* **December 2014**. “Diversity of the biosynthesis pathway for threonylcarbamoyladenosine (t⁶A), a universal modification of tRNA.” *RNA Biology* **11**:1529–1539. https://doi.org/10.4161/15476286.2014.992277. (thiaville2014diversityofthe pages 3-5)
- Zheng X *et al.* **2024**. “Molecular basis of *A. thaliana* KEOPS complex in biosynthesizing tRNA t6A.” *Nucleic Acids Research* **52**:4523–4540. https://doi.org/10.1093/nar/gkae179. (zheng2024molecularbasisof pages 1-2, zheng2024molecularbasisof pages 14-15)
- Ona Chuquimarca SM *et al.* **December 2024**. “Structures of KEOPS bound to tRNA reveal functional roles of the kinase Bud32.” *Nature Communications* **15**. https://doi.org/10.1038/s41467-024-54787-w. (chuquimarca2024structuresofkeops pages 11-11)

References

1. (rojasbenitez2015thelevelsof pages 2-3): Diego Rojas-Benitez, Patrick C. Thiaville, Valérie de Crécy-Lagard, and Alvaro Glavic. The levels of a universally conserved trna modification regulate cell growth. Journal of Biological Chemistry, 290:18699-18707, Jul 2015. URL: https://doi.org/10.1074/jbc.m115.665406, doi:10.1074/jbc.m115.665406. This article has 51 citations and is from a domain leading peer-reviewed journal.

2. (rojasbenitez2015thelevelsof pages 3-5): Diego Rojas-Benitez, Patrick C. Thiaville, Valérie de Crécy-Lagard, and Alvaro Glavic. The levels of a universally conserved trna modification regulate cell growth. Journal of Biological Chemistry, 290:18699-18707, Jul 2015. URL: https://doi.org/10.1074/jbc.m115.665406, doi:10.1074/jbc.m115.665406. This article has 51 citations and is from a domain leading peer-reviewed journal.

3. (lin2015anextensiveallelic pages 2-3): Ching-Jung Lin, Peter Smibert, Xiaoyu Zhao, Jennifer F. Hu, Johnny Ramroop, Stefanie M. Kellner, Matthew A. Benton, Shubha Govind, Peter C. Dedon, Rolf Sternglanz, and Eric C. Lai. An extensive allelic series of drosophila kae1 mutants reveals diverse and tissue-specific requirements for t6a biogenesis. RNA, 21:2103-2118, Oct 2015. URL: https://doi.org/10.1261/rna.053934.115, doi:10.1261/rna.053934.115. This article has 31 citations and is from a domain leading peer-reviewed journal.

4. (lin2015anextensiveallelic pages 5-7): Ching-Jung Lin, Peter Smibert, Xiaoyu Zhao, Jennifer F. Hu, Johnny Ramroop, Stefanie M. Kellner, Matthew A. Benton, Shubha Govind, Peter C. Dedon, Rolf Sternglanz, and Eric C. Lai. An extensive allelic series of drosophila kae1 mutants reveals diverse and tissue-specific requirements for t6a biogenesis. RNA, 21:2103-2118, Oct 2015. URL: https://doi.org/10.1261/rna.053934.115, doi:10.1261/rna.053934.115. This article has 31 citations and is from a domain leading peer-reviewed journal.

5. (lin2015anextensiveallelic pages 1-2): Ching-Jung Lin, Peter Smibert, Xiaoyu Zhao, Jennifer F. Hu, Johnny Ramroop, Stefanie M. Kellner, Matthew A. Benton, Shubha Govind, Peter C. Dedon, Rolf Sternglanz, and Eric C. Lai. An extensive allelic series of drosophila kae1 mutants reveals diverse and tissue-specific requirements for t6a biogenesis. RNA, 21:2103-2118, Oct 2015. URL: https://doi.org/10.1261/rna.053934.115, doi:10.1261/rna.053934.115. This article has 31 citations and is from a domain leading peer-reviewed journal.

6. (zheng2024molecularbasisof pages 1-2): Xinxing Zheng, Chenchen Su, Lei Duan, Mengqi Jin, Yongtao Sun, Li Zhu, and Wenhua Zhang. Molecular basis of a. thaliana keops complex in biosynthesizing trna t6a. Nucleic Acids Research, 52:4523-4540, Mar 2024. URL: https://doi.org/10.1093/nar/gkae179, doi:10.1093/nar/gkae179. This article has 10 citations and is from a highest quality peer-reviewed journal.

7. (wang2022commonalityanddiversity pages 1-2): Jin-Tao Wang, Jing-Bo Zhou, Xue-Ling Mao, Li Zhou, Meirong Chen, Wenhua Zhang, En-Duo Wang, and Xiao-Long Zhou. Commonality and diversity in trna substrate recognition in t6a biogenesis by eukaryotic keopss. Nucleic Acids Research, 50:2223-2239, Feb 2022. URL: https://doi.org/10.1093/nar/gkac056, doi:10.1093/nar/gkac056. This article has 41 citations and is from a highest quality peer-reviewed journal.

8. (lin2015anextensiveallelic media c58bedc0): Ching-Jung Lin, Peter Smibert, Xiaoyu Zhao, Jennifer F. Hu, Johnny Ramroop, Stefanie M. Kellner, Matthew A. Benton, Shubha Govind, Peter C. Dedon, Rolf Sternglanz, and Eric C. Lai. An extensive allelic series of drosophila kae1 mutants reveals diverse and tissue-specific requirements for t6a biogenesis. RNA, 21:2103-2118, Oct 2015. URL: https://doi.org/10.1261/rna.053934.115, doi:10.1261/rna.053934.115. This article has 31 citations and is from a domain leading peer-reviewed journal.

9. (rojasbenitez2013thedrosophilaekckeopscomplex pages 2-3): Diego Rojas-Benítez, Consuelo Ibar, and Álvaro Glavic. The<i>drosophila</i>ekc/keops complex. Fly, 7:168-172, Jul 2013. URL: https://doi.org/10.4161/fly.25227, doi:10.4161/fly.25227. This article has 14 citations and is from a peer-reviewed journal.

10. (thiaville2014diversityofthe pages 3-5): Patrick C Thiaville, Dirk Iwata-Reuyl, and Valérie de Crécy-Lagard. Diversity of the biosynthesis pathway for threonylcarbamoyladenosine (t<sup>6</sup>a), a universal modification of trna. RNA Biology, 11:1529-1539, Dec 2014. URL: https://doi.org/10.4161/15476286.2014.992277, doi:10.4161/15476286.2014.992277. This article has 121 citations and is from a peer-reviewed journal.

11. (rojasbenitez2015thelevelsof pages 5-6): Diego Rojas-Benitez, Patrick C. Thiaville, Valérie de Crécy-Lagard, and Alvaro Glavic. The levels of a universally conserved trna modification regulate cell growth. Journal of Biological Chemistry, 290:18699-18707, Jul 2015. URL: https://doi.org/10.1074/jbc.m115.665406, doi:10.1074/jbc.m115.665406. This article has 51 citations and is from a domain leading peer-reviewed journal.

12. (lin2015anextensiveallelic pages 10-11): Ching-Jung Lin, Peter Smibert, Xiaoyu Zhao, Jennifer F. Hu, Johnny Ramroop, Stefanie M. Kellner, Matthew A. Benton, Shubha Govind, Peter C. Dedon, Rolf Sternglanz, and Eric C. Lai. An extensive allelic series of drosophila kae1 mutants reveals diverse and tissue-specific requirements for t6a biogenesis. RNA, 21:2103-2118, Oct 2015. URL: https://doi.org/10.1261/rna.053934.115, doi:10.1261/rna.053934.115. This article has 31 citations and is from a domain leading peer-reviewed journal.

13. (lin2015anextensiveallelic pages 3-5): Ching-Jung Lin, Peter Smibert, Xiaoyu Zhao, Jennifer F. Hu, Johnny Ramroop, Stefanie M. Kellner, Matthew A. Benton, Shubha Govind, Peter C. Dedon, Rolf Sternglanz, and Eric C. Lai. An extensive allelic series of drosophila kae1 mutants reveals diverse and tissue-specific requirements for t6a biogenesis. RNA, 21:2103-2118, Oct 2015. URL: https://doi.org/10.1261/rna.053934.115, doi:10.1261/rna.053934.115. This article has 31 citations and is from a domain leading peer-reviewed journal.

14. (zheng2024molecularbasisof pages 14-15): Xinxing Zheng, Chenchen Su, Lei Duan, Mengqi Jin, Yongtao Sun, Li Zhu, and Wenhua Zhang. Molecular basis of a. thaliana keops complex in biosynthesizing trna t6a. Nucleic Acids Research, 52:4523-4540, Mar 2024. URL: https://doi.org/10.1093/nar/gkae179, doi:10.1093/nar/gkae179. This article has 10 citations and is from a highest quality peer-reviewed journal.

15. (chuquimarca2024structuresofkeops pages 11-11): Samara Mishelle Ona Chuquimarca, Jonah Beenstock, Salima Daou, Jennifer Porat, Alexander F. A. Keszei, Jay Z. Yin, Tobias Beschauner, Mark A. Bayfield, Mohammad T. Mazhab-Jafari, and Frank Sicheri. Structures of keops bound to trna reveal functional roles of the kinase bud32. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-54787-w, doi:10.1038/s41467-024-54787-w. This article has 8 citations and is from a highest quality peer-reviewed journal.

16. (zheng2024molecularbasisof pages 14-14): Xinxing Zheng, Chenchen Su, Lei Duan, Mengqi Jin, Yongtao Sun, Li Zhu, and Wenhua Zhang. Molecular basis of a. thaliana keops complex in biosynthesizing trna t6a. Nucleic Acids Research, 52:4523-4540, Mar 2024. URL: https://doi.org/10.1093/nar/gkae179, doi:10.1093/nar/gkae179. This article has 10 citations and is from a highest quality peer-reviewed journal.

17. (zheng2024molecularbasisof pages 1-1): Xinxing Zheng, Chenchen Su, Lei Duan, Mengqi Jin, Yongtao Sun, Li Zhu, and Wenhua Zhang. Molecular basis of a. thaliana keops complex in biosynthesizing trna t6a. Nucleic Acids Research, 52:4523-4540, Mar 2024. URL: https://doi.org/10.1093/nar/gkae179, doi:10.1093/nar/gkae179. This article has 10 citations and is from a highest quality peer-reviewed journal.

18. (wang2022commonalityanddiversity pages 5-7): Jin-Tao Wang, Jing-Bo Zhou, Xue-Ling Mao, Li Zhou, Meirong Chen, Wenhua Zhang, En-Duo Wang, and Xiao-Long Zhou. Commonality and diversity in trna substrate recognition in t6a biogenesis by eukaryotic keopss. Nucleic Acids Research, 50:2223-2239, Feb 2022. URL: https://doi.org/10.1093/nar/gkac056, doi:10.1093/nar/gkac056. This article has 41 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Tcs3-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000027 I have extracted Figure 3 panels B and C from page 5 of the document. Panel B shows the primer extension analysis for tRNA-Met[CAU]](Tcs3-deep-research-falcon_artifacts/image-1.png)

## Citations

1. zheng2024molecularbasisof pages 1-2
2. rojasbenitez2015thelevelsof pages 5-6
3. thiaville2014diversityofthe pages 3-5
4. chuquimarca2024structuresofkeops pages 11-11
5. rojasbenitez2015thelevelsof pages 2-3
6. rojasbenitez2015thelevelsof pages 3-5
7. lin2015anextensiveallelic pages 2-3
8. lin2015anextensiveallelic pages 5-7
9. lin2015anextensiveallelic pages 1-2
10. wang2022commonalityanddiversity pages 1-2
11. rojasbenitez2013thedrosophilaekckeopscomplex pages 2-3
12. lin2015anextensiveallelic pages 10-11
13. lin2015anextensiveallelic pages 3-5
14. zheng2024molecularbasisof pages 14-15
15. zheng2024molecularbasisof pages 14-14
16. zheng2024molecularbasisof pages 1-1
17. wang2022commonalityanddiversity pages 5-7
18. CAU
19. AAU
20. CCU
21. https://doi.org/10.1074/jbc.M115.665406.
22. https://doi.org/10.1261/rna.053934.115.
23. https://doi.org/10.4161/15476286.2014.992277.
24. https://doi.org/10.1093/nar/gkae179.
25. https://doi.org/10.1038/s41467-024-54787-w.
26. https://doi.org/10.1074/jbc.m115.665406,
27. https://doi.org/10.1261/rna.053934.115,
28. https://doi.org/10.1093/nar/gkae179,
29. https://doi.org/10.1093/nar/gkac056,
30. https://doi.org/10.4161/fly.25227,
31. https://doi.org/10.4161/15476286.2014.992277,
32. https://doi.org/10.1038/s41467-024-54787-w,