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
