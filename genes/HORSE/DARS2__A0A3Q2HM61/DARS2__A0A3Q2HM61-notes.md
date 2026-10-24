# DARS2 (horse, A0A3Q2HM61) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: A0A3Q2HM61 (652 aa, unreviewed TrEMBL), product of Ensembl gene
ENSECAG00000004044 (ENSECAT00000043786), chosen as the gene-centric canonical DARS2
product in the horse reference proteome UP000002281. No ProtNLM2 file or prediction
evidence was opened or used.

### Deep research

`just deep-research-falcon HORSE DARS2__A0A3Q2HM61 --fallback perplexity-lite` failed:
falcon raised "Failed to authenticate" (Edison JWT), and the perplexity-lite fallback
returned HTTP 401 "insufficient_quota". No deep-research file exists for this folder.
The review relies on the cached human literature (PMID:15779907, PMID:23275545,
PMID:30006346), the human DARS2 review (`genes/human/DARS2/`), and the sequence and
PANTHER-tree analysis already in `genes/HORSE/DARS2/DARS2-bioinformatics/RESULTS-rereview.md`
(read only; not modified).

### Experimental status in horse

There is no experimental characterisation of horse DARS2. The UniProt record has only
genome-sequencing references (PMID:19892987, the horse genome paper) and every
functional comment is ARBA-derived. All 10 GOA rows are IEA (InterPro2GO, EC2GO,
SubCell, ARBA/combined). Every function in this review is therefore inferred, not
established in horse.

### Evolutionary grounding

- PANTHER: `PANTHER; PTHR22594:SF5; ASPARTATE--TRNA LIGASE, MITOCHONDRIAL` in the
  UniProt record; human DARS2 Q6PI48 is in the same subfamily.
- PANTHER 19 tree (from the sibling analysis): horse leaf PTN001475968 and human leaf
  PTN002503203 share the path from the family root through PTN000502597 (SF5 root; PAINT
  IBD for aspartate-tRNA ligase activity and aspartyl-tRNA aminoacylation) and
  PTN000502598 (PAINT IBD for mitochondrion) down to PTN000502607. Horse DARS2 is the
  one-to-one ortholog of human DARS2.
- HAMAP MF_00044 (Asp_tRNA_synth_type1), NCBIfam TIGR00459 (aspS_bact): bacterial-type
  AspRS, i.e. discriminating Asp-specific type, not the non-discriminating AspRS/GluRS
  types. Note that DARS2 SF5 and E. coli AspS share this bacterial type; the eukaryotic
  cytosolic DARS1 lies in another subfamily of PTHR22594 and its functions (e.g.
  multisynthetase complex membership) are not transferred.
- Sequence: A0A3Q2HM61 is 89.9% identical to human Q6PI48 over 643 paired residues; all
  human UniProt substrate-binding residues (aspartate region 244-247 QQFK, ATP/Asp 266-268
  RDE, ATP E535, Asp R542, ATP 584-587 GLDR) are conserved, and the Arg-rich N-terminal
  transit region is retained. Unlike the benchmark isoform A0A9L0SB67, A0A3Q2HM61 retains
  the full insertion domain (human 341-376 present).

### Human experimental anchors (transferred via the SF5 orthology)

- Aminoacylation of mitochondrial and E. coli tRNA(Asp), dimeric enzyme
  [PMID:15779907 "Both belong to the expected class of synthetases, have a dimeric
  organization, and aminoacylate Escherichia coli tRNAs as well as in vitro transcribed
  human mitochondrial tRNAs."]
- Kinetics on mt-tRNA(Asp) transcripts and crystal structure [PMID:23275545 "the mt-aaRS
  charged both cognate and non-cognate tRNAs with similar efficiency"].
- Soluble plus electrostatically membrane-associated sub-mitochondrial pools
  [PMID:30006346 "Chemical treatments revealed that mt-AspRs is anchored in the
  mitochondrial membrane through electrostatic interactions"].

### Notable absence

Horse A0A3Q2HM61 carries no IBA rows in GOA even though its PANTHER leaf sits under the
PAINT nodes that give human DARS2 its IBA annotations. Possibly the IBA is propagated to a
different horse accession of the same gene (PANTHER places one leaf per gene). This is a
propagation-target curation matter, not a biological gap.

### Decisions

- GO:0004815 aspartate-tRNA ligase activity: ACCEPT (core).
- GO:0005759 mitochondrial matrix: ACCEPT (core location).
- GO:0005524 ATP binding: ACCEPT (substrate binding in the catalytic mechanism; residues
  conserved).
- GO:0006418: MODIFY to GO:0070127 tRNA aminoacylation for mitochondrial protein
  translation (the enzyme catalyses the charging step; mitochondrial context supported by
  orthology to the human mt-AspRS).
- GO:0003676 nucleic acid binding: MODIFY to GO:0000049 tRNA binding (anticodon-binding
  OB fold, IPR004365).
- GO:0000166, GO:0004812, GO:0016874, GO:0005737: TOO_GENERAL (entailed by accepted
  specific terms).
- GO:0031966 mitochondrial membrane: KEEP_AS_NON_CORE (human peripheral pool; function
  unknown).
- Did not add: secreted/extracellular immune-modulating roles reported for human DARS2
  (PMID:39039092) and FBXO24 interaction; those are single-species human findings not
  covered by PAINT and are not transferred.
