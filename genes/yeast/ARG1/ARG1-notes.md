# ARG1 (YOL058W, P22768) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Argininosuccinate synthase, EC 6.3.4.5, homotetramer [UniProt:P22768]. Purified enzyme: "Yeast argininosuccinate synthetase has been purified to homogeneity." and "The quaternary structure ... is tetrameric." [PMID:35347]
- Kinetics: "with MgATP as the variable substrate a sigmoid character" ; "Kinetic analysis provided evidence for a random addition of substrates." [PMID:35347]
- Dual role: "anabolic in the biosynthesis of arginine, catabolic as the first enzyme of citrulline utilization as nitrogen source" [PMID:35347]
- Gene identity: "The Saccharomyces cerevisiae ARG1 gene coding for argininosuccinate synthetase has been isolated" [PMID:2897249]; regulation by arginine-specific repression and general amino acid control [PMID:2897249].
- Location: cytosolic/soluble fraction, with the other ornithine-to-arginine enzymes [PMID:205532 "argininosuccinate synthetase, and argininosuccinate lyase, and the two first catabolic enzymes, arginase and ornithine aminotransferase, were in the"].

## Curation decisions
- Core MF: GO:0004055; BP GO:0006526; CC GO:0005829.
- Urea cycle (IBA, PTN000172504): MARK_AS_OVER_ANNOTATED. Yeast is not ureotelic; arginase (CAR1) is catabolic and, with OTCase, forms the epiarginase complex that blocks futile cycling [PMID:12679340]. Precedent: genes/PSEPK/argG REMOVE for the same node.
- ATP binding IEA: non-core (substrate).
