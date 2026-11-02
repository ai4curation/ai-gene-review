# GEI-17 acidic-cluster check

Question: does GEI-17 (Q94361) keep the acidic module to which PMID:24036127 maps PIAS1's
ligase- and SAP-independent inhibition of IRF3 ("the C-terminal region of PIAS1 around a
cluster of acidic amino acids")?

Method: `acidic_clusters.py` reads the cached UniProt records and reports every run of
8-residue windows holding at least 6 D/E, positioned relative to the SP-RING zinc finger
(FT ZN_FING) and the protein end. For each cluster it then looks up to 12 residues upstream
for a SIM-like hydrophobic core of the psi-psi-x-psi or psi-x-psi-psi class (psi = V/I/L),
and reports whether that core overlaps a UniProt-annotated SUMO-binding region or is a motif
call only. It is a positional description, not an alignment.

Run from the repo root:

```
python genes/worm/gei-17/gei-17-bioinformatics/acidic_clusters.py
```

Output (2026-10-05):

```
cluster definition: >= 6 D/E in any 8-residue window
SIM-like core: (?=([VIL][VIL].[VIL]|[VIL].[VIL][VIL])) within 12 aa upstream of a cluster

PIAS1 (human, O75925): length 651, SP-RING 320-405
  annotated SUMO1-binding region 462-473
  acidic cluster 467-476 SSDEEEEEPS: +62 aa from SP-RING end, 175 aa before C-terminus
    SIM-like core 457-460 VEVI (motif only, not annotated)
    SIM-like core 459-462 VIDL (overlaps UniProt SUMO-binding region 462-473 by 1 of 4 aa)

GEI-17 (C. elegans, Q94361): length 780, SP-RING 400-485
  acidic cluster 504-513 ISDDDDDDVV: +19 aa from SP-RING end, 267 aa before C-terminus
    no SIM-like core within 12 aa upstream
  acidic cluster 548-557 LSDDDDEELN: +63 aa from SP-RING end, 223 aa before C-terminus
    SIM-like core 545-548 IITL (motif only, not annotated)
```

Context (sequence slices from the same records):

- PIAS1 455-480: `KKVEVIDLTIDSSSDEEEEEPSAKRT`. The SIM core (VIDL) is followed by the acidic run.
- GEI-17 538-560: `KKPADDDIITLSDDDDEELNRGI`. A SIM-like core (IITL, 545-548) is followed by an
  acidic run, 63 residues past the SP-RING, the same position as in PIAS1.
- Asymmetry: PIAS1 has a UniProt-annotated SUMO1-binding region (462-473, `LTIDSSSDEEEE`) in
  this module, but it abuts the VIDL core (sharing only L462) and mostly covers the acidic run;
  GEI-17's IITL is called by motif and analogy only, and no SUMO-binding region is annotated in
  Q94361.

Interpretation:

- PIAS1 has exactly one acidic cluster under this definition, the SIM-adjacent stretch, so it
  is the most likely candidate for the region PMID:24036127 describes. The abstract does not
  give residue numbers, so this identification is an inference.
- GEI-17 keeps a positionally equivalent, motif-predicted SIM-plus-acidic module after the
  SP-RING. Its own C-terminus (about 600-780) is not acidic, but PIAS1's acidic cluster is not
  at its extreme C-terminus either (175 residues before it).
- So the ligase-independent binding route behind the PIAS1 donor annotation is not excluded
  for GEI-17 by sequence. Whether GEI-17 binds and inhibits any transcription regulator this way
  is untested.
