# CIC review notes

## 2026-10-10: source-preserving whole review

CIC is HGNC:14214 / UniProt Q96RK0. The HGNC record warns that CIC is also an alias of SLC25A1; the review follows the Q96RK0 target. Fresh ownership checks found the literal unchecked catalog entry after CIB2 and no matching gene, alias, accession or publication-queue ownership among 241 complete current-head PR inventories. There was no previous target review or notes file to replace.

Genuine isolated normal intake produced 28 GOA assertions, two products and 13 original references. All original annotation fields, including qualifiers and WITH/FROM entities, remain exact and ordered. No new annotation is proposed. Provider research was attempted concurrently with publication caching: Falcon timed out and its configured Perplexity-lite fallback returned HTTP401 insufficient_quota. No provider report was fabricated or renamed; the literature assessment below is manual.

### Molecular synthesis and products

The core is sequence-specific DNA-binding transcriptional repression, represented by GO:0001227 with negative regulation of Pol II transcription. Human GFP-CIC reporter and ChIP assays in PMID:28278156 connect promoter occupancy to repression; purified or translated HMG–C1 modules establish direct motif recognition. The paper explicitly names NP_055940.3, which the authenticated UniProt record maps to Q96RK0-2. Its 1608-aa sequence is reconstructed by removing canonical residues 1–909 and applying the equal-length alternative N-terminal segment at 910–931. Q96RK0-1 remains the 2517-aa displayed product. Neither is silently removed or marked inactive.

The 2025 structure (PMID:40967212) uses engineered min18/min31 modules rather than either complete protein. Assay and linker context matter: R201W can increase fragment binding, and R215W differs between EMSA and MST. These results do not justify a blanket statement that pathogenic variants invariably abolish DNA binding. The full-length regulatory consequences and the distinct N termini remain explicit questions. CIC-DUX4 activation is not transferred to normal CIC.

### Partner and developmental evidence

Five ATXN1 interaction assertions are refined to transcription corepressor binding. The original screen, native-complex and AP-MS observations retain their distinct methods. Actual PMID:20628574 reporter work shows ATXN1/ATXN1L co-repression with CIC; the class refinement does not transfer partner activity to CIC or assert purified binary affinity for every co-IP. The broad complex assertion is refined to a transcription repressor complex, without a fixed stoichiometry.

The CENPJ record includes both two-hybrid and tagged pull-down evidence, with a CIC C-terminal fragment in the two-hybrid record. CENPJ is a centriolar microtubule regulator associated with the gamma-tubulin complex (also recorded as part_of by current GOA, NAS PMID:11003675), supporting the cytoskeletal partner class. This is an assay-level binding refinement, not a CIC centrosome or centriole function.

The original GOLGA2 record in PMID:29568061 is specifically BioID proximity. A separate positive HuRI pair in PMID:32296183 supports generic binding; neither establishes a native Golgi mechanism for CIC. Both remain non-core and their different evidence types are explicit. GOLGA2 has positive spindle-localization and microtubule-capture evidence, but whether the assayed product meets the cytoskeletal-component class in GO:0008092 remains unresolved. This is a specificity boundary, not a claim that GOLGA2 lacks cytoskeletal associations or that absence of a part_of annotation refutes membership.

Mouse Cic/Q924A2 is the authenticated source for the developmental and behavioral transfers. PMID:28288114 distinguishes Emx1-lineage forebrain learning/memory and upper-layer maturation effects from Otp-lineage hypothalamic/amygdala social phenotypes. These existing annotations are retained as non-core contexts of transcriptional regulation. No new process was inferred solely from loss-of-function phenotypes, and no behavioral core duplicates the transcriptional operation.

### Access and provenance

All seven original PMID caches are exact main bytes. PMID:18337722 has an abstract-only selected main cache and a separate genuine fresh full variant whose Methods and Results were read; the selected cache is not overwritten. PMID:16713569 remains a main abstract, supplemented by an authentic author-hosted PDF read for screening and co-affinity Methods; exact target construct records are from IntAct. PMID:33961781 is labeled full by its cache metadata but actually contains only the abstract, Introduction and Discussion; no complete Methods/Results access is claimed. PMID:17190598 remains abstract-only; later full sources independently support the detailed native-complex and co-repressor interpretation.

Genuine supplementary normal full sources are PMID:28288114, PMID:28278156, PMID:40967212, PMID:20628574 and PMID:22014525. The actual section/paragraph read ledger and all raw records remain in the immutable TMP evidence packet. The compact [source audit](CIC-source-evidence.json) records URLs, source hashes, construct limits and exact interaction identifiers; its authored interpretation is not independent experimental evidence.

The current PAINT node is PTN000990637. Corrected official identity joins resolve fly FBgn0262582 to Q9U1H0 and mouse MGI:1918972 to Q924A2. Initial malformed direct FB/MGI queries failed with HTTP400 and are not negative results. Current source and target evidence supports transfer, while historical IBD placement and the alignment remain uninspected. Target self-evidence and a short donor list are not treated as circular or weak. Existing broader-to-specific refinements describe the human target and preserve every historical source field.

No GO-CAM target activity was found in the authenticated current index. No NEW process or MF is proposed. The publication contains only short primary anchors in YAML; this notes file and the compact audit introduce no quoted primary passages. Exact aggregate counts are checked before sealing.

### Final applicability check

Authenticated main `35d102bc46bae9377ad6c60151bed1f07c62bf85` retains all ten protected source files unchanged and all 14 finite additions absent. The refreshed ownership inventory covers 242 complete current-head PR file/label inventories; gene, aliases, accession and queue remain clear. No shared-cache collisions or GO-CAM target hits were found. There are 13 literal target interaction records, and 19 current donor/source joins containing 32 same-term records; these are reproducibility counts, not evidence-strength or historical-node inferences.


## 2026-10-11 — Biological description update

The summary now connects capicua repression to RTK/Ras–MAPK signaling and names its TGAATGAA-like recognition sequence. It distinguishes normal CIC tumor-suppressor activity and recurrent oligodendroglioma mutations from the oncogenic CIC–DUX4 fusion context. These additions are supported by the selected full text of PMID:28278156 (Introduction, Figure 1 and Discussion), with corroborating background in PMID:40967212 (Introduction). This is a biological summary; it does not assign the fusion's activator activity to normal CIC or generalize every variant's effect on DNA binding.

The existing source-specific annotation decisions, product mapping and experimental construct limits are retained. Earlier source-access and publication records above describe their original snapshots. No additional primary quotation is introduced.
