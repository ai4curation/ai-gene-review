---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T02:01:55.429987'
end_time: '2026-09-25T02:09:17.154121'
duration_seconds: 441.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: CDC5
  gene_symbol: CDC5
  uniprot_accession: P32562
  protein_description: 'RecName: Full=Cell cycle serine/threonine-protein kinase CDC5/MSD2;
    EC=2.7.11.21 {ECO:0000269|PubMed:11371343, ECO:0000269|PubMed:12056824};'
  gene_info: Name=CDC5; Synonyms=MSD2, PKX2; OrderedLocusNames=YMR001C; ORFNames=YM8270.03C;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); POLO_box_1. (IPR033701); POLO_box_2.
    (IPR033695); POLO_box_dom. (IPR000959); POLO_box_dom_sf. (IPR036947)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CDC5-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** P32562
- **Protein Description:** RecName: Full=Cell cycle serine/threonine-protein kinase CDC5/MSD2; EC=2.7.11.21 {ECO:0000269|PubMed:11371343, ECO:0000269|PubMed:12056824};
- **Gene Information:** Name=CDC5; Synonyms=MSD2, PKX2; OrderedLocusNames=YMR001C; ORFNames=YM8270.03C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); POLO_box_1. (IPR033701); POLO_box_2. (IPR033695); POLO_box_dom. (IPR000959); POLO_box_dom_sf. (IPR036947)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CDC5" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CDC5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CDC5** (gene ID: CDC5, UniProt: P32562) in yeast.

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
- **UniProt Accession:** P32562
- **Protein Description:** RecName: Full=Cell cycle serine/threonine-protein kinase CDC5/MSD2; EC=2.7.11.21 {ECO:0000269|PubMed:11371343, ECO:0000269|PubMed:12056824};
- **Gene Information:** Name=CDC5; Synonyms=MSD2, PKX2; OrderedLocusNames=YMR001C; ORFNames=YM8270.03C;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); POLO_box_1. (IPR033701); POLO_box_2. (IPR033695); POLO_box_dom. (IPR000959); POLO_box_dom_sf. (IPR036947)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CDC5" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CDC5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CDC5** (gene ID: CDC5, UniProt: P32562) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Research report: *Saccharomyces cerevisiae* CDC5 (UniProt P32562)

## Executive conclusion

The requested protein identity is verified. **CDC5/YMR001C** in *Saccharomyces cerevisiae* S288c encodes Cdc5, the organism’s sole Polo-like serine/threonine kinase. The literature describes the same characteristic architecture supplied by UniProt P32562: an N-terminal catalytic protein-kinase domain and a C-terminal polo-box domain (PBD) formed by two polo boxes. No evidence concerning an unrelated same-symbol protein was used. The synonymous names MSD2 and PKX2 occur less commonly than CDC5 in the literature. (paulson2006chemicalgeneticanalysis pages 66-72, paulson2006chemicalgeneticanalysis pages 88-92, botchkarev2018functionsandregulation pages 1-3)

Cdc5 is best understood as an essential, spatially targeted cell-cycle kinase. Its primary biochemical activity is ATP-dependent phosphorylation of serine/threonine residues in proteins. Its broader biological role is to coordinate mitotic entry, chromosome segregation, mitotic exit, and cytokinesis by relocating among chromosomes, spindle pole bodies (SPBs), the nucleolus, and the bud neck and phosphorylating different local substrates. The PBD is therefore not merely an accessory domain: it converts a broadly active catalytic domain into a location- and cell-cycle-specific signaling enzyme. (park2004novelfunctionaldissection pages 1-2, botchkarev2018functionsandregulation pages 4-6, botchkarev2018functionsandregulation pages 1-3)

## 1. Identity, family, and molecular architecture

The target is **not a generic “CDC5”**. It is the budding-yeast gene **CDC5, systematic locus YMR001C**, corresponding to UniProt **P32562** in *S. cerevisiae* S288c. Organism-specific literature identifies Cdc5 as the single budding-yeast Polo-like kinase and an essential mitotic regulator. Its kinase domain shares approximately 49% identity with the human PLK1 kinase domain, supporting orthology at the family level without implying that all mammalian PLK1 biology applies to yeast Cdc5. (paulson2006chemicalgeneticanalysis pages 66-72, paulson2006chemicalgeneticanalysis pages 88-92)

The protein has two functionally coupled modules:

1. **N-terminal kinase domain:** catalyzes protein serine/threonine phosphorylation.
2. **C-terminal PBD:** two polo boxes form a pincer-like phosphoserine/phosphothreonine-binding structure that controls localization and substrate recruitment. The supplied InterPro annotations—Polo_box_1, Polo_box_2, Polo_box_dom, and a kinase-like domain—therefore align directly with experimental and structural literature. (park2004novelfunctionaldissection pages 1-2, botchkarev2018functionsandregulation pages 1-3, almawi2020distinctsurfaceson pages 1-2)

## 2. Primary biochemical function and substrate specificity

### Catalyzed reaction

Cdc5 catalyzes the standard protein-kinase reaction:

**ATP + protein–Ser/Thr–OH → ADP + protein–Ser/Thr–O–phosphate.**

Purified full-length Cdc5 phosphorylates dephosphorylated casein in vitro in the presence of ATP and Mg²⁺. One documented radiometric format used 0.125 pmol Cdc5, 100 µM ATP, 10 mM MgCl₂, and a 30-minute reaction at 30°C. These experiments establish ATP-dependent, Mg²⁺-supported kinase chemistry; casein is an artificial assay substrate and does not define physiological specificity. (langloislemay2025centrosomescaffoldsandb pages 222-226, langloislemay2025centrosomescaffoldsanda pages 222-226)

### How physiological substrates are selected

Cdc5 specificity is combinatorial rather than reducible to one short phosphorylation consensus. At least four determinants operate together:

- catalytic-domain sequence preferences around the acceptor Ser/Thr;
- cell-cycle-dependent expression and activating phosphorylation;
- colocalization at chromosomes, SPBs, nucleolus, or bud neck;
- PBD docking to substrate or scaffold proteins. (paulson2006chemicalgeneticanalysis pages 66-72, botchkarev2018functionsandregulation pages 1-3)

In the canonical mechanism, another kinase—frequently Cdk1/Cdc28—creates a priming phosphoserine/threonine site. The Cdc5 PBD recognizes that phosphorylated motif, recruits the kinase, and facilitates phosphorylation of nearby sites. This provides both temporal ordering and local concentration of Cdc5 activity. (paulson2006chemicalgeneticanalysis pages 66-72, almawi2020distinctsurfaceson pages 1-2)

Importantly, PBD binding is not exclusively phosphodependent. Almawi and colleagues solved structures of the Cdc5 PBD alone and with canonical phosphopeptide and Dbf4-derived ligands. Dbf4 uses a noncanonical, phosphorylation-independent sequence, including residues 83–88, **RSIEGA**, on a PBD surface opposite the canonical phosphopeptide pocket. Canonical phosphopeptide and Dbf4 peptide can bind simultaneously and noncompetitively. Mutations disrupting this second surface produced early-anaphase arrest rather than the conventional mitotic-exit phenotype, demonstrating biologically distinct combinatorial recognition. This work was published in *Scientific Reports* in February 2020; DOI: https://doi.org/10.1038/s41598-020-60344-4. (almawi2020distinctsurfaceson pages 1-2)

## 3. Regulation through the cell cycle

CDC5 expression begins during S phase and remains elevated through cell division. Cdc5 is highly active in mitosis and is subsequently degraded after mitosis/cytokinesis through APC–Cdh1 recognition of N-terminal degrons. Activating phosphorylation is crucial: T242 is particularly important, because a T242A mutant is kinase-inactive and inviable. T70 contributes to mitotic-exit-network activation, whereas T238 influences kinase activity and DNA-damage adaptation but is not itself essential for viability. (botchkarev2018functionsandregulation pages 1-3)

Cdc5 abundance, catalytic state, PBD interactions, and localization therefore constitute four regulatory layers. This explains why isolated kinase activity toward a generic substrate is insufficient to predict biological output.

## 4. Localization and localization-specific functions

Cdc5 accumulates strongly in the nucleus from G2 through early anaphase. In late anaphase, Cdc14-dependent release of Cdc5 into the cytoplasm is required for normal mitotic exit. Other experimentally supported sites include chromosome arms and kinetochores, both nuclear and cytoplasmic faces of the SPB, and the daughter-side bud neck. (paulson2006chemicalgeneticanalysis pages 66-72, botchkarev2018functionsandregulation pages 4-6)

Localization-tethering experiments provide unusually direct functional evidence. A kinase-containing Cdc5 fragment defective in normal localization was artificially tethered to either SPBs or the bud neck. SPB-associated activity supported mitotic exit and cytokinesis, whereas bud-neck activity was especially important for Swe1 regulation. Combining SPB- and neck-targeted constructs substantially restored growth. Thus, Cdc5’s pleiotropy reflects spatial partitioning of one kinase rather than a single diffuse signaling output. Park et al. published these experiments in November 2004; DOI: https://doi.org/10.1128/MCB.24.22.9873-9886.2004. (park2004novelfunctionaldissection pages 1-2, park2004novelfunctionaldissection pages 12-13)

## 5. Principal pathways and experimentally supported substrates

### Mitotic entry: Swe1–Cdc28 control

Cdc5 directly phosphorylates the inhibitory kinase Swe1, promoting its ubiquitin-dependent degradation. Loss of Swe1 relieves inhibitory control of Cdc28/Cdk1 and facilitates mitotic progression. Bud-neck targeting experiments place an important portion of this reaction at the neck. Cdc5 also phosphorylates the Mcm1–Fkh2–Ndd1 transcriptional complex involved in expression of the mitotic cyclin CLB2. (park2004novelfunctionaldissection pages 1-2, botchkarev2018functionsandregulation pages 3-4)

### Cohesin cleavage and chromosome segregation

Cdc5 associates with cohesin-bearing chromosome arms during G2/M through PBD-dependent interaction with primed sites in the Scc1/Mcd1 cohesin subunit. It phosphorylates chromatin-bound Scc1 at multiple residues—one synthesis reports ten sites—making Scc1 a better substrate for Esp1/separase and promoting cohesin removal at anaphase. In cdc5-99 cells, cohesin persists on anaphase chromatin and chromosome segregation is defective. Mutating 15 candidate Scc1 priming sites weakens Cdc5 association with cohesin; the resulting defect is modest during ordinary mitosis but causes pronounced phleomycin sensitivity in a sensitized pds1Δ background. (park2004novelfunctionaldissection pages 12-13, botchkarev2018functionsandregulation pages 3-4)

### FEAR, Cdc14 release, and early mitotic exit

The FEAR pathway initiates partial release of the Cdc14 phosphatase from its nucleolar inhibitor Net1/Cfi1. Cdc5 interacts with FEAR components including Esp1 and Slk19 and contributes to Cdc14 activation. Cdc5 and Cdk1-dependent phosphorylation of Net1 correlates with Cdc14 release. However, authoritative synthesis cautions that the exact direct mechanism remains debated: some evidence favors direct Net1 phosphorylation, whereas another model emphasizes Cdc5-driven Swe1 degradation, increased Cdk1 activity, and consequent Cdk1-dependent Net1 phosphorylation. The secure annotation is therefore that Cdc5 is required for efficient FEAR/Cdc14 activation, while Net1 should not be represented as an unqualified sole direct effector. (botchkarev2018functionsandregulation pages 4-6, botchkarev2018functionsandregulation pages 3-4, botchkarev2018functionsandregulation pages 9-11)

### MEN signaling at the spindle pole body

Cdc5 activates the mitotic exit network at the daughter-facing SPB. It phosphorylates Bfa1, inhibiting the Bfa1–Bub2 GTPase-activating complex and permitting Tem1 signaling. It also modifies Bfa1 sites that affect asymmetric SPB localization and phosphorylates Cdc15, supporting MEN activation by more than one route. The pathway culminates in complete Cdc14 release, cyclin-CDK down-regulation, and mitotic exit. (park2004novelfunctionaldissection pages 1-2, botchkarev2018functionsandregulation pages 4-6)

### SPBs, microtubules, and spindle migration

The SPB component Spc72 binds the Cdc5 PBD, is directly phosphorylated by Cdc5 in vitro, and loses mitotic phosphorylation when analog-sensitive Cdc5 is inhibited. Chemical-genetic inhibition of cdc5-as1 had an IC₅₀ of 1.1 µM, while up to 15 µM inhibitor did not affect wild-type cells. Inhibition caused first-cycle mitotic arrest; spindle elongation remained within the mother in 23% of inhibited cells versus 2% of controls. Wild-type Cdc5 rescued this phenotype, whereas a PBD-defective protein did not. These data support a direct, localization-dependent role in spindle orientation or migration rather than merely an indirect consequence of late mitotic arrest. (paulson2006chemicalgeneticanalysis pages 72-76, paulson2006chemicalgeneticanalysis pages 66-72)

### Cytokinesis

Cdc5 connects mitotic exit to physical cell division at the bud neck. Reported substrates or partners include the Rho1 guanine-nucleotide-exchange factors Tus1 and Rom2, the cytokinesis factor Hof1/Cyk2, the Rab GTPase Sec4, septins Cdc11/Cdc12, and regulators of Cdc42. Cdc5-dependent phosphorylation promotes Tus1/Rom2 neck localization and Rho1 activation, contributes to actomyosin-ring organization, regulates Hof1 recruitment, and influences Sec4-dependent membrane addition. Depletion of Cdc5 or disruption of its polo box produces incomplete septa, abnormal septin structures, connected cells, and cytokinesis arrest. Song and Lee’s primary study was published in February 2001; DOI: https://doi.org/10.1083/jcb.152.3.451. (langloislemay2025centrosomescaffoldsand pages 36-39, botchkarev2018functionsandregulation pages 4-6)

The following evidence map summarizes the principal experimentally supported modules.

| Functional module or location | Direct substrate/partner | Molecular consequence | Evidence type/strength | Representative source/date/DOI URL |
|---|---|---|---|---|
| Identity and domain architecture | CDC5/YMR001C; Cdc5 protein (UniProt P32562) | The sole *S. cerevisiae* Polo-like kinase has an N-terminal Ser/Thr kinase domain and a C-terminal polo-box domain (PBD) comprising two polo boxes that direct localization and substrate binding. This matches the specified S288c protein rather than same-symbol genes in other organisms. | **Strong:** organism-specific genetic, biochemical, and structural evidence (paulson2006chemicalgeneticanalysis pages 88-92, botchkarev2018functionsandregulation pages 1-3) | Botchkarev & Haber, 2018-02, [10.1007/s00294-017-0727-2](https://doi.org/10.1007/s00294-017-0727-2) |
| Catalytic reaction | ATP, Mg²⁺, protein Ser/Thr residues; casein in vitro | Transfers the ATP γ-phosphate to serine/threonine residues: ATP + protein-OH → ADP + protein-O-phosphate. Purified full-length Cdc5 phosphorylates dephospho-casein in an ATP- and Mg²⁺-containing assay; casein is an assay substrate, not evidence of physiological specificity. | **Strong for kinase chemistry; limited for physiological specificity:** purified-protein radiometric assay (langloislemay2025centrosomescaffoldsandb pages 222-226) | Chauhan et al., 2019-12, [10.1016/j.heliyon.2019.e03050](https://doi.org/10.1016/j.heliyon.2019.e03050) |
| Canonical PBD docking | Primed phosphoserine/phosphothreonine motifs on substrates | The two polo boxes form a phosphopeptide-binding unit that recruits Cdc5 to prephosphorylated proteins and concentrates catalytic activity near appropriate substrates and structures. | **Strong:** structural, peptide-binding, mutational, and cellular evidence (paulson2006chemicalgeneticanalysis pages 66-72, botchkarev2018functionsandregulation pages 1-3, almawi2020distinctsurfaceson pages 1-2) | Almawi et al., 2020-02, [10.1038/s41598-020-60344-4](https://doi.org/10.1038/s41598-020-60344-4) |
| Noncanonical/combinatorial PBD docking | Dbf4 peptide, including the nonphosphorylated polo-interacting sequence 83-RSIEGA-88 | Dbf4 binds a PBD surface opposite the canonical phosphopeptide pocket. Dbf4 and a canonical phosphopeptide can bind simultaneously and noncompetitively; mutations disrupting the noncanonical surface produce an early-anaphase phenotype distinct from the usual mitotic-exit defect. | **Strong:** crystal structures, solution binding, site-directed mutagenesis, and yeast phenotypes (almawi2020distinctsurfaceson pages 1-2) | Almawi et al., 2020-02, [10.1038/s41598-020-60344-4](https://doi.org/10.1038/s41598-020-60344-4) |
| Chromosome arms and cohesin | Scc1/Mcd1 cohesin subunit | PBD-dependent association places Cdc5 on chromosome-bound cohesin; phosphorylation of multiple Scc1 sites promotes efficient Esp1/separase cleavage and cohesin removal at anaphase. Disrupting priming sites weakens Cdc5–cohesin association and sensitizes cells to DNA damage. | **Strong:** chromatin association, direct interaction, phosphosite mutagenesis, cleavage, and genetic evidence (park2004novelfunctionaldissection pages 12-13, botchkarev2018functionsandregulation pages 3-4) | Pakchuen et al., 2016-08, [10.1074/jbc.M116.727438](https://doi.org/10.1074/jbc.M116.727438) |
| G2/M entry and bud neck | Swe1 kinase | Cdc5 directly phosphorylates and negatively regulates Swe1, promoting its ubiquitin-dependent degradation and thereby relieving inhibitory control of Cdc28/Cdk1. Bud-neck-targeting experiments support a localization-specific role in Swe1 regulation. | **Strong:** direct phosphorylation, genetics, degradation assays, and localization-tethering experiments (park2004novelfunctionaldissection pages 1-2, botchkarev2018functionsandregulation pages 4-6, botchkarev2018functionsandregulation pages 3-4) | Park et al., 2004-11, [10.1128/MCB.24.22.9873-9886.2004](https://doi.org/10.1128/MCB.24.22.9873-9886.2004) |
| FEAR pathway and nucleolus | Net1/Cfi1, Cdc14, Esp1 and Slk19 | Cdc5 helps trigger early-anaphase Cdc14 release from its nucleolar Net1 anchor, cooperating with Cdk1 and FEAR components. Whether Net1 is always the decisive direct Cdc5 substrate is **debated**; an alternative emphasizes indirect promotion through Swe1 degradation and Cdk1-dependent Net1 phosphorylation. | **Strong for Cdc5 requirement and Cdc14 release; mixed/debated for the exact direct substrate mechanism** (botchkarev2018functionsandregulation pages 4-6, botchkarev2018functionsandregulation pages 3-4, botchkarev2018functionsandregulation pages 9-11) | Liang et al., 2009-08, [10.1091/mbc.E08-10-1049](https://doi.org/10.1091/mbc.E08-10-1049) |
| MEN at the daughter-facing spindle pole body | Bfa1–Bub2 GAP and Cdc15 kinase | Cdc5 phosphorylation inhibits the Bfa1–Bub2 GAP to permit Tem1 signaling, helps maintain Bfa1 asymmetry, and phosphorylates Cdc15, collectively promoting full Cdc14 release and mitotic exit. | **Strong:** phosphoregulation, localization, epistasis, and pathway genetics (park2004novelfunctionaldissection pages 1-2, botchkarev2018functionsandregulation pages 4-6) | Geymonat et al., 2003-04, [10.1074/jbc.C300059200](https://doi.org/10.1074/jbc.C300059200) |
| Spindle pole body and spindle migration | Spc72; PBD-dependent SPB docking | Spc72 binds the Cdc5 PBD and is directly phosphorylated by Cdc5. Acute chemical-genetic inhibition caused first-cycle mitotic arrest and frequent spindle elongation within the mother cell, supporting a direct role in spindle orientation/migration. | **Strong:** direct binding/phosphorylation, analog-sensitive inhibition, rescue, and quantitative imaging (paulson2006chemicalgeneticanalysis pages 72-76, paulson2006chemicalgeneticanalysis pages 66-72) | Paulson et al., 2006, chemical-genetic study summarized in retrieved evidence |
| Bud neck and cytokinesis | Tus1, Rom2, Hof1/Cyk2, Sec4; septins Cdc11/Cdc12 | Cdc5 promotes Tus1/Rom2 localization and Rho1 activation, regulates Hof1 recruitment and Sec4-dependent membrane addition, and engages septin-associated cytokinetic machinery. PBD disruption or Cdc5 depletion produces incomplete septa and cytokinesis arrest. | **Strong for cytokinesis and PBD dependence; substrate-specific mechanisms vary in depth of validation** (langloislemay2025centrosomescaffoldsand pages 36-39, botchkarev2018functionsandregulation pages 4-6) | Song & Lee, 2001-02, [10.1083/jcb.152.3.451](https://doi.org/10.1083/jcb.152.3.451) |
| Persistent DNA-damage response and spindle pole bodies | Nud1, Spc110 and Spc72 recruitment scaffolds; proposed Cnm67 and Mps3 substrates | Cdc5 promotes adaptation—the resumption of cell-cycle progression despite persistent DNA damage. A 2024 preprint proposed that SPBs act as signaling platforms recruiting Cdc5 and that Cnm67/Mps3 phosphorylation helps bypass checkpoint arrest; these substrate-level conclusions were **emerging/preprint evidence** in 2024. | **Established for Cdc5-dependent adaptation; emerging for the detailed SPB scaffold/substrate model** (langloislemay2025centrosomescaffoldsand pages 171-173, botchkarev2018functionsandregulation pages 9-11) | Langlois-Lemay & D’Amours, 2024-06-13 preprint, [10.1101/2024.06.13.598907](https://doi.org/10.1101/2024.06.13.598907) |
| Meiotic chromosomes and prophase-I exit | Recombination and synaptonemal-complex machinery; Ndt80-regulated CDC5 expression | Meiotic induction of CDC5 promotes exit from pachytene, synaptonemal-complex disassembly, and processing/resolution of recombination intermediates. A 2024 review places Cdc5-driven recombination control within the Cdc14-centered meiotic network; individual substrate assignments remain less complete than in mitosis. | **Strong for pathway-level requirement; incomplete for a unified direct-substrate mechanism** (langloislemay2025centrosomescaffoldsand pages 171-173) | Alonso-Ramos & Carballo, 2024-11-29, [10.3390/ijms252312861](https://doi.org/10.3390/ijms252312861) |


*Table: Evidence map linking verified budding-yeast Cdc5/P32562 functions and locations to direct partners, molecular consequences, and representative sources. Debated FEAR mechanisms and emerging 2024 spindle-pole-body adaptation findings are explicitly distinguished from established conclusions.*

## 6. DNA-damage signaling and checkpoint adaptation

Cdc5 is required for adaptation: resumption of cell-cycle progression despite a persistent, unrepaired DNA lesion. Excess Cdc5 can override Mec1/ATR-dependent checkpoint signaling, reducing phosphorylation of targets including Ddc2, Rad9, and Rad53 and affecting double-strand-break processing. This finding does not mean that Cdc5 is simply a DNA-repair kinase; its best-supported role is in checkpoint attenuation or bypass and coordination of recovery/adaptation with mitotic machinery. Donnianni et al. reported this work in January 2010; DOI: https://doi.org/10.1371/journal.pgen.1000763. (botchkarev2018functionsandregulation pages 9-11)

A notable recent development was the **13 June 2024 bioRxiv preprint** by Langlois-Lemay and D’Amours, DOI: https://doi.org/10.1101/2024.06.13.598907. It proposed that SPBs operate as supramolecular signaling centers during persistent damage: Nud1, Spc110, and Spc72 recruit Cdc5, after which Cdc5 phosphorylates structural SPB components including Cnm67 and Mps3; those events were reported as necessary for efficient checkpoint adaptation. This was an important mechanistic advance, but it was preprint evidence in 2024 and should be weighted below established peer-reviewed conclusions unless using the subsequently published version. (langloislemay2025centrosomescaffoldsand pages 171-173)

## 7. Meiosis

In budding-yeast meiosis, CDC5 is part of the Ndt80-induced transcriptional program that drives exit from pachytene/prophase I. Cdc5 promotes synaptonemal-complex disassembly and the processing or resolution of meiotic recombination intermediates, linking chromosome remodeling to meiotic cell-cycle progression. The direct-substrate map is less complete than for mitotic cohesin, MEN, or cytokinesis, so pathway-level annotation is more secure than assigning one dominant meiotic substrate. (langloislemay2025centrosomescaffoldsand pages 171-173)

A recent authoritative synthesis is Alonso-Ramos and Carballo, published 29 November 2024 in *International Journal of Molecular Sciences*, DOI: https://doi.org/10.3390/ijms252312861. It places Cdc5 and CDKs in a positive regulatory framework for meiotic recombination and relates their activity to regulated nucleolar Cdc14 release and resolution of recombination intermediates. This is a review rather than new direct substrate evidence.

## 8. Current applications and real-world relevance

Cdc5 is principally a **research model**, not an industrial yeast-engineering target or approved therapeutic target. Its current applications include:

- dissecting conserved Polo-like kinase substrate selection and PBD docking;
- using analog-sensitive alleles for rapid, selective kinase inhibition;
- studying spatial signaling at centrosome-equivalent SPBs;
- analyzing chromosome segregation, cytokinesis, and checkpoint adaptation;
- developing mechanistic concepts relevant to human PLK1, a major cancer-associated kinase.

The cdc5-as1 experiments illustrate the power of chemical genetics: selective inhibition at 1.1 µM produced acute, first-cycle phenotypes while wild-type cells tolerated 15 µM, allowing primary kinase functions to be separated from secondary consequences of prolonged arrest. (paulson2006chemicalgeneticanalysis pages 72-76)

Extrapolation to human therapy nevertheless requires caution. Yeast has one Polo-like kinase, whereas mammals have several PLKs with partially specialized functions. Cdc5 is therefore highly valuable for conserved mechanistic principles—kinase/PBD coupling, phosphopriming, centrosomal signaling, and checkpoint adaptation—but is not interchangeable with human PLK1 in every pathway. (paulson2006chemicalgeneticanalysis pages 66-72, almawi2020distinctsurfaceson pages 1-2)

## 9. Expert assessment and annotation confidence

**High-confidence primary annotation:** Cdc5 is an essential, ATP-dependent Ser/Thr Polo-like kinase whose PBD targets it to phosphorylated and selected nonphosphorylated partners. Its central role is the spatial coordination of chromosome segregation, Cdc14-dependent mitotic exit, and cytokinesis. (botchkarev2018functionsandregulation pages 1-3, almawi2020distinctsurfaceson pages 1-2)

**High-confidence locations:** nucleus/chromosomes in G2–early anaphase; nucleolar/FEAR signaling context; both SPB compartments; and the daughter-side bud neck. Its late-anaphase nuclear-to-cytoplasmic redistribution is functionally important. (paulson2006chemicalgeneticanalysis pages 66-72, botchkarev2018functionsandregulation pages 4-6)

**Best-established direct or near-direct substrates:** Scc1, Swe1, Bfa1, Cdc15, Spc72, and several cytokinetic regulators. The evidence for individual proteins varies, but these assignments are supported by combinations of physical interaction, in-vitro phosphorylation, phosphosite dependence, acute inhibition, genetics, or localization experiments. (paulson2006chemicalgeneticanalysis pages 72-76, park2004novelfunctionaldissection pages 1-2, botchkarev2018functionsandregulation pages 4-6, botchkarev2018functionsandregulation pages 3-4)

**Important uncertainty:** the exact causal sequence through which Cdc5 activates FEAR and releases Cdc14 remains model-dependent; direct Net1 phosphorylation should be annotated with qualification. Likewise, the detailed SPB-scaffold model for DNA-damage adaptation was emerging in 2024, and meiotic direct substrates remain less completely resolved than mitotic ones. (botchkarev2018functionsandregulation pages 4-6, botchkarev2018functionsandregulation pages 9-11)

## Final functional annotation

**CDC5/YMR001C encodes the sole budding-yeast Polo-like serine/threonine protein kinase. Cdc5 uses an N-terminal ATP/Mg²⁺-dependent catalytic domain and a C-terminal two-polo-box targeting domain to recognize primed phosphoproteins and noncanonical partners at chromosomes, spindle pole bodies, the nucleolus, and the bud neck. It phosphorylates substrates governing Swe1/Cdk1 activation, cohesin cleavage, FEAR/MEN-dependent Cdc14 release, spindle positioning, and cytokinesis; it additionally promotes checkpoint adaptation and meiotic prophase exit. Its defining biological function is therefore the spatial and temporal coordination of late cell-cycle transitions rather than one isolated linear pathway.**

References

1. (paulson2006chemicalgeneticanalysis pages 66-72): JL Paulson. Chemical genetic analysis of signaling by the saccharomyces cerevisiae mitotic kinases cdc15, dbf2, and cdc5. Unknown journal, 2006.

2. (paulson2006chemicalgeneticanalysis pages 88-92): JL Paulson. Chemical genetic analysis of signaling by the saccharomyces cerevisiae mitotic kinases cdc15, dbf2, and cdc5. Unknown journal, 2006.

3. (botchkarev2018functionsandregulation pages 1-3): Vladimir V. Botchkarev and James E. Haber. Functions and regulation of the polo-like kinase cdc5 in the absence and presence of dna damage. Current Genetics, 64:87-96, Aug 2018. URL: https://doi.org/10.1007/s00294-017-0727-2, doi:10.1007/s00294-017-0727-2. This article has 47 citations and is from a peer-reviewed journal.

4. (park2004novelfunctionaldissection pages 1-2): Jung-Eun Park, Chong J. Park, Krisada Sakchaisri, Tatiana Karpova, Satoshi Asano, James McNally, Yangil Sunwoo, Sun-Hee Leem, and Kyung S. Lee. Novel functional dissection of the localization-specific roles of budding yeast polo kinase cdc5p. Molecular and Cellular Biology, 24:9873-9886, Nov 2004. URL: https://doi.org/10.1128/mcb.24.22.9873-9886.2004, doi:10.1128/mcb.24.22.9873-9886.2004. This article has 53 citations and is from a domain leading peer-reviewed journal.

5. (botchkarev2018functionsandregulation pages 4-6): Vladimir V. Botchkarev and James E. Haber. Functions and regulation of the polo-like kinase cdc5 in the absence and presence of dna damage. Current Genetics, 64:87-96, Aug 2018. URL: https://doi.org/10.1007/s00294-017-0727-2, doi:10.1007/s00294-017-0727-2. This article has 47 citations and is from a peer-reviewed journal.

6. (almawi2020distinctsurfaceson pages 1-2): Ahmad W. Almawi, Laurence Langlois-Lemay, Stephen Boulton, Javier Rodríguez González, Giuseppe Melacini, Damien D’Amours, and Alba Guarné. Distinct surfaces on cdc5/plk polo-box domain orchestrate combinatorial substrate recognition during cell division. Scientific Reports, Feb 2020. URL: https://doi.org/10.1038/s41598-020-60344-4, doi:10.1038/s41598-020-60344-4. This article has 18 citations and is from a peer-reviewed journal.

7. (langloislemay2025centrosomescaffoldsandb pages 222-226): L Langlois-Lemay. Centrosome scaffolds and combinatorial pbd binding as drivers of functional diversity in the budding yeast polo-like kinase cdc5. Unknown journal, 2025.

8. (langloislemay2025centrosomescaffoldsanda pages 222-226): L Langlois-Lemay. Centrosome scaffolds and combinatorial pbd binding as drivers of functional diversity in the budding yeast polo-like kinase cdc5. Unknown journal, 2025.

9. (park2004novelfunctionaldissection pages 12-13): Jung-Eun Park, Chong J. Park, Krisada Sakchaisri, Tatiana Karpova, Satoshi Asano, James McNally, Yangil Sunwoo, Sun-Hee Leem, and Kyung S. Lee. Novel functional dissection of the localization-specific roles of budding yeast polo kinase cdc5p. Molecular and Cellular Biology, 24:9873-9886, Nov 2004. URL: https://doi.org/10.1128/mcb.24.22.9873-9886.2004, doi:10.1128/mcb.24.22.9873-9886.2004. This article has 53 citations and is from a domain leading peer-reviewed journal.

10. (botchkarev2018functionsandregulation pages 3-4): Vladimir V. Botchkarev and James E. Haber. Functions and regulation of the polo-like kinase cdc5 in the absence and presence of dna damage. Current Genetics, 64:87-96, Aug 2018. URL: https://doi.org/10.1007/s00294-017-0727-2, doi:10.1007/s00294-017-0727-2. This article has 47 citations and is from a peer-reviewed journal.

11. (botchkarev2018functionsandregulation pages 9-11): Vladimir V. Botchkarev and James E. Haber. Functions and regulation of the polo-like kinase cdc5 in the absence and presence of dna damage. Current Genetics, 64:87-96, Aug 2018. URL: https://doi.org/10.1007/s00294-017-0727-2, doi:10.1007/s00294-017-0727-2. This article has 47 citations and is from a peer-reviewed journal.

12. (paulson2006chemicalgeneticanalysis pages 72-76): JL Paulson. Chemical genetic analysis of signaling by the saccharomyces cerevisiae mitotic kinases cdc15, dbf2, and cdc5. Unknown journal, 2006.

13. (langloislemay2025centrosomescaffoldsand pages 36-39): L Langlois-Lemay. Centrosome scaffolds and combinatorial pbd binding as drivers of functional diversity in the budding yeast polo-like kinase cdc5. Unknown journal, 2025.

14. (langloislemay2025centrosomescaffoldsand pages 171-173): L Langlois-Lemay. Centrosome scaffolds and combinatorial pbd binding as drivers of functional diversity in the budding yeast polo-like kinase cdc5. Unknown journal, 2025.

## Artifacts

- [Edison artifact artifact-00](CDC5-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. almawi2020distinctsurfaceson pages 1-2
2. botchkarev2018functionsandregulation pages 1-3
3. langloislemay2025centrosomescaffoldsandb pages 222-226
4. langloislemay2025centrosomescaffoldsand pages 171-173
5. botchkarev2018functionsandregulation pages 9-11
6. paulson2006chemicalgeneticanalysis pages 72-76
7. paulson2006chemicalgeneticanalysis pages 66-72
8. paulson2006chemicalgeneticanalysis pages 88-92
9. park2004novelfunctionaldissection pages 1-2
10. botchkarev2018functionsandregulation pages 4-6
11. langloislemay2025centrosomescaffoldsanda pages 222-226
12. park2004novelfunctionaldissection pages 12-13
13. botchkarev2018functionsandregulation pages 3-4
14. langloislemay2025centrosomescaffoldsand pages 36-39
15. 10.1007/s00294-017-0727-2
16. 10.1016/j.heliyon.2019.e03050
17. 10.1038/s41598-020-60344-4
18. 10.1074/jbc.M116.727438
19. 10.1128/MCB.24.22.9873-9886.2004
20. 10.1091/mbc.E08-10-1049
21. 10.1074/jbc.C300059200
22. 10.1083/jcb.152.3.451
23. 10.1101/2024.06.13.598907
24. 10.3390/ijms252312861
25. https://doi.org/10.1038/s41598-020-60344-4.
26. https://doi.org/10.1128/MCB.24.22.9873-9886.2004.
27. https://doi.org/10.1083/jcb.152.3.451.
28. https://doi.org/10.1007/s00294-017-0727-2
29. https://doi.org/10.1016/j.heliyon.2019.e03050
30. https://doi.org/10.1038/s41598-020-60344-4
31. https://doi.org/10.1074/jbc.M116.727438
32. https://doi.org/10.1128/MCB.24.22.9873-9886.2004
33. https://doi.org/10.1091/mbc.E08-10-1049
34. https://doi.org/10.1074/jbc.C300059200
35. https://doi.org/10.1083/jcb.152.3.451
36. https://doi.org/10.1101/2024.06.13.598907
37. https://doi.org/10.3390/ijms252312861
38. https://doi.org/10.1371/journal.pgen.1000763.
39. https://doi.org/10.1101/2024.06.13.598907.
40. https://doi.org/10.3390/ijms252312861.
41. https://doi.org/10.1007/s00294-017-0727-2,
42. https://doi.org/10.1128/mcb.24.22.9873-9886.2004,
43. https://doi.org/10.1038/s41598-020-60344-4,