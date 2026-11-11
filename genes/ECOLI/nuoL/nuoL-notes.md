# nuoL (E. coli K-12, P33607) notes

## 2026-10-23 / 2026-11-01 review session

Deep-research providers are unavailable in this environment (no API keys), so the
literature was reviewed by hand from cached `publications/PMID_*.md` files and the
UniProt record. Abstract-only experimental papers are deferred to the curator.

Key evidence:
- NuoL deletion halves pumping: [PMID:21417432 "Our data suggest that the H+/2e-
  stoichiometry of the ΔNuoL variant is 2"]; its C-terminal helix is needed for
  energy transmission (same paper).
- Pumped protons exit via NuoL: [PMID:36104567 "This mechanism explains why protons exit
  exclusively from the NuoL subunit and is supported by our mutagenesis data."]
- Antiporter-like (Mrp) fold: [PMID:36920092 "ALS share a cation/proton antiporter MRP
  fold"]; [PMID:23417064 "are homologous to each other and to Na+/H+ antiporter complex
  (Mrp) subunits"]; [PMID:12460669 "these polypeptides (NuoL/ND5, NuoM/ND4, NuoN/ND2) are
  most likely core components of the proton pumping mechanism"]
- NuoL/M/N likely share a pumping mechanism: [PMID:23864658 "It seems likely that NuoL,
  NuoM, and NuoN pump protons by a similar mechanism."]

Decisions:
- GO:0008137 and GO:0015990 ACCEPT (core); GO:0003954 MODIFY to GO:0008137; GO:0030964
  MODIFY to GO:0045271; GO:0016020 MODIFY to GO:0005886.
- No separate proton transmembrane transporter activity (GO:0015078) was added: it is an
  is_a ancestor of GO:0008137, which is already the core contributed activity.
