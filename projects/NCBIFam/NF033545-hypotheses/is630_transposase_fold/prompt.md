# Hypothesis: is this "uncharacterized" insertion-element protein a DDE transposase?

You are an independent computational biologist. Decide whether an
"uncharacterized" protein encoded by a bacterial insertion sequence is a
**transposase**, and if so of what mechanistic class.

## What is known (do not assume beyond this)

- NCBI Protein Family **NF033545** (NCBIFAM/PGAP), an *equivalog*, product name
  "**IS630 family transposase**".
- This representative, UniProt **P16943** (*Shigella sonnei*, 343 aa), is
  UniProt-named "**Insertion element IS630 uncharacterized 39 kDa protein**" — the
  curator did **not** assign transposase activity; it is formally uncharacterized.
- Many DNA transposases are **DDE/DDD-motif** enzymes with an **RNase H-like
  (retroviral integrase) fold** and a catalytic acidic triad that coordinates the
  divalent metals for strand transfer.

## Representative sequence

UniProt **P16943**, 343 aa:

```
MPIIAPISRDERRLMQKAIHKTHDKNYARRLTAMLMLHRGDRVSDVARTLCCARSSVGRWINWFTQSGVEGLKSLPAGRARRWPFEHICTLLRELVKHSPGDFGYQRSRWSTELLAIKINEITGCQLNAGTVRRWLPSAGIVWRRAAPTLRIRDPHKDEKMAAIHKALDECSAEHPVFYEDEVDIHLNPKIGADWQLRGQQKRVVTPGQNEKYYLAGALHSGTGKVSCVGGNSKSSALFISLLKRLKATYRRAKTITLIVDNYIIHKSRETQSWLKENPKFRVIYQPVYSPWVNHVERLWQALHDTITRNHQCSSMWQLLKKVRHFMETVSPFPGGKHGLAKV
```

## The decisive question (scope your work to this)

**Is P16943 a catalytically competent DDE-type transposase?** Answer by:
1. Foldseek fold assignment of the AlphaFold model — does the core adopt the
   **RNase H-like / DDE transposase-integrase fold**, and what are the closest
   experimentally characterized structural homologs?
2. Identify the candidate **DDE (Asp-Asp-Glu) catalytic triad** and state whether
   it is present/intact.
3. State whether assigning "**transposase activity (GO:0004803)**" to this protein
   is **supported** by structure, and name the mechanistic class (DDE cut-and-
   paste, etc.).

Keep other analyses light. Give one clear conclusion with confidence and the one
experiment that would confirm it.
