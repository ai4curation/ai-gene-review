# Xirp2 (mouse, Q4U4S6) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Xirp2 is the experimental reference for the bovine ProtNLM2 benchmark gene E1BL04
(same PANTHER subfamily PTHR22591:SF1). This review was done without opening any ProtNLM2 file.

### Deep research

`just deep-research-falcon mouse Xirp2 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" (Edison API 403) and perplexity-lite returned HTTP 401 (insufficient quota).
No deep-research file exists. The review uses the cached primary literature instead; full text was
read for PMID:20360251, 25772365, 29306897 and 37294664. Abstracts only for 17046827, 17766470,
21689717, 15454575 and 25653358. A PubMed search (Xirp2/myomaxin/mXinbeta, 75 hits) turned up
PMID:25653358 (Francis 2015, a second mouse knockout) and PMID:23985323 (nebulin/nebulette SH3 ligands),
which were cached.

### Evolutionary grounding

- PANTHER: PTHR22591 (XIN), subfamily SF1 (XIRP2). Human XIRP2 A4UGR9 is in SF1 too; XIRP1 (human Q702N8,
  mouse O70373) is in SF2 [file:interpro/panther/PTHR22591/PTHR22591-entries.csv].
- PAINT: PTN000502290 is seeded by both human XIRP1 (SF2) and XIRP2 (SF1), so it sits at or near the
  family root, above the SF1/SF2 split. It carries stress fiber and focal adhesion (colocalizes_with),
  actin filament binding (seeded by both), and actin filament organization (seeded by XIRP1 only).
  Mouse Xirp2 descends from this node and nothing suggests loss.
- Actin filament binding is shown directly for Xin repeats, and "Human XIRP2 contains 28 Xin repeats with
  properties identical to those of Xin" [PMID:15454575]. No co-sedimentation assay on the mouse Xirp2 protein
  itself was found. The mouse data are localization to actin structures and loss-of-function actin
  disorganization [PMID:25772365 "In Xirp2−/− stereocilia, however, filament spacing was less regular, with numerous gaps and disordered regions"].

### Experimentally established in mouse (reference set for transfer)

- Z disc/costamere localization and binding to alpha-actinin-2 [PMID:17046827 "interacts with the sarcomeric Z-disc protein, alpha-actinin-2"].
- Intercalated disc localization, and the requirement for disc maturation and terminal N-cadherin/Xirp1 localization
  [PMID:20360251 "These results suggest that mXinβ is essential for promoting and maintaining the localization of adherens junctional components and mXinα to the mature intercalated discs."].
- Co-IP with Nav1.5 and Kv1.5 from heart lysate; conduction defects in the knockout [PMID:29306897].
- Stereocilia, cuticular plate and hair-cell junction localization; isoforms are distributed differently [PMID:25772365, PMID:25653358, PMID:37294664].
- Short (LIM/CTD) isoform: recruited to noise-induced F-actin gaps, and its CTD pulls down monomeric gamma-actin (G13R)
  [PMID:37294664 "The C-terminal domain (CTD) of XIRP2 is sufficient to pull down monomeric γ-actin."]. This is
  isoform-specific. The bovine E1BL04 model reportedly lacks the C-terminal LIM region, so this function should
  not be transferred to E1BL04.

### Decisions

- Organismal knockout phenotypes: ventricular septum development was marked over-annotated; cardiac muscle tissue
  morphogenesis was kept as non-core. Neither is a core process.
- Generic junction terms (cell junction, anchoring junction) were changed to intercalated disc plus cell-cell junction.
- Cytosol (Reactome TAS) was changed to stereocilium.
- Protein binding: the eEF1A pulldown hit was removed; the Kcna5/Scn5a co-IPs were changed to transmembrane transporter
  binding (GO:0044325, the current label of the former ion channel binding term).
- NEW (location only): intercalated disc, stereocilium, cuticular plate. NEW MF: actin monomer binding (isoform Q4U4S6-3).
- Stereocilium maintenance (GO:0120045) was considered but not added. MGI curated both hair-cell knockout papers and did
  not assign it, and the comparator set is small (Tprn, Clrn2, Pjvk, Elmod3). It is raised as a suggested question.
