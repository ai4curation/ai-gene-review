# XV (protein P15, endolysin) — Enterobacteria phage PRD1 (UniProt P13559)

## Provenance note

Automated deep research was **not available** in this environment (no provider API
keys), so no `-deep-research-<provider>.md` file exists for this gene. These notes
were assembled by reading the cached publications in `publications/`, the UniProt
flat file `XV-uniprot.txt`, and PubMed searches. The GONUTS wiki
(`gowiki.tamu.edu`), which records the CACAO students' evidence per PMID, was
**offline** when queried on 2026-10-29 ("This site is temporarily offline while we
perform upgrades."), so the student-supplied evidence text could not be inspected
for the five CACAO rows.

## Identity

- 149 aa protein, 17.3 kDa, encoded by PRD1 gene *XV*; also called P15, beta-1,4-N-acetylmuramidase, lysozyme, lytic enzyme [PMID:2651121 "The gene for the lytic enzyme of the lipid-containing, broad-host-range bacteriophage PRD1 codes for a protein of 149 amino acids (17271 Da)"].
- Sequence is distinctive among lytic enzymes, with only weak local similarity to phage lysozymes [PMID:2651121 "The sequence of the protein is unique when compared to other lytic enzymes sequenced. However, three regions of weak similarity with other phage lytic enzymes were observed."]. UniProt places it in glycosyl hydrolase family 24 (ECO:0000305) and PIRSF001069 / Pfam PF11860 (Muramidase) / IPR016284 (Phage PRD1 P15 lysozyme).

## Molecular function: muramidase (lysozyme)

- Recombinant P15 purified from an expression plasmid lyses chloroform-treated Gram-negative cells; cell-wall digest analysis establishes the bond specificity [PMID:7925454 "The analysis of cell wall digests indicated that P15 is a glycosidase that cleaves the beta (1-4) linkage between N-acetylmuramic acid and N-acetylglucosamine, thus displaying muramidase activity."].
- Same paper: purity and identity confirmed, lytic activity Gram-negative-selective, pH optimum 7.0–8.0 [PMID:7925454 "The purified protein P15, identified by N-terminal sequence analysis, showed a strong lytic activity against chloroform-treated Gram-negative cells. No activity against Gram-positive bacterial species could be detected."].
- In virion zymograms P15 appears as a ~15 kDa clear zone absent from *sus174*, *sus232*, *sus240* (P15-) and P20- particles [PMID:11741849 "Thus, we concluded that the appearance of the faster-moving clear zone in zymograms was due to the enzymatic activity of protein P15."]. Against Gram-positive (M. lysodeikticus) peptidoglycan, P15 (unlike P7) *is* active in zymograms [PMID:11741849 "Protein P7 was found to be inactive, while protein P15 degraded peptidoglycan obtained from M. lysodeikticus and caused the appearance of a clear zone in zymograms."] — note this is in apparent contrast to the turbidimetric result of PMID:7925454 on intact Gram-positive cells, presumably an accessibility rather than specificity difference.
- UniProt records EC 3.2.1.17 with experimental evidence from both papers [file:BPPRD/XV/XV-uniprot.txt "Reaction=Hydrolysis of (1->4)-beta-linkages between N-acetylmuramic"].

## Biological process: holin-dependent host lysis and progeny release

- PRD1 lyses its host with a canonical two-component holin (P35, gene *XXXV*) / endolysin (P15, gene *XV*) system [PMID:16030234 "Using infected cells and plasmid-borne lysis genes, we demonstrated that a two-component lysis system (holin-endolysin) operates to release progeny phage particles from the host cell."].
- Both proteins are required: neither the holin mutant *sus715* nor the endolysin mutant *sus232* lyses, with or without arsenate [PMID:16030234 "The same result was observed in the case of the endolysin sus232 mutant."; "These observations confirm that both the phage holin and endolysin proteins are necessary for premature lysis."].
- Plasmid-borne reconstruction separates the two activities: holin alone gives K+ leakage and loss of membrane voltage but no lysis; endolysin alone gives nothing; together they lyse [PMID:16030234 "The data on electrochemical properties of the cells carrying recombinant proteins revealed that the K + leakage and loss of ΔΨ were functions of the holin protein and that endolysin was needed for cell lysis."].
- So P15's own step is peptidoglycan hydrolysis from the cytoplasmic side after holin permeabilizes the membrane; the lysis and the release of progeny virions are the direct consequence [file:BPPRD/XV/XV-uniprot.txt "Endolysin involved in host peptidoglycan digestion after"].

## Virion association (cellular component)

- P15 is not only a soluble lysis enzyme but a structural component of the virion, connected to the internal phage membrane [PMID:11741849 "We demonstrate here that P15 is also a structural component of the PRD1 virion and that it is connected to the phage membrane."].
- Evidence is multi-pronged, not a single image: zymogram detection of P15 in isolated, capsid-free and GuHCl-released phage membrane vesicles, both empty and DNA-filled [PMID:11741849 "Zymogram analysis revealed the presence of proteins P7 and P15 in both DNA-filled and empty phage membranes (Fig. 3a )."]; ~5-fold activation of particle-associated lytic activity on partial capsid dissociation by freeze–thaw; and dependence of particle-associated P15 activity on the small integral membrane proteins P20 and P22 [PMID:11741849 "Small viral membrane proteins P20 and P22 modulate incorporation of P15 into the virion and may connect it to the phage membrane."].
- UniProt: Virion membrane; peripheral membrane protein, possibly tethered via P20/P22 [file:BPPRD/XV/XV-uniprot.txt "Peripheral membrane protein {ECO:0000269|PubMed:11741849}. Note=May be"].

## What P15 does *not* do: DNA entry

- The virion-entry muralytic role belongs to the P7 transglycosylase, not P15. P15- particles show no delay in initiating phage DNA replication [PMID:11741849 "However, in the absence of protein P15 no delay in phage DNA replication was detected, suggesting that protein P7 is the main muralytic enzyme involved in bacteriophage PRD1 DNA entry into Salmonella cells."].
- PMID:10931330 is a paper about **P7**, not P15: it reports the P7-associated glycolytic activity in zymograms and maps P14 [PMID:10931330 "We analysed wild-type PRD1 and different mutant particles in zymograms and found a glycolytic activity that was associated with protein P7."]. It carries a CACAO IDA row for GO:0003796 on P13559. Its zymograms of wild-type and mutant particles do also show the second, faster-moving muralytic zone later identified as P15 (PMID:11741849 revisits exactly these zymograms), so the annotation is plausible but the paper's own attribution is to P7; the cached record is abstract-only and the GONUTS page was offline, so this row is left `UNDECIDED` rather than removed (curator-deference rule).
- A secondary, non-enzymatic observation: P2+P15- particles adsorb normally but initiate infection poorly, prompting the speculation that P15 contributes to the DNA-delivery signal at the vertex [PMID:11741849 "This implies either that in the absence of P15 protein P2 does not properly function in signaling initiation of the DNA delivery process or that P15 somehow is part of the signal transduction pathway."]. This is explicitly speculative and is not annotated.

## Notes on the IEA/keyword-derived rows

- `GO:0042742 defense response to bacterium` comes from keyword KW-0081 (Antimicrobial) via GO_REF:0000043. For a phage endolysin this reads a host-killing activity as a *defense* response of the annotated organism; the phage is the attacker, not a defender, and GO:0031640 killing of cells of another organism already carries the real claim. Over-annotation.
- `GO:0003824` and `GO:0016787` are ancestors of the asserted `GO:0033922`/`GO:0003796`; `GO:0016798` likewise. True but entailed.
- `GO:0044659 viral release from host cell by cytolysis` (InterPro IPR016284 = the P15 family itself) matches the experimental picture exactly.
