# SWI4 (P25302, YER111C) — working notes

Saccharomyces cerevisiae S288c. 1093 aa. Alternative name ART1. SGD:S000000913.
UniProt domain map: APSES/KilA-N HTH DNA-binding domain (37-147, HTH 71-92), four
central ankyrin repeats, conserved C-terminal Swi6-binding region; Cdk1 phosphosites at
Ser255 and Ser806 recorded from the Holt et al. 2009 phosphoproteome.

## 1. Biology in brief

**SBF DNA-binding subunit.** Swi4 is the sequence-specific DNA-binding subunit of SBF
(SCB-binding factor), the Swi4-Swi6 heterodimer that drives the Start (G1/S)
transcriptional program. The discovery papers identified the "cell-cycle box" of the HO
promoter and the two SWI genes that act through it
[PMID:3542227 "SWI4 and SWI6 are specifically required for CACGA4-mediated activation of transcription."]
[PMID:2649246 "We show that the SWI4 and SWI6 genes are required for formation of the CCBF-promoter complex in vitro, either as components of CCBF or as modulators of CCBF activity."],
and cloning of SWI4 placed the protein physically in that complex
[PMID:2689885 "We demonstrate by using antibodies to the SWI4 protein in gel-shift assays that the protein is present in the CCBF-DNA complex."].

**SCB elements and the division of labour with Swi6.** The DNA-recognition function sits
in Swi4, the regulatory function in Swi6
[PMID:1465410 "we propose that Swi4 is responsible for binding to the SCB sequence while Swi6, through its association with Swi4, regulates activity of the complex."]
[PMID:8423776 "From these data, we propose that the sequence-specific DNA-binding domain resides in SWI4 but that SWI6 controls the accessibility of this domain in the SWI4/6 complex."].
The N-terminal domain suffices for SCB recognition in vitro
[PMID:10490612 "Swi4 contains an N-terminal DNA binding domain that is sufficient for the specific recognition of SCB sequences in vitro"],
the SCB consensus is CA/GCGAAA
[PMID:20641022 "Swi4 is the sequence-specific DNA-binding subunit (CA/GCGAAA; Taylor et al., 2000), but Swi6 is required for binding to cell cycle-regulated promoters"],
and protein-binding microarrays recover the same motif class
[PMID:19111667 "We obtained binding specificities for 112 DNA-binding proteins representing 19 distinct structural classes."].
Swi4 and Mbp1 are the alternative DNA-binding subunits of the sister complexes SBF and MBF
[PMID:10490612 "Swi4 and Mbp1 are the DNA binding components of SBF and MBF, respectively."].

**C-terminal auto-inhibition relieved by Swi6.** Full-length Swi4 does not bind SCBs alone
because its C terminus folds back onto the DNA-binding domain; Swi6 binding to that C
terminus releases it
[PMID:10490612 "The interaction of the carboxy-terminal region of Swi4 with Swi6 alleviates this inhibition, allowing Swi4 to bind DNA."].
The inhibitory contact is intramolecular: Swi4 is monomeric and SBF is a 1:1 heterodimer
[PMID:10490612 "Full-length Swi4 was determined to be monomeric in solution, suggesting an intramolecular mechanism for auto-inhibition of binding to DNA by Swi4."]
[PMID:10490612 "SBF ran at 180 kDa, a size which is close to the predicted size of a heterodimer of Swi4 (123 kDa) and Swi6 (91 kDa)."].
The C terminus is necessary and sufficient for Swi6 association and dispensable for DNA binding
[PMID:8423776 "The C terminus of SWI4 is not required for SWI6-independent binding of SWI4 to SCB sequences, but it is necessary and sufficient for association with SWI6."],
and overproduced Swi4 can bypass Swi6 for HO transcription
[PMID:8423776 "Overproduction of SWI4 eliminates the SWI6 dependency of HO transcription in vivo and results in a new SWI6-independent, SCB-specific complex in vitro, which is heterogeneous and reacts with SWI4 antibodies."].

**Localization.** Swi4 is nuclear at every cell-cycle stage, in contrast to Swi6
[PMID:10490612 "We conclude that, unlike Swi6, whose localization changes throughout the cell cycle, Swi4 remains nuclear throughout the cell cycle."]
[PMID:10490612 "Indeed, Swi6 localization studies have confirmed that the majority of Swi6 is nuclear throughout the late M and G 1 phases but is largely cytoplasmic during the rest of the cell cycle"].
ChIP-chip and ChIP-PCR place it on promoter chromatin
[PMID:12464632 "Swi4, the DNA-binding component of SBF, was determined to bind upstream of 183 genes by chIp–chip analysis"]
[PMID:12464632 "Twenty-two of the 26 promoters tested were enriched in Swi4–HA immunoprecipitates over immunoprecipitated DNA from the untagged strain."].

**Whi5 repression and Start.** SBF sits on G1/S promoters in early G1 bound by the
corepressor Whi5, which is removed by Cln3-Cdc28 phosphorylation (the Rb/E2F analogy)
[PMID:15210110 "Whi5 was identified as a stably bound component of SBF but not MBF. Inactivation of Whi5 leads to premature expression of G1-specific genes and budding, whereas overexpression retards those processes."]
[PMID:15210110 "Cln/CDK phosphorylation of Whi5 in vitro promotes its dissociation from SBF complexes."]
[PMID:15210111 "Whi5 is recruited to G1/S promoter elements via its interaction with SBF/MBF in vivo and in vitro. In late G1 phase, CDK-dependent phosphorylation dissociates Whi5 from SBF and drives Whi5 out of the nucleus."].
The essential output of SBF (with MBF) is G1 cyclin transcription
[PMID:1832338 "We show that the essential role of SWI4 and SWI6 is to ensure the activity of G1-specific cyclin genes."]
[PMID:1832338 "SWI4 and SWI6 appear necessary for the transcription of CLN1 and CLN2, but not for that of CLN3."]
[PMID:10490612 "Maximal expression of the G 1 cyclin genes CLN1 , CLN2 , PCL1 , and PCL2 at Start requires the activity of a transcription factor, SBF (SCB binding factor)"].
Shut-off after G1 involves mitotic Clb2-Cdc28 binding the Swi4 ankyrin repeats
(Siegmund and Nasmyth 1996, not in the publication cache; taken from the deep-research
synthesis)
[file:yeast/SWI4/SWI4-deep-research-falcon.md "Four ankyrin repeats mediate protein interactions, including association with mitotic **Clb2–Cdc28/Cdk1**."].

**Slt2/Mpk1 cell-wall-integrity pathway.** Independently of Start, Swi4 is the
transcription factor engaged non-catalytically by the CWI MAP kinase Mpk1 (Slt2) and its
pseudokinase paralog Mlp1: activated Mpk1 docks on Swi4, confers DNA binding without
Swi6, and Swi6 is recruited afterwards
[PMID:18268013 "Transcriptional activation of FKS2 was dependent on the Swi4/Swi6 (SBF) transcription factor and on an activating signal to Mpk1 but not on protein kinase activity."]
[PMID:18268013 "Promoter association of Mpk1 and the Swi4 DNA-binding subunit of SBF were codependent but did not require Swi6, indicating that the MAPK confers DNA-binding ability to Swi4."]
[PMID:20641022 "This dimer binds to the FKS2 promoter, but requires the further binding of the Swi6 transcriptional activator for transcriptional initiation."].
Reporter genes for this branch (FKS2, CHA1, YKR013w, YLR042c) are induced by several
cell-wall stresses, heat being the strongest
[PMID:20641022 "Transcriptional induction of all of these reporters by cell wall stress was strictly dependent on both SWI4 and SWI6"]
[PMID:20641022 "Cell wall stress was induced by increasing the growth temperature from 23°C to 39°C, or by treatment with Congo Red"]
[PMID:20641022 "in general, elevated growth temperature was the strongest inducer for all of the reporters"].

**Other regulation (orientation only, from the deep-research file).** Whi5 and Swi6
phosphorylation are partly redundant routes to SBF activation, Bck2 gives a
Cln3-independent input, and during meiotic entry SBF is silenced jointly by Whi5 and a
long undecoded SWI4 transcript isoform (LUTI) that represses the canonical promoter
(Su et al. 2024). None of this is used to grade an annotation.

## 2. Publication cache status

Full text cached: PMID:10490612 (Baetz and Andrews 1999), PMID:12464632 (Horak 2002),
PMID:20641022 (Kim and Levin 2010), PMID:21179020 (Lambert 2010), PMID:37968396
(Michaelis 2023). Abstract only: PMID:3542227, PMID:2649246, PMID:2689885, PMID:1832338,
PMID:1465410, PMID:8423776, PMID:18268013, PMID:16429126, PMID:19111667, PMID:25112483.
Every quote in the review YAML is from the cached text; for abstract-only papers the
claims used are all in the abstract. The SBF-complex IDA from PMID:1832338 rests on
full-text gel-shift data that is not cached and is deferred to the SGD curator.

## 3. Key curation decisions

35 GOA rows, 35 rows in `existing_annotations`. Tally: ACCEPT 24, MODIFY 4, REMOVE 6,
KEEP_AS_NON_CORE 1.

- **GO:0000082 G1/S transition, GO:0001228 activator MF, GO:0000978 cis-regulatory
  DNA binding, GO:0045944 positive regulation of Pol II transcription, GO:0043565,
  GO:0003677, GO:0000785 chromatin, GO:0005634 nucleus, GO:0033309 SBF (x6),
  GO:0090575: ACCEPT.** All follow from Swi4 being the SCB-binding, activating subunit of
  SBF (quotes above). The GO:0000978 IBA carries `contributes_to`, which if anything
  understates the case since Swi4 supplies the DNA-binding activity outright; flagged as
  a suggested question, not changed. Swi4 appearing in its own WITH list on the IBA rows
  is the expected marker of experimental grounding on the target, not circularity.

- **GO:0005737 cytoplasm (IBA, is_active_in): REMOVE.** Seeded by the single donor Swi6,
  whose S/G2/M cytoplasmic pool is a Swi6-specific import-control property; Swi4 is
  constitutively nuclear
  [PMID:10490612 "We show that in contrast to Swi6, Swi4 remains nuclear throughout the cell cycle."]
  and the deep-research synthesis agrees
  [file:yeast/SWI4/SWI4-deep-research-falcon.md "Swi4 is predominantly **nuclear** and was reported to remain nuclear throughout the mitotic cell cycle."].
  Even for Swi6 the cytoplasm is where the inactive pool resides, so `is_active_in` is
  not the right claim for the node. Propagation review: PROPAGATION_BAD,
  COMPARTMENT_OR_COMPLEX_MISMATCH + WRONG_ORTHOLOG_OR_PARALOG.

- **GO:0030907 MBF transcription complex (IBA): REMOVE.** The PANTHER node
  PTN000917496 groups both DNA-binding paralogs (Swi4, Mbp1) with Swi6, so a
  complex-identity term that distinguishes SBF from MBF cannot sit at that node. Swi4 is
  in SBF, never MBF
  [PMID:10490612 "Since the SBF complex formed from insect cells and yeast extracts migrated at the same position, SBF is likely composed of only Swi4 and Swi6 proteins."]
  [file:yeast/SWI4/SWI4-deep-research-falcon.md "SBF contains Swi4 plus Swi6, whereas the related MBF complex substitutes Mbp1 for Swi4 while retaining Swi6."].
  The PomBase donors are correct for themselves (pombe has a single MBF); the SGD donors
  are Mbp1 and Swi6, the actual MBF subunits. Six experimental GO:0033309 rows already
  carry the correct complex.

- **GO:0042802 identical protein binding (IPI x2): REMOVE.** The 1999 IntAct row is a
  GST pull-down of the C-terminal 144 residues against N-terminal fragments in trans; the
  authors themselves conclude Swi4 is monomeric and the contact is intramolecular
  auto-inhibition
  [PMID:10490612 "showing that the C-terminal 144 amino acids of Swi4 can interact in vitro with the first 949 amino acids of Swi4"]
  [PMID:10490612 "Full-length Swi4 was determined to be monomeric in solution, suggesting an intramolecular mechanism for auto-inhibition of binding to DNA by Swi4."]
  [file:yeast/SWI4/SWI4-deep-research-falcon.md "Evidence that full-length Swi4 is monomeric favors **intramolecular** masking rather than inhibition through Swi4 oligomerization."].
  The 2010 row is bait recovery in an mChIP-MS survey; the paper never discusses a Swi4
  homo-oligomer. Recording either as homomeric binding misrepresents the mechanism.
  A dedicated in vivo stoichiometry experiment is proposed in `suggested_experiments`.

- **GO:0005515 protein binding with Swi6 (IPI x5): MODIFY x3, REMOVE x2.** Following
  the protein-binding policy: the targeted studies (Baetz and Andrews 1999, Lambert 2010,
  Imamura 2014) document the obligate SBF heterodimer, so GO:0046982 protein
  heterodimerization activity is proposed; the two proteome-wide surveys (Gavin 2006,
  Michaelis 2023) add nothing beyond the six SBF-complex rows and are marked REMOVE.
  Removal never asserts the interaction is false. Note that Lambert et al. misdescribe
  MBF as Swi4-Mbp1
  [PMID:21179020 "Two protein complexes essential for this process are the MBF and SBF transcription factors, composed of Swi4–Mbp1 and Swi4–Swi6, respectively (Moll et al, 1992)."];
  MBF is Mbp1-Swi6.

- **GO:0006355 regulation of DNA-templated transcription (IMP, PMID:18268013): MODIFY
  to GO:0045944.** Sound assertion, direction-neutral root term; the evidence is
  Swi4-dependent activation of FKS2 by Pol II, which the gene already carries as
  GO:0045944 from the companion 2010 paper. Granularity refinement only.

- **GO:0034605 cellular response to heat (IMP, PMID:20641022): KEEP_AS_NON_CORE.**
  Swi4 genuinely executes the transcriptional output of a heat-triggered response, but
  heat is one of four cell-wall stressors used interchangeably in that paper and the
  process Swi4 serves is the Rlm1-independent CWI transcriptional response, not a
  heat-shock program. Kept, graded non-core. For consistency the term was dropped from
  the `directly_involved_in` list of the second core function (a KEEP_AS_NON_CORE row
  should not be listed as a core process); that core function keeps GO:0045944. Whether
  a CWI-signalling or fungal-type cell wall organization term is the intended
  representation of the Swi4-Mpk1 branch is raised in `suggested_questions`.

- **No NEW rows.** Everything the literature supports is already covered; the missing
  representation of the Swi4-Mpk1 complex and of the contributes_to/enables asymmetry on
  the IBA rows is raised as questions rather than asserted.

## 4. Core functions

1. SCB-binding, Pol II-activating subunit of SBF driving the G1/S regulon (CLN1, CLN2,
   PCL1, PCL2, HO, cell-wall and bud-emergence genes); nucleus, chromatin; in SBF.
2. Transcription factor engaged non-catalytically by Mpk1/Mlp1 under cell-wall stress,
   binding FKS2/CHA1/YKR013w/YLR042c promoters independently of Swi6 before Swi6 is
   recruited; nucleus, chromatin. Process: GO:0045944 (the heat term is graded non-core).

## 5. Session log

- Review blocks completed by the previous reviewer (35/35 rows, no PENDING).
- This session: read the two validation warnings; dropped GO:0034605 from
  core_functions[1] (consistent with KEEP_AS_NON_CORE); added verbatim deep-research
  quotes as corroborating `supported_by` entries on the cytoplasm, MBF and
  identical-protein-binding REMOVE rows and on the Clb2-Cdc28 statement in core
  function 1; populated `findings` for the deep-research reference; checked every
  `existing_annotations` row against SWI4-goa.tsv (35 = 35, no placeholder text);
  wrote these notes; re-validated and rendered.
- 2026-09-29: aligned all seven IBA rows with the current `PTHR24198` PAINT
  snapshot. Added `PANTHER:PTN000917496` as the PTN-level source in
  `propagation_review` blocks for the four supported IBA rows, kept the cytoplasm and
  MBF transfers as `PROPAGATION_BAD`, and searched newer literature. PMID:40124484
  provides 2025 full-text support for Swi4-dependent SWI4 autoregulation at Start but
  does not require a new GO term.
