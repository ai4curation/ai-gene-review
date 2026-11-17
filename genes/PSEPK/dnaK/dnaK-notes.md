# dnaK / Q88DU2 annotation audit notes

## 2026-08-29 — qualifier-aware review

Reviewed the three current `dnaK-goa.tsv` signatures, UniProt Q88DU2, the
Falcon report, the complete cached PMID:33668424 paper, abstract-only
PMID:7937953, the E. coli DnaK precedent, and
`projects/UNFOLDED_PROTEIN_BINDING.md`. Current GOA contains exactly two
`enables` rows and one `involved_in` row. All three are represented exactly once
and ACCEPTed. There are no IBA or PANTHER/PTN rows to audit.

The three current claims are coherent and mutually reinforcing: ATP binding
(GO:0005524) and ATP hydrolysis (GO:0016887) drive the folding process
(GO:0006457). The KT2440-isogenic full text describes the molecular coupling
directly [PMID:33668424, "ATP binding and hydrolysis by DnaK NBD allosterically
controls the binding of SBD to its substrates—short hydrophobic peptide segments
that would normally be buried in the folded structure."]

## GO:0051082 replacement

The initial YAML contained an author-supplied NEW row for GO:0051082, using the
InterPro IEA visible in the UniProt flat file even though that assertion is
absent from the current GOA. GO:0051082 is now obsolete. It was not retained as
an interim or retired annotation merely to silence reconciliation checks.
Instead, the synthetic obsolete row was removed and replaced with a NEW,
qualifier-aware ISS proposal for GO:0140662 **ATP-dependent protein folding
chaperone**, the specific current child of GO:0044183 matching the Hsp70
mechanism.

The evidence code is deliberately ISS rather than IDA. PMID:33668424 is a
full-text P. putida study and describes repeated ATP-dependent binding and
release by DnaK, while its experiments address the C-terminal tail, GraT
phenotypes and competitive fitness rather than purified Q88DU2 client
refolding. Direct biochemical reconstitution is supplied by the canonical E.
coli DnaK ortholog [PMID:7937953, "The binding and release of substrate protein
for folding involves the following ATP hydrolysis-dependent cycle: (i) unfolded
luciferase binds initially to DnaJ; (ii) upon interaction with
luciferase-DnaJ, DnaK hydrolyzes its bound ATP, resulting in the formation of a
stable luciferase-DnaK-DnaJ complex; (iii) GrpE releases ADP from DnaK; and (iv)
ATP binding to DnaK triggers the release of substrate protein, thus completing
the reaction cycle."]

Client binding can transiently prevent aggregation, but the evidence reviewed
here places it inside an ATP-driven foldase cycle. No Q88DU2-specific evidence
establishes a separable ATP-independent holdase regime, so the holdase NTR was
not proposed for this gene and carrier-specific GO:0140309 is inapplicable.

The review is COMPLETE. The remaining experimental gap is direct biochemical
reconstitution of Q88DU2 with its KT2440 DnaJ and GrpE partners, which would
permit an IDA annotation to GO:0140662.

## 2026-08-29 — PR #2730 follow-up

The ISS source for the GO:0140662 NEW annotation is now explicit as
`UniProtKB:P0A6Y8` in annotation-level `supporting_entities`. This accession was
independently verified from the repository: `genes/ECOLI/DnaK/DnaK-ai-review.yaml`
identifies P0A6Y8 as E. coli DnaK, the reviewed UniProt cache records
`DNAK_ECOLI` with gene name `dnaK`, and the UPB cross-species table uses the same
accession.

ATP hydrolysis remains ACCEPTed as a physical GOA annotation but is no longer
duplicated as a separate top-level core function. It is the mechanistic engine
of the single GO:0140662 chaperone-cycle core. The unused UniProt reference entry
was removed because its generic "Acts as a chaperone" statement added no
material support beyond the two literature sources.

Project follow-up: the UPB decision-rule table routes ATP-dependent Hsp70s to
GO:0140662, while its historical cross-species E. coli DnaK row still says
GO:0044183. This one-gene PR follows the more specific current rule and leaves
the project-table cleanup to a separate scoped change.


## 2026-11-06 comparative DnaK-cycle audit

The target remains an inferred ATP-dependent DnaK foldase. PMID:33668424 methods explicitly use PaW85 derivatives described as isogenic to KT2440, with dnaK amplified from the PaW85 chromosome; this supports physiological comparison but is not a purified Q88DU2 KJE cycle assay. E. coli luciferase reconstitution supplies the direct mechanistic comparison. The inherited NEW foldase row remains unchanged outside its review judgment.

All historical annotation rows, including inherited NEW proposals, were preserved outside their review fields; no new annotation rows were added. Source UniProt/GOA, genuine research and prediction artifacts were protected against the pre-edit baseline. PAINT-loss checks found no applicable IRD or IKR.

Primary scope: [PMID:1826368] separates DnaJ stimulation of DnaK-bound ATP hydrolysis from GrpE-mediated nucleotide release. [PMID:7937953] follows denatured firefly luciferase through the E. coli DnaK-DnaJ-GrpE cycle. [PMID:20953191] measures remodeling of a tested misfolded luciferase species; its ATP cost is assay-specific, not a universal per-client constant. Normal forced fetches of those papers and PMID:11162122 and PMID:9103205 succeeded but remained abstract-only. Exact assay construct and E. coli substrain details not stated in those abstracts are not invented. Existing curator assignments are retained where independently supported; the particular complex-assembly process rows citing PMID:9103205 remain UNDECIDED because a structural complex does not alone resolve the assembly-process assertion.

Comparative boundary: [PMID:11162122, abstract] states "Here, DnaJ does not stimulate the DnaK-mediated ATP hydrolysis" for Thermus thermophilus. This is not negative evidence for the E. coli or KT2440 proteins, but rules out treating J-domain identity alone as a universal kinetic guarantee. Official QuickGO definitions were retrieved on 2026-11-06; GO:0051082 and GO:0003767 are obsolete, while GO:0044183 describes folding assistance and GO:0051087 binding to a chaperone protein. Client binding is not chaperone-partner binding.

The pre-existing genuine Falcon report was read as background and preserved unchanged; primary and curated evidence control the review.
