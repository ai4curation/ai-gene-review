# dnajc6 (A0A8M9QG43) - zebrafish auxilin - notes

Zebrafish auxilin (dnajc6; TrEMBL A0A8M9QG43, 974 aa RefSeq XP_021332835.1). The only
primary study of the zebrafish gene is Bai et al. 2010 [PMID:20082716], which is
centred on the paralog gak but characterises zAux in parallel: domain structure
(PTEN-like region, clathrin-binding motif, J domain, no kinase), HeLa-cell
localisation of GFP-zAux, Drosophila rescue with J-domain dependence, and the
neural-restricted expression pattern.

## Re-review 2026-09-28

Validation on entry reported one error: the GO:0072583 clathrin-dependent
endocytosis IEA row (GO_REF:0000117, ARBA) is no longer in the refreshed goa.tsv,
although the refreshed uniprot.txt still lists it (`DR GO; GO:0072583;
P:clathrin-dependent endocytosis; IEA:UniProtKB-ARBA.`). The row was therefore
converted to `action: NEW` (original_reference_id pointing at the uniprot.txt DR
line) rather than deleted, because the zebrafish protein has direct in vivo evidence
for the process [PMID:20082716 "Both zebrafish auxilin and GAK can functionally
substitute for the Drosophila auxilin"] and the human ortholog carries the term by
IBA and IMP.

Row-level changes:

- GO:0004721 phosphoprotein phosphatase activity (IEA, UniRule UR000414225):
  MARK_AS_OVER_ANNOTATED retained, but the reason is now grounded: the UniRule fires
  on the PROSITE tensin-type phosphatase domain (residues 109-276, predicted
  phosphocysteine Cys218), no auxilin has demonstrated phosphatase activity, human
  UniProt hedges it ["May act as a protein phosphatase and/or a lipid phosphatase."]
  and the only functional test of zAux depended on the J domain [PMID:20082716
  "these J-deletions failed to rescue the extra Elav-positive cell phenotype (Figure
  4E &4F) and the lethality"].
- GO:0016787 hydrolase activity (IEA): REMOVE -> MARK_AS_OVER_ANNOTATED, for
  consistency with the phosphatase row from the same rule; the fold is present, the
  activity is unproven, and the ATPase that powers uncoating belongs to Hsc70.
- GO:0030136 clathrin-coated vesicle (IEA SubCell): ACCEPT, now supported by the
  SUBCELLULAR LOCATION line and by zAux/clathrin co-localisation and clathrin
  co-aggregation in HeLa cells [PMID:20082716 "These perinuclear zGAK- and
  zAux-positive structures showed overlaps with clathrin"].
- GO:0005829 cytosol (IDA, ZFIN): ACCEPT -> KEEP_AS_NON_CORE. The observation is a
  low-expression GFP-zAux pattern in HeLa cells [PMID:20082716 "GFP signals were
  mostly cytosolic and slightly enriched near the perinuclear regions"]; a soluble
  pool is expected for a cycling co-chaperone, but the functional site is the coated
  vesicle and the evidence is heterologous overexpression.
- GO:0048471 perinuclear region of cytoplasm (IDA, ZFIN): ACCEPT -> KEEP_AS_NON_CORE.
  Same experiment; the perinuclear structures overlap clathrin and were "most likely
  representing the TGN" without a marker, so no MODIFY to a TGN term.
- Proposed (NEW) rows kept but re-evidenced with the uniprot.txt SUBUNIT line and
  the paper instead of deep-research paraphrases; evidence_type set to ISS to be
  honest that there is no zebrafish biochemistry: GO:0030544 Hsp70 protein binding
  and GO:0001671 ATPase activator activity (J-domain HPD motif present in the
  sequence, "RKAVLVVHPD"; SUBUNIT "Interacts with HSPA8/HSC70 in an ATP-dependent
  manner; this interaction stimulates the HSPA8's ATPase activity"), and GO:0072318
  clathrin coat disassembly (dAux rescue requiring the J domain).

Also rewritten: description (standalone biology, mentions the gak paralog and
neural expression), core_functions (single co-chaperone entry; cytosol dropped from
locations), references (added the zebrafish and human uniprot.txt files with
findings; reference_review on PMID:20082716 verified against the cached title),
suggested questions/experiments (phosphatase activity, clathrin binding, dnajc6 loss
in zebrafish). Validation ends with zero errors and no warnings.

### Follow-up after PR review (2026-10-04)

core_functions now names ATPase activator activity (GO:0001671) as the molecular function instead of Hsp70 protein binding (GO:0030544), matching the core-function prose (auxilin recruits Hsc70 and stimulates its ATPase) and the guidance to prefer an informative activity over a binding term; the binding row remains in existing_annotations as the mechanistic basis. clathrin-dependent endocytosis (GO:0072583) was dropped from directly_involved_in because clathrin coat disassembly (GO:0072318), which remains, is the precise step auxilin performs and the broader term is its ancestor.

### Quote cleanup (2026-10-04)

- Replaced the core_functions falcon deep-research quote ('The primary molecular function is not enzymatic in itself ...') with the contiguous source text, restoring the `**` emphasis that had been stripped.
- No action, reason or term changed; `just validate DANRE A0A8M9QG43` passes with zero errors.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence: cached literature, UniProt, the
PTHR23172 PAINT file and family review, and a new sequence comparison
(`A0A8M9QG43-bioinformatics/compare_isoforms_rereview.py`, `RESULTS-rereview.md`;
no existing bioinformatics files were touched; there were none).

### Identity of the benchmark accession

- A0A8M9QG43 is one of 26 unreviewed UniProt entries for zebrafish dnajc6
  (ZFIN:ZDB-GENE-080104-2), one per RefSeq transcript model. The UniProt
  gene-centric canonical is **A0A8M9Q6X2** (979 aa, XP_021332834.1, annotation
  score 3). A0A8M9QG43 (974 aa, XP_021332835.1) differs only by a 5-residue
  deletion (GPPSP) after residue 66, N-terminal to every domain; phosphatase-like,
  C2, disordered clathrin-binding and J domains are intact, HPD at 938
  [file:DANRE/A0A8M9QG43/A0A8M9QG43-bioinformatics/RESULTS-rereview.md].
- So this is an alternative-splice isoform, not a fragment. Biology is that of the
  gene; differences in GOA between isoforms are a propagation artefact. The
  canonical A0A8M9Q6X2 receives GO_Central IBAs (clathrin binding, synaptic vesicle
  uncoating, clathrin-dependent endocytosis, cytoplasm, vesicle, postsynaptic
  density) that this isoform does not (QuickGO, 2026-10-21).
- No review exists for A0A8M9Q6X2 anywhere in genes/.

### Evolutionary grounding

- PANTHER PTHR23172:SF4 (auxilin) for this entry, the canonical, and human DNAJC6
  (O75061). Bai et al. place zAux with mammalian auxilins rather than zGAK
  [PMID:20082716 "it is more similar to human and mouse auxilin proteins (Figure 2A)"].
- PAINT root PTN000571055 (Eukaryota): IBD clathrin binding, clathrin coat
  disassembly, vesicle, cytoplasm, intracellular membrane-bounded organelle.
  Vertebrate PTN002753975 (Euteleostomi): synaptic vesicle uncoating, postsynaptic
  density. No phosphatase activity at any node, a deliberate omission given the
  PTEN-like fold in every member.
- Family review interpro/panther/PTHR23172/PTHR23172-review.yaml agrees with SF4
  placement (it uses this accession as the SF4 representative) and with the
  non-catalytic reading of the PTEN-like domain. No disagreement.

### Changes

- GO:0004721 phosphoprotein phosphatase activity and GO:0016787 hydrolase activity
  (IEA UniRule): MARK_AS_OVER_ANNOTATED -> REMOVE. The bovine auxilin 1 PTEN-like
  region has no detectable activity [PMID:20826345 "no activity can be detected"],
  attributed to the P loop; zebrafish (CSDGR at C218) and human (CLDGR) share the
  same departure from the PTEN CX5R P loop. Contradicted, not merely unproven.
- GO:0030136 clathrin-coated vesicle: ACCEPT kept, but ARBA SUBCELLULAR LOCATION
  quote replaced by PMID:8524399 and PMID:20082716 (ARBA text is not evidence).
- cytosol, perinuclear region (ZFIN IDA): KEEP_AS_NON_CORE unchanged.
- NEW rows re-grounded: Hsp70 protein binding (ISS, PMID:8524399), ATPase
  activator activity (ISS, curated human UniProt + PMID:8524399), clathrin coat
  disassembly (now IBA-grounded on PTN000571055). ARBA SUBUNIT quotes dropped.
- Added NEW clathrin binding (GO:0030276), root-node IBD inherited by the canonical.
- Dropped the proposed GO:0072583 clathrin-dependent endocytosis row: it is an
  ancestor of GO:0072318 (OLS hierarchicalAncestors), so redundant. Did not propose
  GO:0016191 synaptic vesicle uncoating (descendant) or postsynaptic density; no
  zebrafish synaptic data.
- core_functions: added a clathrin-binding entry; supports switched to primary
  literature and PAINT.
- References added: PMID:8524399, PMID:20826345, PMID:20160091, PAINT tsv,
  RESULTS-rereview.md. None removed; uniprot.txt and deep-research entries carry
  review_notes about their reduced role.

### Relative to review next

Canonical product of the same gene, A0A8M9Q6X2 (dnajc6, 979 aa), relation
same_gene_canonical; no review exists. Suggested folder genes/DANRE/dnajc6 (no
dnajc6 folder exists; this folder is keyed by accession). Closest characterised
ortholog human DNAJC6 (O75061) already has a COMPLETE review.

Modules: modules/synaptic_vesicle_endocytosis.yaml and
modules/synaptic_vesicle_cycle.yaml mention auxilin/DNAJC6.

`just validate DANRE A0A8M9QG43`: valid, no warnings.
