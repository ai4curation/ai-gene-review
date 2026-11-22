# iscU curation notes

- Q88PK7 is the KT2440 IscU-family scaffold. Its informative molecular function is transient iron-sulfur cluster chaperone activity, not generic cluster binding.
- In a reconstituted bacterial ISC system, IscU receives persulfide from IscS, forms a [1Fe-1S] precursor, and dimerizes to generate a [2Fe-2S] cluster for transfer [PMID:39870763 "IscU dissociates from IscS, dimerizes and generates a bridging [2Fe-2S] cluster by fusion of two [1Fe-1S] precursors"].
- Comparative experiments distinguish IscU as the preferred initial assembly scaffold from IscA [PMID:16877383 "iron-sulfur clusters are assembled in IscU, but not in IscA, suggesting that IscU is a preferred iron-sulfur cluster assembly scaffold protein"].


## Isc comparative-evidence audit (2026-11-07)

IscU (PP_0843) is the transient iron-sulfur cluster scaffold of Pseudomonas putida KT2440. It receives sulfur from IscS and coordinates newly assembled clusters for transfer to acceptors. Its conserved scaffold family supports iron loading and cluster delivery, while the detailed loading sequence and HscA/HscB-dependent conformational cycle are characterized in bacterial homologs.

The target remains KT2440; no purified target assay is claimed. Specific curated HAMAP/RuleBase statements or independent NCBIfam/InterPro signatures ground the target inference. ARBA names are not used as proof. All original ordered source payloads are retained. The rows are IEA or historical NEW, not IBA; no donor-count argument, PAINT loss or new evolutionary node placement is asserted.

A genuine Falcon request failed with HTTP 403 authentication/access failure. Existing OpenScientist reports, where present, were preserved; no provider-branded replacement was fabricated. The log is `.cache/module-audit-logs/isc-20261107/psepk-consultation/falcon-iscU.log`.

### Evidence and biological limits

- [PMID:20942799] E. coli IscU did not copurify with iron under conditions that recovered iron-loaded IscA. Quoted support: “fails to bind any iron in E. coli cells under the same experimental conditions.”.
- [PMID:16877383] Comparative reconstitution identifies IscU as the preferred initial Fe-S cluster assembly scaffold.
- [PMID:39870763] The E. coli reconstituted assembly pathway starts with iron loading onto IscU and ends in cluster delivery. Quoted support: “this process is initiated by iron binding to the scaffold protein IscU”.
- [PMID:18986169] A bacterial HscA/HscB system accelerates cluster transfer from holo-IscU to apoferredoxin. Quoted support: “transfer from holo-IscU to apoferredoxin”.

### Decisions

- GO:0005506 iron ion binding: ACCEPT. The 2010 E. coli study failed to recover iron on IscU under its purification conditions; it does not establish universal absence. The later reconstituted E. coli system in PMID39870763 explicitly begins with iron binding to IscU. Together with target RuleBase scaffold function, this supports the inherited iron-binding claim by homolog inference, without asserting a stable free-iron reservoir or a direct KT2440 assay.
- GO:0005737 cytoplasm: ACCEPT. The specific IscU/NCBIfam assignment and soluble intracellular IscS-dependent cluster-assembly mechanism support this location. Lack of target imaging does not make the inferred functional location peripheral. No finer compartment is proposed.
- GO:0016226 iron-sulfur cluster assembly: ACCEPT. The target RuleBase function independently assigns scaffold formation and handoff, supported by homolog reconstitution. It is not merely an ARBA name or a general NifU-family label.
- GO:0051536 iron-sulfur cluster binding: MODIFY. Refine the true binding claim to iron-sulfur cluster chaperone activity, whose definition includes binding and delivery. Target RuleBase explicitly describes building and handing off clusters; homolog transfer experiments support the mechanism. This does not imply that IscU folds a polypeptide.

Additional primary scope check [32131593]: E. coli native mass spectrometry detects iron binding to IscU before cluster completion. Quoted support: “Fe(II) ions bind to the IscU active site cysteine residues and another lower affinity binding site”. The E. coli assay does not establish a native KT2440 kinetic pathway.

Additional primary scope check [36605734]: E. coli experiments allow either iron or sulfur loading first and limit claims about a universal loading sequence. Quoted support: “Our data indicate that either Fe2+ or sulfur transfer can occur first”. The E. coli assay does not establish a native KT2440 kinetic pathway.
