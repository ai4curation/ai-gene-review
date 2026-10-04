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
- **NEW: GO:1904326 negative regulation of circadian sleep/wake cycle, wakefulness** (ISS from mouse PMID:37821426).
  - Participation: mWAKE lowers the excitability of the neurons it sits in.
  - Comparator: fly WAKE carries GO:0045938, positive regulation of circadian sleep/wake cycle, sleep.
  - Mouse Ankfn1 (F6X7B3) has no GO annotations at all, so this is an uncurated gap, not a convention.
- **MF_DARK gap:** the molecular target is unknown.
- **Not used:** the HCC/MEK-ERK claim (PMID:35725908), a single cancer study.
