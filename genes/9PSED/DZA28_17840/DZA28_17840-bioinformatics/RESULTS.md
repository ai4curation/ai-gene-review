# DZA28_17840 bioinformatics: domains, homology, topology and genomic context

Query: dashboard sequence NZ_CP015876.1_2730 (P. putida SJTE-1, 412 aa), reviewed as
A0ABY3D9I3 (P. alloputida B2017, DZA28_17840). All numbers are from `results.json`,
produced by `just all` and recorded as BERIL run
`20261030T213529Z-dza28-17840-domains-homology-context` (projects/hackathon).

Method: pyhmmer hmmsearch with Pfam PF02308 (MgtC) and PF13194 (DUF4010) HMMs from InterPro;
Biopython PairwiseAligner (BLOSUM62, gap open -10, extend -0.5) for identities; pyhmmer
phmmer (E < 1e-5) against the P. aeruginosa PAO1 reference proteome (UP000002438); NCBI
RefSeq GenBank NZ_CP015876.1 for context.

## Identity to the review accession

The query is 98.8% identical to A0ABY3D9I3 over all 412 residues (407/412), with no gaps.

## Domain architecture

| Domain | Query envelope | HMM coverage | Score / i-E-value |
|---|---|---|---|
| PF02308 MgtC N-terminal | 11-129 | 3-120 of 121 | 58.3 / 2.9e-19 |
| PF13194 DUF4010 | 177-387 | 1-208 of 210 | 133.9 / 2.1e-42 |

For comparison, the same PF02308 model scores 136.0 on Salmonella MgtC (D0ZLQ7), 131.5 on
E. coli YhiD (P0AFV2) and 117.8 on M. tuberculosis MgtC (I6YBN6). The query's MgtC N-terminal
module is therefore a divergent member of the family (score 58.3). The query lacks the
cytoplasmic C-terminal domain of canonical MgtC; its C-terminal half is the DUF4010 module.
Aquifex aeolicus aq_1828 (O67688), the only Swiss-Prot member of PANTHER PTHR39084, is a
stand-alone DUF4010 protein (PF13194 score 182.5) with no PF02308 hit.

Pairwise identities to the characterized MgtC-family proteins are low: Salmonella MgtC 31.5%
over 222 globally aligned pairs (17.0% of query length); E. coli YhiD 30.6% over 206; M.
tuberculosis MgtC 34.7% over 216. None of these is a credible ortholog.

## Topology

DeepTMHMM (dashboard evidence) predicts 13 TM helices with no signal peptide: 5 inside the
PF02308 envelope and 6 inside the DUF4010 envelope. UniProt's Phobius calls 7. The protein is
a polytopic inner-membrane protein; both modules are membrane-embedded.

## P. aeruginosa PAO1 homolog

The best PAO1 hit is PA0043 (Q9I789, 460 aa; phmmer E = 8.4e-35, score 118.9), with 42.0%
identity over 362 aligned pairs (query 13-403 to subject 57-459). This is the "34.3%-identity
P. aeruginosa homolog" in the dashboard's PaperBLAST evidence (PMID:27150578).

## Genomic context in P. putida SJTE-1

The query is A210_RS13675 (WP_014756724.1, "MgtC/SapB family protein"), minus strand,
3007449-3008687; its RefSeq translation is identical to the dashboard sequence. It is CDS
number 2749 on the chromosome.

- Neighbours: directly upstream on the same strand is A210_RS13680, a Crp/Fnr family
  transcriptional regulator FnrC (3008672-3009493), overlapping the query by 16 bp, so the
  two are probably co-transcribed. The STRING partner of the 90% homolog is likewise a
  Crp/Fnr family regulator. Further away are two universal stress proteins (A210_RS13690,
  A210_RS13700) and GNAT acetyltransferases. On the other side lie the paaX/paaY regulators and
  the paa phenylacetate-degradation genes (PaaF, PaaG, PaaH, PaaI, 3-oxoadipyl-CoA thiolase,
  PaaK, PaaA, PaaB).
- No integrase, transposase, phage, recombinase or tRNA feature lies within 25 kb on either
  side.
- Gene GC is 60.6%, against a CDS mean of 61.8% (SD 4.1%), z = -0.3. The 50-kb window is 62.6% GC.
- There is no sign of a recent mobile element or genomic island. However, the UniProt mapping
  step's phmmer search found no homolog (E < 1e-5) in the KT2440 (UP000000556), NBRC 14164
  (UP000016702), P. putida UP000218731 or P. plecoglossicida (UP000234744) reference
  proteomes. The gene is therefore strain-variable (accessory), even though it sits in an
  ordinary chromosomal locus with no island signature.
