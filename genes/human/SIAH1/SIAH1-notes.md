# SIAH1 (seven in absentia homolog 1) review notes

UniProt: Q8IUQ4 (SIAH1_HUMAN), 282 aa. EC 2.3.2.27. RING-type E3 ubiquitin ligase.

## Domain architecture
- RING-type zinc finger 41..76 (catalytic RING, recruits E2) [UniProt FT].
- Two additional zinc fingers (93..153) within the SIAH-type substrate-binding domain (SBD).
- Forms homodimers (and heterodimers with SIAH2). N-terminal RING; C-terminal SBD recognizes
  substrate degrons (often a VxP/PxAxVxP motif).

## Core molecular function
- RING-type E3 ubiquitin-protein ligase / ubiquitin-protein transferase (EC 2.3.2.27).
  Accepts ubiquitin from an E2 (thioester) and transfers directly to substrate.
  [UniProt FUNCTION; EC 2.3.2.27 ECO:0000269|PubMed:19224863, PubMed:28546513]
- Zinc ion binding (RING + Zn fingers structurally require Zn) [UniProt; PMID:16085652 structural; PMID:11863358].
- Binds E2 ubiquitin-conjugating enzymes (UBE2D1, UBE2E2, UBE2I, UBE2L6) — "ubiquitin conjugating enzyme binding".
  [PMID:9334332 "the Sina/Siah proteins interacted with ubiquitin-conjugating enzymes (Ubcs)"]

## Substrates / processes (the heart of SIAH1 biology)
- DCC (deleted in colorectal cancer) — first mammalian substrate; ubiquitin-proteasome degradation.
  [PMID:9334332 "DCC was found to be ubiquitinated and the Sina/Siah proteins regulated its expression"]
- beta-catenin (CTNNB1) — Siah1 mediates a p53-inducible, GSK3beta/beta-TrCP-INDEPENDENT
  beta-catenin degradation pathway via APC; part of a multiprotein E3 complex with SIP/CACYBP,
  SKP1, Ebi (TBL1X). [PMID:11389840; PMID:16085652 "Siah1 is the central component of a multiprotein
  E3 ubiquitin ligase complex that targets beta-catenin for destruction in response to p53 activation"]
  -> beta-catenin destruction complex (GO:0030877) part_of [PMID:16085652].
- AXIN1 — Wnt-induced degradation; SIAH1/2 mediate Wnt-induced Axin degradation, a feed-forward
  mechanism to sustain Wnt/beta-catenin signaling. NOTE: this is POSITIVE regulation of canonical Wnt
  (degrading Axin promotes signaling), distinct from the beta-catenin-degrading (negative) role above.
  [PMID:28546513 "identify SIAH1/2 (SIAH) as the E3 ligase mediating Wnt-induced Axin degradation...
  important feed-forward mechanism to achieve sustained Wnt/β-catenin signaling"]
- De novo SIAH1 variants -> developmental delay; also affect Wnt. [PMID:32430360]
- alpha-synuclein (SNCA) monoubiquitylation + synphilin-1 (SNCAIP) ubiquitination -> Lewy body /
  inclusion formation; relevant to Parkinson disease. SIAH activity inhibited by synphilin-1A.
  [PMID:19224863 "SIAH is a ubiquitin-ligase that ubiquitylates alpha-synuclein and synphilin-1
  and is present in Lewy bodies"]. Also Reactome SIAH1 ubiquitinates SNCA/SNCAIP.
- XIAP — ARTS (SEPT4) bridges SIAH1 to XIAP for degradation -> promotes apoptosis (intrinsic).
  [PMID:21185211 "ARTS interacts with the E3 ligase Siah-1...to induce ubiquitination and
  degradation of XIAP...promoting cell death"]
- HIPK2 — constitutive degradation; DAZAP2 promotes SIAH1-mediated HIPK2 ubiquitination/degradation;
  DNA-damage context (p53 response). [PMID:33591310 "DAZAP2 stimulates HIPK2 polyubiquitination and
  degradation through interplay with the ubiquitin ligase SIAH1"]
- Jade-1 (PHF17) — ubiquitination regulated by polycystin-1; "Jade-1 ubiquitination was mediated by
  Siah-1". [PMID:23001567]
- BOB.1/OBF.1 (POU2AF1) stability regulated by SIAH. [PMID:11483518]
- HBx (hepatitis B X protein) poly-ubiquitylation/degradation. [PMID:21878328]
- EGLN2/EGLN3 (PHD prolyl hydroxylases) — degraded by SIAH1/2 under UPR/hypoxia, stabilizing ATF4
  (and indirectly HIF). [UniProt FUNCTION, By similarity] — hypoxia link.
- Many others: ELL2, MYB, PML, RBBP8, FLT3, KLF10/TIEG1, NUMB, BAG1, KIF22, SYP [UniProt].

## Subcellular location
- Predominantly cytoplasmic; partially nuclear. [UniProt SUBCELLULAR LOCATION: Cytoplasm. Nucleus.]
- Cytoplasm/cytosol is the active compartment (is_active_in cytoplasm, IBA). Nuclear pool real
  (HIPK2, transcription-factor substrates). Nucleoplasm IDA from HPA (GO_REF:0000052).

## Apoptosis / tumor suppression / nervous system
- p53-inducible; originally identified in apoptosis and tumor suppression [UniProt ref 8799150].
- Promotes apoptosis (intrinsic pathway via XIAP; POSH/JNK). [PMID:21185211; PMID:16230351 POSH-JNK]
- Nervous system development / axon guidance via DCC regulation. [PMID:9334332; PMID:9403064]

## Annotation-call reasoning
- Core MF: ubiquitin protein ligase activity (GO:0061630) / ubiquitin-protein transferase
  (GO:0004842) — genuine RING E3, catalytic. ACCEPT.
- ubiquitin conjugating enzyme binding (GO:0031624) — ACCEPT (E2 binding is core to RING mechanism).
- zinc ion binding (GO:0008270) — ACCEPT (RING + Zn fingers; structurally demonstrated).
- proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161) — ACCEPT core BP.
- cytoplasm/cytosol — ACCEPT (active site). nucleus/nucleoplasm — KEEP_AS_NON_CORE (real secondary).
- canonical Wnt signaling (GO:0060070) — KEEP_AS_NON_CORE (downstream pathway; AXIN1 substrate).
- apoptosis terms — KEEP_AS_NON_CORE (downstream processes of substrate degradation).
- amyloid fibril formation (GO:1990000) — Reactome/ARBA: alpha-synuclein context; KEEP_AS_NON_CORE
  (this is the substrate's aggregation behavior, not SIAH1's intrinsic function). Borderline
  over-annotation but Reactome TAS curates SIAH1 in the SNCA amyloid pathway.
- protein binding (GO:0005515) bare IPI — KEEP_AS_NON_CORE per curation guidelines.
- identical protein binding (GO:0042802) — ACCEPT/KEEP_AS_NON_CORE: SIAH1 homodimerizes (real),
  but it is a specific informative interaction; keep as non-core (dimerization supports function).
- nervous system development / axon guidance / morphogenesis — KEEP_AS_NON_CORE (pleiotropic dev roles).
- protein destabilization (GO:0031648) — KEEP_AS_NON_CORE (consequence of degradation activity).
- neuron apoptotic process — KEEP_AS_NON_CORE.
</content>
