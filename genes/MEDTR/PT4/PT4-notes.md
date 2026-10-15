# PT4 (MtPT4, Q8GSG4) notes

## 2026-10-02 initial review

Sources: UniProt Q8GSG4, GOA (27 rows), falcon deep research, cached PMIDs 12368495,
17242358, 19692536 (full text), 20687807, 25841038, 26476189, 26511916. Most cached papers are
abstract-only. Added PMID:17242358 (Javot 2007 PNAS) and PMID:19692536 (Pumplin & Harrison
2009), verified by DOI lookup in NCBI eutils.

### Molecular function
- Pht1 subfamily I (AM-specific) phosphate transporter, MFS fold, 12 TM.
- [PMID:12368495 "Complementation of yeast phosphate transport mutants indicated that MtPT4 functions as a phosphate transporter, and estimates of the K(m) suggest a relatively low affinity for phosphate."]
- UniProt: H+/Pi symport reaction (RHEA:29939), Km 500 uM, pH optimum 3-4.
- H+ coupling: [PMID:19692536 "H + -ATPases, which create proton gradients necessary for secondary active transporters such as MtPT4, are induced in AM roots and have been localized to the periarbuscular membrane"]
- Deep research: HA1 needed for symbiotic 33P uptake (Krajinski 2014; not cached), but PT4 H+:Pi stoichiometry never measured.
- No existing annotation has an experimental MF. GO:0005315 IEA modified to GO:0015317 phosphate:proton symporter activity.

### Location
- [PMID:12368495 "immunolocalization revealed that MtPT4 colocalizes with the arbuscules, consistent with a location on the periarbuscular membrane"]
- [PMID:19692536 "As reported previously, MtPT4 is not located in the plasma membrane, and the MtPT4-GFP marker is consistent with this and did not label the plasma membrane."]
- PT4 defines the arbuscule branch domain of the PAM (MtBcp1 marks the trunk domain).
- GO:0085042 periarbuscular membrane is not under plasma membrane in GO (ancestors: host cell part,
  other organism part). So both PM rows (IBA, UniProt SubCell IEA) were modified to periarbuscular
  membrane. IBA: the family-level node is fine; target shows lineage-specific divergence in targeting.

### Genetics
- [PMID:17242358 "Loss of MtPT4 function leads to premature death of the arbuscules; the fungus is unable to proliferate within the root, and symbiosis is terminated."]
- [PMID:25841038 "Premature arbuscule degeneration (PAD) is suppressed when pt4 mutants are nitrogen-deprived"]; [PMID:25841038 "ATM2;3 but not AMT2;4 was required for suppression of PAD in pt4"]
  - So "cellular response to nitrogen levels" (IMP) is a genetic-suppression effect that runs through
    AMT2;3, not a PT4 activity. IMP marked over-annotated; the ARBA IEA copy removed.
- Root-tip, AM-independent role: [PMID:26476189 "Lotus PT4i plants and Medicago mtpt4 mutants did not show any differential response to phosphate levels, suggesting that PT4 genes affect early root branching."]
  - "detection of phosphate ion" claims a transceptor role; the authors only "suggest" P-sensing.
    Marked over-annotated, not removed (the curator had the full text).

### Expression (IEP) rows
- response to symbiotic fungus x4 IEP + 1 IEA: accurate expression readouts (PT4 is a classic AM marker;
  RAM1-dependent). Kept as non-core.

### Project curation-question notes (PLANT_FUNGAL_INTERACTIONS)
- Necessity vs participation (Q3): PT4 passes participation for arbuscular mycorrhizal association.
  It carries out the plant-side Pi uptake step at the interface, so the process rows are accepted.
  The N-response and Pi-detection rows are the necessity-only cases.
- Symbiosis vs defense (Q4): no defense terms are present, which is correct.
