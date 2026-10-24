# IAA17 / AXR3 (At1g04250; P93830) curation notes

## 2026-10 review (auxin_nuclear_signaling module)

- Deep research (falcon) failed (HTTP 402); review based on cached literature.
- Identity: UniProt P93830 IAA17_ARATH, synonym AXR3. Correct.

### Function
- AXR3 cloned as an Aux/IAA: "AXR3 was shown to be a member of the AUX/IAA family, providing direct evidence that AUX/IAA genes are central in auxin signaling" [PMID:9478901].
- axr3-1 (domain II) increases protein half-life sevenfold; IAA17 is nuclear and homo/heterodimerizes [PMID:11283339].
- SCF(TIR1) binds IAA17 domain II, auxin stimulates binding and degradation [PMID:11713520 "We demonstrate that SCF(TIR1) interacts with AXR2/IAA7 and AXR3/IAA17"].
- Repression: GD-IAA17 fusions repress reporters; domain I is an active repression domain [PMID:14742873].
- Nuclear protein bodies with SCF/CSN/proteasome [PMID:15994909].
- Leaf senescence: IAA17 overexpression accelerates and knockout delays senescence [PMID:25324183] - non-core.
- PB1 structure of ARF7: PB1 mutation abolishes interaction with IAA17 [PMID:24706860].

### Decisions
- Huge set of HT protein-binding IPIs (CrY2H-seq, phytohormone interactome, shoot-apex Aux/IAA-ARF interactome): ARF partners -> GO:0140297; Aux/IAA -> GO:0046982; TIR1 -> GO:0031625; unrelated TFs/importins/CSN5B etc. -> REMOVE.
- GO:0003700 ISS -> MODIFY to GO:0003714. GO:0000976 IBA -> MARK_AS_OVER_ANNOTATED.
- NEW: GO:0045892 negative regulation of DNA-templated transcription (IDA, PMID:14742873).
