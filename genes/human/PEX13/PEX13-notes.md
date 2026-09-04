# PEX13 curation notes

## 2026-09-04 — PAINT no-IBA project finishing pass (AI-assisted)

First journal entry for this gene; the review was drafted with all actions assigned but no
`core_functions` block and no notes file. Work done in this session:

### Authored `core_functions`

One core function, built around the SH3 domain rather than around localisation:

- `molecular_function: GO:0030674` protein-macromolecule adaptor activity — PEX13's
  cytoplasmically oriented SH3 domain engages the PTS1 receptor PEX5 and also PEX14, so it
  physically couples the cargo-loaded receptor to the rest of the translocon.
  [PMID:8858165 "We have identified Pex13p, a novel integral peroxisomal membrane from both
  yeast and humans that binds the PTS1 receptor via a cytoplasmically oriented SH3 domain."]
  and [PMID:9653144 "Recombinant Pex14p was specifically recognized by the “import
  inhibiting” ab-MF3 and bound Pex5p and the Src homology 3 (SH3) domain of Pex13p in
  ligand blots."]
- `contributes_to_molecular_function: GO:0008320` — see below.
- `directly_involved_in`: GO:0016558 / GO:0016560 / GO:0016561;
  `locations`: GO:0005778; `in_complex`: GO:1990429.

The loss-of-function phenotype is what makes the adaptor reading rather than a generic
"structural component" reading defensible: the defect is in receptor engagement, not in
membrane assembly. [PMID:8858165 "loss of Pex13p further reduces the amount of
peroxisome-associated Pex5p by approximately 40-fold. Furthermore, loss of Pex13p eliminates
import of peroxisomal matrix proteins that contain either the type-1 or type-2 peroxisomal
targeting signal but does not affect targeting and insertion of integral peroxisomal
membrane proteins. We conclude that Pex13p functions as a docking factor for the
predominantly cytoplasmic PTS1 receptor."]

### Material changes to existing annotations

- **GO:0008320 (IDA, PMID:28765278): MARK_AS_OVER_ANNOTATED → ACCEPT.** The draft argued
  that transmembrane transport is an emergent property of the whole DTM and so should not
  be ascribed to PEX13. That argument is out of date. Ravindran et al. show that Pex13
  itself phase-separates with Pex5-cargo, that import depends on the aromatic residues of
  the Pex13 IDR, and that import coincides with transient Pex13/Pex14 focusing at the
  membrane — i.e. PEX13 is conduit-forming, not a peripheral scaffold. [PMID:37165185
  "cargo import correlates with transient focusing of GFP-Pex13 and GFP-Pex14 on the
  peroxisome membrane"] The activity is still only exercised within a multi-subunit
  translocon, so it sits in `contributes_to_molecular_function`, not `molecular_function`.
  Also fixed the term label (GOA writes "transmembrane protein transporter activity"; the
  ontology snapshot used by the term validator writes "protein transmembrane transporter
  activity" — the latter is what validates).
- **GO:0005515 IPI rows for PMID:8858165 (PEX5) and PMID:9653144 (PEX14):
  MARK_AS_OVER_ANNOTATED → MODIFY**, with `proposed_replacement_terms: GO:0030674`. Project
  guidance is to replace bare protein binding with an informative MF term for adapter
  function rather than merely flagging it. The three PEX19-related protein-binding rows
  (PMID:10704444, PMID:20531392, PMID:32296183) stay MARK_AS_OVER_ANNOTATED — there PEX13
  is PEX19's cargo, which is not a molecular function of PEX13.
- **GO:0034614 cellular response to ROS (IDA, PMID:26344566): kept
  MARK_AS_OVER_ANNOTATED, reasoning rewritten.** The cached record for this paper is full
  text (`full_text_available: true`) and a search of the entire body returns no occurrence
  of PEX13; the ROS-responsive participants characterised are ATM, PEX5, the
  PEX2/PEX10/PEX12 E3 and p62, with PEX1 and PEX14 as the pexophagy readouts. So the usual
  caution — "the abstract foregrounds another gene but the full text may assay the target" —
  does not apply here. Still not REMOVE, because supplementary material is outside the
  cache and PEX13 loss is independently reported to raise peroxisomal ROS.
- **NEW GO:0016558**: reason previously cited GO:0140888, which is not the term being
  proposed and does not belong here; rewritten to state the actual rationale (GOA carries
  the two sub-steps but not their parent, and the loss-of-function phenotype is failure of
  import per se).

### Deep research

Cited `file:human/PEX13/PEX13-deep-research-falcon.md` on the GO:0008320 and GO:0016561
rows and in `core_functions`, where it genuinely informed the decision — it is the source
that frames PEX13 as the conduit rather than a docking-only factor
["PEX13 contributes the core **translocation conduit** in the peroxisomal
docking/translocation module (DTM)"], which is exactly the point on which I reversed the
GO:0008320 call.

### Notable

- The gene is on the project's "human no-IBA" list, but PEX13 in fact receives three IBAs
  (GO:0005778, GO:0016560, GO:1990429) from PANTHER node PTN001063987. The list is stale
  with respect to current GOA. What PEX13 has no IBA for is any **molecular function** — the
  PAINT curation of PTHR19332 is CC/BP only. See the family review at
  `interpro/panther/PTHR19332/PTHR19332-review.yaml`.
- Validation is clean (0 errors, 0 warnings); status set to COMPLETE.
