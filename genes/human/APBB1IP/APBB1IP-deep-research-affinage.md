---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/APBB1IP
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q7Z5R6
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 23
citation_count: 23
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for APBB1IP (human)

## Current model (mechanistic narrative)

APBB1IP (RIAM) is a multidomain Rap1-effector scaffold that couples small-GTPase signaling to integrin activation and actin-based motility [PMID:15469846, PMID:19098287]. It was first identified as a Rap1-GTP-interacting adaptor that also binds Profilin and Ena/VASP proteins, and whose activity is required to retain Rap1-GTP at the plasma membrane and drive integrin activation, cell spreading, and lamellipodia formation [PMID:15469846]. The core of its function is a relay that recruits talin to the membrane: RIAM binds active Rap1 through its RA-PH module — with a Rap1 Lys31–RIAM Glu212 salt bridge serving as the specificity determinant [PMID:24287201] — and binds talin directly via short N-terminal amphipathic helices, such that a minimized Rap-RIAM module is sufficient to recruit talin and activate integrins [PMID:19098287, PMID:22523535]. RIAM additionally engages the talin head to sterically displace the talin rod domain that masks the integrin-binding site, conformationally unmasking talin to promote inside-out integrin activation [PMID:25520155]. RIAM activity is gated by autoinhibition: an intramolecular IN–RA-PH interaction suppresses Rap1 binding and is released by FAK-dependent phosphorylation of Tyr45, while Src-mediated phosphorylation of PH-domain residues Tyr267/Tyr427 unmasks the PIP2-binding site to enable membrane recruitment [PMID:30733287, PMID:33275877]. At the cell periphery RIAM forms a trimeric MRL–integrin–talin complex at the tips of lamellipodial and filopodial protrusions [PMID:26419705] and engages vinculin within the focal-adhesion talin-vinculin complex in a force-independent manner [PMID:41454178]; it also controls focal-adhesion disassembly through a RhoA–MEK–Erk pathway [PMID:22946047]. In vivo, RIAM is essential in leukocytes for β2 integrin activation, adhesion to inflamed vessels, and trafficking to lymphoid organs, while being dispensable for platelet integrins [PMID:26337492, PMID:26324702], and it is required for immunological synapse formation and complement-mediated (CR3/αMβ2) phagocytosis [PMID:28348273, PMID:23420480].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity, GO:0008289 lipid binding, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005886 plasma membrane, GO:0005856 cytoskeleton, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-168256 Immune System, R-HSA-162582 Signal Transduction, R-HSA-1474244 Extracellular matrix organization
- **partners:** RAP1A, TLN1, VASP, PFN1, VCL, SKAP-55, PLCG1, ITGB2
- **complexes:** MRL protein-integrin-talin (MIT) complex, talin-vinculin-RIAM focal adhesion complex, ADAP/SKAP-55 signaling module

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2004 | High | RIAM was identified as a Rap1-GTP-interacting adaptor molecule that directly interacts with active Rap1 (GTP-bound), Profilin, and Ena/VASP proteins. RIAM overexpression induced cell spreading, lamellipodia formation, integrin activation, and cell adhesion; knockdown displaced Rap1-GTP from the plasma membrane and abrogated Rap1-induced adhesion and reduced polymerized actin content. | PMID:15469846 | Developmental cell |
| 2008 | High | RIAM functions as a scaffold connecting membrane-targeting sequences of Ras GTPases (Rap1) to talin, thereby recruiting talin to the plasma membrane to activate integrins. RIAM binds directly to talin via short N-terminal amphipathic helix sequences, and a minimized 50-residue Rap-RIAM module (talin-binding site of RIAM joined to the membrane-targeting sequence of Rap1A) is sufficient to recruit talin and activate integrins. | PMID:19098287 | The Journal of biological chemistry |
| 2006 | Medium | MIG-10 (the C. elegans RIAM ortholog) functions downstream of the attractive guidance cue UNC-6/netrin and repulsive cue SLT-1/slit to direct axon migration. MIG-10 interacts with UNC-34 (Ena/VASP ortholog) to mediate responses to guidance cues, and colocalizes with actin in cultured cells where it can induce lamellipodia formation. | PMID:16563765 | Current biology : CB |
| 2007 | Medium | RIAM constitutively interacts with SKAP-55 (component of the ADAP/SKAP-55 signaling module) in both heterologous transfection systems and primary T cells, linking the ADAP/SKAP-55 module to Rap1 for TCR-mediated integrin activation. Following TCR activation, the ADAP/SKAP-55 module relocalized RIAM and Rap1 to the plasma membrane. | PMID:17403904 | Molecular and cellular biology |
| 2009 | Medium | RIAM is required for TCR-mediated PLC-γ1 translocation to the actin cytoskeleton in T cells. RIAM knockdown impaired inositol trisphosphate generation, intracellular calcium mobilization, NFAT nuclear translocation, Ras-GRP1 activation, and IL-2 gene expression, while ZAP-70 phosphorylation and LAT signalosomes were unaffected. RIAM positions PLC-γ1 near its substrate PIP2. | PMID:19952372 | Science signaling |
| 2010 | Medium | Loss of β3 integrin leads to dephosphorylation of VASP (via loss of PKA-dependent phosphorylation), and dephosphorylated VASP preferentially associates with RIAM both in vitro and in vivo, forming an enhanced VASP-RIAM complex at focal adhesions that promotes talin binding to β1 integrin, revealing a mechanism by which αvβ3 locally suppresses β1 integrin activation. | PMID:20404115 | The Journal of cell biology |
| 2011 | Medium | RIAM is required for BLM melanoma cell invasion and tumor growth. RIAM silencing impairs persistent cell migration directionality via deficient activation of a Vav2-RhoA-ROCK-myosin light chain pathway. Constitutively active Vav2 and RhoA partially rescued invasion in RIAM-depleted cells. RIAM depletion also reduces β1 integrin-dependent adhesion and decreases Erk1/2 MAPK and PI3K activation. | PMID:21454517 | The Journal of biological chemistry |
| 2012 | Medium | RIAM is required for focal adhesion (FA) disassembly: RIAM depletion in melanoma and breast carcinoma cells causes increased FA number, size, and stability due to defective FA disassembly. This is mediated through a RIAM→RhoA→MEK→Erk1/2 pathway downstream of integrin engagement; constitutively active MEK rescued FA disassembly and cell invasion in RIAM-depleted cells. RIAM depletion also weakened associations between FA proteins. | PMID:22946047 | Journal of cell science |
| 2012 | Medium | The RA domain of RIAM is sufficient for GTP-dependent interaction with Rap1B; addition of the PH domain does not change binding affinity but stabilizes the RA domain both in vitro and in cells. A GTP-independent interaction between Rap1B and the N-terminus of RIAM was also detected. | PMID:22523535 | PloS one |
| 2013 | High | Crystal structure of GTP-bound Rap1 in complex with the RA-PH module of RIAM at 1.65 Å resolution reveals that Rap1 Lys31 forms a salt bridge with RIAM Glu212 as the key specificity determinant. Disruption of these interactions reduces Rap1:RIAM association, co-clustering, and cell adhesion. | PMID:24287201 | Journal of molecular cell biology |
| 2013 | Medium | RIAM is required for complement-mediated (CR3/αMβ2-dependent) phagocytosis but not IgG-mediated phagocytosis in myeloid cells. RIAM knockdown impairs αMβ2 integrin affinity changes and blocks Rap1-induced complement phagocytosis enhancement. RIAM mediates its function by recruiting talin to the β2 integrin cytoplasmic tail during phagocytosis. | PMID:23420480 | Cellular and molecular life sciences : CMLS |
| 2014 | High | RIAM binds not only to the talin rod (talin-R) but also to the talin head (talin-H). RIAM binding to talin-H sterically occludes a talin-R domain that otherwise masks the integrin-binding site on talin-H, thereby conformationally unmasking talin and promoting integrin activation. This reveals a novel role for RIAM in talin conformational regulation. | PMID:25520155 | Nature communications |
| 2015 | High | RIAM (MRL protein) forms a complex with talin and activated integrins at the tips of growing actin filaments in lamellipodial and filopodial protrusions ('sticky fingers'). Talin bridges MRL proteins to integrins to form this MRL protein-integrin-talin (MIT) complex. Disruption of the MIT complex markedly impairs cell protrusion. | PMID:26419705 | Nature communications |
| 2015 | High | RIAM deficiency in mice results in loss of β2 integrin activation in multiple leukocyte populations, impaired leukocyte adhesion to inflamed vessels, and accumulation in circulation, demonstrating leukocyte-specific requirement for RIAM. By contrast, β1 integrin family member α4β1 was only partially affected, and platelet integrin activation was unaffected. | PMID:26337492 | Blood |
| 2015 | High | RIAM-deficient mice show defective lymphocyte adhesion to ICAM-1 and VCAM-1 and impaired trafficking of lymphocytes to secondary lymphoid organs (peripheral lymph nodes and bone marrow), associated with defective humoral immunity to T-cell-dependent antigens. Platelet function was intact in RIAM-deficient animals. | PMID:26324702 | Blood |
| 2017 | Medium | The talin R3 domain (which contains a RIAM binding site) is thermodynamically poised to bind either RIAM (closed conformation) or vinculin (open conformation), functioning as a mechanosensitive conformational switch. A mutant of R3 that retains RIAM binding but binds vinculin more weakly is 0.84 kJ/mol more stable when closed. | PMID:29153504 | Structure (London, England : 1993) |
| 2017 | Medium | RIAM expression in T cells is required for formation of immunological synapses: RIAM is recruited to immune synapses along with talin and LFA-1, and loss of RIAM profoundly suppresses antigen-dependent conjugate formation between T cells and APCs, Ag-driven proliferation, and cytotoxic killing. | PMID:28348273 | Journal of immunology (Baltimore, Md. : 1950) |
| 2019 | High | RIAM is autoinhibited by an intramolecular interaction between its N-terminal IN region (aa 27–93) and the RA-PH module, which suppresses Rap1 association. Crystal structure of the IN-RA-PH module at 2.4 Å reveals the structural basis. Phosphorylation of Tyr45 in the IN segment releases autoinhibition; FAK inhibitors block Tyr45 phosphorylation, inhibit RIAM translocation to the plasma membrane, and inhibit integrin-mediated cell adhesion in a Tyr45-dependent manner. | PMID:30733287 | Proceedings of the National Academy of Sciences of the United States of America |
| 2020 | Medium | RIAM-VASP complex functions as a relay for integrin complement receptors in outside-in signaling during complement-dependent phagocytosis. RIAM deficiency impaired particle internalization and downstream integrin signaling. RIAM is required for recruitment of VASP to phagocytic cups, VASP phosphorylation (pSer157-VASP), and formation of actin-rich phagocytic cups. | PMID:32397169 | Cells |
| 2020 | High | Src family kinases phosphorylate RIAM at Tyr267 and Tyr427 in the PH domain, disrupting an intermolecular PH-mediated interface that normally masks the PIP2-binding site. This unmasks the membrane PIP2-binding site and promotes integrin activation and RIAM recruitment to the plasma membrane. | PMID:33275877 | Structure (London, England : 1993) |
| 2021 | Medium | Binding of both Rap1 and RIAM to talin1 synergistically regulates β2 integrin conformation and leukocyte trafficking. Using Rap1-binding mutant talin1 mice crossed with RIAM-deficient mice, simultaneous loss of both pathways produces a rolling phenotype similar to complete talin1 deficiency, indicating that Rap1-direct and RIAM-mediated pathways to talin are the primary β2 integrin regulatory mechanisms in leukocytes. | PMID:34489950 | Frontiers in immunology |
| 2021 | Medium | RIAM controls expression of the phagocytic integrin receptors αMβ2 and αXβ2 at the mRNA level during neutrophilic differentiation. RIAM (as well as VASP and Vinculin) KO cells showed reduced F-actin content that correlated with reduced ITGAM and ITGAX mRNA. The SRF coactivator MRTF-A (which requires actin polymerization) showed cytoplasmic mislocalization in RIAM KO cells, suggesting RIAM regulates integrin gene expression via an actin-MRTF-A-SRF transcriptional pathway. | PMID:36238292 | Frontiers in immunology |
| 2025 | Medium | RIAM binds to the N-terminus of vinculin in focal adhesions in a force-independent manner, as demonstrated by a three-color FRET-cascade TCSPC-FLIM system validated with purified proteins and negative-staining TEM. The RIAM-vinculin interaction occurs within the talin-vinculin-RIAM multiprotein complex at focal adhesions. | PMID:41454178 | Communications chemistry |

## Citations

- PMID:15469846
- PMID:16563765
- PMID:17403904
- PMID:19098287
- PMID:19952372
- PMID:20404115
- PMID:21454517
- PMID:22523535
- PMID:22946047
- PMID:23420480
- PMID:24287201
- PMID:25520155
- PMID:26324702
- PMID:26337492
- PMID:26419705
- PMID:28348273
- PMID:29153504
- PMID:30733287
- PMID:32397169
- PMID:33275877
- PMID:34489950
- PMID:36238292
- PMID:41454178
