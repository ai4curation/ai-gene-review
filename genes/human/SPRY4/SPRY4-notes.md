# SPRY4 (human, Q9C004) curation notes

## 2026-10-01 initial review

Context: reviewed as a negative-feedback regulator of RTK/Ras-ERK signalling for the
ERK cascade and FGFR signalling modules (SPRY is currently outside the fgfr_signaling
module boundary as a feedback regulator).

### Core biology with provenance

- Original human characterisation: SPRY4 suppresses insulin- and EGF-receptor MAPK
  signalling but not RasV12-driven MAPK activation; acts at or upstream of Ras
  [PMID:12027893 "This new sprouty orthologue can suppress the insulin- and EGF-receptor transduced MAP kinase signaling pathway, but fails to inhibit MAP kinase activation by constitutively active V12 ras"]
  [PMID:12027893 "Hspry4 appears to impair the formation of active GTP-ras and exert its activity at the level of wild-type ras or upstream thereof"]
- RAF1 arm: mammalian Spry4 binds RAF1 via the C-terminal cysteine-rich domain; binding
  is necessary for inhibition; blocks VEGF-induced Ras-independent RAF1 activation but
  not EGF-induced Ras-dependent activation
  [PMID:12717443 "Sprouty4 binds to Raf1 through its carboxy-terminal cysteine-rich domain, and this binding is necessary for the inhibitory activity of Sprouty4"]
  (abstract only; species of construct not stated beyond "mammalian").
- SOS1/GRB2 arm: SPRY4 associates with SOS1 (SPRY1 with GRB2); SPRY1/SPRY4 hetero-oligomer
  suppresses GRB2-SOS1 association with FRS2
  [PMID:16339969 "Sprouty1 specifically interacts with Grb2, whereas Sprouty4 interacts with Sos1"]
  (abstract only; co-IP based, directness not shown).
- Tyr75 phosphorylation required for FGF-ERK inhibition
  [PMID:15584898 "expression of human Spry4 suppressed FGF-induced ERK1/2 MAP kinase activation, as measured by phospho-ERK immunoblotting, but Spry4(Y75A) had the opposite effect, enhancing ERK activation"]
- Feedback: Sprouty expression is ERK-dependent
  [PMID:16339969 "Mammalian cells express four Sprouty isoforms (Sprouty1-4) in an ERK-dependent manner"];
  SPRY4 induced by FGFR2 activation and suppresses FGFR-induced ERK phosphorylation in PHCC cells
  [PMID:31761616 "SPRY4 suppressed FGFR-induced proliferation and migration by inhibiting ERK phosphorylation"]
- TESK1 arm (ERK-independent): GST-SPRY4 inhibits TESK1 kinase activity in vitro, suppresses
  integrin-mediated spreading
  [PMID:15584898 "we show that Spry4 inhibits the kinase activity of TESK1 by binding to it through the C-terminal cysteine-rich region"]
  [PMID:15584898 "the inhibition of cell spreading by Spry4 is caused by a mechanism independent of its inhibitory activity on the ERK activation pathway"]
- Context dependence: SPRY4 knockdown did not change ERK phosphorylation in HT1080 p53KO
  cells; SPRY4 mediates MDM2 effects on focal adhesions/RhoA
  [PMID:39164253 "Surprisingly, Spry4 knockdown did not affect ERK phosphorylation in HT1080 p53KO cells"]
- Localization: cytoplasmic vesicles with TESK1; no substantial PM translocation in human study
  [PMID:12027893 "The two proteins colocalize in apparent cytoplasmic vesicles and do not show substantial translocation to the plasma membrane upon receptor tyrosine kinase stimulation"];
  membrane ruffles on EGF by similarity to mouse (UniProt).

### Decisions

- No NOT annotations in GOA for SPRY4.
- 44 `protein binding` IPI rows: TESK1 x2 -> MODIFY (GO:0030291 for PMID:15584898;
  GO:0019901 for PMID:12027893), CBL -> MODIFY GO:0031625; 41 high-throughput rows -> REMOVE
  (uninformative; not a claim the interactions are false).
- IBA rows for FGFR / Ras / ERK negative regulation and kinase inhibitor activity ACCEPTed;
  EGFR row KEEP_AS_NON_CORE (context-dependent; PMID:12717443 shows no effect on EGF-induced
  Ras-dependent RAF1 activation).
- NEW: GO:0030948 negative regulation of VEGFR signalling (PMID:12717443). SPRY4 performs the
  inhibitory step itself (RAF1 binding), so participation test is met.
- MF for the Ras-ERK arm: GO:0004860 protein kinase inhibitor activity (RAF1 binding,
  matches PAINT IBA). Open question whether this is true catalytic inhibition vs
  sequestration (GO:0140311); SOS1 arm is sequestration-like but support is co-IP only.
- PIP2-binding / PLCgamma shielding reported only in review [PMID:38686189]; not annotated.
