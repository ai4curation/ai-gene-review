# GEI-17 acidic-cluster check

Question: does GEI-17 (Q94361) keep the acidic module to which PMID:24036127 maps PIAS1's
ligase- and SAP-independent inhibition of IRF3 ("the C-terminal region of PIAS1 around a
cluster of acidic amino acids")?

Method: `acidic_clusters.py` reads the cached UniProt records and reports every run of
8-residue windows holding at least 6 D/E, positioned relative to the SP-RING zinc finger
(FT ZN_FING) and the protein end. It is a positional description, not an alignment.

Run from the repo root:

```
python genes/worm/gei-17/gei-17-bioinformatics/acidic_clusters.py
```

Output (2026-10-05):

```
PIAS1 (human, O75925): length 651, SP-RING 320-405
  annotated SUMO1-binding region 462-473
  acidic cluster 467-476 SSDEEEEEPS: +62 aa from SP-RING end, 175 aa before C-terminus

GEI-17 (C. elegans, Q94361): length 780, SP-RING 400-485
  acidic cluster 504-513 ISDDDDDDVV: +19 aa from SP-RING end, 267 aa before C-terminus
  acidic cluster 548-557 LSDDDDEELN: +63 aa from SP-RING end, 223 aa before C-terminus
```

Context (sequence slices from the same records):

- PIAS1 455-480: `KKVEVIDLTIDSSSDEEEEEPSAKRT`. The SIM core (VIDL) is followed by the acidic run.
- GEI-17 538-560: `KKPADDDIITLSDDDDEELNRGI`. A SIM-like core (IITL) is followed by an acidic
  run, 63 residues past the SP-RING, the same position as in PIAS1.

Interpretation:

- PIAS1 has exactly one acidic cluster under this definition, the SIM-adjacent stretch, so it
  is the most likely candidate for the region PMID:24036127 describes. The abstract does not
  give residue numbers, so this identification is an inference.
- GEI-17 keeps an equivalent SIM-plus-acidic module at the equivalent position after the
  SP-RING. Its own C-terminus (about 600-780) is not acidic, but PIAS1's acidic cluster is not
  at its extreme C-terminus either (175 residues before it).
- So the ligase-independent binding route behind the PIAS1 donor annotation is not excluded
  for GEI-17 by sequence. Whether GEI-17 binds and inhibits any transcription regulator this way
  is untested.
