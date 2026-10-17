# P2 (P11124) — Pseudomonas phage phi6

## Overview
- **Gene symbol**: P2
- **UniProt ID**: P11124 (`RDRP_BPPH6`)
- **Product**: RNA-directed RNA polymerase P2 (665 AA, 74.8 kDa), encoded on dsRNA segment L.

## Literature & Functional Evidence
- **Primer-independent RNA-directed RNA polymerase (replicase and transcriptase)**: Purified recombinant P2 acts as an in vitro replicase that synthesizes minus-strand RNA on positive-sense ssRNA templates to generate dsRNA and also catalyzes semi-conservative RNA-templated transcription [PMID:10619851, "In this report, recombinant protein P2 of double-stranded RNA bacteriophage phi6 was purified and demonstrated in an in vitro enzymatic assay to act as the replicase. The enzyme efficiently utilizes phage-specific, positive-sense RNA substrates to produce double-stranded RNA molecules, which are formed by newly synthesized, full-length minus-strands base paired with the plus-strand templates."]; [PMID:11602748, "We have previously demonstrated that purified P2 protein, the Pol subunit of the φ6 PC, can act as a replicase and transcriptase in vitro ( 11 , 13 ). Although it accepts RNA templates of both φ6 and heterologous origin, φ6 Pol shows a clear preference for templates containing φ6-specific plus-strand initiation signals at their 3′ ends."]; [PMID:17237359, "ϕ6 RdRP performs de novo initiation and produces full-length dsRNAs from given template ssRNAs. The enzyme is highly processive, replicating ssRNA molecules of practically unlimited length ( Makeyev and Bamford 2000a , b ; Butcher et al. 2001 )."].
- **Manganese and magnesium ion binding**: Structural and mutational studies (E491Q) demonstrate a high-affinity Mn2+-binding site alongside catalytic Mg2+ ions required for structural dynamics, RNA binding, and processive elongation [PMID:18940872, "We have probed the role of Mn(2+) by biochemical, biophysical and structural analyses of the wild-type enzyme and of a mutant form with an altered Mn(2+)-binding site (E491 to Q). The E491Q mutant has much reduced affinity for Mn(2+), reduced RNA binding and a compromised elongation rate."].
- **Secondary terminal nucleotidyltransferase activity**: P2 also catalyzes nontemplated 3'-terminal nucleotide addition to ssRNA and dsRNA both in vitro and inside the nucleocapsid [PMID:18614640, "In this study, we show that this enzyme also catalyzes nontemplated nucleotide additions to single-stranded and double-stranded nucleic acid molecules. This terminal nucleotidyltransferase activity not only is a property of the isolated enzyme but also is detected to take place within the viral nucleocapsid."].
- **Procapsid localization**: Localizes on the inner procapsid surface near the three-fold axes of symmetry prior to RNA packaging [file:BPPH6/P2/P2-uniprot.txt, "SUBCELLULAR LOCATION: Virion. Note=Found in the capsid (12 copies). Prior to RNA packaging, localizes on the inner procapsid surface near the three-fold axis of symmetry."].

## Curation Decisions
- **ACCEPT**:
  - `GO:0003968` (`RNA-directed RNA polymerase activity`, IDA/IMP/IEA): Core enzymatic activity directly established across multiple biochemical and structural papers (`PMID:10619851`, `PMID:11602748`, `PMID:17237359`, `PMID:18614640`, `PMID:18940872`).
  - `GO:0039694` (`viral RNA genome replication`, IEA) and `GO:0001172` (`RNA-templated transcription`, IEA): Core biological processes carried out by P2 inside the procapsid/core.
  - `GO:0003723` (`RNA binding`, IEA), `GO:0000166` (`nucleotide binding`, IEA), and `GO:0046872` (`metal ion binding`, IEA): Supported by biochemical and structural studies showing template/NTP binding and Mn2+/Mg2+ coordination (`PMID:18940872`).
- **KEEP_AS_NON_CORE**:
  - `GO:0050265` (`RNA uridylyltransferase activity`, IDA `PMID:18614640`): Represents the secondary nontemplated 3'-terminal nucleotidyltransferase activity of P2.
- **TOO_GENERAL**:
  - `GO:0016740` (`transferase activity`), `GO:0016779` (`nucleotidyltransferase activity`), `GO:0034062` (`5'-3' RNA polymerase activity`), and `GO:0019079` (`viral genome replication`): Subsumed by `GO:0003968` and `GO:0039694`.
- **REMOVE**:
  - `GO:0006351` (`DNA-templated transcription`, IEA `InterPro:IPR001205`): False electronic mapping; phi6 is a dsRNA phage with no DNA stage, and P2 exclusively uses RNA templates.
