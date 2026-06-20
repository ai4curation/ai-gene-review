# SCN9A (Nav1.7) review notes

UniProt: Q15858 | HGNC: SCN9A | Taxon: NCBITaxon:9606 (human)
PANTHER family: PTHR10037 (VOLTAGE-GATED CATION CHANNEL CALCIUM AND SODIUM)

## Core biology (synthesis)

SCN9A encodes the pore-forming alpha subunit of **Nav1.7**, a tetrodotoxin-sensitive
voltage-gated sodium channel. It is a single-polypeptide channel of ~1977 aa with the
canonical Nav architecture: 4 internal homologous repeats (domains I–IV), each with 6
transmembrane segments (S1–S6); S4 segments are the voltage sensors and the S5–S6
re-entrant loops form the Na+-selective pore. The channel is functional on its own but
is modulated by beta subunits (SCN1B/SCN2B/SCN3B/SCN4B).

- **Molecular function:** voltage-gated sodium channel activity — opens on membrane
  depolarization and selectively conducts Na+ down its electrochemical gradient, mediating
  the rising (depolarizing) phase of the action potential.
  [Rhea:RHEA:34963 Na(+)(in)=Na(+)(out); PMID:7720699 functional expression, TTX-sensitive,
  rapid activation/inactivation kinetics]
- **Cellular location:** plasma membrane, multi-pass; in nociceptor neurons localizes to
  axons, neuron terminals, and nodes of Ranvier. [PMID:30795902 "Cell projection, axon...
  Also detected at Nodes of Ranvier"]
- **Biological role:** Nav1.7 is the principal sodium channel setting the gain/threshold of
  **nociceptor (pain-sensing) neurons**, strongly expressed in dorsal root ganglion (DRG)
  and sympathetic ganglia. It acts as a "threshold channel" that amplifies subthreshold
  depolarizations.

## Tissue specificity

Strongly expressed in **dorsal root ganglion** (nociceptors), sympathetic neurons, with
minor levels elsewhere (smooth muscle, MTC cell line, C-cell carcinoma, vagus nerve).
Original cloning paper explicitly: "Transcripts were not identified in pituitary gland,
brain, heart, liver or kidney" — i.e. **NOT a cardiac channel** (cardiac Nav is
Nav1.5/SCN5A). [PMID:7720699]

## Human genetics = strongest functional evidence

Nav1.7 function is exceptionally well validated by human Mendelian genetics:
- **Congenital insensitivity to pain (CIP)** — autosomal recessive, biallelic nonsense/LOF
  mutations (S459X, I767X, W897X); complete loss of function abolishes pain. "SCN9A is an
  essential and non-redundant requirement for nociception in humans." [PMID:17167479]
- **Inherited/primary erythromelalgia (PERYTHM)** — gain-of-function (hyperpolarizing shift
  of activation) → burning extremity pain. [PMID:15385606, PMID:19369487, PMID:24311784]
- **Paroxysmal extreme pain disorder (PEPD)** — gain-of-function (impaired fast
  inactivation → persistent current). [PMID:17145499]

These establish GO:0019233 sensory perception of pain (IMP) on the firmest possible footing.

## Annotation-relevant publication notes

- PMID:7720699 (EMBO J 1995): cloning/functional expression of hNE-Na (=Nav1.7). Supports
  VGSC activity (IDA), plasma membrane, action potential generation/propagation. Full text
  abstract-only in cache but classic primary functional paper.
- PMID:17145499 (Neuron 2006, PEPD): supports VGSC activity (IDA), plasma membrane (IMP),
  sensory perception of pain (IMP), action potential propagation.
- PMID:30795902 (Neuron 2019, "Defining Functional Role of Nav1.7 in Human Nociception"):
  full text available; supports neuronal action potential (IDA), sensory perception of pain
  (IMP), node of Ranvier (IDA), axon terminus (IDA).
- PMID:30765606 (Science 2019, cryo-EM Nav1.7-beta1-beta2 + toxins): supports VGSC complex
  (part_of, ComplexPortal IPI), membrane depolarization during action potential (IDA).
- PMID:37117223 (Nat Commun 2023, nettle toxins/TMEM233): IPI to TMEM233 (B4DJY2) modulating
  Nav1.7 gating. Annotated as generic GO:0005515 protein binding — per project guidelines
  "protein binding" is uninformative; the real biology is channel-regulator interaction.

## Questionable / over-propagated annotations to scrutinize

1. **GO:0086002 cardiac muscle cell action potential involved in contraction** (IBA,
   GO_REF:0000033). Nav1.7 is NOT a cardiac channel (that is Nav1.5/SCN5A). This is
   phylogenetic over-propagation from the Nav family tree. → MARK_AS_OVER_ANNOTATED / NON_CORE.
2. **GO:0007623 circadian rhythm** (IEA, Ensembl ortholog GO_REF:0000107, from mouse
   Q62205/Scn9a). Not a recognized core function of human Nav1.7; ortholog-transfer, weak.
   → KEEP_AS_NON_CORE at best / candidate over-annotation.
3. **GO:0050974 detection of mechanical stimulus involved in sensory perception** (IEA,
   Ensembl). Nav1.7 is primarily a nociceptor amplifier; mechanosensation detection per se
   is debatable — Nav1.7 contributes to mechanical pain but is not the mechanotransducer.
4. **GO:0050965 detection of temperature stimulus involved in sensory perception of pain**
   (IEA, Ensembl). Plausible (Nav1.7 needed for some thermal/cold pain) but IEA-only.
5. Generic/high-level IEA terms (monoatomic ion channel activity, monoatomic cation channel
   activity, ion transport, transmembrane transport, membrane) — correct but redundant
   parents of the specific experimentally-supported terms; non-core.
6. **GO:0005515 protein binding** (IPI, PMID:37117223) — uninformative per guidelines.
