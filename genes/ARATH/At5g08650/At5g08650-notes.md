# At5g08650 (cpLEPA; Q9FNM5) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No prior review existed. Files fetched with `just fetch-gene ARATH At5g08650 --uniprot-id Q9FNM5`.

Deep research: `just deep-research-falcon ARATH At5g08650 --fallback perplexity-lite`
failed (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota).
No deep-research file exists; the review is built from the cached literature below.

### Identity and evolutionary placement
- UniProt Q9FNM5 GUFP_ARATH, 681 aa precursor, predicted 51-aa chloroplast transit peptide
  (HAMAP MF_03138), tr-type G domain 84..265, LepA C-terminal domain.
- PANTHER PTHR43512:SF4 (TRANSLATION FACTOR GUF1 HOMOLOG, CHLOROPLASTIC), same subfamily as
  E. coli LepA (P60785); mitochondrial GUF1s (Arabidopsis Q9FLE4, yeast P46943, human Q8N442)
  are SF7. Global identity 53.8% to E. coli LepA vs 44-50% to the SF7 proteins
  [file:ARATH/At5g08650/At5g08650-bioinformatics/RESULTS.md].
- PAINT: PTN002460656 (no taxon constraint, i.e. a deep node; seeds SGD GUF1 + E. coli LepA)
  carries ribosome binding (GO:0043022) and positive regulation of translation (GO:0045727).
  PTN000563148 (Eukaryota mitochondrial clade) carries mitochondrion and mitochondrial ribosome
  binding; Q9FNM5 does not receive these, consistent with its plastid branch.
  No GTPase activity IBD is placed in this family; GTPase activity comes only from IEA (InterPro/UniRule).

### Experimental findings in Arabidopsis (PMID:23166764, Ji et al. 2012, full text)
- Immunoblot of fractionated chloroplasts: most cpLEPA in thylakoid fraction, stroma:thylakoid ~0.25;
  released by Na2CO3/CaCl2/urea but not NaCl -> peripheral thylakoid membrane association
  [PMID:23166764 "most of the cpLEPA protein was detected in the thylakoid fractions"].
- T-DNA nulls cplepa-1 (SALK_140697) and cplepa-2: pale green, high chlorophyll fluorescence,
  growth retardation on soil and without sucrose, sensitivity to high light; complemented by 35S::cpLEPA.
- In vivo [35S]-Met pulse labelling with cycloheximide: synthesis of plastid-encoded PsaA/B, D1,
  D2, CP47, CP43, CF1 alpha/beta reduced to 60-70% of WT -> direct evidence the gene is needed for
  plastid translation.
- Polysome loading of psbA, psbB, psaA/B, atpB mRNAs shifted slightly toward lighter fractions;
  authors interpret as translation initiation defect. Plastid transcripts (PEP-dependent) also reduced.
- Not tested: GTP hydrolysis, ribosome binding, back-translocation, in vitro translation.

So experimentally established in Arabidopsis: chloroplast (thylakoid-associated) location and a
requirement for efficient plastid protein synthesis (IMP). Inferred (homology to E. coli LepA,
PMID:17110332; yeast Guf1, PMID:18442968): GTPase activity, ribosome binding, back-translocation.

### Annotation decisions
- mRNA binding (IDA, RIC PMID:32344669): high-throughput capture; for a ribosome-associated GTPase
  likely reflects crosslinking within translating ribosomes. KEEP_AS_NON_CORE.
- plasma membrane (HDA PMID:28887381): fractionation proteomics; contradicts the transit peptide
  and immunolocalization. MARK_AS_OVER_ANNOTATED (not REMOVE: experimental HDA).
- protein domain specific binding (IPI with TOC132, PMID:24736607): preprotein-receptor interaction
  in a split-ubiquitin screen for import substrates; reflects the precursor being an import substrate,
  not a function of the mature protein. MARK_AS_OVER_ANNOTATED.
- NEW: chloroplast thylakoid membrane (IDA), plastid translation (IMP). Comparator check for
  GO:0032544: Arabidopsis chloroplast RRF (Q9M1X0, a ribosome-acting translation factor) carries
  plastid translation IMP, as do ribosomal proteins, so the term is used for translation factors.
