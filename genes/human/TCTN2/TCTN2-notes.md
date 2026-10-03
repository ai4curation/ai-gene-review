# TCTN2 (Tectonic-2, Q96GX1) review notes

## Deep research status
- `just deep-research-falcon human TCTN2` was run first with `--fallback perplexity-lite` (default 600 s timeout; perplexity-lite is not available in this environment), then rerun with `--timeout 2400`. See the bottom of this file for the outcome. The review below rests on the cached primary literature in `publications/`.

## Protein
- Single-pass type I membrane protein: signal peptide 1-25, large luminal/extracellular tectonic domain (26-668), TM 669-689, short cytoplasmic tail (UniProt).
- Tectonic family (TCTN1-3). MKS8 and JBTS24 disease gene [PMID:21462283 "we describe the identification of a novel MKS locus MKS8 that we map to TCTN2"].

## Complex membership and location
- Part of the Tctn1/MKS transition-zone complex [PMID:21725307 "Tctn1 forms a complex with multiple ciliopathy proteins associated with Meckel and Joubert syndromes, including Mks1, Tmem216, Tmem67, Cep290, B9d1, Tctn2 and Cc2d2a."].
- Co-purifies with Tmem231 [PMID:25869670 "Tmem231 interacts with multiple other components of the MKS complex, including Mks1, Tctn1, Tctn2, Tctn3, Cc2d2a (Mks6), and Tmem17"].
- In the TZ, near the ciliary membrane [PMID:29866362 "TMEM67 and TCTN2 are close to the ciliary membrane, whereas MKS1 is likely in between"].

## Function
- Required for ciliogenesis in mouse (tissue-dependent) [PMID:21565611 "Tctn2 was required for ciliogenesis in isolated cells and in vivo, consistent with TCTN2 being a ciliopathy gene"]. But some null MEFs ciliate [PMID:28401750 "For instance, TCNT1 or TCTN2 null MEFS (mouse embryonic fibroblasts) can ciliate"].
- Tissue-specific defects in ciliogenesis and ciliary membrane composition [PMID:21725307 "Like Tctn1, loss of Tctn2, Tmem67 or Cc2d2a causes tissue-specific defects in ciliogenesis and ciliary membrane composition."].
- Human RPE1 TCTN2 KO [PMID:29866362 "We found that TCTN2 depletion resulted in partial TZ damage, loss of ciliary membrane proteins, leakage of intraflagellar transport protein IFT88 toward the basal body lumen, and cilium shortening and curving."]. MKS module assembly [PMID:29866362 "Among the ciliated population, TMEM67 and MKS1 were absent in TCTN2 −/− cells, whereas RPGRIP1L, NPHP4, and CEP290 remained in their ciliary base localizations"].
- Hedgehog signalling [PMID:21565611 "Tctn2-/- cells fail to respond to Hh agonists"]. This is indirect, via ciliary gating.

## Curation decisions
- TZ, MKS complex, cilium assembly, protein localization to TZ: ACCEPT (core).
- Smoothened signalling (IBA/IEA/ISS): KEEP_AS_NON_CORE (downstream of the gate).
- Ciliary membrane (Reactome TAS): ACCEPT (the TZ membrane is a ciliary membrane domain; TCTN2 TM segment sits there).
- NEW: GO:1905349 ciliary transition zone assembly (IMP, PMID:29866362). TCTN2 is a structural TZ constituent needed to incorporate TMEM67/MKS1 (scaffold case). GO:1905349 replaces the obsoleted GO:0097711 and has only ~9 human/mouse annotations (CEP290, CCDC66, DZIP1L, RAB3IP; QuickGO query 2026-10), so the absence for MKS subunits is a sparse-term gap rather than a convention.

## HPA cilium atlas vs module role
- HPA (member_evidence.md): TCTN2 "Primary cilium transition zone (A)" (Approved); HPA main locations Golgi apparatus; Microtubules. The Hansen et al. 2025 atlas [PMID:41005307 "Our analysis identified the subciliary locations of 715 proteins across three cell lines, examining 128,156 individual cilia."] thus places TCTN2 at the TZ with an Approved grade. It is one of the few MKS-module members whose HPA call names the TZ sub-compartment specifically.
- Module role: MKS module component (ciliary diffusion barrier; process ciliary transition zone assembly; location ciliary transition zone). The HPA call agrees with the module role and with the literature. The Golgi pool is expected for a glycosylated single-pass membrane protein in transit. GOA has no HPA (GO_REF:0000052) row for TCTN2; the TZ IDA from HPA could be added by GOA.
- core_functions agree with the module (MKS complex, TZ, TZ assembly, protein localization to TZ).

## Deep research outcome
- Falcon succeeded on the `--timeout 2400` rerun (`TCTN2-deep-research-falcon.md`). Its synthesis (MKS/NPHP-module transition-zone organizer; non-enzymatic; ciliary gate/composition role) matches the conclusions above. No annotation decisions changed after reading it.
