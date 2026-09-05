# Tac1 (HETGA, A0A0P6JY17): where are the processed tachykinin peptides?

## Why this analysis

The naked mole-rat is routinely described as "naturally lacking substance P". That
phrasing invites the inference that something is wrong with the peptide or the gene
that encodes it. The TrEMBL entry `A0A0P6JY17` cannot settle the question on its own:
it carries **no `PEPTIDE` features at all**, only `SIGNAL 1..19`, `CHAIN 20..130`, and
two SMART `Tachykinin` domain calls at `58..68` and `97..107`. So the record never
states whether substance P is in this sequence, let alone whether it is intact.

This analysis asks a narrow, checkable question: **does the naked mole-rat precursor
encode substance P and neurokinin A, and are the processing signals that release them
intact?**

## Method

`peptide_boundaries.py` (stdlib only) reads the two UniProt flat files, compares the
sequences, transfers the reviewed human `PEPTIDE` coordinates from `P20366`
(TKN1_HUMAN, isoform Beta = displayed sequence), and independently checks each
transferred peptide against the tachykinin C-terminal consensus named in the GO
definition of `GO:0007217` (`Phe-X-Gly-Leu-Met-NH2`), plus the Gly amide donor and
dibasic cleavage site that must follow it.

```
uv run --no-project python peptide_boundaries.py
```

The human record is fetched from `https://rest.uniprot.org/uniprotkb/P20366.txt` and
cached alongside the script. `output.txt` is the verbatim run output.

## Results

The two precursors are the same length bar one residue, so the comparison is gap-free
and exact — no alignment heuristic is involved:

```
naked mole-rat A0A0P6JY17: 130 aa
human         P20366    : 129 aa  (isoform Beta, displayed)

ungapped identity over 1..129: 125/129 = 96.9%
substitutions (human->NMR): A6V, Y35S, D72E, S120N
NMR C-terminal extension: 'K' at 130..130
```

Human `PEPTIDE` coordinates transferred to the naked mole-rat precursor:

| peptide | coords | human | naked mole-rat | identical? |
|---|---|---|---|---|
| Substance P | 58..68 | `RPKPQQFFGLM` | `RPKPQQFFGLM` | **yes** |
| Neuropeptide K | 72..107 | `DADSSIEKQVALLKALYGHGQISHKRHKTDSFVGLM` | `EADSSIEKQVALLKALYGHGQISHKRHKTDSFVGLM` | no (D72E) |
| Neuropeptide gamma, 1st part | 72..73 | `DA` | `EA` | no (D72E) |
| Neuropeptide gamma, 2nd part | 89..107 | `GHGQISHKRHKTDSFVGLM` | `GHGQISHKRHKTDSFVGLM` | **yes** |
| Neurokinin A | 98..107 | `HKTDSFVGLM` | `HKTDSFVGLM` | **yes** |
| C-terminal-flanking peptide | 111..126 | `ALNSVAYERSAMQNYE` | `ALNSVAYERNAMQNYE` | no (S120N) |

Processing-signal check, run directly on the naked mole-rat sequence and independent
of the coordinate transfer:

```
  ...FFGLM ends at 68; next 3 residues = 'GKR' (G + dibasic OK)
  ...FVGLM ends at 107; next 3 residues = 'GKR' (G + dibasic OK)
```

## Interpretation

1. **Substance P is present, and it is the same molecule as human substance P.**
   `RPKPQQFFGLM` occupies exactly positions 58-68, the same coordinates as in the
   reviewed human entry, with zero substitutions.

2. **Neurokinin A is also present and also identical** (`HKTDSFVGLM`, 98-107). The
   naked mole-rat precursor therefore encodes *both* mature tachykinins, i.e. it has
   the beta-preprotachykinin architecture, not the alpha form (which encodes substance
   P only). All four differences from human (A6V, Y35S, D72E, S120N) fall outside
   substance P and neurokinin A; only D72E and S120N touch a mature product at all, and
   both are in the N-terminal extension of neuropeptide K or in the C-terminal flanking
   peptide.

3. **The machinery that releases the peptides is intact.** Both tachykinin cores end in
   the `F-x-G-L-M` consensus that the `GO:0007217` definition uses to define a
   tachykinin, and both are immediately followed by `G-K-R`: the glycine that donates
   the C-terminal amide (`-Met-NH2`, required for neurokinin-receptor potency) and the
   dibasic `KR` prohormone-convertase site. There is no lesion in the processing path.

4. **Therefore "the naked mole-rat lacks substance P" cannot be a statement about this
   protein.** The gene is present, the peptide it encodes is human-identical, and the
   amidation and cleavage signals are conserved. The published finding is about *where
   the peptide is made* — it is absent from cutaneous C-fibre nociceptors — not about
   what the protein is or does.

## Limits of this analysis

- Sequence conservation of a processing site is not proof that the site is used
  *in vivo* in the naked mole-rat. No mass-spectrometric or radioimmunoassay
  quantification of mature naked mole-rat substance P was found in the cached
  literature; the peptide has only ever been assayed immunohistochemically.
- No naked mole-rat study in the cached literature examines neurokinin A or the
  neurokinin-2 receptor at all; every naked mole-rat observation of this gene's products
  concerns substance P and NK1R. The neurokinin A arm is therefore sequence-inference
  only for this species.
- The three RefSeq proteins cross-referenced by the entry (`XP_004862783.1`,
  `XP_021098523.1`, `XP_021098524.1`) all carry this one sequence, and the entry
  declares no `ALTERNATIVE PRODUCTS`. Which of the alpha/beta/gamma/delta splice forms
  the naked mole-rat actually transcribes, and in what tissue proportions, is
  **not established** by this record and is not addressed here.
- The one-residue length difference (an extra C-terminal Lys) is taken at face value
  from the automatic RefSeq-derived model; it is downstream of every mature peptide and
  is not interpreted.
