# CG42763 (M9MRG9) homology, domain and distribution check (2026-10-21)

Script: `homology_check.py` (raw output in `homology_check.json`). Run with
`uv run --no-project --with requests python homology_check.py`.

## Identity

M9MRG9 is the only UniProtKB entry cross-referenced to FlyBase FBgn0261831 and is 191 aa.
A cDNA-derived TrEMBL fragment, F3YD93 (MIP30261p, 190 aa), is 100% identical over query
residues 2-191, which shows that the locus is transcribed and that M9MRG9 is the full-length
product.

## Family and domain signals

InterPro returns no entry matches for M9MRG9 (neither integrated InterPro entries nor
member-database signatures), and UniProt lists no PANTHER family. The only sequence feature
is the SignalP-predicted signal peptide (residues 1-22), which leaves a 169-residue mature
chain. UniProt lists no transmembrane segment. The C-terminal sequence is ILKYLTRFPSAKCTLPN,
which has no hydrophobic anchor and no KDEL/HDEL ER-retention motif. The mature chain has
4 cysteines.

## Phylogenetic distribution

- OMA returns no HOG and no orthologs for M9MRG9.
- blastp (EBI NCBI-BLAST, E <= 1e-3) against UniProtKB/Swiss-Prot returned **no hits**.
- Against UniProtKB Eukaryota, all 8 hits are from *Drosophila*. Full-length hits come only
  from melanogaster-group species: D. mauritiana A0A6P8LER2 (88.0% identity), D. yakuba
  A0A0R1DRY4 (77.0%), D. erecta A0A0Q5WAU5 (66.1%) and D. suzukii A0ABM4TPV6 (48.6%).
- The only other D. melanogaster hit is CG31606 (Q8IPG8, and its cDNA fragment G2J5W9), at
  E = 4.2e-4 and 33.7% identity over query residues 7-95. This partial, marginal match is the
  only paralog signal; CG31606 is itself uncharacterised.
- The D. yakuba ortholog A0A0R1DRY4 is named "Protein TsetseEP domain-containing protein",
  but that name is a ProtNLM machine-generated name (`ECO:0008006|Google:ProtNLM`) and is not
  backed by any domain signature. It is not used as evidence here.

## Interpretation

CG42763 is a taxonomically restricted gene of the *D. melanogaster* species group that encodes
a small predicted secreted protein with no recognised domain. It has no characterised ortholog
in any species, no PANTHER subfamily and no PAINT node, so there is no evolutionary basis for
transferring any molecular function or biological process. The sequence features support
only an inferred extracellular (secreted) location.
