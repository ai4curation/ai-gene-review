# cyp26b1 review notes

- Curated in DANRE batch 04. Cyp26b1 is best represented as an ER retinoic-acid hydroxylase/catabolic enzyme. I kept the many craniofacial, tendon, skeletal, and hindbrain annotations as non-core developmental outcomes because the direct mechanism is altered RA degradation/signaling [PMID:15661642 "zebrafish cyp26b1 is involved in limiting the activity of retinoic acid"].

## Re-review 2026-09-29

Starting state: valid with 1 warning (6 PENDING rows); every review block carried the same
four boilerplate supporting quotes (the UniProt FUNCTION lines plus a deep-research
paraphrase) regardless of what the term claimed.

Resolved the 6 PENDING rows. Four of them are second GOA rows for terms already reviewed,
distinguished only by their WITH/FROM entities, and were graded identically to their twins:
GO:0021661 rhombomere 4 morphogenesis IGI (mutant+MO vs triple-MO combination), GO:0030278
regulation of ossification IMP and GO:0048701 embryonic cranial skeleton morphogenesis IMP
(dolphin mutant vs morpholino, PMID:18927157), GO:0048387 IDA (two rows, one experiment).
The two genuinely new rows:

- GO:0004497 monooxygenase activity (IBA, PTN000669383): MODIFY to GO:0008401 + GO:0062183,
  with propagation_review. The node spans plant and animal P450s, so it can only assert the
  reaction type; the substrate is known here [UniProt "Catalyzes the hydroxylation of atRA
  primarily at C-4 and"]. Matches the action already given to the InterPro IEA row for the
  same term.
- GO:0016712 (Rhea RHEA:51984, IEA): MODIFY to GO:0008401. Term definition checked via
  QuickGO — it is the generic flavoprotein-donor monooxygenase class; the same Rhea reaction
  is captured substrate-specifically by the 4-hydroxylase term.

Other changes:

- Replaced the boilerplate supporting_text everywhere with term-appropriate evidence: the
  UniProt SUBCELLULAR LOCATION line for the two GO:0005789 rows, the CATALYTIC/FUNCTION lines
  for the MF rows, and paper-specific quotes for each developmental row, e.g. tendon
  [PMID:29227993 "In the absence of cyp26b1, tenoblasts are generated in normal \nnumbers but
  fail to condense into nascent tendons within the ventral arches and, \nsubsequently, muscles
  project into ectopic locales."], ossification [PMID:18927157 "The hyperossification of
  craniofacial bones and vertebrae of mutant animals is anticipated by an increase in
  osteopontin expression in osteoblasts."], hindbrain [PMID:17164423 "the zebrafish orthologs
  of mammalian Cyp26b1 and Cyp26c1 function redundantly with cyp26a1 to pattern the
  hindbrain"], teeth [PMID:25652838 "Heterozygous adult zebrafish \nheterozygous for the
  cyp26b1 mutant ... possess an extra tooth in the ventral row."]. Dropped the
  deep-research paraphrases of UniProt.
- Participation test on the ZFIN developmental IMP/IGI rows: all kept as KEEP_AS_NON_CORE
  (unchanged action, new argument). In each case the work of the process is done by another
  cell type — osteoblasts ossify, chondrocytes shape cartilage, tenoblasts condense,
  neuroepithelium patterns the hindbrain — while cyp26b1 supplies the local RA sink. The
  phenocopy by RA or by the Cyp26 inhibitor R115866 [PMID:18927155] is what shows the
  molecular defect is loss of RA degradation, so the catabolic-process rows (GO:0034653
  IBA/IMP x2) are the ACCEPTed core process.
- GO:0042573 retinoic acid metabolic process (TAS) kept as MODIFY to GO:0034653: cyp26b1 only
  inactivates RA, it does not synthesize it.
- GO:0048387 (negative regulation of RAR signaling, IDA x2): KEEP_AS_NON_CORE with the
  participation argument stated — the receptor performs the regulated step; the enzyme
  destroys the ligand.
- Added reference_review to all 8 PMIDs. Noted that PMID:9007254 (1996 screen) predates the
  cloning of dolphin as cyp26b1, so the gene is not named there; the curator linked the allele.
- Rewrote description (expression domains and mechanism, with citations), both
  core_functions descriptions and their supported_by, added a question about Cyp26 paralog
  redundancy in osteoblasts and an experiment to confirm zebrafish regiospecificity (currently
  ISS/Rhea-transferred, never assayed in zebrafish).

Validation after edits: zero errors, zero warnings.
