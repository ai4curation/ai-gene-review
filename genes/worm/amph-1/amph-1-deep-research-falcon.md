---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-27T15:28:41.933712'
end_time: '2026-09-27T15:38:31.707789'
duration_seconds: 589.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: amph-1
  gene_symbol: amph-1
  uniprot_accession: Q21004
  protein_description: 'SubName: Full=Amphiphysin {ECO:0000313|EMBL:CAA92465.1};'
  gene_info: Name=amph-1 {ECO:0000313|EMBL:CAA92465.1, ECO:0000313|WormBase:F58G6.1};
    ORFNames=CELE_F58G6.1 {ECO:0000313|EMBL:CAA92465.1}, F58G6.1 {ECO:0000313|WormBase:F58G6.1};
  organism_full: Caenorhabditis elegans.
  protein_family: Not specified in UniProt
  protein_domains: AH/BAR_dom_sf. (IPR027267); Amphiphysin. (IPR003005); BAR_dom.
    (IPR004148); SH3-like_dom_sf. (IPR036028); SH3_domain. (IPR001452)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: amph-1-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q21004
- **Protein Description:** SubName: Full=Amphiphysin {ECO:0000313|EMBL:CAA92465.1};
- **Gene Information:** Name=amph-1 {ECO:0000313|EMBL:CAA92465.1, ECO:0000313|WormBase:F58G6.1}; ORFNames=CELE_F58G6.1 {ECO:0000313|EMBL:CAA92465.1}, F58G6.1 {ECO:0000313|WormBase:F58G6.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AH/BAR_dom_sf. (IPR027267); Amphiphysin. (IPR003005); BAR_dom. (IPR004148); SH3-like_dom_sf. (IPR036028); SH3_domain. (IPR001452)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "amph-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'amph-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **amph-1** (gene ID: amph-1, UniProt: Q21004) in worm.

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
- **UniProt Accession:** Q21004
- **Protein Description:** SubName: Full=Amphiphysin {ECO:0000313|EMBL:CAA92465.1};
- **Gene Information:** Name=amph-1 {ECO:0000313|EMBL:CAA92465.1, ECO:0000313|WormBase:F58G6.1}; ORFNames=CELE_F58G6.1 {ECO:0000313|EMBL:CAA92465.1}, F58G6.1 {ECO:0000313|WormBase:F58G6.1};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Not specified in UniProt
- **Key Domains:** AH/BAR_dom_sf. (IPR027267); Amphiphysin. (IPR003005); BAR_dom. (IPR004148); SH3-like_dom_sf. (IPR036028); SH3_domain. (IPR001452)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "amph-1" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'amph-1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **amph-1** (gene ID: amph-1, UniProt: Q21004) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *C. elegans amph-1* / AMPH-1 (UniProt Q21004)

## Executive conclusion

The requested identity is verified. The *Caenorhabditis elegans* gene **amph-1**, also designated **F58G6.1**, encodes AMPH-1, the worm’s sole identified Amphiphysin/BIN1-family protein. Its experimentally described architecture—an N-terminal amphipathic H0 helix and BAR domain forming an **N-BAR membrane-remodeling module**, followed by a flexible region and C-terminal **SH3 domain**—agrees with the supplied UniProt Q21004 and InterPro annotations. This report does not conflate it with mammalian AMPH1, human BIN1, or “AMPH” as an abbreviation for amphetamine. (pant2009amph1amphiphysinbin1functionswith pages 3-4, pant2009amph1amphiphysinbin1functionswith pages 14-18, gai2025gtphydrolysistriggers pages 1-2, gai2025gtphydrolysistriggers pages 2-3)

The strongest current interpretation is that AMPH-1 is a **membrane-remodeling scaffold/adaptor and low-turnover guanine-nucleotide enzyme** whose principal established function is to form and organize tubular-vesicular carriers in the endocytic recycling pathway. It binds acidic membranes, bends and tubulates them through its N-BAR module, recruits trafficking regulators through NPF and SH3-mediated interactions, and coordinates cargo transfer from RAB-5-positive early endosomes toward RAB-10/RME-1-positive recycling compartments and ultimately the plasma membrane. A distinct perinuclear pool links the nuclear envelope to actin and microtubules and contributes to nuclear positioning. (pant2009amph1amphiphysinbin1functionswith pages 3-4, liu2015basolateralendocyticrecycling pages 1-2, liu2015basolateralendocyticrecycling pages 14-16, d’alessandro2015amphiphysin2orchestrates pages 4-6, gai2025gtphydrolysistriggers pages 9-11)

## Evidence overview

| Functional layer | Direct finding | Experimental basis | Quantitative result | Source/date/DOI URL |
|---|---|---|---|---|
| Identity and architecture | **Direct worm evidence:** F58G6.1 encodes AMPH-1, the sole *C. elegans* Amphiphysin/BIN1-family protein. It has an N-terminal amphipathic H0 helix followed by a BAR domain—together forming an N-BAR membrane-remodeling module—and a C-terminal SH3 domain. This matches UniProt Q21004 and is not mammalian AMPH1. | Gene/deletion mapping, sequence/domain analysis, family comparison, and full-length/domain constructs. | The 2025 construct map places H0 at residues 1–16, BAR approximately 17–240, and SH3 approximately 400–461. | Pant et al., November 2009, [10.1038/ncb1986](https://doi.org/10.1038/ncb1986) (pant2009amph1amphiphysinbin1functionswith pages 3-4, pant2009amph1amphiphysinbin1functionswith pages 14-18); Gai et al., 1 August 2025 (newer than the requested 2023–2024 priority window), [10.1126/sciadv.ads9443](https://doi.org/10.1126/sciadv.ads9443) (gai2025gtphydrolysistriggers pages 1-2, gai2025gtphydrolysistriggers pages 2-3) |
| RME-1/EHD-dependent recycling | **Direct worm evidence:** AMPH-1 localizes to basolateral recycling endosomes, binds the EH domain of RME-1 through two NPF[D/E] motifs, and cooperates with RME-1 to remodel membranes and return transmembrane cargo to the plasma membrane. Loss of AMPH-1 disrupts recycling-endosome tubules rather than clathrin-coated pits or early/late endosomes. | Endogenous/GFP colocalization, yeast two-hybrid and GST pull-downs, *amph-1(tm1060)* deletion analysis, cargo reporters, rescue with NPF mutants, and liposome electron microscopy. | *amph-1* null animals showed **>10-fold** increases in intracellular hTac-GFP and hTfR-GFP puncta. Purified AMPH-1 produced approximately **50-nm-wide, 1.1-µm-long** tubules; AMPH-1–RME-1 tubules were about **one-third** the length of single-protein tubules. | Pant et al., November 2009, [10.1038/ncb1986](https://doi.org/10.1038/ncb1986) (pant2009amph1amphiphysinbin1functionswith pages 3-4, pant2009amph1amphiphysinbin1functionswith pages 8-9, pant2010membraneremodelingby pages 61-65, pant2010membraneremodelingby pages 56-61) |
| RAB-10–TBC-2–RAB-5 cascade | **Direct worm evidence:** AMPH-1’s SH3 domain binds a proline-rich TBC-2 sequence and, together with active RAB-10, recruits the RAB-5 GAP TBC-2 to intestinal endosomes. This promotes RAB-5 inactivation and cargo exit from early endosomes. AMPH-1 also pulls down RAB-10, but RAB-10 is not required for AMPH-1 membrane association. | Yeast two-hybrid mapping, GST pull-down, live-worm colocalization, *amph-1*, *rab-10*, and *tbc-2* mutants, interaction-defective TBC-2 rescue constructs, cargo imaging, and membrane/cytosol fractionation. TBC-2 P150A, P153A, or R155A disrupted AMPH-1 binding. | RAB-5/RAB-10 overlap rose from approximately **53%** in wild type to **76%** in *amph-1* mutants. TBC-2 endosomal signal was strongly reduced in *amph-1* animals (**n = 18; P < 0.001**), RAB-5 membrane association increased, and hTAC cargo accumulated in RAB-5-positive endosomes. | Liu & Grant, 22 September 2015, [10.1371/journal.pgen.1005514](https://doi.org/10.1371/journal.pgen.1005514) (liu2015basolateralendocyticrecycling pages 1-2, liu2015basolateralendocyticrecycling pages 5-6, liu2015basolateralendocyticrecycling pages 6-9, liu2015basolateralendocyticrecycling pages 9-11, liu2015basolateralendocyticrecycling pages 11-14) |
| GTPase/H0 membrane-remodeling mechanism | **Direct biochemical evidence using worm AMPH-1:** AMPH-1 is a guanine-nucleotide-binding, GTP-hydrolyzing N-BAR protein. GTP binding drives deep H0-helix insertion and stable membrane association while suppressing oligomerization; hydrolysis to GDP releases the helices into a shallower position, allowing H0-mediated assembly of stacked rings that curve and tubulate the membrane before fission. This is a major update to the earlier view of AMPH-1 as only a passive BAR scaffold. | MANT-nucleotide binding, steady-state GTP hydrolysis, H0 deletion and L9Q mutants, liposome sedimentation/tubulation, FRET, fluorescence-quenching membrane-depth assays, disulfide cross-linking, dynamic light scattering, and cryo-EM. | Apparent **Kd ≈ 75 µM** for GTP; **kcat = 0.05 ± 0.002 min⁻¹** and **Km = 200 ± 60 µM**. GMPPNP caused about **sixfold** H0-probe fluorescence enhancement. The approximately **8-Å** cryo-EM map showed five-dimer stacked rings, **50.2-Å rise**, **−33.2° twist**, approximately **35-nm external diameter**, and approximately **25-nm lumen**. | Gai et al., 1 August 2025—**newer than the user’s 2023–2024 priority window**—[10.1126/sciadv.ads9443](https://doi.org/10.1126/sciadv.ads9443) (gai2025gtphydrolysistriggers pages 1-2, gai2025gtphydrolysistriggers pages 2-3, gai2025gtphydrolysistriggers pages 3-4, gai2025gtphydrolysistriggers pages 5-6, gai2025gtphydrolysistriggers pages 7-8, gai2025gtphydrolysistriggers pages 8-9, gai2025gtphydrolysistriggers pages 9-11) |
| Nuclear positioning: ANC-1/CLIP-1 | **Direct worm evidence:** AMPH-1 has a second, spatially distinct role around nuclei, where it associates with the nesprin ortholog ANC-1 and the microtubule-plus-end protein CLIP-1 to connect the nuclear envelope to actin and microtubules. *amph-1* loss causes clustered, misshapen seam-cell and hypodermal nuclei; an ANC-1 KASH–CLIP-1 CAP-GLY fusion bypasses AMPH-1 loss. **Mammalian conservation:** BIN1 similarly binds nesprin-2, actin, and CLIP170, but those mammalian results are not direct evidence for Q21004. | Worm RNAi and *amph-1(tm1060)* genetics, fluorescence/CLEM, co-immunoprecipitation, colocalization, epistasis, and fusion-protein rescue; complementary mammalian cell and patient-muscle experiments. | Nuclear-position assays were repeated three times with **n ≥ 60 per genotype** and showed significant defects (**P < 0.001**). The *anc-1; amph-1* double mutant was not more severe than either single mutant, supporting a shared pathway. | D’Alessandro et al., 26 October 2015, [10.1016/j.devcel.2015.09.018](https://doi.org/10.1016/j.devcel.2015.09.018) (d’alessandro2015amphiphysin2orchestrates pages 1-3, d’alessandro2015amphiphysin2orchestrates pages 3-4, d’alessandro2015amphiphysin2orchestrates pages 4-6) |
| Aβ-induced membrane-repair model | **Direct worm disease-model evidence, not proof of endogenous Alzheimer disease:** In intestinal cells exposed to bacterially produced human Aβ1–42, loss of *amph-1* increased formation of RAB-5/RME-1-positive endosomes in a calpain-dependent membrane-repair response. This supports use of the worm BIN1 ortholog to study how membrane trafficking modifies Aβ-induced damage; it does not establish AMPH-1 as a worm Aβ receptor or demonstrate a direct AMPH-1–Aβ interaction. | *vha-6::mCherry* intestinal reporter, Aβ/CRY5B feeding, *amph-1* deletion and RNAi, RAB-5 and RME-1 markers, anti-Aβ super-resolution imaging, and genetic epistasis with *clp-4* calpain. | Aβ-induced endocytosis increased significantly after *amph-1* loss; *clp-4* loss completely blocked the increase caused by *amph-1* RNAi. Reported comparisons reached **P < 0.05** or **P < 0.01**, depending on condition. | Julien et al., November 2018, [10.1186/s40478-018-0634-x](https://doi.org/10.1186/s40478-018-0634-x) (julien2018invivoinduction pages 4-5, julien2018invivoinduction pages 5-7) |


*Table: Evidence matrix for *C. elegans* AMPH-1/Q21004, separating direct worm findings from mammalian conservation and summarizing the strongest quantitative support. The 2025 GTPase mechanism is explicitly identified as newer than the requested 2023–2024 priority period.*

## 1. Identity, family, and molecular architecture

Pant and colleagues identified F58G6.1 as AMPH-1 and described it as the **only *C. elegans* member of the Amphiphysin/BIN1 family**. The protein contains BAR and SH3 domains and two NPF[D/E] motifs. The 2025 structural-biochemical work maps the amphipathic H0 segment to approximately residues 1–16, the BAR region to approximately residues 17–240, and the SH3 domain near residues 400–461. Thus the supplied AH/BAR, amphiphysin, BAR, SH3-like, and SH3 annotations are mutually consistent with the experimental literature. (pant2009amph1amphiphysinbin1functionswith pages 3-4, pant2009amph1amphiphysinbin1functionswith pages 14-18, gai2025gtphydrolysistriggers pages 2-3)

Functionally, these elements divide AMPH-1 into two coupled systems:

- The **H0–BAR/N-BAR module** binds negatively charged phospholipids, dimerizes into an arc-shaped scaffold, senses or generates curvature, and drives membrane tubulation and fission.
- The **NPF[D/E] motifs** bind the EH domain of RME-1/EHD1.
- The **SH3 domain** recruits proline-rich partners, notably the RAB-5 GAP TBC-2, thereby coupling membrane shape to Rab-state regulation. (pant2009amph1amphiphysinbin1functionswith pages 14-18, pant2010membraneremodelingby pages 61-65, liu2015basolateralendocyticrecycling pages 5-6, gai2025gtphydrolysistriggers pages 9-11)

## 2. Primary biochemical function

### Membrane binding and remodeling

AMPH-1 is not a transporter and has no transported substrate. Its broader structural role is to bind cytosolic membrane surfaces and convert relatively low-curvature endosomal membrane into narrow tubules and ultimately transport carriers. Purified protein bound acidic phosphatidylserine-containing membranes, including PS/PIP2 and PS/PI4P liposomes, but not neutral phosphatidylcholine liposomes. In early assays it converted 400-nm liposomes into tubules approximately **50 nm wide and 1.1 μm long**. AMPH-1 and RME-1 together formed shorter, more rigid, regularly coated tubules distinct from structures made by either protein alone. (pant2010membraneremodelingby pages 61-65)

Deletion of the first 16 residues eliminated detectable liposome binding and tubulation without measurably destabilizing the protein, demonstrating that the H0 helix is required rather than merely accessory. The membrane-fission-defective L9Q mutation similarly reduced oligomer formation and uncoupled membrane insertion from nucleotide state. (gai2025gtphydrolysistriggers pages 2-3, gai2025gtphydrolysistriggers pages 3-4, gai2025gtphydrolysistriggers pages 7-8)

### Enzymatic activity and substrate specificity

Recent work materially changes the annotation: purified AMPH-1 directly binds and hydrolyzes **GTP**, whereas comparable fluorescence enhancement was not observed with MANT-ATP. Reported apparent kinetic parameters were **Kd ≈75 μM for GTP**, **kcat = 0.05 ± 0.002 min⁻¹**, and **Km = 200 ± 60 μM**. Its demonstrated enzymatic substrate is therefore GTP, producing GDP and inorganic phosphate; the low turnover is consistent with a mechanochemical regulatory cycle rather than a high-flux metabolic enzyme. (gai2025gtphydrolysistriggers pages 2-3)

The nucleotide cycle regulates membrane remodeling:

1. **GTP-bound state:** H0 helices insert relatively deeply into the bilayer, stabilizing membrane association but preventing productive contacts between AMPH-1 dimers. Nonhydrolyzable GMPPNP therefore supports binding while inhibiting organized tubulation.
2. **After hydrolysis/GDP-bound state:** H0 helices move to a shallower position, favoring positive curvature and becoming available for interdimer contacts.
3. **Scaffold assembly:** AMPH-1 homodimers assemble into stacked rings around narrow membrane tubules, preparing the membrane for fission and carrier formation. (gai2025gtphydrolysistriggers pages 1-2, gai2025gtphydrolysistriggers pages 5-6, gai2025gtphydrolysistriggers pages 7-8, gai2025gtphydrolysistriggers pages 9-11)

A 2025 cryo-EM reconstruction at approximately **8 Å** showed five-homodimer stacked rings with a **50.2-Å axial rise**, **−33.2° rotational offset**, approximately **35-nm external diameter**, and a membrane lumen of approximately **25 nm**. The unresolved flexible middle and SH3 regions were excluded from fitting, so the reconstruction most directly supports the N-BAR lattice rather than a complete atomic structure of full-length AMPH-1. (gai2025gtphydrolysistriggers pages 7-8, gai2025gtphydrolysistriggers pages 8-9)

## 3. Cellular localization

### Recycling endosomes

The best-established site of action is the **cytoplasmic face of tubulovesicular basolateral recycling endosomes**, particularly in intestinal epithelial cells. Endogenous or tagged AMPH-1 colocalized with RME-1/EHD and SDPN-1/syndapin. It showed little or no colocalization with clathrin-coated pits, Golgi, or canonical early- and late-endosomal markers in the original analysis. Loss of AMPH-1 largely eliminated normal RME-1-positive tubules and altered SDPN-1 structures, while DYN-1/dynamin and clathrin localization remained comparatively normal. This argues that its dominant intestinal function is recycling-endosome remodeling rather than initial plasma-membrane internalization. (pant2009amph1amphiphysinbin1functionswith pages 3-4, pant2010membraneremodelingby pages 56-61)

AMPH-1 remains membrane-associated in *rme-1* null mutants, although it redistributes onto enlarged structures. RME-1 is consequently a cooperating effector rather than the sole membrane receptor for AMPH-1. Conversely, RAB-10 loss increased rather than abolished AMPH-1-positive puncta and tubules, potentially because RAB-10 mutants have increased endosomal PI(4,5)P2. (pant2010membraneremodelingby pages 61-65, liu2015basolateralendocyticrecycling pages 9-11)

### Perinuclear localization

A second pool occurs around intestinal and epithelial nuclei. AMPH-1 partially colocalizes with the nesprin ortholog ANC-1 at the nuclear rim and on perinuclear structures. AMPH-1 perinuclear localization was lost after ANC-1 depletion, whereas ANC-1 remained at the nuclear envelope after AMPH-1 loss, placing ANC-1 upstream in localization. (d’alessandro2015amphiphysin2orchestrates pages 4-6)

### Neurons

AMPH-1::GFP has been imaged in the worm nerve cord at synaptic release sites in work on lipid regulation of synaptic-vesicle recycling. However, the strongest AMPH-1-specific genetic and mechanistic evidence concerns intestinal recycling and nuclear positioning; a primary, indispensable AMPH-1 role in worm synaptic-vesicle endocytosis is less firmly established than the corresponding role often assigned to vertebrate amphiphysin. The neuronal observations should therefore be treated as supporting localization rather than the basis for the primary annotation. (marza2008polyunsaturatedfattyacids pages 3-4)

## 4. Pathway context and interaction network

### AMPH-1–RME-1 carrier formation

AMPH-1 contains two NPF[D/E] motifs that bind the EH domain of RME-1. Yeast two-hybrid and GST pull-down experiments demonstrated direct association, and mutation of either NPF motif or nearby acidic residues impaired binding. A double F309A/F363A AMPH-1 protein was expressed at approximately normal levels but failed to rescue cargo accumulation or RME-1 localization defects, demonstrating that this interaction is functionally important in vivo. (pant2009amph1amphiphysinbin1functionswith pages 14-18, pant2010membraneremodelingby pages 61-65)

The inferred sequence is that AMPH-1 binds and curves the recycling-endosome membrane, recruits or organizes RME-1, and jointly constructs coated tubular carriers. RME-1 is an ATPase, so the complex combines AMPH-1’s GTP-regulated N-BAR cycle with RME-1’s ATP-dependent remodeling activity. Earlier results showing nucleotide dependence attributable to RME-1 should not be mistaken for evidence against AMPH-1 GTPase activity; AMPH-1’s own GTPase activity was established later. (pant2009amph1amphiphysinbin1functionswith pages 8-9, gai2025gtphydrolysistriggers pages 2-3)

### RAB-10–AMPH-1–TBC-2 control of RAB-5

In basolateral intestinal recycling, AMPH-1 and active RAB-10 recruit **TBC-2**, a GAP for the earlier-acting GTPase RAB-5. The AMPH-1 SH3 domain binds a proline-rich TBC-2 segment spanning residues 146–160; TBC-2 P150A, P153A, or R155A substitutions disrupted AMPH-1 binding while retaining RAB-10 binding. RAB-10 binds a separate TBC-2 region at residues 279–321. This provides a coincidence-detection mechanism that positions TBC-2 where recycling-endosome identity and AMPH-1-shaped membrane converge. (liu2015basolateralendocyticrecycling pages 2-5, liu2015basolateralendocyticrecycling pages 5-6, liu2015basolateralendocyticrecycling pages 6-9)

Without AMPH-1, TBC-2 becomes diffuse rather than punctate, RAB-5 membrane association increases, and cargo remains in RAB-5-positive early endosomes. RAB-5/RAB-10 overlap increased from approximately **53% in wild type to 76% in *amph-1* mutants**. Thus AMPH-1 is not merely a membrane scaffold: it helps terminate early-endosomal RAB-5 identity so cargo can progress into the RAB-10-controlled recycling pathway. (liu2015basolateralendocyticrecycling pages 6-9, liu2015basolateralendocyticrecycling pages 9-11, liu2015basolateralendocyticrecycling pages 11-14)

### Integrated model

The most coherent pathway model is:

**RAB-5 early endosome → AMPH-1/RAB-10 recruitment of TBC-2 → RAB-5 inactivation and compartment separation → AMPH-1/RME-1-dependent tubular carrier assembly → return of cargo to the basolateral plasma membrane.**

AMPH-1 thereby couples three processes that are often annotated separately: membrane curvature, Rab conversion, and carrier formation. (liu2015basolateralendocyticrecycling pages 1-2, liu2015basolateralendocyticrecycling pages 11-14, liu2015basolateralendocyticrecycling pages 14-16)

## 5. Loss-of-function phenotypes and quantitative evidence

The deletion allele *amph-1(tm1060)* is treated as a null in the principal studies. In intestinal epithelia, intracellular hTac-GFP and hTfR-GFP puncta increased by **more than tenfold**, normal RME-1 tubules were largely lost, and recycling cargo accumulated in RAB-5-positive compartments. Interaction-defective AMPH-1 or TBC-2 constructs failed to rescue corresponding cargo phenotypes, strengthening the causal connection between binding and pathway function. (pant2009amph1amphiphysinbin1functionswith pages 3-4, pant2010membraneremodelingby pages 56-61, liu2015basolateralendocyticrecycling pages 6-9)

Loss of AMPH-1 also caused increased RAB-5 membrane-to-cytosol ratio in biochemical fractionation experiments and significantly increased RAB-5/RAB-10 colocalization. The effect was less severe than complete TBC-2 loss, consistent with residual TBC-2 recruitment through partners such as RAB-10. (liu2015basolateralendocyticrecycling pages 9-11, liu2015basolateralendocyticrecycling pages 11-14)

In epithelial seam cells, AMPH-1 RNAi or *tm1060* caused unevenly spaced, clustered, and misshapen nuclei. These were not interconnected, arguing against failed cytokinesis. Similar defects occurred during hypodermal nuclear positioning. Assays were repeated three times with **n ≥60 per genotype** and reported **P<0.001** for the principal comparisons. Lack of additivity in *anc-1; amph-1* mutants supports a shared pathway. (d’alessandro2015amphiphysin2orchestrates pages 3-4)

## 6. Distinct role in nuclear positioning

AMPH-1 also acts as a cytoskeletal adaptor at the nuclear envelope. Worm AMPH-1 co-immunoprecipitated with a mini-ANC-1/nesprin construct and with CLIP-1, the worm counterpart of the microtubule-plus-end protein CLIP170. A fusion directly linking the CLIP-1 CAP-GLY microtubule-binding module to the ANC-1 KASH nuclear-envelope anchor rescued *amph-1* nuclear-positioning defects. This bypass experiment strongly supports the model that AMPH-1 helps link the nuclear envelope to microtubules; complementary evidence implicates actin as well. (d’alessandro2015amphiphysin2orchestrates pages 4-6)

The nuclear-positioning function is conserved in mammalian BIN1 systems, including patient-derived cells, but those mammalian observations should be interpreted as evolutionary support—not direct evidence about every molecular interaction of Q21004. (d’alessandro2015amphiphysin2orchestrates pages 1-3, d’alessandro2015amphiphysin2orchestrates pages 4-6)

## 7. Recent developments

The main 2023 development was a *Traffic* study, “GTP-stimulated membrane fission by the N-BAR protein AMPH-1,” published online in December 2023 ([DOI 10.1111/tra.12875](https://doi.org/10.1111/tra.12875)). It reported that purified AMPH-1 can tubulate and vesiculate liposomes and that guanine nucleotides stimulate membrane fission. The paper was identified bibliographically, although its full text was not retrievable through the available corpus.

The most consequential mechanistic advance appeared after the requested 2023–2024 priority period: Gai et al., published **1 August 2025** in *Science Advances*, [DOI 10.1126/sciadv.ads9443](https://doi.org/10.1126/sciadv.ads9443). This work supplied binding and hydrolysis kinetics, H0-helix mutants, fluorescence/FRET measurements, cross-linking, and cryo-EM evidence linking GTP hydrolysis to scaffold formation. It elevates AMPH-1 from a conventional BAR-domain coat protein to a **GTP-regulated mechanochemical membrane-remodeling system**. (gai2025gtphydrolysistriggers pages 1-2, gai2025gtphydrolysistriggers pages 2-3, gai2025gtphydrolysistriggers pages 8-9, gai2025gtphydrolysistriggers pages 9-11)

The targeted search found little additional 2023–2024 research directly centered on worm AMPH-1. Many recent papers returned by symbol-based searches instead concerned amphetamine (“AMPH”), mammalian AMPH1/BIN1, or other endosomal factors; these were excluded from gene-specific conclusions.

## 8. Current applications and translational relevance

AMPH-1 currently has applications as a **research model**, not as a clinical target with an established therapy:

1. **Mechanistic model for recycling-endosome carrier biogenesis.** The worm intestine permits live imaging of polarized trafficking and genetic dissection of the RAB-5/RAB-10/RME-1 transition.
2. **Biophysical model of BAR-protein membrane fission.** Purified AMPH-1 provides a tractable system for linking nucleotide state, amphipathic-helix depth, scaffold geometry, and fission.
3. **Model of BIN1-related cell biology.** Because human BIN1 is implicated in centronuclear myopathy and Alzheimer disease risk, worm AMPH-1 can reveal conserved membrane and cytoskeletal functions, although worm phenotypes cannot be directly equated with human disease.
4. **Aβ membrane-damage/repair assays.** In a worm intestinal model, human Aβ1–42 induced RAB-5/RME-1-positive endosomes. *amph-1* loss increased this response, while loss of the calpain *clp-4* blocked the increase caused by *amph-1* RNAi. This supports AMPH-1 as a modifier of membrane-repair trafficking, not as an Aβ receptor or proof of endogenous Alzheimer pathology in worms. (julien2018invivoinduction pages 4-5, julien2018invivoinduction pages 5-7)
5. **Nuclear-positioning and myopathy models.** The ANC-1–AMPH-1–CLIP-1 pathway offers a genetically accessible system for studying how BIN1-family proteins connect nuclear envelopes to cytoskeletons. (d’alessandro2015amphiphysin2orchestrates pages 1-3, d’alessandro2015amphiphysin2orchestrates pages 4-6)

## 9. Evidence-weighted annotation and unresolved questions

### Recommended primary annotation

**AMPH-1 is a cytosolic/peripheral-membrane N-BAR amphiphysin and low-turnover GTPase that binds acidic endosomal membranes, oligomerizes into curvature-generating scaffolds after GTP hydrolysis, recruits RME-1 and TBC-2, and promotes basolateral endocytic recycling from early/recycling endosomes to the plasma membrane. A perinuclear pool links ANC-1/nesprin to actin and CLIP-1-associated microtubules to maintain nuclear position.**

### Confidence assessment

- **High confidence:** identity, N-BAR/SH3 architecture, acidic-membrane binding, homodimerization, membrane tubulation, RME-1 interaction, basolateral recycling function, TBC-2 recruitment, RAB-5 down-regulation, and intestinal recycling-endosome localization.
- **High-to-moderate confidence:** intrinsic GTPase-regulated fission mechanism; the purified-protein evidence is extensive and quantitative, but direct in-vivo testing of nucleotide-binding/hydrolysis mutants remains less developed.
- **Moderate confidence:** nuclear-envelope/cytoskeletal adaptor role, supported by genetics, interactions, localization, and bypass rescue.
- **Limited or context-dependent:** an essential synaptic-vesicle endocytosis role in worms, direct relevance to Alzheimer disease, and tissue-specific deployment of the GTPase cycle outside intestinal recycling.

Important open questions include the structural basis of GTP recognition in a protein lacking a canonical small-GTPase fold, whether a cellular GEF/GAP-like regulator controls AMPH-1, how its GTP cycle is coordinated with the RME-1 ATPase cycle, and whether nucleotide-defective alleles reproduce the endosomal and nuclear phenotypes in vivo. (gai2025gtphydrolysistriggers pages 2-3, gai2025gtphydrolysistriggers pages 9-11)

References

1. (pant2009amph1amphiphysinbin1functionswith pages 3-4): Saumya Pant, Mahak Sharma, Kruti Patel, Steve Caplan, Chavela M. Carr, and Barth D. Grant. Amph-1/amphiphysin/bin1 functions with rme-1/ehd1 in endocytic recycling. Nov 2009. URL: https://doi.org/10.1038/ncb1986, doi:10.1038/ncb1986. This article has 271 citations and is from a highest quality peer-reviewed journal.

2. (pant2009amph1amphiphysinbin1functionswith pages 14-18): Saumya Pant, Mahak Sharma, Kruti Patel, Steve Caplan, Chavela M. Carr, and Barth D. Grant. Amph-1/amphiphysin/bin1 functions with rme-1/ehd1 in endocytic recycling. Nov 2009. URL: https://doi.org/10.1038/ncb1986, doi:10.1038/ncb1986. This article has 271 citations and is from a highest quality peer-reviewed journal.

3. (gai2025gtphydrolysistriggers pages 1-2): Wei Gai, Yuhang Wang, Brianna Martin, Junjie Zhang, C. Carr, and H. Rye. Gtp hydrolysis triggers membrane remodeling by amph-1. Science Advances, Aug 2025. URL: https://doi.org/10.1126/sciadv.ads9443, doi:10.1126/sciadv.ads9443. This article has 1 citations and is from a highest quality peer-reviewed journal.

4. (gai2025gtphydrolysistriggers pages 2-3): Wei Gai, Yuhang Wang, Brianna Martin, Junjie Zhang, C. Carr, and H. Rye. Gtp hydrolysis triggers membrane remodeling by amph-1. Science Advances, Aug 2025. URL: https://doi.org/10.1126/sciadv.ads9443, doi:10.1126/sciadv.ads9443. This article has 1 citations and is from a highest quality peer-reviewed journal.

5. (liu2015basolateralendocyticrecycling pages 1-2): Ou Liu and Barth D. Grant. Basolateral endocytic recycling requires rab-10 and amph-1 mediated recruitment of rab-5 gap tbc-2 to endosomes. PLOS Genetics, 11:e1005514, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005514, doi:10.1371/journal.pgen.1005514. This article has 47 citations and is from a domain leading peer-reviewed journal.

6. (liu2015basolateralendocyticrecycling pages 14-16): Ou Liu and Barth D. Grant. Basolateral endocytic recycling requires rab-10 and amph-1 mediated recruitment of rab-5 gap tbc-2 to endosomes. PLOS Genetics, 11:e1005514, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005514, doi:10.1371/journal.pgen.1005514. This article has 47 citations and is from a domain leading peer-reviewed journal.

7. (d’alessandro2015amphiphysin2orchestrates pages 4-6): Manuela D’Alessandro, Karim Hnia, Vincent Gache, Catherine Koch, Christos Gavriilidis, David Rodriguez, Anne-Sophie Nicot, Norma B. Romero, Yannick Schwab, Edgar Gomes, Michel Labouesse, and Jocelyn Laporte. Amphiphysin 2 orchestrates nucleus positioning and shape by linking the nuclear envelope to the actin and microtubule cytoskeleton. Developmental cell, 35 2:186-98, Oct 2015. URL: https://doi.org/10.1016/j.devcel.2015.09.018, doi:10.1016/j.devcel.2015.09.018. This article has 92 citations and is from a highest quality peer-reviewed journal.

8. (gai2025gtphydrolysistriggers pages 9-11): Wei Gai, Yuhang Wang, Brianna Martin, Junjie Zhang, C. Carr, and H. Rye. Gtp hydrolysis triggers membrane remodeling by amph-1. Science Advances, Aug 2025. URL: https://doi.org/10.1126/sciadv.ads9443, doi:10.1126/sciadv.ads9443. This article has 1 citations and is from a highest quality peer-reviewed journal.

9. (pant2009amph1amphiphysinbin1functionswith pages 8-9): Saumya Pant, Mahak Sharma, Kruti Patel, Steve Caplan, Chavela M. Carr, and Barth D. Grant. Amph-1/amphiphysin/bin1 functions with rme-1/ehd1 in endocytic recycling. Nov 2009. URL: https://doi.org/10.1038/ncb1986, doi:10.1038/ncb1986. This article has 271 citations and is from a highest quality peer-reviewed journal.

10. (pant2010membraneremodelingby pages 61-65): Saumya Pant. Membrane remodeling by novel regulators of the recycling endosome: the rme-1 and amph-1 partnership. ArXiv, Jan 2010. URL: https://doi.org/10.7282/t3sn093v, doi:10.7282/t3sn093v. This article has 0 citations.

11. (pant2010membraneremodelingby pages 56-61): Saumya Pant. Membrane remodeling by novel regulators of the recycling endosome: the rme-1 and amph-1 partnership. ArXiv, Jan 2010. URL: https://doi.org/10.7282/t3sn093v, doi:10.7282/t3sn093v. This article has 0 citations.

12. (liu2015basolateralendocyticrecycling pages 5-6): Ou Liu and Barth D. Grant. Basolateral endocytic recycling requires rab-10 and amph-1 mediated recruitment of rab-5 gap tbc-2 to endosomes. PLOS Genetics, 11:e1005514, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005514, doi:10.1371/journal.pgen.1005514. This article has 47 citations and is from a domain leading peer-reviewed journal.

13. (liu2015basolateralendocyticrecycling pages 6-9): Ou Liu and Barth D. Grant. Basolateral endocytic recycling requires rab-10 and amph-1 mediated recruitment of rab-5 gap tbc-2 to endosomes. PLOS Genetics, 11:e1005514, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005514, doi:10.1371/journal.pgen.1005514. This article has 47 citations and is from a domain leading peer-reviewed journal.

14. (liu2015basolateralendocyticrecycling pages 9-11): Ou Liu and Barth D. Grant. Basolateral endocytic recycling requires rab-10 and amph-1 mediated recruitment of rab-5 gap tbc-2 to endosomes. PLOS Genetics, 11:e1005514, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005514, doi:10.1371/journal.pgen.1005514. This article has 47 citations and is from a domain leading peer-reviewed journal.

15. (liu2015basolateralendocyticrecycling pages 11-14): Ou Liu and Barth D. Grant. Basolateral endocytic recycling requires rab-10 and amph-1 mediated recruitment of rab-5 gap tbc-2 to endosomes. PLOS Genetics, 11:e1005514, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005514, doi:10.1371/journal.pgen.1005514. This article has 47 citations and is from a domain leading peer-reviewed journal.

16. (gai2025gtphydrolysistriggers pages 3-4): Wei Gai, Yuhang Wang, Brianna Martin, Junjie Zhang, C. Carr, and H. Rye. Gtp hydrolysis triggers membrane remodeling by amph-1. Science Advances, Aug 2025. URL: https://doi.org/10.1126/sciadv.ads9443, doi:10.1126/sciadv.ads9443. This article has 1 citations and is from a highest quality peer-reviewed journal.

17. (gai2025gtphydrolysistriggers pages 5-6): Wei Gai, Yuhang Wang, Brianna Martin, Junjie Zhang, C. Carr, and H. Rye. Gtp hydrolysis triggers membrane remodeling by amph-1. Science Advances, Aug 2025. URL: https://doi.org/10.1126/sciadv.ads9443, doi:10.1126/sciadv.ads9443. This article has 1 citations and is from a highest quality peer-reviewed journal.

18. (gai2025gtphydrolysistriggers pages 7-8): Wei Gai, Yuhang Wang, Brianna Martin, Junjie Zhang, C. Carr, and H. Rye. Gtp hydrolysis triggers membrane remodeling by amph-1. Science Advances, Aug 2025. URL: https://doi.org/10.1126/sciadv.ads9443, doi:10.1126/sciadv.ads9443. This article has 1 citations and is from a highest quality peer-reviewed journal.

19. (gai2025gtphydrolysistriggers pages 8-9): Wei Gai, Yuhang Wang, Brianna Martin, Junjie Zhang, C. Carr, and H. Rye. Gtp hydrolysis triggers membrane remodeling by amph-1. Science Advances, Aug 2025. URL: https://doi.org/10.1126/sciadv.ads9443, doi:10.1126/sciadv.ads9443. This article has 1 citations and is from a highest quality peer-reviewed journal.

20. (d’alessandro2015amphiphysin2orchestrates pages 1-3): Manuela D’Alessandro, Karim Hnia, Vincent Gache, Catherine Koch, Christos Gavriilidis, David Rodriguez, Anne-Sophie Nicot, Norma B. Romero, Yannick Schwab, Edgar Gomes, Michel Labouesse, and Jocelyn Laporte. Amphiphysin 2 orchestrates nucleus positioning and shape by linking the nuclear envelope to the actin and microtubule cytoskeleton. Developmental cell, 35 2:186-98, Oct 2015. URL: https://doi.org/10.1016/j.devcel.2015.09.018, doi:10.1016/j.devcel.2015.09.018. This article has 92 citations and is from a highest quality peer-reviewed journal.

21. (d’alessandro2015amphiphysin2orchestrates pages 3-4): Manuela D’Alessandro, Karim Hnia, Vincent Gache, Catherine Koch, Christos Gavriilidis, David Rodriguez, Anne-Sophie Nicot, Norma B. Romero, Yannick Schwab, Edgar Gomes, Michel Labouesse, and Jocelyn Laporte. Amphiphysin 2 orchestrates nucleus positioning and shape by linking the nuclear envelope to the actin and microtubule cytoskeleton. Developmental cell, 35 2:186-98, Oct 2015. URL: https://doi.org/10.1016/j.devcel.2015.09.018, doi:10.1016/j.devcel.2015.09.018. This article has 92 citations and is from a highest quality peer-reviewed journal.

22. (julien2018invivoinduction pages 4-5): Carl Julien, Colson Tomberlin, Christine M. Roberts, Aumbreen Akram, Gretchen H. Stein, Michael A. Silverman, and Christopher D. Link. In vivo induction of membrane damage by β-amyloid peptide oligomers. Acta Neuropathologica Communications, Nov 2018. URL: https://doi.org/10.1186/s40478-018-0634-x, doi:10.1186/s40478-018-0634-x. This article has 61 citations and is from a peer-reviewed journal.

23. (julien2018invivoinduction pages 5-7): Carl Julien, Colson Tomberlin, Christine M. Roberts, Aumbreen Akram, Gretchen H. Stein, Michael A. Silverman, and Christopher D. Link. In vivo induction of membrane damage by β-amyloid peptide oligomers. Acta Neuropathologica Communications, Nov 2018. URL: https://doi.org/10.1186/s40478-018-0634-x, doi:10.1186/s40478-018-0634-x. This article has 61 citations and is from a peer-reviewed journal.

24. (marza2008polyunsaturatedfattyacids pages 3-4): Esther Marza, Toni Long, Adolfo Saiardi, Marija Sumakovic, Stefan Eimer, David H. Hall, and Giovanni M. Lesa. Polyunsaturated fatty acids influence synaptojanin localization to regulate synaptic vesicle recycling. Mar 2008. URL: https://doi.org/10.1091/mbc.e07-07-0719, doi:10.1091/mbc.e07-07-0719. This article has 84 citations and is from a domain leading peer-reviewed journal.

25. (liu2015basolateralendocyticrecycling pages 2-5): Ou Liu and Barth D. Grant. Basolateral endocytic recycling requires rab-10 and amph-1 mediated recruitment of rab-5 gap tbc-2 to endosomes. PLOS Genetics, 11:e1005514, Sep 2015. URL: https://doi.org/10.1371/journal.pgen.1005514, doi:10.1371/journal.pgen.1005514. This article has 47 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](amph-1-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. pant2010membraneremodelingby pages 61-65
2. gai2025gtphydrolysistriggers pages 2-3
3. marza2008polyunsaturatedfattyacids pages 3-4
4. gai2025gtphydrolysistriggers pages 1-2
5. liu2015basolateralendocyticrecycling pages 1-2
6. liu2015basolateralendocyticrecycling pages 14-16
7. gai2025gtphydrolysistriggers pages 9-11
8. pant2010membraneremodelingby pages 56-61
9. liu2015basolateralendocyticrecycling pages 5-6
10. liu2015basolateralendocyticrecycling pages 6-9
11. liu2015basolateralendocyticrecycling pages 9-11
12. liu2015basolateralendocyticrecycling pages 11-14
13. gai2025gtphydrolysistriggers pages 3-4
14. gai2025gtphydrolysistriggers pages 5-6
15. gai2025gtphydrolysistriggers pages 7-8
16. gai2025gtphydrolysistriggers pages 8-9
17. julien2018invivoinduction pages 4-5
18. julien2018invivoinduction pages 5-7
19. liu2015basolateralendocyticrecycling pages 2-5
20. 10.1038/ncb1986
21. 10.1126/sciadv.ads9443
22. D/E
23. 10.1371/journal.pgen.1005514
24. 10.1016/j.devcel.2015.09.018
25. 10.1186/s40478-018-0634-x
26. DOI 10.1111/tra.12875
27. DOI 10.1126/sciadv.ads9443
28. https://doi.org/10.1038/ncb1986
29. https://doi.org/10.1126/sciadv.ads9443
30. https://doi.org/10.1371/journal.pgen.1005514
31. https://doi.org/10.1016/j.devcel.2015.09.018
32. https://doi.org/10.1186/s40478-018-0634-x
33. https://doi.org/10.1111/tra.12875
34. https://doi.org/10.1038/ncb1986,
35. https://doi.org/10.1126/sciadv.ads9443,
36. https://doi.org/10.1371/journal.pgen.1005514,
37. https://doi.org/10.1016/j.devcel.2015.09.018,
38. https://doi.org/10.7282/t3sn093v,
39. https://doi.org/10.1186/s40478-018-0634-x,
40. https://doi.org/10.1091/mbc.e07-07-0719,