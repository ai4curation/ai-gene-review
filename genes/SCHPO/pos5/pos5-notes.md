# pos5 (SPAC323.01c, UniProt Q9UT98) — review notes

## 2026-11-01 — initial review, centred on Nishihara et al. 2026 (PMID:41926382)

### Identity and sequence-level evidence

- UniProt Q9UT98, "NADH kinase pos5, mitochondrial", 386 aa, PE 3 (inferred from
  homology). Curated function is by similarity to S. cerevisiae Pos5
  [file:SCHPO/pos5/pos5-uniprot.txt "Phosphorylates both NADH and NAD(+), with a preference for NADH."].
- Family: NAD kinase family (Pfam PF01513 NAD_kinase, PF20143 NAD_kinase_C; PANTHER
  PTHR20275:SF26 "NADH KINASE POS5, MITOCHONDRIAL"; HAMAP MF_00361)
  [file:SCHPO/pos5/pos5-uniprot.txt "Belongs to the NAD kinase family."].
- Predicted transit peptide 1..42 (ECO:0000255). The paper instead aligns the S. pombe
  N-terminus to the 62-residue ScPos5 transit peptide and places the corresponding
  boundary at residue 83 [PMID:41926382 "The mitochondrial transit peptide in S. cerevisiae Pos5p was 62 amino acids from the N-terminus, and its homologous position is 83 amino acids in S. pombe Pos5."].
- 37% identity with ScPos5, conserved NAD kinase motifs (GGDG ATP-binding motif)
  [PMID:41926382 "S. pombe pos5 gene is predicted to encode a mitochondrial NAD(H) kinase because the Pos5 protein shares 37% identity with S. cerevisiae Pos5"].

### S. cerevisiae Pos5 (ortholog; background, not S. pombe evidence)

- Outten & Culotta 2003 (PMID:12727869, abstract only): recombinant ScPos5 has NADH
  kinase activity and is in the matrix
  [PMID:12727869 "recombinant Pos5p has NADH kinase activity"]
  [PMID:12727869 "is localized to the mitochondrial matrix of yeast and appears to be important"];
  required for oxidative stress resistance, arginine biosynthesis and mitochondrial iron
  homeostasis [PMID:12727869 "to a broad range of oxidative stress conditions, arginine biosynthesis and"].
- These ScPos5 data are the PAINT seed (SGD:S000006109) of the three IBA rows.

### What Nishihara et al. 2026 showed — S. pombe results

All results below are in S. pombe unless marked [Sc].

1. **CoQ10 deficiency of Δpos5.** Found in a Bioneer deletion-library screen; a
   freshly constructed Δpos5 (RYP7) has 0.2-fold of WT CoQ10
   [PMID:41926382 "CoQ levels in the Δpos5 strain of our construct were decreased to 0.2-fold of those in the wild-type strain"].
2. **Not a secondary effect of respiratory failure** (Δcyc1 control)
   [PMID:41926382 "The Δcyc1 strain did not show a marked decrease in CoQ levels, suggesting that respiratory deficiency alone does not account for the low CoQ level in the Δpos5 strain."].
   Authors still cannot exclude an indirect Fe-S route
   [PMID:41926382 "While we cannot rule out a possibility that Pos5 deficiency indirectly affects CoQ levels via impaired Fe-S cluster biogenesis"].
3. **Phenotypes of CoQ-deficient S. pombe**: no growth on glycerol/ethanol, H2O2
   sensitivity, slow growth on minimal medium
   [PMID:41926382 "The Δpos5 strain failed to grow on YEGES medium containing glycerol and ethanol as non-fermentable carbon sources and showed retarded growth on YES containing hydrogen peroxide as well as on minimal medium"];
   high sulfide (brown colonies on CuSO4)
   [PMID:41926382 "When grown on YES containing CuSO4, Δpos5 colonies also developed a brown coloration, similar to the Δdps1 strain"];
   round cell morphology [PMID:41926382 "Δpos5 cells showed a round morphology"].
4. **Arginine auxotrophy** partially rescued by arginine (S1 Fig), attributed to NADPH
   use by Arg11 [PMID:41926382 "This is due to the requirement of NADPH for Arg11-catalyzed reaction in arginine biosynthesis."].
5. **ScPOS5 complements Δpos5 CoQ** (chromosomally integrated, P41nmt1)
   [PMID:41926382 "CoQ levels in the NSP7 strain were recovered to 0.9-fold of that observed in the Δpos5 + pos5 strain (NSP11)"].
6. **Mitochondrial NADP(H) is reduced** in mitochondria-enriched fractions of Δpos5
   [PMID:41926382 "Mitochondrial NADP+ level and total NADP(H) level in Δpos5 were decreased to 0.6- and 0.8-fold, respectively, of those in the wild-type strain"].
   Caveat: modest reduction; crude mitochondrial fraction; no enzyme assay of SpPos5.
7. **Localisation.** Endogenous C-terminal GFP fusion was mislocalised and
   non-functional [PMID:41926382 "The Pos5-GFP signal did not show the expected mitochondrial localization pattern"];
   plasmid-expressed Pos5-GFP co-localised with MitoTracker
   [PMID:41926382 "The Pos5-GFP fluorescence overlapped with the MitoTracker Red FM signal (Fig 5), indicating that Pos5 localizes to mitochondria as a mitochondrial NAD(H) kinase"].
   No sub-mitochondrial fractionation.
8. **Mitochondrial NAD kinase activity is what matters**: N-terminally truncated Pos5
   (ΔMTS83) and cytosolic ScUtr1 fail, while ScUtr1 fused to the SpCoq3 MTS rescues
   [PMID:41926382 "CoQ quantification showed that only MTS36UTR1 restored CoQ production, whereas neither ΔMTS83pos5 nor UTR1 could recover CoQ levels in the Δpos5 strain"].
   This is the strongest (indirect) evidence that the S. pombe protein acts as an
   NAD(H) kinase in mitochondria: the defect is rescued by an unrelated NAD kinase
   only if it is targeted to mitochondria.
9. **Coq6 is not the limiting step**: coq6 overexpression does not help
   [PMID:41926382 "However, CoQ levels in the Δpos5 strain overexpressing coq6 were comparable to that in the Δpos5 strain integrating a vector"];
   VA tends to help (not significant)
   [PMID:41926382 "Although statistical difference was not observed, the addition of VA tended to increase CoQ levels in the Δpos5 strain"];
   PHB partially restores
   [PMID:41926382 "Supplementation of 0.5 mM PHB partially increased CoQ levels in the Δpos5 strain compared to the untreated condition"].
   atd1 overexpression: slight, non-significant increase (S7 Fig).
10. Authors' conclusion: the NADPH-dependent step is upstream, in quinone precursor
    synthesis, and remains unidentified
    [PMID:41926382 "Our results suggest that the requirement for NADPH lies in the synthesis of the precursor of CoQ biosynthesis, although more detailed analysis is necessary to define the specific reaction(s) that depend on mitochondrial NADPH."].

[Sc] results in the same paper: ΔScpos5 CoQ6 is 0.2-fold of WT
[PMID:41926382 "CoQ6 levels in ΔScpos5 were decreased to 0.2-fold of those in the wild-type strain"];
ΔScpos5 respiratory deficiency, H2O2 sensitivity and arginine auxotrophy confirmed (Fig 4A).

Not done in the paper: no in vitro kinase assay of SpPos5, no sub-mitochondrial
localisation, no CoQ intermediate profiling.

Supplementary material not accessible: S1-S7 Figs are only available as captions in
the cached text (images not available); S1 Table (primers) and S2 Table (plasmids) are
XLSX files that were not retrieved. None of these is needed for the annotation
decisions, but the S3/S5 localisation images could not be inspected.

### Decision on "ubiquinone biosynthetic process" (GO:0006744)

Question: does Pos5 participate in CoQ biosynthesis, or is it necessary for it?

- **Who performs the step?** No step of CoQ biosynthesis is assigned to Pos5. Pos5
  makes mitochondrial NADP(H); the step(s) that consume it are unknown (Coq6 excluded
  as the limiting step; precursor synthesis suspected but unidentified; atd1
  overexpression did not significantly rescue). The CoQ reduction (to 20%, not zero)
  fits a supplier of a cofactor pool used by many processes.
- **Comparator check** (QuickGO, GO:0006744 incl. descendants, taxa 284812, 559292,
  9606, run 2026-11-01): the annotated gene products are the Coq enzymes, prenyl
  diphosphate synthases, Coq8/Coq9/Coq11/Coq12 accessory factors, and the
  ferredoxin/ferredoxin-reductase electron donors to Coq6 (S. pombe arh1, etp1;
  S. cerevisiae ARH1, YAH1; human FDX2, FDXR). The ferredoxin system transfers electrons
  directly to the Coq6 reaction — step-level participation. No NADPH-generating enzyme
  carries the term: not ScPOS5 (annotated to NADH kinase activity, matrix, NADP+
  biosynthesis, Fe-S cluster assembly IMP, oxidative stress), not UTR1, ZWF1, human
  NADK/NADK2, G6PD, nor S. pombe zwf1. Note ScPOS5 has an SGD IMP to Fe-S cluster
  assembly (PMID:20889970), so SGD does sometimes annotate a cofactor-supplier IMP;
  but no SGD row exists for CoQ even though this 2026 paper also covers ScPOS5.
- Conclusion: do not add GO:0006744. Pos5's relation to CoQ synthesis is a necessity
  (cofactor supply) relationship whose consuming step is unknown; it is recorded as a
  knowledge gap and a suggested question, and the phenotype is better captured as a
  FYPO phenotype (decreased cellular ubiquinone level) than as a GO process.

### Other BP considerations

- NADP+ biosynthetic process: Pos5 catalyses the NAD(H) -> NADP(H) phosphorylation
  that is the definitional step; S. pombe mitochondrial NADP+ drops in Δpos5. The
  IEA row is accepted with PMID:41926382 as organism-specific support (an IMP row
  would be appropriate for PomBase).
- Cellular response to oxidative stress (IBA): supported by H2O2 sensitivity in both
  yeasts, but this is a downstream consequence of NADPH supply (and of CoQ loss);
  kept as non-core.
- Arginine biosynthesis, respiration, Fe-S assembly: necessity phenotypes via NADPH,
  not added.

### Annotation decisions (summary)

| term | evidence | action |
|---|---|---|
| mitochondrion | HDA (ORFeome) | ACCEPT |
| mitochondrion | IEA (SubCell) | ACCEPT |
| mitochondrial matrix | IBA | ACCEPT |
| NADP+ biosynthetic process | IEA | ACCEPT |
| kinase activity | IEA (ARBA) | MODIFY -> NADH kinase activity |
| phosphotransferase activity, alcohol group as acceptor | IEA (ARBA) | MODIFY -> NADH kinase activity |
| NAD+ metabolic process | IEA (InterPro) | MODIFY -> NADP+ biosynthetic process |
| cellular response to oxidative stress | IBA | KEEP_AS_NON_CORE |
| NADH kinase activity | IBA | ACCEPT |
| NADH kinase activity | IEA (RHEA/EC) | ACCEPT |

No NEW rows. The S. pombe IDA (plasmid Pos5-GFP, mitochondrion) and IMP (mitochondrial
NADP+ decrease, NADP+ biosynthetic process) results from PMID:41926382 would justify
experimental rows, but both terms are already in GOA (validation rejects NEW for a term
already present), so they are cited in the reasons of the existing rows and flagged here
for PomBase curation.
