# BIK1 (BOTRYTIS-INDUCED KINASE 1, AT2G39660, UniProt O48814) — research notes

Research journal for the GO annotation review of *Arabidopsis thaliana* BIK1. Provenance recorded inline as [PMID:xxxx "verbatim quote"].

## Identity and architecture

- BIK1 is a receptor-like cytoplasmic kinase (RLCK, subfamily VII) — a genuine, catalytically active Ser/Thr (dual-specificity) protein kinase. UniProt: "RecName: Full=Serine/threonine-protein kinase BIK1"; EC=2.7.11.1; 395 AA; Protein kinase domain 67-356; ATP-binding Lys-105; active-site (proton acceptor) Asp-202.
- Lipid-anchored at the plasma membrane: N-myristoyl Gly-2 and S-palmitoyl Cys-4. Gly-2 mutations mislocalize the protein [PMID:26021844 myristoylation at Gly-2; G->S "Drastic reduction of plasma membrane localization and strong increase of cytoplasmic localization."].
- Dual-specificity kinase: [PMID:24104392 "we identified nineteen in vitro autophosphorylation sites of BIK1 including three phosphotyrosine sites, thereby proving BIK1 is a dual-specificity kinase for the first time."]. Catalytic activity (EC 2.7.11.1) experimentally established [PMID:24104392, PMID:32846426].

## Core function: immune signaling hub downstream of cell-surface PRRs

- Central RLCK that relays PTI signaling from PRR–BAK1 complexes: [PMID:20018686 "we identified the receptor-like cytoplasmic kinase BIK1 that is rapidly phosphorylated upon flagellin perception, depending on both FLS2 and BAK1. BIK1 associates with FLS2 and BAK1 in vivo and in vitro. BIK1 is phosphorylated by BAK1, and BIK1 also directly phosphorylates BAK1 and FLS2 in vitro."], and [PMID:20018686 "bik1 mutants are compromised in diverse flagellin-mediated responses and immunity ... BIK1 is an essential component in MAMP signal transduction, which links the MAMP receptor complex to downstream intracellular signaling."].
- Trans-phosphorylation order: [PMID:20018686 "BIK1 is likely first phosphorylated upon flagellin perception and subsequently transphosphorylates FLS2/BAK1 to propagate flagellin signaling."].
- BIK1 integrates signaling from multiple immune receptors and is targeted by a Pseudomonas effector (title PMID:20413097). Phosphorylated at Ser-236 by FLS2-complex.
- UniProt FUNCTION: "Plays a central role in immune responses ... Involved in pathogen-associated molecular pattern (PAMP)-triggered immunity (PTI) signaling, including calcium signaling, and defense responses downstream of FLS2."

## Core function: phosphorylation of RBOHD and ROS regulation

- BIK1 directly phosphorylates the NADPH oxidase RBOHD to drive the ROS burst: [PMID:24629339 "the receptor-like cytoplasmic kinase BIK1, a component of the FLS2 immune receptor complex, not only positively regulates flg22-triggered calcium influx but also directly phosphorylates the NADPH oxidase RbohD at specific sites in a calcium-independent manner to enhance ROS generation."], and [PMID:24629339 "BIK1 and RbohD form a pathway that controls stomatal movement in response to flg22, thereby restricting bacterial entry into leaf tissues."].
- Specific RBOHD sites: [PMID:29649442 "BIK1 directly interact and phosphorylate RBOHD at S39, S339, and S343 sites to modulate ROS level"].

## Core function: phosphorylation of Ca2+ channel OSCA1.3 / stomatal immunity

- [PMID:32846426 "the immune receptor-associated cytosolic kinase BIK1 interacts with and phosphorylates the N-terminal cytosolic loop of OSCA1.3 within minutes of treatment with the peptidic PAMP flg22"], and [PMID:32846426 "BIK1-mediated phosphorylation on its N terminus increases this channel activity. Notably, OSCA1.3 and its phosphorylation by BIK1 are critical for stomatal closure during immune signalling."].
- Phosphorylation depends on kinase activity: [PMID:32846426 "This phosphorylation is dependent on BIK1 kinase activity, since a kinase-dead variant, GST–BIK1(KD), did not phosphorylate OSCA1.3-loop1"].
- BIK1/PBL1 required for MAMP/DAMP-induced calcium elevations: [PMID:25522736 "besides PBL1, another RLCK, Botrytis-induced kinase 1 (BIK1), is also required for MAMP/DAMP-induced calcium elevations."], and [PMID:25522736 "PBL1 and BIK1 ... are required for MAMP/DAMP-induced calcium signaling."].

## Defense response / hormone regulation

- Original identification: required for resistance to necrotrophs, negative regulator of basal resistance to Pst, modulates SA: [PMID:16339855 "Inactivation of BIK1 causes severe susceptibility to necrotrophic fungal pathogens but enhances resistance to a virulent strain of the bacterial pathogen Pseudomonas syringae pv tomato."], and [PMID:16339855 "BIK1 is membrane-localized, suggesting possible involvement in early stages of the recognition or transduction of pathogen response."]. The IEP "response to fungus" annotation derives from: [PMID:16339855 "the Arabidopsis thaliana BOTRYTIS-INDUCED KINASE1 (BIK1) gene that is transcriptionally regulated by Botrytis cinerea infection."].
- JA/SA regulation via nuclear WRKY phosphorylation: [PMID:29649442 "EFR regulates the phytohormone jasmonic acid (JA) through direct phosphorylation of a receptor-like cytoplasmic kinase, BIK1."], and [PMID:29649442 "BIK1 also localizes to the nucleus and interacts directly with WRKY transcription factors involved in the JA and salicylic acid (SA) regulation. These findings demonstrate the mechanistic basis of signal transduction from PRR to phytohormones, mediated through a PRR-BIK1-WRKY axis."].

## Subcellular localization assessment

- **Plasma membrane** is the principal, well-supported location (lipid anchor; multiple focused studies): UniProt SUBCELLULAR LOCATION "Cell membrane ... Lipid-anchor". Supported by [PMID:16339855], [PMID:26021844], [PMID:29649442], [PMID:32404997], and the OSCA paper EXP annotation [PMID:32846426].
- **Nucleus** is supported by a focused study with a mechanism (activation-dependent relocation): [PMID:29649442 "in addition to its documented plasma membrane localization, BIK1 also localizes to the nucleus"]; UniProt Note "Linked to the plasma membrane when inactivated, but moves to the nucleus upon pathogen-mediated activation by phosphorylation."
- **Endosome / endosome membrane / endomembrane** supported by ligand-induced internalization study [PMID:32404997 monoubiquitination and internalization "into endocytic compartments"]. UniProt "Endosome membrane".
- **Nucleolus (GO:0005730), cytoplasm (GO:0005737, HDA), Golgi (GO:0005794, HDA), mitochondrion (GO:0005739, ISM)** are from generic high-throughput / predictive sources, NOT focused BIK1 studies:
  - Nucleolus + cytoplasm + nucleus HDA all come from a high-throughput GFP-ORF transient-expression localization screen: [PMID:15610358 "we have used a selection of trimmed ORFs ... defined the localization patterns of 155 fusion proteins. These patterns have been classified into five main categories, including cytoplasmic, nuclear, nucleolar, organellar and endomembrane compartments."]. This GFP-ORF fusion overexpression assay bypasses native N-myristoylation/palmitoylation membrane targeting and is unreliable for an endogenously membrane-anchored kinase. Nucleolar localization has never been substantiated by any focused BIK1 study.
  - Golgi HDA is from a global membrane-protein correlation-profiling proteomics survey: [PMID:28887381 "Global Analysis of Membrane-associated Protein Oligomerization Using Protein Correlation Profiling."] — not a localization claim specific to BIK1 biology.
  - Mitochondrion is ISM (sequence-model prediction, GO_REF:0000122 "AtSubP analysis") with no experimental support and is inconsistent with the myristoyl/palmitoyl PM anchor.

## Developmental / growth-defense tradeoff (non-core)

- bik1 has pleiotropic growth phenotypes: [PMID:16339855 "bik1 mutants show altered root growth, producing more and longer root hairs, demonstrating that BIK1 is also required for normal plant growth and development."]. UniProt DISRUPTION PHENOTYPE: "Altered growth traits, early flowering, weak stems, small siliques and reduced fertility."
- Opposing role with ERECTA in development; BIK1 phosphorylates ER: [PMID:31803215 "BIK1 interacts with ER-family proteins and directly phosphorylates ER."]. (Basis for one of the protein-binding IPI annotations.)
- Negative regulator of brassinosteroid signaling via BRI1 interaction [PMID:23818580 title]; ethylene signaling via EIN3 destabilization [PMID:26021844].

## Protein-binding (IPI) annotations

BIK1 has many GO:0005515 "protein binding" IPI annotations citing interaction studies. The specific, informative relationships captured by these papers are: FLS2/BAK1 (PMID:20018686, PMID:20404519, PMID:20413097), PEPR1 (PMID:23431184), BRI1 (PMID:23818580), RBOHD (PMID:24629339), CPK28 (PMID:25525792), PP2C38 (PMID:27494702), EFR + WRKY TFs (PMID:29649442), ERECTA (PMID:31803215), the AvrAC/XopAC complex (DOI:10.1038/s41586-020-2210-3 references). Bare "protein binding" is uninformative and should not be treated as a core molecular function; the relevant kinase-substrate / receptor-association relationships are captured in the MF kinase term and the BP signaling terms. Per project guidelines, bare protein binding is demoted (MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE), not removed (these are real IPI experimental annotations).

## Summary of curation decisions

- Kinase activity terms (GO:0004672, GO:0004674, GO:0106310, GO:0016301) and ATP binding (GO:0005524): ACCEPT (active kinase, experimentally proven; specific Ser/Thr kinase activity is core).
- protein phosphorylation (GO:0006468), protein autophosphorylation (GO:0046777): ACCEPT/KEEP — autophosphorylation is a real PTM but mechanistic detail; protein phosphorylation (of RBOHD/OSCA1.3/FLS2/BAK1/WRKY/ER) is core.
- PTI/immune signaling BP terms (GO:0002221, GO:0002237, GO:0042742, GO:0050832, GO:1900424): ACCEPT (core immune function).
- Stomatal movement (GO:0010119): ACCEPT/KEEP (real, OSCA1.3-RBOHD pathway).
- Hormone regulation (GO:0080141 JA, GO:0080142 SA), response to fungus (GO:0009620): KEEP_AS_NON_CORE (downstream/regulatory, supported but not the primary biochemical function).
- PM (GO:0005886), endosome/endomembrane (GO:0010008, GO:0005768, GO:0012505), nucleus (GO:0005634): ACCEPT/KEEP (supported by focused studies).
- Nucleolus (GO:0005730): MARK_AS_OVER_ANNOTATED — only from a generic GFP-ORF overexpression screen, never substantiated; biologically implausible for a membrane-anchored kinase.
- Cytoplasm (GO:0005737), Golgi (GO:0005794): KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED — generic high-throughput, weakly supported.
- Mitochondrion (GO:0005739, ISM): REMOVE — pure sequence-model prediction (AtSubP), contradicted by PM lipid-anchor and all experimental localization data.
- protein binding (GO:0005515, IPI x many): KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED — real interactions but uninformative as bare MF; specifics captured elsewhere.
