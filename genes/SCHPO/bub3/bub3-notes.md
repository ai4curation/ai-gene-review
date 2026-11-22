# bub3 (S. pombe, O42860 / SPAC23H3.08c) - curation notes

## Session 1 - full review of the GOA seed

### Sources used

- `bub3-uniprot.txt`: 320 aa, four annotated WD repeats, "WD repeat BUB3 family"; function
  line (from PMID:15509783 and PMID:22660415) covers SAC signaling, repair of incorrect
  kinetochore-microtubule attachments, localizing Bub1 to kinetochores and suppressing Bub1
  activation away from the kinetochore; subunit line records the Bub1-Bub3 complex, the Mad3
  interaction and binding to MELT-phosphorylated Spc7; PTM "Phosphorylated by bub1"; disruption
  phenotype "Sensitive to thiabendazole (TBZ)".
- `bub3-goa.tsv`: 20 rows (PomBase, UniProt, ComplexPortal, GO_Central); no `protein binding`
  rows, no NOT rows, no isoform rows.
- `bub3-deep-research-falcon.md` (Edison): agrees with UniProt and the primary papers; its main
  value is the explicit species-specific caveat that fission yeast Bub3 is not absolutely
  required for arrest, and the summary of the checkpoint-silencing and bi-orientation phenotypes.
  Two of its sources (Vanoosthuyse et al. 2009 on silencing; Mora-Santos et al. 2016 on the
  licensing switch) are not in the publications cache and were used only as background.
- Cached publications: full text for PMID:19680287, PMID:22521786, PMID:28017606,
  PMID:26882497, PMID:17227844, PMID:21070969; abstract-only for PMID:11909965 (abstract plus
  discussion), PMID:15509783, PMID:22660415, PMID:22825872.
- Comparators: `genes/yeast/BUB3` (complete), `genes/human/BUB3` (complete), the S. pombe
  `mad3` review (written in parallel), the module
  `modules/metaphase_anaphase_transition_and_mitotic_exit.yaml` (cites S. pombe bub3 as the MCC
  Bub3 exemplar), and the PomBase GO-CAM `gocams/67369e7600002505` (bub3 placed in
  GO:0007094 at the kinetochore, typed as protein binding).

### Biology, with provenance

- Identity and family: a non-enzymatic WD40 beta-propeller; the conserved Bub3 propeller binds
  Bub1 and Mad3 GLEBS peptides on the same top face
  [PMID:17227844 "Crystal structures of these peptides with Bub3 show that the interactions for Mad3 and Bub1 are similar and mutually exclusive."].
  The fission yeast bub1-dGLEBS allele confirms the architecture functionally
  [PMID:19680287 "Bub1-ΔGLEBS did not localize to kinetochores, abolished Bub3 localization to kinetochores (supplementary Fig S6 online), but preserved SAC activity"].
- Localization: Bub3p is a kinetochore/central-centromere protein in early mitosis
  [PMID:15509783 "We demonstrate by chromatin immunoprecipitation that they all interact with the central domain of centromeres, consistent with their role in monitoring kinetochore-microtubule interactions."],
  and Bub1p and Bub3p need each other, but not the Mad proteins, to get there
  [PMID:15509783 "Bub1p and Bub3p are dependent upon one another, but independent of the Mad proteins, for their kinetochore localization."].
- Recruitment mechanism: Mph1 phosphorylates Spc7 MELT motifs, which recruit the Bub1-Bub3
  complex
  [PMID:22521786 "These data suggest that Mph1 phosphorylation of the MELT motifs in Spc7 recruits the Bub1-Bub3 complex to kinetochores."];
  phospho-mimetic Spc7 bypasses Mph1 but not Bub3
  [PMID:22521786 "The phospho-mimetic spc7-9TE mutant therefore bypasses the requirement for Mph1 kinase activity to load Bub1 to kinetochores, but Bub1 loading still requires the presence of Bub3 (Figure 3A)."];
  the in vitro binding requires Bub3 but not Mad3
  [PMID:22521786 "Consistent with this, interaction of bacterially expressed Spc7-9TE with Bub1 in cell extracts requires Bub3, but not Mad3 (Supplemental Figure 2A)."].
  Yamagishi et al. independently showed the same with a 12-site allele
  [PMID:22660415 "Accordingly, a non-phosphorylatable spc7-12A mutation abolishes kinetochore targeting of Bub1-Bub3, whereas a phospho-mimetic spc7-12E mutation forces them to localize at kinetochores throughout the entire cell cycle, even in the absence of Mph1."].
  Bub3 is the direct phospho-MELT reader
  [PMID:26882497 "structural studies have shown that it is Bub3 that binds directly to the MELT motifs after they are phosphorylated by Mps1Mph1 [43,44]"].
- Downstream of Bub3 at the kinetochore: Mad3 recruitment needs Bub1, Bub3 and Mph1
  [PMID:11909965 "We find Mad3-GFP kinetochore localization to be dependent upon Bub1p, Bub3p, and the Mph1p kinase, but not upon Mad1p or Mad2p."],
  and Mad3p co-immunoprecipitates Bub3p with Mad2p and Slp1
  [PMID:11909965 "Mad3p coimmunoprecipitates Bub3p, Mad2p, and the spindle checkpoint effector Slp1/Cdc20p."].
- Bub3 is NOT essential for the fission yeast SAC (the key species-specific point). Live-cell
  Plo1-GFP assays in nda3-KM311 show a Mad2-dependent delay without Bub3
  [PMID:19680287 "However, the additional deletion of mad2 in nda3-KM311 bub3Δ cells considerably shortened mitosis (Fig 1A), indicating that the SAC had been active in nda3-KM311 bub3Δ cells and that Bub3 was not essential for progression into anaphase."]
  [PMID:19680287 "Together, this indicates that fission yeast Bub3 is not essential for SAC activity, which is consistent with studies by two other groups (Tange & Niwa, 2008; V. Vanoosthuyse & K. Hardwick, personal communication)."].
  This happens even though almost nothing is enriched at kinetochores in bub3
  [PMID:22825872 "In bub3Δ cells, the SAC is functional when only Mph1 and the Aurora kinase Ark1, but no other SAC proteins, are enriched at kinetochores."]
  [PMID:26882497 "The bub3∆ phenotype, where Bub1p, Mad3p, Mad1p and Mad2p all fail to be recruited to kinetochores yet the checkpoint arrest remains robust, also argues against an absolute requirement for checkpoint proteins to be recruited to KNL1Spc7 and kinetochores in fission yeast [50,51,52]."].
  Bub3p is also dispensable for the Mad2-overexpression arrest
  [PMID:11909965 "Mad1p, Bub1p, and Bub3p are not required for this arrest."].
  Nonetheless the authors keep Bub3 inside the SAC
  [PMID:19680287 "It also indicates that fission yeast Bub3 remains intimately linked to the SAC and we hypothesize that, even in fission yeast, Bub3 contributes to SAC signalling but not in an essential manner."]
  and docking of Bub1-Bub3 on Spc7 matters for SAC maintenance
  [PMID:22521786 "Although Bub3 is not critical for SAC arrest in S.pombe [30, 41, 48], disruption of the binding sites for the Bub1-Bub3 complex on Spc7 causes a defect in maintenance of the SAC signal."].
- Bub3 restrains ectopic/premature signaling (the inhibitory arm). Undocked Bub1-Bub3 is
  dominant-negative for maintenance
  [PMID:22521786 "but suggests that when the Bub1-Bub3 complex is not bound to Spc7 it acts as a dominant negative factor that prevents maintenance of the SAC signal."]
  and deleting bub3 rescues spc7-9TA
  [PMID:22521786 "Surprisingly, when spc7-9TA was combined with Δbub3 the SAC response was much improved, although this did not suppress the chromosome mis-segregation defects of spc7-9TA (Figure 4D; data not shown)."].
  The synthetic checkpoint (SynCheck) made this explicit
  [PMID:28017606 "Analysis of bub3Δ mutants demonstrates that Bub3 acts to suppress premature checkpoint signaling."]
  [PMID:28017606 "Deletion of bub3 even allowed TetR-Spc7-9TA, TetR-Δ(1-302)Mph1 to arrest cells, again demonstrating the inhibitory effect of Bub3 (Figure 4D)."]
  [PMID:28017606 "Figure 4E shows a corresponding increase in the level of the Mad1-Bub1 complex in bub3Δ cells."],
  with a proposed mechanism through Bub1 autophosphorylation
  [PMID:28017606 "Bub3 binding might inhibit Bub1 auto-phosphorylation and thereby negatively impact Mad1p binding (see model in Figure 4F)."].
  The nucleoplasm is the relevant compartment for this arm
  [PMID:28017606 "Our interpretation is that soluble, heterodimeric complexes formed between TetR-Spc7 and TetR-Mph1 in the nucleoplasm are sufficient for checkpoint activation."]
  [PMID:28017606 "In normal cells, Bub3 would prevent early nucleoplasmic signaling, and this effect would later be overcome when Mad-Bub complexes assemble at kinetochores and Spc7-Bub3-Bub1 interactions induce conformational changes in the Bub proteins, thereby activating Bub1 for downstream signaling."].
- Checkpoint silencing (the positive arm on the way out of mitosis): Spc7-docked Bub1-Bub3
  accelerates silencing, and the effect is Bub3-dependent
  [PMID:22521786 "These results suggest that enhanced recruitment of Bub1 and Bub3 to the kinetochore in spc7-9TE cells promotes silencing of the SAC to such an extent that it becomes more efficient than in wild type cells."]
  [PMID:22521786 "Importantly, the rapid appearance of Nsk1 on spindle poles in spc7-9TE cells is completely abolished in the absence of Bub3 (Figure 4E)."].
- Chromosome attachment: Bub3 with Bub1 promotes mono- to bi-orientation conversion,
  independently of Sgo2
  [PMID:19680287 "Instead, Bub3, together with Bub1, has a specific function in promoting the conversion from chromosome mono-orientation to bi-orientation."]
  [PMID:19680287 "By contrast, bub3Δ cells more frequently showed mono-oriented chromosomes (20% of all chromosomes; Fig 3C) and, crucially, mono-oriented chromosomes in bub3Δ cells only became bi-oriented after a considerable delay, if at all (Fig 3B,D; supplementary Fig S4B–D online)."]
  [PMID:19680287 "However, unlike in cells lacking Bub1, Sgo2 still localized to the centromeres in the bub3Δ or bub1-ΔGLEBS mutants (Fig 3E; supplementary information online, note 5)."].
  The Bub3-dependent step is movement of a pole-proximal chromosome toward the other pole
  [PMID:19680287 "Bi-orientation, therefore, needs a mechanism to move chromosomes closer to the opposing SPB, which depends on Bub3 and Bub1 (Fig 4A; supplementary information online, note 7)."],
  and Bub3 matters most when kinetochores have been unclustered from the poles
  [PMID:19680287 "This led to a strong increase in chromosome mis-segregation in cells lacking Bub3 (Fig 2B), which indicates that Bub3 is more important for correct kinetochore–microtubule attachment in a situation in which kinetochores become unclustered from the SPBs."].
  The authors favour a direct effect at the mono-oriented kinetochore over a checkpoint-delay
  explanation
  [PMID:19680287 "As Bub3 localizes to mono-oriented chromosomes up to the moment of bi-orientation (Fig 4B), and the abolishment of Bub3 and Bub1 localization to the kinetochores in the bub1-ΔGLEBS mutant leads to persistent mono-orientation (Fig 3B–D), we favour the idea that Bub3 and Bub1 promote bi-orientation by modulating kinetochore–microtubule interactions at the mono-oriented chromosome (indirect pathway)."].
- Ubiquitin binding: the only source is the budding yeast WD40 survey
  [PMID:21070969 "We define a large subset of WD40 β-propellers as a class of ubiquitin-binding domains."];
  the cached running text never names Bub3, and nothing of the kind has been tested in
  S. pombe.

### Decision table

| Row(s) | Action | One-line reason |
|---|---|---|
| GO:0000775 chromosome, centromeric region (IEA, SubCell mapping) | ACCEPT | Restates the central-core ChIP result of PMID:15509783; broad parent of the kinetochore rows, not over-annotated. |
| GO:0000776 kinetochore (IBA PTN000103865) | ACCEPT | Family-wide property, node placement sound; target in its own WITH/FROM is expected (PomBase IDA seeds). |
| GO:0000776 kinetochore (IDA PMID:11909965) | ACCEPT | Abstract-only cache; Bub3 localization figure is in the full text; defer to PomBase, localization is beyond doubt. |
| GO:0000776 kinetochore (IDA PMID:15509783) | ACCEPT | Primary localization study (GFP foci + ChIP). |
| GO:0000776 kinetochore (ISS from mouse Q9WVA3) | ACCEPT | Correct, redundant with the direct rows. |
| GO:0005634 nucleus (EXP x3; IEA) | ACCEPT | Closed mitosis: kinetochore-bound and soluble pools are both intranuclear; broad but correct. |
| GO:0005654 nucleoplasm (IBA) | ACCEPT | Unusually well supported in the target: the restraint of ectopic Bub1-Mad1 signaling is a nucleoplasmic activity (PMID:28017606). |
| GO:0007094 mitotic SAC signaling (IBA) | ACCEPT | Core process; non-essential in S. pombe but still a participant (PMID:19680287, PMID:22521786); matches the PomBase GO-CAM. |
| GO:0007094 mitotic SAC signaling (NAS PMID:22660415, ComplexPortal) | ACCEPT | Weak code, but the assertion is the verified core function of the Bub1-Bub3 complex. |
| GO:0043130 ubiquitin binding (IBA PTN000103837) | KEEP_AS_NON_CORE | In vitro propeller property from a S. cerevisiae survey; top face is GLEBS-occupied in vivo; no checkpoint role known; same call as yeast and human BUB3. |
| GO:0090266 regulation of mitotic SAC (EXP PMID:22660415, PomBase) | ACCEPT | The generic regulation term is the honest summary of a protein that sits on both the positive (docking/silencing) and negative (undocked restraint) sides. |
| GO:0140499 negative regulation of mitotic SAC signaling (IMP PMID:28017606) | ACCEPT | Direct loss-of-function evidence in the target: bub3 deletion advances and derepresses SynCheck arrest and raises Mad1-Bub1 complex levels. |
| GO:1990298 bub1-bub3 complex (IBA; IMP PMID:22521786; IPI PMID:22660415) | ACCEPT | Constitutive complex, recruited as a unit by phospho-Spc7; structurally defined in the family. |
| GO:1990758 mitotic sister chromatid biorientation (IMP PMID:19680287) | ACCEPT | Well-controlled live-cell evidence; Bub3 stays on mono-oriented kinetochores until bi-orientation and the SAC is still active in bub3, so this is participation, not a checkpoint-delay side effect. |
| GO:1990942 mitotic metaphase chromosome recapture (IMP PMID:19680287) | ACCEPT | The MBC-washout assay is a recapture experiment and the Bub3-dependent step (pole-proximal chromosome moving to the spindle centre) is the second half of the term definition; complementary view of the same phenotype as the biorientation row. |

Totals: 20 rows; 19 ACCEPT, 1 KEEP_AS_NON_CORE; no REMOVE, MODIFY, MARK_AS_OVER_ANNOTATED,
UNDECIDED or NEW.

### Notable curation decisions

1. **Both GO:0007094 (SAC signaling) and GO:0140499 (negative regulation of SAC signaling)
   are accepted, and GO:0090266 (regulation of SAC) alongside them.** This is not a
   contradiction: Bub3 promotes kinetochore-based signaling by delivering Bub1 to phospho-Spc7
   and restrains ectopic signaling when the complex is undocked. The PomBase curators chose the
   generic regulation term for PMID:22660415 (which reports both arms) and the specific
   negative-regulation term for PMID:28017606 (which isolates the inhibitory arm). Both
   choices were respected rather than "harmonised".
2. **The GO:0007094 IBA was accepted despite bub3 deletion not abolishing the checkpoint.**
   The fission yeast peculiarity is that Bub3 is non-essential for arrest, not that it is
   uninvolved; the authors who showed the non-essentiality still describe Bub3 as intimately
   linked to the SAC, and the Spc7 docking-site mutants show a maintenance defect. Arguing
   against the node placement would require target-specific evidence of functional loss, which
   does not exist.
3. **GO:0043130 ubiquitin binding (IBA) kept as non-core rather than removed.** The
   descendant evidence (SGD IDA from PMID:21070969) is a survey in which the cached running
   text never names Bub3; the inference is phylogenetically reasonable for the propeller
   family, but no physiological ubiquitin binding by Bub3 is known and the binding surface is
   GLEBS-occupied in vivo. Consistent with the yeast and human BUB3 reviews. Not REMOVE,
   because the SGD curator read the full figure set and the rule is to defer.
4. **GO:1990758 and GO:1990942 were both accepted as direct participation.** The temptation
   was to read the bi-orientation defect as a checkpoint side-effect (less time to correct);
   Windecker et al. rule this out because the SAC is active in bub3 cells and Bub3 stays on the
   mono-oriented kinetochore, and they argue for modulation of kinetochore-microtubule
   interactions. The two rows are two views of one phenotype rather than two functions, which
   the reasons say explicitly.
5. **No NEW terms.** GO:0033597 (mitotic checkpoint complex) was considered because Mad3p
   co-immunoprecipitates Bub3p with Mad2p and Slp1, and both the yeast and human BUB3 reviews
   carry it. PomBase has not annotated bub3 to it, Bub3 is dispensable for the
   Mad2-overexpression arrest and (per the deep research) for Mad2/Mad3 association with
   APC/C, and the S. pombe MCC structure work does not include it, so this was raised as a
   suggested question instead of asserted. GO:0034501 (protein localization to kinetochore)
   was likewise not proposed; the Bub1-docking role is expressed through GO:0140483
   kinetochore adaptor activity in `core_functions`.
6. **Molecular function.** GOA carries no MF for S. pombe bub3 apart from ubiquitin binding
   and the GO-CAM types it as protein binding. `core_functions` uses GO:0140483 kinetochore
   adaptor activity (phospho-MELT reader that docks Bub1; same MF as the yeast and human
   reviews) and GO:0030674 protein-macromolecule adaptor activity for the nucleoplasmic
   restraint of Bub1. These are validator warnings ("not reflected in existing_annotations")
   and are left as such deliberately.

### Core functions written

1. Kinetochore adaptor activity (GO:0140483) in the Bub1-Bub3 complex at the kinetochore,
   directly involved in GO:0007094 and GO:0090266.
2. Protein-macromolecule adaptor activity (GO:0030674) in the Bub1-Bub3 complex in the
   nucleoplasm, directly involved in GO:0140499.
3. Kinetochore adaptor activity (GO:0140483) in the Bub1-Bub3 complex at the kinetochore,
   directly involved in GO:1990758 and GO:1990942.

### Open questions

- Is S. pombe Bub3 a bona fide MCC subunit (GO:0033597)? It co-IPs with Mad3-Mad2-Slp1 but
  is dispensable for Mad2-dependent arrest and for Mad2/Mad3-APC/C association. A direct
  stoichiometry/reconstitution experiment would settle whether the budding yeast/human
  convention applies.
- Mechanism of the restraint: does Bub3 sterically limit Bub1 autophosphorylation of the
  Mad1-binding motif, or block Mph1 access, and is the restraint relieved by a conformational
  change on phospho-Spc7 binding (Yuan et al. model)?
- How does kinetochore-bound Bub1-Bub3 move a pole-proximal mono-oriented chromosome toward
  the opposing pole: Bub1 kinase output, a recruited motor/microtubule regulator, or
  Ark1/Sgo2-independent modulation of Ndc80-Dam1 attachment dynamics?
- The UniProt PTM line "Phosphorylated by bub1" (PMID:15509783) has no functional follow-up;
  whether Bub3 phosphorylation affects MELT binding or the Bub1/Mad3 partner choice is
  unknown.

### Validation

`just validate SCHPO bub3`: valid; remaining warnings are the three core-function MF terms not
present in existing_annotations (deliberate) and the generic note that no annotation cites the
deep-research file (all claims were checked against the primary cached papers instead).
