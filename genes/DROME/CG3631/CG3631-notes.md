# CG3631 (Q95T10) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q95T10 is the reviewed Swiss-Prot canonical entry (XYLK_DROME, 421 aa, sequence version 1)
for FBgn0038268. Full-length precursor: signal peptide 1-21, FAM20 C-terminal kinase domain (PF06702,
IPR009581) with UniProt-annotated ATP-binding (131, 147, 252-255, 319, 329), Mn2+-binding (166, 329) and
active-site (314) residues. Not a fragment, isoform or alternative gene model.

Phylogenetic placement (PANTHER 19.0 classification files):
- CG3631 Q95T10 -> PTHR12450:SF14 GLYCOSAMINOGLYCAN XYLOSYLKINASE, together with human FAM20B (O75063),
  mouse Fam20b (Q8VCS3), zebrafish fam20b (Q5RH51).
- Fly paralog CG31145 (A4VCL2) -> SF22 with worm famk-1; FAM20C proteins -> SF11; FAM20A -> SF12.
- Four-jointed (fj, P54360) -> PTHR13147, a different family.
So the closest experimentally characterised relative is human FAM20B (O75063); no review of FAM20B
(or mouse/zebrafish orthologs) exists in genes/.

Literature:
- [PMID:22900076 "CG3631, which is most closely related to FAM20B"]; tagged CG3631 in S2 cells
  ["CG3631 overlapped both ER and Golgi markers, and was not detectably secreted from S2 cells"].
  The only fly kinase activity reported is for the paralog ["Drosophila CG31145 also has Casein kinase
  activity (not shown)."].
- [PMID:19473117 "we identified FAM20B as a kinase that phosphorylates the xylose residue in the linkage
  region"] (abstract only).
- [PMID:29572475 "xylose phosphorylation within the tetrasaccharide linker region of CS and HS
  proteoglycans has also been demonstrated in Drosophila , and this activity can probably be ascribed to Fam20B"].
- No CG3631 enzyme assay or mutant phenotype found (deep research falcon file concurs).

Decisions:
- ISS GO:0004674 (with fj): REMOVE. Cross-family similarity transfer from a protein kinase; FAM20B
  subfamily phosphorylates glycan xylose; PAINT gave the FAM20B branch only GO:0016773.
- IBA GO:0016773: ACCEPT (no more specific GO MF term for linker-xylose 2-O-kinase exists; suggested
  question raised).
- IBA GO:0030166 (FAM20B-branch node PTN002488224, zebrafish fam20b donor): ACCEPT; the enzyme performs a
  linker step (participation, not mere requirement).
- ER and Golgi (IDA + IEA from UniProt SubCell citing the same paper): ACCEPT.

Family review interpro/panther/PTHR12450/PTHR12450-review.yaml places Q95T10 in SF14 as its reference
protein; no disagreement. Its GO:0004674 assessment is UNRESOLVED and does not scope the term onto SF14.

Modules: modules/dmel_glycosaminoglycan_biosynthesis.yaml models the fly linker steps (Oxt, galactosyl-
and glucuronosyltransferases) but has no xylose 2-O-phosphorylation step; CG3631 is a candidate part
there (not added; curation gap only).
