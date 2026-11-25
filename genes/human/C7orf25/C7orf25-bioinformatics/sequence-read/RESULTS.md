# C7orf25: sequence-only language-model read

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

- Sequence: UniProtKB:Q9BPX7 sequence version 1, 421 aa, CRC64 D7C421DC4CA80E9C.
- Route: claude CLI 2.1.325 (Claude Code), flags: --system-prompt '' --tools '' --output-format json --setting-sources '' --strict-mcp-config --disable-slash-commands --no-chrome.
- Prompts: FEAT and PSEUDO prompts of https://github.com/ai4curation/fable-sequence-to-function @ 442bd92, verbatim.

- The claude tool's usage record lists a second model, claude-haiku-5-5, on 3 of 3 calls. In 3 of them the reply is one turn whose token counts are those of claude-fable-5-2, so the second model's request was a side call by the tool; the record cannot show what it was for.

### Domains and membrane features (FEAT prompt)

- Model protein name: UPF0415 protein C7orf25 (human C7orf25 or close mammalian ortholog).
- Model function: Uncharacterized conserved eukaryotic protein of the UPF0415 family with no experimentally established molecular function; it appears to be a soluble intracellular protein.
- Model EC number: None.
- Predicted Pfam PF18474 (DUF5614) at 5-235: MATCH against InterPro API, boundary IoU 0.91.
- Predicted Pfam PF07000 (DUF1308) at 250-410: MATCH against InterPro API, boundary IoU 0.98.
- Transmembrane helices: 0 predicted, 0 in UniProt, 0 of 0 UniProt helices overlapped by a prediction.
- Signal peptide: predicted False, UniProt False.

### Shuffled-sequence control

- Shuffled sequence: 0 Pfam domains and 0 transmembrane helices predicted; control passes (no domain assigned to the shuffled sequence).

### Catalytic residues (PSEUDO prompt)

- Model enzyme family: None assignable; UPF0415 / DUF1308 family of unknown function, not a recognised enzyme family; catalytically active: uncertain; EC None.
- Model reason: The sequence appears to be the uncharacterized UPF0415 (DUF1308) protein C7orf25, which has no established enzymatic activity, and I see no recognisable catalytic motif or cofactor-binding signature in it. With no canonical active-site template to compare against, activity can be neither confirmed nor excluded from sequence alone, though nothing here positively supports it.
- Reported lost catalytic or cofactor residues: none.

### Catalytic-substitution and decoy probe

- Probe not run: wild type not called active, so a substitution cannot change the call.
