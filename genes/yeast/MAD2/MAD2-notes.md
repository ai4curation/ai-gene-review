# MAD2 (YJL030W) — S. cerevisiae — Curation Notes

Journal of research and reasoning for the AI GO-annotation review of budding yeast Mad2
(UniProt P40958). Provenance recorded inline as [PMID:NNNN "quoted text"].

## Identity

- **Gene**: MAD2 (SGD standard name); systematic name **YJL030W**; SGD:S000003567.
- **UniProt**: P40958 (MAD2_YEAST), reviewed. 196 aa, single HORMA domain (8..192).
- **Family**: MAD2 family; PANTHER PTHR11842 (used in the repository module
  `modules/metaphase_anaphase_transition_and_mitotic_exit.yaml`, where Mad2 is the
  closed-Mad2 active unit of the MCC).
- Historical note: the original MAD screen paper reports cloning "MAD2" as a putative
  calcium-binding protein whose disruption is lethal [PMID:1651172 "We cloned MAD2, which
  encodes a putative calcium-binding protein whose disruption is lethal."]. That clone was
  not the checkpoint gene; the real MAD2 (YJL030W, 196 aa, non-essential) was cloned by
  Chen et al. 1999 [PMID:10436016 "We have cloned the MAD2 gene, which encodes a protein
  of 196 amino acids that remains at a constant level during the cell cycle."]. Do not
  cite PMID:1651172 for MAD2 identity.

## Deep research status

`MAD2-deep-research-falcon.md` (Edison Scientific Literature, 44 citations) was present.
It is consistent with the cached primary literature and adds three items not in the GOA
references: Mad1-Mad2 residence at nuclear pore complexes in unperturbed cells (Iouk et
al. 2002, not cached), O-/C-Mad2 interface mutants that retain Mad1 binding but lose Cdc20
binding and checkpoint function (Nezi et al. 2006, not cached), and 2024 work on meiosis I
(Mukherjee et al.) and prolonged DNA-damage arrest (Zhou et al.). These are used only for
the description and suggested questions, never as `supporting_by` evidence.

## Cached publications (status)

| PMID | Full text | Use |
|---|---|---|
| 9461437 | abstract only | Cdc20 is the SAC target; Mad2 co-IPs with Cdc20 (Mad1-dependent) |
| 10436016 | full | MAD2 cloning; tight Mad1-Mad2 complex required for checkpoint |
| 10688190 | abstract only | Uetz genome-wide Y2H (Mad2-Cdc20 pair) |
| 10704439 | full | Mad3 paper; Mad3p-Cdc20p/Mad2p complex; mad2 benomyl sensitivity |
| 10837255 | abstract only | Mad1-Bub1-Bub3 complex formation requires Mad2p |
| 11726501 | full | Bub3-Cdc20-Mad2-Mad3 complexes, kinetochore-independent |
| 15879521 | full | Two Mad2 complexes: small MCC and large Mad2-Cdc20 |
| 16429126 | abstract only | Gavin TAP/MS survey (Mad2-Mad1 pair) |
| 16651657 | full | Topo II checkpoint requires Mad2 |
| 22940250 | full | Reconstituted SAC: Mad2 + Mad3-Bub3 inhibit APC/C, promote Cdc20 autoubiquitination |
| 24402315 | full | Mad1 kinetochore recruitment via Mps1-phosphorylated Bub1 requires Mad2 |
| 27170178 | full | Two Mad1-Mad2 heterotetramers per Bub3-Bub1 at kinetochores |
| 37968396 | full | 2023 interactome; main text has no Mad2 mention (supplementary pair) |
| 41398407 | full | BIR requires SAC to prolong G2/M arrest |
| 42353152 | full | Tyc1 polymers on microtubules in vitro, with Mad2p as ligand |

## KNOWN (evidence-supported)

1. **Mad1-Mad2 complex.** Tight, cell-cycle-independent, required for checkpoint function
   [PMID:10436016 "Gel filtration and co-immunoprecipitation analyses reveal that Mad2p
   tightly associates with another spindle checkpoint component, Mad1p."; "association of
   Mad2p with Mad1p is critical for checkpoint function and for hyperphosphorylation of
   Mad1p."]. Mad2p is also needed for Mad1 to form its complex with Bub1-Bub3
   [PMID:10837255 "We find that formation of this complex requires Mad2p and Mps1p but not
   Mad3p or Bub2p."].
2. **Kinetochore recruitment.** Mps1 phosphorylates Bub1, which recruits Mad1; the
   reconstitution needs Mad2 [PMID:24402315 "The Mad1 interaction with Bub1 and
   kinetochores can be reconstituted in the presence of Mps1 and Mad2."; "In contrast to
   Bub1 and Bub3, Mad2 was required for the association of Mad1 with the
   Bub1(M)-Spc105-6A fusion kinetochores"]. Quantitatively, [PMID:27170178 "the
   kinetochore recruits two Mad1-Mad2 heterotetramers for every Bub3-Bub1 molecule."].
3. **Cdc20 is the target.** [PMID:9461437 "Mad2 and Mad3 coprecipitated with Cdc20 at all
   stages of the cell cycle. The binding of Mad2 depended on Mad1 and that of Mad3 on Mad1
   and Mad2."; "Mutants in Cdc20 that were resistant to the spindle checkpoint no longer
   bound Mad proteins, suggesting that Cdc20 is the target of the spindle checkpoint."].
4. **MCC and Mad2-Cdc20 subcomplex.** [PMID:11726501 "co-fractionation experiments
   suggest that Mad2, Mad3 and Bub3 may be concomitantly present in protein complexes with
   Cdc20."]; [PMID:10704439 "From this we conclude that Mad2p function is essential for a
   stable Mad3p–Cdc20p interaction, probably because it is itself part of the complex"];
   [PMID:15879521 "There is a small amount of Mad2-Mad3-Bub3-Cdc20 and a much larger
   amount of a complex that contains Mad2-Cdc20."; "The kinetochore is not required to
   form either complex."].
5. **Molecular activity: APC/C-Cdc20 ubiquitin ligase inhibition.** [PMID:22940250 "We
   found that Mad2 alone inhibited Cdc20 binding and autoubiquitination."; "Studies with
   purified proteins revealed that Mad2 and Mad3-Bub3 synergize to effectively inhibit
   securin ubiquitination, while at the same time promoting Cdc20 autoubiquitination."].
   Note the sign change: Mad2 alone inhibits Cdc20 autoubiquitination; only with
   Mad3-Bub3 does the complex promote it.
6. **Checkpoint phenotype.** [PMID:10436016 "When spindle assembly is disrupted, the
   budding yeast mad and bub mutants fail to arrest and rapidly lose viability."];
   [PMID:15879521 "We use conditional mutants to show that both Mad2 and Mad3 are
   essential for establishment and maintenance of the spindle checkpoint."].
7. **Topo II checkpoint.** [PMID:16651657 "The G2/M delay seen in top2-B44 was completely
   bypassed, however, by the deletion of MAD2, indicating that Mad2 is a component of the
   checkpoint system that induced a G2/M delay as a consequence of limited Topo II
   function."; "checkpoint activation is not the result of failed chromosome
   biorientation or a lack of spindle tension."].
8. **BIR.** [PMID:41398407 "We discovered that DDC-induced cell cycle arrest alone is
   insufficient for BIR success; rather, successful BIR completion requires the SAC to
   prolong G2/M arrest."; "Therefore, an alternative mechanism may activate the SAC
   during BIR."].
9. **Tyc1 in vitro study.** [PMID:42353152 "Tyc1p polymers that were formed in the
   presence of Mad2p in association with a Mad2-binding motif peptide were able to suppress
   Taxol-stabilized microtubule depolymerization that was induced by exposure to ice-cold
   CaCl2."; "When only [Mad2p-6xhis + DQ36] was added to the samples, no microtubules were
   observed after ice-cold CaCl2 treatment."].

## Decisions and reasoning

- **GO:0003674 ND -> MODIFY to GO:1990948 ubiquitin ligase inhibitor activity.** Direct
  budding-yeast reconstitution (PMID:22940250) supports an informative MF; the ND
  placeholder is no longer accurate. Consistent with the human MAD2L1 review, which uses
  GO:1990948 as a core function.
- **Twelve bare GO:0005515 IPI rows -> REMOVE**, per repository policy: generic
  protein binding should be removed unless a cited paper supports a better molecular-function
  term. Here the interaction evidence supports complex membership, not a more specific MF.
  The Mad1 interactions point to the MAD1-MAD2 complex; Cdc20 to the CDC20-MAD2 subcomplex;
  and Mad3/Bub3 to the MCC. The two HTP rows (Uetz Y2H, Gavin TAP/MS) and the 2023
  interactome row (no Mad2 in the cached main text) are supported by the targeted papers via
  `additional_reference_ids`; the interactions themselves are not disputed.
- **GO:1990728 MAD1-MAD2 complex -> NEW.** The core Mad1-Mad2 complex was previously used
  only as a proposed replacement for Mad1-targeted `GO:0005515` rows and in `core_functions`.
  Added a dedicated proposed complex annotation from PMID:10436016 so the specific CC assertion
  is explicit and the bare protein-binding rows can be removed cleanly.
- **GO:0000727 BIR IMP -> MARK_AS_OVER_ANNOTATED.** The paper shows necessity (SAC
  prolongs arrest so BIR can finish), not participation of Mad2 in repair; the CLAUDE.md
  substrate/necessity test applies. The checkpoint contribution is already captured by
  GO:0007094 and the GO:0044774 IGI row. Not REMOVE: the mutant phenotype is genuine.
- **GO:0007026 / GO:0015630 IPI (Tyc1) -> MARK_AS_OVER_ANNOTATED.** In vitro EM with
  purified proteins; the activity is attributed by the authors to Tyc1p polymers, and
  Mad2p + peptide alone is inactive. No in vivo evidence for a Mad2 microtubule role.
  Not REMOVE, because Mad2 was assayed and the observation is real.
- **GO:0044774 IGI (Topo II checkpoint) -> KEEP_AS_NON_CORE.** Mad2 does the signaling
  work in a genuine, mechanistically distinct checkpoint; secondary to the SAC.
- **GO:1902499 IDA -> KEEP_AS_NON_CORE.** Real MCC property (with Mad3-Bub3) tied to
  checkpoint silencing; Mad2 alone has the opposite effect.
- **All GO:0007094, GO:0033597, GO:1990333, GO:0000776 rows -> ACCEPT.** IBA rows: node
  PTN000217420 is seeded by experimental annotations across eukaryotes including SGD's
  own MAD2 rows; the target's presence in its own WITH/FROM is expected.
- **GO:0005634 nucleus IEA -> ACCEPT.** Closed mitosis; kinetochores, NPCs and APC/C are
  nuclear.
- **No NEW terms.** Candidate terms considered and rejected: meiotic spindle assembly
  checkpoint signaling (GO:0033316) and nuclear pore (GO:0005643) are supported only by
  papers not in the cache (Mukherjee 2024, Iouk 2002); recorded as suggested questions
  instead. Comparator check for BIR: other SAC components (Bub1, Bub3) carry the same
  screen-derived BIR annotation from SGD, so the over-annotation judgement applies to the
  class, not just Mad2.

## Validation

`just validate yeast MAD2`: valid, 1 warning (core-function MF GO:0042803 protein
homodimerization activity not among existing annotations; retained for consistency with
the human MAD2L1 review's Mad1-templated O/C-Mad2 dimerization core function).

## 2026-09-28 IBA and protein-binding follow-up

Re-reviewed the two GOA IBA rows against current PTHR11842 PAINT. The accepted placement
remains correct: PTN000217420 carries both `GO:0000776 kinetochore` and `GO:0007094
mitotic spindle assembly checkpoint signaling` for the MAD2A subfamily, and the current
PAINT cache keeps MAD2 on the MAD2A branch, separate from the MAD2B/REV7 branch that
carries nucleus, translesion synthesis, and DNA repair functions. MAD2's own SGD
experimental annotations in the WITH/FROM set are legitimate PAINT descendant evidence,
not circular support.

Searched for post-2024 primary budding-yeast MAD2 literature. The search mainly found
checkpoint reviews/modeling papers and the cached 2024 primary yeast work already noted
in the Falcon report, so no newer PMID was added.

Aligned all twelve generic IntAct `GO:0005515 protein binding` rows with current policy:
they are now `REMOVE`, not `MODIFY`, because the evidence supports specific
cellular-component complex membership rather than a replacement molecular-function term.
Added a single explicit `NEW` annotation for `GO:1990728 mitotic spindle assembly checkpoint
MAD1-MAD2 complex` from Chen et al. 1999 so the Mad1-Mad2 complex used in `core_functions`
is represented directly instead of only as an invalid replacement for protein binding.
