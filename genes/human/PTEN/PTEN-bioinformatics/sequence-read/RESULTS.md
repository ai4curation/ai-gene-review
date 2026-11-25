# PTEN: sequence-only language-model read

**Not literature evidence.** A general frontier language model was given only the amino-acid sequence and asked the FEAT and PSEUDO questions of the fable-sequence-to-function study (https://github.com/ai4curation/fable-sequence-to-function). Use it to flag or corroborate, never as the sole support for an annotation.

Caveats:

- This is a language model reading the sequence with no tools, alignment or database; it is not literature and not a curated record.
- Its errors are stated as confidently as its correct calls; every position it names is checked below against the sequence and UniProt.
- For a well-studied protein the answer may be recall of the entry rather than a reading of the residues; the shuffled and decoy controls test the reading.
- A lost catalytic residue suggests, but does not prove, loss of activity: catalytic residues can be displaced, and dead enzymes often have non-catalytic functions.
- Intact catalytic motifs do not guarantee detectable activity.
- In the fs2f benchmark Fable 5.2 named the exact Pfam family for 8 of 15 obscure DUF proteins and Opus 5.5 for 3, so an empty or wrong domain list for a DUF protein is expected, not informative.

Probe verdicts: TRACKS_CATALYTIC_RESIDUE means the catalytic mutant was called inactive and the decoy active; REPORTS_BUT_NOT_INACTIVE means the model named the substituted position but still did not call the mutant inactive (the fs2f pattern of seeing a loss and arguing around it); REJECTS_ANY_CHANGE means the decoy also changed the call, so the read is not residue-specific; INSENSITIVE means neither changed it.

## claude-fable-5-2 (effort high), 2026-11-25

- Sequence: UniProtKB:P60484 sequence version 1, 403 aa, CRC64 75F97C3DD6802BA9.
- Route: claude CLI 2.1.325 (Claude Code), flags: --system-prompt '' --tools '' --output-format json --setting-sources '' --strict-mcp-config --disable-slash-commands --no-chrome.
- Prompts: FEAT and PSEUDO prompts of https://github.com/ai4curation/fable-sequence-to-function @ 442bd92, verbatim.

- The claude tool's usage record lists a second model, claude-haiku-5-5, on 5 of 5 calls. In 5 of them the reply is one turn whose token counts are those of claude-fable-5-2, so the second model's request was a side call by the tool; the record cannot show what it was for.

### Domains and membrane features (FEAT prompt)

- Model protein name: Phosphatidylinositol 3,4,5-trisphosphate 3-phosphatase and dual-specificity protein phosphatase PTEN.
- Model function: Tumour suppressor lipid and dual-specificity protein phosphatase that dephosphorylates the 3-position of PtdIns(3,4,5)P3, antagonising PI3K-AKT signalling to restrain cell growth, survival and migration.
- Model EC number: 3.1.3.67.
- Predicted Pfam PF22785 (Tc-R-P) at 42-180: IN_UNIPROT_NOT_INTERPRO against InterPro API.
- Predicted Pfam PF10409 (PTEN_C2) at 188-349: MATCH against InterPro API, boundary IoU 0.99.
- Reference Pfam PF22784 not predicted.
- Transmembrane helices: 0 predicted, 0 in UniProt, 0 of 0 UniProt helices overlapped by a prediction.
- Signal peptide: predicted False, UniProt False.

### Shuffled-sequence control

- Shuffled sequence: 0 Pfam domains and 0 transmembrane helices predicted; control passes (no domain assigned to the shuffled sequence).

### Catalytic residues (PSEUDO prompt)

- Model enzyme family: Protein tyrosine phosphatase superfamily (Cys-based CX5R phosphatases), PTEN/tensin-type lipid and dual-specificity phosphatase subfamily; catalytically active: yes; EC 3.1.3.67.
- Model reason: The sequence appears to be full-length wild-type human PTEN (403 aa) with an intact P-loop signature HCKAGKGRTG (residues 123-132), including nucleophile Cys124, Arg130 and Gly129, plus the general acid Asp92 and an intact C2 domain. None of the classic inactivating substitutions (C124S, G129E, R130 variants, D92A) is present, so it is predicted to be an active PIP3 3-phosphatase, with additional dual-specificity protein phosphatase activity (EC 3.1.3.16/3.1.3.48).
- Named catalytic residue D92 (general acid/base (WPD-loop equivalent)): present in the sequence, not a UniProt site.
- Named catalytic residue C124 (catalytic nucleophile (forms phosphocysteine intermediate, P-loop HCxxGxxR)): present in the sequence, UniProt ACT_SITE.
- Named catalytic residue R130 (phosphate binding / transition-state stabilisation (P-loop arginine)): present in the sequence, not a UniProt site.
- Named catalytic residue G129 (P-loop glycine required for PIP3 lipid substrate accommodation): present in the sequence, not a UniProt site.
- Reported lost catalytic or cofactor residues: none.

### Catalytic-substitution and decoy probe

- Catalytic substitution C124A (UniProt ACT_SITE): called active no; position reported as lost: True.
- Decoy substitution C83A (drawn from 4 unannotated same-type residues): called active yes; position reported as lost: False.
- Probe verdict: TRACKS_CATALYTIC_RESIDUE (wild type called active yes).
