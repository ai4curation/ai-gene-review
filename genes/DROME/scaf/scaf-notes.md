# scaf (Scarface, Q7K5M0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. Sources: cached PMIDs 20379222, 20530545
(abstract only), 25737837, 30367934, 42531335, 28628612 (full text), the
UniProt record, the FlyBase report, PAINT files, and a new triad check.

### Identity
- Q7K5M0 is the canonical, reviewed (Swiss-Prot) 655-aa Scarface product of
  FBgn0033033 (CG11066), not a fragment, isoform or alternative model. Two
  RefSeq/FlyBase transcripts (FBpp0085396, FBpp0085397) map to this entry.
- Domains: signal peptide 1-24; disordered Pro/Thr-rich region; Scarface-type
  CLIP domain (Pfam PF18399 CLIP_SPH_Scar, 343-407); peptidase S1 domain 421-644.

### Catalytic status (scaf-bioinformatics/RESULTS.md)
- Alignment to bovine chymotrypsinogen A with active psh (Q9VWU1) as control:
  His57 -> Ser465, Asp102 retained (D515), Gly193 -> F597, Ser195 motif
  GDSGGP -> FDVGSA. psh retains all four. Supports the NOT peptidase rows and
  the REMOVE of the IEA proteolysis row.
- Rousset 2010 abstract: [PMID:20530545 "Some proteins of this family, like Scaf, bear an inactive catalytic site"].

### Function
- JNK target and negative-feedback antagonist: [PMID:20530545 "We finally demonstrate that scaf acts as an antagonist by negatively regulating JNK activity."]
  Added NEW GO:0046329 negative regulation of JNK cascade (IMP, PMID:20530545).
- Egfr represses scaf in the lateral epidermis; scaf suppresses dpp/pMad:
  [PMID:28628612 "These observations support a role for Scaf as a suppressor of Dpp signaling in the dorsal ectoderm."]
- Laminin A polarity, germ-band retraction, dorsal closure (PMID:20379222);
  thorax closure (PMID:25737837); radiation-induced hinge-to-pouch fate change
  (PMID:42531335). All kept.

### Evolution / placement
- No characterised ortholog outside Drosophila: DIOPT gives only 1-of-14 scores
  to vertebrate S1 proteases. Scarface-type CLIP domain (PF18399) proteins exist
  across insects (mosquito, beetles, Lepidoptera, Hymenoptera), all
  uncharacterised, and their PANTHER placements scatter across PTHR24250,
  PTHR24252, PTHR24256 and PTHR24258.
- UniProt: PTHR24250:SF27 (ELASTASE 2 LIKE). The PTHR24250 family review records
  that PANTHER 19.0 places Q7K5M0 in PTHR24260:SF145 and leaves Scaf outside
  structured membership. The SF27 "elastase" label is not evidence of activity.
- IBA source PTN000667087 (taxon:1206794, Ecdysozoa) carries extracellular region
  and innate immune response. Immune donors: psh, grass, SPE, modSP, MP1,
  FBgn0030051, FBgn0052382, FBgn0052383 and Anopheles CLIPA8 (A0A1S4H5S2), an
  inactive CLIP-SPH. Because an SPH is among the donors, triad loss does not
  exclude Scaf; no Scaf immune evidence exists. Innate immune response kept
  UNDECIDED.
- Relative chosen for next review: Anopheles gambiae CLIPA8 (A0A1S4H5S2), the
  experimentally characterised noncatalytic CLIP-SPH donor at Scaf's PAINT node.
  It is a family member at the same node, not an ortholog; the tree within
  PTN000667087 was not resolved. No review exists in the repo.

### Fixes to the previous review
- Three supporting_text quotes pointed at sentences no longer present in
  interpro/panther/PTHR24250/PTHR24250-review.yaml; replaced with UniProt,
  PMID:20530545 and RESULTS.md quotes. Reference kept with a note.
- Description rewritten to include JNK antagonism, Egfr/Dpp link and domain
  architecture; core functions split into JNK antagonism and epithelial
  morphogenesis.

### Modules
- Related only: modules/jnk_cascade.yaml, modules/dmel_eiger_tnf_signaling.yaml.
  Scaf is not a part of either.
