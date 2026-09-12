# tartan (trn) — curation notes

UniProt: M9PFH7 (isoform B, 751 aa) · FlyBase: FBgn0010452 · CG11280 · *Drosophila melanogaster* (NCBITaxon:7227)

## Protein architecture (from UniProt M9PFH7)

- Single-pass type I transmembrane protein: N-terminal signal peptide (1–20), large
  extracellular leucine-rich-repeat (LRR) ectodomain, one predicted transmembrane helix
  (442–463), and a short cytoplasmic tail with a disordered/low-complexity C-terminus (713–739).
- Ectodomain is built from ~10 typical LRR units (SMART SM00369 ×10) capped by an
  LRR C-terminal cysteine-rich domain (LRRCT, 382–434), matching InterPro IPR001611
  (Leu-rich_rpt) and IPR000483 (Cys-rich flanking region C). Gene3D 3.80.10.10 (Ribonuclease
  inhibitor-like LRR horseshoe fold). This is the classic Caps/Trn LRR-transmembrane fold.
- Trn and its paralog Capricious (Caps) are closely related: "The XC domains of Trn and Caps
  are 65% identical" [PMID:18817735], and "The LRR domains of Trn and Caps are interchangeable,
  suggesting that they can interact with a common receptor" [PMID:18817735].
- Localization: membrane / cell periphery. UniProt carries an IEA (ARBA) annotation to
  cell periphery (GO:0071944); the biology places the LRR ectodomain at the plasma membrane
  where it engages neighbouring cell surfaces.

## Molecular function

The molecular function is best described as a **cell-surface LRR adhesion/affinity molecule**,
not a signal-transducing receptor. Key points:

- Caps and Trn are repeatedly described as candidate homophilic/heterophilic adhesion
  molecules: "It has been suggested that Caps and Trn act as homophilic or heterophilic
  adhesion receptors or serve another unidentified function during adhesion" [PMID:19064711],
  and both "belong to the family of LRR proteins, suggesting a general role for this class of
  surface receptors in salivary gland morphogenesis" [PMID:19064711].
- Trn acts through its **extracellular (LRR) domain**: in the trachea "Tartan is expressed
  broadly in mesodermal cells" and "mesodermal cells and exerts its role in tracheal branch
  outgrowth through its extracellular domain" [PMID:16764850]. This extracellular-domain
  sufficiency (short cytoplasmic tail largely dispensable) argues against a classical
  transmembrane signal-transducing receptor and for an adhesion/affinity-mediator function.
- The interchangeability of the Trn and Caps LRR domains and the inference that they engage a
  "common receptor" [PMID:18817735] is consistent with heterophilic recognition of a partner
  on apposed cells.
- The precise biochemical binding partner(s) of Trn remain unresolved: "The molecular function
  of both Caps and Trn proteins is still unclear" [PMID:19064711].

Curation implication: the GO_Central IBA "signaling receptor activity" (GO:0038023) is
propagated across an LRR/Toll-like-receptor-containing PANTHER family (the IBA WITH column
includes human TLR3 UniProtKB:O15455 and CD180/RP105 UniProtKB:Q99467, which are bona fide
signaling receptors). For trn there is no evidence of transmembrane signal transduction, and the
extracellular-domain-sufficiency finding argues against it. The more informative and better-supported
MF is **cell-cell adhesion mediator activity (GO:0098632)**.

## Biological processes

### Cell adhesion / cell affinity and boundary formation (core)
Caps/Trn are the canonical LRR determinants of cell affinity in *Drosophila*. Kurusu et al.
summarize: "Trn and Caps are involved in cell-cell interactions in tracheae and imaginal discs,
and Caps regulates layer-specific targeting in the optic lobe" [PMID:18817735]. In imaginal
discs Trn/Caps establish affinity/sorting boundaries (e.g. dorsoventral wing compartment
separation; work of Milan, Shishido, and colleagues cited in the reviewed papers). GO cell
adhesion (GO:0007155) is therefore a core biological process for trn.

### Motor (and photoreceptor/CNS) axon target selection (core)
Kurusu et al. identified trn in a cell-surface-molecule overexpression screen for synaptic
target selection and then analysed loss of function in the embryo. Trn and Caps act largely
redundantly in motor-axon guidance/targeting: "If so, Trn and Caps might function in a redundant
manner to regulate axon guidance and to label muscles as axonal targets" [PMID:18817735];
"trn caps double mutant embryos have stronger motor axon phenotypes than trn single mutants"
[PMID:18817735]; and neuronal Trn is sufficient to rescue: "The trn caps phenotype was rescued
to ~20% penetrance for both ISNb and SNa phenotypes ... by neuronal expression of Trn driven by
Elav-GAL4" [PMID:18817735]. (trn null lethality before 3rd instar — "We could not assess trn LOF
phenotypes in larvae, because trn mutants die before 3rd instar." [PMID:18817735] — is why the
embryonic motor system was used.) Supports GO:0008045 motor neuron axon guidance.

### Tracheal morphogenesis (non-core developmental context)
In the tracheal system Caps and Trn have distinct roles in joining tracheal metameres into a
continuous tube: "repeat transmembrane proteins Capricious and Tartan contribute differently to
the formation of branch interconnections during tracheal development" [PMID:16764850]. Whereas
Caps is on the instructive bridge-cells, "Tartan provides permissive substrate for the ...
migrating tracheal cells during the network formation" [PMID:16764850]. Supports the IMP
annotation to GO:0035147 (branch fusion, open tracheal system) and is the concrete basis for a
role in cell migration (GO:0016477) — trn as a permissive mesodermal substrate for the migrating
tracheal branch cells.

### Salivary gland morphogenesis (non-core developmental context)
A targeted gain-of-function screen for salivary gland tubulogenesis recovered trn/caps, and
loss-of-function supports involvement: "The analysis of caps and tartan mutant phenotypes
suggests a role for these genes in salivary gland morphogenesis" [PMID:19064711]. Supports the
IMP annotation to GO:0007436 (larval salivary gland morphogenesis).

## Localization

Plasma membrane / cell periphery: single-pass TM protein with the LRR ectodomain displayed at
the cell surface (UniProt signal peptide + TM helix; ARBA IEA to GO:0071944 cell periphery).
Trn protein is displayed on muscle surfaces and mesodermal cells in the embryo [PMID:18817735,
PMID:16764850].

## Reference-quality notes

- PMID:18817735 (Kurusu et al., synaptic target selection screen) — full text available;
  directly assays trn loss- and gain-of-function in motor-axon targeting. HIGH relevance,
  VERIFIED.
- PMID:16764850 (Krause et al., tracheal morphogenesis) — abstract cached; directly contrasts
  Caps vs Trn in tracheal branch interconnection. HIGH relevance, VERIFIED (against abstract).
- PMID:19064711 (Maybeck & Röper, salivary gland GOF screen) — full text; trn/caps discussed as
  LRR adhesion hits. MEDIUM–HIGH relevance, VERIFIED.
- PMID:12717815 (De Celis, "Pattern formation in the Drosophila wing: the development of the
  veins") — this NAS reference for GO:0007155 cell adhesion is a wing-vein-patterning review whose
  abstract does not discuss trn or cell adhesion; it is a weak/likely-inappropriate citation for
  the adhesion annotation, though the annotation itself is biologically correct. LOW relevance.
- PMID:12508275 (Tyler & Baker, "Size isn't everything") — a short BioEssays commentary on tissue
  size/shape and cell affinity; the abstract does not mention trn or cell migration. It is the TAS
  basis for GO:0016477 cell migration but is only background/contextual for trn. LOW relevance.

## Summary of curation decisions

| GO term | Evidence | Action | Rationale |
|---|---|---|---|
| GO:0038023 signaling receptor activity | IBA | MODIFY → GO:0098632 cell-cell adhesion mediator activity | trn is an LRR adhesion molecule acting via its ectodomain; no evidence of signal transduction; IBA propagated from a TLR-containing family |
| GO:0007436 larval salivary gland morphogenesis | IMP | KEEP_AS_NON_CORE | supported experimental annotation; a specific developmental context for a pleiotropic gene |
| GO:0008045 motor neuron axon guidance | IMP | ACCEPT | core function; trn/caps redundant in embryonic motor-axon targeting, neuronal Trn rescue |
| GO:0035147 branch fusion, open tracheal system | IMP | KEEP_AS_NON_CORE | supported; specific tracheal developmental context (permissive substrate) |
| GO:0007155 cell adhesion | NAS | ACCEPT | core biological process; well supported by other literature (reference itself is weak) |
| GO:0016477 cell migration | TAS | KEEP_AS_NON_CORE | defensible via permissive substrate for migrating tracheal cells; non-core/indirect |
