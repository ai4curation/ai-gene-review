# dnajc6 (A0A8M9Q6X2) P-loop and J-domain check

Script: `ploop_check.py` (run with `uv run --no-project --with biopython python ploop_check.py`);
raw output in `ploop_check_output.txt`.

## Question

UniProt/UniRule (UR000414225) assigns "phosphoprotein phosphatase activity" and "hydrolase activity"
to zebrafish dnajc6 from its tensin-type phosphatase domain, and PROSITE-ProRule PRU00590 marks
Cys223 as a phosphocysteine intermediate. The bovine auxilin crystal structure (PMID:20826345)
showed that the auxilin PTEN-like region lacks the final arginine of the HCxxGxxR P-loop and has
no detectable phosphatase activity. Does the zebrafish protein retain the canonical motif?

## Results

- Zebrafish dnajc6 A0A8M9Q6X2 is 979 aa; human DNAJC6 O75061 is 913 aa. Global identity over
  aligned columns: 579/865 = 0.669.
- The zebrafish window at the PTP/PTEN P-loop (residues 222-230) is `TCSDGRAPS`; the canonical
  HCxxGxxR motif is NOT matched. The residue at the position of the catalytic arginine (229) is
  Pro, and the motif histidine is replaced by Thr222.
- Zebrafish Cys223 aligns to human Cys164, whose window is `HCLDGRAAS` (also lacking the final Arg,
  consistent with the bovine structure).
- The J domain HPD motif, required for Hsp70 ATPase stimulation by J-domain proteins, is present
  in zebrafish (HPD at 943-945) as in human (877-879).

## Interpretation

The zebrafish PTEN-like domain carries the same degenerate P-loop as mammalian auxilin (and in
addition loses the motif histidine), so the UniRule phosphatase assignment is a fold-based transfer
to a pseudophosphatase domain. The J-domain HPD motif is intact, consistent with conserved Hsp70
co-chaperone function. This is a sequence-only check; no phosphatase assay has been done on the
zebrafish protein.
