# NCU02539 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7SHS5, NEUCR, 1013 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 37 current GOA rows.

## Evidence basis

NCU02539 encodes the Mcm4 subunit of the conserved Mcm2-7 replicative helicase. Mcm4 contributes to DNA binding and ATP-dependent DNA unwinding in a multisubunit complex, participating in origin licensing, initiation and elongation of nuclear DNA replication. Its domain architecture includes the MCM N-terminal and OB-fold regions, an AAA+ ATPase domain and an Mcm4 winged-helix region.

- file:NEUCR/NCU02539/NCU02539-uniprot.txt: “DR   InterPro; IPR008047; MCM_4.”
- PMID:19896182: “The licensing of eukaryotic DNA replication origins, which ensures once-per-cell-cycle replication, involves the loading of six related minichromosome maintenance proteins (Mcm2-7) into prereplicative complexes (pre-RCs).”
- PMID:10567526: “the Mcm4 protein may play a role in the single-stranded DNA binding activity of the complex.”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0033260: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.83"}, {"key": "string_match_text", "value": "GO:0006279"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]
- GO:0006270: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.97"}, {"key": "string_match_text", "value": "GO:1902975"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]
- GO:0003677: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "0.98"}, {"key": "string_match_text", "value": "GO:0003697"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon report returned and was inspected. Publication caching ran concurrently. The report is retained as received; consequential claims are checked against primary sources and sequence evidence below.

## Falcon report appraisal and catalytic caution

The returned Falcon report correctly supports Mcm4 identity through the subfamily-specific MCM_4 signature, distinguishes complex-level DNA unwinding from an autonomous monomer and finds no direct NCU02539 experiment. Its broad review-derived mechanism agrees with the independently cached primary reconstitution PMID:19896182 and Mcm4-containing-complex mutant analysis PMID:10567526. The additional mammalian cancer/application and quantitative claims are not transferred to this fungal gene. RNA/hybrid helicase activity, four-way-junction unwinding and rDNA protrusion residence are unresolved electronic transfers. The PROSITE statement “Lacks conserved residue(s) required for the propagation of feature annotation” is generic: the current record retains Walker A 662–669 and Walker B 726–729 annotations. It does not establish a pseudoenzyme and does not refute replication participation.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Every one of the 37 GOA rows was re-examined. The earlier review
reused one generic three-quote block on every row; this pass gives each row its own ortholog primary
evidence.

### Identity and sequence (file:NEUCR/NCU02539/NCU02539-bioinformatics/RESULTS-rereview.md)
- Q7SHS5 is the full-length canonical Mcm4 product of NCU02539 (1013 aa), not a fragment or alternative gene
  model. Global alignment covers 97-98% of S. cerevisiae MCM4 (P30665; 55.8% identity), S. pombe cdc21/Mcm4
  (P29458; 59.3%) and human MCM4 (P33991; 49.0%). It has an extra ~80 residues at the disordered N-terminus.
- Walker A GDPSTSKS (645-652), Walker B VCCIDEFDK (705) and SRF arginine finger (777) are identical to the
  yeast Mcm4 proteins. **Correction to the 2026-09 notes:** the UniProt Walker A/B MOTIF coordinates
  (662-669, 726-729) are misplaced and contain APRGVYTS / MEQQ. This explains the PROSITE-ProRule caution.
  The earlier claim that "the current record retains Walker A 662–669" was wrong about the residues,
  although its conclusion (no pseudoenzyme) holds.
- No canonical C4 zinc finger is present, but none is present in S. cerevisiae or S. pombe Mcm4 either, so
  this is a fungal Mcm4 feature.

### Evolutionary grounding
- PANTHER PTHR11630:SF66 (MCM4). PAINT nodes: PTN000179968 (Mcm4 subfamily; seeds SGD MCM4, PomBase cdc21)
  carries GO:0000727, GO:0006271 and GO:1902975. PTN000179711 (MCM2-7) carries GO:0042555, GO:0003697 and
  GO:0017116. PTN000179712 carries nucleus. The IRD negations on PTN001701204/PTN002267485 are metazoan
  branches and do not affect fungi.
- Family review interpro/panther/PTHR11630/PTHR11630-review.yaml places NCU02539 in SF66. No disagreement.

### Action changes from the previous review
- MODIFY (too general, refined to terms the gene already carries): GO:0003677 -> GO:0003697. GO:0003678,
  GO:0017116 (IBA+IEA) and GO:0043138 -> GO:1990518 (GO:1990518 is_a both, checked with QuickGO ancestors).
  GO:0006260 -> GO:0033260.
- MARK_AS_OVER_ANNOTATED: GO:0003727 ssRNA binding and GO:0033679 DNA/RNA helicase, both in vitro side
  properties from PMID:16829518 ["they could translocate only along DNA and only DNA stimulates the ATPase
  activity of the enzymes"]. GO:0009378 four-way junction helicase, an in vitro Mcm4,6,7 subcomplex effect
  (PMID:13679365). GO:0030875 rDNA protrusion, a fission-yeast-specific nuclear structure.
- KEEP_AS_NON_CORE (previously ACCEPT): GO:0003682 chromatin binding, GO:0003688 origin binding (ORC selects
  origins; loaded MCM slides along dsDNA, PMID:19896182), and GO:0097373 MCM core complex.
- Cytoplasm stays KEEP_AS_NON_CORE: budding-yeast CDK-driven export (PMID:10559985, PMID:10704410) is not
  tested in Neurospora.
- Core functions were rewritten. (1) contributes_to GO:1990518 in the CMG complex at the nuclear replication
  fork, in initiation and elongation. (2) Licensing: MCM complex in pre-RC assembly, contributing to ssDNA
  binding, on chromatin.

### Relative
- Closest characterised relatives in the same PANTHER subfamily and PAINT node are S. cerevisiae MCM4/CDC54
  (P30665) and S. pombe cdc21 (P29458). S. cerevisiae MCM4 is chosen because it seeds PTN000179968 for
  GO:0000727/GO:0006271 and has the most complete biochemistry. There is no yeast MCM4 review in the repo
  (genes/yeast/CDC21 is the unrelated thymidylate kinase P06785). The repo has worm mcm-4 (genes/worm/mcm-4).
- Modules: modules/dmel_replication_origin_licensing_activation.yaml covers the same licensing/CMG pathway
  in Drosophila.
