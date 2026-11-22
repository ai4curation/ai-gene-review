# HAECO acr-8 notes

## Fetch and setup

- Fetched the full-length Haemonchus contortus ACR-8 accession with
  `just fetch-gene HAECO A9XX24 --alias hco-acr-8`, then renamed the review
  to the bare standard H. contortus symbol `acr-8`.
- `A9XX24` is the UniProtKB record for the 536-aa protein translated from the
  cloned full-length Hco-acr-8 cDNA `EU006785`/`ABV68891.1`.
- Live UniProt also exposes full-length WBParaSite accession `A0A7I4YXE5` and
  short ACR-8 isoform or fragment accessions `D2XI63` and `A0A7I4YWD8`; this
  review uses the cloned full-length ACR-8 record assayed in the L-AChR
  reconstitution paper.
- `just fetch-gene-pmids HAECO acr-8` found no PMIDs in the seeded GOA
  rows, which were all electronic.
- `just deep-research-falcon HAECO acr-8 --fallback perplexity-lite`
  failed because both configured remote providers were unavailable, so the
  review used cached primary papers and manual notes rather than a generated
  `acr-8-deep-research-*` file.

## Evidence summary

PMID:21486278 is the key full-text paper. It cloned the full-length
Hco-acr-8 cDNA from a levamisole-sensitive H. contortus isolate and
reconstituted two H. contortus L-AChR receptor states in Xenopus oocytes. The
ACR-8-containing Hco-L-AChR1 used Hco-ACR-8, Hco-UNC-29.1, Hco-UNC-38,
Hco-UNC-63a plus Hco-RIC-3.1, Hco-UNC-50 and Hco-UNC-74. Removing Hco-acr-8
from the mix greatly reduced expression but left a weaker ACR-8-lacking
Hco-L-AChR2, and Hco-ACR-8 expressed with the ancillary factors alone produced
no homomeric current. Hco-L-AChR1 was much more levamisole-sensitive than
Hco-L-AChR2.

The same paper is explicit about the residual biology gap. The oocyte-defined
Hco-L-AChR1 establishes Hco-ACR-8 as a functional levamisole-sensitive pore
subunit but does not identify where ACR-8-containing receptors assemble in vivo
or whether the reconstituted subunit ratios match any native H. contortus
receptor.

PMID:21945142 and PMID:24503202 are abstract-only in the local cache, but they
are enough for the narrow Hco-acr-8b resistance-marker context. The 2011
abstract reports that a triple-resistant UGA/2004 isolate expressed abundant
truncated Hco-acr-8b mRNA in L3 larvae while a susceptible comparison isolate
did not. The 2014 abstract reports that Hco-acr-8b was present in six
levamisole-resistant isolates and absent from four susceptible isolates, and
that absence of a 63-bp intron-2 indel correlated with both Hco-acr-8b
expression and levamisole resistance.

## Annotation decisions

- Generic Cys-loop receptor, ion-channel and ligand-gated-channel rows were
  refined to `GO:0022848` acetylcholine-gated monoatomic cation-selective
  channel activity because Hco-ACR-8 is a pore subunit of the heteromeric
  Hco-L-AChR1.
- Generic ion-transport process rows were refined to `GO:0098655` monoatomic
  cation transmembrane transport.
- The `GO:0022848` row was accepted, with the core function modeled as
  `contributes_to_molecular_function` because Hco-ACR-8 alone did not form a
  homomeric current.
- The ARBA `GO:0007268` row was refined to cholinergic and postsynaptic
  synaptic-transmission terms.
- The seeded postsynaptic membrane, postsynaptic chemical synaptic
  transmission and excitatory postsynaptic-potential rows were kept as
  inferences from a functional L-AChR pore subunit, while the absence of direct
  in vivo localization and stoichiometry was recorded as a knowledge gap.
- A new `GO:0005892` acetylcholine-gated channel complex row captures that
  Hco-ACR-8 is part of the reconstituted Hco-L-AChR1 complex.
