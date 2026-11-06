# RSP_0333 annotation review notes

## 2026-11-06 complete gene review

Seeded using `just fetch-gene CERS4 RSP_0333 --uniprot-id Q3J125`. The standard symbol is the locus name and was preserved. The pristine review, all source row payloads and both raw hashes were captured in `.cache/module-audit-logs/cellulose-20261105/rhodobacter-baseline.json` before editing. Current UniProt species code CERS4 refers to Cereibacter sphaeroides 2.4.1, historically Rhodobacter sphaeroides.

Applied the annotation-reviewer/core-function guidance. The normal Falcon command `just deep-research CERS4 RSP_0333 --provider falcon` failed with HTTP 403 authentication/access error. No provider report was fabricated; these are manual fallback notes.

PMID:23222542 methods explicitly state the genomic DNA source was Rhodobacter sphaeroides 2.4.1. BcsA was expressed with a C-terminal 12-His tag. The BcsB construct replaced its native signal peptide with PelB and retained residues 21-725, with an additional Met-Gly dipeptide after cleavage. Unmodified PDBe SIFTS responses for 4HG6 and 4P00 are stored with provenance in the RSP_0333 source-analysis directory. 4HG6 maps Q3J125 residues 1-788 and Q3J126 residues 21-725 with identity 1.0. Raw UniProt PDB cross-references independently support this mapping. Construct residue numbering is distinguished from native numbering.

PMID:24704788 directly identifies the BcsA PilZ c-di-GMP switch. PMID:26958837 was initially abstract-only after a 429 fetch failure; normal force-fetch recovered full text, permitting review of all three original IPI sources. Its in-crystal and engineered-mutant experiments identify polymerization/translocation mechanisms, not native-cell ecological phenotypes. PMID:24127606 was normally fetched but remained abstract-only after the publisher XML/HTML/PDF fallbacks failed. Its authoritative PMC article was consulted externally for functional reconstitution; quotes use the unchanged cached abstract. This paper directly assays separately and jointly expressed subunits, not only gene-deletion necessity.

QuickGO term definitions were checked: GO:0016760 describes the UDP-glucose-dependent glucan extension reaction. GO:0010330 cellulose synthase complex explicitly specifies a rosette for the plant cell wall, so it was not assigned to bacterial BcsAB. Neither gene has an IBA row; no PAINT loss judgment is required.

All ten seed rows were reviewed. The three bare protein-binding IPI claims are MODIFY to the already-present UDP-forming cellulose synthase activity because the cited papers directly establish BcsA catalysis. The protein interaction remains accepted biologically. Broad transferase/cellulose synthase terms are similarly refined, membrane is refined to plasma membrane, and the donor-substrate process is refined to cellulose biosynthesis. Direct c-di-GMP binding is retained as integral regulation. No NEW rows were added, and no extra biofilm or transport process was inferred from general pathway context.


## 2026-11-06 PR2143 round-15 BcsA follow-up

PR2143 round-15 IMPORTANT1: changed GO:0006011 from MODIFY to ACCEPT because catalytic BcsA directly consumes UDP-alpha-D-glucose. QuickGO definition checked on 2026-11-06: reactions involving this substrate; cellulose biosynthesis is a separate product-process assertion, not a descendant replacement. Retained both process descriptions in the core. All original annotation payloads and source artifacts are unchanged; no NEW rows were added.

Evidence: PMID:39394223 describes a UDP-glucose-using GT domain and inner-membrane extrusion through the BcsA transmembrane-domain/BcsB tail-anchor pore; PMID:23222542 directly assays purified 2.4.1 BcsAB with UDP-Glc. The substrate is acted upon by catalytic BcsA itself, distinguishing these annotations from noncatalytic BcsB. Current GO definition saved in `.cache/module-audit-logs/cellulose-20261105/bcsa-followup-GO0006011.json`. Focused gene validation and baseline preservation checks passed; logs and before/after hashes are in the same audit directory under `bcsa-followup-*`.
