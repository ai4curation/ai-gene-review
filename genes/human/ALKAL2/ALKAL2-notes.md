# ALKAL2 (human, Q6UX46) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: this gene is the experimentally characterised reference for the donkey
(EQUAS) ALKAL2 ortholog A0A9L0J5U7. Both are in PANTHER subfamily PTHR28676:SF2
(ALK AND LTK LIGAND 2), as confirmed in `interpro/panther/PTHR28676/PTHR28676-entries.csv`
and the UniProt PANTHER cross-reference. ALKAL1 (Q6UXT8) is the paralog subfamily SF1.
No ProtNLM2 files were opened.

### Deep research

`just deep-research-falcon human ALKAL2 --fallback perplexity-lite` failed:
falcon exited with "Exception: Failed to authenticate", and the perplexity-lite
fallback returned HTTP 401 insufficient_quota. There is
no deep-research file, so the review rests on the primary literature cached in
`publications/`. Full text was available for PMID:26418745, PMID:30061385,
PMID:34646012, PMID:34819673 and PMID:33411331, and only the abstract for
PMID:26630010 and PMID:25331893.

### What is experimentally established for human ALKAL2

- Binds the ALK extracellular domain and activates ALK
  [PMID:26418745 "FAM150A and FAM150B bind to the ECD of ALK and, in addition to activation of wild-type ALK, are able to drive ‘superactivation’ of activated ALK mutants from neuroblastoma."].
- Binds and activates both ALK and LTK. ALKAL1 prefers LTK
  [PMID:26630010 "AUG-α binds and robustly activates both ALK and LTK"].
- Purified full-length protein and the augmentor-domain fragment are equally active
  [PMID:30061385 "full-length AUG-α and the AUG-α AD deletion mutant stimulate similar tyrosine phosphorylation of cells expressing either ALK or LTK."].
- Cys66 forms an interchain disulfide. It is primate-specific, which matters for
  transfer to equids. One study proposes that ALKAL2 activates ALK as a dimer
  (PMID:34819673) and another that it acts as a monomer (PMID:34646012); UniProt
  records this as a CAUTION.
- After binding ALK, ALKAL2 contacts the membrane through its alpha1 helix, and
  this is needed for ALK activation
  [PMID:34819673 "Our data provide strong evidence for the key role of the ALKAL2 α1 helix in ALK activation, presumably by anchoring ALKAL2 to the membrane."].
- Downstream readouts measured in heterologous cell lines (PC12, NB1, L6,
  NIH/3T3, Ba/F3): pERK1/2, pERK5, neurite outgrowth and proliferation.
- In a mouse model, ALKAL2 overexpression potentiates MYCN-driven neuroblastoma
  (PMID:33411331). This is a disease phenotype and is not used for any process
  annotation.

### Key curation decisions

- GO:0030298 "receptor signaling protein tyrosine kinase activator activity"
  becomes GO:0030297 "transmembrane receptor protein tyrosine kinase activator
  activity" (MODIFY on all 6 rows). The two terms are siblings under
  GO:0030296. The "receptor signaling protein tyrosine kinase activity" wording
  is an exact synonym of obsolete GO:0004716 "signal transducer, downstream of
  receptor, with protein tyrosine kinase activity", which covers cytoplasmic
  kinases. ALK and LTK are transmembrane RTKs, so GO:0030297 is the correct term;
  it is what EGF and VEGFA use in this repository. Checked with runoak against
  the local go.db.
- The bare protein-binding row (IPI with ALK) becomes GO:0030971 receptor
  tyrosine kinase binding (MODIFY).
- Extracellular region is accepted on all rows. GO:0005615 extracellular space is
  obsolete in the current local GO (runoak reports "obsolete extracellular
  space"), so extracellular region is the most specific extracellular term left.
- Plasma membrane becomes GO:0009897 external side of plasma membrane (MODIFY).
  ALKAL2's membrane association is peripheral, extracellular-facing and
  receptor-dependent.
- ERK1/2, ERK5 and neurite outgrowth regulation are KEEP_AS_NON_CORE: each is an
  indirect outcome measured downstream of ALK.
- IBA rows from PTN002010604 cover both ALKAL subfamilies. The node placement is
  sound because both human paralogs have experimental ligand activity.
- No NEW terms. Protein homodimerization was left out because the two structural
  studies disagree, and energy expenditure/body weight was left out because it is
  an organismal phenotype of the mouse knockout and receptor.

### Transfer guidance for orthologs (e.g. donkey/horse SF2 members)

These can be transferred within SF2: ALK/LTK ligand activity, cytokine activity,
RTK binding, extracellular location and RTK signaling. Do not transfer the
Cys66-dependent dimerization: Cys66 is primate-specific (PMID:30061385).
