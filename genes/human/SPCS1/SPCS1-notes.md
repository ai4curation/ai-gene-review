# SPCS1 (Signal peptidase complex subunit 1) — review notes

UniProt: Q9Y6A9 (SPCS1_HUMAN); aka SPC12, "Microsomal signal peptidase 12 kDa subunit". 169 aa, multi-pass ER membrane protein (two TM helices, residues 94-114 and 116-136). HGNC:23401, gene on chr 3.

## Core identity and function
SPCS1 is one of the three **non-catalytic accessory subunits** (SPCS1, SPCS2, SPCS3) of the eukaryotic ER **signal peptidase complex (SPC)**. The catalytic subunits are SEC11A (SPC-A) or SEC11C (SPC-C). SPCS1 is **dispensable for SPC enzymatic (peptidase) activity**.

- UniProt FUNCTION: "Component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum (PubMed:34388369). Dispensable for SPC enzymatic activity (By similarity)." [UniProt Q9Y6A9]
- UniProt SUBUNIT: "Component of the signal peptidase complex paralog A (SPC-A) composed of a catalytic subunit SEC11A and three accessory subunits SPCS1, SPCS2 and SPCS3 ... Within the complex, interacts with SPCS2 and SPCS3 (PubMed:34388369). The complex induces a local thinning of the ER membrane which is used to measure the length of the signal peptide (SP) h-region of protein substrates."
- Cryo-EM structure of human SPC: [PMID:34388369 "Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage"] establishes SPCS1 as a structural component of the complex and reports phosphorylation.
- Membrane topology established in [PMID:8632014 "Membrane topology of the 12- and the 25-kDa subunits of the mammalian signal peptidase complex"].

So core function = SPC complex membership (GO:0005787), signal peptide processing / protein processing involvement (GO:0006465 / GO:0016485), ER membrane localization (GO:0005789). NOT a catalytic MF.

## Secondary / non-core: viral (flavivirus + HCV) processing
SPCS1 was identified in CRISPR/host-factor screens as required for flavivirus and HCV propagation. This is a host-factor role hijacked by viruses; secondary, not the core cellular function.

- HCV: [PMID:24009510] "identified signal peptidase complex subunit 1 (SPCS1) ... Silencing of endogenous SPCS1 resulted in markedly reduced production of infectious HCV ... SPCS1 was found to interact with both NS2 and E2 ... SPCS1 plays a key role in the formation of the membrane-associated NS2-E2 complex." Note: in this paper, "Propagation of Japanese encephalitis virus was not affected by knockdown of SPCS1" — i.e. virion-assembly role here is HCV-specific via NS2/E2 interaction.
- Flaviviruses (CRISPR screen): [PMID:27383988 "A CRISPR screen defines a signal peptide processing pathway required by flaviviruses"] — SPCS1 required; "Plays a key role in the post-translational processing of flaviviral structural proteins prM, E, and NS1" (UniProt).
- JEV: [PMID:29593046] "The loss of SPCS1 function markedly reduced intracellular virion assembly and the production of infectious JEV particles but did not affect cell entry, RNA replication, or translation ... SPCS1 was found to interact with nonstructural protein 2B (NS2B) ... thereby influencing the posttranslational processing of JEV proteins and the assembly of virions." (Note: contradicts the HCV paper's statement that JEV is unaffected; later work supports a JEV role.)

## Annotation assessment summary
- GO:0005787 signal peptidase complex (IBA, IEA, IPI, TAS) — CORE, ACCEPT. Multiple lines.
- GO:0005789 ER membrane (IDA, IEA, ISS, TAS) — CORE localization, ACCEPT.
- GO:0016020 membrane (IEA, InterPro) — generic parent of ER membrane; KEEP_AS_NON_CORE (less informative).
- GO:0045047 protein targeting to ER (IBA) — SPC acts at the ER on translocated substrates; the IBA term is somewhat broad but defensible as involvement; KEEP_AS_NON_CORE (more accurate process is signal peptide processing).
- GO:0016485 protein processing (IDA, ComplexPortal) — ACCEPT; reflects SP cleavage. (GO:0006465 signal peptide processing is the more specific term; ComplexPortal also annotates GO:0006465 per UniProt DR line.)
- GO:0006508 proteolysis (TAS) — generic; the complex is a peptidase but SPCS1 itself is non-catalytic. KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED — it's a parent of signal peptide processing and SPCS1 is not catalytic. Keep as non-core.
- GO:0005515 protein binding (IPI x several) — KEEP_AS_NON_CORE (bare protein binding, uninformative). Interactions with SPCS2/SPCS3 (intra-complex) and with viral proteins.
- GO:0019068 virion assembly (IMP, PMID:24009510 HCV; PMID:29593046 JEV) — viral host-factor; KEEP_AS_NON_CORE.
- GO:0019082 viral protein processing (IMP, PMID:27383988) — viral host-factor; KEEP_AS_NON_CORE.

## Falcon deep-research findings (incorporated 2026-06)

- SPCS1 facilitates HCV assembly specifically by enhancing SPC-mediated processing of the suboptimal **E2-p7 junction**; loss of SPCS1 impairs E2-p7 separation, and engineering efficient E2/p7 separation makes SPCS1 dispensable for assembly [PMID:35130329 "loss of SPCS1 specifically impairs the HCV E2-p7 processing by the SPC ... efficient separation of E2 and p7 ... leads to SPCS1 dispensable for HCV assembly"]. This establishes a **common mechanism** with flavivirus C-prM processing: SPCS1 exquisitely regulates SPC cleavage at specific, suboptimal target sites [PMID:35130329 "common role of SPCS1 in Flaviviridae family virus propagation as to exquisitely regulate the SPC-mediated processing of specific, suboptimal target sites"]. (Verified PubMed; not cached.)
- Independent CRISPR screen in **placental trophoblasts** validated SPCS1 as essential for **Zika virus** replication, with host factors enriched in the ER membrane complex and signal peptide processing pathway [PMID:33577859 "signal peptidase complex subunit 1 (SPCS1) is crucial for virus replication in trophoblasts"]. Adds a trophoblast/placental disease context (microcephaly, vertical transmission) to the flavivirus host-factor role. (Verified PubMed; not cached.)
- Falcon emphasizes a structural model (Liaci et al. 2021 = PMID:34388369, already cited as the cryo-EM paper) in which all subunits including SPCS1 contribute to a transmembrane "window" that locally thins the ER bilayer (~26% thinning in simulations) — a molecular ruler discriminating short signal-peptide h-regions (mean ~11 aa) from longer TM helices (>18-20 aa excluded). Consistent with existing review; no new reference needed.
- Falcon cites a 2024 yeast study (Chung et al. = PMID:39565596) showing the accessory subunit Spc2/SPCS2 modulates substrate and cleavage-site selection via membrane thinning — relevant to the general accessory-subunit fidelity concept but specific to SPCS2, not SPCS1; logged in the SPCS2 review instead.
- Falcon's "SPC-as-quality-control-enzyme" framing (SPCS1 as a recruitment/exosite factor for noncanonical membrane-protein cleavage, ~1500 cryptic-site substrates, ERAD/Hrd1 coupling) derives from Zanotti 2023, a Heidelberg PhD thesis (doi:10.11588/heidok.00033417) with no PMID and not peer-reviewed primary literature. Interesting hypothesis but NOT added as a reference (unverifiable as a PMID; thesis-level evidence). Noted here only.
- Review-level/background sources (Verhaegen & Vermeire 2024 npj Viruses ER/flavivirus review; Kanojia 2022 flavivirus CRISPR review) reinforce SPC/SPCS1 as a druggable host-directed antiviral target (e.g. cavinafungin inhibits signal peptidase), but are background reviews not adding gene-specific SPCS1 findings beyond what is already captured; not added.
