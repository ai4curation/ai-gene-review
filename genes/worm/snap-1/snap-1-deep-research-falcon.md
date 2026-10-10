---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:51:05.184872'
end_time: '2026-09-27T16:01:20.522501'
duration_seconds: 615.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: snap-1
  gene_symbol: snap-1
  uniprot_accession: Q18921
  protein_description: 'SubName: Full=Alpha-soluble NSF attachment protein {ECO:0000313|EMBL:CCD68312.1};'
  gene_info: Name=snap-1 {ECO:0000313|EMBL:CCD68312.1, ECO:0000313|WormBase:D1014.3a};
    ORFNames=CELE_D1014.3 {ECO:0000313|EMBL:CCD68312.1}, D1014.3 {ECO:0000313|WormBase:D1014.3a};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the SNAP family. {ECO:0000256|ARBA:ARBA00010050,
  protein_domains: NSF_attach. (IPR000744); TPR-like_helical_dom_sf. (IPR011990);
    SNAP (PF14938)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: snap-1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q18921
- **Protein Description:** SubName: Full=Alpha-soluble NSF attachment protein {ECO:0000313|EMBL:CCD68312.1};
- **Gene Information:** Name=snap-1 {ECO:0000313|EMBL:CCD68312.1, ECO:0000313|WormBase:D1014.3a}; ORFNames=CELE_D1014.3 {ECO:0000313|EMBL:CCD68312.1}, D1014.3 {ECO:0000313|WormBase:D1014.3a};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the SNAP family. {ECO:0000256|ARBA:ARBA00010050,
- **Key Domains:** NSF_attach. (IPR000744); TPR-like_helical_dom_sf. (IPR011990); SNAP (PF14938)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "snap-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'snap-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **snap-1** (gene ID: snap-1, UniProt: Q18921) in worm.

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
- **UniProt Accession:** Q18921
- **Protein Description:** SubName: Full=Alpha-soluble NSF attachment protein {ECO:0000313|EMBL:CCD68312.1};
- **Gene Information:** Name=snap-1 {ECO:0000313|EMBL:CCD68312.1, ECO:0000313|WormBase:D1014.3a}; ORFNames=CELE_D1014.3 {ECO:0000313|EMBL:CCD68312.1}, D1014.3 {ECO:0000313|WormBase:D1014.3a};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the SNAP family. {ECO:0000256|ARBA:ARBA00010050,
- **Key Domains:** NSF_attach. (IPR000744); TPR-like_helical_dom_sf. (IPR011990); SNAP (PF14938)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "snap-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'snap-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **snap-1** (gene ID: snap-1, UniProt: Q18921) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *C. elegans snap-1* (UniProt Q18921)

## Executive conclusion

The identity is internally consistent: the target is *Caenorhabditis elegans snap-1* (ORF D1014.3; UniProt Q18921), not neuronal SNAP-25, SNAP29, or a similarly named protein from another organism. Published worm literature pairs *snap-1* with the chromosome V lethal locus *let-408* and annotates its product as alpha-soluble NSF attachment protein (α-SNAP). The D1014.3/Q18921 cross-reference itself comes from the supplied UniProt record rather than the retrieved papers. Its SNAP-family, NSF-attachment, and TPR-like helical-domain annotations agree with α-SNAP’s established architecture and adaptor function (Qin et al., published March 2018; https://doi.org/10.1534/g3.117.300338). (qin2018genomicidentificationand pages 35-37)

The most defensible primary annotation is: **SNAP-1 is an essential, soluble, nonenzymatic α-SNAP adaptor that is expected to bind assembled SNARE complexes and recruit/position the AAA+ ATPase NSF for ATP-dependent SNARE-complex disassembly and recycling.** SNAP-1 itself does not catalyze a chemical reaction and has no conventional small-molecule substrate; its macromolecular substrate is an assembled SNARE complex, while NSF supplies ATPase activity. This molecular assignment is strongly supported for the α-SNAP family, but direct biochemical reconstitution with worm Q18921 has not been reported in the literature retrieved here. (sauvola2021snareregulatoryproteins pages 12-13, white2018structuralprinciplesof pages 1-2, yang2024theroleof pages 3-4)

| Topic | Best-supported conclusion | Evidence type/organism | Confidence/limitations | Key source (author year DOI/URL) |
|---|---|---|---|---|
| Identity | *C. elegans* **snap-1** corresponds to the chromosome V lethal locus **let-408** and encodes an alpha-soluble NSF attachment protein; Q18921/D1014.3 linkage is supplied by UniProt. | Direct literature annotation in *C. elegans* plus supplied UniProt record | **High** for snap-1/let-408/protein description; the cited paper excerpt does not independently state Q18921 or D1014.3. | Qin et al. 2018, [doi:10.1534/g3.117.300338](https://doi.org/10.1534/g3.117.300338) (qin2018genomicidentificationand pages 35-37) |
| Worm phenotypes | **snap-1 RNAi** was associated with defective embryonic osmotic integrity; the **tm2068 deletion** is reported as sterile/lethal. | Direct *C. elegans* phenotype summary, citing RNAi and deletion evidence | **Moderate–high** association; available text provides no penetrance, sample size, stage resolution, rescue, or direct trafficking assay, so the precise causal membrane-trafficking defect remains unresolved. | Stein & Golden 2018, [doi:10.1895/wormbook.1.179.1](https://doi.org/10.1895/wormbook.1.179.1) (stein2018thec.elegans pages 40-41) |
| Primary molecular role | SNAP-1 is best annotated as a **nonenzymatic alpha-SNAP adaptor**: it recognizes assembled SNARE complexes, recruits/positions NSF, and enables NSF-driven, ATP-dependent SNARE disassembly and recycling. ATP hydrolysis is performed by NSF, not SNAP-1. | Strong biochemical/structural evidence in mammalian and reconstituted systems; inference to worm Q18921 from conserved family/domain identity | **High** for alpha-SNAP proteins generally; **moderate** for Q18921 specifically because direct worm binding, ATPase-stimulation, or reconstitution data were not found. | White et al. 2018, [doi:10.7554/eLife.38888](https://doi.org/10.7554/eLife.38888); Sauvola & Littleton 2021, [doi:10.3389/fnmol.2021.733138](https://doi.org/10.3389/fnmol.2021.733138) (sauvola2021snareregulatoryproteins pages 12-13, white2018structuralprinciplesof pages 1-2) |
| Likely localization | Expected to be a **soluble cytosolic/peripheral-membrane protein** recruited transiently to assembled SNARE complexes on SNARE-bearing membranes, including secretory, Golgi/ER-trafficking, endosomal, and synaptic membranes as context requires. It is not predicted to be an integral membrane protein. | Localization inferred from conserved alpha-SNAP mechanism and soluble SNAP-family architecture; not directly mapped for worm SNAP-1 | **Moderate inference**; no convincing SNAP-1-specific *C. elegans* microscopy or organelle-resolved localization was identified, so assigning it exclusively to Golgi, synapse, or eggshell vesicles would overstate the evidence. | White et al. 2018, [doi:10.7554/eLife.38888](https://doi.org/10.7554/eLife.38888); Huang et al. 2019, [doi:10.1126/sciadv.aau8164](https://doi.org/10.1126/sciadv.aau8164) (white2018structuralprinciplesof pages 1-2, huang2019mechanisticinsightsinto pages 1-2) |
| Structural/mechanistic evidence | Captured complexes show differing alpha-SNAP stoichiometries: **two alpha-SNAPs** in one approximately **3.9 Å** NSF–alpha-SNAP–SNARE reconstruction, versus **four alpha-SNAPs** wrapped around a SNARE bundle in another structure; the latter resolved alpha-SNAP–SNARE and NSF-D1D2 portions at **3.9 Å and 3.7 Å**. Alpha-SNAP **R116A** and **L197A** retained only about **2% and 5%** of wild-type disassembly activity, respectively. | Direct cryo-EM, mutational, biochemical, and neuronal-assay evidence using mammalian/reconstituted components | **High** for conserved mechanistic principles; stoichiometry depends on construct/state and should not be treated as a fixed SNAP-1 copy number in worms. Residue equivalence in Q18921 requires sequence alignment and experimental validation. | White et al. 2018, [doi:10.7554/eLife.38888](https://doi.org/10.7554/eLife.38888); Huang et al. 2019, [doi:10.1126/sciadv.aau8164](https://doi.org/10.1126/sciadv.aau8164) (huang2019mechanisticinsightsinto pages 3-4, white2018structuralprinciplesof pages 1-2, huang2019mechanisticinsightsinto pages 1-2) |
| 2024 update | A 2024 review reaffirms that SNAP recruits NSF and that NSF ATP hydrolysis disassembles SNARE complexes for recycling. The reviewed search set yielded **no new 2023–2024 snap-1-specific worm mechanistic or localization study**. | Current review of NSF/SNAP biology; literature-gap assessment for *C. elegans* snap-1 | **High** for the conserved consensus, but not new direct evidence about Q18921. Absence from the retrieved literature is not proof that no relevant dataset exists. | Yang et al. 2024, published October 2024, [doi:10.3389/fnins.2024.1395294](https://doi.org/10.3389/fnins.2024.1395294) (yang2024theroleof pages 3-4) |


*Table: Evidence-tier summary separating direct C. elegans findings from conserved alpha-SNAP-based functional and localization inferences for snap-1/Q18921.*

## 1. Identity verification and ambiguity control

The literature explicitly identifies *snap-1* as the gene associated with *let-408* on chromosome V and describes the encoded protein as α-soluble NSF attachment protein. This matches the supplied UniProt description for Q18921 and supports proceeding with α-SNAP-family evidence. (qin2018genomicidentificationand pages 35-37)

Several potentially confusing proteins were excluded. **SNAP-25 and SNAP29 are SNARE proteins**, whereas α-SNAP is a soluble NSF-recruiting adaptor; similarity of nomenclature does not imply identity. Literature concerning C. elegans SNAP29-dependent lysosomal exocytosis, for example, is not evidence about Q18921. Likewise, “snap freezing” and genes from other organisms returned by broad searches were disregarded.

The supplied domain calls—NSF_attach (IPR000744), TPR-like helical-domain superfamily (IPR011990), and SNAP family/PF14938—are mutually compatible. α-SNAP is predominantly helical and presents extended interaction surfaces suited to recognizing the assembled SNARE bundle and engaging NSF. Structural work in other animal systems confirms this adaptor architecture. (huang2019mechanisticinsightsinto pages 3-4, white2018structuralprinciplesof pages 1-2)

## 2. Primary molecular function

### 2.1 Position in the membrane-fusion cycle

SNARE proteins on opposing membranes assemble into a trans-SNARE bundle that drives membrane fusion. After fusion, the SNAREs reside together in a cis-complex on one membrane. α-SNAP recognizes the assembled bundle, helps form an NSF–α-SNAP–SNARE “20S” disassembly complex, and positions SNARE polypeptide for engagement by NSF. NSF then converts ATP-hydrolysis energy into mechanical unfolding/separation of the SNARE bundle, releasing individual SNAREs for another trafficking cycle. (white2018structuralprinciplesof pages 1-2, yang2024theroleof pages 3-4, huang2019mechanisticinsightsinto pages 1-2)

Accordingly, SNAP-1 is best classified as a **protein-complex adaptor and remodeling cofactor**, not an enzyme, transporter, structural membrane protein, or receptor. Its substrate specificity is expected to be conformational: α-SNAP recognizes the surface and electrostatic properties of an **assembled SNARE helical bundle**, rather than one narrowly defined metabolite or cargo. The family can act on post-fusion cis-SNARE complexes and can also facilitate removal of malformed or off-pathway SNARE assemblies, giving it a probable SNARE-quality-control role. (white2018structuralprinciplesof pages 1-2, choi2018nsfmediateddisassemblyof pages 6-7)

### 2.2 Structural and quantitative evidence

Cryo-EM analysis resolved an NSF–α-SNAP–neuronal SNARE assembly at approximately 3.9 Å. Two α-SNAP molecules contacted a specific SNARE-complex surface and oriented the substrate such that the first 15 residues of SNAP-25A entered the NSF D1 pore; subsequent ATP hydrolysis was proposed to drive complete disassembly. NSF is a homohexamer containing an N-terminal substrate/adaptor-binding domain and D1/D2 ATPase rings. (white2018structuralprinciplesof pages 1-2)

A separate cryo-EM study resolved α-SNAP–SNARE and NSF-D1D2 regions at 3.9 and 3.7 Å, respectively, and observed four α-SNAP molecules around one SNARE bundle. α-SNAP R116 contacted acidic VAMP residues, whereas L197 made hydrophobic contacts with VAMP. R116A and L197A variants retained only approximately 2% and 5% of wild-type disassembly activity. These results demonstrate that α-SNAP actively couples SNARE recognition to mechanical disassembly rather than merely serving as an inert tether. The differing observed stoichiometries likely reflect construct or conformational-state differences and should not be interpreted as a fixed number of worm SNAP-1 molecules per complex. (huang2019mechanisticinsightsinto pages 3-4, huang2019mechanisticinsightsinto pages 1-2)

Single-molecule work further showed that NSF/α-SNAP can disassemble both productive and antiparallel SNARE complexes and that reducing α-SNAP concentration or weakening electrostatic contacts reduces disassembly. Thus, charged surfaces in α-SNAP contribute substantially to substrate recognition and complex remodeling. (choi2018nsfmediateddisassemblyof pages 6-7)

These residue-level findings are **not direct measurements of Q18921**. Assigning equivalent functional residues in worm SNAP-1 would require a sequence alignment followed by mutagenesis and biochemical validation.

## 3. Biological processes and pathways

The immediate pathway assignment is the **NSF-dependent SNARE assembly/disassembly cycle**, a universal component of intracellular membrane trafficking. Consequent processes may include ER–Golgi and intra-Golgi traffic, endosomal traffic, constitutive secretion, regulated exocytosis, and synaptic-vesicle recycling. However, these broader assignments remain family-based inference until SNAP-1 is examined in compartment-specific worm assays. (sauvola2021snareregulatoryproteins pages 12-13, yang2024theroleof pages 3-4)

The 2018 essential-gene study notes that the mouse ortholog is required for vesicular transport between the ER and Golgi. This is useful orthology-based support for secretory-pathway involvement, but it does not establish that ER–Golgi transport is SNAP-1’s exclusive or experimentally demonstrated site of action in *C. elegans*. (qin2018genomicidentificationand pages 35-37)

At synapses, the conserved model places NSF/α-SNAP downstream of fusion, where disassembly replenishes reusable SNAREs and supports maintenance of releasable vesicle pools. Nevertheless, a 2021 review explicitly noted that C. elegans synaptic phenotypes attributable specifically to NSF or α-SNAP mutations had not been reported. Therefore, Q18921 should not currently be described as a worm-specific synaptic factor on direct evidence alone. (sauvola2021snareregulatoryproteins pages 12-13)

## 4. Cellular and subcellular localization

SNAP-1 is expected to be **intracellular and soluble in the cytosol**, with transient peripheral recruitment to SNARE-containing membranes. It lacks the conceptual role of an integral membrane SNARE: instead, assembled SNARE complexes recruit α-SNAP to organellar or plasma membranes, where NSF joins the complex. Likely sites therefore include Golgi/ER trafficking intermediates, endosomes, secretory vesicles, and presynaptic membranes, depending on cell type and physiological context. This is a mechanistic localization inference from the α-SNAP family, not a direct Q18921 imaging result. (white2018structuralprinciplesof pages 1-2, huang2019mechanisticinsightsinto pages 1-2)

No convincing SNAP-1-specific *C. elegans* microscopy, organelle colocalization, secretion assay, or cell-type-resolved localization study was recovered. It would therefore be premature to assign SNAP-1 exclusively to the Golgi, nervous system, eggshell-producing vesicles, or any particular tissue.

## 5. Direct *C. elegans* genetic and phenotypic evidence

The clearest organism-specific evidence is genetic. *snap-1* is associated with the lethal locus *let-408*, supporting an essential developmental function. (qin2018genomicidentificationand pages 35-37)

A WormBook eggshell synthesis summarized RNAi evidence associating *snap-1* depletion with **defective embryonic osmotic integrity** and listed the *tm2068* deletion allele as **sterile/lethal**. These findings connect SNAP-1 to a trafficking-dependent process required for embryonic integrity and organismal viability. However, the available summary provides no sample size, penetrance, developmental timing, rescue experiment, cargo measurement, or direct membrane-trafficking readout. It therefore does not prove that SNAP-1 directly assembles the eggshell or permeability barrier; a parsimonious interpretation is that disruption of essential membrane trafficking secondarily impairs delivery or organization of components needed for embryonic osmotic protection. (stein2018thec.elegans pages 40-41)

The direct evidence hierarchy is consequently:

1. **High confidence:** gene/protein identity as worm α-SNAP and association with an essential locus. (qin2018genomicidentificationand pages 35-37)
2. **Moderate confidence:** requirement for fertility/viability and embryonic osmotic integrity, based on deletion/RNAi summaries. (stein2018thec.elegans pages 40-41)
3. **Strong family-level but indirect evidence:** NSF recruitment, assembled-SNARE recognition, and ATP-dependent SNARE recycling. (huang2019mechanisticinsightsinto pages 3-4, white2018structuralprinciplesof pages 1-2, huang2019mechanisticinsightsinto pages 1-2)
4. **Currently unresolved in the worm:** exact SNARE partners, tissue expression, organelle distribution, trafficking cargo, stage-specific requirement, and whether synaptic transmission is a major physiological context.

## 6. Recent developments, 2023–2024

No 2023–2024 primary study directly characterizing C. elegans SNAP-1/Q18921 was found. The recent literature instead refines the conserved NSF/SNAP framework. A review published in October 2024 reaffirmed that SNAP proteins bind SNARE complexes, recruit NSF, regulate its ATPase cycle, and allow SNARE reuse after ATP-dependent disassembly. It described NSF’s N domain as the SNAP/SNARE-binding module, D1 as the principal ATP-hydrolyzing motor, and D2 as important for ATP binding and maintenance of the hexamer. (yang2024theroleof pages 3-4)

A manuscript first posted in October 2024 and subsequently represented in the retrieved corpus as a later publication extended the model beyond post-fusion recycling: NSF/α-SNAP assemblies were reported to remodel syntaxin oligomers and syntaxin–SNAP-25 binary complexes before fusion, suggesting roles in liberating functional syntaxin and clearing off-pathway assemblies. Because this evidence is not worm-specific and its retrieved record reflects later publication status, it should be treated as an emerging refinement rather than direct annotation evidence for Q18921. (white2025prefusionaaa+remodeling pages 1-5)

Thus, current expert understanding strengthens the annotation of α-SNAP as a general SNARE-remodeling and quality-control adaptor, but it does not close the principal gene-specific gaps for *C. elegans snap-1*.

## 7. Recommended functional annotation

**Suggested concise annotation:**

> *snap-1* encodes the *C. elegans* alpha-soluble NSF attachment protein, an essential, nonenzymatic SNAP-family adaptor predicted to bind assembled SNARE complexes and recruit the AAA+ ATPase NSF, thereby enabling ATP-dependent SNARE-complex disassembly and recycling during intracellular membrane trafficking. Genetic depletion is associated with defective embryonic osmotic integrity, while a deletion allele is reported as sterile/lethal. Its precise cell-type distribution, organellar localization, SNARE partners, and trafficking cargoes in *C. elegans* remain unresolved.

The most informative next experiments would be endogenous SNAP-1 fluorescent tagging with functional rescue controls; stage- and tissue-specific depletion; colocalization with ER, Golgi, endosomal, and synaptic markers; co-immunoprecipitation or proximity labeling of NSF/SNARE partners; and purified Q18921 assays measuring SNARE binding, NSF recruitment, ATPase stimulation, and complex disassembly. These experiments would directly test the currently orthology-based molecular annotation and determine which trafficking compartment explains the essential embryonic phenotype.

References

1. (qin2018genomicidentificationand pages 35-37): Zhaozhao Qin, Robert Johnsen, Shicheng Yu, Jeffrey Shih-Chieh Chu, David L Baillie, and Nansheng Chen. Genomic identification and functional characterization of essential genes in <i>caenorhabditis elegans</i>. Mar 2018. URL: https://doi.org/10.1534/g3.117.300338, doi:10.1534/g3.117.300338. This article has 30 citations.

2. (sauvola2021snareregulatoryproteins pages 12-13): Chad W. Sauvola and J. Troy Littleton. Snare regulatory proteins in synaptic vesicle fusion and recycling. Frontiers in Molecular Neuroscience, Aug 2021. URL: https://doi.org/10.3389/fnmol.2021.733138, doi:10.3389/fnmol.2021.733138. This article has 80 citations.

3. (white2018structuralprinciplesof pages 1-2): K Ian White, Minglei Zhao, Ucheor B Choi, Richard A Pfuetzner, and Axel T Brunger. Structural principles of snare complex recognition by the aaa+ protein nsf. eLife, Sep 2018. URL: https://doi.org/10.7554/elife.38888, doi:10.7554/elife.38888. This article has 99 citations and is from a domain leading peer-reviewed journal.

4. (yang2024theroleof pages 3-4): Jingyue Yang, Lingyue Kong, Li Zou, and Yumin Liu. The role of synaptic protein nsf in the development and progression of neurological diseases. Frontiers in Neuroscience, Oct 2024. URL: https://doi.org/10.3389/fnins.2024.1395294, doi:10.3389/fnins.2024.1395294. This article has 14 citations and is from a peer-reviewed journal.

5. (stein2018thec.elegans pages 40-41): Kathryn K. Stein and A. Golden. The c. elegans eggshell. ArXiv, 4:1-36, Aug 2018. URL: https://doi.org/10.1895/wormbook.1.179.1, doi:10.1895/wormbook.1.179.1. This article has 68 citations.

6. (huang2019mechanisticinsightsinto pages 1-2): Xuan Huang, Shan Sun, Xiaojing Wang, Fenghui Fan, Qiang Zhou, Shan Lu, Yong Cao, Qiu-Wen Wang, Meng-Qiu Dong, Jun Yao, and Sen-Fang Sui. Mechanistic insights into the snare complex disassembly. Science Advances, Apr 2019. URL: https://doi.org/10.1126/sciadv.aau8164, doi:10.1126/sciadv.aau8164. This article has 52 citations and is from a highest quality peer-reviewed journal.

7. (huang2019mechanisticinsightsinto pages 3-4): Xuan Huang, Shan Sun, Xiaojing Wang, Fenghui Fan, Qiang Zhou, Shan Lu, Yong Cao, Qiu-Wen Wang, Meng-Qiu Dong, Jun Yao, and Sen-Fang Sui. Mechanistic insights into the snare complex disassembly. Science Advances, Apr 2019. URL: https://doi.org/10.1126/sciadv.aau8164, doi:10.1126/sciadv.aau8164. This article has 52 citations and is from a highest quality peer-reviewed journal.

8. (choi2018nsfmediateddisassemblyof pages 6-7): Ucheor B Choi, Minglei Zhao, K Ian White, Richard A Pfuetzner, Luis Esquivies, Qiangjun Zhou, and Axel T Brunger. Nsf-mediated disassembly of on- and off-pathway snare complexes and inhibition by complexin. Jul 2018. URL: https://doi.org/10.7554/elife.36497, doi:10.7554/elife.36497. This article has 55 citations and is from a domain leading peer-reviewed journal.

9. (white2025prefusionaaa+remodeling pages 1-5): K. Ian White, Yousuf A. Khan, Kangqiang Qiu, Ashwin Balaji, Sergio Couoh-Cardel, Luis Esquivies, Richard A. Pfuetzner, Jiajie Diao, and Axel T. Brunger. Pre-fusion aaa+ remodeling of target-snare protein complexes enables synaptic transmission. bioRxiv, Oct 2025. URL: https://doi.org/10.1101/2024.10.11.617886, doi:10.1101/2024.10.11.617886. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](snap-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. qin2018genomicidentificationand pages 35-37
2. yang2024theroleof pages 3-4
3. white2018structuralprinciplesof pages 1-2
4. choi2018nsfmediateddisassemblyof pages 6-7
5. sauvola2021snareregulatoryproteins pages 12-13
6. huang2019mechanisticinsightsinto pages 1-2
7. huang2019mechanisticinsightsinto pages 3-4
8. doi:10.1534/g3.117.300338
9. doi:10.1895/wormbook.1.179.1
10. doi:10.7554/eLife.38888
11. doi:10.3389/fnmol.2021.733138
12. doi:10.1126/sciadv.aau8164
13. doi:10.3389/fnins.2024.1395294
14. https://doi.org/10.1534/g3.117.300338
15. https://doi.org/10.1895/wormbook.1.179.1
16. https://doi.org/10.7554/eLife.38888
17. https://doi.org/10.3389/fnmol.2021.733138
18. https://doi.org/10.1126/sciadv.aau8164
19. https://doi.org/10.3389/fnins.2024.1395294
20. https://doi.org/10.1534/g3.117.300338,
21. https://doi.org/10.3389/fnmol.2021.733138,
22. https://doi.org/10.7554/elife.38888,
23. https://doi.org/10.3389/fnins.2024.1395294,
24. https://doi.org/10.1895/wormbook.1.179.1,
25. https://doi.org/10.1126/sciadv.aau8164,
26. https://doi.org/10.7554/elife.36497,
27. https://doi.org/10.1101/2024.10.11.617886,