# Bioinformatics Scripts - Correction Log

## 2026-09 (PR #3229): feature-driven rewrite

**The retracted finding.** An earlier version of this pipeline reported that
Epe1's Fe(II) site is an "HVD motif at position 280" and concluded that the JmjC
domain is non-catalytic. That came from taking the first `H.[DE]` regex hit as
the iron site. It is wrong. UniProt O94603 annotates the Fe(II) ligands as H297
and E299 (FT BINDING), and its CC CAUTION notes Tyr at position 370, where
active JHDM1 enzymes have the third, His, ligand. H280-V281-D282 is a motif
match, not a ligand, and active KDM2A's own ligand H212 is an HVD motif.

**What was changed:**

- **`uniprot_features.py` (new):** parses UniProt FT DOMAIN, FT BINDING,
  FT MUTAGEN and the CC CAUTION position from `../Epe1-uniprot.txt`, and the
  same features from comparator UniProt JSON. Doctests cover the Epe1 values.
- **`01_fetch_sequences.py`:** four of five comparator accessions were
  mislabelled: P84027 is a spider toxin, Q6ZMT4 is KDM7A, Q92833 is the
  inactive JmjC protein JARID2, and P41229 is KDM5C. The table now uses
  verified accessions (O75164 KDM4A, Q9Y2K7 KDM2A, P41229 KDM5C, Q9UGL1 KDM5B,
  Q9Y4C1 KDM3A, Q6ZMT4 KDM7A). The script saves each comparator's UniProt
  JSON, refuses a record whose entry name disagrees with its label, and uses
  the current UniProt search syntax (`taxonomy_name:`).
- **`02_jmjc_domain_analysis.py`:** the JmjC region and Fe(II) ligands come from
  UniProt features, not from the first `H.[DE]` hit. The motif scan is kept
  only as a cross-check, with each hit labelled as an annotated ligand or not.
- **`03_conservation_analysis.py`:** the domains are UniProt features, aligned
  with MAFFT. The output is the residue at each Epe1 annotated site in every
  protein. This replaces a "conservation" score computed on unaligned windows,
  and a verdict ("indicating loss of demethylase catalytic activity") from a
  code path that always fired.
- **`04_functional_regions_analysis.py`:** comparator domains come from UniProt
  instead of hardcoded approximate ranges. It reports the Fe-ligand count in
  place of a hardcoded "Pseudo-enzyme?" label. The HVD summary and the
  "non-catalytic JmjC domain" conclusion are removed.
- **`05_structural_features.py`:**
  - The bare HVD search, its "unusual for Fe(II) binding" message and the red
    figure markers are removed.
  - The hardcoded "Fe-binding region 275-285" and "αKG site 290-305" boxes and
    the "HP1 binding 849-948" segment are removed. The figure now marks the
    UniProt BINDING, CAUTION and MUTAGEN positions.
  - The unconditional "Structure retained but catalytic activity lost" and
    "Functions as a pseudo-enzyme" lines are removed.
- **`justfile`:** the hardcoded "Key Finding: HVD…" and "Conclusion:
  Non-catalytic JmjC domain" echo lines are removed. `summary` prints the
  computed result file.
- **`test_pipeline.py`:** rewritten as pytest tests. They check:
  - the Epe1 features;
  - the canonical H-(D/E)-H triad in KDM4A;
  - that the 280 hit is labelled as not an iron site;
  - that no script carries the retracted hardcoded conclusions.
- **Legacy scripts removed:** `analyze_epe1.py`, `analyze_jmjc_protein.py`, their
  outputs `epe1_refactored.json` and `kdm5a_test.json`, and the `main.py`
  template stub. They hardcoded 400-600 boundaries, used 0-based positions and
  drew an activity verdict from the motif scan.

All `results/` files and figures were regenerated with `just all`. `just test`
passes. See RESULTS.md.

## Earlier fix (superseded)

An earlier pass replaced literal strings such as "HVD instead of HXD" with code
that searched for the motif. That removed the hardcoding but kept the
underlying error, because the searched-for motif was still read as the iron
site. The rewrite above addresses the error itself.
