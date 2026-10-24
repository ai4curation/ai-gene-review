# cdc10 (P01129, SPBC336.12c) — curation notes

Working journal for the GO annotation review of *Schizosaccharomyces pombe* cdc10, the
Start control protein and core subunit of MBF/DSC1. Inline citations use
`[PMID:NNN "verbatim text"]`; all quoted text is from the cached `publications/PMID_*.md`
files unless marked as fetched from PubMed for background. Full text is cached for
19714215, 18662996, 21132016 and 24006488; every other cited paper is abstract-only
(1734281, 7916653, 7926774, 8223442, 8313888, 14648198, 9303312, 9755169, 11781565,
12871901, 7916658, 8657126, 16816948, 7588609, 7739540, 16823372, 8532516, 9034336,
9201720, 17936710, 30134042, 40015273).

The deep-research file `cdc10-deep-research-falcon.md` (Edison/falcon) is present and was
used; it is built mainly on Ayte 1995, Ivanova 2013 and Eshaghi 2011 and its claims were
checked against the cached primary papers before use.

## Identity check

Fission-yeast Cdc10 is the ~85 kDa ankyrin-repeat, Swi6-like subunit of MBF. It is **not**
the budding-yeast Cdc10 septin, and the S. pombe HP1 protein Swi6 is unrelated to
budding-yeast Swi6/Cdc10. The GOA WITH/FROM identifiers resolve as PomBase:SPBC725.16 =
res1 (sct1, P33520) and PomBase:SPAC22F3.09c = res2 (pct1, P41412); UniProtKB:O60094 =
pol5, UniProtKB:P40923 = yox1. `gocams/index.tsv` has no entry for cdc10/SPBC336.12c.
The module `modules/g1_s_transition.yaml` uses cdc10 as the fission-yeast MBF exemplar
(annoton `mbf_cdc10`, function GO:0000981 for the family as a whole).

## Synthesised picture

- **Discovery as a Start gene and as a component of the MCB-binding factor.**
  [PMID:1734281 "We also show that the fission yeast cdc10+ gene product, which is
  required for Start and entry into S phase, is a component of this binding activity."];
  [PMID:8223442 "This is composed of at least the products of the cdc10 and sct1/res1
  genes, and binds to the promoters of genes whose expression increases prior to S
  phase."]; [PMID:7916658 "Commitment to the cell cycle in fission yeast requires the
  function of the cdc10+ transcriptional activator at START."].
- **Two alternative DNA-binding partners, Res1 and Res2; Cdc10 is the common subunit.**
  [PMID:7916653 "p72sct1 is shown to act in partnership with p85cdc10 in a cell cycle
  regulatory transcription complex."]; [PMID:7926774 "We report the cloning of a new gene,
  pct1+, encoding a 73-kD protein that interacts with p85cdc10 to form an MCB-binding
  heteromer."]; [PMID:7588609 "Fission yeast possess two such overlapping systems,
  Res1-Cdc10 and Res2-Cdc10, both of which act to start the mitotic and meiotic cycles."].
  Background (fetched from PubMed, not cached): Whitehall et al. 1999 (PMID:10564266)
  describe MBF as "composed of a common subunit called Cdc10 in combination with two
  alternative DNA-binding partners, Res1 and Res2" and find both Res proteins associated
  with Cdc10 throughout the cycle; Zhu et al. 1997 (PMID:9118941) show that for Res2 "The
  N-terminus is both necessary and sufficient for DNA binding, whereas the C-terminus is
  the region involved in the interaction with the Cdc10 protein."
- **Cdc10 does not supply sequence-specific DNA recognition.** [PMID:7739540 "We
  determined that p72res1 can bind specifically to the cdc22 promoter, when analyzed by
  gel mobility shift assay, and that the N-terminal 157 amino acids of p72res1 are
  sufficient for this specific binding."]; [PMID:7739540 "When overexpressed in vivo, a
  fragment of p72res1 containing this DNA-binding domain could rescue a strain carrying a
  temperature-sensitive cdc10 allele at the restrictive temperature as well as a strain
  with a cdc10 null allele."]; [PMID:7916653 "A single dominant mutation within the
  putative DNA-binding domain of p72sct1 renders the cell independent of cdc10 function for
  the execution of START."]; [PMID:18662996 "cells lacking Res1 or Res2, redundant
  DNA-binding subunits of MBF"]; [PMID:24006488 "whose core elements are the product of the
  Start gene cdc10 and Res1 and Res2, which form a heterodimeric DNA-binding domain"].
  The deep research reaches the same conclusion
  [file:SCHPO/cdc10/cdc10-deep-research-falcon.md "Accordingly, the most defensible model
  is that Res1/Res2 supply sequence-specific promoter recognition while the
  ankyrin-containing Cdc10 subunit serves as an essential interaction and regulatory
  platform."]. UniProt's HTH APSES-type domain (66-173) is a PROSITE-rule call, not an
  experimental one.
- **But MBF activity requires Cdc10 bound to Res1/Res2.** [PMID:7739540 "We also determined
  that the C-terminal region of p72res1 is necessary and sufficient for binding to
  p85cdc10."]; [PMID:7739540 "These results imply that the MBF activity in vivo is
  dependent on the interaction of p85cdc10 with p72res1."]. The Res1-DBD bypass of cdc10
  is the fission-yeast analogue of Swi6 relieving Swi4 auto-inhibition.
- **Activation is supplied by Rep2 (Rep1 in meiosis), not by Cdc10.** [PMID:7588609 "Our
  data suggest that Rep2 is a transcriptional activator subunit which interacts with the
  MCB binding subunit complex formed by Res2 and Cdc10."]; [PMID:14648198 "We found that
  cdc10+, res2+, rep1+ and rep2+ are required for correct meiotic transcription, while
  res1+ is not required for this process."]. Eshaghi et al. 2011 (PMID:21076007, fetched
  from PubMed, not cached) report that Cdc10-Res1-Res2 occupy promoters while Rep2 is
  recruited temporally with RNAP-II.
- **Targets.** cdc18 [PMID:7916658 "The product of the cdc18+ gene is a major downstream
  target of cdc10+, and transcription of cdc18+ is activated by cdc10+ during passage
  through START."]; cdt1 [PMID:8313888 "An essential gene, cdt1, has been isolated whose
  expression is cell cycle regulated in a cdc10 dependent manner."]; cig2 [PMID:11781565
  "We report here that the cell-cycle-regulated expression of the cyclin cig2 gene is
  dependent on MBF."]; cdt2 [PMID:12871901 "The mitotic expression of cdt2(+) was
  regulated by the MCB-DSC1 system."]; ctp1 [PMID:17936710 "Transcription of ctp1(+) is
  periodic during the cell cycle, with the onset of its expression coinciding with the
  start of DNA replication."]; genome-wide [PMID:19714215 "We conclude that both Cdc10p and
  Yox1p bind to most promoters of the previously proposed MBF target genes, including
  their own genes."].
- **Constitutive promoter occupancy; regulation by corepressors and phosphorylation.**
  [PMID:21132016 "MBF is bound to its target promoters throughout the cell cycle ( Wuarin
  et al, 2002 ), suggesting that MBF activity is not due to modulation of its DNA-binding
  activity."]; [PMID:9303312 "We show that the presence of the in vitro bandshift activity
  DSC1, conventionally thought to represent the active complex, requires res2p and
  correlates with inactive transcription."]. Native MBF purified through Cdc10-HA:
  [PMID:21132016 "The most enriched proteins in the purification were Cdc10, Res1, Res2,
  as expected, and a homeodomain-containing protein encoded by a nonessential open reading
  frame (SPBC21B10.13c), recently named Yox1"].
- **Negative role of the Cdc10 C terminus.** [PMID:8532516 "At permissive temperatures
  cdc10-C4 causes expression of MCB-regulated genes through the whole cell cycle, which in
  asynchronously dividing cells is manifested in overall higher expression levels."];
  [PMID:8532516 "These results suggest that DSC1Sp/MBF represses, as well as activates,
  MCB gene expression during the cell cycle."]; mechanism: [PMID:24006488 "the last two
  residues are in the C-terminal region of Cdc10, which is essential for loading the
  Yox1/Nrm1 repressor system onto chromatin"].
- **Replication checkpoint (Cds1).** [PMID:18662996 "Indeed, the double S720E T723E
  mutant, which we call cdc10-2E , and cdc10-8E , in which all eight potential
  phosphorylation sites are changed to glutamate, both showed constitutive cdc22 and
  overall MBF-dependent transcript levels comparable to wild-type checkpoint-induced
  levels"]; but [PMID:18662996 "We found that this allele, cdc10-8A , exhibited no
  significant defect in checkpoint regulation of transcription"], explained by redundancy
  with Nrm1/Yox1 phosphorylation [PMID:18662996 "This model suggests that, while not
  necessary for checkpoint regulation, phosphorylation of Cdc10 is sufficient for
  checkpoint regulation through disruption of the binding and inhibition of MBF by Nrm1."].
- **DNA-damage checkpoint (Chk1).** [PMID:24006488 "Here we show that Cdc10, which is an
  essential part of the MBF core, is the target of the DNA damage checkpoint."];
  [PMID:24006488 "When fission yeast cells are treated with DNA-damaging agents, Chk1 is
  activated and phosphorylates Cdc10 at its carboxy-terminal domain. This modification is
  responsible for the repression of MBF-dependent transcription through induced release of
  MBF from chromatin."]; the complex stays intact [PMID:24006488 "The interaction between
  Cdc10 and Res2 is preserved in MMS-treated cells."]; S720A S732A blocks release
  [PMID:24006488 "However, in a strain that carries the double mutation S720AS732A (here
  Cdc10.2A) and cannot be phosphorylated in vitro and in vivo by Chk1, the release of Cdc10
  was impaired from cdc18 promoter after treatment with MMS (Figure 6A)."].
- **Localization.** Nuclear [PMID:8223442 "We demonstrate that p85cdc10 is a nuclear
  protein"]; UniProt cites Ding et al. 2000 (GFP genomic library) for nucleus. The only
  cytoplasmic evidence is the proteome-wide YFP ORFeome screen [PMID:16823372 "Next, we
  determined the localization of 4,431 proteins, corresponding to approximately 90% of the
  fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."]. No
  Swi6-like regulated shuttling has been reported for Cdc10.
- **Pheromone.** [PMID:9034336 "We find that the G1-specific transcription factor
  p65cdc10-p72res1/sct1 which controls the expression of S-phase genes is fully activated
  in pheromone, unlike the analogous control in budding yeast."].
- **Pol5 / rRNA.** [PMID:16816948 "Pol5p appears to have no role in cell cycle gene
  expression, but is instead required for rRNA production."]; [PMID:16816948
  "Potentially, we have identified a mechanism by which Cdc10p controls rDNA gene
  expression, therefore linking the cell cycle with cellular growth."]; ChIP-chip
  [PMID:19714215 "Among these genes were four 5S ribosomal RNAs (SPRRNA.19, SPRRNA.20,
  SPRRNA.34, and SPRRNA.38), which is consistent with the finding that Cdc10p binds to
  Pol5p that is required for rRNA transcription"]. The 5S genes are Pol III templates,
  Pol5 binds rDNA (Pol I) promoters, and no cdc10 perturbation affecting rRNA synthesis is
  reported; the link stays speculative.
- **Other partners.** Puc1 cyclin and Ran1/Pat1 kinase [PMID:9201720 "We demonstrate that
  the Puc1 cyclin associates with Ran1 and Cdc10 in vivo and that the Ran1 protein kinase
  functions to control the association between Puc1 and Cdc10."]; INO80 [PMID:30134042
  "Here, we report that the Schizosaccharomyces pombe INO80 complex physically interacts
  with the mlui-binding factor (MBF) complex."]; Yox1 co-IP is MBF-dependent
  [PMID:21132016 "in the absence of Res1 or Res2, Yox1 was not able to bind to Cdc10"].

## Decisions on the non-trivial rows

1. **GO:0001228 (13 rows).** Ten enables-qualified experimental rows, the IBA and the ARBA
   IEA are MODIFY -> GO:0003713 transcription coactivator activity, with the explicit note
   that contributes_to GO:0001228 (PomBase's own qualifier on the Baum 1997 row, which is
   ACCEPTed) is an equally acceptable representation. Rationale: GO:0001228 is a
   DNA-binding TF activity, Cdc10 has no demonstrated sequence-specific DNA binding, and
   the DNA-binding subunits are Res1/Res2 (see quotes above). This mirrors the treatment of
   the equivalent IBA in the SWI6 review; the biology behind every row (Cdc10 is essential
   for MBF to activate cdc18/cdt1/cdc22/cig2/cdt2 and meiotic targets) is not questioned.
   The IBA gets a propagation_review (TERM_SCOPING_PROBLEM; ROLE_CONFLATION +
   WRONG_ORTHOLOG_OR_PARALOG) because its WITH list is Res2, Swi4 and Mbp1 only.
   The validator warns about inconsistent actions across the term; this is deliberate.
2. **GO:0000978 (7 rows).** All ACCEPT. Three carry contributes_to (IBA, Caligiuri 1993,
   Zhu 1994), which is exactly right; the enables rows (Lowndes 1992, Reymond 1993,
   Hofmann & Beach 1994, Skribbe 2025 HDA) record assays that physically detect Cdc10 in
   the MCB-bound complex (supershift, IP-PCR, ChIP-seq), and the reviews state that the
   binding is that of the complex.
3. **GO:0003677 IEA (InterPro APSES superfamily).** MARK_AS_OVER_ANNOTATED: intrinsic DNA
   binding has not been shown; the specific complex-level binding is already captured.
4. **GO:0005515 (7 rows).** Res1/Res2 partners -> MODIFY to GO:0140297 DNA-binding
   transcription factor binding (+ GO:0046982 heterodimerization for Ayte 1995 and Zhu
   1994). Pol5 -> REMOVE (no more specific MF supported). Yox1 -> REMOVE (association is
   MBF-dependent and probably indirect via Res2/Nrm1; a corepressor-binding term would
   overstate). Removal does not deny the interactions.
5. **GO:0005737 cytoplasm.** HDA (ORFeome) KEEP_AS_NON_CORE; IBA seeded only by Swi6
   REMOVE with propagation_review (PROPAGATION_BAD), since the Swi6 shuttling is
   lineage-specific and Cdc10 is nuclear and promoter-bound through the cycle.
6. **GO:0006357 EXP, GO:0045893 IDA -> MODIFY to GO:0045944; GO:0045892 IDA -> MODIFY to
   GO:0000122.** Granularity refinements only (all MBF targets are Pol II genes).
7. **GO:0009303 rRNA transcription IDA.** MARK_AS_OVER_ANNOTATED (see Pol5 above).
8. **GO:1900087 IMP (Stern & Nurse 1997).** ACCEPT: MBF transcription of cig2/cdc18/cdt1
   is the positive input to the G1/S CDK step, and cdc10 loss arrests at Start.
9. **Chromatin IDA rows** from abstract-only papers (Limbo 2007, Caligiuri 1997, Knezevic
   2018) are ACCEPTed with deference to the curator; the direct ChIP evidence is in
   Ivanova 2013 and Aligianni 2009.

## Core functions

1. MBF core subunit: GO:0003713 (enables), contributes_to GO:0000978, in GO:0030907,
   involved in GO:0045944 and GO:0000082, at nucleus/chromatin.
2. C-terminal coregulatory switch: GO:0003712, involved in GO:0000122 and GO:0045944
   (Nrm1/Yox1 loading; Cds1/Chk1 phospho-control of MBF occupancy).

No NEW terms proposed. The meiotic transcription role is folded into core function 1
rather than given a separate meiosis-specific process term.

## Open items

- Whether the Cdc10 N-terminal APSES-like region makes any DNA contact (structure needed).
- Whether GO would prefer contributes_to GO:0001228, GO:0003713 or GO:0003712 for the
  shared Swi6/Cdc10 subunits (same question raised in the SWI6 review).
- The Pol5/rRNA and replication-origin associations of Cdc10 lack functional tests.
