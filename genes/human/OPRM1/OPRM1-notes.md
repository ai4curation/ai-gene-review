# OPRM1 (mu-opioid receptor, MOR, µOR) - curation notes

UniProt: P35372 (human). Class A (rhodopsin-like) GPCR, opioid receptor family.

## Deep research status

- 2026-10-23: `just deep-research-falcon human OPRM1 --fallback perplexity-lite` was run twice and
  failed both times: falcon returned `403 Forbidden` ("Edison API request failed: Failed to authenticate")
  and the perplexity-lite fallback was unavailable ("Provider 'perplexity' not available"). No
  deep-research file exists. This review is based on the UniProt record, the cached publications
  for the GOA references, the Reactome entries and the Deutsch et al. 2026 paper (PMID:42870023).

## Core biology

- Receptor for endogenous opioid peptides and opiate drugs. UniProt: "Receptor for endogenous opioids
  such as beta-endorphin and endomorphin" and "Receptor for natural and synthetic opioids including
  morphine, heroin, DAMGO, fentanyl" [file:human/OPRM1/OPRM1-uniprot.txt].
- Primary drug target: "The mu opioid receptor is the primary site of action for the most commonly used
  opioids, including morphine, heroin, fentanyl, and methadone." [PMID:9689128]
- Cloning of human MOR: "The expressed mu OR1 recognized tested opiate drugs and opioid peptides in a
  sodium- and GTP-sensitive fashion" and "Effects on cyclic AMP are similar to those noted for the rat
  mu opiate receptor." [PMID:7905839]. Mestek et al.: "This receptor displays functional coupling to a
  recently cloned G-protein-activated K+ channel." [PMID:7891175]
- G protein coupling: UniProt says the activity is "predominantly coupled to pertussis toxin-sensitive
  G(i) and G(o) G alpha proteins" [file:human/OPRM1/OPRM1-uniprot.txt]. Downstream: inhibition of
  adenylate cyclase, inhibition of N- and L-type Ca channels, activation of GIRK channels, MAPK/ERK,
  PLC (mostly By similarity in UniProt).
- beta-endorphin: A118G (N40D) variant binds beta-endorphin ~3x more tightly and "β-endorphin is
  approximately three times more potent at the A118G variant receptor than at the most common allelic
  form in agonist-induced activation of G protein-coupled potassium channels" [PMID:9689128].
  This is the IMP basis for GO:0004979.

## New mechanism paper: Deutsch et al. 2026 (PMID:42870023)

- smFRET of the Gαi alpha-helical domain (AHD) in µOR–Gi complexes (note: mouse µOR with human
  Gαi1β1γ2; "Mouse μOR was expressed in Sf9 insect cells").
- "The μ-opioid receptors (μORs) are G-protein-coupled receptors (GPCRs) that mediate analgesia and
  reward responses to common opioid drugs by catalyzing guanine nucleotide exchange in heterotrimeric
  Gi proteins" [PMID:42870023].
- Efficacy encoded in G protein dynamics: "This ligand-induced low-FRET occupancy was strongly
  correlated with in vitro GTP turnover activity (a direct measure of efficacy)"; "the apparent rate of
  AHD opening being approximately 2.25-fold faster for LFT-occupied compared to apo-occupied complexes";
  "Full agonists promote AHD opening, facilitating GDP release and, therefore, efficient GTP binding."
  "In contrast, partial agonists restrict open-state occupancy, favoring GDP retention or rebinding"
  [PMID:42870023].
- Significance for GO: directly supports the GEF-like core activity captured by GO:0004930/GO:0004985
  (GPCR activity = activating an associated heterotrimeric G protein by promoting GDP/GTP exchange),
  and G-protein alpha-subunit binding. Does not need a new term. Interesting question: whether GO
  should represent agonist efficacy (partial vs full) - no; that's a ligand property.

## Isoforms

- MOR1K (isoform 12, 6TM): "this 6TM receptor is not expressed at the cell membrane, but instead is
  retained in the intracellular compartment"; "unlike MOR1, which couples to the inhibitory Galphai/o
  complex, MOR1K couples to the stimulatory Galphas complex." [PMID:20525224]. Basis of the cytoplasm
  EXP annotation.
- SV1/SV2 (isoforms 16/17) do not bind [3H]diprenorphine and reduce MOR binding via heterodimers
  [PMID:16580639].
- hMOR-1O/1X: "When transfected into CHO cells, both variants showed high selectivity for mu opioids in
  binding assays." [PMID:12589820]

## Interactors (protein binding IPI rows)

- FLNA: "The carboxyl tail of the human mu opioid receptor was shown to bind the carboxyl terminal region
  of human filamin A" - needed for agonist-induced downregulation/trafficking [PMID:14573758].
- RANBP9 (RanBPM): "RanBPM constitutively associates with MOP"; reduces internalization [PMID:19788913].
- WLS/GPR177: interacts; morphine blocks Wnt2 secretion from MOR-expressing HEK293 [PMID:20214800].
  I could not find Gα binding data in this full text, though UniProt cites it for G-protein
  alpha-subunit binding IDA; the claim itself is correct (structures, IBA).
- Y2H/MYTH screens: SIAH1/2, COPS5, VAPA, AUP1, DOK4, ZYX, GJA4 [PMID:23840749]; Sokolina 2017
  MYTH [PMID:28298427]; RAMP1/2/3 bead array screen [PMID:39083597].
- PENK Met-enkephalin peptide (PRO_0000008243) from PMID:23597562 (FGFR inhibitor paper, likely a
  selectivity panel) - this is a ligand-receptor interaction; maps to neuropeptide binding.

## Decisions summary

- Core MF: G protein-coupled opioid receptor activity (incl. beta-endorphin and morphine receptor
  activities); core BP: opioid receptor signaling pathway / adenylate cyclase-inhibiting GPCR signaling;
  location: plasma membrane (plus neuronal compartments, endosomes after internalization).
- REMOVE: voltage-gated calcium channel activity (MOR inhibits VGCCs via Gβγ, it is not a channel) and
  the derived calcium ion transmembrane transport IEA; protein binding rows (uninformative).
- MODIFY: GPCR activity -> opioid receptor activity; GPCR signaling -> opioid receptor signaling;
  acetylcholine-specific AC-inhibiting pathway and "cyclic nucleotide second messenger" ->
  adenylate cyclase-inhibiting GPCR signaling pathway (GO:0007193); sensory perception -> sensory
  perception of pain; membrane -> plasma membrane.
- Over-annotation: lung cancer cell proliferation; "regulation of cellular response to stress" (the
  Ray 2011 study found OPRM1 Asp40 associated with cue-induced, not stress-induced craving:
  "The Asp40 allele of the OPRM1 was associated with greater cue-induced alcohol craving following
  the neutral imagery condition." [PMID:21039637]); ER/Golgi from Sf9 overexpression; transmission of
  nerve impulse; positive regulation of neurogenesis.
