# CDK16 (blue whale A0A8B8WEF1) vs human CDK16 (Q00536)

Script: `compare_to_human.py` (run with `uv run compare_to_human.py > results.tsv`).
Sequences fetched live from UniProt REST; global alignment (BLOSUM62, gap open -10, extend -0.5).

## Results (from results.tsv)

- Whale length 496 aa; human length 496 aa; 496 alignment columns with 0 gap columns.
- 487 identical positions: 98.19% identity over the full human sequence.
- The nine differences are 21I>V, 44P>L, 47A>G, 50R>H, 53P>S, 56L>P, 59A>G, 257I>V and 476L>I (human position, human residue > whale residue).
- Seven of the nine differences lie in the N-terminal disordered region (UniProt MobiDB-lite 1..104); only 257I>V lies in the kinase domain (165..446), a conservative change.
- Residues at experimentally studied human positions are all conserved: Ser12 (BRSK2 site), Ser95 (CDK5 site), Ser119 (PKA/14-3-3 site), Ser153 (PKA site that blocks cyclin Y binding), Lys194 (ATP-binding lysine), Asp286 (HRD catalytic aspartate, UniProt ACT_SITE 286) and Asp304 (DFG).

## Interpretation

The whale protein is colinear with human CDK16 isoform 1 along its whole length, with no indels, and retains the catalytic residues and every regulatory phosphosite for which there is experimental evidence in human or rodent CDK16. Together with shared PANTHER subfamily PTHR24056:SF174 (from the UniProt record), this supports transferring the human/rodent CDK16 kinase activity, cyclin Y dependence and localisation findings. This alignment shows conservation only; it does not test any function in whale.
