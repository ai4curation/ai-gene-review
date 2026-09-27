# nudA (Aspergillus nidulans, P45444) review notes

## 2026-09-27 initial review (claude-code)

Context: comparative dynein heavy chain member of `modules/nucleokinesis.yaml` (human DYNC1H1 reviewed).

Key evidence
- Cloned as nud gene; cytoplasmic dynein heavy chain, 52% identical to rat [PMID:8134356 "Our study provides in vivo evidence that dynein, a microtubule motor molecule, plays a role in the nuclear migration process."].
- Null viable; backup motors for nuclear migration/division [PMID:7568239 "This suggests that there are redundant backup motor proteins for both nuclear migration and nuclear division."].
- Hyphal tip / plus-end comets; HC-IC interdependence [PMID:11972777]; plus-end accumulation needs kinesin-1 KinA [PMID:12686603].
- ATPase measured on purified dynein; nudF-suppressor alleles in stem/AAA4 [PMID:17237507].
- Walker A mutant binds along MTs; plus-end localization not required for ATPase activation [PMID:20876661].
- Retrograde vesicle transport from tip [PMID:19037104].
- Septation-site localization, septum positioning [PMID:12519184]; tip-cell nucleation and conidiation [PMID:10821171].
- LIS1/NudE relieve dynein phi autoinhibition for HookA activation [PMID:31562232].

Decisions
- Core: GO:0008569 motor activity in GO:0005868; processes GO:0030473 (nuclear migration along MT) and GO:0047496 (vesicle transport along MT).
- REMOVE ARBA system development (animal organ-system concept); cell development marked over-annotated.
- Development (metula, reproduction), MT organization, septum, mitotic spindle organization kept non-core.
- NEW microtubule plus-end (IDA PMID:12686603).

Deep research: no falcon report present at time of review.

## 2026-09-27 falcon deep research incorporated (claude-code)

- Read nudA-deep-research-falcon.md (UniProt accession is P45444; corrected in the header above). Consistent with the review; no action changed.
- New primary papers found via the report and verified at PubMed, then cached: PMID:34428469 (Qiu et al. 2021, AAA3 nucleotide state regulates activation; activated dynein relocates to septal/SPB minus ends) and PMID:9832552 (Beckwith et al. 1998, NudG LC8 co-IPs with the heavy chain and is required for heavy-chain localization).
- Added 9832552 co-IP evidence to the cytoplasmic dynein complex IDA row; 34428469 septal minus-end relocation to the cell septum row (still non-core) and to core function 1; deep-research quote added to core function 1.
- Not used: 2023-2024 mammalian/yeast papers (Okada 2023, Rao 2024 review) - comparative context only.
