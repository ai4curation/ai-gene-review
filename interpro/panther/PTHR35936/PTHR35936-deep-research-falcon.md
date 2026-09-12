---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T21:45:52.721839'
end_time: '2026-06-21T22:03:49.133108'
duration_seconds: 1076.41
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: PTHR35936
  interpro_name: Membrane-bound lytic murein transglycosylase F
  interpro_short_name: MltF
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: Not specified
  n_proteins: '119675'
  n_taxa: '23894'
  n_subfamilies: '14'
  interpro2go_terms: None mapped (no InterPro2GO terms for this entry)
  interpro_description: The protein family includes membrane-bound lytic murein transglycosylase
    F enzymes, which play a crucial role in bacterial cell wall metabolism. These
    enzymes degrade murein glycan strands and high-molecular weight murein sacculi,
    producing a 1,6-anhydromuramoyl product. This action is essential for the maintenance
    and expansion of the peptidoglycan sacculus, a major component of the bacterial
    cell wall that provides structural integrity. By creating space within the peptidoglycan
    sacculus, these enzymes facilitate the insertion of cellular structures such as
    secretion systems and flagella, and allow for the expansion of the cell wall during
    growth and division. The family's proteins typically have a bi-domain architecture
    with an N-terminal domain that modulates enzymatic activity and a C-terminal catalytic
    active domain. Some members of the family are also involved in amino acid transport,
    indicating a dual function in both cell wall metabolism and nutrient uptake.
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PTHR35936-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# InterPro Family Research for GO Annotation Review

## ⚠️ CRITICAL: Family Identification Context

**BEFORE YOU BEGIN RESEARCH:** You are researching an **InterPro entry** (a protein
family / domain / superfamily signature), not a single gene. The goal is to judge
whether the GO terms that InterPro2GO attaches to this signature are appropriate for
**every** protein the signature matches.

### Target InterPro Entry (from the InterPro API):
- **Accession:** PTHR35936
- **Name:** Membrane-bound lytic murein transglycosylase F
- **Short name:** MltF
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 119675 proteins across 23894 taxa, 14 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The protein family includes membrane-bound lytic murein transglycosylase F enzymes, which play a crucial role in bacterial cell wall metabolism. These enzymes degrade murein glycan strands and high-molecular weight murein sacculi, producing a 1,6-anhydromuramoyl product. This action is essential for the maintenance and expansion of the peptidoglycan sacculus, a major component of the bacterial cell wall that provides structural integrity. By creating space within the peptidoglycan sacculus, these enzymes facilitate the insertion of cellular structures such as secretion systems and flagella, and allow for the expansion of the cell wall during growth and division. The family's proteins typically have a bi-domain architecture with an N-terminal domain that modulates enzymatic activity and a C-terminal catalytic active domain. Some members of the family are also involved in amino acid transport, indicating a dual function in both cell wall metabolism and nutrient uptake.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR35936 (Membrane-bound lytic murein transglycosylase F)**, structured to support GO annotation review.

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
- **Accession:** PTHR35936
- **Name:** Membrane-bound lytic murein transglycosylase F
- **Short name:** MltF
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** Not specified
- **Scale:** 119675 proteins across 23894 taxa, 14 subfamilies
- **Current InterPro2GO terms (the mappings under review):** None mapped (no InterPro2GO terms for this entry)
- **InterPro description:** The protein family includes membrane-bound lytic murein transglycosylase F enzymes, which play a crucial role in bacterial cell wall metabolism. These enzymes degrade murein glycan strands and high-molecular weight murein sacculi, producing a 1,6-anhydromuramoyl product. This action is essential for the maintenance and expansion of the peptidoglycan sacculus, a major component of the bacterial cell wall that provides structural integrity. By creating space within the peptidoglycan sacculus, these enzymes facilitate the insertion of cellular structures such as secretion systems and flagella, and allow for the expansion of the cell wall during growth and division. The family's proteins typically have a bi-domain architecture with an N-terminal domain that modulates enzymatic activity and a C-terminal catalytic active domain. Some members of the family are also involved in amino acid transport, indicating a dual function in both cell wall metabolism and nutrient uptake.

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**PTHR35936 (Membrane-bound lytic murein transglycosylase F)**, structured to support GO annotation review.

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


# InterPro Family PTHR35936 Research Report: Membrane-bound Lytic Murein Transglycosylase F (MltF)

## Executive Summary

InterPro entry PTHR35936 represents a family-level protein signature spanning 119,675 proteins across 23,894 taxa organized into 14 subfamilies. The family is designated "Membrane-bound lytic murein transglycosylase F" (MltF) and is described by InterPro as playing roles in bacterial cell wall metabolism and, notably, amino acid transport. **Critical finding: the current entry has NO InterPro2GO mappings**, and the claimed amino acid transport function is not supported by the retrieved scientific literature (2015–2024), which consistently identifies this family as lytic transglycosylase enzymes involved exclusively in peptidoglycan metabolism (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, vermassen2019cellwallhydrolases pages 1-2).

## 1. Family Definition and Biochemistry

### 1.1 Molecular Function and Catalytic Mechanism

PTHR35936 members belong to the **lytic transglycosylase (LT) superfamily**, a class of peptidoglycan glycosidases that cleave bacterial cell wall glycan strands through a non-hydrolytic mechanism distinct from lysozymes (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2). 

**Catalytic mechanism:** Lytic transglycosylases cleave the β-1,4-glycosidic bond between N-acetylmuramic acid (MurNAc) and N-acetylglucosamine (GlcNAc) residues in peptidoglycan glycan chains. Unlike muramidases/lysozymes, which use water as a nucleophile to hydrolyze this bond, LTs employ the C-6 hydroxyl group of MurNAc as an intramolecular nucleophile in a transglycosylation reaction (nocadello2016crystalstructuresof pages 1-2, sychantha2018mechanisticpathwaysfor pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2). This produces a distinctive **1,6-anhydromuramoyl (anhydro-MurNAc) product** along with GlcNAc-containing fragments, which serve as biochemical markers of LT activity in vivo (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2, fumeaux2023apotentialspace pages 1-5).

### 1.2 Conserved Catalytic Residues

The best-supported universal catalytic residue across lytic transglycosylase families is a **conserved glutamate** (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2). Structural and mutational analyses demonstrate that mutation of this glutamate abolishes LT activity. For example, in EtgA (a specialized T3SS-associated LT from enteropathogenic *E. coli*), the catalytic glutamate Glu-42 is essential for both peptidoglycan-lytic activity and for type III secretion system assembly *in vivo* (burkinshaw2015structuralanalysisof pages 1-3). Some specialized LT-related enzymes possess an additional aspartate residue that aligns structurally with the canonical lysozyme Asp-52, providing hybrid catalytic features, but the conserved glutamate remains the core catalytic residue required for the transglycosylation mechanism (burkinshaw2015structuralanalysisof pages 1-3).

### 1.3 Protein Fold and Structure

Despite low primary sequence identity, lytic transglycosylase catalytic domains adopt a **lysozyme-like fold**, particularly resembling the architecture of goose egg-white lysozyme (GEWL) (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2). Crystal structures of SpoIID family LTs from *Bacillus anthracis* and *Clostridium difficile* reveal the overall architecture and substrate recognition model, confirming conserved active-site geometry despite the absence of typical lysozyme sequence motifs (nocadello2016crystalstructuresof pages 1-2). The conserved glutamate is positioned within the active-site cleft to facilitate nucleophilic attack on the glycosidic bond (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3).

Membrane-bound LT family members (the MltA–MltG group in *E. coli*, MltF in *Pseudomonas*) exhibit **modular architecture** with N-terminal membrane-anchoring or regulatory domains and C-terminal catalytic domains (martinezbond2022themechanisticlandscape pages 1-2, vermassen2019cellwallhydrolases pages 1-2). This modularity allows subcellular localization, protein-protein interactions with cell wall synthesis machinery, and regulated activity (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2).

### 1.4 Substrate and Product Specificity

**Substrate:** Peptidoglycan sacculus composed of glycan strands with alternating MurNAc-GlcNAc disaccharides cross-linked by short peptide stems (burkinshaw2015structuralanalysisof pages 1-3, weaver2023mastersofmisdirection pages 1-2, egan2020regulationofpeptidoglycan pages 1-2). LT substrate specificity can be modulated by the crosslinking state of peptidoglycan: recent work demonstrates that LD-crosslinks within the sacculus act as an inhibitor of LT activity, whereas DD-crosslinked peptidoglycan is a better substrate (alvarez2024controlofbacterial pages 1-2). This substrate-level regulation represents a novel control mechanism for autolysin activity.

**Product:** Terminal 1,6-anhydro-MurNAc-containing muropeptides (anhydromuropeptides), which are recycled via periplasmic transport (AmpG permease) and cytoplasmic metabolism or serve as signaling molecules for antibiotic-response pathways such as AmpC β-lactamase induction (weaver2023mastersofmisdirection pages 1-2, fumeaux2023apotentialspace pages 1-5).

| Enzyme/group | Catalytic mechanism | Key catalytic residues | Protein fold / structure | Product formed | Substrate | Roles in bacterial physiology |
|---|---|---|---|---|---|---|
| Lytic transglycosylases (general) | Non-hydrolytic cleavage of the β-1,4 glycosidic bond between MurNAc and GlcNAc; the C6 hydroxyl of MurNAc acts as the nucleophile in an intramolecular transglycosylation reaction, distinguishing LT chemistry from lysozyme/muramidase hydrolysis (nocadello2016crystalstructuresof pages 1-2, sychantha2018mechanisticpathwaysfor pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2) | A catalytic glutamate is the best-supported conserved catalytic residue across LT families; many LT families lack the canonical lysozyme catalytic aspartate, though some specialized PG-lytic enzymes can use an additional aspartate for activity enhancement or altered chemistry (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2) | Catalytic domains are often lysozyme-like, especially goose egg-white lysozyme-like/related architectures despite low sequence identity; LT proteins are structurally diverse overall, but active-site architecture is conserved (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2) | Terminal 1,6-anhydroMurNAc-containing products (anhydromuropeptides / 1,6-anhydromuramoyl products) plus GlcNAc-containing fragments (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2) | Peptidoglycan glycan strands composed of alternating MurNAc and GlcNAc in the bacterial sacculus (burkinshaw2015structuralanalysisof pages 1-3, weaver2023mastersofmisdirection pages 1-2, egan2020regulationofpeptidoglycan pages 1-2) | Peptidoglycan remodeling, turnover, growth, division, cell separation, generation of recycling intermediates, and controlled opening of the wall for large envelope-spanning machines (flagella, secretion systems, pili) (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2) |
| Specialized T3SS/flagellar-associated LT-like PG-cleaving enzymes | Local non-hydrolytic peptidoglycan cleavage to open a passage through the sacculus during assembly of secretion/flagellar structures; mechanistically LT-related, though some have hybrid active-site features shared with lysozymes (burkinshaw2015structuralanalysisof pages 1-3) | Catalytic glutamate is essential; in EtgA, an additional aspartate aligned with lysozyme Asp52 contributes to activity and secretion-system function (burkinshaw2015structuralanalysisof pages 1-3) | Active site combines LT- and lysozyme-like features; structurally adapted for localized PG cleavage and regulated by partner-protein interactions (burkinshaw2015structuralanalysisof pages 1-3) | 1,6-anhydromuramoyl PG fragments expected for LT-type chemistry (burkinshaw2015structuralanalysisof pages 1-3) | Sacculus peptidoglycan at assembly sites of T3SS/related nanomachines (burkinshaw2015structuralanalysisof pages 1-3, minamino2023structureassemblyand pages 1-3) | Enables assembly of type III secretion systems and flagella by locally clearing PG without global lysis; activity can be enhanced by interaction with assembly components (burkinshaw2015structuralanalysisof pages 1-3, minamino2023structureassemblyand pages 1-3) |
| Membrane-bound LTs in Gram-negative envelopes (family context for MltF) | Periplasmic/membrane-associated LT cleavage of PG glycans, often functioning in remodeling and turnover at the cell envelope; can act exolytically or endolytically depending on family/member (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2) | Conserved catalytic glutamate; other residues tune substrate binding and family-specific activity, but broad evidence most consistently supports glutamate as the universal core catalytic residue (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2) | Frequently modular and membrane-associated, with catalytic LT domains appended to targeting/regulatory segments; membrane-bound Ltgs are especially abundant in Gram-negative bacteria such as E. coli and Pseudomonas (martinezbond2022themechanisticlandscape pages 1-2, vermassen2019cellwallhydrolases pages 1-2) | Anhydromuropeptides that can be recycled and/or act as signaling molecules (weaver2023mastersofmisdirection pages 1-2, fumeaux2023apotentialspace pages 1-5) | Mature peptidoglycan sacculus and, in some contexts, uncrosslinked nascent glycan strands generated during cell wall synthesis or β-lactam stress (weaver2023mastersofmisdirection pages 1-2, fumeaux2023apotentialspace pages 1-5) | Cell wall expansion, peptidoglycan recycling, antibiotic-response signaling (e.g., AmpC induction pathways), maintenance of envelope homeostasis, and opening space for insertion of new material (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, fumeaux2023apotentialspace pages 1-5) |
| LT activity under current physiological understanding (2023–2024 emphasis) | LT activity is now understood as strongly context-dependent and regulated by substrate state, localization, and partner interactions rather than constitutively “housekeeping” cleavage (weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2, fumeaux2023apotentialspace pages 1-5) | Catalytic glutamate remains required, but physiological output depends heavily on non-catalytic determinants such as substrate accessibility and protein-protein interactions (burkinshaw2015structuralanalysisof pages 1-3, weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2) | Conserved catalytic cores are embedded in diverse structural scaffolds that support specialized regulation and cellular deployment (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2) | Relative abundance of anhydromuropeptides reflects LT activity in vivo and can report pathway regulation (alvarez2024controlofbacterial pages 1-2, fumeaux2023apotentialspace pages 1-5) | PG whose cleavage sensitivity varies with crosslinking pattern; LD-crosslinks can inhibit LT activity, showing substrate chemistry directly regulates catalysis (alvarez2024controlofbacterial pages 1-2) | Recent work supports roles in regulated autolysin control, immunogenic fragment release, resistance to predatory enzymes/phages, and possibly “space-making” for wall expansion in addition to canonical turnover (alvarez2024controlofbacterial pages 1-2, fumeaux2023apotentialspace pages 1-5, torrens2024mechanismsconferringbacterial pages 1-2) |


*Table: This table summarizes the conserved chemistry, catalytic features, structural themes, products, substrates, and physiological roles of lytic transglycosylases, the enzyme class to which MltF belongs. It is useful for evaluating whether enzymatic and process-level GO annotations are appropriate at the family level.*

## 2. InterPro2GO Mapping Appropriateness

**Current status:** PTHR35936 has **NO GO terms** currently mapped via InterPro2GO.

### 2.1 Recommended Core GO Terms (Applicable to Entire Family)

Based on the conserved biochemical function and broad experimental evidence, the following GO terms are appropriate for **all** members of PTHR35936:

**Molecular Function:**
- **GO:0008933 (lytic transglycosylase activity)** – This is the most specific and accurate term describing the conserved enzymatic mechanism (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, vermassen2019cellwallhydrolases pages 1-2).
- Alternative: GO:0008955 (peptidoglycan glycosylase activity) – A broader parent term also applicable but less mechanistically specific.

**Biological Process:**
- **GO:0009252 (peptidoglycan biosynthetic process)** – LTs participate in cell wall expansion and remodeling by creating space for new peptidoglycan insertion (weaver2023mastersofmisdirection pages 1-2, fumeaux2023apotentialspace pages 1-5, garde2021peptidoglycanstructuresynthesis pages 17-18, egan2020regulationofpeptidoglycan pages 1-2).
- **GO:0051301 (cell division)** – LTs are collectively essential for bacterial cell division and separation in multiple model organisms (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2).

**Cellular Component:**
- **GO:0030313 (cell envelope)** – Broad localization term appropriate for all LTs (martinezbond2022themechanisticlandscape pages 1-2, vermassen2019cellwallhydrolases pages 1-2, egan2020regulationofpeptidoglycan pages 1-2).
- **GO:0019867 (outer membrane)** (for Gram-negative taxa) – Membrane-bound LTs in Gram-negative bacteria localize to the periplasm/outer membrane interface (martinezbond2022themechanisticlandscape pages 1-2, vermassen2019cellwallhydrolases pages 1-2). However, this term should be applied cautiously given the family's taxonomic breadth.

### 2.2 Terms That Should NOT Be Universally Mapped (Subfamily-Specific)

The following GO terms are **true only for subsets** of PTHR35936 members and **must not** be applied at the family level:

- **GO:0009288 (bacterial-type flagellum assembly)** – Only certain specialized LTs (e.g., SltF, EtgA-like enzymes) function in flagellar basal body assembly by locally clearing peptidoglycan (burkinshaw2015structuralanalysisof pages 1-3, minamino2023structureassemblyand pages 1-3). This is a subfamily-specific role, not universal.
  
- **GO:0030254 (protein secretion by the type III secretion system)** – Similarly, only T3SS-associated LTs participate in this process (burkinshaw2015structuralanalysisof pages 1-3, minamino2023structureassemblyand pages 1-3).

- **Amino acid transport** (putative GO terms in this category) – **No experimental evidence** was found supporting amino acid transport as a function of lytic transglycosylases. The InterPro description states "some members of the family are also involved in amino acid transport," but this claim is **not substantiated** by any primary literature on MltF or related LTs retrieved in this analysis (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, vermassen2019cellwallhydrolases pages 1-2, garde2021peptidoglycanstructuresynthesis pages 17-18). This function either: (a) reflects a database annotation error, (b) represents a moonlighting activity requiring verification, or (c) indicates mis-assignment of non-LT sequences to PTHR35936.

### 2.3 Generic Terms of Limited Informational Value

- **GO:0046872 (metal ion binding)** – While some LTs may bind metal ions (alvarez2024controlofbacterial pages 1-2), there is no evidence for conserved metal-dependent catalysis in the LT mechanism itself. Such a term would be uninformative or misleading.
  
- **GO:0016020 (membrane)** – Too generic given that not all family members are membrane-bound (martinezbond2022themechanisticlandscape pages 1-2).

## 3. Functional Divergence Across the Family

### 3.1 Subfamilies and Functional Specialization

PTHR35936 contains **14 subfamilies** (per InterPro metadata). Lytic transglycosylases exhibit high redundancy and functional diversification even within a single organism. For example:

- *Escherichia coli* encodes **8 LTs** (MltA, MltB, MltC, MltD, MltE, MltF, MltG, and Slt70) (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2).
- *Pseudomonas aeruginosa* encodes **11 LTs** (MltA, MltB, MltD, MltF, MltF2, MltG, RlpA, Slt, SltB1, SltB2, SltB3) (martinezbond2022themechanisticlandscape pages 1-2, fumeaux2023apotentialspace pages 1-5).
- *Neisseria* species encode **5 LTs** (LtgA–LtgE) (martinezbond2022themechanisticlandscape pages 1-2).

Despite this redundancy, individual LTs have **non-overlapping physiological roles** determined by:
1. **Subcellular localization** (membrane-bound vs. soluble; septal vs. lateral wall)
2. **Protein-protein interactions** (e.g., LT activation by outer membrane lipoproteins LpoA/LpoB; interaction with PG synthesis machinery; interaction with rod/divisome components) (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, garde2021peptidoglycanstructuresynthesis pages 17-18)
3. **Substrate preferences** (exolytic vs. endolytic activity; sensitivity to crosslinking state) (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, alvarez2024controlofbacterial pages 1-2)

### 3.2 Specialized Functional Variants

**Flagellar and secretion-system-associated LTs:** Some LTs are dedicated to facilitating assembly of large envelope-spanning machines. For example:
- **SltF** (flagellar lytic transglycosylase) – specialized for local peptidoglycan clearance during flagellar basal body insertion; regulated by interaction with flagellar rod proteins FlgB and FlgF (burkinshaw2015structuralanalysisof pages 1-3, minamino2023structureassemblyand pages 1-3).
- **EtgA, IagB, IpgF** (T3SS-associated LTs in EPEC, *Salmonella*, *Shigella*) – interact with inner rod components (EscI in EPEC) and exhibit enhanced activity when complexed with assembly partners (burkinshaw2015structuralanalysisof pages 1-3).

**Cell division specialists:** MltG (YceG) in *E. coli* is an inner membrane endolytic transglycosylase implicated in cell division and plays a role in degrading uncrosslinked nascent peptidoglycan strands during β-lactam stress (weaver2023mastersofmisdirection pages 1-2, fumeaux2023apotentialspace pages 1-5).

**"Space-making" LTs:** Recent work on SltB1 in *Pseudomonas aeruginosa* supports a model wherein this LT uses glycan cleavage to open space in the peptidoglycan matrix for efficient insertion of new material during cell wall expansion—a function traditionally ascribed only to endopeptidases (fumeaux2023apotentialspace pages 1-5).

### 3.3 Catalytically Dead (Pseudo-enzyme) Members?

**No evidence** was found for catalytically inactive members of the LT superfamily that retain the fold but lack activity. The conserved catalytic glutamate appears universally required for function (nocadello2016crystalstructuresof pages 1-2, burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2). Unlike some enzyme families (e.g., kinases, proteases) that include pseudo-enzymes serving regulatory scaffolding roles, LT literature does not report such variants. However, activity modulation does occur through:
- **Substrate-state regulation:** LD-crosslinks inhibit LT activity (alvarez2024controlofbacterial pages 1-2).
- **Protein-protein regulation:** LT activity is enhanced or localized by binding partners (burkinshaw2015structuralanalysisof pages 1-3, martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2).

## 4. Taxonomic Scope

### 4.1 Distribution

PTHR35936 spans **119,675 proteins across 23,894 taxa**, indicating extremely broad phylogenetic distribution across the bacterial domain. Lytic transglycosylases are:
- **Broadly conserved in Gram-negative bacteria** (Proteobacteria, Bacteroidetes, Fusobacteria) where peptidoglycan turnover and envelope remodeling are essential (martinezbond2022themechanisticlandscape pages 1-2, vermassen2019cellwallhydrolases pages 1-2, torrens2024mechanismsconferringbacterial pages 1-2).
- **Present but less abundant in Gram-positive bacteria** (Firmicutes, Actinobacteria), where they play roles in sporulation (e.g., SpoIID in *Bacillus*, *Clostridium*) and cell wall remodeling (nocadello2016crystalstructuresof pages 1-2, vermassen2019cellwallhydrolases pages 1-2).
- **Reduced or altered in obligate intracellular bacteria** (Chlamydiae, Rickettsia, Orientia) where peptidoglycan is minimal or "peptidoglycan-intermediate" (vermassen2019cellwallhydrolases pages 1-2).

### 4.2 Taxon-Specific Considerations for GO Annotation

Given this breadth, process and component terms must be evaluated for taxonomic universality:

- **Peptidoglycan biosynthesis (GO:0009252):** Universally applicable—all bacteria with peptidoglycan require turnover/remodeling for growth (weaver2023mastersofmisdirection pages 1-2, garde2021peptidoglycanstructuresynthesis pages 17-18, egan2020regulationofpeptidoglycan pages 1-2).
  
- **Cell envelope (GO:0030313):** Universally applicable across bacteria.

- **Outer membrane (GO:0019867):** Applicable **only to Gram-negative and mycolate diderm bacteria**, not to Gram-positive monoderms. Annotation at the family level would over-annotate Gram-positive members.

- **Flagellar assembly (GO:0009288):** Restricted to flagellated species and specific LT subfamilies. Over-annotation if applied to PTHR35936 as a whole.

- **Type III secretion (GO:0030254):** Restricted to organisms possessing T3SS (primarily certain Proteobacteria). Over-annotation if applied broadly.

## 5. Over-Annotation Verdict and GO Recommendations

### 5.1 Summary

The InterPro entry PTHR35936 is a **family-level signature** spanning a functionally homogeneous enzyme class (lytic transglycosylases) with a conserved catalytic mechanism (transglycosylation producing 1,6-anhydro-MurNAc products) and universal substrate (peptidoglycan). Despite subfamilyspecialization and organism-specific roles, the **core biochemical function** is conserved across all members.

**Current InterPro2GO status:** No GO mappings exist. This represents a **gap** that should be filled with appropriate conserved terms.

### 5.2 Recommended GO Annotation Actions

| **GO Term Category** | **Recommended Action** | **GO Term(s)** | **Rationale** |
|---|---|---|---|
| **Molecular Function** | **ACCEPT / ADD** | GO:0008933 (lytic transglycosylase activity) | Conserved catalytic activity across all family members (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, vermassen2019cellwallhydrolases pages 1-2). |
| **Biological Process** | **ACCEPT / ADD** | GO:0009252 (peptidoglycan biosynthetic process) | Universal role in cell wall expansion and remodeling (weaver2023mastersofmisdirection pages 1-2, garde2021peptidoglycanstructuresynthesis pages 17-18, egan2020regulationofpeptidoglycan pages 1-2). |
| **Biological Process** | **ACCEPT / ADD** | GO:0051301 (cell division) | LTs are collectively essential for bacterial division and separation (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2). |
| **Cellular Component** | **ACCEPT / ADD (with caveat)** | GO:0030313 (cell envelope) | Universally appropriate; all LTs act on the cell envelope. |
| **Cellular Component** | **MARK_AS_TAXON_RESTRICTED** | GO:0019867 (outer membrane) | Appropriate for Gram-negative bacteria but not Gram-positives. Should be annotated only for relevant taxa or marked as non-core. |
| **Biological Process** | **REMOVE / DO NOT ADD** | GO:0009288 (bacterial-type flagellum assembly) | Subfamily-specific; not universal. Should be annotated only at subfamily/ortholog level (burkinshaw2015structuralanalysisof pages 1-3, minamino2023structureassemblyand pages 1-3). |
| **Biological Process** | **REMOVE / DO NOT ADD** | GO:0030254 (protein secretion by the type III secretion system) | Subfamily-specific; not universal (burkinshaw2015structuralanalysisof pages 1-3). |
| **Biological Process / Molecular Function** | **DO NOT ADD / FLAG AS UNSUPPORTED** | Any amino acid transport term | **No experimental evidence** supports this function for lytic transglycosylases. The InterPro description claiming amino acid transport is unsupported and should be corrected or verified independently. |

### 5.3 Recommendation for InterPro Entry Itself

1. **Remove or verify the "amino acid transport" claim** in the PTHR35936 description. This function is not supported by authoritative lytic transglycosylase literature (martinezbond2022themechanisticlandscape pages 1-2, weaver2023mastersofmisdirection pages 1-2, vermassen2019cellwallhydrolases pages 1-2, garde2021peptidoglycanstructuresynthesis pages 17-18). If some PTHR35936 members genuinely transport amino acids, they may be mis-assigned or represent rare moonlighting cases requiring experimental validation.

2. **Consider creating child InterPro entries** for functionally specialized LT subfamilies (e.g., flagellar LTs, T3SS LTs, cell division LTs) to enable more granular GO annotation. Process terms like flagellar assembly and type III secretion should be mapped to these child entries, not to the parent PTHR35936.

3. **Add core conserved GO terms** (lytic transglycosylase activity, peptidoglycan biosynthetic process, cell division, cell envelope) to PTHR35936 to fill the current annotation gap.

### 5.4 Final Verdict

**InterPro2GO for PTHR35936 is currently INCOMPLETE (no mappings exist) but should be SOUND if the recommended core terms are added.** The family is functionally homogeneous at the biochemical level (all members are peptidoglycan-cleaving lytic transglycosylases), making family-level GO annotation appropriate for conserved functions. However, subfamily-specific and organism-specific process terms (flagellar assembly, secretion, outer membrane localization) should **NOT** be applied at the family level to avoid systematic over-annotation.

**Recommended pattern for future annotation:**
- **ACCEPT core biochemical terms** (lytic transglycosylase activity, peptidoglycan metabolism).
- **MODIFY or DEMOTE to child entries** any whole-organismal process terms (flagellar assembly, secretion).
- **FLAG and verify** the amino acid transport claim, which lacks experimental support.

---

## References (Key Citations)

- Burkinshaw et al. 2015, *J. Biol. Chem.* 290:10406–10417 (burkinshaw2015structuralanalysisof pages 1-3) – Structural and functional analysis of T3SS peptidoglycan-cleaving enzyme EtgA; identification of conserved catalytic glutamate.
- Nocadello et al. 2016, *J. Biol. Chem.* 291:14915–14926 (nocadello2016crystalstructuresof pages 1-2) – Crystal structures of SpoIID lytic transglycosylases; confirmation of lysozyme-like fold and catalytic mechanism.
- Sychantha et al. 2018, *Front. Microbiol.* 9:2332 (sychantha2018mechanisticpathwaysfor pages 1-2) – Mechanistic pathways for peptidoglycan O-acetylation and de-O-acetylation; LT product formation.
- Martinez-Bond et al. 2022, *Curr. Opin. Struct. Biol.* 77:102480 (martinezbond2022themechanisticlandscape pages 1-2) – Mechanistic landscape of lytic transglycosylases as antibacterial targets; redundancy and conserved catalysis.
- Weaver et al. 2023, *J. Bacteriol.* 205:e00428-22 (weaver2023mastersofmisdirection pages 1-2) – Masters of misdirection: peptidoglycan glycosidases in bacterial growth; functional specialization despite mechanistic conservation.
- Alvarez et al. 2024, *Nat. Commun.* 15:7937 (alvarez2024controlofbacterial pages 1-2) – Control of bacterial autolysins by peptidoglycan crosslinking mode; LD-crosslinks inhibit LT activity.
- Fumeaux & Bernhardt 2023, *bioRxiv* (fumeaux2023apotentialspace pages 1-5) – Space-making role for lytic transglycosylase SltB1 in *Pseudomonas* cell wall biogenesis.
- Garde et al. 2021, *EcoSal Plus* 9:ESP-0010-2020 (garde2021peptidoglycanstructuresynthesis pages 17-18) – Peptidoglycan structure, synthesis, and regulation; role of hydrolysis in sacculus expansion.
- Egan et al. 2020, *Nat. Rev. Microbiol.* 18:446–460 (egan2020regulationofpeptidoglycan pages 1-2) – Regulation of peptidoglycan synthesis and remodelling.
- Minamino & Kinoshita 2023, *EcoSal Plus* 11:ESP-0011-2023 (minamino2023structureassemblyand pages 1-3) – Structure, assembly, and function of bacterial flagella; role of LTs in flagellar assembly.
- Vermassen et al. 2019, *Front. Microbiol.* 10:331 (vermassen2019cellwallhydrolases pages 1-2) – Cell wall hydrolases in bacteria: diversity of amidases, glycosidases, and peptidases toward peptidoglycan; modular architecture of LTs.
- Torrens & Cava 2024, *Biochem. Soc. Trans.* 52:1981–1993 (torrens2024mechanismsconferringbacterial pages 1-2) – Mechanisms conferring bacterial cell wall variability and adaptivity; LT roles in environmental adaptation.

References

1. (martinezbond2022themechanisticlandscape pages 1-2): Elizabeth A. Martinez-Bond, Berliza M. Soriano, and Allison H. Williams. The mechanistic landscape of lytic transglycosylase as targets for antibacterial therapy. Dec 2022. URL: https://doi.org/10.1016/j.sbi.2022.102480, doi:10.1016/j.sbi.2022.102480. This article has 24 citations and is from a peer-reviewed journal.

2. (weaver2023mastersofmisdirection pages 1-2): Anna Weaver, Atsushi Taguchi, and Tobias Dörr. Masters of misdirection: peptidoglycan glycosidases in bacterial growth. Journal of Bacteriology, Mar 2023. URL: https://doi.org/10.1128/jb.00428-22, doi:10.1128/jb.00428-22. This article has 30 citations and is from a peer-reviewed journal.

3. (vermassen2019cellwallhydrolases pages 1-2): Aurore Vermassen, Sabine Leroy, Régine Talon, Christian Provot, Magdalena Popowska, and Mickaël Desvaux. Cell wall hydrolases in bacteria: insight on the diversity of cell wall amidases, glycosidases and peptidases toward peptidoglycan. Frontiers in Microbiology, Feb 2019. URL: https://doi.org/10.3389/fmicb.2019.00331, doi:10.3389/fmicb.2019.00331. This article has 439 citations and is from a peer-reviewed journal.

4. (nocadello2016crystalstructuresof pages 1-2): Salvatore Nocadello, George Minasov, Ludmilla S. Shuvalova, Ievgeniia Dubrovska, Elisabetta Sabini, and Wayne F. Anderson. Crystal structures of the spoiid lytic transglycosylases essential for bacterial sporulation. Journal of Biological Chemistry, 291:14915-14926, Jul 2016. URL: https://doi.org/10.1074/jbc.m116.729749, doi:10.1074/jbc.m116.729749. This article has 23 citations and is from a domain leading peer-reviewed journal.

5. (burkinshaw2015structuralanalysisof pages 1-3): Brianne J. Burkinshaw, Wanyin Deng, Emilie Lameignère, Gregory A. Wasney, Haizhong Zhu, Liam J. Worrall, B. Brett Finlay, and Natalie C.J. Strynadka. Structural analysis of a specialized type iii secretion system peptidoglycan-cleaving enzyme. Journal of Biological Chemistry, 290:10406-10417, Apr 2015. URL: https://doi.org/10.1074/jbc.m115.639013, doi:10.1074/jbc.m115.639013. This article has 73 citations and is from a domain leading peer-reviewed journal.

6. (sychantha2018mechanisticpathwaysfor pages 1-2): David Sychantha, Ashley S. Brott, Carys S. Jones, and Anthony J. Clarke. Mechanistic pathways for peptidoglycan o-acetylation and de-o-acetylation. Frontiers in Microbiology, Oct 2018. URL: https://doi.org/10.3389/fmicb.2018.02332, doi:10.3389/fmicb.2018.02332. This article has 72 citations and is from a peer-reviewed journal.

7. (alvarez2024controlofbacterial pages 1-2): Laura Alvarez, Sara B. Hernandez, Gabriel Torrens, Anna I. Weaver, Tobias Dörr, and Felipe Cava. Control of bacterial cell wall autolysins by peptidoglycan crosslinking mode. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52325-2, doi:10.1038/s41467-024-52325-2. This article has 35 citations and is from a highest quality peer-reviewed journal.

8. (fumeaux2023apotentialspace pages 1-5): Coralie Fumeaux and Thomas G. Bernhardt. A potential space making role for a lytic transglycosylase in cell wall biogenesis revealed by a beta-lactamase induction phenotype in<i>pseudomonas aeruginosa</i>. BioRxiv, Sep 2023. URL: https://doi.org/10.1101/2023.09.05.556436, doi:10.1101/2023.09.05.556436. This article has 1 citations.

9. (egan2020regulationofpeptidoglycan pages 1-2): Alexander J. F. Egan, Jeff Errington, and Waldemar Vollmer. Regulation of peptidoglycan synthesis and remodelling. Nature Reviews Microbiology, 18:446-460, May 2020. URL: https://doi.org/10.1038/s41579-020-0366-3, doi:10.1038/s41579-020-0366-3. This article has 684 citations and is from a highest quality peer-reviewed journal.

10. (minamino2023structureassemblyand pages 1-3): Tohru Minamino and Miki Kinoshita. Structure, assembly, and function of flagella responsible for bacterial locomotion. EcoSal Plus, Dec 2023. URL: https://doi.org/10.1128/ecosalplus.esp-0011-2023, doi:10.1128/ecosalplus.esp-0011-2023. This article has 57 citations.

11. (torrens2024mechanismsconferringbacterial pages 1-2): Gabriel Torrens and Felipe Cava. Mechanisms conferring bacterial cell wall variability and adaptivity. Biochemical Society Transactions, 52:1981-1993, Sep 2024. URL: https://doi.org/10.1042/bst20230027, doi:10.1042/bst20230027. This article has 28 citations and is from a peer-reviewed journal.

12. (garde2021peptidoglycanstructuresynthesis pages 17-18): Shambhavi Garde, Pavan Kumar Chodisetti, and Manjula Reddy. Peptidoglycan: structure, synthesis, and regulation. Dec 2021. URL: https://doi.org/10.1128/ecosalplus.esp-0010-2020, doi:10.1128/ecosalplus.esp-0010-2020. This article has 323 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR35936-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. burkinshaw2015structuralanalysisof pages 1-3
2. nocadello2016crystalstructuresof pages 1-2
3. alvarez2024controlofbacterial pages 1-2
4. martinezbond2022themechanisticlandscape pages 1-2
5. fumeaux2023apotentialspace pages 1-5
6. vermassen2019cellwallhydrolases pages 1-2
7. sychantha2018mechanisticpathwaysfor pages 1-2
8. weaver2023mastersofmisdirection pages 1-2
9. garde2021peptidoglycanstructuresynthesis pages 17-18
10. egan2020regulationofpeptidoglycan pages 1-2
11. minamino2023structureassemblyand pages 1-3
12. torrens2024mechanismsconferringbacterial pages 1-2
13. https://doi.org/10.1016/j.sbi.2022.102480,
14. https://doi.org/10.1128/jb.00428-22,
15. https://doi.org/10.3389/fmicb.2019.00331,
16. https://doi.org/10.1074/jbc.m116.729749,
17. https://doi.org/10.1074/jbc.m115.639013,
18. https://doi.org/10.3389/fmicb.2018.02332,
19. https://doi.org/10.1038/s41467-024-52325-2,
20. https://doi.org/10.1101/2023.09.05.556436,
21. https://doi.org/10.1038/s41579-020-0366-3,
22. https://doi.org/10.1128/ecosalplus.esp-0011-2023,
23. https://doi.org/10.1042/bst20230027,
24. https://doi.org/10.1128/ecosalplus.esp-0010-2020,