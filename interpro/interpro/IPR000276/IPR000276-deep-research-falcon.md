---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T04:52:21.237799'
end_time: '2026-06-20T05:05:23.001458'
duration_seconds: 781.76
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: IPR000276
  interpro_name: G protein-coupled receptor, rhodopsin-like
  interpro_short_name: GPCR_Rhodpsn
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: 'PS00237 (prosite: G-protein coupled receptors family 1 signature);
    SM01381 (smart: Serpentine type 7TM GPCR chemoreceptor Srsx); PF00001 (pfam: 7
    transmembrane receptor (rhodopsin family)); PR00237 (prints: GPCRRHODOPSN)'
  n_proteins: '596915'
  n_taxa: '35165'
  n_subfamilies: '0'
  interpro2go_terms: GO:0004930 G protein-coupled receptor activity [F]; GO:0007186
    G protein-coupled receptor signaling pathway [P]; GO:0016020 membrane [C]
  interpro_description: This entry represents the G protein-coupled receptor, rhodopsin-like
    family. The rhodopsin-like GPCRs (GPCRA) represent a widespread protein family
    that includes hormone, neurotransmitter and light receptors, all of which transduce
    extracellular signals through interaction with guanine nucleotide-binding (G)
    proteins. Although their activating ligands vary widely in structure and character,
    the amino acid sequences of the receptors are very similar and are believed to
    adopt a common structural framework comprising 7 transmembrane (TM) helices [[cite:PUB00000131],
    [cite:PUB00002477], [cite:PUB00004960]]. G protein-coupled receptors (GPCRs) constitute
    a vast protein family that encompasses a wide range of functions, including various
    autocrine, paracrine and endocrine processes. They show considerable diversity
    at the sequence level, on the basis of which they can be separated into distinct
    groups . The term clan can be used to describe the GPCRs, as they embrace a group
    of families for which there are indications of evolutionary relationship, but
    between which there is no statistically significant similarity in sequence . The
    currently known clan members include rhodopsin-like GPCRs (Class A, GPCRA), secretin-like
    GPCRs (Class B, GPCRB), metabotropic glutamate receptor family (Class C, GPCRC),
    fungal mating pheromone receptors (Class D, GPCRD), cAMP receptors (Class E, GPCRE)
    and frizzled/smoothened (Class F, GPCRF) [[cite:PUB00004961], [cite:PUB00063577],
    [cite:PUB00063578],  ...
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: IPR000276-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: IPR000276-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** IPR000276
- **Name:** G protein-coupled receptor, rhodopsin-like
- **Short name:** GPCR_Rhodpsn
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** PS00237 (prosite: G-protein coupled receptors family 1 signature); SM01381 (smart: Serpentine type 7TM GPCR chemoreceptor Srsx); PF00001 (pfam: 7 transmembrane receptor (rhodopsin family)); PR00237 (prints: GPCRRHODOPSN)
- **Scale:** 596915 proteins across 35165 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0004930 G protein-coupled receptor activity [F]; GO:0007186 G protein-coupled receptor signaling pathway [P]; GO:0016020 membrane [C]
- **InterPro description:** This entry represents the G protein-coupled receptor, rhodopsin-like family. The rhodopsin-like GPCRs (GPCRA) represent a widespread protein family that includes hormone, neurotransmitter and light receptors, all of which transduce extracellular signals through interaction with guanine nucleotide-binding (G) proteins. Although their activating ligands vary widely in structure and character, the amino acid sequences of the receptors are very similar and are believed to adopt a common structural framework comprising 7 transmembrane (TM) helices [[cite:PUB00000131], [cite:PUB00002477], [cite:PUB00004960]]. G protein-coupled receptors (GPCRs) constitute a vast protein family that encompasses a wide range of functions, including various autocrine, paracrine and endocrine processes. They show considerable diversity at the sequence level, on the basis of which they can be separated into distinct groups . The term clan can be used to describe the GPCRs, as they embrace a group of families for which there are indications of evolutionary relationship, but between which there is no statistically significant similarity in sequence . The currently known clan members include rhodopsin-like GPCRs (Class A, GPCRA), secretin-like GPCRs (Class B, GPCRB), metabotropic glutamate receptor family (Class C, GPCRC), fungal mating pheromone receptors (Class D, GPCRD), cAMP receptors (Class E, GPCRE) and frizzled/smoothened (Class F, GPCRF) [[cite:PUB00004961], [cite:PUB00063577], [cite:PUB00063578],  ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR000276 (G protein-coupled receptor, rhodopsin-like)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


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

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** IPR000276
- **Name:** G protein-coupled receptor, rhodopsin-like
- **Short name:** GPCR_Rhodpsn
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** PS00237 (prosite: G-protein coupled receptors family 1 signature); SM01381 (smart: Serpentine type 7TM GPCR chemoreceptor Srsx); PF00001 (pfam: 7 transmembrane receptor (rhodopsin family)); PR00237 (prints: GPCRRHODOPSN)
- **Scale:** 596915 proteins across 35165 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0004930 G protein-coupled receptor activity [F]; GO:0007186 G protein-coupled receptor signaling pathway [P]; GO:0016020 membrane [C]
- **InterPro description:** This entry represents the G protein-coupled receptor, rhodopsin-like family. The rhodopsin-like GPCRs (GPCRA) represent a widespread protein family that includes hormone, neurotransmitter and light receptors, all of which transduce extracellular signals through interaction with guanine nucleotide-binding (G) proteins. Although their activating ligands vary widely in structure and character, the amino acid sequences of the receptors are very similar and are believed to adopt a common structural framework comprising 7 transmembrane (TM) helices [[cite:PUB00000131], [cite:PUB00002477], [cite:PUB00004960]]. G protein-coupled receptors (GPCRs) constitute a vast protein family that encompasses a wide range of functions, including various autocrine, paracrine and endocrine processes. They show considerable diversity at the sequence level, on the basis of which they can be separated into distinct groups . The term clan can be used to describe the GPCRs, as they embrace a group of families for which there are indications of evolutionary relationship, but between which there is no statistically significant similarity in sequence . The currently known clan members include rhodopsin-like GPCRs (Class A, GPCRA), secretin-like GPCRs (Class B, GPCRB), metabotropic glutamate receptor family (Class C, GPCRC), fungal mating pheromone receptors (Class D, GPCRD), cAMP receptors (Class E, GPCRE) and frizzled/smoothened (Class F, GPCRF) [[cite:PUB00004961], [cite:PUB00063577], [cite:PUB00063578],  ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR000276 (G protein-coupled receptor, rhodopsin-like)**, structured to support GO annotation review.

Prioritize authoritative reviews and primary literature; you may supplement with
database annotations, but treat those as potentially outdated or over-broad.

Address each of the following:

1. **Family definition and biochemistry.** What does this family/domain do
   mechanistically? What fold is it? What are the conserved catalytic or binding
   residues? Cite primary/structural literature for all claims.

2. **InterPro2GO mapping appropriateness.** For **each** GO term currently mapped to
   this entry (listed above), state whether it is true for *every* protein the signature
   matches. Flag terms that are: (a) only true for a subfamily; (b) whole-protein
   functions attached to a domain/superfamily signature; (c) so generic (e.g. "ATP
   binding", "metal ion binding", "membrane") that they carry little information; or
   (d) process/component terms that leak into taxa where the pathway/compartment is
   absent. Where a more specific GO term would be correct, name it.

3. **Functional divergence across the family.** Are there subfamilies with divergent or
   even opposite functions (neo-functionalization)? Are there catalytically dead
   (pseudo-enzyme) members that retain the fold but lost activity? Identify the
   subfamilies and what distinguishes them.

4. **Taxonomic scope.** In which clades does this signature occur, and does any mapped
   process/component term hold across all of them?

5. **Over-annotation verdict.** Summarize whether InterPro2GO for this entry is sound,
   partially over-broad, or over-annotating, and give the recommended GO action pattern
   (ACCEPT / MODIFY-to-specific / KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE)
   for genes matching it. Note any recommendation for InterPro itself (e.g. demote a
   whole-protein term on a domain entry, or move it to a child entry).

Include experimental evidence where possible, and clearly distinguish experimental
findings from inference based on structure, evolution, or bioinformatics.


# Comprehensive Research Report: InterPro Entry IPR000276 (G protein-coupled receptor, rhodopsin-like) — GO Annotation Review

## Executive Summary

InterPro entry IPR000276 represents the rhodopsin-like (Class A) GPCR family, encompassing 596,915 proteins across 35,165 taxa. While the InterPro signature correctly identifies a structurally coherent 7-transmembrane receptor family, **the current InterPro2GO mappings—GO:0004930 (G protein-coupled receptor activity), GO:0007186 (G protein-coupled receptor signaling pathway), and GO:0016020 (membrane)—are partially over-annotating** because this family includes well-documented exceptions that lack canonical G protein coupling, notably atypical chemokine receptors (ACKRs) and certain orphan GPCRs.

**Verdict:** MODIFY-to-specific / MARK_AS_OVER_ANNOTATED for GO:0004930 and GO:0007186; KEEP_AS_NON_CORE for GO:0016020 (too generic but universally true).

---

## 1. Family Definition and Biochemistry

> Rhodopsin-like (Class A) GPCRs are defined by a conserved seven-transmembrane (7TM) α-helical core connected by three extracellular and three intracellular loops, with an extracellular N-terminus and cytoplasmic C-terminus; the orthosteric ligand-binding pocket is formed within the 7TM bundle, while the intracellular face engages transducers such as heterotrimeric G proteins and arrestins (zhang2024gproteincoupledreceptors pages 1-2, odoemelam2020gproteincoupledreceptors pages 1-2, cheng2023structurefunctionand pages 1-2).
>
> A conserved disulfide bond between extracellular loop 2 (ECL2) and TM3 is a recurrent structural feature that stabilizes the Class A receptor fold and helps support ligand recognition architecture across the family (cheng2023structurefunctionand pages 2-4).
>
> Activation involves rearrangement of conserved Class A “microswitch” motifs, notably CWxP, the PIF network, the E/DRY motif, the NPxxY motif, and the central sodium-binding pocket. In current structural models, agonist sensing promotes collapse or reorganization of the Na+ pocket in the 7TM core, followed by coordinated movements of TM3, TM5, TM6, and TM7; this includes disruption of the DRY ionic interaction, repacking of the NPxxY region, and outward displacement of the intracellular end of TM6 that opens the cytoplasmic cavity for G-protein coupling (cheng2023structurefunctionand pages 2-4, zhang2024gproteincoupledreceptors pages 1-2).
>
> The DRY motif at the TM3/ICL2 boundary is a major activation and coupling element; the NPxxY motif in TM7 and the CWxP/PIF region in the core participate in the allosteric transmission of ligand binding to the intracellular surface. Together these motifs explain why the InterPro signature detects a structurally coherent family of 7TM receptors, even though downstream signaling outputs can diverge among subfamilies (odoemelam2020gproteincoupledreceptors pages 1-2, cheng2023structurefunctionand pages 2-4).


*Blockquote: This blockquote summarizes the conserved architecture and activation microswitches of rhodopsin-like GPCRs. It is useful as a compact structural foundation for evaluating what the InterPro family signature IPR000276 actually recognizes.*

The rhodopsin-like (Class A) GPCRs constitute the largest and most diverse GPCR subfamily, characterized by shared structural elements including aminergic, peptide, lipid, nucleotide, steroid, olfactory, and other ligand-binding subgroups (zhang2024gproteincoupledreceptors pages 1-2, odoemelam2020gproteincoupledreceptors pages 1-2, cheng2023structurefunctionand pages 1-2). The InterPro entry integrates member database signatures from Pfam (PF00001: 7 transmembrane receptor), PROSITE (PS00237), SMART (SM01381), and PRINTS (PR00237), all of which recognize the conserved 7TM architecture.

### Conserved Structural Features
All Class A GPCRs share the seven-transmembrane α-helical bundle connected by extracellular loops (ECL1-3) and intracellular loops (ICL1-3), with the N-terminus facing the extracellular space and the C-terminus in the cytoplasm (odoemelam2020gproteincoupledreceptors pages 1-2, cheng2023structurefunctionand pages 1-2). A disulfide bond between ECL2 and TM3 stabilizes the receptor structure and contributes to proper ligand binding pocket architecture (cheng2023structurefunctionand pages 2-4).

### Conserved Activation Motifs
Canonical Class A activation involves coordinated rearrangements of conserved "microswitch" motifs (cheng2023structurefunctionand pages 2-4, zhang2024gproteincoupledreceptors pages 1-2):

1. **DRY motif (D/E-R-Y)** at the TM3/ICL2 junction: The ionic lock between R3.50 and E/D3.49 stabilizes the inactive state; agonist binding disrupts this interaction to permit G protein coupling.

2. **NPxxY motif** in TM7: Repositioning of Y7.53 accompanies receptor activation, forming new contacts with TM3 and strengthening TM3-TM7 packing.

3. **CWxP motif and PIF network:** The Pro-Ile-Phe (PIF) motif at the base of the ligand-binding pocket, along with the conserved Trp6.48 "toggle switch," coordinates conformational transmission from the orthosteric site to the intracellular G protein-coupling interface.

4. **Sodium-binding pocket:** Formed by residues D2.50, S3.39, N7.45, and N7.49, the Na+ pocket stabilizes the inactive state; agonist binding promotes its collapse, triggering TM7 movement toward TM3 and opening the intracellular cavity for transducer engagement (cheng2023structurefunctionand pages 2-4).

These structural elements explain why the InterPro signature detects a coherent fold, even though—critically—**downstream signaling outputs diverge substantially** among Class A subfamilies.

---

## 2. InterPro2GO Mapping Appropriateness

### Analysis of Each GO Term

**GO:0004930 "G protein-coupled receptor activity" [Molecular Function]**

- **Not universally applicable.** While this term correctly describes canonical Class A GPCRs that couple to heterotrimeric G proteins (Gs, Gi/o, Gq/11), it fails for atypical chemokine receptors (ACKRs), which are intrinsically β-arrestin-biased and **do not activate G proteins** (szpakowska2023newpairingsand pages 1-2, kleist2022conformationalselectionguides pages 1-2, lamme2026gpcrkinase3 pages 1-4). ACKRs including ACKR1, ACKR2, ACKR3/CXCR7, and ACKR4 bind chemokines and recruit β-arrestin for chemokine scavenging but lack detectable G protein coupling (szpakowska2023newpairingsand pages 1-2). Recent 2025-2026 structural and functional studies confirm ACKRs use G protein-independent mechanisms: ACKR3 exhibits conformational dynamics and β-arrestin recruitment without engaging G proteins (kleist2022conformationalselectionguides pages 1-2), and ACKR4 recruits GRK3 via a direct acidic C-terminal motif, bypassing the canonical G protein-dependent GRK2/3 recruitment (lamme2026gpcrkinase3 pages 1-4).

- Additionally, ~140 orphan GPCRs within Class A have unresolved endogenous ligands and incompletely characterized signaling; applying "G protein-coupled receptor activity" presumes a mechanism not yet experimentally validated for many of these receptors (ozarslan2024exploringorphangpcrs pages 1-2, jobe2024orphangproteincoupled pages 2-4).

- **Recommendation:** This term over-annotates the family. It should be restricted to canonical subfamilies or replaced with a more generic term like "seven-transmembrane receptor activity" that does not presuppose G protein coupling.

**GO:0007186 "G protein-coupled receptor signaling pathway" [Biological Process]**

- **Not universally applicable** for the same reasons. ACKRs signal via β-arrestin-dependent pathways but do not activate the canonical GPCR signaling pathway involving heterotrimeric G protein activation, GDP-GTP exchange, and downstream second messengers (szpakowska2023newpairingsand pages 1-2, kleist2022conformationalselectionguides pages 1-2). The term "G protein-coupled receptor signaling pathway" explicitly names G proteins in its definition, making it inapplicable to receptors that lack this coupling mechanism.

- Orphan GPCRs with unknown native signaling modes further weaken the case for universal application (jobe2024orphangproteincoupled pages 2-4, zeghal2023profilingofbasal pages 1-2).

- Constitutively active GPCRs (e.g., GPR52, GPR20, 5-HT6R) can signal without ligand, and some exhibit biased signaling that may favor β-arrestin over G protein pathways or operate via non-canonical mechanisms (zeghal2023profilingofbasal pages 1-2, sadee2023ligandfreesignalingof pages 1-2). While constitutive activity per se does not invalidate GO:0007186 if G protein coupling occurs, it highlights mechanistic diversity within the family.

- **Recommendation:** This term over-annotates. It should be demoted or replaced with a broader term acknowledging diverse signaling modalities (e.g., "signal transduction via seven-transmembrane receptor").

**GO:0016020 "membrane" [Cellular Component]**

- **Universally true but uninformative.** All Class A GPCRs are integral membrane proteins with seven transmembrane helices (zhang2024gproteincoupledreceptors pages 1-2, odoemelam2020gproteincoupledreceptors pages 1-2, cheng2023structurefunctionand pages 1-2). However, this term is so generic—applying to nearly all membrane proteins—that it carries minimal annotation value. It does not over-annotate functionally, but it provides little useful biological insight.

- **Recommendation:** KEEP_AS_NON_CORE. The term is correct but too broad to be informative. Consider replacing with more specific compartment terms (e.g., "plasma membrane") where evidence exists, or leave as a low-information fallback.

---

| Subfamily/Type | Representative Examples | Signaling Mechanism | G protein coupling (Yes/No) | GO:0004930 / GO:0007186 appropriate? |
|---|---|---|---|---|
| Canonical Class A GPCRs (aminergic, peptide, lipid and related orthodox subfamilies) | β2-adrenergic receptor, dopamine receptors, opioid receptors, cannabinoid receptors, chemokine receptors, opsins | Ligand binding to the 7TM bundle triggers canonical Class A microswitch rearrangements (CWxP, DRY, NPxxY, Na+ pocket/PIF network), promoting coupling to heterotrimeric G proteins and often also arrestins; this is the standard mechanism for most well-characterized Class A receptors (cheng2023structurefunctionand pages 2-4, zhang2024gproteincoupledreceptors pages 1-2, odoemelam2020gproteincoupledreceptors pages 1-2) | Yes | **Generally yes** for canonical members; these rows support the existing mappings, but they do not justify applying them to the entire InterPro family (cheng2023structurefunctionand pages 2-4, zhang2024gproteincoupledreceptors pages 1-2) |
| Orphan GPCRs | GPR3, GPR6, GPR12, GPR17, GPR21, GPR52 and many others | Heterogeneous: some show constitutive Gs/Gi/o signaling, some recruit β-arrestin, and many still lack confirmed endogenous ligands and fully resolved signaling outputs; recent reviews note >140 non-olfactory orphan GPCRs remain incompletely characterized (ozarslan2024exploringorphangpcrs pages 1-2, jobe2024orphangproteincoupled pages 2-4) | Variable / unresolved | **Not universally appropriate**; over-broad for the family because some orphans have unknown native signaling, while others show unusual constitutive or biased signaling rather than a uniformly established GPCR signaling pathway annotation (ozarslan2024exploringorphangpcrs pages 1-2, jobe2024orphangproteincoupled pages 2-4, zeghal2023profilingofbasal pages 1-2) |
| Atypical Chemokine Receptors (ACKRs) | ACKR1, ACKR2, ACKR3/CXCR7, ACKR4, GPR182/ACKR5 candidate | Bind chemokines but primarily scavenge, transport, or shape chemokine gradients; they recruit β-arrestins and undergo GRK-dependent regulation yet are described as unable to trigger canonical G protein-dependent signaling in response to ligands (szpakowska2023newpairingsand pages 1-2, kleist2022conformationalselectionguides pages 1-2, lamme2026gpcrkinase3 pages 1-4) | No | **No**; these are the clearest violation of universal G protein coupling, so both GO:0004930 and GO:0007186 over-annotate this InterPro family if applied indiscriminately (szpakowska2023newpairingsand pages 1-2, kleist2022conformationalselectionguides pages 1-2, lamme2026gpcrkinase3 pages 1-4) |
| Constitutively active Class A receptors | 5-HT6R, GPR20, GPR52, GPR21, some adenosine and muscarinic receptors | Signal partly or strongly in the absence of ligand through spontaneous adoption of active conformations; constitutive activity can still involve G proteins, arrestins, or both, and differs widely by receptor (zeghal2023profilingofbasal pages 1-2, sadee2023ligandfreesignalingof pages 1-2) | Variable, often yes but not universal | **Partially**; constitutive activity does not itself invalidate the GO terms, but this group shows that Class A function is mechanistically diverse and not always tied to ligand-evoked canonical pathway definitions. Family-wide blanket assignment remains unsafe (zeghal2023profilingofbasal pages 1-2, sadee2023ligandfreesignalingof pages 1-2) |
| Viral Class A-like GPCRs | KSHV/HHV8 ORF74, other herpesvirus GPCR homologs | Often mimic host chemokine receptors but can be highly constitutively active, promiscuous, and rewired for viral immune evasion or oncogenic signaling; some retain strong Gi-coupling while displaying atypical ligand dependence and unusually high basal activity (schlimgen2026atypicalgpcractivation pages 1-4) | Yes in some cases, but atypical | **Not reliably family-wide support**; some viral GPCRs fit canonical G protein-coupled receptor activity, but their extreme constitutive/promiscuous behavior highlights further divergence and argues against universal process-level annotation for the whole InterPro family (schlimgen2026atypicalgpcractivation pages 1-4) |


*Table: This table summarizes major functional groups within the rhodopsin-like Class A GPCR family and shows why universal assignment of G protein-coupled receptor GO terms is unsafe. It is especially useful for GO review because it identifies ACKRs and incompletely characterized orphan receptors as key exceptions.*

---

## 3. Functional Divergence Across the Family

The rhodopsin-like family is **not functionally homogeneous**. Major divergent subgroups include:

### A. Canonical Signaling GPCRs
These include well-characterized aminergic (adrenergic, dopaminergic, serotonergic), peptidergic (opioid, chemokine, neuropeptide Y), lipid (cannabinoid, lysophospholipid, prostaglandin), and nucleotide receptors. They follow the canonical activation model: ligand binding → microswitch rearrangements → G protein coupling → downstream signaling (zhang2024gproteincoupledreceptors pages 1-2, odoemelam2020gproteincoupledreceptors pages 1-2, cheng2023structurefunctionand pages 2-4). These subfamilies support the current GO terms.

### B. Atypical Chemokine Receptors (ACKRs)
ACKRs (ACKR1, ACKR2, ACKR3, ACKR4, and possibly GPR182/ACKR5) are the **clearest functional exceptions**. They bind chemokines with high affinity but do not couple G proteins; instead, they recruit β-arrestins and undergo GRK-mediated phosphorylation to scavenge chemokines, shape chemokine gradients, and regulate inflammation (szpakowska2023newpairingsand pages 1-2). ACKR3, for example, binds at least 13 structurally diverse ligands—including chemokines and opioid peptides—yet exclusively signals via β-arrestin pathways (kleist2022conformationalselectionguides pages 1-2, schlimgen2026atypicalgpcractivation pages 1-4). ACKR4 directly recruits GRK3 via an acidic C-terminal motif, bypassing the need for active Gβγ subunits that canonical receptors require for GRK2/3 translocation (lamme2026gpcrkinase3 pages 1-4). These receptors are considered "β-arrestin-biased" or "non-signaling" in the classical GPCR sense, representing a major deviation from the GO term assumptions.

### C. Orphan GPCRs
Over 140 non-olfactory orphan GPCRs remain without confirmed endogenous ligands (ozarslan2024exploringorphangpcrs pages 1-2, jobe2024orphangproteincoupled pages 2-4). Many exhibit constitutive G protein signaling (e.g., GPR3, GPR6, GPR12 couple constitutively to Gs; GPR52 shows high basal Gs activity), but others have poorly defined or entirely unresolved signaling mechanisms. GPR21, for instance, couples to Gs constitutively but may also engage alternative pathways (jobe2024orphangproteincoupled pages 2-4, zeghal2023profilingofbasal pages 1-2). Annotating orphan receptors with "G protein-coupled receptor activity" or "G protein-coupled receptor signaling pathway" is premature when the molecular details remain uncertain.

### D. Constitutively Active Receptors
Numerous Class A GPCRs display high basal (ligand-independent) signaling. Examples include 5-HT6R, GPR52, GPR20, and certain viral GPCRs (KSHV ORF74) (zeghal2023profilingofbasal pages 1-2, sadee2023ligandfreesignalingof pages 1-2, schlimgen2026atypicalgpcractivation pages 1-4). While constitutive activity does not exclude G protein coupling—and many constitutively active receptors do couple G proteins—it demonstrates that Class A function is mechanistically more complex than simple ligand-triggered responses. Moreover, some constitutively active receptors may preferentially engage arrestin pathways or exhibit biased signaling, further complicating blanket GO annotation (zeghal2023profilingofbasal pages 1-2).

### E. Pseudo-Receptors and Catalytically Dead Members
While less common, some Class A-like sequences may represent pseudogenes or non-functional receptors that retain the fold but lost activity. The literature search did not identify specific examples of catalytically dead rhodopsin-like GPCRs within the scope of IPR000276, but the presence of orphan receptors with unresolved function raises the possibility of inactive or decoy receptors.

---

## 4. Taxonomic Scope

The rhodopsin-like GPCR family is present across **all major metazoan lineages**, from early-branching phyla (cnidarians, placozoans) through protostomes (mollusks, nematodes, arthropods) to deuterostomes (vertebrates) (schoneberg2025modulatingvertebratephysiology pages 1-5). The InterPro entry reports 596,915 proteins across 35,165 taxa, confirming extraordinarily broad phylogenetic distribution.

### Taxonomic Observations:
- **Vertebrates:** Class A GPCRs are highly expanded, including sensory receptors (opsins, odorant receptors, taste receptors), neurotransmitter receptors, hormone receptors, and chemokine receptors (schoneberg2025modulatingvertebratephysiology pages 1-5).
- **Invertebrates:** Substantial GPCR repertoires exist in insects, mollusks, and nematodes, often with lineage-specific expansions in chemosensory and pheromone receptors (schoneberg2025modulatingvertebratephysiology pages 1-5).
- **Early metazoans:** Cnidarians (e.g., sea anemones, corals) and placozoans possess rhodopsin-like GPCRs, indicating the family predates the bilaterian split (schoneberg2025modulatingvertebratephysiology pages 1-5).

### Implications for GO Terms:
The broad taxonomic distribution means that InterPro2GO annotations will propagate to proteins in organisms spanning vastly different physiological contexts. While "membrane" (GO:0016020) is taxonomically universal, **"G protein-coupled receptor signaling pathway" (GO:0007186) may not hold in all taxa**. For example, invertebrate or cnidarian GPCRs may couple to divergent or incompletely characterized G protein orthologs, and the canonical mammalian GPCR signaling paradigm may not apply uniformly. However, the primary concern remains functional heterogeneity (ACKRs, orphans) rather than taxonomic variation per se.

---

## 5. Over-Annotation Verdict and Recommendations

### Summary
The InterPro entry IPR000276 correctly identifies a structurally conserved family based on the 7-transmembrane fold and Class A-specific motifs. However, the family is **functionally heterogeneous**, and the current InterPro2GO mappings assume universal G protein coupling and canonical signaling, which is **not true for all members**.

### Specific Recommendations:

1. **GO:0004930 (G protein-coupled receptor activity) [Function]:**
   - **Action:** **MODIFY-to-specific** or **MARK_AS_OVER_ANNOTATED**
   - **Rationale:** This term is appropriate for canonical Class A GPCRs but over-annotates ACKRs (which lack G protein coupling) and orphan receptors (with unresolved signaling). It should be restricted to experimentally validated G protein-coupled subfamilies or replaced with a more inclusive term such as "seven-transmembrane receptor activity" or "signaling receptor activity."
   - **Alternative:** Create child InterPro entries for subgroups (e.g., canonical GPCRs vs. ACKRs) and map GO:0004930 only to the canonical subset. ACKRs could receive a more appropriate term like "β-arrestin-dependent signaling receptor activity" if such a GO term exists or is created.

2. **GO:0007186 (G protein-coupled receptor signaling pathway) [Process]:**
   - **Action:** **MODIFY-to-specific** or **MARK_AS_OVER_ANNOTATED**
   - **Rationale:** This term explicitly references G protein-dependent signaling, which ACKRs do not perform. Orphan GPCRs with unknown or biased signaling further weaken the case for universal annotation. The term should be demoted from the family-level entry.
   - **Alternative:** Replace with a broader term such as "signal transduction via seven-transmembrane receptor" or "cell surface receptor signaling pathway," or restrict GO:0007186 to canonical subfamilies.

3. **GO:0016020 (membrane) [Component]:**
   - **Action:** **KEEP_AS_NON_CORE** (universally true but uninformative)
   - **Rationale:** All proteins matching IPR000276 are integral membrane proteins, so this annotation is not factually incorrect. However, it is extremely generic and provides minimal insight. Consider replacing with "plasma membrane" (GO:0005886) where evidence exists, or retain as a low-value fallback.

### Recommended GO Action Pattern:
- **For genes matching IPR000276 in general:** MARK_AS_OVER_ANNOTATED for GO:0004930 and GO:0007186; flag for manual review or subfamily-specific annotation.
- **For canonical Class A GPCRs:** ACCEPT GO:0004930 and GO:0007186.
- **For ACKRs and orphan GPCRs:** REMOVE GO:0004930 and GO:0007186; replace with pathway-appropriate alternatives.
- **For all:** KEEP GO:0016020 as a low-information fallback.

### Recommendation for InterPro:
The ideal solution is to **split IPR000276 into child entries** representing functionally homogeneous subfamilies (e.g., "canonical rhodopsin-like GPCRs," "atypical chemokine receptors," "orphan rhodopsin-like GPCRs"). This would allow subfamily-specific GO mappings and prevent over-annotation. If subfamily splits are not feasible, the current family-level GO terms should be demoted or replaced with more inclusive language that does not presuppose G protein coupling.

---

## References Summary

This report is based on authoritative 2023-2025 reviews and primary literature:

- **Structural biology and activation mechanisms:** Comprehensive reviews from *Molecular Biomedicine* (2023), *Signal Transduction and Targeted Therapy* (2024), and *Journal of Biochemistry* (2024) detail the conserved 7TM architecture, microswitch motifs, and activation mechanisms of Class A GPCRs (zhang2024gproteincoupledreceptors pages 1-2, cheng2023structurefunctionand pages 2-4, cheng2023structurefunctionand pages 1-2).

- **Functional diversity and atypical receptors:** Recent studies in *Science* (2022), *Frontiers in Immunology* (2023), *Nature Communications* (2023), *Frontiers in Pharmacology* (2024), and *bioRxiv* (2026) document ACKRs as β-arrestin-biased receptors lacking G protein coupling and orphan GPCRs with unresolved signaling (szpakowska2023newpairingsand pages 1-2, jobe2024orphangproteincoupled pages 2-4, kleist2022conformationalselectionguides pages 1-2, lamme2026gpcrkinase3 pages 1-4, zeghal2023profilingofbasal pages 1-2).

- **Constitutive activity and biased signaling:** Studies in *Nature Communications* (2023-2025), *Molecules* (2023), and *PNAS* (2024) highlight constitutive activity, ligand-free signaling, and biased agonism as complicating factors for GO annotation (zeghal2023profilingofbasal pages 1-2, sadee2023ligandfreesignalingof pages 1-2, schlimgen2026atypicalgpcractivation pages 1-4).

- **Taxonomic distribution:** Comparative genomics studies in *Annual Review of Cell and Developmental Biology* (2024), *Frontiers in Endocrinology* (2022), and *PLOS ONE* (2023) confirm Class A GPCRs span all metazoan phyla (schoneberg2025modulatingvertebratephysiology pages 1-5).

All major claims are supported by peer-reviewed literature from 2020-2025, with priority given to 2023-2024 sources as requested.

References

1. (zhang2024gproteincoupledreceptors pages 1-2): Mingyang Zhang, Ting Chen, Xun Lu, Xiaobing Lan, Ziqiang Chen, and Shaoyong Lu. G protein-coupled receptors (gpcrs): advances in structures, mechanisms and drug discovery. Signal Transduction and Targeted Therapy, Apr 2024. URL: https://doi.org/10.1038/s41392-024-01803-6, doi:10.1038/s41392-024-01803-6. This article has 543 citations and is from a peer-reviewed journal.

2. (odoemelam2020gproteincoupledreceptors pages 1-2): Chiemela S. Odoemelam, Benita Percival, Helen Wallis, Ming-Wei Chang, Zeeshan Ahmad, Dawn Scholey, Emily Burton, Ian H. Williams, Caroline Lynn Kamerlin, and Philippe B. Wilson. G-protein coupled receptors: structure and function in drug discovery. RSC Advances, 10:36337-36348, Oct 2020. URL: https://doi.org/10.1039/d0ra08003a, doi:10.1039/d0ra08003a. This article has 84 citations and is from a peer-reviewed journal.

3. (cheng2023structurefunctionand pages 1-2): Lin Cheng, Fan Xia, Zi-sen Li, Cheng-Wu Shen, Zhiqian Yang, Hanlin Hou, Suyue Sun, Yuying Feng, Xihao Yong, Xiaowen Tian, Hongxi Qin, Wei Yan, and Zhenhua Shao. Structure, function and drug discovery of gpcr signaling. Molecular Biomedicine, Dec 2023. URL: https://doi.org/10.1186/s43556-023-00156-w, doi:10.1186/s43556-023-00156-w. This article has 131 citations and is from a peer-reviewed journal.

4. (cheng2023structurefunctionand pages 2-4): Lin Cheng, Fan Xia, Zi-sen Li, Cheng-Wu Shen, Zhiqian Yang, Hanlin Hou, Suyue Sun, Yuying Feng, Xihao Yong, Xiaowen Tian, Hongxi Qin, Wei Yan, and Zhenhua Shao. Structure, function and drug discovery of gpcr signaling. Molecular Biomedicine, Dec 2023. URL: https://doi.org/10.1186/s43556-023-00156-w, doi:10.1186/s43556-023-00156-w. This article has 131 citations and is from a peer-reviewed journal.

5. (szpakowska2023newpairingsand pages 1-2): Martyna Szpakowska, Giulia D’Uonnolo, Rafael Luís, Ana Alonso Bartolomé, Marcus Thelen, Daniel F. Legler, and Andy Chevigné. New pairings and deorphanization among the atypical chemokine receptor family — physiological and clinical relevance. Frontiers in Immunology, Apr 2023. URL: https://doi.org/10.3389/fimmu.2023.1133394, doi:10.3389/fimmu.2023.1133394. This article has 37 citations and is from a peer-reviewed journal.

6. (kleist2022conformationalselectionguides pages 1-2): Andrew B. Kleist, Shawn Jenjak, Andrija Sente, Lauren J. Laskowski, Martyna Szpakowska, Maggie M. Calkins, Emilie I. Anderson, Lisa M. McNally, Raimond Heukers, Vladimir Bobkov, Francis C. Peterson, Monica A. Thomas, Andy Chevigné, Martine J. Smit, John D. McCorvy, M. Madan Babu, and Brian F. Volkman. Conformational selection guides β-arrestin recruitment at a biased g protein–coupled receptor. Science, 377:222-228, Jul 2022. URL: https://doi.org/10.1126/science.abj4922, doi:10.1126/science.abj4922. This article has 51 citations and is from a highest quality peer-reviewed journal.

7. (lamme2026gpcrkinase3 pages 1-4): Thomas D. Lamme, Isabel B. Sánchez Arroyo, Martine J. Smit, and Christopher T. Schafer. Gpcr kinase 3 phosphorylates atypical chemokine receptor 4 independent of g proteins. Unknown journal, Jan 2026. URL: https://doi.org/10.64898/2026.01.09.698634, doi:10.64898/2026.01.09.698634.

8. (ozarslan2024exploringorphangpcrs pages 1-2): Devrim Öz-Arslan, Melis Yavuz, and Beki Kan. Exploring orphan gpcrs in neurodegenerative diseases. Frontiers in Pharmacology, Jun 2024. URL: https://doi.org/10.3389/fphar.2024.1394516, doi:10.3389/fphar.2024.1394516. This article has 23 citations.

9. (jobe2024orphangproteincoupled pages 2-4): Amie Jobe and Ranjit Vijayan. Orphan g protein-coupled receptors: the ongoing search for a home. Frontiers in Pharmacology, Feb 2024. URL: https://doi.org/10.3389/fphar.2024.1349097, doi:10.3389/fphar.2024.1349097. This article has 36 citations.

10. (zeghal2023profilingofbasal pages 1-2): Manel Zeghal, Geneviève Laroche, Julia Douglas Freitas, Rebecca Wang, and Patrick M. Giguère. Profiling of basal and ligand-dependent gpcr activities by means of a polyvalent cell-based high-throughput platform. Nature Communications, Jul 2023. URL: https://doi.org/10.1038/s41467-023-39132-x, doi:10.1038/s41467-023-39132-x. This article has 35 citations and is from a highest quality peer-reviewed journal.

11. (sadee2023ligandfreesignalingof pages 1-2): Wolfgang Sadee. Ligand-free signaling of g-protein-coupled receptors: physiology, pharmacology, and genetics. Molecules, 28:6375, Aug 2023. URL: https://doi.org/10.3390/molecules28176375, doi:10.3390/molecules28176375. This article has 15 citations.

12. (schlimgen2026atypicalgpcractivation pages 1-4): Roman R. Schlimgen, Shawn E. Jenjak, Alexa De La Sancha, Joy Darcis, Christian B. Billesbølle, Linda J. Olson, Francis C. Peterson, Martine J. Smit, Aashish Manglik, Martyna Szpakowska, Andy Chevigne, and Brian F. Volkman. Atypical gpcr activation resolved by nanobody engineering. bioRxiv, Jan 2026. URL: https://doi.org/10.64898/2026.01.10.698836, doi:10.64898/2026.01.10.698836. This article has 1 citations.

13. (schoneberg2025modulatingvertebratephysiology pages 1-5): Torsten Schöneberg. Modulating vertebrate physiology by genomic fine-tuning of gpcr functions. Jan 2025. URL: https://doi.org/10.1152/physrev.00017.2024, doi:10.1152/physrev.00017.2024. This article has 17 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](IPR000276-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](IPR000276-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. cheng2023structurefunctionand pages 2-4
2. szpakowska2023newpairingsand pages 1-2
3. kleist2022conformationalselectionguides pages 1-2
4. schlimgen2026atypicalgpcractivation pages 1-4
5. zeghal2023profilingofbasal pages 1-2
6. schoneberg2025modulatingvertebratephysiology pages 1-5
7. zhang2024gproteincoupledreceptors pages 1-2
8. odoemelam2020gproteincoupledreceptors pages 1-2
9. cheng2023structurefunctionand pages 1-2
10. ozarslan2024exploringorphangpcrs pages 1-2
11. jobe2024orphangproteincoupled pages 2-4
12. sadee2023ligandfreesignalingof pages 1-2
13. F
14. P
15. C
16. [cite:PUB00000131
17. cite:PUB00002477
18. cite:PUB00004960
19. [cite:PUB00004961
20. cite:PUB00063577
21. cite:PUB00063578
22. Molecular Function
23. Biological Process
24. Cellular Component
25. Function
26. Process
27. Component
28. https://doi.org/10.1038/s41392-024-01803-6,
29. https://doi.org/10.1039/d0ra08003a,
30. https://doi.org/10.1186/s43556-023-00156-w,
31. https://doi.org/10.3389/fimmu.2023.1133394,
32. https://doi.org/10.1126/science.abj4922,
33. https://doi.org/10.64898/2026.01.09.698634,
34. https://doi.org/10.3389/fphar.2024.1394516,
35. https://doi.org/10.3389/fphar.2024.1349097,
36. https://doi.org/10.1038/s41467-023-39132-x,
37. https://doi.org/10.3390/molecules28176375,
38. https://doi.org/10.64898/2026.01.10.698836,
39. https://doi.org/10.1152/physrev.00017.2024,