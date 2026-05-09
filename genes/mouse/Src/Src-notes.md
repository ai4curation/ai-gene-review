# Src review notes

Falcon deep research attempt was not completed on 2026-05-04 after the provider
timed out during the batch run; no `Src-deep-research-falcon.md` file was
produced. Review decisions used the cached UniProt record, cached publications,
and BioReason research.

Core function judgment: SRC is a non-receptor protein tyrosine kinase with
SH3-SH2-kinase architecture. UniProt describes activation after engagement of
many receptor classes and phosphorylation of receptor/adaptor/cytoskeletal
substrates [UniProt:P05480 "Non-receptor protein tyrosine kinase... activated
following engagement of many different classes of cellular receptors"]. The
BioReason report independently supports the same domain-based call
[file:mouse/Src/Src-deep-research-bioreason.md "A cytoplasmic non-receptor
tyrosine kinase"].

Key local evidence for pathway and localization calls includes Src kinase
activation in growth factor-like signaling [PMID:8910389 "rapidly and
transiently activate Src family tyrosine kinases"], osteoclast function via
Src/Cbl/PI3K signaling [PMID:14739300 "Src kinase activity is essential for
osteoclast function"], Src-induced podosome formation [PMID:21525037
"Src-induced podosome formation"], inflammation-induced epithelial regeneration
through a gp130-Src-YAP module [PMID:25731159 "gp130-Src-YAP module"], and
laminin-induced Rac/JNK activation by Src family kinases [PMID:18044967
"initiated by Src family kinases"].

Curation stance: protein tyrosine kinase activity, non-membrane spanning
protein tyrosine kinase activity, tyrosine phosphorylation, and major
cytoplasmic/plasma-membrane signaling localizations are core. Receptor-specific,
adhesion, osteoclast, podosome, epithelial, mitochondrial, and developmental
terms are kept as non-core pathway contexts. Generic protein-binding and broad
binding labels are marked over-annotated unless the term describes an
informative domain-mediated recognition mode.
