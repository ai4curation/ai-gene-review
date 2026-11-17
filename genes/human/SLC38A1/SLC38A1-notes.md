# SLC38A1 (SNAT1 / ATA1) curation notes

UniProt: Q9H2H9 (S38A1_HUMAN), 487 aa, 11 TM domains. HGNC:13447, chr 12.
Family: amino acid/polyamine transporter 2 family; PANTHER PTHR22950:SF184
"SODIUM-COUPLED NEUTRAL AMINO ACID SYMPORTER 1"; Pfam PF01490 Aa_trans;
TCDB 2.A.18.6.14 (amino acid/auxin permease family). SLC38 family.

## Core biology — System A transporter

SNAT1 is a **System A** Na+-coupled neutral amino acid transporter (symporter).
Key defining features (all consistent with "System A"):
- **Na+:amino acid cotransport, electrogenic, pH-dependent**, driven by the Na+
  electrochemical gradient; **Na+:AA stoichiometry 1:1**.
  [PMID:10891391 "the cloned transporter mediates Na(+)-coupled transport of the
  system A-specific model substrate alpha-(methylamino)isobutyric acid. The transport
  process is saturable with a Michaelis-Menten constant of 0. 89 +/- 0.12 mM. The
  Na(+):amino acid stoichiometry is 1:1"]
- **Substrate: small short-chain neutral amino acids** (alanine, glutamine,
  asparagine, serine, glycine, proline, histidine, methionine, cysteine, threonine).
  [PMID:10891391 "The transporter is specific for small short-chain neutral amino
  acids."] UniProt lists Rhea catalytic-activity reactions (by similarity to rat
  Q9JM15) for Gln, Ala, Asn, His, Ser, Cys, Met, Gly, Thr, Pro each cotransported
  with Na+.
- **MeAIB-sensitive** (the System A diagnostic): KM = 890 uM for MeAIB.
  [UniProt BIOPHYSICOCHEMICAL PROPERTIES; ACTIVITY REGULATION "Inhibited by
  alpha-(methylamino)isobutyric acid (MeAIB)"]
- UniProt FUNCTION: "Symporter that cotransports short-chain neutral amino acids and
  sodium ions from the extracellular to the intracellular side of the cell membrane
  ... The transport is elctrogenic, pH dependent and driven by the Na(+)
  electrochemical gradient" [ECO:0000269|PubMed:10891391, PubMed:20599747].

Note: UniProt carries legacy alt-names "N-system amino acid transporter 2" / "System
N amino acid transporter 1", but functionally SNAT1 is **System A** (MeAIB-sensitive);
System N (SNAT3/SNAT5) is the H+-coupled, pH-regulated Gln/His/Asn system. The MeAIB
sensitivity settles it as System A.

## Localization

- **Plasma membrane** (cell membrane), multi-pass. [UniProt SUBCELLULAR LOCATION
  "Cell membrane {ECO:0000269|PubMed:15054072}"]
- In neurons restricted to the **somatodendritic compartment** (perikarya +
  dendrites), NOT axonal. [UniProt Note "Restricted to the somatodendritic compartment
  of neurons"; PMID:15054072 "neuronal SNAT1 ir was almost exclusively observed in
  perikarya and dendritic profiles"]. => axon (GO:0030424, IEA) is over-annotated.
- Expressed by pyramidal and GABAergic neurons, astrocytes; also placenta, heart,
  lung, muscle, spleen, stomach, testis. [PMID:15054072; PMID:10891391]
- Detected at the blood-brain barrier endothelium: "ATA1 were found only in hCMEC/D3
  cells" [PMID:23137377] — supports a peripheral role in amino-acid transport across
  the BBB.
- Found in B-cell exosome proteomics (HDA) [PMID:20458337] — common for membrane
  proteins; peripheral.

## Neuronal / glutamine–glutamate–GABA cycle role

SNAT1 mediates glutamine influx into neurons; proposed to replenish glutamate/GABA
transmitter pools, and (by similarity) supplies astroglia-derived glutamine to
GABAergic interneurons for de novo GABA synthesis.
[PMID:15054072 "SNAT1 mediates glutamine (Gln) influx into neurons and is believed to
replenish the transmitters pools of glutamate (Glu) and gamma-aminobutyric acid
(GABA)."]
Caveat: the Melone 2004 EM/localization study concluded "These findings suggest that
the major function of SNAT1 is not to replenish the transmitter pools of Glu and GABA"
[PMID:15054072] — so the neurotransmitter-replenishment / GABAergic-transmission roles
are indirect and contested; treat as non-core. "Neurotransmitter uptake"
(GO:0001504) is a mis-framing: SNAT1 imports the precursor glutamine, not the
neurotransmitters themselves.

## Placenta / pregnancy

System A activity in placental trophoblast; SNAT1 contributes to that activity and is
down-regulated by hypoxia. [PMID:20599747 (cited in UniProt) "contribution of SNAT1 to
system A amino acid transporter activity in human placental trophoblast"; PMID:12388062
hypoxia reduces System A]. "female pregnancy" (GO:0007565, IEA from rat) is a
whole-organism physiological context downstream of the transport function — SNAT1
supplies amino acids but does not itself execute "pregnancy" => over-annotated.

## Interactions

UniProt lists ~25 binary interactors, all from high-throughput Y2H interactome maps
(HuRI, PMID:32296183; PMID:25416956). None define a specific molecular function; all
bare GO:0005515 protein binding rows => REMOVE per protein-binding policy. Many
partners are unrelated membrane proteins (GPCRs, SLC10A1/6, AQP6, etc.), typical of
HT interactome co-detection.

## Action summary rationale

- Core MF: neutral L-amino acid:sodium symporter activity (GO:0005295) and
  L-glutamine transmembrane transporter activity (GO:0015186); substrate-specific
  :sodium symporter terms (Gln via GO:0005283, Ala GO:0015655, Gly GO:0015375,
  Pro GO:0005298, Asn GO:0140901) all backed by UniProt catalytic-activity reactions
  => ACCEPT.
- Core BP: amino acid transmembrane transport (GO:0003333, IBA), L-glutamine transport
  (GO:0006868, IBA), neutral amino acid transport, glutamine import across PM,
  Na+ transmembrane transport, amino acid import => ACCEPT.
- Core CC: plasma membrane (GO:0005886) => ACCEPT; membrane (GO:0016020) TOO_GENERAL.
- Non-core/indirect: GABAergic transmission regulation, synaptic plasticity
  regulation, BBB transport, exosome, basolateral PM => KEEP_AS_NON_CORE.
- Over-annotated: axon, external side of apical PM, female pregnancy, neurotransmitter
  uptake.
- All checked GO ids non-obsolete via QuickGO (2026-11-15). No proposed new terms
  needed — existing live GO terms cover the System A / glutamine symporter function.
