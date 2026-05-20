---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T11:42:22.228713'
end_time: '2026-05-12T11:59:46.909548'
duration_seconds: 1044.68
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

Perform concise GO-focused deep research on the human RARA gene (UniProt P10276; retinoic acid receptor alpha, nuclear receptor). Summarize the core molecular function, major biological processes, cellular locations, key experimental evidence, ligand/DNA-binding and transcriptional regulation mechanism, disease/fusion context only where relevant to function, and GO annotation caveats. Include PMID or DOI citations where available, and keep the report focused for gene annotation review.

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

Perform concise GO-focused deep research on the human RARA gene (UniProt P10276; retinoic acid receptor alpha, nuclear receptor). Summarize the core molecular function, major biological processes, cellular locations, key experimental evidence, ligand/DNA-binding and transcriptional regulation mechanism, disease/fusion context only where relevant to function, and GO annotation caveats. Include PMID or DOI citations where available, and keep the report focused for gene annotation review.

## GO-focused research report: Human **RARA** (retinoic acid receptor alpha; UniProt P10276)

### 1) Key concepts and definitions (current understanding)

**RARA encodes RARα**, a ligand-activated nuclear receptor that functions as a **sequence-specific DNA-binding transcription factor**. RARα typically acts as a heterodimer with retinoid X receptor (RXR) on **retinoic acid response elements (RAREs)**, classically composed of **direct repeats of the hexamer PuG(G/T)TCA** spaced by 1–5 bp (e.g., DR5, DR2, DR1). Element spacing determines **heterodimer polarity** and can alter transcriptional outcome (activation vs repression). (bastien2004nuclearretinoidreceptors pages 3-5)

RARα supports a canonical nuclear-receptor **cofactor “switch” mechanism**: in the **absence of ligand**, RARα/RXR bound on DNA recruits **corepressors** such as **NCoR/SMRT** that are associated with histone deacetylase (HDAC) activity and transcriptional repression; upon **retinoid agonist binding**, ligand-induced conformational changes (notably involving AF-2/helix 12 in the ligand-binding domain) destabilize corepressor binding and favor recruitment of **coactivators** (e.g., p160/SRC family, CBP/p300, Mediator/DRIP/TRAP components), enabling transcriptional activation of retinoid-responsive genes. (bastien2004nuclearretinoidreceptors pages 3-5, mouchon1999allostericregulationof pages 1-2, zechel2002syntheticretinoidsdissociate pages 3-4)

### 2) Core molecular function (GO molecular function focus)

#### 2.1 Retinoid ligand binding and ligand potency
Primary quantitative data for **human RARα** show nanomolar ligand-binding affinities and transcriptional activation potencies for natural and synthetic retinoids. In one study, binding **Kd (nM)** to hRARα included: **all-trans retinoic acid (atRA) 3.3**, **9-cis RA 7.1**, **TTNPB 2.2**, **CD367 4.0**, **Am580 8.1**, **CD3106 20.0**, and **CD2425 ~10,000**; the corresponding cell-based reporter **EC50 (nM)** values for RAR/RXR-driven transcription included **atRA 10.8**, **TTNPB 1.05**, **CD367 0.91**, and **Am580 0.74** (assayed across ~10⁻¹⁰ to 10⁻⁶ M ligand ranges). (mouchon1999allostericregulationof pages 2-3)

These measurements support GO MF concepts consistent with **“retinoic acid receptor activity”** and **ligand-dependent transcription factor activation**, with the caveat that potency depends strongly on response element context and receptor/cofactor states (see caveats). (mouchon1999allostericregulationof pages 2-3, mouchon1999allostericregulationof pages 9-10)

#### 2.2 Sequence-specific DNA binding to RAREs and polarity dependence
RARα binds RAREs primarily as an RXR heterodimer. Structural and biochemical evidence includes a **1.7 Å** crystal structure of RXR and RAR DNA-binding domains (DBDs) assembled on a **DR1** element that shows **RAR bound to the upstream (5′) half-site and RXR bound downstream (3′)**, i.e., **reverse polarity** compared with other RXR heterodimers. (rastinejad2000structureofthe pages 2-4, rastinejad2000structureofthe pages 1-2)

This structural work also provides quantitative binding behavior: the RXR–RAR heterodimer showed **half-maximal DR1 binding at ~300–350 nM**, while RXR DBD alone bound ~10× more weakly to a single AGGTCA site; importantly, the DBDs did not dimerize detectably in the absence of DNA response elements, supporting DNA-dependent cooperative assembly. (rastinejad2000structureofthe pages 2-4)

A complementary DBD-interface mapping study showed that specific DBD surfaces determine cooperative binding on DR elements, including a requirement for the RXR D-box for heterodimerization and DR-element-dependent determinants within the partner DBD that drive cooperative binding. (zechel1994dimerizationinterfacesformed pages 1-2)

**Implication for GO annotation review:** the same protein complex can support different outcomes depending on DR spacing and polarity; thus, “DNA-binding transcription factor activity, sequence-specific” is well supported, but BP-level terms tied to “activation” should be applied with response-element/context awareness. (bastien2004nuclearretinoidreceptors pages 3-5, mouchon1999allostericregulationof pages 9-10)

#### 2.3 RXR heterodimerization and allosteric coupling by DNA and ligand
DNA and ligand act as allosteric inputs that shape RARα/RXR transcriptional output. Experiments using purified proteins and DNA-bound complexes support that **RARE subtype/spacing** can modulate recruitment of coactivators (e.g., SRC-1) versus other cofactors, and that RXR AF-2 function can be required for full responsiveness of heterodimers to RAR ligands under certain contexts. (mouchon1999allostericregulationof pages 9-10)

### 3) Transcriptional regulation mechanism (GO: regulation of transcription by RNA polymerase II)

#### 3.1 Unliganded repression (corepressor complexes)
RARα/RXR complexes bound to RAREs recruit **NCoR/SMRT** corepressors linked to HDAC activity, supporting a mechanistic basis for **ligand-modulated transcriptional repression**. (bastien2004nuclearretinoidreceptors pages 3-5)

Direct biochemical evidence for corepressor engagement includes electrophoretic mobility shift assays (EMSA) where a **RAR–RXR heterodimer bound a RARE probe**, and addition of a SMRT interaction domain produced a **supershift**; importantly, the corepressor was **dissociated by a RAR agonist (AM580)** but **not** by an RXR-specific ligand, emphasizing that repression/activation switching can be ligand-isotype selective in a heterodimer. (benko2003moleculardeterminantsof pages 6-8)

#### 3.2 Ligand-induced activation (coactivator recruitment)
Ligand binding can drive coactivator recruitment to RARα complexes. In one mutational analysis of the RARα ligand-binding domain (LBD), dose–response reporter assays reported **AM580 EC50 ~7 nM** for RAR-LBD activity, and **~6.7 nM** for full-length RAR–RXR heterodimers; an LBD mutant (A392R) shifted potency to **~0.9–1.5 nM**, linking helix-12-adjacent residues to cofactor affinity and basal activity states. (benko2003moleculardeterminantsof pages 6-8)

Independent DNA- and ligand-dependent protein–protein interaction assays demonstrated that retinoids can promote **SRC-1 recruitment** to DNA-bound RXR–RAR heterodimers (with reported experimental replication and small SEs for some interaction measurements), further supporting a ligand-regulated coactivator switch. (mouchon1999allostericregulationof pages 9-10)

### 4) Cellular locations (GO cellular component focus)

RARα is primarily described as **nuclear** and **chromatin-associated** through binding to promoter/enhancer RAREs; nucleosomes do not necessarily preclude binding. (bastien2004nuclearretinoidreceptors pages 3-5, lefebvre2001molecularbasisfor pages 2-5)

A key structure supporting DNA-bound nuclear localization and chromatin engagement is shown in the RXR–RAR DBD complex on DR1 (Figure 2B in Rastinejad et al.), which visualizes the heterodimer orientation on DNA and the spatial arrangement of the DBDs engaging the response element. (rastinejad2000structureofthe media 89fe3bd5)

### 5) Major biological processes (GO biological process focus)

**Retinoic acid signaling and transcriptional regulation:** RARα is a central effector of retinoid signaling by converting ligand occupancy and DNA-element context into transcriptional activation/repression of RA-responsive genes. This is supported by quantitative reporter assays, DNA-dependent cofactor recruitment experiments, and structural studies of DNA recognition and cofactor switching. (mouchon1999allostericregulationof pages 2-3, mouchon1999allostericregulationof pages 9-10, rastinejad2000structureofthe pages 2-4)

**Myeloid differentiation (function-linked context):** RARα-mediated transcriptional programs are tightly linked to hematopoietic differentiation, illustrated most clearly by acute promyelocytic leukemia (APL) contexts where altered RARα signaling blocks granulocytic differentiation and pharmacologic retinoid restores differentiation gene expression. (bercier2024historyofdeveloping pages 4-6, chen2024alltransretinoicacid pages 2-4)

### 6) Recent developments (prioritizing 2023–2024)

#### 6.1 Updated mechanistic view of PML::RARA transcriptional dysregulation (LLPS and BRD4)
A 2024 PNAS study proposes that the APL fusion **PML/RARα** forms **phase-separated condensates (“microspeckles”)** that coassemble **BRD4** and redistribute BRD4 binding to chromatin, with preferential occupancy at **super-enhancers and broad promoters** and transcriptional activation functions supporting APL survival. This extends the classical “corepressor-driven repression” model by adding a condensate-mediated chromatin reprogramming mechanism. (zhang2024phaseseparationof pages 1-2)

#### 6.2 HDAC3 as a mechanistic node in PML-RARα repression and degradation pathways
A 2023 study in *Cell Death & Differentiation* highlighted **HDAC3** as a corepressor component recruited/activated via **NCoR/SMRT**, promoting H3 deacetylation and transcriptional repression, and further showed that HDAC3 **deacetylates PML-RARα at Lys394**, reducing SUMOylation and RNF4-dependent ubiquitylation/degradation; pharmacologic HDAC3 inhibition promoted PML-RARα degradation and differentiation/apoptosis, including in ATRA/arsenic-resistant contexts. (dai2023targetinghdac3to pages 1-2)

#### 6.3 Updated pharmacology and concentration dependence of ATRA responses in APL
A 2024 review in *Frontiers in Pharmacology* emphasized a functional concentration threshold: **physiological ATRA levels (≤90 nmol/L)** may be insufficient to release corepressors from multimerized PML-RARα, while **pharmacological ATRA (~1 μmol/L)** can restore transcription, promote PML-RARα degradation, and induce differentiation; it also summarized strong clinical outcomes for arsenic-trioxide-containing regimens (e.g., ~2-year event-free survival ~98% in standard-risk APL and ~96.4% in high-risk APL, with overall survival ~99–100%). (chen2024alltransretinoicacid pages 2-4)

### 7) Current applications and real-world implementations (function-linked)

**Differentiation therapy in APL (clinical implementation):** RARα’s ligand-regulated transcriptional switch is directly leveraged in APL therapy using retinoids (ATRA) and arsenic trioxide to overcome the differentiation block driven by PML::RARA; modern outcomes summarized in recent sources report very high survival and event-free survival in standard-risk and high-risk groups, consistent with durable clinical implementation. (chen2024alltransretinoicacid pages 2-4, bercier2024historyofdeveloping pages 4-6)

### 8) GO annotation caveats (critical for annotation review)

1. **Response-element dependence (DR1 vs DR2/DR5):** polarity and cofactor recruitment can differ by DR spacing. A DR1 structure shows reversed polarity compared with DR2/DR5-oriented complexes, and DNA spacing can allosterically modulate coactivator recruitment. Annotating downstream BP terms should consider whether evidence derives from DR1-like vs DR5-like contexts. (rastinejad2000structureofthe pages 2-4, bastien2004nuclearretinoidreceptors pages 3-5, mouchon1999allostericregulationof pages 9-10)

2. **Cofactor switch is modular and ligand-selective:** corepressor release can be induced by a RAR ligand without being replicated by an RXR ligand in the same heterodimer context (e.g., AM580-driven SMRT release vs RXR ligand non-effect), so ligand specificity should be captured in interpretations of “activation.” (benko2003moleculardeterminantsof pages 6-8)

3. **Fusion protein evidence vs wild-type RARα:** PML::RARA and other RARA fusions preserve some RARα biochemical properties (DNA binding, retinoid responsiveness) but add fusion-specific multimerization, chromatin targeting, condensate formation, and altered transcriptional programs; these findings are mechanistically informative but should not be transferred wholesale to wild-type RARA GO annotations. (bercier2024historyofdeveloping pages 6-7, zhang2024phaseseparationof pages 1-2)

4. **Indirect vs direct effects in RA-treated systems:** many transcriptomic or phenotypic outcomes in RA-treated cells reflect indirect downstream programs (e.g., differentiation cascades) rather than direct RARα DNA binding; IDA evidence for MF/CC (structure, EMSA, cofactor recruitment assays) is stronger than broad BP assertions unless direct targets are shown. (mouchon1999allostericregulationof pages 2-3, bastien2004nuclearretinoidreceptors pages 3-5)

### 9) GO-relevant evidence summary table

| GO aspect (MF/BP/CC) | Proposed GO concept (plain English label) | Mechanistic description | Key experimental evidence (assay types and key quantitative values where available) | Best supporting citations |
|---|---|---|---|---|
| MF | Retinoic acid receptor activity / retinoid ligand binding | RARα is a ligand-activated nuclear receptor whose LBD binds all-trans retinoic acid and synthetic retinoids; ligand-induced AF-2/H12 repositioning shifts the receptor from corepressor-compatible to coactivator-compatible states. | Quantitative ligand binding and reporter assays for human RARα: Kd (nM) atRA 3.3, 9-cis RA 7.1, TTNPB 2.2, CD367 4.0, Am580 8.1, CD3106 20.0; corresponding reporter EC50s (nM) included atRA 10.8, TTNPB 1.05, CD367 0.91, Am580 0.74. Structural/biochemical studies support ligand-specific AF-2 conformational switching. | (mouchon1999allostericregulationof pages 2-3, mouchon1999allostericregulationof pages 1-2) |
| MF | Sequence-specific DNA binding to RAREs | RARα binds DNA mainly as an RXR heterodimer on retinoic acid response elements composed of direct repeats of PuG(G/T)TCA motifs; recognized spacings include DR1, DR2, and DR5. Orientation is response-element dependent. | Structural and biochemical evidence: 1.7 Å crystal structure of RXR–RAR DBDs on DR1; each DBD recognition helix inserts into the major groove of AGGTCA half-sites. On DR2/DR5, RXR occupies the 5' half-site and RAR the 3' half-site; on DR1, polarity reverses (5'-RAR/RXR-3'). EMSA, crystallography, and DBD mutagenesis support cooperative, sequence-specific binding. | (rastinejad2000structureofthe pages 2-4, bastien2004nuclearretinoidreceptors pages 3-5, zechel1994dimerizationinterfacesformed pages 1-2) |
| MF | RXR heterodimerization | RARα forms functional heterodimers with RXR through DBD- and LBD-mediated interfaces; heterodimerization enhances DNA-binding specificity and transcriptional regulation. | DBD interface mapping showed the RXR D-box is required for cooperative binding on DR4/DR5 and RAR DBD determinants specify RXR/RAR binding on DR5. DR1 crystal structure and biochemical binding showed DNA-dependent heterodimer assembly, with half-maximal DR1 binding at ~300–350 nM for RXR–RAR DBDs and ~10-fold weaker binding for RXR DBD alone to a single site. | (rastinejad2000structureofthe pages 2-4, rastinejad2000structureofthe pages 1-2, zechel1994dimerizationinterfacesformed pages 1-2) |
| MF | Transcriptional repression via NCoR/SMRT/HDAC corepressor complexes | In the unliganded state, DNA-bound RARα recruits NCoR/SMRT corepressors and associated HDAC activity, maintaining retinoid target loci in a repressed chromatin state. | Review-synthesized primary evidence shows unliganded, DNA-bound RAR/RXR complexes recruit NCoR and SMRT linked to HDAC complexes; biochemical assays showed SMRT binding to RAR–RXR complexes and supershift on RARE probes, with release dependent on RAR agonist rather than RXR ligand. In APL mechanistic work, NCOR/SMRT-dependent HDAC3 deacetylates PML-RARα K394, stabilizing repression. | (bastien2004nuclearretinoidreceptors pages 3-5, benko2003moleculardeterminantsof pages 6-8, dai2023targetinghdac3to pages 1-2) |
| MF | Ligand-dependent coactivator recruitment | Upon ligand binding, RARα recruits transcriptional coactivators including p160/SRC family, CBP/p300, and Mediator/DRIP components, promoting RNA polymerase II transcription of retinoid-responsive genes. | GST pull-downs, mammalian two-hybrid, and reporter assays showed ligand-dependent SRC-1/DRIP205 recruitment to RARα or RARα–RXR complexes; DRIP205/TRAP220 recruited to RAR LBD in response to AM580. AM580 EC50s for RARα-dependent activation were ~7 nM for RAR-LBD and 6.7 nM for full-length RAR–RXR, with mutant A392R ~0.9–1.5 nM. DNA spacing altered SRC-1 vs RIP140 recruitment. | (mouchon1999allostericregulationof pages 2-3, mouchon1999allostericregulationof pages 9-10, benko2003moleculardeterminantsof pages 6-8) |
| CC | Nuclear/chromatin-associated transcription factor | RARα is predominantly nuclear, binds response elements in chromatin, and functions within chromatin-associated repressive or activating transcriptional complexes. | Structural/review evidence describes RARs/RXRs as constitutively nuclear; nucleosomes do not prevent RAR/RXR binding. DR1 structural data indicate DNA-dependent assembly; chromatin-associated repression/activation is mediated through HDAC- or HAT-linked complexes. | (bastien2004nuclearretinoidreceptors pages 3-5, lefebvre2001molecularbasisfor pages 2-5) |
| BP | Retinoic acid signaling / regulation of transcription by RNA polymerase II | RARα is a core effector of retinoic acid signaling, transducing ligand binding into activation or repression of RA-responsive transcriptional programs. | Reporter assays with TREpal/RARE elements, GST cofactor-binding assays, and mutational analyses demonstrate ligand-, DNA-, and RXR-dependent transcriptional output. Mechanistic literature consistently places RARα/RXR at the center of RA-responsive gene regulation. | (mouchon1999allostericregulationof pages 2-3, mouchon1999allostericregulationof pages 1-2, bercier2024historyofdeveloping pages 4-6) |
| BP | Myeloid differentiation linked to RA signaling | RARα-mediated transcription contributes to granulocytic/myeloid differentiation; disruption of RARα signaling blocks differentiation, while pharmacologic activation restores it. | Functional evidence summarized in APL-focused reviews: physiological ATRA is insufficient to release corepressor from PML-RARα, but pharmacologic ATRA (~1 µM) restores differentiation gene transcription and induces differentiation. Genetic studies cited in review indicate dominant-negative RARA mutants impair differentiation, whereas altered RARA dosage affects progenitor maturation. | (chen2024alltransretinoicacid pages 2-4, bercier2024historyofdeveloping pages 4-6, powała2024molecularinteractionsof pages 1-2) |
| BP | PML::RARA fusion perturbation relevant to WT RARA function | The PML::RARA fusion preserves RARα DNA-binding/ligand-binding modules but exaggerates oligomerization, corepressor recruitment, and resistance to physiological ligand, thereby illuminating normal RARα repression/activation logic. | APL mechanistic studies/reviews show PML::RARA acts as a dominant-negative RARα, binds DNA via the RARα moiety, dimerizes with RXR, recruits SMRT/NCOR/HDAC complexes, and requires pharmacologic ATRA for derepression. Recent work adds HDAC3-controlled acetylation/SUMO-ubiquitin turnover and BRD4-containing phase-separated condensates at super-enhancers/broad promoters. | (dai2023targetinghdac3to pages 1-2, bercier2024historyofdeveloping pages 6-7, zhang2024phaseseparationof pages 1-2) |
| BP/CC caveat | Response-element dependence (DR1 vs DR2/DR5) | RARα output is not uniform across all RAREs; spacing and polarity alter receptor orientation, cofactor recruitment, and whether liganding produces activation or persistent repression. | DR1 crystal structure and biochemical models show reversed polarity on DR1 versus DR2/DR5; DNA spacing allosterically changes SRC-1/RIP140 recruitment and can favor repression versus activation depending on element context. | (rastinejad2000structureofthe pages 2-4, bastien2004nuclearretinoidreceptors pages 3-5, mouchon1999allostericregulationof pages 9-10) |
| Annotation caveat | Cell-type specificity and indirect RA-response effects | Many RA-treatment transcriptomic changes are indirect or cell-context dependent; GO curation should distinguish direct RARα DNA-bound mechanisms from downstream differentiation phenotypes. | Evidence base includes purified-protein structural studies, transfection/reporter assays, and disease models; these support direct MF/CC annotations more strongly than broad BP claims in every cell type. Reviews note AF-1/cellular context dependence and variable ligand/cofactor responses across systems. | (lefebvre2001molecularbasisfor pages 2-5, mouchon1999allostericregulationof pages 1-2, powała2024molecularinteractionsof pages 1-2) |
| Annotation caveat | Fusion protein evidence should not be transferred wholesale to WT RARA | PML::RARA data are mechanistically informative for corepressor recruitment, ligand response thresholds, and chromatin regulation, but fusion-specific behaviors (multimerization, microspeckles, altered target spectrum) are not equivalent to wild-type RARα biology. | APL literature shows fusion-specific dominant-negative behavior, altered degradation pathways, and BRD4 phase-separated condensates; these should support cautionary notes or separate annotations rather than direct WT functional transfer. | (dai2023targetinghdac3to pages 1-2, bercier2024historyofdeveloping pages 6-7, zhang2024phaseseparationof pages 1-2) |


*Table: This table summarizes GO-relevant molecular functions, processes, cellular locations, and annotation caveats for human RARA using direct mechanistic evidence and recent function-relevant literature. It is designed to help reviewers separate strong wild-type RARA evidence from response-element-, context-, and fusion-specific effects.*

### 10) Key cited sources (with URLs/DOIs and publication dates where available)

- Rastinejad F. *et al.* **Structure of the RXR–RAR DNA-binding complex on the retinoic acid response element DR1**. *The EMBO Journal* (Mar 2000). DOI: https://doi.org/10.1093/emboj/19.5.1045 (rastinejad2000structureofthe pages 2-4, rastinejad2000structureofthe media 89fe3bd5)
- Mouchon A. *et al.* **Allosteric regulation… by RXR and DNA**. *Molecular and Cellular Biology* (Apr 1999). DOI: https://doi.org/10.1128/mcb.19.4.3073 (mouchon1999allostericregulationof pages 2-3)
- Zechel C. *et al.* **DBD dimerization interfaces determine cooperative binding… to DR5/DR4**. *The EMBO Journal* (Mar 1994). DOI: https://doi.org/10.1002/j.1460-2075.1994.tb06395.x (zechel1994dimerizationinterfacesformed pages 1-2)
- Bastien J., Rochette-Egly C. **Nuclear retinoid receptors and transcription of retinoid-target genes**. *Gene* (Mar 2004). DOI: https://doi.org/10.1016/j.gene.2003.12.005 (bastien2004nuclearretinoidreceptors pages 3-5)
- Dai B. *et al.* **Targeting HDAC3 to overcome resistance… via degradation of PML-RARα**. *Cell Death & Differentiation* (Mar 2023). DOI: https://doi.org/10.1038/s41418-023-01139-8 (dai2023targetinghdac3to pages 1-2)
- Zhang Y. *et al.* **Phase separation of PML/RARα and BRD4…** *PNAS* (Aug 2024). DOI: https://doi.org/10.1073/pnas.2406519121 (zhang2024phaseseparationof pages 1-2)
- Chen Y. *et al.* **All-trans retinoic acid in hematologic disorders…** *Frontiers in Pharmacology* (Jul 2024). DOI: https://doi.org/10.3389/fphar.2024.1404092 (chen2024alltransretinoicacid pages 2-4)
- Bercier P., de Thé H. **History of developing APL treatment…** *Cancers* (Mar 2024). DOI: https://doi.org/10.3390/cancers16071351 (bercier2024historyofdeveloping pages 4-6)


References

1. (bastien2004nuclearretinoidreceptors pages 3-5): Julie Bastien and Cécile Rochette-Egly. Nuclear retinoid receptors and the transcription of retinoid-target genes. Gene, 328:1-16, Mar 2004. URL: https://doi.org/10.1016/j.gene.2003.12.005, doi:10.1016/j.gene.2003.12.005. This article has 1016 citations and is from a peer-reviewed journal.

2. (mouchon1999allostericregulationof pages 1-2): Arnaud Mouchon, Marie-Hélène Delmotte, Pierre Formstecher, and Philippe Lefebvre. Allosteric regulation of the discriminative responsiveness of retinoic acid receptor to natural and synthetic ligands by retinoid x receptor and dna. Molecular and Cellular Biology, 19:3073-3085, Apr 1999. URL: https://doi.org/10.1128/mcb.19.4.3073, doi:10.1128/mcb.19.4.3073. This article has 49 citations and is from a domain leading peer-reviewed journal.

3. (zechel2002syntheticretinoidsdissociate pages 3-4): Christina Zechel. Synthetic retinoids dissociate coactivator binding from corepressor release. Journal of Receptors and Signal Transduction, 22:31-61, Jan 2002. URL: https://doi.org/10.1081/rrs-120014587, doi:10.1081/rrs-120014587. This article has 14 citations and is from a peer-reviewed journal.

4. (mouchon1999allostericregulationof pages 2-3): Arnaud Mouchon, Marie-Hélène Delmotte, Pierre Formstecher, and Philippe Lefebvre. Allosteric regulation of the discriminative responsiveness of retinoic acid receptor to natural and synthetic ligands by retinoid x receptor and dna. Molecular and Cellular Biology, 19:3073-3085, Apr 1999. URL: https://doi.org/10.1128/mcb.19.4.3073, doi:10.1128/mcb.19.4.3073. This article has 49 citations and is from a domain leading peer-reviewed journal.

5. (mouchon1999allostericregulationof pages 9-10): Arnaud Mouchon, Marie-Hélène Delmotte, Pierre Formstecher, and Philippe Lefebvre. Allosteric regulation of the discriminative responsiveness of retinoic acid receptor to natural and synthetic ligands by retinoid x receptor and dna. Molecular and Cellular Biology, 19:3073-3085, Apr 1999. URL: https://doi.org/10.1128/mcb.19.4.3073, doi:10.1128/mcb.19.4.3073. This article has 49 citations and is from a domain leading peer-reviewed journal.

6. (rastinejad2000structureofthe pages 2-4): Fraydoon Rastinejad, Trixie Wagner, Qiang Zhao, and Sepideh Khorasanizadeh. Structure of the rxr–rar dna‐binding complex on the retinoic acid response element dr1. The EMBO Journal, 19:1045-1054, Mar 2000. URL: https://doi.org/10.1093/emboj/19.5.1045, doi:10.1093/emboj/19.5.1045. This article has 282 citations.

7. (rastinejad2000structureofthe pages 1-2): Fraydoon Rastinejad, Trixie Wagner, Qiang Zhao, and Sepideh Khorasanizadeh. Structure of the rxr–rar dna‐binding complex on the retinoic acid response element dr1. The EMBO Journal, 19:1045-1054, Mar 2000. URL: https://doi.org/10.1093/emboj/19.5.1045, doi:10.1093/emboj/19.5.1045. This article has 282 citations.

8. (zechel1994dimerizationinterfacesformed pages 1-2): Christina Zechel, Xi-Qiang Shen, P. Chambon, and Hinrich Gronemeyerl. Dimerization interfaces formed between the dna binding domains determine the cooperative binding of rxr/rar and rxr/tr heterodimers to dr5 and dr4 elements. The EMBO Journal, 13:1414-1424, Mar 1994. URL: https://doi.org/10.1002/j.1460-2075.1994.tb06395.x, doi:10.1002/j.1460-2075.1994.tb06395.x. This article has 282 citations.

9. (benko2003moleculardeterminantsof pages 6-8): Szilvia Benko, James D. Love, Marta Beládi, John W.R. Schwabe, and Laszlo Nagy. Molecular determinants of the balance between co-repressor and co-activator recruitment to the retinoic acid receptor*. Journal of Biological Chemistry, 278:43797-43806, Oct 2003. URL: https://doi.org/10.1074/jbc.m306199200, doi:10.1074/jbc.m306199200. This article has 47 citations and is from a domain leading peer-reviewed journal.

10. (lefebvre2001molecularbasisfor pages 2-5): P. Lefebvre. Molecular basis for designing selective modulators of retinoic acid receptor transcriptional activities. Aug 2001. URL: https://doi.org/10.2174/1568008013341389, doi:10.2174/1568008013341389. This article has 38 citations.

11. (rastinejad2000structureofthe media 89fe3bd5): Fraydoon Rastinejad, Trixie Wagner, Qiang Zhao, and Sepideh Khorasanizadeh. Structure of the rxr–rar dna‐binding complex on the retinoic acid response element dr1. The EMBO Journal, 19:1045-1054, Mar 2000. URL: https://doi.org/10.1093/emboj/19.5.1045, doi:10.1093/emboj/19.5.1045. This article has 282 citations.

12. (bercier2024historyofdeveloping pages 4-6): Pierre Bercier and Hugues de Thé. History of developing acute promyelocytic leukemia treatment and role of promyelocytic leukemia bodies. Cancers, 16:1351, Mar 2024. URL: https://doi.org/10.3390/cancers16071351, doi:10.3390/cancers16071351. This article has 11 citations.

13. (chen2024alltransretinoicacid pages 2-4): Yan Chen, Xia Tong, Rongyuan Lu, Zhengfu Zhang, and Tao Ma. All-trans retinoic acid in hematologic disorders: not just acute promyelocytic leukemia. Frontiers in Pharmacology, Jul 2024. URL: https://doi.org/10.3389/fphar.2024.1404092, doi:10.3389/fphar.2024.1404092. This article has 28 citations.

14. (zhang2024phaseseparationof pages 1-2): Yi Zhang, Jiacheng Lou, Yabin Liu, Peng Jin, Yun Tan, Huan Song, Wen Jin, Dan Wang, Fangyi Dong, Shishuang Wu, Hai Fang, Saijuan Chen, Zhu Chen, and Kankan Wang. Phase separation of pml/rarα and brd4 coassembled microspeckles governs transcriptional dysregulation in acute promyelocytic leukemia. Proceedings of the National Academy of Sciences of the United States of America, Aug 2024. URL: https://doi.org/10.1073/pnas.2406519121, doi:10.1073/pnas.2406519121. This article has 15 citations and is from a highest quality peer-reviewed journal.

15. (dai2023targetinghdac3to pages 1-2): Bo Dai, Feng Wang, Ying Wang, Jiayan Zhu, Yunxuan Li, Tingting Zhang, Lu Zhao, Li-Ling Wang, Wen-hui Gao, Jun Yu Li, A. Liang, Hongming Zhu, Ke Li, and Jiong Hu. Targeting hdac3 to overcome the resistance to atra or arsenic in acute promyelocytic leukemia through ubiquitination and degradation of pml-rarα. Cell Death & Differentiation, 30:1320-1333, Mar 2023. URL: https://doi.org/10.1038/s41418-023-01139-8, doi:10.1038/s41418-023-01139-8. This article has 33 citations and is from a domain leading peer-reviewed journal.

16. (bercier2024historyofdeveloping pages 6-7): Pierre Bercier and Hugues de Thé. History of developing acute promyelocytic leukemia treatment and role of promyelocytic leukemia bodies. Cancers, 16:1351, Mar 2024. URL: https://doi.org/10.3390/cancers16071351, doi:10.3390/cancers16071351. This article has 11 citations.

17. (powała2024molecularinteractionsof pages 1-2): Katarzyna Powała, Teresa Żołek, Geoffrey Brown, and Andrzej Kutner. Molecular interactions of selective agonists and antagonists with the retinoic acid receptor γ. International Journal of Molecular Sciences, 25:6568, Jun 2024. URL: https://doi.org/10.3390/ijms25126568, doi:10.3390/ijms25126568. This article has 9 citations.

## Citations

1. bastien2004nuclearretinoidreceptors pages 3-5
2. mouchon1999allostericregulationof pages 2-3
3. rastinejad2000structureofthe pages 2-4
4. zechel1994dimerizationinterfacesformed pages 1-2
5. mouchon1999allostericregulationof pages 9-10
6. benko2003moleculardeterminantsof pages 6-8
7. zhang2024phaseseparationof pages 1-2
8. chen2024alltransretinoicacid pages 2-4
9. bercier2024historyofdeveloping pages 4-6
10. mouchon1999allostericregulationof pages 1-2
11. zechel2002syntheticretinoidsdissociate pages 3-4
12. rastinejad2000structureofthe pages 1-2
13. lefebvre2001molecularbasisfor pages 2-5
14. bercier2024historyofdeveloping pages 6-7
15. https://doi.org/10.1093/emboj/19.5.1045
16. https://doi.org/10.1128/mcb.19.4.3073
17. https://doi.org/10.1002/j.1460-2075.1994.tb06395.x
18. https://doi.org/10.1016/j.gene.2003.12.005
19. https://doi.org/10.1038/s41418-023-01139-8
20. https://doi.org/10.1073/pnas.2406519121
21. https://doi.org/10.3389/fphar.2024.1404092
22. https://doi.org/10.3390/cancers16071351
23. https://doi.org/10.1016/j.gene.2003.12.005,
24. https://doi.org/10.1128/mcb.19.4.3073,
25. https://doi.org/10.1081/rrs-120014587,
26. https://doi.org/10.1093/emboj/19.5.1045,
27. https://doi.org/10.1002/j.1460-2075.1994.tb06395.x,
28. https://doi.org/10.1074/jbc.m306199200,
29. https://doi.org/10.2174/1568008013341389,
30. https://doi.org/10.3390/cancers16071351,
31. https://doi.org/10.3389/fphar.2024.1404092,
32. https://doi.org/10.1073/pnas.2406519121,
33. https://doi.org/10.1038/s41418-023-01139-8,
34. https://doi.org/10.3390/ijms25126568,