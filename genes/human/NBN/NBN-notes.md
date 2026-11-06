# NBN (nibrin, NBS1) review notes

## Literature search (no deep-research provider available)

No deep-research provider keys were available, so this review rests on a manual search. Sources checked:

- UniProt O60934 (`NBN-uniprot.txt`): FUNCTION, SUBUNIT, DOMAIN and PTM comments. The PTM comment names CDK2 (not CK2) as the Ser-432 kinase.
- All 68 GOA-cited publications, cached with `just fetch-gene-pmids human NBN`. Most are abstract-only; full text was available for PMID:28216226, 18411307, 18583988, 19804756, 27918544, 30657944, 38961290, 26215093, 29709199, 22369660 and others.
- 94 Reactome events cached under `reactome/` (92 nucleoplasm, 2 cytosol).
- Context: telomere end-joining pathway choice (module and GO-CAM review proposed in ai4curation/ai-gene-review#5904; not on this branch and not used as evidence). The cached GO-CAM source model `gocams/65a1f4f800002884/65a1f4f800002884-src.yaml` was read.

## Key findings with provenance

- NBN is the third subunit of MRN: [PMID:9590181 "We have isolated the gene encoding p95, a member of the hMre11/hRad50 double-strand break repair complex."]
- NBN has no DNA-binding region of its own: [PMID:12419185 "NBS1 has no DNA binding region but carries a combination of the fork-head associated (FHA) and the BRCA1 C-terminal domains (BRCT)."]
- NBN binds phosphorylated MDC1 to reach DSB chromatin: [PMID:18583988 "this phosphorylation of MDC1 promotes direct, phosphorylation-dependent interactions with NBS1 in a manner that requires the closely apposed FHA and twin BRCT domains in the amino terminus of NBS1."]
- RAD17 recruits MRN independently of MDC1: [PMID:24534091 "Rad17 is phosphorylated by ATM at a novel Thr622 site resulting in a direct interaction of Rad17 with NBS1"]
- NBN activates ATM: [PMID:16622404 "the ATM-binding domain of Nbs1 is required and sufficient to convert unphosphorylated ATM monomers into enzymatically active monomers in the absence of DNA."]
- NBN activates the MRE11 nuclease: [PMID:30787182 "NBS1 then activates the MRE11-RAD50 nuclease through direct physical interactions with MRE11."] and [PMID:27889449 "NBS1 is absolutely required in the human system."]
- Checkpoints: [PMID:11438675 "the ATM-dependent activation of Chk2 by gamma- radiation requires Nbs1"]
- Telomere repair choice: [PMID:28216226 "Phosphorylation of NBS1 serine 432 by CDK2 in S/G2 dissociates NBS1 from TRF2"] and [PMID:28216226 "Classical-NHEJ-mediated repair of telomeres lacking TRF2 requires phosphorylated NBS1S432 to activate ATM, while interaction of de-phosphorylated NBS1S432 with TRF2 promotes alternative-NHEJ repair of telomeres lacking POT1-TPP1."]

## Curation decisions worth flagging

- Protein binding (36 rows): REMOVE, except 6 rows MODIFIED to GO:0140031 phosphorylation-dependent protein binding. In those 6 the cited paper shows that binding depends on partner phosphorylation (gamma-H2AX, MDC1, RAD17).
- Damaged DNA binding: the IBA and IEA rows (enables) are marked over-annotated, because DNA binding in MRN is carried by MRE11 and RAD50. The IC row (contributes_to) is kept as non-core. The validator flags this as an action mismatch on the same term; the mismatch is deliberate, since the qualifiers make different claims.
- PELI1-derived ISS rows: K63-linked ubiquitination is removed (NBN is the PELI1 substrate, not a ligase, and does none of the ubiquitination). Positive regulation of HR (GO:1905168) is MODIFIED to GO:0000724 HR rather than removed: NBN does promote HR, but as a participant (MRE11 nuclease activation, MRN tethering), and a participant is annotated to the process rather than to its regulation. The bad PELI1 transfer is recorded in that row's propagation_review (PR #5944 review).
- NEW: GO:0170053 nuclease activator activity (IDA, PMID:30787182). Three chromatin-protein adaptor rows cite in vitro nuclease papers. They are accepted because the adaptor claim holds for the gene, and the nuclease activation they actually show is added as its own NEW row.
- GO-CAM 65a1f4f800002884 puts chromatin-protein adaptor activity on NBN with has_input TERF2. The TRF2-NBS1 structure paper describes TRF2 as the hub [PMID:28216226 "We have previously shown that the TRFH domains of TRF1 and TRF2 function as a docking platform for various telomeric and telomere-associated proteins"]. Under the GO:0140463 definition ("or the complex to which it belongs"), NBN docking on TRF2 to hold MRN at telomeres still fits, so the NBN row is accepted. The question is recorded in suggested_questions.
- GO:0110025 (resection at replication forks): kept as non-core. The cited IDA papers use DSB-end substrates; the fork claim rests on PMID:22565321 (fork restart).
- GO:1904354 negative regulation of telomere capping (PMID:17694070): MODIFY to GO:0032206 positive regulation of telomere maintenance, following the paper's model in which TRF1 release promotes telomerase access.

## PR #5944 review follow-up

- Rule applied across the NBN and LIG4 reviews: a developmental or tissue-level process term whose only basis is the knockout phenotype of a housekeeping DNA repair factor (lethality, apoptosis, progenitor loss) records necessity, not participation, and is MARK_AS_OVER_ANNOTATED; it is kept as non-core only where the gene performs a step inside the process itself (as LIG4 does in V(D)J joining during lymphocyte differentiation). Applied to GO:0001701 and GO:0001832 (both MARK_AS_OVER_ANNOTATED).
