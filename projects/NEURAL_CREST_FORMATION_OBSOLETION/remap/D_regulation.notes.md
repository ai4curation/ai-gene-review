# Group D: regulation-term rows (GO:0090299 / GO:0090300 / GO:0090301)

Input: `D_regulation.input.tsv` (12 distinct rows). Output: `D_regulation.tsv`.
All GO ids checked against QuickGO on 2026-10-09 (live, labels exact). There is no
GO term for regulation of neural crest cell migration or delamination, apart from
cardiac outflow-tract-specific terms (GO:1905310 etc.), so those were not options.

## hdac4 (zebrafish; A0A0R4IAH0, Q08BS8): PMID:22676467, IMP, GO:0090299
Full text read. hdac4 MO removes the anterior cranial crest subset that migrates
medial to the eye, which gives palatal (ethmoid) defects. Premigratory sox10:EGFP
distribution is normal at 12-14 hpf and acridine orange shows no increase in cell
death. The authors leave open whether the cause is specification or migration
("a critical role of hdac4 in a migratory or premigratory anterior population of CNC cells").
**Decision:** REPLACE with the default, GO:1905292 regulation of neural crest cell
differentiation. No more precise term is supported. GO:0001755 neural crest cell
migration (acts_upstream_of_or_within) is a defensible alternative. Uncertain.

## parp3 (zebrafish; Q7ZVB0): PMID:21264220, IMP, GO:0090299
Full text read. The MO reduces sox9a ("the neural crest specifier sox9a is indeed reduced
in parp3 morphants at 10, 16 and 24 hpf") and crestin in premigratory and migratory
crest. dlx3b at the neural plate border is "not severely affected in morphants at 10 hpf".
The authors speculate about a role at the neural plate border, but the border-marker data
do not support NTR neural plate border formation.
**Decision:** REPLACE with GO:1905295 regulation of neural crest cell fate specification.
The data point to a positive sign (GO:1905297). The unsigned term is kept to match the
curator's choice; reviewers could upgrade it.

## Id2 (chicken; O73933): PMID:15242799, IEP, GO:0090300
Abstract only. Id2 is expressed in cardiac crest, and crest ablation *reduces* Id2
expression in the outflow tract. The causal direction is crest → Id2 expression, not
Id2 → crest formation.
**Decision:** REMOVE. This is an expression-only (IEP) row, and expression is not
participation.

## SOX9 (chicken; P48434): PMID:23382206, IMP, GO:0090300
Full text read. Sox9 MO given after crest specification (HH11) blocks trunk crest
delamination, and WT Sox9 rescues it. Phosphorylated, SUMOylated Sox9 cooperates
with Snail2 to drive delamination.
**Decision:** REPLACE with GO:0036032 neural crest cell delamination, the direct process
term. Sox9 performs the step and does not regulate differentiation.

## rgs2 (zebrafish; A0A8M1N0Y4, Q6DG95): PMID:27979767, IMP, GO:0090301
Abstract only (full_text_available: false). Rgs2 loss "induced the formation of neural
crest progenitors" through derepressed Ppard, which activates sox10 transcription.
Rgs2 loss also increased non-ectomesenchymal proliferation and inhibited ectomesenchymal
derivatives.
**Decision:** REPLACE with GO:1905296 negative regulation of neural crest cell fate
specification. The default GO:1905293 would be misleading because Rgs2 *promotes*
ectomesenchymal differentiation. This needs a full-text check of the specifier-marker
data (sox10/foxd3).

## TSPAN18 (chicken; A0A8V0ZLT4): PMID:23418345, IMP, GO:0090301
Full text read. Tspan18 keeps Cad6B protein in premigratory cranial crest and
"antagonize[s] cranial neural crest EMT". Overexpression blocks migration. Knockdown
does not advance emigration timing. Nothing in the paper concerns specification or
differentiation.
**Decision:** REPLACE with GO:0010719 negative regulation of epithelial to mesenchymal
transition. GO has no regulation-of-crest-delamination term. If GO wants a crest-specific
term, "negative regulation of neural crest cell delamination" would be an NTR.

## Fuz (mouse Q3UYI6, IMP PMID:23806618; rat Q3B756 ISS + ISO; human Q9BT04 ISS)
Full text read. Fuz mutants have excess cranial crest with no increase in mitosis or
apoptosis. The defect is non-cell-autonomous: the paper reports "Fuz requirements in the
neural tissue prior to NC induction", where Gli3 processing restrains Fgf8. A
Wnt1-cre conditional knockout does not reproduce it. No specifier-marker data are given.
**Decision:** REPLACE with the default, GO:1905293 negative regulation of neural crest cell
differentiation. The effect is indirect, through Fgf8. The ISS/ISO transfers to rat and
human follow the mouse decision.
