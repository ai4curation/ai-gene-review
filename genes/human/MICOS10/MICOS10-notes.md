# MICOS10 (MIC10, MINOS1, C1orf151) review notes

## 2026-10-08 session (claude-code, MICROPROTEINS Tier 4)

### Identity
- UniProt Q5TGZ0 (MIC10_HUMAN), 78 aa, canonical protein-coding gene (HGNC:32068). Not an
  alternative-ORF peptide: it is the primary ORF of its own locus. Initiator Met removed,
  Ser2 N-acetylated (large-scale proteomics, UniProt FT). Isoform 2 (Q5TGZ0-2) is 24 aa,
  ending after the first transmembrane segment (VSP_042062/3), and is unlikely to be functional.
- Sequence inspection (UniProt SQ): both hydrophobic segments carry a glycine-rich motif,
  TM1 `IGTGFGLGIV` and TM2 `AFGSGMGLGMA`, and the inter-TM loop is basic (`FFKRRMWP`),
  matching yeast Mic10 (Q96VH5: `MGFGVGVF`, `GIGFGVGRG`, `FFKRRAFP`). These are the motifs
  shown in yeast to drive Mic10 oligomerisation and membrane bending and inner-membrane
  targeting [PMID:25955210 "Both transmembrane segments of Mic10 carry a characteristic
  four-glycine motif"; "targeting of Mic10 to the mitochondrial inner membrane requires a
  positively charged internal loop"].

### Localisation and complex membership (human)
- Integral inner membrane protein, C terminus in IMS [PMID:22114354 "Thus we concluded that
  MINOS1 was an integral membrane protein of the inner membrane in human mitochondria."].
- In human mitofilin complexes with MIC60, MIC19, HSPA9 and outer membrane SAMM50/MTX1/MTX2
  [PMID:22114354 "In agreement, we found the outer mitochondrial membrane proteins Sam50 and
  metaxin 1 and 2 to coisolate with MINOS1, indicating that MINOS1 is part of a
  mitofilin-containing complex that associates with the outer membrane."].
- Complexome profiling places MICOS subunits in MICOS, a membrane bridging subcomplex with
  SAMM50/MTX2/MTX3, and the full MIB complex [PMID:26477565, abstract only]. GOA's
  `SAM complex` HDA row from this paper is a projection of MIB co-migration onto an
  outer-membrane complex; the sibling reviews of APOO and APOOL already REMOVE the same row.
- MIC13/QIL1 is required to incorporate MIC10 into mature MICOS [PMID:25997101 "Thus, QIL1
  appears to be required for incorporation of MIC10, MIC26, and MIC27 into the MICOS
  complex."]; MIC10 and MIC13 stabilise one another [PMID:27479602].
- Integrative structure (preprint) of human MIC60-MIC19-MIC10-MIC13 [PMID:42539326]; only the
  MIC10 homodimer was a confident homo-oligomer AF3 prediction.

### Function
- Yeast Mic10 bends membranes in vitro via GxGxGxG-dependent oligomerisation
  [PMID:25955211 "Oligomerization mutants fail to induce curvature in model membranes"],
  abstract only. Simulation work on the MIC10 subcomplex supports cardiolipin-assisted
  oligomerisation and curvature stabilisation [PMID:42647630].
- Yeast Mic10 also binds dimeric ATP synthase [PMID:28315355]; not tested in human in the
  cached literature, so not proposed.
- Human knockouts: MIC10-KO HeLa cells lose lamellar cristae and have >70 % fewer crista
  junctions; remaining CJs are wider; cristae become tube-like/onion-like [PMID:32567732
  "Compared to WT cells, the occurrence of CJs was reduced by about 25% in Mic26‐KO cells and
  by more than 70% in Mic10‐, Mic13‐, and Mic19‐KO cells."]. Note this paper argues the
  MIC60 subcomplex, not MIC10, is necessary for CJ formation per se, and that MIC10 shapes
  lamellar cristae. [PMID:33130824] Mic10 KO HeLa: loss of CJs, spherical/onion-like cristae,
  reduced crista dynamics.
- Disease: biallelic MICOS10 variants (exon-1 deletion + p.Cys58Ser) in a hepatocerebral
  mtDNA depletion syndrome; MIC10 protein lost in fibroblasts, cristae and respiration rescued
  by re-expression [PMID:39510533 "Defects in MICOS10 had a significant impact on cristae
  formation and reduced mitochondrial function."].

### Annotation decisions
- Bare protein binding (7 rows): REMOVE. Koob 2015 (MIC60/MIC26/MIC27) and ARMC1 are
  genuine MICOS/MIB associations already captured by complex CC terms; HuRI Y2H partners
  MPC2, APOC4, CIDEB have no supported functional context.
- SAM complex HDA: REMOVE (wrong membrane; MIB complex row captures the evidence).
- All mitochondrion/inner membrane/MICOS/MIB/crista junction/cristae formation rows: ACCEPT.
- NEW: GO:0180020 membrane bending activity by ISS from yeast Mic10 (Q96VH5). SGD carries
  the BP GO:0097753 membrane bending (IDA, PMID:25955211) on yeast MIC10; the MF term is
  newer and is used for OPA1, CHMP2A/CHMP3 etc. Participation test: MF, the protein itself
  bends the membrane, so it passes. Human-specific in vitro bending has not been shown.

### Side observation for the MICROPROTEINS project
- STREMI, the SLC35A4 uORF microprotein, is reported to share topology and motifs with MIC10
  and to regulate cristae morphogenesis (PMID:42069946, not cached; abstract read via
  E-utilities only). Relevant to the SLC35A4 alt-ORF review, not used here.
