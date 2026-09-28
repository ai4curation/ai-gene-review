# Provenance: Computed checks for SSQ1 (Q05931) curation review

All queries executed via `execute_code` (Python `requests`) against public APIs; outputs pasted verbatim below. No values were hand-edited.

## 1. Key primary-literature abstracts (NCBI efetch)
Retrieved PMIDs 11601843, 10779357, 23615440, 20224575, 16554755, 19536198, 12756240, 16431909, 32397253, 37968396. Verbatim quotes used as citation snippets (validated by knowledge-state tool):
- **PMID11601843** (Schmidt 2001, J Mol Biol): "Ssq1 showed typical chaperone properties by binding to unfolded substrate proteins in an ATP-regulated manner." / "no interaction of Ssq1 with the two other mitochondrial Hsp70-cochaperones, Tim44 and Mdj1, was observed."
- **PMID16431909** (Dutkiewicz 2006, JBC): "nonspecific binding of Ssq1p to Nfs1p helped to prevent its unfolding" / "Ssq1p/Jac1p/Mge1p are not important for Fe/S cluster synthesis on Isu1p."
- **PMID23615440** (Uzarska 2013, MBoC): "Ssq1 binds to the scaffold protein Isu1, thereby facilitating dissociation of the newly synthesized Fe/S cluster on Isu1 and its transfer to target apoproteins."
- **PMID20224575** (Pukszta 2010, EMBO Rep): "specializes in iron-sulphur cluster biogenesis."
- **PMID37968396** (Michaelis 2023, Nature): genome-scale affinity-enrichment MS interactome (HTP).

## 2. GO term definitions (QuickGO ontology service)
| GO ID | Name | Aspect | Note |
|---|---|---|---|
| GO:0051082 | **OBSOLETE** unfolded protein binding | MF | obsolete |
| GO:0042026 | protein refolding | BP | "restores the biological activity of an unfolded or misfolded protein" |
| GO:0140662 | ATP-dependent protein folding chaperone | MF | assist folding, ATP-driven |
| GO:0044183 | protein folding chaperone | MF | assist folding |
| GO:0140309 | **unfolded protein holdase activity** | MF | "binds to a protein in an unfolded state and escorts it to an acceptor molecule or to a specific location … prevents aggregation" |
| GO:0016226 | iron-sulfur cluster assembly | BP | core |
| GO:0005759 | mitochondrial matrix | CC | |

## 3. Current GO annotations for Q05931 (QuickGO annotation API; 28 records, deduped)
Folding claims are **IBA** (ECO:0000318, GO_REF:0000033 = PANTHER):
- GO:0044183 protein folding chaperone (MF) — IBA
- GO:0042026 protein refolding (BP) — IBA
- GO:0031072 heat shock protein binding (MF) — IBA
Experimentally supported MF: GO:0016887 ATP hydrolysis (PMID12756240, 16431909, 26545917); GO:0005515 protein binding IPI (PMID12756240, 12947415, 37968396 — **not** Nop1).
Core BP: GO:0016226 Fe-S cluster assembly (IMP: PMID11171977, 9813017). CC: GO:0005759 mitochondrial matrix (IDA: PMID8707841, 10779357, 11273703).

## 4. PANTHER family (pantherdb geneinfo)
Q05931 → **family PTHR19375, subfamily SF197**, protein class **"Hsp70 family chaperone" (PC00027)**. Propagates GO:0044183 / GO:0031072 by descent → origin of the IBA folding annotations. Matches seed's PTHR19375 folding/refolding IBD path (no NOT/IRD).

## 5. IntAct interactions for Q05931 (findInteractions API)
- Total records: **123**. Nop1/P15646 records: **2**.
- Both Nop1 records: `detectionMethod = tap` (co-complex), type association/physical association, **intactMiscore = 0.56**, from `publicationPubmedIdentifier` **19536198** and **16554755** (the two non-independent AP-MS studies). No direct-binary detection method.
- Partner set dominated by abundant nuclear/chromatin/cytosolic proteins (ASF1, HHT1, HIR3, INO80, EAF6/EAF7, IES1, ELF1) plus genuine ISU1/ISU2 → sticky-Hsp70 AP-MS promiscuity.

## Access limitations (reported plainly)
- WebFetch backend was unavailable (model error), so PANTHER treeinfo node-by-node, Craig-lab author PDFs, and journal full-text figures (Fig4C/4D, Fig8, Fig3D) were **not** independently retrieved. Figure-level claims rely on the seed's descriptions + abstracts; none were fabricated.
