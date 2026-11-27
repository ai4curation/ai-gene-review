# THBD (thrombomodulin, CD141; UniProtKB P07204) review notes

## 2026-11-26 session journal

### Setup and deep research

- `just fetch-gene human THBD`: 51 GOA rows seeded (25 of them bare GO:0005515
  protein binding, 24 from the HuRI binary interactome PMID:32296183).
- `just deep-research human THBD --provider asta` ran but returned 19 papers that
  are all unrelated to thrombomodulin (protein-annotation tools, proteomics
  resources, saffron network pharmacology, etc.); the "report" contains no
  information about THBD. The file was discarded rather than committed so that no
  reader mistakes it for a literature summary. These notes are the literature
  survey instead.
- PubMed queries run (PubMed MCP, 2026-11-26):
  - `thrombomodulin TAFI activation human` (186 hits; read 8663147, 26663133)
  - `lectin-like domain thrombomodulin HMGB1` (15 hits; primary paper 15841214
    taken from the UniProt record)
  - `thrombomodulin mutations atypical hemolytic uremic syndrome` (34 hits; read
    19625716 full text, 20513133 abstract)
  - `Bajzar Nesheim TAFI thrombin-thrombomodulin complex couples coagulation
    fibrinolytic` (1 hit: 8663147)
  - metadata lookup of the GOA reference PMID:12524220 (Mann et al. 2003 review,
    "The dynamics of thrombin formation"), which `fetch-gene` had failed to cache.
- Primary papers cited by the UniProt FUNCTION/SUBUNIT text were also fetched:
  9395524, 26663133, 29323190, 33836597, 27055590, 15841214, 7811989.

### Identity and architecture

- Type I transmembrane glycoprotein of 575 aa: signal peptide 1-18, extracellular
  19-515, TM helix 516-539, cytoplasmic 540-575 (UniProt FT). Domains: N-terminal
  C-type lectin-like domain (D1, 31-169), six EGF-like repeats (241-481), a
  Ser/Thr-rich juxtamembrane region carrying an O-linked chondroitin sulfate
  chain, TM helix and short tail.
  [PMID:2822087 "The EGF-homology region consists of six tandemly repeated EGF-like domains."]
- Made by vascular endothelium. [PMID:2822087 "Thrombomodulin mRNA was not detected in human brain, HepG2 hepatoma cells, or the monocytic U937 cell line."]
  UniProt TISSUE SPECIFICITY: "Endothelial cells are unique in synthesizing thrombomodulin."
- Not an enzyme. No catalytic domain; all its anticoagulant output is carried
  out by thrombin's active site once TM is bound.

### Core activity: thrombin cofactor (protein C and TAFI activation)

- TM binds thrombin exosite I via EGF5-6 and presents protein C (EGF4) to the
  unaltered thrombin active site.
  [PMID:10761923 "The Y-shaped thrombomodulin fragment binds to thrombin's anion-binding exosite-I, preventing binding of procoagulant substrates."]
  [PMID:10761923 "TME45 may bind substrates in such a manner that their zymogen-activation cleavage sites are presented optimally to the unaltered thrombin active site."]
- This switches thrombin from procoagulant to anticoagulant.
  [PMID:10761923 "profoundly alters the substrate specificity of thrombin from pro- to anticoagulant by activating protein C"]
- TAFI (CPB2) activation: the thrombin-TM complex is the physiological activator,
  and TM raises catalytic efficiency 1250-fold, mostly via kcat.
  [PMID:8663147 "Thrombomodulin increases the catalytic efficiency of the reaction by a factor of 1250, an effect expressed almost exclusively through an increase in kcat."]
- On cultured human endothelial cells a blocking anti-TM antibody inhibits both
  activations. [PMID:26663133 "Blocking TM with CTM1009 inhibited both TAFI and PC activation."]
- Ca2+ in EGF6 is needed for the cofactor function and for tight thrombin binding.
  [PMID:10336638 "A 75-fold decrease in the binding affinity of thrombin to TM was observed with immobilized solulin treated with EDTA to remove the high affinity Ca2+"]
- Reconstituted human coagulation: soluble TM + protein C shuts down thrombin
  generation (unless FV Leiden). [PMID:9252393 "thrombin generation catalyzed by normal factor V was abolished after the initial formation of 25 nM thrombin."]
- Modulators: PF4 binds the chondroitin sulfate chain and enhances APC generation
  [PMID:9395524]; angiopoietin-1/2 bind TM and inhibit both activations
  [PMID:29323190 "Ang1 and Ang2 inhibited the thrombin/TM-mediated generation of activated protein C and TAFI in cultured endothelial cells"];
  protease nexin-1 binds TM via the CS chain and decreases protein C activation
  [PMID:17379830].
- MF term choice: GO:0061133 endopeptidase activator activity ("Binds to and
  increases the activity of an endopeptidase") fits exactly; it is the term used in
  this corpus for the analogous non-catalytic coagulation cofactors (F5 and PROS1
  reviews). TM is not annotated to it in GOA.

### Process terms: comparator check for proteolysis / zymogen activation

- GOA has NAS rows (from the Mann 2003 review) for GO:0006508 proteolysis and
  GO:0031638 zymogen activation. Participation question: who performs the cleavage?
  Thrombin's active site. TM positions substrate and raises kcat, which is
  captured by the MF term.
- QuickGO comparator query (2026-11-26), annotations to GO:0006508 and descendants:
  F5 P12259 = 0, F8 P00451 = 0, PROS1 P07225 = 0, PROCR Q9UNN8 = 0, mouse Thbd
  P15306 = 0; F3 P13726 = 2 (protein processing, IDA). Positive control F10
  P00742 = 2 (IEA, IBA) confirms the query returns hits. So same-role
  non-catalytic cofactors are, by convention, not carried on proteolysis
  processes; these two rows are over-annotation rather than error.

### Anticoagulant, antifibrinolytic and other processes

- Coagulation: TM deficiency or mutation is linked to thrombophilia (THPH12)
  [PMID:7811989] and TM is an anticoagulant, so "blood coagulation" and "common
  pathway" rows are sign errors for "negative regulation of blood coagulation".
- Fibrinolysis: via TAFI activation TM inhibits fibrinolysis [PMID:8663147].
- Platelets: TM described as a direct inhibitor of thrombin-induced platelet
  activation [PMID:17379830 "a direct inhibitor of thrombin-induced platelet activation and fibrinogen clotting"]
  (by sequestering thrombin exosite I); a consequence of thrombin binding.
- Complement: TM binds C3b and factor H and accelerates factor I-mediated C3b
  inactivation; via TAFI it accelerates C3a/C5a inactivation; aHUS variants lose
  this. [PMID:19625716 "Thrombomodulin enhanced CFI-mediated inactivation of C3b in a dose-dependent manner in the presence of either CFH or C4bBP"]
- Inflammation: the lectin-like D1 domain binds HMGB1 and sequesters it.
  [PMID:15841214 "TM, via D1, binds high-mobility group-B1 DNA-binding protein (HMGB1)"]
- Endothelial quiescence: CRISPR TM-/- human endothelial cells show increased
  permeability and NF-kB activation [PMID:33836597]. Mechanism not resolved;
  not annotated here.
- Leukocyte integrins LFA-1/Mac-1 bind the Ser/Thr-rich domain [PMID:27055590];
  noted only (non-core).

### Annotation decisions (summary)

- MF signaling receptor rows (GO:0038023 IDA/TAS, GO:0004888 IEA): TM is called a
  "thrombin receptor" in the literature but does not transduce a signal; the cited
  crystal structure shows binding and cofactor geometry. MARK_AS_OVER_ANNOTATED.
- 25 bare protein binding rows: F2 row MODIFY to GO:0002020 protease binding
  (thrombin binding is the paper's measured result); the rest REMOVE per the
  protein-binding policy.
- CC: plasma membrane, cell surface and external side of plasma membrane accepted;
  bare "membrane" TOO_GENERAL.
- NEW: GO:0061133 (core), GO:0045916 negative regulation of complement activation,
  GO:0070379 HMGB1 binding, GO:0050728 negative regulation of inflammatory response.

## 2026-11-26 PR review follow-up
- GO:0050728 negative regulation of inflammatory response, listed above as a candidate NEW, was not proposed: the HMGB1 evidence supports the binding (GO:0070379), and the anti-inflammatory outcome is a downstream consequence rather than work THBD is shown to do in the process.
