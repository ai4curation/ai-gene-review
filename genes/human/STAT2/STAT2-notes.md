# STAT2 (human, P52630) — Gene Review Notes

Journal of research for the STAT2 AI gene review. Provenance recorded inline as [PMID:xxxx "verbatim quote"].

## Summary of gene function

STAT2 (Signal Transducer and Activator of Transcription 2; "p113") is a member of the
STAT family dedicated to **type I (IFN-alpha/beta) and type III interferon signaling**.
Unlike other STATs, STAT2 does **not** bind DNA on its own GAS element; instead it acts
as the obligate partner of STAT1 and IRF9 in the **ISGF3 complex**, contributing a strong
C-terminal transactivation domain (TAD) and the IRF9 interaction surface.

### Domain architecture (UniProt P52630)
- 851 aa; STAT family. Domains: N-terminal domain (NTD), coiled-coil (CC), DNA-binding
  domain (DBD), linker, SH2 domain (residues 572–667), C-terminal transactivation domain.
- SH2 domain mediates docking to phospho-IFNAR1 (pTyr466) and STAT1/STAT2 dimerization.
- Tyr690 is the activating JAK-phosphorylation site [UniProt MOD_RES 690 "Phosphotyrosine; by JAK"].
- Ser287 phosphorylation in the CC domain negatively regulates transcriptional output.

### Canonical mechanism (type I IFN / ISGF3)
[PMID:28165510 "The binding of type I IFNs to the receptor subunits IFNAR1 and IFNAR2 induces the activation of their associated Janus family tyrosine kinases TYK2 and JAK1, respectively"]
[PMID:28165510 "Activated TYK2 and JAK1 in turn phosphorylate IFNAR2-associated STAT2 and STAT1, which results in formation of the DNA binding STAT1/STAT2/IRF9 ternary complex IFN-stimulated gene factor 3 (ISGF3). ISGF3 promotes expression of genes with the IFN-stimulated response element in their promoters"]

STAT2 contributes the TAD but cannot itself stably contact DNA:
[PMID:9020188 "Although Stat2 is a potent transactivator, it does not interact stably with DNA in complex with p48 alone."]
[PMID:9020188 "Stat2 contributes a potent transactivation domain but is unable to directly contact DNA, while Stat1 stabilizes the heteromeric complex by contacting DNA directly."]
[PMID:9020188 "ISGF3 assembly involves p48 functioning as an adaptor protein to recruit Stat1 and Stat2 to an IFN-alpha-stimulated response element"]

Note: STAT2 *can* form a homodimer that interacts with p48/IRF9 and activate transcription
in vitro [PMID:9020188 "Stat2 is capable of forming a stable homodimer that interacts with p48, can be recruited to DNA, and can activate transcription"], so the IDA DNA-binding TF annotations are defensible at the level of the complex.

### Receptor docking
[PMID:12220192 "Interferon alpha binding to the receptor induces phosphorylation of tyrosine 466 on IFNaR1, which in turn binds the SH2 domain of the latent transcription factor Stat2 to initiate signaling. Stat2 also binds to IFNaR2 in a constitutive, phosphorylation-independent manner."]
[PMID:8605876 "A phosphopeptide corresponding to the major phosphorylation site (Tyr466) binds STAT2, but not STAT1, in an SH-2-dependent manner."]
- 8605877: SH2 domains of STAT1/STAT2 mediate multiple interactions including homo- and heterodimerization.
- 9121453: functional subdomains of STAT2 required for preassociation with IFNAR and for signaling.
- 9677371: residues critical for SH2-dependent docking of STAT2 to IFNAR1.

### Negative-feedback role (USP18)
STAT2 is a positive effector but ALSO an obligate adaptor for USP18-mediated negative feedback:
[PMID:28165510 "STAT2 is a well-known essential and specific positive effector of type I IFN signaling. Here, we report that STAT2 is also a previously unrecognized, crucial component of the USP18-mediated negative-feedback control in both human and mouse cells. We found that STAT2 recruits USP18 to the type I IFN receptor subunit IFNAR2 via its constitutive membrane-distal STAT2-binding site."]
This is the basis of GO:0060339 (negative regulation of type I IFN signaling) and the
GO:0044389 (ubiquitin-like protein ligase binding — USP18 is a UBL/ISG15 protease) annotations.

### Disease / loss & gain of function (human genetics)
- **IMD44 (loss of function):** STAT2 deficiency → susceptibility to viral illness.
  [PMID:23391734 "Patient fibroblasts were indeed abnormally permissive for viral replication in vitro, associated with profound failure of type I IFN signaling and absence of STAT2 protein."]
  [PMID:23391734 "The complete lack of STAT2 provided a ready explanation for the failure to induce ISGs dependent upon activation by the ISGF3 complex."]
  Notably, ISGF3-dependent signaling is dispensable for adaptive immunity and not essential
  for defense against most common viruses [PMID:23391734 "type I IFN signaling [through interferon-stimulated gene factor 3 (ISGF3)] is surprisingly not essential for host defense against the majority of common childhood viral infections"].
- **PTORCH3 (gain of function, R148Q/R148W):** type I interferonopathy from loss of USP18 trafficking.
  [PMID:32092142 "The variant is a gain of function (GOF) for induction of the late, but not early, response to IFN-I."]
  [PMID:32092142 "the STAT2 R148Q variant is a GOF because it fails to appropriately traffic USP18 to IFNAR2, thereby preventing USP18 from negatively regulating responses to IFN-I."]
  [PMID:31836668 paper: "Severe type I interferonopathy and unrestrained interferon signaling due to a homozygous germline mutation in STAT2."]

### Mitochondrial fission (a distinct, non-canonical role)
STAT2 deficiency causes a mitochondrial fission disorder via DRP1 (DNM1L) phosphorylation:
[PMID:26122121 "Taken together, these findings implicate STAT2 as a novel regulator of DRP1 phosphorylation at serine 616, and thus of mitochondrial fission"]
[PMID:26122121 "All three patients harboured decreased levels of DRP1 phosphorylated at serine residue 616 (P-DRP1(S616)), a post-translational modification known to activate DRP1, and increased levels of DRP1 phosphorylated at serine 637 (P-DRP1(S637)), associated with the inactive state of the DRP1 GTPase."]
This underlies GO:0090140 (regulation of mitochondrial fission) and GO:0001932 (regulation of
protein phosphorylation). Treat as a real but **non-core / pleiotropic** function — likely an
indirect downstream consequence of disrupted IFN tone rather than a direct STAT2 enzymatic role.

### Chromatin / TAD recruitment
[PMID:31127039 "HDAC4 is recruited to ISG promoters after IFN-α stimulation and that HDAC4 is required for normal STAT2 recruitment to these promoters"]
[PMID:31127039 "A fusion protein containing the C-terminal 104 amino acids of STAT2, including the transactivation domain (TAD)"]
Supports the IC chromatin annotation and the role of the STAT2 TAD.

### Phosphoregulation
[PMID:23139419 "STAT2 is a positive modulator of the transcriptional response to type I interferons (IFNs). STAT2 acquires transcriptional function by becoming tyrosine phosphorylated and imported to the nucleus following type I IFN receptor activation."]
[PMID:23139419 "in response to type I IFN, STAT2 is serine phosphorylated in the coiled-coil domain that when phosphorylated can negatively regulate the biological activities of type I IFNs"]

### Subcellular localization
[PMID:11150296 paper: arginine/lysine-rich element involved in IFN-induced nuclear import of STATs.]
UniProt: Cytoplasm and Nucleus; "Translocated into the nucleus upon activation by IFN-alpha/beta."

## Annotation review strategy

Core functions to capture:
1. **Type I interferon-mediated signaling pathway** (GO:0060337) — the defining biology.
2. **Transcription coactivator / DNA-binding TF activity within ISGF3** — STAT2 supplies the
   TAD; DNA binding is a property of the complex (STAT1 contacts DNA). Capture via
   GO:0000981 (DNA-binding TF activity, Pol II-specific) and positive regulation of Pol II
   transcription (GO:0045944), modelled through the ISGF3 complex (GO:0070721).
3. **JAK-STAT signaling** (GO:0007259) and **defense response to virus** (GO:0051607).
4. **Negative regulation of type I IFN signaling** (GO:0060339) via USP18 adaptor role — core
   regulatory function; KEEP.

Non-core / pleiotropic: mitochondrial fission, regulation of protein phosphorylation.

Over-annotations / non-informative:
- The ~20 `protein binding` (GO:0005515) IPI annotations: mostly large-scale interactome /
  AP-MS screens (28514442, 26966684, 33961781, 35140242, 40205054, 21903422) or viral-antagonist
  interaction papers. Per CLAUDE.md, `protein binding` is uninformative → MARK_AS_OVER_ANNOTATED
  for the high-throughput screens; KEEP_AS_NON_CORE for specific informative pairwise interactions
  (e.g. IFNAR docking, USP18). GO:0042802 identical protein binding (homodimerization) is real
  (STAT2 homodimer, PMID:9020188; 8605877) → KEEP_AS_NON_CORE.
- The many Reactome `cytosol`/`nucleoplasm` TAS location annotations are correct but redundant
  reaction-level localizations → KEEP_AS_NON_CORE (location ACCEPT is fine but non-core).
- GO:0003677 (DNA binding) IEA and GO:0003700 (DNA-binding TF activity) IEA from InterPro:
  STAT2 alone does not stably bind DNA; the more specific Pol II-specific term + ISGF3 modelling
  is preferred. Generic GO:0003700 IEA → MARK_AS_OVER_ANNOTATED/MODIFY toward GO:0000981; but the
  IDA-supported GO:0003700/GO:0000981 (PMID:9020188, 31127039) are defensible (homodimer + complex)
  → KEEP_AS_NON_CORE / ACCEPT.

GAS-binding caveat: STAT2 is NOT a classic GAS-binding TF; its sequence-specific DNA association
is only as part of ISGF3 binding ISRE. Avoid annotating STAT2 with autonomous DNA-binding as core.
