# RPUSD2 (human, Q8IZ73) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RPUSD2 is the closest experimentally characterised relative of the
Drosophila RluA-1 (Q9VKV0) benchmark gene. No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon human RPUSD2 --fallback perplexity-lite` failed on
2026-10-21: falcon raised "Exception: Failed to authenticate" and the
perplexity-lite fallback returned HTTP 401 (insufficient quota). No
deep-research file exists; this review is built from the cached primary
literature (PMID:41136621, PMID:41698914, PMID:35051350, PMID:31477916,
PMID:22658674) and the UniProt record.

### Evolutionary placement

- UniProt places Q8IZ73 in PANTHER PTHR21600:SF40 "PSEUDOURIDYLATE SYNTHASE
  RPUSD2" (also confirmed in `interpro/panther/PTHR21600/PTHR21600-entries.csv`).
  Fly RluA-1 (Q9VKV0) and RluA-2 sit in the same subfamily and share the PAINT
  node PANTHER:PTN002727951; human RPUSD2 is a co-ortholog of both fly paralogs.
- Domain: RluA-family catalytic domain (Pfam PF00849, PROSITE PS01129 PSI_RLU,
  InterPro IPR006225/IPR006145/IPR020103). UniProt ACT_SITE 274 (by similarity
  to E. coli RluA P0AA37). I checked the sequence: residues 265-285 read
  KELHPLHRLDRLTSGVLMFAK, with D274 inside the canonical HRLD motif, so the
  catalytic aspartate is retained (contrast RPUSD3, whose catalytic Asp is a Gly
  [PMID:41136621]).
- PMID:41136621 phylogenetic discussion: "bacterial RluA and RluC may serve as
  the ancestors of eukaryotic RPUSD2 and RPUSD4, respectively" and "Compared
  with bacterial RluA, eukaryotic RPUSD2 has lost its activity towards rRNAs,
  while its function on tRNA Ψ32 is well maintained." The yeast SF40 member RIB2
  is a bifunctional fungal paralog (deaminase + PUS); its review
  (genes/yeast/RIB2) also marked the node-level rRNA IBA as over-annotated.

### Experimental evidence in human (this species)

1. tRNA Ψ31/Ψ32 (+Ψ34) — PMID:41136621 (Xu et al. 2025, Nat Cell Biol, HCT116
   RPUSD2-KO, BACS): "RPUSD2 installs Ψ modification at position 31–32 in both
   cy-tRNAs and mt-tRNAs as well as the anticodon position 34 in cy-tRNAs".
   Loose VNΨHWNNDNNH motif. Note: catalytic-dead rescue was done for RPUSD1
   (D67A), not for RPUSD2, so RPUSD2's tRNA assignments rest on KO loss of
   modification.
2. mt-tRNA Ψ31/Ψ32 — PMID:41698914 (Liu et al. 2026, Nat Commun, HEK293T
   RPUSD2-/-, PRAISE): "RPUSD2 pseudouridylates Ψ31 of mt-tRNALeu(CUN), Ψ32 of
   mt-tRNAPro and mt-tRNACys"; modification "nearly abolished (dropped to
   0.00%)". In contrast to (1), this study "did not find any confident cytosolic
   tRNA substrates for RPUSD2". The cytosolic targets therefore rest on one
   study/cell line, the mitochondrial targets on two independent labs.
   MitoFates predicts an N-terminal mitochondrial targeting signal for both
   RPUSD2 isoforms (prediction, not imaging).
3. mRNA/pre-mRNA — PMID:35051350 (Martinez et al. 2022): recombinant His-tagged
   human RPUSD2 purified from E. coli pseudouridylated a synthetic pool of
   pre-mRNA site sequences in vitro (Pseudo-seq); "These results identify
   site-specific RNA targets for previously uncharacterized PUS (e.g. RPUSD2,
   PUS7L)". No RPUSD2 knockdown in cells in that paper. PMID:31477916 (Carlile
   2019) is abstract-only in cache; the abstract says mRNA targets of "five
   pseudouridine synthases" without naming them; UniProt cites it with
   ECO:0000269 for mRNA activity, so I defer to the curators.
4. RNA binding — PMID:22658674 HeLa mRNA interactome capture (abstract-only);
   consistent with an RNA-modifying enzyme, non-core.

### Not established in human

- rRNA pseudouridylation: no RPUSD2-dependent rRNA site in either KO dataset;
  RPUSD4 is the mt-rRNA RluA enzyme. The IBA to GO:0000455 comes from a deep
  RluA node seeded with bacterial RluA-F and yeast Pus5/Pus9.
- Subcellular localization: no imaging data in the cached literature; UniProt
  carries no subcellular-location comment. Mitochondrial (and possibly
  nuclear/cytosolic) action is inferred from substrates and MTS prediction.
- Physiological role / phenotype: no human organismal phenotype studied here.

### Decisions summary

- Core: tRNA pseudouridine(31)/(32) synthase activity; tRNA pseudouridine
  synthesis including mitochondrial tRNA.
- Non-core: mRNA pseudouridine synthesis (in vitro), RNA binding.
- Over-annotation: enzyme-directed rRNA pseudouridine synthesis (IBA).
- General IEA process terms (pseudouridine synthesis, RNA modification, RNA
  processing) -> MODIFY to tRNA/mRNA pseudouridine synthesis.
- For transfer to fly RluA-1: experimentally established in human = tRNA
  Ψ31/Ψ32 (mt-tRNA in two labs; cy-tRNA in one) and in vitro pre-mRNA
  pseudouridylation; Ψ34 in cy-tRNA-Ile-TAT from one study only.
