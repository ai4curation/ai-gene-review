# ttc39c (Danio rerio, Q1LXE6) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted for this review.

### Deep research status

`just deep-research-falcon DANRE ttc39c --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" (HTTP 403) and the
perplexity-lite fallback also failed. No deep-research file exists; the review is
based on the literature read directly (PubMed search for "ttc39c OR TTC39C",
17 hits, 2026-10-21) and on the UniProt and PANTHER/PAINT data.

### Gene and family

- 579 aa, Swiss-Prot reviewed but PE 2 (transcript level). Three TPR repeats
  (311-344, 349-382, 481-514) inside a Pfam PF10300 Iml2-TPR_39 domain; a short
  disordered polar region at 182-202. Isoform 2 is truncated after residue 275.
- PANTHER PTHR31859 (TTC39 family), subfamily SF1 (TTC39C). Human TTC39C (Q8N584)
  is also SF1. TTC39A (SF3/SF7) and TTC39B (SF4) are separate subfamilies.
- PAINT (`interpro/panther/PTHR31859/PTHR31859-paint.tsv`): zebrafish ttc39c
  (ZFIN:ZDB-GENE-050522-194) is the only seed of two IBD nodes:
  - PTN001275223, GO:0060271 cilium assembly, taxon 6072 (Eumetazoa);
  - PTN002840059, GO:0032474 otolith morphogenesis, taxon 117571 (Euteleostomi).
  The other node in the family, PTN001275282 (taxon 40674, Mammalia, seeded by
  mouse Ttc39b, MGI:1917113), carries the lipid/cholesterol homeostasis terms. A
  QuickGO check (2026-10-21) shows human TTC39B gets those, human TTC39C gets only
  the two ttc39c-seeded IBAs, and human TTC39A gets neither. So the cilium node lies
  on the TTC39C branch and does not cover the TTC39A/B paralogs.
- PAINT did NOT propagate the third ttc39c IMP term, GO:0061371 determination of
  heart left/right asymmetry. I read that as a deliberate decision: laterality is
  an organism-level consequence of node (Kupffer's vesicle) cilia, not something
  ttc39c does.

### Experimental evidence in zebrafish: Xu et al. 2015 (PMID:25860617, full text)

- Morpholino screen of ten TTC genes. ttc39c MO: more than 84% curved bodies,
  rescued by MO-resistant ttc39c mRNA (the rescue was scored for body curvature).
  [PMID:25860617 "the body curvature phenotypes of the morphants were rescued upon coinjection of the corresponding MO-resistant mRNA of zebrafish ttc4, -9c, -36, or -39c, but not of the mRNA of EGFP"]
- The ttc39a morphant (paralog, different subfamily) was below the 17% abnormality
  threshold. That is a useful internal contrast with ttc39c.
- Otoliths abnormal in more than 75% of morphants; heart tube misoriented in more than 64% of
  ttc39c morphants.
- Kupffer's vesicle cilia were reduced in number and length; pronephric cilia were
  disorganized at 24 hpf and largely paralyzed at 60 hpf (CBF 5.6 Hz vs 42.2 Hz in controls).
  [PMID:25860617 "both the number and length of the KV cilia were significantly reduced in the ttc morphants"]
  [PMID:25860617 "5.6 ± 1.8 Hz for ttc39c morphants"]
- The authors speculate a role in axonemal dynein arm assembly/activity; this is not tested.
- Mouse TTC39C (FLAG, in HEK293T plus testis lysate): weak co-IP with IFT144 and
  IFT139 (IFT-A). The antibody failed in immunostaining, so localization is unknown.
  [PMID:25860617 "TTC39c showed weak association with IFT144 and IFT139, two subunits of IFT-A"]
  [PMID:25860617 "As to TTC39c, we were not sure of its subcellular localization because the antibody did not work for immunostaining."]
- All of the zebrafish evidence is morpholino knockdown. No stable mutant has been reported.

### Mammalian evidence (not zebrafish)

- Hayes et al. 2019 (PMID:31188487, abstract only): mouse Ttc39c is upregulated in
  neurogenic muscle atrophy. Overexpressed GFP fusion is cytoplasmic in muscle cells.
  Both overexpression and knockdown impair myoblast differentiation and Hedgehog/ERK
  signaling, and overexpression raises IFT144/IFT43 levels. This is consistent with
  a cilium/IFT-A link but is cell-culture perturbation data in another species.
- Rong et al. 2022 (PMID:36303158): lung cancer expression and prognosis study.
  Not informative on molecular function.
- No molecular function (activity) has been established for any TTC39C.

### Decisions

- Cilium assembly (IMP and IBA): ACCEPT. This is the most proximal process the data
  support (fewer and shorter KV cilia), though knockdown alone does not show which
  step ttc39c performs.
- Otolith morphogenesis (IMP and IBA): KEEP_AS_NON_CORE. It is a downstream
  consequence of inner-ear cilia defects. The PAINT curator did propagate it, but at
  the Euteleostomi node only.
- Heart L/R asymmetry (IMP): KEEP_AS_NON_CORE. This is an organismal laterality
  phenotype and must not be transferred (PAINT deliberately declined to).
- ND cellular_component: ACCEPT. No localization data exist for zebrafish ttc39c,
  and the only mammalian attempt failed.
- No NEW terms. Cilium movement and IFT-A binding were considered and rejected:
  the motility defect may be secondary, and the co-IP is weak and heterologous.
