# YvgJ (UniProtKB:O32206) notes

## Identity
- UniProt O32206 = YVGJ_BACSU, gene `yvgJ`, locus BSU33360 (note: the CMMMech
  thulium record and the Moriwaki manuscript use **BSU33400**, a locus-tag
  discrepancy worth checking; UniProt current = BSU33360). PE 3 (inferred from
  homology).
- Functionally characterised as an **LTA primase** (not a polymer synthase):
  it transfers the first glycerolphosphate onto the glycolipid anchor to make
  GroP-Glc2-DAG [PMID:21255105 "YvgJ functions as an LTA primase, transferring
  the initial glycerolphosphate subunit onto the glycolipid anchor and therefore
  producing GroP-Glc2-DAG"]. A strain expressing YvgJ only makes no LTA polymer.
  It is the B. subtilis counterpart of L. monocytogenes primase Lmo0644.
- Mn2+-dependent PG hydrolysis in vitro like the other three; does not restore
  S. aureus LTA synthesis [PMID:17483484].

## CMMMech cross-reference (data/records/thulium.yaml) — do NOT edit CMMMech
- Identity O32206 = YvgJ: **correct**. CMMMech calls it
  "Lipoteichoic acid primase/synthase YvgJ", consistent with its primase role.
- **Locus tag discrepancy.** CMMMech uses yvgJ / **BSU33400**; current UniProt
  O32206 lists **BSU33360**. (BSU33400 appears to be an outdated/renumbered tag.)
- **EC number wrong.** CMMMech asserts EC 2.7.8.40 (an unrelated Aeromonas
  O-antigen enzyme). YvgJ has no specific EC in UniProt; its reaction is a
  glycerophosphate priming transfer (EC 2.7.8.-).
- The CMMMech causal graph treats all four paralogues as "LTA synthases" that
  "produce" the LTA layer. YvgJ is strictly a **primase** and cannot elongate
  the polymer; the shared GENE_OR_PROTEIN node label slightly over-states YvgJ's
  role, though it does contribute the priming step.
