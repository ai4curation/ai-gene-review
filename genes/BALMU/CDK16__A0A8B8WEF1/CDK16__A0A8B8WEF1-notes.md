# CDK16 (Balaenoptera musculus, A0A8B8WEF1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: the first full review of whale CDK16. It is the closest characterised relative of the ProtNLM2 benchmark entry A0A8B8WEG2, which has the same GeneID 118888515 and the same PANTHER subfamily, PTHR24056:SF174. No ProtNLM2 files were opened.

### Provenance and process
- Ran `just fetch-gene BALMU A0A8B8WEF1 --alias CDK16`, which gave 13 IEA annotations. None is experimental and the UniProt entry is unreviewed (PE 3).
- Deep research failed. `just deep-research-falcon BALMU CDK16 --fallback perplexity-lite` stopped with a falcon "Failed to authenticate" error, and the perplexity fallback returned HTTP 401 (insufficient quota). No deep-research file was written. Literature came instead from a PubMed search (CDK16/PCTAIRE1/PCTK1, 128 hits), and 20 key papers were cached in publications/.
- Bioinformatics: `CDK16-bioinformatics/compare_to_human.py` aligns the whale protein with human Q00536. Identity is 98.19% with 0 gaps. Seven of the nine differences fall in the disordered N-terminus. Lys194, Asp286 (HRD), Asp304 (DFG), Ser12, Ser95, Ser119 and Ser153 are all conserved. See RESULTS.md.

### Evolutionary grounding
- The whale protein, human CDK16 (Q00536) and mouse Cdk16 (Q04735) all share PANTHER PTHR24056:SF174.
- PAINT: the CDK16-specific node PTN004656776 carries IBD for synaptic vesicle, exocytosis and neuron projection development, all seeded only by mouse MGI:97516 (interpro/panther/PTHR24056/PTHR24056-paint.tsv). The whale TreeGrafter rows cite the graft node PTN000623744.
- Mouse experimental terms that PAINT did NOT propagate: spermatogenesis (IMP, 22184064), growth hormone secretion (IMP, 16461345) and regulation of insulin secretion (IMP, 22798068). Human IDA positive regulation of autophagy (32098961) was not propagated either. I treated these omissions as deliberate and did not propose any of them as NEW. Spermatogenesis is a knockout organismal phenotype in any case.
- The human IBA rows for cytoplasm and for the cyclin-dependent protein kinase holoenzyme complex come from PTN002373304. The whale protein lacks the complex term, and I proposed it as NEW on the strength of the direct structural and biochemical evidence for the CCNY complex.

### Established experimentally (human/mouse/rat only; nothing in whale)
- Cyclin Y-dependent Ser/Thr kinase activity, proline-directed with a +4 basic preference [PMID:22796189 "PCTAIRE-1 binds to a novel cyclin family member, cyclin Y, which increased PCTAIRE-1 activity towards PCTAIRE-tide >100-fold"].
- Activation needs phosphorylated cyclin Y bound to 14-3-3 [PMID:26205494] and has a cryo-EM structure [PMID:41857027].
- Cytoplasmic, with cyclin Y-dependent recruitment to the plasma membrane [PMID:22184064 "a fraction of CDK16-GFP was recruited to the plasma membrane"].
- Phosphorylates NSF S569 and modulates regulated exocytosis in PC12 cells [PMID:16461345].
- Needed for dendrite development in rodent neurons [PMID:21335063].

### Decisions
- GO:0004693 is ACCEPTed as the core MF. GO:0004672, GO:0004674, GO:0016301 and GO:0016740 are MODIFIED to GO:0004693. GO:0000166 is MODIFIED to ATP binding, and ATP binding is ACCEPTed.
- Cytoplasm is ACCEPTed. Nucleus is marked over-annotated (deep-node CDK location; CDK16 data say cytoplasmic). Synaptic vesicle is marked over-annotated (co-association only).
- Exocytosis is MODIFIED to regulation of exocytosis. Neuron projection development is KEEP_AS_NON_CORE. Regulation of cell cycle is marked over-annotated: it is a logical inference from the MF label, and the cell-cycle data come only from cancer cells.
- NEW: plasma membrane and cyclin-dependent protein kinase holoenzyme complex (orthology).
