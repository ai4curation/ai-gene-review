---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-12-11T22:51:18.076685'
end_time: '2025-12-11T22:53:59.358696'
duration_seconds: 161.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: HPX
  gene_symbol: HPX
  uniprot_accession: P02790
  protein_description: 'RecName: Full=Hemopexin; AltName: Full=Beta-1B-glycoprotein;
    Flags: Precursor;'
  gene_info: Name=HPX;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the hemopexin family. .
  protein_domains: Heme_transport/Cell_adhesion. (IPR051298); Hemopexin. (IPR016358);
    Hemopexin-like_dom. (IPR000585); Hemopexin-like_dom_sf. (IPR036375); Hemopexin-like_repeat.
    (IPR018487)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 55
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P02790
- **Protein Description:** RecName: Full=Hemopexin; AltName: Full=Beta-1B-glycoprotein; Flags: Precursor;
- **Gene Information:** Name=HPX;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the hemopexin family. .
- **Key Domains:** Heme_transport/Cell_adhesion. (IPR051298); Hemopexin. (IPR016358); Hemopexin-like_dom. (IPR000585); Hemopexin-like_dom_sf. (IPR036375); Hemopexin-like_repeat. (IPR018487)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HPX" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HPX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HPX** (gene ID: HPX, UniProt: P02790) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

<think>
Let me analyze this request carefully. The user is asking for a comprehensive research report on the gene HPX (UniProt P02790) in humans. They've provided extensive search results about hemopexin.

First, I need to verify I'm researching the correct gene/protein:
1. Gene symbol: HPX - VERIFIED in multiple sources
2. UniProt: P02790 - VERIFIED 
3. Organism: Homo sapiens (Human) - VERIFIED
4. Protein family: Hemopexin family - VERIFIED across multiple sources
5. Key domains: Hemopexin-like repeats - VERIFIED

All the search results are about hemopexin (HPX), so I'm definitely on the right track.

Now I need to plan a comprehensive report that covers:
1. Function (primary)
2. Biological processes
3. Localization
4. Molecular mechanisms
5. Signaling/biochemical pathways
6. Evidence for the above

The search results are very comprehensive. Let me organize them into a narrative structure that addresses the key questions:

Main sections I should include:
1. Gene and Protein Overview - description, structure, expression
2. Primary Function - Heme Binding and Scavenging
3. Molecular Mechanism of Heme Binding - structural details and binding characteristics
4. Cellular Localization and Expression Pattern
5. Heme Transport and Clearance Pathway - LRP1/CD91 receptor-mediated endocytosis
6. Regulation of Gene Expression - acute phase response, control mechanisms
7. Biological Processes - protective functions, physiological roles
8. Pathophysiological Functions - roles in disease states
9. Emerging Functions and Context-Dependent Roles

I have excellent sources to cite:
- Structural information from crystallographic studies [14][17][32][35]
- Molecular binding studies [2]
- Functional studies about heme scavenging [1][5]


- Receptor mechanisms and trafficking pathways [7][8][43][50]
- Gene expression regulation including acute phase signaling [1][4][20][28]
- Disease-related applications and pathological roles [5][11][37][40][41]
- Specialized functions in the central nervous system [26][29]
- Iron metabolism and homeostatic regulation [21][24]

I'll structure this as a detailed scientific report with at least 10,000 words, integrating all these research areas into a cohesive narrative.
</think>

# Hemopexin (HPX): A Comprehensive Analysis of Gene Function, Molecular Mechanisms, and Biological Roles

## Executive Summary

Hemopexin (HPX), encoded by the HPX gene located at chromosome 11p15.5-p15.4 in humans, is a plasma glycoprotein that serves as the highest-affinity heme-binding protein known in the human proteome, with extraordinary binding affinity for heme that exceeds all other known proteins[1][14]. This 60-kDa glycoprotein circulates in plasma at concentrations of 0.5–1.5 mg/mL and functions as a critical component of the body's defense system against heme toxicity by scavenging free heme released from hemoproteins during hemolysis, hemorrhage, and other pathological states[1][5][51]. Beyond its primary heme-scavenging role, hemopexin participates in complex receptor-mediated endocytosis, iron homeostasis, inflammatory regulation, and tissue protection across multiple organ systems including the liver, central nervous system, and immune tissues[1][7][8]. The protein undergoes receptor-specific internalization through the low-density lipoprotein receptor-related protein 1 (LRP1/CD91) and potentially through transferrin receptor-mediated pathways, leading to heme catabolism, iron recycling, and the induction of protective antioxidant responses within target cells[7][8][43]. Recent evidence has expanded understanding of hemopexin beyond classical heme detoxification, revealing its involvement in immune regulation, neurogenesis, skeletal muscle signaling, and cardiovascular homeostasis, establishing it as a multifunctional acute-phase protein with both protective and context-dependent harmful effects depending on tissue location and disease state.

## Gene Structure, Organization, and Genomic Localization

The HPX gene, encoding hemopexin, exhibits a well-characterized genomic organization that reflects its evolutionary history and functional domains. The gene spans approximately 12 kilobases and is organized into 9 exons interrupted by 8 introns, with remarkable structural symmetry that suggests duplication of an ancestral gene during evolution[1]. The direct correspondence between exons and the 10 repeating units identified in the hemopexin protein sequence indicates that the gene's organization mirrors the protein's structural organization, a feature that has been conserved throughout evolutionary time[1]. The introns are not positioned randomly within the gene; rather, they fall in the center of regions of amino acid sequence homology in strikingly similar locations in six of the ten protein units and in a symmetric position in each half of the coding sequence[1]. This organizational symmetry suggests that hemopexin consists of two similar structural halves connected by a central hinge region, a feature that has profound implications for the protein's three-dimensional structure and heme-binding mechanism[1].

The HPX gene has been precisely mapped to human chromosome 11 at position 11p15.5-p15.4, the same chromosomal location as the beta-globin gene complex[1]. This chromosomal assignment was accomplished through Southern blot analysis of human/hamster hybrid cells containing different combinations of human chromosomes and confirmed through in situ hybridization studies[1]. The proximity of the HPX gene to the beta-globin locus may reflect coordinated regulation during hemolytic stress, as both gene products are involved in hemoglobin metabolism and response to hemolysis. The genomic organization and chromosomal localization of HPX have remained consistent across published studies, providing confidence in the accuracy of this genetic mapping. The primary structure of human hemopexin has been deduced through sequence analysis of peptides obtained from chemical and enzymatic digests, revealing that the protein consists of approximately 440 amino acid residues and contains about 20% carbohydrate by mass[32][35].

Notably, hemopexin contains unique glycosylation features including one galactosamine oligosaccharide linked O-glycosidically to the amino-terminal threonine residue and five glucosamine oligosaccharides attached at N-glycosylation sites following the consensus sequence Asn-X-Thr/Ser[32][35]. The galactosamine oligosaccharide at the amino terminus is unusual and had not been previously identified in hemopexin before detailed structural analysis, demonstrating the complexity of hemopexin's post-translational modifications[32][35]. These glycosylation sites are distributed throughout the protein: the galactosamine and one glucosamine are located in the amino-terminal region, three glucosamine oligosaccharides are in the middle region, and one glucosamine is in the carboxyl-terminal region[35]. The structural analysis revealed that hemopexin contains eighteen tryptophan residues arranged in four unusual clusters, with each cluster containing three to four tryptophan residues separated by zero to twelve intervening amino acids[32][35]. Twelve of the eighteen tryptophans are conserved in homologous positions, suggesting functional importance of this clustering[1]. Additionally, the histidine residues in hemopexin are clustered in a histidine-rich sequence in the middle region where histidines flank beta-turns presumably located at the protein surface[35].

## Gene Expression Pattern and Regulation

The transcriptional regulation of the HPX gene exhibits tissue-specific patterns with marked preferential expression in hepatocytes, although expression occurs in other tissues under specific conditions. Early studies using specific complementary DNA probes demonstrated that the HPX gene is expressed predominantly in the liver, with expression below detection limits in most other tissues or cell lines examined[1]. Using S1 mapping analysis, the transcription initiation site in hepatic cells was located 28 base pairs upstream from the AUG initiation codon of the hemopexin gene, establishing the precise point at which transcription of the primary hepatic hemopexin message begins[1]. However, subsequent research has revealed that HPX expression extends to multiple extrahepatic tissues including the nervous system, skeletal muscle, retina, and kidney[5][51][54]. In the central nervous system specifically, hemopexin is expressed by both neurons and glial cells and can be synthesized intrathecally, contributing to cerebrospinal fluid hemopexin levels that are approximately tenfold lower than those in plasma[5][51].

The regulation of hemopexin gene expression is controlled by the acute-phase response pathway, whereby the synthesis of HPX is induced during infection and inflammatory states through signaling by pro-inflammatory cytokines. Hemopexin and haptoglobin are both classified as acute-phase proteins, the synthesis of which are induced during infection and after inflammatory states to minimize tissue injury and facilitate tissue repair[1]. The specific cytokines that induce hemopexin synthesis include interleukin-6 (IL-6), interleukin-1 beta (IL-1β), and tumor necrosis factor-alpha (TNF-α), which act on hepatocytes to increase transcription of the HPX gene[20]. A type II interleukin-6 response element has been identified within the hemopexin gene, indicating direct induction through the IL-6 signaling pathway[28]. Notably, hemopexin mRNA levels increase not only during infection and inflammation but also in response to certain forms of systemic stress; hemopexin mRNA levels were notably elevated in rodent models subjected to sham abdominal surgery or partial hepatectomy, indicating responsiveness to surgical stress and tissue injury[5][51].

The acute-phase response regulation of hemopexin contrasts with constitutive expression patterns in extrahepatic tissues. In extrahepatic sites such as nervous system, skeletal muscle, and retina, hemopexin appears to be constitutively expressed at lower levels, suggesting local production to support tissue-specific functions. This tissue-specific expression pattern indicates that hemopexin has both systemic roles (through hepatic production and plasma circulation) and local tissue roles (through local synthesis). Age-related changes in plasma hemopexin levels have been documented, with hemopexin levels increasing from an average of 60 mg/100 mL (range 40–70) in individuals aged 1–12 years to an average of 77 mg/100 mL (range 66–100) in individuals aged 20–40 years, but then declining to 50–80 mg/100 mL in individuals aged 50–70 years[55]. These age-related variations in hemopexin levels may reflect changes in hepatic synthesis capacity and altered susceptibility to hemolytic stress.

## Primary Function: Heme Binding with Extraordinary Affinity

The primary and most extensively characterized function of hemopexin is the binding and scavenging of free heme with affinity exceeding all other known proteins in the human proteome. Hemopexin binds heme with the highest affinity of any known protein, with a dissociation constant (Kd) estimated at less than 10^-13 M[1][22], representing binding affinity that is extraordinary even among high-affinity protein-ligand interactions. This extraordinary binding affinity enables hemopexin to effectively remove free heme from the circulation and tissues, preventing the oxidative damage and inflammatory effects that free heme causes[1]. The main function of hemopexin is scavenging the heme released or lost by the turnover of heme proteins such as hemoglobin and thus protecting the body from the oxidative damage that free heme can cause[1]. The binding stoichiometry of hemopexin with heme exhibits concentration-dependent behavior, exhibiting a 1:1 binding ratio at low heme concentrations and at least a 2:1 ratio (heme:hemopexin) at higher heme concentrations[5][51].

The molecular basis for hemopexin's exceptional heme-binding affinity has been elucidated through crystallographic analysis of the rabbit hemopexin-heme complex, revealing structural features that provide both extraordinary binding strength and controlled heme release[14][17]. The crystal structure reveals that hemopexin has four-bladed β-propeller folding motifs that are similar in the N- and C-terminal domains, joined by a flexibly structured hinge sequence[2]. The heme binding site is formed between these two similar four-bladed β-propeller domains and is bounded by the interdomain linker region[14][17]. The ligand is bound to two histidine residues (identified as H236 and H293) in the linker region in a pocket dominated by aromatic and basic groups[14][17]. Further stabilization of the heme-hemopexin complex is achieved by the association of the two β-propeller domains, which form an extensive polar interface that includes a cushion of ordered water molecules[14][17].

Detailed molecular docking and spot-synthesis studies have identified specific amino acid residues critical for heme binding within hemopexin. Seven linear peptide sequences in hemopexin were identified to bind hemin (designated H1–H7), with histidine residues playing particularly important roles in heme coordination[2]. The amino acid composition analysis of these identified heme-binding sequences demonstrated that histidine residues are relevant for heme binding, with H105, H293, H373, H400, H429, and H462 being distributed across the H1–H7 peptide sequences[2]. H293 was present in the H3 peptide sequence with particularly high hemin binding capacity, showing a signal of approximately 50%, while H373 was present in peptides with the highest signal spots exceeding 90%[2]. Molecular dynamic simulations have revealed that tyrosine residues (Y646 and Y642) coordinate with heme iron, and during heme transfer, two serine residues (S557 and S563) capture heme[2]. These findings indicate that while histidine residues coordinate the heme iron axially, a broader network of aromatic and polar amino acids contributes to both heme binding and the subsequent release process.

The mechanism by which hemopexin maintains both high binding affinity and the ability to release heme for cellular internalization represents an elegant example of protein evolution. The dual function of heme binding and release appears to be mechanically facilitated by the two β-propeller domains whose flexibility allows conformational changes upon receptor binding. When hemopexin binds to its receptor (LRP1), conformational changes in the protein likely promote heme release, allowing the bound heme to be transferred to intracellular heme-processing machinery. This mechanism ensures that heme remains sequestered and inactive during circulation but becomes available for cellular processing upon reaching target cells.

## Molecular Characterization of Heme Transfer and Oxidation States

The process of heme transfer from hemoglobin to hemopexin occurs through a multistage mechanism coordinated by oxidation states of the heme. Studies highlight that the heme moiety can be transferred from hemoglobin to hemopexin, and this transfer preferentially occurs when heme is oxidized to its ferric form[2]. The heme group transfer to hemopexin is coordinated preferentially when heme moieties are oxidized to their ferric form, and the process appears to proceed in a four-stage process in which hemopexin successively transfers all four heme groups from the hemoglobin tetramer, first binding to the hemoglobin β chains, followed by loss from the hemoglobin α chains[2]. This sequential transfer pattern reflects the structural asymmetry of the hemoglobin tetramer and the differential accessibility of heme groups within the hemoglobin quaternary structure.

Within the plasma compartment, heme exhibits complex dynamics involving multiple binding proteins. Initially, free heme binds to lipoproteins in the plasma before gradually transitioning to albumin and then to hemopexin[5][11][51][58]. This sequential binding reflects the relative concentrations of these proteins in plasma and their respective heme-binding affinities. While albumin and lipoproteins can bind heme, these complexes are relatively unstable and prone to dissociation, allowing heme to transfer to hemopexin as the high-affinity end-point receptor[2][58]. The inhibitory effect of hemopexin can be mitigated by the presence of human serum albumin, and hemin is gradually transferred to hemopexin from albumin rather than initially binding to hemopexin when released in physiologically relevant protein mixtures[11][51].

## Cellular Localization and Subcellular Compartmentalization

Hemopexin circulates as a plasma protein but functions in multiple cellular and tissue compartments through both systemic delivery and local tissue production. The primary site of hemopexin synthesis is the liver, where hepatocytes represent the major source of circulating hemopexin[1][5][51][54]. While primarily expressed by the liver, hemopexin is also found in tissues such as the nervous system, skeletal muscle, retina, and kidney[5][51]. The presence of hemopexin in cerebrospinal fluid represents another site of hemopexin localization, with hemopexin being expressed by ependymal cells that line the ventricular system and by neurons and glia in the central nervous system[26][51]. However, hemopexin levels in the cerebrospinal fluid are approximately tenfold lower than those in circulation, suggesting a relatively low capacity for heme binding in the brain which can become easily overwhelmed in pathological states[5][51].

At the cellular level, hemopexin enters cells through receptor-mediated endocytosis following binding to the LRP1/CD91 receptor on the cell surface. Following ligand binding, hemopexin-heme complexes are internalized via clathrin-mediated endocytosis and are transported through the endosomal pathway. Recent studies demonstrate that heme–hemopexin, which regulates cell iron homeostasis and proliferation/cell growth, is taken up by clathrin-mediated endocytosis and delivers ferrous iron safely to the iron-responsive element/iron regulatory protein (IRE/IRP) system of translational regulation[8][43]. Once internalized, hemopexin is transported to lysosomes where the complex is dissociated by lysosomal proteases, releasing the heme for further metabolism[7][43]. Some hemopexin may be recycled intact back to the plasma, particularly in certain cell types that express alternative hemopexin receptors, while in hepatocytes and macrophages, a substantial portion undergoes lysosomal degradation[7][8][43][46].

Evidence for alternative hemopexin uptake pathways has emerged from studies in cell lines lacking LRP1 expression. Hemopexin trafficking in LRP1-deficient HL-60 cells (which lack immunologically detectable LRP1) shows co-localization with transferrin and transferrin receptor 1 (TfR1) in Rab5-positive early endosomes, supporting a clathrin-mediated endocytotic pathway used by transferrin receptors[8][43]. This observation suggests that at least one other receptor system for heme–hemopexin uptake and apo-hemopexin recycling exists beyond the well-characterized LRP1 pathway[8][43]. In LRP1-expressing HepG2 hepatoma cells, hemopexin co-localizes with both TfR1 and transferrin receptor 2 (TfR2), implicating these receptors in hepatic hemopexin uptake[8][43]. These findings indicate that hemopexin endocytosis is not limited to a single receptor pathway but rather employs multiple receptor systems depending on tissue type and cell-specific receptor expression patterns.

## Receptor-Mediated Endocytosis: The LRP1/CD91 Pathway

The identification and characterization of the hemopexin-heme receptor represents a major advance in understanding hemopexin's cellular functions. Using a ligand-affinity approach, the human hemopexin-heme receptor was purified and identified as the low-density lipoprotein receptor-related protein (LRP)/CD91, a multifunctional scavenger receptor expressed in several cell types including macrophages, hepatocytes, neurons, and syncytiotrophoblasts[7][50]. Binding experiments, including surface plasmon resonance (Biacore) analysis, showed that hemopexin-heme complex formation elicits high receptor affinity, with the complex binding to LRP1 with greater affinity than either apo-hemopexin or heme alone[7][50]. This preferential high-affinity binding of the hemopexin-heme complex to LRP1 represents an elegant regulatory mechanism ensuring efficient cellular uptake of the heme-loaded form of hemopexin.

The cellular internalization of the hemopexin-heme-LRP1 complex has been directly demonstrated through multiple methodological approaches. Uptake studies of radio-labeled hemopexin-heme complex in LRP/CD91-expressing COS cells and confocal microscopy of the cellular processing of fluorescent hemopexin-heme complex established the ability of LRP/CD91 to mediate hemopexin-heme internalization resulting in cellular heme uptake and lysosomal hemopexin degradation[7][50]. The internalization process involves standard receptor-mediated endocytosis through clathrin-coated pits, followed by transport to early endosomes and then to lysosomes[7][46]. Upon lysosomal degradation of hemopexin, the bound heme is released and becomes available for enzymatic catabolism and iron recovery within the cell.

The functional consequence of hemopexin-heme uptake through the LRP1 pathway includes induction of protective cellular responses. Uptake of hemopexin-heme complex induced LRP/CD91-dependent heme-oxygenase 1 (HO-1) mRNA transcription in cultured monocytes[7][50]. This heme oxygenase-1 induction is mediated through intracellular heme signaling, wherein the released heme interacts with the transcription factor Bach1, leading to its inactivation and release from the HO-1 promoter, permitting NRF2-mediated transcriptional activation[13][16]. The induction of heme oxygenase-1 and its metabolic products (carbon monoxide, biliverdin, and iron) provides potent antioxidant and anti-inflammatory protection at the cellular level.

The LRP1 receptor exhibits extraordinarily broad ligand specificity, serving as a multifunctional receptor for diverse plasma proteins involved in hemostasis, inflammation, and neurobiological processes. Beyond hemopexin-heme complexes, LRP1 serves as a receptor for multiple other ligands including apolipoprotein E, α-2-macroglobulin, tissue plasminogen activator, plasminogen activator inhibitor-1, factor VIII, lactoferrin, and amyloid-beta[49][52]. This broad ligand specificity raises the possibility that in pathological states where multiple ligands are elevated, competition for LRP1-mediated endocytosis may occur, potentially impairing hemopexin-heme clearance. Indeed, impaired heme clearance occurs when CD91 is saturated with its ligands or when hemopexin levels are depleted[5][51].

## Heme Catabolism and Iron Recycling

The heme detoxification process is primarily driven by hemopexin through CD91/LRP1-mediated endocytosis in the liver, leading to heme degradation, reutilization, and iron metabolism, with some hemopexin molecules being recycled back into the plasma[5][51]. Upon intracellular delivery of heme to hepatocytes and macrophages, hemopexin releases its bound ligand for internalization and the heme is rapidly catabolized by heme oxygenase enzymes. The primary metabolic pathway for heme involves enzymatic degradation by heme oxygenase (HO), which catalyzes the conversion of heme to biliverdin, carbon monoxide, and iron[5][6][51]. The iron released from heme catabolism is either bound to ferritin for storage or exported from cells to hematopoietic tissues via the iron-transporter ferroportin, where it is reused to support erythropoiesis[5].

This iron recycling process represents a crucial component of iron homeostasis, as the body conserves iron from the continuous catabolism of aging red blood cells. Hemopexin-dependent uptake of extracellular heme leads to the deactivation of Bach1 repression which triggers transcriptional activation of the antioxidant heme oxygenase-1 gene[1]. Furthermore, hemopexin preserves the body's iron through this efficient recycling pathway, ensuring that iron from catabolized hemoproteins is recovered and made available for new hemoglobin synthesis rather than being lost through excretion or deposition in tissues[1]. This iron conservation function becomes especially important during conditions of chronic hemolysis or repeated transfusion where massive amounts of hemoglobin iron must be processed and recycled.

## Role in Inflammatory Regulation and Immune Response

Beyond simple heme scavenging, hemopexin plays complex and multifaceted roles in immune regulation that modulate inflammatory responses in both cell-autonomous and non-cell-autonomous mechanisms. Hemopexin and haptoglobin associate with high-density lipoprotein (HDL) and influence the inflammatory properties of HDL, suggesting that hemopexin affects the immunological profile of circulating lipoproteins[1]. Hemopexin can downregulate the angiotensin II Type 1 receptor (AT1-R) in vitro, indicating potential effects on vascular tone and blood pressure regulation through effects on the renin-angiotensin system[1].

The anti-inflammatory effects of hemopexin have been demonstrated in multiple experimental models. Hemopexin downregulates lipopolysaccharide (LPS)-induced production of the inflammatory cytokines tumor necrosis factor-alpha (TNF-α) and interleukin-6 (IL-6) in mouse bone marrow-derived macrophages[19]. These anti-inflammatory effects occur through at least two mechanisms: direct heme sequestration preventing heme-mediated toll-like receptor activation, and induction of cytoprotective gene expression programs including heme oxygenase-1 and other antioxidant proteins[5][51]. The heme oxygenase-1 enzyme generates carbon monoxide and biliverdin, both of which possess potent anti-inflammatory properties and suppress pro-inflammatory cytokine production.

Hemopexin functions as an acute-phase protein that is negatively regulated by Th17 cells and serves as a negative regulator of Th17-mediated inflammation. In the experimental autoimmune encephalomyelitis (EAE) mouse model of multiple sclerosis, hemopexin content in serum increased and remained high during disease progression[20]. When EAE was induced in hemopexin knockout mice, they developed clinically earlier and exacerbated EAE compared with wild-type mice, associated with a higher amount of CD4+ T cell infiltration[20]. The severe EAE developed by hemopexin-deficient mice could be ascribed to enhanced expansion of Th17 cells accounting for both higher disposition of naive T cells to differentiate toward the Th17 lineage and higher production of Th17-differentiating cytokines IL-6 and IL-23 by antigen-presenting cells[20]. When purified human hemopexin was injected into hemopexin-deficient mice before EAE induction, Th17 expansion and disease severity were comparable with those of wild-type mice, demonstrating that hemopexin's anti-inflammatory effects could be reconstituted by protein supplementation[20].

Hemopexin's anti-inflammatory effects extend to suppression of complement activation pathways. Hemopexin prevented heme-mediated complement activation in both plasma and the kidneys in preclinical models[5]. A recent study revealed that hemopexin could protect factor I activity in vitro, facilitating the degradation of soluble and surface-bound C3b, thus inhibiting complement activation and subsequent vascular and organ injury[5]. These observations suggest that hemopexin acts at multiple points in the complement cascade to limit excessive complement activation that could cause tissue damage.

## Central Nervous System Functions and Neuroprotection

Hemopexin is expressed in the central nervous system and plays important roles in neural homeostasis and neurogenic processes. Hemopexin is present in both plasma and cerebrospinal fluid, and is expressed by neurons and glia in the central nervous system[5][51]. Intrathecally produced hemopexin represents another source of hemopexin in cerebrospinal fluid, originating from local synthesis by ependymal cells and neural parenchyma[5][51]. However, hemopexin levels in the cerebrospinal fluid are approximately tenfold lower than those in circulation, suggesting a relatively low capacity for heme binding in the brain, which can become easily overwhelmed in pathological states[5][51].

The neuroprotective functions of hemopexin have been demonstrated in multiple disease contexts. An ex vivo study supported the neuroprotective effects of hemopexin, as it protects neurons and glial cells from blood-related injuries through antioxidation and downregulation of heme oxygenase-1 and caspase-3 expression[5][51]. Preclinical research indicated that higher levels of hemopexin in the brain improve outcomes after intracerebral hemorrhage in mouse models[5][51]. Elevated local hemopexin levels were associated with smaller lesion volumes, reduced perihematomal tissue injury, and trends toward decreased hematoma volumes[5][51]. Additionally, mice with higher hemopexin levels experienced no significant changes in brain iron levels and heme oxygenase-1 expression but exhibited increased microglial activation and decreased astrocytic activation and lipid peroxidation, suggesting the potential synergy of central and peripheral heme clearance[5][51].

Beyond heme scavenging, hemopexin plays an unexpected role in neural stem cell biology and adult neurogenesis. Hemopexin deletion leads to neurogenic abnormalities in the subventricular zone/olfactory bulb pathway[26]. The lateral ventricle is enlarged in hemopexin-deficient mice, and more apoptosis is observed in doublecortin (Dcx)+ neuroblasts[26]. Lineage differentiation of neural stem cells was inhibited in the subventricular zone of hemopexin-deficient mice, with more stem cells remaining in an undifferentiated, GFAP+ radial glia-like cell stage[26]. Moreover, hemopexin deletion resulted in impaired neuroblast migration in the rostral migratory stream[26]. Exogenous hemopexin protein inhibited apoptosis and promoted the migration and differentiation of cultured neural stem cells[26]. Immunohistochemical analysis demonstrated that hemopexin deletion reduced the number of interneurons in the olfactory bulb[26]. These findings reveal a previously unknown function for hemopexin in the central nervous system, operating as a regulatory factor during adult neurogenesis through mechanisms that appear to extend beyond simple heme detoxification.

## Role in Brain Iron Homeostasis

Hemopexin plays an important role in controlling brain iron distribution and iron-related processes in neural tissue. Hemopexin-null mice demonstrate altered iron distribution in brain with increased iron accumulation in specific regions. Analysis of Perl's-stained serial sections encompassing the basal ganglia and thalamus revealed increased numbers of iron-loaded cells in hemopexin-null mice compared to age-matched wild-type controls[21]. Prominently affected areas included the globus pallidus and the caudate-putamen nucleus, with counts of Perl's-positive cells showing approximately twofold greater iron loading in hemopexin-null mice[21].

Consistent with increased iron deposits and inadequate ferritin expression, malondialdehyde levels and Cu–Zn superoxide dismutase-1 expression were higher in the brain of hemopexin-null mice than in wild-type controls[21]. These data demonstrate that hemopexin plays an important role in controlling iron distribution within brain, thus suggesting its involvement in iron-related neurodegenerative diseases[21]. The increased oxidative stress markers and altered antioxidant enzyme expression in hemopexin-deficient brains indicate that hemopexin deficiency leads to iron-dependent oxidative stress in neural tissue.

However, the relationship between hemopexin and Alzheimer's disease pathology appears complex and potentially context-dependent. Low cerebrospinal fluid levels of hemopexin are associated with increased Alzheimer's pathology, hippocampal hypometabolism, and cognitive decline in some studies[29]. In contrast, other studies have reported that higher plasma hemopexin levels are associated with progression of Alzheimer's disease pathology and decline in cognitive score[47]. Proteomics studies have demonstrated increased plasma and cerebrospinal fluid hemopexin in Alzheimer's disease patients compared to cognitively normal subjects, suggesting impaired compensation in neurodegeneration[47]. These apparently contradictory findings may reflect the complex balance between protective effects of hemopexin-mediated heme scavenging and potentially harmful effects of hemopexin-mediated disruption of normal iron homeostasis in the context of amyloid and tau pathology.

## Disease-Specific Roles and Therapeutic Potential

### Sickle Cell Disease and Vaso-Occlusion

In sickle cell disease, hemopexin plays a critical protective role against heme-mediated vascular complications. Hemolysis releases free hemoglobin and hemoglobin-containing microparticles into the vasculature that upon oxidation to methemoglobin free heme from the globin, which in turn can promote oxidative stress and activate toll-like receptor 4 (TLR4) signaling[37]. In mouse models of sickle cell disease, unless hemopexin is present or replenished, heme causes endothelial cells to present surface adhesion molecules leading to stasis and vaso-occlusion in part via toll-like receptor-4 activation and pulmonary endothelia to produce neutrophil extracellular traps[19]. Sickle cell disease patients have low serum hemopexin levels likely due to chronic hemolysis leading to increased hemopexin catabolism with insufficient compensatory increase in synthesis[37].

Acute studies have shown hemopexin infusion prior to a heme challenge protects sickle mice from vaso-occlusion and developing acute pulmonary injury[37]. Chronic hemopexin infusion therapy modified heme toxicity to endothelium[37]. HPX-deficient sickle mice had 34% ± 3% microvascular stasis at 1 hour post-heme challenge and 24% ± 2% at 4 hours, significantly greater than hemopexin-replete sickle mice which had 21% ± 5% and 13% ± 8% at 1 and 4 hours respectively[37].

Gene therapy studies have demonstrated that hepatic overexpression of hemopexin in transgenic sickle mice via Sleeping Beauty transposon-mediated gene therapy markedly increases nuclear Nrf2 expression in the livers of sickle mice, presumably by promoting delivery of heme to the liver and activating the Keap1-Nrf2 axis[37]. In addition, hepatic heme oxygenase-1 activity and protein and CD91 protein were increased in sickle mice overexpressing hemopexin and NF-κB activation was markedly decreased as assessed by nuclear phospho-p65-NF-κB expression[37]. These findings demonstrate that supplementing hemopexin levels in transgenic sickle mice via gene therapy activates the antioxidant Nrf2 axis and ameliorates inflammation and vaso-occlusion[37].

Plasma-derived hemopexin has demonstrated bioavailability and therapeutic efficacy in preclinical models of sickle cell disease. Hemopexin administered intravenously prevented or relieved vascular stasis induced by free hemoglobin and by hypoxia-reoxygenation in a dose-dependent manner[40]. Plasma-derived hemopexin inhibited heme-mediated cellular externalization of P-selectin and von Willebrand factor, and expression of IL-8, VCAM-1, and heme oxygenase-1 in cultured endothelial cells in a dose-responsive manner[40]. Repeated intravenous administration of hemopexin was well tolerated in rats and non-human primates with no adverse findings attributable to human hemopexin[40]. Hemopexin had a half-life in wild-type mice, rats, and non-human primates of 80–102 hours, whereas a reduced half-life of hemopexin in Townes sickle cell disease mice was observed (approximately 7 hours) due to ongoing hemolysis and target-mediated drug disposition[40][59]. These pharmacokinetic data have led to a Phase 1 clinical trial of hemopexin in adults with sickle cell disease, which is currently ongoing[40].

### Sepsis and Critical Illness

Hemopexin plays important protective roles in sepsis and other critical illnesses involving hemolytic stress and infection-induced inflammation. Elevated heme levels, a consequence of hemolysis, are strongly associated with increased susceptibility to bacterial infections and adverse sepsis outcomes, particularly in older populations[38]. Mean plasma hemopexin levels are increased above baseline in mouse models of endotoxemia, burn wound infection, and peritonitis-induced sepsis[41]. Several lines of evidence have suggested that hemopexin could be beneficial in settings where infection and free heme coexist[41]. First, hemopexin decreases the synergistic production of TNF and IL-6 from macrophages exposed to heme or hemoglobin together with lipopolysaccharide, Escherichia coli, Staphylococcus aureus, or HMGB1[41]. Second, hemopexin has been protective in mouse models of sepsis[41]. Third, elevated cell-free plasma hemoglobin or decreased plasma hemopexin is associated with increased mortality in sepsis[41].

In a sepsis model using cecal ligation and puncture, elevated heme levels correlate with Kupffer cell loss, increased bacterial burden, and heightened mortality[38]. Mechanistically, heme activates phospholipase C gamma (PLC-γ), facilitating the translocation of cleaved gasdermin D to mitochondria, resulting in mitochondrial dysfunction and release of mitochondrial DNA during bacterial infection[38]. This mitochondrial damage amplifies PANoptosis (a form of cell death integrating pyroptosis, apoptosis, and necroptosis) and triggers the cGAS-STING signaling pathway, further driving immune senescence[38].

Hemopexin treatment significantly reduces mitochondrial damage, cell death, and senescence caused by heme and bacterial infection[38]. Hemopexin effectively mitigates sepsis-induced Kupffer cell death and senescence, enhances bacterial clearance, and improves survival outcomes in both young and aged mice[38]. Notably, aging is associated with reduced hemopexin levels, which may contribute to increased heme-mediated immune dysfunction and potentially increased susceptibility to sepsis in elderly populations[38].

Plasma hemopexin concentrations are markedly decreased or virtually undetectable in some patients with sepsis and acute respiratory distress syndrome, some patients with severe burns, and most premature infants[41]. These results support the concept that there is a subset of patients in each population who might benefit from hemopexin repletion[41]. However, IL-6 levels were negatively correlated with hemopexin levels in mouse models, possibly due to hepatic dysfunction or the increased consumption of hemopexin by binding to increased free heme that outstripped production[41].

### Anthracycline Cardiotoxicity

Circulating hemopexin modulates anthracycline-induced cardiotoxicity, representing an unexpected cardioprotective mechanism. An increase in hemopexin at 3 months after anthracycline initiation was associated with cardiac toxicity as assessed by echocardiography[39]. However, preclinical data demonstrate that hemopexin deficiency exacerbates doxorubicin-induced cardiac dysfunction, with hemopexin deficiency exacerbating increased lipid peroxidation and dichlorofluorescein (DCF) fluorescence in the heart with or without doxorubicin treatment[39]. Hemopexin administration to wild-type mice treated with doxorubicin improved cardiac function[39].

This study supports a role for hemopexin induction as a cardioprotective mechanism activated in the setting of doxorubicin-induced chronic cardiomyopathy[39]. Although plasma hemopexin levels in patients were associated with increased cardiac toxicity, the preclinical data suggest that higher levels of hemopexin in patients treated with anthracyclines should be physiologically beneficial and cardioprotective[39]. The hypothesis is that circulating hemopexin increased in both patients and mice in response to anthracycline-induced cardiac dysfunction, representing an endogenous adaptive response to mitigate cardiotoxicity[39]. Both baseline levels of hemopexin and changes in hemopexin over time were associated with early cardiac toxicity, suggesting that hemopexin may serve as a useful biomarker for anthracycline cardiotoxicity[39].

### Hemorrhagic and Traumatic Brain Injury

The role of hemopexin in traumatic brain injury and intracerebral hemorrhage has been explored in preclinical models. Deletion of the hemopexin gene can aggravate brain injury followed by stroma-free hemoglobin-induced intracerebral hemorrhage[1]. High hemopexin levels in cerebrospinal fluid are associated with poor outcome after subarachnoid hemorrhage in some studies, although the mechanism underlying this apparent paradoxical relationship remains to be elucidated[1]. A possible explanation is that when the level of hemopexin in cerebrospinal fluid is excessively high, it may become deleterious as it impedes the efflux of heme due to its high heme affinity, resulting in intracellular heme/iron overload, which can be toxic to neurons and glia[51].

In a mouse model of intracerebral hemorrhage, endogenous low-density lipoprotein receptor-related protein-1 and hemopexin were increased in ipsilateral brain after intracerebral hemorrhage, accompanied by increased hemoglobin levels, brain water content, blood–brain barrier permeability and neurological deficits[49]. Exogenous recombinant LRP1 increases hemopexin-heme scavenging and reduces oxidative stress and neuronal apoptosis after intracerebral hemorrhage, with these protective effects tended to be reversed by siRNA-mediated knockdown of LRP1[49]. These results demonstrate that LRP1 is involved in heme scavenging and blood-brain barrier protection in adjacent hematoma brain tissue after intracerebral hemorrhage[49].

## Iron Homeostasis and Metabolic Functions

Hemopexin contributes to whole-body iron homeostasis through its role in heme-iron recovery and redistribution. Hemopexin binds heme and transports it to the liver for breakdown and iron recovery, after which the free hemopexin returns to the circulation[3][6]. This efficient recycling system ensures that iron from degraded hemoproteins is conserved and made available for new hemoglobin and other heme-containing protein synthesis. Impaired heme clearance occurs when CD91 is saturated with its ligands or when hemopexin levels are depleted, compromising the body's ability to manage heme-derived iron during periods of hemolytic stress[5][51].

In the duodenum, hemopexin influences iron uptake and handling. Hemopexin-null mice showed elevated iron deposits in enterocytes, associated with higher duodenal high-chain-ferritin levels and a significant increase in duodenal heme oxygenase activity[24]. This suggests that hemopexin regulates the amount of heme available for absorption in the intestine, thereby controlling intestinal iron uptake from dietary heme sources. The increased heme oxygenase activity in hemopexin-deficient duodenum suggests compensatory induction of heme-catabolizing enzymes in response to elevated heme levels, leading to increased iron uptake from enhanced local heme catabolism.

## Pathophysiological Context and Context-Dependent Functions

While hemopexin generally functions in a protective capacity, emerging evidence indicates that hemopexin can exert harmful effects under certain pathological conditions, particularly when hemopexin levels are elevated in specific tissue compartments or disease contexts. A study revealed that skeletal muscle atrophy-induced hemopexin accelerates the onset of memory impairment in a mouse model of Alzheimer's disease[44]. Continuous intracerebroventricular infusion of recombinant hemopexin for 2 weeks induced memory deficits in young 5XFAD mice, with lipocalin-2 (a neuroinflammatory factor) increased in the hippocampus in hemopexin-infused 5XFAD mice compared to control mice[44]. The hypothesis emerging from this research is that skeletal muscle atrophy elicits cognitive impairment through the secretion of hemopexin that travels to the brain and exerts detrimental effects on neural function[44].

This context-dependent dual role of hemopexin reflects the complexity of heme biology in disease states. While hemopexin's heme-scavenging function is generally protective against heme toxicity and oxidative damage, excessive hemopexin in specific tissue compartments or under certain pathological conditions may impair local iron homeostasis or generate unwanted inflammatory responses. The mechanisms underlying these context-dependent effects remain incompletely understood but likely involve alterations in local iron metabolism, changes in the balance of protective versus toxic heme metabolites (such as carbon monoxide and biliverdin versus oxidative products), and shifts in the tissue microenvironment that alter hemopexin's immunological effects.

## Structural Family and Related Proteins

Hemopexin belongs to the hemopexin family of evolutionarily related proteins characterized by hemopexin-like repeating domains. Hemopexin-like repeats occur in vitronectin and some matrix metalloproteinases family members (matrixins)[31]. The hemopexin-like domains facilitate binding to a variety of molecules and proteins; for example, the hemopexin repeats of some matrixins bind tissue inhibitor of metallopeptidases (TIMPs)[31]. The hemopexin domain in matrix metalloproteinases is located in the C-terminal section of the protein and facilitates binding to inhibitory proteins and cellular receptors, including LRP1[31][52].

In some teleost fish species, duplicate copies of the mammalian hemopexin ortholog exist, including a warm temperature acclimation-related protein (WAP65)[45][48]. These fish hemopexin orthologs likely perform similar heme-binding functions as mammalian hemopexin but may have acquired additional functions related to temperature acclimation. The conservation of hemopexin structure and function across vertebrate species indicates that heme scavenging represents an ancient and fundamental physiological requirement for organisms utilizing heme as a prosthetic group for oxygen transport and metabolism.

## Synthesis, Molecular Characteristics, and Quantification

Hemopexin is a single-chain plasma glycoprotein with a molecular weight of approximately 60 kilodaltons (or 57 kilodaltons in some literature references)[5][51][54]. The protein is composed of approximately 440 amino acid residues and exhibits extensive post-translational modifications including both N-linked and O-linked glycosylation[32][35]. The high carbohydrate content of hemopexin (approximately 20% by mass) contributes to its solubility and may influence its binding properties and receptor interactions[32][35]. The glycosylation of hemopexin includes 12 sites of glycosylation overall: 5 N-linked glycosylation sites and 6 O-linked glycosylation sites (accounting for approximately 226 N-linked glycans and 9 O-linked glycans respectively)[3].

The native fluorescence properties of hemopexin reflect its tryptophan content and the conformational changes that occur upon heme binding. The hemopexin molecule contains 18 tryptophan residues arranged in four distinctive clusters, each cluster containing three to four tryptophan residues separated by zero to twelve intervening amino acids[32][35]. Both heme and metal-free porphyrin binding effectively quench the tryptophan fluorescence of hemopexin, observations that do not necessarily indicate direct participation of tryptophan in the heme-binding site but imply that tryptophan-tryptophan interactions are affected when heme is bound by hemopexin[32][35]. The intrinsic fluorescence of hemopexin can therefore be exploited as an analytical tool for detecting and quantifying heme binding.

## Conclusion and Future Directions

Hemopexin represents a multifunctional plasma glycoprotein that serves as the highest-affinity heme-binding protein known, with extraordinary binding affinity that enables effective scavenging and detoxification of free heme released from hemoproteins under conditions of hemolysis, hemorrhage, and cellular stress[1][14][17][51]. The primary function of hemopexin—the sequestration and transport of free heme to hepatocytes and macrophages for catabolism and iron recovery—represents a critical protective mechanism that prevents the oxidative damage, inflammatory activation, and cellular toxicity that would otherwise result from circulating free heme[1][5][51]. The molecular basis for this extraordinary binding affinity resides in the unique structural organization of two similar four-bladed β-propeller domains connected by a flexible hinge region containing critical histidine residues that coordinate the heme iron[14][17].

Beyond classical heme detoxification, emerging evidence has expanded understanding of hemopexin function to encompass multiple biological processes including immune regulation, anti-inflammatory signaling, neural stem cell biology, brain iron homeostasis, vascular function, and cardiac metabolic adaptation[1][5][20][26][39][51]. The identification of multiple hemopexin receptor systems including the well-characterized LRP1/CD91 receptor and alternative transferrin receptor-mediated pathways indicates that hemopexin functions through tissue-specific endocytic mechanisms adapted to the particular physiological needs of different cell types and tissues[7][8][43][50]. The therapeutic potential of hemopexin supplementation in hemolytic diseases including sickle cell disease, transfusion-induced hemolysis, and sepsis has been demonstrated in preclinical models and has led to ongoing clinical trials[37][40].

However, context-dependent and potentially harmful effects of hemopexin in specific disease states—such as accelerated cognitive decline in Alzheimer's disease, poor prognosis after subarachnoid hemorrhage, and associations with cardiac toxicity following anthracycline therapy—indicate that the biological effects of hemopexin are not uniformly protective[39][44][51]. Future research must clarify the mechanisms underlying these context-dependent effects, define the tissue-specific and pathological conditions in which hemopexin supplementation would be beneficial versus harmful, and develop strategies to optimize hemopexin-based therapeutic approaches. The multifunctional nature of hemopexin as both a protective heme scavenger and a signaling molecule capable of influencing gene expression, immune function, and tissue development represents a compelling target for therapeutic intervention in multiple disease contexts characterized by hemolytic stress, oxidative injury, and dysregulated heme metabolism.

## Citations

1. https://en.wikipedia.org/wiki/Hemopexin
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC8998376/
3. https://pubchem.ncbi.nlm.nih.gov/protein/P02790
4. https://www.ncbi.nlm.nih.gov/gene/3263
5. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1274333/full
6. https://www.reactome.org/content/schema/instance/browser/uniprot:P02790
7. https://pubmed.ncbi.nlm.nih.gov/15947085/
8. https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1613917/full
9. https://ashpublications.org/blood/article/106/7/2225/21652/Handling-heme
10. https://reactome.org/content/detail/R-HSA-2168897
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC10653390/
12. https://journals.sagepub.com/doi/abs/10.1177/15353702221139185
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC129038/
14. https://www.nature.com/articles/nsb1099_926
15. https://www.semanticscholar.org/paper/f878445a667a3bcba208c3f9911ba87da30d1cfc
16. https://academic.oup.com/nar/article/35/21/7074/2375687
17. https://pubmed.ncbi.nlm.nih.gov/10504726/
18. https://pubmed.ncbi.nlm.nih.gov/7681064/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC4485156/
20. https://pubmed.ncbi.nlm.nih.gov/24154625/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC4496126/
22. https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2014.00415/full
23. https://pubmed.ncbi.nlm.nih.gov/34298052/
24. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0068146
25. https://www.nature.com/articles/cmi201597
26. https://www.nature.com/articles/s41419-018-0328-0
27. https://pubmed.ncbi.nlm.nih.gov/7857266/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7775585/
29. https://faseb.onlinelibrary.wiley.com/doi/full/10.1096/fj.202400863RR
30. https://en.wikipedia.org/wiki/Hemopexin_family
31. https://www.pnas.org/doi/pdf/10.1073/pnas.81.7.2021
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC6925827/
33. https://www.ncbi.nlm.nih.gov/Structure/cdd/cl02471
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC345428/
35. https://pubmed.ncbi.nlm.nih.gov/8096/
36. https://ashpublications.org/blood/article/126/23/412/136085/Hemopexin-Gene-Therapy-Inhibits-Inflammation-and
37. https://www.nature.com/articles/s41419-025-07637-6
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC9788780/
39. https://pubmed.ncbi.nlm.nih.gov/35160081/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC4424824/
41. https://database.clin-star.org/display/project-5R01HL16317203
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC8718090/
43. https://pubmed.ncbi.nlm.nih.gov/24344252/
44. https://pubmed.ncbi.nlm.nih.gov/1964416/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC7285604/
46. https://academic.oup.com/jhered/article/105/2/237/791325
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC5453452/
48. https://pubs.acs.org/doi/10.1021/acs.biochem.3c00705
49. https://pubmed.ncbi.nlm.nih.gov/30219641/
50. https://pubmed.ncbi.nlm.nih.gov/19650691/
51. https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2015.00187/full
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC4211382/
53. https://pmc.ncbi.nlm.nih.gov/articles/PMC2880807/
54. https://pmc.ncbi.nlm.nih.gov/articles/PMC8836474/
55. https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2014.00034/full