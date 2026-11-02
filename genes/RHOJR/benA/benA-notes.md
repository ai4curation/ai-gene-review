# benA (Q932V1, Rhodococcus jostii RHA1) notes

## Provenance of this review

- Created as a cross-genus representative member of
  `modules/benzoate_upper_pathway.yaml`, so the module is grounded beyond
  Pseudomonas putida KT2440.
- Deep research: `just deep-research-falcon RHOJR benA` was attempted and failed with
  "Failed to authenticate" (provider credentials rejected), so there is no
  `-deep-research-*.md` file and none was written by hand. The review rests on
  the UniProt entry and the cached publications: PMID:11673430.
- Every quotation is verbatim from those cached sources; several are
  abstract-only, flagged with `full_text_unavailable` on the reference.

## This gene

- The strongest genetic evidence in the module: the benA insertion mutant RBD169
  neither grows on nor transforms benzoate [PMID:11673430 "The resultant mutant
  strain, RBD169, neither grew on benzoate nor transformed benzoate"]. GO:0043639
  is already IMP in GOA from this paper and is ACCEPTed; the molecular function
  GO:0018623 is absent from GOA and is added as NEW.
- UniProt flags `CAUTION: Lacks conserved residue(s) required for the propagation
  of feature annotation.` on the Rieske ProRule. I checked the sequence directly:
  the Rieske cluster-binding motif `CSHRGAMLCRRKTDNRTTFTCPFH` is present starting at residue
  97 of 458, with the same spacing as the ADP1 and KT2440 proteins, and the
  knockout shows the protein is functional. The
  caution concerns propagation of individual site features, not domain
  membership, so GO:0051537 is ACCEPTed.
- Biphenyl: deliberately no biphenyl term, now recorded as an explicit
  `suggested_questions` entry rather than a silent omission. Benzoate is a
  *product* of the biphenyl upper pathway, so BenA acts on its output rather than
  performing a step of it; the diminished growth on biphenyl is necessity, not
  participation.
