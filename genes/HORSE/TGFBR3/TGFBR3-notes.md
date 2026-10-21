# TGFBR3 (horse, Equus caballus) — F7E1V2

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This is the first review of this entry. ProtNLM2 predictions were not consulted.

### Data and literature
- `just fetch-gene HORSE F7E1V2 --alias TGFBR3`: 15 GOA rows, all electronic (IBA, ARBA IEA,
  SubCell IEA). Horse has no experimental TGFBR3 literature.
- Deep research (`just deep-research-falcon HORSE TGFBR3 --fallback perplexity-lite`) FAILED:
  the Edison API returned "Failed to authenticate" (403), and the perplexity-lite fallback also
  failed. No deep-research file exists. The review uses primary literature on the rat, mouse,
  human and chicken orthologs, cached in publications/. All of these are abstract-only.

### Identity / gene model
- F7E1V2 is the unreviewed TrEMBL entry from Ensembl ENSECAT00000021086.3 (809 aa). It is the
  only horse TGFBR3 entry in UniProt. PANTHER PTHR14002:SF7 is the same subfamily as human
  Q03167, mouse O88393 and rat P26342.
- Sequence comparison [file:HORSE/TGFBR3/TGFBR3-bioinformatics/RESULTS.md]: 87% identity to human
  over 806 aligned residues. Horse residues 1-41 do not align with human 1-80, and the horse
  N-terminus has no signal-peptide h-region. This is likely a gene-model error in the first exon.
  The GAG serines (horse S494/S505), the phospho-Thr (T798), the ZP domain, the TM helix and the
  C-terminal STA tail are all conserved. So this is the full-length ortholog with a defective
  N-terminal model, not an isoform or a fragment that lacks functional domains.

### Biology (orthologs; transfer justified by PANTHER SF7 + PAINT PTN002678643)
- Betaglycan is a membrane-anchored proteoglycan that binds TGF-beta with high affinity
  [PMID:1657406 "a polymorphic membrane-anchored proteoglycan with high affinity for transforming growth factor-beta (TGF-beta)"].
- It presents ligand to TbetaRII. TGF-beta binds the N-terminal endoglin-related region, and the
  GAG chains are not needed for this [PMID:8106553 "presents TGF-beta to the type II signaling receptor"].
  Soluble shed betaglycan acts as an antagonist [PMID:8106553 "recombinant soluble betaglycan acts as potent inhibitor of TGF-beta binding to membrane receptors"].
- Its cytoplasmic domain is phosphorylated by TbetaRII and is needed for TGF-beta2 signalling
  [PMID:11323414]. Beta-arrestin2 binding leads to internalisation and downregulation
  [PMID:12958365].
- It is an inhibin coreceptor with ActRII [PMID:10746731] and a BMP receptor that binds
  BMP-2/4/7 and GDF-5 [PMID:18184661].
- Endocardial EMT in the chick heart requires TBRIII [PMID:10092230]. BMP-2 stimulates
  TbetaRIII-mediated EMT [PMID:18184661]. Tgfbr3-null mice die with heart and liver defects
  [PMID:12773577]. That is necessity evidence, not a participation term.
- It regulates epithelial cell migration through beta-arrestin2/Cdc42, independently of
  TGF-beta signalling [PMID:19416857].

### Decisions summary
- MF GO:0005024 rows (IBA + ARBA) -> MODIFY to GO:0070123 TGF-beta receptor activity, type III.
  This is the specific child; human and rat carry it by IDA.
- GO:0016477 cell migration -> MODIFY to GO:0030334 regulation of cell migration. TGFBR3 modulates
  migration and does not drive it.
- GO:0090100 -> MODIFY to GO:0030513 and GO:0030511.
- GO:0048513 animal organ development -> MARK_AS_OVER_ANNOTATED. It is an uninformative ARBA
  term that rests on knockout phenotypes.
- GO:0005539 glycosaminoglycan binding -> KEEP_AS_NON_CORE. Rodent curators assert it
  experimentally, but the abstracts do not show it, and betaglycan is better described as a
  GAG-bearing proteoglycan.
- All other rows are accepted. The relative to review next is human TGFBR3 (Q03167): it has no
  review in the repo.
