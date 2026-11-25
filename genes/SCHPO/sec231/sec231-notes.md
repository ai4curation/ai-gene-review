# sec231 review notes

## Setup

- The GO-CAM labels `PomBase:SPCC31H12.07` as `sec2301`, but the current UniProt and PomBase symbol for `SPCC31H12.07` is `sec231`.
- `just fetch-gene SCHPO sec2301` failed because `sec2301` is not a current S. pombe UniProt gene name.
- `just fetch-gene SCHPO sec231` created the review stub, GOA seed, and UniProt cache.
- `just fetch-gene-pmids SCHPO sec231` found all cited PMIDs already present.
- `just mod-description-deep-research SCHPO sec231` skipped because `SCHPO` has no configured model-organism-description provider.
- `just deep-research-falcon SCHPO sec231 --fallback perplexity-lite` could not run: the local wrapper reported that `falcon` was unavailable, and the fallback reported that `perplexity` was unavailable.
- PAINT lineage-loss check: no IRD or IKR loss on the `sec231` lineage.

## Literature and database evidence

- The cached S. pombe `sec231` literature is sparse; the UniProt record lists only the genome paper and marks the protein as inferred from homology, so direct S. pombe evidence is not enough to prove each existing row on its own.
- The protein is a full-length Sec23-family member, `O74873`, assigned by UniProt to the SEC23/SEC24 family and Sec23 subfamily [file:genes/SCHPO/sec231/sec231-uniprot.txt, "InterPro; IPR037364; Sec23."].
- Conserved COPII literature places Sec23 in the inner coat with Sec24 and Sar1: after Sar1-GTP is recruited to the ER membrane, Sec23 and Sec24 form the inner layer, and Sec13/Sec31 assemble on Sec23 to form the outer layer [PMID:27432890, "Sec13 and Sec31 proteins assemble into an outer layer on COPII-coated vesicles around the pre-budding complex through interactions with Sec23"].
- The same conserved mechanism supports Sec23 as the GAP that stimulates Sar1 GTP hydrolysis during uncoating [PMID:27432890, "Sec23 is a GTPase-activating protein (GAP) for Sar1"].
- Sec23 and Sec24 are peripheral cytosolic coat subunits rather than integral ER or Golgi proteins. The UniProt locations for the COPII vesicle membrane, ER membrane, and Golgi membrane all specify "Peripheral membrane protein" and "Cytoplasmic side" by similarity.

## GO-CAM context

Model `693b3c0900004859` enables two activities with `PomBase:SPCC31H12.07`: Sec23 molecular adaptor activity in COPII budding and Sec23 GAP activity in COPII uncoating. The core biology is right, but the model currently calls the Sar1-GTPase edge from the GAP activity `directly negatively regulates`; a GAP increases GTP hydrolysis, so the edge to the GTPase-activity node should be positive. The GO-CAM review already records this as a confirmed GO-CAM source defect.
