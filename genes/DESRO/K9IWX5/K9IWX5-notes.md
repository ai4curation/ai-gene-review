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
