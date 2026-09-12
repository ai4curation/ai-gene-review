# actI-ORF1 / KSα (Q02059, SCO5087) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`). MIBiG BGC0000194
(*Streptomyces coelicolor* A3(2), actinorhodin type II PKS). GenBank CAC44200.1 →
UniProt **Q02059** (ACTI1_STRCO), gene *actI-ORF1* / SCO5087.

## Function

ActI-ORF1 is the **ketosynthase (KSα)** of the actinorhodin "minimal" type II
polyketide synthase. With ActI-ORF2 (the chain-length factor, KSβ/CLF) it forms the
heterodimeric **KS-CLF** that polymerizes the poly-β-keto chain of the aromatic
polyketide antibiotic actinorhodin.

- "In type II polyketide synthases (PKSs), chains are polymerized by the
  heterodimeric ketosynthase-chain length factor (KS-CLF)." [PMID:15286722]
- KSα carries the catalytic activity: "Although CLF regulates chain length, it does
  not have an active site; KS must catalyze both chain initiation and elongation."
  [PMID:15286722]
- PDB **1TQY** ("An antibiotic factory caught in action") — the 2.0-Å act KS-CLF
  heterodimer; polyketide elongated in a ~17-Å tunnel at the heterodimer interface.

## Annotation issues

The GOA is built from fatty-acid-synthase (KAS/FabB) domain signatures, which
mis-cast this **polyketide** synthase as a **fatty-acid** enzyme:

- GO:0004315 3-oxoacyl-ACP synthase activity (IEA) → MODIFY → **GO:0016218 polyketide
  synthase activity** (mechanistically a ketosynthase, but a PKS not a FAS).
- GO:0006633 fatty acid biosynthetic process (IEA) → MODIFY → **GO:1901112
  actinorhodin biosynthetic process** (the actual product).
- GO:0030497 fatty acid elongation (IEA) → REMOVE (wrong-specific FAS term; polyketide
  chain extension is captured by the actinorhodin BP).
- GO:0016746 acyltransferase activity (IEA) → ACCEPT (accurate broad parent).
- GO:0005829 cytosol (IBA) → ACCEPT.

Add: **GO:0034082 type II polyketide synthase complex** (CC) — the KS-CLF heterodimer.

## Predicted-complex evidence (BGC project)

Moriwaki et al. (bioRxiv 2025.10.26.684697) predict the KSα–KSβ/CLF heterodimer
(BGC0000194; CAC44200.1/CAC44201.1) at **ipTM 0.96**, matching PDB 1TQY.

## References
- PMID:15286722 — Keatinge-Clay et al. 2004, Nat Struct Mol Biol (act KS-CLF
  structure, PDB 1TQY; abstract-only in cache but the abstract states the key
  catalytic/non-catalytic facts). VERIFIED.
