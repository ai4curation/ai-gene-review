# dehH1 (Q7DI61) sequence checks

Script: `compare_entries.py` (fetches both UniProtKB records live from the REST
API; nothing below is hardcoded). Raw run captured in `output.txt`.

## 1. Q7DI61 and Q01398 are the same protein sequence

```
Q7DI61: length=294 crc64=7BA7F07359182703 taxid=80866
Q01398: length=294 crc64=7BA7F07359182703 taxid=118147

sequences identical: True
```

Q7DI61 (TrEMBL, `Q7DI61_DELAC`, *Delftia acidovorans*, NCBITaxon:80866, plasmid
pUO1, from EMBL BAB85585.1/BAC81979.1) and Q01398 (Swiss-Prot, `DEH1_MORSB`,
*Moraxella* sp. strain B, NCBITaxon:118147, plasmid POU1, from EMBL BAA14412.1)
carry byte-identical 294-residue sequences with the same CRC64 checksum. Strain
B was reclassified from *Moraxella* sp. to *Delftia acidovorans*, so the two
accessions are the same `dehH1` gene product of the same strain deposited under
the old and the new organism name. Q01398 is the curated entry (EC 3.8.1.3,
direct protein sequencing, catalytic-site features); Q7DI61 is an uncurated
TrEMBL duplicate.

## 2. Catalytic residues are present

```
position 105: D (context HLVGHDRGGRT)
position 272: H (context SLPGGHFFVDQ)
```

Asp105 sits on a canonical alpha/beta-hydrolase nucleophile elbow
(Sm-X-Nu-X-Sm, here G-H-**D**-R-G) and His272 is retained. These are the two
residues identified experimentally as the catalytic nucleophile and the base
catalyst of this enzyme, so the sequence underlying Q7DI61 is not a degraded or
pseudo-enzymatic copy.

## 3. No evidence of a membrane-spanning segment

```
Kyte-Doolittle candidate transmembrane segments (window 19, mean > 1.6): none
```

A crude hydropathy screen finds no 19-residue window averaging above 1.6, and
neither UniProt record carries a signal peptide, transmembrane feature, or
lipid-anchor site; the only feature is the AB hydrolase-1 domain spanning almost
the whole chain. This is consistent with the soluble, cytoplasmic enzyme
described in the literature and is evidence against the electronically
propagated `GO:0016020 membrane` annotation.

The screen is a cheap heuristic, not a transmembrane predictor; it can only fail
to find a segment, and a negative result is weaker than a dedicated tool would
give. It is used here only as one line of support alongside the published
descriptions of the purified enzyme.
