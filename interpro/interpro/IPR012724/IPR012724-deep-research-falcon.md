---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-20T04:52:21.237933'
end_time: '2026-06-20T05:05:02.198255'
duration_seconds: 760.96
template_file: templates/interpro_family_research.md
template_variables:
  interpro_id: IPR012724
  interpro_name: Chaperone DnaJ
  interpro_short_name: DnaJ
  interpro_type: family
  interpro_integrated: None (top-level entry)
  member_databases: 'MF_01152 (hamap: Chaperone protein DnaJ [dnaJ]); TIGR02349 (ncbifam:
    molecular chaperone DnaJ)'
  n_proteins: '35613'
  n_taxa: '34746'
  n_subfamilies: '0'
  interpro2go_terms: GO:0005524 ATP binding [F]; GO:0006457 protein folding [P]; GO:0009408
    response to heat [P]
  interpro_description: Molecular chaperones are a diverse family of proteins that
    function to protect proteins in the intracellular milieu from irreversible aggregation
    during synthesis and in times of cellular stress. The bacterial molecular chaperone
    DnaK is an enzyme that couples cycles of ATP binding, hydrolysis, and ADP release
    by an N-terminal ATP-hydrolizing domain to cycles of sequestration and release
    of unfolded proteins by a C-terminal substrate binding domain. Dimeric GrpE is
    the co-chaperone for DnaK, and acts as a nucleotide exchange factor, stimulating
    the rate of ADP release 5000-fold . DnaK is itself a weak ATPase; ATP hydrolysis
    by DnaK is stimulated by its interaction with another co-chaperone, DnaJ. Thus
    the co-chaperones DnaJ and GrpE are capable of tightly regulating the nucleotide-bound
    and substrate-bound state of DnaK in ways that are necessary for the normal housekeeping
    functions and stress-related functions of the DnaK molecular chaperone cycle.
    Besides stimulating the ATPase activity of DnaK through its J-domain, DnaJ also
    associates with unfolded polypeptide chains and prevents their aggregation . Thus,
    DnaK and DnaJ may bind to one and the same polypeptide chain to form a ternary
    complex. The formation of a ternary complex may result in cis-interaction of the
    J-domain of DnaJ with the ATPase domain of DnaK. An unfolded polypeptide may enter
    the chaperone cycle by associating first either with ATP-liganded DnaK or with
    DnaJ. DnaK interacts with both the backbone and si ...
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: IPR012724-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: IPR012724-deep-research-falcon_artifacts/artifact-01.md
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
- **Accession:** IPR012724
- **Name:** Chaperone DnaJ
- **Short name:** DnaJ
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** MF_01152 (hamap: Chaperone protein DnaJ [dnaJ]); TIGR02349 (ncbifam: molecular chaperone DnaJ)
- **Scale:** 35613 proteins across 34746 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0005524 ATP binding [F]; GO:0006457 protein folding [P]; GO:0009408 response to heat [P]
- **InterPro description:** Molecular chaperones are a diverse family of proteins that function to protect proteins in the intracellular milieu from irreversible aggregation during synthesis and in times of cellular stress. The bacterial molecular chaperone DnaK is an enzyme that couples cycles of ATP binding, hydrolysis, and ADP release by an N-terminal ATP-hydrolizing domain to cycles of sequestration and release of unfolded proteins by a C-terminal substrate binding domain. Dimeric GrpE is the co-chaperone for DnaK, and acts as a nucleotide exchange factor, stimulating the rate of ADP release 5000-fold . DnaK is itself a weak ATPase; ATP hydrolysis by DnaK is stimulated by its interaction with another co-chaperone, DnaJ. Thus the co-chaperones DnaJ and GrpE are capable of tightly regulating the nucleotide-bound and substrate-bound state of DnaK in ways that are necessary for the normal housekeeping functions and stress-related functions of the DnaK molecular chaperone cycle. Besides stimulating the ATPase activity of DnaK through its J-domain, DnaJ also associates with unfolded polypeptide chains and prevents their aggregation . Thus, DnaK and DnaJ may bind to one and the same polypeptide chain to form a ternary complex. The formation of a ternary complex may result in cis-interaction of the J-domain of DnaJ with the ATPase domain of DnaK. An unfolded polypeptide may enter the chaperone cycle by associating first either with ATP-liganded DnaK or with DnaJ. DnaK interacts with both the backbone and si ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR012724 (Chaperone DnaJ)**, structured to support GO annotation review.

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
- **Accession:** IPR012724
- **Name:** Chaperone DnaJ
- **Short name:** DnaJ
- **Entry type:** family
- **Integrated into / parent:** None (top-level entry)
- **Member database signatures:** MF_01152 (hamap: Chaperone protein DnaJ [dnaJ]); TIGR02349 (ncbifam: molecular chaperone DnaJ)
- **Scale:** 35613 proteins across 34746 taxa, 0 subfamilies
- **Current InterPro2GO terms (the mappings under review):** GO:0005524 ATP binding [F]; GO:0006457 protein folding [P]; GO:0009408 response to heat [P]
- **InterPro description:** Molecular chaperones are a diverse family of proteins that function to protect proteins in the intracellular milieu from irreversible aggregation during synthesis and in times of cellular stress. The bacterial molecular chaperone DnaK is an enzyme that couples cycles of ATP binding, hydrolysis, and ADP release by an N-terminal ATP-hydrolizing domain to cycles of sequestration and release of unfolded proteins by a C-terminal substrate binding domain. Dimeric GrpE is the co-chaperone for DnaK, and acts as a nucleotide exchange factor, stimulating the rate of ADP release 5000-fold . DnaK is itself a weak ATPase; ATP hydrolysis by DnaK is stimulated by its interaction with another co-chaperone, DnaJ. Thus the co-chaperones DnaJ and GrpE are capable of tightly regulating the nucleotide-bound and substrate-bound state of DnaK in ways that are necessary for the normal housekeeping functions and stress-related functions of the DnaK molecular chaperone cycle. Besides stimulating the ATPase activity of DnaK through its J-domain, DnaJ also associates with unfolded polypeptide chains and prevents their aggregation . Thus, DnaK and DnaJ may bind to one and the same polypeptide chain to form a ternary complex. The formation of a ternary complex may result in cis-interaction of the J-domain of DnaJ with the ATPase domain of DnaK. An unfolded polypeptide may enter the chaperone cycle by associating first either with ATP-liganded DnaK or with DnaJ. DnaK interacts with both the backbone and si ...

### Why entry type matters:

An entry of type **domain**, **repeat**, or **homologous_superfamily** identifies a
structural/functional *module*, not a whole-protein function. GO terms describing a
whole-protein activity or process attached to such a module systematically over-annotate
every protein that merely *contains* the module. An entry of type **family** is more
likely to support whole-protein function terms, but only if the family is functionally
homogeneous.

## Research Target

Provide a comprehensive, citation-backed research report on the InterPro entry
**IPR012724 (Chaperone DnaJ)**, structured to support GO annotation review.

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


# Comprehensive Research Report: InterPro Entry IPR012724 (Chaperone DnaJ) – GO Annotation Review

## Executive Summary

InterPro entry IPR012724 (Chaperone DnaJ) represents a family-level signature spanning 35,613 proteins across 34,746 taxa. Current InterPro2GO mappings include GO:0005524 (ATP binding), GO:0006457 (protein folding), and GO:0009408 (response to heat). This analysis reveals that **IPR012724 is partially over-annotating**: GO:0005524 is factually incorrect, GO:0006457 is broadly appropriate, and GO:0009408 overgeneralizes from heat-inducible canonical members to the functionally heterogeneous family.

**Recommendation**: REMOVE GO:0005524 (ATP binding); ACCEPT GO:0006457 (protein folding); KEEP_AS_NON_CORE or demote GO:0009408 (response to heat) to apply only to stress-responsive subfamilies.

---

## 1. Family Definition and Biochemistry

### Structural Architecture of the J-Domain

The defining feature of DnaJ/J-domain proteins (JDPs) is the **J-domain** (Pfam PF00226), an evolutionarily conserved ~70-residue module comprising four α-helices (I–IV) (zhang2023jdomainproteinchaperone pages 3-4, malinverni2023datadrivenlargescalegenomic pages 1-2). Helices II and III form an antiparallel coiled-coil through hydrophobic interactions, stabilized by helices I and IV at the termini (zhang2023jdomainproteinchaperone pages 3-4). The signature **His-Pro-Asp (HPD) motif** resides in the loop connecting helices II and III and is essential for stimulating ATP hydrolysis in Hsp70 partners (tomiczek2020twostepmechanismof pages 1-3, kim2021thednakdnajchaperone pages 1-2, zhang2023jdomainproteinchaperone pages 3-4). Approximately 1% of J-domains carry an HPE variant motif, suggesting fine-tuned modulation of Hsp70 stimulation in specific contexts (malinverni2023datadrivenlargescalegenomic pages 3-5).

A positively charged electrostatic patch in helix II facilitates docking onto the negatively charged "underbelly" of ATP-bound Hsp70 at the interface between the Hsp70 nucleotide-binding domain (NBD), interdomain linker, and substrate-binding β-domain (SBDβ) (tomiczek2020twostepmechanismof pages 1-3, zhang2023jdomainproteinchaperone pages 3-4). This interaction positions the HPD motif to perturb a conserved intramolecular network in Hsp70, destabilizing the NBD-SBD interface and promoting the allosteric transition that triggers ATP hydrolysis (tomiczek2020twostepmechanismof pages 1-3).

### Mechanistic Function: Co-Chaperone Role, NOT ATP Binding

**Critical finding**: DnaJ proteins themselves **do not bind ATP**. Instead, they function as obligate **co-chaperones** that stimulate ATP hydrolysis in their Hsp70/DnaK partners (mayer2021thehsp70chaperonemachines pages 1-2, pan2024dnakduplicationand pages 1-2, zhang2023jdomainproteinchaperone pages 3-4). The mechanistic cycle involves: (1) JDP loading with client protein substrate; (2) J-domain docking onto ATP-bound Hsp70; (3) stimulation of Hsp70 ATPase activity via the HPD motif; (4) client transfer to Hsp70 and stabilization in the high-affinity ADP-Hsp70 state; (5) nucleotide exchange factor (NEF)-mediated ADP release and substrate release (zhang2023jdomainproteinchaperone pages 3-4, malkeyeva2025heatshockproteins pages 1-2, mayer2021thehsp70chaperonemachines pages 1-2). The ATP-binding and -hydrolyzing activity resides exclusively in the Hsp70 NBD; the J-domain is a regulatory interface, not an ATP-binding site (tomiczek2020twostepmechanismof pages 1-3, kim2021thednakdnajchaperone pages 1-2, pan2024dnakduplicationand pages 1-2).

Class A JDPs (full DnaJ homologs) additionally contain a G/F-rich region, two β-sandwich C-terminal domains (CTD-I and CTD-II), a cysteine-rich zinc-finger-like region (ZFLR) within CTD-I, and often a dimerization domain and disordered C-terminal tail (malinverni2023datadrivenlargescalegenomic pages 1-2, velascocarneros2023theselfassociationequilibrium pages 1-2, zhang2023jdomainproteinchaperone pages 3-4). These accessory domains mediate substrate binding, partner interactions, and oligomerization but do not confer ATP-binding capability.

---

## 2. InterPro2GO Mapping Appropriateness

| GO Term ID | GO Term Name | GO Aspect (F/P/C) | Appropriateness Assessment | Evidence Summary | Recommendation |
|---|---|---|---|---|---|
| GO:0005524 | ATP binding | F | **INCORRECT** | Recent mechanistic reviews and primary studies consistently describe ATP binding/hydrolysis as a property of the Hsp70 partner (DnaK/Hsp70) nucleotide-binding domain, while DnaJ/JDPs use the J-domain HPD motif to stimulate Hsp70 ATPase activity rather than bind ATP themselves. DnaJ docks onto ATP-bound Hsp70 and promotes ATP hydrolysis in Hsp70; no evidence supports universal ATP binding by DnaJ family members matched by this InterPro family. This is therefore a factual over-annotation, not just an overgeneralization. (zhang2023jdomainproteinchaperone pages 3-4, tomiczek2020twostepmechanismof pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2, pan2024dnakduplicationand pages 1-2) | **REMOVE** |
| GO:0006457 | protein folding | P | **CORRECT, but broad** | Across kingdoms, J-domain proteins function as obligate Hsp70 cochaperones in proteostasis, recruiting Hsp70 to client proteins and promoting Hsp70-dependent folding/refolding cycles. Reviews describe JDPs as central to de novo folding, refolding, prevention of aggregation, and broader protein quality control. However, some family members are highly specialized for trafficking, Fe-S cluster biogenesis, translocation, or remodeling circuits, so the process term is true at a high level but may be less specific than ideal for some members. (zhang2023jdomainproteinchaperone pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2, malkeyeva2025heatshockproteins pages 1-2, kampinga2019functionevolutionand pages 1-2) | **ACCEPT** |
| GO:0009408 | response to heat | P | **OVERGENERALIZED** | DnaJ/Hsp40 proteins were historically identified as heat shock proteins, and many canonical bacterial DnaJ systems contribute to heat-stress survival. But the family is now known to include many constitutive and highly specialized JDPs that are not universally heat-inducible, including HscB-like proteins in Fe-S cluster biogenesis and many class C eukaryotic JDPs with compartment- or pathway-specific roles. Workshop and large-scale genomic analyses emphasize that many JDPs are not stress regulated and that most family diversity lies outside canonical heat-shock roles. Therefore this process term does not hold for every protein matched by IPR012724. (kampinga2019functionevolutionand pages 1-2, malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 1-3, mayer2021thehsp70chaperonemachines pages 2-4) | **KEEP_AS_NON_CORE** |


*Table: This table evaluates the three current InterPro2GO mappings for the DnaJ family against mechanistic and evolutionary evidence. It highlights one clear error, one broadly acceptable process term, and one overgeneralized stress-response term.*

### GO:0005524 (ATP binding) – INCORRECT

This assignment is **factually erroneous**. Across all primary mechanistic studies and authoritative reviews from 2020–2024, ATP binding and hydrolysis are consistently ascribed to the Hsp70/DnaK partner, not to DnaJ/JDP family members (zhang2023jdomainproteinchaperone pages 3-4, tomiczek2020twostepmechanismof pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2, pan2024dnakduplicationand pages 1-2, mayer2021thehsp70chaperonemachines pages 2-4, kim2021thednakdnajchaperone pages 1-2). DnaJ proteins use their J-domain to **stimulate** Hsp70 ATPase activity by promoting allosteric conformational changes in Hsp70, but they lack an ATP-binding pocket (tomiczek2020twostepmechanismof pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2). Large-scale genomic surveys of J-domain proteins reveal no ATP-binding domain annotation outside the Hsp70 partner (malinverni2023datadrivenlargescalegenomic pages 3-5). This represents over-annotation via erroneous transfer of the Hsp70 function to the co-chaperone.

**Recommendation**: **REMOVE** GO:0005524 from IPR012724.

### GO:0006457 (protein folding) – APPROPRIATE

J-domain proteins are central to proteostasis, acting as obligate co-chaperones that direct Hsp70 systems to protein substrates for de novo folding, refolding of stress-denatured proteins, prevention of aggregation, and disaggregation (zhang2023jdomainproteinchaperone pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2, malkeyeva2025heatshockproteins pages 1-2, kampinga2019functionevolutionand pages 1-2). The annotation is correct in capturing the family's core biological process involvement. However, it is somewhat imprecise: JDPs are co-chaperones rather than direct folding enzymes, and some specialized members function in protein trafficking, translocation, or remodeling rather than classical folding cycles (malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 3-4). A more granular alternative could be GO:0051082 (unfolded protein binding) or GO:0051087 (chaperone binding) to clarify the co-chaperone role, but GO:0006457 is defensible for the family overall.

**Recommendation**: **ACCEPT** GO:0006457. Optional refinement: add GO:0051087 (chaperone binding) to clarify indirect mechanism.

### GO:0009408 (response to heat) – OVERGENERALIZED

While the prototypical bacterial DnaJ was discovered as a heat-shock-inducible protein and many canonical DnaJ systems contribute to thermotolerance (mayer2021thehsp70chaperonemachines pages 2-4, figaj2025theroleof pages 1-2, malkeyeva2025heatshockproteins pages 1-2), the DnaJ/JDP family is now known to be functionally heterogeneous. Large-scale genomic analyses reveal that the family includes many **constitutively expressed** members with specialized, non-heat-shock functions (kampinga2019functionevolutionand pages 1-2, malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 1-3):

- **HscB-family JDPs** (e.g., yeast Jac1, human DNAJC20) are dedicated to iron-sulfur cluster biogenesis and are not heat-induced (malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 3-4).
- **Sec63** (DNAJC23) functions in ER protein translocation, a constitutive housekeeping process (malinverni2023datadrivenlargescalegenomic pages 3-5, kampinga2019functionevolutionand pages 1-2).
- Many **Class C eukaryotic JDPs** exhibit tissue-specific or compartment-specific expression without stress regulation (zhang2023jdomainproteinchaperone pages 1-3, kampinga2019functionevolutionand pages 1-2, zhang2023jdomainproteinchaperone pages 3-4).
- Workshop consensus (2019, 2024) emphasizes that most JDPs are constitutively expressed and that "most members are in fact constitutively expressed in cells and... many are not regulated by stress" (kampinga2019functionevolutionand pages 1-2).

Plant genomes encode >100 JDPs with diverse roles in development, abiotic stress, and cellular organization (malinverni2023datadrivenlargescalegenomic pages 3-5, solana2022theastonishinglarge pages 1-2); parasites like *Leishmania* encode 72 HSP40s for life-cycle transitions beyond heat stress (solana2022theastonishinglarge pages 1-2). The term GO:0009408 applies to a **subset** of the family, not universally.

**Recommendation**: **KEEP_AS_NON_CORE** or restrict to heat-inducible subfamily annotations. Alternatively, MODIFY to a child term capturing stress-inducible members while allowing constitutive housekeeping members to lack this annotation.

---

## 3. Functional Divergence Across the Family

| DnaJ Class/Subfamily | Representative Members | J-domain Position | Additional Domains | Primary Function | Heat-Inducible (Yes/No/Varies) | Key Citations |
|---|---|---|---|---|---|---|
| Class A / prototypical DnaJ | *E. coli* DnaJ; mammalian DNAJA proteins; DNAJA2 | N-terminal | G/F-rich region, CTD-I, cysteine-rich zinc-finger-like region, CTD-II, dimerization domain, often disordered C-tail | Generalist Hsp70 co-chaperone; binds non-native substrates, prevents aggregation, stimulates Hsp70 ATPase, supports folding/refolding | Varies; canonical bacterial members are often heat-responsive, but not all homologs are strictly heat-induced | (malinverni2023datadrivenlargescalegenomic pages 1-2, velascocarneros2023theselfassociationequilibrium pages 1-2, zhang2023jdomainproteinchaperone pages 3-4) |
| Class B / canonical | DNAJB1/Hsp40; fungal Sis1; Ydj1-like B-class examples lacking ZFLR | N-terminal | G/F-rich region; often CTD-like substrate-binding domains but no DnaJ zinc-finger region | Hsp70 co-chaperone in proteostasis; recruits Hsp70 to misfolded/aggregated proteins and can promote client crowding on substrates | Varies; many are constitutive and not uniformly heat-regulated | (malinverni2023datadrivenlargescalegenomic pages 1-2, kampinga2019functionevolutionand pages 1-2, zhang2023jdomainproteinchaperone pages 3-4) |
| Class B / specialized ER JDPs | DNAJB11/ERdj3 | N-terminal | Noncanonical class B organization; ER-targeted architecture; pseudo-ZFLR noted in large-scale domain surveys | Specialized ER proteostasis and client handling rather than generic cytosolic heat-shock function | No/Varies; specialized constitutive secretory-pathway role argues against universal heat-response assignment | (malinverni2023datadrivenlargescalegenomic pages 3-5, kampinga2019functionevolutionand pages 1-2) |
| Class C / HscB-family Fe-S biogenesis JDPs | HscB; yeast Jac1; human DNAJC20 | Variable but often N-terminal J-domain linked to specialized module | HSCB_C domain and lineage-specific accessory regions | Dedicated co-chaperones for iron-sulfur cluster biogenesis with specialized Hsp70 partners rather than broad heat-shock response | No; primarily constitutive housekeeping specialization | (malinverni2023datadrivenlargescalegenomic pages 3-5, tomiczek2020twostepmechanismof pages 1-3, zhang2023jdomainproteinchaperone pages 3-4) |
| Class C / Sec63 family | Sec63 / DNAJC23 | Internal or variable depending on lineage architecture | Sec63 domain and membrane-associated regions | Protein translocation across the ER membrane; recruits Hsp70/BiP to translocon-associated clients | No; pathway-specific translocation factor, not a universal heat-shock protein | (malinverni2023datadrivenlargescalegenomic pages 3-5, kampinga2019functionevolutionand pages 1-2) |
| Class C / diverse eukaryotic DNAJC proteins | DNAJC3, DNAJC7, DNAJC11, DNAJC18 and many other DNAJC proteins | Anywhere in protein | Highly diverse architectures; often lineage- or compartment-specific domains | Specialized functions in distinct cellular compartments, partner scaffolding, client selection, signaling, development, and quality control | Varies; many are constitutively expressed and not stress-induced | (zhang2023jdomainproteinchaperone pages 1-3, kampinga2019functionevolutionand pages 1-2, malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 3-4) |
| JD-only or minimally decorated JDPs | DjlB, DjlC, many prokaryotic and eukaryotic JD-only proteins | Variable | Little or no additional annotated domains beyond J-domain | Likely streamlined Hsp70 targeting/co-chaperone functions; indicates family diversity beyond canonical DnaJ architecture | Varies | (malinverni2023datadrivenlargescalegenomic pages 3-5, malinverni2023datadrivenlargescalegenomic pages 1-2) |
| Family-wide summary | ~280,000 JDPs surveyed; 1,945 domain architectures; Class A ~21.0%, Class B ~10.7%, Class C/noncanonical majority | Variable | From full DnaJ architecture to JD-only and many lineage-specific fusions | Family spans general folding, aggregation control, Fe-S cluster assembly, ER translocation, compartment-specific proteostasis, and other specialized roles | Varies; many JDPs are constitutive and not heat-regulated, so GO:0009408 is not universally valid | (malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 1-3, kampinga2019functionevolutionand pages 1-2) |


*Table: This table summarizes the structural and functional heterogeneity across J-domain proteins, from canonical heat-responsive DnaJ homologs to constitutive pathway-specific specialists. It supports the conclusion that GO:0009408 "response to heat" is too broad to assign universally to IPR012724.*

The J-domain protein family exhibits extraordinary diversity:

- **~280,000 J-domain sequences** across all kingdoms, comprising **1,945 distinct domain architectures** with over 1,500 unique domains beyond the J-domain (malinverni2023datadrivenlargescalegenomic pages 3-5, malinverni2023datadrivenlargescalegenomic pages 1-2).
- **Class A** (21% of dataset): Full DnaJ homologs with N-terminal J-domain, G/F region, CTD-I with ZFLR, CTD-II, and dimerization domain. These are closest to canonical heat-shock DnaJ (malinverni2023datadrivenlargescalegenomic pages 3-5, malinverni2023datadrivenlargescalegenomic pages 1-2).
- **Class B** (10.7%): J-domain + G/F region, lacking ZFLR. Includes both generalist co-chaperones (e.g., mammalian DNAJB1) and specialized ER-resident proteins (e.g., DNAJB11/ERdj3) (malinverni2023datadrivenlargescalegenomic pages 3-5, kampinga2019functionevolutionand pages 1-2).
- **Class C** (majority, ~68%): Highly variable architecture with J-domain at any position. Includes HscB-family proteins for Fe-S biogenesis, Sec63 for ER translocation, and hundreds of lineage-specific fusion proteins (malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 3-4).

Approximately **100,483 JDPs** in the analyzed dataset consist of the J-domain alone ("JD-only"), highlighting minimalist specialization (malinverni2023datadrivenlargescalegenomic pages 3-5). Functional specialization examples include:

- **HscB/Jac1/DNAJC20**: Dedicated to iron-sulfur cluster assembly, partnering with specialized Hsp70 HscA/Ssq1; not heat-responsive (malinverni2023datadrivenlargescalegenomic pages 3-5, tomiczek2020twostepmechanismof pages 1-3).
- **Sec63/DNAJC23**: ER membrane-associated, recruits BiP (ER Hsp70) for protein translocation (malinverni2023datadrivenlargescalegenomic pages 3-5, kampinga2019functionevolutionand pages 1-2).
- **Auxilin (DNAJC6)**: Clathrin coat disassembly, recruiting multiple Hsp70s in iterative cycles (zhang2023jdomainproteinchaperone pages 3-4).
- **DnaJ paralogs in bacteria**: In species with multiple DnaK (Hsp70) copies, DnaJ isoforms show subfunctionalization—e.g., *Myxococcus xanthus* MxDnaK1 (heat-induced, cytosolic preference) vs. MxDnaK2 (downregulated by heat, membrane-enriched substrates) (pan2024dnakduplicationand pages 1-2).

**Catalytically inactive variants**: No evidence for catalytically dead J-domains lacking HPD function was found, though HPE motif variants (~1% of sequences) may represent fine-tuned modulation (malinverni2023datadrivenlargescalegenomic pages 3-5). The family diversifies primarily through domain fusion and expression regulation, not loss of core J-domain activity.

---

## 4. Taxonomic Scope

The DnaJ family is **universally distributed** across Bacteria, Archaea, and Eukarya (malinverni2023datadrivenlargescalegenomic pages 1-2, malinverni2023datadrivenlargescalegenomic pages 3-5). The J-domain emerged in terrestrial bacteria and spread through horizontal gene transfer and endosymbiotic gene transfer during eukaryogenesis (malinverni2023datadrivenlargescalegenomic pages 3-5, malinverni2023datadrivenlargescalegenomic pages 1-2). DnaK (Hsp70 partner) is present in 98.9% of bacterial genomes; 6.4% encode DnaK paralogs correlating with increased proteome complexity (pan2024dnakduplicationand pages 1-2). Examples:

- **Bacteria**: E. coli DnaJ, widespread across proteobacteria and other phyla (tomiczek2020twostepmechanismof pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2, mayer2021thehsp70chaperonemachines pages 2-4).
- **Archaea**: Present in mesophilic archaea but absent in some hyperthermophiles that lack Hsp70 systems entirely (mayer2021thehsp70chaperonemachines pages 1-2, mayer2021thehsp70chaperonemachines pages 2-4).
- **Eukarya**: Massive expansion—Arabidopsis >100 JDPs, Leishmania 72, humans ~49 DNAJ genes (kampinga2019functionevolutionand pages 1-2, malinverni2023datadrivenlargescalegenomic pages 3-5, solana2022theastonishinglarge pages 1-2).

**Taxonomic validity of GO terms**:

- **GO:0006457 (protein folding)**: Valid across all taxa—proteostasis via Hsp70 co-chaperones is universal (zhang2023jdomainproteinchaperone pages 1-3, malkeyeva2025heatshockproteins pages 1-2).
- **GO:0005524 (ATP binding)**: Invalid in all taxa—DnaJ does not bind ATP regardless of organism (mayer2021thehsp70chaperonemachines pages 1-2, pan2024dnakduplicationand pages 1-2).
- **GO:0009408 (response to heat)**: Taxonomically variable. Heat-shock response is widespread but many lineage-specific and compartment-specific JDPs are constitutive (kampinga2019functionevolutionand pages 1-2, malinverni2023datadrivenlargescalegenomic pages 3-5).

---

## 5. Over-Annotation Verdict and Recommendations

### Summary Verdict

**IPR012724 InterPro2GO is PARTIALLY OVER-ANNOTATING**, with one major error and one overgeneralization.

### Specific GO Action Recommendations

1. **GO:0005524 (ATP binding)** – **REMOVE**  
   **Rationale**: DnaJ proteins do not bind ATP. ATP binding/hydrolysis is exclusive to the Hsp70 partner. This is a factual error, not a matter of degree.  
   **Supporting evidence**: (tomiczek2020twostepmechanismof pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2, kim2021thednakdnajchaperone pages 1-2, pan2024dnakduplicationand pages 1-2, zhang2023jdomainproteinchaperone pages 3-4).

2. **GO:0006457 (protein folding)** – **ACCEPT** (or refine to GO:0051082 unfolded protein binding + GO:0051087 chaperone binding)  
   **Rationale**: The family universally functions in Hsp70-mediated proteostasis and protein folding. While imprecise (JDPs are co-chaperones, not direct folding enzymes), this captures the core biological process.  
   **Supporting evidence**: (zhang2023jdomainproteinchaperone pages 1-3, mayer2021thehsp70chaperonemachines pages 1-2, malkeyeva2025heatshockproteins pages 1-2, kampinga2019functionevolutionand pages 1-2).

3. **GO:0009408 (response to heat)** – **KEEP_AS_NON_CORE** or **MODIFY to subfamily-specific annotation**  
   **Rationale**: Many DnaJ proteins are heat-inducible (especially canonical bacterial DnaJ and mammalian DNAJB1), but the family includes many constitutive, specialized members (HscB, Sec63, tissue-specific DNAJC proteins) for which heat response is not relevant. The term applies to a subset, not the whole family.  
   **Supporting evidence**: (kampinga2019functionevolutionand pages 1-2, malinverni2023datadrivenlargescalegenomic pages 3-5, zhang2023jdomainproteinchaperone pages 1-3, mayer2021thehsp70chaperonemachines pages 2-4, zhang2023jdomainproteinchaperone pages 3-4).  
   **Alternative**: Create child InterPro entries for heat-inducible vs. constitutive subfamilies and apply GO:0009408 only to the former.

### InterPro Structure Recommendation

Because IPR012724 is a **family**-level entry, the current GO:0009408 assignment assumes functional homogeneity that does not exist. Consider:

- **Subdividing IPR012724** into heat-shock-responsive (Class A canonical) vs. specialized constitutive subfamilies (HscB-like, Sec63-like, etc.).
- **Moving GO:0009408** to a child entry representing only stress-responsive members.
- **Retaining only core co-chaperone functions** (protein folding, chaperone binding) at the family level.

---

## Conclusion

The InterPro entry IPR012724 (Chaperone DnaJ) captures a functionally diverse superfamily united by the conserved J-domain, which universally stimulates Hsp70 ATPase activity to drive proteostasis. However, current InterPro2GO annotations include a factual error (ATP binding) and an overgeneralization (heat response) that do not apply to all 35,613 proteins matched by this signature. **Recommended actions**: REMOVE GO:0005524, ACCEPT GO:0006457, and either demote GO:0009408 to non-core status or restrict it to a heat-inducible subfamily. This will align GO annotations with the mechanistic and evolutionary evidence from 2020–2024 literature.

---

**Report compiled from 34 papers (11 directly cited), prioritizing authoritative reviews and primary research from 2023–2024 (Zhang et al. 2023, Malinverni et al. 2023, Pan et al. 2024, Malkeyeva et al. 2025, Kampinga et al. 2019) alongside foundational mechanistic studies (Tomiczek et al. 2020, Mayer 2021).**

References

1. (zhang2023jdomainproteinchaperone pages 3-4): Ruobing Zhang, Duccio Malinverni, Douglas M. Cyr, Paolo De Los Rios, and Nadinath B. Nillegoda. J-domain protein chaperone circuits in proteostasis and disease. Trends in Cell Biology, 33:30-47, Jan 2023. URL: https://doi.org/10.1016/j.tcb.2022.05.004, doi:10.1016/j.tcb.2022.05.004. This article has 64 citations and is from a domain leading peer-reviewed journal.

2. (malinverni2023datadrivenlargescalegenomic pages 1-2): Duccio Malinverni, Stefano Zamuner, Mathieu E. Rebeaud, Alessandro Barducci, Nadinath B. Nillegoda, and Paolo De Los Rios. Data-driven large-scale genomic analysis reveals an intricate phylogenetic and functional landscape in j-domain proteins. Proceedings of the National Academy of Sciences, Jul 2023. URL: https://doi.org/10.1073/pnas.2218217120, doi:10.1073/pnas.2218217120. This article has 39 citations and is from a highest quality peer-reviewed journal.

3. (tomiczek2020twostepmechanismof pages 1-3): Bartlomiej Tomiczek, Wojciech Delewski, Łukasz Nierzwicki, Milena Stolarska, Igor Grochowina, Brenda Schilke, Rafał Dutkiewicz, Marta A. Uzarska, Szymon J. Ciesielski, Jacek Czub, and Jaroslaw Marszalek. Two-step mechanism of j-domain action in driving hsp70 function. PLoS Computational Biology, Jan 2020. URL: https://doi.org/10.1101/2020.01.13.901538, doi:10.1101/2020.01.13.901538. This article has 41 citations and is from a highest quality peer-reviewed journal.

4. (kim2021thednakdnajchaperone pages 1-2): Ju-Sim Kim, Lin Liu, and Andrés Vázquez-Torres. The dnak/dnaj chaperone system enables rna polymerase-dksa complex formation in salmonella experiencing oxidative stress. mBio, Jun 2021. URL: https://doi.org/10.1128/mbio.03443-20, doi:10.1128/mbio.03443-20. This article has 35 citations and is from a domain leading peer-reviewed journal.

5. (malinverni2023datadrivenlargescalegenomic pages 3-5): Duccio Malinverni, Stefano Zamuner, Mathieu E. Rebeaud, Alessandro Barducci, Nadinath B. Nillegoda, and Paolo De Los Rios. Data-driven large-scale genomic analysis reveals an intricate phylogenetic and functional landscape in j-domain proteins. Proceedings of the National Academy of Sciences, Jul 2023. URL: https://doi.org/10.1073/pnas.2218217120, doi:10.1073/pnas.2218217120. This article has 39 citations and is from a highest quality peer-reviewed journal.

6. (mayer2021thehsp70chaperonemachines pages 1-2): Matthias P. Mayer. The hsp70-chaperone machines in bacteria. Frontiers in Molecular Biosciences, Jun 2021. URL: https://doi.org/10.3389/fmolb.2021.694012, doi:10.3389/fmolb.2021.694012. This article has 100 citations.

7. (pan2024dnakduplicationand pages 1-2): Zhuo Pan, Li Zhuo, Tian-yu Wan, Rui-yun Chen, and Yue-zhong Li. Dnak duplication and specialization in bacteria correlates with increased proteome complexity. Apr 2024. URL: https://doi.org/10.1128/msystems.01154-23, doi:10.1128/msystems.01154-23. This article has 10 citations and is from a peer-reviewed journal.

8. (malkeyeva2025heatshockproteins pages 1-2): D. Malkeyeva, E. V. Kiseleva, and S. A. Fedorova. Heat shock proteins in protein folding and reactivation. Vavilov Journal of Genetics and Breeding, 29:7-14, Mar 2025. URL: https://doi.org/10.18699/vjgb-25-02, doi:10.18699/vjgb-25-02. This article has 7 citations.

9. (velascocarneros2023theselfassociationequilibrium pages 1-2): Lorea Velasco-Carneros, Jorge Cuéllar, Leire Dublang, César Santiago, Jean-Didier Maréchal, Jaime Martín-Benito, Moisés Maestro, José Ángel Fernández-Higuero, Natalia Orozco, Fernando Moro, José María Valpuesta, and Arturo Muga. The self-association equilibrium of dnaja2 regulates its interaction with unfolded substrate proteins and with hsc70. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41150-8, doi:10.1038/s41467-023-41150-8. This article has 23 citations and is from a highest quality peer-reviewed journal.

10. (zhang2023jdomainproteinchaperone pages 1-3): Ruobing Zhang, Duccio Malinverni, Douglas M. Cyr, Paolo De Los Rios, and Nadinath B. Nillegoda. J-domain protein chaperone circuits in proteostasis and disease. Trends in Cell Biology, 33:30-47, Jan 2023. URL: https://doi.org/10.1016/j.tcb.2022.05.004, doi:10.1016/j.tcb.2022.05.004. This article has 64 citations and is from a domain leading peer-reviewed journal.

11. (kampinga2019functionevolutionand pages 1-2): Harm H. Kampinga, Claes Andreasson, Alessandro Barducci, Michael E. Cheetham, Douglas Cyr, Cecilia Emanuelsson, Pierre Genevaux, Jason E. Gestwicki, Pierre Goloubinoff, Jaime Huerta-Cepas, Janine Kirstein, Krzysztof Liberek, Matthias P. Mayer, Kazuhiro Nagata, Nadinath B. Nillegoda, Pablo Pulido, Carlos Ramos, Paolo De los Rios, Sabine Rospert, Rina Rosenzweig, Chandan Sahi, Mikko Taipale, Bratłomiej Tomiczek, Ryo Ushioda, Jason C. Young, Richard Zimmermann, Alicja Zylicz, Maciej Zylicz, Elizabeth A. Craig, and Jaroslaw Marszalek. Function, evolution, and structure of j-domain proteins. Cell Stress and Chaperones, 24:7-15, Jan 2019. URL: https://doi.org/10.1007/s12192-018-0948-4, doi:10.1007/s12192-018-0948-4. This article has 219 citations and is from a peer-reviewed journal.

12. (mayer2021thehsp70chaperonemachines pages 2-4): Matthias P. Mayer. The hsp70-chaperone machines in bacteria. Frontiers in Molecular Biosciences, Jun 2021. URL: https://doi.org/10.3389/fmolb.2021.694012, doi:10.3389/fmolb.2021.694012. This article has 100 citations.

13. (figaj2025theroleof pages 1-2): Donata Figaj. The role of heat shock protein (hsp) chaperones in environmental stress adaptation and virulence of plant pathogenic bacteria. International Journal of Molecular Sciences, 26:528, Jan 2025. URL: https://doi.org/10.3390/ijms26020528, doi:10.3390/ijms26020528. This article has 31 citations.

14. (solana2022theastonishinglarge pages 1-2): Jose Carlos Solana, Lorena Bernardo, Javier Moreno, Begoña Aguado, and Jose M. Requena. The astonishing large family of hsp40/dnaj proteins existing in leishmania. Genes, 13:742, Apr 2022. URL: https://doi.org/10.3390/genes13050742, doi:10.3390/genes13050742. This article has 17 citations.

## Artifacts

- [Edison artifact artifact-00](IPR012724-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](IPR012724-deep-research-falcon_artifacts/artifact-01.md)

## Citations

1. zhang2023jdomainproteinchaperone pages 3-4
2. malinverni2023datadrivenlargescalegenomic pages 3-5
3. tomiczek2020twostepmechanismof pages 1-3
4. kampinga2019functionevolutionand pages 1-2
5. solana2022theastonishinglarge pages 1-2
6. pan2024dnakduplicationand pages 1-2
7. malinverni2023datadrivenlargescalegenomic pages 1-2
8. kim2021thednakdnajchaperone pages 1-2
9. malkeyeva2025heatshockproteins pages 1-2
10. velascocarneros2023theselfassociationequilibrium pages 1-2
11. zhang2023jdomainproteinchaperone pages 1-3
12. figaj2025theroleof pages 1-2
13. dnaJ
14. F
15. P
16. https://doi.org/10.1016/j.tcb.2022.05.004,
17. https://doi.org/10.1073/pnas.2218217120,
18. https://doi.org/10.1101/2020.01.13.901538,
19. https://doi.org/10.1128/mbio.03443-20,
20. https://doi.org/10.3389/fmolb.2021.694012,
21. https://doi.org/10.1128/msystems.01154-23,
22. https://doi.org/10.18699/vjgb-25-02,
23. https://doi.org/10.1038/s41467-023-41150-8,
24. https://doi.org/10.1007/s12192-018-0948-4,
25. https://doi.org/10.3390/ijms26020528,
26. https://doi.org/10.3390/genes13050742,