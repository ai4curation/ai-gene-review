---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-05-30T16:14:23.301202'
end_time: '2026-05-30T16:14:23.302760'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: Edem2
  gene_symbol: Edem2
  uniprot_accession: Q9VK27
  protein_description: 'RecName: Full=alpha-1,2-Mannosidase {ECO:0000256|RuleBase:RU361193};
    EC=3.2.1.- {ECO:0000256|RuleBase:RU361193};'
  gene_info: Name=Edem2 {ECO:0000313|EMBL:AAF53255.2, ECO:0000313|FlyBase:FBgn0032480};
    Synonyms=dEDEM2 {ECO:0000313|EMBL:AAF53255.2}, Dmel\CG5682 {ECO:0000313|EMBL:AAF53255.2},
    EDEM2 {ECO:0000313|EMBL:AAF53255.2}, edem2 {ECO:0000313|EMBL:AAF53255.2}, Edem2-RA
    {ECO:0000313|EMBL:ACL68693.1}; ORFNames=CG5682 {ECO:0000313|EMBL:AAF53255.2, ECO:0000313|FlyBase:FBgn0032480},
    Dmel_CG5682 {ECO:0000313|EMBL:AAF53255.2};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Belongs to the glycosyl hydrolase 47 family.
  protein_domains: 6hp_glycosidase-like_sf. (IPR012341); EDEM1/2/3. (IPR044674); EDEM3_PA.
    (IPR037322); Glyco_hydro_47. (IPR001382); PA_dom_sf. (IPR046450)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Edem2-deep-research-falcon_artifacts/artifact-00.md
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
- **UniProt Accession:** Q9VK27
- **Protein Description:** RecName: Full=alpha-1,2-Mannosidase {ECO:0000256|RuleBase:RU361193}; EC=3.2.1.- {ECO:0000256|RuleBase:RU361193};
- **Gene Information:** Name=Edem2 {ECO:0000313|EMBL:AAF53255.2, ECO:0000313|FlyBase:FBgn0032480}; Synonyms=dEDEM2 {ECO:0000313|EMBL:AAF53255.2}, Dmel\CG5682 {ECO:0000313|EMBL:AAF53255.2}, EDEM2 {ECO:0000313|EMBL:AAF53255.2}, edem2 {ECO:0000313|EMBL:AAF53255.2}, Edem2-RA {ECO:0000313|EMBL:ACL68693.1}; ORFNames=CG5682 {ECO:0000313|EMBL:AAF53255.2, ECO:0000313|FlyBase:FBgn0032480}, Dmel_CG5682 {ECO:0000313|EMBL:AAF53255.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the glycosyl hydrolase 47 family.
- **Key Domains:** 6hp_glycosidase-like_sf. (IPR012341); EDEM1/2/3. (IPR044674); EDEM3_PA. (IPR037322); Glyco_hydro_47. (IPR001382); PA_dom_sf. (IPR046450)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Edem2" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Edem2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Edem2** (gene ID: Edem2, UniProt: Q9VK27) in DROME.

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
- **UniProt Accession:** Q9VK27
- **Protein Description:** RecName: Full=alpha-1,2-Mannosidase {ECO:0000256|RuleBase:RU361193}; EC=3.2.1.- {ECO:0000256|RuleBase:RU361193};
- **Gene Information:** Name=Edem2 {ECO:0000313|EMBL:AAF53255.2, ECO:0000313|FlyBase:FBgn0032480}; Synonyms=dEDEM2 {ECO:0000313|EMBL:AAF53255.2}, Dmel\CG5682 {ECO:0000313|EMBL:AAF53255.2}, EDEM2 {ECO:0000313|EMBL:AAF53255.2}, edem2 {ECO:0000313|EMBL:AAF53255.2}, Edem2-RA {ECO:0000313|EMBL:ACL68693.1}; ORFNames=CG5682 {ECO:0000313|EMBL:AAF53255.2, ECO:0000313|FlyBase:FBgn0032480}, Dmel_CG5682 {ECO:0000313|EMBL:AAF53255.2};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Belongs to the glycosyl hydrolase 47 family.
- **Key Domains:** 6hp_glycosidase-like_sf. (IPR012341); EDEM1/2/3. (IPR044674); EDEM3_PA. (IPR037322); Glyco_hydro_47. (IPR001382); PA_dom_sf. (IPR046450)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Edem2" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Edem2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Edem2** (gene ID: Edem2, UniProt: Q9VK27) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Research Report: Functional Annotation of **Edem2** (Drosophila melanogaster)

### 0) Target verification (critical disambiguation)
The literature surveyed consistently identifies **Drosophila melanogaster Edem2** as **CG5682** (also called **dEDEM2**), an ER protein quality-control factor homologous to mammalian EDEM proteins and yeast Htm1p, aligning with the UniProt-provided accession **Q9VK27** (alpha-1,2-mannosidase-like; GH47 family). (kang2009suppressionofretinal pages 3-4)

### 1) Key concepts and definitions (current understanding)

#### 1.1 ER-associated degradation (ERAD) and glycoprotein ERAD (gpERAD)
**ER-associated degradation (ERAD)** is a conserved pathway that recognizes misfolded proteins in the endoplasmic reticulum (ER), retrotranslocates them to the cytosol, and targets them for proteasomal degradation. In the case of **glycoprotein ERAD (gpERAD)**, progressive trimming of **high-mannose N-glycans** helps “time” folding attempts and creates glycan signals that promote commitment of terminally misfolded clients to ERAD. In mammalian systems, recent mechanistic syntheses place **EDEM2** as the factor catalyzing the **first mannose-trimming step** that initiates gpERAD, with later steps involving other EDEM-family members. (ninagawa2024uggt1mediatedreglucosylationof pages 20-22)

#### 1.2 EDEM proteins and “α-mannosidase-like” activity
EDEM proteins (ER degradation-enhancing α-mannosidase-like proteins) are class I α-mannosidase-like factors (GH47-related) implicated in accelerating disposal of misfolded glycoproteins. Biochemically, mammalian EDEM1/EDEM2 show **bona fide mannosidase activity in vitro**, but with **substrate folding-state dependence**: activity is modest on free glycans/native glycoproteins and substantially higher on **denatured/unfolded glycoproteins**, consistent with selective action on misfolded ER clients. (shenkman2018mannosidaseactivityof pages 1-2, shenkman2018mannosidaseactivityof pages 4-5)

### 2) Gene product function: what Edem2 does in Drosophila

#### 2.1 Primary cellular role: ER proteostasis factor promoting clearance of misfolded ER clients
Multiple Drosophila studies show Edem2 functions as a **misfolded-protein clearance factor in the ER** that reduces levels of aberrant proteins and mitigates downstream ER stress and tissue degeneration.

* In a Drosophila retinal degeneration model driven by misfolded rhodopsin **Rh-1G69D**, Edem2 overexpression selectively reduced mutant Rh-1G69D levels (but not wild-type Rh-1), physically associated with Rh-1G69D, suppressed an ER-stress reporter (**xbp1-EGFP**), and delayed adult retinal degeneration. (kang2009suppressionofretinal pages 4-5, kang2009suppressionofretinal pages 3-4)
* In another in vivo ER proteinopathy model, neuronal Edem2 overexpression reduced **Aβ42** levels and suppressed neurodegenerative/locomotor phenotypes, indicating Edem2 can protect against chronic ER proteotoxicity in aging tissues. (sekiya2017edemfunctionin pages 5-7)

Collectively, these data support Edem2 as an ER quality-control/ERAD-associated factor whose primary function is to **promote disposal of misfolded ER clients**, thereby improving proteostasis and organismal fitness under chronic proteotoxic burden. (kang2009suppressionofretinal pages 4-5, sekiya2017edemfunctionin pages 5-7)

#### 2.2 Enzymatic activity and substrate specificity (direct Drosophila evidence + mechanistic inference)
**Direct Drosophila functional assays** show that Edem2 influences the abundance/clearance of canonical ERAD substrates:

* Edem2 (with Edem1) downregulated a classic luminal ERAD substrate, **α1-antitrypsin NHK**, in Drosophila assays. (kang2009suppressionofretinal pages 3-4)
* In Sekiya et al. (2017), overexpression of wild-type dEDEM2 reduced steady-state NHK protein levels, whereas a catalytically inactive mutant (E144Q) increased NHK levels, implying that **mannosidase-catalytic activity contributes to clearance of at least some glycoprotein ERAD substrates**. (sekiya2017edemfunctionin pages 5-7)

**What is the reaction and substrate?** Based on family biochemistry and mammalian mechanistic work, EDEM2 is an **α1,2-mannose trimming enzyme** acting on **high-mannose N-glycans** of misfolded glycoproteins to promote gpERAD commitment; however, the Drosophila studies above primarily demonstrate *functional outcomes* (client reduction, stress suppression, phenotypes) rather than providing residue-level structural glycan endpoints (e.g., Man9→Man8 at a defined branch) in flies. (ninagawa2024uggt1mediatedreglucosylationof pages 20-22, sekiya2017edemfunctionin pages 5-7)

**Folded-state selectivity (inference from authoritative biochemistry):** In vitro mammalian experiments demonstrate EDEM2’s mannosidase activity is much higher on **unfolded/denatured glycoproteins**, trimming N-glycans to smaller high-mannose species (reported endpoints include M8→M5 species), consistent with selective targeting of misfolded clients rather than mature folded proteins. (shenkman2018mannosidaseactivityof pages 4-5, shenkman2018mannosidaseactivityof pages 1-2)

#### 2.3 Mannosidase-independent (“chaperone-like”) role in some contexts
A notable finding in Drosophila is that Edem2 can protect against some forms of ER proteinopathy even when mannosidase activity is disrupted:

* In Sekiya et al. (2017), catalytically inactive dEDEM mutants (including dEDEM2 E123Q/E144Q) retained protective effects in aging/ER proteinopathy paradigms, and dEDEMs were reported to bind Aβ42 by co-immunoprecipitation, supporting a **substrate-binding/chaperone-like function** for certain nonglycosylated or atypical ER proteotoxic species. (sekiya2017edemfunctionin pages 5-7, sekiya2017edemfunctionin pages 9-10)

This indicates Edem2’s functional repertoire in vivo may include (i) **mannose trimming–dependent gpERAD promotion** for canonical glycoprotein ERAD clients (e.g., NHK), and (ii) **mannosidase-independent client engagement** that can still mitigate ER proteotoxicity in particular models. (sekiya2017edemfunctionin pages 5-7)

### 3) Subcellular localization (where Edem2 acts)
Across Drosophila functional studies, Edem2 activity is consistently linked to ER processes: it acts on ER luminal substrates (NHK) and on misfolded rhodopsin that induces ER stress, and its manipulations modulate ER stress readouts. This functional positioning supports Edem2 as an **ER-resident/ER lumen-facing** quality control factor acting upstream of ERAD commitment and disposal. (kang2009suppressionofretinal pages 4-5, sekiya2017edemfunctionin pages 5-7)

### 4) Pathways and biological processes involving Edem2

#### 4.1 Photoreceptor proteostasis and retinal degeneration (ADRP-like rhodopsin proteinopathy)
In a Drosophila autosomal-dominant-retinitis-pigmentosa (ADRP) model using misfolded **Rh-1G69D**, Edem2 acts as a protective ER quality-control factor: it reduces mutant rhodopsin burden, suppresses ER stress reporter activation, and delays structural degeneration of the retina. (kang2009suppressionofretinal pages 4-5)

#### 4.2 Aging and chronic ER proteinopathy
In aging flies, ERAD capacity can decline, and increasing dEDEM activity is protective in the context of chronic ER proteinopathy. Tissue-specific overexpression shows distinct outcomes depending on where proteostasis is boosted (neurons, muscle, midgut). (sekiya2017edemfunctionin pages 9-10)

#### 4.3 Genetic interaction evidence for substrate-selective ERAD roles in photoreceptors
Hiramatsu et al. (2019) used Edem2 (Edem2DG03809) with Edem1 alleles in photoreceptor genetics to impair ERAD and test whether degradation of EMC-dependent multipass membrane proteins was ERAD-mediated. They observed that loss of Edem1/Edem2 could increase ER accumulation of certain proteins in specific genetic backgrounds (e.g., with Syx5), but did not rescue EMC3-dependent losses of Rh1/TRP, supporting the conclusion that some client degradation is **ERAD-independent** while other substrates remain **Edem-dependent**. (hiramatsu2019ermembraneprotein pages 5-9)

### 5) Recent developments (2023–2024 prioritized)
Direct 2023–2024 primary literature specifically interrogating **Drosophila** Edem2 (CG5682/Q9VK27) appears limited in the retrieved corpus. Nevertheless, high-authority 2024 work refines the **conserved** mechanistic model for EDEM2-family function:

* A 2024 eLife study on ER glycoprotein fate decisions highlights a “tug-of-war” between folding (UGGT1-mediated reglucosylation) and degradation (EDEM-driven demannosylation), and cites work positioning **EDEM2 as catalyzing the first mannose-trimming step initiating gpERAD**, including a role for an EDEM2–TXNDC11 complex in mammals. While this is not Drosophila-specific, it represents the most up-to-date authoritative mechanistic framing relevant for interpreting Drosophila Edem2’s conserved biochemical role. (ninagawa2024uggt1mediatedreglucosylationof pages 20-22)

### 6) Current applications and real-world implementations
Edem2 is currently used primarily as a **functional proteostasis/ERAD lever** in model systems:

1. **Disease-like proteotoxicity models in vivo**: 
   * Rhodopsin misfolding/retinal degeneration (Rh-1G69D) to study ERAD modulation and photoreceptor survival. (kang2009suppressionofretinal pages 4-5)
   * ER proteinopathy in neurons (Aβ42) to test genetic enhancement of ER quality control as a protective strategy. (sekiya2017edemfunctionin pages 5-7)

2. **ER stress / ERAD readouts and reporters**:
   * **xbp1-EGFP** reporter to quantify ER stress (UPR activation proxy) in eye discs under misfolded Rh1 burden and its suppression by Edem2. (kang2009suppressionofretinal pages 4-5)
   * Canonical ERAD substrates (e.g., NHK) as molecular readouts of ERAD enhancement or impairment upon Edem2 manipulation. (sekiya2017edemfunctionin pages 5-7)

These applications are relevant to broader real-world problems in protein misfolding diseases and age-associated proteostasis decline, where ERAD modulation is a proposed intervention axis; Drosophila Edem2 provides an experimentally tractable genetic handle on this biology. (sekiya2017edemfunctionin pages 9-10, kang2009suppressionofretinal pages 4-5)

### 7) Expert interpretation and synthesis (what authoritative sources imply)

1. **Edem2 is best interpreted as a substrate-selective ER quality control factor rather than a general UPR activator.** In vivo, Edem2 manipulations can strongly suppress ER stress readouts driven by misfolded Rh1, consistent with reducing misfolded client burden upstream rather than merely altering stress signaling. (kang2009suppressionofretinal pages 4-5)

2. **Edem2 likely contributes to gpERAD both through enzymatic demannosylation and through client engagement.** Drosophila evidence indicates mannosidase catalytic residues are important for clearance of at least some glycoprotein ERAD clients (NHK), while other protective effects (notably Aβ42-associated) can persist even with catalytic mutants, implying additional non-enzymatic roles. (sekiya2017edemfunctionin pages 5-7, sekiya2017edemfunctionin pages 9-10)

3. **Conserved mechanism suggests Edem2 may act early in the ERAD commitment process.** Mammalian mechanistic framing (2024 synthesis) places EDEM2 at the first mannose-trimming step of gpERAD; while branch/residue-level specificity has not been demonstrated directly in the cited Drosophila studies here, the strong homology and conserved ERAD phenotypes make this the most parsimonious mechanistic hypothesis for the Drosophila protein. (ninagawa2024uggt1mediatedreglucosylationof pages 20-22, kang2009suppressionofretinal pages 3-4)

### 8) Key quantitative statistics (from primary studies)

* **ER stress suppression**: Edem2 overexpression suppresses Rh-1G69D-driven **xbp1-EGFP** activation (**n=3, P=0.0052**). (kang2009suppressionofretinal pages 4-5)
* **Retinal degeneration delay (pseudopupil assay)**: at 28 days, **64.43 ± 11.11%** of ninaE^G69D/+ flies retained intact pseudopupils with Edem2 overexpression vs ~**10.47 ± 8.46%** for lacZ control (**n=4, P=0.0002**). (kang2009suppressionofretinal pages 4-5)
* **Rhabdomere preservation**: ommatidia retaining all seven rhabdomeres were ~**68.9 ± 16.1%** with Edem2 (**n=3**). (kang2009suppressionofretinal pages 4-5)
* **Lifespan medians depend on tissue**: neuronal overexpression median lifespan **47→50 days**; midgut overexpression median lifespan **67→76 days**; muscle overexpression **67→64 days** (with locomotor benefits but not lifespan extension in muscle). (sekiya2017edemfunctionin pages 9-10)
* **Photoreceptor genetics (ER accumulation metric)**: TRP ER-accumulation ratio increased from **0.95 ± 0.25** (Syx5 single) to **1.64 ± 0.30** (Syx5, Edem1, Edem2 triple), indicating Edem1/Edem2 loss affects ERAD-dependent handling in that genetic background. (hiramatsu2019ermembraneprotein pages 5-9)

### 9) Consolidated evidence table
| Evidence type | Key finding | Experimental system | Quantitative/statistical details | Interpretation for Edem2 function | Source (short citation) | URL |
|---|---|---|---|---|---|---|
| Genetic/biochemical/phenotype | **Identity verified:** Drosophila **Edem2 = CG5682**; homologous to mammalian EDEM2/EDEM3 and yeast Htm1p; belongs to GH47/class I α-mannosidase-like ERAD factors | Drosophila sequence comparison and ERAD functional assays in eye disc/S2 cell models | Homology-based assignment; no direct kinetic value reported in this excerpt (kang2009suppressionofretinal pages 3-4) | Supports that Q9VK27 is the correct **D. melanogaster Edem2** and that its expected core role is glycoprotein quality control in ERAD | Kang 2009 PNAS | https://doi.org/10.1073/pnas.0905566106 |
| Biochemical | Edem2 overexpression selectively reduces **misfolded Rh-1G69D**, but not wild-type Rh-1; also downregulates luminal ERAD substrate **α1-antitrypsin NHK** | Drosophila larval eye imaginal discs; S2 cells; transgenic overexpression | Rh-1G69D reduction quantified with **n=6**; NHK reduction qualitative in excerpt (kang2009suppressionofretinal pages 4-5, kang2009suppressionofretinal pages 3-4) | Edem2 acts on **misfolded ER clients**, including both membrane and luminal substrates, consistent with a substrate-selective ERAD factor | Kang 2009 PNAS | https://doi.org/10.1073/pnas.0905566106 |
| Biochemical | Edem2 physically **co-immunoprecipitates with Rh-1G69D but not Rh-1WT** | Drosophila S2 cell co-IP | Interaction is substrate-selective; quantitative binding constants not reported (kang2009suppressionofretinal pages 4-5, kang2009suppressionofretinal pages 3-4) | Strong evidence that Edem2 preferentially recognizes aberrant conformers rather than normal Rh1 | Kang 2009 PNAS | https://doi.org/10.1073/pnas.0905566106 |
| Phenotype/UPR readout | Edem2 suppresses **ER stress** caused by Rh-1G69D, measured by **xbp1-EGFP** splicing reporter | Drosophila eye imaginal discs | **xbp1-EGFP suppression n=3, P=0.0052**; no suppression reported for Rh-1WT-driven signal (kang2009suppressionofretinal pages 4-5) | Edem2 lowers burden of misfolded ER proteins, likely by promoting their disposal before they trigger strong UPR signaling | Kang 2009 PNAS | https://doi.org/10.1073/pnas.0905566106 |
| Phenotype | Edem2 delays **retinal degeneration** in the ADRP model **ninaE^G69D/+** | Adult Drosophila retina/pseudopupil and rhabdomere analyses | At 28 d, **64.43 ± 11.11%** retained intact pseudopupils with Edem2 vs ~**10.47 ± 8.46%** lacZ control; **n=4, P=0.0002**. Ommatidia retaining all 7 rhabdomeres: **68.9 ± 16.1%**, **n=3** (kang2009suppressionofretinal pages 4-5) | In vivo evidence that increasing Edem2-mediated ER quality control is protective against chronic rhodopsin proteotoxicity | Kang 2009 PNAS | https://doi.org/10.1073/pnas.0905566106 |
| Genetic/biochemical | Wild-type dEDEM2 reduces steady-state **NHK** levels, whereas catalytic mutant **E144Q** increases NHK levels | Drosophila neuronal overexpression assays with ERAD substrate NHK | Significant effects reported; exact fold-change not included in excerpt (sekiya2017edemfunctionin pages 5-7) | Indicates **mannosidase activity contributes to glycoprotein ERAD substrate clearance** by dEDEM2 | Sekiya 2017 Dev Cell | https://doi.org/10.1016/j.devcel.2017.05.019 |
| Biochemical/phenotype | dEDEM2 lowers **Aβ42** levels and suppresses Aβ42-induced locomotor and neurodegenerative phenotypes; catalytically inactive mutants retain protection | Drosophila neuronal Aβ42 ER proteinopathy model; co-IP with Aβ42 | Protective effects significant; exact behavioral values not in excerpt. Catalytic mutants **E123Q/E144Q** still reduced Aβ42 and protected (sekiya2017edemfunctionin pages 5-7) | Suggests dEDEM2 has both **mannosidase-dependent ERAD activity** (for glycoproteins like NHK) and **mannosidase-independent/chaperone-like activity** for some nonglycosylated toxic ER proteins | Sekiya 2017 Dev Cell | https://doi.org/10.1016/j.devcel.2017.05.019 |
| Phenotype/aging | dEDEM2 overexpression improves age-associated physiology; neuronal overexpression modestly extends lifespan, gut overexpression extends lifespan more strongly | Adult Drosophila overexpression in neurons, muscle, and midgut | Neuronal median lifespan **47 → 50 d**; muscle **67 → 64 d**; midgut **67 → 76 d**. Locomotor benefits significant; lifespan by log-rank, sample sizes ~**n=190–306** depending on assay (sekiya2017edemfunctionin pages 9-10, sekiya2017edemfunctionin pages 10-12) | Boosting Edem2-linked ERAD capacity can improve organismal proteostasis during aging, with tissue-specific benefit | Sekiya 2017 Dev Cell | https://doi.org/10.1016/j.devcel.2017.05.019 |
| Mechanistic/UPR | Chronic dEDEM overexpression protects without broad canonical UPR activation; aging is associated with slower ERAD substrate turnover | Adult Drosophila brains | Aging slows NHK degradation and causes CD3d-YFP accumulation; overexpression had minimal PERK/Xbp1-RB induction in excerpt (sekiya2017edemfunctionin pages 9-10, sekiya2017edemfunctionin pages 7-9) | Supports Edem2 as an **ERAD enhancer**, not simply a general UPR activator | Sekiya 2017 Dev Cell | https://doi.org/10.1016/j.devcel.2017.05.019 |
| Genetic | Loss of Edem1/Edem2 contributes to stabilization of some ERAD substrates in photoreceptors, but does **not** rescue EMC-dependent Rh1/TRP loss | Drosophila photoreceptors; Edem1/Edem2 alleles combined with Syx5 or EMC3 mutants | TRP accumulation ratio: **Syx5 single 0.95 ± 0.25** vs **Syx5, Edem1, Edem2 triple 1.64 ± 0.30**. EMC3Δ6 TRP ratio: **0.42 ± 0.05** vs **0.46 ± 0.08** in triple mutant (hiramatsu2019ermembraneprotein pages 5-9) | Edem2 participates in photoreceptor **ERAD**, but some client degradation in EMC-deficient cells is **ERAD-independent**, refining substrate scope | Hiramatsu 2019 Mol Biol Cell | https://doi.org/10.1091/mbc.e19-08-0434 |
| Genetic/substrate specificity | In EMC3-deficient photoreceptors, Edem1/Edem2 loss allows **NaKβ** accumulation but not rescue of Rh1, NaKα, or TRP | Drosophila photoreceptor genetics | Qualitative substrate selectivity; ratio values above for TRP (hiramatsu2019ermembraneprotein pages 5-9) | Implies Edem2-dependent ERAD is **substrate-selective**, not universally responsible for degradation of all unstable photoreceptor proteins | Hiramatsu 2019 Mol Biol Cell | https://doi.org/10.1091/mbc.e19-08-0434 |
| Mechanistic (mammalian context) | Mammalian EDEM2 has **bona fide mannosidase activity**, weak on free glycans/native glycoproteins but stronger on **denatured/unfolded glycoproteins**; trimming can proceed from **M8 to M5** | In vitro mammalian biochemistry with recombinant proteins and glycan analysis | ERManI trimmed free glycans about **3-fold** more than EDEM1/EDEM2; EDEM2 interacts with **PDI/TXNDC11**, with ~**50% stronger** co-IP with TXNDC11 in excerpt (shenkman2018mannosidaseactivityof pages 4-5, shenkman2018mannosidaseactivityof pages 5-6, shenkman2018mannosidaseactivityof pages 4-4, shenkman2018mannosidaseactivityof pages 1-2) | Provides conserved mechanistic context for Drosophila Edem2: likely a **folding-state-sensitive GH47 α1,2-mannosidase-like ERAD factor** acting preferentially on misfolded glycoproteins | Shenkman 2018 Commun Biol | https://doi.org/10.1038/s42003-018-0174-8 |
| Mechanistic (mammalian context) | Recent synthesis of mammalian work places **EDEM2 at the first mannose-trimming step that initiates gpERAD**, acting with **TXNDC11** before further trimming by other EDEMs | Mammalian ERAD pathway synthesis/review of primary studies | No new kinetic values in excerpt; mechanistic placement cites prior primary studies (ninagawa2024uggt1mediatedreglucosylationof pages 20-22) | Supports inference that Drosophila Edem2 likely functions early in glycoprotein ERAD by generating/advancing the demannosylation signal on terminally misfolded clients | Ninagawa 2024 eLife | https://doi.org/10.1101/2023.10.18.562958 |


*Table: This table compiles the most relevant experimental and mechanistic findings for Drosophila Edem2/CG5682, emphasizing direct Drosophila evidence and clearly separating mammalian EDEM2 context used for functional inference.*

### 10) Primary source list with publication dates and URLs (most relevant)
* Kang MJ, Ryoo HD. **2009-10**. *PNAS*. “Suppression of retinal degeneration in Drosophila by stimulation of ER-associated degradation.” https://doi.org/10.1073/pnas.0905566106 (kang2009suppressionofretinal pages 4-5, kang2009suppressionofretinal pages 3-4)
* Sekiya M, Maruko-Otake A, et al. **2017-06**. *Developmental Cell*. “EDEM function in ERAD protects against chronic ER proteinopathy and age-related physiological decline in Drosophila.” https://doi.org/10.1016/j.devcel.2017.05.019 (sekiya2017edemfunctionin pages 5-7, sekiya2017edemfunctionin pages 9-10)
* Hiramatsu N, Tago T, et al. **2019-11**. *Molecular Biology of the Cell*. “ER membrane protein complex is required for the insertions of late-synthesized transmembrane helices of Rh1 in Drosophila photoreceptors.” https://doi.org/10.1091/mbc.e19-08-0434 (hiramatsu2019ermembraneprotein pages 5-9)
* Shenkman M, Ron E, et al. **2018-10**. *Communications Biology*. “Mannosidase activity of EDEM1 and EDEM2 depends on an unfolded state of their glycoprotein substrates.” https://doi.org/10.1038/s42003-018-0174-8 (shenkman2018mannosidaseactivityof pages 1-2, shenkman2018mannosidaseactivityof pages 4-5)
* Ninagawa S, Matsuo M, et al. **2024-09**. *eLife*. “UGGT1-mediated reglucosylation of N-glycan competes with ER-associated degradation of unstable and misfolded glycoproteins.” https://doi.org/10.1101/2023.10.18.562958 (ninagawa2024uggt1mediatedreglucosylationof pages 20-22)


References

1. (kang2009suppressionofretinal pages 3-4): Min-Ji Kang and Hyung Don Ryoo. Suppression of retinal degeneration in drosophila by stimulation of er-associated degradation. Proceedings of the National Academy of Sciences, 106:17043-17048, Oct 2009. URL: https://doi.org/10.1073/pnas.0905566106, doi:10.1073/pnas.0905566106. This article has 110 citations and is from a highest quality peer-reviewed journal.

2. (ninagawa2024uggt1mediatedreglucosylationof pages 20-22): Satoshi Ninagawa, Masaki Matsuo, Deng Ying, Shuichiro Oshita, Shinya Aso, Kazutoshi Matsushita, Mai Taniguchi, Akane Fueki, Moe Yamashiro, Kaoru Sugasawa, Shunsuke Saito, Koshi Imami, Yasuhiko Kizuka, Tetsushi Sakuma, Takashi Yamamoto, Hirokazu Yagi, Koichi Kato, and Kazutoshi Mori. Uggt1-mediated reglucosylation of n-glycan competes with er-associated degradation of unstable and misfolded glycoproteins. eLife, Sep 2024. URL: https://doi.org/10.1101/2023.10.18.562958, doi:10.1101/2023.10.18.562958. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (shenkman2018mannosidaseactivityof pages 1-2): Marina Shenkman, Efrat Ron, Rivka Yehuda, Ron Benyair, Isam Khalaila, and Gerardo Z. Lederkremer. Mannosidase activity of edem1 and edem2 depends on an unfolded state of their glycoprotein substrates. Communications Biology, Oct 2018. URL: https://doi.org/10.1038/s42003-018-0174-8, doi:10.1038/s42003-018-0174-8. This article has 71 citations and is from a peer-reviewed journal.

4. (shenkman2018mannosidaseactivityof pages 4-5): Marina Shenkman, Efrat Ron, Rivka Yehuda, Ron Benyair, Isam Khalaila, and Gerardo Z. Lederkremer. Mannosidase activity of edem1 and edem2 depends on an unfolded state of their glycoprotein substrates. Communications Biology, Oct 2018. URL: https://doi.org/10.1038/s42003-018-0174-8, doi:10.1038/s42003-018-0174-8. This article has 71 citations and is from a peer-reviewed journal.

5. (kang2009suppressionofretinal pages 4-5): Min-Ji Kang and Hyung Don Ryoo. Suppression of retinal degeneration in drosophila by stimulation of er-associated degradation. Proceedings of the National Academy of Sciences, 106:17043-17048, Oct 2009. URL: https://doi.org/10.1073/pnas.0905566106, doi:10.1073/pnas.0905566106. This article has 110 citations and is from a highest quality peer-reviewed journal.

6. (sekiya2017edemfunctionin pages 5-7): Michiko Sekiya, Akiko Maruko-Otake, Stephen Hearn, Yasufumi Sakakibara, Naoki Fujisaki, Emiko Suzuki, Kanae Ando, and Koichi M. Iijima. Edem function in erad protects against chronic er proteinopathy and age-related physiological decline in drosophila. Developmental cell, 41 6:652-664.e5, Jun 2017. URL: https://doi.org/10.1016/j.devcel.2017.05.019, doi:10.1016/j.devcel.2017.05.019. This article has 38 citations and is from a highest quality peer-reviewed journal.

7. (sekiya2017edemfunctionin pages 9-10): Michiko Sekiya, Akiko Maruko-Otake, Stephen Hearn, Yasufumi Sakakibara, Naoki Fujisaki, Emiko Suzuki, Kanae Ando, and Koichi M. Iijima. Edem function in erad protects against chronic er proteinopathy and age-related physiological decline in drosophila. Developmental cell, 41 6:652-664.e5, Jun 2017. URL: https://doi.org/10.1016/j.devcel.2017.05.019, doi:10.1016/j.devcel.2017.05.019. This article has 38 citations and is from a highest quality peer-reviewed journal.

8. (hiramatsu2019ermembraneprotein pages 5-9): Naoki Hiramatsu, Tatsuya Tago, Takunori Satoh, and Akiko K. Satoh. Er membrane protein complex is required for the insertions of late-synthesized transmembrane helices of rh1 in drosophila photoreceptors. Molecular Biology of the Cell, 30:2890-2900, Nov 2019. URL: https://doi.org/10.1091/mbc.e19-08-0434, doi:10.1091/mbc.e19-08-0434. This article has 17 citations and is from a domain leading peer-reviewed journal.

9. (sekiya2017edemfunctionin pages 10-12): Michiko Sekiya, Akiko Maruko-Otake, Stephen Hearn, Yasufumi Sakakibara, Naoki Fujisaki, Emiko Suzuki, Kanae Ando, and Koichi M. Iijima. Edem function in erad protects against chronic er proteinopathy and age-related physiological decline in drosophila. Developmental cell, 41 6:652-664.e5, Jun 2017. URL: https://doi.org/10.1016/j.devcel.2017.05.019, doi:10.1016/j.devcel.2017.05.019. This article has 38 citations and is from a highest quality peer-reviewed journal.

10. (sekiya2017edemfunctionin pages 7-9): Michiko Sekiya, Akiko Maruko-Otake, Stephen Hearn, Yasufumi Sakakibara, Naoki Fujisaki, Emiko Suzuki, Kanae Ando, and Koichi M. Iijima. Edem function in erad protects against chronic er proteinopathy and age-related physiological decline in drosophila. Developmental cell, 41 6:652-664.e5, Jun 2017. URL: https://doi.org/10.1016/j.devcel.2017.05.019, doi:10.1016/j.devcel.2017.05.019. This article has 38 citations and is from a highest quality peer-reviewed journal.

11. (shenkman2018mannosidaseactivityof pages 5-6): Marina Shenkman, Efrat Ron, Rivka Yehuda, Ron Benyair, Isam Khalaila, and Gerardo Z. Lederkremer. Mannosidase activity of edem1 and edem2 depends on an unfolded state of their glycoprotein substrates. Communications Biology, Oct 2018. URL: https://doi.org/10.1038/s42003-018-0174-8, doi:10.1038/s42003-018-0174-8. This article has 71 citations and is from a peer-reviewed journal.

12. (shenkman2018mannosidaseactivityof pages 4-4): Marina Shenkman, Efrat Ron, Rivka Yehuda, Ron Benyair, Isam Khalaila, and Gerardo Z. Lederkremer. Mannosidase activity of edem1 and edem2 depends on an unfolded state of their glycoprotein substrates. Communications Biology, Oct 2018. URL: https://doi.org/10.1038/s42003-018-0174-8, doi:10.1038/s42003-018-0174-8. This article has 71 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Edem2-deep-research-falcon_artifacts/artifact-00.md)

## Citations

1. kang2009suppressionofretinal pages 3-4
2. sekiya2017edemfunctionin pages 5-7
3. kang2009suppressionofretinal pages 4-5
4. sekiya2017edemfunctionin pages 9-10
5. hiramatsu2019ermembraneprotein pages 5-9
6. shenkman2018mannosidaseactivityof pages 1-2
7. shenkman2018mannosidaseactivityof pages 4-5
8. sekiya2017edemfunctionin pages 10-12
9. sekiya2017edemfunctionin pages 7-9
10. shenkman2018mannosidaseactivityof pages 5-6
11. shenkman2018mannosidaseactivityof pages 4-4
12. https://doi.org/10.1073/pnas.0905566106
13. https://doi.org/10.1016/j.devcel.2017.05.019
14. https://doi.org/10.1091/mbc.e19-08-0434
15. https://doi.org/10.1038/s42003-018-0174-8
16. https://doi.org/10.1101/2023.10.18.562958
17. https://doi.org/10.1073/pnas.0905566106,
18. https://doi.org/10.1101/2023.10.18.562958,
19. https://doi.org/10.1038/s42003-018-0174-8,
20. https://doi.org/10.1016/j.devcel.2017.05.019,
21. https://doi.org/10.1091/mbc.e19-08-0434,