# LDHD (Q86WU2): placing reported variants on the protein

Inputs were retrieved on 2026-11-26 by `fetch_data.py` (UniProt REST, RCSB PDB, AlphaFold DB v6, NCBI ClinVar E-utilities, gnomAD v4 GraphQL, RefSeq NM_153486.4 and NM_194436.3). Run `just all` to refetch and recompute; `just analyze` recomputes from the downloaded snapshot. Downloaded inputs live in `data/` (git-ignored); every number below is written by a script into `results/`.

| Script | Question | Output |
|---|---|---|
| `isoform_exons.py` | How do the two coding transcripts differ? | `results/isoform_exons.json` |
| `structure_survey.py` | Which residues contact FAD, Mn2+ and D-lactate; where is the isoform-1-only segment? | `results/structure_survey.json` |
| `analyze_variants.py` | Which numbering did each paper use; where is each variant in the structure? | `results/reported_variants_placed.{json,tsv}` |
| `population_variants.py` | What do gnomAD v4 and ClinVar show? | `results/population_variants.json`, `results/*.tsv` |
| `topology_scan.py` | Is there an N-terminal membrane anchor? | `results/topology_scan.json` |
| `mitocarta_lookup.py` | Which sub-mitochondrial compartment does MitoCarta3.0 record? | `results/mitocarta_lookup.json` |

## 1. Two isoforms, two numbering systems

- UniProt displays isoform 1 (Q86WU2-1, 507 aa, NM_153486); the MANE Select transcript NM_194436 encodes isoform 2 (Q86WU2-2, 484 aa).
- The two transcripts have the same 11 exons and differ only in exon 6, which is 269 nt in NM_153486 and 200 nt in NM_194436.
- The extra 69 nt are the first 69 nt of exon 6 and end in AG, so isoform 2 uses an alternative 3' splice site 69 nt downstream of the one used by isoform 1.
- The 69 nt encode residues 211-233 of isoform 1 (FGFWPEIPHHTAWYSPCVSLGRR); isoform 2 numbering equals isoform 1 numbering up to residue 210 and is 23 lower after residue 233.
- Mouse LDHD (Q7TNG8, 484 aa) aligns with human isoform 2 without a gap, so mouse numbering (used in PDB 8JDB-8JDZ and in PMID:37863926) equals human isoform 2 numbering at every position (413 of 484 residues identical).
- None of the eight non-human orthologs examined (mouse, rat, cow, chicken, Xenopus, zebrafish, yeast Dld1, Arabidopsis D-LDH) has residues aligned to the isoform-1-only segment.
- In the AlphaFold model of isoform 1 the segment has mean pLDDT 36.8 (minimum 28.9), against 89.75 for the whole model.
- After superposing the AlphaFold model on PDB 8JDE (0.76 A over 455 CA pairs) the segment comes no closer than 22.8 A to FAD and 26.6 A to D-lactate.
- Conclusion: the isoform-1-only segment is a human-lineage, low-confidence surface insertion far from the active site, and isoform 2 is the form conserved across species.

## 2. Active site in the mouse structure and its human equivalents

PDB 8JDE is wild-type mouse LDHD with FAD, Mn2+ and D-lactate at 1.73 A; chain numbering equals mouse UniProt numbering (checked residue by residue). All 18 mouse LDHD entries are deposited as monomeric assemblies.

| Role in 8JDE | Mouse / human isoform 2 | Human isoform 1 (UniProt) | Distance |
|---|---|---|---|
| Mn2+ ligand | His398 | His421 | 2.26 A |
| Mn2+ ligand | His405 | His428 | 2.32 A |
| Mn2+ ligand | Glu442 | Glu465 | 2.10 A |
| Substrate carboxylate | Arg347 | Arg370 | 2.87 A to D-lactate |
| Catalytic base | His443 | His466 | 2.84 A to D-lactate |
| Flavin and substrate pocket wall | Trp351 | Trp374 | 3.43 A to FAD, 4.11 A to D-lactate |

- D-lactate also coordinates Mn2+ through its carboxylate oxygen (2.09 A) and its C2 hydroxyl (2.04 A).
- Every BINDING and ACT_SITE feature on the human UniProt record (isoform 1 numbering) maps to an identical mouse residue that contacts the stated ligand in 8JDE.

## 3. Reported disease variants

Protein positions are given in both numberings; the literature uses isoform 1 for missense variants.

| Variant (isoform 1) | MANE / mouse | Source | Check against transcripts | Structural context in 8JDE | gnomAD v4 allele frequency | ClinVar |
|---|---|---|---|---|---|---|
| p.Arg370Trp | Arg347 | PMID:31638601 | c.1108C>T fits NM_153486 only | Buried (relative SASA 0.00); guanidinium 2.87 A from the D-lactate carboxylate, salt bridge to Glu277, 4.23 A from Mn2+ | 8.68e-06, no homozygotes | VCV000872931 Pathogenic |
| p.Trp374Cys | Trp351 | PMID:30931947 | c.1122G>T fits NM_153486 | Buried (0.00); 3.43 A from FAD, 4.11 A from D-lactate; packs on Val101, Ser365, Ala353-Leu355 | 6.85e-07 (1 allele) | VCV000586968 Likely pathogenic |
| p.Thr463Met | Thr440 | PMID:30931947 | c.1388C>T fits NM_153486 only | Relative SASA 0.14; 7.69 A from FAD; OG1 hydrogen-bonds Asp367 OD2 (2.70 A) and the backbone N of Gly444 (2.92 A) and His443 (3.28 A) | 1.9e-04 (306 alleles), no homozygotes | VCV000586969 Likely pathogenic |
| p.Thr251Met | Thr228 | PMID:37021930, PMID:34258137 | c.752C>T fits NM_153486 only | Relative SASA 0.07; 5.54 A from FAD; OG1 hydrogen-bonds Ser225 O (2.67 A); contacts Glu226, Gly230 and the C-terminal residues Lys469, Met478, Asn479, Lys482, Val483 | 1.3e-05, no homozygotes | VCV003381192 Pathogenic |
| p.Val69Ala | Val69 | PMID:37021930 | reported as c.206C>T, but both transcripts have T at c.206; rs1035398551 is c.206T>C p.Val69Ala | Buried (0.00) in the FAD-binding domain core, 11.08 A from FAD and 25 A from the substrate | 2.48e-06 (4 alleles) | VCV003381191 Pathogenic |
| c.1363dup | c.1294dup | PMID:37021930 | In NM_153486: Ala455Gly, then 57 aberrant residues, stop after 58 codons, 511-residue product | Replaces the last 53 residues, which carry Glu465, His466 and Asn502 | not in gnomAD | VCV003381194 Pathogenic |
| c.469+1dup | c.469+1dup | PMID:34258137 | c.469 is the last base of exon 4 in both transcripts | Splice donor of exon 4 | 6.85e-07 (1 allele) | VCV003381193 Pathogenic |
| deletion of exons 1-7 | c.1_930del | PMID:40678184 | includes the start codon | No protein expected | not applicable | not found |
| c.561_562del | p.Leu188fs | ClinVar only | frameshift in both transcripts | Truncation within the FAD-binding domain | not looked up | VCV003376153 Likely pathogenic |

Observations that correct or qualify the literature:

- The paper's p.(AlaGly432fsTer58) for c.1363dup mixes numberings: codon 455 is the first changed codon in NM_153486 (c.1363), codon 432 is the same residue in NM_194436 (c.1294), and a new stop after 58 codons is the NM_153486 result (it is 35 codons in NM_194436).
- The c.1363dup frameshift lies in the last exon and predicts a C-terminally altered 511-residue protein lacking the catalytic histidine, not a truncated one.
- The abstract of PMID:37021930 prints the Melanesian variant as c.206C>T; the reference base at c.206 is T in both transcripts and gnomAD and ClinVar record rs1035398551 as c.206T>C p.Val69Ala.
- PMID:38373542 calls the two Monroe variants W323C and T412M; both numbers are 51 lower than the isoform 1 numbers 374 and 463, consistent with numbering from residue 52 of the precursor.
- Thr440 (human Thr463) is the N-cap of the turn carrying Glu442 and His443: its hydroxyl bonds the backbone amides of His443 and Gly444 and the carboxylate of Asp367. A methionine cannot make these bonds, which agrees with the loop-distortion mechanism proposed from mutagenesis of the mouse enzyme.
- Arg347 and Trp351 (human Arg370 and Trp374) line the substrate pocket itself, so the structure supports a substrate-binding defect for R370W and W374C, not a defect of a separate electron-acceptor site.
- Val69 is far from the active site; the only structural reading available for p.Val69Ala is loss of core packing in the FAD-binding domain, and no functional assay of this variant was found.

## 4. Population data

- gnomAD v4 shows no constraint against heterozygous loss of function: pLI = 0.00, LOEUF = 1.36 (58 observed against 52.9 expected), missense Z = -1.30.
- The most frequent stop-gain allele in gnomAD, c.669G>A p.Trp223Ter (563 alleles, frequency 3.5e-04, one homozygote), lies in the isoform-1-only segment and is intronic in the MANE Select transcript, so it is not a loss-of-function allele of the conserved isoform 2.
- Counting only high-confidence pLoF variants of the MANE transcript that pass gnomAD filters gives 137 distinct variants (568 alleles) with a cumulative frequency of 4.8e-04 (carrier frequency about 1 in 1,035) and one homozygous individual (c.835del p.Leu279TrpfsTer5); including six variants flagged AS_VQSR gives 143 variants and 575 alleles.
- Adding the five reported pathogenic missense alleles gives a cumulative frequency of 7.0e-04, which predicts about one biallelic individual per 2.1 million births under Hardy-Weinberg proportions.
- ClinVar holds 129 small LDHD variants: 10 pathogenic or likely pathogenic (8 of them in LDHD itself for lactic aciduria due to D-lactic acid), 91 of uncertain significance, 18 benign or likely benign; 47 further records are large copy-number events spanning the gene.
- ClinVar and gnomAD number LDHD variants on NM_194436 (isoform 2), while every published missense variant is numbered on NM_153486 (isoform 1).

## 5. Membrane anchor (inconclusive)

- A 19-residue Kyte-Doolittle scan finds no window reaching the 1.6 threshold in the first 120 residues of human, mouse or zebrafish LDHD (human maximum 1.18, residues 32-50).
- The same scan also fails to flag yeast Dld1 (maximum 1.06, residues 43-61), so this heuristic cannot distinguish an anchored from a soluble protein in this family and the result says nothing about topology.

## 6. MitoCarta3.0 sub-mitochondrial assignment

- MitoCarta3.0 assigns LDHD to the mitochondrial inner membrane (MIM), with evidence "literature, yeast mito homolog+, mito protein domain, MS/MS++".
- LDHD was detected in neither the APEX matrix proteome nor the APEX intermembrane-space proteome, so MitoCarta3.0 does not say which face of the inner membrane it occupies.
- Comparators in the same table are resolved by proximity labelling: D2HGDH and L2HGDH carry APEX_matrix evidence, and GPD2, which faces the intermembrane space, carries APEX_IMS evidence.
- In the MitoCarta mouse tissue survey the LDHD ortholog was found by MS/MS in kidney, liver, heart, adipose, stomach, placenta and testis (24 unique peptides).

## Limits

- Structural context is read from the mouse enzyme; no experimental structure of human LDHD exists. The four mutated residues with structural readings are identical in human and mouse.
- No free-energy calculation was run; contacts and hydrogen bonds are geometric (3.5 A for polar contacts, 4 A for neighbours).
- The Hardy-Weinberg estimate ignores consanguinity and unreported pathogenic missense alleles, so it is a lower bound on prevalence.
- Deletion and splice variants were not modelled beyond their position in the coding sequence.
