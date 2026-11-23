# nuoC (NuoCD, P33599) notes

## 2026-10-23 review session

Deep-research providers are not available here (no API keys), so I reviewed
the literature by hand from cached publications/PMID_*.md and the UniProt
record. I cached one extra paper, PMID:25545070 (full text, PMC).

- NuoCD is a single polypeptide that fuses the 30-kDa (NuoC) and 49-kDa (NuoD)
  subunits [PMID:20979355 "the hydrophilic subunits NuoC/Nqo5/30k and
  NuoD/Nqo4/49k are fused together in a single polypeptide as the NuoCD
  subunit"]. It has no cofactor [PMID:20979355 "The NuoCD subunit is the only
  subunit that does not bear a cofactor in the peripheral arm."].
- Quinone binding is confirmed from the literature:
  - Thermus Nqo4 ligates the DQ head group [PMID:23417064 "hydrogen-bonded to
    4_Tyr87, while another interacts, unexpectedly, with 4_His38"].
  - In the E. coli structure the equivalent residues point to the Q site
    [PMID:34308841 "Both DTyr273 and DHis224, found in the proximity of bound
    decylubiquinone (Baradaran et al., 2013) are conserved in E. coli and point
    toward the quinone binding site"].
  - Mutagenesis agrees [PMID:25545070 "residues Tyr273 and His224 were
    considered candidates for having important interactions with the quinone
    headgroup"].
  - Result: the core MF is GO:0048038 quinone binding, plus contributes_to
    GO:0008137.
- I removed GO:0051287 NAD binding (InterPro2GO from IPR001135), because NADH
  binds at the FMN of NuoF. I removed GO:0050136 (the non-electrogenic term),
  because NDH-1 is the proton-gradient-generating enzyme [PMID:3122832].
- Three bare protein-binding IPI rows (NuoG, FliM/FliG) are removed under
  policy. NuoCD loss does not affect the flagellar motor [PMID:22210351].
- General terms are MODIFIED to their specific descendants already present in
  the review: membrane -> plasma membrane; NADH dehydrogenase complex ->
  respiratory chain complex I; GO:0003954/0016651/0016655 -> GO:0008137.
- Cytoplasm is kept as non-core (UniProt, from PMID:16079137).
- Validation: `just validate ECOLI nuoC` reports 0 warnings and 0 errors (run
  with UV_NATIVE_TLS unset; that variable otherwise adds an environment
  deprecation warning).
