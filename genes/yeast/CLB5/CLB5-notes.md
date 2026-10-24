# CLB5 (P30283, YPR120C) — curation notes

Working notes for the GO annotation review of the budding-yeast S-phase cyclin Clb5.
Inline citations are verbatim quotes from the cached publications; the deep research
file is `CLB5-deep-research-falcon.md` (not edited).

## Identity and family

- S-phase entry cyclin-5; cyclin family, cyclin A/B subfamily; 435 aa; ~520 molecules/cell
  (UniProt P30283). Not essential. Interacts with Cdc28 (IntAct NbExp=6).
- CLB5 and CLB6 lie tail-to-tail next to CLB2 and CLB1 respectively and form a distinct pair
  of B-type cyclins [PMID:8253070 "Two new B-type cyclin genes from Saccharomyces cerevisiae,
  called CLB5 and CLB6, are located in a tail to tail arrangement adjacent to the G2/M phase
  promoting cyclins CLB2 and CLB1, respectively."].

## Core biology: S-phase cyclin of Cdc28

- Transcribed at Start with the G1/S program [PMID:8319908 "We describe a new family of B-type
  cyclin genes, CLB5 and CLB6, whose transcripts appear in late G1 along with those of CLN1,
  CLN2, and many genes required for DNA replication."]; expression peaks early in the cycle
  [PMID:8253070 "Both genes are periodically expressed, peaking early in the cell cycle."].
- Deletion phenotypes: [PMID:8319908 "Deletion of CLB6 has little or no effect, but deletion of
  CLB5 greatly extends S phase, and deleting both genes prevents the timely initiation of DNA
  replication."]; [PMID:8253070 "Loss of function mutants are viable, but clb5- mutants exhibit
  a delay in S phase whereas clb6- mutants show a delay in late G1 and/or S phase."].
- The S-phase-driving kinase is Clb5/6-Cdc28, not Cln-Cdc28 [PMID:8319908 "Thus, the kinase
  activity associated with Clb5/6 and not with Cln cyclins may be responsible for S-phase
  entry."]; ectopic CLB5 bypasses the Cln requirement [PMID:8319908 "Transcription of CLB5 and
  CLB6 is normally dependent on Cln activity, but ectopic CLB5 expression allows cells to
  proliferate in the absence of Cln cyclins."].
- Sic1 holds Clb-Cdc28 (not Cln-Cdc28) inactive until its Cdc34/SCF-dependent destruction
  [PMID:7954792 "cdc34 mutants cannot enter S phase because they fail to destroy p40SIC1, which
  is a potent inhibitor of Clb but not Cln forms of the Cdc28 kinase."]; the clb1-6 sextuple
  mutant arrests in G1 [PMID:7954792 "A sextuple clb1-6 mutant arrests as multibudded G1 cells
  that resemble cells lacking the Cdc34 ubiquitin-conjugating enzyme."].
- Origin-timing output: [PMID:9734354 "clb5 cells activate early origins but not late origins,
  explaining the previously described long clb5 S phase."]; [PMID:9734354 "Therefore, Clb5p
  promotes the timely activation of early and late origins, but Clb6p can activate only early
  origins."].
- Substrate targeting (deep research, not from cached primary papers): the Clb5 hydrophobic
  patch docks RXL/Cy motifs in Sic1, Orc6 and Cdc6; Clb5 binds Sld2 and clb5 clb6 delays Sld2
  phosphorylation; origin-bound Clb5-Orc6 docking contributes to re-replication control
  (Archambault et al. 2005, doi:10.4161/cc.4.1.1402; Bloom & Cross 2007, doi:10.1038/nrm2105).

## Localization and degradation

- [PMID:10848575 "In unbudded cells, small budded cells, and most large budded cells with an
  undivided nucleus, Clb5p is concentrated in the nucleus."]; at nuclear division the signal
  becomes diffuse [PMID:10848575 "In large budded cells with an undivided DNA mass near or
  spanning the bud neck and in large budded cells with two DNA signals, Clb5p is distributed
  diffusely throughout the cell."], coincident with destruction-box-dependent degradation
  [PMID:10848575 "Destruction box-dependent Clb5p degradation is strongly increased in mitotic
  cells"]. A residual cytoplasmic pool exists [PMID:10848575 "These differences in stability
  correlate with loss of detectable nuclear accumulation of Clb5p in dividing cells (although
  significant cytoplasmic signal remains)."].
- No study reports Clb5 at the spindle pole body; the propagated MTOC IBA (node PTN007424001,
  seeded by cdc13, crs1, cyclin B1/B2, Clb2) therefore lacks target evidence.

## Secondary (non-core) roles

- Spindle/SPB separation with Clb3/Clb4: [PMID:8319908 "Clb5 also has a function, along with
  Clb3 and Clb4, in the formation of mitotic spindles."]. Mechanism: the early Clb kinases
  inactivate APC-Hct1 in S phase [PMID:11438663 "Here we show that this relationship between
  anaphase-promoting complex (APC) and Clb proteins is reversed in S phase such that the early
  Clb kinases (Clb3, Clb4, and Clb5 kinases) inactivate APC Hct1 to allow Clb2 accumulation."];
  [PMID:11438663 "clb5 Δ cells fail to fully convert Hct1 to a single, low-mobility band"];
  [PMID:11438663 "In vitro assays have shown that Hct1 can also be phosphorylated by Clb5
  kinase"]. Cdh1 inactivation stabilizes Cin8/Kip1/Ase1 [PMID:16688214 "Our findings are
  consistent with a regulatory scheme for SPB separation ( Figure 7B ) in which Cdc28-Clb kinase
  mediates stabilization of microtubule-associated proteins (Cin8, Kip1 and Ase1) by
  inactivating Cdh1 via phosphorylation."]. So Clb5-Cdc28 does part of the work (Hct1
  phosphorylation), but the role is redundant and regulatory: KEEP_AS_NON_CORE for
  GO:0010696, GO:1901673 and GO:0000086.
- DNA damage response: [PMID:26801641 "Highest enrichment was observed for Cln2, Clb2 and
  Clb5"]; [PMID:26801641 "We found that clb5Δ cells show a decreased rate of extensive
  resection"]; [PMID:26801641 "Clb2 and Clb5 are needed for resistance of cells to DNA damaging
  agents"]. Graded KEEP_AS_NON_CORE, as in the CLB2 review.

## Meiosis

- [PMID:9732268 "Diploid clb5/clb5 clb6/clb6 mutants are unable to perform premeiotic DNA
  replication."]; single mutant: [PMID:9732268 "DNA replication in clb5/clb5 mutants was first
  detectable at ∼8 hr and appeared to be incomplete in many cells even after 24 hr"]; Clb5-Cdc28
  complexes are present in meiotic cells [PMID:9732268 "Clb5 is also detected in association
  with Cdc28 in extracts from meiotic cells"]. Clb1/3/4 cannot substitute even when expressed
  from the CLB5 promoter (DeCesare & Stuart 2012, doi:10.1534/genetics.111.134684; not cached).
  Premeiotic DNA replication rows are ACCEPTed as core because the function is Clb5/6-specific.

## Curation decisions worth flagging

1. GO:0005515 protein binding (4 IPI rows, all with Cdc28): the Kuhne & Linder row is MODIFIED
   to GO:0016538 because the paper's conclusion is that Clb5 associates with the p34CDC28 kinase
   in vivo [PMID:8253070 "Both cyclins have the potential to interact with the p34CDC28 kinase
   in vivo."]; the three high-throughput rows (Uetz Y2H, Breitkreutz KPI-MS, Michaelis AE-MS)
   are REMOVED as uninformative and redundant with GO:0016538/GO:0000307, without disputing the
   interaction.
2. GO:0007089 traversing Start (IBA from PTN000808767, seeded by S. pombe cig2 = SPAPB2B4.03;
   note the CLB2 review calls this donor cdc13, but PomBase resolves SPAPB2B4.03 to cig2 and
   SPBC582.03 to cdc13): MARK_AS_OVER_ANNOTATED. Clb5 is a product of the Start program and is
   Sic1-inhibited until after Start; its role is the G1/S transition (GO:0000082, ACCEPT), not
   the transcription/G1-CDK feedback that defines Start.
3. GO:0005815 MTOC (IBA): MARK_AS_OVER_ANNOTATED for lack of any SPB localization evidence on
   Clb5 and because the SPB-separation contribution runs through nuclear Cdh1 inactivation.
4. GO:0006355 regulation of DNA-templated transcription (IMP, Schwob & Nasmyth 1993):
   UNDECIDED. The cached record is abstract-only, the Genes Dev full text returned HTTP 403,
   and the abstract mentions transcription only as an input to CLB5/CLB6 expression.
5. GO:0045740 positive regulation of DNA replication: ACCEPTed as-is rather than MODIFIED to
   GO:0006270/GO:1902975 DNA replication initiation. Comparator check (QuickGO, taxon 559292):
   DNA replication initiation is carried by ORC/MCM/Sld2/Dpb11/Cdc7/Dbf4 and by no cyclin or
   by CDC28; SGD's convention places the cyclin-CDK on the regulatory term plus G1/S transition.
6. GO:0061575 (activator activity) is used in core_functions but not added as NEW: QuickGO shows
   SGD annotates no Cln/Clb cyclin to GO:0061575 (only BUR2/CTK2/CKS1 by IBA), whereas PomBase
   (cig2, cdc13) and human (CCNB1, CCND1-3) do; adding a child of the already-carried
   GO:0016538 would be redundant, so this is left as a validator warning and a note.
7. WITH/FROM oddities: the IGI rows from PMID:8253070 and PMID:9732268 list SGD:S000006324,
   which resolves to CLB5 itself (the genetic partner in both papers is CLB6, SGD:S000003341).
   Fields left as seeded; noted in the review summaries.

## Identifier resolutions used

SGD: S000000038 CLN3; S000002314 CLB3; S000003340 CLB1; S000003341 CLB6; S000004200 CLB4;
S000004812 CLN1; S000005584 ASE1; S000006177 CLN2; S000006323 CLB2; S000006324 CLB5.
PomBase: SPAPB2B4.03 cig2; SPBC582.03 cdc13; SPBC2G2.09c crs1; SPBC19F5.01c puc1; SPCC4E9.02 cig1.
