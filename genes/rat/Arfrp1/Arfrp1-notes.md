# Curation Notes for Rat Arfrp1 (UniProtKB:Q63055, RGD:621683)

## 1. Gene Identity & Direct Rat Biochemical Evidence
- **Symbol / Accession**: `Arfrp1` (`UniProtKB:Q63055`, `RGD:621683`; alias `Arp1`, `ARP`), 201 aa, 100% identical to mouse `Arfrp1` (`Q8BXL7`) and 97.5% identical to human `ARFRP1` (`Q13795`) in `PANTHER:PTHR45909:SF1` (`PTN000196303`).
- **Founding Cloning and Biochemical Characterization in Rat (`PMID:8530503`)**:
  - Schürmann, Massmann & Joost (1995, `PMID:8530503`) cloned the rat and human `ARP` (`Arfrp1`) homologs, detected broad mRNA expression across rat skeletal muscle, fat, liver, kidney, spleen, testis, adrenals, ovary, thymus, intestine, and lung, identified the endogenous ~25-kDa membrane-associated protein in rat liver, testis, and kidney membranes, and demonstrated saturable GTPgammaS binding and intrinsic GTPase activity of recombinant ARP in the absence of phospholipids or tissue extracts.
- **Conserved Functional Motifs**:
  - Retains the N-terminal NatC/SYS1-binding amphipathic helix `1-MYTLLSGLYKYMFQ-14` (`Tyr2`), P-loop `24-GLDNAGKT-31` (`Lys30`, `Thr31`), Switch II catalytic `75-DLGGQ-79` (`Gln79`), and G4 `134-NKQD-137`.

## 2. Key Annotation Decisions
- **`GO:0003924`, `GO:0005525`, `GO:0005794`, `GO:0005802`, `GO:0006886`, `GO:0034067`, `GO:0042147`, `GO:0043001`**: `ACCEPT`, consistent with `human/ARFRP1`, `mouse/Arfrp1`, and `PTHR45909-review.yaml`.
- **`GO:0005829` (`cytosol`, `IEA`)** and **`GO:0007369` (`gastrulation`, `ISO` from `MGI:1923938`)**: `KEEP_AS_NON_CORE` (soluble cytosolic pool and downstream organismal embryonic phenotype, matching `mouse/Arfrp1`).
- **`GO:0016020` (`membrane`, `IEA` and `ISO` from `MGI:1923938`)**: `MODIFY` to `GO:0032588` (`trans-Golgi network membrane`).
