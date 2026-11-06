# celA evidence and identity review

A9CEZ7 / Atu3309 is729 aa, with GenBankAAK90083.1 and RefSeqWP_010972931.1 crossreferences. The first UniSave entry (2008) and the current GenBank protein both have729 aa. The 2018 review's Table2 gives2190 bp(789 aa);2190 coding bases correspond to729 residues plus stop, so the parenthetical789 is internally inconsistent. This does not justify revising the current sequence.

The original celABC/celDE genetics [PMID:7860585] and extract UDP-glucose incorporation [PMID:7860586] support the pathway, with no purified A9CEZ7 kinetic measurement claimed. The target has cellulose synthase, glycosyltransferase2 and PilZ domains. Curated RuleBaseRU365020 describes UDP-glucose-dependent polymerization. The mechanistic Rhodobacter BcsAB structure [PMID:23222542] supports coupling of polymerization to inner-membrane translocation by homology.

Agrobacterium PilZ-domain mutagenesis reduces cellulose production [PMID:24443526]; this supports the regulatory-domain role, not a direct target ligand-binding assay. The Rhodobacter c-di-GMP-bound complex [PMID:24704788] identifies the direct BcsA switch. The published Ser594 mutation cannot be mapped by number to current A9CEZ7 (Ile594; context584–604 GGSDTWVPASIDNVSVHGLLI). Exact construct alignment is unresolved; no residue-specific claim is transferred. The inferred c-di-GMP-binding annotation remains justified by independent domain and homolog evidence.

Five source annotations are accepted and three refined (membrane, general hexosyltransferase, general cellulose synthase); no rows added. UDP-glucose metabolism is retained because CelA directly consumes the donor, and it is not an ancestor of cellulose biosynthesis.

Research access and provenance (2026-11-05)

The standard fetch-gene workflow seeded the frozen UniProt/GOA sources before review. The accession-named output directories were renamed to the conventional symbols without changing source bytes. Original non-review annotation payloads and source SHA256 values are preserved in `.cache/module-audit-logs/cellulose-20261105/agrobacterium-baseline.json`. Review actions do not rewrite these payloads. Normal default Falcon research was attempted independently for all three genes; all failed HTTP403 (missing/invalid/unauthorized API key). Logs are in the same audit cache. No provider research document was written manually. These notes are the manual research record.

PMIDs7860585,7860586,24443526 were fetched/retried normally but remain abstract-only. NCBI PMC efetch XML explicitly states that the publisher does not permit full XML downloading. PDF links returned an HTML challenge, and EuropePMC fullTextXML failed. PMID:16167770 remains abstract-only; its publisher PDF returned403. No unseen figure or isolated-protein measurement is inferred from these abstracts. Full cached primary homolog structural papers PMID:23222542 and PMID:24704788 and full reviews PMID:26077867 and PMID:29998422 were examined.

Identity and strain scope

The current organism is Agrobacterium fabrum C58 (NCBITaxon176299), historically called A. tumefaciens C58. Indexed primary text of PMID:7860586 identifies A1045 as a chvB mutant of C58, corroborated by Table1 of primary PMC2293172. The available primary-paper copy is https://www.academia.edu/23372784/Mechanism_of_cellulose_synthesis_in_Agrobacterium_tumefaciens ; the independent strain table is https://pmc.ncbi.nlm.nih.gov/articles/PMC2293172/ . Thus A1045 is a C58 lineage strain, not evidence for another wild-type accession. This does not establish exact identity of every historical engineered protein construct to the current UniProt sequence.

Ontology and scope check

Live QuickGO definitions/ancestors were checked and saved as agrobacterium-term-checks.json and agrobacterium-parents-comparators.json in the audit cache. Cellulose synthase (UDP-forming), GO0016760, is below cellulose synthase and hexosyltransferase; plasma membrane is below membrane. Cellulose biosynthesis and UDP-glucose metabolism are not ancestor/descendant processes. No target accessions occur in gocams/index.tsv. No NEW row is needed for CelA's already-covered catalytic function. CelB's replacement is a role correction based on structural participation, not a new assertion based on necessity. Adhesion, virulence and biofilm changes are not promoted to direct functions of these proteins.


## 2026-11-06 — round 16 follow-up

The accepted UDP-glucose metabolism claim now appears explicitly in the catalytic core, consistent across all five catalytic BcsA reviews carrying that term.
