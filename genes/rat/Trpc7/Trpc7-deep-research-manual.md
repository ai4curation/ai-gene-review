# Trpc7 (rat) - manual literature synthesis

No deep-research provider was available for this session, so this file was written by hand
from cached publications (`publications/PMID_*.md`) and PubMed searches (query `TRPC7[Title]`,
26 hits). Quotes are verbatim from the cached records.

## Identity and nomenclature

- Rat Trpc7 (RGD:628820, NCBI GeneID 282822, Ensembl gene ENSRNOG00000012727) has no
  Swiss-Prot entry. UniProt holds several unreviewed TrEMBL entries for the gene (F1LQF7,
  A0A8I6GIE6, A0A8I6GIF7, A7L635). GOA keys the RGD and PAINT annotations to F1LQF7 (958 aa);
  A0A8I6GIE6 (904 aa, carries the GeneID cross-reference) has only 5 IEA rows.
- Caution: an unrelated 1998 human clone called "TRPC7" on chromosome 21q22.3, 1503 aa, highly
  expressed in brain [PMID:9806837 "We have isolated cDNA clones for a novel human protein, TRPC7
  (transient receptor potential-related channels), which consists of 1503 amino acid residues"]
  is the melastatin-family channel now named TRPM2, not canonical TRPC7. Papers on "TRPC7" and
  bipolar disorder on chromosome 21 refer to that gene.

## Family and structure

- TRPC7 belongs to the TRPC3/6/7 subfamily of canonical TRP channels: six transmembrane helices
  (Phobius predicts six TM segments, 449-766 in F1LQF7), N-terminal ankyrin repeats and a TRP
  domain (InterPro IPR002153 TRPC_channel, IPR005463 TRPC7_channel; PANTHER PTHR10117:SF9).
- [PMID:17217055 "TRPC7 is directly activated by diacylglycerol (DAG), one of the PLC products,
  having high sequence homologywith TRPC3 and TRPC6, which are also activated by DAG."]

## Channel function (mouse and human orthologs)

- Mouse TRPC7 cloning and electrophysiology in HEK cells [PMID:10488066]: constitutively active,
  receptor-enhanced Ca2+-permeable cation channel activated by DAG independently of PKC; it "did
  not affect capacitative Ca(2+) entry induced by thapsigargin", i.e. not store-operated in that
  system; "Relative permeabilities indicate that TRP7 is slightly selective to divalent cations."
  Mn2+ influx (a fura-2 quench surrogate of divalent entry) was potentiated by DAG.
- Human TRPC7 in HEK-293 cells [PMID:15342342]: "when transiently expressed in HEK-293 cells,
  TRPC7 forms channels that are activated by PLC-stimulating agonists, but not by Ca(2+) store
  depletion. However, when stably expressed in HEK-293 cells, TRPC7 can be activated by either
  Ca(2+) store depletion or PLC activation." Store-operated gating is therefore
  context-dependent, not the defining mode.
- Native human keratinocytes [PMID:16741513]: antisense knockdown of TRPC7 reduced ATP- and
  carbachol-induced Ca2+ entry and OAG currents; "activation of both muscarinic and purinergic
  receptors via a common DAG-dependent link opens Ca(2+)-permeable TRPC7 channels."
- Regulation [PMID:18158870]: Ca2+ entering through TRPC7 inactivates the channel; IP3 in the
  pipette sensitised the OAG current to Ca2+-dependent inhibition "independent of the IP3
  receptor". This is an effect of IP3, not a demonstration that TRPC7 binds IP3.

## Rat-specific data

- [PMID:18452405] (full text): human TRPC3 and TRPC7 expressed in COS-7 cells localise to the
  plasma membrane and to a large intracellular pool in the TGN and cis-Golgi (BFA-sensitive).
  Endogenous TRPC7 in the rat pituitary GH4C1 cell line "was detected in a Golgi-like area close
  to the nucleus (Figure 4A)" and co-localised with the cis-Golgi marker alpha-mannosidase II.
  Overexpression of TRPC3 or TRPC7 increased secreted alkaline phosphatase 2-4-fold; the authors
  propose an additional role in enhancing constitutive secretion (overexpression phenotype only).
- [PMID:12787073] (abstract only): single-cell RT-PCR of TRPC transcripts in rat aminergic
  neurons; TRPC6 and TRPC7 not co-expressed in individual VTA/TMN neurons.

## Synthesis

TRPC7 is a receptor-operated, DAG-activated, Ca2+-permeable nonselective cation channel of the
plasma membrane, acting downstream of Gq/PLC-coupled receptors, with a substantial intracellular
Golgi/TGN pool. Store-operated gating, IP3 binding and fertilization roles are family-level
propagations not established for TRPC7.
