

## Full-gene re-review, 2026-09-20

All14 rows reviewed. Four broad catalytic/nucleotide annotations and membrane/cytosol restored to ACCEPT; cytoplasmic support now explicitly comes from PAINT rather than solubility. The four autophagy rows remain UNDECIDED while root independently checks PTN000681272 and target placement. Neither the LOK-related family name, domain count, huge ciliate kinome nor absence of a target assay is sufficient counterevidence. Falcon was read completely and its target-substrate/location limits incorporated; generic ciliate pathway discussion was removed from the biological description. Source rows are unchanged.


### Actual PAINT topology resolved during the same review

Root obtained the nested tree with POST to the PANTHER treeinfo endpoint. The exact lineage was independently read: PTN002805221 → PTN000681272 → PTN007795585 → PTN008401646 → PTN001218730 → PTN007795752 → PTN002805316 (A0BFB4/GSPATT00028266001). This supersedes the earlier inability to inspect the tree. All four autophagy rows are now ACCEPT as inherited functions. The evidence snapshot and explanation are in A0BFB4-placement-evidence.md/json and root’s projects/TREEGRAFTER/rereview-2026-09-20/a0bfb4-paint-classification-check.json. The remaining focused question reconciles live sequence classification with actual PAINT family assignment; it does not assume that the target lies outside the autophagy clade.


## Recovery PR specificity follow-up (2026-09-22)

Make the molecular work or process role explicit separately for each challenged term; retain evidence-based core versus peripheral judgments rather than treating ontology breadth as non-coreness.


## Final evidence and annotation-action reconciliation (2026-09-23)

Removed limitation/tool-access statements from positive support where applicable and retained the actual lineage or sequence evidence. Historical uncertainties remain in the rationale rather than being treated as proof of function.


## OpenScientist autophagy-architecture follow-up (2026-10-10)

Read the focused report on the PTHR24348 versus PTHR44167 placement issue. The report supports the same conclusion as the earlier topology snapshot that A0BFB4 is genuinely Atg1/ULK-related rather than misplaced into PTHR24348 by a donor-count artifact. Its new target-relevant argument is narrower: A0BFB4 retains the compact kinase domain but lacks the canonical C-terminal Atg1 interaction module, and ciliates lack the Atg13/Atg17/Atg101 initiation complex. Retained the kinase MF rows and broad PAINT localizations, marked the four autophagy BP/CC rows as over-annotated, and removed autophagosome assembly / phagophore assembly site from the core function pending Paramecium-specific localization or knockdown evidence.


## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence used: UniProt record, GOA rows, PTHR24348 PAINT
table, PTHR44167 family review, PMID:28123910 (full text), PMID:24280724, the falcon report,
the earlier placement-evidence file and OpenScientist report, and a new kinase-domain analysis.

Identity: A0BFB4 is the only UniProt product of GSPATT00028266001 (381 aa, TrEMBL, PE 3). It is
not a fragment or isoform as far as the record shows: kinase domain 96-348, with an N-terminal
~95-residue segment and a 33-residue C-terminal tail. A full-length Atg1/ULK protein is ~900-1050
aa with a central S/P-rich region and a C-terminal EAT/MIT domain. A0BFB4 lacks both. Per
PMID:28123910 this is true of every ciliate Atg1-like kinase, so it reflects the gene structure of
this lineage, not a truncated gene model.

New analysis (A0BFB4-bioinformatics/, RESULTS.md):
- Catalytic motifs intact: GEGTFG(103), ACK(123; K125), HRDIKPDN(213), DFG(236), APE(260).
- Kinase-domain MAFFT + BLOSUM62 NJ against 17 characterised kinases. Identity to everything is
  24.8-32.0%, with no discriminating best hit (unc-51 32.0, ULK2 30.7, CAMK2A 30.1, SLK 29.8; yeast
  ATG1 24.8). A0BFB4 sits on a long branch near the ULK+STE20 clade. It formed an exclusive clade
  with ATG1/ULK in only 1/200 bootstraps.
- This disagrees with the OpenScientist claim of ~35% to ULK1/2 as clean evidence of Atg1 ancestry.
  The OpenScientist report also wrongly calls PTHR44167 a function-less catch-all. Per
  interpro/panther/PTHR44167 it is the CHK2/Rad53 and CDC7/DDK family.

Placement: the PANTHER reference tree grafts A0BFB4 (leaf PTN002805316) into PTHR24348:SF22,
which is the fungal ATG1 subfamily by current HMM membership, below the Atg1/ULK node
PTN000681272. The current HMM instead assigns PTHR44167:SF18. The IBA rows come from the tree.
With weak sequence support for the graft and the target-specific loss of the Atg1 C-terminal
module and partners, I do not transfer Atg1-node-specific BP/CC terms.

Action changes vs previous version:
- membrane (IBA, PTN000681272): ACCEPT -> MARK_AS_OVER_ANNOTATED (Atg1-node localization that
  depends on the missing complex-recruitment module).
- regulation of autophagy: UNDECIDED -> MARK_AS_OVER_ANNOTATED (same source node and argument as
  the sister rows; "open question" is not evidence).
- autophagosome assembly, phagophore assembly site, autophagosome: MARK_AS_OVER_ANNOTATED kept,
  with reasons rewritten to cite PMID:28123910 full text and the new analysis.
- cytosol (from PTN000681272): ACCEPT -> KEEP_AS_NON_CORE. cytoplasm (from the family node
  PTN002805221): ACCEPT.
- protein Ser/Thr kinase activity (IBA, IEA) and ATP binding: ACCEPT.
- nucleotide binding -> MODIFY to ATP binding. Protein kinase activity, kinase activity and
  transferase activity -> MODIFY to GO:0004674 (correct-but-general rule).
- Description rewritten to be project-independent and to state the classification conflict.

Family review disagreement: interpro/panther/PTHR44167/PTHR44167-review.md ("Focused A0BFB4 update
— 2026-09-20") still says the gene review accepts the four autophagy terms. That is out of date (not
edited here; outside this gene folder).

Relative for next review: S. cerevisiae ATG1 (P53104) is the experimentally best-characterised
member of the PAINT subfamily (PTHR24348:SF22) into which A0BFB4 is grafted. No yeast ATG1 review
exists in the repo. Human ULK1 has a review stub (status INITIALIZED). Dictyostelium atg1 and worm
unc-51 have complete reviews. Because orthology is not established, the relation is family_member,
not ortholog.
