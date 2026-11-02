# Tango5 (Drosophila melanogaster) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Identity
- The benchmark accession Q7KVQ7 (428 aa, TrEMBL) is a **shorter isoform** of Tango5/Vmp1 (FBgn0052675). Q7KVQ7 is an exact C-terminal suffix of Q9W2S1 (530 aa, TrEMBL), starting at Q9W2S1 Met103. It lacks only a disordered N-terminal extension, and keeps all four predicted TM helices plus the KMS1_N and VMP1_C domains. See [file:DROME/Tango5/Tango5-bioinformatics/RESULTS.md].
- Neither UniProt entry is Swiss-Prot reviewed. Q9W2S1 carries 5 RefSeq products and the GO Central PAINT IBA annotations, so it is effectively the gene's canonical product. No review of Q9W2S1 exists in the repo.
- PANTHER: all three of Q7KVQ7, Q9W2S1 and human VMP1 Q96GC9 are in PTHR10281:SF1 (VACUOLE MEMBRANE PROTEIN 1). Global identity to human VMP1 is about 54%. This repo has no PANTHER family review for PTHR10281. (`interpro/panther/PTHR19375` is an unrelated HSP70 family.)
- The PAINT nodes on Q9W2S1 are PTN000031590, with phospholipid scramblase activity (GO:0017128; donor Q96GC9), ER and endomembrane system organization, and PTN000031591, with autophagosome assembly and Golgi organization (donors include FBgn0052675 itself, Q96GC9 and DDB_G0285175). PAINT did **not** propagate protein secretion. I read that as a deliberate decision.

### Fly literature
- Bard et al. 2006 [PMID:16452979] (abstract only): S2-cell genome-wide RNAi secretion screen. The FlyBase comment says Tango5 dsRNA inhibits secretion and causes Golgi–ER fusion in >50% of cells.
- Shen et al. 2021 [PMID:34019822] (full text): "Drosophila Vmp1 (also known as Tango5)". "GFP-Vmp1 co-localizes with the ER markers Sec61β and SERCA in intestine cells". vmp1 RNAi cells "did not accumulate mCherryAtg8a autophagy reporter puncta". vmp1(Δ) cells accumulate Ref2p. The paper also shows defective mitochondrial clearance, increased mitochondria–ER contact, Vps13D acting downstream and Marf suppression. These are necessity and genetic-pathway data.
- Mammalian VMP1 biochemistry: TMEM41B and VMP1 are ATP- and Ca2+-independent phospholipid scramblases [PMID:33929485; PMID:33850023].

### Decisions
- ND molecular_function → MODIFY to GO:0017128. The ND is superseded by the PAINT scramblase node, which covers this subfamily.
- ER (IDA, IEA) → MODIFY to ER membrane GO:0005789. The protein is a multipass integral ER protein, and endogenous GFP-Vmp1 co-localizes with Sec61β.
- Vacuolar membrane (IEA, from the SubCell name) → MARK_AS_OVER_ANNOTATED. The name is historical, and no fly evidence places the protein on the vacuole or lysosome.
- Golgi organization IMP → KEEP_AS_NON_CORE. This is a real screen phenotype that PAINT propagated, but it is probably a downstream effect of ER membrane homeostasis.
- Protein secretion IMP → KEEP_AS_NON_CORE. This is a screen phenotype only, it is likely indirect, and PAINT chose not to propagate it.
- NEW GO:0017128 (IBA, from the PTN000031590 placement) and NEW GO:0000045 autophagosome assembly (PTN000031591, plus the fly Atg8a puncta defect). In the mammalian model the VMP1 scramblase re-equilibrates the ER donor leaflet during ATG2-mediated phagophore expansion. That is participation, not just necessity, and PAINT curators placed it on the node.
- Mitophagy and mitochondria–ER contact phenotypes are not proposed as process annotations. They are downstream organelle phenotypes of the autophagy defect, and are recorded as suggested questions instead.
- Relative to review next: the canonical product Q9W2S1 (same gene). It would go in folder genes/DROME/Tango5__Q9W2S1, because genes/DROME/Tango5 is keyed to Q7KVQ7.

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0017128, GO:0000045) on this accession. GOA already carries the same terms on
another product of the same gene, reviewed in `genes/DROME/Tango5__Q9W2S1/`. GOA propagates gene-level
annotations to one representative product per gene, so adding them to a second product fills a
convention rather than a curation gap. The rows were withdrawn, following the rule applied across the
ProtNLM2 re-review cohorts (first raised in the review of PR #5303). The gene-level function is unchanged.
