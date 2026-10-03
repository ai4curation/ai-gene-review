# RPGRIP1L (MKS5/NPHP8/fantom, Q68CZ1) review notes

## Deep research status
- Falcon was run with `--fallback perplexity-lite` (600 s; fallback not available here), then rerun with `--timeout 2400`; the outcome is at the bottom of this file. The review rests on cached primary literature.

## Key literature
- Disease genes: JBTS7/MKS5 [PMID:17558409 "we identified missense and truncating mutations in RPGRIP1L (KIAA1005) in both CORS and MKS"]; JBTS [PMID:17558407 "We show that RPGRIP1L interacts with nephrocystin-4 and that mutations in the gene encoding nephrocystin-4 (NPHP4) that are known to cause SLSN disrupt this interaction."]; COACH3.
- Basal body/centrosome [PMID:17558409 "RPGRIP1L colocalizes at the basal body and centrosomes with the protein products of both NPHP6 and NPHP4"].
- Assembly factor (worm) [PMID:26392567 "MKS-5 ... functions as an assembly factor"]; [PMID:26392567 "This activity is needed to form TZ ultrastructure, which comprises Y-shaped axoneme-to-membrane connectors."]; CIZE [PMID:26392567 "MKS-5 establishes a ciliary zone of exclusion (CIZE) at the TZ that confines signalling proteins"].
- Foundation of both assembly pathways [PMID:26982032 "MKS-5 (Rpgrip1L/Rpgrip1 orthologue) represents the foundation of two distinct assembly pathways for the MKS and NPHP modules"].
- Mouse/vertebrate gating [PMID:33625872 "Rpgrip1l governs ciliary gating by ensuring the proper amount of Cep290 at the vertebrate TZ"]; [PMID:33625872 "Rpgrip1l deficiency leads to a reduced amount of Cep290, Nphp1, Nphp4, and Invs at the TZ"]; [PMID:33625872 "Most likely, Rpgrip1l functions as a TZ scaffold for Nphp1 but not for Cep290."].
- Ciliary proteasome [PMID:26150391 "the ciliary proteasome is regulated by Rpgrip1l via its interaction with Psmd2 at the ciliary TZ"].
- RPGR complex, retinal modifier [PMID:19430481 "Co-transfection of COS-1 cells followed by co-IP demonstrated that Xpress-tagged RPGR and GFP-RPGRIP1L proteins are part of the same complex"].
- TBXA2R [PMID:19464661 "KIAA1005/TPIP is a novel TP interacting protein that regulates TP-mediated signal transduction negatively"]. Single overexpression study, kept as non-core.

## Curation decisions (35 GOA rows + 1 NEW)
- 7 protein binding: REMOVE (NPHP4 and RPGR interactions captured by complex/location terms).
- TZ, basal body, cilium, connecting cilium, NPHP complex, protein localization to TZ, non-motile cilium assembly: ACCEPT.
- Cytoplasm/cytosol (incl. HPA GO_REF:0000052), centrosome, junctions, axoneme, TBXA2R binding (IPI and IBA), negative regulation of GPCR signalling, regulation of signal transduction: KEEP_AS_NON_CORE.
- NEW GO:1905349 ciliary transition zone assembly (ISS, PMID:26392567). Comparator: CEP290, the other foundational TZ scaffold, carries the term.

## HPA cilium atlas vs module role
- HPA (member_evidence.md): "Primary cilium (S); Basal body (U)" (Supported; Uncertain); HPA main locations Cytosol; Plasma membrane. GOA carries the HPA rows as cilium IDA and cytosol IDA (GO_REF:0000052). Hansen et al. 2025 atlas [PMID:41005307 "We employed antibody-based spatial proteomics to expand the Human Protein Atlas to primary cilia."].
- HPA does not resolve RPGRIP1L to the TZ sub-compartment (no "Primary cilium transition zone" call), whereas the literature places it precisely at the TZ, close to the axoneme and distal to CEP290 (PMID:28401750). The HPA "Primary cilium (S)" call is consistent at lower resolution. The basal body (U) call fits its basal body/TZ position, and the cytosol call matches a known diffuse pool.
- Module role: NPHP module component; "transition zone scaffold"; TZ assembly. The literature strongly supports RPGRIP1L as the foundational TZ assembly factor/scaffold. Its role is in fact broader than the NPHP module: it is upstream of both the MKS and the NPHP modules (and of CEP290), so placing it solely within the NPHP module undersells it. core_functions follow the module's TZ assembly assignment but note this upstream, cross-module role.
