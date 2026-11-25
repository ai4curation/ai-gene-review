# RGA5 (F7J0N2, Oryza sativa subsp. japonica) — curation notes

## 2026-10-02 — initial review (claude-code, claude-opus-5-5)

Sources: UniProt F7J0N2, GOA (16 rows), RGA5-deep-research-falcon.md, cached papers
PMID:21251109 (abstract), 23548743 (abstract only; PMC full text not retrievable via
PubMed MCP), 25024433 (full text), 27289079 (abstract), 28087830 (full text),
30355769 (full text).

### Identity and architecture
- CC-NB-LRR at the Pia locus on chr11 next to RGA4; both are needed for Pia function
  [PMID:21251109 "SasRGA4 and SasRGA5, that are located next to each other and oriented in the opposite direction are necessary for Pia function"].
- An integrated HMA/RATX1 domain after the LRR (~997-1069). Only the RGA5-A splice form works
  [PMID:23548743 "Genetic analysis showed that only RGA5-A confers resistance, while RGA5-B is inactive."].

### Sensor function (core)
- Binds AVR-Pia and AVR1-CO39 directly [PMID:23548743 "revealed direct binding of AVR-Pia and AVR1-CO39 to RGA5-A"].
- Binding to the HMA decoy is needed for recognition [PMID:28087830 "this interaction is required for effector recognition"].
- Crystal structure of the HMA–AVR1-CO39 complex; Kd 5.4 uM (RGA5_S) [PMID:30355769].
- HMA metal motif is degenerate [PMID:30355769 "The metal-binding motif, characteristic of HMAs, is degenerated in RGA5HMA, as only the first Cys is conserved, while the second is replaced by a Ser."] -> REMOVE metal ion binding.

### Repressor of RGA4 (core, distinguishes sensor from executor)
- [PMID:25024433 "RGA4 mediates cell death activation, while RGA5 acts as a repressor of RGA4 and as an AVR receptor"]
- CC-domain hetero-complexes; the CC domain is needed for repression and the RATX1 domain is dispensable for it [PMID:25024433].
- Repression is specific: Orin1 and L6-MHV cell death are not suppressed [PMID:25024433].
- RGA5 never activates cell death itself. MHD mutants are not autoactive, and the K210R P-loop mutant is fully functional [PMID:25024433 "an intact RGA5 P-loop motif is not necessary for repression of RGA4-induced cell death"].
- Cytosolic, with no nuclear relocalization after AVR-Pia [PMID:25024433].

### Bacteria
- Xanthomonas resistance appears only when Xoo/Xoc carrying designer TALEs switch on a transgene encoding the fungal AVR1-CO39 [PMID:27289079]. This is not native bacterial recognition -> MARK_AS_OVER_ANNOTATED for defense response to bacterium (IDA + IEA). The IDA cites PMID:23548743, whose abstract is fungal only. I did not claim mis-attribution; the argument is biological.

### Term decisions / comparator checks
- GO:0035872 (NLR signaling pathway) has 0 annotations in Viridiplantae (QuickGO). Plant NLRs use GO:0002758 (e.g. RPS4), so I kept GO:0002758.
- GO:0062207 (regulation of PRR signaling) -> MODIFY to GO:0010363 regulation of plant-type hypersensitive response. In plants, PRR means surface PAMP receptors.
- protein binding (IPI with RGA4) -> MODIFY to GO:0140678 molecular function inhibitor activity.
- Hypersensitive response rows: KEEP_AS_NON_CORE for RGA5 (RGA4 executes it).
- GO:7770053 "NLR receptor complex" exists in current GO, but I did not use it (new id range; may not validate).

### Project Q5 (sensor vs executor)
- GOA for RGA4 is nearly identical to RGA5's: same BP/CC rows, including GO:0062207 EXP and the HR IMPs. The only differences in RGA5's set are GO:0140376 (receptor) and the HMA metal mapping. After this review, RGA5 is distinguished by receptor activity plus MF inhibitor activity and regulation of HR, with HR as non-core.
