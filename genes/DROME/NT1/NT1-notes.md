# NT1 (DNT1, Spz2; UniProtKB:B7TB45) curation notes

## Literature search (2026-11-06)

No deep-research API keys were available, so no provider deep-research file was generated and
`just deep-research` was not run. FlyBase has no hand-written gene description for NT1, so there
is no `-deep-research-flybase.md` file. Searches were made by hand from the GOA references, the
UniProt FUNCTION comment references and the references of the module
`modules/neurotrophin_toll_signaling.yaml`. Papers read from the local cache (full text unless
stated): PMID:19018662, PMID:23892553, PMID:24124519, PMID:28373203, PMID:28846707,
PMID:31088910, PMID:22022271 (fetched in this session), PMID:32066523, PMID:25741726.

## Identity and structure

- DNT1 is a secreted Spätzle-family cystine-knot protein, named as the first Drosophila
  neurotrophin [PMID:19018662 "structurally related to all known neurotrophins and highly
  conserved in insects"].
- Prepro-protein with a signal peptide, pro-domain, cystine knot (CK) and a C-terminal tail
  [PMID:19018662 "Thus, DNT1 presents structural, cleavage, and dimerising features of canonical
  NTs."].
- Cleaved by furins; secreted both full length and cleaved [PMID:28373203 "DNT1 and 2 are cleaved
  intracellularly by conserved furins."; PMID:23892553 "DNT1 is secreted both as full-length and
  mature forms"].
- PANTHER PTHR23199:SF12 (UniProt DR line), PAINT node PTN002354018 shared with spz, spz5, spz6,
  spz3, spz4. No PAINT IRD/IKR losses on the lineage (`just paint-losses DROME NT1`).

## Receptors and signaling

- Binds Toll-7 (and promiscuously Toll-6) [PMID:23892553 "Together, these data demonstrate that
  DNT1 binds Toll-7 and DNT2 binds promiscuously Toll-6 and Toll-7."].
- Genetic epistasis: activated Toll-7 rescues DNT1 loss of function [PMID:23892553 "Over-expression
  of Toll-7CY in all neurons rescued the apoptosis caused by loss of DNT1 function"].
- Mature DNT1 activates NF-kB (Dorsal/Dif) and ERK via Toll-6/7, while pro-DNT1 can activate JNK
  [PMID:28373203 "Collectively, these data show that DNT1 and 2 can activate the prosurvival
  signaling pathways NF-κB and ERK via Toll-6 and -7 and that pro-DNT1 can activate the
  proapoptotic JNK pathway."].
- Binds Kek-6 in vitro (promiscuous) [PMID:28846707 "Ligand binding is promiscuous, as Kek-6 can
  also bind DNT1"].
- In vitro, the DNT1 (Spz-2) cystine knot binds Toll-1 and Toll-7 ectodomains and activates a
  drosomycin reporter in S2 cells [PMID:31088910 "Focusing on Toll-1 and Toll-7, our co-IP assays
  indicate the ectodomains of each bind Spz-1, -2, and -5"]. No in vivo evidence places DNT1 in
  the Toll-1 immune pathway.
- Tracheal immunity: Spz2/DNT1 is the proposed ligand of Toll-8/Tollo in a module that dampens
  IMD-driven AMP expression in the trachea [PMID:22022271 "antagonized by a constitutively active
  signalling module involving the receptor Toll-8/Tollo, the ligand Spätzle2/DNT1 and Ect-4"].

## Biological roles

- Neuronal survival, non-autonomous [PMID:19018662 "show that DNT1 promotes cell survival
  nonautonomously in the CNS"].
- Motor axon targeting (ISNb/d, SN) [PMID:19018662 "In all cases, there is a significant increase
  in the incidence of misrouting phenotypes in ISNb/d and SN fascicles compared to wild type"].
- No early CNS formation defect: [PMID:19018662 "In the CNS of homozygous DNT141 null mutant
  embryos, apoptosis levels are comparable to wild type at stages 13/14, and there are no axon
  guidance defects (unpublished data)."]. The "central nervous system formation" annotations
  therefore over-state the phenotype.
- NMJ: DNT1 and DNT2 act redundantly in synaptogenesis/NMJ growth [PMID:24124519 "Our data
  indicate that DNTs are produced in muscle and are required in neurons for synaptogenesis."].
  Synaptic plasticity is only speculated in PMID:19018662 ("Further functions of the DNTs could
  also include synaptic and neuronal activity, learning, and memory.").

## Decisions summary

- MF: growth factor activity (GO:0008083) is the core ligand-activity term (child of receptor
  ligand activity). Toll binding rows MODIFY per projects/LIGANDS_IN_SIGNALING.md.
- BP: GO:0008063 Toll signaling pathway (receptor Toll-1 by definition) rests on an S2-cell
  reporter assay with Toll-1 and Toll-7; MODIFY to GO:0038179 neurotrophin signaling pathway,
  which is what the Toll-7 arm and the in vivo data (PMID:23892553, PMID:28373203) support.
- innate immune response IBA: kept as non-core (Tollo tracheal role, PMID:22022271).
