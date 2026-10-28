# Is it oxaloacetate acetylhydrolase (OAH) or isocitrate lyase (ICL)?

Analysis of three TrEMBL entries that UniProt names "Isocitrate lyase (EC 4.1.3.1)"
on the strength of PROSITE-ProRule PRU10119:

- UniProtKB:A0A5M3MM75 (Coniophora puteana RWD-64-598-SS2, CONPUDRAFT_105298)
- UniProtKB:F8PSW8 (Serpula lacrymans var. lacrymans S7.3, SERLA73DRAFT_105238)
- UniProtKB:B6HR98 (Penicillium rubens Wisconsin 54-1255, Pc22g24830)

Script: `oah_vs_icl_markers.py` (fetches all sequences live from UniProt, UniParc
and RCSB; run with `uv run --with biopython python oah_vs_icl_markers.py`).
Raw output: `results.tsv`. Nothing below is hard-coded in the script except the
accessions and the reference residue positions taken from PMID:20558740.

## 1. The PROSITE signature behind the name is not diagnostic for ICL

PS00161 (ISOCITRATE_LYASE, ProRule PRU10119) is the six-residue pattern
`K-[KR]-C-G-H-[LMQR]`, whose third position PROSITE itself flags as
`active_site(?)`. It matches the catalytic-cysteine loop shared by the whole
PEP mutase/isocitrate lyase superfamily. In this run it matched, besides the
three query proteins and three characterised OAHs, also:

| protein | PS00161 match |
|---|---|
| A. niger 2,3-dimethylmalate lyase (PDB 3FA3) | `KRCGHL` |
| E. coli 2-methylisocitrate lyase PrpB (P77541) | `KRCGHR` |
| Dianthus petal death protein (Q05957) | `KKCGHM` |

So a PS00161 hit cannot distinguish isocitrate lyase from oxaloacetase,
dimethylmalate lyase or methylisocitrate lyase. The `FT ACT_SITE` that the rule
places on each query entry (186 in A0A5M3MM75, 180 in F8PSW8, 150 in B6HR98) is
exactly the cysteine of this motif, i.e. the superfamily catalytic Cys
(Cys-192 in C. parasitica OAH numbering), not an ICL-specific feature.

## 2. None of the three has an isocitrate lyase domain, and real ICLs sit beside them

True isocitrate lyases carry Pfam PF00463 (ICL) and are 428-590 residues long.
All three queries carry only PF13714 (PEP_mutase) and are 326-364 residues.
Each of the three reference proteomes contains separate, full-length PF00463
proteins (UniProt query `proteome:<id> AND xref:pfam-PF00463`):

| proteome | PF00463 proteins (length) |
|---|---|
| UP000053558 C. puteana | A0A5M3N7P6 (552), A0A5M3MQD7 (539) |
| UP000008063 S. lacrymans | F8QF23 (547), F8PZU2 (539) |
| UP000000724 P. rubens | B6HRS2 (538), B6HVG1 (590) |

The glyoxylate-cycle ICL of each organism is therefore a different gene; the
EC 4.1.3.1 on the PF13714-only entries is a second, redundant assignment.

## 3. Global identity places all three in the OAH/DMML branch, not with ICL

Percent identity (global Needleman-Wunsch, BLOSUM62, from `results.tsv`):

| query | C. parasitica OAH1 D5LIR7 | A. niger OahA (UPI00001AA410) | B. cinerea OahA Q6PNM8 | A. niger DMML 3FA3 | G. trabeum S7Q6Y6 | A. nidulans ICL P28298 | M. tuberculosis ICL P9WKK7 | E. coli MICL P77541 |
|---|---|---|---|---|---|---|---|---|
| A0A5M3MM75 | 44.1 | 43.5 | 43.7 | 51.5 | 78.8 | 31.0 | 30.3 | 33.6 |
| F8PSW8 | 44.4 | 46.9 | 44.6 | 51.9 | 82.1 | 28.2 | 29.5 | 37.1 |
| B6HR98 | 68.4 | 81.6 | 70.4 | 58.2 | 45.1 | 32.6 | 28.2 | 33.3 |

Identity to genuine isocitrate lyases is at or below the ~30% background for the
superfamily, while identity to characterised OAHs is 44-82%.

## 4. The OAH active-site machinery is complete, including the specificity serine

Chen et al. (PMID:20558740) identify the residue that distinguishes OAH from its
closest relative, 2,3-dimethylmalate lyase: OAH has Ser-308, which hydrogen-bonds
the pro-S C(2) hydroxyl of the oxaloacetate gem-diol, where DMML and
2-methylisocitrate lyase have a proline that packs against a methyl group. The
B. cinerea S260P mutant (the counterpart of Ser-308) lost 40-fold OAH activity and
gained 15-fold dimethylmalate lyase activity. Joosten et al. (PMID:17654546)
proposed the same serine as the sequence marker for OAH activity within the
superfamily.

Aligned to D5LIR7, all three queries have:

- Ser at the 308 position (DMML 3FA3 and E. coli PrpB have Pro; A. nidulans ICL has Asp)
- the Tyr-111/His-182 pair (replaced by Phe-Phe in the broad-specificity petal death protein)
- the metal ligands Asp-126, Asp-155, Asp-157, Glu-184
- the invariant gating-loop Lys-190/Arg-191 and the catalytic Cys-192
- the shared-proton Glu-259 and Asn-282

The one named residue that is not conserved is Arg-221; the ±4 windows in
`results.tsv` show the alignment there is sound and that the position is
variable across the branch (Arg in A. niger OahA, Asn in B. cinerea OahA, Gly in
DMML), so it is not a usable marker.

## 5. Per-protein conclusion

**B6HR98 (Pc22g24830) is oxaloacetate acetylhydrolase.** It is 81.6% identical to
A. niger OahA and 68-70% to the two OAHs with enzymology, carries the Ser marker,
and is the gene whose heterologous expression conferred oxalate production on
S. cerevisiae and whose deletion abolished oxalate formation in P. chrysogenum
(PMID:21549851). Its paralog B6HBX9/Pc18g05100, which did not confer oxalate
production in that experiment, is only 57.7% identical to it, so sequence
similarity within this family is not by itself sufficient - the experimental
result is what settles B6HR98.

**A0A5M3MM75 and F8PSW8 are OAH-branch lyase/hydrolase enzymes of unresolved
substrate specificity.** They are not isocitrate lyases, and the Ser marker is
present, but they are closer to A. niger DMML (51.5-51.9%) than to any
characterised OAH (43.5-46.9%), and their nearest relative in this set is the
single OAH-branch PF13714 protein of another brown-rot fungus, Gloeophyllum
trabeum (S7Q6Y6, 78.8-82.1%); each is also the only PF13714 protein in its own
reference proteome. Several active-site neighbourhoods differ from the
ascomycete OAHs (e.g. Thr-113 to Ser, and the Glu-259 window `VCFIEGVKT` against
`VGLLEGFRS`). No basidiomycete OAH has been characterised at the protein level,
so "oxaloacetase candidate" is as far as sequence takes these two; assigning
EC 3.7.1.1 would be as unsupported as the EC 4.1.3.1 now on them.
