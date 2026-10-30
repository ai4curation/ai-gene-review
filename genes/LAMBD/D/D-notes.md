# D (P03712) - Capsid decoration protein (gpD)

## Summary
- **Gene symbol**: `D`
- **UniProt ID**: `P03712`
- **Organism**: *Escherichia phage lambda* (`NCBITaxon:2681611`)
- **Protein**: Capsid decoration protein (`gpD`, 110 aa; 109 aa after initiator Met removal)

## Biological Function
- Trimeric capsid decoration / cementing protein (`gpD`) that binds to the exterior surface of the expanded $T=7$ icosahedral phage lambda capsid at the quasi-threefold and icosahedral threefold axes (140 trimers = 420 copies per virion, equimolar with the 415/420 copies of major capsid protein `gpE`) [PMID:18786402, PMID:18801370, PMID:25053840].
- As viral dsDNA is packaged into the procapsid (~30-50% genome packaged), internal DNA pressure triggers an irreversible procapsid-to-capsid expansion that exposes high-affinity binding sites for `gpD` trimers on the outer shell [PMID:18786402, PMID:18801370].
- Binding of `gpD` trimers mechanically reinforces the thin expanded `gpE` lattice against the ~25-50 atm internal pressure of the full-length 48.5 kb genome, enabling packaging of the final ~15-20% of the wild-type chromosome and stabilizing the mature head against environmental stress [PMID:609100, PMID:18786402, PMID:18801370, PMID:25053840].

## Curation Decisions
- **ACCEPT**:
  - `GO:0098021` (`viral capsid, decoration`, IDA/IMP/IEA `PMID:18786402`, `PMID:25053840`, `PMID:609100`, `GO_REF:0000043`)
  - `GO:0019073` (`viral DNA genome packaging`, IDA `PMID:18801370`)
  - `GO:0030430` (`host cell cytoplasm`, IEA `GO_REF:0000044`)
- **MODIFY**:
  - `GO:0019028` (`viral capsid`, IEA `GO_REF:0000043`) -> `GO:0098021` (`viral capsid, decoration`)
