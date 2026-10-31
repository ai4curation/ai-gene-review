# parA (PP_0002, P0A149), Pseudomonas putida KT2440

## 2026-10-23: initial review

**Identity.** PP_0002 is the chromosomal ParA of the ParABS partition system, encoded next to
parB (PP_0001) at the start of the genome beside oriC. UniProt still names the Swiss-Prot entry
"Uncharacterized protein PP_0002" (sequence version 1, 2005), with only a curated similarity
note: "SIMILARITY: To B.subtilis soj." [file:PSEPK/parA/parA-uniprot.txt]. NCBI names the WP_
protein "ParA family protein" from SPARCLE architecture 11439703.

**GOA has no annotation at all.** The Pfam match (AAA_31, PF13614) has no InterPro2GO mapping and
the PANTHER subfamily (PTHR13696:SF52, "PARA FAMILY PROTEIN CT_582") brings no IBA. NCBI's
architecture GO (ATP binding, ATP hydrolysis activity) is the only GO this protein has anywhere.

**Paralog caution.** KT2440 also carries an orphan ParA-family protein, ParI, on a genomic
island, which interferes with IncP-7 plasmid partition [PMID:22925377 "ParI, an orphan ParA
family protein from Pseudomonas putida KT2440-specific genomic island, interferes with the
partition system of IncP-7 plasmids"]. The evidence below is specific to the oriC-adjacent
PP_0002, not to ParI.

**P. putida genetics.**
- parA and parB mutants give anucleate cells, but only in minimal medium at the entry into
  stationary phase [PMID:11832517 "However, in M9-minimal medium different parA and parB
  mutations gave between 5 and 10% anucleate cells during the transition from exponential phase
  to stationary phase."]. The authors link this to division without ongoing replication.
- parAB deletion and ParAB overproduction both raise anucleate-cell frequencies in deceleration
  phase, and an oriC-region parS-like sequence stabilises a mini-F in E. coli only with ParAB
  [PMID:11849535 "One was inserted into an unstable mini-F and shown to stabilize it in E. coli
  in a ParAB-dependent manner."].

**Orthology to P. aeruginosa ParA.** 84% identity over the full length, with an identical deviant
Walker A box (KGGVGKT, 11-17) [file:PSEPK/parA/parA-bioinformatics/RESULTS.md]. Purified P.
aeruginosa ParA hydrolyses ATP [PMID:25139949 "ParA-His6 demonstrated ATPase activity (Fig. 3)
of ~1.2 pmol Pi released min−1 (pmol ParA)−1."]. The DNA-binding arginines of B. subtilis Soj
are conserved in P. putida ParA [PMID:18077387 "The arginine residues are conserved among other
chromosomal homologues, including the ParAs from Caulobacter crescentus, Pseudomonas aeruginosa,
Pseudomonas putida"], but DNA binding has not been tested in either Pseudomonas, so it is not
proposed.

**Decisions.** NEW ATP hydrolysis activity (ISO from P. aeruginosa ParA) and NEW chromosome
segregation (IMP, P. putida mutants). ParA does work in segregation as the partition ATPase, so
the process term passes the "does the gene do any of the work" test.

**NCBI/CDD comparison** (see `parA-pgap-predictions-review.yaml` and projects/REFSEQ_GO.md):
both NCBI terms are correct and absent from GOA. This is the clearest case so far of CDD
architecture GO filling a complete GOA gap.
