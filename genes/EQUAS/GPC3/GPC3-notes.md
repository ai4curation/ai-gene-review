# GPC3 (donkey, Equus asinus; UniProt A0A9L0J2B1) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl ENSEASP00005043430.1), 565 aa: `GPC3-uniprot.txt`.
- Donkey GOA: 8 IEA rows (5 TreeGrafter GO_REF:0000118 from PANTHER:PTN001327382; 2 InterPro2GO GO_REF:0000002 from IPR001863; plasma membrane via GO_REF:0000120).
- Human GPC3 (P51654) UniProt record fetched 2026-10-14: `GPC3-bioinformatics/human-GPC3-P51654-uniprot.txt`.
- Alignment: `GPC3-bioinformatics/RESULTS.md`.
- Cached publications (already present in `publications/`): PMID:24496449 (GPC3 binds Frizzled; abstract only), PMID:14610063 (furin processing of GPC3; full text), PMID:17549790 (GPC3 inhibits CD26/DPP4; abstract only).
- Human QuickGO (2026-10-14) comparator: IDA positive regulation of canonical Wnt signaling (PMID:24496449); IBA extracellular region, plasma membrane, cell surface, cell migration, regulation of protein localization to membrane; ISS negative regulation of smoothened signaling pathway; the extracellular matrix and regulation of signal transduction rows on human GPC3 are InterPro2GO only.

## Sequence

- [RESULTS.md "The donkey GPC3 protein matches human GPC3 at 92.61% identity over 555 paired residues"]
- [RESULTS.md "The furin-like cleavage site (human R358/S359), the two heparan sulfate attachment serines (human S495, S509) and the GPI-anchor asparagine (human N554) are all conserved in the donkey sequence."]

## Function

- GPI-anchored heparan sulfate proteoglycan [human UniProt "Cell membrane {ECO:0000269|PubMed:14610063}; Lipid-anchor, GPI-anchor"].
- Wnt: [PMID:24496449 "GPC3 stimulates HCC growth by promoting canonical Wnt signaling."]; [human UniProt "Positively regulates the canonical Wnt signaling pathway by binding to the Wnt receptor Frizzled"].
- Hedgehog: [human UniProt "Negatively regulates the hedgehog signaling pathway when attached via the GPI-anchor to the cell surface by competing with the hedgehog receptor PTC1 for binding to hedgehog proteins"] (by similarity to mouse).
- Processing: [PMID:14610063 "This processing is essential for GPC3 modulating Wnt"]; cell movements [PMID:14610063 "for supporting embryonic cell movements"].
- Shedding: [human UniProt "leading to its shedding from the cell surface"].

## Review decisions (summary)

- plasma membrane, cell surface, positive regulation of canonical Wnt signaling: ACCEPT.
- extracellular region (shed form), cell migration, regulation of protein localization to membrane: KEEP_AS_NON_CORE.
- regulation of signal transduction: TOO_GENERAL (entailed by positive regulation of canonical Wnt signaling, and by the NEW Hh term).
- extracellular matrix: MARK_AS_OVER_ANNOTATED (GPC3 is GPI-anchored to the cell surface, not an ECM constituent; InterPro2GO family mapping).
- NEW: negative regulation of smoothened signaling pathway (GO:0045879).
