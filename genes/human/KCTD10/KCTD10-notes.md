# KCTD10 (Q9H3F6) — curation notes

KCTD10 (potassium channel tetramerization domain-containing 10; also **BACURD3**)
is, despite the "potassium channel tetramerization domain" name, **not an ion
channel**. It is the **substrate-recognition subunit of a Cullin-3–RBX1 (CRL3 /
BCR) RING E3 ubiquitin ligase**. Family: BACURD (BTB/POZ adapters for CUL3).

## Core molecular function

- Substrate-specific adapter of a **BCR(BTB-CUL3-RBX1)** E3 ubiquitin ligase
  complex; mediates ubiquitination of multiple substrates for proteasomal or
  lysosomal degradation, or non-degradative (signaling) ubiquitination
  [UniProtKB:Q9H3F6 FUNCTION].
- Binds CUL3 directly via its N-terminal **BTB/POZ** domain and oligomerizes —
  forms a homopentamer and a **5:5 heterodecamer with CUL3** [PMID:28963344].
- GO MF: **ubiquitin-like ligase-substrate adaptor activity** (GO:1990756, IDA
  [PMID:30404837]); complex: **Cul3-RING ubiquitin ligase complex** (GO:0031463).

## Substrate-specific outcomes (pleiotropic; non-core)

- **RHOB** — K63-linked polyubiquitination → lysosomal degradation, preserving
  endothelial barrier function. [PMID:29358211 "RhoB is primarily K63
  polyubiquitinated and subsequently degraded in lysosomes."; "Cullin-3–Rbx1–
  KCTD10–mediated RhoB ubiquitination and degradation preserves endothelial
  barrier function"]
- **CEP97** — proteasomal degradation upon serum starvation, removing the
  CEP97–CP110 complex from the mother centriole to license **primary cilium
  formation**. [PMID:30404837 "Cullin-3-KCTD10-mediated CEP97 degradation
  promotes primary cilium formation."]
- **SLC7A11 (xCT)** — destabilization by polyubiquitination → reduced cystine
  uptake and GSH synthesis → **positive regulation of ferroptosis**. The
  CRL3^KCTD10 E3 is opposed by the deubiquitinase USP18. [PMID:38959043 "KCTD10
  destabilizes SLC7A11 by promoting its polyubiquitylation for subsequent
  proteasome degradation, leading to shortened protein half-life."]
- **TICAM1/TRIF** — K27-linked polyubiquitination at Lys-523, promoting
  TLR3/4-mediated innate immune signaling [UniProtKB FUNCTION, PMID:31511519].
- **KCTD13** — degradative ubiquitination controlling neuronal progenitor
  proliferation (by similarity); **TCEA2** — ubiquitination to resolve
  transcription–replication conflicts [UniProtKB FUNCTION, PMID:41062692].

## Localization, structure, isoforms

- Subcellular: **nucleus** [PMID:19125419] and **cytoplasm** (IDA
  [PMID:30404837]); nucleoplasm by HPA immunofluorescence (GO_REF:0000052).
- Homo-oligomer (BTB-mediated); interacts with CUL3, KCTD13, TNFAIP1, PCNA,
  POLD2. Three splice isoforms (Q9H3F6-1/-2/-3).

## Curation flag — confirmed mis-citation propagated into GOA

The GOA annotation **GO:0160020 positive regulation of ferroptosis (IDA,
PMID:30404837)** cites the **CEP97/ciliogenesis** paper, which contains no
ferroptosis/SLC7A11 content (verified abstract). The correct primary source is
**PMID:38959043** (Gou et al., *PNAS* 2024), which UniProt cites for this exact
function. This is the same mechanically-valid-but-semantically-wrong citation
found in GO-CAM gomodel:69729a3800005900 (USP18/SLC7A11 activity), where
PMID:30404837 was inherited from the (correctly-cited) KCTD10 adaptor activity
onto the antagonist node. The ferroptosis *biology is correct*; only the
reference is wrong. Recorded in the GO:0160020 review with additional_reference_ids.

## Summary

KCTD10's single core molecular function — **CRL3 substrate-recognition adapter** —
is deployed against several unrelated substrates (RHOB, CEP97, SLC7A11, TICAM1,
KCTD13, TCEA2), so its many biological-process annotations (Rho signaling,
ciliogenesis, ferroptosis, endothelial barrier, innate immunity) are
substrate-specific consequences of one ubiquitin-ligase-adapter activity rather
than independent core functions.
