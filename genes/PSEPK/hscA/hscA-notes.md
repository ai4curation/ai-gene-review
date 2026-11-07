# hscA curation notes

- Q88PK4 is the dedicated HscA-family ATP-dependent chaperone encoded in the KT2440 isc locus.
- ATP hydrolysis is mechanistically correct but under-specific. The core molecular function is ATP-dependent protein folding chaperone activity because HscA uses its ATPase cycle with HscB to remodel cluster-bearing IscU.
- No direct KT2440 biochemical study was found in this pass; UniProt/HAMAP and the HscA-specific family assignment support the conserved role.


## Isc comparative-evidence audit (2026-11-07)

HscA (PP_0846) is the specialized Hsp70-family ATPase of the Pseudomonas putida KT2440 Isc system. Its ATPase cycle is stimulated by HscB and is coupled to IscU-dependent iron-sulfur cluster transfer. The conserved mechanism involves nucleotide-dependent scaffold binding and release; homolog studies distinguish this specialized cycle from generic refolding of damaged proteins.

The target remains KT2440; no purified target assay is claimed. Specific curated HAMAP/RuleBase statements or independent NCBIfam/InterPro signatures ground the target inference. ARBA names are not used as proof. All original ordered source payloads are retained. The rows are IEA or historical NEW, not IBA; no donor-count argument, PAINT loss or new evolutionary node placement is asserted.

A genuine Falcon request failed with HTTP 403 authentication/access failure. Existing OpenScientist reports, where present, were preserved; no provider-branded replacement was fabricated. The log is `.cache/module-audit-logs/isc-20261107/psepk-consultation/falcon-hscA.log`.

### Evidence and biological limits

- [PMID:18986169] ATPase-defective HscA fails to stimulate cluster transfer in the characterized homolog system. Quoted support: “A mutant form of HscA lacking ATPase activity, HscA(T212V), was unable to accelerate cluster transfer”.
- [PMID:22782893] E. coli HscA stabilizes disordered IscU and acts as a holdase in the studied conformational cycle. Quoted support: “HscA decreases the D → S rate and binds to and stabilizes the disordered state of IscU”.

### Decisions

- GO:0005524 ATP binding: ACCEPT. ATP binding is required for the HscA nucleotide cycle and is distinct from hydrolysis. It is a core mechanistic property, not peripheral merely because a catalytic term is more informative. Target curated HscA activity supports the conserved binding claim.
- GO:0006457 protein folding: UNDECIDED. The term concerns assistance in formation of correct tertiary structure, not breadth of client range. E. coli HscA preferentially binds disordered IscU and slows its transition to the structured state in PMID22782893. ATP-dependent cluster transfer is well supported, but a target folding endpoint is unresolved. Do not infer generic folding solely from Hsp70 membership or reject all folding solely from specialization.
- GO:0016226 iron-sulfur cluster assembly: ACCEPT. Curated target maturation function and HscA-specific signatures support this role. Homolog ATPase-defective mutant experiments show dependence of cluster transfer on the nucleotide cycle; they are not KT2440 mutant assays.
- GO:0016887 ATP hydrolysis activity: ACCEPT. Hydrolysis drives the specialized scaffold-transfer cycle. The target HAMAP activity and the homolog ATPase-defective mutant support a core ATPase assignment; no generic foldase activity is needed to make the catalytic claim.
- GO:0140662 ATP-dependent protein folding chaperone: NEW (retired historical proposal). Withdraw this inherited proposal from active use: GO0140662 requires ATP-driven assistance to protein folding, whereas the reviewed evidence establishes specialized IscU-state selection and cluster transfer. PMID22782893 finds stabilization of disordered IscU, not a target folding endpoint. This is insufficient precision for an active NEW assertion, not proof that HscA can never assist any folding reaction. The original ISS/file payload and row order are preserved; existing GO0016887 supplies the supported catalytic core.

The existing NEW GO:0140662 proposal is explicitly retired, not deleted or relabeled. ATP hydrolysis GO:0016887 was already present and is now the core catalytic term. The specific IscU-transfer mechanism remains in biological descriptions; absence of a proven target folding endpoint is not universal evidence against all protein-folding activity.
