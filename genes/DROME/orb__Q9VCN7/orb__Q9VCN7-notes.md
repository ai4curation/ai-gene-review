# orb / Q9VCN7 (canonical gene-centric Orb product, isoforms A/G, 915 aa)

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Identity and folder
- Q9VCN7 is UniProt's gene-centric canonical product of orb (FBgn0004882). It is an unreviewed
  TrEMBL entry; fly orb has no Swiss-Prot entry. The folder `genes/DROME/orb/` is keyed to the
  559-aa isoform C/E product Q8IMZ2, so this product gets `orb__Q9VCN7`, following the
  `CycA__P14785` precedent. It was fetched with `just fetch-gene DROME Q9VCN7 --alias orb__Q9VCN7`.
- Q8IMZ2 is identical to Q9VCN7 residues 364-915
  ([RESULTS.md](../orb/orb-bioinformatics/RESULTS.md)). All RRMs and the ZZ domain lie in that
  shared region. The extra ~356 N-terminal residues of Q9VCN7 are mostly disordered or
  low-complexity (MobiDB-lite regions 1-27, 40-59, 308-355).

### Evolutionary grounding
- PANTHER: Q9VCN7 is in PTHR12566:SF9 (CPEB1 subfamily), according to both the UniProt
  cross-reference and the PANTHER 19.0 fly classification. SF9 also contains human CPEB1 (Q9BZB8),
  mouse Cpeb1 (P70166, MGI:108442), rat Cpeb1 (P0C279, RGD:1310421) and worm cpb-3. The other
  subfamilies are Orb2 (SF12), CPEB2 (SF8; mouse MGI:2442640), CPEB3 (SF7; MGI:2443075, Q8NE35,
  RGD:1564670), CPEB4 (SF2; MGI:1914829, Q17RY0, RGD:1311931) and fog-1 (SF6).
- PMID:27791065 states: "Drosophila Orb and Orb2 are single members of the CPEB1 and CPEB2
  subfamilies of the CPEB proteins, respectively."
- All IBAs come from the family root node PTN000286163. I split them by whether an SF9 donor
  exists:
  - An SF9 donor exists for mRNA 3'-UTR binding, translation repressor activity GO:0000900,
    negative regulation of cytoplasmic translation, nucleus, cytoplasm, neuron projection (rat
    Cpeb1) and synapse (mouse and rat Cpeb1).
  - No SF9 donor exists for translation factor activity, RNA binding GO:0008135 (CPEB3 only) or
    ribosome binding GO:0043022 (Cpeb2 only). I marked both as over-annotated, as transfers of
    subfamily-specific terms across subfamilies.
  - Neuron projection and synapse have SF9 donors, but Orb is germline-restricted
    [PMID:21900268 "orb ... has no known somatic functions or expression outside of the germline"].
    The fly neuronal CPEB is Orb2. I marked both as over-annotated (CONTEXT_OR_TISSUE_MISMATCH).
  - Repressor activity and negative regulation of translation are kept as non-core. They are
    inferred from vertebrate CPEB1 and are not shown in flies. In the fly orb autoregulatory loop,
    the repressor is dFMR1 [PMID:15737929].

### What is experimentally established in Drosophila (for transfer use)
- mRNA 3'-UTR binding: osk 3'UTR UV cross-linking [PMID:10525352], CLIP of CPE-like 3'UTR sites
  through the RRMs [PMID:27791065], and RIP enrichment of aPKC and orb 3'UTRs [PMID:30865627].
- Cytosolic mRNA polyadenylation and positive regulation of oskar translation [PMID:12538512;
  PMID:10525352]. Orb associates physically with PAP and Wispy [PMID:18434412].
- Locations: cytoplasm (16-cell cyst, then the oocyte) [PMID:11809824], sponge bodies / P-body
  edge [PMID:19301391; PMID:23178881], nuage [PMID:25862242], oocyte subcortex [PMID:30865627],
  and an mRNP complex with Rin [PMID:24069162].
- Developmental requirements, kept non-core: 16-cell cyst formation and oocyte differentiation,
  D/V (gurken) and A/P (oskar) patterning, and oocyte repolarization. oskar mRNA localization
  appears to be indirect, through cytoskeleton and Par proteins [PMID:30865627].

### Actions summary
- MODIFY: nucleic acid binding, RNA binding and the three mRNA binding rows go to mRNA 3'-UTR
  binding. Regulation of translation goes to positive regulation of translation.
- REMOVE: the 2 bare protein binding IPIs (policy).
- MARK_AS_OVER_ANNOTATED: GO:0008135, GO:0043022, GO:0043005, GO:0045202 (IBA, each with a
  propagation_review), and translation GO:0006412 (IEA derived from GO:0008135).
- No NEW terms were added.

### Deep research
- `just deep-research-falcon DROME orb__Q9VCN7 --alias orb --fallback perplexity-lite` failed.
  Falcon reported "Failed to authenticate" and the perplexity fallback returned 401 insufficient
  quota. No deep-research file was written for this folder. Note that the wrapper resolved its
  output path to `genes/DROME/orb/orb-deep-research-falcon.md`. Because it failed, nothing was
  overwritten (verified with git status).
- The review relies on primary literature read from `publications/`. Full text was checked for
  PMID:11809824, 19301391, 23178881, 24069162, 25862242, 30865627 and 34531401. The other sources
  were abstracts only.
- No ProtNLM2 files or prediction-evidence were opened.
