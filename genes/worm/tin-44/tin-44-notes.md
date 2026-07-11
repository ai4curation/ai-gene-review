# tin-44 (C. elegans) — research notes

Gene: **tin-44** (WormBase `T09B4.9`, WBGene00020383); UniProt **O02161** (TIM44_CAEEL).
Ortholog of human **TIMM44** / yeast **Tim44**. Protein Existence level **PE=3 (Inferred from
homology)** — the worm protein's own biochemistry has NOT been directly characterized.

## Summary of what this gene is

TIM44 is the central organizing subunit of the **presequence translocase-associated import
motor (PAM)**, the ATP-driven engine on the matrix side of the TIM23 (presequence) translocase
that pulls nucleus-encoded, presequence-bearing preproteins across the mitochondrial inner
membrane into the matrix. TIM44 docks on the matrix face of the TIM23 channel and
recruits/tethers **mitochondrial HSP70** (mtHsp70; worm **HSP-6**) together with its regulatory
co-chaperones (J-protein Pam18/Tim14 = worm **dnj-21**, J-like Pam16/Tim16 = worm **tim-16**,
and nucleotide-exchange factor GrpE/Mge1), coupling cycles of mtHsp70 ATP binding/hydrolysis to
the vectorial (ratchet/motor) inward movement of the incoming polypeptide.

## KNOWN (established)

- **Family/orthology.** tin-44 belongs to the Tim44 family (InterPro IPR017303 Tim44;
  Pfam PF04280; PANTHER PTHR10721 "MITOCHONDRIAL IMPORT INNER MEMBRANE TRANSLOCASE SUBUNIT
  TIM44"). Contains an NTF2-like C-terminal domain fold (IPR032710). [UniProt:O02161]
- **Worm identity + import-machinery membership + co-regulation (direct worm data).**
  Xin et al. 2022 (worm, full text) explicitly identify tin-44 as the C. elegans homolog of
  mammalian tim44 and place it in the matrix-pulling step of import:
  [PMID:35608535 "After passing through the inner membrane pore formed by TIM17 and TIM23, the
  precursor proteins are pulled into the matrix by TIM44 and mtHSP70 (HSP-6)"] and
  [PMID:35608535 "We found that hsp-6 and tin-44, as well as mppa-1 and mppb-1, which are
  C. elegans homologs of mammalian mtHsp70, tim44, and Mpp, respectively, were also upregulated
  by cco-1 RNAi"]. i.e. tin-44 is transcriptionally co-induced with the rest of the TIM/TOM
  import machinery upon activation of the mitochondrial UPR (UPRmt).
- **Conserved PAM/import-motor mechanism (by-similarity basis).** In yeast/human, matrix import
  requires Tim23/Tim17/Tim44 acting with mtHsp70:
  [PMID:10339406 "translocation of preproteins into the matrix requires the membrane proteins
  Tim23, Tim17 and Tim44, which drive translocation in cooperation with mtHsp70 and its
  co-chaperone Mge1p"]. Human Tim44 topology differs from yeast:
  [PMID:10339406 "hTim44 is localized in the matrix and, in contrast to yeast, only loosely
  associated with the inner membrane"].
- **UniProt curated FUNCTION/SUBUNIT (by similarity to human Q07914).**
  FUNCTION: "Essential component of the PAM complex ... Recruits mitochondrial HSP70 to drive
  protein translocation into the matrix using ATP as an energy source." SUBUNIT: "Probable
  component of the PAM complex at least composed of a mitochondrial HSP70 protein, GrpE, tin-44,
  tim-16 and tim-14/dnj-21. The complex interacts with the tim-23 component of the TIM23
  complex." SUBCELLULAR LOCATION: "Mitochondrion inner membrane {ECO:0000305}". [UniProt:O02161]

## NOT known (knowledge gaps)

- **The molecular activity of worm TIN-44 has never been directly measured.** Its recruitment/
  tethering of mtHsp70 (HSP-6), its role as the PAM scaffold, and the coupling of mtHsp70 ATPase
  cycles to matrix translocation are all inferred from yeast/human Tim44. The only direct worm
  evidence is transcriptional co-regulation (PMID:35608535); there is no worm biochemistry,
  interaction, structure, or import-assay data on the TIN-44 protein itself. (UniProt keeps the
  name "**Probable** mitochondrial import inner membrane translocase subunit" and all FUNCTION/
  SUBUNIT annotations at evidence ECO:0000250 "by similarity".)
- **Submitochondrial topology of worm TIN-44 is unverified.** It is annotated to the
  mitochondrial *inner membrane*, but the human ortholog is matrix-localized and only *loosely*
  membrane-associated (PMID:10339406); whether worm TIN-44 is peripheral on the matrix face or
  more tightly membrane-anchored is untested.
- **Loss-of-function phenotype / essentiality in C. elegans not characterized** in the cached
  literature. (Mammalian TIMM44 is essential; worm phenotype not established here.)

## Existing GOA annotations (6) — review plan

1. GO:0001405 PAM complex, Tim23 associated import motor (CC, part_of, IBA) → **ACCEPT** (core complex membership)
2. GO:0030150 protein import into mitochondrial matrix (BP, involved_in, IBA) → **ACCEPT** (core BP)
3. GO:0051087 protein-folding chaperone binding (MF, enables, IBA) → **ACCEPT** (core MF — binds/tethers mtHsp70)
4. GO:0005743 mitochondrial inner membrane (CC, located_in, IEA) → **ACCEPT** (core location; see topology caveat)
5. GO:0030150 protein import into mitochondrial matrix (BP, involved_in, IEA/InterPro) → **ACCEPT** (same correct BP, InterPro2GO)
6. GO:0051087 protein-folding chaperone binding (MF, enables, IEA/InterPro) → **ACCEPT** (same correct MF, InterPro2GO)

No `protein binding`-type uninformative MF present. All 6 annotations are consistent with the
Tim44 family assignment and the conserved PAM function; none contradicted by worm data.

## Key references
- **PMID:35608535** — Xin et al., "The UPRmt preserves mitochondrial import to extend lifespan"
  (worm, full text). Only direct-worm reference for tin-44: homolog identity + import-machinery
  membership + UPRmt co-induction. HIGH relevance.
- **PMID:10339406** — Bauer et al. 1999, "Genetic and structural characterization of the human
  mitochondrial inner membrane translocase" (abstract only). Establishes the conserved
  Tim23/Tim17/Tim44 + mtHsp70 matrix-import mechanism and human Tim44 matrix/loose-membrane
  topology. MEDIUM relevance (by-similarity basis).
- **UniProt:O02161** — Swiss-Prot record; curated FUNCTION/SUBUNIT (by similarity to human
  TIMM44 Q07914) and inner-membrane location.
- **PMID:24662282** — Bennett et al. 2014, "Activation of the mitochondrial unfolded protein
  response does not predict longevity in C. elegans" (worm, full text). Direct worm RNAi data:
  [PMID:24662282 "E04A4.5 (TIM17), T09B4.9 (TIM44), F45G2.8 (TIM16), F15D3.7 (TIM23), and
  dnj-21 (TIM14), which function in the TIM23 complex that transports proteins into the inner
  membrane and the matrix"] and [PMID:24662282 "a subset of RNAi clones related to
  mitochondrial protein import (tomm-22, E04A4.5, T09B4.9, F45G2.8, F15D3.7, and dnj-21)"].
  tin-44 (T09B4.9) was an hsp-6p::gfp UPRmt-inducing clone and is grouped with the
  lifespan-SHORTENING import knockdowns. HIGH relevance.

## Deep research provenance / falcon verification

- Falcon (Edison) deep research completed at 2026-07-04T13:55 (1210 s, 37 citations):
  `tin-44-deep-research-falcon.md`. Verified as a real Edison output (proper frontmatter,
  real artifacts, real papers e.g. `xin2022theuprmtpreserves` = PMID:35608535,
  `bennett2014activationofthe` = PMID:24662282). The perplexity-lite fallback failed (401
  quota), but the falcon file itself is genuine.
- **Falcon fact-check caveat:** the falcon report asserted tin-44 RNAi "extended mean lifespan
  by 11.1% (P = 2.4 × 10⁻¹⁴)". This is a falcon ERROR — the cited Bennett 2014 full text
  instead places tin-44/T09B4.9 among RNAi clones that SIGNIFICANTLY REDUCED lifespan. The
  falcon claim was NOT used; only verbatim, verified quotes from the cached paper were used.
