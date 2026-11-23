# UFO (UNUSUAL FLORAL ORGANS, FBX1, At1g30950; UniProt Q39090) curation notes

## 2026-10-05 — initial review (floral_meristem_identity module)

- Identity check: UFO_ARATH, Q39090, At1g30950. Correct.
- Falcon deep research attempted; provider failed (exit code 1). Notes from cached publications.

### Genetics

- ufo affects floral meristem identity, whorl pattern, determinacy, and AP3/PI activation
  [PMID:7780306 "UFO is involved in establishing the whorled pattern of floral organs, controlling the determinacy of the floral meristem, and activating the APETALA3 and PISTILLATA genes required for petal and stamen identity."]
- 35S::UFO activates AP3 only with LFY [PMID:9016705 "However, 35S::UFO could not restore petal and stamen development in lfy mutants, indicating that UFO can only function in the presence of LFY activity."]

### Mechanism

- F-box protein binding ASK (SKP1-like) proteins [PMID:10607296]; SCF(UFO) with CSN [PMID:12724534]; genetic interaction with CUL1 [PMID:15047903].
- UFO-LFY physical interaction; recruitment to AP3 promoter; proteasome needed [PMID:18287201].
- Ubiquitination link mostly dispensable; LFY-UFO-DNA complex at new cis-elements; cryo-EM [PMID:36732360 "This work reveals a unique mechanism of an F-box protein directly modulating the DNA binding specificity of a master transcription factor."]

### Identifier issue

- One IPI protein binding row (PMID:10607296) has WITH/FROM UniProtKB:P43291, which is SnRK2.4/SRK2A (synonym "ASK1", a kinase). The paper concerns SKP1-like ASK proteins (ASK1 = SKP1A = Q39255). Likely an IntAct synonym mis-mapping of the partner; the UFO activity itself is fine (MODIFY to adaptor activity like other ASK rows).

### Decisions

- ubiquitin-protein transferase activity (IBA, IMP) -> MODIFY to GO:1990756 ubiquitin-like ligase-substrate adaptor activity (F-box subunit is not catalytic).
- ASK protein binding rows -> MODIFY to GO:1990756; LFY binding -> MODIFY to GO:0140297.
- ubiquitin ligase complex -> MODIFY to GO:0019005 SCF ubiquitin ligase complex.
- NEW: GO:0003713 transcription coactivator activity (IDA, PMID:36732360) as the core MF.
- Proteolysis BP terms -> KEEP_AS_NON_CORE (no substrate known).
