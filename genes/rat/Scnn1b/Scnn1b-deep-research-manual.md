# Scnn1b (rat) - manual literature synthesis

No deep-research API provider was available in this session; this file is a manual
synthesis of the cached publications (`publications/PMID_*.md`) and the UniProt record
P37090 (SCNNB_RAT). Most cached papers are abstract-only; full text was available for
PMID:17562820, PMID:18308722, PMID:24419567, PMID:26297031 and PMID:27413634.

## Identity and family

- Scnn1b encodes the beta subunit of the amiloride-sensitive epithelial sodium channel
  (ENaC), member of the DEG/ENaC family (TC 1.A.6). UniProt: "This is one of the three
  pore-forming subunits of the heterotrimeric epithelial sodium channel (ENaC), a critical
  regulator of sodium balance and fluid homeostasis" [UniProtKB:P37090 CC:FUNCTION].
- Topology: cytoplasmic N-terminus (1-50), TM1 (51-71), large extracellular domain
  (72-530, cysteine-rich, N-glycosylated), TM2 (531-551), cytoplasmic C-terminus with a
  PY motif (614-618) [UniProtKB:P37090 FT].
- The rat beta subunit was cloned by functional complementation of alpha-ENaC in Xenopus
  oocytes [PMID:8107805 "Here we identify two other subunits (beta and gamma) by
  functional complementation of the alpha-subunit of the rat epithelial Na+ channel"].

## Channel activity and complex

- alpha, beta and gamma together reconstitute the native channel's selectivity, gating and
  amiloride pharmacology [PMID:8107805 "The ion-selective permeability, the gating
  properties and the pharmacological profile of the channel formed by coexpressing the
  three subunits in oocytes are similar to that of the native channel."].
- Stoichiometry: pore-lining mutants support 2alpha:1beta:1gamma around a central pore
  [PMID:17562820 "Our results support a tetrameric arrangement of ENaC subunits where
  2alpha, 1beta, and 1gamma come together around central pore."]. Current consensus from
  cryo-EM of human ENaC (not cached here) is a 1:1:1 heterotrimer; UniProt states
  heterotrimer.
- Biochemical association of subunits [PMID:12136275 "Co-immunoprecipitation studies with
  FLAG-tagged ENaC subunits suggest that during dissociation of ENaC tetramers the
  composition of dimers is completely random."].
- A conserved N-terminal glycine (G37 in human beta; PHA-1 mutation) controls gating
  (open probability) without changing conductance or selectivity [PMID:9118951 "Single
  channel conductances and ion selectivities of the mutant channels were identical to that
  of wild-type."].
- ENaC is a constitutively active channel; it is not gated by a canonical agonist. Its
  activity is set by surface number and open probability, modulated by proteolysis of
  alpha/gamma, Na+ self-inhibition, and kinases [PMID:24419567 "Proteolytic processing of
  external domains and inhibition with increased sodium concentrations are important
  regulatory features of epithelial sodium channel complexes expressed in the distal
  nephron."]. A cGMP analog activates the channel externally [PMID:20007351 "8-pCPT-cGMP
  may serve as a novel ENaC ligand in addition to activating PKG signal"], but this is
  pharmacological, not a physiological ligand gate.

## Regulation via the beta C-terminus

- The beta PY motif binds NEDD4 WW domains [PMID:8665844 "Our yeast two-hybrid and in vitro
  binding studies revealed that the rNedd4-WW domains mediate this association by binding
  to the P2 regions, which include the PY motifs (XPPXY) of either betarENaC (PPPNY) or
  gammarENaC (PPPRY)."]; NMR of WW(II+III) with the beta P2 peptide [PMID:9923703].
- Deletion of the beta PY motif (Liddle syndrome) hyperactivates the channel [PMID:8665844].
- ERK sites (beta T613) and the PY motif mediate cAMP- and progesterone-dependent
  regulation [PMID:16476738; PMID:16172119].
- CK2 phosphorylates beta S631; loss of the CK2 sites strongly reduces ENaC current, and the
  requirement disappears when the Nedd4-2 pathway is removed [PMID:18308722 "Phosphorylation
  by CK2 is essential for ENaC activation, and to a lesser degree, it also controls membrane
  expression of alphabetagamma-ENaC."; "Channels lacking the Nedd4-2 binding motif in
  beta-ENaC (R561X, Y618A) no longer required the CK2 site for channel activity"].
- The beta C-terminus contributes to Cl(-)-dependent inhibition [PMID:16027156 "The results
  confirm a role of the carboxyl terminus of betaENaC for Cl(-)-dependent inhibition of the
  Na+ channel"].

## Localization

- Rat kidney: all three subunits in CNT/CD principal cells; beta and gamma largely
  intracellular in cortex; immuno-EM shows apical membrane and intracellular vesicles
  [PMID:11352848 "Immunoelectron microscopy confirmed the presence of ENaC subunits in both
  the apical plasma membrane and intracellular vesicles."].
- MDCK cells: apical, not basal [PMID:11773057 "we demonstrated apical, but not basal,
  membrane localization of ENaC in these cells"]; rapid surface turnover (t1/2 ~1 h).
- Regulated apical targeting in nephrotic rats [PMID:15075188], hypoxia-reduced and
  beta2-agonist-increased apical abundance in alveolar cells [PMID:12372821; PMID:24093724],
  vasopressin increases intracellular beta/gamma pool [PMID:16528252].
- Non-epithelial expression: VSMC [PMID:16844921; PMID:18024548], nodose baroreceptor
  neurons [PMID:26297031], PC12 cells [PMID:16192303], cytotrophoblasts [PMID:24553299].

## Physiology

- ENaC is the rate-limiting step of Na+ reabsorption in distal nephron, distal colon,
  exocrine ducts and lung [PMID:8107805 "The amiloride-sensitive epithelial sodium channel
  constitutes the rate-limiting step for sodium reabsorption in epithelial cells that line
  the distal part of the renal tubule, the distal colon, the duct of several exocrine
  glands, and the lung."].
- Loss of function of beta causes PHA-1 salt wasting; gain of function (PY deletion) causes
  Liddle hypertension [PMID:9118951; PMID:8665844].
- Mouse transgenic overexpression of beta-ENaC in airway (Scnn1b-Tg) produces
  airway-surface-liquid depletion, mucus obstruction and neutrophilic inflammation - a
  gain-of-function disease model, not a normal role of beta-ENaC in mucus secretion or
  neutrophil activity (background knowledge; not cached). UniProt notes "This subunit is
  not essential for ENaC function in airway surface liquid homeostasis and proper mucus
  clearance" [UniProtKB:P37090 CC:FUNCTION, by similarity to mouse].
- Many rat studies report expression changes (salt diet, aldosterone, testosterone,
  hypoxia, ischemia, NGF) that are responses of the gene's expression, not activities of
  the protein.
