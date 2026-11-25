# ADPRHL1: sequence-only language-model read

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

- Sequence: UniProtKB:Q8NDY3 sequence version 1, 354 aa, CRC64 B880003EB955EB78.
- Route: claude CLI 2.1.325 (Claude Code), flags: '--system-prompt  --tools  --output-format json --setting-sources  --strict-mcp-config --disable-slash-commands --no-chrome'.
- Prompts: FEAT and PSEUDO prompts of https://github.com/ai4curation/fable-sequence-to-function @ 442bd92, verbatim.

- The claude tool's usage record lists a second model, claude-haiku-5-5, on 3 of 3 calls. In 3 of them the reply is one turn whose token counts are those of claude-fable-5-2, so the second model's request was a side call by the tool; the record cannot show what it was for.
### Domains and membrane features (FEAT prompt)

- Model protein name: [Protein ADP-ribosylarginine] hydrolase-like protein 1 (ADPRHL1).
- Model function: Member of the ADP-ribosylarginine hydrolase family that is thought to be catalytically inactive (a pseudoenzyme) and is required for myofibril assembly and cardiac chamber outgrowth in the developing heart.
- Model EC number: None.
- Predicted Pfam PF03747 (ADP_ribosyl_GH) at 7-321: MATCH against InterPro API, boundary IoU 0.9.
- Transmembrane helices: 0 predicted, 0 in UniProt, 0 of 0 UniProt helices overlapped by a prediction.
- Signal peptide: predicted False, UniProt False.

### Shuffled-sequence control

- Shuffled sequence: 0 Pfam domains and 1 transmembrane helices predicted; control passes (no domain assigned to the shuffled sequence).

### Catalytic residues (PSEUDO prompt)

- Model enzyme family: ADP-ribosylarginine hydrolase (ARH/DraG-like) family; inactive pseudoenzyme member; catalytically active: no; EC None.
- Model reason: The sequence has the ARH fold and matches ADPRHL1 (identified from recall, not a database search), but the essential vicinal Asp-Asp pair is Asp-Asn (D57-N58) and the C-terminal Mg2+-binding motif GGDSDST is degenerated to GGESAAT. Loss of these metal-coordinating acidic residues is consistent with ADPRHL1 being a pseudoenzyme without ADP-ribosylarginine hydrolase activity; the positions of the C-terminal substitutions rest on an alignment to ARH1 done from memory and are less certain than the D-to-N change at 58.
- Named catalytic residue S56 (retained Mg2+-coordinating Ser (equivalent to ARH1 Ser54)): present in the sequence, not a UniProt site.
- Named catalytic residue D57 (retained first Asp of the vicinal acidic pair (equivalent to ARH1 Asp55)): present in the sequence, not a UniProt site.
- Reported lost residue: second Asp of the vicinal Asp-Asp pair essential for catalysis and Mg2+ binding (ARH1 Asp56), expected D, found N at 58 (matches the sequence).
- Reported lost residue: C-terminal Mg2+-coordinating Asp (ARH1 GGDSDST motif, first Asp), expected D, found E at 304 (matches the sequence).
- Reported lost residue: C-terminal Mg2+-coordinating Asp (ARH1 GGDSDST motif, second Asp), expected D, found A at 306 (matches the sequence).

### Catalytic-substitution and decoy probe

- Probe not run: wild type not called active, so a substitution cannot change the call.
