# GEMIN5 (horse, F6WDM0) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: F6WDM0 is the full-length (1517 aa) product of horse GEMIN5 (Ensembl gene ENSECAG00000020479,
protein ENSECAP00000018265). It is kept in its own folder (`GEMIN5__F6WDM0`) because `genes/HORSE/GEMIN5/`
holds a different UniProt accession from the same gene (A0A9L0R5P7). ProtNLM2 output was not consulted.

Deep research: `just deep-research-falcon HORSE GEMIN5__F6WDM0 --alias GEMIN5 --fallback perplexity-lite`
failed (falcon: "Exception: Failed to authenticate"; perplexity-lite fallback: HTTP 401 insufficient quota).
No deep-research file was produced. The review relies on the cached primary literature on human GEMIN5
and on the human review at `genes/human/GEMIN5/`.

Evolutionary grounding:
- F6WDM0 and human Q8TEQ6 are both PANTHER PTHR46362:SF1 and receive IBAs from PAINT node PTN005299808
  (donors include human, mouse and Drosophila rig). Ensembl Compara GO_REF:0000107 rows cite human
  ENSP00000285873 as one-to-one ortholog.
- Alignment (GEMIN5__F6WDM0-bioinformatics/RESULTS.md): 88.8% identity over 1507 aligned positions; full
  length; one 9-aa horse insertion in the second WD40 propeller (after human 618). All 12 snRNA-contact
  residues mutated in PMID:27881601, the m7G contacts Y474/L580/N582 and the cap-binding residues W286/F338
  (PMID:19750007) are identical.

Experimental status: there are no experimental data on horse GEMIN5. Every function here is inferred.
- Phylogenetically placed (IBA, PTN005299808): spliceosomal snRNP assembly, mRNA 3'-UTR binding,
  SMN complex, nucleus.
- Ortholog transfer only (Ensembl Compara from human IDA): snRNA binding (and U1/U4/U4atac), RNA
  7-methylguanosine cap binding, ribosome binding, regulation of translation, SMN-Gemin2 and SMN-Sm
  protein complexes, cytosol, nuclear body.
- PAINT did not place snRNA binding or cap binding at PTN005299808 despite human IDA. Treated as a
  node-level decision (the node includes insects); transfer between one-to-one mammalian orthologs with a
  fully conserved binding surface is still accepted, but flagged as a suggested question. Ribosome binding
  and translation regulation (single-lab human evidence, not propagated by PAINT) are kept non-core.

Decisions (consistent with the human review): RNA binding -> MODIFY to snRNA binding + mRNA 3'-UTR binding;
nucleus (IBA) -> MODIFY to nucleoplasm + gems; cytoplasm -> MODIFY to cytosol; nuclear body -> MODIFY to
gems; regulation of translation -> MODIFY to positive + negative regulation of translation.
