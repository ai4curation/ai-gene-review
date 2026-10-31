# P2rx2 (rat, UniProt P49653) - manual literature research

No deep-research provider was available for this review. This summary was
assembled by hand from the cached publications in `publications/` and the
UniProt record `P2rx2-uniprot.txt`. Every claim carries its source.

## Identity and structure

- P2rx2 encodes the P2X2 purinoceptor, a 472-aa subunit of the P2X family of
  extracellularly ATP-gated cation channels (Pfam PF00864; PANTHER
  PTHR10125:SF4). Each subunit has two transmembrane helices (TM1 35-52, TM2
  327-347), a large glycosylated extracellular loop that carries the ATP-binding
  residues, and intracellular N- and C-termini (UniProt P49653, by similarity to
  zebrafish P2X4 structure P56373).
- Rat P2X2 was the first P2X receptor cloned, from PC12 cells
  [PMID:7523952 "the deduced sequence of a cloned P2x receptor predicts an unusual subunit structure resembling voltage-insensitive cation channels"].
- Functional channels are trimers. P2X2 forms homotrimers and heterotrimers with
  P2X1 [PMID:15313628 "the slowly desensitising subtypes P2X2, P2X4, and P2X5 are trimers of identical subunits"],
  with P2X3 [PMID:11181939 "agonist-evoked ionic currents by P2X receptors resulting from the coexpression of P2X(2) and P2X(3) subunits"],
  with P2X6, whose stoichiometry depends on relative expression
  [PMID:17449665 "when expression of the P2X(2) subunit predominates, the receptors contain primarily 2 x P2X(2) subunits and 1 x P2X(6) subunit"],
  and a P2X2/4/6 heterotrimer has been reported
  [PMID:24815693 "indicating the presence of a P2X2/4/6 heterotrimer"].
- Alternative splicing produces a C-terminally shortened P2X2(b)/P2X2-2 variant
  with faster desensitization
  [PMID:9119082 "ATP-activated currents mediated by heterologous expressed P2X(2) or P2X(2-2) receptors showed significant differences in desensitization time constants"],
  and a truncated form in pituitary and cochlea, originally named P2xR1-2
  [PMID:7542879 "A truncated form of the P2xR1 purinoceptor subunit (which we designate P2xR1-2) was detected in rat pituitary gland"].

## Molecular function: ATP-gated non-selective cation channel

- UniProt (experimental, ECO:0000269): "ATP-gated nonselective transmembrane
  cation channel permeable to potassium, sodium and calcium".
- Ion selectivity and calcium permeability were measured in mammalian cells
  [PMID:8961184 "The calcium permeability of P2X1 receptors was greater than that of P2X2 receptors."].
- Transmembrane segments TM1 and TM2 take part in gating; some alanine
  substitutions abolish ATP responses
  [PMID:15317863 "Four mutants (V45A, Y47A, V51A, and D349A) failed to respond to ATP."].
- The conserved pre-TM2 ectodomain region (Arg304-Ile314) is needed for correct
  conformation and channel function; the receptor reaches the cell surface in
  HEK-293 cells, as shown by surface biotinylation
  [PMID:18616429 "The mutant K308A was efficiently expressed at the cell surface"].
- Allosteric regulation:
  - Trace metals potentiate ATP currents. Copper and zinc act at a shared
    extracellular histidine site (His120, His192, His213, His245)
    [PMID:16190872 "We propose that His120, His192, His213 and His245 form part of a common allosteric metal-binding site of the P2X2 receptor"];
    His120 and His213 bridge subunits
    [PMID:17517890 "Histidines 120 and 213 have previously been shown to be essential in binding zinc across an intersubunit binding site."].
    Nickel, cobalt and cadmium also potentiate, more weakly, and mercury acts
    through a different, histidine-independent mechanism (PMID:16190872 abstract).
  - Membrane phosphoinositides bind the proximal cytoplasmic C-terminus
    (Lys365/Lys369) and slow desensitization and pore dilation
    [PMID:16857707 "We found that the recombinant proteins that included the positively charged region bound to PIPs and PIP(2)s, and that this binding was eliminated by the K365Q and K369Q mutations."].
  - Fe65 binds the C-terminus of P2X2(a), but not of P2X2(b), at excitatory
    synapses and inhibits the activation-dependent change in ion selectivity
    [PMID:16330549 "Fe65 colocalizes with P2X(2) subunits at the postsynaptic specialization of excitatory synapses"].

## Localization

- Plasma membrane (UniProt, PMID:15313628) and cell surface (PMID:18616429).
- In the CNS, immunogold EM puts P2X2 at the periphery of the postsynaptic
  specialization of parallel fibre-Purkinje cell and Schaffer collateral-CA1
  glutamatergic synapses, and in cell bodies, dendrites and spines
  [PMID:11160443 "In CA1 pyramidal cells, postsynaptic membranes apposed to terminals of Schaffer collaterals were immunogold-labeled for P2X(2), P2X(4), and P2X(6) subunits."].
- Presynaptically, P2X2 is found in vagal afferent terminals in the NTS
  [PMID:10974431 "The P2X(2) receptor was localized presynaptically in vagal afferent fibres and terminals in the nucleus tractus solitarius at the ultrastructural level"]
  and in the presynaptic active zone fraction of hippocampal nerve terminals
  [PMID:16000618 "We report that the most abundant P2X receptor subunits enriched in the presynaptic active zone fraction are P2X 1 , P2X 2 , P2X 3 , P2X 5 , and P2X 6 ( Fig. 5 B )."].
- In the cochlea, P2X2 is found on cells bordering endolymph and on outer hair
  cell stereocilia
  [PMID:10813788 "immunoreactivity was observed in most cells bordering on the endolymphatic compartment (scala media), particularly in the supporting cells"].

## Physiological roles (mostly mouse knockout and human genetics)

- Fast purinergic synaptic transmission. Hippocampal glutamate release is
  facilitated pharmacologically via P2X1, P2X2/3 and P2X3 (PMID:16000618). In mouse
  myenteric neurons P2X2 homomers carry part of the fast EPSP
  [PMID:12937291 "It is concluded that P2X2 homomeric receptors contribute to fEPSPs in neural pathways underlying peristalsis studied in vitro."].
- Carotid body chemoreflex: ATP released by glomus cells acts on P2X2-containing
  receptors on sinus nerve afferents
  [PMID:14672995 "We conclude that P2X receptors containing the P2X2 subunit play a pivotal role in carotid body function and in mediating ventilatory responses to hypoxia."].
- Taste: ATP is the transmitter from taste buds to gustatory afferents, and
  P2X2/P2X3 double knockout abolishes taste nerve responses
  [PMID:16322458 "Genetic elimination of ionotropic purinergic receptors (P2X2 and P2X3) eliminates taste responses in the taste nerves"].
- Hearing: human P2RX2 p.V60L causes DFNA41, and P2rx2-null mice develop
  progressive hearing loss
  [PMID:23345450 "P2RX2-null mice developed severe progressive hearing loss"].
- Sensory afferents, pain and bladder: P2X2 knockout reduces formalin pain
  behaviour, bladder reflexes and pelvic afferent firing
  [PMID:15961431 "P2X2-/- and P2X2/P2X3(Dbl-/-) mice had reduced pain-related behaviours in response to intraplantar injection of formalin."].
- NMJ: P2X2 is expressed during NMJ development, and knockout NMJs are
  disorganized
  [PMID:17706883 "These findings demonstrate a role for P2X2 receptor-mediated signaling in NMJ formation"].
- Ischemia: P2X2 is upregulated after glucose/oxygen deprivation, and the
  non-selective P2 antagonists suramin and basilen blue reduce cell death
  (PMID:12849743). This shows expression change and pharmacology, not a
  P2X2-specific requirement.
