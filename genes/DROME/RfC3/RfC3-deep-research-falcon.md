---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T19:03:34.640878'
end_time: '2026-10-09T19:16:53.390849'
duration_seconds: 798.75
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: RfC3
  gene_symbol: RfC3
  uniprot_accession: Q9VKW3
  protein_description: 'RecName: Full=Activator 1 subunit 5 {ECO:0000256|ARBA:ARBA00080380};'
  gene_info: Name=RfC3 {ECO:0000313|EMBL:AAF52944.2, ECO:0000313|FlyBase:FBgn0032244};
    Synonyms=Dmel\CG5313 {ECO:0000313|EMBL:AAF52944.2}, DmRFC3 {ECO:0000313|EMBL:AAF52944.2},
    DRFC {ECO:0000313|EMBL:AAF52944.2}, Rfc3 {ECO:0000313|EMBL:AAF52944.2}, rfc3 {ECO:0000313|EMBL:AAF52944.2};
    ORFNames=CG5313 {ECO:0000313|EMBL:AAF52944.2, ECO:0000313|FlyBase:FBgn0032244},
    Dmel_CG5313 {ECO:0000313|EMBL:AAF52944.2};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the activator 1 small subunits family.
  protein_domains: AAA+_ATPase. (IPR003593); ATPase_AAA_core. (IPR003959); DNA_pol3_clamp-load_cplx_C.
    (IPR008921); DNA_Rep/Repair_Clamp_Loader. (IPR050238); P-loop_NTPase. (IPR027417)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: RfC3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: RfC3-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000015 Table 2, located on page 5, lists the
    phenotypes of various knockdowns using the SD-Gal4 driver. For the specific responder
    ''Rfc3 I'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9VKW3
- **Protein Description:** RecName: Full=Activator 1 subunit 5 {ECO:0000256|ARBA:ARBA00080380};
- **Gene Information:** Name=RfC3 {ECO:0000313|EMBL:AAF52944.2, ECO:0000313|FlyBase:FBgn0032244}; Synonyms=Dmel\CG5313 {ECO:0000313|EMBL:AAF52944.2}, DmRFC3 {ECO:0000313|EMBL:AAF52944.2}, DRFC {ECO:0000313|EMBL:AAF52944.2}, Rfc3 {ECO:0000313|EMBL:AAF52944.2}, rfc3 {ECO:0000313|EMBL:AAF52944.2}; ORFNames=CG5313 {ECO:0000313|EMBL:AAF52944.2, ECO:0000313|FlyBase:FBgn0032244}, Dmel_CG5313 {ECO:0000313|EMBL:AAF52944.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the activator 1 small subunits family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ATPase_AAA_core. (IPR003959); DNA_pol3_clamp-load_cplx_C. (IPR008921); DNA_Rep/Repair_Clamp_Loader. (IPR050238); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RfC3" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RfC3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RfC3** (gene ID: RfC3, UniProt: Q9VKW3) in DROME.

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
- **UniProt Accession:** Q9VKW3
- **Protein Description:** RecName: Full=Activator 1 subunit 5 {ECO:0000256|ARBA:ARBA00080380};
- **Gene Information:** Name=RfC3 {ECO:0000313|EMBL:AAF52944.2, ECO:0000313|FlyBase:FBgn0032244}; Synonyms=Dmel\CG5313 {ECO:0000313|EMBL:AAF52944.2}, DmRFC3 {ECO:0000313|EMBL:AAF52944.2}, DRFC {ECO:0000313|EMBL:AAF52944.2}, Rfc3 {ECO:0000313|EMBL:AAF52944.2}, rfc3 {ECO:0000313|EMBL:AAF52944.2}; ORFNames=CG5313 {ECO:0000313|EMBL:AAF52944.2, ECO:0000313|FlyBase:FBgn0032244}, Dmel_CG5313 {ECO:0000313|EMBL:AAF52944.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the activator 1 small subunits family.
- **Key Domains:** AAA+_ATPase. (IPR003593); ATPase_AAA_core. (IPR003959); DNA_pol3_clamp-load_cplx_C. (IPR008921); DNA_Rep/Repair_Clamp_Loader. (IPR050238); P-loop_NTPase. (IPR027417)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RfC3" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RfC3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RfC3** (gene ID: RfC3, UniProt: Q9VKW3) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation of *Drosophila melanogaster* RfC3

## Identity and scope

The target is **RfC3/CG5313 (FlyBase FBgn0032244; UniProt [Q9VKW3](https://www.uniprot.org/uniprotkb/Q9VKW3/entry))**, a fruit-fly protein described in the supplied UniProt record as an activator 1 small subunit with AAA+ ATPase and DNA-clamp-loader domains. A fly-specific study explicitly identifies Rfc3 as a replication factor C (RFC) subunit and perturbs it in vivo. Thus the symbol is sufficiently identifiable for a functional annotation, although **literature directly characterizing this particular fly subunit is limited**. Fly *Rfc1* and *Rfc4*, and genes called *RFC3* in other organisms, must not be treated as experimental studies of Q9VKW3. (kohzaki2018thefunctionof pages 1-2, kohzaki2018thefunctionof pages 2-5, tsuchiya2007transcriptionalregulationof pages 1-2, krause2001lossofcell pages 1-2)

## Primary molecular function and substrate

**The best-supported annotation is an ATP-dependent DNA-clamp-loader subunit.** RfC3 is predicted to contribute to the small-subunit core of RFC complexes, whose principal replication function is to place the ring-shaped proliferating cell nuclear antigen (**PCNA**) clamp around DNA at a **3′ primer–template junction**. PCNA then provides a mobile platform that supports processive DNA synthesis, notably by DNA polymerase δ. RFC is therefore **not a DNA polymerase**: its relevant substrates are ATP and the PCNA–primed-DNA loading assembly, rather than free nucleotides for incorporation into DNA. The reaction is best described at the *complex* level—ATP-dependent PCNA ring opening and placement around primed DNA, followed by ATP hydrolysis and clamp-loader release—not as an independently demonstrated catalytic reaction of isolated fly RfC3. Fly RfC3-specific ATPase kinetics, ATP-binding requirements and substrate specificity have not been established in the retrieved studies. (tsuchiya2007transcriptionalregulationof pages 1-2, zheng2024structureofthe pages 1-2, he2024cryoemrevealsa pages 1-2, he2024cryoemrevealsa pages 2-3)

The structural basis for this assignment is substantial but **cross-species**. RFC complexes contain one large subunit and four smaller RFC2–RFC5 subunits with AAA+ and C-terminal collar architecture. A 2024 human cryo-EM study resolved **seven** structural states of the alternative CTF18–RFC complex as it engages PCNA and a 3′ single-stranded/double-stranded DNA junction; these states show how the shared small-subunit machinery contributes to clamp loading. Its authors distinguish canonical RFC, which predominantly loads PCNA, from alternative complexes that exchange the large subunit. Their human RFC3 structural position must not be mapped residue-for-residue onto fly Q9VKW3 without a fly-specific alignment or structure. (he2024cryoemrevealsa pages 1-2, he2024cryoemrevealsa pages 2-3, he2024cryoemrevealsa pages 3-5)

**Complex membership determines pathway specificity.** Canonical RFC1–RFC2–RFC3–RFC4–RFC5 loads PCNA during replication; CTF18-containing RFC-like complexes also load PCNA, whereas Elg1-containing complexes preferentially *unload* it. A 2024 yeast structural/biochemical study demonstrated PCNA unloading by Elg1–RFC and identified features of the exchanged large subunit that restrict DNA access. Thus it would be misleading to label RfC3 itself an exclusively loading or exclusively unloading enzyme, or to equate it with the large-subunit checkpoint clamp loader. Direct incorporation of fly Q9VKW3 into each proposed alternative complex was not established by the studies assessed here. (zheng2024structureofthe pages 1-2, he2024cryoemrevealsa pages 1-2, zheng2024structureofthe pages 2-3)

## Fly-specific biological evidence and cellular location

In a tissue-specific experiment, **Kohzaki (2018)** expressed the *Rfc3 IR-9* RNAi construct using **SD-Gal4**, which acts predominantly in developing wing imaginal discs. **All 158 scored adult flies had a wing phenotype**; the paper groups Rfc3 with replication-elongation factors whose depletion impairs wing development. This is direct evidence that reducing fly *Rfc3* disrupts normal development of a proliferating tissue. It is **not** a direct measurement of PCNA loading, DNA synthesis, checkpoint signaling or a distinct wing-patterning activity; the reported result uses one Rfc3 RNAi reagent, and the retrieved text does not establish an independent rescue. The original table confirms the denominator and percentage. (kohzaki2018thefunctionof pages 1-2, kohzaki2018thefunctionof pages 2-5, kohzaki2018thefunctionof pages 5-6, kohzaki2018thefunctionof media ab80de68)

A fly larval transcriptome study by **Érdi and colleagues (2012)** names **RfC3** among DNA-replication-related transcripts in a class repressed under starvation in autophagy-mutant animals. That is evidence of context-dependent **gene expression**, not of RfC3 protein depletion, a measured RfC3-specific fold change, or a direct molecular role in autophagy. The most parsimonious pathway assignment remains **nuclear DNA replication and PCNA-dependent DNA metabolism**, with possible participation in repair through shared clamp-loader machinery; a fly-RfC3-specific DNA-repair or signaling mechanism remains unproven by these observations. (erdi2012lossofthe pages 4-5, erdi2012lossofthe pages 3-4, tsuchiya2007transcriptionalregulationof pages 1-2, he2024cryoemrevealsa pages 1-2)

RfC3’s **expected site of action is the nucleus, at primed DNA or replication-associated chromatin**, because that is where RFC handles PCNA and DNA. This is a **functional localization inference**, not a demonstrated immunolocalization of Q9VKW3. For comparison, a fly study observed **DmRFC4** in replicating nuclei and studied its checkpoint phenotypes, but those are measurements of a *different subunit* and cannot establish RfC3’s precise localization, cell-cycle dynamics or checkpoint activity. No extracellular or membrane-transport role is supported. (tsuchiya2007transcriptionalregulationof pages 1-2, krause2001lossofcell pages 1-2, he2024cryoemrevealsa pages 1-2)

The evidence distinctions are summarized below.

| Aspect | Specific observation or inference | Organism | Evidence strength / limitation |
|---|---|---|---|
| Developmental phenotype | Wing-disc expression of the single **Rfc3 IR-9** RNAi reagent with **SD-Gal4** produced an abnormal-wing phenotype in **100% of 158 adult flies**. (kohzaki2018thefunctionof pages 2-5, kohzaki2018thefunctionof pages 5-6, kohzaki2018thefunctionof media ab80de68) | *D. melanogaster* | **Direct, quantitative RfC3 perturbation evidence.** Strong phenotype, but only one RNAi reagent was reported; no rescue, clamp-loading assay, or DNA-replication-rate measurement establishes the mechanism. |
| Nutrient-responsive expression | **RfC3** was listed among DNA-replication genes repressed in starved autophagy-mutant larvae. (erdi2012lossofthe pages 4-5, erdi2012lossofthe pages 3-4) | *D. melanogaster* | **High-throughput transcriptomic association.** No RfC3-specific fold change or functional test; this does not establish a direct role in autophagy. |
| Conserved biochemical function | The shared **RFC2–RFC5 AAA+ module** participates in ATP-dependent handling of PCNA at primed **3′ ssDNA/dsDNA junctions**; 2024 structures captured seven CTF18-RFC loading intermediates. (he2024cryoemrevealsa pages 1-2, he2024cryoemrevealsa pages 2-3, he2024cryoemrevealsa pages 3-5) | Human complex | **Strong structural and biochemical evidence for conserved RFC architecture**, but activity of fly Q9VKW3 was not measured directly. |
| Loading versus unloading | Canonical RFC loads PCNA, whereas Elg1-RFC—with the same small-subunit core—unloads it; large-subunit features determine directionality and DNA access. (zheng2024structureofthe pages 1-2, zheng2024structureofthe pages 2-3) | Budding yeast complex | **Strong mechanistic evidence**, but assignment to fly RfC3 is evolutionary inference rather than a fly-specific assay. |
| Cellular location | A nuclear, chromatin-associated S-phase role is expected because RFC acts on PCNA and primed DNA. | Inferred for *D. melanogaster* | **Plausible but indirect.** No verified RfC3-specific localization experiment in flies was found. |
| Evidence explicitly excluded | DmRfc4 localizes to replicating nuclei and participates in replication/damage-checkpoint control. (krause2001lossofcell pages 1-2) | *D. melanogaster* | **Direct evidence for another RFC subunit only.** It provides complex-level context but must not be attributed as an observed property of Q9VKW3/RfC3. |


*Table: Evidence for Drosophila RfC3 is strongest for an RNAi developmental phenotype, while its precise clamp-loader activity and nuclear localization remain conservation-based inferences. The table separates direct fly observations from evidence obtained for other RFC subunits or species.*

## Recent developments and practical interpretation

The most informative **2023–2024-era mechanistic advances retrieved are 2024 studies of conserved clamp-loader complexes**, not new biochemical experiments on fly RfC3. **He and colleagues**, published **26 April 2024**, used human CTF18–RFC cryo-EM to capture seven PCNA-loading intermediates. **Zheng and colleagues**, published **1 March 2024**, resolved yeast Elg1–RFC structures and tested unloading biochemically. Together, these sharpen the functional interpretation of fly Q9VKW3: its conserved small-subunit architecture supports an RFC clamp-handling role, while the *large-subunit partner* and DNA context help determine the precise operation. They do **not** demonstrate that purified fly RfC3 catalyzes either reaction or establish which fly RFC-like assemblies contain it in vivo. (zheng2024structureofthe pages 1-2, he2024cryoemrevealsa pages 1-2, zheng2024structureofthe pages 2-3, he2024cryoemrevealsa pages 2-3)

A real-world **research use** of *RfC3* is tissue-targeted RNAi in flies to test the developmental requirement for replication machinery; the 2018 wing experiment provides a quantitative example. The retrieved evidence does not justify a clinical indication, biomarker claim or therapeutic application for this *Drosophila* gene. The decisive next experimental distinctions for a higher-confidence annotation would be fly-protein complex purification, PCNA-loading and ATPase assays, tagged-protein localization, and independently validated genetic perturbation; these are **evidence gaps**, not results already demonstrated. (kohzaki2018thefunctionof pages 2-5, kohzaki2018thefunctionof pages 5-6, kohzaki2018thefunctionof media ab80de68)

### Principal sources and dates

- Kohzaki H. **June 2018**. “The function of replication and SCF complex during Drosophila wing development.” *Frontiers in Bioscience* 23:2235–2244. [https://doi.org/10.2741/4702](https://doi.org/10.2741/4702). Direct fly *Rfc3* RNAi phenotype and sample size. (kohzaki2018thefunctionof pages 1-2, kohzaki2018thefunctionof pages 5-6, kohzaki2018thefunctionof media ab80de68)
- Érdi B *et al.* **July 2012**. “Loss of the starvation-induced gene Rack1 leads to glycogen deficiency and impaired autophagic responses in Drosophila.” *Autophagy* 8:1124–1135. [https://doi.org/10.4161/auto.20069](https://doi.org/10.4161/auto.20069). Fly transcriptomic context, not an RfC3 autophagy-function assay. (erdi2012lossofthe pages 4-5, erdi2012lossofthe pages 3-4)
- He Q *et al.* **26 April 2024**. “Cryo-EM reveals a nearly complete PCNA loading process and unique features of the human alternative clamp loader CTF18-RFC.” *PNAS* 121. [https://doi.org/10.1073/pnas.2319727121](https://doi.org/10.1073/pnas.2319727121). Conserved-core mechanistic evidence from **human**, not fly, protein. (he2024cryoemrevealsa pages 1-2, he2024cryoemrevealsa pages 2-3)
- Zheng F *et al.* **1 March 2024**. “Structure of the PCNA unloader Elg1-RFC.” *Science Advances* 10. [https://doi.org/10.1126/sciadv.adl1739](https://doi.org/10.1126/sciadv.adl1739). Alternative-complex mechanistic evidence from **yeast**, not fly. (zheng2024structureofthe pages 1-2, zheng2024structureofthe pages 2-3)
- Krause SA *et al.* **August 2001**. “Loss of Cell Cycle Checkpoint Control in Drosophila Rfc4 Mutants.” *Molecular and Cellular Biology* 21:5156–5168. [https://doi.org/10.1128/MCB.21.15.5156-5168.2001](https://doi.org/10.1128/MCB.21.15.5156-5168.2001). **RfC4 only**; included to delimit, not support, RfC3-specific localization or checkpoint claims. (krause2001lossofcell pages 1-2)

**Conclusion.** Fly RfC3 is most defensibly annotated as a conserved, nuclear-acting **RFC small subunit that enables ATP-dependent PCNA clamp handling at primed DNA**, chiefly in genome replication. The **direct fly-specific evidence** retrieved is a strong wing-development RNAi phenotype and a contextual transcriptomic observation; the detailed biochemical reaction, individual substrate contacts and localization of Q9VKW3 remain **inferred from conserved complexes rather than directly measured in the fly protein**. (kohzaki2018thefunctionof pages 2-5, kohzaki2018thefunctionof pages 5-6, erdi2012lossofthe pages 4-5, he2024cryoemrevealsa pages 1-2, kohzaki2018thefunctionof media ab80de68)

References

1. (kohzaki2018thefunctionof pages 1-2): Hidetsugu Kohzaki. The function of replication and scf complex during drosophila wing development. Frontiers in bioscience, 23:2235-2244, Jun 2018. URL: https://doi.org/10.2741/4702, doi:10.2741/4702. This article has 1 citations and is from a peer-reviewed journal.

2. (kohzaki2018thefunctionof pages 2-5): Hidetsugu Kohzaki. The function of replication and scf complex during drosophila wing development. Frontiers in bioscience, 23:2235-2244, Jun 2018. URL: https://doi.org/10.2741/4702, doi:10.2741/4702. This article has 1 citations and is from a peer-reviewed journal.

3. (tsuchiya2007transcriptionalregulationof pages 1-2): Akihiro Tsuchiya, Yoshihiro H. Inoue, Hiroyuki Ida, Yukari Kawase, Koji Okudaira, Katsuhito Ohno, Hideki Yoshida, and Masamitsu Yamaguchi. Transcriptional regulation of the drosophila rfc1 gene by the dre–dref pathway. The FEBS Journal, 274:1818-1832, Apr 2007. URL: https://doi.org/10.1111/j.1742-4658.2007.05730.x, doi:10.1111/j.1742-4658.2007.05730.x. This article has 36 citations.

4. (krause2001lossofcell pages 1-2): Sue A. Krause, Marie-Louise Loupart, Sharron Vass, Stefan Schoenfelder, Steve Harrison, and Margarete M. S. Heck. Loss of cell cycle checkpoint control in drosophila rfc4 mutants. Molecular and Cellular Biology, 21:5156-5168, Aug 2001. URL: https://doi.org/10.1128/mcb.21.15.5156-5168.2001, doi:10.1128/mcb.21.15.5156-5168.2001. This article has 62 citations and is from a domain leading peer-reviewed journal.

5. (zheng2024structureofthe pages 1-2): Fengwei Zheng, Nina Y. Yao, Roxana E. Georgescu, Huilin Li, and Michael E. O’Donnell. Structure of the pcna unloader elg1-rfc. Science Advances, Mar 2024. URL: https://doi.org/10.1126/sciadv.adl1739, doi:10.1126/sciadv.adl1739. This article has 8 citations and is from a highest quality peer-reviewed journal.

6. (he2024cryoemrevealsa pages 1-2): Qing He, Feng Wang, Michael E. O’Donnell, and Huilin Li. Cryo-em reveals a nearly complete pcna loading process and unique features of the human alternative clamp loader ctf18-rfc. Proceedings of the National Academy of Sciences of the United States of America, Apr 2024. URL: https://doi.org/10.1073/pnas.2319727121, doi:10.1073/pnas.2319727121. This article has 18 citations and is from a highest quality peer-reviewed journal.

7. (he2024cryoemrevealsa pages 2-3): Qing He, Feng Wang, Michael E. O’Donnell, and Huilin Li. Cryo-em reveals a nearly complete pcna loading process and unique features of the human alternative clamp loader ctf18-rfc. Proceedings of the National Academy of Sciences of the United States of America, Apr 2024. URL: https://doi.org/10.1073/pnas.2319727121, doi:10.1073/pnas.2319727121. This article has 18 citations and is from a highest quality peer-reviewed journal.

8. (he2024cryoemrevealsa pages 3-5): Qing He, Feng Wang, Michael E. O’Donnell, and Huilin Li. Cryo-em reveals a nearly complete pcna loading process and unique features of the human alternative clamp loader ctf18-rfc. Proceedings of the National Academy of Sciences of the United States of America, Apr 2024. URL: https://doi.org/10.1073/pnas.2319727121, doi:10.1073/pnas.2319727121. This article has 18 citations and is from a highest quality peer-reviewed journal.

9. (zheng2024structureofthe pages 2-3): Fengwei Zheng, Nina Y. Yao, Roxana E. Georgescu, Huilin Li, and Michael E. O’Donnell. Structure of the pcna unloader elg1-rfc. Science Advances, Mar 2024. URL: https://doi.org/10.1126/sciadv.adl1739, doi:10.1126/sciadv.adl1739. This article has 8 citations and is from a highest quality peer-reviewed journal.

10. (kohzaki2018thefunctionof pages 5-6): Hidetsugu Kohzaki. The function of replication and scf complex during drosophila wing development. Frontiers in bioscience, 23:2235-2244, Jun 2018. URL: https://doi.org/10.2741/4702, doi:10.2741/4702. This article has 1 citations and is from a peer-reviewed journal.

11. (kohzaki2018thefunctionof media ab80de68): Hidetsugu Kohzaki. The function of replication and scf complex during drosophila wing development. Frontiers in bioscience, 23:2235-2244, Jun 2018. URL: https://doi.org/10.2741/4702, doi:10.2741/4702. This article has 1 citations and is from a peer-reviewed journal.

12. (erdi2012lossofthe pages 4-5): Balázs Érdi, Péter Nagy, Ágnes Zvara, Ágnes Varga, Karolina Pircs, Dalma Ménesi, László G. Puskás, and Gábor Juhász. Loss of the starvation-induced gene rack1 leads to glycogen deficiency and impaired autophagic responses in drosophila. Autophagy, 8:1124-1135, Jul 2012. URL: https://doi.org/10.4161/auto.20069, doi:10.4161/auto.20069. This article has 92 citations and is from a domain leading peer-reviewed journal.

13. (erdi2012lossofthe pages 3-4): Balázs Érdi, Péter Nagy, Ágnes Zvara, Ágnes Varga, Karolina Pircs, Dalma Ménesi, László G. Puskás, and Gábor Juhász. Loss of the starvation-induced gene rack1 leads to glycogen deficiency and impaired autophagic responses in drosophila. Autophagy, 8:1124-1135, Jul 2012. URL: https://doi.org/10.4161/auto.20069, doi:10.4161/auto.20069. This article has 92 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](RfC3-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000015 Table 2, located on page 5, lists the phenotypes of various knockdowns using the SD-Gal4 driver. For the specific responder 'Rfc3 I](RfC3-deep-research-falcon_artifacts/image-1.png)

## Citations

1. krause2001lossofcell pages 1-2
2. kohzaki2018thefunctionof pages 1-2
3. kohzaki2018thefunctionof pages 2-5
4. tsuchiya2007transcriptionalregulationof pages 1-2
5. zheng2024structureofthe pages 1-2
6. he2024cryoemrevealsa pages 1-2
7. he2024cryoemrevealsa pages 2-3
8. he2024cryoemrevealsa pages 3-5
9. zheng2024structureofthe pages 2-3
10. kohzaki2018thefunctionof pages 5-6
11. erdi2012lossofthe pages 4-5
12. erdi2012lossofthe pages 3-4
13. Q9VKW3
14. https://doi.org/10.2741/4702
15. https://doi.org/10.4161/auto.20069
16. https://doi.org/10.1073/pnas.2319727121
17. https://doi.org/10.1126/sciadv.adl1739
18. https://doi.org/10.1128/MCB.21.15.5156-5168.2001
19. https://www.uniprot.org/uniprotkb/Q9VKW3/entry
20. https://doi.org/10.2741/4702](https://doi.org/10.2741/4702
21. https://doi.org/10.4161/auto.20069](https://doi.org/10.4161/auto.20069
22. https://doi.org/10.1073/pnas.2319727121](https://doi.org/10.1073/pnas.2319727121
23. https://doi.org/10.1126/sciadv.adl1739](https://doi.org/10.1126/sciadv.adl1739
24. https://doi.org/10.1128/MCB.21.15.5156-5168.2001](https://doi.org/10.1128/MCB.21.15.5156-5168.2001
25. https://doi.org/10.2741/4702,
26. https://doi.org/10.1111/j.1742-4658.2007.05730.x,
27. https://doi.org/10.1128/mcb.21.15.5156-5168.2001,
28. https://doi.org/10.1126/sciadv.adl1739,
29. https://doi.org/10.1073/pnas.2319727121,
30. https://doi.org/10.4161/auto.20069,