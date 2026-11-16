# PA1204 (Q9I4D4) review notes

## Literature

- Crystal structure (1.28 A) of Q9I4D4, an NAD(P)H-dependent FMN reductase; FMN binding confirmed and an unusual FMN-binding motif identified [PMID:16552139 "it has been confirmed to bind flavin mononucleotide and the binding site was identified via X-ray crystallography"]; activity [PMID:16552139 "NADPH-dependent activity has been confirmed with biochemical assays."].
- P. aeruginosa orthologs of MdaB, ChrR, WrbA, NfsB and NQO1 reduce quinones in vitro by a two-electron route [PMID:25085734 "In in vitro assays, each enzyme was shown to reduce quinone substrates with only minimal semiquinone formation."]; only WrbA and MdaB overexpression protected a katA mutant from H2O2 [PMID:25085734 "in a katA mutant, H2O2 challenged strains over-expressing the WrbA and MdaB orthologs grew significantly better than the empty plasmid control"].
- Ryan et al. place PA1204 among putative azoreductases by structure and cite its quinone reductase activity [PMID:24915188 "Recent data have shown that PA0949, PA1204, PA2580 and PA4975, have NAD(P)H quinone oxidoreductase activities [75]."]; PA1204 is in the BexR-repressed pa1202-pa1205 operon [PMID:24915188 "The protein encoded by pa1204 is part of the BexR regulon in P. aeruginosa"].
- PANTHER places PA1204 in PTHR30543 (chromate reductase), subfamily SF21 (Lot6-like); UniProt: SsuE family.

Search: PubMed metadata for all GOA-cited PMIDs; PMID:24915188 full text cached and read for PA1204 passages; PMID:25085734 and PMID:16552139 abstract only. NCBI E-utilities and Europe PMC search were unavailable (HTTP 500/503) during this session.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001254275 | GO:0003955 NAD(P)H dehydrogenase (quinone) activity | 4 | 167 (74 taxa) | GO:0003955, IMP, PMID:25085734 | SOUND | The abstract reports in vitro quinone reduction by the purified P. aeruginosa orthologs, and Ryan et al. name PA1204 among them. The term is right; the evidence code should be IDA (PSEUDOCAP WRONG_EVIDENCE_CODE, PROBABLE). | yeast Lot6 (SGD:S000004001), E. coli ChrR (P0AGE6), Synechocystis ArsH (P74312), all characterised quinone reductases | Yes |

Node term suits the clade (SsuE/ChrR/ArsH/Lot6 FMN-dependent quinone reductases). No GO_CENTRAL defect.

Other PseudoCAP row: GO:0016655 IDA from PMID:24915188 is true but the paper only cites PA1204's activity (WRONG_EVIDENCE_CODE, PROBABLE); set TOO_GENERAL because GO:0003955 is_a GO:0016655.

The GO:0034599 IBA rests on yeast Lot6 alone; no oxidative-stress phenotype has been shown for PA1204, so marked over-annotated (not a seed of this gene).
