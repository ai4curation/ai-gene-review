# EIP9 (SDJ1, DNAJ1, At5g64360; UniProt Q9FMF3) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output or prediction-evidence files were consulted for this review.

### Setup
- `just fetch-gene ARATH EIP9` first resolved the symbol to the wrong TrEMBL entry, B9DFS0
  (a 464-aa At5g64360 cDNA entry with no GOA rows). I re-ran it with `--uniprot-id Q9FMF3 --force`
  and corrected the stub id to Q9FMF3. This gave 13 GOA rows.
- Deep research (falcon) failed with "Failed to authenticate". The perplexity-lite fallback
  failed with HTTP 401 (insufficient quota). No deep-research file exists, so the review relies
  on the cached literature below.

### Identity and nomenclature
- At5g64360 = SDJ1 [PMID:33445404 "The protein encoded by At5g64360 was already named as SDJ1."]
  = DNAJ1 of Harris et al. 2018 (TAIR attributes the PMID:30523112 IDA/IPI rows to this locus).
- UniProt names SDJ2 = At2g01710 (PTHR45496:SF1) and SDJ3 = At1g62970 (SF10). The IGI row from
  PMID:34185870 lists At1g62970 and At5g09540 (SF28) as partners. The SDJ2 assignment may
  therefore differ between papers, and I do not resolve it here.

### Evolutionary grounding
- PANTHER PTHR45496:SF19. Arabidopsis members of PTHR45496 (UniProt REST query) are SF19
  (At5g64360 only), SF1 (At2g01710), SF10 (At1g62970), SF28 (At5g09540) and SF32 (ADMETOS
  At4g11940, At4g38065, At4g11930).
- PAINT node PTN002896004 (taxon:3398, Magnoliopsida) carries IBDs for GO:0005634 (seeds
  At1g62970, At4g11940, At5g64360) and GO:0001228 (seeds At1g62970, At2g01710, At5g64360)
  (interpro/panther/PTHR45496/PTHR45496-paint.tsv). The Magnoliopsida origin agrees with
  [PMID:40331371 "we discovered that DNAJ1/2/3 originated within Magnoliopsida"].
- J-domain check (EIP9-bioinformatics/RESULTS.md): the SDJ1 J domain (79-144) lacks the HPD motif.
  The loop reads NPS. SDJ3 also lacks HPD, while SDJ2 keeps it. So canonical Hsp70 co-chaperone
  activity should not be inferred for SDJ1 from the J domain alone, and Jia et al. describe the
  WUS-SDJ complex as "independent of HSP70 proteins" [PMID:33445404].

### Experimentally established in Arabidopsis
- Complex with SUVH1/SUVH3, which recruit SDJ1 to methylated DNA [PMID:30523112 "Thus, SUVH1 and SUVH3 are required to recruit DNAJ1 and DNAJ2 to methylated DNA."]
- No methyl-binding domain of its own [PMID:30523112 "DNAJ1 and DNAJ2 lack any discernible methyl-binding domain"]
- Tethered SDJ1 activates transcription in plants, yeast and mammalian cells, but only of genes
  that are already expressed. It is a coactivator, not a DNA-binding TF [PMID:30523112].
- Required for expression of genes near RdDM sites, including ROS1 [PMID:30523112].
- Binds WUS and enhances WUS promoter activity, but does not bind promoter DNA alone [PMID:33445404].
- Nuclear [PMID:33445404; PMID:21700722].
- eip9 mutants flower early and overexpressors flower late [PMID:21700722, abstract only].
- sdj1/2/3 triple mutants show hypomethylation at a subset of RdDM loci, and SDJ1 binds RDM1/DMS3
  [PMID:34185870, abstract only]. This contrasts with no methylation change in dnaj1 dnaj2 [PMID:30523112].

### Decisions
- GO:0001228 (IBA + IDA): MODIFY to GO:0003713 transcription coactivator activity, because SDJ1
  has no DNA binding of its own.
- GO:0045944: ACCEPT. GO:0005634: ACCEPT. GO:0005737 (IDA, ISM): KEEP_AS_NON_CORE.
- GO:0009909 (IMP): KEEP_AS_NON_CORE, as a whole-plant phenotype.
- GO:0080188 (IGI): KEEP_AS_NON_CORE, contributory and disputed.
- GO:0005515 x4: REMOVE under the protein-binding policy. The interactions themselves are real.
- No NEW terms proposed.

### Notes for transfer to orthologs (e.g. ABRPR A0A8B8L1Z3, same SF19)
- Transferable with experimental grounding: transcription coactivator activity, nucleus, and
  positive regulation of Pol II transcription (shared at PTN002896004 across SDJ paralogs).
- Not to transfer: flowering-time regulation (a species phenotype); the RdDM methylation role
  (disputed, triple-mutant only); the WUS interaction (a specific partner).
- Do not transfer Hsp70 co-chaperone activity, since HPD is absent.
