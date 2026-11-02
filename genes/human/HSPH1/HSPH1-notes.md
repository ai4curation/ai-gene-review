# HSPH1 (Q92598) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: HSPH1 is the closest experimentally characterised relative of the ProtNLM2 benchmark
gene human HSPA4 (P34932). This review is written for HSPH1 in its own right and does not use
any ProtNLM2 output.

### Deep research

`just deep-research-falcon human HSPH1 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient
quota). No deep-research file exists. The review is based on the UniProt record, the cached
GOA references, the PAINT slice for PTHR45639, and primary papers fetched into
`publications/` with `just fetch-pmid` (abstracts and, where available, full text).

### Evolutionary placement

- PANTHER: HSPH1 is in PTHR45639:SF2 "HEAT SHOCK PROTEIN 105 KDA", together with the
  mouse (Q61699), rat (Q66HA8), hamster (Q60446), bovine and orangutan HSPH1 orthologs
  (`interpro/panther/PTHR45639/PTHR45639-entries.csv`). HSPA4 (Apg-2, also called HSPH2) is in
  SF6, and HSPA4L (Apg-1, HSPH3, O95757) is a further Hsp110 paralog. The mouse ortholog Q61699
  is therefore a valid 1:1 SF2 ortholog for transfers (e.g. the GO_REF:0000107 rows).
- PAINT (`PTHR45639-paint.tsv`):
  - PTN002900795: GO:0000774 adenyl-nucleotide exchange factor activity; seeds CGD
    CAL0000182153, SGD S000000373, S000001556, S000006027 and UniProtKB:Q92598 (HSPH1
    itself, from the Rauch & Gestwicki IDA).
  - PTN000452854 (eukaryotic Hsp110 node, taxon:2759): GO:0005829 cytosol (seeds include
    Q92598, P34932, O95757, Arabidopsis), GO:0005634 nucleus (seeds include Q92598, MGI:105053
    = mouse Hsph1), GO:0006457 protein folding (seeds yeast, Candida, mouse Hsph1, worm).
  - The family node PTN000452648 carries GO:0016887 ATP hydrolysis activity and GO:0044183
    protein folding chaperone, but HSPH1 does not receive IBAs for them. The PAINT curator
    therefore did not assign ATP hydrolysis or Hsp70-type chaperone activity to the Hsp110
    branch; I treat this as a deliberate decision, consistent with the biochemistry below.

### Experimentally established in human HSPH1

- Nucleotide exchange on Hsp70: Rauch & Gestwicki measured binding of human HSPA1A to
  BAG1/2/3 and "the unrelated NEF Hsp105", and showed that affinity "predicted their potency
  in nucleotide and peptide release assays" [PMID:24318877]. Dragovic et al. showed NEF
  activity of human Hsp110 (HspH1) on Hsp70: "we found NEF activity on Hsp70 for human Hsp110"
  and the MABA-ADP dissociation rate "was increased ~5-fold in the presence of human Hsp110"
  [PMID:16688212]. In the same paper, human Hsp70 + Hsp110 (HspH1) were used in luciferase
  refolding assays (Fig. 1D).
- Physical binding to HSPA1A/HSPA1B via the Hsp70 NBD [PMID:24318877; UniProt SUBUNIT].
- Localization: immunofluorescence showed "hsp105 was present in the cytoplasm but was not
  found in the nucleoli of mammalian cells under both nonstressed and stressed conditions"
  [PMID:9931472]. HPA immunofluorescence (GO_REF:0000052) gives cytosol and nucleoplasm.
- Stress induction: "The transcript of pBH105-1 was induced by various stresses in HeLa
  cells" while the beta isoform (lacking 44 aa) is induced only by 42 °C heat shock
  [PMID:9931472].
- Disaggregation in mammalian cytosol: Mattoo/Shorter immunodepleted the two Hsp110s from
  cytosol: "Hsp105-depleted cytosol had slightly reduced luciferase and GFP disaggregase
  activity, whereas Apg-2-depleted cytosol had greatly reduced disaggregase activity"
  [PMID:22022600]. So in that system HSPA4 (Apg-2) is the dominant Hsp110 and HSPH1 contributes
  modestly. The metazoan Hsp70–J-protein–Hsp110 disaggregase studied by Nillegoda et al. used
  HSPH2 (= HSPA4), not HSPH1 [PMID:26245380]. Rampelt et al. state that human Hsp110 drives
  disaggregation through nucleotide exchange, "not on ATPase activity" [PMID:22990239]; only
  the abstract is cached, so I do not assert which human paralog(s) were tested there.
- Disease/cancer: HSP110ΔE9, an exon-9-skipped mutant lacking the substrate-binding domain,
  arises in MSI colorectal cancer and acts as a dominant negative of HSP110 chaperone and
  antiapoptotic function [PMID:21946539].

### Mammalian but not clearly human-species evidence

- Hamster Hsp110: holds heat-denatured proteins soluble and folding-competent, more
  efficiently than Hsc70, and overexpression confers thermoresistance (including HeLa cells)
  [PMID:9395504].
- Hatayama group Hsp105alpha (species of the protein not stated in the abstracts; the lab
  cloned mouse hsp105): Hsp105alpha/beta prevent thermal aggregation of luciferase, "did not
  show ATPase activity" alone, suppress Hsc70/Hsp40-mediated refolding [PMID:10860841], and
  suppress Hsc70 ATPase in an interaction-dependent way [PMID:15292236]. Mouse Hsp105alpha
  binds alpha-tubulin and colocalizes with microtubules [PMID:12749852]; this is the source of
  the GO_REF:0000107 microtubule/alpha-tubulin rows on human HSPH1.

### Interpretation

Core function: HSPH1 is a cytosolic Hsp110-family nucleotide-exchange factor for Hsp70s
(HSPA1A/B, HSPA8). It binds the Hsp70 NBD and accelerates ADP release, so it sets the timing of
client release in the Hsp70/J-protein cycle, which is how it contributes to protein folding,
refolding and aggregate dissolution. It also has an Hsp70-like substrate-binding domain and can
act as a holdase that keeps denatured proteins soluble (mammalian ortholog data), but GO has no
current holdase MF term. Intrinsic ATP hydrolysis is weak or absent (not detected by
Yamagishi et al.; disaggregation depends on nucleotide exchange, not ATPase) and is not
inherited from the PAINT family node, so ATP hydrolysis activity is over-annotation. ATP
binding is part of the Hsp110 mechanism (ATP-bound Hsp110 forms the NEF complex), but that was
shown for yeast Sse1 [PMID:18550409], not human HSPH1.

Immune and extracellular annotations (CD1d upregulation, NK T cell activation, SCARF1
endocytosis) come from a commentary and Reactome descriptions of exogenous recombinant protein
effects. The NK T cell part is explicitly speculative in the commentary [PMID:12952910].

For transfer to HSPA4: the NEF activity and the Hsp110-node localizations/protein folding are
placed at ancestral nodes that include both HSPH1 and HSPA4 (both are seeds of PTN000452854
cytosol). HSPH1-specific findings that are not node-level (alpha-tubulin binding, HSP110ΔE9 in
colorectal cancer, CD1d effects) should not be transferred.
