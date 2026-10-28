# E. coli K-12 ammonia-assimilation review

## 2026-10-27 evidence assessment

Original annotation payloads and both raw source files were snapshotted before review. The three-gene panel contains 50 existing rows; no NEW row is introduced. Provider research and fitness attempts are recorded in the shared ammonia acquisition logs. No generated provider text was fabricated or substituted for primary evidence.

The gltBDF study (PMID:2448295) explicitly identifies gltB and gltD as large and small glutamate synthase subunits and reports restoration of synthase activity by gltB complementation. Its polar insertion and gltF-linked nitrogen phenotypes are not evidence that either enzyme subunit is a transcriptional regulator. The original PMID:4565085 record has no accessible abstract or full text, but target UniProt cites it for the coupled reaction and heterodimer membership. UniProt identifies that experiment as E. coli strain W, not K-12; it is used as conserved curated biochemical evidence rather than a K-12-specific assay.

The native K-12 W3110 subunit study PMID:770440 was read separately in the publisher PDF, while its immutable PMID cache remains abstract-only. See [historical subunit analysis](../gltB/gltB-source-analysis/historical-subunits.md) for exact page/table scope and access failures. Very low recovered activities after SDS/urea separation must be distinguished from intact-holoenzyme site allocation. The target's legacy UniProt miscellaneous statement apparently assigning 2-oxoglutarate to the small chain and the large-chain FAD statement are not adopted as modern mechanistic proof.

Primary Azospirillum biochemistry PMID:10785395 assigns the pyridine-nucleotide FAD site to beta and the FMN/2-oxoglutarate site to alpha; its E. coli BL21 is an expression host, not the source organism. That study leaves the two [4Fe-4S] centers unlocalized; PMID:31473159 cryo-EM locates both on beta. These are comparative mechanistic evidence, reinforced by target GltB GATase/FMN domains and GltD FAD/NAD/ferredoxin domains. The exact two-center stoichiometry is not asserted as measured in K-12. The accessible PMID:10357231 summary further supports the small-chain NAD(P)H electron-relay family; full_text_html metadata does not turn its abstract-like fetched content into a complete review.

The original generic protein-binding screen rows (PMID:15690043 and PMID:16606699) remain UNDECIDED because the actual target interaction partners and experiments could not be recovered. The known GltB–GltD complex does not establish the meaning of every screen edge; no experimental REMOVE or invented enzyme-binding replacement is introduced. Cytosol is retained from the coherent native MC4100 proteomic assignment (PMID:18304323), acknowledging that supplemental target rows were not retrieved.

The core function separates each chain's direct activity from contribution to coupled NADPH-GOGAT: GltB glutamine hydrolysis and FMN chemistry; GltD NADPH electron input. Original qualifiers and all machine assertion fields are preserved. Broad classes refine to supported specific activities already covered by the reaction or replacement terms; no NEW row is added.


## 2026-10-28 — PR #5696 review follow-up

The glutamine-hydrolysis and ammonia-channel mechanism remains in the biological description and core-function prose. The machine-readable core now records contribution to GO:0004355 glutamate synthase (NADPH) activity, with the native small chain required for NADPH input, rather than a separate GO:0004359 glutaminase activity. This policy is applied to all four reviewed large chains; the inherited PSEPK standalone proposal is archived, and no new rows are added to fill coverage warnings. Direct E. coli partial-activity evidence (PMID:770440) remains valid and retained.
Both generic binding rows name the reciprocal GOGAT subunit. Their refinement to GO:0046982 is supported independently by the curated UniProt CC:SUBUNIT heterodimer statement and native gltBDF genetics (PMID:2448295); unrecovered assay details from the interaction screens are not invented.
