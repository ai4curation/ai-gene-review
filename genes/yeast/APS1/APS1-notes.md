# APS1 (P35181, YLR170C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: APS1 is the experimentally characterised S. cerevisiae relative of S. pombe vas2/Aps1 (Q9P7N2).
ProtNLM2 output was not consulted.

### Process
- `just fetch-gene yeast APS1` created the stub (32 GOA rows).
- `just deep-research-falcon yeast APS1 --fallback perplexity-lite` FAILED: falcon failed and the
  perplexity-lite fallback timed out after 600 s. No deep-research file exists. The review is built from
  cached literature that I read directly.
- Extra papers cached: PMID:8157009 (Phan 1994), PMID:8373805 (YAP19 cloning), PMID:11879634
  (Valdivia 2002), PMID:26658609 (Whitfield 2016, full text), PMID:19624755 (S. pombe AP-1, Ma 2009),
  PMID:16823372 (S. pombe ORFeome).

### Evolutionary grounding
- UniProt: "Belongs to the adaptor complexes small subunit family." PANTHER family PTHR11753; according to the
  task brief, PANTHER 19 places APS1 and S. pombe Q9P7N2 together in PTHR11753:SF5 "AP COMPLEX SUBUNIT SIGMA".
  I did not re-query this myself; the SF5 name is confirmed in interpro/panther/panther.obo.
- PAINT (interpro/panther/PTHR11753/PTHR11753-paint.tsv): the only IBD nodes are at the root PTN000204281, for
  GO:0016192 vesicle-mediated transport and GO:0043231 intracellular membrane-bounded organelle. SGD:S000004160
  (APS1) is itself an experimental donor. PAINT propagated no AP-1-specific term (such as AP-1 adaptor complex)
  from the root, which is correct because the root covers sigma1/2/3/4 and COPI zeta.
- The ISS localization rows come from S. pombe Q9P7N2, which is in the same subfamily. The Golgi, endosome and
  CCV localizations in pombe come from the AP-1 subunit study [PMID:19624755 "the deletion of any subunit
  generally caused the disassociation of the heterotetrameric complex from endosomes"]. The nucleus and
  cytoplasm localizations come only from the genome-wide ORFeome GFP screen (PMID:16823372). I therefore
  marked nucleus as over-annotated.

### What is experimental in S. cerevisiae
- AP-1 subunit composition, including Aps1, by co-IP; only AP-1 binds clathrin [PMID:10564262 "As assessed by in
  vitro binding assays and coimmunoprecipitation, only AP-1 interacts with clathrin."]. Abstract only.
- Aps1 co-fractionates with CCVs. aps1 deletion has no phenotype alone, but it worsens chc1-ts growth and
  alpha-factor maturation [PMID:8157009 "These results comprise evidence that Aps1p is involved in a subset of
  clathrin functions at the Golgi apparatus."].
- Aps1 is shared by AP-1 and AP-1R [PMID:26658609 "The two forms of AP-1 share the same large (Apl2 and Apl4)
  and small (Aps1) subunits but incorporate different medium subunits (Apm1 or Apm2)."]. The aps1 deletion
  raises surface levels of the Snc1 reporter GSS [PMID:26658609 "Loss of APM2, APL4, and APS1 led to a slight but
  significant increase in GSS surface levels"].
- AP-1 retains Chs3 and Tlg1 in the TGN/early endosome [PMID:11879634 "We propose that clathrin and AP-1 act to
  recycle Chs3p and Tlg1p from the early endosome to the TGN."]. The abstract speaks of AP-1 in general, not of
  aps1 specifically.
- AP-1 mutants fail to deliver ubiquitylated cargo to the vacuole lumen. The paper attributes this to defective
  Fab1 activation (PMID:17003107). I kept the IMP Golgi to vacuole transport row, as non-core.

### Inferred, not established for Aps1 itself
- Dileucine-signal recognition by the gamma/sigma hemicomplex. In yeast this is stated by analogy
  [PMID:26658609 "Because the dileucine-based motif of Chs3 binds the γ/σ subunits present in both AP-1 and
  AP-1R"]. It has not been mutationally mapped to Aps1. Hence `contributes_to` clathrin-cargo adaptor activity.

### Decisions in brief
- AP-1 adaptor complex (EXP/IDA/NAS/IEA) and CCV membrane: ACCEPT.
- Clathrin-cargo adaptor activity (IEA): ACCEPT. ND root: MODIFY to GO:0035615.
- 10 bare protein-binding IPI rows (all with other AP-1 subunits): REMOVE under the protein-binding policy.
- Golgi apparatus, endosome: ACCEPT. Cytoplasm and membrane coat: TOO_GENERAL, since both are entailed by
  AP-1 adaptor complex. Nucleus: MARK_AS_OVER_ANNOTATED.
- Intracellular protein transport and vesicle-mediated transport (IBA and IEA): ACCEPT. Protein transport:
  TOO_GENERAL. Intercellular transport (ARBA): REMOVE. Golgi to vacuole transport (IMP): KEEP_AS_NON_CORE.
- No NEW terms. UniProt also carries GO:0048203 (vesicle targeting, trans-Golgi to endosome; IMP from
  ComplexPortal), but it is not in the GOA set and I did not add it. Valdivia's model is endosome-to-TGN
  recycling, so the direction is not settled.
