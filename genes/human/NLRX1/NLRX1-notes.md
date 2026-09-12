# NLRX1 (NLR family member X1; NOD5/NOD9; CLR11.3) — review notes

UniProt: Q86UT6 (NLRX1_HUMAN), 975 aa precursor, HGNC:29890. N-terminal mitochondrial
transit peptide (1-86); NACHT NTPase domain (160-483); C-terminal LRR region (667-975).
Homohexamer (homodimers trimerize). PDB 3UN9 (LRR/RNA-binding element).

## Summary of function

NLRX1 is an atypical NOD-like receptor (NLR) that, unlike most NLRs, localizes to the
mitochondrion (outer membrane, with the transit peptide targeting it to mitochondria;
the C-terminal LRR has an RNA-binding element). It is a mitochondrial regulator that sits
at the intersection of antiviral signaling, autophagy/mitophagy, ROS, and inflammasome
control.

Core/established functions:
1. Negative regulation of MAVS-mediated (RIG-I/RLH) antiviral signaling. NLRX1 localizes
   to the mitochondrial outer membrane and interacts with MAVS, inhibiting the virus-induced
   RIG-I-like-helicase-MAVS interaction and dampening type I interferon induction
   [PMID:18200010 "human NLRX1 ... localizes to the mitochondrial outer membrane and interacts with MAVS. Expression of NLRX1 results in the potent inhibition of RLH- and MAVS-mediated interferon-beta promoter activity and in the disruption of virus-induced RLH-MAVS interactions. Depletion of NLRX1 ... promotes virus-induced type I interferon production"].
2. Promotion of autophagy via TUFM. NLRX1 binds the mitochondrial elongation factor TUFM,
   which in turn recruits the autophagy proteins ATG5-ATG12 (ATG16L1), linking NLRX1 to
   autophagy induction and modulation of type I IFN [UniProt FUNCTION; PMID:22749352
   "The mitochondrial proteins NLRX1 and TUFM form a complex that regulates type I interferon and autophagy"].
   The TUFM interaction is also captured by the cached PMID:28611246 (TUFM as a host
   restriction factor against avian influenza, correlated with autophagy), where NLRX1-TUFM
   is the IPI partner in the GOA. NLRX1 is thus a mitochondrial regulator of autophagy/mitophagy
   (TUFM/ATG5-ATG12).
3. Regulation of MAVS-dependent NLRP3 inflammasome activation / attenuation of apoptosis
   and inflammation. NLRX1 inhibits MAVS-dependent NLRP3 inflammasome activation, reducing
   IL-1beta/IL-18/IL-6 and apoptosis (shown in myocardial ischemia)
   [PMID:27393910 "NLRX1 ... regulated MAVS-dependent NLRP3 inflammasome activation ... NLRX1 overexpression significantly inhibited hypoxia-induced up-regulation of MAVS, NLRP3 and Caspase-1 expression"].
4. ROS and NF-kB/JNK modulation. NLRX1 has no inhibitory function on NF-kB itself but
   amplifies NF-kB and JNK signaling through ROS production [UniProt FUNCTION; PMID:18219313].
   Note the GOA carries an IBA "negative regulation of canonical NF-kappaB signal transduction"
   transferred from the mouse ortholog - this is contested (UniProt explicitly states NLRX1
   "Has no inhibitory function on NF-kappa-B signaling pathway, but enhances NF-kappa-B and
   JUN N-terminal kinase dependent signaling through the production of reactive oxygen species").

## Localization
Mitochondrion / mitochondrial outer membrane (transit peptide; multiple EXP/IDA/HTP/IBA/TAS).
The Reactome cytosol annotation (R-HSA-9749471, "NLRX1 binds CHUK:IKBKB:IKBKG") reflects a
pathway-step model; NLRX1's dominant localization is the mitochondrion. Mitochondrion is the
core compartment.

## Annotation assessment highlights
- Mitochondrial outer membrane (GO:0005741) and mitochondrion (GO:0005739): ACCEPT (core),
  across EXP/IDA/IBA/HTP/TAS evidence.
- negative regulation of RIG-I signaling pathway (GO:0039536, IBA): ACCEPT - core antiviral
  function (corroborated by experimental PMID:18200010 disrupting RLH-MAVS).
- negative regulation of canonical NF-kappaB signal transduction (GO:0043124, IBA): contested.
  UniProt (human) says NLRX1 has no inhibitory NF-kB function and instead enhances NF-kB via
  ROS. The IBA term is transferred from the mouse ortholog. Given the human-specific UniProt
  statement and that this is an unverified phylogenetic inference, mark MARK_AS_OVER_ANNOTATED
  (do not REMOVE - the mouse ortholog evidence is real and per guidelines IBA over-propagation
  can be argued against but the direction is genuinely disputed in the literature).
- protein binding (GO:0005515) IPI with TUFM (PMID:28611246) and SARM1 (PMID:21903422):
  KEEP_AS_NON_CORE; the TUFM interaction underpins the autophagy function but bare protein
  binding is uninformative.
- cytosol (GO:0005829 TAS Reactome): KEEP_AS_NON_CORE (pathway-step; mitochondrion is core).

## Functions NOT yet annotated (candidate NEW)
- Interaction with TUFM and recruitment of ATG5-ATG12 to promote autophagy (PMID:22749352)
  is in UniProt FUNCTION but not yet a GO BP annotation in the GOA - candidate for a
  positive regulation of autophagy / regulation of mitophagy NEW annotation.
- negative regulation of MAVS/type I IFN is the experimental core (PMID:18200010) but the
  GOA only carries the IBA RIG-I term and Reactome.
