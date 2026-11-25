# C7orf25: sequence-only language-model read

**Not literature evidence.** A general frontier language model was given only the amino-acid sequence and asked the FEAT and PSEUDO questions of the fable-sequence-to-function study (https://github.com/ai4curation/fable-sequence-to-function). Use it to flag or corroborate, never as the sole support for an annotation.

Caveats:

- This is a language model reading the sequence with no tools, alignment or database; it is not literature and not a curated record.
- Its errors are stated as confidently as its correct calls; every position it names is checked below against the sequence and UniProt.
- For a well-studied protein the answer may be recall of the entry rather than a reading of the residues; the shuffled and decoy controls test the reading.
- A lost catalytic residue suggests, but does not prove, loss of activity: catalytic residues can be displaced, and dead enzymes often have non-catalytic functions.
- Intact catalytic motifs do not guarantee detectable activity.
- In the fs2f benchmark Fable 5.2 named the exact Pfam family for 8 of 15 obscure DUF proteins and Opus 5.5 for 3, so an empty or wrong domain list for a DUF protein is expected, not informative.

Probe verdicts: TRACKS_CATALYTIC_RESIDUE means the call changed for the catalytic substitution and not for the decoy; REJECTS_ANY_CHANGE means the decoy also changed the call, so the read is not residue-specific; INSENSITIVE means neither changed it.

## claude-fable-5-2 (effort high), 2026-11-25

- Sequence: UniProtKB:Q9BPX7 sequence version 1, 421 aa, CRC64 D7C421DC4CA80E9C.
- Route: claude CLI 2.1.325 (Claude Code), flags: '--system-prompt  --tools  --output-format json --setting-sources  --strict-mcp-config --disable-slash-commands --no-chrome'.
- Prompts: FEAT and PSEUDO prompts of https://github.com/ai4curation/fable-sequence-to-function @ 442bd92, verbatim.

- The claude tool's usage record lists a second model, claude-haiku-5-5, on 3 of 3 calls. In 3 of them the reply is one turn whose token counts are those of claude-fable-5-2, so the second model's request was a side call by the tool; the record cannot show what it was for.
### Domains and membrane features (FEAT prompt)

- Model protein name: UPF0415 protein C7orf25 homolog.
- Model function: Uncharacterized protein of the UPF0415 family with no experimentally established molecular function; predicted to be soluble and non-secreted.
- Model EC number: None.
- Predicted Pfam PF18474 (DUF5614) at 6-218: MATCH against InterPro API, boundary IoU 0.97.
- Predicted Pfam PF07000 (DUF1308) at 232-395: MATCH against InterPro API, boundary IoU 0.83.
- Transmembrane helices: 0 predicted, 0 in UniProt, 0 of 0 UniProt helices overlapped by a prediction.
- Signal peptide: predicted False, UniProt False.

### Shuffled-sequence control

- Shuffled sequence: 0 Pfam domains and 0 transmembrane helices predicted; control passes (no domain assigned to the shuffled sequence).

### Catalytic residues (PSEUDO prompt)

- Model enzyme family: Uncharacterized UPF0415/DUF1308 family; no established enzyme family (a possible distant link to PD-(D/E)xK nuclease-like folds is unconfirmed); catalytically active: uncertain; EC None.
- Model reason: The sequence appears to be an uncharacterized protein of unknown function with no experimentally defined catalytic activity or active-site residues. I could not confidently assign a canonical catalytic motif from the sequence alone, so activity can be neither asserted nor excluded.
- Reported lost catalytic or cofactor residues: none.

### Catalytic-substitution and decoy probe

- Probe not run: wild type not called active, so a substitution cannot change the call.
