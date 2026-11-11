# SNAP23 (donkey, Equus asinus; UniProt A0A8C4M285) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl ENSEASP00005019168.1): `SNAP23-uniprot.txt`. Length 97 aa.
- Donkey GOA (8 IEA rows: 6 TreeGrafter GO_REF:0000118 from PANTHER:PTN000447812, plasma membrane via GO_REF:0000120, presynapse via GO_REF:0000108 inferred from synaptic vesicle priming): `SNAP23-goa.tsv`.
- Human SNAP23 (O00161) UniProt record, fetched 2026-10-14: `SNAP23-bioinformatics/human-SNAP23-O00161-uniprot.txt`.
- Donkey-human alignment: `SNAP23-bioinformatics/RESULTS.md`.
- Human/mouse QuickGO annotations (queried 2026-10-14) as comparator: human SNAP23 has IDA for helical-bundle zippering fusogenic activity, SNARE complex, vesicle fusion and plasma membrane; the synaptic vesicle priming and synaptic vesicle fusion to presynaptic active zone membrane rows on human/mouse SNAP23 are IBA only.
- No publication-based GOA rows for the donkey protein; no publications fetched.

## Sequence

- The entry is a truncated SNAP23 product [file:EQUAS/SNAP23/SNAP23-bioinformatics/RESULTS.md "The donkey entry A0A8C4M285 is a 97-residue product."].
- It keeps the first SNARE motif and the palmitoylated cysteine linker [RESULTS.md "all five linker cysteines (human C79, C80, C83, C85, C87) are conserved"].
- It lacks the second SNARE motif [RESULTS.md "The product lacks the human region 90..211, which includes the C-terminal t-SNARE coiled-coil motif (Qc, human 146..208)."].
- Other donkey SNAP23 entries exist in UniProt (A0A8C4M333, 211 aa; A0A8C4M5X5, 222 aa; A0A9L0K6I4, 209 aa; A0A9L0J3X0, 158 aa), queried 2026-10-14.

## Function (human ortholog)

- [human UniProt "SNAP23 is a t-SNARE (target-SNARE) that resides on"] target membranes and functions in fusion of transport vesicles with the plasma membrane; it supplies two of the four helices of the SNARE bundle.
- Localization: [human UniProt "Lipid-anchor {ECO:0000269|PubMed:21044946}"]; donkey record [donkey UniProt "SUBCELLULAR LOCATION: Cell membrane"].

## Review decisions (summary)

- plasma membrane: ACCEPT (palmitoylation cysteines conserved).
- helical-bundle zippering fusogenic activity, SNARE complex, exocytosis, vesicle fusion: UNDECIDED for this 97-aa product (correct for full-length SNAP23 but this product lacks the Qc SNARE motif; no data on whether such a product assembles into fusogenic complexes).
- synaptic vesicle priming, synaptic vesicle fusion to presynaptic active zone membrane, presynapse: MARK_AS_OVER_ANNOTATED (neuronal SNAP25 functions propagated across the SNAP-25 family; SNAP23 is the ubiquitous non-neuronal paralog).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

### Deep research
- `just deep-research-falcon EQUAS SNAP23 --fallback perplexity-lite` failed: falcon "Failed to authenticate" (Edison client), and the perplexity-lite fallback returned HTTP 401 insufficient_quota. No deep-research file was produced. Literature was gathered directly instead (cached with `just fetch-pmid`): PMID:8663154, PMID:12556468, PMID:30811271, PMID:12859899, PMID:17728451, PMID:21044946.

### Identity of the benchmark accession
- A0A8C4M285 (97 aa, ENSEASP00005019168 / ENSEAST00005020804) is an **alternative-terminal-exon product of the single donkey SNAP23 gene** (ENSEASG00005013173) [file:EQUAS/SNAP23/SNAP23-bioinformatics/RESULTS-rereview.md "The benchmark product is therefore an alternative-splice (alternative terminal exon) gene model, not a separate gene."]. It shares exons 1-4 with the full-length transcript and ends in a unique exon encoding FNIRSRAQ.
- It is 97 aa vs 211 aa for the canonical product; it retains the Qb SNARE motif and all five palmitoylated linker cysteines but lacks human 90..211 including the Qc SNARE motif (RESULTS.md).
- It is not the counterpart of human SNAP-23b (which lacks 90..142 but keeps the Qc motif; human UniProt VAR_SEQ VSP_006188).
- UniProt gene-centric canonical for this gene in UP000694387 is **A0A8C4M333** (211 aa, same length as human SNAP-23a); Ensembl's own canonical is the 222-aa ENSEAST00005020800 (A0A8C4M5X5) with an 11-residue insertion (FSDVGCFYETR).

### Evolutionary placement
- All donkey SNAP23 entries are in PTHR19305:SF4 (SNAP23 subfamily) together with human O00161, mouse O09044, rat O70377; human SNAP25 is in SF5 (`interpro/panther/PTHR19305/PTHR19305-entries.csv`). No PANTHER family review exists under `interpro/panther/PTHR19305/` (only metadata and entries), so there is no subfamily disagreement to report.
- Human SNAP23 IBA rows (QuickGO, queried 2026-10-21): fusogenic activity, SNARE complex, exocytosis via a broad node; synaptic vesicle priming and synaptic vesicle fusion to presynaptic active zone membrane come only from PTN000447754 with Drosophila Snap25 (FBgn0011288) as the donor. Human SNAP23 has IDA for fusogenic activity (PMID:28265073, PMID:30811271), vesicle fusion (PMID:28265073), SNARE complex and plasma membrane.

### Evidence for the synaptic terms
- SNAP23 overexpressed in Snap25-null chromaffin cells: [PMID:12859899 "whereas SNAP-23 did not support a standing pool of primed vesicles"].
- SNAP23 in Snap25-null neurons: [PMID:17728451 "SNAP-23 supported asynchronous release only"]; [PMID:17728451 "synchronous release required SNAP-25a/b in both glutamatergic and GABAergic neurons"].
- So the PAINT node placement carries a SNAP25-type neuronal function above the SNAP23/SNAP25 duplication; SNAP23 is the ubiquitous paralog [PMID:8663154 "Unlike SNAP-25, SNAP-23 was expressed in all tissues examined."].

### N-terminal SNARE motif alone
- [PMID:12556468 "SNAP-23N can assemble spontaneously with the coiled-coil domains from SNAP-23C, syntaxin-4, and VAMP-3 to form a heterotetrameric complex."] The truncated product could in principle enter SNARE assemblies only if a Qc helix is provided by another molecule; this keeps the SNARE complex / fusogenic rows UNDECIDED rather than REMOVE.

### Decisions (unchanged actions, strengthened support)
- plasma membrane: ACCEPT (palmitoylation linker in shared exons; [PMID:30811271 "a plasma membrane—localized Qbc-SNARE"]).
- fusogenic activity, exocytosis, vesicle fusion, SNARE complex: UNDECIDED (gene-level true; product lacks Qc and expression unverified).
- synaptic vesicle priming, SV fusion to active zone, presynapse: MARK_AS_OVER_ANNOTATED, now with rescue-experiment evidence.
- Replaced a reference finding that quoted the ARBA-only SIMILARITY line with the PANTHER SF4 cross-reference.

### Relative to review next
- Same gene canonical product A0A8C4M333 (no review in repo; folder would be genes/EQUAS/SNAP23__A0A8C4M333). Human SNAP23 (O00161) also has no review in the repo.
- Modules: `modules/synaptic_vesicle_exocytosis.yaml` and `modules/synaptic_vesicle_cycle.yaml` list the SNAP-25 family (PTHR19305) as Qbc-SNARE with SNAP25 representatives only; SNAP23 is not a part of those neuronal modules.
