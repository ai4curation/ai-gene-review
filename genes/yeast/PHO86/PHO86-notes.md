# PHO86 review notes

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the defensible core curation is ER-localized chaperone-mediated regulation of phosphate transport and ER-to-Golgi traffic, not direct phosphate ion transport or generic protein binding.

## 2026-09-28 cached-publication and newer-literature pass

- Rechecked `PHO86-ai-review.yaml`, `PHO86-uniprot.txt`, `PHO86-deep-research-falcon.md`, and all cached PMID-backed references. PHO86 has no IBA annotations in the current GOA snapshot, so there were no PAINT rows to align.
- `PMID:10655492` is abstract-only locally and directly supports the review's core distinction: Pho84 is the high-affinity phosphate transporter, while Pho86 is an ER-resident protein required for Pho84 packaging into COPII vesicles and ER exit.
- `PMID:15623581` is abstract-only locally and supports `GO:0051082` -> `GO:0044183`: Pho86 belongs to the specialized ER membrane-localized chaperone class that prevents aggregation of cognate polytopic membrane clients.
- Large-scale interactome publications `PMID:16429126`, `PMID:18467557`, `PMID:27107014`, and `PMID:37968396` were checked only for the existing `GO:0005515` IPI rows. These rows were migrated from `MARK_AS_OVER_ANNOTATED` to `REMOVE`, because bare protein binding is not useful for Pho86's specific ER membrane chaperone/export role. ERG29 (`P40207`) recurs as a reported Pho86 partner in UniProt and GOA, but this preserves only physical-interaction context rather than justifying a generic protein-binding MF.
- `PMID:26928762` has full text locally and remains suitable high-throughput support for ER localization.
- PubMed query for `(Saccharomyces OR yeast) AND (PHO86 OR Pho86 OR YJL117W)` in 2024-2026 returned no direct PHO86 abstracts. Web searches for recent PHO86/Pho86/Pho84/COPII papers likewise found no newer PHO86-specific mechanistic paper that changes the current review; the 2023 PHO84 antisense RNA-seq paper concerns PHO84/SPL2 expression rather than Pho86 function.
