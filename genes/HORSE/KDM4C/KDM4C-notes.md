# KDM4C (horse, Equus caballus; UniProt A0A3Q2HAR2) - review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used. This is the first review of this horse accession.

### Identity

- Unreviewed TrEMBL entry, 1053 aa, Ensembl ENSECAP00000030682.2, VGNC:19338 KDM4C, PE 3.
  Domains: JmjN (16-58), JmjC (144-310), PHD/EPHD (749-862), two Tudor domains (Pfam Tudor_2 x2).
- PANTHER PTHR10694:SF104 (LYSINE-SPECIFIC DEMETHYLASE 4C), same subfamily as human Q9H3R0 and
  mouse Q8VCD7 (interpro/panther/PTHR10694/PTHR10694-entries.csv). No disagreement with the
  repo PANTHER files; there is no family review under interpro/panther/PTHR10694 (only entries
  and metadata).
- Alignment to human KDM4C (KDM4C-bioinformatics/RESULTS.md): 91.17% identity, 99.72% coverage
  of human; all Fe(II), 2OG and Zn ligands conserved. Not a fragment or isoform; it is the
  canonical full-length horse KDM4C gene product.

### Deep research

`just deep-research-falcon HORSE KDM4C --fallback perplexity-lite` failed: falcon
"Failed to authenticate", perplexity-lite HTTP 401 insufficient_quota. Review proceeds from
cached literature and UniProt.

### Evidence

- [PMID:16732293 "we identified the protein GASC1 (gene amplified in squamous cell carcinoma 1), which belongs to the JMJD2 (jumonji domain containing 2) subfamily"]; [PMID:16732293 "three members of this subfamily of proteins demethylate H3K9me3/me2 in vitro through a hydroxylation reaction requiring iron and alpha-ketoglutarate as cofactors"]
- [PMID:16603238 "other human JMJD2 subfamily members also functioned as trimethylation-specific demethylases"]
- [PMID:17277772 "Assembly of ligand-bound androgen receptor and JMJD2C on androgen receptor-target genes results in demethylation of trimethyl H3K9 and in stimulation of androgen receptor-dependent transcription"]
- [PMID:21914792 "KDM4A–C, which are highly conserved in all vertebrates, and demethylate both H3K9 and H3K36"]
- Human UniProt (ECO:0000269 PMID:16603238, 28262558): "Demethylates trimethylated H3 'Lys-9' and H3 'Lys-36' residue, while it has no activity on mono- and dimethylated residues."
- [PMID:28262558 "KDM4C H190A/E192A"] used as catalytically inactive control; horse H190/E192 conserved.

### PAINT reading

- H3K9 and H3K36 demethylase IBAs come from PTN000075207 (KDM4/JHDM3 clade). The H3K36 donor set
  lists KDM4A/B/C relatives but not KDM4D/E, matching the experimental finding that KDM4D/E are
  H3K9-only; horse KDM4C is in the dual-specificity KDM4A-C subclass.
- chromatin, nucleus, chromatin remodeling, regulation of gene expression come from the deep
  node PTN000075014.
- Human KDM4C IDA/IMP terms not propagated by PAINT (AR binding, transcription coactivator,
  positive regulation of cell population proliferation) are treated as deliberate omissions and
  not proposed as NEW.

### Decisions

- chromatin (IBA), nucleus (IBA, IEA): ACCEPT.
- chromatin remodeling (IBA): ACCEPT; histone demethylase activity is part_of chromatin remodeling in GO.
- H3K9 demethylase (IBA, IEA): MODIFY to H3K9me2/H3K9me3 demethylase (GO:0140684), which the gene already carries (EC).
- H3K9me2/me3 demethylase (IEA, EC): ACCEPT, core.
- H3K36 demethylase (IBA): MODIFY to H3K36me2/H3K36me3 demethylase (GO:0140681) (trimethyl-specific; consistent with donkey KDM4C review).
- metal ion binding (IEA): MODIFY to ferrous iron binding + zinc ion binding (cofactor sites conserved).
- DNA-templated transcription (IEA): MARK_AS_OVER_ANNOTATED; it modifies chromatin and does not synthesise RNA.
- regulation of DNA-templated transcription (IEA), regulation of gene expression (IBA): MODIFY to positive regulation of transcription by RNA polymerase II (human IDA, AR target genes).

### Relative

Human KDM4C (Q9H3R0), same PANTHER subfamily SF104 and the PAINT donor for the KDM4 node;
no review exists in genes/human/. Donkey KDM4C (genes/EQUAS/KDM4C, A0A9L0K3L6) is the cohort
partner and already reviewed.
