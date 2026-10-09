---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-10-09T19:23:51.304167'
end_time: '2026-10-09T19:40:15.463112'
duration_seconds: 984.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: DROME
  gene_id: cav
  gene_symbol: cav
  uniprot_accession: Q95RV2
  protein_description: 'RecName: Full=Telomere-binding protein cav {ECO:0000303|PubMed:12510197};
    AltName: Full=Anonymous fast evolving 1G5 {ECO:0000303|PubMed:12510197}; AltName:
    Full=HP1/ORC-associated protein {ECO:0000303|PubMed:11408576}; Short=HOAP p55
    {ECO:0000303|PubMed:11408576}; AltName: Full=Protein caravaggio {ECO:0000303|PubMed:12510197};'
  gene_info: Name=cav {ECO:0000303|PubMed:12510197}; Synonyms=anon fe 1G5 {ECO:0000303|PubMed:11408576,
    ECO:0000303|PubMed:12510197}, anon1G5 {ECO:0000303|PubMed:10581279}, Hoap {ECO:0000303|PubMed:11408576},
    IG5 {ECO:0000303|PubMed:9275195}; ORFNames=CG6219 {ECO:0000312|FlyBase:FBgn0026257};
  organism_full: Drosophila melanogaster (Fruit fly).
  protein_family: Not specified in UniProt
  protein_domains: Not specified in UniProt
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 56
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: cav-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: cav-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000028 I have extracted Figure 1, panels B and
    C, which show the fluorescence localization of Flag-tagged D. melanogaster HOAP[mel]
    and D.'
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q95RV2
- **Protein Description:** RecName: Full=Telomere-binding protein cav {ECO:0000303|PubMed:12510197}; AltName: Full=Anonymous fast evolving 1G5 {ECO:0000303|PubMed:12510197}; AltName: Full=HP1/ORC-associated protein {ECO:0000303|PubMed:11408576}; Short=HOAP p55 {ECO:0000303|PubMed:11408576}; AltName: Full=Protein caravaggio {ECO:0000303|PubMed:12510197};
- **Gene Information:** Name=cav {ECO:0000303|PubMed:12510197}; Synonyms=anon fe 1G5 {ECO:0000303|PubMed:11408576, ECO:0000303|PubMed:12510197}, anon1G5 {ECO:0000303|PubMed:10581279}, Hoap {ECO:0000303|PubMed:11408576}, IG5 {ECO:0000303|PubMed:9275195}; ORFNames=CG6219 {ECO:0000312|FlyBase:FBgn0026257};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Not specified in UniProt

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cav" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cav' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cav** (gene ID: cav, UniProt: Q95RV2) in DROME.

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
- **UniProt Accession:** Q95RV2
- **Protein Description:** RecName: Full=Telomere-binding protein cav {ECO:0000303|PubMed:12510197}; AltName: Full=Anonymous fast evolving 1G5 {ECO:0000303|PubMed:12510197}; AltName: Full=HP1/ORC-associated protein {ECO:0000303|PubMed:11408576}; Short=HOAP p55 {ECO:0000303|PubMed:11408576}; AltName: Full=Protein caravaggio {ECO:0000303|PubMed:12510197};
- **Gene Information:** Name=cav {ECO:0000303|PubMed:12510197}; Synonyms=anon fe 1G5 {ECO:0000303|PubMed:11408576, ECO:0000303|PubMed:12510197}, anon1G5 {ECO:0000303|PubMed:10581279}, Hoap {ECO:0000303|PubMed:11408576}, IG5 {ECO:0000303|PubMed:9275195}; ORFNames=CG6219 {ECO:0000312|FlyBase:FBgn0026257};
- **Organism (full):** Drosophila melanogaster (Fruit fly).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Not specified in UniProt

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "cav" matches the protein description above**
2. **Verify the organism is correct:** Drosophila melanogaster (Fruit fly).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'cav' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **cav** (gene ID: cav, UniProt: Q95RV2) in DROME.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

# Functional annotation report: *Drosophila melanogaster cav* (HOAP)

## Identity and principal function

The target is *caravaggio* (*cav*; CG6219), encoding HOAP (HP1/ORC-associated protein), also identified historically as the product of *anon fe 1G5*. The supplied UniProt accession is **Q95RV2**. Primary fly studies independently link *cav* to HOAP; this report does **not** concern mammalian caveolins or another gene abbreviated “cav.” HOAP’s best-established function is as a **nuclear chromosome-end protection protein**: it helps assemble and maintain a protein cap that prevents natural telomeres from being treated as DNA double-strand breaks and fused together. It is a structural DNA/chromatin-associated factor, **not an enzyme or transporter**; no catalyzed reaction or transported substrate is established. (saintleandre2020adaptiveevolutionof pages 1-2, shareef2001drosophilaheterochromatinprotein pages 10-11, raffa2009thedrosophilamodigliani pages 1-2, raffa2011termininaprotein pages 2-3)

The distinction matters because fly chromosome ends differ from conventional telomerase-maintained telomeres. *D. melanogaster* lacks telomerase-based elongation and instead maintains terminal DNA through the specialized retrotransposons **HeT-A, TART and TAHRE**. Nonetheless, HOAP-dependent capping can be assembled at chromosome ends **without a particular terminal DNA sequence**; protection and retrotransposon-driven elongation are related but separable processes. (zhang2016mtvanssdna pages 1-2, gao2010hiphopinteractswith pages 1-2, saintleandre2020adaptiveevolutionof pages 4-5)

## Where HOAP acts and how the cap works

Immunostaining locates HOAP at the tips of **mitotic chromosomes and larval salivary-gland polytene chromosomes**. In cultured fly cells it forms detergent-resistant **nuclear foci** that remain detectable following experimentally induced DNA damage. A direct visual example is the cropped chromosome-localization image from Saint-Leandre *et al.*: both native-species and cross-species HOAP mark mitotic chromosome tips, with HipHop present at those tips. The experimentally demonstrated site of its principal action is therefore **telomeric chromatin in the nucleus**, not the plasma membrane or extracellular space. (raffa2011termininaprotein pages 3-5, saintleandre2020adaptiveevolutionof pages 4-5, saintleandre2020adaptiveevolutionof media 82aff822, on2023telomerecappingprotein pages 7-9)

HOAP binds HipHop, which also interacts with heterochromatin protein 1A (**HP1A**). Biochemical experiments further support HOAP interactions with the capping proteins **Moi** and **Ver**. HOAP and HipHop are interdependent for stable accumulation in the *D. melanogaster* telomere system; depletion of one compromises the other and exposes ends to fusion. Chromatin immunoprecipitation places HOAP–HipHop across roughly **11 kb of terminal chromatin**, including a terminal-deletion model lacking the usual retrotransposon array. This is strong evidence for a chromosome-end-recognition mechanism that does not require a fixed telomeric repeat sequence. (raffa2011termininaprotein pages 3-5, gao2010hiphopinteractswith pages 1-2, gao2010hiphopinteractswith pages 5-6)

The historical name **“terminin”** refers to the fly telomere-specific capping machinery, initially described around HOAP, HipHop, Moi and Ver; Tea was identified subsequently. A useful mechanistic refinement is that **HOAP–HipHop preferentially associates with the duplex telomeric region**, whereas purified **Moi–Tea–Ver (MTV)** binds and protects single-stranded DNA in vitro, with Tea recruiting Moi and Ver. HP1A is an interacting chromatin factor rather than a uniquely telomere-restricted terminin subunit. This division into duplex- and single-strand-associated modules is better supported than assuming that every named protein forms one permanently assembled, biochemically demonstrated complex. The exact architecture of the native chromosome terminus remains unresolved. (raffa2011termininaprotein pages 3-5, zhang2016mtvanssdna pages 1-2)

The functional consequence is unusually clear genetically: a review of the original mutant analyses reports **approximately five telomeric fusions per cell** in severe *cav*, *moi* or *ver* mutants, compared with **fewer than 0.01** G1 or S/G2 telomeric fusions per wild-type cell. The end-protection defect can yield multicentric chromosome chains and lethality. These observations make prevention of inappropriate chromosome-end joining the highest-confidence primary annotation for *cav*. (raffa2011termininaprotein pages 3-5, raffa2011termininaprotein pages 2-3)

## DNA binding, domains and associated pathways

Shareef *et al.* identified HOAP as a roughly 55-kDa HP1/ORC-associated protein and reported **sequence similarity at its amino terminus to HMG-like DNA-binding proteins**. Purified recombinant HOAP bound certain *D. melanogaster* satellite DNAs—particularly AATAT, AATAG and AATAACATAG—and a telomere-associated sequence in electrophoretic mobility-shift experiments. **Those in-vitro binding preferences do not imply that any of those sequences is obligatory for telomere recruitment in vivo**: experiments on terminally deleted chromosomes show that chromosome-end assembly is sequence independent. Nor does HMG-like sequence similarity establish a structurally verified HMG-box domain or a confidently assigned HOAP protein family. The original work also associated HOAP with HP1 and origin-recognition-complex proteins and found dosage-sensitive effects on heterochromatin-associated reporter silencing; an independent essential ORC-catalytic role for HOAP has not been demonstrated. (shareef2001drosophilaheterochromatinprotein pages 10-11, raffa2011termininaprotein pages 3-5, gao2010hiphopinteractswith pages 1-2, shareef2001drosophilaheterochromatinprotein pages 9-10)

The relevant cellular pathways are **telomere capping**, **control of telomeric chromatin and retrotransposons**, and interactions with the **DNA-damage response**. ATM and the Mre11–Rad50–Nbs system influence accumulation of HOAP or its partners at chromosome ends, connecting capping to end-sensing machinery; this does not mean HOAP itself is a kinase, nuclease or general-purpose DNA-repair enzyme. HOAP has also been implicated experimentally in heterochromatin-dependent regulation, but this broader phenotype should not displace its directly established telomeric function. (raffa2011termininaprotein pages 5-6, shareef2001drosophilaheterochromatinprotein pages 1-2, gao2010hiphopinteractswith pages 5-6)

## A second function: restraining telomeric retrotransposons

A particularly informative separation-of-function experiment replaced *D. melanogaster* HOAP with the divergent *D. yakuba* protein. The cross-species HOAP still localized to fly telomeres, recruited HipHop and supported near-normal viability and end protection. The reported frequencies of **chromosome-end associations** were **9%** with HOAP[mel], **15%** with HOAP[yak] and **73%** with the defective *cav1* allele; these percentages describe the study’s association assay and **must not be equated with confirmed fusion rates**. In contrast, HOAP[yak] increased ovarian expression of **all three** telomeric retrotransposons. Over **50 experimental generations**, the investigators observed increases in retrotransposon-mapping sequence and HeT-A signal at **all five assayed polytene chromosome tips**, consistent with excessive telomere elongation. Thus, capping and containment of elements that elongate the telomere are experimentally distinguishable HOAP functions. (saintleandre2020adaptiveevolutionof pages 4-5, saintleandre2020adaptiveevolutionof pages 6-8)

The altered HOAP genotype also had **reduced telomeric H3K9me3** and fewer telomere-associated piRNAs. The authors propose a chromatin/piRNA-mediated mechanism for the increased retrotransposon transcription, but explicitly note that experimentally restoring H3K9me3 would be needed to establish causality in this genotype. Increased telomeric repeat accumulation may involve new insertions, recombination or both; HOAP is **not** established to catalyze retrotransposition. (saintleandre2020adaptiveevolutionof pages 6-8, saintleandre2020adaptiveevolutionof pages 9-11)

## Developments in 2023–2025

**Damage-responsive modification, 2023.** In *Drosophila* S2R+ cells, etoposide or bleomycin exposure induced phosphorylation of HOAP, whereas HipHop did not show the same response. RNAi experiments implicated **ATM and Nbs** in HOAP hyperphosphorylation, and deletion analysis identified HOAP residues **211–270** as necessary for the measured response. HOAP retained DNA-associated nuclear foci and HipHop colocalization in the reported assays. **S249 and T269 are candidate, not verified, phosphorylation sites**: the authors could not establish them by point-mutant confirmation. Whether HOAP phosphorylation changes chromosome-end protection or directly facilitates repair of non-telomeric breaks remains open. (on2023telomerecappingprotein pages 7-9, on2023telomerecappingprotein pages 1-2)

**Partner coevolution, 2024 preprint and 2025 peer-reviewed study.** Swapping *D. yakuba* HipHop into *D. melanogaster* prevented recruitment of the resident HOAP, caused lethal telomeric fusions and exposed a species-specific protein–protein compatibility requirement. The **November 2024 preprint** reported that replacing six interaction-surface residues in otherwise *D. melanogaster* HipHop increased the proportion of mitotic cells with fusions from **3.33% to 93.10%** in its comparison; reciprocal substitutions restored compatibility. Supplying the cognate *D. yakuba* HOAP also restored recruitment, end protection and viability. The **November 2025 peer-reviewed *Science* report** supports the central rescue and compensatory-coevolution conclusion. These are functional tests of a critical HOAP–HipHop interface, not proof that a specific retrotransposon protein directly binds that interface. Because the accessible text indexed under the 2025 article includes pages from the earlier preprint, the numerical fusion comparison above is attributed specifically to the **2024 preprint**. (lin2025rapidcompensatoryevolution pages 7-9, lin2024adaptiveproteincoevolution pages 6-9, lin2025rapidcompensatoryevolution pages 6-7)

The following evidence map distinguishes directly measured functions from structural or mechanistic interpretations. (zhang2016mtvanssdna pages 1-2, saintleandre2020adaptiveevolutionof pages 4-5, on2023telomerecappingprotein pages 1-2, lin2024adaptiveproteincoevolution pages 6-9)

| Molecular aspect | Strongest evidence / quantitative observation | Interpretation / limitation | Source |
|---|---|---|---|
| Identity, putative DNA-binding region | The *anon fe 1G5* product was identified as HOAP p55; its N-terminus showed similarity to sequence-specific HMG proteins. Recombinant HOAP bound double-stranded AATAT, AATAG and AATAACATAG satellite repeats and a 457-bp telomere-associated sequence in mobility-shift assays. (shareef2001drosophilaheterochromatinprotein pages 10-11, shareef2001drosophilaheterochromatinprotein pages 9-10) | Supports intrinsic DNA-binding activity and an HMG-like region, but does **not** establish a structurally validated HMG-box domain or define its binding specificity at native telomeres. | [Shareef et al., 2001](https://doi.org/10.1091/mbc.12.6.1671) |
| Telomeric recruitment and chromatin occupancy | HOAP, HipHop and HP1 occupied an approximately 11-kb terminal chromatin domain; HOAP and HipHop reached roughly 270-fold and 320-fold enrichment, respectively, in a sequence-defined terminal-deletion model lacking canonical telomeric retrotransposon sequence. (gao2010hiphopinteractswith pages 1-2, gao2010hiphopinteractswith pages 5-6) | Demonstrates broad, sequence-independent recruitment to chromosome-end chromatin. It does not establish that HOAP recognizes a particular DNA sequence in vivo. | [Gao et al., 2010](https://doi.org/10.1038/emboj.2009.394) |
| Localization and end protection | HOAP localizes to mitotic- and polytene-chromosome telomeres. Strong *cav*, *moi* or *ver* mutants exhibit approximately five telomeric fusions per cell, versus fewer than 0.01 G1 or S–G2 fusions per wild-type cell. (raffa2011termininaprotein pages 3-5, raffa2011termininaprotein pages 2-3) | Strong genetic evidence that HOAP is a structural chromosome-end cap required to prevent inappropriate fusion; the review-level “terminin” model evolved as additional components were identified. | [Raffa et al., 2011](https://doi.org/10.4161/nucl.2.5.17873) |
| Duplex- versus ssDNA-protective modules | HOAP–HipHop occupies the telomeric duplex region, whereas purified Moi–Tea–Ver (MTV) binds and protects ssDNA without sequence specificity; Tea recruits Moi and Ver to telomeres. (zhang2016mtvanssdna pages 1-2) | Refines the older unitary terminin model into functionally specialized modules: HOAP–HipHop acts primarily on duplex terminal chromatin, while MTV protects an ssDNA component. The precise architecture of native chromosome ends remains incompletely resolved. | [Zhang et al., 2016](https://doi.org/10.1371/journal.pgen.1006435) |
| Conserved capping versus retrotransposon control | D. *yakuba* HOAP localized to D. *melanogaster* telomeres and supported Mendelian viability. Chromosome-end **associations** occurred in 9% of HOAP[mel], 15% of HOAP[yak] and 73% of *cav1* preparations. HOAP[yak] nevertheless increased HeT-A, TART and TAHRE RNA and, over experimental evolution, their copy number and telomeric HeT-A signal. (saintleandre2020adaptiveevolutionof pages 4-5, saintleandre2020adaptiveevolutionof pages 6-8) | A separation-of-function result: end protection is evolutionarily conserved, whereas retrotransposon silencing/containment is species sensitive. The 9%, 15% and 73% measurements are chromosome associations and must not be interpreted as rates of cytologically proven fusion. Reduced H3K9me3 and piRNAs are associated mechanisms, but causal ordering was not established. | [Saint-Leandre et al., 2020](https://doi.org/10.7554/eLife.60987) |
| DNA-damage-responsive phosphorylation | Etoposide or bleomycin induced HOAP—but not HipHop—phosphorylation in S2R+ cells. RNAi implicated ATM and Nbs; deletion mapping identified aa 211–270 as necessary, while phosphorylation did not visibly disrupt DNA binding, nuclear foci or HipHop colocalization. (on2023telomerecappingprotein pages 1-2, on2023telomerecappingprotein pages 7-9) | Establishes regulated HOAP phosphorylation during induced DSB stress. S249 and T269 are candidate ATM S/TQ sites, but point-mutant confirmation failed because mutant proteins were poorly expressed; direct participation of phosphorylated HOAP in DSB repair therefore remains unproven. | [On et al., 2023](https://www.jstage.jst.go.jp/browse/jibs/92/1/_contents) |
| Coevolution of the HOAP–HipHop interface | In the 2024 preprint, replacing six residues in D. *melanogaster* HipHop with the D. *yakuba* state increased the percentage of mitotic cells with telomere fusions from 3.33% to 93.10%; the reciprocal six-residue substitution restored compatibility. Cognate D. *yakuba* HOAP restored telomeric recruitment, end protection and viability. (lin2024adaptiveproteincoevolution pages 1-4, lin2024adaptiveproteincoevolution pages 6-9, lin2025rapidcompensatoryevolution pages 6-7) | Indicates that as few as six adaptively evolving HipHop residues can determine compatibility with HOAP. Exact percentages derive from a preprint; the work was subsequently expanded and peer reviewed. | [Lin et al., 2024 preprint](https://doi.org/10.1101/2024.11.11.623029) |
| Peer-reviewed coevolution update | The peer-reviewed study confirmed that species-mismatched HipHop disrupts HOAP recruitment and causes lethal telomere fusions, whereas reverting six interaction-surface sites or supplying cognate D. *yakuba* HOAP restores recruitment, telomere integrity and viability. (lin2025rapidcompensatoryevolution pages 7-9) | Strong in-vivo evidence for compensatory protein–protein coevolution preserving HOAP-dependent end protection. The proposal that selfish telomeric elements directly drove these interface changes remains an evolutionary model rather than a demonstrated molecular interaction. | [Lin et al., 2025](https://doi.org/10.1126/science.adv0657) |


*Table: Compact evidence map linking Drosophila cav/HOAP identity, localization, molecular partners, end protection, retrotransposon control, damage-responsive phosphorylation and recent coevolution experiments. Limitations distinguish direct observations from proposed mechanisms.*

## Applications and evidence-based annotation

HOAP is used in fly experiments as a **chromosome-tip marker**, a genetic handle for testing chromosome-end protection, and a model for understanding how telomere caps can function without telomerase or a fixed terminal repeat. Cross-species gene replacements and protein-interface swaps are research implementations that distinguish essential capping from retrotransposon repression; they are **not clinical applications**. An appropriately precise annotation is: **“nuclear telomere-associated DNA/chromatin-binding capping factor; interacts with HipHop and other end-protection proteins to prevent end-to-end chromosome fusion; also contributes to repression and containment of telomeric retrotransposons.”** Sequence-specific recognition at native telomeres, a validated HMG-box fold, the direct mechanism of chromatin silencing and a repair role for phosphorylated HOAP remain less certain. (raffa2011termininaprotein pages 3-5, zhang2016mtvanssdna pages 1-2, saintleandre2020adaptiveevolutionof pages 4-5, lin2025rapidcompensatoryevolution pages 7-9, shareef2001drosophilaheterochromatinprotein pages 9-10)

**Selected sources and publication dates:** [Shareef *et al.*, *Molecular Biology of the Cell*, June 2001](https://doi.org/10.1091/mbc.12.6.1671); [Raffa *et al.*, *PNAS*, February 2009](https://doi.org/10.1073/pnas.0812702106); [Gao *et al.*, *EMBO Journal*, February 2010](https://doi.org/10.1038/emboj.2009.394); [Raffa *et al.*, *Nucleus* review, September 2011](https://doi.org/10.4161/nucl.2.5.17873); [Zhang *et al.*, *PLOS Genetics*, November 2016](https://doi.org/10.1371/journal.pgen.1006435); [Saint-Leandre *et al.*, *eLife*, December 2020](https://doi.org/10.7554/eLife.60987); On *et al.*, *Journal of Insect Biotechnology and Sericology* **92:1–15 (2023)**; [Lin *et al.*, bioRxiv preprint, November 11, 2024](https://doi.org/10.1101/2024.11.11.623029); and [Lin *et al.*, *Science*, November 2025](https://doi.org/10.1126/science.adv0657). (shareef2001drosophilaheterochromatinprotein pages 10-11, zhang2016mtvanssdna pages 1-2, gao2010hiphopinteractswith pages 1-2, raffa2009thedrosophilamodigliani pages 1-2, raffa2011termininaprotein pages 2-3, saintleandre2020adaptiveevolutionof pages 4-5, on2023telomerecappingprotein pages 1-2, lin2024adaptiveproteincoevolution pages 1-4, lin2025rapidcompensatoryevolution pages 1-4)

References

1. (saintleandre2020adaptiveevolutionof pages 1-2): Bastien Saint-Leandre, Courtney Christopher, and Mia T Levine. Adaptive evolution of an essential telomere protein restricts telomeric retrotransposons. eLife, Dec 2020. URL: https://doi.org/10.7554/elife.60987, doi:10.7554/elife.60987. This article has 29 citations and is from a domain leading peer-reviewed journal.

2. (shareef2001drosophilaheterochromatinprotein pages 10-11): Mohammed Momin Shareef, Chadwick King, Mona Damaj, RamaKrishna Badagu, Da Wei Huang, and Rebecca Kellum. Drosophila heterochromatin protein 1 (hp1)/origin recognition complex (orc) protein is associated with hp1 and orc and functions in heterochromatin-induced silencing. Molecular biology of the cell, 12 6:1671-85, Jun 2001. URL: https://doi.org/10.1091/mbc.12.6.1671, doi:10.1091/mbc.12.6.1671. This article has 164 citations and is from a domain leading peer-reviewed journal.

3. (raffa2009thedrosophilamodigliani pages 1-2): Grazia D. Raffa, Giorgia Siriaco, Simona Cugusi, Laura Ciapponi, Giovanni Cenci, Edward Wojcik, and Maurizio Gatti. The drosophila modigliani (moi) gene encodes a hoap-interacting protein required for telomere protection. Proceedings of the National Academy of Sciences, 106:2271-2276, Feb 2009. URL: https://doi.org/10.1073/pnas.0812702106, doi:10.1073/pnas.0812702106. This article has 91 citations and is from a highest quality peer-reviewed journal.

4. (raffa2011termininaprotein pages 2-3): Grazia D. Raffa, Laura Ciapponi, Giovanni Cenci, and Maurizio Gatti. Terminin: a protein complex that mediates epigenetic maintenance of drosophila telomeres. Nucleus, 2:383-391, Sep 2011. URL: https://doi.org/10.4161/nucl.2.5.17873, doi:10.4161/nucl.2.5.17873. This article has 107 citations and is from a peer-reviewed journal.

5. (zhang2016mtvanssdna pages 1-2): Yi Zhang, Liang Zhang, Xiaona Tang, Shilpa R. Bhardwaj, Jingyun Ji, and Yikang S. Rong. Mtv, an ssdna protecting complex essential for transposon-based telomere maintenance in drosophila. PLOS Genetics, 12:e1006435, Nov 2016. URL: https://doi.org/10.1371/journal.pgen.1006435, doi:10.1371/journal.pgen.1006435. This article has 39 citations and is from a domain leading peer-reviewed journal.

6. (gao2010hiphopinteractswith pages 1-2): Guanjun Gao, Jean-Claude Walser, Michelle L Beaucher, Patrizia Morciano, Natalia Wesolowska, Jie Chen, and Yikang S Rong. Hiphop interacts with hoap and hp1 to protect drosophila telomeres in a sequence‐independent manner. The EMBO Journal, 29:819-829, Feb 2010. URL: https://doi.org/10.1038/emboj.2009.394, doi:10.1038/emboj.2009.394. This article has 113 citations.

7. (saintleandre2020adaptiveevolutionof pages 4-5): Bastien Saint-Leandre, Courtney Christopher, and Mia T Levine. Adaptive evolution of an essential telomere protein restricts telomeric retrotransposons. eLife, Dec 2020. URL: https://doi.org/10.7554/elife.60987, doi:10.7554/elife.60987. This article has 29 citations and is from a domain leading peer-reviewed journal.

8. (raffa2011termininaprotein pages 3-5): Grazia D. Raffa, Laura Ciapponi, Giovanni Cenci, and Maurizio Gatti. Terminin: a protein complex that mediates epigenetic maintenance of drosophila telomeres. Nucleus, 2:383-391, Sep 2011. URL: https://doi.org/10.4161/nucl.2.5.17873, doi:10.4161/nucl.2.5.17873. This article has 107 citations and is from a peer-reviewed journal.

9. (saintleandre2020adaptiveevolutionof media 82aff822): Bastien Saint-Leandre, Courtney Christopher, and Mia T Levine. Adaptive evolution of an essential telomere protein restricts telomeric retrotransposons. eLife, Dec 2020. URL: https://doi.org/10.7554/elife.60987, doi:10.7554/elife.60987. This article has 29 citations and is from a domain leading peer-reviewed journal.

10. (on2023telomerecappingprotein pages 7-9): K On, Y Kato, and M Itoh. Telomere capping protein hoap is phosphorylated via the atm-nbs pathway following treatment with dsb inducing drugs in drosophila. Unknown journal, 2023.

11. (gao2010hiphopinteractswith pages 5-6): Guanjun Gao, Jean-Claude Walser, Michelle L Beaucher, Patrizia Morciano, Natalia Wesolowska, Jie Chen, and Yikang S Rong. Hiphop interacts with hoap and hp1 to protect drosophila telomeres in a sequence‐independent manner. The EMBO Journal, 29:819-829, Feb 2010. URL: https://doi.org/10.1038/emboj.2009.394, doi:10.1038/emboj.2009.394. This article has 113 citations.

12. (shareef2001drosophilaheterochromatinprotein pages 9-10): Mohammed Momin Shareef, Chadwick King, Mona Damaj, RamaKrishna Badagu, Da Wei Huang, and Rebecca Kellum. Drosophila heterochromatin protein 1 (hp1)/origin recognition complex (orc) protein is associated with hp1 and orc and functions in heterochromatin-induced silencing. Molecular biology of the cell, 12 6:1671-85, Jun 2001. URL: https://doi.org/10.1091/mbc.12.6.1671, doi:10.1091/mbc.12.6.1671. This article has 164 citations and is from a domain leading peer-reviewed journal.

13. (raffa2011termininaprotein pages 5-6): Grazia D. Raffa, Laura Ciapponi, Giovanni Cenci, and Maurizio Gatti. Terminin: a protein complex that mediates epigenetic maintenance of drosophila telomeres. Nucleus, 2:383-391, Sep 2011. URL: https://doi.org/10.4161/nucl.2.5.17873, doi:10.4161/nucl.2.5.17873. This article has 107 citations and is from a peer-reviewed journal.

14. (shareef2001drosophilaheterochromatinprotein pages 1-2): Mohammed Momin Shareef, Chadwick King, Mona Damaj, RamaKrishna Badagu, Da Wei Huang, and Rebecca Kellum. Drosophila heterochromatin protein 1 (hp1)/origin recognition complex (orc) protein is associated with hp1 and orc and functions in heterochromatin-induced silencing. Molecular biology of the cell, 12 6:1671-85, Jun 2001. URL: https://doi.org/10.1091/mbc.12.6.1671, doi:10.1091/mbc.12.6.1671. This article has 164 citations and is from a domain leading peer-reviewed journal.

15. (saintleandre2020adaptiveevolutionof pages 6-8): Bastien Saint-Leandre, Courtney Christopher, and Mia T Levine. Adaptive evolution of an essential telomere protein restricts telomeric retrotransposons. eLife, Dec 2020. URL: https://doi.org/10.7554/elife.60987, doi:10.7554/elife.60987. This article has 29 citations and is from a domain leading peer-reviewed journal.

16. (saintleandre2020adaptiveevolutionof pages 9-11): Bastien Saint-Leandre, Courtney Christopher, and Mia T Levine. Adaptive evolution of an essential telomere protein restricts telomeric retrotransposons. eLife, Dec 2020. URL: https://doi.org/10.7554/elife.60987, doi:10.7554/elife.60987. This article has 29 citations and is from a domain leading peer-reviewed journal.

17. (on2023telomerecappingprotein pages 1-2): K On, Y Kato, and M Itoh. Telomere capping protein hoap is phosphorylated via the atm-nbs pathway following treatment with dsb inducing drugs in drosophila. Unknown journal, 2023.

18. (lin2025rapidcompensatoryevolution pages 7-9): Sung-Ya Lin, Hannah R. Futeran, Briana N. Cruga, Andrew Santiago-Frangos, and Mia T. Levine. Rapid compensatory evolution within a multiprotein complex preserves telomere integrity. Science, 390:918-924, Nov 2025. URL: https://doi.org/10.1126/science.adv0657, doi:10.1126/science.adv0657. This article has 4 citations and is from a highest quality peer-reviewed journal.

19. (lin2024adaptiveproteincoevolution pages 6-9): Sung-Ya Lin, Hannah Futeran, and Mia T. Levine. Adaptive protein coevolution preserves telomere integrity. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.11.623029, doi:10.1101/2024.11.11.623029. This article has 1 citations.

20. (lin2025rapidcompensatoryevolution pages 6-7): Sung-Ya Lin, Hannah R. Futeran, Briana N. Cruga, Andrew Santiago-Frangos, and Mia T. Levine. Rapid compensatory evolution within a multiprotein complex preserves telomere integrity. Science, 390:918-924, Nov 2025. URL: https://doi.org/10.1126/science.adv0657, doi:10.1126/science.adv0657. This article has 4 citations and is from a highest quality peer-reviewed journal.

21. (lin2024adaptiveproteincoevolution pages 1-4): Sung-Ya Lin, Hannah Futeran, and Mia T. Levine. Adaptive protein coevolution preserves telomere integrity. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.11.623029, doi:10.1101/2024.11.11.623029. This article has 1 citations.

22. (lin2025rapidcompensatoryevolution pages 1-4): Sung-Ya Lin, Hannah R. Futeran, Briana N. Cruga, Andrew Santiago-Frangos, and Mia T. Levine. Rapid compensatory evolution within a multiprotein complex preserves telomere integrity. Science, 390:918-924, Nov 2025. URL: https://doi.org/10.1126/science.adv0657, doi:10.1126/science.adv0657. This article has 4 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](cav-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000028 I have extracted Figure 1, panels B and C, which show the fluorescence localization of Flag-tagged D. melanogaster HOAP[mel] and D.](cav-deep-research-falcon_artifacts/image-1.png)

## Citations

1. zhang2016mtvanssdna pages 1-2
2. lin2025rapidcompensatoryevolution pages 7-9
3. saintleandre2020adaptiveevolutionof pages 1-2
4. shareef2001drosophilaheterochromatinprotein pages 10-11
5. raffa2009thedrosophilamodigliani pages 1-2
6. raffa2011termininaprotein pages 2-3
7. gao2010hiphopinteractswith pages 1-2
8. saintleandre2020adaptiveevolutionof pages 4-5
9. raffa2011termininaprotein pages 3-5
10. on2023telomerecappingprotein pages 7-9
11. gao2010hiphopinteractswith pages 5-6
12. shareef2001drosophilaheterochromatinprotein pages 9-10
13. raffa2011termininaprotein pages 5-6
14. shareef2001drosophilaheterochromatinprotein pages 1-2
15. saintleandre2020adaptiveevolutionof pages 6-8
16. saintleandre2020adaptiveevolutionof pages 9-11
17. on2023telomerecappingprotein pages 1-2
18. lin2024adaptiveproteincoevolution pages 6-9
19. lin2025rapidcompensatoryevolution pages 6-7
20. lin2024adaptiveproteincoevolution pages 1-4
21. lin2025rapidcompensatoryevolution pages 1-4
22. mel
23. yak
24. Shareef et al., 2001
25. Gao et al., 2010
26. Raffa et al., 2011
27. Zhang et al., 2016
28. Saint-Leandre et al., 2020
29. On et al., 2023
30. Lin et al., 2024 preprint
31. Lin et al., 2025
32. Shareef *et al.*, *Molecular Biology of the Cell*, June 2001
33. Raffa *et al.*, *PNAS*, February 2009
34. Gao *et al.*, *EMBO Journal*, February 2010
35. Raffa *et al.*, *Nucleus* review, September 2011
36. Zhang *et al.*, *PLOS Genetics*, November 2016
37. Saint-Leandre *et al.*, *eLife*, December 2020
38. Lin *et al.*, bioRxiv preprint, November 11, 2024
39. Lin *et al.*, *Science*, November 2025
40. https://doi.org/10.1091/mbc.12.6.1671
41. https://doi.org/10.1038/emboj.2009.394
42. https://doi.org/10.4161/nucl.2.5.17873
43. https://doi.org/10.1371/journal.pgen.1006435
44. https://doi.org/10.7554/eLife.60987
45. https://www.jstage.jst.go.jp/browse/jibs/92/1/_contents
46. https://doi.org/10.1101/2024.11.11.623029
47. https://doi.org/10.1126/science.adv0657
48. https://doi.org/10.1073/pnas.0812702106
49. https://doi.org/10.7554/elife.60987,
50. https://doi.org/10.1091/mbc.12.6.1671,
51. https://doi.org/10.1073/pnas.0812702106,
52. https://doi.org/10.4161/nucl.2.5.17873,
53. https://doi.org/10.1371/journal.pgen.1006435,
54. https://doi.org/10.1038/emboj.2009.394,
55. https://doi.org/10.1126/science.adv0657,
56. https://doi.org/10.1101/2024.11.11.623029,