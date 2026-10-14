# GRAP2 (GADS) review notes

## Identity and architecture

- Human GRAP2, UniProt O75791; aliases GADS, GrpL, Grf40, Mona, GRID. GRB2 family (PANTHER PTHR46037).
  SH3 (1-56), SH2 (58-149), Gln/Pro-rich linker (~143-244), C-terminal SH3 (271-330).
- Hematopoietic-restricted: [PMID:9878555 "can only be detected in tissues rich in leukocytes and in two leukemia cell lines"].
- Independent clonings: Gads from a phospho-SHC screen [PMID:9872323 "Gads is most highly expressed in the thymus and spleen of adult animals"], Mona from a phospho-Fms screen [PMID:9857184 "Mona interacts with activated Fms on phosphorylated Tyr697, which is also the Grb2-binding site"], GrpL [PMID:10209041], Grf40 [PMID:10224278].

## Core mechanism: LAT-GADS-SLP-76 bridge

- C-SH3 binds SLP-76 RxxK motif with high affinity, constitutively:
  [PMID:10021361 "The constitutive interaction between Gads and SLP-76 was mediated by the carboxy-terminal SH3 domain of Gads and a 20 amino-acid proline-rich region in SLP-76"];
  [PMID:12176364 "a nonproline-based R-X-X-K motif found in SLP-76 binds to the Gads carboxy-terminal SH3 domain with high affinity"];
  [PMID:17235283 "In signaling from the T-cell receptor (TCR), the Gads C-terminal SH3 domain binds a core RxxK sequence motif in the SLP-76 scaffold"].
- SH2 binds phospho-LAT: [PMID:10811803 "Tyr(171), and Tyr(191), but not Tyr(226), are necessary for Gads binding"];
  [PMID:15029250 "Gads-SH2 binds LAT tyrosine phosphorylation sites 171 and 191 with higher affinities than the other sites"].
  Numbering: these are short-isoform LAT numbers; in canonical LAT O43561-1 they are Y200/Y220 (and Y132 -> Y161, Y226 -> Y255), per the LAT review.
- Knockouts: [PMID:11239162 "Immunoprecipitation experiments revealed that the association between SLP-76 and LAT was uncoupled in GADS- thymocytes"];
  human Jurkat KO [PMID:25452106 "Gads conferred responsiveness to weak TCR stimuli, leading to PLC-γ1 phosphorylation and calcium flux"].
- Mast cells: [PMID:18664516 "Bone marrow-derived mast cells from Gads(-/-) mice failed to induce Ca(2+) mobilization, degranulation and cytokine production upon cross-linking of FcepsilonRI"].
- Platelets: partial/redundant role [PMID:18826392 "Gads plays a key role in linking the adapter LAT to SLP-76 in response to weak activation of GPVI and CLEC-2"]; [PMID:31948362 "only partial defects were seen in Grb2 or Gads single-deficient platelets"].
- Review: [PMID:31402911 "Gads is positively regulated by dimerization, which promotes its cooperative binding to LAT"].
- Other partners: HPK1 via C-SH3 [PMID:11313918]; CD6 pY629 via SH2 [PMID:28289074]; ITK phosphorylates Gads Y45 [PMID:33931484].
- Does not bind SOS: [PMID:9872323 "Gads does not interact with Sos, Cbl or Sam68"]; [PMID:10209041 "GrpL can be coimmunoprecipitated with SLP-76 but not with Sos1 or Sos2"].

## Curation decisions (summary)

- 97 GOA rows: 52 `protein binding` IPI rows. Mechanistic SLP-76 rows (PMID:17235283, 17010654, 20534575) -> MODIFY to
  signaling adaptor activity (GO:0035591), consistent with LCP2. Phosphopeptide/SH2 assays (LAX1, ERBB2 array, KIT/GAB1 FP) ->
  MODIFY to phosphotyrosine residue binding (GO:0001784). All other screen-derived rows removed as uninformative.
- Nucleus/nucleoplasm/endosome kept as non-core (overexpression/HPA observations, no function). Ras signal transduction and
  cell-cell signaling (TAS, cloning paper) marked over-annotated.
- NEW: T cell receptor signaling pathway (GO:0050852), Fc-epsilon receptor signaling pathway (GO:0038095), part_of TCR
  signalosome (GO:0036398). Comparator: LAT and LCP2 (same-complex adaptors) carry all three; GADS does part of the work
  (physical bridging), so the participation test is met.
- GPVI/CLEC-2 and M-CSF receptor roles left as suggested questions (partial/redundant phenotypes or overexpression only).

## Deep research integration (falcon)

Report: `GRAP2-deep-research-falcon.md` (Edison/Falcon, completed 2026-10-03 after ~21 min). It arrived after the
annotation review was drafted; every substantive claim was checked against primary literature before use.

Adopted (traced to primary papers, cached and quoted in the review):
- Human HuT78 GADS knockdown: reduced SLP-76/PLCG1 recruitment to LAT, calcium and IL-2/IFN-g, with preserved SLP-76/PLCG1
  phosphorylation and adhesion [PMID:25636200 "The defect in cytokine production occurred because of impaired calcium mobilization due to reduced recruitment of SLP-76 and PLC-γ1 to the LAT complex"].
  Added to the NEW TCR signaling row and core function 1.
- Full-length GADS-SLP-76 Kd 9 nM and the circular LAT-GADS-SLP-76-PLCG1 quaternary complex
  [PMID:30510001 "The K d for SLP-76 FL /Gads FL binding was 9 nM"]. Added to core function 1.
- Jurkat GRB2-family knockouts / AP-MS: [PMID:37006259 "our analysis showed that 100% of the SLP76 molecules are constitutively associated with GADS"];
  GADS loss remodels the SLP76 interactome but minimally affects proximal events. Added to core function 1 and a suggested question.
- FLT3 pY955/pY969 binding (PMID:26895103): recorded as a suggested question only (overexpression/xenograft); explains the
  Reactome "Active FLT3 binds to GRAP2" cytosol row.

Not adopted / limitations:
- CD28 binding (Ellis et al. 2000, J Immunol, DOI 10.4049/jimmunol.164.11.5805): no PMID resolved for the DOI via the ID
  converter; not cited. It is consistent with the Reactome "Gads binds CD28" row (cytosol, accepted) and with PMID:31402911.
- HPK1-mediated phosphorylation of GADS T262: not traced to a cached primary paper; PMID:25452106 reports the T262 site by MS
  only. Not used.
- Microcluster dynamics drawn from a 2000 thesis (liu2000) cited by the report: not used.

Report errors / caveats:
- LAT Y171/Y191 given in short-isoform numbering without the canonical O43561-1 equivalents (Y200/Y220).
- Mast-cell phenotype attributed to the Yablonski review; the primary Gads-/- mast cell paper is PMID:18664516 (used instead).
- No outright factual errors found in the claims checked.
