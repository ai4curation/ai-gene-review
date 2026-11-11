# A0A804UIX9 (Zea mays, Zm00001eb381380) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Annotation state
- The GOA file has no rows, so there are no existing annotations to review.
- UniProt PE 4 (predicted). The only reference is the B73 genome paper (PMID:34353948). There is no
  literature on this locus.

### Identity / gene model (see A0A804UIX9-bioinformatics/RESULTS-rereview.md)
- A0A804UIX9 is the product of the Ensembl canonical transcript Zm00001eb381380_T001 (375 aa). The
  alternative transcript T002 is A0A804R394 (316 aa).
- Residues 1-297 are about 98% identical to the tandem paralog A0A804R017 (Zm00001eb380900). The
  C-terminal 298-375 is not conserved. The paralog, and T002 in a different frame, carry the
  conserved PGG/TM continuation `LLGLMGAYAAGSCREVHESTYVICLNAGVLAYIFLQ`. The T001 tail therefore
  looks like a frame-shifted read-through, which probably truncates the second PGG domain (missing
  its last TM). The benchmark accession is the canonical product of its gene, but it is a probably
  defective gene model at the C-terminus. No reviewed canonical entry exists for this gene.
- The genomic sequence could not be retrieved (Ensembl REST sequence endpoint returned 503), so the
  frameshift is inferred from protein comparisons only.

### Family / evolutionary placement
- PTHR24177 "CASKIN" is entirely plant: UniProt query
  `xref:panther-PTHR24177 AND taxonomy_id:33090` gives 12,734 of 12,734 members, and
  taxonomy_id:33208 (Metazoa) gives 0. Human CASKIN1 Q8WXD9 is in PTHR24174. The earlier review
  and the OpenScientist report say that the plant proteins are "grouped with animal CASKINs" by a
  cross-kingdom misassignment. That is wrong: the family contains no animal members, and
  only its name is misleading.
- No PTHR24177 member is reviewed in Swiss-Prot. SF432 (296 members) is grass/monocot-only and
  wholly uncharacterised.
- ACD6 (Q8LPS2), ITN1, NPR4 and the other reviewed PGG proteins are all in PTHR24186, a different
  family. The earlier review called ACD6 the "closest characterized homolog". That relationship is
  domain-level only (Pfam PF13962), not a subfamily or orthology relationship. ACD6 functions
  (ion-channel-like Ca2+ influx, SA-dependent defence) must not be transferred.
- PAINT/IBA: no IBA rows exist for this protein, and there is no PAINT node to argue with.

### Corrections made to the review
- The description now records the gene-model caveat and the all-plant family composition, and
  drops the "closest homolog ACD6" framing.
- The core function supporting quote that cited bracketed editorial text attributed to the falcon
  report was replaced with verbatim UniProt Phobius feature lines and the new RESULTS-rereview.md.
- The falcon deep research (PGIP misinterpretation) was kept as a reference flagged MISCITED. The
  OpenScientist report was kept, and its CASKIN cross-kingdom claim is flagged.
- Core function: still the molecular_function root plus membrane. No NEW annotations were made.

### Relative
- No characterised member in PTHR24177. The nearest experimentally characterised PGG protein is
  Arabidopsis ACD6 (Q8LPS2, PTHR24186:SF46), a domain-level family member only. No review exists
  in the repo.
- Modules: none relevant. grep hits for "PGG" in modules/ are unrelated substrings.
