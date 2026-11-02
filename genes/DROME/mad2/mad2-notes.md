# mad2 (DROME) review notes

- UniProt Q9VRQ2 (TrEMBL, unreviewed) confirmed by fetch-gene: FlyBase FBgn0035640, GeneID 38656.
- No deep-research provider was available. The manual synthesis is in `mad2-deep-research-manual.md`.
- Abstract-only papers: PMID:15075237, 15886105, 17182852, 17417628, 18555779. Their key claims
  are stated explicitly in the abstracts.
- Full texts read: PMID:19273613 (key paper), 31913420, 18562695, 17576797, 26714316, 24335260,
  20421417, 27159240.

## Decisions

- Kinetochore rows and SAC signaling rows: ACCEPT. These are the core activity.
  [PMID:17182852 "Depletion of Mad2 by RNAi from S2 cells shows that it is essential to prevent mitotic exit after spindle damage"]
- GO:0090266 (regulation of the SAC), GO:0007346 and the IEA GO:1901991 rows: MODIFY to GO:0007094.
  Mad2 is a component of the checkpoint signal, not a regulator of it, and GO:0007094 is a
  descendant of the two broader terms.
- GO:1901673 regulation of mitotic spindle assembly:
  - IGI row from PMID:18555779: MARK_AS_OVER_ANNOTATED. Mad2 contributes only the mitotic delay.
  - IMP row from PMID:19273613: MARK_AS_OVER_ANNOTATED. The phenotype is a change in anaphase
    spindle elongation, not in spindle assembly.
- GO:0051276 chromosome organization (PMID:24335260): MARK_AS_OVER_ANNOTATED. Mad2 RNAi was only a
  tool to induce CIN.
- GO:0048133 male GSC asymmetric division (PMID:26714316): MARK_AS_OVER_ANNOTATED. The only
  evidence is overexpression rescue of the Mtor mutant.
  [PMID:26714316 "Expression of Mad2 and Mps1 of the SAC complex effectively rescued the GSC loss phenotype associated with loss of Mtor function."]
- Protein binding (Mtor co-IP): REMOVE, per the protein-binding policy.
- Peripheral locations (nucleus, nucleoplasm, NE, cytoplasm, spindle, pole, K-fibre, spindle
  matrix): KEEP_AS_NON_CORE.
- NEW MF GO:1990948 ubiquitin ligase inhibitor activity (IC). It rests on Cdc20 binding
  [PMID:20421417] and the premature cyclin B degradation in the null [PMID:17417628], together with
  the conserved MAD2 mechanism. No NEW process terms are proposed.

## 2026-10-28 review fixes

GO:0007346 regulation of mitotic cell cycle (IMP, PMID:19273613) changed MODIFY -> TOO_GENERAL to match Mgtor (GO:0007094 already asserted); moved the &id010 anchor to the GO:0090266 row. Only one GO:0007346 row exists.
