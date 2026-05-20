---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T16:03:15.806817'
end_time: '2026-05-12T16:34:44.985399'
duration_seconds: 1889.18
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

Concise GO annotation research for human MAML1 / UniProt Q92585. Focus only on GO-relevant evidence for MAML1/Mastermind-like protein 1: transcription coactivator activity in the NOTCH intracellular domain-CSL/RBPJ/RBPSUH transcriptional activation complex; positive regulation of transcription of Notch receptor target genes (for example HES1) versus broader Notch signaling pathway terms; nuclear/nucleoplasm/nuclear speck localization and the specific MAML1-RBP-Jkappa-ICN1 complex; interactions with NOTCH1-4, RBPJ/RBPSUH, CREBBP/CBP, CDK8/Cyclin C, TP53 and whether these support specific terms over generic protein binding; roles in phosphorylation/turnover of NOTCH intracellular domain, chromatin/nucleosome acetylation at Notch enhancers, p53 coactivation, myogenic differentiation, heart/atrioventricular node development, and any caveats for over-broad developmental annotations or high-throughput protein binding. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human MAML1 / UniProt Q92585. Focus only on GO-relevant evidence for MAML1/Mastermind-like protein 1: transcription coactivator activity in the NOTCH intracellular domain-CSL/RBPJ/RBPSUH transcriptional activation complex; positive regulation of transcription of Notch receptor target genes (for example HES1) versus broader Notch signaling pathway terms; nuclear/nucleoplasm/nuclear speck localization and the specific MAML1-RBP-Jkappa-ICN1 complex; interactions with NOTCH1-4, RBPJ/RBPSUH, CREBBP/CBP, CDK8/Cyclin C, TP53 and whether these support specific terms over generic protein binding; roles in phosphorylation/turnover of NOTCH intracellular domain, chromatin/nucleosome acetylation at Notch enhancers, p53 coactivation, myogenic differentiation, heart/atrioventricular node development, and any caveats for over-broad developmental annotations or high-throughput protein binding. Include PMID/DOI citations and keep under 1500 words.

## Concise GO annotation research report: Human **MAML1** (Mastermind-like protein 1), UniProt **Q92585**

### Scope and intent
This report summarizes **GO-relevant** evidence for MAML1, emphasizing (i) its **specific transcription coactivator role** in the **nuclear NOTCH intracellular domain (NICD/ICN)–CSL/RBPJ** activation complex, (ii) **positive regulation of transcription of canonical Notch target genes** (e.g., HES family), (iii) **nuclear subcompartment localization** evidence, (iv) recruitment of **EP300/CREBBP (p300/CBP)** and **Mediator kinase module (CDK8–Cyclin C)**, and (v) evidence/caveats for broader developmental or high-throughput “binding” style annotations.

### Key concepts and GO-relevant definitions (current understanding)

**Canonical Notch transcription activation complex (NTC).** After Notch receptor activation and cleavage, NICD enters the nucleus and forms a **DNA-bound ternary complex** with **RBPJ/CSL** and **Mastermind-like (MAML)** proteins; this complex recruits coactivators and enables transcription of Notch target genes. Primary and review sources emphasize that MAML proteins act as **core coactivators** of NICD–RBPJ complexes rather than generic interactors. (wu2000maml1ahuman pages 2-3, wu2002identificationofa pages 2-3, hall2022thestructurebinding pages 1-2)

**GO emphasis: “positive regulation of transcription of Notch target genes” vs broad “Notch signaling.”** The strongest direct evidence for MAML1 typically reads out **transcriptional activation** (HES/HES4/DTX1 reporters; chromatin templates; ChIP-linked acetylation changes), supporting specific transcriptional regulation terms rather than broad pathway-level terms (which can be context- and tissue-dependent). (wu2000maml1ahuman pages 2-3, rogers2020maml1dependentnotchresponsivegenes pages 1-2)

**Coactivator recruitment at chromatin.** MAML1 is a scaffold-like coactivator that supports Notch-driven transcription by recruiting/activating histone acetyltransferases (**p300/CBP**) and linking to Mediator kinase module components (**CDK8–Cyclin C**), coupling transcriptional activation with **NICD phosphorylation and turnover**. (ribeiro2009transcriptionalmechanismsby pages 3-4, hansson2009thetranscriptionalcoactivator pages 1-1, ribeiro2009gsk3βisa pages 1-2, hall2022thestructurebinding pages 1-2)

### Molecular function (MF): specific coactivator activity in the NICD–RBPJ/CSL complex

**Ternary complex assembly and specificity.** Seminal work demonstrated that MAML1 forms a **DNA-binding complex** with **ICN (NICD)** and **RBP-Jκ (RBPJ/CSL)** and functions as a **transcriptional co-activator** for Notch receptors; it enhances Notch-induced transcription from a HES1 promoter reporter, and dominant-negative MAML1 reduces activation. (Wu et al., 2000, *Nat Genet*, Dec 2000, DOI: https://doi.org/10.1038/82644) (wu2000maml1ahuman pages 2-3)

**NOTCH1–4 interaction breadth.** Wu et al. reported that MAML1 can bind ICN1 and also interacts with ICN2–4 in vitro, supporting annotations consistent with coactivator activity across mammalian Notch intracellular domains in canonical transcriptional activation contexts (carefully: intracellular domains, not membrane receptors). (wu2000maml1ahuman pages 2-3)

**Prefer complex/coactivator terms over generic “protein binding.”** Because the core evidence is **functional (reporter activation) + mechanistic (ternary complex formation)**, MAML1 is better captured by Notch transcription coactivator/complex-associated terms than by a broad “protein binding” annotation alone. (wu2000maml1ahuman pages 2-3, wu2002identificationofa pages 2-3)

### Biological process (BP): positive regulation of transcription of Notch target genes (e.g., HES family)

**HES1-class transcriptional outcomes.** In the original characterization, MAML1 amplified NOTCH-induced transcription and specifically enhanced HES1 promoter activation, while dominant-negative MAML1 reduced it—direct functional support for **positive regulation of transcription of Notch target genes**. (wu2000maml1ahuman pages 2-3)

**Genetic requirement for Notch-responsive target gene induction.** In Jurkat T-ALL cells, **MAML1 knockout** eliminated Notch-responsive activation of representative targets (HES4, DTX1) and mapped essential regions for Notch-dependent induction; reduced transcription associated with reduced histone acetylation at targets (see below). (Rogers et al., 2020, *Mol Cell Biol*, May 2020, DOI: https://doi.org/10.1128/mcb.00014-20) (rogers2020maml1dependentnotchresponsivegenes pages 1-2)

**Caveat: promoter vs enhancer dependencies.** The same study showed promoter-proximal and enhancer-regulated targets can have different cofactor requirements (e.g., p300-HAT fusion rescue at one locus but not another), arguing for careful selection of GO BP terms focused on transcriptional regulation rather than over-generalizing to all Notch pathway outputs. (rogers2020varyingcofactorrequirements pages 1-5, rogers2020maml1dependentnotchresponsivegenes pages 1-2)

### Cellular component (CC): nucleus, nucleoplasm, nuclear bodies/speckles, and complex localization

**Nuclear localization is robust.** MAML proteins are nuclear and contain an NLS; nuclear localization is consistent with their role in DNA-bound NICD–RBPJ transcriptional activation. (ribeiro2009transcriptionalmechanismsby pages 2-3)

**Nuclear bodies / PML-associated structures (with caveats).** MAML1 was observed to localize to nuclear bodies and to relocalize ICN1 (and, in other work, p300 and acetylated histones) to nuclear bodies. However, several observations rely on overexpression and nuclear-body composition can vary (e.g., not always PML-positive), so “nuclear speck/PML body” annotations should be conservative unless supported by endogenous localization. (wu2000maml1ahuman pages 2-3, hansson2009thetranscriptionalcoactivator pages 1-1, wu2002identificationofa pages 2-3)

**Specific complex membership: NICD–RBPJ–MAML1.** Evidence supports MAML1 as a component of the **Notch transcription activation complex** rather than a generic nuclear complex, including biochemical purification/complex assembly logic in foundational work. (wu2002identificationofa pages 2-3, hall2022thestructurebinding pages 1-2)

### Chromatin and transcriptional machinery: EP300/CREBBP and Mediator kinase module (CDK8–Cyclin C)

**Recruitment/activation of p300/CBP and histone acetylation.** Primary experimental evidence indicates MAML1 recruits p300 to DNA–CSL–NICD complexes, binds p300 (C/H3 domain), and that p300–MAML1 complexes acetylate histone H3/H4 tails on chromatin in vitro; MAML1 also potentiates p300 autoacetylation and HAT activity, with correlated localization of MAML1/p300/acetylated histones to nuclear bodies. (Hansson et al., 2009, *Nucleic Acids Res*, Mar 2009, DOI: https://doi.org/10.1093/nar/gkp163) (hansson2009thetranscriptionalcoactivator pages 1-1, hansson2009thetranscriptionalcoactivator pages 9-10)

**H3K27 acetylation at Notch-responsive loci.** In Jurkat T-ALL, loss of MAML1 reduced Notch target gene expression together with decreased H3K27 acetylation, consistent with MAML1-dependent acetyltransferase activity at Notch-responsive chromatin. (rogers2020varyingcofactorrequirements pages 1-5, rogers2020maml1dependentnotchresponsivegenes pages 1-2)

**Mediator kinase module recruitment and NICD phosphorylation/turnover.** Multiple sources support that MAML1 interacts with/recruits **CDK8** (often discussed with Cyclin C as the Mediator kinase module), which phosphorylates serines in the NICD PEST domain and promotes proteasomal turnover linked to FBW7-mediated degradation—supporting GO BP terms around regulation of NICD stability/turnover in the transcription complex context. (ribeiro2009transcriptionalmechanismsby pages 3-4, ribeiro2009gsk3βisa pages 1-2, hall2022thestructurebinding pages 1-2)

### Notch-independent but GO-relevant transcriptional coactivation: TP53

**Direct p53 coactivator function.** Zhao et al. showed MAML1 interacts with p53 (N-terminus of MAML1 with p53 DNA-binding domain), occupies native p53 response elements (ChIP), enhances p53-dependent gene induction, and knockdown reduces p53-dependent gene expression; MAML1 also increased p53 half-life and enhanced phosphorylation/acetylation after DNA damage. (Zhao et al., 2007, *J Biol Chem*, Apr 2007, DOI: https://doi.org/10.1074/jbc.M608974200) (zhao2007thenotchregulator pages 1-2)

**GO implication.** These data support **specific “transcription coactivator activity” in a p53 context**, but curators should not conflate this with Notch complex membership; separate MF/BP annotations are warranted. (zhao2007thenotchregulator pages 1-2)

### Recent developments (2023–2024) and real-world implementation context

**Therapeutic targeting of the Notch transcription complex (NTC).** A 2023 T-ALL review lists agents that disrupt the Notch transcription complex via MAML1/NTC interference, including **SAHM1** (stapled peptide interfering with MAML1 binding to the NTC) and **NADI-351** (described as disrupting the NTC). While not providing new mechanistic data itself, it reflects expert synthesis of an application direction: targeting **NICD–RBPJ–MAML1** transcriptional output rather than upstream cleavage. (Toribio & González-García, 2023, *Int J Mol Sci*, Jan 2023, DOI: https://doi.org/10.3390/ijms24021383) (toribio2023notchpartnersin pages 5-6)

**Pharmacologic modulation of Notch loss-of-function phenotypes (HDAC axis).** In a 2024 in vivo intestinal context, Dai et al. showed that the HDAC inhibitor **valproic acid** could prevent intestinal consequences caused by Notch dimerization deficiency and by gamma-secretase inhibitors, highlighting real-world translational interplay between Notch transcriptional output and chromatin repression machinery. (Dai et al., 2024, *PLOS Genet*, Dec 2024, DOI: https://doi.org/10.1371/journal.pgen.1011486) (dai2024lossofnotch pages 1-2)

**Quantitative transcription-hub model (2024) with Mediator CDK module recruitment.** Live-imaging work in 2024 (Drosophila Mastermind, the orthologous coactivator class) provides a modern mechanistic model consistent with MAML1’s GO-relevant role: Mastermind-containing complexes promote formation of Notch transcription hubs that concentrate factors including the Mediator CDK module; importantly, only a subset of hubs become transcriptionally productive (reported ~37%), and a second signal can raise activation probability (~70%). This supports the idea that coactivator-driven assemblies regulate the probability of transcriptional initiation, and it offers a conceptual framework for how Mediator kinase module recruitment might shape Notch target transcription dynamics. (DeHaro-Arbona et al., 2024, *eLife*, May 2024, DOI: https://doi.org/10.7554/eLife.92083.3) (deharoarbona2024dynamicmodesof pages 1-2, deharoarbona2024dynamicmodesof pages 15-17)

### Annotation caveats (avoid over-broad terms; avoid HTP-only binding)

1. **Prefer “Notch target gene transcription” over broad “Notch signaling pathway”** unless direct pathway-level phenotypes are tied specifically to human MAML1 (not dnMAML pan-inhibition, not paralog redundancy). (rogers2020maml1dependentnotchresponsivegenes pages 1-2)
2. **Nuclear bodies/specks:** nuclear-body localization is supported but is **often overexpression-linked**; annotate cautiously at specific subnuclear compartments. (wu2002identificationofa pages 2-3, ribeiro2009transcriptionalmechanismsby pages 2-3)
3. **Complex vs binding:** many interactions (NOTCH1-4 ICD, RBPJ, p300/CBP, CDK8) are best captured as **functional complex membership/coactivator recruitment** rather than generic “protein binding,” because functional readouts (reporters, chromatin transcription, acetylation, KO) exist. (wu2000maml1ahuman pages 2-3, hansson2009thetranscriptionalcoactivator pages 1-1)

### Evidence-to-annotation map (summary)
| GO aspect (MF/BP/CC) | Suggested GO term label (not GO ID) | Evidence summary (1 sentence) | Key experimental system/assay | Representative paper (authors, year, journal) | DOI/URL | Caveats for annotation breadth/HTP |
|---|---|---|---|---|---|---|
| MF | transcription coactivator activity, RNA polymerase II transcription factor binding | Human MAML1 binds NICD and RBPJ/CSL to form the canonical Notch ternary complex and amplifies HES1-class reporter activation, supporting a specific coactivator role rather than generic protein binding. (wu2000maml1ahuman pages 2-3, wu2002identificationofa pages 2-3) | GST pulldown, co-IP, EMSA/co-shift, luciferase reporter | Wu et al., 2000, *Nature Genetics*; Wu et al., 2002, *MCB* | https://doi.org/10.1038/82644 ; https://doi.org/10.1128/MCB.22.21.7688-7700.2002 | Prefer specific Notch transcription-complex/coactivator terms over broad “protein binding”; avoid inferring noncanonical coactivator functions from Notch assays alone. |
| BP | positive regulation of transcription of Notch receptor target genes | MAML1 is required for activation of canonical Notch targets (HES1/HES4/DTX1 contexts), and knockout or dominant-negative constructs block induction. (wu2000maml1ahuman pages 2-3, rogers2020maml1dependentnotchresponsivegenes pages 1-2) | Jagged/NICD-responsive reporters, Jurkat MAML1 knockout and rescue | Wu et al., 2000, *Nature Genetics*; Rogers et al., 2020, *MCB* | https://doi.org/10.1038/82644 ; https://doi.org/10.1128/MCB.00014-20 | Strongest support is for positive regulation of transcription of Notch target genes, not necessarily for every broader “Notch signaling pathway” child term. |
| CC | nucleus / nucleoplasm | MAML1 is a nuclear protein with an NLS and functions in nuclear Notch transcription complexes on DNA/chromatin. (ribeiro2009transcriptionalmechanismsby pages 2-3) | Localization studies, domain analysis, chromatin transcription assays | Ribeiro & Wallberg, 2009, *Current Protein & Peptide Science* | https://doi.org/10.2174/138920309789630543 | Nuclear localization is well supported; “nucleoplasm” is reasonable, but exact subnuclear assignment depends on assay context. |
| CC | nuclear body / nuclear speck / PML body-associated localization | MAML1 localizes to nuclear bodies and can relocalize ICN1, p300, and acetylated histones there, but much of this evidence uses overexpression and not all bodies are PML-positive. (wu2000maml1ahuman pages 2-3, hansson2009thetranscriptionalcoactivator pages 1-1, wu2002identificationofa pages 2-3) | Fluorescence colocalization, overexpression microscopy | Wu et al., 2000, *Nature Genetics*; Hansson et al., 2009, *NAR* | https://doi.org/10.1038/82644 ; https://doi.org/10.1093/nar/gkp163 | Use caution with “nuclear speck” or “PML body” annotations because nuclear-body formation is partly overexpression-based and may not reflect a constitutive endogenous compartment. |
| CC | Notch transcription activation complex | Endogenous and reconstituted data support MAML1 as a component of the DNA-bound NICD–RBPJ/CSL activation complex, including ICN1 and also ICN2-4 binding. (wu2000maml1ahuman pages 2-3, wu2002identificationofa pages 2-3) | Size-exclusion chromatography, co-IP, in vitro complex assembly | Wu et al., 2002, *MCB* | https://doi.org/10.1128/MCB.22.21.7688-7700.2002 | This is stronger than generic “protein-containing complex”; annotate the specific Notch activation complex when possible. |
| MF/BP | NOTCH1-4 intracellular domain binding in activation complex context | MAML1 directly interacts with ICN1 and can bind ICN2-4, supporting receptor-family breadth within canonical Notch transcriptional activation. (wu2000maml1ahuman pages 2-3, wu2002identificationofa pages 2-3) | GST pulldown, reporter assays across ICN1-4 | Wu et al., 2000, *Nature Genetics*; Wu et al., 2002, *MCB* | https://doi.org/10.1038/82644 ; https://doi.org/10.1128/MCB.22.21.7688-7700.2002 | Binding evidence is strongest for intracellular domains in canonical transcription assays; avoid overextending to all receptor contexts or surface-signaling steps. |
| MF/BP | CREBBP/EP300 recruitment and chromatin acetylation at Notch-regulated loci | MAML1 recruits p300/CBP to DNA-CSL-NICD complexes, stimulates p300 autoacetylation/HAT activity, and supports H3/H4 acetylation and H3K27ac at Notch-responsive promoters/enhancers. (rogers2020varyingcofactorrequirements pages 1-5, ribeiro2009transcriptionalmechanismsby pages 3-4, hansson2009thetranscriptionalcoactivator pages 1-1) | In vitro chromatin transcription, HAT assays, ChIP/acetylation readouts, KO-rescue | Hansson et al., 2009, *NAR*; Rogers et al., 2020, *MCB* | https://doi.org/10.1093/nar/gkp163 ; https://doi.org/10.1128/MCB.00014-20 | Strong support for coactivator-mediated recruitment/activation of acetyltransferase activity; do not over-annotate MAML1 itself as the acetyltransferase. |
| BP | regulation of Notch intracellular domain phosphorylation / turnover | MAML1 recruits CDK8/cyclin C-associated machinery that promotes NICD PEST phosphorylation and subsequent FBW7-linked degradation, coupling transcriptional activation to NICD turnover. (ribeiro2009transcriptionalmechanismsby pages 3-4, ribeiro2009gsk3βisa pages 1-2, rogers2020maml1dependentnotchresponsivegenes pages 1-2) | Biochemical interaction studies, chromatin assays, mechanistic genetics/review synthesis | Hansson et al., 2009, *NAR*; Rogers et al., 2020, *MCB* | https://doi.org/10.1093/nar/gkp163 ; https://doi.org/10.1128/MCB.00014-20 | Best treated as regulation of NICD stability/turnover in the Notch transcription complex; evidence is partly mechanistic synthesis rather than a single direct human loss-of-function experiment. |
| MF/BP | TP53 coactivator activity / positive regulation of p53 target gene transcription | MAML1 directly interacts with p53, occupies p53-response elements, increases p53 half-life and phosphorylation/acetylation, and enhances p53-dependent transcription independently of Notch. (zhao2007thenotchregulator pages 1-2, ribeiro2009transcriptionalmechanismsby pages 4-5) | ChIP, p53 reporter assays, knockdown/overexpression, DNA damage assays | Zhao et al., 2007, *JBC* | https://doi.org/10.1074/jbc.M608974200 | This supports specific p53 coactivator terms, not generic protein binding; keep separate from canonical Notch annotations. |
| BP | positive regulation of myogenic differentiation | MAML1 has reported Notch-independent coactivator activity with MEF2C in myogenesis, supporting a possible myogenic BP annotation if direct human evidence is curated. (ribeiro2009transcriptionalmechanismsby pages 3-4, ribeiro2009transcriptionalmechanismsby pages 1-2) | Biochemical interaction/function studies summarized in review | Ribeiro & Wallberg, 2009, *Current Protein & Peptide Science* | https://doi.org/10.2174/138920309789630543 | Evidence here is largely review-level and cross-species/contextual; weaker than canonical Notch evidence and should be curated conservatively. |
| BP | heart / atrioventricular node development | Cardiac phenotypes from dominant-negative MAML or pathway-level studies implicate MAML-dependent Notch signaling in AV node development, but direct attribution to human MAML1 is indirect. (dai2024lossofnotch pages 1-2, toribio2023notchpartnersin pages 5-6) | Mouse developmental genetics, pathway perturbation, review synthesis | MacGrogan et al., 2018, *Nat Rev Cardiol*; Zhou & Liu, 2013, *Braz J Med Biol Res* | https://doi.org/10.1038/s41569-018-0100-2 ; https://doi.org/10.1590/1414-431X20133177 | Avoid over-broad human MAML1 developmental annotations unless supported by direct gene-specific experiments; dnMAML affects multiple MAML paralogs/pathway output. |


*Table: This table maps the strongest GO-relevant candidate annotations for human MAML1 to representative evidence and highlights where annotations should remain specific rather than broad. It is useful for distinguishing well-supported canonical Notch coactivator functions from weaker or context-dependent developmental and localization claims.*

### Representative publications (with dates and URLs)
- Wu et al. “MAML1… transcriptional co-activator for NOTCH receptors.” *Nature Genetics* (Dec 2000). https://doi.org/10.1038/82644 (wu2000maml1ahuman pages 2-3)
- Wu et al. “Identification of a family of Mastermind-like transcriptional coactivators…” *Molecular and Cellular Biology* (Nov 2002). https://doi.org/10.1128/MCB.22.21.7688-7700.2002 (wu2002identificationofa pages 2-3)
- Hansson et al. “MAML1 regulates p300 autoacetylation and HAT activity.” *Nucleic Acids Research* (Mar 2009). https://doi.org/10.1093/nar/gkp163 (hansson2009thetranscriptionalcoactivator pages 1-1)
- Zhao et al. “MAML1 interacts with p53 and functions as a coactivator.” *J Biol Chem* (Apr 2007). https://doi.org/10.1074/jbc.M608974200 (zhao2007thenotchregulator pages 1-2)
- Rogers et al. “MAML1-dependent Notch-responsive genes…” *Molecular and Cellular Biology* (May 2020). https://doi.org/10.1128/mcb.00014-20 (rogers2020maml1dependentnotchresponsivegenes pages 1-2)
- Toribio & González-García. “Notch partners in T-ALL pathogenesis.” *Int J Mol Sci* (Jan 2023). https://doi.org/10.3390/ijms24021383 (toribio2023notchpartnersin pages 5-6)
- DeHaro-Arbona et al. “Dynamic modes of Notch transcription hubs…” *eLife* (May 2024). https://doi.org/10.7554/eLife.92083.3 (deharoarbona2024dynamicmodesof pages 1-2, deharoarbona2024dynamicmodesof pages 15-17)
- Dai et al. “Loss of Notch dimerization perturbs intestinal homeostasis…” *PLOS Genetics* (Dec 2024). https://doi.org/10.1371/journal.pgen.1011486 (dai2024lossofnotch pages 1-2)


References

1. (wu2000maml1ahuman pages 2-3): Lizi Wu, Jon C. Aster, Stephen C. Blacklow, Robert Lake, Spyros Artavanis-Tsakonas, and James D. Griffin. Maml1, a human homologue of drosophila mastermind, is a transcriptional co-activator for notch receptors. Nature Genetics, 26:484-489, Dec 2000. URL: https://doi.org/10.1038/82644, doi:10.1038/82644. This article has 757 citations and is from a highest quality peer-reviewed journal.

2. (wu2002identificationofa pages 2-3): Lizi Wu, Tao Sun, Karla Kobayashi, Ping Gao, and James D. Griffin. Identification of a family of mastermind-like transcriptional coactivators for mammalian notch receptors. Molecular and Cellular Biology, 22:7688-7700, Nov 2002. URL: https://doi.org/10.1128/mcb.22.21.7688-7700.2002, doi:10.1128/mcb.22.21.7688-7700.2002. This article has 365 citations and is from a domain leading peer-reviewed journal.

3. (hall2022thestructurebinding pages 1-2): Daniel Hall, Benedetto Daniele Giaimo, Sung-Soo Park, Wiebke Hemmer, Tobias Friedrich, Francesca Ferrante, Marek Bartkuhn, Zhenyu Yuan, Franz Oswald, Tilman Borggrefe, Jean-François Rual, and Rhett A. Kovall. The structure, binding and function of a notch transcription complex involving rbpj and the epigenetic reader protein l3mbtl3. Nucleic Acids Research, 50:13083-13099, Feb 2022. URL: https://doi.org/10.1093/nar/gkac1137, doi:10.1093/nar/gkac1137. This article has 10 citations and is from a highest quality peer-reviewed journal.

4. (rogers2020maml1dependentnotchresponsivegenes pages 1-2): Julia M. Rogers, Bingqian Guo, Emily D. Egan, Jon C. Aster, Karen Adelman, and Stephen C. Blacklow. Maml1-dependent notch-responsive genes exhibit differing cofactor requirements for transcriptional activation. May 2020. URL: https://doi.org/10.1128/mcb.00014-20, doi:10.1128/mcb.00014-20. This article has 12 citations and is from a domain leading peer-reviewed journal.

5. (ribeiro2009transcriptionalmechanismsby pages 3-4): M. Saint Just Ribeiro and A. Wallberg. Transcriptional mechanisms by the coregulator maml1. Current Protein &amp; Peptide Science, 10:570-576, Dec 2009. URL: https://doi.org/10.2174/138920309789630543, doi:10.2174/138920309789630543. This article has 32 citations and is from a peer-reviewed journal.

6. (hansson2009thetranscriptionalcoactivator pages 1-1): Magnus L. Hansson, Anita E. Popko-Ścibor, Mariana Saint Just Ribeiro, Beverley M. Dancy, Mikael J. Lindberg, Philip A. Cole, and Annika E. Wallberg. The transcriptional coactivator maml1 regulates p300 autoacetylation and hat activity. Nucleic Acids Research, 37:2996-3006, Mar 2009. URL: https://doi.org/10.1093/nar/gkp163, doi:10.1093/nar/gkp163. This article has 76 citations and is from a highest quality peer-reviewed journal.

7. (ribeiro2009gsk3βisa pages 1-2): M. Saint Just Ribeiro, M. L. Hansson, M. J. Lindberg, A. E. Popko-Scibor, and A. E. Wallberg. Gsk3β is a negative regulator of the transcriptional coactivator maml1. Nucleic Acids Research, 37:6691-6700, Sep 2009. URL: https://doi.org/10.1093/nar/gkp724, doi:10.1093/nar/gkp724. This article has 45 citations and is from a highest quality peer-reviewed journal.

8. (rogers2020varyingcofactorrequirements pages 1-5): Julia M. Rogers, Bingqian Guo, Emily D. Egan, Jon C. Aster, Karen Adelman, and Stephen C. Blacklow. Varying co-factor requirements for maml1-dependent transcription at different notch-responsive target genes. bioRxiv, Jan 2020. URL: https://doi.org/10.1101/2020.01.13.905612, doi:10.1101/2020.01.13.905612. This article has 0 citations.

9. (ribeiro2009transcriptionalmechanismsby pages 2-3): M. Saint Just Ribeiro and A. Wallberg. Transcriptional mechanisms by the coregulator maml1. Current Protein &amp; Peptide Science, 10:570-576, Dec 2009. URL: https://doi.org/10.2174/138920309789630543, doi:10.2174/138920309789630543. This article has 32 citations and is from a peer-reviewed journal.

10. (hansson2009thetranscriptionalcoactivator pages 9-10): Magnus L. Hansson, Anita E. Popko-Ścibor, Mariana Saint Just Ribeiro, Beverley M. Dancy, Mikael J. Lindberg, Philip A. Cole, and Annika E. Wallberg. The transcriptional coactivator maml1 regulates p300 autoacetylation and hat activity. Nucleic Acids Research, 37:2996-3006, Mar 2009. URL: https://doi.org/10.1093/nar/gkp163, doi:10.1093/nar/gkp163. This article has 76 citations and is from a highest quality peer-reviewed journal.

11. (zhao2007thenotchregulator pages 1-2): Yongtong Zhao, Rebecca B. Katzman, Laurie M. Delmolino, Ishfaq Bhat, Ying Zhang, Channabasavaiah B. Gurumurthy, Aleksandra Germaniuk-Kurowska, Honey V. Reddi, Aharon Solomon, Mu-Sheng Zeng, Aisha Kung, Hui Ma, Qingshen Gao, Goberdhan Dimri, Adina Stanculescu, Lucio Miele, Lizi Wu, James D. Griffin, David E. Wazer, Hamid Band, and Vimla Band. The notch regulator maml1 interacts with p53 and functions as a coactivator*. Journal of Biological Chemistry, 282:11969-11981, Apr 2007. URL: https://doi.org/10.1074/jbc.m608974200, doi:10.1074/jbc.m608974200. This article has 105 citations and is from a domain leading peer-reviewed journal.

12. (toribio2023notchpartnersin pages 5-6): María Luisa Toribio and Sara González-García. Notch partners in the long journey of t-all pathogenesis. International Journal of Molecular Sciences, 24:1383, Jan 2023. URL: https://doi.org/10.3390/ijms24021383, doi:10.3390/ijms24021383. This article has 23 citations.

13. (dai2024lossofnotch pages 1-2): Quanhui Dai, Kristina Preusse, Danni Yu, Rhett A. Kovall, Konrad Thorner, Xinhua Lin, and Raphael Kopan. Loss of notch dimerization perturbs intestinal homeostasis by a mechanism involving hdac activity. PLOS Genetics, 20:e1011486, Dec 2024. URL: https://doi.org/10.1371/journal.pgen.1011486, doi:10.1371/journal.pgen.1011486. This article has 2 citations and is from a domain leading peer-reviewed journal.

14. (deharoarbona2024dynamicmodesof pages 1-2): F Javier DeHaro-Arbona, Charalambos Roussos, Sarah Baloul, Jonathan Townson, María J Gómez Lamarca, and Sarah Bray. Dynamic modes of notch transcription hubs conferring memory and stochastic activation revealed by live imaging the co-activator mastermind. eLife, May 2024. URL: https://doi.org/10.7554/elife.92083.3, doi:10.7554/elife.92083.3. This article has 22 citations and is from a domain leading peer-reviewed journal.

15. (deharoarbona2024dynamicmodesof pages 15-17): F Javier DeHaro-Arbona, Charalambos Roussos, Sarah Baloul, Jonathan Townson, María J Gómez Lamarca, and Sarah Bray. Dynamic modes of notch transcription hubs conferring memory and stochastic activation revealed by live imaging the co-activator mastermind. eLife, May 2024. URL: https://doi.org/10.7554/elife.92083.3, doi:10.7554/elife.92083.3. This article has 22 citations and is from a domain leading peer-reviewed journal.

16. (ribeiro2009transcriptionalmechanismsby pages 4-5): M. Saint Just Ribeiro and A. Wallberg. Transcriptional mechanisms by the coregulator maml1. Current Protein &amp; Peptide Science, 10:570-576, Dec 2009. URL: https://doi.org/10.2174/138920309789630543, doi:10.2174/138920309789630543. This article has 32 citations and is from a peer-reviewed journal.

17. (ribeiro2009transcriptionalmechanismsby pages 1-2): M. Saint Just Ribeiro and A. Wallberg. Transcriptional mechanisms by the coregulator maml1. Current Protein &amp; Peptide Science, 10:570-576, Dec 2009. URL: https://doi.org/10.2174/138920309789630543, doi:10.2174/138920309789630543. This article has 32 citations and is from a peer-reviewed journal.

## Citations

1. ribeiro2009transcriptionalmechanismsby pages 2-3
2. zhao2007thenotchregulator pages 1-2
3. toribio2023notchpartnersin pages 5-6
4. dai2024lossofnotch pages 1-2
5. wu2002identificationofa pages 2-3
6. hansson2009thetranscriptionalcoactivator pages 1-1
7. hall2022thestructurebinding pages 1-2
8. ribeiro2009transcriptionalmechanismsby pages 3-4
9. rogers2020varyingcofactorrequirements pages 1-5
10. hansson2009thetranscriptionalcoactivator pages 9-10
11. deharoarbona2024dynamicmodesof pages 1-2
12. deharoarbona2024dynamicmodesof pages 15-17
13. ribeiro2009transcriptionalmechanismsby pages 4-5
14. ribeiro2009transcriptionalmechanismsby pages 1-2
15. https://doi.org/10.1038/82644
16. https://doi.org/10.1128/mcb.00014-20
17. https://doi.org/10.1093/nar/gkp163
18. https://doi.org/10.1074/jbc.M608974200
19. https://doi.org/10.3390/ijms24021383
20. https://doi.org/10.1371/journal.pgen.1011486
21. https://doi.org/10.7554/eLife.92083.3
22. https://doi.org/10.1128/MCB.22.21.7688-7700.2002
23. https://doi.org/10.1128/MCB.00014-20
24. https://doi.org/10.2174/138920309789630543
25. https://doi.org/10.1038/s41569-018-0100-2
26. https://doi.org/10.1590/1414-431X20133177
27. https://doi.org/10.1038/82644,
28. https://doi.org/10.1128/mcb.22.21.7688-7700.2002,
29. https://doi.org/10.1093/nar/gkac1137,
30. https://doi.org/10.1128/mcb.00014-20,
31. https://doi.org/10.2174/138920309789630543,
32. https://doi.org/10.1093/nar/gkp163,
33. https://doi.org/10.1093/nar/gkp724,
34. https://doi.org/10.1101/2020.01.13.905612,
35. https://doi.org/10.1074/jbc.m608974200,
36. https://doi.org/10.3390/ijms24021383,
37. https://doi.org/10.1371/journal.pgen.1011486,
38. https://doi.org/10.7554/elife.92083.3,