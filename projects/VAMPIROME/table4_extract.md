# Vampirome Table 4 Extract (DESRO)

Source: Table 4 and surrounding text from the Vampirome transcriptome/proteome paper on Desmodus rotundus salivary glands. [PMC3685427](https://pmc.ncbi.nlm.nih.gov/articles/PMC3685427/)

Notes:
- IDs below are Vampirome transcript IDs (BatTrinityAbyss-* or DrSigp-SigP-*). They are *not* HGNC/UniProt gene symbols and require mapping.
- This is an extract focused on immune/hemostasis/host-modulating candidates. It is not the full supplemental dataset.
- The original condensed table and supplemental spreadsheet are referenced by the paper but currently hosted on a moved NIAID portal; add them once accessible.
- Mapped TSA/UniProt accessions for the IDs in this list are in `projects/VAMPIROME/uniprot_mapping.md` (generated via NCBI TSA + UniProt REST).

## Candidate transcript seeds (immune/hemostasis relevant)

### Platelet function / coagulation / hemostasis
- Phosphatase: BatTrinityAbyss-508800 (Comments/Target: platelet function)
- Apyrase: BatTrinityAbyss-537653 (Comments/Target: platelet function)
- Plasminogen activator: BatTrinityAbyss-499018 (Comments/Target: fibrinolytic)
- Clotting pathway proteases: BatTrinityAbyss-499228, BatTrinityAbyss-489254 (Comments/Target: protease)
- TFPI-like Kunitz inhibitor: BatTrinityAbyss-523646 (Kunitz; TFPI-like per paper text)

### Neutrophil/innate immune modulation
- DNase: BatTrinityAbyss-499100, BatTrinityAbyss-532109 (Comments/Target: neutrophil function)

### Vascular/angiogenesis modulators
- ADAMTS-1 metalloprotease: BatTrinityAbyss-517665, BatTrinityAbyss-521171 (Comments/Target: angiogenesis)
- PACAP: BatTrinityAbyss-500584 (vasodilatory neuropeptide in paper text)
- C-type natriuretic peptide (CNP): BatTrinityAbyss-538594 (vasodilation in paper text)

### Lipid mediator/ligand binding
- Lipocalins: BatTrinityAbyss-466603, BatTrinityAbyss-495622, BatTrinityAbyss-496761, BatTrinityAbyss-495626, BatTrinityAbyss-495631, BatTrinityAbyss-495624
- Secretoglobin: BatTrinityAbyss-500441 (mentioned in paper text)

### Antigen-5/CRISP (CAP family)
- Antigen-5/CRISP: BatTrinityAbyss-495870

### Cytokine/chemokine-like or inflammatory modulators
- CCL28-like: BatTrinityAbyss-506850
- TNF-inducible gene (TSG-6-related): BatTrinityAbyss-527888, BatTrinityAbyss-509950
- Lymphotoxin: BatTrinityAbyss-86412

### Antimicrobial proteins (accessory gland enriched)
- Defensin: BatTrinityAbyss-401005
- Lysozyme: BatTrinityAbyss-500942
- BPI/LBP/CETP-like: BatTrinityAbyss-429618

### Protease inhibitors (multiple families)
- Kunitz-type protease inhibitor: BatTrinityAbyss-541822
- Cystatin: BatTrinityAbyss-41885
- Kazal domain inhibitor: BatTrinityAbyss-36340
- TIL domain inhibitor: DrSigp-SigP-495835
- Serpins: BatTrinityAbyss-548577 (neuroserpin), BatTrinityAbyss-518161 (alpha-1 antitrypsin), DrSigp-SigP-532391 (protease C1 inhibitor), BatTrinityAbyss-543253, BatTrinityAbyss-25903
- Metalloprotease inhibitor domain: BatTrinityAbyss-534229, BatTrinityAbyss-37180
- Other inhibitors: BatTrinityAbyss-8258 (alpha-macroglobulin), DrSigp-SigP-210264 (endopeptidase inhibitor), BatTrinityAbyss-321620 (inter-alpha-trypsin inhibitor), DrSigp-SigP-36965 (peptidase inhibitor)

### Other enzymatic candidates noted in Table 4
- Sphingomyelinase: BatTrinityAbyss-549118
- Epoxide hydrolase: BatTrinityAbyss-508632
- Dipeptidyl peptidase: BatTrinityAbyss-561424

## TODO
- Retrieve and parse the full condensed table (Table4-web.xlsx) and supplemental spreadsheet (Supplemental-web.xlsx) from the moved NIAID transcriptome resources.
- Map transcript IDs to DESRO gene symbols/UniProt accessions.
