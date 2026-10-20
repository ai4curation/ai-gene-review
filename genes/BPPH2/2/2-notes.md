# Gene 2 (DNA polymerase, P03680) — Curation Notes

## Summary of Function
Gene `2` of *Bacillus phage phi29* (`NCBITaxon:2884424`) encodes the 575-amino-acid protein-primed family B DNA-directed DNA polymerase (gp2, p2; UniProt `P03680`, EC `2.7.7.7`). It is a monomeric polymerase that catalyzes all phases of phi29 protein-primed viral DNA replication (`GO:0039685`):
1. **Initiation (terminal protein deoxynucleotidylation)**: Forms a heterodimer with the viral terminal protein gp3 (`P03681`) and catalyzes the template-directed covalent linkage (phosphoester bond) between the hydroxyl group of Ser232 of gp3 and 5'-dAMP, directed by the second thymidine at the 3' end of the template strand via a sliding-back mechanism (`PMID:6402761`, `PMID:3863101`).
2. **Elongation and intrinsic strand displacement**: Dissociates from the parental/primer gp3 after synthesizing a short transition oligonucleotide and elongates the nascent DNA chain with exceptionally high processivity (>70 kb) and intrinsic strand-displacement activity without requiring an accessory helicase (`PMID:3863101`).
3. **Proofreading (`3'-5'` exonuclease)**: Contains an N-terminal `3'-5'` exonuclease domain (`GO:0008408`) that excises misincorporated deoxynucleotides to ensure high replication fidelity (`file:BPPH2/2/2-uniprot.txt`).

## Domain Architecture & Structural Features
- **InterPro / Pfam / PANTHER**:
  - `InterPro:IPR006172` (DNA-directed DNA polymerase, family B), `InterPro:IPR004868` (DNA-directed DNA polymerase, family B, mitochondrial/viral), `InterPro:IPR014416` (DNA-directed DNA polymerase, family B, bacteriophage phi29-type).
  - `InterPro:IPR043502` (DNA/RNA polymerase superfamily), `InterPro:IPR023211` (DNA polymerase, palm domain superfamily), `InterPro:IPR012337` / `InterPro:IPR036397` (RNase H-like superfamily, corresponding to the 3'-5' exonuclease fold).
  - `Pfam:PF03175` (`DNA_pol_B_2`), `PANTHER:PTHR33568:SF3`.
- **Unique insertions (TPR1 and TPR2)**: Relative to canonical family B DNA polymerases, phi29 gp2 contains two specific insertions in the polymerization domain, Terminal Protein Regions 1 and 2 (TPR1 and TPR2). TPR1 interacts with the terminal protein gp3 and DNA, while TPR2 forms a narrow downstream template tunnel with the thumb, palm, and exonuclease domains that separates the template and non-template strands during replication, conferring intrinsic strand-displacement activity and high processivity.
- **Cofactor**: Binds two catalytic divalent metal ions (`Mg2+`, `GO:0000287`, coordinated by conserved aspartates Asp12, Asp66, Asp169 in the exonuclease domain and Asp249, Asp456, Asp458 in the palm polymerization active site).

## Literature & Annotation Review
- `PMID:3863101`: Demonstrated in vitro synthesis of full-length phi29 DNA using purified terminal protein p3 and DNA polymerase p2.
- `PMID:6402761`: Demonstrated that functional gene 2 product is required for formation of the p3-dAMP initiation complex.
- `PMID:820555`: Classical genetic characterization showing gene 2 mutants fail to synthesize phage DNA.
- **GO Annotation Decisions**:
  - Core MF terms: `GO:0003887` (`DNA-directed DNA polymerase activity`), `GO:0008408` (`3'-5' exonuclease activity`), `GO:0003677` (`DNA binding`), and `GO:0000287` (`magnesium ion binding`).
  - Core BP term: `GO:0039685` (`protein-primed viral DNA replication`), which is the specific descendant of `GO:0039693` (`viral DNA genome replication`), `GO:0006260` (`DNA replication`), and captures the unified initiation/elongation mechanism of gp2.
  - Broad enzymatic and binding IEA terms (`GO:0000166`, `GO:0001882`, `GO:0016740`, `GO:0016779`, `GO:0016787`) are marked `TOO_GENERAL` as they are entailed by `GO:0003887` and `GO:0008408`. Intermediate terms (`GO:0034061`, `GO:0004518`, `GO:0004527`, `GO:0003676`, `GO:0046872`, `GO:0006260`, `GO:0006270`, `GO:0039693`) are refined via `MODIFY` to their specific experimentally supported descendants.
