
## Horse-pair evidence and exact protein model

The selected horse ALG5 A0A5F5PM72 retains the N-terminal hydrophobic membrane anchor, but the 294-aa sequence deletes canonical human residues 95–124. The remaining 294 residues align at 94.6% identity. Do not equate sequence-family identity with demonstrated activity of a deletion-bearing model. The horse GOA enzyme activity is UNDECIDED pending model/structure validation; ER membrane residence remains supported by the preserved anchor.

[PMID:10359825](https://pubmed.ncbi.nlm.nih.gov/10359825/), DOI [10.1073/pnas.96.12.6982](https://doi.org/10.1073/pnas.96.12.6982), studies BOTH ALG5 and ALG6 despite its ALG6-focused title. “Expression of the human ALG5 and ALG6 cDNA could partially complement the respective S. cerevisiae alg5 and alg6 deficiency.” This supports human ALG5 glucose-donor pathway identity and demonstrates why title-only paralog attribution is unsafe. The independent human UniProt biochemical statement is explicitly experimental-source-derived, not ARBA.

The ProtNLM paragraph instead describes GDP-mannose transfer and DPM synthase, which are not established properties of this ALG5-family sequence. The internal deletion does not itself establish conversion to a GDP-mannose-dependent enzyme. No horse functional paper was identified; human deep research is prioritized.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined both GOA rows, the description and core functions for A0A5F5PM72 without opening any ProtNLM2 file. New analysis: `ALG5-bioinformatics/compare_isoforms_rereview.py` -> `RESULTS-rereview.md`, `results-rereview.json` (inputs `Q9Y673-2-rereview.fasta`, `horse_ALG5_all_models-rereview.fasta`, `alg5_sf91_orthologs-rereview.fasta`, fetched from UniProt REST 2026-10-20).

Deep research: `just deep-research HORSE ALG5 --provider falcon` failed ("Exception: Failed to authenticate", provider falcon exited with code 1). No horse deep-research file exists; I used the human ALG5 falcon report, the human UniProt record and the cached PMID:10359825 full text.

### Identity of the benchmark accession (isoform / alternative gene model)

- A0A5F5PM72 (294 aa; Ensembl ENSECAT00000069953.2, gene ENSECAG00000024592) is an alternative-splice gene model of horse ALG5, not the canonical full-length product. It lacks exactly the segment that human isoform 2 lacks: human Q9Y673 isoform 1 is 324 aa, isoform 2 (VSP_041019, residues 95-124 missing) is 294 aa, and the horse model pairs over all 294 residues with isoform 2 with no gaps (278/294 identical) [file:HORSE/ALG5/ALG5-bioinformatics/RESULTS-rereview.md].
- The missing human segment is `QKRDPAFTYEVIVVDDGSKDQTSKVAFKYC`. Its core, a hydrophobic strand followed by a V-V-D-D-G-S-x-D motif, is conserved in every PTHR10859:SF91 ortholog compared (mouse, Drosophila, Dictyostelium, S. pombe, S. cerevisiae; e.g. yeast `EIVIVDDGSTDNT`). It lies inside the Pfam Glycos_transf_2 (PF00535) domain, which UniProt maps to horse 85-216, just before the junction. The DXD motif (ADADG, horse position 132) and the C-terminal region are retained.
- None of the ten horse ALG5 UniProt entries is a full-length 324-aa product. Nine contain the segment (horse `QKQDPTFTYEVIVVDDGSKDQTSEVAFKYC`) but each is truncated or diverged at the N- or C-terminus or has another internal deletion. A0A5F5PM72 is the only one with the complete N-terminal anchor and complete C-terminus, and it lacks the segment. UniProt therefore has no canonical horse ALG5 (isoform-1 equivalent).
- No isoform-2-specific activity has been reported for any species (UniProt Q9Y673 records isoform 2 only as an alternative product from a cDNA project, PubMed:14702039). Whether a GT2 enzyme missing a conserved strand and the DDGS motif keeps Dol-P-Glc synthase activity is unknown.

### Evolutionary grounding

- PANTHER: horse, human, mouse, fly, S. pombe and S. cerevisiae ALG5 are all in PTHR10859:SF91 (DOLICHYL-PHOSPHATE BETA-GLUCOSYLTRANSFERASE), separate from the DPM1 (mannosyltransferase) subfamily. So the gene is an ALG5 ortholog, and glucose (not mannose) transfer is the gene-level function.
- PAINT (interpro/panther/PTHR10859/PTHR10859-paint.tsv): GO:0004581 and GO:0006488 are IBD at PTN001653583, and GO:0005789 ER membrane is IBD at PTN000092356 (eukaryotes). Experimental donors include human Q9Y673, FB:FBgn0261020 (wol), PomBase SPBC56F2.10c and SGD S000006148. This horse entry has only IEA rows (EC and SubCell mappings) and no IBA.
- Human experimental basis: human ALG5 cDNA partially complements yeast alg5 [PMID:10359825 "Expression of the human ALG5 and ALG6 cDNA could partially complement the respective S. cerevisiae alg5 and alg6 deficiency."]. Note that the 1999 human cDNA was described as encoding 242 aa [PMID:10359825 "encoding a polypeptide of 242 amino acids"], a shorter ORF than the current 324-aa canonical sequence; the paper does not say which isoform region it contains.

### Decisions

- GO:0004581 (IEA, EC mapping): stays UNDECIDED. Glucose transfer is the gene-level function by SF91 orthology, but this particular product lacks a subfamily-invariant motif segment, and no isoform-2 activity data exist. Neither ACCEPT nor REMOVE is justified for this accession.
- GO:0005789 ER membrane (IEA, SubCell): ACCEPT. The signal-anchor TM (horse 8-28) is preserved, and ER membrane is a PAINT IBD across eukaryotes.
- No NEW rows. GO:0006488 dolichol-linked oligosaccharide biosynthesis would depend on the unresolved catalytic competence of this product.
- Core function: written at the gene level (ALG5 Dol-P-Glc synthase) with an explicit caveat that the competence of A0A5F5PM72 is unresolved.

### Family review / modules

- interpro/panther/PTHR10859/PTHR10859-review.yaml uses A0A5F5PM72 as an SF91 representative and says glucose transfer applies "including the matched horse target by orthology". The SF91 placement is correct. However, a 30-residue-deleted isoform model is a weak representative for the GO:0004581 claim, and the family review does not mention the deletion.
- Modules: modules/dolichol_phosphate_sugar_donor_supply.yaml (ALG5 Dol-P-Glc step); modules/n_glycan_llo_assembly_lumenal.yaml (ALG6/ALG8/ALG10 consumers of Dol-P-Glc); modules/n_glycan_llo_assembly_cytoplasmic.yaml (context only).
- Relative to review next: human ALG5 Q9Y673 (same SF91 subfamily; PAINT donor). genes/human/ALG5/ALG5-ai-review.yaml exists with all rows actioned and core functions (status field IN_PROGRESS). The task rule about a same-gene canonical product does not apply because UniProt has no canonical full-length horse ALG5 entry.
