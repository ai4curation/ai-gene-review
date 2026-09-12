# PET117 (Q6UWS5) review notes

## Summary of function

PET117 (Protein PET117 homolog, mitochondrial; HGNC:40045; gene MIM 614771) is a small
(81 aa) nucleus-encoded mitochondrial protein that acts as an **assembly chaperone for
cytochrome c oxidase (COX / mitochondrial respiratory chain complex IV)**. It is the human
ortholog of *S. cerevisiae* PET117, a known COX assembly factor. It is **non-catalytic**: it
carries no enzyme domain and functions as an assembly/stabilization factor, not an enzyme.

The mature protein is short with a predicted N-terminal mitochondrial transit peptide (aa
1–22) and a single Pfam PET117 domain (PF15786; InterPro IPR031568). AlphaFold/SMR models a
predominantly coiled-coil fold, consistent with a small coiled-coil scaffold/chaperone.

## Provenance / key evidence

- **Ortholog prediction + mitochondrial localization (IDA):** PET117 (LOC100303755) is the
  human ortholog of yeast PET117 ("Assembly of COX"), and GFP-tagged human PET117 co-localizes
  with a mitochondrial marker in live HEK293 cells.
  [PMID:22356826 "AURKAIP1-, C7orf44-, C12orf62- and PET117-GFP) co-localize with the mitochondrial marker"]
  The same study co-purified the COX assembly factor COX17 with PET117-TAP as bait, linking it
  to the COX assembly machinery. [PMID:22356826 "When using PET100, PET117, C7orf44 and C12orf62 as bait, the COX17 protein was co-purified"]

- **Role in module-based COX assembly (IDA):** In a quantitative-MS reconstruction of the human
  COX assembly pathway, PET117 acts together with the highly conserved PET100 chaperone (and the
  newly identified MR-1S) to assist COX biogenesis.
  [PMID:28199844 "works with the highly conserved PET100 and PET117 chaperones to assist COX biogenesis in higher eukaryotes"]
  Abstract-only cache; the annotation is an experimental IDA made by a curator with full-text access.

- **COX1 synthesis regulation via TACO1 (IDA):** PET117 depletion reduces the mitochondrial
  oxygen consumption rate and impairs mitochondrial function; PET117 stabilizes the COX1
  translational activator TACO1 and prevents its ubiquitination, thereby supporting COX1 (a
  mtDNA-encoded core subunit) synthesis.
  [PMID:37247699 "PET117, a chaperone protein involved in complex IV assembly, in the regulation"]
  [PMID:37247699 "Depletion of PET117 reduced mitochondrial oxygen consumption rate and impaired mitochondrial function"]
  Abstract-only cache.

- **High-throughput mitochondrial proteome (HTP):** PET117 is a member of the high-confidence
  human mitochondrial proteome. [PMID:34800366 — MS-based mitochondrial proteome inventory]

- **Disease:** Biallelic PET117 variants cause Mitochondrial complex IV deficiency, nuclear
  type 19 (MC4DN19; MIM 619063), an autosomal recessive disorder with global developmental
  delay, developmental regression, and complex IV deficiency; the reported variant deletes the
  C-terminal residues 58–81 (PMID:28386624, not in GOA/cache but recorded in UniProt).
  [file:human/PET117/PET117-uniprot.txt "Missing (in MC4DN19)"]
  (A pituitary/other phenotype has also been discussed in the broader literature; the
  canonical UniProt disease is the MC4DN19 neurodevelopmental phenotype.)

## Curation decisions

All 8 GOA lines are ACCEPTed:
- GO:0033617 (mito resp chain complex IV assembly) — core BP. Two experimental IDAs
  (PMID:28199844, PMID:37247699) plus a PAN-GO IBA converge here.
- GO:0005739 (mitochondrion) — multiple IDA/HTP/IEA/IBA; accepted. The finer inner-membrane
  location (GO:0005743) is captured in core_functions.located_in.

No molecular function is asserted: PET117 is non-catalytic and has only chaperone/scaffold
activity; no informative MF term is supported by experimental data (interactions are with
COX17/TACO1 but the only candidate MF would be bare protein binding, which is uninformative
and per policy omitted from core_functions).

## core_functions
- BP: GO:0033617 mitochondrial respiratory chain complex IV assembly (directly_involved_in)
- CC: GO:0005743 mitochondrial inner membrane (located_in) — COX assembly occurs in the inner
  membrane; PET117 is an inner-membrane-associated assembly chaperone.
- MF: omitted (non-catalytic; only bare protein binding would apply).
