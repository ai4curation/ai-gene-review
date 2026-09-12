# swi6 (S. pombe) curation notes

Swi6 / P40381 / SPAC664.01c — the principal HP1 (heterochromatin protein 1) ortholog of fission yeast.
328 aa, chromodomain (CD, ~81-143) + chromoshadow domain (CSD, ~267-328) connected by a disordered hinge.

## Domain architecture & molecular function
- CD binds H3K9me2/3 (written by Clr4); CSD homodimerizes and is a protein-protein interaction platform.
- [PMID:11242054 "HP1 can bind with high affinity to histone H3 methylated at lysine 9 but not at lysine 4. The chromo domain of HP1 is identified as its methyl-lysine-binding domain."] — H3K9me reader = CD.
- [PMID:11242054 "the methylase activity of Clr4 is necessary for the correct localization of Swi6 at centromeric heterochromatin and for gene silencing."]
- [PMID:10801440 "The 1.9 A crystal structure of the Swi6 CSD is presented here. This reveals a novel dimeric structure"] and [PMID:10801440 "Dimerisation through the CSD of HP1-like proteins results in the simultaneous formation of a putative protein-protein interaction pit, providing a potential means of targeting CSD-containing proteins to particular chromatin sites."] — CSD dimerization / adaptor platform; this is the homodimerization (identical protein binding) annotation.
- [PMID:23485968 "binding of the key S. pombe HP1 protein, Swi6, to methylated nucleosomes drives a switch from an auto-inhibited state to a spreading-competent state."] and [PMID:23485968 "The CD recognizes the H3K9me3 mark ... while the CSD can homodimerize ... and binds specific protein sequences ... The hinge is implicated in sequence-independent RNA and DNA binding"]. Self-association/oligomerization drives spreading. DimerX (L315D) disrupts CSD-CSD dimerization.
- RNA binding: [PMID:22683269 "RNA competes with methylated histone H3K9 for binding to the chromodomain of HP1(Swi6)"]; [PMID:22683269 "the fission yeast HP1(Swi6) protein guarantees tight repression of heterochromatic genes through RNA sequestration and degradation."] Hinge basic patch binds RNA.
- DNA binding: hinge binds DNA sequence-independently (PMID:23485968). Note GOA DNA-binding annotation PMID:37400983 is actually a Chp2 paper; treat with caution (see below).

## Chromatin-protein adaptor activity (scaffold/effector recruitment)
- Cohesin: [PMID:11780129 "the preferential localization of cohesins at the centromeric repeats is dependent on Swi6"]; [PMID:11780129 "a cohesin subunit Psc3 interacts with Swi6 and its mouse homologue HP1."] = chromatin-protein adaptor; Psc3 = SPAC17H9.20.
- Epe1 (JmjC): [PMID:16762840 "Epe1 is recruited to heterochromatic loci by the heterochromatin protein Swi6/HP1."]; balances opposing activities [PMID:16762840 "Swi6/HP1 recruits opposing chromatin-modifying activities, the balancing of which is crucial for heterochromatin maintenance."] (Epe1 = SPBP35G2.03c; also PMID:17449867.)
- Ers1 (RNAi/RDRC bridge): [PMID:22474355 "Swi6 recruits RDRC to heterochromatin through Ers1"]; [PMID:22474355 "a direct interaction with Swi6 was detected"]. Ers1 = O94717 / SPAC3G6.01.
- SHREC / Clr3 recruitment governed by Swi6 phosphorylation: [PMID:19136623 "a HP1 homolog Swi6 recruits SHREC, Epe1, and cohesin, which are involved in transcriptional gene silencing (TGS), transcriptional activation, and sister chromatid cohesion, respectively."]; CK2 phospho of Swi6 controls SHREC recruitment / TGS: [PMID:19136623 "CK2-dependent Swi6 phosphorylation specifically controls TGS in heterochromatin."]
- Shugoshin Sgo1 (meiotic cohesion protection): [PMID:18716626 "the heterochromatin protein Swi6 associates directly with meiosis-specific shugoshin Sgo1, a protector of cohesin at centromeres."]; [PMID:18716626 "The forced centromeric localization of Sgo1 restores proper meiotic chromosome segregation in swi6 cells."] = GO:1990813 meiotic centromeric cohesion protection. Sgo1 = Q9P7A0.
- DDK (Hsk1-Dfp1): PMID:14625560 (Hsk1=P50582) & PMID:31000521 Swi6-Dfp1; [PMID:31000521 "Swi6 interacts with Dfp1, a regulatory subunit of DBF4-dependent kinase (DDK)"].
- Swi2 (mat switching donor selection): [PMID:36951094 "we identified two functionally important motifs in Swi2, a Swi6 (HP1 homolog)-binding site and two DNA-binding AT-hooks."]; [PMID:36951094 "the Swi6-binding site was required for Swi2 localization at SRE2 to select mat2-P in M cells."]
- Hrp3 (CHD remodeler) interaction: PMID:22990236 (O14139).

## Localization / cellular component
- [PMID:7660126 "Swi6p localizes with these three chromosomal regions"] (mating-type loci, centromeres, telomeres); [PMID:7660126 "In cells lacking Swi6p, centromeres lag on the spindle during anaphase and chromosomes are lost at high rates."]
- [PMID:11069763 "GFP-Swi6p localises to the nucleus and is concentrated at the heterochromatic centromeres and telomeres."]
- [PMID:11283354 "Localization of Swi6 ... to heterochomatic regions is dependent on H3 Lys9 methylation."]
- Heterochromatin island (facultative): PMID:22144463 (RNA elimination machinery / meiotic mRNA islands).

## Biological process
- Heterochromatin/silencing at centromere, telomere, mat locus, rDNA.
- Pericentric het formation: PMID:19443688, PMID:19136623, PMID:31000521 (cohesin enrichment, biorientation, segregation).
- Cohesion/segregation: [PMID:31000521 "Swi6 is required for cohesin enrichment at the pericentromere. Loss of Swi6 leads to abnormal mitosis, including defects in the establishment of bioriented sister kinetochores and microtubule attachment."]; [PMID:31000521 "Swi6 is necessary for centromeric localization of Rad21-GFP independent of DDK."]
- Mat switching / donor selection / gene conversion: PMID:1620099, PMID:6587363, PMID:29852001, PMID:36951094. [PMID:29852001 "Mating-type switching in Schizosaccharomyces pombe entails programmed gene conversion events regulated by DNA replication, heterochromatin, and the HP1-like chromodomain protein Swi6."]; donor directionality — in absence of Swi6 cells prefer mat3-M [PMID:36951094 "in the absence of Swi6, h90 cells prefer to use the mat3-M donor over the mat2-P donor"].
- RNAi / co-transcriptional silencing: PMID:17512405, PMID:12193640, PMID:22474355, PMID:19111658. [PMID:19111658 "Swi6 ... is required for efficient RNAi-dependent processing of these transcripts"] and [PMID:19111658 "Swi6 ... a major role in processing of centromeric transcripts into siRNAs."]
- siRNA-mediated mat-cassette het formation: PMID:39747188 (TF-driven transcription → siRNA → nucleation).
- Heterochromatin boundary formation: PMID:21211723 (Asf1/HIRA), PMID:26438724. Surprising boundary/demarcation role: [PMID:26438724 "Swi6 dimerization in demarcating constitutive heterochromatin from neighboring euchromatin"]; [PMID:26438724 "rather than promoting maintenance and spreading of heterochromatin, Swi6 appears to limit these processes and appropriately confine heterochromatin."]
- Telomere tethering: PMID:25778919 (Aurora B / telomere dispersion); subtelomeric het via Tls1 splicing PMID:25245948.
- Chromatin organization: PMID:9710635 (rhp6 mat silencing), PMID:19111658.

## Caveats / over-annotation watch
- "protein binding" (GO:0005515) IPI rows: uninformative; the informative MF is chromatin-protein adaptor activity / homodimerization / H3K9me reader. MARK_AS_OVER_ANNOTATED for bare protein binding, but note the interactor.
- PMID:37400983 "Cooperative DNA-binding activities of Chp2..." — this paper is about Chp2, not Swi6; the GO:0003677 DNA binding annotation to swi6 may be mis-attributed or a comparative point. Swi6 hinge does bind DNA (PMID:23485968) so DNA binding is plausible MF but the cited reference is about a paralog → UNDECIDED/keep cautiously.
- Heterochromatin "maintenance/spreading" should be tempered: Swi6 is largely dispensable for H3K9me maintenance (PMID:26438724); its core is reading H3K9me + recruiting effectors + confining/demarcating heterochromatin + compaction via oligomerization.

## Core function synthesis
MF: H3K9me2/3 reader (chromodomain); chromatin-protein adaptor/scaffold (chromoshadow); protein homodimerization; (RNA binding via hinge). 
BP: heterochromatin assembly & transcriptional gene silencing at centromere/telomere/mat/rDNA; cohesin enrichment → sister chromatid cohesion & accurate chromosome segregation; mating-type switching (donor selection); heterochromatin boundary/confinement.
CC: pericentric, mating-type region, subtelomeric heterochromatin; nucleus/chromatin.
