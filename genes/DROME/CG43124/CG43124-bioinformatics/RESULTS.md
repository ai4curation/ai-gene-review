# CG43124: catalytic-site analysis of A0A0B4K7P3

CG43124 lacks two essential residues of the trypsin catalytic triad: the profile-aligned histidine is Ser69 and the aspartate is Asn112. This supports a catalytically inactive serine-protease homolog rather than a conventional serine endopeptidase.

## Sequence identity and methods

The frozen benchmark sequence is 245 residues (SHA256 `55983baacebd323c9cc94619943c15fcffe6c24c8a6d411f2a6b8cb26f8c9770`). FlyBase FBgn0262587 lists one polypeptide, CG43124-PA / FBpp0293647, with 245 residues and accession A0A0B4K7P3. Its corresponding RefSeq is NP_001247345. The current UniProt record has sequence version 1, dated 2015-04-01. The released prediction record does not contain its input sequence, so this establishes the current target identity, not an independently recovered prediction-time input.

HMMER 3.4 `hmmalign` aligns target and reference sequences to Pfam PF00089.33 (220 match states). Catalytic positions are read from the downloaded UniProt JSON feature records, not supplied as assumed residue indices. Bovine trypsin P00760 is the active positive control. Toad ovochymase-2 Q90WD8 is the actual ProtNLM phmmer donor recorded for this prediction. Its two-domain sequence is not a same-gene ortholog control; its first domain supplies an additional homologous catalytic-site mapping. `hmmsearch` independently records domain coverage.

## Direct outputs

| Reference active site | CG43124 aligned residue |
|---|---|
| P00760 His63 / Q90WD8 His90 | Ser69 |
| P00760 Asp107 / Q90WD8 Asp140 | Asn112 |
| P00760 Ser200 / Q90WD8 Ser238 | Not reliably mapped |

The target's significant profile hit spans residues 38–140 and profile states 12–116 (independent E-value 6.4e-19, domain score 56.3). Thus both mapped substitutions fall within a supported homologous segment. The trypsin control spans profile states 1–220 and residues 24–239. The target has 100 uppercase profile-aligned residues, versus 213 for P00760 and 218 for the aligned Q90WD8 domain.

The target C-terminal region aligns poorly: a second weak hit at residues 202–227 has E-value 0.14. The catalytic serine position is a gap in the profile alignment and cannot be assigned confidently from this analysis. This gap is not evidence of a literal sequence deletion. The His-to-Ser and Asp-to-Asn replacements suffice to contradict the conventional catalytic triad; no particular third-site substitution is asserted.

In the separate positive-control run, Q90WD8 His90, Asp140 and Ser238 map to P00760 His63, Asp107 and Ser200. All three active residues are recovered correctly. The preserved trypsin-like sequence architecture with loss of essential catalytic chemistry supports pseudoenzyme status; this is sequence evidence, not an experimental assay of zero proteolytic activity. It does not identify the native noncatalytic function or refute participation in a proteolytic signaling pathway.

## Reproducibility checklist

- [x] Analysis scripts read sequence/profile/reference inputs; no results or gene-specific catalytic substitutions are hardcoded.
- [x] The same script was tested with an independent target, active bovine trypsin.
- [x] Both analysis and positive control completed successfully.
- [x] Inputs, profile alignment, domain searches, JSON results and `justfile` are retained.
- [x] Provenance, alignment limitations and inference boundaries are stated above.

Sources: [Pfam Trypsin](https://www.ebi.ac.uk/interpro/entry/pfam/PF00089/), [UniProt P00760](https://www.uniprot.org/uniprotkb/P00760/entry), [UniProt Q90WD8](https://www.uniprot.org/uniprotkb/Q90WD8/entry), [FlyBase CG43124](https://flybase.org/reports/FBgn0262587). Retrieved 2026-09-08; exact downloaded comparator records are in `inputs/`.
