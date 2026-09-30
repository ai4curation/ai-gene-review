# G9JWI5 (NvNotch, Nematostella vectensis) — curation notes

## Identity

- UniProt G9JWI5 (unreviewed, TrEMBL), gene name `notch`, 1977 aa, **Fragment** (N-terminus
  incomplete: first EGF repeat begins at residue 14; no signal peptide or TM segment is annotated
  in the TrEMBL features). EMBL AEW42991.1, from Marlow et al. 2012 (PMID:22155407).
- Chosen by UniProt REST search (organism_id:45351, Notch/DSL Pfam) — it is the only
  Nematostella UniProt entry named `notch` with NOD/NODP/LNR + ankyrin architecture and is the
  sequence characterised in the literature. No full-length reference-proteome NEMVEDRAFT Notch
  entry was found.
- PANTHER: PTHR45836 (SLIT HOMOLOG) / PTHR45836:SF23 (NEUROGENIC LOCUS NOTCH HOMOLOG PROTEIN 1).
- InterPro: Notch (IPR008297), Notch_dom/LNR (IPR000800), NOD (IPR010660), NODP (IPR011656),
  Notch_C (IPR024600), ankyrin repeats, many EGF/cbEGF repeats.

## Literature

- Single Notch receptor: [PMID:22155407 "only a single gene with the diagnostic organization of
  well-conserved LNR domains, a NOD domain, transmembrane domain and Notch-like intracellular
  region was identified"]; conserved NLS [PMID:22155407 "We were also able to identify a
  conserved nuclear localization signal in the C terminus of the protein"].
- Neural repression: [PMID:25705370 "We found that inhibiting Nvnotch by injecting the Nvnotch MO
  or by treating with DAPT resulted in upregulation of the differentiated markers."] and
  [PMID:25705370 "Conversely, overactivation of Notch by overexpressing the Nvnicd:venus mRNA
  suppressed expression of the differentiation markers."]
- Canonical vs non-canonical: Layden & Martindale found no Hes response [PMID:25705370 "In
  Nematostella, gene-specific knockdown of Nvnotch, NvsuH, or overactivation of Nvnicd did not
  significantly affect expression levels of Nvhes genes"]; Richards & Rentzsch found the opposite
  [PMID:26443634 "This suggests that NvHes2 and -3 are indeed targets of NvNotch, and thus, that
  Notch signalling in Nematostella neurogenesis can occur via a canonical Hes-dependent
  mechanism."]. Marlow 2012 showed Su(H) MO/dominant-negative reduce cnidocytes
  [PMID:22155407 "Morpholino mediated knock-down and dominant negative inhibition of Su(H), an
  effector of Notch signaling, similarly result in a substantial loss of cnidocytes."]
- Endoderm induction / germ-layer boundary (2025): NICD nuclear and sufficient for endoderm genes
  [PMID:40858588 "Strikingly, injection of TBP::NICD-mCherry plasmid resulted in ectopic
  expression of foxA and brachyury in 60% of cases"].
- Gastruloids (2026): Notch needed for axis re-establishment; Su(H) MO phenocopies
  [PMID:42321198 "Our results show that gastruloids made from SuH MO-injected embryos also
  phenocopy LY-411575 treated gastruloids"].

## Assessment

- Core: transmembrane signaling receptor activity; Notch signaling pathway; PM + nucleus.
- Removed taxonomically inappropriate ARBA transfers (hemopoiesis, segmentation, system process),
  "Secreted", and generic protein domain specific binding.
- Variant-relevant biology: debated CSL/Hes-independent ("non-canonical") neural repression in a
  non-bilaterian; context-dependent canonical signalling (cnidogenesis, endoderm).

## Deep research

- `just deep-research-falcon NEMVE G9JWI5 --alias notch --fallback perplexity-lite` launched
  2026-09-30. Review based on cached full-text publications.
