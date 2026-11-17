# Comparative flagellar panel: identity and assay scope

The ten reviewed accessions are defined by their frozen UniProt records. Protein sequence identity, native assay background, engineered complementation and heterologous expression are recorded separately. Sequence identity does not turn every experiment on a Salmonella laboratory derivative into a native LT2 experiment.

| Target | Reference identity | Primary evidence and limits |
|---|---|---|
| PSEPK PP_4336 / Q88EW6 | KT2440 MotC | PMID36409076 explicitly maps MotCD to PP_4336/PP_4335. KT2440 FliC_S267C labeling background and stator deletions/complementation; liquid swimming and semisolid spreading, not direct proton flux. |
| PSEPK PP_4335 / Q88EW7 | KT2440 MotD | Same matched native-background evidence. MotAB and MotCD are alternative stators with different environmental contributions; neither pair should be a universal obligatory assembly gate. |
| SALTY fliI / P26465 | LT2 STM1972 | Existing curated review; PMID29946050 reconstructs transport in inverted membrane vesicles. ATP-only export in those conditions is distinct from normal PMF-supported export and from ATPase-deficient bypass mutants. |
| SALTY fliJ / P0A1K1 | LT2 STM1973 | RCSB3AJW contains its complete147-residue sequence plus N-terminalGSH. PMID21934659 tests native Salmonella SJW backgrounds and tagged interaction constructs; FlhA binding/export activation is distinct from motor torque. |
| SALTY flhA / P40729 | LT2 STM1913 | PMID21934659 and26943926 distinguish wild-type export, ΔfliHI bypass and overexpression ion assays. Transfer to the LT2 reference is explicit; no exact native LT2 assay claim is manufactured. |
| SALTY fliK / P26416 | LT2 STM1974 | RCSB2RRL contains HM followed by reference residues204–370. It is a fragment, not a complete405-residue ruler. PMID19732341 and29946050 establish switching and hook-length regulation in their respective genetic/reconstitution contexts. |
| SALTY flgE / P0A1J1 | LT2 STM1177 | RCSB6K3I entity1 exactly matches residues2–403, with initiatorMet absent. Other polyhook studies use SJW880; do not relabel those preparations LT2 merely because the reference sequence matches. |
| SALTY flgM / P26477 | LT2 STM1172 | PMID10972838 publisher Table2 lists LT2; transduction methods explicitly describe introduction of inducible flhDC insertions into LT2. Native checkpoint assays use engineered derivatives. |
| VIBAL pomA / O06873 | Species-level V.alginolyticus accession | RCSB8ZYW entity2 exactly matches all253 residues. PMID39793043 structural preparation is recombinant BL21(DE3)/pLysS. Native Vibrio functional assays and mutant ion-leak proxies are separate. |
| VIBAL pomB / O06874 | Species-level V.alginolyticus accession | RCSB8ZYW entity1 exactly matches all315 residues plus C-terminalHis6. The alternative SIFTS accession A0A7H8DMV8 differs at position132 and is not used as an exact construct identity. |

## Important source distinctions

- [PMID10972838 publisher full text](https://onlinelibrary.wiley.com/doi/full/10.1046/j.1365-2958.2000.02081.x), Experimental procedures, transduction methods: “were transduced into LT2 to separate them from the flhC::MudJ element”. The publication cache remains abstract-only. This short passage was read through the web article reader; the separate Python retrieval returned403 and is not represented as a successful full-text acquisition.
- PMID37500658 uses ATCC17749 DNA, modified PomB preparations including a protease insertion, and VaPotAB hybrid functional tests in Salmonella LT2. Those hybrid experiments do not establish native Vibrio anchoring or motor assembly.
- PMID18326582 separates V.alginolyticus NMB191 ΔpomAB and VIO5 experiments from E.coli PomA/PotB hybrid experiments. It measures swimming speed as well as semisolid-agar rings. Its informal word “swarming” does not alone establish GO collective solid-surface swarming.
- PMID39793043 resolves PomAB structures with ions and phenamil and tests mutants. Growth inhibition after plug deletion is an ion-leak proxy; structural sodium occupancy is not itself a single-channel flux measurement. The modern stator is A5B2 despite the still-stale A4B2 wording in GO0120101.
- PMID26943926 establishes conditional sodium-supported export and FlhA ion conductance; this is not sodium-driven stator rotation. GO0009977 currently requires pH-gradient dependence, whereas efficient wild-type export can be Δψ-driven; it is not used as a universal replacement for FlhA function.

## Reproducible sequence checks

`sequence-bridges.yaml` records authoritative URLs and response/sequence hashes. `construct-sequences.fasta` retains only the five assayed protein sequences needed for the exact comparison. `check-sequence-bridges.py` compares them to frozen gene UniProt records and reports the expected fragment/tag boundaries. No cached publication, UniProt source, GOA payload or provider report was edited.
