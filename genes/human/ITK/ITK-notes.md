# ITK notes

## 2026-10-03 initial review (ADAPTIVE_IMMUNITY, TCR trunk)

ITK (Q08881) is a Tec-family non-receptor tyrosine kinase of T, NK and mast cells
[PMID:8364206 "a unique human tyrosine kinase that is expressed mainly in T lymphocytes (EMT) and natural killer (NK) cells"];
[PMID:18443296 "ITK is expressed in a limited number of cell types, including T cells, NK cells, and mast cells"].

Activation sequence:
- PH domain recruitment to the membrane via PI3K/PIP3
  [PMID:17060314 "results in recruitment of Itk to the plasma membrane via its pleckstrin homology domain"].
- SH2 docking on phospho-SLP-76 activates it
  [PMID:21725281 "Catalytic activation of Itk depends on the inducible interaction of its SH2 domain with the N-terminal tyrosines of SLP-76"];
  [PMID:17420479 "an ongoing physical interaction between SLP-76 and ITK is required to maintain ITK in an active conformation"].
- LCK phosphorylates the activation loop (mouse Tyr511 = human Tyr512)
  [PMID:9312162 "The major site of Lck phosphorylation on Itk was mapped to the conserved tyrosine (Tyr511)"],
  then Tyr180 in the SH3 domain is autophosphorylated
  [PMID:12573241 "for Itk Y180"].

Substrates: PLCG1 Y783/Y775 [PMID:17420479 "ITK efficiently phosphorylated Y(783) and Y(775) of PLC-gamma1"];
LAT C-terminal tyrosines [PMID:12186560]; SLP-76 Y173 [PMID:21725281 "Itk, a kinase that selectively phosphorylated Y173 in vitro"].

Kinase-independent: VAV1 localization and actin polarization
[PMID:15661896 "kinase-independent scaffolding function for Itk in the regulation of Vav"]; [PMID:12682224].
CypA binds ITK SH2 proline and restrains Th2 signaling [PMID:15308100 "CypA bound Itk via the PPIase active site."].

Disease: LPFS1, R335W in the SH2 domain destabilizes ITK; patients lack NKT cells [PMID:19425169].

## Decisions

- MF: GO:0004715 (consistent with LCK/ZAP70); all four rows accepted.
- 25 `protein binding` rows: 2 SLP-76 rows MODIFY to GO:0001784 phosphotyrosine residue binding (SH2 docking);
  rest REMOVED (substrate pairs LAT/PLCG1; SH2 array ERBB2; isolated SH3 hits FASLG/WAS; HSP90/14-3-3 client
  screens; PDZ fragmentomics; XL-MS AHNAK).
- B cell receptor signaling IBA REMOVED: ITK is not expressed in B cells; node PTN000700360 assertion fits BTK/TEC.
- NKT differentiation, cytokine production, gamma-delta T cell activation, T cell activation, adaptive immune
  response, nucleus: KEEP_AS_NON_CORE (necessity/knockout-derived or broad).
- cellular defense response TAS: MARK_AS_OVER_ANNOTATED.
- No NEW annotations proposed. Possible curation item (not a knowledge gap): PIP3 binding by the PH domain
  is well known but the cached evidence (PMID:17060314) shows PH-dependent membrane recruitment, not direct
  lipid binding; not added.
- IntAct flags the P10686 PLCG1 interaction as Xeno (cross-species); recorded as a suggested question.

## Deep research integration (falcon)

Report: `ITK-deep-research-falcon.md` (completed in this session, ~20 min). Used as leads only.

Adopted (traced to primary papers, cached and quoted):
- PLCG1 substrate selection by phosphotyrosine-independent docking of PLCG1 SH2C onto the ITK kinase domain.
  The report cites a 2008 PhD thesis (Min); the peer-reviewed papers are PMID:17439160, PMID:19955438
  ["phosphorylation of PLC-gamma1 by Itk requires a direct, phosphotyrosine-independent interaction between the Src homology 2 (SH2) domain of PLC-gamma1 and the kinase domain of Itk"]
  and PMID:23219468 (docking surface = acidic G-helix patch on ITK). Added to core function 1.
- Human ITK p.Q17X with CD4 lymphopenia and absent iNKT cells: PMID:25061172
  ["illustrating that the absence of iNKT-cells is a primary phenotype of ITK deficiency"]. Added to NKT row (still non-core) and description.
- ITK-Ca2+ switch between Th17 and Treg-like cells (mouse): PMID:39042726. Added as support on the cytokine
  production row, kept non-core (necessity, mouse).

Rejected / not used:
- Drug development content (soquelitinib/CPI-818 Cys442 binding, BSJ-05-037 degrader, NCT trials, ibrutinib): not
  relevant to GO annotation.
- Candidate substrates T-bet, TIM-3, TFII-I: the report itself flags evidence as weak; not added (T-bet left as a
  suggested question).
- 2024 single-patient case report (Di Filippo): confounded, not used.

Report errors / caveats:
- Uses mouse numbering Tyr511 for the LCK-phosphorylated activation-loop tyrosine; human Q08881 is Tyr512.
- Cites a thesis instead of the published papers for the docking mechanism.
- Nothing in the report changed any annotation action; it confirmed the core MF (GO:0004715) and the TCR pathway placement.
