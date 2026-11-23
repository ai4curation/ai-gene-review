# IRF9 (human, Q00978) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised relative of donkey
EQUAS/IRF9 (A0A9L0I7X9). ProtNLM2 outputs were not consulted.

### Deep research

`just deep-research-falcon human IRF9 --fallback perplexity-lite` failed for
both providers with authentication errors ("Edison API request failed: Failed
to authenticate"; perplexity fallback: "JWT token required for JWT
authentication"). No deep-research file exists; the review uses the cached
publications listed below plus the UniProt record.

### Evolutionary placement

- UniProt PANTHER cross-references: PTHR11949 (INTERFERON REGULATORY FACTOR),
  subfamily PTHR11949:SF26 (INTERFERON REGULATORY FACTOR 9).
  `interpro/panther/PTHR11949/PTHR11949-entries.csv` lists human Q00978 and mouse
  Q61179 as SF26 members.
- IBA rows on human IRF9 come from two PAINT nodes: PTN000942746 (DNA binding,
  RNAPII DbTF activity, nucleus, regulation of transcription by RNAPII) and
  PTN000942747 (immune system process). These are IRF-family-wide properties.
  Neither node propagates an interferon-signalling term, so the ISGF3 role is
  supported by subfamily-level experimental evidence from human and mouse IRF9,
  not by the PAINT nodes.

### Literature (cached)

- Veals et al. 1992 [PMID:1630447, abstract only]: cloned ISGF3 gamma (p48 =
  IRF9). "ISGF3 gamma serves as the DNA recognition subunit"; in vitro
  translated protein "bound DNA with a specificity indistinguishable from that of
  ISGF3 gamma purified from HeLa cells"; it "interacted with HeLa cell ISGF3 alpha
  to form the mature ISGF3 DNA-binding complex". Activation "occurs in the
  cytoplasm, with subsequent translocation of the activated factor to the
  nucleus".
- Hernandez et al. 2018 [PMID:30143481, full text]: human AR IRF9 deficiency
  (splice-site, in-frame exon 7 deletion in the IAD). Patient cells form GAF but
  not ISGF3 after IFN-a2b; EMSA shows "abolished ISRE binding in vitro"; ISRE
  reporter abolished; "a small amount of IRF9 was visible in the nucleus even
  under basal conditions"; phenotypes "rescued by wild-type IRF9". Human-specific
  experimental evidence for the type I IFN pathway role.
- Bravo Garcia-Morato et al. 2019 [PMID:30826365, abstract not informative in
  cache]: second family with complete IRF9 deficiency; used only as disease
  context.
- Cheon et al. 2013 [PMID:24065129, full text]: unphosphorylated STAT1/STAT2/IRF9
  form U-ISGF3 that occupies ISREs (ChIP) and sustains a subset of ISGs; co-IP of
  STAT2-IRF9 in nuclear fractions.
- Rengachari et al. 2018 [PMID:29317535, full text]: crystal structures of the
  IRF9 IAD alone and with STAT2 CCD; the IAD-CCD interface is required for ISGF3
  activity (reporter assays in IRF9-/- IRF3-/- mouse MEFs).
- Tang et al. 2007 [PMID:17923090, abstract only]: IRF9 docks on CBP-acetylated
  IFNAR2 Lys399 through its IH2 (IAD) domain; acetylation of IRF9 DBD required.
  Single-lab report; treated as non-core.
- Kimura et al. 1996 [PMID:9078371, abstract only]: mouse p48-/- MEFs lack ISRE
  binding and antiviral state for IFN-a and IFN-g. Mouse (same SF26 subfamily);
  used only as corroborating ortholog evidence.
- Reich 2002 [PMID:11846981, review abstract]: IRF9 regulated by
  nuclear/cytoplasmic redistribution.
- Measles V protein [PMID:32581091, abstract only] blocks IRF9-STAT2 binding;
  host-virus context only.
- Yin et al. 2017 [PMID:28473536]: HT-SELEX; IRF9 not mentioned in the cached
  main text (data presumably in supplementary tables). IDA accepted, deferring
  to curator.
- TRIM6 paper [PMID:24882218]: cached text is truncated (introduction only).
  The IMP row for RNAPII cis-regulatory region binding cannot be inspected;
  accepted because the activity is well established for IRF9 by other evidence.

### Experimentally established in human vs inferred

Established in human: ISRE sequence-specific DNA binding (as ISGF3 gamma,
PMID:1630447; loss in patient cells, PMID:30143481); ISGF3 complex membership
and STAT2 binding (PMID:1630447, PMID:24065129); ISRE-driven transcriptional
activation in type I IFN signalling (PMID:30143481, PMID:24065129); cytoplasmic
and nuclear localization (PMID:30143481, PMID:11846981).

Inferred / ortholog-supported: requirement in type II (IFN-gamma) ISRE responses
(mouse KO, PMID:9078371); type III IFN involvement (not directly tested in the
cached human paper).

### Comparator check for NEW GO:0060337

Neither human nor mouse IRF9 carries GO:0060337 type I interferon-mediated
signaling pathway in GOA (QuickGO query 2026-10-21), while both other ISGF3
subunits do with experimental evidence: STAT1 P42224 (IDA PMID:23386060) and
STAT2 P52630 (IMP PMID:23391734, PMID:31836668, PMID:32092142). IRF9 stands in
the same role (subunit of the pathway's effector transcription factor) and
performs a step of the pathway itself: it is the DNA-binding subunit that
targets ISGF3 to ISREs. The pathway term's scope ends with transcriptional
regulation, so the effector TF participates; this is not a substrate case. The
absence on IRF9 is therefore treated as a curation gap and GO:0060337 is
proposed as NEW. Defense response to virus was not proposed (it is a downstream
outcome of ISG induction; patient-cell virus-control data establish necessity).
