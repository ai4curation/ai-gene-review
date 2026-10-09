# rad50 (Drosophila RAD50) review notes

## Literature journal
- Null phenotypes: [PMID:15296753 "null mutations in the Drosophila mre11 and rad50 genes cause both telomeric fusion and chromosome breakage"]; localization [PMID:15296753 "we show that this protein is uniformly distributed along mitotic chromosomes"]; [PMID:15296753 "Rad50 is unstable in the absence of its binding partner Mre11"].
- Capping: [PMID:15296753 "Cytological analysis revealed that mutations in rad50 and mre11 drastically reduce accumulation of HOAP and HP1 at telomeres."]
- P-element allele: [PMID:15135728 "The induction of DSBs and defects in chromosome segregation are in agreement with a role of Drosophila Rad50 in repairing the DSBs that arise during replication."]
- No telomerase in Drosophila: [PMID:15296751 "Since Drosophila telomeres are not added by a telomerase"].

## Curation decisions
- Core: ATPase subunit of MRN in DSB processing/repair; telomere capping.
- Telomere maintenance via telomerase (IBA) removed: no telomerase in Drosophila.
- Telomere maintenance via recombination: IBA/IEA over-annotated, IMP modified to telomere capping (GO:0016233).
- Intracellular protein localization IMP modified to protein localization to chromosome, telomeric region (GO:0070198).
- Protein binding (IPI) removed; telomeric/G4 DNA binding IBAs kept as non-core.

## Falcon deep research (added after the initial review)
- The report agrees with the review: Rad50 is the ATP-dependent architectural MRN subunit, with nuclease activity supplied by Mre11 [file:DROME/rad50/rad50-deep-research-falcon.md "Rad50 contributes ATP-dependent structural control while Mre11 supplies nuclease activity"]. It also supports telomere capping via HOAP/HP1 recruitment [file:DROME/rad50/rad50-deep-research-falcon.md "HOAP and HP1 also failed to accumulate detectably at mutant polytene-chromosome"]. No annotation decisions changed.
