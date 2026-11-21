# Ddr (Q59DZ7) bioinformatics: collagen-pocket and kinase catalytic residues

## Method

`ds_kinase_conservation.py` downloads canonical sequences from the UniProt REST API and
makes global pairwise alignments (Biopython PairwiseAligner, BLOSUM62, gap open -10,
extend -0.5) of human DDR2 (Q16832) against Drosophila melanogaster Ddr (Q59DZ7, the
1054-residue full-length isoform) and against DDR homologues from other animals. For each
alignment it reports the residue aligned to:

- the ten human DDR2 residues that line the collagen-binding pocket in the DDR2
  discoidin (DS) domain-collagen peptide crystal structure (Trp52, Thr56, Asp69, the
  Cys73-Cys177 disulfide, Arg105, His110, Ile112, Glu113, Asn175; PMID:20004161);
- canonical protein-kinase catalytic residues of DDR2, located by motif search on the
  DDR2 sequence: the beta3 lysine (VAVK, Lys608), the HRD aspartate (Asp710), the
  catalytic-loop asparagine (HRDLATRN, Asn715), the DFG aspartate (Asp728), and the
  three activation-loop tyrosines (Tyr736, Tyr740, Tyr741).

Run from the repository root (uses the repository's own uv environment, which already
provides Biopython, to avoid a second environment):

```
uv run python genes/DROME/Ddr/Ddr-bioinformatics/ds_kinase_conservation.py
```

Raw output is in `output.txt`. Sequences are fetched live, so results follow the current
UniProt sequence versions. The output ends with each homologue's UniProt review status and
protein-existence level and a 17-residue window around each aligned catalytic position, so
the per-homologue statements below can be checked against it.

## Results

Overall, fly Ddr is 40.3% identical to human DDR2 over aligned positions (DS domain
40.6%, kinase domain 49.6%).

Residue table (DDR2 site -> aligned residue):

| DDR2 site | human DDR1 | D. virilis Ddr | Anopheles | Tribolium | Apis | C. elegans ddr-1 | C. elegans ddr-2 | D. melanogaster Ddr |
|---|---|---|---|---|---|---|---|---|
| pocket W52 | W53 | H136 | H17 | F105 | Y55 | F47 | F47 | H128 |
| pocket T56 | T57 | V141 | V22 | V110 | V59 | V52 | T52 | V133 |
| pocket D69 | D70 | G154 | G35 | G123 | G72 | S65 | S65 | G146 |
| pocket C73 | C74 | C158 | C39 | C127 | C76 | C69 | C69 | C150 |
| pocket R105 | R105 | R189 | R70 | R158 | R107 | R100 | R100 | R181 |
| pocket E113 | E113 | E197 | E78 | E166 | E115 | E108 | E108 | E189 |
| pocket N175 | S175 | T260 | T141 | T229 | T178 | T170 | T171 | T252 |
| pocket C177 | C177 | C262 | C143 | C231 | C180 | C172 | C173 | C254 |
| beta3 Lys K608 | K655 | A795 | S634 | K716 | P674 | H556 | K554 | A789 |
| HRD Asp D710 | D766 | D898 | D736 | D821 | D779 | H638 | D645 | D892 |
| catalytic-loop Asn N715 | N771 | S903 | S741 | N826 | N784 | N643 | N650 | S897 |
| DFG Asp D728 | D784 | S916 | T754 | D839 | D797 | S656 | D663 | S910 |
| A-loop Tyr Y736 | Y792 | Y926 | Y764 | Y847 | Y805 | P657 | Y671 | Y920 |
| A-loop Tyr Y740 | Y796 | Y930 | Y768 | Y851 | Y809 | S661 | Y675 | Y924 |
| A-loop Tyr Y741 | Y797 | C931 | C769 | Y852 | S810 | H662 | Y676 | C925 |

(His110 and Ile112 rows are in `output.txt`; they vary in every invertebrate.)

The fly sequence around these sites reads (Q59DZ7 numbering): `TLVAVATLRPG` (beta3 strand;
DDR2 `VLVAVKMLRAD`), `HRDLATRSC` (catalytic loop; DDR2 `HRDLATRNC`), and `KVCSIGTV`
(DDR2 `KIADFGMS`), as seen in the alignment.

## Interpretation

1. **Kinase catalytic residues.** D. melanogaster Ddr retains the HRD aspartate but has lost three residues that are required for phosphotransfer in canonical protein kinases: the beta3 lysine (Ala789), the catalytic-loop asparagine (Ser897) and the DFG aspartate (Ser910). The same three losses, with different replacement residues, are found in Drosophila virilis and Anopheles gambiae Ddr, so the change is shared by Diptera and is not a sequencing or gene-model artefact of one genome. Tribolium DDR and C. elegans ddr-2 keep all three. The honeybee entry keeps the catalytic-loop asparagine (Asn784) and the DFG aspartate (Asp797) but has Pro674 at the beta3 lysine position (output window 666-682 reads PRLVVARV[P]VCTGDIRG, with no VAxK motif); it is an unreviewed entry (A0A7M7MKP6, PE 3, a RefSeq-derived isoform X1 model) whose catalytic loop also reads VHK[D] rather than HRD, so a gene-model or alignment problem cannot be excluded there. C. elegans ddr-1 keeps the catalytic-loop asparagine (Asn643) but not the beta3 lysine (His556) or the DFG aspartate (Ser656), and also lacks the HRD aspartate (His638) that the dipterans retain, a different degeneration pattern in its own lineage. The three-residue loss is therefore shared by the dipterans examined, and not by Tribolium or C. elegans ddr-2. Dipteran Ddr is therefore predicted to be a pseudokinase. No experiment on fly Ddr kinase activity has been reported, so this is a prediction, not a measured loss.
2. **Collagen-binding pocket.** Of the ten DDR2 residues lining the collagen pocket, the two disulfide cysteines and the Arg105-Glu113 salt bridge are conserved in all homologues, but Trp52 and Asp69 (and Thr56, Asn175) are replaced in fly Ddr and in every invertebrate DDR examined. The pocket that recognises the GVMGFO motif of fibrillar collagens in vertebrates is thus not conserved in invertebrates, as expected since insects have no fibrillar collagen. This does not exclude collagen binding by a different surface, but sequence gives no support for transferring the vertebrate collagen-binding mode to Ddr.
3. Alignments of the variable DS loops can shift by a residue or two; the conclusions rest on the consistent pattern across eight sequences, not on any single position.

