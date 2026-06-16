# BBS1 (Q8NFJ9) research notes

Gene: BBS1 / "BBSome complex member BBS1" / Bardet-Biedl syndrome 1 protein. Human, HGNC:966. 593 aa, chromosome 11.

## Summary of function

BBS1 is a core subunit of the **BBSome** (GO:0034464), an octameric, coat-like protein complex
(BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP1/BBIP10). The BBSome is structurally related
to COPI/COPII/clathrin coats and functions as a cargo adaptor that traffics specific transmembrane
proteins (notably ciliary GPCRs and Hedgehog-pathway components) into and out of the primary cilium
by coupling them to intraflagellar transport (IFT).

- BBSome is a membrane-trafficking coat that sorts membrane proteins to primary cilia
  [PMID:20603001 "the BBSome constitutes a coat complex that sorts membrane proteins to primary cilia"].
- The BBSome is the major effector of the Arf-like GTPase **ARL6/BBS3**; GTP-bound ARL6 recruits the
  BBSome to the ciliary membrane and the two colocalize at ciliary punctae in an interdependent manner
  [PMID:20603001 "The BBSome is the major effector of the Arf-like GTPase Arl6/BBS3, and the BBSome
  and GTP-bound Arl6 colocalize at ciliary punctae in an interdependent manner"].
- Cargo recognition: the ciliary targeting signal of somatostatin receptor 3 (SSTR3) is directly
  recognized by the BBSome to mediate ciliary targeting
  [PMID:20603001 "the ciliary targeting signal of somatostatin receptor 3 needs to be directly
  recognized by the BBSome in order to mediate targeting of membrane proteins to cilia"].

### BBS1 as the β-propeller / ARL6-binding subunit
- Structural work shows BBS1 contains a 7-bladed β-propeller that binds ARL6/BBS3-GTP, providing the
  membrane-targeting interface of the BBSome [PMID:25402481 "Structural basis for membrane targeting
  of the BBSome by ARL6"]. The IntAct annotation records direct BBS1–ARL6 (Q9H0F7) interaction.
  Disease-causing BBS1 M390R maps to this propeller and weakens ARL6 binding (literature).

### BBSome assembly and Rab8/ciliary membrane biogenesis
- BBS1 was identified as part of the original 7-subunit BBSome core that, together with Rab8 GEF
  (RAB3IP/Rabin8), promotes ciliary membrane biogenesis [PMID:17574030 "A core complex of BBS proteins
  cooperates with the GTPase Rab8 to promote ciliary membrane biogenesis"; UniProt: "INTERACTION WITH
  RAB3IP"]. The BBSome associates with the ciliary membrane and binds RAB3IP/Rabin8, the GEF for Rab8;
  Rab8-GTP then promotes docking/fusion of carrier vesicles at the ciliary base (UniProt FUNCTION).
- BBSome assembly is chaperonin-assisted: BBS6/BBS10/BBS12 + CCT/TRiC mediate assembly of the BBSome
  [PMID:20080638 "BBS6, BBS10, and BBS12 form a complex with CCT/TRiC family chaperonins and mediate
  BBSome assembly"; BBS1 IDA part_of BBSome from this paper]. Sequential, intrinsic PPI-driven assembly
  with the BBS7–BBS2 and chaperonin intermediates [PMID:22500027].

### Cargo / signaling roles
- **Hedgehog (SHH):** Loss of BBS genes causes accumulation of Smoothened (SMO) and Patched1 (PTCH1) in
  cilia and a decreased Shh response; BBS genes genetically interact with the IFT pathway to modulate
  SHH-related developmental phenotypes [PMID:22228099 "the loss of BBS genes in mice result in
  accumulation of Smoothened and Patched 1 in cilia and have a decreased Shh response"]. NOTE: This is a
  **genetic interaction / cilia-accumulation** study, not a direct binding assay; the "patched binding"
  and "smoothened binding" IPI annotations from this paper are over-interpretations of genetic/trafficking
  data (BBSome regulates SMO/PTCH1 ciliary levels). The IBA propagation of these MF terms is therefore weak.
- **Leptin receptor (LEPR):** BBS proteins are required for leptin receptor signaling; BBS1 interacts with
  LEPR and Bbs loss causes leptin resistance (relevant to obesity) [PMID:19150989; IntAct BBS1–Lepr
  (mouse, P48356)]. The "Golgi to plasma membrane protein transport" IMP from this paper reflects defective
  LEPR surface trafficking.
- **Polycystin-1 (PKD1/PC1):** BBS1 (and BBS3) regulate ciliary trafficking of PC1; PC1 interacts with a
  subset of BBSome subunits (BBS1/4/5/8) and only BBS1 depletion/mutation impairs PC1 ciliary trafficking
  [PMID:24939912 "the ADPKD protein polycystin-1 (PC1) interacts with BBS1, BBS4, BBS5 and BBS8... Only
  depletion or mutation of BBS1... impairs ciliary trafficking of PC1"]. Supports BBS1 as the principal
  cargo-recognition subunit.

### Regulation / interactions with NPHP/Cep290 module
- NPHP5 (IQCB1) and CEP290 regulate BBSome integrity, ciliary trafficking and cargo delivery
  [PMID:25552655; IntAct BBS1–IQCB1 Q15051]. BBSome physically/genetically interacts with CEP290 (via BBS4)
  and modifies CEP290-ciliopathy phenotypes [PMID:23943788]. BBS1 mutations modify phenotypic expression of
  CEP290-related ciliopathies — basis for the IMP "protein localization to cilium" annotation.

### Centrosome / centriolar satellites
- BBS proteins localize at/near the centrosome and centriolar satellites; BBS4 (with DISC1) recruits PCM1
  to the centrosome [PMID:18762586]. BBS1 IntAct interaction with PCM1 (Q15154) and centrosome IDA derive
  from this/related work. AZI1/CEP131 (centriolar satellite) interacts with BBS4 and regulates BBSome
  ciliary trafficking [PMID:24550735]. UniProt subcellular location: cilium membrane; cytoplasm;
  centrosome; centriolar satellite. Note the original BBSome paper found the complex is **dispensable for
  centriolar satellite function** (UniProt FUNCTION), so centriolar-satellite localization is likely a
  pool/staging location rather than a core functional site.

### Transcriptional regulation (PMID:22302990)
- This paper foregrounds **BBS7** (which has a nuclear export signal and interacts with PcG protein RNF2);
  it argues "a similar role for other BBS proteins" in transcription. The BBS1 IPI "RNA polymerase II-specific
  DNA-binding transcription factor binding" to RNF2 (Q99496) is an over-extrapolation from BBS7 data to BBS1
  and is not a core BBS1 function. Keep as non-core / mark over-annotated.

## Disease
- Bardet-Biedl syndrome 1 (BBS1, MIM:209900): pigmentary retinopathy, obesity, polydactyly, hypogenitalism,
  renal malformation, intellectual disability. BBS1 is the **most commonly mutated** BBS gene; M390R is the
  most common allele [PMID:12118255 founding paper]. Autosomal recessive; some forms show oligogenic/triallelic
  inheritance [PMID:16327777 CCDC28B modifier]. Retinal degeneration / photoreceptor maintenance defects
  [PMID:17980398].

## Interaction partners (IntAct, from GOA) — mostly BBSome subunits + cargo/regulators
- BBSome subunits: BBS2 (Q9BXC9), BBS4 (Q96RK4), BBS7 (Q8IWZ6), BBS9 (Q3SYG4). These IPI "protein binding"
  annotations simply re-establish complex membership.
- ARL6/BBS3 (Q9H0F7) — small GTPase, membrane-targeting (direct, structural).
- RAB3IP/Rabin8 (Q96QF0) — Rab8 GEF.
- Cargo/regulators: LEPR (P48356, mouse), PKD1 (Q8TAM2), IQCB1/NPHP5 (Q15051), PCM1 (Q15154).
- Possibly non-specific / interactome-screen hits: EEF1A1 (P68104), ALDOB (P05062), PARK7/DJ-1 (Q99497),
  DCTN1 (Q14203), CCDC28B (Q9BUN5). Several are from high-throughput interactome maps (PMID:27173435,
  29039417, 32814053, 33961781, 40205054) and the legacy "novel interaction partners" screen (PMID:18000879).

## Annotation review judgments (summary)
- CORE: BBSome (part_of, GO:0034464) — strongly supported, multiple IDA. ACCEPT.
- CORE: protein localization to cilium (GO:0061512) — BBSome cargo trafficking. ACCEPT (IMP/IBA).
- CORE: cilium / non-motile cilium assembly (GO:1905515 / GO:0060271) — ACCEPT IMP/IBA.
- CORE: small GTPase binding — not currently annotated as such but is the real MF (ARL6-GTP). The generic
  "protein binding" IPI annotations to ARL6 should ideally be MF small GTPase binding; propose new term.
- centrosome (GO:0005813), ciliary membrane (GO:0060170), cytosol (GO:0005829), cytoplasm (GO:0005737):
  ACCEPT as supported localizations (cilium membrane + cytoplasm + centrosome per UniProt).
- centriolar satellite (GO:0034451): KEEP_AS_NON_CORE (staging pool; complex dispensable for satellite fn).
- axoneme (GO:0005930) IBA: weakly supported — BBSome acts at ciliary membrane/base; KEEP_AS_NON_CORE.
- patched binding / smoothened binding (GO:0005113 / GO:0005119): over-annotated — derived from genetic /
  cilia-accumulation data, not direct binding. MARK_AS_OVER_ANNOTATED.
- RNA Pol II TF binding (GO:0061629): over-annotated, extrapolated from BBS7. MARK_AS_OVER_ANNOTATED.
- fat cell differentiation (GO:0045444), retina homeostasis (GO:0001895), photoreceptor cell maintenance
  (GO:0045494): downstream/physiological consequences of ciliary dysfunction; KEEP_AS_NON_CORE.
- regulation of cilium beat frequency involved in ciliary motility (GO:0060296) + motile cilium (GO:0031514):
  BBS1/BBSome act on NON-motile (primary/sensory) cilia; these motile-cilium terms are likely mis-propagated
  Ensembl IEA. MARK_AS_OVER_ANNOTATED / REMOVE candidates (IEA, not curator).
- Golgi to plasma membrane protein transport (GO:0043001) IMP: from LEPR surface-trafficking; KEEP_AS_NON_CORE.
- intracellular protein localization (GO:0008104) IEA ARBA: vague generalization of cargo trafficking; MODIFY
  to protein localization to cilium.
- signaling receptor binding (GO:0005102) IEA: defensible (BBSome binds GPCR cargo) but generic; KEEP_AS_NON_CORE.
- phosphoprotein binding (GO:0051219) IEA Ensembl: weakly supported; UNDECIDED/over-annotated.
- protein binding (GO:0005515) IPI ×many: uninformative per guidelines; the BBSome-subunit ones support
  complex membership; KEEP_AS_NON_CORE (avoid promoting "protein binding").
</content>
