# MCM4 (CDC54, YPR019W; UniProt P30665), Saccharomyces cerevisiae

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised reference for transfer to the
PTHR11630:SF66 (MCM4) subfamily, including Neurospora NCU02539. No ProtNLM2 output was
consulted.

### Deep research

`just deep-research-falcon yeast MCM4 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 (insufficient
quota). There is no deep-research file. The review rests on the cached publications for the 31
GOA-cited PMIDs (14 with full text), the UniProt record and the PANTHER/PAINT data in
`interpro/panther/PTHR11630/`.

### Evolutionary placement

- UniProt: `PANTHER; PTHR11630:SF66; DNA REPLICATION LICENSING FACTOR MCM4`, with the
  `MCM_4` InterPro signature IPR008047 and a WHD_MCM4 Pfam domain.
- PAINT (`PTHR11630-paint.tsv`):
  - PTN000179711 (MCM2-7 node): IBD for MCM complex, ssDNA binding (seeded by SGD
    S000006223 = this gene alone) and ssDNA helicase activity.
  - PTN000179712: nucleus.
  - PTN000179968 (Mcm4 subfamily node, taxon 2759): GO:0000727 BIR and GO:0006271 strand
    elongation, both seeded by this gene; GO:1902975 mitotic replication initiation, seeded by
    S. pombe cdc21.
  - Not propagated at any node: pre-RC assembly (GO:0006267), origin binding (GO:0003688),
    premeiotic replication, four-way junction helicase and 3'-5' helicase. If these are
    transferred to orthologs, the omission should be treated as a deliberate PAINT decision.
  - There are IRD (NOT) nodes for Drosophila and Deuterostomia branches. They do not affect
    yeast.

### Experimentally established in S. cerevisiae (direct evidence)

- Subunit of Mcm2-7, reconstituted from recombinant subunits [PMID:12480933 "have reconstituted the Mcm2-7p complex from individual subunits"].
- Loaded by ORC-Cdc6-Cdt1 onto origins as head-to-head double hexamers that encircle and slide on dsDNA
  [PMID:19896182 "DNA runs through a central channel in the double hexamer, and, once loaded, Mcm2-7 can slide passively along double-stranded DNA"];
  [PMID:19910535 "MCM2-7 loading was found to be dependent on the presence of all pre-RC proteins, origin DNA, and ATP hydrolysis"].
- Required continuously for fork progression
  [PMID:10834843 "depletion of MCMs after initiation irreversibly blocks the progression of replication forks in Saccharomyces cerevisiae"].
- Mcm467 helicase with leading-strand tracking, polarity opposite to DnaB (3'->5')
  [PMID:13679365 "The Mcm4,6,7 mechanism is very similar to DnaB, except the proteins translocate with opposite polarity along DNA"].
- Mcm2-7 helicase reconstituted; Mcm4 Walker A K574A abolishes it
  [PMID:18657510 "Our results show that purified Mcm2-7 acts as a helicase"].
- ATP-dependent ssDNA binding
  [PMID:17895243 "possess a similar ATP-dependent single-stranded DNA (ssDNA) binding activity"].
- CMG subunit [PMID:26854665 "The CMG helicase is composed of Cdc45, Mcm2-7 and GINS"].
- Principal DDK target at firing
  [PMID:26854664 "Dbf4-dependent kinase (DDK, composed of Cdc7 and Dbf4) phosphorylation of primarily Mcm4 recruits Cdc45"].
- Required for BIR [PMID:20516198 "BIR requires the replicative DNA helicase (Cdc45, the GINS, and Mcm2-7 proteins)"].
- CDK-driven nuclear exclusion
  [PMID:10559985 "CDKs exclude the essential prereplicative-complex component Mcm4 from the nucleus"].

### Inferred or not experimentally established here

- Zinc binding rests on the RCA zinc-proteome survey and on the MCM family N-terminal zinc
  motif. In the P30665 sequence I found a C4 cluster at Cys349/Cys352/Cys371/Cys376 (CX2C-X18-CX4C)
  by a simple sequence scan. That is my own observation, not a published structural assignment.
- Premeiotic DNA replication (GO:0006279): the only experimental row cites PMID:20484375, whose
  full text has no meiotic data. I marked it UNDECIDED and flagged it as a possible mis-keyed
  reference.

### Key decisions

- 27 protein-binding IPI rows: REMOVE under the GO:0005515 policy. The interactions are real
  but are captured by the complex terms.
- `DNA helicase activity` / `helicase activity` rows: MODIFY to GO:0043138 3'-5' DNA helicase
  activity plus GO:0017116, qualified contributes_to. The isolated subunit has no helicase
  activity on its own.
- `DNA replication` (GO:0006260) and `nuclear DNA replication` (GO:0033260): MODIFY to the
  specific terms the gene already carries (GO:0006271, GO:1902975).
- Origin binding: KEEP_AS_NON_CORE. ORC recognises the origin; MCM encircles DNA without
  sequence specificity.
- MCM core complex (Mcm467), four-way junction helicase and cytoplasm: KEEP_AS_NON_CORE. These
  are in vitro or regulatory-state findings.
