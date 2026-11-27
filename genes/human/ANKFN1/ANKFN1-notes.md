# ANKFN1 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKFN1 (Q8N957; mouse mWAKE) is the vertebrate ortholog of fly Wide awake/Banderuola (FBgn0266418). The fly gene has two experimentally supported roles:
  - spindle orientation and asymmetric division in neural precursors (PMID:25088559, the source of the PAINT donor annotations);
  - a sleep-promoting clock output that co-immunoprecipitates with the GABA-A receptor RDL (PMID:24631345).
- **Mouse:** mWAKE is a clock-dependent brake on arousal in the DMH (PMID:37821426) and sets rhythmic excitability through Ca2+-activated K+ channels in the amygdala (PMID:39303704). The nmf9 null allele has vestibular and neurological phenotypes.
- **Zebrafish:** Ankfn1 genes are needed for vestibular function (PMID:35100349).
- **The 3 IBAs (spindle orientation, spindle, bipolar cell polarity):** KEEP_AS_NON_CORE with NO_FAILURE_NON_CORE.
  - These are plausibly ancestral: the Bnd authors note the mammalian Bnd-Dlg interaction is conserved.
  - No vertebrate counter-evidence, but untested in vertebrates in the studies reviewed. Single donor, but per CLAUDE.md donor count is not weakness.
- **NEW (round 1, withdrawn in round 2): GO:1904326 negative regulation of circadian sleep/wake cycle, wakefulness** (ISS from mouse PMID:37821426). See round 2: the paper's Results show total wake time unchanged.
  - Participation: mWAKE lowers the excitability of the neurons it sits in.
  - Comparator: fly WAKE carries GO:0045938, positive regulation of circadian sleep/wake cycle, sleep.
  - Mouse Ankfn1 (F6X7B3) has no GO annotations at all, so this is an uncurated gap, not a convention.
- **MF_DARK gap:** the molecular target is unknown.
- **Not used:** the HCC/MEK-ERK claim (PMID:35725908), a single cancer study.

## 2026-10-04 round 2 (reviewer comments on #4072)

- **Withdrew GO:1904326.** I quoted the abstract's "brake on arousal" framing, but the Results of PMID:37821426 say "mWake mutants exhibit changes in the quality, but not quantity, of wakefulness at night". Total wake time is unchanged, so a negative-regulation-of-wakefulness term overstates it.
- **NEW is now GO:1902608** positive regulation of large conductance calcium-activated potassium channel activity (ISS, PMID:39303704; mouse F6X7B3 in supporting_entities). The measured effect is "mWAKE promotes BK channel activity at night to inhibit neuronal excitability", and conditional knockouts in the DMH and CeA raise excitability (PMID:37821426, PMID:40835437). It is also the core function.
- **Spindle IBA (is_active_in):** now has its own CC reasoning. FlyBase records spindle and centrosome IDA for Banderuola from the full text, while the cached abstract stresses cortical domains. Kept non-core rather than adopted.
- **Affinage accounting:** PMID:40835437 is used. PMID:36533556 (crispant cilia screen) and PMID:33140455 (expression atlas) are declined, with reasons.
- **No vestibular term:** zebrafish double mutants and the mouse nmf9 allele show that ANKFN1 is needed for vestibular function, but not what it does there, so no vestibular process term is proposed (necessity, not participation).

## 2026-10-04 round 3 (reviewer comments on #4072)

- **Citation fix:** the spindle row's cortical-domain claim now quotes the abstract sentence that says it ("Bnd acts together with ... Dlg to establish antagonistic cortical domains during ACD"). It previously quoted the polarity/spindle sentence.
- **NEW row:** evidence code ISS changed to ISO (orthology to mouse F6X7B3). The reason acknowledges that the authors leave open whether mWAKE changes BK levels or gating ("How might mWAKE modulate BK levels or function?").
- **Knowledge gap:** now names BK (KCNMA1).
- **Not adopted:** GO:0042391 regulation of membrane potential (suggested). GO:1902608 already names the measured mechanism, and adding a broad parent-level effect term would duplicate it.
