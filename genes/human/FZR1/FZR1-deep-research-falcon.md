---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T01:12:33.180643'
end_time: '2026-09-25T01:19:49.704584'
duration_seconds: 436.52
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: FZR1
  gene_symbol: FZR1
  uniprot_accession: Q9UM11
  protein_description: 'RecName: Full=Fizzy-related protein homolog {ECO:0000305};
    Short=Fzr; AltName: Full=CDC20-like protein 1; AltName: Full=Cdh1/Hct1 homolog;
    Short=hCDH1 {ECO:0000303|PubMed:31722219};'
  gene_info: Name=FZR1 {ECO:0000312|HGNC:HGNC:24824}; Synonyms=CDH1 {ECO:0000303|PubMed:14701726},
    FYR, FZR, KIAA1242;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the WD repeat CDC20/Fizzy family. .
  protein_domains: Cdc20/Fizzy. (IPR033010); WD40/YVTN_repeat-like_dom_sf. (IPR015943);
    WD40_CDC20-Fz. (IPR056150); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf. (IPR036322)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: FZR1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9UM11
- **Protein Description:** RecName: Full=Fizzy-related protein homolog {ECO:0000305}; Short=Fzr; AltName: Full=CDC20-like protein 1; AltName: Full=Cdh1/Hct1 homolog; Short=hCDH1 {ECO:0000303|PubMed:31722219};
- **Gene Information:** Name=FZR1 {ECO:0000312|HGNC:HGNC:24824}; Synonyms=CDH1 {ECO:0000303|PubMed:14701726}, FYR, FZR, KIAA1242;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the WD repeat CDC20/Fizzy family. .
- **Key Domains:** Cdc20/Fizzy. (IPR033010); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_CDC20-Fz. (IPR056150); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf. (IPR036322)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FZR1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FZR1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FZR1** (gene ID: FZR1, UniProt: Q9UM11) in human.

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
- **UniProt Accession:** Q9UM11
- **Protein Description:** RecName: Full=Fizzy-related protein homolog {ECO:0000305}; Short=Fzr; AltName: Full=CDC20-like protein 1; AltName: Full=Cdh1/Hct1 homolog; Short=hCDH1 {ECO:0000303|PubMed:31722219};
- **Gene Information:** Name=FZR1 {ECO:0000312|HGNC:HGNC:24824}; Synonyms=CDH1 {ECO:0000303|PubMed:14701726}, FYR, FZR, KIAA1242;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the WD repeat CDC20/Fizzy family. .
- **Key Domains:** Cdc20/Fizzy. (IPR033010); WD40/YVTN_repeat-like_dom_sf. (IPR015943); WD40_CDC20-Fz. (IPR056150); WD40_repeat_CS. (IPR019775); WD40_repeat_dom_sf. (IPR036322)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FZR1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FZR1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FZR1** (gene ID: FZR1, UniProt: Q9UM11) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Human FZR1 (UniProt Q9UM11): Functional-Annotation Research Report

## Executive summary

**Identity verification succeeded.** The requested target is human **FZR1** (*fizzy and cell division cycle 20 related 1*; ENSG00000105325), encoding the protein usually called **CDH1**, FZR, or the HCT1 homolog. This agrees with UniProt **Q9UM11**, the stated *Homo sapiens* origin, and membership in the WD-repeat CDC20/Fizzy family. No conflicting same-symbol protein was used. Importantly, “CDH1” is historically ambiguous because it also denotes E-cadherin; throughout this report, **CDH1 means FZR1/CDH1, the APC/C co-activator**, not E-cadherin. Human genetic studies and Open Targets independently connect this exact FZR1 locus to developmental and epileptic encephalopathy 109 (DEE109). (OpenTargets Search: -FZR1, manivannan2021denovofzr1 pages 11-14, rodriguez2019anovelhuman pages 3-4)

FZR1 is **not an enzyme acting alone**. It is a non-catalytic substrate receptor and co-activator for the anaphase-promoting complex/cyclosome (**APC/C**), a large E3 ubiquitin ligase. FZR1 binds selected proteins through short degradation signals, activates APC/C, and positions substrates for ubiquitin transfer by E2 enzymes. Its principal physiological role is to remove mitotic and cell-cycle-entry proteins from late mitosis through G1 and in quiescent or differentiated cells, thereby maintaining low cyclin/CDK activity and stabilizing cell-cycle exit. (yamano2019apcccurrentunderstanding pages 5-6, ledvin2023theanaphasepromotingcomplex pages 1-3)

| Aspect | Functional annotation | Strongest evidence | Confidence / caveat |
|---|---|---|---|
| Verified identity | **Human FZR1** (UniProt **Q9UM11**; ENSG00000105325) encodes fizzy-related protein 1, commonly called **CDH1**; aliases include FZR, FYR, KIAA1242, and HCT1 homolog. It is not E-cadherin, which is also commonly called CDH1. | Human genetic and cellular studies identify *FZR1* as encoding the APC/C co-activator CDH1; Open Targets maps FZR1 to ENSG00000105325 and DEE109 (OpenTargets Search: -FZR1, ledvin2023theanaphasepromotingcomplex pages 1-3, rodriguez2019anovelhuman pages 3-4). | **High.** Identity, organism, aliases, and function agree with the supplied UniProt record. The historical alias CDH1 is ambiguous unless qualified as FZR1/CDH1. |
| Family and architecture | Member of the conserved **CDC20/Fizzy WD-repeat family**. Its C-terminal WD40 beta-propeller provides degron-binding surfaces, while conserved N-terminal motifs, including the **C-box**, dock and activate APC/C. | Structural and biochemical studies establish the CDH1 WD40 propeller as the substrate-recruiting module and the C-box–APC8 interaction as part of catalytic-module repositioning (yamano2019apcccurrentunderstanding pages 5-6, yamano2019apcccurrentunderstanding pages 10-10). | **High** for family and WD40 mechanism. Exact InterPro boundaries are database annotations not independently re-established in the cited excerpts. |
| Primary molecular function | FZR1 is a **non-catalytic substrate receptor and co-activator** of the multisubunit E3 ubiquitin ligase APC/C. It recruits selected proteins, stimulates APC/C, and positions substrates for ubiquitin transfer by E2 enzymes; FZR1 does not itself catalyze ubiquitin transfer. | APC/C–CDH1 supports substrate ubiquitination and K11-linked-chain formation; UBCH10/UBE2C initiates ubiquitination, while UBE2S enhances highly ubiquitinated products (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3). | **High.** Catalysis belongs to the APC/C–E2 machinery, so describing isolated FZR1 as an enzyme would be misleading. |
| Substrate specificity | The WD40 propeller recognizes **D-box**, **KEN-box**, and **ABBA** degrons, often combinatorially and in a context supplied by disordered regions. D-box binding uses a bipartite receptor formed by CDH1 and APC10; degron accessibility and nearby phosphorylation can alter affinity and ubiquitination processivity. | Mutating degrons or their WD40-binding surfaces blocks ubiquitination; structures define distinct D-box and KEN-box surfaces and CDH1–APC10 co-reception (yamano2019apcccurrentunderstanding pages 5-6, yamano2019apcccurrentunderstanding pages 10-10). | **High** for canonical recognition but **moderate** for predicting new substrates. A motif alone does not establish physiological targeting. |
| Cell-cycle timing | APC/C–FZR1 is most active from **late mitosis and mitotic exit through G1**, after APC/C–CDC20 initiates anaphase. It clears mitotic regulators and maintains low cyclin/CDK activity, stabilizing G1 or quiescent arrest. | Reviews distinguish mitotic CDC20 from G1 CDH1 activity; FZR1 loss stabilizes mitotic proteins, and CDH1-dependent protein degradation helps maintain CDK4/6-inhibitor-induced arrest (yamano2019apcccurrentunderstanding pages 5-6, ke2024reciprocalantagonismof pages 3-4). | **High.** Exact activity windows vary by substrate and cell state; APC/C–FZR1 can also reactivate during stress outside canonical G1. |
| Spatial localization | FZR1 acts with APC/C in **nuclear and chromatin-associated** as well as cytosolic contexts. Nuclear/chromatin activity is evident during mitotic exit and neuronal differentiation; APC/C–CDH1 also functions in postmitotic neurons. | Chromatin proteomics and ubiquitination assays implicate APC/C–CDH1 in clearing INCENP/CPC proteins, Ki-67, and topoisomerase II alpha during neuronal differentiation (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3). | **Moderate.** Nuclear/chromatin function is directly supported, but a fixed nuclear-versus-cytosolic assignment is inaccurate because localization and APC/C association are regulated. |
| Canonical cell-cycle substrates | APC/C co-activators drive destruction of **securin and mitotic cyclins** to coordinate chromosome separation and mitotic exit. FZR1 mainly performs late-mitotic/G1 cleanup and continued cyclin suppression; initial securin and cyclin-B destruction at anaphase onset is predominantly APC/C–CDC20. | Mechanistic reviews describe the CDC20-to-CDH1 transition and the broader substrate specificity of CDH1 (yamano2019apcccurrentunderstanding pages 5-6, yamano2019apcccurrentunderstanding pages 10-10). | **High** for general APC/C biology. Securin destruction should not be presented as exclusively or primarily FZR1-dependent at metaphase–anaphase. |
| Chromosomal passenger complex | APC/C–FZR1 terminates chromosomal passenger complex activity by targeting **Aurora B** and CPC-associated proteins. Evidence supports CDH1-dependent ubiquitination of **INCENP** through conserved D-boxes and **borealin/CDCA8** through a noncanonical degron; survivin/BIRC5 also accumulates when neuronal APC/C–CDH1 function is impaired. | In 2023 proteomics, 9,452 proteins were quantified; 38 increased in Cdh1-mutant and 21 in Apc7-mutant cerebella. INCENP, Aurora B, survivin, and borealin were prominent shared changes, while corresponding mRNAs were unchanged (ledvin2023theanaphasepromotingcomplex pages 3-5). | **High** for INCENP and the borealin/Aurora-B pathway; **moderate** for direct survivin recognition. Accumulation after perturbation does not alone prove direct binding. |
| Additional chromatin substrates | **Ki-67** and **topoisomerase II alpha** were identified among major APC-targeted chromatin proteins eliminated during neuronal differentiation, preventing persistence of phosphorylated mitotic factors after cell-cycle exit. | Integrated neuronal proteomics and biochemical analyses identified Ki-67, topoisomerase II alpha, and CPC proteins as APC-regulated chromatin factors (ledvin2023theanaphasepromotingcomplex pages 1-3). | **Moderate to high.** The pathway is supported by APC/FZR1 models, but direct binding evidence is not equally complete for every proposed substrate. |
| PIN1 feedback loop | **PIN1** and FZR1 exhibit reciprocal antagonism. Active APC/C–FZR1 lowers PIN1 and other mitotic proteins. CDK4 phosphorylation of FZR1 at **Ser163** creates a PIN1-binding pSer-Pro site, and PIN1-catalyzed isomerization stabilizes phosphorylated, APC/C-inactive FZR1. | FZR1 knockout stabilized PIN1; S163A enhanced APC/C activity and G1 arrest, whereas S163E reduced activity. PIN1 increased the cis-Pro164 peptide fraction from 7% to 14.2%, and PIN1 knockout reduced FZR1-Ser163 phosphorylation by nearly twofold (ke2024reciprocalantagonismof pages 6-7, ke2024reciprocalantagonismof pages 5-6, ke2024reciprocalantagonismof pages 3-4). | **High** mechanistic evidence in cultured cells and mouse or cancer models. Clinical utility remains investigational. |
| Upstream regulation | **CDK phosphorylation** inhibits FZR1 association with APC/C during proliferative phases; dephosphorylation at mitotic exit promotes activation. **EMI1/FBXO5** inhibits APC/C–FZR1 around G1/S, permitting substrate accumulation. PIN1 can preserve the phosphorylated inhibitory state. | CDK4-dependent Ser163 phosphorylation reduced APC/C activity; palbociclib reduced FZR1 phosphorylation and increased APC/C binding, and PIN1 knockout strengthened this effect (ke2024reciprocalantagonismof pages 6-7, ke2024reciprocalantagonismof pages 5-6). | **High** for CDK4–Ser163–PIN1 regulation. EMI1 inhibition and mitotic-exit dephosphorylation are established general APC/C mechanisms but were not quantified in the retrieved excerpts. |
| Postmitotic neurons | APC/C–FZR1 participates in neuronal differentiation and chromatin-protein clearance after terminal mitosis. FZR1 may also have APC/C-independent functions, so phenotypes caused by FZR1 depletion alone cannot automatically be assigned to the ligase. | Conditional neuronal Cdh1 loss elevated a restricted chromatin/CPC protein set. A 2024 core-APC4 deletion study failed to confirm several proposed neuronal substrates and instead implicated USP1 and primary-neurite number (ledvin2023theanaphasepromotingcomplex pages 3-5, day2024deletionofa pages 16-16). | **Moderate.** Strong causal designs should combine FZR1 manipulation with core-APC/C perturbation and direct ubiquitination or rescue assays. |
| Human neurodevelopmental disease | Heterozygous de novo loss-of-function or damaging missense variants cause **developmental and epileptic encephalopathy 109**, characterized by developmental delay or intellectual disability, generalized or myoclonic-atonic epilepsy, and sometimes ataxia or microcephaly. | A p.Asp187Gly variant found among 390 neurodevelopmental-disorder trios reduced CDH1 abundance and APC/C activity. Later cases carried p.Asp187Asn or p.Asn333Lys; reported constraint metrics included pLI 1, missense observed/expected 0.04, and z-score 3.64 (OpenTargets Search: -FZR1, manivannan2021denovofzr1 pages 11-14, manivannan2021denovofzr1 pages 8-11, rodriguez2019anovelhuman pages 3-4). | **High** gene–disease confidence, but few individuals have been reported. Phenotypic breadth and genotype–phenotype relationships remain incomplete; microcephaly is not obligatory. |
| 2023 development | Quantitative neurodevelopmental proteomics refined FZR1 annotation toward a selective **postmitotic chromatin-protein clearance system**, highlighting an APC/C-controlled ubiquitination–phosphoprotein axis involving CPC proteins, Ki-67, and topoisomerase II alpha. | Ledvin et al., *Developmental Cell*, December 2023, DOI: https://doi.org/10.1016/j.devcel.2023.10.002 (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3). | **High** for the studied mouse cerebellar and human-cell models. Generalization to all neuronal populations requires further testing. |
| 2024 development and therapy | Combined **PIN1 and CDK4/6 inhibition** can activate APC/C–FZR1, reduce PIN1 and mitotic proteins, enforce cell-cycle exit, and stimulate antitumor immunity in triple-negative breast-cancer models. In nine paired breast tumors treated with endocrine blockade plus palbociclib, PIN1 increased after progression and correlated with Ki-67. | Ke et al., *Nature Communications*, April 2024, DOI: https://doi.org/10.1038/s41467-024-47427-w (ke2024reciprocalantagonismof pages 6-7, ke2024reciprocalantagonismof pages 1-2). | **Promising preclinical evidence**, not an approved FZR1-directed therapy. Manipulating APC/C–FZR1 may also affect genome stability and normal proliferative tissues. |
| Translational status | FZR1 is currently most actionable as a **diagnostic disease gene**, mechanistic biomarker, and pathway node that may influence responses to CDK4/6- or PIN1-directed treatment, rather than as an established direct drug target. | Open Targets links FZR1 to DEE109 and developmental delay; current therapeutic studies manipulate upstream regulators or APC/C activity rather than clinically validated FZR1-selective compounds (OpenTargets Search: -FZR1, ke2024reciprocalantagonismof pages 1-2). | **High** for genetic-diagnostic relevance but **low to moderate** for therapeutic readiness. No approved FZR1-selective activator or inhibitor or direct clinical-efficacy evidence was identified. |


*Table: Compact functional-annotation table distinguishing direct FZR1/CDH1 evidence from broader APC/C biology. It integrates molecular mechanism, localization, substrates, regulation, disease genetics, and key 2023–2024 developments.*

## 1. Protein architecture and primary biochemical function

The C-terminal portion of FZR1 forms a **WD40 beta-propeller**, consistent with the supplied Cdc20/Fizzy and WD40 InterPro assignments. This propeller is a protein-interaction scaffold rather than a catalytic domain. It recognizes APC/C substrates bearing destruction motifs, especially:

- **D-boxes**, commonly represented as RxxLxxxxN;
- **KEN boxes**;
- **ABBA motifs**.

D-box and KEN-box peptides occupy distinct surfaces on the WD40 propeller. The D-box is recognized by a bipartite receptor formed by FZR1/CDH1 and APC10. The conserved N-terminal **C-box** of FZR1 binds the APC/C platform, including APC8, and helps reposition the APC2–APC11 catalytic module into an active configuration. Thus, FZR1 contributes both **substrate recruitment** and **allosteric activation**. Mutating a substrate degron or the corresponding WD40-binding surface inhibits ubiquitination. Degron number, spacing, accessibility, surrounding disorder, and nearby phosphorylation determine affinity and processivity; merely finding a D-box-like sequence is therefore insufficient to call a protein a physiological FZR1 substrate. (yamano2019apcccurrentunderstanding pages 5-6, yamano2019apcccurrentunderstanding pages 10-10)

Once recruited, substrate lysines are ubiquitinated by APC/C-associated E2 enzymes. UBE2C/UBCH10 supports ubiquitin initiation, while UBE2S promotes formation or extension of highly ubiquitinated, commonly K11-linked products that are recognized by the proteasome. FZR1 does not itself transfer ubiquitin and has no independent catalytic reaction or small-molecule substrate specificity analogous to an enzyme or transporter. (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3)

## 2. Cell-cycle pathway and temporal regulation

APC/C uses two related WD40 co-activators in sequence. **CDC20** primarily operates during mitosis and initiates anaphase-associated destruction; **FZR1/CDH1** assumes the dominant role during late mitosis, mitotic exit, and G1. FZR1 has broader recognized substrate specificity than CDC20, although the complete structural basis for that breadth remains unresolved. Therefore, securin and cyclin-B degradation at initial anaphase onset should not be attributed exclusively to FZR1; its clearest role is late-mitotic/G1 cleanup and continued suppression of mitotic cyclins and other cell-cycle-entry factors. (yamano2019apcccurrentunderstanding pages 5-6, yamano2019apcccurrentunderstanding pages 10-10)

FZR1 activity is controlled by several interlocking mechanisms:

1. **Inhibitory CDK phosphorylation:** phosphorylation reduces FZR1 association with APC/C during proliferative phases.
2. **Dephosphorylation at mitotic exit:** this promotes APC/C binding and activation.
3. **EMI1/FBXO5 inhibition near G1/S:** inhibition of APC/C–FZR1 allows cyclins and other S-phase proteins to accumulate.
4. **Substrate-level controls:** degron masking, phosphorylation, localization, and competition tune individual degradation rates.
5. **PIN1-dependent conformational regulation:** recent work shows that CDK4 phosphorylation of FZR1 at Ser163 creates a pSer-Pro site recognized by PIN1, which helps preserve an APC/C-inactive FZR1 state. (ke2024reciprocalantagonismof pages 6-7, ke2024reciprocalantagonismof pages 5-6)

In 2024 experiments, phospho-deficient **FZR1-S163A** increased APC/C activity and G1 arrest, whereas phosphomimetic **S163E** reduced APC/C activity and opposed CDK4-inhibitor-induced loss of mitotic proteins. PIN1 knockout reduced Ser163 phosphorylation by nearly twofold and increased FZR1–APC/C association. Biophysical measurements showed PIN1 increasing the cis-Pro164 fraction of a phosphorylated FZR1 peptide from 7% to 14.2%. These results define a CDK4–FZR1–PIN1 switch that can operate independently of canonical RB transcriptional control. (ke2024reciprocalantagonismof pages 6-7, ke2024reciprocalantagonismof pages 5-6)

## 3. Subcellular localization and site of action

FZR1 acts intracellularly with APC/C and should not be annotated as secreted, membrane-spanning, or extracellular. Its function is dynamic rather than confined to one organelle. The strongest evidence supports action in:

- the **nucleus and on chromatin**, particularly during mitotic exit and removal of residual mitotic chromatin proteins;
- the **nucleoplasm/cytosol**, where APC/C–FZR1 can encounter soluble cell-cycle regulators;
- **postmitotic neurons**, where it participates in non-mitotic proteostasis and developmental programs.

Chromatin-associated activity is supported by the accumulation of chromosome-passenger-complex proteins, Ki-67, and topoisomerase II alpha when neuronal APC/C–FZR1 function is impaired. Because phosphorylation, APC/C binding, and the cell cycle alter its distribution and activity, assigning FZR1 a single fixed localization would be misleading. (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3)

## 4. Principal substrates and biological processes

### 4.1 Mitotic exit and maintenance of G1

The central pathway is **APC/C-dependent ubiquitin-mediated proteolysis**. By maintaining low abundance of mitotic cyclins and other cell-cycle proteins after mitosis, APC/C–FZR1 reinforces low CDK activity, stable G1, quiescence, or terminal differentiation. FZR1 loss stabilizes PIN1 and multiple mitotic proteins despite only modest changes in their transcripts, supporting predominantly post-translational control. (yamano2019apcccurrentunderstanding pages 5-6, ke2024reciprocalantagonismof pages 3-4)

### 4.2 Chromosomal passenger complex termination

APC/C–FZR1 helps terminate the chromosomal passenger complex (**CPC**) after mitosis. Direct or strong mechanistic evidence supports targeting of:

- **Aurora B/AURKB**;
- **INCENP**, recognized through four conserved D-boxes and additional disordered-region features;
- **borealin/CDCA8**, through a noncanonical N-terminal degron;
- likely regulation of **survivin/BIRC5**, although accumulation alone is weaker evidence of direct recognition.

Failure to clear these factors can sustain Aurora-B-associated signaling into G1 and interfere with subsequent DNA replication. (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3)

A 2023 neuronal proteomics study quantified **9,452 proteins**. Only **38 proteins increased in Cdh1-mutant cerebella** and **21 in Apc7-mutant cerebella**, indicating a selective rather than global effect. INCENP, Aurora B, survivin, and borealin were among the strongest shared changes, while INCENP and Aurora-B mRNA did not increase, supporting post-transcriptional clearance. Reconstituted APC/C–FZR1 ubiquitinated INCENP with UBE2C, and UBE2S enhanced highly ubiquitinated products. (ledvin2023theanaphasepromotingcomplex pages 3-5)

### 4.3 Postmitotic chromatin remodeling and neurodevelopment

The same 2023 study identified the CPC, **Ki-67**, and **topoisomerase II alpha** as major APC-targeted chromatin factors during neuronal differentiation. Their removal prevents phosphorylated mitotic proteins from persisting after terminal cell-cycle exit and establishes a mechanistic link between ubiquitination and the neuronal chromatin phosphoproteome. The paper was published in *Developmental Cell* in December 2023: https://doi.org/10.1016/j.devcel.2023.10.002. (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3)

A significant expert caveat is that FZR1 and CDC20 may also have APC/C-independent functions. Consequently, a phenotype caused only by FZR1 knockdown is not sufficient to establish APC/C dependence. A 2024 study deleting the core subunit APC4 in neurons failed to validate several previously proposed neuronal APC/C substrates and instead implicated USP1 abundance and the number of primary neurites. Strong substrate assignments should therefore combine FZR1 perturbation with core-APC/C perturbation, degron mutagenesis, binding, direct ubiquitination, and rescue. The APC4 study appeared in *Frontiers in Molecular Neuroscience* in June 2024: https://doi.org/10.3389/fnmol.2024.1352782. (day2024deletionofa pages 16-16)

## 5. Human disease and functional genetics

Heterozygous de novo damaging variants in FZR1 cause **developmental and epileptic encephalopathy 109**. Reported manifestations include developmental delay or intellectual disability, generalized or myoclonic-atonic seizures, mild ataxia, and sometimes prenatal microcephaly. Microcephaly is not obligatory. Open Targets associates the exact human FZR1 locus with DEE109, global developmental delay, and early-onset epileptic encephalopathy. (OpenTargets Search: -FZR1, manivannan2021denovofzr1 pages 11-14)

A 2019 study screened **390 parent–child trios** with neurodevelopmental disease and found de novo **p.Asp187Gly**. Patient leukocytes had reduced FZR1/CDH1 abundance; expression in HEK293T cells produced less protein, lower APC/C activity, and altered cell-cycle distribution. The mutant also failed to rescue the enlarged replicative phase caused by Fzr1 loss in cortical progenitors. This provides a molecular chain from variant to reduced protein/APC/C function to disturbed progenitor-cell cycling. Publication: Rodríguez et al., *Journal of Neurochemistry*, August 2019, https://doi.org/10.1111/jnc.14828. (rodriguez2019anovelhuman pages 3-4)

Subsequent cases included de novo **p.Asp187Asn** and recurrent **p.Asn333Lys** variants, with Drosophila rescue and neurodevelopmental assays supporting loss of function. Reported human constraint metrics—**pLI 1**, missense observed/expected **0.04**, and missense z-score **3.64**—indicate strong intolerance to disruptive variation. The cohort evidence remains small, so the full phenotypic range and variant-specific correlations are not yet settled. (manivannan2021denovofzr1 pages 11-14, manivannan2021denovofzr1 pages 8-11)

## 6. Recent developments, 2023–2024

### 6.1 Selective neuronal chromatin clearance—2023

Ledvin and colleagues refined the view of APC/C–FZR1 in neurons: rather than causing indiscriminate proteome turnover, FZR1 loss affected a limited protein set enriched for chromatin and CPC factors. This supports a precise postmitotic function—eliminating mitotic chromatin machinery after neuronal cell-cycle exit—while also showing that deletion of mitotic co-activator CDC20 produces a substantially different developmental phenotype. (ledvin2023theanaphasepromotingcomplex pages 3-5, ledvin2023theanaphasepromotingcomplex pages 1-3)

### 6.2 PIN1–FZR1 reciprocal antagonism—2024

Ke and colleagues identified APC/C–FZR1 as a major PIN1-associated E3-ligase system. Active APC/C–FZR1 reduces PIN1 and mitotic proteins, while PIN1 recognizes phosphorylated FZR1 and reinforces APC/C inactivation. Combined PIN1 and CDK inhibition created positive feedback toward FZR1 activation, persistent mitotic-protein degradation, cell-cycle exit, and antitumor immunity in triple-negative breast-cancer models. In **nine paired breast tumors** collected before treatment and after progression on endocrine blockade plus palbociclib, PIN1 increased after progression and correlated with Ki-67. Publication: *Nature Communications*, April 2024, https://doi.org/10.1038/s41467-024-47427-w. (ke2024reciprocalantagonismof pages 6-7, ke2024reciprocalantagonismof pages 1-2)

The study also reported breast-cancer survival comparisons with PIN1-low versus PIN1-high groups—56 versus 9 patients in one dataset and 103 versus 57 in a tissue microarray—with reported p-values of **7×10⁻⁴** and **0.0235**. These data strengthen clinical association but do not yet establish FZR1-directed therapeutic efficacy in patients. (ke2024reciprocalantagonismof pages 3-4)

## 7. Applications and translational status

### Genetic diagnosis

FZR1 is clinically relevant as a disease gene in exome/genome interpretation for children with developmental delay, generalized or myoclonic-atonic epilepsy, ataxia, or microcephaly. Variant interpretation is strengthened by de novo occurrence, absence from population databases, location in structurally important regions, reduced protein abundance or APC/C activity, and functional rescue assays. (OpenTargets Search: -FZR1, manivannan2021denovofzr1 pages 11-14, rodriguez2019anovelhuman pages 3-4)

### Cancer biomarkers and drug-response research

APC/C–FZR1 activity may influence the durability of arrest produced by **CDK4/6 inhibitors**. Palbociclib decreased inhibitory FZR1 phosphorylation and increased FZR1–APC/C binding, with stronger effects after PIN1 loss. This suggests that tumors with weak APC/C–FZR1 activity or elevated PIN1 may escape pharmacologically induced arrest more readily. However, this is a mechanistic and biomarker hypothesis, not an established clinical test. (ke2024reciprocalantagonismof pages 6-7, ke2024reciprocalantagonismof pages 5-6, ke2024reciprocalantagonismof pages 1-2)

### Therapeutic targeting

No approved FZR1-selective activator or inhibitor was identified. Current strategies act indirectly by inhibiting CDKs or PIN1, manipulating APC/C regulators, or exploiting the degradation pathway. Therapeutic activation may suppress proliferation by degrading mitotic proteins, but excessive or mistimed APC/C–FZR1 activity can also promote inappropriate cell-cycle exit, endoreplication, or genome instability in stressed cells. Systemic intervention could affect normal proliferative tissues and postmitotic neuronal functions; substrate- and context-selective approaches would therefore be preferable.

## 8. Expert assessment and annotation confidence

The most defensible primary annotation is:

> **Human FZR1 is the WD40 substrate-receptor/co-activator of APC/C that recognizes degron-bearing proteins and activates their polyubiquitination, principally from late mitosis through G1 and in differentiated cells, thereby terminating mitotic signaling and maintaining cell-cycle exit.**

Confidence is **high** for identity, APC/C co-activation, WD40 degron recognition, late-mitotic/G1 timing, and the neurodevelopmental disease association. Confidence is **high to moderate** for individual substrates: INCENP and borealin have direct degron/ubiquitination evidence, whereas accumulation of a protein after FZR1 loss alone is insufficient. Localization is best described as dynamic nuclear/chromatin and cytosolic activity rather than a single compartment. Therapeutic relevance is promising but remains preclinical; at present, the clearest real-world implementation is genetic diagnosis of DEE109 rather than direct pharmacological targeting.

References

1. (OpenTargets Search: -FZR1): Open Targets Query (-FZR1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (manivannan2021denovofzr1 pages 11-14): Sathiya N. Manivannan, Jolien Roovers, Noor Smal, Candace T. Myers, Dilsad Turkdogan, Filip Roelens, Oguz Kanca, Hyung-Lok Chung, Tasja Scholz, Katharina Hermann, Tatjana Bierhals, S. Hande Caglayan, Hannah Stamberger, Heather Mefford, Peter de Jonghe, Shinya Yamamoto, Sarah Weckhuysen, and Hugo J. Bellen. De novo fzr1 loss-of-function variants cause developmental and epileptic encephalopathies including myoclonic atonic epilepsy. Brain : a journal of neurology, Jun 2021. URL: https://doi.org/10.1101/2021.06.12.21256778, doi:10.1101/2021.06.12.21256778. This article has 0 citations.

3. (rodriguez2019anovelhuman pages 3-4): Cristina Rodríguez, Irene Sánchez‐Morán, Sara Álvarez, Pilar Tirado, Daniel M. Fernández‐Mayoralas, Beatriz Calleja‐Pérez, Ángeles Almeida, and Alberto Fernández‐Jaén. A novel human cdh1 mutation impairs anaphase promoting complex/cyclosome activity resulting in microcephaly, psychomotor retardation, and epilepsy. Journal of Neurochemistry, 151:103-115, Aug 2019. URL: https://doi.org/10.1111/jnc.14828, doi:10.1111/jnc.14828. This article has 23 citations and is from a domain leading peer-reviewed journal.

4. (yamano2019apcccurrentunderstanding pages 5-6): Hiroyuki Yamano. Apc/c: current understanding and future perspectives. F1000Research, 8:725, May 2019. URL: https://doi.org/10.12688/f1000research.18582.1, doi:10.12688/f1000research.18582.1. This article has 143 citations and is from a peer-reviewed journal.

5. (ledvin2023theanaphasepromotingcomplex pages 1-3): Leya Ledvin, Brandon M. Gassaway, Jonathan Tawil, Olivia Urso, Donald Pizzo, Kaeli A. Welsh, Derek L. Bolhuis, Daniel Fisher, Azad Bonni, Steven P. Gygi, Nicholas G. Brown, and Cole J. Ferguson. The anaphase-promoting complex controls a ubiquitination-phosphoprotein axis in chromatin during neurodevelopment. Dec 2023. URL: https://doi.org/10.1016/j.devcel.2023.10.002, doi:10.1016/j.devcel.2023.10.002. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (yamano2019apcccurrentunderstanding pages 10-10): Hiroyuki Yamano. Apc/c: current understanding and future perspectives. F1000Research, 8:725, May 2019. URL: https://doi.org/10.12688/f1000research.18582.1, doi:10.12688/f1000research.18582.1. This article has 143 citations and is from a peer-reviewed journal.

7. (ledvin2023theanaphasepromotingcomplex pages 3-5): Leya Ledvin, Brandon M. Gassaway, Jonathan Tawil, Olivia Urso, Donald Pizzo, Kaeli A. Welsh, Derek L. Bolhuis, Daniel Fisher, Azad Bonni, Steven P. Gygi, Nicholas G. Brown, and Cole J. Ferguson. The anaphase-promoting complex controls a ubiquitination-phosphoprotein axis in chromatin during neurodevelopment. Dec 2023. URL: https://doi.org/10.1016/j.devcel.2023.10.002, doi:10.1016/j.devcel.2023.10.002. This article has 16 citations and is from a highest quality peer-reviewed journal.

8. (ke2024reciprocalantagonismof pages 3-4): Shizhong Ke, Fabin Dang, Lin Wang, Jia-Yun Chen, Mandar T. Naik, Wenxue Li, Abhishek Thavamani, Nami Kim, Nandita M. Naik, Huaxiu Sui, Wei Tang, Chenxi Qiu, Kazuhiro Koikawa, Felipe Batalini, Emily Stern Gatof, Daniela Arango Isaza, Jaymin M. Patel, Xiaodong Wang, John G. Clohessy, Yujing J. Heng, Galit Lahav, Yansheng Liu, Nathanael S. Gray, Xiao Zhen Zhou, Wenyi Wei, Gerburg Wulf, and Kun Ping Lu. Reciprocal antagonism of pin1-apc/ccdh1 governs mitotic protein stability and cell cycle entry. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47427-w, doi:10.1038/s41467-024-47427-w. This article has 18 citations and is from a highest quality peer-reviewed journal.

9. (ke2024reciprocalantagonismof pages 6-7): Shizhong Ke, Fabin Dang, Lin Wang, Jia-Yun Chen, Mandar T. Naik, Wenxue Li, Abhishek Thavamani, Nami Kim, Nandita M. Naik, Huaxiu Sui, Wei Tang, Chenxi Qiu, Kazuhiro Koikawa, Felipe Batalini, Emily Stern Gatof, Daniela Arango Isaza, Jaymin M. Patel, Xiaodong Wang, John G. Clohessy, Yujing J. Heng, Galit Lahav, Yansheng Liu, Nathanael S. Gray, Xiao Zhen Zhou, Wenyi Wei, Gerburg Wulf, and Kun Ping Lu. Reciprocal antagonism of pin1-apc/ccdh1 governs mitotic protein stability and cell cycle entry. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47427-w, doi:10.1038/s41467-024-47427-w. This article has 18 citations and is from a highest quality peer-reviewed journal.

10. (ke2024reciprocalantagonismof pages 5-6): Shizhong Ke, Fabin Dang, Lin Wang, Jia-Yun Chen, Mandar T. Naik, Wenxue Li, Abhishek Thavamani, Nami Kim, Nandita M. Naik, Huaxiu Sui, Wei Tang, Chenxi Qiu, Kazuhiro Koikawa, Felipe Batalini, Emily Stern Gatof, Daniela Arango Isaza, Jaymin M. Patel, Xiaodong Wang, John G. Clohessy, Yujing J. Heng, Galit Lahav, Yansheng Liu, Nathanael S. Gray, Xiao Zhen Zhou, Wenyi Wei, Gerburg Wulf, and Kun Ping Lu. Reciprocal antagonism of pin1-apc/ccdh1 governs mitotic protein stability and cell cycle entry. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47427-w, doi:10.1038/s41467-024-47427-w. This article has 18 citations and is from a highest quality peer-reviewed journal.

11. (day2024deletionofa pages 16-16): Jennifer L. Day, Marilyn Tirard, and Nils Brose. Deletion of a core apc/c component reveals apc/c function in regulating neuronal usp1 levels and morphology. Frontiers in Molecular Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnmol.2024.1352782, doi:10.3389/fnmol.2024.1352782. This article has 2 citations.

12. (manivannan2021denovofzr1 pages 8-11): Sathiya N. Manivannan, Jolien Roovers, Noor Smal, Candace T. Myers, Dilsad Turkdogan, Filip Roelens, Oguz Kanca, Hyung-Lok Chung, Tasja Scholz, Katharina Hermann, Tatjana Bierhals, S. Hande Caglayan, Hannah Stamberger, Heather Mefford, Peter de Jonghe, Shinya Yamamoto, Sarah Weckhuysen, and Hugo J. Bellen. De novo fzr1 loss-of-function variants cause developmental and epileptic encephalopathies including myoclonic atonic epilepsy. Brain : a journal of neurology, Jun 2021. URL: https://doi.org/10.1101/2021.06.12.21256778, doi:10.1101/2021.06.12.21256778. This article has 0 citations.

13. (ke2024reciprocalantagonismof pages 1-2): Shizhong Ke, Fabin Dang, Lin Wang, Jia-Yun Chen, Mandar T. Naik, Wenxue Li, Abhishek Thavamani, Nami Kim, Nandita M. Naik, Huaxiu Sui, Wei Tang, Chenxi Qiu, Kazuhiro Koikawa, Felipe Batalini, Emily Stern Gatof, Daniela Arango Isaza, Jaymin M. Patel, Xiaodong Wang, John G. Clohessy, Yujing J. Heng, Galit Lahav, Yansheng Liu, Nathanael S. Gray, Xiao Zhen Zhou, Wenyi Wei, Gerburg Wulf, and Kun Ping Lu. Reciprocal antagonism of pin1-apc/ccdh1 governs mitotic protein stability and cell cycle entry. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47427-w, doi:10.1038/s41467-024-47427-w. This article has 18 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](FZR1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. ledvin2023theanaphasepromotingcomplex pages 3-5
2. ledvin2023theanaphasepromotingcomplex pages 1-3
3. day2024deletionofa pages 16-16
4. rodriguez2019anovelhuman pages 3-4
5. ke2024reciprocalantagonismof pages 3-4
6. yamano2019apcccurrentunderstanding pages 5-6
7. yamano2019apcccurrentunderstanding pages 10-10
8. ke2024reciprocalantagonismof pages 6-7
9. ke2024reciprocalantagonismof pages 5-6
10. ke2024reciprocalantagonismof pages 1-2
11. https://doi.org/10.1016/j.devcel.2023.10.002
12. https://doi.org/10.1038/s41467-024-47427-w
13. https://doi.org/10.1016/j.devcel.2023.10.002.
14. https://doi.org/10.3389/fnmol.2024.1352782.
15. https://doi.org/10.1111/jnc.14828.
16. https://doi.org/10.1038/s41467-024-47427-w.
17. https://doi.org/10.1101/2021.06.12.21256778,
18. https://doi.org/10.1111/jnc.14828,
19. https://doi.org/10.12688/f1000research.18582.1,
20. https://doi.org/10.1016/j.devcel.2023.10.002,
21. https://doi.org/10.1038/s41467-024-47427-w,
22. https://doi.org/10.3389/fnmol.2024.1352782,