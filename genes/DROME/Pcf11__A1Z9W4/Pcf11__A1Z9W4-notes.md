# Pcf11 (A1Z9W4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full review of A1Z9W4, the 1953-residue long product of Drosophila Pcf11 (FBgn0264962, CG10228, Inr-a), done as the experimentally characterised reference for the 86-residue product C0P8M6 (reviewed separately in `genes/DROME/Pcf11/`). ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon DROME Pcf11__A1Z9W4 --fallback perplexity-lite` failed on 2026-10-21: falcon (Edison) returned "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 (insufficient quota). No deep-research file was written for this folder. The review relies on primary literature read directly from `publications/`. The locus-level falcon report in `genes/DROME/Pcf11/Pcf11-deep-research-falcon.md` was read for leads only and is not cited.

### Identity and evolutionary grounding

- A1Z9W4 is in PANTHER PTHR15921:SF3 together with yeast Pcf11 P39081, human PCF11 O94913, S. pombe Q10237 and worm pcf-11 Q09345 (PANTHER 19.0 classification files). SCAF8 is in SF7. Transfer from yeast and human Pcf11 is therefore within one subfamily.
- The 573-residue product Q8IGR2 shares residues 1-372 of A1Z9W4, which cover the whole CID (17-149) and the helical region (190-224). The fly antibody (aa 1-283) and the N-terminal constructs used in the experiments recognise or represent a region that A1Z9W4 contains in full [file:DROME/Pcf11__A1Z9W4/Pcf11__A1Z9W4-bioinformatics/RESULTS.md].
- A1Z9W4 has a conserved first zinc-finger motif (1368-1390) that matches human PCF11 1343-1365, and a Pcf11 C-terminal domain (1465-1509).

### Experimentally established in Drosophila

- Termination: [PMID:16387654 "depletion of dPcf11 with RNAi causes Pol II to readthrough the normal region of termination"]. Termination at a widely spaced tandem gene pair depends on Pcf11, but at polo-snap it does not [PMID:22992452].
- CTD binding and RNA bridging; dismantling of paused elongation complexes without nucleotides [PMID:16387654 "dPcf11 forms a bridge between the CTD and RNA"].
- Location in the nucleus and on chromatin: transcribed polytene loci and the hsp70 3' end [PMID:16387654]; spermatocyte nuclei [PMID:39111825]; perinucleolar in late spermatocytes [PMID:40896257].
- CFII with Cbc: HA-Cbc co-IPs the >250 kDa Pcf11 band (the long forms, which include A1Z9W4), but not the ~70 kDa RB form [PMID:39111825].
- Alternative polyadenylation: knockdown shifts cleavage to distal sites, and overexpression shifts it to proximal sites [PMID:39111825].
- piRNA-guided transposon silencing: tethered Pcf11 stalls Pol II through condensates with Spt5 that depend on its helical region [PMID:40015272, abstract only].
- Recessive lethality and inverse dosage effect on white [PMID:22690379]. These are phenotypes and are not annotated as processes.

### Inferred only (orthologs in the same subfamily)

- RNA binding via the C-terminal zinc fingers [PMID:30139799, human]. No RNA-binding region has been mapped for the fly protein.
- Separable CTD-binding and processing functions [PMID:12727883, yeast].

### Decisions

- GO:0000993 (IBA and IEA): MODIFY to GO:0099122, because the fly evidence specifies CTD binding.
- GO:0006369 (IEA): MODIFY to GO:0030846, which is also present by IBA and is ACCEPTed.
- Cytoplasm (IBA): MARK_AS_OVER_ANNOTATED, because there is no fly evidence for a cytoplasmic site.
- gene expression and protein-containing complex (ARBA): TOO_GENERAL.
- piRNA heterochromatin (IMP): KEEP_AS_NON_CORE.
- NEW: GO:0110104 mRNA alternative polyadenylation (IMP, PMID:39111825). The comparator check found CPSF6 and CPSF7 (CFIm) carrying this term in GOA. NEW: GO:0000785 chromatin (IDA, PMID:16387654).
