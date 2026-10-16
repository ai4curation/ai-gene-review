# TBCK review notes

## Why this gene was selected

TBCK is a case where the gene *name* asserts more than the evidence supports: "TBC1 domain-containing
kinase" carries "kinase" in the symbol, and GOA carries `GO:0004672 protein kinase activity`. The
supporting evidence code is **NAS** (non-traceable author statement) against the Manning human-kinome
census, not an experiment — and the same GOA record simultaneously carries a **NOT** annotation for
`GO:0006468 protein phosphorylation` from the very same reference. GOA therefore already holds both
sides of the question, incoherently.

## The kinase assignment

Provenance of the NAS pair is the kinome census, which was an inventory of kinase-fold genes, not an
assay: [PMID:12471243 "We identify 518 putative protein kinase genes, of which 71 have not previously
been reported or described as kinases"]. UniProt's own comment on the entry (Q8TEA7) is
`DOMAIN: The protein kinase domain is predicted to be catalytically inactive. {ECO:0000255}` — i.e.
a sequence-model prediction, matching the negative `NOT|involved_in GO:0006468` row.

The 2026 biochemistry closes this. Full-length human TBCK was expressed in Sf9 cells and purified for
the first time; the pseudokinase domain does not even bind nucleotide:
[PMID:42546825 "Biochemical and biophysical analyses reveal that the catalytically inactive pseudokinase
domain of TBCK lacks nucleotide binding, consistent with the absence of the canonical VAIK, HRD, and DFG
motifs required for catalysis."]. The DSF titrations with ATP, GTP, ADP, GDP and Mg2+ gave no ligand-induced
shift: [PMID:42546825 "These results, therefore, indicate that none of the tested nucleotides measurably
stabilize or destabilize the global thermal stability of TBCK under the conditions examined, consistent with
TBCK functioning as a class I pseudokinase."]. Coupled-enzyme assays found no hydrolysis of either nucleotide:
[PMID:42546825 "This indicates that the TBCK pseudokinase domain exhibits no detectable ATPase activity under
these conditions"] and [PMID:42546825 "Similarly, no GTP hydrolysis was observed in the assay when ATP was
replaced with GTP, indicating this is not specific to ATP."].

**Caveats weighed.** This is a single laboratory publishing in a methods-oriented journal (Protein Expr
Purif), and PMID:41958985 is the bioRxiv preprint of the same work by the same authors — it is not
independent corroboration, and I have counted it as one body of evidence, not two. Against that: the
biochemistry agrees with a sequence argument that was already in UniProt and in the original disease
papers, the assays include the right positive control (asparagine synthetase), and no publication in
twenty years has reported a TBCK kinase activity or a TBCK substrate. On balance the kinase and
ATP-binding assignments are argued down rather than merely demoted.

## The Rab-GAP assignment is the better-supported one

The TBC domain, unlike the pseudokinase domain, retains its catalytic machinery:
[PMID:42546825 "The TBC domain of TBCK retains conserved arginine and glutamine residues characteristic of
GTPase-activating proteins (GAPs), suggesting that TBCK may function as a GAP toward small GTPases"].
Disease genetics pointed the same way a decade earlier — the recurrent missense allele sits on the TBC
arginine finger: [PMID:27040692 "Structural analysis implicated Arg511 as a required residue for Rab-GAP
function"] and [PMID:27040692 "These results suggest that loss of Rab-GAP activity is the underlying
mechanism of disease."].

This was demonstrated in 2025-2026. A Fudan group identified the GAP and its target
(primary paper PMID:41207833, Sci Bull; summarised by the same authors in an Autophagy punctum):
[PMID:41789809 "we identify TBCK as the catalytic core of a heterotrimeric complex comprising TBCK,
PPP1R21, and FERRY3/C12orf4"], [PMID:41789809 "This complex functions as a specific GTPase-activating
protein (GAP) for RAB5."], and the loss-of-function phenotype is what a RAB5-GAP loss predicts:
[PMID:41789809 "TBCK deficiency or missense mutations of its key residues in the RABGAP-TBC domain lead to
constitutive RAB5 hyperactivation, which blocks the transition from early to late endosomes and results in
the formation of massively enlarged RAB5-positive endosomes."].

So the two halves of the protein point in opposite directions: the domain in the gene's name is dead, and
the domain that is not in the name is the catalytic one.

## FERRY complex membership

TBCK is a subunit of the five-protein FERRY complex, a Rab5 effector:
[PMID:37267905 "we discovered a Rab5 effector, the five-subunit endosomal Rab5 and RNA/ribosome intermediary
(FERRY) complex, that recruits mRNAs and ribosomes to early endosomes through direct mRNA-interaction"].
The mRNA contact is made by other subunits, not by TBCK:
[PMID:42546825 "This is consistent with the observation that TBCK does not directly participate in mRNA
interactions within the FERRY complex"]. The `regulation of intracellular mRNA localization` annotation is
therefore a complex-level process TBCK participates in, not an activity of TBCK itself.

## The mTOR claim is contested

The original TBCK paper reported mTOR effects on knockdown:
[PMID:23977024 "Knockdown of TBCK induces a significant decrease in the protein levels of components of mTOR
complex (mTORC), and suppresses the activity of mTOR signaling"] and
[PMID:23977024 "Depletion of TBCK significantly inhibits cell proliferation, reduces cell size, and disrupts
the organization of actin, but not microtubule."].
A human neural-progenitor model does not reproduce it:
[PMID:39553985 "These data showed that loss of TBCK did not inhibit mTORC1 activity in neither NPC nor neurons."]
and [PMID:39553985 "mTORC1 inhibition is inconsistent across different patients and cell types"].
The 2026 review of the field says as much:
[PMID:41789809 "While the TBCK gene has been implicated in MTOR signaling, its primary molecular function has
remained controversial."]. Kept, but non-core, with the dispute recorded.

## Curation position taken

- `GO:0004672` protein kinase activity (NAS) and `GO:0005524` ATP binding (IEA InterPro + NAS) →
  **REMOVE**. NAS author statements and a kinase-fold signature transfer, both contradicted by direct
  biochemistry on the purified human protein and by UniProt's own inactivity prediction. This is the
  case CLAUDE.md reserves REMOVE for (wrong IEA/signature mapping, arguable on biological grounds),
  not the case it forbids (second-guessing an experimental annotation).
- `NOT|involved_in GO:0006468` protein phosphorylation (NAS) → **ACCEPT**. The negative assertion is
  correct and is now experimentally corroborated.
- `GO:0005096` GTPase activator activity (IBA) → **ACCEPT** as the core molecular function.
- `GO:0032006` regulation of TOR signaling (IMP) → **KEEP_AS_NON_CORE**, dispute recorded.
- `GO:0008283` cell population proliferation and `GO:0030036` actin cytoskeleton organization (IMP) →
  **MARK_AS_OVER_ANNOTATED**: knockdown phenotypes several steps downstream of an endosomal GAP.
- Mitotic-apparatus locations (spindle, mitotic spindle, midbody) → **KEEP_AS_NON_CORE**: a single
  2014 study of a long TBCK isoform, not reproduced and not connected to the endosomal function.
- Bare `protein binding` → over-annotated.

## Open questions

Does the pseudokinase domain do anything? Class I pseudokinases commonly work as allosteric or
scaffolding modules, and TBCK's has a sizeable but low-confidence cavity in the AlphaFold model. The
rhodanese-like domain is likewise predicted dead:
[PMID:42546825 "the rhodanese-like domain is predicted to be catalytically inactive, as it lacks the
conserved CX4-5R active-site motif found in enzymatically active rhodanese family members"]. Neither
domain has a described binding partner or function, yet disease alleles hit the protein throughout.
