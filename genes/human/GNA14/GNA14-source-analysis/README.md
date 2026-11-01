# Human G14 construct provenance in the muscarinic BRET panel

This analysis distinguishes a traceable human construct from a sequence-verified assay of canonical UniProt O95837. No sequence comparison of the actual assayed plasmid was performed.

## Evidence chain

1. **PMID:38671143**, normally cached in `publications/PMID_38671143.md`, assays M1/M3-driven G14 activation with a heterotrimer BRET readout. Its BRET-method references include the platform protocol **PMID:26260597**. The G14 experiments use Ric8A coexpression and PTX-related controls; the separate human Gi/o purification paragraph does not establish G14 species.
2. The underlying platform primary **PMID:26628681**, normally cached in `publications/PMID_26628681.md`, explicitly states: “pcDNA3.1+ plasmids encoding GαoB, Gαz, Gα11, Gα14, Gα15, Gαs long isoform (GαsL), Gαolf, and Gα13 were purchased from the Missouri S&T cDNA Resource Center.” Its phylogenetic-analysis section separately lists human Gα14 NM_004297; that list describes the phylogeny and is not an assay-plasmid sequence verification.
3. The supplier's authoritative catalog, [cDNA Resource Center catalog](https://www.cdna.org/files/catalog.pdf), lists **GNA1400000**, **GenBank AF493903**, as human wild-type G-protein alpha14 in pcDNA3.1+, amplified from IMAGE clone299064. The catalog also lists modified Q205L and epitope-tagged derivatives separately. This supports the human wild-type provenance inference when combined with the platform's named vendor/vector, but the 2024 article does not identify a catalog number or provide its assayed sequence.
4. The 2024 supplementary PDF was inspected separately and did not resolve an accession/plasmid-sequence identifier. No statement here treats that absence as evidence of a nonhuman construct.

## Conclusion and limits

The experiment supports muscarinic-receptor-dependent activation of the reported G14 construct in a reconstituted cellular system. The source chain supports a **human-construct inference**, not demonstrated sequence identity of the actual sample to O95837. It is not an assay of purified receptor–G14–PLC chemistry or native human tissue wiring. Independent **PMID:26377666** explicitly studies human G14/Gz chimeras and establishes PLCbeta/IP3 effector activation; that separate assay should not be silently merged with the muscarinic BRET experiment.

## Reproduction

Run `python recover_provenance.py`, then `pdftotext -layout Missouri-cDNA-catalog.pdf Missouri-cDNA-catalog.txt`. The retrieval script uses the original supplier URL and writes URL, retrieval time, SHA256 and byte count to `supplier-provenance.json`. The full catalog is retained to avoid selectively reconstructing a two-column PDF. Relevant product entries occur around lines1813–1819 of the layout-preserving extraction. PubMed sources were fetched through the repository's normal cache tooling; no cached publication text was hand-edited.
