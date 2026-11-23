# nuoE notes

- NuoE is the small 2Fe-2S electron-transfer subunit of the peripheral input arm
  [file:PSEPK/nuoE/nuoE-uniprot.txt "Name=[2Fe-2S] cluster"]. It relays
  electrons but does not independently oxidize NADH.

- GO:0051537 is retained as the direct cofactor function; whole-complex
  oxidoreductase terms are not treated as direct NuoE activities.

## 2026-09-24 TreeGrafter re-review

The TreeGrafter GO:0003954 NADH dehydrogenase activity row was changed from
MARK_AS_OVER_ANNOTATED to MODIFY, proposing GO:0008137 NADH dehydrogenase
(ubiquinone) activity with a contributes_to qualifier: the generic term is an
is_a ancestor of the complex-level activity and should be handled the same way
as the UniProt-sourced GO:0008137 rows in the sibling Nuo reviews
(projects/TREEGRAFTER/rereview-2026-09-24/batch-06a.yaml).

## 2026-11-02 rework to a full review

Deep-research providers are unavailable in this environment (no API keys); the
review rests on curated UniProt rule/signature content for Q88FH4 (PIRSR
[2Fe-2S] ligands Cys91/96/132/136, PIRSF000216, NCBIfam TIGR01958, PROSITE
PS01099) and on E. coli literature for the orthologue (same PANTHER subfamily,
PTHR10371:SF3), stated as orthology in each reason. RecName quotes removed.

- GO:0003954 (TreeGrafter): MODIFY -> ACCEPT. The PAINT source node is a
  contributes_to assertion; the N-module activity is the right reading.
- GO:0016491: over-annotated (no substrate site). GO:0030964 -> GO:0045271 (MODIFY).
- GO:0051537: accepted (PIRSR ligands; E. coli N1a mutagenesis [PMID:28509551]).
- NEW (ISS from E. coli): GO:0009055 electron transfer activity [PMID:18316732
  "The major part of N1a undergoes very fast reduction with a time constant"],
  GO:0045271, GO:0022904, GO:0005886.
- Core function: MF GO:0009055, contributes_to GO:0008137 (module leaf for NuoE).
