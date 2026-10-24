# ureF curation notes

## 2026-08-11

- Q88J01 is reviewed UniProt UreF/PP_2848 and belongs to `PTHR33620:SF1`.
- UreF joins the UreD-bound apoprotein and recruits UreG. Mutational analysis
  supports a checkpoint role rather than a simple generic chaperone function
  [PMID:22369361, "UreF gates the GTPase activity of UreG to enhance the
  fidelity of urease metallocenter assembly"].
- Nickel binding remains `UNDECIDED`. Current UniRule transfer is not backed by
  a direct Q88J01 assay, whereas PMID:22369361 directly supports UreG recruitment
  and GTPase gating in the orthologous system.
- The first OpenScientist submission was rejected before execution with HTTP
  429 and is being retried with the full provider timeout.

## 2026-08-12

- Final review removes the unsupported nickel-binding transfer and records
  UreG GTPase regulation as the defining orthology-supported function.
