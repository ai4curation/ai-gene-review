# Gsk3b (rat, UniProt P18266) - manual literature synthesis

No deep-research API was available for this review. This synthesis was written by
hand from the cached publications in `publications/` (the PMIDs cited in the rat
GOA file plus PMID:20042609) and the UniProt record `Gsk3b-uniprot.txt`. Each
statement carries its provenance. Where a cached paper is abstract-only this is
noted, because the GO curators read the full text.

## Identity and biochemistry

- Rat GSK-3beta was cloned from rat brain cDNA as one of two GSK-3 genes; the beta
  form encodes a ~47 kDa protein 85% identical to GSK-3alpha and both clones are
  active kinases [PMID:2164470 "Both alpha and beta clones exhibit kinase activity
  when expressed in COS-1 cells"; "the products of distinct genes"].
- Recombinant rat GSK-3beta was expressed in insect cells via baculovirus and
  purified for characterisation, establishing it as the mammalian homologue of
  Drosophila zw3/shaggy [PMID:1346104, abstract only, "we have expressed this
  protein in insect cells using recombinant baculovirus"].
- UniProt: constitutively active Ser/Thr protein kinase, most substrates require
  priming phosphorylation; activated by Tyr-216 phosphorylation and inhibited by
  Ser-9 phosphorylation [file:rat/Gsk3b/Gsk3b-uniprot.txt "Constitutively active
  protein kinase"; "Requires primed phosphorylation of the majority of its
  substrates"]. Kinase domain 56-340, proton acceptor Asp181, ATP-binding Lys85
  (FT lines, PROSITE-ProRule PRU00159).

## Upstream inhibitory kinases (Ser-9)

- PKB/Akt inactivates GSK3 downstream of insulin and PI3K [PMID:8524413, abstract
  only, "it is the product of the proto-oncogene protein kinase B (PKB, also known
  as Akt/RAC)"].
- PKA phosphorylates Ser-9 of GSK-3beta and physically associates with it
  [PMID:11035810, abstract only, "Protein kinase A physically associates with,
  phosphorylates, and inactivates both isoforms of GSK-3"].
- In rat soleus muscle adrenaline (via PKA) and insulin (via PKB) increase Ser-9
  phosphorylation of GSK-3beta [PMID:16934435, abstract only].
- CaMKII associates with and phosphorylates GSK-3alpha/beta during depolarisation
  to promote neuronal survival [PMID:20841359, abstract only, "CaMKII associated
  with and phosphorylated GSK-3alpha/beta"].
- In osteoblastic UMR-106 cells and primary mouse osteoblasts, dynamic strain
  activates IGF-IR/PI3K/AKT, which inhibits GSK-3beta and activates beta-catenin
  independently of Wnt/LRP5 [PMID:20042609, full text read, "AKT in turn generates
  inhibitory phosphorylation of GSK-3β resulting in activation of β-catenin and
  stimulation of Lef/TCF-mediated transcription"].

## Wnt / beta-catenin destruction complex

- Rat Axin was isolated as a GSK-3beta-interacting protein; it binds GSK-3beta and
  beta-catenin at distinct sites, forms a ternary complex and promotes
  GSK-3beta-dependent phosphorylation of beta-catenin [PMID:9482734, abstract only,
  "rAxin promoted GSK-3beta-dependent phosphorylation of beta-catenin"].
- FWD1/beta-TrCP forms a complex with beta-catenin, Axin, GSK-3beta and APC and
  mediates ubiquitination after GSK-3beta/Axin phosphorylation [PMID:10228155,
  abstract only].
- MACF1 associates with the Axin/beta-catenin/GSK3beta/APC complex and helps
  translocate it to LRP6 at the membrane [PMID:16815997, abstract only].

## Tau and microtubules

- Originally identified as tau protein kinase I; immunoelectron microscopy and
  fractionation of rat cerebellum place TPKI/GSK-3beta, but not GSK-3alpha, in
  mitochondria [PMID:8576078, abstract only, "was present in mitochondria, but
  GSK-3 alpha was not"]. Note that the GOA row citing this paper is to
  `microtubule`, not mitochondrion.
- Apoptotic stimuli dephosphorylate Ser-9 and recruit GSK-3beta into neuronal
  lipid rafts, where inhibitors block tau phosphorylation [PMID:16735023, abstract
  only].
- Peroxynitrite in rat hippocampus activates GSK-3beta together with tau
  hyperphosphorylation [PMID:16879317, abstract only].
- GSK-3beta inhibition causes multiple axons in rat hippocampal neurons, preceded by
  microtubule stabilisation [PMID:18268107, full text].

## Neuronal polarity, dendrites, synapses

- Differential GSK-3beta activity in axon vs dendrites; active GSK-3beta inhibits
  axon formation and inhibition yields multiple axons [PMID:15652487, abstract
  only].
- Cdc42/Par6-PKCzeta phosphorylate GSK-3beta at the leading edge of migrating rat
  astrocytes to polarise the centrosome via APC [PMID:12610628, abstract only].
- ILK inhibits GSK-3beta; GSK-3beta inhibition causes dendrite initiation
  [PMID:17182785]; GSK-3/CRMP-2 couples activity to dendritic growth
  [PMID:23470087].
- GSK3beta is required for NMDAR-dependent LTD and is inhibited after LTP
  [PMID:17329210, abstract only, "GSK3beta inhibitors block the induction of LTD"].
- GSK-3beta phosphorylates PSD-95 Thr-19, destabilising PSD-95 and enabling AMPA
  receptor internalisation and LTD [PMID:23864697, full text, "PSD-95 ... is
  phosphorylated on threonine-19 (T19) by GSK-3β"].
- In rat hippocampal cultures, GSK3 inhibition changes synapse density in an
  age-dependent way; the neuromuscular-junction experiments in the same paper are in
  Drosophila only [PMID:25764078, full text].
- Hyperdopaminergic D2 signalling increases GSK-3beta activity, which disrupts
  beta-catenin/NR2B and attenuates NMDA receptor currents [PMID:20007479, abstract
  only].

## Apoptosis and cell survival (context dependent)

- Pro-apoptotic in neurons and astrocytes: recombinant GSK3beta induces cortical
  neuron apoptosis [PMID:12393899]; constitutively active S9A but not kinase-dead
  K85M induces astrocyte apoptosis, with NF-kB inhibition [PMID:12808104, full
  text]; ER stress and trophic withdrawal activate GSK-3beta in CGNs
  [PMID:16765055].
- Anti-apoptotic/pro-proliferative in vascular SMC, positively regulating Notch
  signalling [PMID:21557011, full text].

## Other tissue contexts (mostly correlative or pharmacological)

Muscle protein degradation after burn injury [PMID:17686886]; cardiomyocyte
hypertrophy and mPTP regulation via VDAC/ANT interaction [PMID:19318234]; GATA6
nuclear localisation [PMID:23624080]; spermatogenesis/meiotic DNA synthesis
[PMID:12721208]; ventral midbrain dopamine neuron differentiation [PMID:15522889];
bone and orthodontic models [PMID:28731198, PMID:29224185, PMID:26722385];
hepatic stellate cell activation [PMID:28061416]; many IEP papers that measure
GSK-3beta phosphorylation or mRNA after a treatment (xenobiotics, lithium,
ultrasound, glutamate, angiotensin II, methamphetamine/CPP, iron, H2O2, EPO,
zinc). These largely report GSK-3beta as a regulated pathway node rather than a
process it executes.
