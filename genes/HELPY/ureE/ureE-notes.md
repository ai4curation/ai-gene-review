# ureE (Q09064, H. pylori 26695) - curation notes

Deep research: not available. `just deep-research HELPY ureG --provider perplexity` was run
once (2026-10-23) and failed - only `falcon` and `openscientist` providers are configured. No
`-deep-research-*.md` file was created; the notes below rest on cached publications fetched
with `just fetch-pmid` plus the UniProt record.

## Role in the pathway

UreE is the nickel metallochaperone that stands between cellular nickel trafficking and
urease activation:

- Binds one Ni(2+) per dimer, Kd 0.15 uM; also a distinct Zn(2+) site, Kd 0.49 uM
  [PMID:19476442 "ITC (isothermal titration calorimetry) showed that HpUreE binds one
  equivalent of Ni(2+) (Kd=0.15 microM) or Zn(2+) (Kd=0.49 microM) per dimer"].
- Receives nickel from HypA and hands it to UreG via the 2E-2G complex, which also
  pre-loads GTP onto UreG [PMID:25752610 "the formation of 2E-2G complex not only facilitates
  nickel transfer from UreE to UreG, but also enhances the binding of GTP"; "UreE serves as a
  bridge to grasp Ni(2+) from HypA, subsequently donating it to UreG"].
- Nickel-charged UreE is the sufficient nickel source for in vitro urease activation, and
  apo-UreE is inactive [PMID:29203664 "The nickel-charged UreE dimer, providing the sole
  source of nickel, and the UreG2F2H2 complex could activate urease in vitro in the presence
  of GTP."; "adding apo-UreE 2 without the bound nickel (UreE 2 ) failed to activate urease"].

Note that `ureE` is **not** in the set of genes whose mutation abolished urease in the E. coli
reconstitution [PMID:1313413], and stepwise addition of ureE to ureFGH increases activity
rather than being all-or-none [PMID:16404152]; this is consistent with cytoplasmic nickel being
able to reach UreG inefficiently without a chaperone, not with UreE being dispensable in vivo.

## Decisions

- Both bare `GO:0005515` rows (partner UreG): MODIFY to `GO:0170061 nickel chaperone activity`
  (def. "Directly binding to and delivering nickel ions to a target protein") - the one case
  in this module where an interaction row has a precisely characterized molecular meaning.
- `GO:0016151`: ACCEPT (core, measured directly on the H. pylori protein).
- `GO:0006457 protein folding`: MODIFY to `GO:0051604 protein maturation`. UreE does not fold
  anything; urease folds and assembles without accessory proteins [PMID:1612735]. The
  precise child `GO:0110147 protein maturation by nickel ion transfer` is **obsolete**
  (checked in the local GO build), so the parent is the available term.
- `GO:0065003 protein-containing complex assembly`: MODIFY to `GO:0051604` for the same
  reason - urease oligomer assembly is accessory-independent.
- `GO:0019627 urea metabolic process`: MODIFY to `GO:0043419 urea catabolic process`.
