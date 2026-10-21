# Vmn2r73 (A0A3B2WCZ5) review notes

## 2026-10-20 full re-review

### Product identity

- A0A3B2WCZ5 is 496 aa, Ensembl ENSMUSP00000156768 / transcript ENSMUST00000232965
  (Vmn2r73-203), **not** the Ensembl canonical transcript. The canonical product is
  ENSMUSP00000076687 (ENSMUST00000077478, Vmn2r73-201; 851 aa), UniProt D3Z7M3. Eight
  UniProt TrEMBL entries exist for the locus (475-851 aa) (Ensembl REST lookup; UniProt
  search `gene_exact:Vmn2r73`).
- Re-ran a reproducible global alignment that reads the target sequence from the UniProt flat
  file and the canonical sequence from `Vmn2r73-same-gene-reference.json`
  [file:mouse/Vmn2r73/Vmn2r73-bioinformatics/RESULTS.md "| 1-429 | 1-429 | 429 |"].
  Residues 1-429 are identical; the 9-Cys segment (ref 506-548) is retained at 430-472;
  the remaining 24 residues are a divergent tail. None of the seven reference TM helices is
  retained, and a Kyte-Doolittle 19-residue scan finds no hydrophobic window except the
  signal peptide.
- Conclusion: an alternative-transcript product encoding a soluble ectodomain (signal
  peptide + VFT + NCD), missing the entire 7TM signaling module. It is an isoform of the
  gene in this folder, not a different gene.

### Evolutionary placement

- PANTHER PTHR24061 (CALCIUM-SENSING RECEPTOR-RELATED), subfamily SF413 "VOMERONASAL 2,
  RECEPTOR 66-RELATED". UniProt search for SF413 members returns only rodents (Mus, Rattus,
  Peromyscus, Neotoma, Apodemus, hamsters, jerboa, vole); mouse members are Vmn2r66-Vmn2r79,
  i.e. a rodent-specific family-A V2R expansion. No member of SF413 has experimental data
  and no SF413 member has an IBA/PAINT annotation in GOA for this product.
- Nearest characterised V2Rs are in different subfamilies: Vmn2r116 (E9Q6I0, SF398; ESP1
  receptor), Vmn2r26 (Q6TAC4, SF536), Vmn2r1 (O70410, SF546, family C). Global identity of
  canonical Vmn2r73 to them is 47.6%, 36.8% and 29.6% respectively (scratch alignment,
  consistent with Vmn2r116 being the closest characterised family-A relative). Because they
  are in different PANTHER subfamilies, their ligands (ESP1, MHC peptides) are not
  transferable.
- PANTHER family review `interpro/panther/PTHR24061/PTHR24061-review.yaml` places Vmn2r73 in
  SF413, consistent with UniProt; no disagreement. That review is centred on this truncated
  product.

### Literature

- Falcon deep research: no Vmn2r73-specific ligand, localisation, signaling or knockout data;
  everything is V2R-family inference, and the report treats the canonical 7TM receptor.
- PMID:9288755 (abstract): V2Rs are "seven transmembrane receptors with sequence similarity with
  Ca2+-sensing and metabotropic glutamate receptors".
- PMID:30675062 (full text): class C "VFT is connected to the 7TM domain by means of the CRD,
  which provides a semi-rigid linker between the ligand binding and 7TM (signaling) domains".

### Decisions

- GO:0004930 GPCR activity (IEA InterPro): REMOVE for this product (no 7TM).
- GO:0007186 GPCR signaling (IEA): MARK_AS_OVER_ANNOTATED (accessory role untested).
- GO:0005886 plasma membrane (ARBA SubCell "multi-pass") and GO:0016020 membrane (IEA):
  MARK_AS_OVER_ANNOTATED; product predicted soluble/secreted.
- No core functions asserted: nothing about this product's function is established.
- Previous version of this review and notes was built around a function-prediction
  evaluation; it was rewritten here independently of those predictions and the
  bioinformatics script was changed to take the target sequence from the UniProt record.

### Modules

- No module in `modules/` covers vomeronasal receptors or V2R signaling.
