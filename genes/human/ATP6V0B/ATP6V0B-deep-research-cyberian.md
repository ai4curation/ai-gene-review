---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T01:08:54.990637'
end_time: '2026-01-24T01:20:52.468925'
duration_seconds: 717.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ATP6V0B
  gene_symbol: ATP6V0B
  uniprot_accession: Q99437
  protein_description: 'RecName: Full=V-type proton ATPase 21 kDa proteolipid subunit
    c'''' {ECO:0000305}; Short=V-ATPase 21 kDa proteolipid subunit c'''' {ECO:0000305};
    AltName: Full=Vacuolar proton pump 21 kDa proteolipid subunit c'''' {ECO:0000305};
    AltName: Full=hATPL;'
  gene_info: Name=ATP6V0B; Synonyms=ATP6F;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the V-ATPase proteolipid subunit family.
  protein_domains: ATPase_proteolipid_c-like_dom. (IPR002379); ATPase_proteolipid_csu.
    (IPR000245); F/V-ATP_Csub_sf. (IPR035921); ATP-synt_C (PF00137)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q99437
- **Protein Description:** RecName: Full=V-type proton ATPase 21 kDa proteolipid subunit c'' {ECO:0000305}; Short=V-ATPase 21 kDa proteolipid subunit c'' {ECO:0000305}; AltName: Full=Vacuolar proton pump 21 kDa proteolipid subunit c'' {ECO:0000305}; AltName: Full=hATPL;
- **Gene Information:** Name=ATP6V0B; Synonyms=ATP6F;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the V-ATPase proteolipid subunit family.
- **Key Domains:** ATPase_proteolipid_c-like_dom. (IPR002379); ATPase_proteolipid_csu. (IPR000245); F/V-ATP_Csub_sf. (IPR035921); ATP-synt_C (PF00137)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATP6V0B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATP6V0B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATP6V0B** (gene ID: ATP6V0B, UniProt: Q99437) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATP6V0B: The c'' Proteolipid Subunit of Vacuolar H⁺-ATPase

## Introduction

ATP6V0B (also known as ATP6F) encodes the c'' subunit of the V₀ membrane sector of vacuolar H⁺-ATPase (V-ATPase), a multi-subunit enzyme responsible for the acidification of intracellular compartments in all eukaryotic cells. The gene product is a 21 kDa proteolipid that forms part of the proton-conducting pore of V-ATPase, participating directly in the translocation of protons across membranes. V-ATPase activity is essential for maintaining the acidic pH of lysosomes, endosomes, the trans-Golgi network, and secretory vesicles, and plays critical roles in processes including protein degradation, receptor-mediated endocytosis, autophagy, neurotransmitter loading, and nutrient sensing[stevens-1997-vatpase-review-abstract].

The human ATP6V0B gene was first cloned and characterized by Nishigori and colleagues in 1998, who identified it as a homolog of the *Saccharomyces cerevisiae* VMA16 protein[nishigori-1998-atp6f-abstract]. The gene maps to chromosome 1p32.3 and encodes a highly hydrophobic protein of 205 amino acids with five predicted transmembrane domains. A critical glutamic acid residue (Glu98) within the fourth transmembrane segment is essential for proton transport activity[nishigori-1998-atp6f-abstract]. While V-ATPase has long been considered a housekeeping enzyme required for basic cellular functions, recent research has revealed that ATP6V0B expression is dynamically regulated and plays specific roles in cellular signaling pathways, particularly the mTORC1 pathway controlling cell growth and autophagy.

## V-ATPase Complex Structure and Organization

The V-ATPase holoenzyme is a rotary motor that couples ATP hydrolysis to proton pumping across membranes. It consists of two functional domains: a cytoplasmic V₁ sector (~500 kDa) responsible for ATP hydrolysis, and a membrane-embedded V₀ sector (~250 kDa) that forms the proton-conducting pore[stevens-1997-vatpase-review-abstract]. The V₁ sector contains eight different subunits (A-H) arranged in an A₃B₃CDE₃FG₃H structure, with the catalytic sites located at the interfaces between the A and B subunits. The V₀ sector in mammals consists of multiple subunits including the 116 kDa subunit a (with tissue-specific isoforms a1-a4), the proteolipid subunits c, c', and c'', subunit d, and subunit e[stevens-1997-vatpase-review-abstract].

The proteolipid subunits (c, c', and c'') are the key components of the proton-conducting rotor ring. Unlike bacterial and archaeal V-type ATPases which have homo-oligomeric c-rings, eukaryotic V-ATPases possess hetero-oligomeric rings composed of multiple c subunit isoforms[zhao-2015-cryo-em-vatpase-abstract]. Cryo-electron microscopy studies of the yeast V-ATPase revealed that the c-ring contains 10 proteolipid subunits arranged in a ring structure[zhao-2015-cryo-em-vatpase-abstract]. This stoichiometry establishes the ATP:H⁺ ratio for proton pumping at 3:10, meaning that hydrolysis of three ATP molecules is coupled to the translocation of ten protons across the membrane[zhao-2015-cryo-em-vatpase-abstract].

## ATP6V0B as the c'' Proteolipid Subunit

ATP6V0B encodes the c'' isoform of the V-ATPase proteolipid. The human c'' protein is 205 amino acids in length and shares 61% amino acid identity and 83% similarity with the yeast Vma16p protein[nishigori-1998-atp6f-abstract]. The mouse ortholog, characterized by Sun-Wada and colleagues, exhibits 83-84% similarity to both yeast Vma16p and *Caenorhabditis elegans* vha-4, indicating strong evolutionary conservation of this subunit across eukaryotes[sun-wada-2001-mouse-atp6f-abstract].

Structural analysis predicts five transmembrane α-helical segments in ATP6V0B, similar to other c-type proteolipids[nishigori-1998-atp6f-abstract]. A critical feature is the conserved glutamic acid residue (Glu98 in humans) located in the middle of the fourth transmembrane helix, which serves as the proton-binding site during transport[nishigori-1998-atp6f-abstract]. Mutation of this glutamate abolishes proton pumping activity, establishing it as essential for the catalytic function of the enzyme. The high-resolution cryo-EM structure of the yeast V₀ sector at 3.5 Å resolution revealed the precise arrangement of amino acids constituting the proton pathway at the interface between the proteolipid ring and subunit a[roh-2018-v0-structure-abstract].

The genomic organization of ATP6V0B is conserved between human and mouse, with both genes consisting of 8 exons separated by 7 introns that follow the GT-AG splicing rule[sun-wada-2001-mouse-atp6f-abstract]. The gene is transcribed as two mRNA species of approximately 1.0 and 1.8 kb in multiple tissues, with varying expression levels suggesting tissue-specific regulation[sun-wada-2001-mouse-atp6f-abstract].

## Mechanism of Proton Translocation

The V-ATPase operates as a rotary motor in which ATP hydrolysis in the V₁ sector drives the rotation of the central rotor subcomplex, which is mechanically coupled to the proteolipid c-ring in V₀. As the c-ring rotates against the stationary subunit a, protons are picked up from the cytoplasmic side of the membrane and released into the luminal side through a two-channel mechanism.

Each proteolipid subunit carries a single proton on its essential glutamate residue. On the cytoplasmic side, protons enter through a half-channel in subunit a and bind to the glutamate of an incoming c-subunit. The c-ring then rotates, carrying the protonated glutamate through the hydrophobic core of the membrane. On completing nearly a full rotation, the protonated glutamate encounters a second half-channel in subunit a opening to the luminal side, where the proton is released. The cryo-EM structures of yeast V-ATPase in three rotational states provided direct visualization of the conformational changes that occur during this rotary catalytic cycle[zhao-2015-cryo-em-vatpase-abstract].

## Subcellular Localization and Membrane Targeting

ATP6V0B, as part of the V-ATPase complex, localizes to the membranes of multiple acidic intracellular compartments. Studies with epitope-tagged constructs demonstrated localization to endomembrane organelles including the endoplasmic reticulum, Golgi apparatus, endosomes, and lysosomes[sun-wada-2001-mouse-atp6f-abstract]. The specific localization of V-ATPase is largely determined by the isoform of the subunit a that is incorporated into the complex. In yeast, the Vph1p isoform targets V-ATPase to the vacuole, while the Stv1p isoform targets it to the late Golgi and endosomes[finnigan-2011-vatpase-isoforms-abstract]. Similarly, in mammals, different a-subunit isoforms (a1-a4) direct V-ATPase to specific cellular locations including lysosomes, the Golgi, synaptic vesicles, and the plasma membrane of specialized cells.

V-ATPase is assembled in the endoplasmic reticulum through a complex pathway requiring dedicated assembly factors. The V₀ sector assembles first, requiring factors including Vma21p (TMEM199 in humans) and Voa1p[roh-2018-v0-structure-abstract]. Remarkably, the high-resolution structure of yeast V₀ revealed that the C-terminus of the assembly factor Voa1 remains as an integral component of the mature complex, with its transmembrane helix bound inside the proteolipid ring contributing to complex stability[roh-2018-v0-structure-abstract].

## Biological Processes and Cellular Pathways

### Lysosomal Acidification and Autophagy

The primary function of V-ATPase containing ATP6V0B is the acidification of intracellular compartments. Lysosomal acidification to pH 4.5-5.0 is essential for the activity of acid hydrolases that degrade macromolecules during autophagy and endocytosis. V-ATPase inhibition leads to accumulation of undigested material, disruption of autophagy, and cell death[stevens-1997-vatpase-review-abstract].

### mTORC1 Signaling and Amino Acid Sensing

A groundbreaking discovery by Zoncu and colleagues demonstrated that V-ATPase is essential for amino acid activation of mTORC1, the master regulator of cell growth[zoncu-2011-mtorc1-vatpase-abstract]. The V-ATPase engages in amino acid-sensitive interactions with the Ragulator complex, which anchors the Rag GTPases to the lysosomal surface. In the presence of amino acids, V-ATPase activity promotes the interaction between Ragulator and the Rag heterodimers, leading to mTORC1 recruitment to the lysosome where it is activated by the GTPase Rheb[zoncu-2011-mtorc1-vatpase-abstract][bar-peled-2012-ragulator-gef-abstract]. This "inside-out" mechanism suggests that amino acids are sensed within the lysosomal lumen, with the signal transmitted through V-ATPase to activate mTORC1 on the cytoplasmic surface[zoncu-2011-mtorc1-vatpase-abstract].

### E2F1 Transcriptional Regulation

A significant finding by Meo-Evoli and colleagues identified ATP6V0B as a direct transcriptional target of the E2F1 transcription factor[meo-evoli-2015-e2f1-vatpase-abstract]. Chromatin immunoprecipitation assays confirmed E2F1 binding to the ATP6V0B promoter, and E2F1 activation led to increased ATP6V0B mRNA expression. Importantly, ectopic expression of ATP6V0B alone was sufficient to increase V-ATPase activity and mTORC1 signaling, while ATP6V0B knockdown abrogated E2F1-induced mTORC1 activation[meo-evoli-2015-e2f1-vatpase-abstract]. This pathway links E2F1-driven cell cycle progression to V-ATPase activity and mTORC1-dependent cell growth, with implications for understanding the metabolic reprogramming in proliferating and cancer cells.

### Thyroid Hormone-Induced Expression

Thyroid hormone (T3) has been identified as a regulator of V-ATPase subunit expression, including ATP6V0B[tseng-2023-thyroid-hormone-abstract]. Tseng and colleagues demonstrated that T3 activates expression of numerous lysosomal genes in a thyroid hormone receptor-dependent manner, including ATP6V0B, ATP6V0D1, and ATP6V1E1. This hormonal regulation links V-ATPase expression to metabolic state, as thyroid hormone promotes lysosomal biogenesis and autophagy during periods of increased metabolic demand. The T3-induced upregulation of V-ATPase components enhances lysosomal function, facilitating the breakdown of lipids and other macromolecules during autophagy[tseng-2023-thyroid-hormone-abstract].

### Neurosecretion and Membrane Fusion

Beyond its role in acidification, the V₀ sector has been implicated in membrane fusion events independent of proton pumping. In synaptic vesicles, V-ATPase acidification is required for neurotransmitter loading, but studies suggest V₀ may also directly participate in vesicle fusion with the plasma membrane[morel-2015-neurosecretion-abstract]. V₀ interacts with SNARE proteins and calmodulin, and perturbation of these interactions affects neurotransmitter release. The V₀ sector may function as a pH sensor that regulates SNARE complex assembly during vesicle priming and may contribute to fusion pore formation and stability[morel-2015-neurosecretion-abstract].

## Disease Associations and Clinical Relevance

### Cancer

Overexpression of ATP6V0B has been associated with tumor progression in multiple cancer types. In bladder cancer, ATP6V0B is overexpressed and correlates with poor patient prognosis[wang-2025-bladder-cancer-abstract]. Functional studies demonstrated that ATP6V0B promotes proliferation, invasion, and migration of bladder cancer cells, while knockdown inhibits tumor growth in vivo. Mechanistically, ATP6V0B activates PI3K/AKT signaling through upregulation of PAQR4[wang-2025-bladder-cancer-abstract]. ATP6V0B has also been identified as a potential biomarker for pancreatic cancer in extracellular vesicle-based liquid biopsy approaches[greenberg-2025-pancreatic-ev-abstract]. Additionally, ATP6V0B expression has been associated with cellular senescence phenotypes in hepatocellular carcinoma and has been identified as a hub gene in osteomyelitis-associated programmed cell death pathways.

### Pigmentation and Neurofibromatosis Type 1

Genetic studies have linked ATP6V0B variants to pigmentation phenotypes. In patients with Neurofibromatosis type 1 (NF1), SNPs near the ATP6V0B locus (rs4660761 and rs7161) were significantly associated with café-au-lait macule count[pemov-2014-nf1-calm-abstract]. These SNPs are predicted to regulate ATP6V0B expression, and the association suggests a role for V-ATPase in melanosome biology and skin pigmentation[pemov-2014-nf1-calm-abstract]. Studies comparing melanocytes from individuals with dark versus light skin identified ATP6V0B among genes showing differential expression, supporting an evolutionary role in the pigmentary phenotype[lopez-2015-melanocyte-abstract].

### V-ATPase Subunit Mutations and Human Disease

While specific pathogenic mutations in ATP6V0B have not been reported, mutations in other V-ATPase subunits cause well-characterized human diseases. Mutations in ATP6V0A3 (a3 subunit) cause autosomal recessive osteopetrosis with neurodegeneration. Mutations in ATP6V0A2 (a2 subunit) cause cutis laxa type II with wrinkly skin syndrome. Mutations in ATP6V1B1 and ATP6V0A4 cause distal renal tubular acidosis with sensorineural deafness[shine-2014-vision-abstract]. The structural and functional conservation of the c'' subunit suggests that damaging mutations would likely be incompatible with life or cause severe developmental abnormalities. Indeed, genetic studies in *Drosophila* demonstrated that V-ATPase knockout mutations are recessive lethal, with lethal alleles of multiple V-ATPase subunits showing consistent phenotypes including transparent Malpighian tubules[allan-2005-drosophila-vatpase-abstract]. The essential nature of V-ATPase for organismal viability explains the absence of loss-of-function mutations in core subunits like ATP6V0B in human disease databases.

## Open Questions

Several important questions remain about ATP6V0B function and regulation:

1. **Subunit stoichiometry in mammalian V-ATPase**: While the yeast c-ring contains 10 proteolipids, the exact composition and stoichiometry of c, c', and c'' subunits in the mammalian c-ring remains to be definitively established.

2. **Tissue-specific functions**: Do different expression ratios of the proteolipid isoforms (c, c', c'') confer tissue-specific properties to V-ATPase function?

3. **ATP6V0B in cancer progression**: What is the precise mechanism by which ATP6V0B overexpression promotes tumor metastasis beyond activation of PI3K/AKT signaling? Does it involve altered lysosomal positioning, enhanced matrix degradation, or other mechanisms?

4. **Regulatory mechanisms**: Beyond E2F1 regulation, what other transcription factors and signaling pathways control ATP6V0B expression under different physiological conditions?

5. **Therapeutic targeting**: Can selective modulation of ATP6V0B-containing V-ATPases provide therapeutic benefit in cancer without disrupting essential V-ATPase functions in normal tissues?

6. **Non-canonical functions**: Does ATP6V0B play direct roles in membrane fusion or other cellular processes independent of its function in the V-ATPase proton pore?

## References

* **nishigori-1998-atp6f-abstract**: Nishigori H, Yamada S, Tomura H, et al. Identification and characterization of the gene encoding a second proteolipid subunit of human vacuolar H(+)-ATPase (ATP6F). *Genomics*. 1998;50(2):222-8. PMID: 9653649. DOI: [10.1006/geno.1998.5310](https://doi.org/10.1006/geno.1998.5310)

* **sun-wada-2001-mouse-atp6f-abstract**: Sun-Wada GH, Murakami H, Nakai H, et al. Mouse Atp6f, the gene encoding the 23-kDa proteolipid of vacuolar proton translocating ATPase. *Gene*. 2001;274(1-2):93-9. PMID: 11675001. DOI: [10.1016/s0378-1119(01)00603-5](https://doi.org/10.1016/s0378-1119(01)00603-5)

* **izumi-2003-promoter-abstract**: Izumi H, Ise T, Murakami T, et al. Structural and functional characterization of two human V-ATPase subunit gene promoters. *Biochim Biophys Acta*. 2003;1628(2):97-104. PMID: 12890556. DOI: [10.1016/s0167-4781(03)00119-2](https://doi.org/10.1016/s0167-4781(03)00119-2)

* **stevens-1997-vatpase-review-abstract**: Stevens TH, Forgac M. Structure, function and regulation of the vacuolar (H+)-ATPase. *Annu Rev Cell Dev Biol*. 1997;13:779-808. PMID: 9442887. DOI: [10.1146/annurev.cellbio.13.1.779](https://doi.org/10.1146/annurev.cellbio.13.1.779)

* **zhao-2015-cryo-em-vatpase-abstract**: Zhao J, Benlekbir S, Rubinstein JL. Electron cryomicroscopy observation of rotational states in a eukaryotic V-ATPase. *Nature*. 2015;521(7551):241-5. PMID: 25971514. DOI: [10.1038/nature14365](https://doi.org/10.1038/nature14365)

* **roh-2018-v0-structure-abstract**: Roh SH, Stam NJ, Hryc CF, et al. The 3.5-Å CryoEM Structure of Nanodisc-Reconstituted Yeast Vacuolar ATPase V₀ Proton Channel. *Mol Cell*. 2018;69(6):993-1004.e3. PMID: 29526695. DOI: [10.1016/j.molcel.2018.02.006](https://doi.org/10.1016/j.molcel.2018.02.006)

* **zoncu-2011-mtorc1-vatpase-abstract**: Zoncu R, Bar-Peled L, Efeyan A, et al. mTORC1 senses lysosomal amino acids through an inside-out mechanism that requires the vacuolar H(+)-ATPase. *Science*. 2011;334(6056):678-83. PMID: 22053050. DOI: [10.1126/science.1207056](https://doi.org/10.1126/science.1207056)

* **bar-peled-2012-ragulator-gef-abstract**: Bar-Peled L, Schweitzer LD, Zoncu R, Sabatini DM. Ragulator is a GEF for the rag GTPases that signal amino acid levels to mTORC1. *Cell*. 2012;150(6):1196-208. PMID: 22980980. DOI: [10.1016/j.cell.2012.07.032](https://doi.org/10.1016/j.cell.2012.07.032)

* **meo-evoli-2015-e2f1-vatpase-abstract**: Meo-Evoli N, Almacellas E, Massucci FA, et al. V-ATPase: a master effector of E2F1-mediated lysosomal trafficking, mTORC1 activation and autophagy. *Oncotarget*. 2015;6(29):28057-70. PMID: 26356814. DOI: [10.18632/oncotarget.4812](https://doi.org/10.18632/oncotarget.4812)

* **morel-2015-neurosecretion-abstract**: Morel N, Poëa-Guyon S. The membrane domain of vacuolar H(+)ATPase: a crucial player in neurotransmitter exocytotic release. *Cell Mol Life Sci*. 2015;72(13):2561-73. PMID: 25795337. DOI: [10.1007/s00018-015-1886-2](https://doi.org/10.1007/s00018-015-1886-2)

* **pemov-2014-nf1-calm-abstract**: Pemov A, Sung H, Hyland PL, et al. Genetic modifiers of neurofibromatosis type 1-associated café-au-lait macule count identified using multi-platform analysis. *PLoS Genet*. 2014;10(10):e1004575. PMID: 25329635. DOI: [10.1371/journal.pgen.1004575](https://doi.org/10.1371/journal.pgen.1004575)

* **wang-2025-bladder-cancer-abstract**: Wang X, Qu Y, Sun Y, et al. ATP6V0B promotes the tumorigenesis of bladder cancer by activating PAQR4/PI3K/AKT signaling. *BMC Cancer*. 2025;25(1):789. PMID: 40295930. DOI: [10.1186/s12885-025-14183-z](https://doi.org/10.1186/s12885-025-14183-z)

* **shine-2014-vision-abstract**: Shine L, Kilty C, Gross J, Kennedy B. Vacuolar ATPases and their role in vision. *Adv Exp Med Biol*. 2014;801:97-103. PMID: 24664686. DOI: [10.1007/978-1-4614-3209-8_13](https://doi.org/10.1007/978-1-4614-3209-8_13)

* **lopez-2015-melanocyte-abstract**: López S, Smith-Zubiaga I, García de Galdeano A, et al. Comparison of the Transcriptional Profiles of Melanocytes from Dark and Light Skinned Individuals under Basal Conditions and Following Ultraviolet-B Irradiation. *PLoS One*. 2015;10(8):e0134911. PMID: 26244334. DOI: [10.1371/journal.pone.0134911](https://doi.org/10.1371/journal.pone.0134911)

* **finnigan-2011-vatpase-isoforms-abstract**: Finnigan GC, Hanson-Smith V, Houser BD, et al. The reconstructed ancestral subunit a functions as both V-ATPase isoforms Vph1p and Stv1p in Saccharomyces cerevisiae. *Mol Biol Cell*. 2011;22(17):3176-91. PMID: 21737673. DOI: [10.1091/mbc.E11-03-0244](https://doi.org/10.1091/mbc.E11-03-0244)

* **greenberg-2025-pancreatic-ev-abstract**: Greenberg ZF, Ali S, Brock A, et al. Nanomaterial isolated extracellular vesicles enable high precision identification of tumor biomarkers for pancreatic cancer liquid biopsy. *J Nanobiotechnology*. 2025;23(1):467. PMID: 40598203. DOI: [10.1186/s12951-025-03527-3](https://doi.org/10.1186/s12951-025-03527-3)

* **tseng-2023-thyroid-hormone-abstract**: Tseng YT, Lu PY, Lee WJ, et al. Thyroid hormone upregulates ATP6V0B and increases lysosomal function in autophagy. *Biochem Biophys Res Commun*. 2023;662:66-75. PMID: 37099812. DOI: [10.1016/j.bbrc.2023.04.061](https://doi.org/10.1016/j.bbrc.2023.04.061)

* **allan-2005-drosophila-vatpase-abstract**: Allan AK, Du J, Davies SA, Bhartiya DP. Genome-wide survey of V-ATPase genes in Drosophila reveals a conserved renal phenotype for lethal alleles. *Physiol Genomics*. 2005;22(2):128-38. PMID: 15855386. DOI: [10.1152/physiolgenomics.00233.2004](https://doi.org/10.1152/physiolgenomics.00233.2004)


## Citations

1. allan-2005-drosophila-vatpase-abstract.md
2. bar-peled-2012-ragulator-gef-abstract.md
3. finnigan-2011-vatpase-isoforms-abstract.md
4. greenberg-2025-pancreatic-ev-abstract.md
5. higashida-2016-atp6v0c-neurotransmitter-abstract.md
6. izumi-2003-promoter-abstract.md
7. lopez-2015-melanocyte-abstract.md
8. meo-evoli-2015-e2f1-vatpase-abstract.md
9. morel-2015-neurosecretion-abstract.md
10. nishigori-1998-atp6f-abstract.md
11. pemov-2014-nf1-calm-abstract.md
12. roh-2018-v0-structure-abstract.md
13. shine-2014-vision-abstract.md
14. stevens-1997-vatpase-review-abstract.md
15. sun-wada-2001-mouse-atp6f-abstract.md
16. tseng-2023-thyroid-hormone-abstract.md
17. wang-2025-bladder-cancer-abstract.md
18. zhao-2015-cryo-em-vatpase-abstract.md
19. zoncu-2011-mtorc1-vatpase-abstract.md