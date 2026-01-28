---
provider: cyberian
model: deep-research
cached: true
start_time: '2026-01-23T16:52:36.385780'
end_time: '2026-01-23T16:52:36.387577'
duration_seconds: 0.0
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: PARD6G
  gene_symbol: PARD6G
  uniprot_accession: Q9BYG4
  protein_description: 'RecName: Full=Partitioning defective 6 homolog gamma; Short=PAR-6
    gamma; AltName: Full=PAR6D;'
  gene_info: Name=PARD6G; Synonyms=PAR6G;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the PAR6 family. .
  protein_domains: PAR6_homolog. (IPR051741); PB1-like. (IPR053793); PB1_dom. (IPR000270);
    PB1_Par6. (IPR034868); PDZ. (IPR001478)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 16
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9BYG4
- **Protein Description:** RecName: Full=Partitioning defective 6 homolog gamma; Short=PAR-6 gamma; AltName: Full=PAR6D;
- **Gene Information:** Name=PARD6G; Synonyms=PAR6G;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the PAR6 family. .
- **Key Domains:** PAR6_homolog. (IPR051741); PB1-like. (IPR053793); PB1_dom. (IPR000270); PB1_Par6. (IPR034868); PDZ. (IPR001478)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PARD6G" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PARD6G' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PARD6G** (gene ID: PARD6G, UniProt: Q9BYG4) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PARD6G (PAR-6 gamma): A Comprehensive Review

## Introduction

PARD6G encodes Partitioning defective 6 homolog gamma (PAR-6 gamma), a 376-amino acid adapter protein that functions as a critical regulator of cell polarity in human cells. The gene is located on chromosome 18q23 and is a member of the evolutionarily conserved PAR6 family, which includes three paralogs in mammals: PARD6A, PARD6B, and PARD6G [noda-2001-par6-adaptor-abstract]. The PAR (partitioning-defective) genes were originally identified in Caenorhabditis elegans as essential regulators of asymmetric cell division in early embryos, and their mammalian homologs have since been recognized as fundamental components of the cell polarity machinery [noda-2001-par6-adaptor-abstract].

PARD6G functions primarily as a scaffolding protein that nucleates the assembly of the PAR polarity complex, linking small GTPases of the Rho family (particularly Cdc42 and Rac1) to atypical protein kinase C (aPKC) isoforms. This complex plays essential roles in establishing and maintaining apicobasal polarity in epithelial cells, tight junction assembly, neuronal polarization, and centrosome organization. While PARD6G shares core functions with its paralogs, emerging evidence reveals isoform-specific roles, most notably in centrosome biology and tumor suppression [dormoy-2013-par6gamma-centriole-abstract][marques-2016-par6g-cancer-abstract].

## Domain Architecture and Structural Basis of Function

PARD6G contains three conserved functional domains that mediate its scaffolding function. The N-terminal region contains a Phox and Bem1p (PB1) domain (residues 18-98), which mediates heterotypic interactions with the PB1 domain of aPKC isoforms PKCiota (PRKCI) and PKCzeta (PRKCZ) [hirano-2005-apkc-par6-pb1-abstract]. The central region harbors a partial or semi-CRIB (Cdc42/Rac interactive binding) motif (residues 134-151), which is required for binding to GTP-loaded Rho GTPases. The third major domain is a PDZ (PSD-95, Discs-large, ZO-1) domain (residues 158-251) that mediates interactions with various binding partners including PALS1 and the C-termini of other polarity proteins [garrard-2003-cdc42-par6-structure-abstract].

The crystal structure of Cdc42 in complex with the GTPase-binding domain of Par6 revealed that the semi-CRIB motif adopts an extended conformation that forms an antiparallel beta-sheet with the beta-2 strand of Cdc42 [garrard-2003-cdc42-par6-structure-abstract]. Remarkably, this interaction also involves the PDZ domain, which serves as a structural scaffold that partially organizes the semi-CRIB motif even in the unbound state. The semi-CRIB and PDZ domains together form a continuous eight-stranded beta-sheet when engaged with Cdc42, burying approximately 1100 square angstroms of surface area and achieving a binding affinity of approximately 50 nM [garrard-2003-cdc42-par6-structure-abstract].

Beyond structural stabilization, Cdc42 binding triggers an allosteric conformational change in the Par6 PDZ domain that enhances its ligand-binding affinity approximately 13-fold [peterson-2004-cdc42-allosteric-abstract]. In the absence of Cdc42, the Par6 PDZ domain adopts a non-canonical conformation with low affinity for C-terminal peptide ligands. Cdc42-GTP binding induces a conformational transition in the CRIB-PDZ module, mediated by a dipeptide switch involving residues L164 and K165, that converts the PDZ to a canonical high-affinity configuration [peterson-2004-cdc42-allosteric-abstract]. This allosteric mechanism enables PARD6G to integrate GTPase signaling with downstream protein-protein interactions.

The interaction between Par6 and aPKC occurs through their respective PB1 domains in a "front-to-back" manner. The crystal structure of the PKCiota-Par6alpha PB1 domain complex at 1.5 angstrom resolution revealed that both PB1 domains adopt a ubiquitin-like fold [hirano-2005-apkc-par6-pb1-abstract]. The PKCiota PB1 domain presents an OPCA (OPR, PC, and AID) motif containing acidic and hydrophobic residues that form salt bridges with a conserved lysine residue on the Par6 PB1 domain. This interaction mode is essential for the assembly of the aPKC-Par6 subcomplex that forms the catalytic core of the PAR polarity complex [hirano-2005-apkc-par6-pb1-abstract].

## Subcellular Localization

PARD6G exhibits a complex pattern of subcellular localization that reflects its diverse cellular functions. In polarized epithelial cells, PARD6G localizes to the apical membrane domain and tight junctions, consistent with its role in establishing and maintaining apicobasal polarity [noda-2001-par6-adaptor-abstract]. The protein is also found in the cytoplasm and, under certain conditions, in the nucleus. When co-expressed with aPKC and constitutively active Rac1 in cultured cells, PARD6G co-localizes with these partners to membrane ruffles at the leading edge of migrating cells [noda-2001-par6-adaptor-abstract].

A distinctive feature of PARD6G that distinguishes it from other Par6 family members is its specific localization to the mother centriole within the centrosome [dormoy-2013-par6gamma-centriole-abstract]. The centrosome contains two centrioles of different ages, and the older mother centriole possesses specialized protein appendages that confer unique functions including microtubule organization and ciliogenesis. Dormoy and colleagues demonstrated that PARD6G is a novel component of the mother centriole, and this localization depends on the C-terminal region of the protein (amino acids 259-376) [dormoy-2013-par6gamma-centriole-abstract]. Importantly, centrosomal targeting of PARD6G is independent of intact microtubules, the dynein/dynactin transport complex, and the canonical PAR polarity complex components (Par3 and aPKC), suggesting a distinct targeting mechanism.

## The PAR Polarity Complex and Cell Polarity Establishment

PARD6G functions as a central scaffold within the PAR polarity complex, which comprises PAR3 (PARD3), Par6, aPKC, and the small GTPase Cdc42. This complex is evolutionarily conserved from invertebrates to mammals and represents a fundamental mechanism for establishing and maintaining cellular asymmetry [hurd-2003-par6-pals1-abstract]. The PAR complex localizes to the apical domain of polarized epithelial cells, where it excludes basolateral determinants through aPKC-mediated phosphorylation.

The molecular assembly of the PAR complex involves multiple protein-protein interactions. Par6 binds aPKC through PB1 domain heterodimerization, forming a stable core subcomplex. This subcomplex is recruited to the membrane through Cdc42-GTP binding to the Par6 CRIB-PDZ module. Par3 associates with the aPKC-Par6 subcomplex through its interaction with the aPKC kinase domain via a conserved region called CR3. This association is relatively weak and dynamic, allowing for regulated assembly and disassembly of the full PAR complex.

A critical link exists between the PAR complex and the Crumbs polarity complex, mediated by a direct interaction between Par6 and PALS1 (Proteins Associated with Lin Seven 1) [hurd-2003-par6-pals1-abstract]. The amino terminus of PALS1 binds directly to the Par6 PDZ domain, and this interaction is regulated by Cdc42-GTP. Through this mechanism, the transmembrane protein Crumbs can recruit Par6 to the cell surface. Disruption of the Par6-PALS1 interaction perturbs the proper localization of polarity proteins and tight junction markers, demonstrating the functional importance of this connection between polarity complexes [hurd-2003-par6-pals1-abstract].

## Role in Tight Junction Assembly

Tight junctions form the apical-most intercellular junctions in epithelial cells and serve dual functions: they create a barrier that controls paracellular permeability and they establish a fence that prevents mixing of apical and basolateral membrane proteins. The PAR complex plays a complex role in tight junction regulation, with evidence for both positive and negative regulatory functions.

Studies by Gao et al. demonstrated that Par6 can negatively regulate tight junction assembly in MDCK epithelial cells [gao-2002-par6-tight-junction-abstract]. Overexpression of Par6 delayed the reassembly of tight junctions following calcium switch, as measured by transepithelial resistance and paracellular permeability assays. The N-terminal fragment of PKCzeta that binds Par6 similarly suppressed tight junction assembly, suggesting that the aPKC-Par6 subcomplex has inhibitory activity. Activated Cdc42 could also disrupt tight junctions, implicating the GTPase-regulated PAR complex in this negative regulatory mechanism [gao-2002-par6-tight-junction-abstract].

These findings suggest a model in which the PAR complex serves a regulatory rather than simply structural role in tight junction dynamics. The complex may function to maintain tight junctions in a dynamic, remodeling-competent state that allows cells to respond to developmental and physiological cues requiring junction plasticity.

## TGFbeta Signaling and Epithelial-Mesenchymal Transition

A major pathway through which Par6 proteins regulate epithelial plasticity involves direct phosphorylation by TGFbeta receptors. Ozdamar et al. discovered that Par6 interacts with TGFbeta receptors at tight junctions and is directly phosphorylated by the type II TGFbeta receptor (TbetaRII) at serine 345 [ozdamar-2005-tgfbeta-par6-abstract]. This phosphorylation event is required for TGFbeta-dependent epithelial-to-mesenchymal transition (EMT) in mammary gland epithelial cells.

The mechanism underlying TGFbeta-induced EMT through Par6 involves the E3 ubiquitin ligase Smurf1. Phosphorylation of Par6 at Ser345 promotes its interaction with Smurf1, which then targets the small GTPase RhoA for ubiquitination and proteasomal degradation [ozdamar-2005-tgfbeta-par6-abstract]. Since RhoA activity is required for tight junction maintenance through actin polymerization, its localized degradation results in the dissolution of junctional complexes and the acquisition of mesenchymal characteristics. Importantly, this pathway operates independently of the canonical TGFbeta-Smad transcriptional program, representing a non-transcriptional mechanism for TGFbeta-induced cell plasticity.

This TGFbeta-Par6 axis has significant implications for cancer progression. Phosphorylation of Par6 at Ser345 has been implicated in the invasion and metastatic progression of breast cancer cells and correlates with reduced patient survival. Atypical PKC can also phosphorylate Par6 to drive EMT and increase migratory potential, suggesting that multiple kinases converge on Par6 to regulate epithelial plasticity. These findings position Par6 proteins at a critical node where polarity signaling integrates with growth factor pathways to control cell fate decisions.

## Centrosome Function and Ciliogenesis

A major advance in understanding PARD6G-specific functions came from the discovery of its role at the mother centriole. Dormoy et al. found that PARD6G localizes specifically to the mother centriole and controls the protein composition of the centrosome through a Par6alpha-dependent pathway [dormoy-2013-par6gamma-centriole-abstract]. Depletion of PARD6G resulted in dramatic changes in centrosomal protein composition, with loss of numerous proteins including centriolar components (HsSAS-6, STIL, Cep192, Cep152), appendage proteins (Cep164, Cep170, ninein), and centriolar satellite proteins (PCM-1, BBS4, Cep290). Notably, gamma-tubulin complex components remained unaffected.

The functional consequences of PARD6G depletion include severe defects in ciliogenesis, with primary cilia formation decreasing from approximately 80% in controls to approximately 10% in depleted cells [dormoy-2013-par6gamma-centriole-abstract]. Microtubule organization was also disrupted, with 77% of PARD6G-depleted cells displaying disorganized microtubule arrays. During mitosis, 83% of depleted cells exhibited aberrant multipolar spindles at 48 hours post-depletion. Cell migration was impaired due to defective centrosome reorientation in wound-healing assays.

Mechanistically, PARD6G controls centrosomal protein composition by regulating the association of Par6alpha and p150Glued (a dynactin subunit) with the centrosome [dormoy-2013-par6gamma-centriole-abstract]. PARD6G interacts specifically with Par6alpha but not Par6beta, and this interaction is critical for the downstream effects on centrosome composition. Importantly, this centrosomal function of PARD6G operates independently of the canonical PAR polarity complex, as depletion of Par3alpha or aPKC isoforms did not affect centrosomal protein composition [dormoy-2013-par6gamma-centriole-abstract].

## Signaling Pathways and Regulation of Cell Proliferation

Beyond its structural and organizational roles, PARD6G participates in signaling pathways that regulate cell proliferation, with important implications for cancer biology. Studies by Marques et al. revealed that PARD6G functions as a negative regulator of the phosphatidylinositol 3-kinase (PI3K)/phosphoinositide-dependent protein kinase 1 (PDK1)/Akt pathway [marques-2016-par6g-cancer-abstract]. Using three-dimensional mammary epithelial organoid cultures, they demonstrated that silencing of PARD6G alone was sufficient to sustain proliferation and prevent epithelial cell cycle restriction.

The signaling mechanism involves regulation of Akt activation at specific phosphorylation sites. PARD6G-deficient acinar structures retained phosphorylation of Akt at serine 473, a modification associated with full kinase activation [marques-2016-par6g-cancer-abstract]. This contrasts with PARD6B-deficient structures, which showed weak phospho-Akt signal that was enhanced by oncogenic Myc activation. These findings suggest that PARD6G normally suppresses Akt pathway activity to maintain epithelial quiescence.

The relationship between Par6 family members and mitogenic signaling pathways exhibits striking isoform specificity. While PARD6G negatively regulates the PI3K/Akt pathway, PARD6B appears to primarily activate the MAPK pathway and promote proliferation [marques-2015-par6-cancer-editorial-abstract]. This functional divergence manifests in opposite mutational patterns in human cancers: PARD6B frequently undergoes amplification and overexpression (particularly in breast cancer), while PARD6G is targeted by loss-of-function mutations including chromosomal deletions and loss of heterozygosity [marques-2016-par6g-cancer-abstract].

## Neuronal Polarity

In neurons, the PAR complex including Par6 proteins plays a central role in axon specification and dendrite development [insolera-2011-par-neuronal-polarity-abstract]. As neurons polarize, Par3 and Par6 become selectively enriched at the tip of the future axon. Disruption of this polarized distribution impairs proper axon formation. The Par6-Cdc42/Rac1 interaction is particularly important in this context, as it regulates actin cytoskeleton dynamics at the growth cone.

The neuronal polarity machinery integrates multiple signaling inputs. The PI3K/GSK3beta pathway shows selective activation at the future axon, where elevated PI3K activity suppresses GSK3beta to promote axon elongation. Wnt signaling through Dishevelled associates with the Par3/Par6/aPKC complex and stabilizes aPKC activity. Additionally, TGFbeta receptor II phosphorylates Par6 at serine 345, contributing to axon formation [insolera-2011-par-neuronal-polarity-abstract].

The PAR complex cross-regulates other polarity kinases including Par1 (MARK family kinases) and Par4 (LKB1). aPKC phosphorylates and inhibits MARK2 in developing axons, preventing MARK2-mediated phosphorylation of microtubule-associated proteins like tau [insolera-2011-par-neuronal-polarity-abstract]. This regulation promotes microtubule stability in the axon. The interplay between the PAR complex and MARK kinases represents a conserved mechanism linking polarity signaling to cytoskeletal organization.

## Expression Pattern and Tissue Distribution

PARD6G shows broad expression across human tissues with notable enrichment in certain organs. Northern blot analysis originally detected a 4.0-kb transcript at highest levels in adult and fetal kidney [noda-2001-par6-adaptor-abstract]. Additional expression was observed at lower levels in all other tissues examined, indicating widespread expression. More recent transcriptomic data from the Human Protein Atlas indicates enhanced expression in skin, with measurable levels across bone marrow and lymphoid tissues, brain, gastrointestinal tract, kidney, and many other tissues.

The relative expression levels of the three Par6 isoforms vary across tissues and cell types. In breast cancer cell lines, PARD6A and PARD6G are expressed at significantly lower levels compared to PARD6B. In hyperplastic enlarged lobular units of the breast, PARD6B shows overexpression while PARD6A and PARD6G do not, suggesting isoform-specific regulation in preneoplastic tissue changes [marques-2015-par6-cancer-editorial-abstract].

## Implications for Human Disease

The tumor suppressor function of PARD6G has significant implications for cancer biology. Analysis of tumor mutation databases reveals frequent loss-of-function alterations affecting PARD6G across multiple epithelial cancer types, including chromosomal losses, deletions, and loss of heterozygosity [marques-2016-par6g-cancer-abstract]. This contrasts sharply with PARD6B, which shows predominantly gain-of-function changes including amplification and overexpression. The opposing mutational landscapes of these paralogs suggest that cancer cells may selectively tune Par6 pathway activity, decreasing PARD6G-mediated growth suppression while increasing PARD6B-mediated proliferative signals.

The centrosomal functions of PARD6G also have disease relevance. Centrosome abnormalities are a hallmark of cancer cells and can drive chromosomal instability through multipolar spindle formation. The finding that PARD6G depletion causes multipolar spindles suggests that loss of PARD6G function could contribute to genomic instability in tumors [dormoy-2013-par6gamma-centriole-abstract]. Additionally, the role of PARD6G in ciliogenesis connects it to ciliopathies, genetic disorders caused by defective cilia function.

## Evolutionary Conservation

The PAR proteins constitute one of the most highly conserved polarity networks in metazoan biology. The PAR system was originally identified through genetic screens in Caenorhabditis elegans, where mutations in the par genes cause defects in asymmetric cell division of the one-cell embryo. Homologs of Par6, along with Par3 and aPKC, have been identified in Drosophila, vertebrates, and all other bilateral animals examined, indicating that these proteins were fundamental players in cell polarization mechanisms more than 500 million years ago.

In C. elegans, PAR-6 contains a single PDZ domain and a CRIB-like domain for GTPase binding, similar to its mammalian counterparts. The PAR-3/PAR-6/PKC-3 complex localizes to the anterior cortex of the one-cell embryo and is essential for establishing the anterior-posterior axis. In Drosophila, the Par6 homolog localizes to the apical domain of epithelial cells and is required for both epithelial polarity and asymmetric division of neuroblasts. The core biochemical interactions between Par6, Par3, aPKC, and Cdc42 are preserved across these species, although the specific biological contexts in which they function have diversified.

Despite the strong conservation of core Par6 functions, the expansion to three Par6 paralogs in mammals (PARD6A, PARD6B, PARD6G) has allowed for functional specialization. While the PB1 and PDZ domains show greater than 70% sequence similarity among the three human paralogs, the C-terminal regions diverge substantially. This divergence likely underlies isoform-specific functions such as the unique centrosomal localization of PARD6G mediated by its C-terminal domain. The evolutionary duplication and subsequent specialization of Par6 genes in mammals may have enabled more sophisticated regulation of polarity in the diverse cell types of complex organisms.

## Open Questions

Several important questions about PARD6G biology remain to be addressed:

1. **Isoform-specific targeting mechanisms:** What determines the specific localization of PARD6G to the mother centriole, and why do other Par6 isoforms not share this localization? The C-terminal region that mediates centrosomal targeting differs substantially between Par6 paralogs, but the molecular details of this targeting mechanism are unknown.

2. **Functional redundancy versus specificity:** To what extent do the three human Par6 paralogs serve redundant versus distinct functions? The centrosomal function appears specific to PARD6G, but the degree of functional overlap in other cellular contexts is unclear.

3. **Regulation of PARD6G expression and activity:** What mechanisms control PARD6G protein levels and activity in different cellular contexts? Post-translational modifications, protein stability, and transcriptional regulation remain poorly characterized.

4. **Integration with other polarity pathways:** How does PARD6G coordinate with other polarity complexes (Crumbs, Scribble) in different cellular contexts, and how does loss of PARD6G affect overall polarity network function?

5. **Therapeutic implications:** Can the tumor suppressor function of PARD6G be exploited therapeutically? Understanding whether PARD6G function can be restored or enhanced in cancers with PARD6G loss could identify new therapeutic strategies.

6. **Structural basis of isoform specificity:** High-resolution structural information specific to PARD6G is limited. Structural studies could reveal the molecular basis for isoform-specific protein interactions and functions.

## References

- **noda-2001-par6-adaptor-abstract:** Noda Y, Takeya R, Ohno S, Naito S, Ito T, Sumimoto H. Human homologues of the Caenorhabditis elegans cell polarity protein PAR6 as an adaptor that links the small GTPases Rac and Cdc42 to atypical protein kinase C. Genes to Cells. 2001 Feb;6(2):107-19. DOI: 10.1046/j.1365-2443.2001.00404.x. PMID: 11260256.

- **dormoy-2013-par6gamma-centriole-abstract:** Dormoy V, Tormanen K, Sütterlin C. Par6gamma is at the mother centriole and controls centrosomal protein composition through a Par6alpha-dependent pathway. J Cell Sci. 2013 Feb 1;126(Pt 3):860-70. DOI: 10.1242/jcs.121186. PMID: 23264737. PMCID: PMC3619814.

- **marques-2016-par6g-cancer-abstract:** Marques E, Englund JI, Tervonen TA, Virkunen E, Laakso M, Myllynen M, Mäkelä A, Ahvenainen M, Lepikhova T, Monni O, Hautaniemi S, Klefström J. Par6G suppresses cell proliferation and is targeted by loss-of-function mutations in multiple cancers. Oncogene. 2016 Mar 17;35(11):1386-98. DOI: 10.1038/onc.2015.196. PMID: 26073086. PMCID: PMC4800288.

- **garrard-2003-cdc42-par6-structure-abstract:** Garrard SM, Capaldo CT, Gao L, Rosen MK, Macara IG, Tomchick DR. Structure of Cdc42 in a complex with the GTPase-binding domain of the cell polarity protein, Par6. EMBO J. 2003 Mar 3;22(5):1125-33. DOI: 10.1093/emboj/cdg110. PMID: 12606577. PMCID: PMC150343. PDB: 1NF3.

- **peterson-2004-cdc42-allosteric-abstract:** Peterson FC, Penkert RR, Volkman BF, Prehoda KE. Cdc42 regulates the Par-6 PDZ domain through an allosteric CRIB-PDZ transition. Mol Cell. 2004 Mar 12;13(5):665-76. DOI: 10.1016/s1097-2765(04)00086-3. PMID: 15023337.

- **hirano-2005-apkc-par6-pb1-abstract:** Hirano Y, Yoshinaga S, Takeya R, Suzuki NN, Horiuchi M, Kohjima M, Sumimoto H, Inagaki F. Structure of a cell polarity regulator, a complex between atypical PKC and Par6 PB1 domains. J Biol Chem. 2005 Mar 11;280(10):9653-61. DOI: 10.1074/jbc.M409823200. PMID: 15590654. PDB: 1WMH.

- **hurd-2003-par6-pals1-abstract:** Hurd TW, Gao L, Roh MH, Macara IG, Margolis B. Direct interaction of two polarity complexes implicated in epithelial tight junction assembly. Nat Cell Biol. 2003 Feb;5(2):137-42. DOI: 10.1038/ncb923. PMID: 12545177.

- **gao-2002-par6-tight-junction-abstract:** Gao L, Joberty G, Macara IG. Assembly of epithelial tight junctions is negatively regulated by Par6. Curr Biol. 2002 Feb 5;12(3):221-5. DOI: 10.1016/s0960-9822(01)00663-7. PMID: 11839275.

- **insolera-2011-par-neuronal-polarity-abstract:** Insolera R, Chen S, Shi SH. Par proteins and neuronal polarity. Dev Neurobiol. 2011 Jun;71(6):483-94. DOI: 10.1002/dneu.20867. PMID: 21557502. PMCID: PMC3153582.

- **marques-2015-par6-cancer-editorial-abstract:** Marques E, Klefström J. Par6 family proteins in cancer. Oncoscience. 2015 Nov;2(11):894-5. DOI: 10.18632/oncoscience.255. PMID: 26909361. PMCID: PMC4675776.

- **ozdamar-2005-tgfbeta-par6-abstract:** Ozdamar B, Bose R, Barrios-Rodiles M, Wang HR, Zhang Y, Wrana JL. Regulation of the polarity protein Par6 by TGFbeta receptors controls epithelial cell plasticity. Science. 2005 Mar 11;307(5715):1603-9. DOI: 10.1126/science.1105718. PMID: 15761148.


## Citations

1. dormoy-2013-par6gamma-centriole-abstract.md
2. dormoy-2013-par6gamma-centriole-summary.md
3. gao-2002-par6-tight-junction-abstract.md
4. garrard-2003-cdc42-par6-structure-abstract.md
5. garrard-2003-cdc42-par6-structure-summary.md
6. hirano-2005-apkc-par6-pb1-abstract.md
7. hirano-2005-apkc-par6-pb1-summary.md
8. hurd-2003-par6-pals1-abstract.md
9. insolera-2011-par-neuronal-polarity-abstract.md
10. marques-2015-par6-cancer-editorial-abstract.md
11. marques-2016-par6g-cancer-abstract.md
12. marques-2016-par6g-cancer-summary.md
13. noda-2001-par6-adaptor-abstract.md
14. noda-2001-par6-adaptor-summary.md
15. ozdamar-2005-tgfbeta-par6-abstract.md
16. peterson-2004-cdc42-allosteric-abstract.md