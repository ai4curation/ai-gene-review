# NQO2 (P16083, NQO2_HUMAN) — review notes

## Gene identity and core function

NQO2 = **NRH:quinone oxidoreductase 2 / quinone reductase 2 (QR2)**; UniProt recommended name
*Ribosyldihydronicotinamide dehydrogenase [quinone]*, **EC 1.10.5.1**. A 231-aa cytosolic FAD
flavoprotein, homodimer, member of the NAD(P)H:quinone oxidoreductase family (paralog of NQO1).

**Defining biochemical distinction from NQO1:** NQO2 does **not** use NAD(P)H efficiently as the
electron donor. Instead it uses **dihydronicotinamide riboside (NRH)** (and other reduced
N-ribosyl/N-alkyl dihydronicotinamides) as the reducing co-substrate.
[PMID:10945627 "its activity is normally latent, and a nonbiogenic co-substrate such as NRH [nicotinamide riboside (reduced)] is required for enzymatic activity"]
UniProt MISCELLANEOUS: "Uses dihydronicotinamide riboside (NRH) rather than NAD(P)H as an electron donor."

- **Catalysis:** two-electron reduction of quinones to hydroquinones (quinols), NRH + quinone + H+ →
  N-ribosylnicotinamide + quinol (RHEA:12364; EC 1.10.5.1; GO:0001512). FAD-dependent.
- **Cofactors:** FAD (flavin) and one structural Zn2+ per subunit (UniProt COFACTOR).
- **Biological role:** quinone reduction/detoxification (produces less-toxic hydroquinones for
  conjugation), though notably QR2 can in some cases generate **more** reactive species than the
  parent quinone [PMID:18254726 "it was believed that QR2 might also serve as a detoxification enzyme that can produce hydroquinones which are less toxic to cells compared with the parent quinones"]. Also implicated in prodrug bioactivation (CB1954, mitomycin C).

## Pharmacology — the MT3 melatonin site and resveratrol

QR2 is the long-sought **cytosolic "MT3" melatonin binding site**.
[PMID:18254726 "MT3 was purified to homogeneity and identified as QR2 (quinone reductase 2)"]
Melatonin is a **competitive inhibitor** of QR2 (vs the dihydronicotinamide donor), binding in the
**active site** (not allosteric): [PMID:18254726 "melatonin is a competitive inhibitor against N-methyldihydronicotinamide"] and X-ray structures show
[PMID:18254726 "melatonin binds in multiple orientations within the active sites of the QR2 dimer as opposed to an allosteric site"].

QR2 is also one of the highest-affinity molecular targets of **resveratrol** (an inhibitor here,
in contrast to cao-1 where resveratrol is a substrate):
[PMID:18254726 "It is one of the most potently inhibited (nanomolar) molecular targets of resveratrol, a natural polyphenol found in wine and peanuts, and the X-ray structure of QR2 in complex with resveratrol has been determined"].

So the `melatonin binding` and `resveratrol binding` IDA annotations reflect **inhibitor/ligand
binding at the active site**, well-evidenced (co-crystals, ITC/kinetics) but pharmacological rather
than the core catalytic function → KEEP_AS_NON_CORE.

**Provenance of the `resveratrol binding` IDA (GO:1905594 → PMID:18254726):** In the annotated
paper the direct evidence is a **binding assay, not a structure** — ITC gave a Kd of ~39 nM
[PMID:18254726 "Resveratrol was found to interact strongly with QR2 with a Kd of 39 nM"], plus IC50
inhibition assays; resveratrol served as a positive control there. The **crystal structure** of the
QR2:resveratrol complex is from an earlier paper — **Buryanovskyy et al. 2004 (PDB 1SG0; PMID:15342248)**,
who also first measured the Kd (~35 nM) by intrinsic tryptophan fluorescence — which Calamini et al.
reuse for molecular replacement/docking. Buryanovskyy 2004 is a candidate reference to add (it is the
primary structural + first-binding source but is absent from NQO2's GOA reference set).

## Annotation review decisions (26 GOA annotations)

### Molecular function — catalytic
- **GO:0001512** dihydronicotinamide riboside quinone reductase activity (IDA PMID:18254726; IEA) →
  **ACCEPT (core)**. Exactly matches EC 1.10.5.1 / RHEA:12364.
- **GO:0003955** NAD(P)H dehydrogenase (quinone) activity (IBA) → **MODIFY → GO:0001512**. This term
  maps to EC 1.6.5.2 (NAD(P)H donor); NQO2 uses NRH, not NAD(P)H. Family IBA propagated the
  NQO1-type activity. Replace with the NRH-specific term.
- **GO:0016661** oxidoreductase activity, acting on other nitrogenous compounds as donors (IDA
  PMID:10945627) → **MODIFY → GO:0001512**. Maps to EC 1.7.-.- (nitrogenous donors), a different
  branch than NQO2's EC 1.10.5.1; the specific NRH:quinone reductase term is the correct classification.
- **GO:0016491** oxidoreductase activity (IDA PMID:10945627) → **KEEP_AS_NON_CORE**. Correct root
  term but uninformatively general.
- **GO:0009055** electron transfer activity (IDA PMID:10945627, PMID:18254726) → **MARK_AS_OVER_ANNOTATED**.
  This term denotes electron-carrier proteins in electron transport chains; QR2 is a soluble
  two-electron quinone reductase, and its electron flow is already captured by the quinone reductase MF.

### Molecular function — cofactor/ligand binding
- **GO:0071949** FAD binding (IDA) → **ACCEPT** (core cofactor; flavoprotein).
- **GO:0008270** zinc ion binding (IDA) → **ACCEPT** (structural Zn2+, 1/subunit per UniProt).
- **GO:0031404** chloride ion binding (IDA) → **KEEP_AS_NON_CORE**. Not a recognized functional
  cofactor (absent from UniProt COFACTOR); likely a crystallographic ion.
- **GO:1904408** melatonin binding (IDA) → **KEEP_AS_NON_CORE** (MT3 site; active-site competitive inhibitor).
- **GO:1905594** resveratrol binding (IDA) → **KEEP_AS_NON_CORE** (nanomolar inhibitor binding).
- **GO:0042803** protein homodimerization activity (IPI PMID:18254726) → **ACCEPT** (genuine homodimer;
  informative, unlike bare protein binding). Non-core.

### Molecular function — protein binding (5× IPI, GO:0005515)
- PMID:16189514, 25416956, 31515488, 32296183 = large-scale interactome (Y2H) screens;
  PMID:24606901 = HSCB/HSC20 LYR-motif cochaperone study. All → **KEEP_AS_NON_CORE**. `protein binding`
  is uninformative (project guideline: avoid); none identifies a functional partnership that revises
  the core-function picture.

### Biological process
- **GO:1901662** quinone catabolic process (IDA PMID:18254726) → **ACCEPT**. Captures the quinone
  reduction/detoxification role (main BP).

### Cellular component
- **GO:0005829** cytosol (IDA GO_REF:0000052; also TAS Reactome, IBA, IDA PMID:10945627) → **ACCEPT (core)**.
  QR2 is cytosolic.
- **GO:0005737** cytoplasm (IEA) → **ACCEPT** (general parent).
- **GO:0070062** extracellular exosome (HDA PMID:23533145, PMID:19056867) → **KEEP_AS_NON_CORE**.
  High-throughput exosome proteomics detection; not a functionally informative localization for a
  cytosolic enzyme.

## Enzyme-function / Rhea comparison
- Core MF **GO:0001512** carries EC=1.10.5.1, RHEA:12364, MetaCyc 1.10.99.2-RXN, Reactome R-HSA-8936519 —
  a fully-resolved, reaction-specific term (unlike cao-1, where no reaction-level term existed).
- The IBA **GO:0003955** carries EC=1.6.5.2 (NAD(P)H) — the wrong cofactor branch for NQO2; this is the
  crux of the MODIFY.
- Contrast with cao-1: there resveratrol is the **substrate** of a stilbenoid dioxygenase; here
  resveratrol is a **high-affinity inhibitor** of a quinone reductase — same molecule, opposite role,
  and a good illustration of why `resveratrol binding` alone (causal-role, ligand-agnostic) underspecifies biology.
