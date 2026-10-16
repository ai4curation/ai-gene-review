# CLN2 (P20438, *Saccharomyces cerevisiae*) - curation notes

Working journal for the GO annotation review in `CLN2-ai-review.yaml`.
Systematic name YPL256C; Complex Portal CPX-342 (CLN2-CDC28 kinase complex).
Not to be confused with human *CLN2* (neuronal ceroid lipofuscinosis 2, now
*TPP1*, a lysosomal tripeptidyl peptidase), which is unrelated.

## 1. Biology in brief

Cln2 is one of the two closely related late-G1 cyclins (Cln1/Cln2) of budding
yeast and, with the upstream cyclin Cln3, forms the trio of Cln proteins of
which at least one is required for passage through Start. It has no catalytic
activity: it is a cyclin-box protein that binds the sole essential CDK Cdc28
and confers a strong, G1-restricted kinase activity on it.

**Discovery and genetics.** CLN1 and CLN2 were cloned as dosage suppressors of
*cdc28-ts*; the dominant *CLN2-1* truncation removes the destabilising C
terminus and short-circuits G1 control
[PMID:2569741 "Two Saccharomyces cerevisiae genes were isolated based upon their dosage-dependent rescue of a temperature-sensitive mutation of the gene CDC28"]
[PMID:2569741 "A dominant mutation in the CLN2 gene, CLN2-1, advances the G1- to S-phase transition in cycling cells and impairs the ability of cells to arrest in G1 phase in response to external signals"].
The three CLN genes are redundant for an essential G1 function
[PMID:2574633 "Mutational elimination of the CLN1, CLN2, and DAF1/WHI1 products leads to cell cycle arrest independent of cell type, while expression of any one of the genes allows cell proliferation"]
[PMID:2574633 "The data are consistent with the hypothesis that Cln proteins activate the Cdc28 protein kinase, shown to be essential for the G1 to S phase transition in S. cerevisiae"],
and the triple-mutant arrest is a genuine Start arrest independent of the
pheromone pathway
[PMID:2147225 "Null mutations in three genes encoding cyclin-like proteins (CLN1, CLN2, and CLN3) in Saccharomyces cerevisiae cause cell cycle arrest in G1 (cln arrest)"]
[PMID:2147225 "These results are consistent with a specific CLN requirement for START transit"].

**Cdc28 holoenzyme and activator activity.** Cln2 co-immunoprecipitates with
p34CDC28 as an active kinase
[PMID:2142620 "we demonstrate that the Cln2 polypeptide interacts with p34CDC28 to form an active protein kinase complex"].
Activation was reconstituted biochemically: a GST-Cln2 chimera added to a
cyclin-depleted G1 extract activates Cdc28 as an H1 kinase in a manner that
needs ATP, cytosol and the CAK site Thr169
[PMID:7862657 "A glutathione S-transferase-G1 cyclin chimera (GST-Cln2p) efficiently binds to and activates Cdc28p as a histone H1 kinase"]
[PMID:7862657 "Activation of Cdc28p by GST-Cln2p requires ATP, crude yeast cytosol, and the conserved Thr-169 residue that serves in other organisms as a substrate for phosphorylation by cyclin-dependent protein kinase-activating kinase"].
The active G1 holoenzyme is a trimer with Cks1
[PMID:10913169 "Cln2 and Cdc28 subunits coexpressed in baculovirus-infected insect cells fail to exhibit protein kinase activity towards multiple substrates in the absence of Cks1"]
[PMID:10913169 "Cks1 can both stabilize Cln2-Cdc28 complexes and activate intact complexes in vitro"].
Cln1/Cln2-associated kinase is far stronger than that of the rare Cln3, which
was proposed to act upstream
[PMID:8387915 "Cln3 is a much rarer protein than Cln1 or Cln2 and has a much weaker associated histone H1 kinase activity"]
[PMID:8387915 "the G1 cyclins Cln1, Cln2 and Cln3 regulate entry into the cell cycle (Start) by activating the Cdc28 protein kinase"].

**SBF-driven transcription and the Whi5 feedback loop.** CLN1 and CLN2 are
transcribed in late G1 by SBF (Swi4/Swi6)
[PMID:1832338 "SWI4 and SWI6 appear necessary for the transcription of CLN1 and CLN2, but not for that of CLN3"],
and the transcript and protein peak in G1 and collapse in S phase or on
pheromone exposure
[PMID:2142620 "The CLN2 gene encodes a 62 kd polypeptide that accumulates periodically, peaking during G1 and decreasing rapidly thereafter, and is rapidly lost following exposure of cells to mating pheromone"].
Cln3-Cdc28 begins the derepression of SBF by acting on the bound repressor
Whi5; Cln2-Cdc28 completes it. Recombinant Cln2-Cdc28 phosphorylates Whi5 and
strips it from a preassembled Whi5-Swi4-Swi6 complex, an activity that purified
Cln3-Cdc28 and Pcl9-Pho85 lack, and in vivo the Whi5 phosphoforms depend on
CLN1/CLN2
[PMID:19823668 "As expected, Cln2-Cdc28 phosphorylation caused most of the SBF-bound Whi5 to be released into the soluble fraction"]
[PMID:19823668 "However, both purified Cln3-Cdc28 and Pcl9-Pho85 failed to affect Whi5-SBF stability in vitro, while complex disruption was effectively achieved in the presence of Cln2-Cdc28 kinases"]
[PMID:19823668 "slow migrating Whi5 isoforms present in asynchronous wt extracts (Figure 2B, lane 1) were modestly reduced in cells lacking CLN3 (Figure 2B, lane 7) and completely absent in a cln1Δ cln2Δ double mutant (Figure 2B, lane 6), confirming that Whi5 phosphorylation depends on Cln-Cdc28 kinase complexes"]
[PMID:19823668 "Whi5 is then further phosphorylated by Cln1- and Cln2-Cdc28 complexes leading to complete disassembly of the Whi5-SBF complex, Whi5 nuclear export and a burst in gene expression necessary for the G1/S phase transition"]
[PMID:15210110 "Cln/CDK phosphorylation of Whi5 in vitro promotes its dissociation from SBF complexes"].
Cln1/Cln2-Cdc28 are also the physiological kinases for the Swi6-binding Start
regulator Stb1
[PMID:10409718 "Stb1 was an excellent substrate for both the Cln1-Cdc28 and Cln2-Cdc28 kinases in vitro and was a better in vitro substrate than histone H1"]
[PMID:10409718 "several observations suggest that Cln1-Cdc28 and Cln2-Cdc28 are the physiological kinases for Stb1 phosphorylation"].
Note the historical caveat that Cln3 alone suffices to switch SBF on
[PMID:10409718 "CLN1 and CLN2 are not required for gene activation but are important for the proper execution of other Start-related events such as budding and DNA synthesis"];
the Cln1/Cln2 contribution is the positive feedback that makes the burst
complete and coherent
[PMID:19823668 "recent analysis of cyclin gene expression using a single cell assay affirms that positive feedback involving the Cln1 and Cln2 cyclins induces the G1/S regulon, and that this regulatory feedback is important for maintaining coherence of gene expression at Start"].
The deep-research synthesis reaches the same picture
[file:yeast/CLN2/CLN2-deep-research-falcon.md "SBF induces **CLN1** and **CLN2**, after which Cln1/2–Cdc28 reinforces the transition by phosphorylating the SBF repressor Whi5. This creates positive feedback that sharpens late-G1 transcription and promotes commitment."].

**Sic1 and Far1 phosphorylation - releasing Clb-Cdc28.** DNA replication needs
Clb5/6-Cdc28, which is held inactive by Sic1, an inhibitor that does not act on
Cln-Cdc28
[PMID:7954792 "cdc34 mutants cannot enter S phase because they fail to destroy p40SIC1, which is a potent inhibitor of Clb but not Cln forms of the Cdc28 kinase"].
Cln2-Cdk1 initiates the multisite phosphorylation of Sic1 through a
Cln2-specific docking motif, building the platform that Clb5-Cdk1 then extends
to the Cdc4 degrons
[PMID:21993622 "We propose that in late G1, Clb5-Cdk1 is inhibited by Sic1, and the cascade of phosphorylation events begins with T5 phosphorylation by Cln2-Cdk1"]
[PMID:21993622 "However, the phosphorylated cluster pT5/pT33/pT45/pS76 serves as a powerful Cln2-Cdk1-dependent docking platform for emerging Clb5-Cdk1"]
[PMID:21993622 "we additionally mutated the Cln2-specific docking site VLLPP in the triple mutant background"].
Far1, the pheromone-induced CDK inhibitor that binds Cln-Cdc28 after Fus3
phosphorylation, is itself phosphorylated on Ser87 by Cdc28-Cln2, which
licenses its SCF(Cdc4)-dependent ubiquitylation in the nucleus
[PMID:11080155 "The cell cycle arrest function requires phosphorylation of Far1 by Fus3, which promotes binding of Far1 to the Cdc28–Cln complex ( Peter et al ."]
[PMID:11080155 "ubiquitylation of Far1-nls1 or Far1-nls1/2 was dependent on phosphorylation of serine 87 by Cdc28–Cln2"]
[PMID:11080155 "cells arrested by depletion of the G 1 cyclins did not accumulate phosphorylated forms of wild-type Far1 or Far1-nls1 (Figure 4 B, – Cln2), while the same cells grown under conditions that allow expression of Cln2 resulted in efficient phosphorylation of these proteins (+ Cln2)"]
[PMID:11080155 "These results imply that the kinase that triggers degradation of Far1 is active in the nucleus."].

**Bud emergence and the cytoplasmic pool.** Cln2 is the cyclin thought to
trigger bud emergence, and unlike Cln3 it is mostly cytoplasmic, concentrated at
sites of polarized growth
[PMID:11509671 "Cln2, thought to trigger other events, such as bud emergence ( 7 , 12 , 15 , 40 ), is localized primarily to the cytoplasm ( 45 )."]
[PMID:10611233 "In contrast, Cln2p localizes to the cytoplasm."]
[PMID:10611233 "This is the first indication of a cytoplasmic function for a cyclin-dependent kinase"]
[PMID:11792824 "Cytoplasmic Cln2 was concentrated at sites of polarized growth"].
A nuclear pool is also functional: an appended NES cripples some Cln2
functions, Cln2-GFP is seen in both compartments, and forced-localization
cassettes split the functions between compartments
[PMID:10611233 "We found NES-dependent decreases in Cln2p and Cln3-1p activity in both cln complementation and cell size assays, indicating that the presence of Cln proteins in the nucleus is critical for some CLN functions"]
[PMID:11080155 "Cln1–GFP as well as Cln2–GFP were localized in both the nucleus and the cytoplasm"]
[PMID:11792824 "Forced localization showed that some functions of Cln2 required a cytoplasmic location, while other functions required a nuclear location"].
The steady-state cytoplasmic residence is an actively maintained, Cdc28-dependent
state: unphosphorylated Cln2 is nuclear, and Cdc28-dependent phosphorylation of
the C terminus drives nuclear exclusion
[PMID:11509671 "Both binding to Cdc28p and Cdc28p-dependent phosphorylation in the C-terminal region of Cln2p are independently required for efficient nuclear depletion of Cln2p, suggesting that this process may be physiologically regulated"]
[PMID:11509671 "These data are consistent with regulated shuttling of Cln2p in and out of the nucleus, where nonphosphorylated Cln2p is enriched in the nucleus and phosphorylated Cln2p is enriched in the cytoplasm"].
The specific cytoplasmic substrates remain incompletely defined
[PMID:10611233 "Although the putative cytoplasmic function remains poorly defined, it is likely to involve some aspect of cell polarity determination or bud emergence ( 29 )."];
the deep-research file highlights the cyclin-replacement work of Ercan et al.
2021 (not cached) showing that a mitotic cyclin cannot substitute for Cln
function in polarization and budding.

**Grr1-dependent instability.** Cln2 protein is short-lived; the deep-research
file gives a half-life of about 10 min and maps the instability to PEST-rich
C-terminal sequences
[file:yeast/CLN2/CLN2-deep-research-falcon.md "The protein is highly unstable, with an estimated half-life of approximately **10 minutes**, and older measurements generally place it below **15 minutes**."].
Turnover is mainly through SCF(Grr1), reconstituted for the paralog Cln1
[PMID:11080155 "In addition to Sic1, SCF Cdc4 is required to degrade Far1, Cdc6 and Gcn4, while ubiquitylation of the G 1 cyclins, Cln1 and Cln2, and the bud emergence protein Gic2 is mediated by SCF Grr1 ( Deshaies, 1999 )."]
[PMID:10213692 "Phosphorylated Cln1 was ubiquitinated by SCF (Skp1-Cdc53-F-box protein) complexes containing the F-box protein Grr1, Rbx1, and the E2 Cdc34."],
with a context-dependent SCF(Cdc4) contribution that the deep-research file
flags as unresolved
[file:yeast/CLN2/CLN2-deep-research-falcon.md "SCF^Grr1-mediated ubiquitylation and proteasomal destruction are strongly established. Loss of SCF^Grr1 activity impairs normal Cln2 turnover and causes abnormal accumulation."].

**Pheromone response and recovery.** Beyond degrading Far1, Cln2-Cdc28 shuts the
mating MAPK pathway off by phosphorylating the scaffold Ste5 (and Ste20), which
is why cells past Start are refractory to pheromone
[PMID:17289571 "In this study, we report that G1 CDK activity inhibits pheromone signaling by inhibiting Ste5 membrane recruitment"]
[PMID:17289571 "Cln2/CDK can phosphorylate the PAK-family kinase Ste20"].
POG1 and MSG5 promote recovery from pheromone arrest through CLN2
[PMID:9927449 "Genetic tests strongly argue that POG1 promotes recovery through upregulation of the CLN2 gene and that the resulting Cln2 protein promotes recovery primarily through an effect on Ste20, an activator of the mating MAPK cascade"].

## 2. Review decisions

34 GOA rows plus one proposed NEW row. Summary of calls:

### ACCEPT (core)

- **GO:0000082 G1/S transition of mitotic cell cycle** (IBA). The IBD at node
  PTN000019791 (G1 cyclins) is sound; Cln2's Whi5/Sic1/Far1 biology is exactly
  the term definition (build-up of G1 CDK, transcription of G1 cyclins,
  positive feedback committing the cell to S phase). Cln2 is not in this row's
  WITH/FROM, but the sister members Cln3, Clb5 and Clb6 are.
- **GO:0007089 traversing start control point** (IEA, IGI x2, IMP). The
  classic CLN genetics (Hadwiger 1989, Richardson 1989, Cross 1990) and an ARBA
  mapping that happens to be specific and correct.
- **GO:0000307 cyclin-dependent protein kinase holoenzyme complex** (IBA, IDA,
  IEA, IPI). Directly demonstrated (Wittenberg 1990, Reynard 2000). The target
  appearing in its own IBA WITH/FROM is expected, not circular.
- **GO:0005634 nucleus** (IBA `is_active_in`, IDA x3). Two labs and three
  methods (NES effect, GFP, fractionation/forced localization) plus nuclear
  substrates (Whi5, Stb1, Sic1, Far1).
- **GO:0005737 cytoplasm** (IBA `is_active_in`, IDA x4, IMP). The point of
  divergence from the CLN3 review: for Cln3 the IBA cytoplasm row is
  over-stated (the ER pool is sequestered), but for Cln2 cytoplasmic activity
  is a documented, Cln2-specific property confirmed by forced-localization
  genetics, so the same node-level IBA is accepted here. The IMP row (Miller &
  Cross 2001) records that phospho-site, cdc28-4 and cyclin-box mutants shift
  Cln2 into the nucleus, i.e. the cytoplasm is the actively maintained default.

### MODIFY

- **GO:0016538 CDK regulator activity -> GO:0061575 CDK activator activity**
  (IBA, IEA, IDA x3). Same treatment as CLN3: every experiment measures Cln2
  conferring kinase activity on Cdc28 (Deshaies & Kirschner 1995 in vitro;
  Tyers 1993 and Ho 1999 immunoprecipitates), the PAINT node contains no CDK
  inhibitors, and the parent is merely less informative. All five rows carry
  the same action so the validator's consistency check is satisfied. IBA
  `propagation_review`: `TERM_SCOPING_PROBLEM` / `GRANULARITY_MISMATCH`, node
  `SUPPORTS_TRANSFER`.
- **GO:0005515 protein binding** (IPI x6, all with Cdc28). Repository policy:
  generic protein binding is uninformative. The four high-throughput AP-MS
  rows (Gavin 2002, Ho 2002, Gavin 2006, Breitkreutz 2010) -> GO:0019901
  protein kinase binding. Reynard 2000 (Cln2-Cdc28 kinase assays) and
  Strickfaden 2007 (Cln2/CDK phosphorylation of Ste5) -> GO:0061575, since
  both measure Cln2 acting as the activating, substrate-directing subunit.
- **GO:1902806 regulation of cell cycle G1/S phase transition -> GO:1900087
  positive regulation of G1/S transition of mitotic cell cycle** (NAS from
  Complex Portal on Hadwiger 1989). The definition fits and the sign is
  positive (CLN2-1 advances G1/S); mirrors the CLN3 call.
- **GO:2000045 regulation of G1/S transition of mitotic cell cycle ->
  GO:1900087** (IEA, InterPro2GO from the Cyclin_CLN family IPR014399).
  Correct but direction-less family mapping.

### KEEP_AS_NON_CORE

- **GO:0000321 re-entry into mitotic cell cycle after pheromone arrest**
  (IGI x2 with POG1 and MSG5, Leza & Elion 1999). The participation test is
  met - Cln2-Cdc28 phosphorylates Far1 and Ste5/Ste20, which is the work of
  recovery - so the annotation is correct, but it is a context-specific
  downstream application of the same G1 CDK activity that executes Start,
  hence non-core. Abstract-only cache; the epistasis details are deferred to
  the SGD curator.

### NEW

- **GO:0045944 positive regulation of transcription by RNA polymerase II**
  (`involved_in`, IDA, PMID:19823668). Added to close the gap between
  `core_functions` (which lists the term for the Whi5/Stb1 feedback function)
  and `existing_annotations`, where CLN2 carried nothing on the transcription
  branch. Participation: Cln2-Cdc28 is the kinase that phosphorylates Whi5 and
  Stb1 and dissociates Whi5 from SBF - it performs the step, it is not merely
  required for it. Comparator: SGD annotates the sister cyclin Cln3 to
  GO:0006357 (IGI/IMP) from the same Huang et al. 2009 paper, so this branch is
  one curators use for the Whi5 kinase; the CLN3 review modifies those rows to
  GO:0045944, and using the positive term here keeps the two reviews
  consistent. GO:0045944 is on a different branch from GO:0000082 /
  GO:0007089, so it is not redundant with them. The "Cln1/Cln2 not required
  for gene activation" caveat (Ho 1999) is acknowledged in the row: it concerns
  the initial switch-on, which Cln3 can achieve alone, not the feedback that
  completes it.

### No REMOVE, MARK_AS_OVER_ANNOTATED or UNDECIDED calls

Every experimental row is consistent with the synthesized picture. The
abstract-only caches (Hadwiger 1989, Richardson 1989, Cross 1990, Wittenberg
1990, Tyers 1993, Deshaies & Kirschner 1995, Leza & Elion 1999, Reynard 2000,
Edgington & Futcher 2001, de Bruin 2004, and the four AP-MS surveys) each state
the relevant result in the abstract; full text is cached for Miller & Cross
2000/2001, Ho 1999, Blondel 2000, Huang 2009, Koivomagi 2011, and the
abstract-plus-introduction of Strickfaden 2007.

## 3. Core functions

1. **Cdc28 activator that executes Start** - MF GO:0061575; BP GO:0000082,
   GO:0007089, GO:0045944; CC nucleus; complex GO:0000307. The Whi5/Stb1
   positive-feedback arm.
2. **Inhibitor-clearing and morphogenetic arm** - the same MF/complex; BP
   GO:1900087; locations nucleus and cytoplasm. Sic1 priming, Far1 Ser87
   phosphorylation, Ste5 inhibition, and the cytoplasmic pool at sites of
   polarized growth.

Open questions recorded in `suggested_questions`: the identity of the
cytoplasmic substrates behind the Cln2-specific budding role; whether the
transient nuclear pool of hypophosphorylated Cln2 in newborn cells is the one
that acts on Whi5/Sic1; and the physiological split between SCF(Grr1) and
SCF(Cdc4) in Cln2 turnover.

## 4. Validation log

- Initial state (previous reviewer, interrupted before notes): valid with 2
  warnings - no annotation cited the Falcon deep-research file, and the
  core-function term GO:0045944 was absent from `existing_annotations`.
- Fixes: NEW GO:0045944 row added (IDA, Huang et al. 2009 full text, plus de
  Bruin 2004 abstract, Ho 1999 and the deep-research file); the deep-research
  file also cited on the cytoplasm IBA row; `file:` and PMID:15210110
  reference entries added with `reference_review`.
- Coverage check: all 34 GOA rows (term x evidence x reference) have a
  matching `existing_annotations` entry with complete `review` blocks; no
  placeholder text remains. Final tally: 19 ACCEPT, 13 MODIFY, 2
  KEEP_AS_NON_CORE, 1 NEW.
- Final state: 0 errors, 0 warnings.
