# TTBK2 review notes

## 2026-10-03: sources and scope

- GOA snapshot 65 rows; UniProt Q6IQ55. All GOA PMIDs cached (PMID:23141541 abstract-only).
- Additional papers: PMID:31455668 (CEP83 substrate), PMID:24982133, PMID:25297623, PMID:30532139 (SCA11 alleles, cilia stability), PMID:36322399 and PMID:31934864 (cilium stability, Purkinje neurons; cached, not cited in YAML).
- Deep research: first falcon run (600 s) timed out; second run with `--timeout 2400` was killed (exit 137); third run succeeded (`TTBK2-deep-research-falcon.md`).

## Functional synthesis

- TTBK2 is a dedicated initiator of ciliogenesis [PMID:23141541 "TTBK2 acts at the distal end of the basal body, where it promotes the removal of CP110, which caps the mother centriole, and promotes recruitment of IFT proteins, which build the ciliary axoneme."]
- Kinase specificity [PMID:21548880 "In the present study we first assess the substrate specificity of TTBK2 and demonstrate that it has an unusual preference for a phosphotyrosine residue at the +2 position relative to the phosphorylation site."]; SCA11 truncations reduce activity and increase nuclear localization.
- Recruitment by CEP164 is essential [PMID:25297623 "Using TTBK2 variants that contained mutations in the SxIP or proline-rich motifs, we obtained evidence that Cep164, but not EB1, is essential for centriolar localization of TTBK2."]
- Substrates linked to cap removal: MPHOSPH9 [PMID:30375385 "After phosphorylation by Tau Tubulin Kinase 2 (TTBK2) at the beginning of ciliogenesis, MPP9 is targeted for degradation via the ubiquitin-proteasome system, which facilitates the removal of CP110 and CEP97 from the distal end of the mother centriole."] and CEP83 [PMID:31455668 "TTBK2-dependent CEP83 phosphorylation is important for early ciliogenesis steps, including ciliary vesicle docking and CP110 removal."]
- Post-initiation roles in cilium length, SMO trafficking and stability [PMID:30532139 "Our studies have also revealed new functions for TTBK2 after cilia initiation in the control of cilia length, trafficking of a subset of SHH pathway components, including Smoothened (SMO), and cilia stability."]
- Non-ciliary: EB1/3-dependent +TIP that phosphorylates KIF2A [PMID:26323690 "These findings indicate that TTBK2 with EB1/3 phosphorylates KIF2A and antagonizes KIF2A-induced depolymerization at MT plus ends for cell migration."]
- Tau: kinase named for in vitro tau phosphorylation; physiological relevance unknown [PMID:21548880 "Whether endogenous TTBK1 and/or TTBK2 regulate phosphorylation of endogenous tau has not been established."]

- Deep research adds: CP110 itself is not an established TTBK2 substrate [file:human/TTBK2/TTBK2-deep-research-falcon.md "CP110 removal is a TTBK2-dependent outcome, not evidence that CP110 itself is a confirmed direct TTBK2 substrate."]; Bernatik et al. 2020 mapped TTBK2 sites on CEP164 (T1309, S1317, S1346, S1347, S1443) and biochemically on CEP89, CCDC92, Rabin8 and DVL3, and found that the +2 phosphotyrosine preference seen with truncated kinase is not the dominant motif in physiological substrates; HUWE1 ubiquitinates TTBK2 to promote cilium disassembly (Lin 2024); neuronal tau S422 is phosphorylated mainly by TTBK1 [file:human/TTBK2/TTBK2-deep-research-falcon.md "phosphorylation is driven principally by TTBK1, not TTBK2"], which supports keeping tau kinase activity non-core. These extra papers were not cached or annotated.

## Annotation decisions

- Accept kinase activity (S/T, serine), ATP binding, peptidyl-serine phosphorylation, cilium assembly, centriole/basal body/transition zone/ciliary base/cilium/cytoplasm.
- Microtubule dynamics, cell migration, kinesin binding, cerebellar development, tau kinase activity, nucleus, cytosol: non-core.
- Signal transduction (IBA), smoothened signaling (IEA/ISS), tau protein binding (NAS), microtubule plus-end binding (TAS; binding is via EBs), extracellular region (tear proteomics): over-annotated.
- All six bare protein binding rows: remove.

## HPA cilium atlas vs module role

- Module role: "kinase removing CP110-CEP97 cap" (function GO:0004674, recruited by CEP164).
- HPA v25: Primary cilium (Approved); Primary cilium transition zone (Approved); Basal body (Approved); main locations cytosol and microtubules.
- Comparison: HPA calls (all Approved) match the ciliary-base location, and the microtubule main location matches the EB1/3-dependent +TIP behaviour; the cytosol call matches the soluble pool recruited by CEP164. The kinase activity term in the module is right. One wording point: TTBK2 does not remove the cap itself. It phosphorylates MPHOSPH9 (leading to its degradation) and CEP83, and these events lead to CP110-CEP97 release. A more accurate module role would be "kinase that triggers CP110-CEP97 cap removal". core_functions are written accordingly.
