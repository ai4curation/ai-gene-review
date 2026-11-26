# gltA (P14165, PA1580) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 31)

No deep-research provider was available; the notes below are my own reading of the UniProt record, the
two cited papers (both abstract-only in the cache; the PubMed MCP returned no PMC full text for
PMC1135760 or PMC210395) and QuickGO.

## Identity

- *Pseudomonas aeruginosa* PAO1 locus PA1580, UniProt P14165 (CISY_PSEAE, reviewed), 428 aa.
- Type I bacterial (hexameric, "large", NADH-sensitive) citrate synthase: InterPro IPR010953
  (Citrate_synthase_typ-I), IPR024176 (Citrate_synthase_bac-typ), NCBIfam TIGR01798 (cit_synth_I),
  Pfam PF00285, PROSITE PS00480; PANTHER PTHR42871:SF1. Active sites at 265, 306, 363 (UniProt FT ACT_SITE).
- UniProt: catalytic activity oxaloacetate + acetyl-CoA + H2O = citrate + CoA + H+ (EC 2.3.3.16, RHEA:16845),
  evidence ECO:0000269 PubMed:2507528; "Allosterically inhibited by NADH." (ECO:0000269 PubMed:2507528);
  subunit "Homohexamer."; pathway "tricarboxylic acid cycle; isocitrate from oxaloacetate: step 1/2."

## Literature

- Donald et al. 1989 cloned and sequenced the gene and expressed it in *E. coli*
  [PMID:2507528 "The structural gene for the allosteric citrate synthase of Pseudomonas aeruginosa has been
  cloned from a genomic library"]. The product, purified from the *E. coli* host, was active and
  NADH-inhibited [PMID:2507528 "the proteins were identical by immunological criteria and very similar in
  kinetics of substrate saturation and NADH inhibition"]. Activity is therefore tied to this ORF
  [PMID:2507528 "Because the cloned gene contained only one open reading frame large enough to encode a
  polypeptide of such a size, the three peaks must represent different forms of the same protein"].
  Note that *E. coli* has its own gltA, so the activity assignment rests on separable peaks and the P.
  aeruginosa antiserum, not on a null background; UniProt and GOA nevertheless treat it as EXP and I agree.
- Mitchell et al. 1995 purified two citrate synthases from *P. aeruginosa* itself
  [PMID:7626013 "Two types of citrate synthase (CS) have been purified from Pseudomonas aeruginosa, a 'large'
  form (CSI) and a 'small' form (CSII)."]; CSI is a hexamer [PMID:7626013 "CSI is a hexamer and CSII is a
  dimer"]. CSI matches the gltA product (type I hexamer, NADH-regulated). The paper does not identify genes
  [PMID:7626013 "It is suggested that the CS isoenzymes are products of different structural genes."], so the
  PseudoCAP attribution of the CSI activity to PA1580 is an inference from the type I hexamer, though a
  sound one. CSII (dimer, 36.5 kDa subunit) is probably the PrpC-type 2-methylcitrate synthase, which also
  has citrate synthase activity; I did not verify that.
- Process: citrate synthase catalyses the first step of the TCA cycle (UniProt PATHWAY line). Neither paper
  measures TCA cycle flux or a mutant phenotype; the PseudoCAP IDA to GO:0006099 is a process inferred from
  the activity (IC would be the accurate evidence code). The process claim itself is uncontroversial for
  the sole type I citrate synthase of PAO1.
- Citrate synthase also supplies citrate in the glyoxylate shunt; I do not propose a NEW glyoxylate cycle
  term because no *P. aeruginosa* gltA-specific evidence was read.

## Annotation decisions

- GO:0036440 citrate synthase activity (EXP, IDA, IBA, IEA): ACCEPT, the core MF.
- GO:0006099 tricarboxylic acid cycle (IDA PseudoCAP, IBA, IEA): ACCEPT; evidence code of the PseudoCAP row
  flagged as SUSPECTED (IDA for a process inferred from enzyme activity).
- GO:0046912 acyltransferase activity, acyl groups converted into alkyl on transfer (IEA InterPro): MODIFY to
  GO:0036440, its descendant already carried.
- GO:0005829 cytosol (IBA, seeded by E. coli GltA P0ABH7 which has IDA/HDA cytosol): ACCEPT.
- GO:0005737 cytoplasm (IEA InterPro): MODIFY to cytosol (GO:0005829).

## PseudoCAP IBA-seed assessment

QuickGO (2026-10-28, withFrom=PANTHER:PTN002450857) returns 54 IBA rows: 18 leaves each for GO:0036440,
GO:0006099 and GO:0005829 (cytosol is seeded by E. coli P0ABH7). The 18 leaves are type I citrate synthases:
gltA of E. coli (P0ABH7), Vibrio cholerae (Q9KQA8), Shewanella oneidensis (Q8EFP4), Xanthomonas (Q8P5V0),
Helicobacter pylori (P56062), and gltA proteins of Yersinia (taxon 632), Salmonella (99287), Coxiella
(227377), Bradyrhizobium (224911), Neisseria (122586), Rhodopirellula (243090) and Leptospira (189518, two),
Mycobacterium tuberculosis GltA2 (P9WPD5), Streptomyces CitA (Q9R339) and two Paramecium proteins (taxon
5888). E. coli GltA carries no experimental citrate synthase annotation in GOA, so P14165 is indeed the only
experimental seed.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002450857 | GO:0036440 citrate synthase activity | 1 (sole) | 18 (16 taxa) | GO:0036440, EXP, PMID:2507528 (UniProt); GO:0036440, IDA, PMID:7626013 (PseudoCAP) | SOUND | Activity of the cloned, expressed gene product (PMID:2507528) and of the native hexameric CSI (PMID:7626013). Catalytic residues and the PS00480 signature are conserved family-wide; the node term suits a clade of type I citrate synthases. |
| PTN002450857 | GO:0006099 tricarboxylic acid cycle | 1 (sole) | 18 (16 taxa) | GO:0006099, IDA, PMID:7626013 (PseudoCAP) | SOUND | The paper shows enzyme activity, not TCA cycle participation, so IDA overstates the evidence (IC from the activity would be accurate; flagged SUSPECTED). The claim itself is correct: citrate synthase catalyses the TCA cycle's first step, and the term is appropriate for every leaf in this clade of housekeeping citrate synthases. |
