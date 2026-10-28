# Alginate O-acetylation: literature and taxon audit

## 2026-10-25

The module covers AlgI, AlgJ/AlgV, AlgF and AlgX-mediated maturation of bacterial alginate. Precursor synthesis, polymerization, export and mannuronate epimerization remain adjacent modules. Physical coupling to the export machinery does not require importing the whole secretion pathway into this module.

Recent reviews: PMID:40171682 (2025, transmembrane polymer acylation), PMID:40821665 (2025, Azotobacter alginate biosynthesis), PMID:37884397 (2023, Pseudomonas biofilm exopolysaccharides), and PMID:35401471 (2022, Azotobacter regulation; correction PMID:35756034). These establish a comparative Pseudomonas/Azotobacter envelope; they do not establish universal bacterial or brown-algal O-acetylation machinery. Azotobacter AlgV corresponds to Pseudomonas AlgJ, whereas a separate Azotobacter export protein has historically been called AlgJ. Accession and locus identity must govern the comparison.

PMID:40171682 proposes that AlgI's C-terminal acyl-shuttle motif receives an acetyl group and passes it to AlgJ. The primary experimental mechanisms behind this proposal concern Dlt proteins (PMID:37308592) and PatA/PatB (PMID:40280421), not purified AlgI. The review explicitly says the full alginate model has not been demonstrated. Therefore the donor and relay chemistry stay qualified; acetyl-CoA is not asserted as an experimentally established AlgI substrate merely because another review describes it categorically.

PMID:37797696 provides direct P. putida as well as P. aeruginosa evidence. Its Methods identify KT2440 AlgF and AlgX, and its structural modeling identifies all four relevant accessions. KT2440 AlgF29-215 lacks detectable acetylesterase activity and binds AlgJ75-370 and AlgX by ITC; P. aeruginosa AlgF is used for NMR structural work, negative mannuronate binding and native association experiments. The organisms and constructs are kept separate. AlgF is supported as a protein-interaction mediator, not an enzymatic acetyltransferase inferred from the process name.

PMID:25165982 likewise assays both Pseudomonas AlgJ proteins: the crystallized protein is P. putida, and the P. aeruginosa catalytic positions differ from those in that structure. AlgJ acetylesterase activity is directly measurable in vitro, while its physiological relay substrate is not established. AlgX transfers acetyl groups from a surrogate donor to polymannuronate directly; this does not identify the native upstream donor.

A native Azotobacter algF mutant producing unacetylated alginate is described in PMID:10352233. This strengthens cross-genus process evidence, but does not by itself assign transferase chemistry to AlgF or directly establish the functions of all neighboring homologs.

The module deep-research provider attempt failed authentication/quota. No provider report was written by hand. Source caches, independent primary-paper reading and individual annotation reviews support this audit.

Final member QA distinguishes an intrinsic AlgX O-acetyltransferase inference from an unsupported AlgF molecular-function assignment. Pairwise AlgF contacts do not prove simultaneous adaptor bridging; AlgF retains its directly supported process/localization roles. AlgV likewise has no asserted physiological transferase MF until donor/recipient chemistry is established. Pre-existing PSEPK algI/algJ NEW process rows duplicate their own specific MODIFY replacements and are removed without losing process coverage. The two remaining pre-existing acetylation process proposals have native-role comparator checks recorded in gene notes.

All four module roles have a family descriptor and three verified representatives. InterPro IPR028362 and IPR035422 are full-family entries; IPR034657 and IPR034655 are domain entries, used only as domain constraints for the AlgJ/AlgV and AlgX groups. Exact labels were verified against live InterPro records. The sole remaining module-validator advisory is that the configured ontology adapter cannot check the InterPro prefix; manual verification supplies that check.

The connection type PROVIDES_INPUT_FOR explicitly includes context in the repository schema. Thus AlgF edges describe interaction/assembly context with NOT_APPLICABLE material chaining, rather than an acetyl intermediate. AlgI-to-AlgJ and AlgJ-to-AlgX chemistry remains marked KNOWLEDGE_GAP. The pseudomonad family taxon is an evidence envelope for the reviewed lineages, not a universal-presence or ancestor claim.

The final 12-member review set contains 51 rows: all 42 original GOA annotations, four retained older proposals and five audit-added proposals. Two older proposals duplicate specific replacements and were removed. Actions are 32 ACCEPT, nine MODIFY, nine NEW and one KEEP_AS_NON_CORE. The AlgJ statement is limited to its measured binding behavior; the cited paper establishes AlgX polymer transfer but does not establish a negative AlgJ transfer assay.
