# ITPR2 notes

## 2026-11-25 GO-CAM 671ae02600000964 review

`just fetch-gene human ITPR2 --force` populated UniProt Q14571, the 55-row
GOA TSV and the 54-row review stub after the child checkout was pointed at its
own `src/` via `PYTHONPATH=src`. `just fetch-gene-pmids human ITPR2` confirmed
that the seeded PMIDs were cached and added `PMID_8081734.md`; the other seeded
publication caches were already present.

Automated provider research was attempted with
`just deep-research-falcon human ITPR2 --fallback perplexity-lite`, but Falcon
was unavailable in this runtime and the Perplexity fallback was unavailable
because `agentapi` was not in `PATH`. No provider-authored deep-research file
was produced, so this review uses the GOA rows, UniProt record, cached
publications, cached Reactome entries, the ITPR1/ITPR3 sibling reviews and the
GO-CAM model as manually checked sources.

The PANTHER loss check reported `Q14571 is not a leaf of this tree; losses not
checked` for PTHR45816 and found no IRD or IKR loss on the ITPR2 lineage.

### Manual evidence synthesis

- Human ITPR2 encodes type 2 IP3 receptor; Yamamoto-Hino et al. cloned the
  human type 2 and type 3 receptors and reported that "Human type 2 and type 3
  IP3Rs are 2701 amino acids and 2671 amino acids long" with the expected
  C-terminal six-transmembrane architecture [PMID:8081734].
- Adkins et al. tested cells expressing predominantly each IP3 receptor subtype
  and showed that IP3-evoked calcium mobilization by type 2 receptors, like
  types 1 and 3, is calmodulin-sensitive [PMID:10620513, "Using cell types
  expressing predominantly type-1, -2 or -3 InsP(3) receptors, we show that
  InsP(3)-evoked Ca(2+) mobilization from each is similarly inhibited by
  calmodulin"].
- The UniProt Q14571 record summarizes the orthology-supported core activity as
  an "Inositol 1,4,5-trisphosphate-gated calcium channel" that transports
  calcium from the endoplasmic reticulum lumen to the cytoplasm and places the
  channel in the ER membrane [file:human/ITPR2/ITPR2-uniprot.txt].
- Reactome platelet dense-tubular-system events agree with the canonical
  mechanism: IP3 receptors mobilize calcium from ER-like internal stores into
  the cytoplasm [Reactome:R-HSA-139854, "mobilizes Ca2+ from internal stores in
  the ER to the cytoplasm"].
- Platelet fractionation found type II IP3 receptor in both human platelet
  plasma-membrane and internal-membrane fractions, supporting the existing
  plasma-membrane row as a non-core platelet location and supporting GO checking
  the BHF-UCL sarcoplasmic-reticulum membrane row for re-pointing to a separate
  platelet dense tubular network membrane assertion; the independently supported
  sarcoplasmic-reticulum membrane claim should be retained or re-sourced
  [PMID:10828023, "The type II receptor exhibited a dual distribution"].
- Garcia et al. found all three IP3R isoforms in neonatal and adult rat
  ventricular cardiomyocytes and in human heart tissue, supporting the propagated
  sarcoplasmic-reticulum rows as true but secondary muscle-store locations
  [PMID:28923351, "The three IP3R proteins are expressed throughout the
  cardiomyocyte sarcoplasmic reticulum"].
- BANK1 scaffold binding is a peripheral B-cell regulatory interaction
  [PMID:11782428, "associate with the distinct regions of BANK"]. The Tespa1
  paper detected all three IP3R family members in a Jurkat pull-down but
  followed the functional mechanism through IP3R1, so it supports removing the
  bare GO:0005515 row rather than keeping a generic protein-binding annotation
  [PMID:28598420, "we detect all members of the IP3R family of proteins"].
- Three rows could not be verified from the cached text: the hypoxia row rests
  on transcript changes [PMID:19120137, "gene expression of all IP3Rs
  decreased"], the SERCA2b/3 platelet abstract names hTRPC1 but not ITPR2
  [PMID:18068335, "SERCA2b and 3 with the hTRPC1 channel"], and the PX-FERM
  paper describes a broad cargo-binding screen without enough extracted
  supplemental detail to confirm the ITPR2 signaling-receptor-complex row
  [PMID:23382219, "promiscuous ability to bind a wide array of putative cargo
  molecules"].

### GO-CAM consistency notes

Do not edit `gocams/671ae02600000964/` in the gene PR. Reconcile these
observations in the final GO-CAM consistency-notes PR after this ITPR2 review
merges:

- The model and the pre-existing GOA rows use the broad process `GO:0051209`
  release of sequestered calcium ion into cytosol. The gene review modifies this
  to the ER-specific child `GO:1903514` release of sequestered calcium ion into
  cytosol by endoplasmic reticulum. This defect is already recorded in
  `gocams/671ae02600000964/671ae02600000964-review.yaml`.
- The model output calcium participant uses `GO:0005737` cytoplasm; cytosol
  (`GO:0005829`) is the more precise compartment for calcium after ITPR2 channel
  opening. This defect is already recorded in the GO-CAM review.
- The model's IP3 activator edge uses `ECO:0000314` with/from `UniProtKB:Q14573`;
  the cached gene-level and GO-CAM review did not include enough evidence to
  confirm that ITPR3 with/from value for an ITPR2 activity. This query is already
  recorded in the GO-CAM review.
- The GO-CAM review's `consistency: NO_GENE_REVIEW` judgement and the
  `modules/er_calcium_store_cycling.yaml` note saying no local ITPR2 review
  exists become stale once this PR merges.
