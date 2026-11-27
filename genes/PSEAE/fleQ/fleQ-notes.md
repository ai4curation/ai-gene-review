# fleQ (PA1097, G3XCV0) review notes

## Literature summary

- FleQ heads the flagellar cascade as an NtrC/NifA-type activator [PMID:12218010 "Direct interaction of FleQ with flhA , fliE , fliL , and fleSR promoters was demonstrated by gel shift assay, along with experiments to conclusively determine the specificity of its binding."]; the flhA site works in vivo [PMID:12218010 "Mutagenesis of the FleQ binding site in the flhA promoter confirmed its functionality in vivo."].
- fleQ mutants are non-motile and lose mucin adhesion [PMID:9287015 "A chromosomal insertional mutation in the fleQ gene abolished mucin adhesion and motility of P. aeruginosa PAK and PAK-NP."]; FleQ and RpoN drive fleSR [PMID:9287015 "Promoter fusion experiments showed that the fleSR operon was regulated by RpoN and FleQ."] and the class II genes [PMID:14617143 "Class II genes including fleSR, encoding a two-component regulatory system require FleQ and RpoN (sigma54) for their transcriptional activation."].
- FleQ is a c-di-GMP receptor: it binds pel promoter DNA, and c-di-GMP inhibits the binding [PMID:18485075 "FleQ binds to pel promoter DNA and that this binding is inhibited by c-di-GMP."]; it binds c-di-GMP [PMID:18485075 "FleQ binds radiolabelled c-di-GMP in vitro."].
- At pelA it is both repressor and activator [PMID:22581773 "FleQ acts as a repressor in the absence of c-di-GMP and as an activator in the presence of c-di-GMP."], at two sites [PMID:22581773 "FleQ binds to two sites called box 1 and 2."].
- c-di-GMP binds at the Walker A motif and inhibits ATPase [PMID:24167275 "a relatively low concentration of c-di-GMP competitively inhibited FleQ ATPase activity"; "a FleQ Walker A motif mutant failed to bind c-di-GMP"].
- FleN is an antiactivator that does not block DNA binding [PMID:11673434 "FleN does not inhibit the DNA binding ability of FleQ in vitro, thus indicating that it probably utilizes another mechanism(s) to serve as a FleQ antiactivator."].

Literature search (2026-11-05): PubMed MCP and NCBI E-utilities returned server errors throughout; Europe PMC
was intermittently available. Review based on the cached PMIDs above (18485075, 22581773, 12218010, 11673434 full
text; 9287015, 14617143, 24167275 abstract only) and QuickGO queries of the node seeds.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000787214 | GO:0000987 cis-regulatory region sequence-specific DNA binding | 4 | 214 (28 taxa) | GO:0000987, IDA, PMID:18485075 | SOUND | Full text: gel-shift binding of purified FleQ to pel promoter DNA, inhibited by c-di-GMP. | E. coli GlrR P0AFU4 (IDA PMID:19843219), FhlA P19323 (IDA PMID:8034727), NorR P37013 (IDA PMID:15375149) | Yes; three EcoCyc IDA seeds |
| PTN000787214 | GO:0001216 DNA-binding transcription activator activity | 6 | 214 (28 taxa) | GO:0001216, IMP, PMID:22581773 | SOUND | Full text: footprinting at pelA box 1/box 2 and box-mutant lacZ fusions show c-di-GMP-dependent activation from box 1. The same row from CollecTF (IMP, IPI) is also a seed. | X. campestris FleQ Q8P9D2, P. aeruginosa CbrB Q9HV73, V. cholerae FlrA Q9KQ67 and VC_0665 Q9KU59, Geobacter GnfM Q74EF9 (CollecTF IMP/IPI) | Yes; five independent CollecTF-seeded orthologues/paralogues |

Node-level assessment for PTN000787214 (recorded once here, on fleQ, the gene with the most direct evidence;
cross-referenced from genes/PSEAE/algB/algB-notes.md). The node is a clade of sigma-54 enhancer-binding proteins
(PTHR32071). All four IBD terms on it (GO:0000987, GO:0001216, GO:0032993, GO:0045893) rest on several independent
experimental seeds from E. coli (EcoCyc), Vibrio, Xanthomonas and Geobacter (CollecTF), checked live in QuickGO on
2026-11-05. The terms suit the clade. No GO_CENTRAL defect is needed; the IBDs stand without the FleQ and AlgB
seeds. One caveat for the clade: FleQ and AlgB can also act at sigma-70/sigma-22 promoters and FleQ also
represses, but that does not undermine the activator, DNA-binding and positive-regulation node terms.

## Source defects (non-seed rows)

- GO:2000155 positive regulation of cilium-dependent cell motility (IMP, PMID:12218010): eukaryote-only term
  (only_in_taxon Eukaryota). PSEUDOCAP WRONG_TERM, CONFIRMED, repoint to GO:1902210.
- GO:0006351 DNA-templated transcription (IDA, PMID:9287015): an activator annotated to transcription itself.
  PSEUDOCAP WRONG_TERM, PROBABLE (abstract only), repoint to GO:0045893.

## Action summary

32 rows. ACCEPT 16; KEEP_AS_NON_CORE 7 (GO:0032993 x5, GO:0010811, GO:1901202); TOO_GENERAL 7 (GO:0000976 x4,
GO:0006355 x2, GO:0043565); MODIFY 2 (GO:0006351, GO:2000155).
