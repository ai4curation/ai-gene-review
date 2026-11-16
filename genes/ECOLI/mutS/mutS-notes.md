# E. coli mutS (P23909) notes

## 2026-11-13 review session

Context: reference MutS for the MutH-independent MMR module
(`modules/muth_independent_mismatch_repair.yaml`); E. coli itself uses the
Dam/MutH-directed route, but MutS recognition is shared.

### Function summary (with provenance)

- Specific mismatch binding by purified MutS [PMID:3014530 "mutS-encoded protein specifically binds to DNA regions containing a single base-pair mismatch"].
- Asymmetric dimer; one subunit recognizes the mismatch and holds ADP; clamp-like duplex embrace [PMID:11048711 "Only one monomer recognizes the mismatch specifically and has ADP bound."].
- Slow intrinsic ATPase, stimulated by DNA, kinetics change on heteroduplex binding [PMID:10715140 "has a slow ATPase activity that obeys Michalelis-Menten kinetics"].
- Bending during search, kink then unbend at mismatch [PMID:14634210 "binds to DNA nonspecifically and bends it in search of a mismatch"].
- Licensing step enables MutL binding [PMID:33820992 "a dramatic conformational change that enables MutL binding and initiation of the repair"]; connector domain binds MutL [PMID:20080788].
- Tetramers at mismatches [PMID:21666597].
- Reconstituted methyl-directed MMR requires MutS [PMID:2665076]; mutator alleles [PMID:6987663].
- Anti-recombination: mutS mutants lose the E. coli/Salmonella barrier [PMID:2555716 "The requirement for DNA sequence homology in generalized genetic recombination is greatly relaxed in bacterial mutL, mutS and mutH mutants deficient in mismatch repair"]; MMR-null MutS alleles fail to block homeologous recombination [PMID:12606120].
- mutS induced by mitomycin C [PMID:11967071 "the mutS gene involved in mismatch repair is especially noteworthy"].

### Decisions

- GO:0000018 regulation of DNA recombination (IMP, NAS) -> MODIFY to GO:0045910 negative regulation of DNA recombination (is_a child; verified in local GO via runoak).
- GO:0003690 dsDNA binding IBA -> MODIFY to GO:0030983 (GO:0030983 is_a GO:0003690, verified).
- GO:0003684 damaged DNA binding -> MARK_AS_OVER_ANNOTATED (GO:0030983 is not under damaged DNA binding).
- Four bare GO:0005515 rows -> REMOVE (policy).
- Identical protein binding, ATP/ADP binding, DNA bending, A/C mispair binding -> KEEP_AS_NON_CORE.
- PMID:18304323 cytosol: MutS not in the cached text (supplementary tables); deferred to curator, ACCEPT.
- PMID:31757945 (NAS recombination row): the cached full text does not mention recombination; row refined consistently with the IMP row.
