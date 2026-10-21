# NARF (Q9UHQ1, NARF_HUMAN) review notes

Folder note: `genes/human/NARF/` holds the review of J3KS48, a 217-residue alternative
gene-model product of the same gene (ProtNLM2 benchmark target). This folder
(`NARF__Q9UHQ1`) holds the review of the canonical 456-residue Swiss-Prot entry Q9UHQ1,
following the `<HOST>__<ACC>` convention for a second UniProt accession under the same symbol.

## Deep research

- 2026-10-20: `just deep-research-falcon human NARF__Q9UHQ1 --fallback perplexity-lite` failed.
  Falcon: "Exception: Failed to authenticate" (Edison client). Fallback perplexity-lite:
  HTTP 401 insufficient_quota. No deep-research file was produced. The review was written from
  the cached primary literature (PMID:10514485, PMID:36490339, PMID:18270200, PMID:41655866,
  PMID:31823109), the UniProt record, PANTHER 19 and QuickGO, plus a PubMed title/abstract search
  for "nuclear prelamin A recognition factor" OR IOP2.

## Evolutionary placement

- PANTHER 19 places Q9UHQ1 in PTHR11615:SF124 (NUCLEAR PRELAMIN A RECOGNITION FACTOR), queried
  via the PANTHER geneinfo API. The paralog NARFL/IOP1/CIAO3 (Q9H6Q4) is in a different
  subfamily (SF322).
- PAINT node PTN002614243 (QuickGO withFrom query, 2026-10-20) carries exactly two terms,
  lamin binding (GO:0005521, enables) and lamin filament (GO:0005638, is_active_in), and
  propagates them to vertebrate NARF orthologs: mouse Q9CYQ7, rat Q2YDU6, zebrafish Q6DHP6,
  Xenopus Q6GP25 and others in mammals, birds, fish. The donor is human Q9UHQ1 itself. No
  cytosolic Fe-S assembly term (the NARFL/Nar1 function) is propagated to this node, which is a
  deliberate PAINT decision consistent with the knockdown data below.
- No NARF ortholog in another model organism has been characterized experimentally, so every
  experimental claim below is human-specific (and cell-line based).

## Experimental findings (human)

- Prelamin A binding: isolated by yeast two-hybrid with the prelamin A tail
  [PMID:10514485 "Using the yeast two-hybrid assay, we isolated a novel human protein, Narf, that binds the carboxyl-terminal tail of prelamin A."].
  Binding depends on farnesylation
  [PMID:10514485 "Inhibition of farnesyltransferase and mutation or deletion of the CaaX motif from the prelamin A tail domain inhibits Narf binding in yeast two-hybrid and in vitro binding assays."].
- Localization: nuclear fractions, salt-extractable from nuclear envelopes, exclusively nuclear
  and partly at the lamina
  [PMID:10514485 "When a FLAG epitope-tagged Narf is expressed in HeLa cells, it is exclusively nuclear and partially co-localizes with the nuclear lamina."].
  HPA immunofluorescence (GO_REF:0000052) adds nucleoplasm and nucleolus.
- The hydrogenase similarity is limited
  [PMID:10514485 "Narf has limited homology to iron-only bacterial hydrogenases and eukaryotic proteins of unknown function."].
  No hydrogenase activity or Fe-S cluster has been reported for NARF.
- Paralog boundary: IOP2/NARF knockdown does not affect cytosolic or mitochondrial aconitase,
  unlike IOP1/NARFL [PMID:18270200 "Knockdown of IOP2, in contrast, had no effect on either."].
- Transcription coactivator (breast cancer cells, hypoxia): HIF-1 target gene; NARF binds OCT4
  (endogenous co-IP), is recruited by OCT4 to NANOG/SOX2/KLF4 sites (ChIP), and recruits KDM6A
  to remove H3K27me3 [PMID:36490339 "NARF functions as an essential coactivator by recruiting the histone demethylase KDM6A to OCT4 bound to genes encoding the pluripotency factors NANOG, KLF4, and SOX2"].
- Transcription coactivator (hepatocellular carcinoma cells): a second, independent lab reports
  NARF recruits EP300 to LEF1-binding sites
  [PMID:41655866 "Mechanistically, NARF recruited acetyltransferase EP300 to enhance H3K27 acetylation at lymphoid enhancer binding factor 1 (LEF1)-binding sites, thereby amplifying LEF1-dependent transcriptional activity."].
  Abstract only.
- Mitochondrial association claimed in an MS proteomics/histology study
  [PMID:31823109 "NARF is a protein associated with the mitochondria which has also been linked to mitochondrial defects in multiple sclerosis."].
  Not a localization assay of the protein, abstract only; not used for annotation.

## Decisions

- Lamin binding (IBA + IPI): ACCEPT, core.
- Lamin filament (IBA + IDA), nuclear lamina (TAS): ACCEPT (partial lamina association).
- Nucleus (IEA), nucleoplasm (HPA IDA): ACCEPT. Nucleolus (HPA only): KEEP_AS_NON_CORE.
- Nuclear lumen (IDA): MODIFY to nucleoplasm and lamin filament, which the gene already carries.
- NEW: transcription coactivator activity (GO:0003713) and positive regulation of transcription
  by RNA polymerase II (GO:0045944). Participation test: NARF does the coactivator work itself
  (bridges DNA-bound OCT4/LEF1 to KDM6A/EP300); two independent labs. Both are cancer-cell-line
  studies, so these are flagged as human-only, not transferable by PAINT yet.
- Not added: response to hypoxia (NARF is a HIF-1 target; that is regulation of NARF, not
  NARF participation), stem cell maintenance / EMT / metastasis (phenotypes), any Fe-S assembly
  or hydrogenase term (paralog-specific, explicitly not propagated, tested negative for aconitase).
