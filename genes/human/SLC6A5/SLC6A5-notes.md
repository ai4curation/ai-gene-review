# SLC6A5 (GlyT2, Q9Y345) — curation notes

Batch 9 canonical-surfaceome backfill. Research journal for the GO annotation review.

## Identity and family

- Human **SLC6A5**, HGNC:11051, UniProt **Q9Y345** (SC6A5_HUMAN), 797 aa, chromosome 11p15.1.
  Synonyms GLYT2, NET1. Protein existence: evidence at protein level (multiple cryo-EM structures,
  e.g. PDB 9HUE/9WBR).
- Belongs to the **sodium:neurotransmitter symporter (SNF / NSS) family, TC 2.A.22, SLC6A5 subfamily**
  [file:human/SLC6A5/SLC6A5-uniprot.txt "Belongs to the sodium:neurotransmitter symporter (SNF) (TC 2.A.22) family. SLC6A5 subfamily."].
  PANTHER PTHR11616 (SODIUM/CHLORIDE DEPENDENT TRANSPORTER), subfamily PTHR11616:SF241
  (SODIUM- AND CHLORIDE-DEPENDENT GLYCINE TRANSPORTER 2). InterPro IPR000175 (Na/neurotransmitter
  symport), Pfam PF00209 (SNF). 12 TM helices (TM1 ~200–220 … TM12 ~717–735), large disordered
  cytoplasmic N-terminus (1–118).

## Core biology

- GlyT2 is a **secondary-active (Na+- and Cl--dependent) symporter** that performs **presynaptic
  glycine reuptake** at inhibitory glycinergic synapses in spinal cord, brainstem and cerebellum.
  It transports glycine from the synaptic cleft into the presynaptic terminal cytosol, recycling
  glycine for refilling of synaptic vesicles.
  [PMID:9845349 "transports glycine in a Na+/Cl--dependent manner"]
  [file:human/SLC6A5/SLC6A5-uniprot.txt "Terminates the action of glycine by its high affinity ... sodium-dependent reuptake into presynaptic terminals"]
  [PMID:40725001 "transporter GlyT2, which supplies glycine to presynaptic terminals to maintain"]
- **Stoichiometry 3 Na+ : 1 Cl- : 1 glycine** (electrogenic). The UniProt/Rhea catalytic reaction is
  glycine(out) + chloride(out) + 3 Na(+)(out) = glycine(in) + chloride(in) + 3 Na(+)(in)
  (Rhea:70695; ChEBI:57305 glycine, ChEBI:29101 Na+, ChEBI:17996 chloride)
  [file:human/SLC6A5/SLC6A5-uniprot.txt "glycine(out) + chloride(out) + 3 Na(+)(out) = glycine(in) + chloride(in) + 3 Na(+)(in)"].
  The higher Na+ coupling (3:1 vs GlyT1's 2:1:1) makes GlyT2 concentrative in the inward direction,
  which is why it (not GlyT1) refills presynaptic terminals. It is a **symporter**, not an antiporter
  or uniporter, and is **monomeric** (no heavy chain, no obligate heteromeric partner).
- Substrate specificity: glycine-selective; uptake is **not inhibited by sarcosine** (the GlyT1-type
  substrate), distinguishing GlyT2 from GlyT1 (SLC6A9)
  [PMID:9845349 "This uptake is not affected by sarcosine"]. Km for glycine in the 10–240 uM range
  across studies (108 uM in the original human clone) [PMID:9845349 "Km of 108 microM"].
- Na+ binding sites mapped on the structure (residues 206, 208, 209, 213, 477, 509, 574, 577; by
  similarity to Drosophila dDAT Q7K4Y6). N-glycosylated on the large extracellular loop (TM3–TM4);
  disulfide 311–320.

## Localization

- **Plasma (cell) membrane**, multi-pass; this is where the reuptake activity acts, on the
  presynaptic terminal surface.
  [file:human/SLC6A5/SLC6A5-uniprot.txt SUBCELLULAR LOCATION "Cell membrane"]
  [PMID:16751771 "encoding the presynaptic glycine transporter 2 (GlyT2)"]
  [PMID:31370103 "through various intracellular compartments to the cellular surface"]
- **Presynaptic** compartment of glycinergic synapses (the disease is "presynaptic" precisely because
  GlyT2 is presynaptic, in contrast to the postsynaptic GlyR/gephyrin genes)
  [PMID:16751771 "presynaptic glycine transporter 2 (GlyT2)"].
- Endosomal localization: GlyT2 undergoes constitutive endocytosis/recycling; an ISS endosome
  annotation is transferred from rat GlyT2 (UniProtKB:P58295). Plausible for a recycling surface
  transporter; kept as non-core. Rat source (P58295) also carries a **dense core granule** ISS
  annotation — an unusual claim I cannot verify from accessible primary evidence; left UNDECIDED.

## Disease

- Loss-of-function mutations in SLC6A5 cause **hyperekplexia 3 (HKPX3 / startle disease)**, MIM 614618:
  neonatal hypertonia, exaggerated startle, life-threatening neonatal apnea. SLC6A5 is the major
  **presynaptic** component of hereditary hyperekplexia (postsynaptic components are GLRA1, GLRB, GPHN,
  ARHGEF9) [PMID:16751771 "subcellular GlyT2 localization, decreased glycine uptake or both"].
  Disease mechanism = "blockade of glycinergic neurotransmission"
  [PMID:40725001 "disease is caused by a blockade of glycinergic neurotransmission"]. Pathogenic
  variants (e.g. T425M, W482C, Y491C, N509S, S510R, P429L, G449E) impair glycine transport and/or
  surface trafficking.

## GO review reasoning

### Molecular function
- Core MF = **GO:0015375 glycine:sodium symporter activity** (def: glycine(out) + Na+(out) =
  glycine(in) + Na+(in); verified via OLS). This is the most specific existing GO MF term for GlyT2.
  Nine GOA rows (IBA, IDA x3, IMP x2, TAS x3) assert it; all ACCEPT, consistent. The IBA
  (PTN008522004) carries Q9Y345 and RGD:621824 in WITH/FROM — the target's own experimental
  annotation is a legitimate IBD seed (grounding), not circular.
- **GO has no glycine:Na+:Cl- symporter term.** GO:0015375 captures only the Na+ co-substrate, not
  the obligatory chloride (confirmed by OLS: no such term; the only Na:Cl amino-acid-betaine analogue
  is GO:0140814 glycine betaine:sodium:chloride symporter activity). Proposed as a new term.
- GO:0015370 solute:sodium symporter activity (IEA/ARBA) is a strict is_a ancestor of GO:0015375
  (verified via OLS ancestor list) → TOO_GENERAL.

### Process
- GO:1903804 glycine import across plasma membrane — core process; ACCEPT (IBA self-grounded + IDA).
- GO:0098810 **neurotransmitter reuptake** (NEW): GlyT2 itself performs the reuptake step
  (def: directed movement of neurotransmitter from the extrasynaptic space into the presynaptic
  cytosol; is_a neurotransmitter uptake is_a GO:0006836 neurotransmitter transport, verified OLS).
  Participation test passes (GlyT2 is the transporter that does the work); comparator transporters
  SLC6A1/A2/A3/A4 carry uptake/reuptake terms, so this is a real gap for GlyT2, not a convention.
- GO:0006836 neurotransmitter transport (TAS Reactome) → TOO_GENERAL (ancestor of the NEW reuptake term).
- GO:0035725 sodium ion transmembrane transport (IBA) — Na+ is the co-transported driving ion of the
  symport; true but mechanistically ancillary to the glycine-transport core → KEEP_AS_NON_CORE.
- GO:0060012 synaptic transmission, glycinergic (IBA self-grounded + IMP) — GlyT2 contributes to
  glycinergic transmission by supplying/recycling glycine (reuptake sustains and terminates the
  inhibitory signal); defensible participant → KEEP_AS_NON_CORE.
- GO:0007268 chemical synaptic transmission (TAS) → TOO_GENERAL (ancestor of GO:0060012, verified OLS).

### Location
- GO:0005886 plasma membrane — core location (7 rows: EXP, IBA, IDA, IEA, IMP, TAS x2); all ACCEPT.
- GO:0016020 membrane (IEA InterPro; TAS) → MODIFY to GO:0005886 plasma membrane (refinement; PM is
  directly supported).
- GO:0045202 synapse (IEA GO_REF:0000120, derived from the BP terms) → MODIFY to GO:0098793 presynapse
  (GlyT2 is specifically presynaptic).
- GO:0005768 endosome (ISS from rat P58295) → KEEP_AS_NON_CORE (recycling).
- GO:0031045 dense core granule (ISS from rat P58295) → UNDECIDED (unusual, source evidence inaccessible).

### Paralog note (GlyT1 / GlyT2)
- GlyT1 = SLC6A9 (P48067, in several WITH/FROM lists here). GlyT2 is distinguished from GlyT1 by its
  3:1:1 (vs 2:1:1) stoichiometry and sarcosine-insensitivity. The IBA MF row sits at a PANTHER node
  (PTN008522004) for the glycine-transporter clade and is grounded on GlyT2 itself — no cross-paralog
  mis-propagation seen. The broader plasma-membrane IBA (PTN000177662) and Na+-transport IBA span the
  wider SLC6 family, which is fine for those general terms.
