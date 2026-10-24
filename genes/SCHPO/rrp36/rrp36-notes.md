# rrp36 evidence notes

Rrp36 is a conserved nucleolar ribosome-biogenesis factor associated with the 90S preribosome. It supports early processing of the small-subunit rRNA precursor and production of the 40S ribosomal subunit. Comparative experiments in budding yeast and human cells establish a conserved requirement for early pre-rRNA cleavages, while fission yeast localization and curated phylogenetic evidence support the corresponding role of Rrp36. An intrinsic RNA-cleaving activity has not been established.

## Identity and prediction provenance

PomBase primary symbol rrp36, locus SPAC823.04, current UniProt Q9P6P2. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:20038530 Evolutionarily conserved function of RRP36 in early cleavages of the pre-rRNA and production of the 40S ribosomal subunit.] "We show that the Rrp36p protein is nucleolar and interacts with 90S and pre-40S preribosomal particles. Its depletion affects early cleavages of the 35S pre-rRNA and results in a rapid decrease in mature 18S rRNA levels."
- [PMID:16823372 ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe.] "Next, we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."

## Evidence limits and adjudication


Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

The full original function paragraph and all atomic claims are assessed in [rrp36-protnlm-function-review.md](rrp36-protnlm-function-review.md).

## Provider report appraisal

The Falcon report correctly distinguishes budding yeast/human RRP36 experiments from the fission yeast target; its absence-of-localization finding is incomplete because GOA includes the target tagged-ORFeome observations. The report and primary PMID:20038530 were inspected.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9P6P2 is the reviewed, canonical Swiss-Prot entry for rrp36/SPAC823.04 (279 aa, sequence version 4 after the gene-model revision in PMID:21270388). It is not a fragment, isoform or alternative gene model. It carries the full RRP36 domain (PF06102, IPR009292), a coiled coil (160-218), and disordered charged termini (1-117, 245-279).

Evolutionary grounding: PTHR21738 has one subfamily, SF0, and all 72 cached members are in it, including S. pombe Q9P6P2, S. cerevisiae RRP36 Q12481 and human RRP36 Q96EU6 (interpro/panther/PTHR21738/PTHR21738-entries.csv). The PAINT node PTN000497661 propagated the SSU-rRNA maturation process and 90S preribosome membership from SGD RRP36, and nucleolus from SGD plus human. PAINT did not propagate a pre-40S term, and I add none. The PANTHER family review (interpro/panther/PTHR21738/PTHR21738-review.yaml) agrees, with no subfamily placement issue.

Literature: [PMID:20038530 "Its depletion affects early cleavages of the 35S pre-rRNA and results in a rapid decrease in mature 18S rRNA levels."], human ortholog conserved. [PMID:31996908 "strong positive interactions were observed for Rrp9 with Rrp36 and Sgd1"]; [PMID:31996908 "some SSU-processome proteins remain unmapped, including Rrp36 and Sgd1 for which no 3D structures are established"]. Fission yeast direct data are limited to the ORFeome localization (UniProt "Nucleus, nucleolus {ECO:0000269|PubMed:16823372}").

Actions: GO:0000462 IBA ACCEPT. GO:0003674 ND ACCEPT (no activity or motif known). Nucleus HDA MODIFY to nucleolus, which is more specific, in the same paper, and already on the gene. Nucleolus HDA/IBA/IEA ACCEPT. 90S preribosome IBA ACCEPT. I rewrote the description to be more specific, added suggested questions and experiments, and proposed no NEW terms.

Relative for next review: S. cerevisiae RRP36 (Q12481, YOR287C, SGD:S000005813). It is the PAINT donor in the same subfamily (SF0) and the experimentally characterised ortholog. There is no review in the repo (no genes/yeast/RRP36). Modules: none found for the SSU processome or 90S.
