# HP_1507 start site: strain survey, genomic context, domain boundaries

Computed in this job from live public records. Retrieval date: 2026-11-26.
Companion to `hp1507_start_site_analysis.md` and `plot_2.png`.

## 1. Identical Protein Group for WP_015056101.1

`efetch db=protein id=WP_015056101.1 rettype=ipg`

- 78 rows, all *Helicobacter pylori*, 78 distinct assemblies.
- CDS span length: **1200 nt in 78 / 78 entries** (399 codons + stop).
- Strains include 26695, 26695-1, 26695-1CH, 26695-1CL, 26695-1MET, 26695-dR,
  26695-dRdM1dM2, HpGP-26695-ATCC, FDAARGOS_299, Rif1, Rif2, T-2064, PIK2_1, PIK14_1,
  PIK16_1, PIK17_2.

Every genome assembly in RefSeq that carries this exact protein annotates it from the TTG.

## 2. H. pylori strain survey

`esearch db=protein term="Helicobacter pylori[Organism] AND saccharopine dehydrogenase[All Fields]"`
returned **6456** records. A 400-record sample was fetched (POST efetch, FASTA) and filtered
to HP_1507 orthologs by requiring >70 % ungapped identity over the C-terminal 100 residues.
**382** passed.

### Annotated length

| Length | Count | Fraction | N-terminus |
|---|---|---|---|
| 399 aa | 375 | 98.2 % | `MHTVLQIGAGGVGS...` and close variants |
| 380 aa | 6 | 1.6 % | `MGMNRDVFKNII...` (G27-style) |
| 317 aa | 1 | 0.3 % | `MALPYQDLTIMQ...` |
| **385 aa (O26037 form)** | **0** | **0 %** | `MVAHKMGMNRD...` |

### Annotated N-terminal 16-mer

| 16-mer | Count | Contains GxGxxG |
|---|---|---|
| MHTVLQIGAGGVGSVV | 362 | yes |
| MGMNRDVFKNIILASR | 6 | no |
| MHTVLQIGAGGVGGVV | 4 | yes |
| MYTVLQIGAGGVGSVV | 2 | yes |
| MHTVLQIGAGGIGSVV | 2 | yes |
| MHTVLQIGAGGVGSVA | 2 | yes |
| MHTILQIGAGGVGSVV | 1 | yes |
| MHTVLQIGSGGVGSVV | 1 | yes |
| MHTVLQIGAGGVGSVL | 1 | yes |
| MALPYQDLTIMQACLE | 1 | no |

The 6 entries at 380 aa carry ENA/DDBJ submitter protein accessions
(GAB0021728.1, GAA8843083.1, GAA9571442.1, GAA9436210.1, GAA8419539.1, GAA9344715.1),
not RefSeq PGAP accessions.

**375 / 382 = 98.2 % of H. pylori annotations begin at the position equivalent to M1 of the
399-residue form. The 385-aa O26037 start is reproduced by none of them.**

Caveat: the 400-record sample is an arbitrary slice of 6456 records and is not a random
sample of distinct strains; many records may come from closely related isolates. The
direction of the result is unambiguous but the exact percentage should not be quoted as a
population frequency.

## 3. Genomic context (NC_000915.1 feature table, 1578000..1582500)

| Locus | Coordinates | Strand |
|---|---|---|
| HP_RS07450 | 1578000..1578971 | - |
| HP_RS07455 / HP1506 `gltS` | 1578968..1580194 | - |
| **HP_RS07460 / HP1507** | **1580280..1581479** | **+** |
| HP_RS07465 / HP1508 `ccoG` | 1581489..(1582500) | - |

- HP1506 and HP1507 are **divergent**; intergenic region 1580195..1580279 = **85 bp**.
- The proposed TTG start at 1580280 is the **first base after** the intergenic region.
- The first in-frame upstream stop (TAA at 1580229) lies **inside** the intergenic region,
  so the extended CDS does not overlap `gltS`.
- The annotated GTG at 1580322 would leave a 127 nt region between the intergenic boundary
  and the start codon.

## 4. InterPro / Pfam boundaries

| Entry | Length | PF03435 (NADP-binding) | SSF51735 (Rossmann) | PF16653 (C-terminal) |
|---|---|---|---|---|
| H. mustelae D3UGV5 | 399 | 1-134 | 1-191 | 141-389 |
| H. cetorum I0ESJ2 | 399 | 4-135 | 2-190 | 141-392 |
| H. acinonychis Q17ZI8 | 399 | 4-135 | 2-190 | 141-392 |
| H. pylori 26695 O26037 | 385 | 2-120 | 15-176 | 127-378 |
| O26037 **mapped to 399 numbering (+14)** | | **16-134** | **29-190** | **141-392** |

- PF03435 N-terminal boundary: 12 residues later in O26037 than in the orthologs.
- SSF51735 N-terminal boundary: 27 residues later.
- Both C-terminal boundaries agree within 1 residue; PF16653 agrees exactly (141-392).

Only the N-terminal boundary of the cofactor-binding domain differs, by the size of the
annotation discrepancy. The GxGxxG fingerprint at positions 8-13 falls outside the O26037
match entirely.

## 5. Transcriptional evidence not retrieved

The H. pylori 26695 primary transcriptome (dRNA-seq, Sharma et al., PMID 20164839; protocol
and browser in Bischler et al., PMID 26091613) maps transcription start sites genome-wide and
would give the 5' UTR of this transcript directly. The TSS table was not retrieved
programmatically in this job, so no statement is made about the TSS position upstream of
1580280. This remains the most direct unexercised test.

## 6. Tools that could not be used

- No N-terminomics / ribosome-profiling dataset for H. pylori was located through PubMed
  search; none is quoted.
- UniProt holds no entry for the 399-residue 26695 protein (A0A2X5A3P4 was deleted as
  "Not part of a reference proteome"); its sequence was obtained from UniParc UPI000D224D86.
