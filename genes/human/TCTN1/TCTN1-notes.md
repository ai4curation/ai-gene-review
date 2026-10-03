# TCTN1 curation notes

## 2026-10-03 — initial review (primary cilium life cycle module, stage 3 transition zone)

Human TCTN1 = UniProt Q2MV58 (Tectonic-1). 17 GOA annotations seeded; all reviewed.

### Deep research status

`just deep-research-falcon human TCTN1` was run first with `--fallback perplexity-lite` (falcon timed out at
600 s; the perplexity provider is not available in this environment) and then re-run with `--timeout 2400`
(see the section at the end of this file for the outcome). The review was built from the cached primary literature
listed below.

### Biology

- Founding member of the tectonic family of "secreted and transmembrane" proteins; mouse Tectonic regulates Hedgehog
  signalling downstream of Smo and Rab23 [PMID:16357211 "founding member of a previously undescribed family of
  evolutionarily conserved secreted and transmembrane proteins"; "mouse Tectonic is required for formation of the most
  ventral cell types and for full Hedgehog (Hh) pathway activation"].
- TCTN1 has a signal peptide (1-22) and no transmembrane segment (UniProt). UniProt notes the full-length protein might
  not be secreted.
- Tctn1 is part of the MKS/tectonic transition-zone complex [PMID:21725307 "Tctn1 forms a complex with multiple
  ciliopathy proteins associated with Meckel and Joubert syndromes, including Mks1, Tmem216, Tmem67, Cep290, B9d1, Tctn2
  and Cc2d2a"; "Components of this complex co-localize at the transition zone, a region between the basal body and
  ciliary axoneme"].
- Tissue-specific ciliogenesis and ciliary membrane composition [PMID:21725307 "found that it is essential for
  ciliogenesis in some, but not all, tissues"; "Cell types that do not require Tctn1 for ciliogenesis require it to
  localize select membrane-associated proteins to the cilium, including Arl13b, AC3, Smoothened and Pkd2"].
- The nine-protein complex is a diffusion barrier [PMID:22179047 "acts as a diffusion barrier to maintain the cilia
  membrane as a compartmentalized signalling organelle"].
- Disease: Joubert syndrome 13 (PMID:21725307).

### Key decisions

- Cytosol (Reactome TAS x3): REMOVE — a signal-peptide secretory-pathway protein cannot be cytosolic; Reactome draws
  the whole MKS complex in cytosol, which is only appropriate for its soluble members (MKS1, B9D1, B9D2).
- Extracellular region / membrane IEA: KEEP_AS_NON_CORE (topologically luminal/extracellular-facing; generic).
- TZ, MKS complex, cilium assembly, protein localization to TZ: ACCEPT.
- No NEW terms. Hedgehog-signalling phenotypes are downstream of ciliary gating; not proposed as annotations.

## HPA cilium atlas vs module role

- HPA (v25 / Hansen et al. 2025, PMID:41005307) calls TCTN1 at the **primary cilium (Approved)**; HPA main locations
  are "Actin filaments; Primary cilium" (projects/HUMAN_PROTEIN_ATLAS/cilium_life_cycle/member_evidence.md). No
  GO_REF:0000052 (HPA) row exists for TCTN1 in GOA.
- Module role: MKS-module transition-zone component (stage 3). The HPA call is consistent: at light-microscope
  resolution the transition zone is part of the cilium, and the Approved grade (not Supported/Enhanced) and lack of a
  sub-ciliary "transition zone" call (which HPA does give for TCTN2) means the atlas neither confirms nor contradicts the
  precise TZ position. The actin-filament signal has no counterpart in the literature and is not used.
- core_functions are consistent with the module role (MKS complex, ciliary transition zone, cilium assembly).
