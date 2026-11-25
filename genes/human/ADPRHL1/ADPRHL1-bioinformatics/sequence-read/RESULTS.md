# ADPRHL1: sequence-only language-model read

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

- Sequence: UniProtKB:Q8NDY3 sequence version 1, 354 aa, CRC64 B880003EB955EB78.
- Route: claude CLI 2.1.325 (Claude Code), flags: --system-prompt '' --tools '' --output-format json --setting-sources '' --strict-mcp-config --disable-slash-commands --no-chrome.
- Prompts: FEAT and PSEUDO prompts of https://github.com/ai4curation/fable-sequence-to-function @ 442bd92, verbatim.

- The claude tool's usage record lists a second model, claude-haiku-5-5, on 3 of 3 calls. In 3 of them the reply is one turn whose token counts are those of claude-fable-5-2, so the second model's request was a side call by the tool; the record cannot show what it was for.

### Domains and membrane features (FEAT prompt)

- Model protein name: Inactive ADP-ribosyltransferase ARH2 (ADP-ribosylhydrolase-like protein 1, ADPRHL1).
- Model function: Catalytically inactive member of the ADP-ribosylarginine hydrolase family, thought to act as a pseudoenzyme required for myofibril assembly and outgrowth of the cardiac chambers in the developing heart.
- Model EC number: None.
- Predicted Pfam PF03747 (ADP_ribosyl_GH) at 7-320: MATCH against InterPro API, boundary IoU 0.9.
- Transmembrane helices: 0 predicted, 0 in UniProt, 0 of 0 UniProt helices overlapped by a prediction.
- Signal peptide: predicted False, UniProt False.

### Shuffled-sequence control

- Shuffled sequence: 0 Pfam domains and 1 transmembrane helices predicted; control passes (no domain assigned to the shuffled sequence).

### Catalytic residues (PSEUDO prompt)

- Model enzyme family: ADP-ribosylarginine hydrolase (ARH) family, ADP-ribosyl-[dinitrogen reductase] hydrolase-like fold; pseudoenzyme member; catalytically active: no; EC None.
- Model reason: The sequence matches ADPRHL1 (identified from recall of the ARH1 sequence, not a database search), which keeps the ARH fold but has SDNT in place of the SDDT di-aspartate motif and GGESAAT in place of the GGDSDST Mg2+-binding motif. With three of the four acidic metal-binding and catalytic residues substituted, it is predicted to be a catalytically inactive pseudoenzyme, consistent with its known structural role in cardiac myofibril assembly.
- Named catalytic residue D57 (retained first aspartate of the di-aspartate motif (equivalent to ARH1 Asp55); not sufficient for catalysis on its own): present in the sequence, not a UniProt site.
- Reported lost residue: second aspartate of the catalytic di-aspartate motif (ARH1 Asp56), Mg2+ coordination and catalysis, expected D, found N at 58 (matches the sequence).
- Reported lost residue: C-terminal Mg2+-binding aspartate (ARH1 Asp302), expected D, found E at 304 (matches the sequence).
- Reported lost residue: C-terminal Mg2+-binding aspartate (ARH1 Asp304), expected D, found A at 306 (matches the sequence).

### Catalytic-substitution and decoy probe

- Probe not run: wild type not called active, so a substitution cannot change the call.
