---
provider: cyberian
model: deep-research
cached: true
start_time: '2026-01-23T16:53:03.072021'
end_time: '2026-01-23T16:53:03.075046'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: POLDIP2
  gene_symbol: POLDIP2
  uniprot_accession: Q9Y2S7
  protein_description: 'RecName: Full=Polymerase delta-interacting protein 2 {ECO:0000303|PubMed:26984527};
    AltName: Full=38 kDa DNA polymerase delta interaction protein {ECO:0000303|PubMed:12522211};
    Short=p38 {ECO:0000303|PubMed:12522211}; Flags: Precursor;'
  gene_info: Name=POLDIP2 {ECO:0000303|PubMed:26984527, ECO:0000312|HGNC:HGNC:23781};
    Synonyms=PDIP38 {ECO:0000303|PubMed:12522211, ECO:0000303|PubMed:16428295}, POLD4;
    ORFNames=HSPC017;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: ApaG_domain. (IPR007474); ApaG_sf. (IPR036767); Hemimethylated_DNA-bd_dom.
    (IPR011722); Hemimethylated_DNA-bd_sf. (IPR036623); DUF525 (PF04379)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9Y2S7
- **Protein Description:** RecName: Full=Polymerase delta-interacting protein 2 {ECO:0000303|PubMed:26984527}; AltName: Full=38 kDa DNA polymerase delta interaction protein {ECO:0000303|PubMed:12522211}; Short=p38 {ECO:0000303|PubMed:12522211}; Flags: Precursor;
- **Gene Information:** Name=POLDIP2 {ECO:0000303|PubMed:26984527, ECO:0000312|HGNC:HGNC:23781}; Synonyms=PDIP38 {ECO:0000303|PubMed:12522211, ECO:0000303|PubMed:16428295}, POLD4; ORFNames=HSPC017;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ApaG_domain. (IPR007474); ApaG_sf. (IPR036767); Hemimethylated_DNA-bd_dom. (IPR011722); Hemimethylated_DNA-bd_sf. (IPR036623); DUF525 (PF04379)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "POLDIP2" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'POLDIP2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **POLDIP2** (gene ID: POLDIP2, UniProt: Q9Y2S7) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# POLDIP2 (Polymerase Delta-Interacting Protein 2): A Comprehensive Functional Review

## Introduction

Polymerase delta-interacting protein 2 (POLDIP2), also known as PDIP38 (polymerase delta-interacting protein of 38 kDa), is a multifunctional adaptor protein that has emerged as a central nexus connecting genome stability, redox metabolism, and mitochondrial function in metazoan cells. Originally identified in 2003 through a yeast two-hybrid screen as an interacting partner of the p50 subunit of DNA polymerase delta and proliferating cell nuclear antigen (PCNA)[liu-2003-pdip38-discovery-abstract], the biological roles of POLDIP2 have expanded dramatically over the subsequent two decades. The protein has since been implicated in DNA damage tolerance through translesion synthesis, regulation of NADPH oxidase activity and reactive oxygen species production, mitochondrial protein quality control, metabolic adaptation to hypoxia, and regulation of the cytoskeleton[hernandes-2017-review-fulltext]. This review synthesizes current understanding of POLDIP2 molecular function, subcellular localization, pathway involvement, and physiological significance based on the primary scientific literature.

POLDIP2 is encoded by a gene on human chromosome 17q11.2 and is highly conserved throughout metazoans, though notably absent in prokaryotes, plants, and fungi[hernandes-2017-review-fulltext]. The conservation pattern suggests that POLDIP2 evolved through fusion of ancestral bacterial genes during the opisthokont radiation, likely after the Ichthyosporea split from the lineage leading to metazoans[kulik-2021-structure-abstract]. The essential nature of this protein is underscored by the observation that homozygous deletion in mice results in perinatal lethality, with only 3% of expected knockout animals surviving to birth[amanso-2014-knockout-abstract].

## Protein Structure and Domain Architecture

POLDIP2 is translated as a 368-amino acid, 42 kDa protein that can be post-translationally processed to a 37 kDa form through cleavage of an N-terminal mitochondrial targeting sequence[hernandes-2017-review-fulltext]. The mature protein comprises two conserved globular domains connected by an alpha-helical linker region: an N-terminal YccV-like domain and a C-terminal DUF525 (Domain of Unknown Function 525) domain[kulik-2021-structure-abstract][strack-2020-clpxp-abstract].

The crystal structure of human POLDIP2 (residues 51-368) was determined at 2.8 Angstrom resolution and deposited in the Protein Data Bank (PDB: 6Z9C)[kulik-2021-structure-abstract]. This structure reveals a compact, beta-strand-rich globular architecture with the two domains positioned in close proximity through the conserved interdomain linker. The N-terminal (YccV-like) domain (residues 67-200) adopts an SH3-like beta-barrel fold, while the C-terminal (DUF525) domain (residues 233-368) forms an immunoglobulin-like beta-sandwich structure[kulik-2021-structure-abstract][strack-2020-clpxp-abstract].

A notable structural feature is an internal cavity or channel traversing the protein at the interface between the extended YccV and DUF525 domains. This channel is approximately 6.5 Angstroms wide and is lined with predominantly hydrophilic residues[kulik-2021-structure-abstract]. Within this channel, cysteine 266 displays anomalous electron density suggestive of an oxidized or otherwise modified state, raising the possibility that POLDIP2 may function as a redox sensor capable of conformational switching in response to the cellular oxidative environment[kulik-2021-structure-abstract]. Molecular dynamics simulations reveal that the N-terminal region preceding the YccV domain is highly dynamic, providing conformational flexibility that likely facilitates interactions with the protein's many diverse binding partners[kulik-2021-structure-abstract].

The YccV-like domain contains three potential PCNA-interacting protein (PIP) box motifs, with one (PIP2) located on a flexible loop and therefore accessible for PCNA binding[kulik-2021-structure-abstract]. The evolutionary origin of this domain traces to bacterial YccV (HspQ) proteins that bind hemimethylated DNA and regulate gene expression. The DUF525 domain shares homology with bacterial ApaG proteins and contains conserved motifs found in NAD- and FAD-binding proteins involved in binding the ADP moiety[liu-2003-pdip38-discovery-abstract][hernandes-2017-review-fulltext]. The C-terminal DUF525 domain harbors a highly conserved putative substrate binding pocket that is implicated in recognizing target proteins for delivery to the CLPXP protease[strack-2020-clpxp-abstract].

## Subcellular Localization

POLDIP2 exhibits complex and cell-type-dependent subcellular localization patterns that reflect its multifunctional nature. The protein has been identified in the nucleus, mitochondrial matrix, cytoplasm, and plasma membrane, with distribution influenced by cell proliferation state and interactions with cell adhesion receptors[hernandes-2017-review-fulltext].

In vascular smooth muscle cells, POLDIP2 localizes prominently to focal adhesions and stress fibers, consistent with its roles in regulating cytoskeletal dynamics and NADPH oxidase 4 (Nox4) activity at these sites[lyle-2009-nox4-abstract]. Cell fractionation experiments across multiple cell types consistently demonstrate that the majority of POLDIP2 distributes to the mitochondrial fraction, with only a minor proportion detected in the nucleus[hernandes-2017-review-fulltext]. However, in certain cell types including rat bladder carcinoma NBT-II cells, intestinal epithelial IEC18 cells, rat brain endothelial cells, and HeLa cells, POLDIP2 does not localize to mitochondria[hernandes-2017-review-fulltext], highlighting the context-dependent nature of its distribution.

Mitochondrial targeting of POLDIP2 occurs in a membrane potential-dependent manner, and within mitochondria the protein resides in the matrix compartment where it colocalizes with its partner protein CLPX[strack-2020-clpxp-abstract]. The full-length 42 kDa form contains the mitochondrial targeting sequence, while cleavage of this sequence during or after mitochondrial import yields the 37 kDa form. Whether these two forms have distinct functional roles remains an important unresolved question[hernandes-2017-review-fulltext]. Notably, the N-terminal region required for interaction with PrimPol overlaps with the mitochondrial targeting sequence, and truncated POLDIP2 lacking the first 50 amino acids fails to stimulate PrimPol DNA polymerase activity, suggesting that the mitochondrial form may not regulate PrimPol function[guilliam-2016-primpol-abstract].

## DNA Replication and Damage Tolerance Functions

### Interaction with DNA Polymerase Delta and PCNA

POLDIP2 was originally identified through its physical association with the p50 subunit of DNA polymerase delta (encoded by POLD2), one of the core subunits of the replicative DNA polymerase[liu-2003-pdip38-discovery-abstract]. The interaction was demonstrated through multiple biochemical approaches including yeast two-hybrid analysis, GST pull-down assays, coimmunoprecipitation from calf thymus tissue and mammalian cell extracts, immunoaffinity chromatography, and native gel electrophoresis[liu-2003-pdip38-discovery-abstract]. POLDIP2 also directly interacts with PCNA, the DNA sliding clamp that serves as an essential processivity factor for DNA polymerase delta, suggesting that POLDIP2 may function as an integral component of the DNA replication machinery[liu-2003-pdip38-discovery-abstract][hernandes-2017-review-fulltext].

Biochemical studies demonstrate that POLDIP2 stimulates the DNA polymerase activity of Pol delta without affecting its fidelity[maga-2013-pol-lambda-abstract]. This enhancement of polymerase activity, combined with simultaneous interactions with PCNA and specialized translesion synthesis polymerases, positions POLDIP2 as a coordinator of polymerase switching events at sites of DNA damage.

### Translesion Synthesis and DNA Damage Tolerance

One of the most well-characterized molecular functions of POLDIP2 is its role in DNA damage tolerance through regulation of translesion synthesis (TLS). When replicative DNA polymerases encounter lesions in template DNA strands, cells employ two principal strategies to restore stalled replication forks: error-prone translesion DNA synthesis by specialized DNA polymerases, and error-free template switching involving homologous recombination with the sister chromatid[tissier-2019-tls-vs-ts-abstract].

POLDIP2 physically associates with multiple TLS polymerases including DNA polymerase eta (Pol eta), DNA polymerase lambda (Pol lambda), DNA polymerase zeta (Pol zeta), Rev1, and the primase-polymerase PrimPol[hernandes-2017-review-fulltext][guilliam-2016-primpol-abstract][maga-2013-pol-lambda-abstract]. Yeast two-hybrid experiments confirmed direct interactions between POLDIP2 and Pol eta, Pol zeta, and Rev1[tissier-2019-tls-vs-ts-abstract]. Purified POLDIP2 stimulates TLS activity of Pol lambda and PrimPol in vitro through enhancement of DNA binding, processivity, and catalytic efficiency[maga-2013-pol-lambda-abstract][guilliam-2016-primpol-abstract].

The interaction between POLDIP2 and PrimPol has been particularly well characterized. PrimPol is a specialized enzyme possessing both primase and DNA polymerase activities involved in DNA damage tolerance and mitochondrial DNA maintenance[guilliam-2016-primpol-abstract]. POLDIP2 increases PrimPol's polymerase activity in a dose-dependent manner by enhancing DNA binding affinity and processivity[guilliam-2016-primpol-abstract]. Processivity measurements show that POLDIP2 extends PrimPol products from approximately 4 nucleotides to over 16 nucleotides per binding event, representing greater than a 4-fold improvement[guilliam-2016-primpol-abstract]. Cross-linking mass spectrometry revealed that POLDIP2's N-terminus (residues 1-8) mediates interaction with PrimPol's catalytic domain around amino acid positions 60-70, a region showing strong homology to Pol eta's POLDIP2-binding region[guilliam-2016-primpol-abstract]. Importantly, POLDIP2 also acts as a fidelity factor for PrimPol during bypass of 8-oxoguanine (8-oxoG) lesions, enhancing error-free dCTP incorporation opposite this common oxidative DNA lesion[guilliam-2016-primpol-abstract].

For DNA polymerase lambda, POLDIP2 similarly functions as a processivity factor specifically during 8-oxoG bypass[maga-2013-pol-lambda-abstract]. The physical interaction between POLDIP2 and Pol lambda increases both processivity and catalytic efficiency of error-free lesion bypass. POLDIP2 additionally stimulates Pol lambda and Pol eta-mediated bypass of other common DNA lesions including abasic sites and cyclobutane thymine dimers[maga-2013-pol-lambda-abstract]. Notably, POLDIP2 does not stimulate DNA polymerases beta or iota, indicating specificity in its regulatory effects[maga-2013-pol-lambda-abstract].

Cellular evidence supports the physiological importance of these biochemical activities. Depletion of POLDIP2 in human cells causes decreased replication fork rates following UV irradiation, similar to the phenotype observed in PrimPol-knockout cells[guilliam-2016-primpol-abstract]. Critically, depleting POLDIP2 in PrimPol-knockout cells does not produce a further decrease in fork rates, demonstrating that these proteins function epistatically in the same pathway[guilliam-2016-primpol-abstract]. POLDIP2 silencing also increases cellular sensitivity to oxidative stress, an effect potentiated in a Pol lambda-deficient background[maga-2013-pol-lambda-abstract].

### Regulation of TLS versus Template Switching

Beyond activating individual TLS polymerases, POLDIP2 plays a broader regulatory role in determining the balance between translesion synthesis and template switching pathways. Studies in chicken DT40 B lymphocytes and human cell lines demonstrate that PDIP38/POLDIP2 shifts the DNA damage tolerance pathway balance toward TLS and away from template switching[tissier-2019-tls-vs-ts-abstract].

Disruption of PDIP38 in DT40 cells caused a three-fold decrease in TLS-mediated immunoglobulin V gene hypermutation while simultaneously increasing template switching frequency through immunoglobulin gene conversion[tissier-2019-tls-vs-ts-abstract]. Sister chromatid exchange analysis revealed that loss of PDIP38 increased UV-induced SCE by more than 50% in both chicken and human cell lines, indicating enhanced reliance on homologous recombination-based mechanisms[tissier-2019-tls-vs-ts-abstract]. Using a transposon-based assay system with integrated UV damage, researchers found that PDIP38-deficient cells showed a significant increase in the relative usage of template switching, from approximately 5% to 13-26%[tissier-2019-tls-vs-ts-abstract].

Rather than simply activating TLS polymerases, POLDIP2 appears to suppress template switching pathways, thereby increasing the relative contribution of translesion synthesis to overall damage tolerance without necessarily enhancing total cellular resistance to DNA-damaging agents[tissier-2019-tls-vs-ts-abstract]. This regulatory function may explain why both excessive and insufficient POLDIP2 levels can be detrimental to cells[hernandes-2017-review-fulltext].

## NADPH Oxidase Regulation and Redox Signaling

### Discovery as a Nox4 Activator

A major functional role for POLDIP2 outside of DNA metabolism was discovered through a yeast two-hybrid screen using the C-terminal tail of p22phox as bait against a vascular smooth muscle cell cDNA library[lyle-2009-nox4-abstract]. This screen identified POLDIP2 as a novel p22phox binding partner. p22phox is an essential membrane-associated subunit of the NADPH oxidase (Nox) complex that is required for the stability and activity of several Nox isoforms including Nox1, Nox2, Nox3, and Nox4[lyle-2009-nox4-abstract].

Biochemical validation confirmed that POLDIP2 associates with p22phox, Nox1, and Nox4 and colocalizes with p22phox at sites of Nox4 localization including focal adhesions, stress fibers, and nuclear compartments[lyle-2009-nox4-abstract]. GST-pulldown assays demonstrated that radiolabeled POLDIP2 binds to GST-p22phox fusion proteins, and coimmunoprecipitation studies showed that endogenous POLDIP2 associates with p22phox in cells. The interaction of tagged POLDIP2 with Nox4 requires p22phox, as POLDIP2 coimmunoprecipitates with Nox4 in control cells but not in cells lacking p22phox[lyle-2009-nox4-abstract].

### Functional Effects on Nox4 Activity

POLDIP2 substantially enhances Nox4 enzymatic activity. Overexpression of POLDIP2 increases Nox4-dependent reactive oxygen species production by approximately 3-fold[lyle-2009-nox4-abstract]. POLDIP2 positively regulates basal ROS production in vascular smooth muscle cells, with superoxide (O2-) increased by 86.3 +/- 15.6% and hydrogen peroxide (H2O2) increased by 40.7 +/- 4.5%[lyle-2009-nox4-abstract]. This effect is Nox4-dependent, as it is blocked when Nox4 is depleted by siRNA[lyle-2009-nox4-abstract]. Conversely, knockdown of POLDIP2 decreases both superoxide and hydrogen peroxide production[lyle-2009-nox4-abstract].

In vivo validation comes from studies of Poldip2 heterozygous mice (homozygous deletion being perinatally lethal). These animals show significantly decreased NADPH-dependent production of both O2- and H2O2 in the vasculature, confirming that POLDIP2 contributes to Nox4 activity in vivo[sutliff-2013-vascular-abstract]. The H2O2 produced through the POLDIP2-Nox4 pathway appears to serve important signaling functions, as supplementing cultured vascular smooth muscle cells from Poldip2+/- mice with H2O2 normalizes their extracellular matrix production[sutliff-2013-vascular-abstract].

### Downstream Effects on Cell Signaling and Cytoskeleton

POLDIP2-Nox4-dependent ROS production has important downstream consequences for cell signaling and cytoskeletal organization. Overexpression of POLDIP2 activates Rho GTPase by approximately 180%, strengthens focal adhesions, and increases stress fiber formation[lyle-2009-nox4-abstract]. These phenotypic changes are blocked by dominant negative Rho, demonstrating that Rho activation lies downstream of POLDIP2-Nox4 signaling. Conversely, depletion of either POLDIP2 or Nox4 results in loss of focal adhesion and stress fiber structures, which can be rescued by expression of constitutively active Rho[lyle-2009-nox4-abstract].

More recent work has elucidated a specific mechanism by which the NOX4-POLDIP2 complex regulates cytoskeletal dynamics through direct oxidation of filamentous actin[cheng-2018-nox4-actin-abstract]. During integrin-mediated cell adhesion, F-actin undergoes oxidation through sulfenylation, with a peak occurring approximately 3 hours after cell attachment[cheng-2018-nox4-actin-abstract]. This oxidation is enhanced by POLDIP2 overexpression and inhibited by approximately 78-99% upon depletion of POLDIP2 or NOX4, or by scavenging H2O2 with catalase[cheng-2018-nox4-actin-abstract]. Silencing of POLDIP2 or NOX4 impairs the interaction between actin and vinculin, disturbing focal adhesion maturation and inhibiting cell migration[cheng-2018-nox4-actin-abstract]. Thus, integrin engagement activates the POLDIP2-Nox4 complex to oxidize actin, which modulates focal adhesion assembly.

### Cell Migration Effects

Both overexpression and depletion of POLDIP2 block PDGF-induced vascular smooth muscle cell migration, indicating that optimal POLDIP2 levels are critical for normal cell motility[lyle-2009-nox4-abstract][hernandes-2017-review-fulltext]. Excessive POLDIP2 appears to prevent focal adhesion dissolution required for cell movement, while insufficient POLDIP2 prevents focal adhesion formation in the first place[hernandes-2017-review-fulltext]. This biphasic effect suggests that POLDIP2 may be a therapeutic target for vascular pathologies involving abnormal smooth muscle cell migration, such as restenosis and atherosclerosis[lyle-2009-nox4-abstract].

### Differential Regulation of Nox Isoforms

Interestingly, POLDIP2's effects on different NADPH oxidase isoforms appear to be divergent. While POLDIP2 positively regulates Nox4 activity, studies on phagocyte NADPH oxidase 2 (Nox2) revealed an opposite effect[hernandes-2017-review-fulltext]. Using membranes from circulating resting neutrophils, ROS production by Nox2 was down-regulated approximately 2.5-fold by POLDIP2[hernandes-2017-review-fulltext]. This inhibitory effect on Nox2 appears to be mediated through interaction with p47phox rather than p22phox, representing a novel regulatory mechanism. These findings suggest that POLDIP2 could act as a tunable switch capable of differentially regulating NADPH oxidase isoforms, potentially orchestrating the level and type of ROS generated by different Nox enzymes in cells[hernandes-2017-review-fulltext].

## Mitochondrial Functions

### CLPXP Protease Adaptor

A major advance in understanding POLDIP2's mitochondrial functions came with the identification of POLDIP2/PDIP38 as the first mammalian adaptor protein for the mitochondrial AAA+ protease CLPXP[strack-2020-clpxp-abstract]. CLPXP is a conserved ATP-dependent protease consisting of CLPX, an AAA+ unfoldase that recognizes and unfolds target proteins, and CLPP, a serine protease that degrades the unfolded substrates[strack-2020-clpxp-abstract]. AAA+ proteases in bacteria use specialized cofactors called adaptor proteins to alter substrate recognition and specificity, but prior to the characterization of PDIP38, no such adaptor had been identified in mammalian mitochondria.

Human PDIP38 resides in the mitochondrial matrix where it colocalizes with CLPX[strack-2020-clpxp-abstract]. The N-terminal YccV-like domain of PDIP38 specifically interacts with CLPX through the adaptor docking loop within CLPX's N-terminal zinc binding domain[strack-2020-clpxp-abstract]. This interaction has multiple functional consequences: PDIP38 modulates the substrate specificity of CLPXP in vitro, and perhaps equally importantly, protects CLPX from degradation by the mitochondrial LON protease, thereby stabilizing cellular CLPX levels[strack-2020-clpxp-abstract].

### Regulation of Lipoylation and Metabolic Adaptation

One of the most physiologically significant mitochondrial functions of POLDIP2 is its regulation of protein lipoylation and consequently of key TCA cycle enzymes[amanso-2018-lipoylation-abstract]. Lipoic acid is an essential cofactor for several mitochondrial enzyme complexes including pyruvate dehydrogenase (PDH) and alpha-ketoglutarate dehydrogenase (alphaKGDH), where it is covalently attached to lysine residues of the E2 subunits (DLAT and DLST, respectively).

POLDIP2 regulates lipoylation through a pathway involving CLPXP and the lipoic acid-activating enzyme ACSM1[amanso-2018-lipoylation-abstract]. When POLDIP2 levels are normal, it binds to CLPX and restrains CLPXP protease activity toward ACSM1. When POLDIP2 levels decrease, CLPXP becomes active and degrades ACSM1. Without ACSM1, lipoyl-AMP cannot be synthesized, preventing LIPT1 from transferring lipoyl groups to DLAT and DLST. The resulting decrease in PDH and alphaKGDH lipoylation inhibits these TCA cycle enzymes, suppressing mitochondrial respiration and reducing cellular alpha-ketoglutarate levels[amanso-2018-lipoylation-abstract].

Cells deficient in POLDIP2 show significantly reduced levels of lipoyl-DLAT and lipoyl-DLST, with corresponding decreases in PDH and alphaKGDH enzymatic activities[amanso-2018-lipoylation-abstract]. Importantly, forced expression of ACSM1 in POLDIP2-deficient cells rescues lipoylation levels, confirming that ACSM1 is the critical intermediate[amanso-2018-lipoylation-abstract].

This mechanism has important implications for cellular adaptation to hypoxia and cancer metabolism. POLDIP2 expression is down-regulated by hypoxia across multiple cell types, triggering the lipoylation deficit and subsequent inhibition of PDH and alphaKGDH[amanso-2018-lipoylation-abstract]. This metabolic rewiring contributes to HIF-1alpha stabilization through inhibition of alpha-ketoglutarate-dependent prolyl hydroxylases. Triple-negative breast cancer (TNBC) cells exhibit basal suppression of POLDIP2 and complete inhibition of DLAT/DLST lipoylation. Restoring POLDIP2 expression in TNBC cells increases mitochondrial respiration and reduces cancer cell growth rate[amanso-2018-lipoylation-abstract], suggesting a tumor suppressive role in some contexts.

### Heme Biosynthesis Regulation

More recently, POLDIP2 has been identified as a heme-sensing adaptor that delivers aminolevulinic acid synthase (ALAS) for degradation by CLPXP[hernandes-2017-review-fulltext]. ALAS catalyzes the first and rate-limiting step of heme biosynthesis in mitochondria. By serving as an adaptor that responds to heme levels, POLDIP2 participates in feedback regulation of heme biosynthesis, linking POLDIP2 function to porphyria-related disorders caused by CLPX mutations[hernandes-2017-review-fulltext].

## Vascular and Cardiovascular Phenotypes

Studies in Poldip2-deficient mice have revealed important roles for this protein in vascular structure and function. Because complete Poldip2 deletion is perinatally lethal (with only about 3% of expected homozygous knockout animals surviving to birth), most in vivo studies have utilized heterozygous animals with approximately 50% reduced protein levels[sutliff-2013-vascular-abstract][amanso-2014-knockout-abstract].

Poldip2 heterozygous mice show multiple vascular abnormalities[sutliff-2013-vascular-abstract]. Their aortas exhibit disordered and fragmented elastic lamellae when examined by transmission electron microscopy, along with excessive extracellular matrix deposition[sutliff-2013-vascular-abstract]. Vascular smooth muscle cells isolated from these animals secrete elevated levels of collagen I, an effect that can be normalized by supplementing culture medium with hydrogen peroxide[sutliff-2013-vascular-abstract]. This suggests that POLDIP2-Nox4-derived H2O2 normally suppresses excessive extracellular matrix production[sutliff-2013-vascular-abstract].

Functionally, aortas from Poldip2+/- mice show impaired contractile responses to both phenylephrine and potassium chloride stimulation, with maximal force reduced by approximately 48% and 44% respectively[sutliff-2013-vascular-abstract]. The combination of structural abnormalities (fragmented elastic lamellae, excess collagen) and decreased contractility results in increased arterial stiffness[sutliff-2013-vascular-abstract][hernandes-2017-review-fulltext]. Paradoxically, these structural changes may provide protection in certain disease contexts: Poldip2+/- mice demonstrate resistance to experimental aortic dilatation induced by calcium chloride treatment[sutliff-2013-vascular-abstract], and heterozygous animals show protection against injury-induced neointimal hyperplasia[hernandes-2017-review-fulltext].

POLDIP2 also promotes ischemia-induced collateral vessel formation, with heterozygous deletion impairing revascularization following femoral artery ligation[hernandes-2017-review-fulltext]. This suggests that appropriate POLDIP2 levels are required for adaptive angiogenesis.

## Cell Cycle, Proliferation, and Mitotic Spindle Function

Poldip2 knockout mouse embryonic fibroblasts (MEFs) exhibit markedly reduced cellular growth rates[amanso-2014-knockout-abstract]. These cells show cell cycle arrest or delay in both G1 and G2/M phases, accompanied by decreased expression of cell cycle regulators cdk1 and Cyclin A2[amanso-2014-knockout-abstract][hernandes-2017-review-fulltext]. Additionally, Poldip2 knockout increases markers of autophagy in MEFs[amanso-2014-knockout-abstract], potentially as a compensatory response to metabolic dysfunction.

Beyond its roles during interphase, POLDIP2 also functions during mitosis. Studies using immunofluorescence microscopy demonstrated that PDIP38 localizes to the mitotic spindle throughout all stages of mitosis[klaile-2008-spindle-abstract]. Functional experiments using anti-PDIP38 antibody microinjection and siRNA silencing revealed that loss of PDIP38 function causes defects in spindle organization, aberrant chromosome segregation, and the formation of multinucleated cells[klaile-2008-spindle-abstract]. These findings indicate that PDIP38 plays distinct roles at different stages of the cell cycle: during S phase it facilitates DNA replication and damage tolerance, while during M phase it contributes to proper mitotic spindle organization and accurate chromosome segregation[klaile-2008-spindle-abstract].

The mechanisms underlying the proliferation defects observed in POLDIP2-deficient cells likely involve multiple functions: the DNA damage tolerance activities (required for efficient progression through S phase), the mitotic spindle organization function (required for accurate chromosome segregation), and the metabolic functions (required for mitochondrial ATP production). The observation that POLDIP2 depletion increases cell sensitivity to oxidative stress[maga-2013-pol-lambda-abstract] suggests that accumulation of unrepaired oxidative DNA damage may also contribute to the proliferation defect.

## RNA Splicing and Alternative Splicing Regulation

An unexpected function for POLDIP2/PDIP38 emerged from studies examining its nuclear localization in response to DNA damage. While PDIP38 was expected to localize to UV-induced DNA repair foci given its established roles in translesion synthesis, researchers observed that in certain cell lines (HeLa and A549), UV irradiation instead triggers PDIP38 translocation to nuclear speckles where it colocalizes with the spliceosome marker SC35[wong-2013-splicing-abstract].

Nuclear speckles are subnuclear domains enriched in pre-mRNA splicing factors and serve as storage and assembly sites for the splicing machinery. The functional significance of PDIP38 localization to these structures was demonstrated by examining alternative splicing of MDM2, a key p53 regulator. UV treatment normally induces alternative splicing of MDM2, generating splice variants that affect p53 regulation and DNA damage responses. Cells expressing shRNA targeting PDIP38 showed greatly reduced UV-induced MDM2 alternative splicing, establishing that PDIP38 is required for this stress-induced splicing response[wong-2013-splicing-abstract]. Similar PDIP38 translocation and splicing effects occurred when cells were treated with the transcription inhibitors actinomycin D or alpha-amanitin, suggesting that PDIP38 responds broadly to transcriptional stress[wong-2013-splicing-abstract].

This splicing function appears to be cell-type specific: in MRC-5 fibroblasts, PDIP38 localizes to UV repair foci consistent with its translesion synthesis role, while in HeLa and A549 cells it preferentially translocates to spliceosomes[wong-2013-splicing-abstract]. This context-dependent behavior exemplifies the moonlighting nature of POLDIP2 and raises questions about how cells regulate the partitioning of this protein among its various functional compartments.

## Neurological Functions and Disease Associations

POLDIP2 has been implicated in several neurological contexts, though some findings remain controversial. Studies in neuronal cell lines demonstrated that POLDIP2 expression is increased in response to multiple stress signals including amyloid-beta (Abeta), TNF-alpha, and hydrogen peroxide[kim-2015-tau-abstract]. Importantly, POLDIP2 was identified through cDNA library screening as a factor that promotes Tau aggregation. Ectopic expression of POLDIP2 enhanced Tau aggregate formation without affecting Tau phosphorylation, while POLDIP2 knockdown alleviated ROS-induced Tau aggregation[kim-2015-tau-abstract]. Mechanistically, POLDIP2 overexpression impaired both autophagy and proteasome activities, with these effects mapping to the DUF525 domain[kim-2015-tau-abstract].

In vivo validation came from Drosophila models of tauopathy. Knockdown of the Drosophila POLDIP2 homolog (CG12162) attenuated the rough eye phenotype induced by human Tau overexpression and extended the lifespan of flies expressing disease-associated Tau(R406W)[kim-2015-tau-abstract]. These findings suggest that POLDIP2 inhibition might be neuroprotective in tauopathies.

However, some reports have suggested opposite effects. siRNA against Poldip2 was reported to alleviate H2O2-induced Tau aggregation in SH-SY5Y human neuroblastoma cells[hernandes-2017-review-fulltext], consistent with a pro-aggregation role. Conversely, other in vitro studies found that purified PolDIP2 actually inhibits Tau oligomer and fibril formation in biochemical assays[hernandes-2017-review-fulltext]. These apparently contradictory findings may reflect different experimental systems (cellular versus cell-free), the complex relationship between POLDIP2's effects on protein quality control pathways versus direct protein-protein interactions, or context-dependent functions.

In cerebrovascular disease, Poldip2 heterozygous mice exhibited significantly decreased Evans blue dye extravasation following cerebral ischemia, indicating reduced blood-brain barrier permeability and improved survival[hernandes-2017-review-fulltext]. This protective effect in heterozygotes likely relates to the reduced Nox4-dependent ROS production, suggesting that POLDIP2 inhibition might be beneficial in ischemic stroke through reduction of oxidative stress at the blood-brain barrier.

## Open Questions

Despite significant progress in understanding POLDIP2 biology, several important questions remain unresolved.

First, the relative importance of POLDIP2's diverse functions in different physiological and pathological contexts is unclear. The protein has documented roles in at least three major cellular compartments (nucleus, mitochondria, cytoplasm/focal adhesions), and the phenotypes of Poldip2-deficient cells and organisms likely reflect the combined loss of multiple functions. Tissue-specific and inducible knockout models, along with structure-function studies using domain-specific mutations, will be needed to dissect the individual contributions.

Second, the functional relationship between the 42 kDa and 37 kDa forms of POLDIP2 remains undefined. Whether these forms have distinct interaction partners and functions, and how the balance between them is regulated, are important open questions[hernandes-2017-review-fulltext]. The observation that the N-terminal region required for PrimPol interaction overlaps with the mitochondrial targeting sequence suggests that the nuclear and mitochondrial forms may have non-overlapping functions[guilliam-2016-primpol-abstract].

Third, how POLDIP2 localization is regulated in response to cellular conditions (proliferation state, oxidative stress, DNA damage) requires further investigation. The finding that POLDIP2 contains a potential redox-sensing cysteine residue within an internal channel[kulik-2021-structure-abstract] raises the possibility of direct redox regulation, but this remains to be demonstrated functionally.

Fourth, the relationship between POLDIP2's role in DNA damage tolerance and cancer remains complex. On one hand, POLDIP2 promotes error-prone translesion synthesis which could contribute to mutagenesis; on the other hand, low POLDIP2 in triple-negative breast cancer cells contributes to metabolic dysfunction that may promote tumor growth[amanso-2018-lipoylation-abstract]. Expression correlation studies have yielded mixed results, with some reports showing correlation with breast cancer tumors and others showing inverse correlation with lung cancer risk[hernandes-2017-review-fulltext].

Fifth, the transcriptional regulation of POLDIP2 and the mechanisms controlling its expression in response to hypoxia and other stresses are poorly characterized. Understanding these regulatory pathways will be important for evaluating POLDIP2 as a potential therapeutic target.

Finally, POLDIP2 interacts with over 40 documented protein partners[hernandes-2017-review-fulltext], and this interaction network is likely incomplete. How these numerous interactions are coordinated spatially and temporally, and whether POLDIP2 functions as a signaling hub that integrates information from multiple pathways, represents an exciting area for future investigation.

## References

1. **liu-2003-pdip38-discovery-abstract**: Liu L, Rodriguez-Belmonte EM, Mazloum N, Xie B, Lee MY. (2003) Identification of a novel protein, PDIP38, that interacts with the p50 subunit of DNA polymerase delta and proliferating cell nuclear antigen. *J Biol Chem* 278(12):10041-10047. PMID: 12522211. DOI: 10.1074/jbc.M208694200

2. **hernandes-2017-review-fulltext**: Hernandes MS, Lassegue B, Griendling KK. (2017) Polymerase delta-interacting protein 2: a multifunctional protein. *J Cardiovasc Pharmacol* 69(6):335-342. PMID: 28574953. PMCID: PMC5556945. DOI: 10.1097/FJC.0000000000000465

3. **lyle-2009-nox4-abstract**: Lyle AN, Deshpande NN, Taniyama Y, Seidel-Rogol B, Pounkova L, Du P, Papaharalambus C, Lassegue B, Griendling KK. (2009) Poldip2, a novel regulator of Nox4 and cytoskeletal integrity in vascular smooth muscle cells. *Circ Res* 105(3):249-259. PMID: 19574552. PMCID: PMC2744198. DOI: 10.1161/CIRCRESAHA.109.193722

4. **guilliam-2016-primpol-abstract**: Guilliam TA, Bailey LJ, Brissett NC, Doherty AJ. (2016) PolDIP2 interacts with human PrimPol and enhances its DNA polymerase activities. *Nucleic Acids Res* 44(7):3317-3329. PMID: 26984527. PMCID: PMC4838387. DOI: 10.1093/nar/gkw175

5. **maga-2013-pol-lambda-abstract**: Maga G, Villani E, Locatelli GA, Crespan E, Shevelev I, Jiricny J, Hubscher U. (2013) DNA polymerase delta-interacting protein 2 is a processivity factor for DNA polymerase lambda during 8-oxo-7,8-dihydroguanine bypass. *Proc Natl Acad Sci USA* 110(47):18850-18855. PMID: 24191025. PMCID: PMC3839753. DOI: 10.1073/pnas.1308760110

6. **sutliff-2013-vascular-abstract**: Sutliff RL, Hilenski J, Amanso DB, et al. (2013) Polymerase delta interacting protein 2 sustains vascular structure and function. *Arterioscler Thromb Vasc Biol* 33(9):2154-2161. PMID: 23825363. PMCID: PMC3837414. DOI: 10.1161/ATVBAHA.113.301913

7. **kulik-2021-structure-abstract**: Kulik AA, Maruszczak KK, Thomas DC, Nabi-Aldridge NLA, Carr M, Bingham RJ, Cooper CDO. (2021) Crystal structure and molecular dynamics of human POLDIP2, a multifaceted adaptor protein in metabolism and genome stability. *Protein Sci* 30(6):1196-1209. PMID: 33884680. PMCID: PMC8138528. DOI: 10.1002/pro.4085. PDB: 6Z9C

8. **strack-2020-clpxp-abstract**: Strack PR, Brodie EJ, Zhan H, et al. (2020) Polymerase delta-interacting protein 38 (PDIP38) modulates the stability and activity of the mitochondrial AAA+ protease CLPXP. *Commun Biol* 3(1):666. PMID: 33184454. PMCID: PMC7665182. DOI: 10.1038/s42003-020-01358-6

9. **amanso-2014-knockout-abstract**: Amanso DB, Seidel-Rogol SS, Griendling KK. (2014) Poldip2 knockout results in perinatal lethality, reduced cellular growth and increased autophagy of mouse embryonic fibroblasts. *PLOS ONE* 9(5):e96657. PMID: 24797518. PMCID: PMC4010529. DOI: 10.1371/journal.pone.0096657

10. **amanso-2018-lipoylation-abstract**: Amanso DB, Seidel-Rogol SS, Shao Y, Bhayani I, San Martin A, Griendling KK. (2018) Poldip2 is an oxygen-sensitive protein that controls PDH and alphaKGDH lipoylation and activation to support metabolic adaptation in hypoxia and cancer. *Proc Natl Acad Sci USA* 115(8):1789-1794. PMID: 29437960. PMCID: PMC5828627. DOI: 10.1073/pnas.1720693115

11. **tissier-2019-tls-vs-ts-abstract**: Tissier A, Lemoine R, Yamada K, et al. (2019) PDIP38/PolDIP2 controls the DNA damage tolerance pathways by increasing the relative usage of translesion DNA synthesis over template switching. *PLOS ONE* 14(3):e0213383. PMID: 30817784. PMCID: PMC6402704. DOI: 10.1371/journal.pone.0213383

12. **cheng-2018-nox4-actin-abstract**: Cheng G, Amanso DB, et al. (2018) NOX4 (NADPH Oxidase 4) and Poldip2 (Polymerase delta-Interacting Protein 2) Induce Filamentous Actin Oxidation and Promote Its Interaction With Vinculin During Integrin-Mediated Cell Adhesion. *Arterioscler Thromb Vasc Biol* 38(11):2651-2666. PMID: 30354218. DOI: 10.1161/ATVBAHA.118.311668

13. **klaile-2008-spindle-abstract**: Klaile E, Kukalev A, Obrink B, Muller MM. (2008) PDIP38 is a novel mitotic spindle-associated protein that affects spindle organization and chromosome segregation. *Cell Cycle* 7(20):3180-3186. PMID: 18843206. DOI: 10.4161/cc.7.20.6813

14. **wong-2013-splicing-abstract**: Wong A, Zhang S, Mordue D, Wu JM, Zhang Z, Darzynkiewicz Z, Lee EYC, Lee MYWT. (2013) PDIP38 is translocated to the spliceosomes/nuclear speckles in response to UV-induced DNA damage and is required for UV-induced alternative splicing of MDM2. *Cell Cycle* 12(19):3184-3193. PMID: 23989611. PMCID: PMC3865014. DOI: 10.4161/cc.26221

15. **kim-2015-tau-abstract**: Kim N, et al. (2015) Essential role of POLDIP2 in Tau aggregation and neurotoxicity via autophagy/proteasome inhibition. *Biochem Biophys Res Commun* PMID: 25930997


## Citations

1. amanso-2014-knockout-abstract.md
2. amanso-2018-lipoylation-abstract.md
3. cheng-2018-nox4-actin-abstract.md
4. guilliam-2016-primpol-abstract.md
5. hernandes-2017-review-fulltext.md
6. kim-2015-tau-abstract.md
7. klaile-2008-spindle-abstract.md
8. kulik-2021-structure-abstract.md
9. liu-2003-pdip38-discovery-abstract.md
10. lyle-2009-nox4-abstract.md
11. maga-2013-pol-lambda-abstract.md
12. strack-2020-clpxp-abstract.md
13. sutliff-2013-vascular-abstract.md
14. tissier-2019-tls-vs-ts-abstract.md
15. wong-2013-splicing-abstract.md