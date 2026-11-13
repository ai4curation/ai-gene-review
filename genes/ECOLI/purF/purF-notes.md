# purF (Escherichia coli K-12, UniProtKB:P0AG16) notes

## 2026-11-13 review for the de_novo_purine_synthesis module

PurF is the glutamine phosphoribosylpyrophosphate (PRPP) amidotransferase of Escherichia coli, a cytosolic homotetramer that catalyses the committed first step of de novo IMP biosynthesis: transfer of the glutamine amide nitrogen, generated in an N-terminal Ntn glutaminase domain with an N-terminal cysteine nucleophile, through an ammonia channel to PRPP in a C-terminal phosphoribosyltransferase domain, giving 5-phosphoribosylamine. It is feedback-inhibited by AMP and GMP and is also inhibited by the stringent-response alarmone ppGpp.

### Provenance

No provider deep-research report was generated for this gene. These notes were written by the reviewer from: the fetched UniProt record (file:ECOLI/purF/purF-uniprot.txt), the cached primary publications cited below (most abstract-only; full_text_available is recorded in each publications/PMID_*.md file), the PANTHER family reviews under interpro/panther/, and the P. putida, yeast and human orthologue reviews used as precedents.


### Core function evidence

- amidophosphoribosyltransferase activity (GO:0004044):
  [PMID:372191 "Glutamine 5-phosphoribosylamine:pyrophosphate phosphoribosyltransferase (amidophosphoribosyl-transferase) has been purified to homogeneity from Escherichia coli."]
  [PMID:7037784 "These results establish that the NH2-terminal cysteine is the active site residue required for the glutamine amide transfer function of the enzyme."]

### Decisions other than ACCEPT

- GO:0000287 magnesium ion binding (IDA, PMID:9333323): KEEP_AS_NON_CORE. Mg2+ binds the PRTase active site with PRPP.
- GO:0000287 magnesium ion binding (IEA, GO_REF:0000104): KEEP_AS_NON_CORE. Mg2+ binds the PRTase active site with PRPP.
- GO:0005737 cytoplasm (IBA, GO_REF:0000033): MODIFY -> GO:0005829. Correct but general location; the gene also carries the more specific cytosol term.
- GO:0005737 cytoplasm (IDA, PMID:7037784): MODIFY -> GO:0005829. Correct but general location; the gene also carries the more specific cytosol term.
- GO:0006164 purine nucleotide biosynthetic process (EXP, PMID:7037784): MODIFY -> GO:0006189. Correct but general process; PurF acts specifically in de novo IMP biosynthesis.
- GO:0006164 purine nucleotide biosynthetic process (IBA, GO_REF:0000033): MODIFY -> GO:0006189. Correct but general process; PurF acts specifically in de novo IMP biosynthesis.
- GO:0006164 purine nucleotide biosynthetic process (IDA, PMID:7037784): MODIFY -> GO:0006189. Correct but general process; PurF acts specifically in de novo IMP biosynthesis.
- GO:0006164 purine nucleotide biosynthetic process (IMP, PMID:6447689): MODIFY -> GO:0006189. Correct but general process; PurF acts specifically in de novo IMP biosynthesis.
- GO:0006541 L-glutamine metabolic process (IDA, PMID:7037784): KEEP_AS_NON_CORE. Glutamine is the amide donor of the reaction.
- GO:0006541 L-glutamine metabolic process (IMP, PMID:2188964): KEEP_AS_NON_CORE. Deletions show the N-terminal domain supplies the glutamine-dependent activity.
- GO:0009113 purine nucleobase biosynthetic process (IEA, GO_REF:0000002): MODIFY -> GO:0006189. Nucleobase-process term misclassifies a ribonucleotide pathway step.
- GO:0016757 glycosyltransferase activity (IDA, PMID:7037784): MODIFY -> GO:0004044. Correct but general class; PurF is a specific phosphoribosyltransferase.
- GO:0042802 identical protein binding (IDA, PMID:372191): KEEP_AS_NON_CORE. PurF is a homo-oligomer.
- GO:0042802 identical protein binding (IDA, PMID:9514258): KEEP_AS_NON_CORE. The crystal structure shows a PurF homotetramer.
- GO:0097216 guanosine tetraphosphate binding (IDA, PMID:30559427): KEEP_AS_NON_CORE. ppGpp binds PurF allosterically and inhibits it.

Precedents followed: PSEPK pur* reviews, yeast ADE2/ADE5,7 and the PANTHER family reviews (PTHR10520 TOO_DEEP GAR synthetase node; PTHR11609 WRONG_NODE for GO:0004638 and GO:0006144).
