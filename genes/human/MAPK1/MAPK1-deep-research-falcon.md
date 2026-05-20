---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T21:28:55.391359'
end_time: '2026-05-12T21:47:01.793924'
duration_seconds: 1086.4
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

Concise GO annotation research for human MAPK1 / UniProt P28482 (mitogen-activated protein kinase 1, ERK2). Focus only on GO-relevant evidence: core molecular function as a serine/threonine protein kinase/MAP kinase with ATP binding and phosphotransfer activity; activation by dual phosphorylation by MEK1/2; core roles in MAPK cascade, ERK1/ERK2 cascade, intracellular signal transduction, response to growth factors; nuclear/cytoplasmic localization and stimulus-dependent nuclear translocation; substrates and downstream processes including transcription factor phosphorylation, cell proliferation/differentiation, apoptosis/senescence, cell migration, and whether these should be core or non-core; scaffold/protein binding annotations; over-annotation risks for generic protein binding, broad development/cancer/cell cycle/transcription terms, high-throughput substrate claims, and phenotypes from inhibitor/overexpression studies. Include caveats distinguishing direct MAPK1 kinase activity from downstream pathway outcomes. Include PMID/DOI citations and keep under 1500 words.

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

Concise GO annotation research for human MAPK1 / UniProt P28482 (mitogen-activated protein kinase 1, ERK2). Focus only on GO-relevant evidence: core molecular function as a serine/threonine protein kinase/MAP kinase with ATP binding and phosphotransfer activity; activation by dual phosphorylation by MEK1/2; core roles in MAPK cascade, ERK1/ERK2 cascade, intracellular signal transduction, response to growth factors; nuclear/cytoplasmic localization and stimulus-dependent nuclear translocation; substrates and downstream processes including transcription factor phosphorylation, cell proliferation/differentiation, apoptosis/senescence, cell migration, and whether these should be core or non-core; scaffold/protein binding annotations; over-annotation risks for generic protein binding, broad development/cancer/cell cycle/transcription terms, high-throughput substrate claims, and phenotypes from inhibitor/overexpression studies. Include caveats distinguishing direct MAPK1 kinase activity from downstream pathway outcomes. Include PMID/DOI citations and keep under 1500 words.

## Concise GO annotation research report: human MAPK1 / ERK2 (UniProt P28482)

### Scope and principles (GO-relevant evidence only)
MAPK1 (ERK2) is best annotated in GO by (i) conserved biochemical activity (ATP-dependent, proline-directed Ser/Thr protein kinase), (ii) conserved activation mechanism (MEK1/2 dual phosphorylation of the activation loop), (iii) conserved pathway placement (MAPK/ERK cascade downstream of Ras–Raf–MEK), (iv) experimentally supported subcellular distribution (cytoplasm↔nucleus shuttling with stimulus-dependent nuclear accumulation), and (v) motif/exosite-mediated docking interactions that govern partner binding and spatial regulation. Downstream phenotypes (proliferation, differentiation, apoptosis, senescence, migration) are frequently ERK-pathway outcomes and are high risk for over-annotation unless direct MAPK1-specific causality is demonstrated. (novak2023mutationinthe pages 1-2, karlsson2006spatiotemporalregulationof pages 1-2, caunt2010stimulusinduceduncouplingof pages 1-2)

### 1) Key concepts and definitions (current understanding)

#### 1.1 Core Molecular Function (MF)
**Protein serine/threonine kinase activity (MAP kinase) + ATP binding.** ERK2 is a Ser/Thr MAPK that transfers the γ-phosphate of ATP to Ser/Thr-Pro motifs; like other protein kinases it binds ATP in an active-site cleft, with MgATP2− serving as the relevant phosphoryl donor in vitro. (rainey2004astructurefunctionanalysis pages 20-24, rainey2004astructurefunctionanalysis pages 24-29, waas2003physiologicalconcentrationsof pages 1-2)

**Mechanistic detail useful for MF curation.** Structural/biophysical descriptions emphasize ATP binding by the N-lobe (β strands and glycine-rich loop) and ATP/substrate engagement by both lobes; this supports annotating “ATP binding” and “protein serine/threonine kinase activity” as core MF terms. (novak2023mutationinthe pages 1-2)

**Data/quantitative note.** Dual phosphorylation causes an extremely large increase in catalytic efficiency (reported as ~600,000-fold in one mechanistic source), emphasizing that “active ERK2 kinase activity” is conditional on upstream activation. (rainey2004astructurefunctionanalysis pages 24-29)

#### 1.2 Activation mechanism (upstream regulation)
**Dual phosphorylation by MEK1/2.** ERK activation requires phosphorylation on one threonine and one tyrosine in the activation loop by the dual-specificity kinase MEK (MAPKK/ERK kinase). This is described in biochemical/structural terms and is central to GO BP annotation for MAPK cascade. (butch1996characterizationoferk1 pages 1-2, novak2023mutationinthe pages 1-2)

**Site mapping (ERK2).** Recent ERK2-focused biochemical work explicitly identifies the ERK2 activation loop residues as Thr185 and Tyr187 (ERK1: Thr202/Tyr204), phosphorylated by MEK1/2. (novak2023mutationinthe pages 1-2)

**Specificity note (curation relevance).** MEK is described as highly specific for ERK (“only known substrate for MEK” in the cited source), supporting a conservative upstream relationship (MAPKK→MAPK) rather than broad “protein kinase regulator activity” claims. (butch1996characterizationoferk1 pages 1-2)

### 2) Core Biological Process (BP) annotations (conservative, evidence-driven)

#### 2.1 MAPK cascade / ERK1-ERK2 cascade / intracellular signal transduction
ERK2 is consistently positioned as a downstream effector in the Ras–Raf–MEK–ERK signal transduction cascade, converting extracellular cues (including growth factors/serum) into intracellular phosphorylation events and responses. (novak2023mutationinthe pages 1-2, rainey2004astructurefunctionanalysis pages 20-24, waas2003physiologicalconcentrationsof pages 1-2)

**GO-relevant framing:** annotate ERK2 to **MAPK cascade / ERK1 and ERK2 cascade** and **intracellular signal transduction**; optionally include **response to growth factor** where the evidence is directly about upstream stimuli triggering ERK activation/translocation rather than downstream phenotypes. (waas2003physiologicalconcentrationsof pages 1-2, karlsson2006spatiotemporalregulationof pages 1-2)

#### 2.2 Downstream outcomes: core vs non-core
Many sources link ERK signaling to proliferation/differentiation and disease contexts, but these are typically emergent outcomes of the pathway rather than direct MAPK1 enzymatic functions. For example, ERK signaling is described as converting stimuli into proliferation/differentiation and being implicated in oncogenic transformation when deregulated. These statements support pathway-level BP terms, but **do not automatically justify** GO terms like “cell cycle,” “transcription,” “cancer,” or broad developmental processes as core MAPK1 BPs. (novak2023mutationinthe pages 1-2, butch1996characterizationoferk1 pages 1-2)

### 3) Cellular Component (CC): localization and stimulus-dependent translocation

#### 3.1 Basal distribution and stimulus-dependent nuclear accumulation
ERK is predominantly cytoplasmic in quiescent cells and accumulates in the nucleus after activation by certain stimuli; nuclear ERK phosphorylates nuclear targets and contributes to induced gene expression programs. (karlsson2006spatiotemporalregulationof pages 1-2)

#### 3.2 ERK lacks obvious intrinsic NLS/NES → partner-mediated trafficking
ERK lacks obvious intrinsic NLS/NES elements, implying nuclear-cytoplasmic trafficking depends on binding partners that carry localization motifs (e.g., MEK, DUSPs, scaffolds). (karlsson2006spatiotemporalregulationof pages 1-2, caunt2006seventransmembranereceptorsignalling pages 2-3, caunt2010stimulusinduceduncouplingof pages 1-2)

#### 3.3 Cytoplasmic anchoring and nuclear sequestration (directly relevant regulators)
- **MEK as cytoplasmic anchor:** MEK contains a leucine-rich NES and an ERK-binding site that anchors inactive ERK in the cytoplasm; activation dissociates the MEK–ERK complex and enables ERK nuclear translocation. (karlsson2006spatiotemporalregulationof pages 1-2, karlsson2006spatiotemporalregulationof pages 2-3)
- **DUSP6/MKP-3 as cytoplasmic tether:** MKP-3/DUSP6 binds ERK2 and can dephosphorylate and tether inactive ERK2 in the cytoplasm; mutating MKP-3 NES or KIM abolishes cytoplasmic anchoring. (karlsson2006spatiotemporalregulationof pages 2-3, karlsson2006spatiotemporalregulationof pages 1-2)
- **DUSP5 as nuclear sequestration factor:** DUSP5 contains an NLS; co-expression experiments show DUSP5 can inactivate and sequester ERK2 in the nucleus in an NLS- and KIM-dependent manner. (karlsson2006spatiotemporalregulationof pages 2-3)

#### 3.4 Docking-domain dependence of nuclear localization (caution)
Stimulus-induced nuclear localization is **not always proportional** to TEY phosphorylation; a phosphorylation-independent component of nuclear accumulation can depend on D-domain docking interactions (e.g., reduced by ERK2 D319N affecting the D-domain binding interface). This supports annotating “stimulus-dependent nuclear translocation” cautiously and discourages inferring nuclear localization solely from phospho-ERK immunoblot signals. (caunt2010stimulusinduceduncouplingof pages 1-2, caunt2010stimulusinduceduncouplingof pages 2-3)

### 4) Protein binding / scaffold & docking annotations (avoid generic binding)

#### 4.1 Motif/exosite-mediated docking is central to ERK specificity
ERK docking is mediated by defined motifs and complementary exosites: D-domains/KIMs and DEF/FXFP motifs on partners bind ERK CD/FRS-related surfaces and other exosites. Biochemical peptide-competition experiments show docking-site peptides from MEK/MKPs/Elk-1 can inhibit MEK2–ERK2 binding and ERK2 phosphorylation of Elk-1-like substrates, indicating docking interactions are crucial for enzymatic function. (bardwell2003dockingsiteson pages 5-6, rainey2004astructurefunctionanalysis pages 24-29)

#### 4.2 Avoid over-annotation to “protein binding”
Because docking is motif-driven and structurally/biochemically dissectable, using only “protein binding” is typically uninformative and risks over-annotation. Additionally, yeast two-hybrid and peptide-based assays may capture indirect interactions or partial interfaces, so direct “binding” annotations should be limited to partners with orthogonal support. (rainey2004astructurefunctionanalysis pages 29-33, rainey2004astructurefunctionanalysis pages 24-29)

### 5) Substrates and downstream processes: direct vs indirect; 2023–2024 developments

#### 5.1 Direct phosphorylation: what is strong enough for GO use?
**Strongest direct evidence** comes from direct biochemical phosphorylation assays and/or site-level validation. Examples in the evidence set include:
- ERK2 phosphorylation of an ETS-derived substrate (EtsΔ138) at Thr-38 in vitro (example of direct Ser/Thr-Pro phosphorylation). (waas2003physiologicalconcentrationsof pages 1-2)
- ERK2 phosphorylation of Elk-1–derived peptide/protein substrates in vitro assays using purified, dually phosphorylated ERK2. (bardwell2003dockingsiteson pages 5-6)

A later review compiles additional site-level candidates (e.g., PKM2 Ser37; PAK1 Thr212; PFAS Thr619) but also notes that some are based on global phosphoproteomics and context-dependent signaling; these are useful for hypothesis generation but should not all be elevated to “direct substrate” GO annotations without independent validation. (martin–vega2025erk12mapksignalingmetabolic pages 3-5)

#### 5.2 2024 mechanistic advance: kinase-independent ERK2 function via direct binding
A major 2024 development relevant to GO curation is **direct structural and functional evidence** for an ERK2 binding interaction that regulates a process **independently of ERK kinase activity**. Becker et al. (Cell Reports, 2024-10; DOI:10.1016/j.celrep.2024.114831; URL: https://doi.org/10.1016/j.celrep.2024.114831) report a cryo-EM DHPS–ERK2 complex in which ERK2 physically occludes access to the DHPS active site, inhibiting deoxyhypusination in vitro, and show the interaction can be regulated by ERK2 regions outside the catalytic site (including an ERK2 Ser-Pro-Ser motif). This supports a careful “protein binding”/complex annotation for a specific partner (DHPS) and highlights that not all ERK2-associated biological outcomes are mediated by phosphorylation. (becker2024erk12interactionwith pages 1-3, becker2024erk12interactionwith media 4b826433, becker2024erk12interactionwith media dca6815c)

#### 5.3 Processes like proliferation/migration/apoptosis/senescence: typically non-core for MAPK1
While ERK pathway activity is frequently associated with proliferation, differentiation, apoptosis/senescence, and migration, these are often downstream, cell-type- and stimulus-dependent outcomes mediated by networks of effectors and feedback loops. GO BP annotation for MAPK1 should therefore prioritize **cascade membership and signal transduction**, and use downstream process terms only when MAPK1-specific, direct mechanistic links (not only inhibitor/overexpression phenotypes) are demonstrated. (novak2023mutationinthe pages 1-2, caunt2010stimulusinduceduncouplingof pages 1-2, martin–vega2025erk12mapksignalingmetabolic pages 3-5)

### 6) Current applications and real-world implementations (annotation-relevant)
ERK pathway components are major drug targets; however, therapeutic studies primarily inform **pathway perturbation phenotypes** rather than MAPK1 core GO functions. In a 2024 cardiovascular-focused review, ERK dimerization/autophosphorylation and nuclear shuttling mechanisms are discussed alongside peptide tools that perturb ERK dimerization or ERK–Importin7 interaction, illustrating how localization/complex formation is a practical intervention axis. These are useful as mechanistic context for CC annotations (nuclear translocation) but should not be used to assert broad disease-process GO terms for MAPK1. (mohammed2024mekinhibitorsa pages 2-3)

### 7) Recommended conservative GO annotation set (with over-annotation warnings)
The table below summarizes the most defensible GO scope from the evidence.

| GO aspect | Recommended core GO term(s) | Evidence type | Key supporting statements | Key citation IDs | Over-annotation caveat |
|---|---|---|---|---|---|
| MF | protein serine/threonine kinase activity; mitogen-activated protein kinase activity; ATP binding | direct biochemical | ERK2 is a Ser/Thr MAPK that transfers phosphate from ATP/MgATP to Ser/Thr-Pro motifs; ATP binds in the active site, with N-lobe/glycine-rich loop contributions to nucleotide binding and catalysis. | (rainey2004astructurefunctionanalysis pages 20-24, rainey2004astructurefunctionanalysis pages 24-29, waas2003physiologicalconcentrationsof pages 1-2, novak2023mutationinthe pages 1-2) | Do not infer tyrosine kinase activity, broad “catalytic activity,” or substrate-level specificity beyond supported proline-directed Ser/Thr phosphorylation. |
| MF | MAP kinase kinase activity toward protein substrates | direct biochemical | Catalytic efficiency rises dramatically after dual phosphorylation; purified dually phosphorylated ERK2 phosphorylates peptide/protein substrates, including Elk-1-derived peptides and ETS/Runx-related transcription factor substrates in biochemical assays. | (rainey2004astructurefunctionanalysis pages 24-29, bardwell2003dockingsiteson pages 5-6, waas2003physiologicalconcentrationsof pages 1-2) | Do not treat every phosphoproteomics hit or motif-containing protein as a direct MAPK1 substrate. |
| BP | ERK1 and ERK2 cascade; MAPK cascade; intracellular signal transduction; response to growth factor | review/mechanistic plus direct pathway evidence | ERK2 is a principal effector downstream of Ras-Raf-MEK; activated by extracellular stimuli including serum/growth factors and mediates canonical MAPK/ERK signaling. | (novak2023mutationinthe pages 1-2, waas2003physiologicalconcentrationsof pages 1-2, rainey2004astructurefunctionanalysis pages 20-24) | Keep pathway terms close to the conserved cascade; avoid annotating broad disease, cancer, development, or generic transcription terms from pathway membership alone. |
| BP | positive regulation of protein phosphorylation of direct substrates; phosphorylation of transcription factors | direct biochemical | ERK2 directly phosphorylates defined downstream targets such as Elk-1/ETS-family and other transcription-factor substrates in vitro and in cells; docking motifs/exosites help determine substrate recognition. | (bardwell2003dockingsiteson pages 5-6, waas2003physiologicalconcentrationsof pages 1-2, rainey2004astructurefunctionanalysis pages 24-29) | Direct substrate phosphorylation can support narrower process terms only when the substrate/process link is demonstrated; do not infer all downstream transcriptional programs as direct MAPK1 functions. |
| BP | regulation of cell proliferation/differentiation; apoptosis/senescence; cell migration | review/mechanistic, usually non-core | Literature links ERK2 signaling to proliferation, differentiation, survival/death decisions, and motility, often through many downstream effectors and context-specific scaffolds. | (novak2023mutationinthe pages 1-2, martin–vega2025erk12mapksignalingmetabolic pages 3-5, butch1996characterizationoferk1 pages 1-2) | These are often pathway outcomes, not direct MAPK1 actions; avoid making them core GO annotations unless supported by direct loss-of-function/rescue and mechanistic evidence specific to MAPK1. |
| CC | cytoplasm; nucleus | cell biology localization | In quiescent cells ERK is mainly cytoplasmic; after activation it accumulates in the nucleus. ERK lacks clear intrinsic NLS/NES and relies on partner-mediated trafficking. | (karlsson2006spatiotemporalregulationof pages 1-2, caunt2006seventransmembranereceptorsignalling pages 2-3, caunt2010stimulusinduceduncouplingof pages 1-2, caunt2010stimulusinduceduncouplingof pages 2-3) | Prefer cytoplasm/nucleus over highly specific compartments unless direct localization evidence exists for MAPK1 itself in that context. |
| CC | cytoplasm to nucleus translocation upon stimulation | cell biology localization | MEK binds inactive ERK in the cytoplasm; TEY phosphorylation and release from anchors permit nuclear accumulation. Nuclear localization depends on phosphorylation but can also require D-domain interactions beyond phosphorylation alone. | (karlsson2006spatiotemporalregulationof pages 1-2, caunt2010stimulusinduceduncouplingof pages 1-2, caunt2010stimulusinduceduncouplingof pages 2-3) | Do not annotate constitutive nuclear localization; stimulus dependence matters, and nuclear entry should not be inferred solely from ERK phosphorylation readouts. |
| CC | cytoplasmic anchoring complex with MEK/DUSP6-like regulators; nuclear sequestration with DUSP5-like regulators | cell biology localization; review/mechanistic | MEK NES helps anchor inactive ERK in cytoplasm; DUSP6/MKP-3 tethers inactive ERK2 in cytoplasm; DUSP5 contains an NLS and can inactivate/sequester ERK2 in the nucleus. | (karlsson2006spatiotemporalregulationof pages 2-3, karlsson2006spatiotemporalregulationof pages 1-2, caunt2010stimulusinduceduncouplingof pages 11-11) | These support localization regulation and specific complexes, not broad stable residence in every compartment or all phosphatase-binding annotations. |
| MF | sequence-specific protein docking / scaffold-mediated binding | direct biochemical; review/mechanistic | ERK2 recognizes D-domain/KIM and DEF/FXFP docking motifs through common-docking and exosite regions; these interactions are crucial for MEK, MKP, Elk-1 and scaffold/substrate binding. | (rainey2004astructurefunctionanalysis pages 24-29, bardwell2003dockingsiteson pages 5-6, rainey2004astructurefunctionanalysis pages 29-33) | Avoid generic “protein binding” if a more informative docking/scaffold interaction term can be used; also avoid inferring direct binding from yeast two-hybrid or peptide competition alone without orthogonal support. |
| BP | scaffold-mediated spatial regulation of MAPK signaling | review/mechanistic | Scaffold and anchoring proteins such as β-arrestin, Naf1, paxillin/GIT1/IQGAP1/KSR1 shape where ERK signals and which outputs are engaged. | (rainey2004astructurefunctionanalysis pages 29-33, martin–vega2025erk12mapksignalingmetabolic pages 3-5) | Scaffold-dependent localization does not automatically justify annotating MAPK1 to every scaffold’s biological process or cellular site. |
| BP | nuclear transcription factor phosphorylation leading to gene expression changes | direct substrate plus mechanistic | ERK nuclear translocation enables phosphorylation of nuclear substrates such as Elk-1 and related transcription factors that contribute to induced gene expression. | (caunt2006seventransmembranereceptorsignalling pages 2-3, bardwell2003dockingsiteson pages 5-6, butch1996characterizationoferk1 pages 1-2) | Annotate the direct phosphorylation event or upstream signaling role rather than broad “regulation of transcription” unless MAPK1-specific causality is directly established. |
| General guidance | core set should emphasize kinase activity, MEK-dependent activation, MAPK/ERK cascade role, intracellular signaling, and cytoplasm/nucleus shuttling | synthesis | Best-supported core annotations are those nearest to direct chemistry, canonical pathway position, and experimentally observed localization dynamics. | (novak2023mutationinthe pages 1-2, karlsson2006spatiotemporalregulationof pages 1-2, caunt2010stimulusinduceduncouplingof pages 1-2) | Be cautious with inhibitor/overexpression phenotypes, cancer-context reviews, and high-throughput substrate claims; distinguish direct MAPK1 action from downstream pathway outcomes. |


*Table: This table summarizes GO-relevant evidence and annotation boundaries for human MAPK1/ERK2 using only the provided evidence contexts. It highlights the strongest core annotations and flags common over-annotation risks for downstream phenotypes, generic binding, and indirect pathway outcomes.*

### Key caveats for curators (high priority)
1. **Do not infer “nuclear” localization from phospho-ERK alone.** Nuclear accumulation can be partially uncoupled from TEY phosphorylation and depends on docking interactions and anchors. (caunt2010stimulusinduceduncouplingof pages 1-2, caunt2010stimulusinduceduncouplingof pages 2-3)
2. **Avoid broad BP terms (cancer, development, cell cycle, transcription) from pathway membership.** Prefer “MAPK/ERK cascade” and “intracellular signal transduction,” and only add downstream BPs with direct MAPK1 evidence. (novak2023mutationinthe pages 1-2, butch1996characterizationoferk1 pages 1-2)
3. **Be conservative with high-throughput substrate claims.** Motif presence is insufficient; only a minority of Ser/Thr-Pro sites are bona fide MAPK substrates in vivo, and phosphoproteomics hits need orthogonal validation. (rainey2004astructurefunctionanalysis pages 24-29, martin–vega2025erk12mapksignalingmetabolic pages 3-5)
4. **Use specific docking/scaffold language rather than generic binding when possible.** Docking is mediated by defined motifs (KIM/D-domain, DEF/FXFP) and ERK exosites; peptide/yeast assays can be indirect. (bardwell2003dockingsiteson pages 5-6, rainey2004astructurefunctionanalysis pages 29-33)
5. **Distinguish kinase-dependent vs kinase-independent ERK functions.** The DHPS–ERK2 interaction demonstrates direct binding-mediated regulation independent of ERK catalytic activity, warning against attributing every ERK-associated outcome to “protein phosphorylation.” (becker2024erk12interactionwith pages 1-3, becker2024erk12interactionwith media 4b826433)

### References (URLs, dates, identifiers)
- Novak L. et al. *Cancers* (2023-05). “Mutation in the Common Docking Domain Affects MAP Kinase ERK2 Catalysis and Stability.” DOI:10.3390/cancers15112938. URL: https://doi.org/10.3390/cancers15112938 (novak2023mutationinthe pages 1-2)
- Becker A.E. et al. *Cell Reports* (2024-10). “ERK1/2 interaction with DHPS regulates eIF5A deoxyhypusination independently of ERK kinase activity.” DOI:10.1016/j.celrep.2024.114831. URL: https://doi.org/10.1016/j.celrep.2024.114831 (becker2024erk12interactionwith pages 1-3, becker2024erk12interactionwith media 4b826433)
- Mohammed K.A.K. et al. *Frontiers in Cardiovascular Medicine* (2024-07). “MEK inhibitors: a promising targeted therapy for cardiovascular disease.” DOI:10.3389/fcvm.2024.1404253. URL: https://doi.org/10.3389/fcvm.2024.1404253 (mohammed2024mekinhibitorsa pages 2-3)
- Karlsson M. et al. *Biochemical Society Transactions* (2006-10). “Spatio-temporal regulation of MAPK signalling by protein phosphatases.” DOI:10.1042/bst0340842. URL: https://doi.org/10.1042/bst0340842 (karlsson2006spatiotemporalregulationof pages 1-2)
- Caunt C.J. et al. *Trends Endocrinol Metab* (2006-09). “Seven-transmembrane receptor signalling and ERK compartmentalization.” DOI:10.1016/j.tem.2006.07.008. URL: https://doi.org/10.1016/j.tem.2006.07.008 (caunt2006seventransmembranereceptorsignalling pages 2-3)
- Caunt C.J. & McArdle C.A. *J Cell Sci* (2010-12). “Stimulus-induced uncoupling of ERK phosphorylation from nuclear localization…” DOI:10.1242/jcs.076349. URL: https://doi.org/10.1242/jcs.076349 (caunt2010stimulusinduceduncouplingof pages 1-2, caunt2010stimulusinduceduncouplingof pages 2-3)
- Waas W.F. & Dalby K.N. *Biochemistry* (2003-03). “Physiological concentrations of divalent magnesium ion activate… ERK2.” DOI:10.1021/bi027171w. URL: https://doi.org/10.1021/bi027171w (waas2003physiologicalconcentrationsof pages 1-2)
- Bardwell A.J. et al. *Biochem J* (2003-03). “Docking sites… compete for MAPK binding and are crucial for enzymic activity.” DOI:10.1042/bj20021806. URL: https://doi.org/10.1042/bj20021806 (bardwell2003dockingsiteson pages 5-6)



References

1. (novak2023mutationinthe pages 1-2): Leonore Novak, Maria Petrosino, Alessandra Pasquo, Apirat Chaikuad, Roberta Chiaraluce, Stefan Knapp, and Valerio Consalvi. Mutation in the common docking domain affects map kinase erk2 catalysis and stability. Cancers, 15:2938, May 2023. URL: https://doi.org/10.3390/cancers15112938, doi:10.3390/cancers15112938. This article has 7 citations.

2. (karlsson2006spatiotemporalregulationof pages 1-2): M. Karlsson, M. Mandl, and S.M. Keyse. Spatio-temporal regulation of mitogen-activated protein kinase (mapk) signalling by protein phosphatases. Biochemical Society transactions, 34 Pt 5:842-5, Oct 2006. URL: https://doi.org/10.1042/bst0340842, doi:10.1042/bst0340842. This article has 35 citations and is from a peer-reviewed journal.

3. (caunt2010stimulusinduceduncouplingof pages 1-2): Christopher J. Caunt and Craig A. McArdle. Stimulus-induced uncoupling of extracellular signal-regulated kinase phosphorylation from nuclear localization is dependent on docking domain interactions. Journal of Cell Science, 123:4310-4320, Dec 2010. URL: https://doi.org/10.1242/jcs.076349, doi:10.1242/jcs.076349. This article has 34 citations and is from a domain leading peer-reviewed journal.

4. (rainey2004astructurefunctionanalysis pages 20-24): MA Rainey. A structure/function analysis of macromolecular recognition by the protein kinase erk2. Unknown journal, 2004.

5. (rainey2004astructurefunctionanalysis pages 24-29): MA Rainey. A structure/function analysis of macromolecular recognition by the protein kinase erk2. Unknown journal, 2004.

6. (waas2003physiologicalconcentrationsof pages 1-2): William F. Waas and Kevin N. Dalby. Physiological concentrations of divalent magnesium ion activate the serine/threonine specific protein kinase erk2. Biochemistry, 42 10:2960-70, Mar 2003. URL: https://doi.org/10.1021/bi027171w, doi:10.1021/bi027171w. This article has 60 citations and is from a peer-reviewed journal.

7. (butch1996characterizationoferk1 pages 1-2): Elizabeth R. Butch and Kun-Liang Guan. Characterization of erk1 activation site mutants and the effect on recognition by mek1 and mek2 (*). The Journal of Biological Chemistry, 271:4230-4235, Feb 1996. URL: https://doi.org/10.1074/jbc.271.8.4230, doi:10.1074/jbc.271.8.4230. This article has 77 citations.

8. (caunt2006seventransmembranereceptorsignalling pages 2-3): Christopher J. Caunt, Ann R. Finch, Kathleen R. Sedgley, and Craig A. McArdle. Seven-transmembrane receptor signalling and erk compartmentalization. Trends in Endocrinology & Metabolism, 17:276-283, Sep 2006. URL: https://doi.org/10.1016/j.tem.2006.07.008, doi:10.1016/j.tem.2006.07.008. This article has 115 citations and is from a domain leading peer-reviewed journal.

9. (karlsson2006spatiotemporalregulationof pages 2-3): M. Karlsson, M. Mandl, and S.M. Keyse. Spatio-temporal regulation of mitogen-activated protein kinase (mapk) signalling by protein phosphatases. Biochemical Society transactions, 34 Pt 5:842-5, Oct 2006. URL: https://doi.org/10.1042/bst0340842, doi:10.1042/bst0340842. This article has 35 citations and is from a peer-reviewed journal.

10. (caunt2010stimulusinduceduncouplingof pages 2-3): Christopher J. Caunt and Craig A. McArdle. Stimulus-induced uncoupling of extracellular signal-regulated kinase phosphorylation from nuclear localization is dependent on docking domain interactions. Journal of Cell Science, 123:4310-4320, Dec 2010. URL: https://doi.org/10.1242/jcs.076349, doi:10.1242/jcs.076349. This article has 34 citations and is from a domain leading peer-reviewed journal.

11. (bardwell2003dockingsiteson pages 5-6): A. Jane BARDWELL, Mahsa ABDOLLAHI, and Lee BARDWELL. Docking sites on mitogen-activated protein kinase (mapk) kinases, mapk phosphatases and the elk-1 transcription factor compete for mapk binding and are crucial for enzymic activity. Biochemical Journal, 370:1077-1085, Mar 2003. URL: https://doi.org/10.1042/bj20021806, doi:10.1042/bj20021806. This article has 150 citations and is from a domain leading peer-reviewed journal.

12. (rainey2004astructurefunctionanalysis pages 29-33): MA Rainey. A structure/function analysis of macromolecular recognition by the protein kinase erk2. Unknown journal, 2004.

13. (martin–vega2025erk12mapksignalingmetabolic pages 3-5): Ana Martin–Vega and Melanie H. Cobb. Erk1/2-mapk signaling: metabolic, organellar, and cytoskeletal interactions. Current Opinion in Cell Biology, 95:102526, Aug 2025. URL: https://doi.org/10.1016/j.ceb.2025.102526, doi:10.1016/j.ceb.2025.102526. This article has 12 citations and is from a peer-reviewed journal.

14. (becker2024erk12interactionwith pages 1-3): Andrew E. Becker, Paweł Kochanowski, Pui-Kei Wu, Elżbieta Wątor, Wenjing Chen, Koushik Guchhait, Artur P. Biela, Przemysław Grudnik, and Jong-In Park. Erk1/2 interaction with dhps regulates eif5a deoxyhypusination independently of erk kinase activity. Cell reports, 43:114831-114831, Oct 2024. URL: https://doi.org/10.1016/j.celrep.2024.114831, doi:10.1016/j.celrep.2024.114831. This article has 4 citations and is from a highest quality peer-reviewed journal.

15. (becker2024erk12interactionwith media 4b826433): Andrew E. Becker, Paweł Kochanowski, Pui-Kei Wu, Elżbieta Wątor, Wenjing Chen, Koushik Guchhait, Artur P. Biela, Przemysław Grudnik, and Jong-In Park. Erk1/2 interaction with dhps regulates eif5a deoxyhypusination independently of erk kinase activity. Cell reports, 43:114831-114831, Oct 2024. URL: https://doi.org/10.1016/j.celrep.2024.114831, doi:10.1016/j.celrep.2024.114831. This article has 4 citations and is from a highest quality peer-reviewed journal.

16. (becker2024erk12interactionwith media dca6815c): Andrew E. Becker, Paweł Kochanowski, Pui-Kei Wu, Elżbieta Wątor, Wenjing Chen, Koushik Guchhait, Artur P. Biela, Przemysław Grudnik, and Jong-In Park. Erk1/2 interaction with dhps regulates eif5a deoxyhypusination independently of erk kinase activity. Cell reports, 43:114831-114831, Oct 2024. URL: https://doi.org/10.1016/j.celrep.2024.114831, doi:10.1016/j.celrep.2024.114831. This article has 4 citations and is from a highest quality peer-reviewed journal.

17. (mohammed2024mekinhibitorsa pages 2-3): Khaled A. K. Mohammed, Paolo Madeddu, and Elisa Avolio. Mek inhibitors: a promising targeted therapy for cardiovascular disease. Frontiers in Cardiovascular Medicine, Jul 2024. URL: https://doi.org/10.3389/fcvm.2024.1404253, doi:10.3389/fcvm.2024.1404253. This article has 17 citations and is from a peer-reviewed journal.

18. (caunt2010stimulusinduceduncouplingof pages 11-11): Christopher J. Caunt and Craig A. McArdle. Stimulus-induced uncoupling of extracellular signal-regulated kinase phosphorylation from nuclear localization is dependent on docking domain interactions. Journal of Cell Science, 123:4310-4320, Dec 2010. URL: https://doi.org/10.1242/jcs.076349, doi:10.1242/jcs.076349. This article has 34 citations and is from a domain leading peer-reviewed journal.

## Citations

1. novak2023mutationinthe pages 1-2
2. rainey2004astructurefunctionanalysis pages 24-29
3. karlsson2006spatiotemporalregulationof pages 1-2
4. karlsson2006spatiotemporalregulationof pages 2-3
5. waas2003physiologicalconcentrationsof pages 1-2
6. bardwell2003dockingsiteson pages 5-6
7. mohammed2024mekinhibitorsa pages 2-3
8. caunt2006seventransmembranereceptorsignalling pages 2-3
9. caunt2010stimulusinduceduncouplingof pages 1-2
10. rainey2004astructurefunctionanalysis pages 20-24
11. caunt2010stimulusinduceduncouplingof pages 2-3
12. rainey2004astructurefunctionanalysis pages 29-33
13. caunt2010stimulusinduceduncouplingof pages 11-11
14. https://doi.org/10.1016/j.celrep.2024.114831
15. https://doi.org/10.3390/cancers15112938
16. https://doi.org/10.3389/fcvm.2024.1404253
17. https://doi.org/10.1042/bst0340842
18. https://doi.org/10.1016/j.tem.2006.07.008
19. https://doi.org/10.1242/jcs.076349
20. https://doi.org/10.1021/bi027171w
21. https://doi.org/10.1042/bj20021806
22. https://doi.org/10.3390/cancers15112938,
23. https://doi.org/10.1042/bst0340842,
24. https://doi.org/10.1242/jcs.076349,
25. https://doi.org/10.1021/bi027171w,
26. https://doi.org/10.1074/jbc.271.8.4230,
27. https://doi.org/10.1016/j.tem.2006.07.008,
28. https://doi.org/10.1042/bj20021806,
29. https://doi.org/10.1016/j.ceb.2025.102526,
30. https://doi.org/10.1016/j.celrep.2024.114831,
31. https://doi.org/10.3389/fcvm.2024.1404253,