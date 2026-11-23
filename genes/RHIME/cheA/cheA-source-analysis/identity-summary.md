# Sinorhizobium chemotaxis identity and evidence boundaries

Reviewed 2026-11-06. Reproduce the sequence comparison with `uv run python genes/RHIME/cheA/cheA-source-analysis/verify_identity.py`; output is identity-proof.json. Inputs are the unmodified, normally fetched UniProt records and official sequence deposits, with SHA256 and source URLs in adjacent provenance files.

The ENA U13166.1 record explicitly identifies Rhizobium meliloti RU11001. Its CDS translations AAA86673.1 (CheY1, 121 aa), AAA86678.1 (CheY2, 129 aa), and AAA86672.1 (orf2, 97 aa) exactly match Q52879, Q52884, and Q52878, respectively. PMID22194454 establishes orf2 as cheS. These UniProt entries have species-level taxon 382; that taxonomy is retained rather than replaced by an invented strain taxonomy.

The current 1021 CheA Q52880 differs from RU11001 AAA86674.1 at five of 758 positions: current/reference D189E, S192A, N215D, E297K, S308P. UniProt labels all five as sequence conflicts, not demonstrated strain polymorphisms. Three discrepancies fall within the reported CheS-binding region CheA163–256. No separate exact current RU CheA accession was recovered in UniProt searches by cheA and AAA86674. The qualitative chemotaxis-kinase and phosphate-shuttle functions are transferred to the 1021 ortholog; RU affinity or rate measurements are not asserted as 1021 measurements.

The 2024 CheT paper, PMID39081077, Figure1 explicitly names NP_384751.1. The official NCBI record identifies strain 1021 locus SMc03013. Its complete 124-aa sequence exactly matches current Q92S03. This proves identity to the paper's alignment reference, not identity of the RU11/001 experimental construct. Main-text Table1 names pBS359 (pTYB11-cheT), pBS445 (cheT complementation), pBS639 (D57A), and pBS667 (Q61A); it does not deposit the complete insert sequence. CheT's phosphatase function is therefore inferred for Q92S03 from the paper-linked ortholog, and no RU binding constant is assigned to Q92S03 as a direct measurement.

## Primary full-text reading

PMID22194454 was read at https://pmc.ncbi.nlm.nih.gov/articles/PMC3294773/. PMID39081077 was read at https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.15303. Both identify the experimental lineage as RU11/001, a streptomycin-resistant derivative of MV II-1, not Rm2011 or 1021. The normal publication caches are abstract-only; no cached publication was manually replaced. Main-text interpretations below are reviewer analysis, not a fabricated provider report or full-text archive.

The 2012 study shows CheS–CheA complex formation and enhanced CheY1 affinity for that complex. Crosslinking did not detect direct CheS–CheY1 or CheS–CheY2 binding, with a caveat that isolated CheS required refolding. The authors leave the physical mechanism unresolved. Thus CheS is a noncovalent regulator of CheA/response-regulator coupling, not a demonstrated phosphatase or established two-partner bridge. Table1 and Table2 have inconsistent RU11/307 versus RU11/308 deletion labels; the 2024 Table1 agrees with the 2012 Table1 (307 is cheY2;308 is cheY1). Gene-specific biochemical results are interpreted by the named proteins, not by the inconsistent mutant numbers alone.

The 2024 study directly demonstrates CheT-stimulated CheY1-P dephosphorylation, with no enhancement of CheY2-P decay. Mutating its DXXXQ motif impairs activity. The CheR complex is observed, but neither partner changed the other's measured enzymatic activity. A contribution to coupling adaptation and termination remains a hypothesis; no separate CheR-regulator activity is asserted.

## Ontology, comparators, and model check

Current QuickGO definitions and ancestors were retrieved 2026-11-06 and logged in .cache/module-audit-logs/chemotaxis-20261106/. GO:0006935 is chemotactic movement under taxis and response to chemicals, not substrate processing. Each proposed participant performs signal chemistry (CheY1/CheY2/CheT) or changes the functional CheA–CheY1 complex (CheS). Gene necessity alone is not the argument. Chemotaxis is not an ancestor or descendant of the already carried phosphorelay process, and no redundant positive/negative taxis or general regulatory BP is added.

Same-role comparator queries: E.coli CheY P0AE67 carries chemotaxis, while P.putida CheY Q88EW2 does not; this mixed coverage does not demonstrate a systematic convention excluding response regulators. The phosphate-sink role itself is established by direct S.meliloti phosphotransfer assays, rather than transferred from E.coli motor-control behavior. E.coli CheZ P0A9H9 and B.subtilis CheC P40403 both carry chemotaxis and phosphoprotein phosphatase activity. E.coli CheW P0A964 and P.putida CheW Q88EX0 both carry chemotaxis; each is a comparator for noncatalytic signaling-complex participation, not evidence that CheS has CheW's adaptor mechanism. The local GO-CAM index contained none of Q52879/Q52884/Q52878/Q52880/Q92S03. GOA comparator state is recorded only as a policy check and never cited as molecular evidence.

## Short source excerpts checked in the full text

PMID22194454 Results, source URL above: “the data revealed an affinity of CheS for CheA but not for CheY1 or CheY2.”

PMID39081077 Figure1, source URL above: “S. meliloti CheT (NP_384751.1)”. Methods: “The wild-type S. meliloti strain RU11/001, is a spontaneous streptomycin-resistant derivative of MVII-1”. These excerpts record the identity and mechanistic boundaries; they do not replace the normal publication caches.
