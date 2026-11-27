# res2 (P41412, SPAC22F3.09c; synonym pct1) - curation notes

Working notes for the GO annotation review of *Schizosaccharomyces pombe* res2.
Companion file to `res2-ai-review.yaml`. Deep research: `res2-deep-research-falcon.md`
(Edison/falcon synthesis, generated for this review). Sibling reviews written in
parallel: `genes/SCHPO/cdc10`, `genes/SCHPO/res1`; finished comparators
`genes/yeast/MBP1`, `genes/yeast/SWI4`.

## 1. Identity check

- UniProt P41412, "Cell division cycle-related protein res2/pct1", 657 aa. Domain
  architecture from the UniProt record: HTH APSES-type domain 8-115 with the H-T-H
  motif at 39-60, two ankyrin repeats (247-276, 368-397), a disordered basic/low
  complexity region at 113-192.
- Independently cloned twice in 1994: as res2+ (multicopy suppressor of a res1 null;
  Miyamoto, Tanaka and Okayama) and as pct1+ (a p85cdc10 partner; Zhu, Takeda,
  Nasmyth and Jones). [PMID:7926774 "We report the cloning of a new gene, pct1+,
  encoding a 73-kD protein that interacts with p85cdc10 to form an MCB-binding
  heteromer."] [PMID:7926774 "p73pct1 has centrally located ankyrin repeats and a
  putative amino-terminal DNA-binding domain that has extensive sequence similarity
  to the DNA-binding domains of the Saccharomyces cerevisiae SWI4 and MBP1 proteins."]
- Name trap: a second, unrelated *S. pombe* protein is also called Pct1, the
  303-residue RNA 5'-triphosphatase of the mRNA capping machinery. The UniProt
  SUBUNIT line on P41412 ("Interacts with cdc10 and cdk9", PMID:12475973) is the
  capping-enzyme Pct1, not Res2; the deep-research file flags this explicitly and
  the review does not use it. No GOA row on P41412 derives from that literature.

## 2. Biological overview

Res2 is one of the two APSES-domain DNA-binding subunits (with its paralog Res1) of
the fission yeast MBF/DSC1 complex, the G1/S (Start) transcription factor built
around the shared Swi6-like subunit Cdc10. The Res2-Cdc10 heteromer binds MCB
elements but not SCB or E2F sites [PMID:7926774 "The p73pct1/p85cdc10 complex binds
both in vitro and in vivo to MCB but not SCB or E2F sites."], and the DNA-binding
activity of the complex maps to the Res2 N-terminus [PMID:24006488 "Res2, which
contains the DNA-binding activity of the MBF complex in its amino-terminal region"].
Res1 and Res2 together form the DNA-binding unit of the vegetative complex
[PMID:24006488 "Res1 and Res2, which form a heterodimeric DNA-binding domain"], and
Res2 is retained on Cdc10 even when the complex leaves chromatin after DNA damage
[PMID:24006488 "As shown in Figure 2B, the interaction between Cdc10 and Res2 was
well preserved, if not improved, after treating fission yeast cells with MMS."].

Two parallel Start systems. res2+ is largely redundant with res1+ in the mitotic
cycle but is the dominant subunit in meiosis [PMID:8168485 "res2+ is largely
redundant in function with res1+ and is required for the initiation of mitotic and
premeiotic DNA synthesis, but has an additional role in meiotic division."]
[PMID:8168485 "We conclude that the fission yeast contains two functionally
overlapping parallel 'start' systems, Res1-Cdc10 and Res2-Cdc10, the former of
which plays a major role in mitotic cycle whereas the latter in meiotic cycle."].
res2+ is nitrogen-starvation/conjugation induced and depends on Cdc10 for activity
[PMID:8168485 "Unlike res1+, res2+ is highly induced during conjugation and
strongly depends on cdc10+ for its activity."]; the pct1 deletion is viable with a
severe meiotic defect [PMID:7926774 "A deletion of pct1+ is not lethal but does
result in a severe meiotic defect."]. In premeiotic S phase a DSC1-like complex
drives the MCB genes rec8, rec11, cdc18 and cdc22 and requires res2 but not res1
[PMID:14648198 "We found that cdc10+, res2+, rep1+ and rep2+ are required for
correct meiotic transcription, while res1+ is not required for this process."]
[PMID:14648198 "A DSC1-like transcription factor complex that binds to MCB motifs
was also identified in meiotic cells."]. The conjugation-specific cig2 (cyc17)
transcript is res2-dependent [PMID:7909513 "This induction is lost in res2- cells,
whereas the poly(A)+ transcript is significantly reduced in res1- cells."].

Coactivator and complex. Rep2 is the activator subunit recruited by the Res2-Cdc10
DNA-binding unit [PMID:7588609 "Our data suggest that Rep2 is a transcriptional
activator subunit which interacts with the MCB binding subunit complex formed by
Res2 and Cdc10."]. Cdc10 purification recovers Res1 and Res2 as the top hits
[PMID:21132016 "The most enriched proteins in the purification were Cdc10, Res1,
Res2, as expected"].

Activator and repressor. The Baum/Nurse work first showed that Res2 is needed to
shut S-phase transcription off in G2 [PMID:9303312 "define a new role for res2p,
previously demonstrated to be important in the meiotic cycle, in switching off
S-phase transcription during G2 of the mitotic cycle"] [PMID:9303312 "We suggest
that S-phase transcription is controlled by both activation and repression, and
that res2p represses transcription in G2 of the cell cycle as a part of the DSC1
complex."]. The mechanism is docking of negative-feedback regulators on Res2: the
cyclin Cig2 [PMID:11781565 "Cig2p can bind to Res2p, promote the phosphorylation
of Res1p and inhibit MBF-dependent gene transcription."] and the Nrm1/Yox1
corepressor pair [PMID:30635289 "Nrm1 and Yox1 are known to form a dimer that
suppresses the transcriptional activity of the MBF complex outside of G1 by
interacting with Res2"] [PMID:21132016 "in the absence of Res1 or Res2, Yox1 was
not able to bind to Cdc10"]. At the cnp1 (CENP-A) promoter, Res2 occupancy and
the MCB1 box are what confine transcription to G1 [PMID:30635289 "ChIP analysis
showed that Nrm1, Yox1, and Res2 bind to the cnp1 promoter ( Figure 4B )."]
[PMID:30635289 "the nrm1 ∆ res2 ∆ and yox1 ∆ res2 ∆ double mutants display the same
cnp1 mRNA level as the res2 ∆ single mutant ( Figure 4C ), suggesting that Nrm1 and
Yox1 suppress cnp1 levels by interacting with Res2."]. The complex is promoter-bound
throughout the cycle, so the switch is a change of state of DNA-bound MBF rather
than loss of binding [PMID:21132016 "MBF is bound to its target promoters
throughout the cell cycle ( Wuarin et al, 2002 ), suggesting that MBF activity is
not due to modulation of its DNA-binding activity."].

## 3. Decision table

37 GOA rows reviewed. Counts: ACCEPT 22, MODIFY 13, KEEP_AS_NON_CORE 2, REMOVE 1.

| GO term | Evidence / ref | Action | One-line reason |
|---|---|---|---|
| GO:0000082 G1/S transition of mitotic cell cycle | IBA GO_REF:0000033 | ACCEPT | Res2-Cdc10 is one of the two parallel Start systems; node placement sound. |
| GO:0000122 negative regulation of transcription by Pol II | EXP PMID:30635289 | ACCEPT | Res2 on cnp1 promoter; Nrm1/Yox1 repress cnp1 through Res2 (double mutants = res2 alone). |
| GO:0000122 negative regulation of transcription by Pol II | IMP PMID:9303312 | ACCEPT | res2p required to switch off S-phase transcription in G2. |
| GO:0000785 chromatin | IDA PMID:17936710 | ACCEPT | Abstract-only (Ctp1 paper); claim correct for the gene, curator's full-text read not second-guessed. |
| GO:0000785 chromatin | IDA PMID:24006488 | ACCEPT | Res2-HA ChIP on cdc22/cdc18 promoters. |
| GO:0000978 Pol II cis-regulatory region seq-specific DNA binding | HDA PMID:40015273 | ACCEPT | TF ChIP-seq atlas; agrees with targeted MCB-binding evidence. |
| GO:0000978 | IBA GO_REF:0000033 | ACCEPT | APSES node; Res2 in own WITH list is expected (own IDA seeds the IBD). |
| GO:0000978 | IDA PMID:30635289 | ACCEPT | ChIP at cnp1 MCB1 plus box mutagenesis abolishing res2-dependent effect. |
| GO:0000978 | IDA PMID:7926774 | ACCEPT | p73pct1/p85cdc10 binds MCB, not SCB/E2F; contributes_to appropriate. |
| GO:0001227 DNA-binding transcription repressor activity | EXP PMID:9303312 | ACCEPT | Res2 is the DNA-bound subunit through which Cig2 and Nrm1/Yox1 repress. |
| GO:0001228 DNA-binding transcription activator activity | EXP PMID:14648198 | ACCEPT | res2 (not res1) required for meiotic MCB-driven transcription. |
| GO:0001228 | IBA GO_REF:0000033 | ACCEPT | All donors are G1/S activator DNA-binding subunits. |
| GO:0001228 | IEA GO_REF:0000117 | ACCEPT | ARBA reproduces the experimental MF. |
| GO:0001228 | IMP PMID:7909513 | ACCEPT | Conjugation-induced cig2 transcript lost in res2 cells. |
| GO:0003677 DNA binding | IEA GO_REF:0000002 | ACCEPT | Generic but true: APSES domain carries MBF DNA-binding activity. |
| GO:0005515 protein binding (Cig2, PomBase) | IPI PMID:11781565 | MODIFY -> GO:0030332 cyclin binding | Abstract attributes direct cyclin contact to Res2. |
| GO:0005515 protein binding (Cdc10, PomBase) | IPI PMID:11781565 | MODIFY -> GO:0046982 protein heterodimerization activity | Obligate Res2-Cdc10 unit of MBF. |
| GO:0005515 protein binding (Res1, PomBase) | IPI PMID:11781565 | MODIFY -> GO:0046982 | Res1-Res2 heterodimeric DNA-binding domain. |
| GO:0005515 protein binding (Cdc10, IntAct P01129) | IPI PMID:11781565 | MODIFY -> GO:0046982 | IntAct duplicate of the row above. |
| GO:0005515 protein binding (Res1, IntAct P33520) | IPI PMID:11781565 | MODIFY -> GO:0046982 | IntAct duplicate. |
| GO:0005515 protein binding (Cig2, IntAct P36630) | IPI PMID:11781565 | MODIFY -> GO:0030332 | IntAct duplicate. |
| GO:0005515 protein binding (Nrm1) | IPI PMID:18682565 | MODIFY -> GO:0001222 transcription corepressor binding | Nrm1 is the MBF corepressor docking on Res2. |
| GO:0005515 protein binding (Cdc10) | IPI PMID:21132016 | MODIFY -> GO:0046982 | Cdc10 IP-MS recovers Res2; heterodimeric unit. |
| GO:0005515 protein binding (Rep2) | IPI PMID:7588609 | MODIFY -> GO:0001223 transcription coactivator binding | Rep2 is the activator subunit recruited by Res2-Cdc10. |
| GO:0005515 protein binding (Cdc10) | IPI PMID:7588609 | MODIFY -> GO:0046982 | Same heterodimer. |
| GO:0005515 protein binding (Cdc10) | IPI PMID:7926774 | MODIFY -> GO:0046982 | Discovery of the p73pct1/p85cdc10 heteromer. |
| GO:0005634 nucleus | HDA PMID:16823372 | ACCEPT | Site of the core function (promoter chromatin). |
| GO:0005737 cytoplasm | HDA PMID:16823372 | KEEP_AS_NON_CORE | Single ORFeome YFP observation from an over-expressed construct. |
| GO:0005737 cytoplasm | IBA GO_REF:0000033 | REMOVE | Swi6-seeded is_active_in propagation; Res2 has no cytoplasmic activity and stays promoter-bound. |
| GO:0005829 cytosol | HDA PMID:16823372 | KEEP_AS_NON_CORE | Same dataset as the cytoplasm HDA row. |
| GO:0006357 regulation of transcription by Pol II | IDA PMID:8168485 | MODIFY -> GO:0045944 positive regulation of transcription by Pol II | Founding paper establishes a positive Start function; term too general. |
| GO:0030907 MBF transcription complex | EXP PMID:9303312 | ACCEPT | DSC1 bandshift requires res2p. |
| GO:0030907 | IBA GO_REF:0000033 | ACCEPT | Restates Res2's own experimental complex membership. |
| GO:0030907 | IDA PMID:24006488 | ACCEPT | Co-IP with Cdc10-HA; released from chromatin as a complex. |
| GO:0045944 positive regulation of transcription by Pol II | IBA GO_REF:0000033 | ACCEPT | Family-wide G1/S activator function. |
| GO:0045944 | IMP PMID:7909513 | ACCEPT | Loss of cig2 induction in res2 cells. |
| GO:0051445 regulation of meiotic cell cycle | IMP PMID:7926774 | MODIFY -> GO:0051446 positive regulation of meiotic cell cycle | Direction is clearly positive (loss blocks premeiotic S and meiotic progression). |
| GO:0090575 Pol II transcription regulator complex | IEA GO_REF:0000117 | ACCEPT | Correct parent of GO:0030907. |

## 4. Notable curation decisions

1. **Both activator and repressor MFs kept as core.** Unlike Res1, Res2 is the subunit
   on which the negative-feedback regulators dock, and its loss derepresses most of
   the regulon in G2. The 2019 paper states the dual nature outright [PMID:30635289
   "Res2, a DNA-binding protein, together with Res1 and Cdc10, forms the core of the
   MBF complex, and is involved in both activation and repression of the
   transcriptional activity"]. GO:0001227 (repressor) and GO:0001228 (activator) are
   therefore both accepted and each anchors its own core function. Whether GO:0001227
   overstates an *intrinsic* repressor activity (versus a docking function) is left as
   a suggested question.
2. **All eleven `protein binding` IPI rows MODIFIED, never removed.** Each partner has
   a well-defined role: Cdc10 (x5, PomBase and IntAct duplicates) and Res1 (x2) ->
   GO:0046982 protein heterodimerization activity, mirroring the treatment of
   Mbp1-Swi6, Swi4-Swi6 and Res1-Cdc10 in the sibling reviews; Cig2 (x2) -> GO:0030332
   cyclin binding, since the abstract attributes the direct cyclin contact to Res2;
   Nrm1 -> GO:0001222 transcription corepressor binding [PMID:18682565 "Nrm1, a
   corepressor of MBF dependent G 1 -S transcription, is a target of the DNA
   replication checkpoint kinase Cds1"]; Rep2 -> GO:0001223 transcription coactivator
   binding [PMID:7588609 "Here we show that the Rep2 zinc finger protein is an
   essential component of the active Res2-Cdc10 transcriptional regulator complex
   and likely to play a role in the control of cell cycle 'start'."].
3. **The single REMOVE is the Swi6-seeded `is_active_in cytoplasm` IBA.** The PAINT
   node PTN000917496 groups the DNA-binding subunits with the shared regulatory
   subunits, and the sole donor for cytoplasm is budding yeast Swi6 (SGD:S000004172),
   whose regulated nucleocytoplasmic shuttling is a Swi6-specific property. Res2 acts
   on promoter chromatin, stays promoter-bound through the cycle, and no cytoplasmic
   function has been described; the same call was made for Res1, Cdc10, Swi4 and
   Mbp1. The HDA cytoplasm/cytosol rows from the ORFeome screen [PMID:16823372 "Next,
   we determined the localization of 4,431 proteins, corresponding to approximately
   90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent
   protein."] are kept as non-core rather than removed, because they are genuine
   observations, if from over-expressed plasmid constructs.
4. **Two generality MODIFYs.** GO:0006357 (IDA, founding paper) -> GO:0045944, and
   GO:0051445 -> GO:0051446, both because the direction of the effect is unambiguous
   in the cited evidence. No process term for meiosis itself was proposed: Res2 does
   the work as a transcription factor, so a regulation term is the right level.
5. **Deference on abstract-only rows.** Eleven of the fourteen cited papers are
   abstract-only in the cache. The GO:0000785 chromatin IDA from the Ctp1 paper
   [PMID:17936710 "Transcription of ctp1(+) is periodic during the cell cycle, with
   the onset of its expression coinciding with the start of DNA replication."] does
   not mention Res2 in the abstract; it is ACCEPTed with deference to the PomBase
   curator, and the same term is independently supported by full-text ChIP data
   [PMID:24006488 "Loading of Res1 (left) or Res2 (right) on cdc22 and cdc18
   promoters was measured by ChIP analysis of chromatin extracts isolated from
   untreated or MMS-treated"]. Likewise the HDA rows from PMID:16823372 and
   PMID:40015273 [PMID:40015273 "We created a comprehensive library of 89
   endogenously tagged S. pombe TFs, mapping their protein and chromatin interactions
   using immunoprecipitation-mass spectrometry and chromatin immunoprecipitation
   sequencing."] rest on datasets in which Res2 is not named in the abstract.
6. **IBA rows with Res2 in its own WITH list** (GO:0000978, GO:0001228, GO:0030907,
   GO:0045944) are accepted as expected: Res2's own experimental rows seeded the IBD.
   Not marked circular.
7. **No `NEW` terms.** The meiotic role is fully represented by GO:0051446 plus the
   activator MF; a meiosis-specific transcription term was not added (comparator
   check: budding yeast Mbp1/Swi4 do not carry meiotic process terms, and the res1
   review does not either).

## 5. Core functions (as written in the YAML)

1. MCB-binding activator subunit of MBF at the mitotic Start (GO:0001228; contributes
   to GO:0000978; GO:0045944, GO:0000082; chromatin/nucleus; GO:0030907).
2. Docking subunit through which MBF is repressed outside G1 (GO:0001227; GO:0000122;
   chromatin/nucleus; GO:0030907).
3. Res2-Cdc10 as the meiotic Start complex (GO:0001228; GO:0045944, GO:0051446).

GO:0051446 (core function 3) is not itself among the existing_annotations; it is the
proposed replacement for the GO:0051445 IMP row. `just validate SCHPO res2` passes
with no validator warnings.

## 6. Open questions

- Is the G2 repression by Res2 purely a docking function for Nrm1/Yox1 and Cig2, or
  does Res2 make a promoter-specific contribution of its own? Genome-wide, most MBF
  targets are derepressed in res2 cells but yox1, cig2 and mik1 are not (deep-research
  summary of Eshaghi et al. 2011, not cached), which hints at promoter-specific
  behaviour.
- Which meiotic outputs (rec8, rec11, cdc18, cdc22, cig2 poly(A)- transcript, and the
  older mat1/mei3 link) are direct Res2 targets by ChIP in meiotic cells?
- Should the PAINT node be split so that DNA-binding subunit terms (MCB binding,
  chromatin) and regulatory-subunit terms (Swi6 cytoplasmic shuttling) propagate to
  the right clades? This would remove the cytoplasm IBA at source for Res1, Res2,
  Swi4 and Mbp1.
- The cdc10-129 rescue but not cdc10-null rescue by pct1+ overexpression
  [PMID:7926774 "Overexpression of pct1+ is sufficient to rescue the growth of the
  cdc10-129 temperature-sensitive mutant at the restrictive temperature, although it
  is unable to rescue a cdc10 null mutation."] shows the heterodimer, not Res2 alone,
  is the functional unit; whether Res2 has any Cdc10-independent DNA-bound role
  remains untested in vivo.

## 7. Provenance

- Papers with full text cached: PMID:18682565 (abstract + discussion), PMID:21132016,
  PMID:24006488, PMID:30635289. All others abstract-only.
- Deep-research file quoted only for summaries of papers not in the cache (Zhu 1997,
  Eshaghi 2011, Dutta 2008); those claims were cross-checked against the cached primary
  abstracts before use.
- Review completed 2026-09-26/27; notes written after the YAML.
