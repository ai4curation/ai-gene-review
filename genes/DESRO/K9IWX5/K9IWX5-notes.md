# K9IWX5 Research Notes

## Key findings
- UniProt describes this protein as a putative scp crisp extracellular protein [file:DESRO/K9IWX5/K9IWX5-uniprot.txt "SubName: Full=Putative scp crisp: scp-like extracellular protein"].
- UniProt assigns this protein to the CRISP family [file:DESRO/K9IWX5/K9IWX5-uniprot.txt "Belongs to the CRISP family."].
- Deep research identifies K9IWX5 as a CRISP-like extracellular protein from vampire bat [file:DESRO/K9IWX5/K9IWX5-deep-research-falcon.md "K9IWX5 is a UniProt accession (not a gene symbol) that encodes a putative CRISP-like extracellular protein from Desmodus rotundus (common vampire bat)."].
- UniProt cautions that conserved residues required for feature propagation are missing [file:DESRO/K9IWX5/K9IWX5-uniprot.txt "CAUTION: Lacks conserved residue(s) required for the propagation of"].

## 2026-07-31 compliance review

Traced the provenance of this entry. The EMBL record behind K9IWX5 (JAA45881.1,
TISSUE=Salivary gland) comes from the "Vampirome" study of the *D. rotundus*
submaxillary glands, now cached as PMID:23411029. That paper is directly usable
as a reference for this protein and resolves two things the review previously
had to leave open:

- **Secretion is solidly supported, and the UniProt CAUTION is unrelated to it.**
  The CAUTION is scoped to `PROSITE-ProRule:PRU01005`, which is the *ShKT* rule —
  it limits ShKT feature/functional transfer, not the subcellular location. The
  location is independently supported by the SignalP signal peptide (1..22 with a
  cleaved 23..241 chain), CRISP family membership, and direct proteomic recovery
  of the family from the gland: [PMID:23411029 "secretoglobin (65 ions) and
  antigen-5/CRISP families (57)"]. Changed `GO:0005576` from UNDECIDED to ACCEPT
  on that basis.
- **The molecular function really is unknown, and the field says so.** The same
  paper states [PMID:23411029 "With few exceptions [59, 116], their function is
  unknown."] and [PMID:23411029 "Evidently, the function of these proteins in bat
  saliva can only be assigned after recombinant expression."]. This is a genuine
  BIOLOGY/MF_DARK gap rather than an under-curation gap, so the core function is
  recorded with a location but deliberately **no** `molecular_function` term, plus
  two knowledge gaps (unknown activity; possibly degenerate ShKT module).

Deliberately did *not* import the deep-research file's CRISP ion-channel and
reproduction narrative as positive evidence: it is family-level inference drawn
largely from snake-venom reviews that the report itself flags as low-quality
journals, and none of it concerns *Desmodus*. Marked that reference
`relevance: MEDIUM / correctness: UNVERIFIED`.

## Review follow-up (2026-07-31)

Addressed the PR review on the `weekly-compliance-2026-07-31-K9IWX5` branch:

- **Hedged the secretion claim.** The `description` and the PMID:23411029
  `findings` statement asserted that the protein is "a bona fide component of
  vampire bat saliva delivered to the host bite site". The evidence does not
  carry that: the proteomic hit [PMID:23411029 "secretoglobin (65 ions) and
  antigen-5/CRISP families (57)"] is a *family-level* ion count from dissected
  gland homogenate, not a peptide assignment to K9IWX5 and not expectorated
  saliva. Both now say the family is translated in the gland and that delivery
  of this protein into saliva has not been directly demonstrated — which is
  consistent with `suggested_experiments` #3, that proposes to test exactly this.
  The `GO:0005576` ACCEPT is unaffected: signal peptide + cleaved chain + CRISP
  family membership carry it independently.
- **Moved the annotation-propagation caution out of `description`.** Per
  CLAUDE.md the top-level `description` is a project-independent biological
  summary, so the "lacks conserved residues required for propagating ShKT
  feature annotation" sentence is restated biologically (the ShKT module is
  degenerate at residues conserved in canonical ShKT domains). The curation
  caveat itself is already recorded in the second `knowledge_gaps` entry.
- **Re-attributed the InterPro quote.** `InterPro; IPR018244; Allrgn_V5/Tpx1_CS.`
  is a `DR` line from the UniProt record, not text of GO_REF:0000002, so it now
  hangs off the `file:DESRO/K9IWX5/K9IWX5-uniprot.txt` reference. The GO_REF
  finding keeps its statement with no `supporting_text`, matching the convention
  used elsewhere in the repo for GO_REFs (no cached GO_REF documents exist).
- **Dropped the falcon deep-research file from the `GO:0005576` `supported_by`.**
  That reference is graded `correctness: UNVERIFIED` with review_notes saying it
  is "Not used here to support any positive functional claim" — localisation is a
  positive claim. The other three lines of evidence carry the ACCEPT. (This makes
  validation emit a non-blocking warning that no annotation cites the deep
  research file; that is the intended state here.)
- **Corrected the disulfide count** in `suggested_experiments` #1: UniProt
  annotates only two disulfides (215..233, 224..237); the mature 23-241 chain
  carries 16 cysteines, so up to eight bonds are *expected* for the CRISP fold
  rather than predicted in the record.
