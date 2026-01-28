---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T02:13:20.084698'
end_time: '2026-01-24T02:25:52.260038'
duration_seconds: 752.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: RASA4
  gene_symbol: RASA4
  uniprot_accession: O43374
  protein_description: 'RecName: Full=Ras GTPase-activating protein 4; AltName: Full=Calcium-promoted
    Ras inactivator; AltName: Full=Ras p21 protein activator 4; AltName: Full=RasGAP-activating-like
    protein 2;'
  gene_info: Name=RASA4; Synonyms=CAPRI, GAPL, KIAA0538;
  organism_full: Homo sapiens (Human).
  protein_family: Not specified in UniProt
  protein_domains: C2_dom. (IPR000008); C2_domain_sf. (IPR035892); PH-like_dom_sf.
    (IPR011993); PH_domain. (IPR001849); Ras_GTPase. (IPR039360)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** O43374
- **Protein Description:** RecName: Full=Ras GTPase-activating protein 4; AltName: Full=Calcium-promoted Ras inactivator; AltName: Full=Ras p21 protein activator 4; AltName: Full=RasGAP-activating-like protein 2;
- **Gene Information:** Name=RASA4; Synonyms=CAPRI, GAPL, KIAA0538;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_dom. (IPR000008); C2_domain_sf. (IPR035892); PH-like_dom_sf. (IPR011993); PH_domain. (IPR001849); Ras_GTPase. (IPR039360)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RASA4" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RASA4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RASA4** (gene ID: RASA4, UniProt: O43374) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RASA4 (CAPRI): A Calcium-Regulated Ras GTPase-Activating Protein

## Introduction and Summary

RASA4, also known as CAPRI (Calcium-Promoted Ras Inactivator), GAPL, or KIAA0538, is a member of the GAP1 family of Ras GTPase-activating proteins (RasGAPs) in humans. The protein was first identified and characterized in 2001 by Lockyer and colleagues as a calcium-dependent negative regulator of the Ras-MAPK signaling pathway [lockyer-2001-capri-discovery-abstract]. RASA4/CAPRI functions as a molecular switch that links calcium signaling to the inactivation of small GTPases, primarily Ras and Rap1, at the plasma membrane. Its primary biochemical activity is to accelerate the intrinsic GTPase activity of Ras proteins, converting them from the active GTP-bound state to the inactive GDP-bound state, thereby terminating Ras-mediated signaling [scheffzek-2019-rasgap-review-abstract].

The defining feature of RASA4/CAPRI is its regulation by intracellular calcium. Upon elevation of cytosolic calcium levels, CAPRI rapidly translocates from the cytoplasm to the plasma membrane, where it exerts its GAP activity on membrane-localized Ras and Rap1 [lockyer-2001-capri-discovery-abstract]. This calcium-dependent translocation mechanism positions CAPRI as a critical integrator of calcium and Ras signaling pathways, two fundamental signaling systems that control cell proliferation, differentiation, and numerous other cellular processes.

## Domain Architecture and Structure

RASA4/CAPRI possesses a modular domain architecture characteristic of the GAP1 family, which also includes GAP1(IP4BP), GAP1(m), and RASAL [kupzig-2006-gap1-dual-activity-abstract]. The protein is organized with two amino-terminal C2 domains (C2A and C2B), a central GAP-related domain (GRD) containing the catalytic RasGAP activity, and a carboxyl-terminal pleckstrin homology (PH) domain followed by a Bruton's tyrosine kinase (Btk) motif [liu-2005-capri-rasal-temporal-fulltext].

The tandem C2 domains are the primary calcium-sensing modules of CAPRI. C2 domains are approximately 130-residue motifs that bind calcium ions and phospholipids, mediating calcium-dependent membrane association [liu-2005-capri-rasal-temporal-fulltext]. Studies using domain deletion and chimeric constructs demonstrated that the C2A and C2B domains together are both necessary and sufficient for sensing increases in cytosolic calcium, driving the initial translocation of CAPRI to membranes [liu-2005-capri-rasal-temporal-fulltext]. However, the sustained association of CAPRI with the plasma membrane, which distinguishes it from the related protein RASAL, requires the PH domain. A domain-breaking mutation (W664A) in the PH domain abolished sustained membrane translocation while preserving the initial calcium-triggered response [liu-2005-capri-rasal-temporal-fulltext].

The central GRD contains the catalytic machinery for GAP activity, including the critical "arginine finger" residue that is inserted into the active site of Ras to stabilize the transition state for GTP hydrolysis [scheffzek-2019-rasgap-review-abstract]. Mutagenesis of this arginine finger (R473S in CAPRI) eliminates both RasGAP and RapGAP activities, confirming that both substrates utilize the same catalytic mechanism [kupzig-2006-gap1-dual-activity-abstract].

## Biochemical Function: Dual RasGAP and RapGAP Activity

A fundamental discovery regarding CAPRI was that it possesses dual specificity, acting as a GTPase-activating protein for both Ras and the related GTPase Rap1 [kupzig-2006-gap1-dual-activity-abstract]. This dual activity is shared by other GAP1 family members including GAP1(IP4BP) and RASAL, but not by GAP1(m), which appears to be Ras-specific [kupzig-2006-gap1-dual-activity-abstract]. Kinetic analyses of GAP1(IP4BP), which is biochemically similar to CAPRI, revealed Km values of 213 μM for Ras and 42 μM for Rap, with estimated kcat values of 48 s⁻¹ and 16 s⁻¹ respectively [kupzig-2006-gap1-dual-activity-abstract]. Importantly, regions outside the isolated GRD are required for Rap GAP activity; the GRD alone retains RasGAP activity but has very low RapGAP activity [kupzig-2006-gap1-dual-activity-abstract].

A sophisticated mechanism for switching between RasGAP and RapGAP activities was elucidated by Dai and colleagues in 2011 [dai-2011-capri-dimerization-abstract]. They discovered that CAPRI forms calcium-dependent homodimers both in vitro and in living cells. The dimerization site was mapped to a C-terminal helix motif that forms a hydrophobic interface. Critically, monomeric and dimeric CAPRI exhibit different substrate preferences: monomeric CAPRI displays stronger RasGAP activity, while the dimeric form has stronger RapGAP activity [dai-2011-capri-dimerization-abstract]. This calcium-dependent switch in oligomeric state provides a mechanism for coordinating the regulation of Ras and Rap1 signaling pathways in response to the amplitude of calcium signals.

## Calcium-Dependent Regulation and Temporal Signal Processing

One of the most distinctive features of CAPRI is its behavior as a "low-pass filter" for calcium signals, contrasting sharply with RASAL, which tracks calcium oscillations in real time [liu-2005-capri-rasal-temporal-fulltext]. When cells are stimulated with agonists that induce calcium oscillations, RASAL undergoes synchronous, oscillatory associations with the plasma membrane, deactivating Ras during each period of membrane association [walker-2004-rasal-discovery-abstract]. In contrast, CAPRI displays a long-lasting, sustained translocation to the plasma membrane that is refractory to ongoing calcium oscillations [liu-2005-capri-rasal-temporal-fulltext].

Quantitative analysis revealed that CAPRI has a half-maximal dissociation time of greater than 280 seconds from the plasma membrane, compared to only 17 seconds for RASAL and 13 seconds for PKCγ, a conventional protein kinase C [liu-2005-capri-rasal-temporal-fulltext]. This sustained membrane association is not simply a consequence of prolonged calcium elevation; experiments performed in calcium-free conditions showed that CAPRI dissociation from the membrane occurs much more slowly than the decline in cytosolic calcium, indicating that predominantly calcium-independent interactions maintain CAPRI at the plasma membrane after the initial calcium-triggered translocation [liu-2005-capri-rasal-temporal-fulltext]. The PH domain is critical for this sustained association, likely through interactions with membrane lipids or protein partners that become available following receptor activation.

The functional consequence of this temporal filtering is that CAPRI converts different intensities of stimulation into different durations of Ras inactivation, rather than encoding information in the frequency domain as RASAL does [liu-2005-capri-rasal-temporal-fulltext]. As summarized in a commentary by Muallem, CAPRI acts as an integrator that extends the duration of calcium's effect on Ras activity, while RASAL functions as a linear decoder that preserves calcium frequency information [muallem-2005-decoding-ca-commentary].

## Tissue Expression and Subcellular Localization

According to the Human Protein Atlas, RASA4 shows widespread tissue expression with particularly high RNA levels in skeletal muscle (223 nTPM), tongue, and endometrium [human-protein-atlas-rasa4]. Moderate expression is observed across brain regions including the amygdala, hippocampal formation, and cerebral cortex, as well as in kidney. Protein-level detection has been confirmed in colon (peripheral nerve/ganglion), kidney tubular cells, and testis Leydig cells, though the Human Protein Atlas notes that antibody-based detection shows variable reliability due to potential cross-reactivity [human-protein-atlas-rasa4].

At the subcellular level, CAPRI is predominantly cytoplasmic at rest, lacking phosphoinositide binding activity that would otherwise target it to membranes. Immunofluorescence studies in the Human Protein Atlas indicate localization to vesicles and cell junctions in cultured cell lines, with notable single-cell variation in expression levels [human-protein-atlas-rasa4]. However, the functional literature establishes that CAPRI exerts its primary function at the plasma membrane, where it acts on Ras pools localized to this compartment. Pivotal work by Bivona and colleagues demonstrated that Ras is activated on and signals from both the plasma membrane and the Golgi apparatus, with distinct mechanisms regulating each compartment [bivona-2003-ras-golgi-abstract]. While calcium positively regulates Ras at the Golgi through the guanine nucleotide exchange factor RasGRP1, it negatively regulates Ras at the plasma membrane through CAPRI [bivona-2003-ras-golgi-abstract]. In Jurkat T cells stimulated through the T-cell receptor, Ras activation was found to be restricted to the Golgi apparatus specifically because CAPRI inactivated plasma membrane Ras, demonstrating an unambiguous physiological role for compartmentalized Ras signaling [bivona-2003-ras-golgi-abstract].

Using live-cell imaging with a GFP-tagged Ras-binding domain (RBD) reporter, Liu and colleagues directly visualized calcium-triggered Ras deactivation by CAPRI in real time [liu-2005-capri-rasal-temporal-fulltext]. Upon receptor stimulation, CAPRI translocated to the plasma membrane, which correlated precisely with dissociation of the GFP-RBD reporter from the membrane, indicating loss of active Ras-GTP. Importantly, CAPRI showed no detectable GAP activity at resting calcium levels, suggesting that it exists in an inactive or "closed" conformation in the cytosol and is acutely activated upon membrane recruitment [liu-2005-capri-rasal-temporal-fulltext].

## Biological Functions

### Regulation of Neutrophil Chemotaxis

A significant recent advance in understanding CAPRI function came from studies of neutrophil chemotaxis by Xu and colleagues [xu-2021-capri-neutrophil-chemotaxis-abstract]. Neutrophils navigate through enormous concentration ranges of chemoattractant gradients (10⁻¹¹ to 10⁻⁶ M) through a process called adaptation, whereby cells remain sensitive to stronger stimuli despite continued exposure to existing chemoattractants. Using CRISPR-generated CAPRI knockout neutrophil-like cells, they demonstrated that CAPRI controls GPCR-stimulated Ras adaptation [xu-2021-capri-neutrophil-chemotaxis-abstract].

CAPRI-deficient cells displayed nonadaptive Ras activation in response to chemoattractants, with significantly increased phosphorylation of downstream effectors including AKT, GSK-3α/β, and cofilin, and excessive actin polymerization [xu-2021-capri-neutrophil-chemotaxis-abstract]. Phenotypically, CAPRI knockout cells showed defective chemotaxis in response to high-concentration gradients but, interestingly, exhibited improved chemotaxis in low or subsensitive concentration gradients due to their enhanced sensitivity [xu-2021-capri-neutrophil-chemotaxis-abstract]. This work established that CAPRI functions to lower cellular sensitivity to chemoattractants, enabling neutrophils to chemotax through a wider concentration range.

More recent work by the same group in 2025 further elucidated the upstream pathway controlling CAPRI activity in neutrophils [xu-2025-plcg2-capri-abstract]. They demonstrated that phospholipase Cγ2 (PLCγ2) is essential for both spontaneous and chemoattractant-induced calcium oscillations. PLCγ2-knockout cells exhibited impaired calcium oscillations and diminished CAPRI membrane targeting, resulting in elevated Ras activation and enhanced downstream signaling. This study established a PLCγ2 → calcium oscillation → CAPRI → Ras inactivation signaling axis that controls neutrophil sensitivity to chemoattractants [xu-2025-plcg2-capri-abstract].

### Fc Receptor-Mediated Phagocytosis

Zhang and colleagues discovered an unexpected adaptor function for CAPRI in Fc gamma receptor-mediated phagocytosis, independent of its GAP activity [zhang-2005-capri-phagocytosis-abstract]. CAPRI-deficient macrophages showed impaired FcγR-mediated phagocytosis and oxidative burst, along with defective activation of the Rho GTPases Cdc42 and Rac1 [zhang-2005-capri-phagocytosis-abstract]. Remarkably, CAPRI was found to interact constitutively with both Cdc42 and Rac1, serving as an adaptor protein that recruits these GTPases to phagocytic cups during FcγR-mediated phagocytosis [zhang-2005-capri-phagocytosis-abstract]. CAPRI-deficient mice exhibited impaired innate immune responses to bacterial infection, demonstrating the physiological importance of this adaptor function [zhang-2005-capri-phagocytosis-abstract]. This study revealed that CAPRI provides a previously unknown link between Fc receptors and Rho GTPase activation essential for innate immunity.

### T Cell Adhesion

In T lymphocytes, CAPRI was found to mediate CD28-dependent inhibition of cell adhesion [strazza-2015-cd28-capri-abstract]. CD28 signaling induces calcium influx, which triggers CAPRI translocation to the plasma membrane via its C2 domains. At the membrane, CAPRI inhibits Rap1 activity through its RapGAP function, leading to decreased LFA-1-mediated adhesion to antigen-presenting cells [strazza-2015-cd28-capri-abstract]. This pathway provides a mechanism for CD28 co-stimulation to modulate T cell adhesion dynamics during immune responses.

### Splice Variants and RANKL Regulation

An alternatively spliced variant of CAPRI, termed deltaCAPRI, was identified in primary osteoblasts [hikita-2005-deltacapri-rankl-abstract]. This variant lacks one exon within the GAP-related domain and, in contrast to full-length CAPRI, acts to activate rather than inactivate the Ras pathway [hikita-2005-deltacapri-rankl-abstract]. DeltaCAPRI promotes the shedding of RANKL (receptor activator of NF-κB ligand), a critical regulator of osteoclastogenesis, by upregulating expression of MMP14 through Ras signaling [hikita-2005-deltacapri-rankl-abstract]. This finding highlights the importance of alternative splicing in generating functionally distinct CAPRI isoforms with opposing effects on Ras signaling.

## Role in Disease

### Cancer

RasGAPs have emerged as an expanding class of tumor suppressors, since loss of GAP function provides an alternative mechanism for aberrant Ras activation beyond direct Ras mutations [maertens-2014-rasgap-cancer-review-abstract]. While NF1 (neurofibromin) is the best-characterized tumor suppressor RasGAP, other family members including RASAL are epigenetically silenced in various cancers [jin-2007-rasal-epigenetic-abstract]. RASA4 hypermethylation has been reported in juvenile myelomonocytic leukemia, where it correlates with poor prognosis and higher relapse risk after stem cell transplantation [poetsch-2014-rasa4-jmml-abstract]. In cervical cancer, reduced RASA4 expression correlates with tumor progression, and ectopic RASA4 expression inhibits proliferation of cervical cancer cells through effects on HIF-α signaling [chen-2021-rasa4-cervical-cancer-abstract].

## Open Questions

Several important questions about RASA4/CAPRI remain to be addressed:

1. **Structural basis of dual specificity**: While it is established that CAPRI has both RasGAP and RapGAP activities, the structural details of how Rap1 engages the catalytic domain, and how the oligomeric state influences substrate preference, remain incompletely understood.

2. **PH domain ligands**: The identity of the membrane ligands (lipids and/or proteins) that engage the PH domain and maintain CAPRI at the plasma membrane after the initial calcium-triggered translocation is not fully defined.

3. **Tissue-specific functions**: CAPRI is expressed in multiple cell types, but its specific functions in different tissues and developmental contexts are not comprehensively characterized.

4. **Coordination with other calcium sensors**: How CAPRI integrates with the broader network of calcium-sensing proteins, including conventional PKCs, to coordinate cellular responses to calcium signals remains an area of active investigation.

5. **Therapeutic targeting**: Whether loss of CAPRI function contributes to cancer progression broadly, and whether CAPRI activity can be therapeutically modulated, represents an important translational question.

6. **Interaction with Rho GTPases**: The molecular basis of CAPRI's constitutive interaction with Cdc42 and Rac1, and how this adaptor function is coordinated with its GAP activities, requires further investigation.

## References

- **lockyer-2001-capri-discovery-abstract**: Lockyer PJ, Kupzig S, Cullen PJ. CAPRI regulates Ca(2+)-dependent inactivation of the Ras-MAPK pathway. Curr Biol. 2001;11(12):981-6. PMID: 11448776. DOI: https://doi.org/10.1016/s0960-9822(01)00261-5

- **liu-2005-capri-rasal-temporal-fulltext**: Liu Q, Walker SA, Gao D, et al. CAPRI and RASAL impose different modes of information processing on Ras due to contrasting temporal filtering of Ca2+. J Cell Biol. 2005;170(2):183-90. PMID: 16009725. PMCID: PMC1351313. DOI: https://doi.org/10.1083/jcb.200504167

- **kupzig-2006-gap1-dual-activity-abstract**: Kupzig S, Deaconescu D, Bouyoucef D, et al. GAP1 family members constitute bifunctional Ras and Rap GTPase-activating proteins. J Biol Chem. 2006;281(15):9891-900. PMID: 16431904. PMCID: PMC1904491. DOI: https://doi.org/10.1074/jbc.M512802200

- **dai-2011-capri-dimerization-abstract**: Dai Y, Walker SA, de Vet E, et al. Ca2+-dependent monomer and dimer formation switches CAPRI Protein between Ras GTPase-activating protein (GAP) and RapGAP activities. J Biol Chem. 2011;286(22):19905-16. PMID: 21460216. PMCID: PMC3103366. DOI: https://doi.org/10.1074/jbc.M110.201301

- **zhang-2005-capri-phagocytosis-abstract**: Zhang J, Guo J, Dzhagalov I, He YW. An essential function for the calcium-promoted Ras inactivator in Fcgamma receptor-mediated phagocytosis. Nat Immunol. 2005;6(9):911-9. PMID: 16041389. PMCID: PMC1464573. DOI: https://doi.org/10.1038/ni1232

- **bivona-2003-ras-golgi-abstract**: Bivona TG, Pérez De Castro I, Ahearn IM, et al. Phospholipase Cgamma activates Ras on the Golgi apparatus by means of RasGRP1. Nature. 2003;424(6949):694-8. PMID: 12845332. DOI: https://doi.org/10.1038/nature01806

- **xu-2021-capri-neutrophil-chemotaxis-abstract**: Xu X, Wen X, Moosa A, Bhimani S, Jin T. Ras inhibitor CAPRI enables neutrophil-like cells to chemotax through a higher-concentration range of gradients. Proc Natl Acad Sci USA. 2021;118(43):e2002162118. PMID: 34675073. PMCID: PMC8639426. DOI: https://doi.org/10.1073/pnas.2002162118

- **strazza-2015-cd28-capri-abstract**: Strazza M, Azoulay-Alfaguter I, Dun B, et al. CD28 inhibits T cell adhesion by recruiting CAPRI to the plasma membrane. J Immunol. 2015;194(6):2871-7. PMID: 25637021. DOI: https://doi.org/10.4049/jimmunol.1401492

- **walker-2004-rasal-discovery-abstract**: Walker SA, Kupzig S, Bouyoucef D, et al. Identification of a Ras GTPase-activating protein regulated by receptor-mediated Ca2+ oscillations. EMBO J. 2004;23(8):1749-60. PMID: 15057271. PMCID: PMC394250. DOI: https://doi.org/10.1038/sj.emboj.7600197

- **scheffzek-2019-rasgap-review-abstract**: Scheffzek K, Shivalingaiah G. Ras-Specific GTPase-Activating Proteins-Structures, Mechanisms, and Interactions. Cold Spring Harb Perspect Med. 2019;9(3):a031500. PMID: 30104198. PMCID: PMC6396337. DOI: https://doi.org/10.1101/cshperspect.a031500

- **maertens-2014-rasgap-cancer-review-abstract**: Maertens O, Cichowski K. An expanding role for RAS GTPase activating proteins (RAS GAPs) in cancer. Adv Biol Regul. 2014;55:1-14. PMID: 24814062. DOI: https://doi.org/10.1016/j.jbior.2014.04.002

- **muallem-2005-decoding-ca-commentary**: Muallem S. Decoding Ca2+ signals: a question of timing. J Cell Biol. 2005;170(2):173-5. PMID: 16027217. PMCID: PMC2171404. DOI: https://doi.org/10.1083/jcb.200506047

- **hikita-2005-deltacapri-rankl-abstract**: Hikita A, Kadono Y, Chikuda H, et al. Identification of an alternatively spliced variant of Ca2+-promoted Ras inactivator as a possible regulator of RANKL shedding. J Biol Chem. 2005;280(50):41700-6. PMID: 16234249. DOI: https://doi.org/10.1074/jbc.M507000200

- **jin-2007-rasal-epigenetic-abstract**: Jin H, Wang X, Ying J, et al. Epigenetic silencing of a Ca(2+)-regulated Ras GTPase-activating protein RASAL defines a new mechanism of Ras activation in human cancers. Proc Natl Acad Sci USA. 2007;104(30):12353-8. PMID: 17640920. PMCID: PMC1941473. DOI: https://doi.org/10.1073/pnas.0700153104

- **poetsch-2014-rasa4-jmml-abstract**: Poetsch AR, Lipka DB, Witte T, et al. RASA4 undergoes DNA hypermethylation in resistant juvenile myelomonocytic leukemia. Epigenetics. 2014;9(9):1252-60. PMID: 25147919. PMCID: PMC4169017. DOI: https://doi.org/10.4161/epi.29941

- **chen-2021-rasa4-cervical-cancer-abstract**: Chen J, Huang J, Huang Q, et al. RASA4 inhibits the HIFα signaling pathway to suppress proliferation of cervical cancer cells. Bioengineered. 2021;12(2):10723-10733. PMID: 34752201. PMCID: PMC8809920. DOI: https://doi.org/10.1080/21655979.2021.2002499

- **xu-2025-plcg2-capri-abstract**: Xu X, Kim WS, Lee A, Jin T. PLCγ2 controls neutrophil-like cell sensitivity through calcium oscillation and gates chemoattractant concentration range for chemotaxis. Front Immunol. 2025;16:1633390. PMID: 40821808. PMCID: PMC12354650. DOI: https://doi.org/10.3389/fimmu.2025.1633390

- **human-protein-atlas-rasa4**: The Human Protein Atlas. RASA4 - Ras GTPase-activating protein 4. URL: https://www.proteinatlas.org/ENSG00000105808-RASA4. Accessed January 2026.


## Citations

1. bivona-2003-ras-golgi-abstract.md
2. chen-2021-rasa4-cervical-cancer-abstract.md
3. dai-2011-capri-dimerization-abstract.md
4. hikita-2005-deltacapri-rankl-abstract.md
5. human-protein-atlas-rasa4.md
6. jin-2007-rasal-epigenetic-abstract.md
7. kupzig-2006-gap1-dual-activity-abstract.md
8. liu-2005-capri-rasal-temporal-fulltext.md
9. lockyer-2001-capri-discovery-abstract.md
10. maertens-2014-rasgap-cancer-review-abstract.md
11. muallem-2005-decoding-ca-commentary.md
12. poetsch-2014-rasa4-jmml-abstract.md
13. scheffzek-2019-rasgap-review-abstract.md
14. strazza-2015-cd28-capri-abstract.md
15. walker-2004-rasal-discovery-abstract.md
16. xu-2021-capri-neutrophil-chemotaxis-abstract.md
17. xu-2025-plcg2-capri-abstract.md
18. zhang-2005-capri-phagocytosis-abstract.md