# dsbB notes

## 2026-10-02

Falcon deep research could not run in this EC2 worktree because `agentapi` was
not on `PATH` and no supported provider API key was available. These manual
notes therefore use the fetched UniProt record, the GOA-seeded PubMed cache, and
the DsbAB module literature.

DsbB is the integral inner-membrane partner that regenerates oxidized DsbA.
Bardwell et al. identified DsbB as the second protein necessary for disulfide
bond formation and proposed that it reoxidizes DsbA, "thereby regenerating its
ability to donate its disulfide bond to target proteins" [PMID:8430071].
Respiratory-chain perturbation experiments then showed that the respiratory
electron-transfer chain participates in DsbA oxidation primarily through DsbB
[PMID:9342327].

The biochemical endpoint is electron flow from reduced DsbA to quinone. A
purified reconstitution found that DsbB uses quinones as electron acceptors
and directly couples disulfide bond formation to the electron transport chain
[PMID:10428033]. Follow-up work showed that DsbB contains a high-affinity
quinone-binding site and that the DsbA-DsbB-quinone system catalyzes oxidative
refolding in vitro [PMID:10854438]. The later EMBO J mechanism paper states
that DsbB "catalyses the oxidation of the periplasmic dithiol oxidase DsbA by
ubiquinone" and resolves the role of the two DsbB catalytic disulfides
[PMID:12853466].

The generic DsbB-DsbA `protein binding` rows are structural captures of the
redox relay, not binding as an independent molecular function. They are better
represented by DsbB electron-transfer activity and quinone-linked oxidation of
DsbA [PMID:17110337; PMID:18775700].


## 2026-11-06 independent annotation audit

The original annotation payloads, including inherited NEW proposals, and frozen UniProt/GOA bytes were preserved. Every row and the core synthesis were reassessed. An initial provider-unspecified invocation was rejected by the CLI; the subsequent explicit Falcon request genuinely reached the provider and failed HTTP403 authentication. No provider report was written. PAINT lineage checks completed after retrying a concurrent cache-download race for the E. coli targets; no IRD/IKR loss was found.

Official QuickGO defines GO:0015035 as “Catalysis of the reaction: a protein with reduced sulfide groups = a protein with oxidized disulfide bonds.” Its reversible equation includes physiological protein oxidation despite the reductase label. GO:0015035 is a descendant of GO:0015036 and GO:0016491. GO:0016672 instead specifies a sulfur-containing donor and quinone acceptor; it is not a descendant of GO:0015035 or GO:0009055. These are distinct specificity axes, not interchangeable granularity levels. Definitions and is_a/part_of ancestor responses were saved in the ignored original-five audit cache from https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015035 and corresponding term/ancestors endpoints.

DsbB directly regenerates oxidized DsbA, using the protein dithiol as electron donor and quinone as acceptor [PMID:12853466: “catalyses the oxidation of the periplasmic dithiol oxidase DsbA by ubiquinone.”]. The purified folding system confirms quinone reduction [PMID:10854438: “we show that quinones get reduced during the course of the reaction.”]. Both protein-disulfide exchange and directed electron transfer are core-compatible claims, not peripheral annotations. Generic membrane refines to plasma membrane. The heat-response row remains UNDECIDED: full24580753 describes the panel experiments but the DsbB-specific figure/supplement result is not exposed in the extracted text; it is not removed as a wrong-gene claim.

Current action counts: {"ACCEPT": 11, "MODIFY": 3, "UNDECIDED": 1}.
