# mre11: original ProtNLM2 function paragraph

Source: [preserved XML](mre11-protnlm-source.xml), pre-release `post-processed-2026_02_28k.xml`. The source paragraph is reproduced verbatim. Current sequence and taxonomy are identity checks, not proven prediction-time input.

> Involved in DNA double-strand break repair (DSBR). Possesses single-strand endonuclease activity and double-strand-specific 3'-5' exonuclease activity. Also involved in meiotic DSB processing.

## Atomic claim assessments

### Claim 1: Involved in DNA double-strand break repair (DSBR).

Assessment: **CNN** (score 2). Target rad32 mutants have defective physical repair of radiation-induced DSBs and impaired homologous gene conversion. This is established MRN biology and matches existing repair annotations.

- [PMID:7885834](https://pubmed.ncbi.nlm.nih.gov/7885834/): "Pulsed field gel electrophoresis of DNA from irradiated cells indicates that the rad32 mutant, in comparison to wild type cells, has decreased ability to repair DNA double strand breaks. The mutant also undergoes decreased meiotic recombination and displays reduced stability of minichromosomes."
- [PMID:12628934](https://pubmed.ncbi.nlm.nih.gov/12628934/): "We found that the homologous recombination (HR) genes rhp51(+), rad22A(+), rad32(+) and the nucleotide excision repair gene rad16(+) were required for efficient interchromosomal gene conversion."
### Claim 2: Possesses single-strand endonuclease activity

Assessment: **CNN** (score 2). Purified human MRN has manganese-dependent ssDNA endonuclease activity. The specific Mre11 family, conserved target catalytic domain, fission yeast nuclease-mutant phenotypes, and curated ISO/IBA activity support transfer of this chemistry to Rad32. The catalytic subunit is Mre11, not an accessory scaffold.

- [PMID:9705271](https://pubmed.ncbi.nlm.nih.gov/9705271/): "We show that the Rad50-Mre11-p95 complex possesses manganese-dependent single-stranded DNA endonuclease and 3' to 5' exonuclease activities."
- [PMID:22705791](https://pubmed.ncbi.nlm.nih.gov/22705791/): "To understand the functional architecture of MRN, we determined the crystal structures of the Schizosaccharomyces pombe Mre11 dimeric catalytic domain alone and in complex with a fragment of Nbs1."
- [PMID:19139281](https://pubmed.ncbi.nlm.nih.gov/19139281/): "This study demonstrates for the first time that Mre11 (Schizosaccharomyces pombe Rad32(Mre11)) nuclease activity is required for the removal of Rec12(Spo11)."
### Claim 3: double-strand-specific 3'-5' exonuclease activity.

Assessment: **CNN** (score 2). Purified Mre11 biochemistry establishes 3′-to-5′ exonuclease activity, with double-stranded substrate specificity already represented by curated GO:0008311. Target structure supports conserved nuclease architecture. This intrinsic chemistry is compatible with net 5′-strand resection by the larger repair pathway.

- [PMID:9651580](https://pubmed.ncbi.nlm.nih.gov/9651580/): "We have investigated the enzymatic activities of the purified proteins and found that Mre11 by itself has 3' to 5' exonuclease activity that is increased when Mre11 is in a complex with Rad50. Mre11 also exhibits endonuclease activity, as shown by the asymmetric opening of DNA hairpin loops."
- [PMID:22705791](https://pubmed.ncbi.nlm.nih.gov/22705791/): "To understand the functional architecture of MRN, we determined the crystal structures of the Schizosaccharomyces pombe Mre11 dimeric catalytic domain alone and in complex with a fragment of Nbs1."
### Claim 4: Also involved in meiotic DSB processing.

Assessment: **CNN** (score 2). Fission yeast Rad32 nuclease mutants impair removal of Rec12-linked DNA ends. This target experiment establishes meiotic end processing before recombinational repair. It does not imply Rad32 is required for ordinary Rec12-dependent DSB formation.

- [PMID:19139281](https://pubmed.ncbi.nlm.nih.gov/19139281/): "This study demonstrates for the first time that Mre11 (Schizosaccharomyces pombe Rad32(Mre11)) nuclease activity is required for the removal of Rec12(Spo11)."
- [PMID:19752195](https://pubmed.ncbi.nlm.nih.gov/19752195/): "Rec12-oligonucleotide generation strictly requires Ctp1 (Sae2 nuclease homolog), the Rad32 (Mre11) nuclease domain, and Rad50 of the MRN complex."
- [PMID:15238514](https://pubmed.ncbi.nlm.nih.gov/15238514/): "Meiotic DNA breakage in Schizosaccharomyces pombe did not require Rad50 or Rad32, although the homologs Rad50 and Mre11 are required in Saccharomyces cerevisiae; these proteins are required for meiotic DNA break repair in both yeasts."

These are prose-claim assessments; no GO mappings were invented for the paragraph. CNN denotes established equivalent biology, including justified conserved-family inference, and makes no assertion about training-data membership.
