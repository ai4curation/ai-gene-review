# Cdh22 (Mus musculus, Q9WTP5) — curation notes

## 2026-11-26 — initial review (claude-code fork, Fable 5.2)

Review built from the existing GOA (all IBA/IEA/ISO; no experimental rows) plus Kroon et al.
2026 (*Nat Neurosci*, DOI:10.1038/s41593-026-02515-6), the paper that first characterizes
CDH22 function in cortical inhibitory circuit wiring. The paper has **no PMID yet** (published
online 2026-11-26); cited by DOI, cached at `publications/DOI_10.1038_s41593-026-02515-6.md`.

### Gene gestalt
- Cadherin-22 / PB-cadherin ("pituitary and brain cadherin"), a classical type-I single-pass
  transmembrane cadherin. UniProt: "Cadherins are calcium-dependent cell adhesion proteins.
  They preferentially interact with themselves in a homophilic manner"; three Ca²⁺ bound at
  each cadherin-domain interface rigidify the ectodomain
  [file:mouse/Cdh22/Cdh22-uniprot.txt]. Brain-enriched (olfactory bulb, cerebrum, cerebellum).
- The GOA is entirely generic classical-cadherin biology propagated phylogenetically /
  electronically: calcium-dependent + homophilic cell-cell adhesion, adherens junction,
  catenin complex / beta-catenin binding, cadherin binding, plasma membrane, cell migration/
  morphogenesis. None of it is CDH22-specific or captures the new synaptic role.

### New finding (Kroon et al. 2026): CDH22 is the FEZF2 effector for PV+ perisomatic inhibition
- CDH22 is one of three top-ranked cell-surface molecules (with Cntn6, Igsf21) downregulated
  when L5 ET neuron activity is lowered [DOI:10.1038/s41593-026-02515-6 "the three top-ranked
  genes downregulated by a reduction in the activity of L5 ET neurons, Cdh22, Cntn6 and Igsf21,
  encode cell-surface molecules"]. It functions **downstream of the transcription factor FEZF2**
  in an activity-dependent manner [... "the cell-surface molecule CDH22 functions downstream of
  FEZF2 in L5 ET pyramidal cells in an activity-dependent manner"]: FEZF2 overexpression raises
  Cdh22 (+22%) [... "overexpression of Fezf2 increases Cdh22 expression"], shFezf2 abolishes the
  activity-induced Cdh22 increase, and activity promotes FOS binding to intronic Cdh22 regions
  [... "activity promotes FOS binding to intronic regions of the Cdh22 locus, but not of Cntn6"].
- **Localization:** overexpressed CDH22-HA is "primarily restricted to the perisomatic plasma
  membrane" and "clusters at the postsynaptic sites of PV+ inputs in ET neurons" → NEW CC row
  `GO:0098982 GABA-ergic synapse` (IDA; caveat: tagged overexpression construct).
- **Necessity:** shRNA knockdown of Cdh22 reduces mIPSC frequency (−56% Cs-gluconate; −32%
  pharmacologically isolated) and reduces PV+ (Syt2+) perisomatic bouton density, with
  shRNA-resistant rescue → NEW BP row `GO:0007416 synapse assembly` (IMP, involved_in). CDH22 is
  the adhesion molecule physically at the synapse (participation test passes — unlike the TF
  FEZF2, which acts upstream), so `involved_in` is appropriate, as for neuroligins.
- **Specificity:** knockdown of Cdh22 (or Fezf2) does **not** affect mEPSCs
  [... "knockdown of Fezf2 or Cdh22 did not affect mEPSCs"] — the role is inhibitory-specific.
- **Partner:** "CDH22 can form homophilic and heterophilic interactions with other
  cadherin-family members"; Cdh7 is enriched in PV+ basket cells, a candidate heterophilic
  trans-synaptic partner. Left as a `suggested_question` / `knowledge_gap`, not asserted.

### Decisions worth a second look
| Term | Action | Why |
|---|---|---|
| GO:0098978 glutamatergic synapse (IEA, ARBA) | MARK_AS_OVER_ANNOTATED | Unvetted ARBA prediction; experimentally the synaptic role is GABAergic (PV+ postsynaptic localization; knockdown hits mIPSCs not mEPSCs). Not REMOVE — data don't prove absence from glutamatergic synapses. |
| GO:0007155 cell adhesion / GO:0098609 cell-cell adhesion / GO:0016020 membrane | TOO_GENERAL | Entailed by the specific homophilic / calcium-dependent cell-cell adhesion and plasma-membrane terms asserted here. Term-level, not an evidence challenge. |
| GO:0044331 (obsolete) cell-cell adhesion mediated by cadherin | KEEP_AS_NON_CORE | Obsolete term, redundant with the accepted GO:0016339 row. Flagged; not REMOVE (biology correct). |
| GO:0098982 GABA-ergic synapse | NEW (IDA) | Perisomatic PV+ postsynaptic localization of CDH22-HA. |
| GO:0007416 synapse assembly | NEW (IMP) | Knockdown + rescue; PV+ perisomatic inhibitory synapse formation. |

All generic classical-cadherin IBA/IEA/ISO rows kept (ACCEPT for the core homophilic/
calcium-dependent adhesion and cadherin/calcium binding; KEEP_AS_NON_CORE for the peripheral
adherens-junction, catenin-complex, cell-migration/morphogenesis inferences).

### Not done / follow-ups
- No deep-research file generated (none pre-existing; the Kroon paper + UniProt were sufficient
  for the function under review). The embryonic/developmental expression (PubMed:10398531, the
  original PB-cadherin paper) is only lightly reviewed — the GOA carries no experimental rows
  from it.
- A more specific "inhibitory/GABAergic perisomatic synapse assembly" CC/BP term, if one exists
  or is created, would be preferable to GO:0098982 + GO:0007416; recorded as a suggested question.
- Mouse Fezf2 review and the FEZF2→Cdh22→PV-synapse module are handled separately (parent task).
