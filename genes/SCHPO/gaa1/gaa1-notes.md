# gaa1 curation notes

## GO-GPT cysteine endopeptidase prediction, 2026-10-10

The BioReason/GO-GPT leaf output proposed `GO:0004197` cysteine-type endopeptidase activity for `gaa1`. A focused OpenScientist report refutes this as a subunit-level transfer: the GPI transamidase complex contains cysteine-protease chemistry, but the catalytic activity resides in Gpi8/PIG-K rather than the noncatalytic Gaa1 subunit. [file:SCHPO/gaa1/gaa1-hypotheses/prediction-cysteine-endopeptidase/openscientist.md, "the catalytic cysteine-protease/transamidase activity belongs to Gpi8/PIG-K."]

The new prediction review therefore marks `GO:0004197` as `NPI` with `COMPLEX_ACTIVITY_TRANSFER`. The existing GOA review is left unchanged: it already treats Gaa1 as a structural/substrate-positioning GPI-transamidase complex subunit and notes the whole-complex convention around `GO:0003923`.
