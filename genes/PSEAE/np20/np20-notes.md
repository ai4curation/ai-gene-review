# np20 / zur (PA5499, Q9HT74) review notes

## Literature

- Np20 is the P. aeruginosa zinc uptake regulator (Zur): np20 is co-transcribed with znuC and znuB; Δzur cells accumulate more intracellular zinc; znuA transcription is zinc-repressed in PAO1 but not in PAO-Zur [PMID:24086521 "transcription of znuA was repressed in a zinc-dependent manner in strain PAO1, however zinc-dependent transcriptional repression was alleviated in strain PAO-Zur"]; recombinant Zur binds the znuA promoter, and binding is lost with the zinc chelator TPEN [PMID:24086521 "Electrophoretic mobility shift assays also revealed that recombinant ZurPA specifically binds to the promoter region of znuA and does not bind in the presence of the zinc chelator N,N',N-tetrakis(2-pyridylmethyl) ethylenediamine (TPEN)."]. Full text cached (PMC3781045).
- In a transposon screen for pyocyanin-deficient mutants, an np20 mutant had reduced transcription of several quorum-sensing-controlled genes [PMID:12426334 "Third, mutations in the putative regulators np20 and PA3946 reduced transcription of a number of quorum sensing-controlled genes, showing that these functions participate in the quorum-sensing regulatory network."]; the authors note np20 is a Zur homologue. The mechanism linking Zur to pyocyanin was not examined. Full text cached.
- Domain: Fur family (PF01475), PANTHER PTHR33202 (zinc uptake regulation protein); PIRSR zinc-binding site.

Search: PubMed metadata for both GOA-cited PMIDs, both full texts cached and read for the np20 passages. NCBI E-utilities and Europe PMC search were unavailable (HTTP 500/503) during this session.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002112386 | GO:0045892 negative regulation of DNA-templated transcription | 16 | 83 (37 taxa) | GO:0045892, IDA, PMID:24086521 | SOUND | Full text: zinc-dependent repression of znuA lost in Δzur, plus specific, zinc-dependent EMSA binding to the znuA promoter. | 15 others incl. Fur of E. coli (P0A9A9), B. subtilis (P54574), P. aeruginosa (Q03456), Listeria (Q8Y5U9) and M. tuberculosis Zur (P9WN85) | Yes |
| PTN002112386 | GO:1900376 regulation of secondary metabolite biosynthetic process | 2 | 71 (33 taxa) | GO:1900376, IMP, PMID:12426334 | INDIRECT-PHENOTYPE | Full text: a pleiotropic transposon-mutant phenotype (less pyocyanin, lower expression of quorum-sensing-controlled genes) with no mechanism shown; Np20's demonstrated function is zinc-responsive repression of zinc uptake genes. PSEUDOCAP defect DELETE_ROW, PROBABLE. | P. aeruginosa Fur (Q03456; PseudoCAP IMP GO:1900705 negative regulation of siderophore biosynthesis, PMID:8885270) | No: it would rest on Fur alone, a Fur-lineage function, while the node is the whole Fur superfamily (Fur, Zur, PerR, Irr and others) |

Node-level GO_CENTRAL defect for the GO:1900376 IBD at PTN002112386 is already recorded once, on the GO:1900705 row of `genes/PSEAE/fur/fur-ai-review.yaml` (WRONG_TERM, CHECK, PROBABLE); it is not duplicated here. Note that the fur defect described the np20 seed as reasonable for that gene; this review finds it an indirect phenotype, which strengthens the case for withdrawing the IBD. The GO:1900376 IBA row on np20 is removed.

The other PTN002112386 IBDs (GO:0045892, GO:0003700, GO:0000976, GO:0008270) rest on many characterised Fur-family repressors and stand (see the fur notes).
