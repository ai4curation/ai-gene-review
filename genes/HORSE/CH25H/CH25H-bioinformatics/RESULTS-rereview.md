# CH25H horse F6T000: histidine-box conservation (re-review)

Human O95992 (272 aa) vs horse F6T000 (270 aa); global alignment identity 83.33% over 270 paired residues.

## Human UniProt histidine-box MOTIF features mapped to horse

- Histidine box-1: human 142-146 WHLLH -> horse 142-146 WHVLH; all histidines conserved: True
- Histidine box-2: human 157-161 HKVHH -> horse 157-161 HKMHH; all histidines conserved: True
- Histidine box-3: human 238-244 HHDLHHS -> horse 238-244 HHDLHHS; all histidines conserved: True

## Horse regex scan for HX2HH boxes (1-based start, motif)

143 HVLHH, 157 HKMHH, 239 HDLHH

Interpretation: conservation of every histidine in the three boxes is consistent with an intact diiron site, as required for catalysis in the human/mouse enzymes; it is not an assay of horse activity.

Reproduce with `uv run python genes/HORSE/CH25H/CH25H-bioinformatics/hisbox_rereview.py`.
