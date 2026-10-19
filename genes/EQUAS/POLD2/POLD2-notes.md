# POLD2 (donkey, A0A9L0IND0) notes

## 2026-10-14 DONKEY40 review

- Record: TrEMBL, 487 aa, "DNA polymerase delta subunit 2" (name from ARBA), Ensembl gene model from the donkey genome project (PMID:33293529, genome sequencing only; no functional experiment on donkey POLD2). All 14 GOA rows are electronic (InterPro2GO, ARBA, TreeGrafter GO_REF:0000118, Ensembl Compara GO_REF:0000107 from human P49005, combined GO_REF:0000120, SubCell GO_REF:0000044).
- Sequence: 95.52% identity to human POLD2 P49005 over the full human length; donkey has an 18-aa N-terminal extension only [file:EQUAS/POLD2/POLD2-bioinformatics/RESULTS.md "The donkey sequence A0A9L0IND0 (487 residues) aligns to human P49005 (469 residues) with 95.52% identity among 469 paired residues."]. Function transfer from human is therefore well justified.
- Human POLD2 is the B subunit of Pol delta and shared accessory subunit of Pol zeta:
  - [file:EQUAS/POLD2/POLD2-bioinformatics/human-P49005-uniprot.txt "Accessory component of both the DNA polymerase delta complex and the DNA polymerase zeta complex"]
  - [PMID:31449058 "The mammalian polymerase δ complex is a heterotetramer consisting of the catalytic subunit POLD1 and the accessory subunits POLD2, POLD3, and POLD4"]
  - [PMID:24449906 "The purified four-subunit Pol ζ4 (Rev3–Rev7–PolD2–PolD3) is much more efficient and more processive at bypassing a 1,2-intrastrand d(GpG)-cisplatin cross-link than the two-subunit Pol ζ2 (Rev3–Rev7)."]
  - [PMID:22465957 "the B-subunit of Pol δ binds equally well to the catalytic subunit of either Pol δ or Pol ζ"]
  - Pol eta binds POLD2 [PMID:25662213 "Only POLD2, the B-subunit of Polδ, was found to bind to Polη in a two-hybrid experiment"]
- POLD2 itself has no polymerase active site; it contributes to DNA-directed DNA polymerase activity of the holoenzyme. The PolD2/PolD3 cocrystal shows no obvious DNA-binding surface [PMID:24449906 "shows a primarily negatively charged molecular surface without obvious features for DNA binding"] -> InterPro2GO DNA binding is an over-annotation (same call as the human review genes/human/POLD2).
- Repair: Pol delta carries out NER synthesis and BIR [human UniProt "DNA polymerase delta carries out approximately half of nucleotide excision"].
- Enzyme activator activity (Ensembl from human): POLD2/POLD3 increase Pol zeta efficiency, but as integral accessory subunits of the polymerase complex, not as a separate regulator; marked as over-annotation.
- ProtNLM2 GO: DNA replication (LSP, exact term in GOA, less specific than DNA strand elongation involved in DNA replication) and DNA repair (COR; absent from donkey GOA; error-prone TLS is under DNA damage tolerance, not DNA repair, in GO; checked with QuickGO ancestors).
