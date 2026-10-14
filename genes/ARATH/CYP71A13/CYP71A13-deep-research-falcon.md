---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-02T06:23:47.628711'
end_time: '2026-10-02T06:43:07.209912'
duration_seconds: 1159.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ARATH
  gene_id: CYP71A13
  gene_symbol: CYP71A13
  uniprot_accession: O49342
  protein_description: 'RecName: Full=Indoleacetaldoxime dehydratase; EC=4.8.1.3 {ECO:0000269|PubMed:17573535};
    AltName: Full=Cytochrome P450 71A13;'
  gene_info: Name=CYP71A13; OrderedLocusNames=At2g30770; ORFNames=T11J7.16;
  organism_full: Arabidopsis thaliana (Mouse-ear cress).
  protein_family: Belongs to the cytochrome P450 family. .
  protein_domains: Cyt_P450. (IPR001128); Cyt_P450_CS. (IPR017972); Cyt_P450_E_grp-I.
    (IPR002401); Cyt_P450_sf. (IPR036396); p450 (PF00067)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 51
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: CYP71A13-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: CYP71A13-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000044 Figure 1 from page 2 illustrates the
    biosynthetic pathway of camalexin, including the conversion of IAOx to indole
    cyanohydrin by C'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O49342
- **Protein Description:** RecName: Full=Indoleacetaldoxime dehydratase; EC=4.8.1.3 {ECO:0000269|PubMed:17573535}; AltName: Full=Cytochrome P450 71A13;
- **Gene Information:** Name=CYP71A13; OrderedLocusNames=At2g30770; ORFNames=T11J7.16;
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the cytochrome P450 family. .
- **Key Domains:** Cyt_P450. (IPR001128); Cyt_P450_CS. (IPR017972); Cyt_P450_E_grp-I. (IPR002401); Cyt_P450_sf. (IPR036396); p450 (PF00067)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CYP71A13" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CYP71A13' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CYP71A13** (gene ID: CYP71A13, UniProt: O49342) in ARATH.

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
- **UniProt Accession:** O49342
- **Protein Description:** RecName: Full=Indoleacetaldoxime dehydratase; EC=4.8.1.3 {ECO:0000269|PubMed:17573535}; AltName: Full=Cytochrome P450 71A13;
- **Gene Information:** Name=CYP71A13; OrderedLocusNames=At2g30770; ORFNames=T11J7.16;
- **Organism (full):** Arabidopsis thaliana (Mouse-ear cress).
- **Protein Family:** Belongs to the cytochrome P450 family. .
- **Key Domains:** Cyt_P450. (IPR001128); Cyt_P450_CS. (IPR017972); Cyt_P450_E_grp-I. (IPR002401); Cyt_P450_sf. (IPR036396); p450 (PF00067)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CYP71A13" matches the protein description above**
2. **Verify the organism is correct:** Arabidopsis thaliana (Mouse-ear cress).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CYP71A13' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CYP71A13** (gene ID: CYP71A13, UniProt: O49342) in ARATH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: Arabidopsis CYP71A13

**Identity verified.** The target is *Arabidopsis thaliana* CYP71A13 (locus **At2g30770**, UniProt **[O49342](https://www.uniprot.org/uniprotkb/O49342/entry)**), annotated as cytochrome P450 71A13/indoleacetaldoxime dehydratase (EC 4.8.1.3). The accession, locus and EC assignment are supplied in the question’s UniProt record; independent Arabidopsis literature confirms that CYP71A13 is a CYP71-family P450 acting in camalexin synthesis. The specified Cyt_P450/PF00067 and related domain annotations agree with that experimentally established family assignment. **CYP71A12 and CYP71A27 are separate Arabidopsis genes**, not alternative names for this protein. (bak2011cytochromesp450 pages 11-12, pastorczyk2020theroleof pages 1-2, koprivova2019rootspecificcamalexinbiosynthesis pages 3-4)

## Molecular function and substrate specificity

CYP71A13 diverts **indole-3-acetaldoxime (IAOx)**, a tryptophan-derived branch-point metabolite, toward the sulfur-containing antimicrobial phytoalexin **camalexin**. Its established annotated reaction is **IAOx → indole-3-acetonitrile (IAN) + H₂O**. The original biochemical assignment is Nafisi *et al.*, “Arabidopsis Cytochrome P450 Monooxygenase 71A13 Catalyzes the Conversion of Indole-3-Acetaldoxime in Camalexin Synthesis,” *The Plant Cell* (**June 2007**), [doi:10.1105/tpc.107.051383](https://doi.org/10.1105/tpc.107.051383); an authoritative P450 review independently describes the IAOx-to-IAN activity. The original article was identifiable but its full text was not available in this retrieval, so the detailed original assay conditions cannot be independently reproduced here. (bak2011cytochromesp450 pages 11-12)

**The dehydration annotation does not capture the entire current pathway model.** Subsequent work implicates CYP71A13, particularly strongly relative to CYP71A12, in production of an activated IAN-derived intermediate described as **indole-3-cyanohydrin**. Glutathione conjugation of that intermediate supplies **GS-IAN**, which is processed to **cysteine-IAN [Cys(IAN)]**; the downstream P450 **PAD3/CYP71B15**, rather than CYP71A13, then converts Cys(IAN) toward camalexin. IAN can therefore be named as a demonstrated product/intermediate without asserting that a pool of freely released IAN must precede every instance of cyanohydrin formation. This distinction is illustrated in Mucha *et al.*’s pathway figure. (mucha2019theformationof pages 1-2, mucha2019theformationof pages 2-3, mucha2019theformationof media e594cac2, bottcher2009themultifunctionalenzyme pages 1-2)

The **experimentally supported physiological substrate is IAOx**; the available evidence does not justify assigning CYP71A13 a similarly well-established substrate panel or calling it the final camalexin-forming enzyme. In yeast microsomes, coexpression of CYP79B2, CYP71A13 and the reductase ATR1 shifted tryptophan-derived products toward IAN. The apparent *K*ₘ for **CYP79B2 acting on tryptophan** changed from **17.5 ± 1.9 to 6.9 ± 0.9 µM** with CYP71A13 present—evidence consistent with functional coupling, **not a measurement of CYP71A13’s own *K*ₘ for IAOx**. Mucha *et al.*, *The Plant Cell* (**2019**), [doi:10.1105/tpc.19.00403](https://doi.org/10.1105/tpc.19.00403). (mucha2019theformationof pages 5-6, mucha2019theformationof pages 7-8)

The following evidence map separates reactions performed by CYP71A13 from adjacent pathway steps and qualified inferences. (bak2011cytochromesp450 pages 11-12, mucha2019theformationof pages 1-2, mucha2019theformationof pages 2-3)

| Reaction / biological step | Enzyme(s) | Evidence strength | Important caveat / interpretation |
|---|---|---|---|
| **Upstream precursor formation:** L-tryptophan → indole-3-acetaldoxime (IAOx) | CYP79B2, CYP79B3 | **Strong biochemical and genetic support.** IAOx is the shared branch-point precursor for camalexin, indole glucosinolates, indole-carbonyl nitriles and related metabolites. *The Formation of a Camalexin Biosynthetic Metabolon* (2019), DOI: [10.1105/tpc.19.00403](https://doi.org/10.1105/tpc.19.00403) (mucha2019theformationof pages 1-2, mucha2019theformationof pages 2-3) | This is upstream of CYP71A13 and is not specific to camalexin. In healthy tissue, much IAOx instead enters indole-glucosinolate biosynthesis through CYP83B1. |
| **Principal annotated reaction:** IAOx → indole-3-acetonitrile (IAN); subsequent oxidative “activation” toward indole-3-cyanohydrin contributes to camalexin synthesis | **CYP71A13**; partially redundant CYP71A12 | **Strong support for IAOx-to-IAN conversion; substantial pathway evidence for further activation.** Recombinant/heterologous and mutant evidence established the dehydration reaction, while later work places CYP71A13—especially strongly—also in indole-3-cyanohydrin formation. *Cytochromes P450* (2011), DOI: [10.1199/tab.0144](https://doi.org/10.1199/tab.0144); *Camalexin Biosynthetic Metabolon* (2019), DOI above (bak2011cytochromesp450 pages 11-12, mucha2019theformationof pages 1-2, mucha2019theformationof pages 2-3, mucha2019theformationof media e594cac2) | IAN is a detected and important pathway intermediate, but current models should not imply that freely diffusible IAN is the sole obligatory immediate intermediate in every catalytic context. Reactive intermediates may be metabolically channeled within an ER-associated complex. |
| **Sulfur incorporation:** indole-3-cyanohydrin/reactive IAN-derived intermediate + glutathione → GS-IAN | One or more glutathione transferases; GSTU4 physically associates with CYP71A13 and other pathway enzymes | **Strong evidence for glutathione conjugation; weak evidence for a uniquely required GST isoform.** A yeast survey found many Arabidopsis GSTs capable of supporting GS-IAN formation. *Camalexin Biosynthetic Metabolon* (2019), DOI above (mucha2019theformationof pages 6-7, mucha2019theformationof pages 7-8) | GSTU4 interaction is **not** proof that GSTU4 is the required biosynthetic GST. In fact, `gstu4` knockout plants accumulated more camalexin, whereas GSTU4 overexpression reduced it, indicating a competing or regulatory role rather than an indispensable catalytic role (mucha2019theformationof pages 8-9). |
| **Conjugate processing and final synthesis:** GS-IAN → Cys(IAN) → dihydrocamalexic acid/camalexin | GGP1 participates in shortening GS-IAN to Cys(IAN); PAD3/CYP71B15 performs the terminal multifunctional P450 reactions | **Strong biochemical and genetic support.** `pad3` mutants are camalexin deficient and accumulate precursors; heterologously expressed CYP71B15 converts Cys(IAN) toward camalexin. *The Multifunctional Enzyme CYP71B15…* (2009), DOI: [10.1105/tpc.109.066670](https://doi.org/10.1105/tpc.109.066670) (bottcher2009themultifunctionalenzyme pages 1-2, bak2011cytochromesp450 pages 12-13, mucha2019theformationof pages 1-2) | CYP71A13 does not itself catalyze the final conversion to camalexin; that downstream role belongs to PAD3/CYP71B15. |
| **Subcellular site and electron supply:** ER-associated camalexin metabolon; CYP71A13 receives reducing equivalents through a P450 reductase | CYP71A13, ATR1, CYP79B2, CYP71A12, CYP71B15 and associated soluble enzymes | **Direct localization and interaction evidence.** Fluorescent CYP71A13 fusions localized to the ER in *Nicotiana benthamiana*; targeted co-IP repeatedly detected CYP71A13–ATR1 and CYP71A13–CYP71B15 associations, while Arabidopsis microsomal co-IP supported the native metabolon. *Camalexin Biosynthetic Metabolon* (2019), DOI above (mucha2019theformationof pages 5-5, mucha2019theformationof pages 5-6, mucha2019theformationof pages 6-7, mucha2019theformationof pages 3-4) | Direct CYP71A13 localization microscopy was performed mainly in a heterologous leaf system; native Arabidopsis support comes principally from microsomal interaction/proteomic evidence. The reported apparent *K*ₘ shift—from 17.5 ± 1.9 to 6.9 ± 0.9—belongs to **CYP79B2 for tryptophan**, measured without versus with CYP71A13; it is not a CYP71A13 *K*ₘ (mucha2019theformationof pages 5-6). |
| **Paralog specialization and tissue context** | CYP71A13 versus CYP71A12; distinct CYP71A27 in roots | **Strong mutant/metabolomic support for overlapping but biased functions.** CYP71A13 is the principal contributor to induced leaf camalexin synthesis; CYP71A12 contributes more prominently to pathogen-induced ICA/ICN-related metabolism. Both can contribute to camalexin, particularly in roots. *The Role of CYP71A12…* (2020), DOI: [10.1111/nph.16118](https://doi.org/10.1111/nph.16118); *Root-specific Camalexin Biosynthesis…* (2019), DOI: [10.1073/pnas.1818604116](https://doi.org/10.1073/pnas.1818604116) (pastorczyk2020theroleof pages 1-2, pastorczyk2020theroleof pages 6-7, koprivova2019rootspecificcamalexinbiosynthesis pages 3-4) | CYP71A12 and CYP71A13 are close tandem paralogs and can compensate transcriptionally, so single-mutant phenotypes depend on tissue and elicitor. CYP71A27 is a separate, root-biased gene and must not be conflated with the target CYP71A13/At2g30770. |


*Table: Evidence-weighted map of Arabidopsis CYP71A13 function, pathway context, localization and paralog distinctions. Caveats separate directly demonstrated reactions from metabolon models and prevent misattribution of CYP79B2 kinetics to CYP71A13.*

## Cellular site and pathway organization

**CYP71A13 functions at the endoplasmic reticulum (ER), in an ER-associated camalexin-biosynthetic enzyme assembly.** Fluorescent CYP71A13 fusions showed ER localization when expressed in *Nicotiana benthamiana* leaves; microscopy distinguished the ER-localized P450 from cytosolic GST proteins. This is direct localization of the Arabidopsis protein in a **heterologous** plant, not a claim that the same imaging experiment mapped native CYP71A13 in every Arabidopsis tissue. In Arabidopsis leaves, microsomal co-immunoprecipitation after challenge independently supports its association with an ER-membrane pathway complex. The predicted positioning of its catalytic domain on the **cytosolic face** follows the usual topology of eukaryotic ER P450s and is less directly demonstrated for this particular protein than ER association itself. (mucha2019theformationof pages 1-2, mucha2019theformationof pages 6-7, mucha2019theformationof pages 3-4, mucha2019theformationof pages 5-5)

Targeted co-immunoprecipitation detected CYP71A13 with **ATR1**, a P450 reductase, and with downstream **CYP71B15/PAD3**; co-immunoprecipitation and fluorescence-lifetime/FRET experiments also support contacts with other pathway proteins. In infected Arabidopsis leaf material, CYP71A13 was enriched **109-fold** in a CYP71B15 pull-down relative to controls (**P = 0.00014**). Together, physical association and the yeast product-shift experiment support **metabolic channeling** of reactive intermediates, although they do not establish an immutable complex or prove that all intermediate molecules remain bound throughout synthesis. (mucha2019theformationof pages 5-6, mucha2019theformationof pages 3-4, mucha2019theformationof pages 8-9)

CYP71A13 is **not an extracellular enzyme**: its characterized biosynthetic site is ER-associated. Antimicrobial camalexin can subsequently act beyond the producing cell; that disposition must not be confused with the localization of the CYP71A13 protein. GSTU4’s physical recruitment to the complex likewise does **not** establish that it is an indispensable GS-IAN-producing enzyme: **41** Arabidopsis GSTs supported product formation in a heterologous screen, while *gstu4* knockouts generally had **more**, and GSTU4-overexpressing plants **less**, induced camalexin. (mucha2019theformationof pages 6-7, mucha2019theformationof pages 7-8, mucha2019theformationof pages 8-9)

## Biological role, paralogs and regulation

CYP71A13 supplies an **inducible biochemical branch of pathogen defense**, rather than functioning as a pathogen receptor or transcription factor. *cyp71a13* mutants make greatly reduced camalexin after *Pseudomonas syringae* or *Alternaria brassicicola* challenge and show increased susceptibility to *A. brassicicola*. A separate leaf study associated *cyp71a13* loss with low *Botrytis cinerea*-induced camalexin and larger lesions. These observations support a contribution to resistance, but the size of the phenotype depends on tissue, challenge and compensation by other tryptophan-derived defenses. Bak *et al.*, *The Arabidopsis Book* (**2011**), [doi:10.1199/tab.0144](https://doi.org/10.1199/tab.0144); Koprivova *et al.*, *PNAS* (**July 2019**), [doi:10.1073/pnas.1818604116](https://doi.org/10.1073/pnas.1818604116). (bak2011cytochromesp450 pages 12-13, koprivova2019rootspecificcamalexinbiosynthesis pages 3-4)

**Paralog specificity matters for annotation.** CYP71A12 and CYP71A13 are closely related tandem genes, reported to have approximately **89% amino-acid similarity**. Both can contribute to camalexin, but in the infection contexts examined CYP71A13 is the more important contributor in **leaves**, whereas CYP71A12 contributes prominently to **root** camalexin and to pathogen-induced **indole-3-carboxylic-acid (ICA)** and indole-carbonyl-nitrile-related metabolism. In infected leaves, disrupting either CYP71A gene increased expression of the other; accordingly, a single-gene mutant is not a clean measure of exclusive substrate specificity. Pastorczyk *et al.*, *New Phytologist* (accepted **August 2019**, published in volume 225, **2020**), [doi:10.1111/nph.16118](https://doi.org/10.1111/nph.16118). The distinct root-associated CYP71A27 must not be assigned CYP71A13’s direct biochemical reaction simply because it influences camalexin phenotypes. (pastorczyk2020theroleof pages 1-2, pastorczyk2020theroleof pages 6-7, koprivova2019rootspecificcamalexinbiosynthesis pages 3-4)

IAOx is supplied upstream by **CYP79B2/CYP79B3**; in healthy tissues, the competing enzyme **CYP83B1** instead directs much of it toward indole glucosinolates. Pathogens and elicitors induce the CYP71A13-associated defense branch. An authoritative **August 2024** review discusses microbial pattern recognition, MAP kinase and WRKY-linked control of camalexin-pathway gene expression, including CYP71A13: Hu, Teng and Li, *Current Opinion in Biotechnology*, [doi:10.1016/j.copbio.2024.103148](https://doi.org/10.1016/j.copbio.2024.103148). Such signaling regulates **production of the enzyme**; it does not make CYP71A13 itself a signaling protein. Regulator-to-gene relationships should be interpreted by their underlying assays rather than treating a review schematic as proof of direct binding to the CYP71A13 promoter. (hu2024unleashingplantsynthetic pages 3-4, mucha2019theformationof pages 2-3, lin2024abaregulatedjaz1proteins pages 1-3, somssich2025gunsinrosettes pages 5-6)

## Recent evidence and practical relevance

A **2024 Arabidopsis immune-priming experiment** found that pretreatment with the synthetic strigolactone analogue **rac-GR24** reduced *B. cinerea* leaf-lesion area from **27.3 ± 2.35 to 20.1 ± 3.55 mm²** (**26%**), while pathogen-induced camalexin rose **36% at 18 hours** and **44% at 24 hours** relative to untreated controls. Priming depended on downstream **PAD3** and ethylene signaling in the tested mutants. Importantly, this experiment assayed **PAD3 and camalexin**, **not a CYP71A13-specific loss-of-function or enzymatic response**: it demonstrates an application of the pathway, not a newly established reaction for CYP71A13. Fujita *et al.*, *Journal of Pesticide Science* (published online **9 August 2024**), [doi:10.1584/jpestics.D24-019](https://doi.org/10.1584/jpestics.d24-019). (fujita2024enhanceddiseaseresistance pages 4-5, fujita2024enhanceddiseaseresistance pages 5-6, fujita2024enhanceddiseaseresistance pages 1-2)

The current real-world **implementation is primarily experimental**: CYP71A13 mutants, tagged P450s and reconstituted yeast microsomes are used to dissect pathogen resistance, substrate flow and potential metabolic engineering. The 2024 review proposes manipulating defense elicitation to improve specialized-metabolite production; the retrieved evidence does **not** demonstrate a deployed CYP71A13-engineered crop or justify promising field-scale disease control from this gene alone. Root experiments additionally show why deployment cannot simply extrapolate from infected leaves: CYP71A12 and the separate CYP71A27 contribute differently across organs and microbial interactions. (mucha2019theformationof pages 5-6, hu2024unleashingplantsynthetic pages 3-4, koprivova2019rootspecificcamalexinbiosynthesis pages 3-4, fujita2024enhanceddiseaseresistance pages 5-6)

**Annotation conclusion.** The highest-confidence assignment for UniProt O49342 is **ER-associated, P450-dependent conversion of IAOx into the IAN/activated-cyanohydrin arm of tryptophan-derived camalexin biosynthesis**. The IAOx→IAN dehydratase reaction is established; the detailed partitioning between released IAN and further CYP71A13-mediated activation is more context-dependent. CYP71A13 is neither the downstream PAD3 enzyme nor the CYP71A12-dominated ICA-pathway enzyme. (bak2011cytochromesp450 pages 11-12, mucha2019theformationof pages 1-2, pastorczyk2020theroleof pages 1-2, mucha2019theformationof pages 2-3, mucha2019theformationof media e594cac2)

References

1. (bak2011cytochromesp450 pages 11-12): Søren Bak, Fred Beisson, Gerard Bishop, Björn Hamberger, René Höfer, Suzanne Paquette, and Danièle Werck-Reichhart. Cytochromes p450. The Arabidopsis Book, 2011:e0144, Jan 2011. URL: https://doi.org/10.1199/tab.0144, doi:10.1199/tab.0144. This article has 540 citations and is from a peer-reviewed journal.

2. (pastorczyk2020theroleof pages 1-2): Marta Pastorczyk, Ayumi Kosaka, Mariola Piślewska‐Bednarek, Gemma López, Henning Frerigmann, Karolina Kułak, Erich Glawischnig, Antonio Molina, Yoshitaka Takano, and Paweł Bednarek. The role of cyp71a12 monooxygenase in pathogen-triggered tryptophan metabolism and arabidopsis immunity. The New phytologist, 225:400-412, Sep 2020. URL: https://doi.org/10.1111/nph.16118, doi:10.1111/nph.16118. This article has 93 citations.

3. (koprivova2019rootspecificcamalexinbiosynthesis pages 3-4): Anna Koprivova, Stefan Schuck, Richard P. Jacoby, Irene Klinkhammer, Bastian Welter, Lisa Leson, Anna Martyn, Julia Nauen, Niklas Grabenhorst, Jan F. Mandelkow, Alga Zuccaro, Jürgen Zeier, and Stanislav Kopriva. Root-specific camalexin biosynthesis controls the plant growth-promoting effects of multiple bacterial strains. Proceedings of the National Academy of Sciences of the United States of America, 116:15735-15744, Jul 2019. URL: https://doi.org/10.1073/pnas.1818604116, doi:10.1073/pnas.1818604116. This article has 263 citations and is from a highest quality peer-reviewed journal.

4. (mucha2019theformationof pages 1-2): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

5. (mucha2019theformationof pages 2-3): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

6. (mucha2019theformationof media e594cac2): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

7. (bottcher2009themultifunctionalenzyme pages 1-2): C. Böttcher, L. Westphal, Constanze Schmotz, Elke Prade, D. Scheel, and E. Glawischnig. The multifunctional enzyme cyp71b15 (phytoalexin deficient3) converts cysteine-indole-3-acetonitrile to camalexin in the indole-3-acetonitrile metabolic network of arabidopsis thaliana[w][oa]. The Plant Cell Online, 21:1830-1845, Jun 2009. URL: https://doi.org/10.1105/tpc.109.066670, doi:10.1105/tpc.109.066670. This article has 279 citations.

8. (mucha2019theformationof pages 5-6): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

9. (mucha2019theformationof pages 7-8): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

10. (mucha2019theformationof pages 6-7): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

11. (mucha2019theformationof pages 8-9): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

12. (bak2011cytochromesp450 pages 12-13): Søren Bak, Fred Beisson, Gerard Bishop, Björn Hamberger, René Höfer, Suzanne Paquette, and Danièle Werck-Reichhart. Cytochromes p450. The Arabidopsis Book, 2011:e0144, Jan 2011. URL: https://doi.org/10.1199/tab.0144, doi:10.1199/tab.0144. This article has 540 citations and is from a peer-reviewed journal.

13. (mucha2019theformationof pages 5-5): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

14. (mucha2019theformationof pages 3-4): Stefanie Mucha, Stephanie Heinzlmeir, Verena Kriechbaumer, Benjamin Strickland, Charlotte Kirchhelle, Manisha Choudhary, Natalie Kowalski, Ruth Eichmann, Ralph Hueckelhoven, Erwin Grill, Bernhard Kuster, and Erich Glawischnig. The formation of a camalexin biosynthetic metabolon. Plant Cell, 31:2697-2710, Sep 2019. URL: https://doi.org/10.1105/tpc.19.00403, doi:10.1105/tpc.19.00403. This article has 105 citations and is from a highest quality peer-reviewed journal.

15. (pastorczyk2020theroleof pages 6-7): Marta Pastorczyk, Ayumi Kosaka, Mariola Piślewska‐Bednarek, Gemma López, Henning Frerigmann, Karolina Kułak, Erich Glawischnig, Antonio Molina, Yoshitaka Takano, and Paweł Bednarek. The role of cyp71a12 monooxygenase in pathogen-triggered tryptophan metabolism and arabidopsis immunity. The New phytologist, 225:400-412, Sep 2020. URL: https://doi.org/10.1111/nph.16118, doi:10.1111/nph.16118. This article has 93 citations.

16. (hu2024unleashingplantsynthetic pages 3-4): Rongbin Hu, Xiaoxuan Teng, and Yanran Li. Unleashing plant synthetic capacity: navigating regulatory mechanisms for enhanced bioproduction and secondary metabolite discovery. Current Opinion in Biotechnology, 88:103148, Aug 2024. URL: https://doi.org/10.1016/j.copbio.2024.103148, doi:10.1016/j.copbio.2024.103148. This article has 10 citations and is from a peer-reviewed journal.

17. (lin2024abaregulatedjaz1proteins pages 1-3): Jie Lin, Ivan Monsalvo, Md Asraful Jahan, Melissa Ly, Dasol Wi, Izabella Martirosyan, Israt Jahan, and Nikola Kovinich. Aba-regulated jaz1 proteins bind nac42 transcription factors to suppress the activation of phytoalexin biosynthesis in plants. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.26.615281, doi:10.1101/2024.09.26.615281. This article has 1 citations.

18. (somssich2025gunsinrosettes pages 5-6): Marc Somssich, Daniel J Kliebenstein, and Tonni Grube Andersen. Guns in rosettes: the arabidopsis chemical weapons arsenal. Plant Physiology, Sep 2025. URL: https://doi.org/10.1093/plphys/kiaf411, doi:10.1093/plphys/kiaf411. This article has 4 citations and is from a highest quality peer-reviewed journal.

19. (fujita2024enhanceddiseaseresistance pages 4-5): Moeka Fujita, Tomoya Tanaka, Miyuki Kusajima, Kengo Inoshima, Futo Narita, Hidemitsu Nakamura, Tadao Asami, Akiko Maruyama-Nakashita, and Hideo Nakashita. Enhanced disease resistance against botrytis cinerea by strigolactone-mediated immune priming in arabidopsis thaliana. Journal of Pesticide Science, 49:186-194, Aug 2024. URL: https://doi.org/10.1584/jpestics.d24-019, doi:10.1584/jpestics.d24-019. This article has 10 citations and is from a peer-reviewed journal.

20. (fujita2024enhanceddiseaseresistance pages 5-6): Moeka Fujita, Tomoya Tanaka, Miyuki Kusajima, Kengo Inoshima, Futo Narita, Hidemitsu Nakamura, Tadao Asami, Akiko Maruyama-Nakashita, and Hideo Nakashita. Enhanced disease resistance against botrytis cinerea by strigolactone-mediated immune priming in arabidopsis thaliana. Journal of Pesticide Science, 49:186-194, Aug 2024. URL: https://doi.org/10.1584/jpestics.d24-019, doi:10.1584/jpestics.d24-019. This article has 10 citations and is from a peer-reviewed journal.

21. (fujita2024enhanceddiseaseresistance pages 1-2): Moeka Fujita, Tomoya Tanaka, Miyuki Kusajima, Kengo Inoshima, Futo Narita, Hidemitsu Nakamura, Tadao Asami, Akiko Maruyama-Nakashita, and Hideo Nakashita. Enhanced disease resistance against botrytis cinerea by strigolactone-mediated immune priming in arabidopsis thaliana. Journal of Pesticide Science, 49:186-194, Aug 2024. URL: https://doi.org/10.1584/jpestics.d24-019, doi:10.1584/jpestics.d24-019. This article has 10 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CYP71A13-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000044 Figure 1 from page 2 illustrates the biosynthetic pathway of camalexin, including the conversion of IAOx to indole cyanohydrin by C](CYP71A13-deep-research-falcon_artifacts/image-1.png)

## Citations

1. mucha2019theformationof pages 8-9
2. mucha2019theformationof pages 5-6
3. pastorczyk2020theroleof pages 1-2
4. koprivova2019rootspecificcamalexinbiosynthesis pages 3-4
5. mucha2019theformationof pages 1-2
6. mucha2019theformationof pages 2-3
7. bottcher2009themultifunctionalenzyme pages 1-2
8. mucha2019theformationof pages 7-8
9. mucha2019theformationof pages 6-7
10. mucha2019theformationof pages 5-5
11. mucha2019theformationof pages 3-4
12. pastorczyk2020theroleof pages 6-7
13. hu2024unleashingplantsynthetic pages 3-4
14. somssich2025gunsinrosettes pages 5-6
15. fujita2024enhanceddiseaseresistance pages 4-5
16. fujita2024enhanceddiseaseresistance pages 5-6
17. fujita2024enhanceddiseaseresistance pages 1-2
18. O49342
19. doi:10.1105/tpc.107.051383
20. Cys(IAN)
21. doi:10.1105/tpc.19.00403
22. 10.1105/tpc.19.00403
23. 10.1199/tab.0144
24. 10.1105/tpc.109.066670
25. 10.1111/nph.16118
26. 10.1073/pnas.1818604116
27. doi:10.1199/tab.0144
28. doi:10.1073/pnas.1818604116
29. doi:10.1111/nph.16118
30. doi:10.1016/j.copbio.2024.103148
31. doi:10.1584/jpestics.D24-019
32. w
33. oa
34. https://www.uniprot.org/uniprotkb/O49342/entry
35. https://doi.org/10.1105/tpc.107.051383
36. https://doi.org/10.1105/tpc.19.00403
37. https://doi.org/10.1199/tab.0144
38. https://doi.org/10.1105/tpc.109.066670
39. https://doi.org/10.1111/nph.16118
40. https://doi.org/10.1073/pnas.1818604116
41. https://doi.org/10.1016/j.copbio.2024.103148
42. https://doi.org/10.1584/jpestics.d24-019
43. https://doi.org/10.1199/tab.0144,
44. https://doi.org/10.1111/nph.16118,
45. https://doi.org/10.1073/pnas.1818604116,
46. https://doi.org/10.1105/tpc.19.00403,
47. https://doi.org/10.1105/tpc.109.066670,
48. https://doi.org/10.1016/j.copbio.2024.103148,
49. https://doi.org/10.1101/2024.09.26.615281,
50. https://doi.org/10.1093/plphys/kiaf411,
51. https://doi.org/10.1584/jpestics.d24-019,