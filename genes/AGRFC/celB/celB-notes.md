# celB evidence and identity review

Q7CS46 / Atu3308 is827 aa, with GenBankAAK90084.2 and RefSeqWP_010972930.1 crossreferences. The 2018 Table2's2484 bp(828 aa) is consistent with counting the stop triplet as a codon; the current protein is827 residues. No exact historical construct sequence is asserted.

The target has AcsB/BcsB-family carbohydrate-binding and flavodoxin-like domains, a signal peptide at1–24 and a C-terminal membrane segment at798–820. The homolog Rhodobacter structure [PMID:23222542, “BcsB is a periplasmic protein that is anchored to the inner membrane via a single, C-terminal TM-helix.”] supports a membrane-anchored periplasmic structural partner. This is a homology-supported core role, not a C58 stoichiometry or direct glucan-binding measurement. The1995 polar-insertion evidence is not treated as a purified CelB activity.

UniProt's RuleBaseRU365021 direct c-di-GMP-binding statement is flagged for reassessment. The established direct switch is BcsA/CelA's cytoplasmic PilZ domain [PMID:24704788]; the old BcsB name and broad family propagation are insufficient target binding evidence. No NEW c-di-GMP-binding or catalytic glycosyltransferase annotation is added.

Same-role comparator check: QuickGO P37652 (E.coliBcsB) and Q88JL3 (P.putidaBcsB) both carry UDP-glucose metabolism but lack cellulose biosynthesis. This absence is recorded, not used to manufacture a gap. The explicit lateral replacement of the donor-metabolism row with cellulose biosynthesis is justified by the protein's structural participation in the synthase complex: CelA performs chemistry, CelB supplies the complex architecture. No ancestor relationship is claimed and no duplicate NEW BP is added. Plasma membrane is accepted and membrane refined to it.

Research access and provenance (2026-11-05)

The standard fetch-gene workflow seeded the frozen UniProt/GOA sources before review. The accession-named output directories were renamed to the conventional symbols without changing source bytes. Original non-review annotation payloads and source SHA256 values are preserved in `.cache/module-audit-logs/cellulose-20261105/agrobacterium-baseline.json`. Review actions do not rewrite these payloads. Normal default Falcon research was attempted independently for all three genes; all failed HTTP403 (missing/invalid/unauthorized API key). Logs are in the same audit cache. No provider research document was written manually. These notes are the manual research record.

PMIDs7860585,7860586,24443526 were fetched/retried normally but remain abstract-only. NCBI PMC efetch XML explicitly states that the publisher does not permit full XML downloading. PDF links returned an HTML challenge, and EuropePMC fullTextXML failed. PMID:16167770 remains abstract-only; its publisher PDF returned403. No unseen figure or isolated-protein measurement is inferred from these abstracts. Full cached primary homolog structural papers PMID:23222542 and PMID:24704788 and full reviews PMID:26077867 and PMID:29998422 were examined.

Identity and strain scope

The current organism is Agrobacterium fabrum C58 (NCBITaxon176299), historically called A. tumefaciens C58. Indexed primary text of PMID:7860586 identifies A1045 as a chvB mutant of C58, corroborated by Table1 of primary PMC2293172. The available primary-paper copy is https://www.academia.edu/23372784/Mechanism_of_cellulose_synthesis_in_Agrobacterium_tumefaciens ; the independent strain table is https://pmc.ncbi.nlm.nih.gov/articles/PMC2293172/ . Thus A1045 is a C58 lineage strain, not evidence for another wild-type accession. This does not establish exact identity of every historical engineered protein construct to the current UniProt sequence.

Ontology and scope check

Live QuickGO definitions/ancestors were checked and saved as agrobacterium-term-checks.json and agrobacterium-parents-comparators.json in the audit cache. Cellulose synthase (UDP-forming), GO0016760, is below cellulose synthase and hexosyltransferase; plasma membrane is below membrane. Cellulose biosynthesis and UDP-glucose metabolism are not ancestor/descendant processes. No target accessions occur in gocams/index.tsv. No NEW row is needed for CelA's already-covered catalytic function. CelB's replacement is a role correction based on structural participation, not a new assertion based on necessity. Adhesion, virulence and biofilm changes are not promoted to direct functions of these proteins.
