# nspC evidence notes

## 2026-08-11

The exact KT2440 record assigns NspC to the carboxyspermidine/
carboxynorspermidine decarboxylase subfamily and gives EC 4.1.1.96. Its adjacency
to PP_2928 matches the paired dehydrogenase/decarboxylase organization of the
alternative pathway established in Vibrio cholerae. [PMID:19196710 "Genetic
deletion of the V. cholerae CANSDC led to accumulation of
carboxynorspermidine"]

No direct KT2440 NspC assay is available. The current GO molecular-function
annotation is only the broad carboxy-lyase parent, so a specific EC 4.1.1.96
term is proposed.

## 2026-11-02 (module curation: bacterial_carboxyspermidine_biosynthesis)

- Replaced the NEW spermidine-process support that quoted the UniProt `DR GO`
  line (a label restating an electronic annotation) with the curated function
  statement, the PTHR43727:SF1 classification and primary genetics from other
  bacteria: C. jejuni [PMID:22025614 "the carboxynorspermidine decarboxylase
  orthologue is responsible for synthesizing spermidine and not
  sym-norspermidine in vivo"] and B. thetaiotaomicron [PMID:27118128
  "carboxyspermidine decarboxylase is essential for synthesizing spermidine in
  B. thetaiotaomicron"].
- GO:0003824 catalytic activity changed from MARK_AS_OVER_ANNOTATED to
  TOO_GENERAL, matching the new Vibrio cholerae NspC (Q9KRL4) review; the term is
  true but entailed by the accepted carboxy-lyase activity.
- The GO:0008836 diaminopimelate decarboxylase REMOVE rests on the chemistry:
  the V. vulnificus orthologue showed no activity with meso-diaminopimelate
  [PMID:19196710 "no activity with l -arginine, l -lysine, and meso
  -diaminopimelate"], and Q88IS0 is classified in the NspC subfamily
  PTHR43727:SF1, not the LysA subfamily SF2.
  Note how this row reaches Q88IS0, which is not the same route as in the Vibrio
  orthologue. Here it is a TreeGrafter IEA (GO_REF:0000118) grafted from
  PANTHER:PTN001691018. That node is absent from
  interpro/panther/PTHR43727/PTHR43727-paint.tsv, so PAINT does not expose it and
  the PTHR43727 family review does not assess it; the family review's
  NEEDS_PRUNING verdict is on PTN000159906, whose IBA rows reach V. cholerae
  Q9KRL4 instead. The family review's reasoning about SF1 divergence supports this
  removal, but it is not the node this row came from.
- No gene-level deep-research file exists for this gene; none was generated in
  this session (provider not run). The module and P. putida project
  OpenScientist reports were used for retrieval.


## 2026-11-05 complete gene-level comparative audit

Re-read every existing annotation, core function, raw UniProt record, relevant
provider report and primary literature. Original annotation payloads and raw
UniProt/GOA snapshots were preserved; no new annotation rows were added. Five
authored NEW rows across the four-gene baseline remain inherited proposals, not
new proposals from this audit. Default Falcon research was attempted with
`just deep-research ORGANISM GENE --provider falcon`; it failed with HTTP 403
authentication. No provider report was fabricated or overwritten. Manual findings
are recorded here; the command logs are in the ignored module-audit cache.

QuickGO on 2026-11-05 confirmed active GO:0102143 includes both carboxynorspermidine
and carboxyspermidine dehydrogenase reactions, and GO:0102144 is obsolete as the
same activity. Searches for carboxyspermidine/carboxynorspermidine decarboxylase
and carboxypolyamine returned no specific decarboxylase term. The existing NTR
name was retained; no GO or PTN identifier was invented. PANTHER official names
were checked in panther.obo, and exact protein/subfamily assignments against the
unchanged UniProt records (PTHR43796:SF2 for the dehydrogenases; PTHR43727:SF1 for
the decarboxylases).

The comparative literature requires a substrate-specific reading. The B. fragilis
and C. leptum enzymes have measured putrescine/DAP kinetics, but these are not
measurements of this target [PMID:37437886, "These data suggest that both enzymes
can use putrescine or DAP and thus produce carboxyspermidine or
carboxynorspermidine."]. Agmatine was not tested in those comparisons. The 2025
reconstruction shows that related pairs can make tetramines or use agmatine;
those functions are not transferred here [PMID:40074085, "The ASA-dependent
pathway consisting of CASDH/CASDC homologs has diversified during evolution
to produce norspermidine (29), N1-aminopropylagmatine (37), and as we have shown
here, spermidine and Spm/Tspm."]. Physiological product identity, reconstructed
pathway activity and isolated-enzyme turnover are distinct evidence.

Refined GO:0003824 and all GO:0016831 rows to MODIFY with the already-supported
NTR carboxyspermidine/carboxynorspermidine decarboxylase activity; the core uses
proposed_molecular_function with the matching proposal. This changes specificity,
not the claimed chemistry. Existing lysine/diaminopimelate removals remain
consistent with the family review.

GO:0045312 changed from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED: family/rule
assignment predicts substrate capability but does not establish endogenous
carboxynorspermidine supply or norspermidine biosynthesis in KT2440. The earlier
notes' claim that this was a real peripheral process exceeded the evidence.
The inherited spermidine NEW row remains a comparative inference, not an assay.
The TreeGrafter source PTN001691018 remains distinct from Vibrio's IBA node.

Targeted searches for PP_2928/carboxyspermidine and nspC/KT2440 did not recover
a direct target assay. The paired pathway remains a comparative proposal.
Family identity and adjacency are supportive but insufficient to establish
native diamine preference, particularly after CAPA-pathway diversification
[PMID:37878710]. The H. pylori putrescine assay cited previously cannot establish
physiological substrate preference: that homolog was also characterized as CAPADH.
No new PLP-binding or homodimerization row was added solely from family architecture;
the specific catalytic proposal already captures the core activity.


## PR 6089 review 5812319279 follow-up (2026-11-07)

Added the previously prose-cited PMID37878710 to references with a bounded CAPA-diversification finding. No annotation action, payload, lifecycle or core changed.

Read-only source caches were used; no downloads or source refreshes. Original annotation payloads/order and every historical NEW lifecycle are preserved. Heavy validation and rendering are deferred because disk space is critically low.
