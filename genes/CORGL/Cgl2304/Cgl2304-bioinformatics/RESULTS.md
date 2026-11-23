# Cgl2304 (Q8NNA0): comparison with characterised maltokinases, catalytic residues and gene context

Query: dashboard sequence NZ_CP025533.1_2296, identical to UniProt Q8NNA0 (363 aa;
`query_identical_to_Q8NNA0: true`).

Scripts (run from `projects/hackathon/` with `uv run beril run`):

- `mak_comparison.py` (run `20261030T233147Z-cgl2304-mak-comparison`): downloads the query and
  reference sequences from UniProt; global alignments with free end gaps (Biopython
  PairwiseAligner, BLOSUM62, gap open -10, extend -0.5); maps published Mak residues onto the
  query; regex motif scan; pyhmmer hmmsearch with Pfam PF18085 (Mak_N_cap) and PF01636 (APH).
- `genome_context.py` (run `20261030T233251Z-cgl2304-genome-context`): NCBI GenBank region of
  NC_003450.3 around the gene, in-frame upstream extension check, UniRef50 and COG3281 lengths.

Outputs are copied to `data/`.

## 1. Similarity to characterised maltokinases

| Reference | Length | Identity over aligned pairs | Query coverage |
|---|---|---|---|
| A1TH50 Mak, *M. vanbaalenii* (crystal structure 4U94) | 441 | 43.5% (144/331) | 91.2% |
| O07177 Mak (Pep2), *M. tuberculosis* Rv0127 | 455 | 42.9% (148/345) | 95.0% |
| Q7U2S7 Mak, *M. bovis* (identical to the BCG enzyme) | 455 | 42.9% (148/345) | 95.0% |
| A0R6D9 Mak/Pep2, *M. smegmatis* MSMEG_6514 | 441 | 39.5% (137/347) | 95.6% |
| Q7WUM3 Mak1, *Actinoplanes missouriensis* | 437 | 42.0% (149/355) | 97.8% |
| Q7AKG7 Pep2A, *S. coelicolor* SCO5441 | 464 | 40.7% (146/359) | 98.9% |
| Q8NNA1 TreS, *C. glutamicum* Cgl2303 (control) | 598 | 28.7% (90/314) | 86.5% |

Cgl2304 is about 40-44% identical to all six characterised maltokinases over 91-99% of its length.

## 2. Catalytic and substrate-binding residues

Residues named in the *M. vanbaalenii* Mak structure paper (PMID:25619172), mapped through the
A1TH50 alignment:

| Mvan Mak residue | Role | Cgl2304 |
|---|---|---|
| Glu134, Gln135, Ser136, Asn137 | P-loop (AEQSNTSV), gamma-phosphate | Glu89, Gln90, Ser91, Asn92 (conserved) |
| Lys149 | invariant ATP alpha-phosphate lysine | Lys105 (conserved) |
| Arg152 | strictly conserved cap/intermediate interface | Arg108 (conserved) |
| His303, Gly304, Asp305 | catalytic loop HGD, Asp305 catalytic base | His246, Gly247, Asp248 (conserved) |
| His307, Gln310 | catalytic loop; Gln310 Mg ligand | His250, Gln253 (conserved) |
| Asp322, Phe323, Glu324 | DFE motif, Asp322 Mg-binding | Asp265, Phe266, Glu267 (conserved) |
| Arg334 | stabilises DFE Glu | Arg277 (conserved) |
| Arg267, Arg342 | basic residues of maltose pocket | Arg211 (conserved); Lys285 (Arg->Lys) |
| Lys413, Tyr416, Tyr420 | maltose binding (alanine mutants practically inactive) | Lys335, Tyr338, Tyr342 (conserved) |
| Asp88, Asp92 | strictly conserved, cap/intermediate salt bridges | not aligned (cap region divergent) |

The catalytic loop of Cgl2304 is HGDLHLGQ (residues 246-253). It is identical to the loop of
every reference maltokinase (Mvan 303, Mtb 320, M. smegmatis 302, Actinoplanes 303,
S. coelicolor 335). As in all maltokinases, the position of the canonical Brenner-motif Asn
(HxDxxxxN) is a Gln (Gln253 = Mvan Gln310, the Mg1 ligand), so the strict HxDxxxxN pattern
matches none of the seven sequences. The Mg-binding DFE motif is at 265-267 (Mtb Asp339, whose
D339N mutant is inactive, maps to Asp265). All four Mtb positions tested by mutagenesis (Ser144,
Asn145, Asp339, Arg351) are conserved (Ser91, Asn92, Asp265, Arg277).

## 3. N-terminal cap subdomain

The Pfam Mak_N_cap HMM (PF18085) hits all six reference maltokinases (domain i-E-values
1e-29 to 9e-17, envelopes starting at residues 8-26) but gives no hit on Cgl2304. The Pfam APH
HMM (PF01636) hits Cgl2304 at residues 83-319 (i-E-value 2.6e-07), like the Mtb Mak (248-400).
In the alignment with A1TH50 the first ~88 query residues align only patchily to the Mak cap
region, with long gaps; Mvan Asp88 and Asp92 have no query counterpart. Cgl2304 therefore has a
shortened, divergent N-terminal region in place of the ~88-residue cap subdomain. This accounts
for most of the length difference from the ~440-455 aa maltokinases.

## 4. Gene model and genomic context

- Cgl2304 (RefSeq CGL_RS11420, old tag NCgl2222, WP_011015024.1) is at NC_003450.3
  2439907-2440998 (+), 363 aa, start codon ATG.
- The upstream gene treS (CGL_RS11415, NCgl2221, maltose alpha-D-glucosyltransferase) is on the
  same strand and ends at 2439910. The two CDSs overlap by 4 nt (gap_to_next = -4), the ATGA
  overlap typical of translationally coupled genes.
- The query's reading frame extends only 5 codons upstream of the annotated ATG before an
  in-frame stop codon, with no alternative start codon. An N-terminal extension that could
  encode a full cap subdomain is therefore impossible; the 363-aa model is not truncated at the
  N-terminus.
- Downstream, idi (Cgl2305) is on the opposite strand.
- Short COG3281 proteins of similar length occur in other corynebacteria (for example C.
  efficiens Q8FND8, 362 aa; C. callunae M1UMH1, 365 aa; C. durum L1MDT9, 361 aa; C. imitans
  A0A076NL10, 361 aa). All 25 Corynebacterium COG3281 entries in UniProt are 400 aa or
  shorter. In Mycobacteriales as a whole, 16 of 52 such entries are 401-460 aa. The short form is
  typical of the genus. UniRef50_Q8NNA0 has only two members (Q8NNA0 and the identical-length
  [Brevibacterium] flavum A0A0F6Z6G4).

## Conclusion

Cgl2304 is a maltokinase homolog with every catalytic, Mg-binding, nucleotide-binding and
maltose-binding residue examined conserved, and its catalytic loop is identical to that of all
characterised maltokinases. It is encoded immediately downstream of treS with a 4-nt
translational-coupling overlap, the same treS-mak arrangement as in mycobacteria. The protein
lacks the Mak N-terminal cap subdomain signature. This is a genus-typical feature, not a
truncated gene model. Whether the missing cap affects activity or binding to TreS is untested.
