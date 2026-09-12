# Is this "uncharacterized" IS630-element protein a DDE transposase? (Foldseek fold call only)

You are an independent computational biologist. Run **one** decisive analysis and
report it concisely — do not broaden the investigation.

## Context (do not assume beyond this)

- UniProt **P16943** (*Shigella sonnei*, 343 aa), UniProt-named "Insertion element
  IS630 **uncharacterized** 39 kDa protein"; NCBIFAM family **NF033545** =
  "IS630 family transposase" (equivalog). Curator assigned no activity.
- Many DNA transposases adopt the **RNase H-like (retroviral integrase / DDE)
  fold** with a catalytic **DDE (Asp-Asp-Glu)** metal-binding triad.

## Representative sequence (UniProt P16943, 343 aa)

```
MPIIAPISRDERRLMQKAIHKTHDKNYARRLTAMLMLHRGDRVSDVARTLCCARSSVGRWINWFTQSGVEGLKSLPAGRARRWPFEHICTLLRELVKHSPGDFGYQRSRWSTELLAIKINEITGCQLNAGTVRRWLPSAGIVWRRAAPTLRIRDPHKDEKMAAIHKALDECSAEHPVFYEDEVDIHLNPKIGADWQLRGQQKRVVTPGQNEKYYLAGALHSGTGKVSCVGGNSKSSALFISLLKRLKATYRRAKTITLIVDNYIIHKSRETQSWLKENPKFRVIYQPVYSPWVNHVERLWQALHDTITRNHQCSSMWQLLKKVRHFMETVSPFPGGKHGLAKV
```

## The single decisive analysis

Fetch the AlphaFold model (AF-P16943-F1) and run **Foldseek** against PDB100 /
AFDB-SwissProt. Report ONLY:
1. the top structural homologs and whether the catalytic core is the **RNase
   H-like / DDE transposase-integrase fold** (with confidence);
2. whether a candidate **DDE (D,D,E) catalytic triad** is present/intact; and
3. a one-line verdict: is "**transposase activity (GO:0004803)**" structurally
   supported for P16943?

Do not run disorder, targeting, phylogeny, or literature surveys. One structural
analysis, one clear verdict, one confirmatory experiment.
