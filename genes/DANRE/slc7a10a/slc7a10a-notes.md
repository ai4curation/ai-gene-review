# slc7a10a notes

## Setup and provenance

- Fetched with `just fetch-gene` on G8JL19 (TrEMBL, 511 aa); 10 GOA rows (5 IBA, 5 IEA), none with a PMID. ZFIN
  ZDB-GENE-080116-1, Ensembl ENSDARG00000008100, chromosome 7.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is invalid. Literature
  searched by hand via Europe PMC (`(slc7a10b OR slc7a10a)`, `(slc7a10 OR slc7a10a OR slc7a10b OR asc-1) AND
  zebrafish`, `slc7a10 AND (fish OR teleost)`, Asc-1 structure/knockout queries).
- DANRE_DUPLICATION batch 4, random draw 18 (seed 20260928); paralog slc7a10b. PANTHER TGD_tree 1:1 pair (PTHR11785);
  Ensembl Compara places the duplication at Osteoglossocephalai.

## Zebrafish literature

- No functional study of slc7a10a. A catalogue of zebrafish SLC7 genes lists an adult EST profile for slc7a10a only
  [PMID:34338990 "slc7a10a (Chr 7)Developmental stage|adultAdult|heart > kidney > brain > eye---slc7a10b (Chr 25)----"].
- The zebrafish obesity study used slc7a10b, chosen by sequence identity
  [PMID:36172277 "Moreover, Slc7a10b was chosen over Slc7a10a due to its slightly higher sequence identity (76% over 74%) with the human SLC7A10 (found using the T-coffee multiple sequence alignment tool (Notredame et al., 2000))."].

## Mammalian SLC7A10 (Asc-1)

- Na-independent small neutral amino acid exchanger that needs 4F2hc
  [PMID:10734121 "Asc-1 required 4F2hc for its functional expression."];
  [PMID:10734121 "Asc-1 preferred small neutral amino acids such as Gly, L-Ala, L-Ser, L-Thr, and L-Cys, and alpha-aminoisobutyric acid as substrates."];
  also D-serine [PMID:10734121 "Asc-1 also transported D-isomers of the small neutral amino acids, in particular D-Ser, a putative endogenous modulator of N-methyl-D-aspartate-type glutamate receptors, with high affinity."].
- Structure: disulfide to 4F2hc [PMID:38589439 "The HAT-specific disulfide bond is found between Cys154 of Asc-1 and Cys211 of 4F2hc"];
  gate residues [PMID:38589439 "Notably, E257A and R339A mutants also display almost no transport activity, indicating that the interaction between Glu257 and Arg339 is crucial for the transport cycle."].
- In vivo: glycine supply for inhibitory transmission
  [PMID:25755256 "Asc-1 works as a glycine and L-serine transporter, and its transport activity is required for the subsequent conversion of L-serine into glycine in vivo."];
  astrocytic in caudal CNS [PMID:27759100 "We find that SLC7A10 is substantially enriched in a subset of astrocytes of the caudal brain and spinal cord in a distribution corresponding with high densities of glycinergic inhibitory synapses."].

## My analysis (slc7a10a-bioinformatics/RESULTS.md)

- 77.8% identity between copies; both closer to SLC7A10 than to SLC7A8. All ten tested Asc-1 residues (N52, Y131,
  I138, C154, F243, F250, Y253, E257, Y333, R339) conserved in both copies, gar, coelacanth and medaka.
- slc7a10a evolves somewhat faster (42 vs 25 unique changes vs gar; P<0.05).
- Expression: slc7a10a broad (21 Bgee calls including heart, kidney, muscle, intestine, bone, brain) and rising in
  larvae; slc7a10b narrow (brain, eye, bone, testis, early embryo). Gar SLC7A10 calls resemble slc7a10b.

## GOA review decisions

All 10 rows accepted (IBA rows at the right level; IEA rows general but correct).
