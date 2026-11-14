# PA0845 / cerN (Q9I596) review notes

Secreted neutral ceramidase (EC 3.5.1.23). Purified from culture supernatant and
shown to hydrolyse ceramides reversibly [PMID:9603946 "Interestingly, the 70-kDa protein catalyzed a reversible reaction in which the N-acyl linkage of ceramide was either cleaved or synthesized."]. Gene cloned and expressed in E. coli [PMID:10593963 "Recombinant ceramidase was purified to homogeneity from the lysate of E. coli cells and confirmed to be identical to the Pseudomonas enzyme in its specificity and other enzymatic properties."]. In the lung it is part of the SphR regulon; a clean PA0845 deletion abolishes ceramide-induced sphA [PMID:24465209 "Ceramide fails to induce PA5325-lacZ in the absence of the neutral ceramidase"]; renamed cerN [PMID:24465209 "We propose that PA0845 be renamed cerN for ceramidase, neutral."].

## PseudoCAP IBA-seed assessment

Other seeds' experimental support from .cache/paint/IBD.gaf and QuickGO, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN004377481 | GO:0017040 N-acylsphingosine amidohydrolase activity | 7 | 156 (78 taxa) | GO:0017040, IMP PMID:10593963 (PseudoCAP), IDA PMID:9603946 (UniProt) | SOUND | PA0845 purified and assayed; recombinant expression confirms activity. Self-seed expected. | human ASAH2 Q9NR71, mouse/rat/zebrafish/fly ceramidases, M. tuberculosis O06769 (IDA PMID:10593963/20139604) | Yes |

Node term is the exact ceramidase activity; suits the clade. No PSEUDOCAP or GO_CENTRAL
defect on the GO:0017040 seed.

Related nodes on the same PTN (leaf IBAs received by PA0845, and where PA0845 seeds):
- GO:0042759 long-chain fatty acid biosynthetic process: seeded by PA0845 (Q9I596) and
  O06769 only. A ceramidase RELEASES a free fatty acid by hydrolysis; it does not
  synthesise one. Node term misfits the family -> GO_CENTRAL defect (CHECK, PROBABLE),
  recorded on the PA0845 IDA row (most direct evidence). Rows MARK_AS_OVER_ANNOTATED.
- GO:0046512 sphingosine biosynthetic process: KEEP_AS_NON_CORE (sphingosine is a true
  product; conserved family annotation, peripheral role here).
- GO:0046514 ceramide catabolic process: ACCEPT (the reaction performed).
- GO:0051872 sphingosine catabolic process IDA PMID:24465209 (PseudoCAP, full text read):
  cerN generates sphingosine and is upstream of the sph catabolic genes; it does not
  catabolise sphingosine. MODIFY to GO:0046514; PSEUDOCAP WRONG_TERM, CONFIRMED.
