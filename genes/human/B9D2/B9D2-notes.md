# B9D2 curation notes

## 2026-10-03 — initial review (primary cilium life cycle module, stage 3 transition zone)

Human B9D2 (MKSR2) = UniProt Q9BPU9. 56 GOA annotations seeded; all reviewed.

### Deep research status

The first falcon run failed with HTTP 429 (rate limit), perplexity fallback unavailable; re-run with
`--timeout 2400` (outcome recorded at the end of this file). Review based on cached primary literature.

### Biology

- Central bridge of the MKS1–B9D2–B9D1 complex [PMID:32726168 "B9D2 interacts directly with MKS1 and B9D1, whereas the
  latter two proteins do not directly interact with each other"; "demonstrate their interdependent localization to the
  TZ"; "Both the MKS1-KO and the B9D2-KO cell lines were moderately compromised with respect to ciliogenesis
  efficiency"; "formation of the B9D protein complex is crucial for creating a diffusion barrier for ciliary membrane
  proteins"].
- Human MKSR proteins localize to basal bodies and cilia; knockdown impairs ciliogenesis [PMID:19208769 "the human
  orthologues also localize to basal bodies, as well as cilia"; "disrupting human MKSR1 or MKSR2 causes ciliogenesis
  defects"].
- Zebrafish B9d2 binds IFT components, supports inversin and opsin transport [PMID:21602787 "IFT particle components,
  and a Meckel-Gruber syndrome 1 (MKS1)-related, B9 domain protein, B9d2, bind each other"; "B9d2, Inversin, and
  Nephrocystin 5 support, in turn, the transport of a cargo protein, Opsin"].
- Diseases: Meckel syndrome 10, JBTS34.

### Key decisions

- 19 protein binding rows: REMOVE (policy). MKS1/B9D1 rows reflect the real bridge interaction captured by MKS complex;
  HuRI binary hits (TLX3, QARS1, P4HA3, VPS25, ALKBH7 etc.) have no functional support.
- 18 cytosol TAS rows: KEEP_AS_NON_CORE. Many derive from Reactome kinetochore/mitosis reactions in which B9D2 is a
  listed component; I found no ciliary-literature support for a kinetochore role (flagged as a question).
- Gamma-tubulin binding (IEA/ISS from mouse, UniProt "by similarity"): UNDECIDED — source experiment not reviewed.
- Nucleus (by similarity; HPA nucleoli), axoneme, centrosome, membrane: KEEP_AS_NON_CORE.
- TZ, basal body, MKS complex, cilium, cilium assembly, protein localization to TZ: ACCEPT.

## HPA cilium atlas vs module role

- HPA: **Basal body (Supported); Centrosome (Uncertain)**; main locations "Golgi apparatus; Nucleoli". GOA has
  GO:0036064 ciliary basal body IDA GO_REF:0000052 (ACCEPTED).
- Module role: MKS-module TZ component (stage 3). Consistent (basal body call = TZ at confocal resolution). The Golgi
  and nucleolar main-location calls are not supported by the ciliary literature and are not used for core functions.
- core_functions follow the module role.
