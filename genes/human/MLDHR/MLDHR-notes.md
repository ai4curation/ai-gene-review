# MLDHR (MP31; PTEN uORF micropeptide; UniProt C0HLV8) - review notes

## 2026-10-03 - initial review (claude-code)

### Identity
- 31-aa peptide (MWRDSLCAAAGYALGAGTRLRSVLSSRKLQP) encoded by an upstream ORF in the 5' UTR of
  PTEN (chr10). Separate UniProt entry (C0HLV8, PE1) with its own HGNC symbol MLDHR
  (HGNC:55481), so it gets its own folder. It is NOT PTEN-L (P60484-2), which is an in-frame
  N-terminally extended PTEN isoform.
- InterPro IPR054159 / Pfam PF22001 "MP31" (single-member family). No PANTHER/PAN-GO
  ("0 GO annotations based on evolutionary models").
- UniProt: partial protein sequence 4-19 by MS; S5A and Y12A abolish LDHA/LDHB interaction.

### Literature (whole literature is from one lab, Zhang N, Sun Yat-sen Univ.)
- PMID:33406399 (Huang et al. 2021 Cell Metab; abstract-only in cache, no PMC). Primary paper.
  [PMID:33406399 "MP31, a micropeptide encoded by the upstream open reading frame (uORF) of phosphatase and tensin homolog (PTEN) acting as a \"circuit breaker\" that limits lactate-pyruvate conversion in mitochondria by competing with mitochondrial lactate dehydrogenase (mLDH) for nicotinamide adenine dinucleotide (NAD+)"]
  - Mouse homolog KO: [PMID:33406399 "Knocking out the MP31 homolog in mice enhanced global lactate metabolism, manifesting as accelerated oxidative phosphorylation (OXPHOS) and increased lactate consumption and production"]
  - Tumour suppressor in astrocyte cKO; recombinant peptide crosses BBB.
  - Erratum PMID:33535099 (not cached; erratum only).
- PMID:37280112 (Huang et al. 2023 Neuro Oncol; full text in PMC). Second paper.
  - [PMID:37280112 "MP31, a phosphatase and tensin homolog (PTEN) uORF-translated and mitochondria-localized micropeptide"]
  - recalls first paper: [PMID:37280112 "We reported that MP31 restricted lactate oxidation in GBM cells by interacting with mitochondrial LDHB."]
  - New: MP31 competes with V-ATPase A1 for LDHB binding -> lysosomal alkalinization, block of
    mitophagosome-lysosome fusion, MMP loss, ROS. These are downstream/indirect cellular
    phenotypes of overexpression in GBM cells and KO in normal human astrocytes; no direct
    mitophagy/lysosome activity of MP31 itself. Not proposed as GO terms.
- PMID:41090342 (2025 review of GBM micropeptides; abstract only) - background only.

### Mechanistic tension
- Abstract says MP31 "compet[es] with mLDH for NAD+", while UniProt/GOA record binding to
  LDHA/LDHB (IPI) and LDH inhibitor activity (IDA). The GO term GO:0160193 is defined as
  "Binds to and stops, prevents or reduces the activity of L-lactate dehydrogenase" - consistent
  with the LDH-binding mutants (S5A, Y12A). Exact mechanism (NAD+ binding vs. LDH binding) is
  not resolvable from the abstract; curator had full text. Accept MF.
- Direction: inhibits lactate -> pyruvate (lactate oxidation) in mitochondria; existence of an
  "mitochondrial LDH" is itself debated in the field (worth an expert question).

### Decisions
- protein binding x2 (LDHA, LDHB) -> MODIFY to GO:0160193 L-lactate dehydrogenase inhibitor activity.
- mitochondrion IDA/IEA -> ACCEPT (two independent papers state mitochondrial localization).
- negative regulation of oxidative phosphorylation (IMP) -> KEEP_AS_NON_CORE: OXPHOS increase is a
  downstream consequence of more pyruvate supply in mouse KO; the direct process is lactate
  oxidation. No GO term "negative regulation of lactate catabolic/oxidation process" found in QuickGO
  search, so no NEW.
- L-lactate dehydrogenase inhibitor activity (IDA) -> ACCEPT (core).
- No NEW terms: mitophagy/lysosome phenotypes are indirect.
- Evidence caveat: single laboratory; no independent replication; human peptide detected in brain;
  low/absent in GBM.
