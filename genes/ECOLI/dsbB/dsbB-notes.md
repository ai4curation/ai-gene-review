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
