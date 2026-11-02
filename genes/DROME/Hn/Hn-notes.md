# Hn-PD review notes

FlyBase confirms the native 178-residue PD product. [Sequence comparison](Hn-bioinformatics/RESULTS.md) maps it to full-length positions 275–452 with all three annotated iron ligands retained. The large deletion includes much of the catalytic scaffold; binding and enzyme activity cannot be inferred from the remaining ligand residues alone. Conversely, no direct assay of inactivity was identified. The three catalytic IEAs are removed and the external oxidoreductase claim is NPI: controlled human-to-Hn mapping identifies missing substrate and cofactor-binding architecture. Iron binding and both biological-process rows remain UNDECIDED; the external metabolic-process claim is UNC. Gene-level full-length Henna biology is not disputed.

[PMID:10694386](https://pubmed.ncbi.nlm.nih.gov/10694386/) and [PMID:12126628](https://pubmed.ncbi.nlm.nih.gov/12126628/) supply structural positions, checked against full-length Hn before interpreting the PD deletion. See the additional `just human` analysis and its positive control.

Falcon completed after its wrapper timed out. Its gene-level synthesis supports full-length Henna biology, including dietary tyrosine rescue and distinction from neuronal Trh; it does not resolve the native PD product. The manual synthesis supplies the exact-isoform structural analysis.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** E8NH57 is not the canonical Henna product. FlyBase lists it as Hn-PD (FBpp0306708, 178 aa, transcript Hn-RD, RefSeq NP_001261543; full cDNA BT125933). I re-checked the sequences directly: E8NH57 is an exact suffix of reviewed P17276 (452 aa, Hn-PA/PC), starting at internal Met275 (P17276 275-452, no substitutions). So it is an N-terminally truncated alternative isoform that lacks the ACT domain (36-107) and residues 1-274 of the catalytic scaffold, while keeping the iron ligands His284/His289/Glu329 (PD His10/His15/Glu55) and the C-terminal oligomerization region. No protein-level evidence for Hn-PD was found; the 45 kD embryonic band reported by Neckameyer and White 1992 (FlyBase snapshot) is too large to be PD (20 kD).

**Evolutionary placement.** UniProt places E8NH57 in PANTHER PTHR11473:SF24 (PHENYLALANINE-4-HYDROXYLASE). PAINT puts phenylalanine 4-monooxygenase activity, L-tyrosine biosynthesis and L-phenylalanine catabolism at PTN000895564 (Bilateria), with FB:FBgn0001208 (Hn) among the donors, so the function is ancestral for full-length Henna. The question for this entry is not placement but whether the truncated product keeps the domain needed for the activity; it does not (existing Hn-bioinformatics/RESULTS.md human-PAH site mapping, re-read; no new analysis needed).

**Changes vs previous version.**
- Catalytic MF rows (GO:0004497, GO:0004505, GO:0016714): REMOVE kept, reason rewritten as an explicit domain-architecture mismatch for the isoform, noting the activity is correct for full-length Henna.
- GO:0005506 iron ion binding: UNDECIDED kept (ligands retained, pocket half missing, untested).
- GO:0006571 L-tyrosine biosynthetic process and GO:0009072 aromatic amino acid metabolic process: UNDECIDED -> MARK_AS_OVER_ANNOTATED. True of the gene, but rest only on the electronic catalytic inference that fails for PD; a non-catalytic role is untested.
- Description rewritten to cover the gene and to state clearly that this accession is the Hn-PD isoform.
- Added suggested_questions/experiments (is PD translated; does it co-assemble with full-length Hn).
- core_functions left empty on purpose: no function is established for the PD polypeptide itself.

**Family review.** interpro/panther/PTHR11473/PTHR11473-review.yaml agrees on SF24 placement. Small point: it uses E8NH57 (the short isoform) as the SF24 representative; full-length P17276 would be a better catalytic representative.

**Next relative.** Canonical P17276 (full-length Henna) has no review in the repo, so it is the next target (folder genes/DROME/Hn__P17276, since genes/DROME/Hn is keyed to E8NH57).

**Modules.** Relevant: modules/catecholamine_biosynthesis.yaml, modules/serotonin_melatonin_biosynthesis.yaml, modules/tetrahydrobiopterin_metabolism.yaml (all reference PTHR11473/PAH).
