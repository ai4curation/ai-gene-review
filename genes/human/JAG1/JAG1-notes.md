# JAG1 (human, P78504) review notes

## Identity
- Protein jagged-1; Serrate-class DSL ligand. PANTHER PTHR12916 ("CYTOCHROME C OXIDASE POLYPEPTIDE VIC-2", official name) / PTHR12916:SF12 (DELTA-LIKE PROTEIN).
- IBA: Notch binding from PTN002371879.

## Key findings
- Binds NOTCH1/NOTCH3 directly, Ca2+-dependent [PMID:11006133].
- DSL-EGF3 crystal structure; same DSL face for cis and trans interactions [PMID:18660822 "this surface is required for both cis- and trans-regulatory interactions with Notch"].
- MIB1 recognises two epitopes (N-box, C-box) in the JAG1 tail [PMID:25747658].
- JAG1 is a ligand for CD46 on T cells [PMID:23086448 "Here we identified the Notch family member Jagged1 as a physiological ligand for CD46."]
- Alagille syndrome by haploinsufficiency [PMID:9207787]; TOF/PS variants lose Notch activation [PMID:20437614]; CMT2HH variants impair glycosylation/surface expression [PMID:32065591].
- Soluble JAG1 ectodomain antagonises endogenous JAG1 signaling [PMID:11427524] -> adhesion/migration phenotypes from sJ1 (PMID:11549580) treated as over-annotation.
- LFNG/MFNG reduce JAG1-triggered NOTCH2 signaling [PMID:11346656].
- HTRA1 cleaves JAG1 ICD [PMID:29713059].

## Decisions
- Core: Notch binding; receptor ligand activity (NEW, IMP PMID:20437614; comparator DLL1 carries GO:0048018 IDA).
- growth factor activity -> MODIFY to receptor ligand activity; structural molecule activity -> REMOVE.
- protein binding rows: NOTCH1 -> Notch binding; CD46 -> signaling receptor binding; PDZ survey -> PDZ domain binding; HTRA1/VASN -> REMOVE.

## Variant-relevant biology
- Serrate-type ligand: 16 EGF repeats + cysteine-rich region; Fringe-sensitive (Fringe reduces Jagged signaling through NOTCH1/2); C-terminal PDZ motif; JAG1-CD46 non-Notch receptor interaction.
