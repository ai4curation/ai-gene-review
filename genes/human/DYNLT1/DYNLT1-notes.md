# DYNLT1 (Tctex-1) — curation notes

## Deep research status

- First run (`--fallback perplexity-lite`) stopped (falcon 600 s default timeout; perplexity-lite
  unavailable). Re-run with `--timeout 2400`; outcome recorded at the end. Review based on cached
  literature.

## Identity

- UniProt P63172, dynein light chain Tctex-type 1 (TCTEX1); DYNLT family with DYNLT3 (rp3) and the
  divergent DYNLT2B (TCTEX1D2, "Tctex-2"). Also identical to AGS2 (receptor-independent activator
  of G protein signaling) [PMID:17491591].

## Dynein light chain

- Recombinant human dynein-1 reconstitution includes DYNLT1
  [PMID:24986880 "We co-expressed genes for all six dynein subunits—DYNC1H1 (DHC), DYNC1I2 (DIC), DYNC1LI2 (DLIC), DYNLT1 (Tctex), DYNLRB1 (Robl) and DYNLL1 (LC8)—from a single baculovirus in Sf9 cells."].
- Homo/heterodimers; homodimers bind all intermediate chains
  [PMID:17965411 "Yeast two-hybrid and co-immunoprecipitation assays demonstrate that both members of the DYNLT family are capable of forming homodimers and heterodimers."];
  [PMID:17965411 "In addition, both homodimers of the DYNLT family bind all six intermediate chain isoforms."];
  DYNLT associates exclusively with dynein [PMID:17965411 "The DYNLT light chains, but not DYNLL light chains, associate exclusively with the dynein complex."].
- Dynein-2: co-isolates with WDR34 [PMID:25205765 "Here, all known dynein-1 light chain isoforms (LC8-1 and LC8-2, Tctex-1 and Tctex-3, and roadblock-1 and roadblock-2) were identified in association with mGFP–WDR34."];
  in the dynein-2 structure as TCTEX-TCTEX1D2 dimer [PMID:31451806 "4) to the TCTEX-TCTEX1D2 dimer identified in biochemical studies38."].
- Cilium length: [PMID:21700358 "We identify the dynein light chain Tctex-1 as a key modulator of cilia length control; depletion of Tctex-1 results in longer cilia"];
  [PMID:21700358 "Our data show that Tctex-1 is a key regulator of cilia length and most likely functions as part of dynein-2."].

## Dynein-independent functions

- Gbetagamma effector, neurite outgrowth
  [PMID:17491591 "Tctex-1, a light-chain component of the cytoplasmic dynein motor complex, can function independently of dynein to regulate multiple steps in neuronal development."];
  [PMID:17491591 "Furthermore, Gbeta competes with the dynein intermediate chain for binding to Tctex-1, regulating assembly of Tctex-1 into the dynein motor complex."].
- Rab3D binding in osteoclasts [PMID:21262767 "We demonstrate that Tctex-1 binds specifically to Rab3D in a GTP-dependent manner and co-occupies Rab3D-bearing vesicles in bone-resorbing osteoclasts."].
- Viral Gag targeting (M-PMV) [PMID:18647839].

## Ciliary resorption (module role)

- [PMID:21394082 "We show that Tctex-1 phosphorylated at Thr 94 is recruited to ciliary transition zones before S-phase entry and has a pivotal role in both ciliary disassembly and cell cycle progression."]
- [PMID:21394082 "Exogenously adding a phospho-mimic Tctex-1(T94E) mutant accelerates cilium disassembly and S-phase entry."]
- Mechanism involves actin dynamics [PMID:21394082 "Mechanistic studies show the involvement of actin dynamics in Tctex-1-regulated cilium resorption."].
- Upstream: IGF-1R -> AGS3-regulated Gbetagamma -> recruits pT94-Tctex-1 to the transition zone
  [PMID:23954591 "At the base of the cilium, phosphorylated IGF-1R activates an AGS3-regulated Gβγ signaling pathway that subsequently recruits phospho(T94)Tctex-1 to the transition zone."].
- Note the apparent paradox: Tctex-1 depletion lengthens cilia [PMID:21700358], consistent with
  both a dynein-2 role in length control and the resorption role. The two papers use different
  readouts (steady-state length vs. serum-induced resorption).
- Comparator check for NEW GO:0061523: NEDD9 (AURKA activator), AURKA and HDAC6 carry GO:0061523
  in human GOA. Phospho-Tctex-1 is a comparable signalling effector acting at the ciliary base, so
  the term fits the existing convention for regulators that execute part of the resorption
  programme. Evidence is the 2011 abstract (cached abstract-only) plus Yeh et al. 2013 (full text).

## Curation decisions summary

- ACCEPT core: cytoplasmic dynein complex, dynein complex, dynein intermediate chain binding,
  microtubule-based movement (as dynein subunit), intraciliary retrograde transport (dynein-2),
  cilium, cytoplasm/cytosol.
- MODIFY: identical protein binding -> protein homodimerization activity; protein binding with
  DYNLT3/DYNLT2B -> protein heterodimerization activity.
- REMOVE: other generic protein binding rows; `host cell` (a symbiont-side term mis-propagated to a
  host protein).
- MARK_AS_OVER_ANNOTATED: Reactome neutrophil-degranulation extracellular/granule lumen rows.
- UNDECIDED: male germ cell nucleus (NAS, basis not visible), positive regulation of SAC
  (NAS from an LIC1 paper; the sign looks inverted relative to dynein's role in checkpoint silencing).
- KEEP_AS_NON_CORE: spindle orientation, GPCR signaling regulation, negative regulation of
  neurogenesis, viral protein transport, Rab3D/secretory vesicle, Golgi, spindle, cytoplasmic
  microtubule, positive regulation of intracellular transport.
- NEW: GO:0061523 cilium disassembly (IMP, PMID:21394082).

## HPA cilium atlas vs module role

- HPA v25: no cilia/centrosome call; main locations Acrosome; Cytosol. No HPA-sourced GOA rows.
  The HPA atlas paper (PMID:41005307) is cached as metadata only.
- Module role (stage 7: "Tctex-1; resorption"). The primary literature supports this: phospho-T94
  Tctex-1 at the transition zone promotes ciliary resorption. The absence of a transition-zone call
  in HPA is not evidence against the role, because the active pool is a phospho-specific
  sub-population detected with a phospho-T94 antibody, while total Tctex-1 is mostly cytosolic.
- core_functions lists the dynein light chain role (dynein-1 and dynein-2) first, because it is the
  constitutive, best-supported function, and the resorption role second. The module should treat
  DYNLT1 as pleiotropic: the resorption function is a regulated activity (possibly dynein-independent, not established) of a
  phospho-pool, and dynein-2 membership also links it to retrograde IFT and length control.
