# EFR3A (horse, A0A3Q2GU27) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Record.** A0A3Q2GU27 (TrEMBL, 821 aa) is the full-length canonical-start product of horse
EFR3A (Ensembl ENSECAG00000014883, transcript ENSECAT00000044066; VGNC:17452). PANTHER
PTHR12444:SF1 (EFR3 homolog A subfamily). GOA has three rows: plasma membrane (IBA, IEA/ARBA)
and protein localization to plasma membrane (IBA, PTN000278197). No ProtNLM2 file or
prediction-evidence folder was opened.

**Deep research.** `just deep-research-falcon HORSE EFR3A__A0A3Q2GU27 --alias EFR3A --fallback perplexity-lite`
failed (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). No
deep-research file was created. Literature used instead: the cached full texts behind the human
EFR3A review (genes/human/EFR3A), PMID:23229899, PMID:24360784, PMID:39705356, PMID:25608530.
No horse-specific experimental study of EFR3A is known.

**Evolutionary grounding.** Horse, human (Q14156) and mouse (Q8BG67) EFR3A are all in
PTHR12444:SF1 and descend from PTN000278197, where PAINT placed plasma membrane and protein
localization to plasma membrane. Yeast Efr3 is in a different PANTHER family (PTHR47766), so the
yeast structure in PMID:24360784 is not used for transfer; the mouse EFR3A basic-patch mutant in
that paper is.

**Bioinformatics** (EFR3A__A0A3Q2GU27-bioinformatics/compare_to_human.py, RESULTS.md): 98.54%
identity to human over all 821 residues; Cys6-Cys9 palmitoylation cluster identical
[PMID:23229899 "palmitoylation-deficient mutants (C6S/C7S/C8S/C9S for EFR3A and C5S/C7S/C8S for EFR3B) were localized in the cytosol"];
basic patch K50/R53/R61/R68/R70 identical [PMID:24360784 "A conserved basic patch in Efr3, which binds acidic phospholipids, anchors the complex to the plasma membrane."];
C-terminal TTC7B/FAM126A-binding region 724-787 63/64 identical (I786V)
[PMID:39705356 "The EFR3A C terminus undergoes a disorder-order transition upon binding to the PI4KA complex, with an unexpected direct interaction with both TTC7B and FAM126A."].

**Decisions.** Accept all three GOA rows (inferred, not observed, in horse). Add NEW ISS
GO:0043495 protein-membrane adaptor activity, the activity behind the two IBA rows, as in the
human review. Not added: a phosphoinositide biosynthesis process, because PAINT did not propagate
one at PTN000278197 (treated as a deliberate decision; raised as a suggested question), and the
GPCR-responsiveness and SynGO synaptic terms, which are indirect phenotypes in human/mouse.

**Established in horse vs inferred.** Nothing is experimentally established for horse EFR3A.
Everything is inferred from human/mouse EFR3A in the same subfamily, with every functional
element conserved.
