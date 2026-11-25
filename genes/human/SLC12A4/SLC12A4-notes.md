# SLC12A4 (KCC1, Q9UP95) — curation notes

## Identity / overview
- SLC12A4 = Solute carrier family 12 member 4 = electroneutral K-Cl cotransporter 1 (KCC1 / hKCC1 / erythroid K-Cl cotransporter 1).
- Member of the SLC12A (cation-chloride cotransporter, CCC) family, K/Cl co-transporter (KCC) subfamily. TCDB 2.A.30.1.17.
- 1085 aa, 12 TM helices, large cytoplasmic CTD, homodimer (domain-swapped at scissor helices). Multiple cryo-EM structures (6KKR/T/U, 7AIP/Q/R, 7TTH/I).

## Core molecular function
- Mediates electroneutral K+:Cl- symport (cotransport), activated by cell swelling (hypotonic). Net K+ and Cl- EFFLUX under physiological gradients → regulatory volume decrease / cell-volume homeostasis.
  - [PMID:10913127 "Both KCCs express minimal K(+)-Cl(-) cotransport under isotonic conditions, with significant activation by cell swelling under hypotonic conditions."]; Km(K+) ≈ 25.5 mM.
  - UniProt CATALYTIC ACTIVITY: K+(in) + chloride(in) = K+(out) + chloride(out) (RHEA:72427); EXP PMID:10913127, IDA PMID:34031912, PMID:35759661.
  - [PMID:34031912 "Potassium-coupled chloride transporters (KCCs) play crucial roles in regulating cell volume and intracellular chloride concentration."]
- GO MF: GO:0015379 potassium:chloride symporter activity (verified OLS: K+(out)+Cl-(out)=K+(in)+Cl-(in)).

## Localization
- Plasma membrane (cell membrane; multi-pass). ISS/TAS/IEA all agree. UniProt: Cell membrane. In NaCl-absorbing epithelia implicated in basolateral Cl- exit (By similarity Q9JIS8) — i.e. NOT apical. Ubiquitous; strongly expressed in erythrocytes (K+ efflux pathway, elevated in HbSS/HbSC → RBC dehydration, sickle cell).
- IBA is_active_in GO:0016324 apical plasma membrane is a family-level call (KCC family members have varied polarity); for KCC1 the specific "apical" is not supported — generalize to plasma membrane.
- GO:0005765 lysosomal membrane (HDA, PMID:17897319, lysosomal proteomics) — peripheral; KCCs undergo lysosomal trafficking/degradation (KCC2 PKC site → lysosomal degradation, 34031912). Keep as non-core.

## Regulation
- ATP/ADP-binding pocket in the CTD (IDA PMID:34031912) — regulatory, NOT the energy source (secondary active transporter uses K+ gradient). [PMID:34031912 "we map additional phosphorylation sites as well as a previously unknown ATP/ADP-binding pocket in the large C-terminal domain"]. ATP bound via backbone to V730, side chains K699/K707.
- Phospho-regulated (SPAK/OSR1; WNK3 inhibits — PMID:21613606). Inhibited under isotonic conditions.

## Annotation decisions (summary)
- Core MF: GO:0015379 K:Cl symporter — ACCEPT all 8 rows (EXP/IBA/IDA/IEA/ISSx2/TASx2).
- Plasma membrane GO:0005886 — ACCEPT (all evidence codes).
- Processes: cell volume homeostasis GO:0006884 (TAS), chloride transport GO:0006821 (IBA), potassium ion transmembrane transport GO:0071805 (IBA/ISS), chloride transmembrane transport GO:1902476 (TAS) — ACCEPT.
- chloride/potassium ion homeostasis GO:0055064/GO:0055075 (ISS) — KEEP_AS_NON_CORE (downstream consequence).
- ATP binding GO:0005524 (IDA) — KEEP_AS_NON_CORE (regulatory).
- lysosomal membrane GO:0005765 (HDA) — KEEP_AS_NON_CORE.
- TOO_GENERAL (entailed by specific accepted terms): GO:0006811 monoatomic ion transport, GO:0015377 chloride:monoatomic cation symporter activity, GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport.
- MODIFY: GO:0016020 membrane ×2 → GO:0005886 plasma membrane; GO:0016324 apical plasma membrane → GO:0005886 plasma membrane (apical not supported for KCC1; basolateral by similarity); GO:1990573 potassium ion import across plasma membrane → GO:0071805 potassium ion transmembrane transport (KCC1 mediates K+ EFFLUX not import; OLS: GO:1990573 = movement of K+ from outside into cytosol — wrong direction).
- GO:0005515 protein binding ×9 (IPI, PMID:32296183 ×8, PMID:40355756 ×1) — REMOVE (uninformative bare protein binding; interactors are mostly keratin-associated proteins/sticky baits: CYSRT1, KRTAP12-2, KRTAP19-2, CNFN, MB21D2, TMEM102, ZNF655, AP3M1 — no evidence-backed specific MF).

## References checked
- PMID:10913127 (abstract) functional expression KCC1 vs KCC4, kinetics, swelling activation.
- PMID:34031912 (full text) cryo-EM, ATP pocket, phospho-regulation.
- PMID:8663127 (abstract) cloning/functional expression KCC1.
- PMID:9516379 (abstract) erythroid K:Cl cotransport, RBC dehydration.
- PMID:17897319 (abstract) lysosomal membrane proteome.
- PMID:32296183 / PMID:40355756 interactome (binary / SLC interactome) — bare binding.
