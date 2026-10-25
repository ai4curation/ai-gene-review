# hldE notes

## 2026-10-02 ADP-heptose module review

HldE/RfaE is the bifunctional E. coli ADP-heptose enzyme. Kneidinger et al. purified E. coli HldE and GmhB and reconstituted the pathway from sedoheptulose 7-phosphate through ADP-D-beta-D-heptose, assigning HldE's N-terminal activity to heptose 7-phosphate kinase and its C-terminal activity to heptose-1-phosphate adenylyltransferase [PMID:11751812].

The LPS-core process annotations are appropriate in E. coli. Valvano et al. found that an E. coli rfaE/hldE disruption causes a heptoseless LPS phenotype, and separable domain experiments supported a bifunctional model with Domain I required for the kinase-side function and Domain II for ADP transfer [PMID:10629197].

The homodimerization row is non-core but experimentally supported. McArthur et al. found that purified HldE1 eluted at a mass consistent with dimers and that tagged HldE constructs co-purify in vivo; ATP-binding-site mutants exerted a dominant-negative effect, supporting a functional HldE dimer [PMID:16030223].

Review decisions:

- Accept both exact MFs, `GO:0033785` and `GO:0033786`.
- Accept `GO:0097171` and `GO:0009244` for E. coli because the full HldE/GmhB/HldD route to the L,D-heptose LPS donor is present.
- Keep cytosol, ATP binding, and homodimerization as non-core.
- Mark broad catalytic and carbohydrate terms as over-annotated.

## 2026-10-25 — complete annotation and evidence audit

Applied the review and annotation-reviewer instructions to every seeded row. Source fields were preserved and a JSON comparison checked that only annotation review blocks changed. Correct broad terms were refined with MODIFY, not treated as false or excessive claims. No new process annotations were added.

Research provenance: the actual `just deep-research-falcon ECOLI hldE --fallback perplexity-lite` run was launched concurrently with publication caching. Falcon/Edison returned HTTP 403 authentication failure; the Perplexity fallback returned HTTP 401 insufficient_quota. This session-wide provider outage applies to this four-gene audit; these notes are manual primary-source research, not a provider-generated report. Existing and additional publication caches were fetched with supported commands; no publication cache was hand-edited.

`just fetch-fitness ECOLI hldE` was attempted and failed because no local FEBA data or reachable data source was available; no fitness artifact was written. PSEAE additionally lacks an organism mapping in the fetcher. No fitness phenotype is inferred from that failure.

All 21 existing rows reviewed. Both exact enzyme activities and the ADP-L,D-heptose/LPS core pathways are retained. Catalytic activity, kinase, phosphorus-transfer, alcohol phosphotransfer, nucleotidyltransferase and general carbohydrate metabolism are refined to their supported specific descendants. ATP binding, the functional homodimer and cytosolic localization are accepted as core molecular features rather than labelled peripheral merely because they differ from catalytic activity.

PMID11751812 full text reconstructs the pathway using E. coli HldE and GmhB. Crucially, the first preparative isomerization uses **A. thermoaerophilus** GmhA, so this is not an all-E. coli four-enzyme assay. HldE phosphorylates the C1 hydroxyl of D,D-heptose 7-phosphate in the beta configuration; GmhB removes phosphate at C7; HldE transfers **AMP** from ATP to the remaining beta-heptose 1-phosphate, yielding ADP-D,D-heptose. HldD then determines L,D stereochemistry. The UniProt phrase “ADP transfer” should not be interpreted as transfer of an intact ADP group from ATP.

PMID10629197 full text genetically separates HldE domains and shows a heptoseless rfaE mutant. PMID16030223 full text independently supports functionally important kinase-domain dimerization and ATP-site mutants. Exact quote: “Altogether, our data support the notions that the HldE functional unit is a dimer and that structural components present in each HldE1 monomer are required for enzymatic activity.”

PMID15911532 describes fractionation/proteomic localization; PMID18304323 full text documents a cytosolic proteome. Target-specific supplementary peptide tables were not re-extracted, and the existing curator-assigned IDA rows are retained with that limitation, not dismissed.


### PR5542 follow-up, 2026-10-25

Removed the cohort-level proteomics quotation from cytosol/cytoplasm annotation support. The publication reference and source-specific curator rationale remain, without presenting the aggregate 1,103-protein measurement as an independently verified HldE peptide identification.
