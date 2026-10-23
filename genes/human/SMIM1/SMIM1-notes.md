# SMIM1 notes

## 2026-10-08: initial review (MICROPROTEINS Tier 2)

UniProt B2RUZ4, 78 aa, Swiss-Prot reviewed, PE1 (protein sequenced by MS from red cells). Not an
alternative-ORF peptide: SMIM1 is the canonical product of its own protein-coding locus on 1p36.32.

### Identity and topology
- Vel blood group carrier, identified by three groups in 2013. Purified from RBC membranes; disulfide
  complexes [PMID:23505126 "we now know that SMIM1 can form molecular complexes (likely homodimers) via disulphide bonds"].
- Transmembrane protein on RBCs [PMID:23563606 "evolutionarily conserved transmembrane protein expressed on RBCs"].
- Type II topology, Vel on C-terminus [PMID:26452714 "In conclusion, all our experimental data argue for SMIM1 being a type II membrane protein that displays the Vel antigen on its C-terminus."].
- Tail-anchored, homodimers in cell-free system [PMID:32301496 "is a tail-anchored transmembrane protein and readily forms homodimers in a cell-free system"].
- Dimerization via Cys77 and TM GxxxG [PMID:31879955 "dimerization is mediated both by an extracellular Cys77-dependent, homomeric"] (abstract only).

### Function (unknown)
- No known function at discovery [PMID:23563608 "SMIM1 was only recently annotated as a bona-fide protein-coding gene and has no known function."].
- Zebrafish morpholino: mild RBC reduction [PMID:23563608 "In vivo zebrafish smim1 knock down studies showed a mild reduction in the number of red blood cells, identifying SMIM1 as a novel regulator of red blood cell formation."]. Morpholino only; no stable mutant or mouse knockout found in PubMed (search 2026-10-08).
- Human SMIM1-null: heavier, lower T3/T4, lower REE [PMID:38906141 "individuals have lower average levels of total triiodothyronine (T3) and thyroxine (T4)"]; still "a protein of yet unknown function(s), up until now only known as the antigen underlying the Vel blood group" [PMID:38906141].

### GOA review decisions (64 rows)
- 54 x protein binding (HuRI Y2H, PMID:32296183): REMOVE. Partners are unrelated membrane proteins; typical TM-helix Y2H pattern.
- Plasma membrane (IBA, IEA, IDA, IMP) and cell surface (IBA, IMP x2, IDA): ACCEPT (8 rows).
- Protein homodimerization activity (IDA): KEEP_AS_NON_CORE; structural property, well replicated.
- Nucleate erythrocyte development (IBA from ZFIN smim1): MODIFY to GO:0030218 erythrocyte differentiation.
  GO:0048823 refers to nucleated mature erythrocytes (non-mammalian); wrong cell type for human. Evidence weak
  (morpholino + GWAS eQTL).
- No MF assigned in core_functions: none known.
