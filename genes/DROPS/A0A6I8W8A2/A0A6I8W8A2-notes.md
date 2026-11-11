# A0A6I8W8A2 (LOC117183218, Drosophila pseudoobscura) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. GOA has no annotations for this accession, so the
review covers identity, description and core functions only.

### Identity (isoform)
- A0A6I8W8A2 is RefSeq isoform X3 (XP_033239512.1, 169 aa) of LOC117183218 (NCBI Gene
  117183218, chromosome X, 4 transcripts/4 proteins). The other products are X1
  A0A6I8W805 (282 aa), X2 A0A6I8W807 (233 aa) and X4 A0A6I8W815 (144 aa); none is
  reviewed in UniProt. [file:DROPS/A0A6I8W8A2/A0A6I8W8A2-bioinformatics/RESULTS.md]
- X3 residues 6-169 = X1 residues 119-282; X3 has an alternative 5-residue N-terminus
  (MSPLI vs HVCRL) and lacks X1 residues 1-118, which include part of X1's first RCC1
  repeat (X1 repeats 50-144, 145-200, 201-255; X3 repeats 32-87, 88-142).
- No product of the gene has a HECT domain. The "HERC3" RefSeq name is a homology label
  based on RCC1 repeats only. The earlier review's framing ("truncated isoform of a HERC3
  E3 ligase") was wrong: the whole gene is RCC1-only, not just this isoform.

### Evolutionary placement
- PANTHER: X1/X3/X4 are in PTHR22872 (BTK-BINDING PROTEIN-RELATED) at family level with no
  subfamily, but X2 of the same gene is in PTHR22870:SF408, so the PANTHER placement is
  unstable for this short sequence.
- Closest relatives (local alignment of X1): D. pseudoobscura LOC6903915 (RCC1-only, 91%),
  then the N-terminal RCC1-like domain of D. pseudoobscura Herc4 (76-79%, PTHR45622:SF76,
  HECT-containing), then D. melanogaster Herc4 (FBgn0035207, 63-64%). D. melanogaster has no
  RCC1-only counterpart and NCBI lists no orthologs. This points to a lineage-specific
  partial duplication of the Herc4 RLD (pairwise inference, no tree).
- The closest characterised relative is therefore Herc4, which sits in a different PANTHER
  family (PTHR45622) from this gene (PTHR22872). Its HECT ligase function cannot be
  transferred because the HECT domain is absent. The PAINT IBD for ligase activity at
  PTN002504778 (PTHR22872 PAINT file, seeded by FB:FBgn0035207 and HERC5) does not reach
  this accession: no IBA exists for it.
- Deep research (falcon) assumed a HERC3 ortholog with a HECT domain and transferred mammalian
  HERC3 ERAD/MM1/EIF5A2 functions; that is rejected here.

### Changes from the previous review
- Removed the root `molecular_function` (GO:0003674) and the unsupported `cytoplasm` location
  from the core function; stated that no MF has been established.
- Replaced support quotes that relied on deep research and the ProtNLM review with the
  UniProt features and a new reproducible analysis (A0A6I8W8A2-bioinformatics/).
- Rewrote the description to correct the HERC3 framing and record the isoform identity.

### Family review / modules
- interpro/panther/PTHR22872/PTHR22872-review.yaml uses this accession as the only
  representative of a generic "RCC1-repeat multidomain proteins" entry and does not mention
  that the sequence has no PANTHER subfamily or that a sibling isoform is in PTHR22870. Its
  ligase-activity verdict (not justified for this sequence; family-wide scope unresolved)
  agrees with this review.
- No modules/ entry covers this gene.
