# Ranbp21 (Q9VWE7, CG12234, FBgn0031051; dmExp5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Setup and provenance

- `just fetch-gene DROME Ranbp21` produced the UniProt record (TrEMBL, unreviewed, 1241 aa) and
  9 GOA rows, all phylogenetic (IBA) or electronic (IEA). There are no experimental GO
  annotations for this gene in GOA.
- Deep research: `just deep-research-falcon DROME Ranbp21 --fallback perplexity-lite` failed.
  Falcon returned `HTTPStatusError: Client error '403 Forbidden'` at the Edison auth endpoint,
  and the perplexity-lite fallback also failed, so no deep-research file exists. This review is
  built from primary literature I located with PubMed esearch and cached with
  `ai-gene-review fetch-pmid`:
  - PMID:16963774 Shibata et al. 2006, NAR (full text). The primary biochemical and RNAi study of
    dmExp5.
  - PMID:39098529 Li et al. 2024, JBC (full text). Exp5 PAR-CLIP in S2R+ cells.
  - PMID:17599402 Okamura et al. 2007, Cell (full text). Mirtron biogenesis; Exp5 RNAi in S2 cells.
  - PMID:12426392 Bohnsack et al. 2002, EMBO J (abstract only). Mammalian/Xenopus Exp5 exports
    eEF1A via aminoacylated tRNA. Background only.
  - PMID:14730017 Bohnsack et al. 2004, RNA. Xenopus Exp5 is the RanGTP-dependent pre-miRNA
    exporter. Background only.
- ProtNLM2 files and prediction-evidence folders were not opened.

### Evolutionary placement

- UniProt: PANTHER PTHR11223:SF3 (EXPORTIN-5), InterPro IPR045478 Exportin-5_C, Pfam PF19273
  (Exportin-5), plus IBN_N (importin-beta N-terminal, Ran-binding) and Xpo1 domains
  [file:DROME/Ranbp21/Ranbp21-uniprot.txt "DR   PANTHER; PTHR11223:SF3; EXPORTIN-5; 1."].
- PAINT (interpro/panther/PTHR11223/PTHR11223-paint.tsv):
  - PTN000131749 (XPO1 + XPO5 ancestor): nuclear export signal receptor activity (GO:0005049),
    nucleus, cytoplasm.
  - PTN000131750 (exportin-5 clade): RNA binding (GO:0003723), RNA export from nucleus
    (GO:0006405).
  - Not propagated at either node: protein export from nucleus, pre-miRNA export
    (GO:0035281), tRNA export (GO:0006409). Read as a deliberate decision. The protein-export
    omission fits the family review's caution that XPO1 cargo biology should not be inherited
    by exportin-5. The omission of the specific RNA-export terms reflects real cargo divergence
    across the clade (plant HASTY, yeast Msn5, human XPO5 have different cargo preferences;
    PMID:16963774). Specific RNA terms in this review therefore rest on Drosophila experiments,
    not on transfer.

### Experimental findings in Drosophila (direct, this gene)

1. **pre-miRNA binding, RanGTP-dependent (in vitro, recombinant protein, EMSA).**
   [PMID:16963774 "We observed that hsExp5 and dmExp5 efficiently bound pre-miR-30"]
   [PMID:16963774 "The binding of the Exp5 orthologues to pre-miRNA was specific, since it was Ran-dependent"]
   The probe was human pre-miR-30, with fly RanQ69L-GTP added.
2. **tRNA binding, RanGTP-dependent, stronger than human XPO5.**
   [PMID:16963774 "The bacterially expressed recombinant dmExp5 immunoprecipitated tRNAs only in the presence of dmRanQ69L-GTP"]
   [PMID:16963774 "From these results, we conclude that dmExp5 preferentially binds to tRNA compared with hsExp5."]
3. **dsRNA binding**: a 22 bp dsRNA with a 2-nt 3' overhang competed with pre-miR-30 for all
   Exp5 orthologues; dsDNA did not compete.
4. **RNAi in S2 cells lowers mature tRNA-Met, tRNA-Ser and miR-2**, but not U6 or U1 snRNA.
   The authors take this as an *indirect* readout of export
   [PMID:16963774 "which we took for an indirect indication for their export defect"].
   Knocking down Drosha or DGCR8 lowered miRNA without lowering tRNA, which argues against the tRNA
   effect being secondary to miRNA loss. Human XPO5 partially rescued miR-2 but rescued tRNA-Ser
   poorly.
5. Drosophila has no exportin-t ortholog
   [PMID:16963774 "it was predicted that no Exp-t orthologous gene exists in several arthropods including Drosophila melanogaster (dm)"],
   so dmExp5 is the main candidate tRNA exporter.
6. **Mirtron hairpins depend on Exp5** (RNAi, S2 cells)
   [PMID:17599402 "We observed 60%–80% reduction in mirtron hairpins and mature products for endogenous mir-1003 and mir-1008 in cells treated with either Exportin-5 dsRNA"];
   canonical miR-2b fell only modestly (about 50%).
7. **PAR-CLIP (overexpressed FLAG-HA-Exp5, S2R+ cells)** recovered miRNAs, tRNAs, 7SL RNA, many
   mRNAs/lncRNAs (enriched for intronless mRNAs) and pre-tRNAs that still carry 5' leaders and 3'
   trailers [PMID:39098529]. The mRNA and lncRNA binding comes from overexpression in a cell line,
   and the authors say so; there is no functional export assay for those RNAs. I do not
   annotate mRNA export.

What is NOT experimentally established in flies: direct nuclear-export assays (e.g. FISH or
fractionation of cargo after Exp5 loss); subcellular localisation of the endogenous protein;
any protein cargo; in vivo (organismal) mutant phenotypes. Okamura et al. note that animal
mutants had not been described.

### Decisions

- GO:0003723 RNA binding (IBA): MODIFY to tRNA binding plus pre-miRNA binding (fly IDA data).
- GO:0005049 nuclear export signal receptor activity (IBA, IEA): ACCEPT. The definition covers RNA
  cargo. It is the best available MF for an RNA exportin; Ran-dependent cargo binding supports it.
- GO:0005634 nucleus, GO:0005737 cytoplasm (IBA): ACCEPT, as the two compartments an exportin
  shuttles between. Neither is experimentally shown for the fly protein.
- GO:0006405 RNA export from nucleus (IBA): MODIFY to tRNA export from nucleus and pre-miRNA
  export from nucleus.
- GO:0006611 protein export from nucleus (IEA; ARBA + XPO1/5 InterPro): MARK_AS_OVER_ANNOTATED.
  It comes from XPO1-dominated family-level mapping; PAINT declined it; there is no fly protein
  cargo. Mammalian Exp5 exports eEF1A only via tRNA bridging.
- GO:0006886 intracellular protein transport (IEA, IBN_N domain): MARK_AS_OVER_ANNOTATED, same
  reasoning.
- GO:0031267 small GTPase binding (IEA): ACCEPT. Cargo binding by dmExp5 requires RanGTP. The
  specific Ran-binding term (GO:0008536) is obsolete, so this is the most precise term.
- NEW: tRNA binding (IDA), pre-miRNA binding (IDA), tRNA export from nucleus (IMP), pre-miRNA
  export from nucleus (IMP), all PMID:16963774; PMID:17599402 adds support for pre-miRNA (mirtron) export.

Participation check for the process NEWs: an exportin is the entity that does the work of moving
cargo through the pore, so assigning the export process to Exp5 is participation, not the
substrate case. The evidence is indirect (mature RNA levels), so the process rows are IMP and the
caveat is stated in each reason.

### Note for transfer to Drosophila orthologs

The experimentally established functions (tRNA and pre-miRNA binding, Ran-dependent, and roles in
tRNA and pre-miRNA levels by RNAi) are specific to D. melanogaster Exp5 in PTHR11223:SF3. Within
the Drosophila genus the gene is 1:1 (exportin-t is absent from Drosophila), so the tRNA-export role
is the one most specific to this lineage. Human XPO5 does not share it to the same degree
(PMID:16963774).
