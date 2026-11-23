# FZD10 notes

## Deep research
- `just deep-research-falcon human FZD10 --fallback perplexity-lite` failed (falcon/perplexity
  providers unavailable in this environment, 2026-10-21). Research below is from the cached
  publications and the UniProt record.

## Identity and topology
- Frizzled-10 (CD350), class F GPCR, 581 aa. "human FZD10 gene encodes a seven-transmembrane-receptor of
  581 amino acids, with the N-terminal cysteine-rich domain and the C-terminal Ser/Thr-Xxx-Val motif"
  [PMID:10448064]. Signal peptide 1-20, extracellular CRD (21-225), 7 TM helices; three N-glycosylation
  sites in UniProt [file:human/FZD10/FZD10-uniprot.txt].
- FZD9/FZD10 subfamily: "FZD10 and FZD9 constitute a subfamily among the Frizzled genes" [PMID:10448064].

## Localization (cell-surface benchmark)
- Cell surface, ECD exposed: an anti-ECD antibody mediated ADCC on synovial sarcoma cells
  [PMID:16007199 "a polyclonal antibody specifically recognizing the extracellular domain (ECD) of FZD 10"];
  "MAb 92‐13 bound to cell surfaces of four FZD10‐overexpressing synovial sarcoma cell lines" and is
  internalized after binding [PMID:18271942].
- Conclusion: plasma membrane, extracellular CRD exposed at the cell surface; internalizes on antibody binding.
- Cytoplasm IDA (PMID:16007199) is from IHC of tumors (abstract-only); not verifiable here.

## Function
- Wnt receptor: in FZD-knockout rescue, "Wnt9b induced canonical signaling with FZD5 and FZD8, but also with
  FZD4 and FZD10" and "Wnt9a signaled only via FZD4 and FZD10" [PMID:28733458].
- Non-canonical: overexpression in synovial sarcoma activates Dvl2/3 phosphorylation and Rac1-JNK,
  lamellipodia [PMID:19137009].
- HIG2/HILPDA binds the FZD10 ECD and enhances Wnt signaling [PMID:15930302]; myocilin binds Frizzled CRDs
  [PMID:19188438].
- PDZ-binding C-terminal motif binds many PDZ proteins in holdup assays [PMID:36115835].

## Curation issues
- ISS rows for neuron differentiation and cellular response to retinoic acid have WITH = UniProtKB:P56706,
  which is human WNT7B (a ligand, not a homolog); sequence-similarity transfer from it is invalid.
- IBA extracellular region comes from the sFRP node PTN002259328 (see PTHR11309 family review); FZD10 is a
  7TM protein, not secreted.
