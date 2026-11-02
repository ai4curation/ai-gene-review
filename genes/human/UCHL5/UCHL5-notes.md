# UCHL5 (human, Q9Y5K5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: UCHL5 is the closest experimentally characterised relative of S. pombe uch2 (Q9UUB6). Both are in
PANTHER subfamily PTHR10589:SF16 (UBIQUITIN CARBOXYL-TERMINAL HYDROLASE ISOZYME L5), per
`interpro/panther/PTHR10589/PTHR10589-entries.csv`. UCHL5 seeds PAINT node PTN000063280, the source of the
GO:0004843 and GO:0005737 IBAs. S. cerevisiae has no member of this subfamily; Qiu et al. note that UCH37 "is
not found in budding yeast" [PMID:17139257]. ProtNLM2 outputs were not opened or used.

### Deep research

`just deep-research-falcon human UCHL5 --fallback perplexity-lite` failed. Falcon gave "Failed to authenticate"
and perplexity-lite gave HTTP 401 for insufficient quota. No deep-research file exists. The review is built from
cached publications and the UniProt record.

### Literature cached for this review (beyond the GOA set)

PMID:16906146 (Yao 2006), PMID:9034192 (Lam 1997, bovine), PMID:33156996 (Deol 2020), PMID:34761751 (Song 2021),
PMID:35451368 (Du 2022), PMID:25702872 (Vander Linden 2015) and PMID:25702870 (Sahtoe 2015). I verified the
PMIDs against NCBI esummary titles before fetching them.

### What is experimentally established for the human (or mammalian) protein

- Deubiquitinase activity: Uch37 accounts for the PA700 isopeptidase activity, and "PA700 isopeptidase
  disassembles Lys 48-linked polyubiquitin specifically from the distal end of the chain" [PMID:16906146].
  UniProt records that C88A "Abolishes enzymatic activity" (PubMed:16906146).
- Proteasome recruitment and activation: ADRM1/hRpn13 binds the UCH37 C-terminal tail and relieves
  autoinhibition [PMID:16906146, PMID:17139257, PMID:16990800]. Polyubiquitin processing requires
  incorporation into the 19S [PMID:16906146, PMID:18922472].
- K48 debranching: UCH37 "cleaves K48 branched chains", and this is enhanced by RPN13 and promotes degradation
  in reconstituted proteasomes [PMID:33156996]. A K48 chain-specific binding site is required
  [PMID:35451368]. In human cells, binding and deubiquitination of branched chains promote proteasome
  clearance [PMID:34761751].
- INO80: UCH37 is a nuclear INO80 subunit held inactive there [PMID:18922472]. NFRKB inhibits it by blocking the
  ubiquitin-binding site [PMID:25702872, PMID:25702870]. It sits in the N-terminal, metazoan-specific module,
  which is "not required for ATP-dependent nucleosome remodeling" [PMID:21303910].
- Substrate: UCH37 deubiquitinates and stabilises hSmo [PMID:28992318].

### Opposite effects on degradation

Knockdown increased degradation in some studies [PMID:18162577, PMID:23770237] and impaired it in others
[PMID:33156996, PMID:34761751]. Both are compatible with the editing model (rescue of poorly ubiquitinated
substrates) plus debranching (promotes turnover of branched-chain substrates). I accepted the general
regulation term GO:0061136 and kept the negative-regulation term GO:0032435 as non-core.

### Decisions worth flagging

- GO:0004866 endopeptidase inhibitor activity (IMP, PMID:18162577): REMOVE. The abstract itself says UCH37
  RNAi had "no detectable effect on ... proteolytic capacity".
- PMID:25016522 (replication stress): the cached full text mentions only Ino80 and Arp8 knockdowns, never
  UCH37/UCHL5. Its two IMP rows are MARK_AS_OVER_ANNOTATED, and a suggested question asks whether a
  UCHL5-specific knockdown exists.
- INO80-level phenotypes (chromatin remodeling, chromosome organization, cell cycle, transcription) are not
  treated as UCHL5 participation. UCHL5 is inactive in INO80 and sits in a module not needed for remodeling.
  The GO:0033044 IBA (PTN000834083, Eumetazoa, seeded only by human and mouse UCHL5) and its IMP seed are kept
  as non-core rather than removed.
- NEW: GO:1990380 K48-linked deubiquitinase activity, and GO:0005838 proteasome regulatory particle (UCH37 is
  "an intrinsic subunit of PA700" [PMID:9034192]).
- Protein binding: rows with proteasome subunits (ADRM1, PSMD2, PSMD4, PSMA6) are MODIFY to GO:0070628. Rows
  with INO80 subunits, UIP1/HAUS7 and ZBED1 are REMOVE under the protein-binding policy.

### For transfer to S. pombe uch2

Experimentally grounded in human and transferable within SF16: cysteine-type deubiquitinase activity
(also in the PTN000063280 IBA), proteasome binding and the proteasome-associated role. S. pombe Uch2 is the
major proteasome-associated DUB [PMID:15533439]. Do not transfer the following, because they are specific to
metazoan UCHL5: INO80 membership (NFRKB/INO80G is a metazoan-specific INO80 subunit [PMID:21303910]), the
GO:0033044 IBA (its node is Eumetazoa-scoped), and Hedgehog/Smoothened regulation. Whether ADRM1-dependent
activation and K48 debranching are conserved in pombe needs pombe-specific evidence.
