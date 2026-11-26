# ADPRH: sequence-only language-model read

**Not literature evidence.** A general frontier language model was given only the amino-acid sequence and asked the FEAT and PSEUDO questions of the fable-sequence-to-function study (https://github.com/ai4curation/fable-sequence-to-function). Use it to flag or corroborate, never as the sole support for an annotation.

Caveats:

- This is a language model reading the sequence with no tools, alignment or database; it is not literature and not a curated record.
- Its errors are stated as confidently as its correct calls; every position it names is checked below against the sequence and UniProt.
- For a well-studied protein the answer may be recall of the entry rather than a reading of the residues; the shuffled and decoy controls test the reading.
- A lost catalytic residue suggests, but does not prove, loss of activity: catalytic residues can be displaced, and dead enzymes often have non-catalytic functions.
- Intact catalytic motifs do not guarantee detectable activity.
- In the fs2f benchmark Fable 5.2 named the exact Pfam family for 8 of 15 obscure DUF proteins and Opus 5.5 for 3, so an empty or wrong domain list for a DUF protein is expected, not informative.

Probe verdicts: TRACKS_CATALYTIC_RESIDUE means the catalytic mutant was called inactive and the decoy active; REPORTS_BUT_NOT_INACTIVE means the model named the substituted position but still did not call the mutant inactive (the fs2f pattern of seeing a loss and arguing around it); REJECTS_ANY_CHANGE means the decoy also changed the call, so the read is not residue-specific; INSENSITIVE means neither changed it.

## claude-fable-5-2 (effort high), 2026-11-25, isolated read via the claude CLI

- Sequence: UniProtKB:P54922 sequence version 1, 357 aa, CRC64 4E23B12FAE84F12B.
- Route: claude CLI 2.1.325 (Claude Code), flags: --system-prompt '' --tools '' --output-format json --setting-sources '' --strict-mcp-config --disable-slash-commands --no-chrome.
- Prompts: FEAT and PSEUDO prompts of https://github.com/ai4curation/fable-sequence-to-function @ 442bd92, verbatim.

- The claude tool's usage record lists a second model, claude-haiku-5-5, on 5 of 5 calls. In 5 of them the reply is one turn whose token counts are those of claude-fable-5-2, so the second model's request was a side call by the tool; the record cannot show what it was for.

### Domains and membrane features (FEAT prompt)

- Model protein name: ADP-ribosylarginine hydrolase (ADPRH, ARH1).
- Model function: Cytosolic enzyme that removes mono-ADP-ribose from ADP-ribosylated arginine residues of proteins, releasing ADP-ribose and regenerating free arginine, thereby reversing arginine-specific mono-ADP-ribosylation.
- Model EC number: 3.2.2.19.
- Predicted Pfam PF03747 (ADP_ribosyl_GH) at 6-330: MATCH against InterPro API, boundary IoU 0.94.
- Transmembrane helices: 0 predicted, 0 in UniProt, 0 of 0 UniProt helices overlapped by a prediction.
- Signal peptide: predicted False, UniProt False.

### Shuffled-sequence control

- Shuffled sequence: 0 Pfam domains and 0 transmembrane helices predicted; control passes (no domain assigned to the shuffled sequence).

### Catalytic residues (PSEUDO prompt)

- Model enzyme family: ADP-ribosylglycohydrolase (ARH) family; Mg2+-dependent ADP-ribosyl-arginine hydrolase; catalytically active: yes; EC 3.2.2.19.
- Model reason: The 357-residue sequence matches ADP-ribosylarginine hydrolase ARH1 as recalled from memory (not checked against a database), and it retains the essential vicinal aspartates D55/D56 in the SDD motif and the second Mg2+-binding motif D302/D304/S305 (GDSDS). With no substitution at any canonical catalytic or metal-binding position, it is predicted to be an active hydrolase of N(omega)-ADP-ribosyl-arginine.
- Named catalytic residue S54 (Mg2+ coordination (site 1)): present in the sequence, UniProt BINDING.
- Named catalytic residue D55 (Catalytic acidic residue / Mg2+ coordination (site 1), essential vicinal aspartate): present in the sequence, UniProt BINDING.
- Named catalytic residue D56 (Catalytic acidic residue / Mg2+ coordination (site 1), essential vicinal aspartate): present in the sequence, UniProt BINDING.
- Named catalytic residue D302 (Mg2+ coordination (site 2)): present in the sequence, UniProt BINDING.
- Named catalytic residue D304 (Mg2+ coordination (site 2)): present in the sequence, UniProt BINDING.
- Named catalytic residue S305 (Mg2+ coordination (site 2)): present in the sequence, UniProt BINDING.
- Reported lost catalytic or cofactor residues: none.

### Catalytic-substitution and decoy probe

- Catalytic substitution D55A (residue named by the model (no UniProt ACT_SITE)): called active no; position reported as lost: True.
- Decoy substitution D255A (drawn from 13 unannotated same-type residues): called active yes; position reported as lost: False.
- Probe verdict: TRACKS_CATALYTIC_RESIDUE (wild type called active yes).
