# Is human AK4P3 an over-annotated pseudogene, or a functional AK4 duplicate?

Run 2026-09-26. Script: `analyze_ak4p3.py` (no dependencies; sequences fetched live from the
UniProt REST API, comparison and digest computed — nothing hardcoded). Raw output:
`run-output.txt`.

## Why this was asked

AK4P3 carries **19 GO annotations** describing a working mitochondrial adenylate kinase — AMP
kinase activity, nucleoside triphosphate adenylate kinase activity, mitochondrial matrix, ATP/GTP
metabolic process. Every one is IEA or IBA, applied by automatic pipelines (chiefly HAMAP-Rule
MF_03170) on similarity to AK4.

But **HGNC names the locus "adenylate kinase 4 pseudogene 3", `locus_type: pseudogene`**. Those
cannot both be casually true.

## Result

| Test | Finding |
|---|---|
| ORF length | 223 aa — identical to AK4 (P27144) |
| Identity to AK4 | **221/223 (99.1%)** |
| Differences | **two**, both conservative: M53V and V177A |
| Catalytic P-loop (Walker A) | `GPPGSGK` at position 12 — **intact in both** |
| Tryptic peptides unique to AK4P3 (≥7 aa) | **two**: `ASTEVGEVAK`, `DAAKPVIELYK` |

## Reading

**The sequence gives no evidence of pseudogenisation at the protein level.** The ORF is intact,
full-length, and near-identical to a functional enzyme, with the catalytic P-loop conserved. So
the GO annotations are *appropriate to this sequence* — the automatic pipelines are not
misfiring on a decayed relic the way they do for, say, a frameshifted remnant.

The genuine uncertainty is one level up and outside GO's reach: **is this locus transcribed and
translated?** HGNC says pseudogene; Ensembl gives the same locus `biotype: protein_coding` while
keeping the pseudogene name; UniProt has it unreviewed (TrEMBL) at **PE=1, evidence at protein
level**, with a PeptideAtlas cross-reference.

**The PE=1 is checkable, which is the useful part.** Peptide-to-protein assignment between
99%-identical paralogs is exactly where proteomic evidence goes wrong — but here two fully tryptic
peptides *are* unique to AK4P3, and both substitutions are mass-distinguishable (M→V is −32 Da,
V→A is −28 Da). So the evidence *can* be attributed correctly. Whether it *was* depends on whether
those two peptides are the ones observed, which this analysis cannot determine.

## Limitations, stated plainly

- Two sequences, protein level only. Says nothing about the genomic context, promoter, or
  transcript structure that HGNC's pseudogene call presumably rests on.
- An intact ORF with an intact active site is not proof of catalytic activity, only absence of
  evidence against it. Nobody has assayed this protein.
- The tryptic-peptide result establishes that discrimination is *possible*, not that PeptideAtlas
  performed it. Resolving PE=1 requires looking at the observed peptide list, which is outside
  what this script does.
- Conversely, near-identity is itself compatible with a very recent duplication that is
  transcribed but not under selection — indistinguishable, at this level of analysis, from a
  functional gene.
