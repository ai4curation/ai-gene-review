# ant (P19655) — Curation Notes

## Summary
- **Gene symbol**: `ant` (`ant1` / `ant2`, formerly `rebA` / `rebB`, `coi` in early papers)
- **UniProtKB**: `P19655` (`ANT_BPP1`, 322 aa for full-length Ant1, 36.4 kDa; alternative initiation at Met-84 produces 239-aa Ant2, 27.3 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: Antirepressor proteins Ant1 and Ant2 encoded in the `immI` locus (`c4-icd-ant1/2` operon). Antagonize the primary lytic repressor C1 to induce lytic development and mediate heteroimmune prophage induction in a process requiring the phage-specific `sas` (site of Ant specificity) DNA sequence located centrally within the `ant` coding region.

## Literature Evidence
- **Heisig, Severin, Velleman & Schuster 1989 (`PMID:2585500`)**:
  - Sequenced the `immI` region and analyzed the `ant/reb` gene by amber and deletion mutagenesis. Showed that a single open reading frame encodes two in-frame proteins: Ant1 (322 aa, apparent MW ~42 kDa, `rebB`) and Ant2 (239 aa, apparent MW ~32 kDa, `rebA`, initiated at Met-84). Both proteins are required together (as an Ant1-Ant2 heteromeric complex) for full antirepressor activity against C1 repressor.
  - Quote: `"The immI region of bacteriophage P1 includes the ant/reb gene, which encodes the antirepressor protein, and the c4 gene, which encodes a repressor molecule that negatively regulates antirepressor synthesis. The antirepressor interferes with the activity of the P1 repressor of lytic function, the product of the c1 gene."`
  - Quote: `"two antirepressor proteins of molecular weights 42,000 and 32,000 are encoded by a single open reading frame, with the smaller protein initiating at an in-frame start codon"`
- **Hansen 1989 (`PMID:2661830`)**:
  - Noted extensive sequence homology between the C-terminal region of KilA and the C-terminal region of the P1/P7 Ant proteins (`InterPro:IPR005039`), including a predicted helix-turn-helix DNA-binding motif.
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Reviewed the structure and function of the `c4-icd-ant1/2` operon in `immI`. Synthesis of Ant1 requires translational coupling with the upstream 73-codon `icd` ORF (whose RBS is occluded by C4 antisense RNA in lysogens). Highlighted the central `sas` (site of Ant specificity) DNA element inside `ant`, onto which Ant proteins load in cis/trans to perform their antirepressor function during heteroimmune superinfection.
  - Quote: `"An additional specificity determinant, sas (site of Ant specificity), is involved in determining the capacity of Ant proteins to induce prophage on heteroimmune superinfection. The site resides centrally within the ant genes of P1 and P7"`
  - Quote: `"It was suggested that Ant proteins must normally load onto their phage-specific sas sites to perform their antirepressor function"`

## Annotation Review Decisions
- `GO:0003677` (`DNA binding`, IEA: `GO_REF:0000120`): **ACCEPT**. Supported by the conserved C-terminal helix-turn-helix DNA-binding domain (`InterPro:IPR005039`, shared with KilA) and genetic evidence that Ant1/2 loads onto the phage-specific `sas` DNA site within the `ant` gene to execute antirepressor function (`PMID:15489417`).
