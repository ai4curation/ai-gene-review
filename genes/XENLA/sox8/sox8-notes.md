# sox8 (Xenopus laevis, Q6VVD7) — curation notes

Project context: NEURAL_CREST_ORIGINS, Tier 1 (neural crest specifier, SoxE group with sox9 and sox10).

## Identity

- SOX8_XENLA, 459 aa, Swiss-Prot reviewed; sox8.L (Xenbase XB-GENE-480869). SoxE-group HMG-box
  transcription factor: Sox_N/DIM dimerisation region (56-96), HMG box (98-166), TAM (222-297) and
  TAC (342-459) transactivation domains, 9aaTAD motif (413-421) (UniProt features, by similarity to
  mouse Sox8 P57073). PANTHER PTHR45803:SF2 "TRANSCRIPTION FACTOR SOX-8".
- Only one *X. laevis* sox8 entry is reviewed; no S homeolog accession is curated here.

## Molecular activity (family-level, not Q6VVD7-specific)

- SoxE HMG domain binds the minor groove and bends DNA [PMID:39936824 "binds to the DNA in the minor groove causing 70-85° bending toward the major groove"].
- No *Xenopus* Sox8 ChIP/CUT&RUN, EMSA or reporter assay was found; MF is inferred from the
  conserved HMG box and transactivation domains plus the IBA. Treat RNA Pol II-specific
  DNA-binding TF activity as solid; activator vs repressor is not established for this protein.

## Expression (network-layer placement)

- Earliest SoxE in frog crest: [PMID:16943273 "Sox8 accumulates at the lateral edges of the neural plate at the mid-gastrula stage; in contrast to its mouse and chick orthologs, Sox8 expression precedes that of Sox9 and Sox10 in neural crest progenitors"].
- Persists in migrating crest [PMID:16943273 "Sox8 expression persists in migrating cranial crest cells as they populate the pharyngeal arches and in trunk neural crest cells"].
- Low-level blastula transcripts that disappear by gastrulation; reappear in NC regions at mid-gastrula
  [PMID:30144418 "A third SoxE factor, Sox8, is expressed at low levels in blastula stage embryos but is not detectable by the onset of gastrulation"]. So, unlike SoxB1 factors, Sox8 is not a sustained blastula pluripotency factor.
- Single-cell timing: early/immature NC programme [PMID:38683994 "gene programs that define early and immature neural crest cells (e.g. expression of snail2, foxd3, and sox8 genes)"].
- Species differences in SoxE order [PMID:33424631 "In Xenopus, sox8 is expressed first followed by sox9 then sox10"]; [PMID:33424631 "In zebrafish, sox9a and sox9b expression precedes that of sox10 in the neural crest while sox8 is not expressed in these cells"].

## Upstream inputs (Sox8 is downstream of the border specifiers)

- Pax3 + Zic1 (border specifiers) induce sox8 as an early NC specifier [PMID:23509273 "a group of early genes ( snail1 , sox8 , and myc ) was activated during early neurulation (between stages 12 and 15)"]; [PMID:23509273 "these transcription factors cooperate to activate the NC specifiers snail2 ( snai2 ), soxE ( sox8, 9, 10 ), and foxd3 in the ectoderm"].
- Microarray of Pax3/Zic1 targets recovers sox8 [PMID:24360908 "This group included 10 well-characterized NC-specific genes: ednra, foxd3, gbx2, olig4, snail2, sox8, sox9, tcf7, twist and zic5"]. Not shown to be direct.

=> Network layer: **neural crest specifier** (first-wave), not border specifier. It is induced by the
border module (Pax3/Zic1, AP2a, Wnt + BMP attenuation), not the converse.

## Loss of function

- Morpholino knockdown [PMID:16943273 "Although morpholino-mediated knockdown of Sox8 protein did not prevent the formation of neural crest progenitors, the timing of their induction was severely affected"].
- Lineage consequences attributed to migration failure [PMID:16943273 "We demonstrate that these defects are due to the inability of neural crest cells to migrate into the periphery, rather than to a deficiency in neural crest progenitors specification and survival"].
- Authors' conclusion [PMID:16943273 "the control of Sox8 expression at the neural plate border is a key process in initiating neural crest formation in Xenopus"].
- Abstract-only in cache; full text not read. Rescue by SoxE paralogs reported secondarily
  [PMID:33424631 "The neural crest can be rescued in Sox8 morphants by any of the SoxE factors suggesting there is functional redundancy between the SoxE factors"].

## Gain of function / sufficiency

- No sox8-specific GOF in cached literature. SoxE proteins are functionally equivalent in frog
  [PMID:16256735 "the activities of individual SoxE factors are well conserved"]; Sox9/Sox10 GOF expands crest
  (see sox9-a, sox10 reviews). Sufficiency of Sox8 itself is inferred from equivalence and the
  cross-rescue, not shown directly.

## Synthesis / decisions

- MF: GO:0000981 + GO:0000978 (IBA) accepted; nucleus accepted.
- Process: the neural crest formation rows (IMP, ARBA IEA) are refined to GO:0014036 neural crest cell fate
  specification (part_of neural crest formation), consistent with sox9-a and sox10 reviews. GO:0014029 is
  defined as formation of the ectodermal region itself, which in the project framing belongs to the border
  layer. For the IMP row I also propose GO:0001755 neural crest cell migration because the authors
  explicitly attribute the lineage defects to failed migration. Caveat: the migration defect may be a
  downstream consequence of delayed specification; flagged as a question.
- PNS/ENS development, epithelium morphogenesis, negative regulation of transcription: IBA family-level
  transfers dominated by mammalian Sox9/Sox10 biology; plausible but non-core for frog Sox8.
- Mammalian Sox8 is largely dispensable [PMID:39936824 "Sox8 is not essential for the proper development of any of the involved systems, as it functions redundantly with Sox9 or Sox10"]. Frog dependence on Sox8 is therefore a lineage-specific (paralog-allocation) feature.

## Evolution (for NEURAL_CREST_ORIGINS)

- Gnathostome Sox8/9/10 and lamprey SoxE1-3 arose by independent duplications [PMID:21889937 "understanding the independent evolution of duplicated SoxE genes among agnathan and gnathostome vertebrates"]; [PMID:39936824 "SoxE genes independently duplicated from a common ancestor in the vertebrate groups of agnathans (primitive jawless fishes) and gnathostomes (jawed vertebrates)"].
- Lamprey SoxE1/2 occupy the early neural fold/crest role [PMID:33424631 "SoxE1 and SoxE2 are expressed in the neural folds and migrating neural crest while SoxE3, the ortholog to Sox9 in gnathostomes, lacks early embryonic expression"].
- Amphioxus: [PMID:22241841 "neural crest enhancers are not detected proximal to amphioxus soxE"].
- Interpretation: the NC-specifier role belongs to the vertebrate SoxE group, recruited into the crest
  by cis-regulatory change; which paralog carries the earliest role is species-specific (Sox8 in frog,
  Sox9 in chick/mouse, sox9a/b in zebrafish, SoxE1/2 in lamprey). So frog Sox8's specifier role is not
  evidence for an ancestral Sox8-specific function, and orthology-based transfer of it to other species
  (e.g. zebrafish sox8, not expressed in NC) would be unsafe.

## Open questions

- No GO term for neural plate border formation/specification (project-wide issue).
- Is the sox8 MO migration phenotype a separate requirement or a consequence of delayed specification?
- Direct targets of Sox8 (sox10? snai2? foxd3?) unknown in frog.
