# PEP1 / VPS10 (YBL017C, P32319) curation notes

## Session 2026-11-21: provenance of the research

- Hosted deep-research providers (falcon, perplexity) are not configured in this
  environment, so `just deep-research*` was not run and no
  `PEP1-deep-research-<provider>.md` file exists. Everything below is my own reading of
  the cached publications and the UniProt record.
- `just mod-description-deep-research yeast PEP1` succeeded and wrote
  `PEP1-deep-research-sgd.md` (SGD hand-written description). Its claims are checked
  below and in the review's `reference_review`.
- `just paint-losses yeast PEP1`: "No IRD or IKR loss on this gene's lineage."
- PubMed E-utilities searches (esearch + esummary): `Vps10[tiab] AND Saccharomyces[tiab]`,
  `Vps10p[tiab]`, `Vps10[ti]`, `Vps10p[ti]`, `Cooper AA[au] AND Stevens TH[au] AND Vps10p`,
  `Cereghino JL[au] AND Vps10p`, `Seaman MN[au] AND Vps10p`, `Deloche O[au] AND Vps10p`,
  `Suzuki SW[au] AND retromer AND bipartite`, `Nothwehr SF[au] AND Vps35p AND direct
  interaction`, `Hong E[au] AND Kaiser CA[au] AND misfolded vacuole`,
  `Vps10[tiab] AND retromer[tiab] AND yeast[tiab]`, `Vps10[tiab] AND Gga[tiab]`, and
  `(Vps10 OR Vps10p) AND (AP-3 OR AP3 / Apl5 / Apl6 / Apm3 / Aps3 / ALP pathway /
  misfolded / quality control)`.
- Cached with `just fetch-pmid` (new): PMID:8534908, PMID:8636229, PMID:8662642,
  PMID:10095782, PMID:9105038 (full text), PMID:11038177 (full text), PMID:11179429,
  PMID:12475953, PMID:8909538, PMID:31337624 (full text). The others are abstract only
  (PMC refused the HTML fallback with 403).
- Already tracked in the repository and added to this sparse checkout: PMID:35175277
  (Eising et al. 2022, full text) and PMID:9700157 (Seaman et al. 1998, full text).
- PMID:25533483 (Dhungel et al. 2015, the TAS row) is cached abstract-only. I read the
  full text through NCBI efetch (db=pmc, PMC4289081) into the scratchpad, not into the
  repository. The relevant author statement is: "Vps10 helps sort misfolded proteins from
  the trans-golgi network (TGN) to prevacuolar endosomes for degradation (Reitz, 2012)".
  Because the cached copy lacks it, the review row quotes other papers instead.

## Identity and domain architecture

- 1,579-residue type I transmembrane glycoprotein: signal peptide 1..21, lumenal 22..1397,
  TM helix 1398..1414, cytoplasmic tail 1415..1579 (UniProt, sequence analysis).
- Lumenal region: two Vps10p domains (23..718 and 728..1380), each a 10-bladed
  beta-propeller followed by 10CCa/10CCb cysteine-rich modules (PROSITE PS52072). UniProt
  DOMAIN: "The lumenal domain contains two regions of approximately 650 AA that exhibit 20%
  identity. The cytoplasmic domain serves as a Golgi retention/recycling signal."
- Founding member of the Vps10p-domain receptor (sortilin) family; PANTHER PTHR12106
  (sortilin related), subfamily SF27. Paralogs in S. cerevisiae: VTH1 (YIL173W,
  SGD:S000001435, P40438) and VTH2 (YJL222W, SGD:S000003758, P40890), both donors of the
  PTN000950011 IBA rows.

## Molecular function: vacuolar sorting receptor

- Original identification [PMID:8187177 "The S. cerevisiae VPS10 (vacuolar protein sorting)
  gene encodes a type I transmembrane protein of 1577 amino acids required for the sorting
  of the soluble vacuolar protein carboxypeptidase Y (CPY)."]
- Direct binding, signal-dependent [PMID:8187177 "Chemical cross-linking studies
  demonstrate that Vps10p and the Golgi-modified precursor form of CPY directly interact. A
  single amino acid change in the CPY vacuolar sorting signal prevents this interaction."]
- Stoichiometric binding [PMID:8636229 "In vitro equilibrium binding studies established
  that the 1,380-amino acid lumenal domain of Vps10p binds CPY precursor in a 1:1
  stoichiometry"]. Vps10 is made 20-fold more slowly than CPY, so it must recycle.
- Ligands beyond CPY: proteinase A [PMID:8662642 "Vps10p and proteinase A interact directly
  and specifically as shown by chemical cross-linking"], aminopeptidase Y
  [PMID:10095782 "Moreover, we show that aminopeptidase Y (APY) is a ligand of Vps10p."].
- Domain mapping: lumenal domain 2 binds CPY, PrA, APY and invertase hybrids; two binding
  sites, one possibly recognising unfolded structure [PMID:10095782 "we suggest that an
  unfolded structure in these ligands is recognized by Vps10p"].
- Vacuolar proteomics (QPrevail) of vps10 cells [PMID:35175277 "Our data suggest that most
  luminal vacuolar proteins are either transported by the Vps10 sorting receptor or the CVT
  pathway."]. Cargoes include CPY, Pep4, Yhr202w, Ydr415c, Atg42, Ape3 and Npc2, mostly
  through domain 2; domain 1 deletion affects only Ydr415c.
- Misfolded lumenal proteins [PMID:8909538 "Together these findings suggest that yeast have
  a salvage pathway for degradation of nonnative luminal proteins by receptor-mediated
  transport to the vacuole."].
- GO: GO:0010209 vacuolar sorting signal receptor activity ("Binding to a vacuolar sorting
  signal, a specific peptide sequence that acts as a signal to localize the protein within
  the vacuole", checked in OLS) fits. ACCEPT the IMP row.

## Itinerary: TGN -> late endosome (PVC) -> TGN

- Steady state: late Golgi (TGN). [PMID:8187177 "Subcellular fractionation indicates that
  the majority of Vps10p is localized to a late Golgi compartment where vacuolar proteins
  are sorted."]; [PMID:8636229 "Vps10p has been immunolocalized to the late-Golgi
  compartment where CPY is sorted away from the secretory pathway."]; about 85-90% in the
  Golgi-enriched P100 fraction [PMID:9105038].
- Exit from TGN in clathrin-coated vesicles [PMID:11179429 "Our results suggest that CCVs
  mediate Vps10p transport from the TGN to the endosome independent of direct interactions
  between Vps10p and clathrin coats."], Gga-dependent [PMID:35175277 "Taken together,
  QPrevail revealed Vps10 as one of very few transmembrane proteins that require the Gga
  proteins for sorting."]. In clathrin mutants Vps10 is rerouted via the plasma membrane
  [PMID:12475953].
- Retrieval from the PVC: needs the cytoplasmic tail [PMID:8534908, PMID:8636229 (YSSL
  signal)], retromer [PMID:9105038; PMID:9700157 "Disruption of VPS29, VPS30, or VPS35
  resulted in almost complete mislocalization of the Vps10 receptor to the vacuole, causing
  CPY to be secreted from the cell."]. Retrieval also from the vacuole membrane, with
  retromer, Vps1 and Ypt7 [PMID:25512334].
- Cargo recognition by retromer: allele-specific suppression between Vps35 and the Vps10
  tail (Q1499L suppresses vps35-105) [PMID:11038177 "The allele-specific suppression data
  argue that the interaction between the cytosolic domains of A-ALP and Vps10p with Vps35p
  is direct rather than being mediated by another member of the complex."], but direct
  cross-linking of Vps10 to Vps35 failed [PMID:11038177 "Thus far we have been unsuccessful
  at reproducibly demonstrating cross-linking between Vps10p and Vps35p."].
- Bipartite recycling signal 1428-FGEIRL-1433 + 1492-YSSL-1495, recognised through Vps26
  (F334, L285) and Vps35; Vps10-GFP coprecipitates with Vps26-FLAG only when Vps35 is present
  and with Vps35-FLAG only when Vps26 is present; Vps10 recycling needs both Vps5 and Vps17
  [PMID:31337624]. Vps5-FLAG binding to Vps10-GFP is lost in vps29 cells [PMID:31337624].
- The location terms: TGN membrane (GO:0032588) and late endosome membrane (GO:0031902,
  whose search synonym in OLS is "prevacuolar compartment") are both supported by a TM
  helix plus sub-organelle assays. Neither is in GOA, so both are proposed as NEW (IC).

## Phenotypes and process terms

- vps10 secretes >90% of CPY and ~50% PrA [PMID:8636229]; the PrA effect is saturable and
  partly redundant with Vth1/Vth2 and Vps10-independent routes [PMID:8662642].
- Pexophagy/mitophagy IMP rows [PMID:31332264]: vps10 reduces Pex11-GFP and Tom70-GFP
  processing (about 75% of wild type for pexophagy) with no effect on bulk autophagy or
  ribophagy, and the authors attribute it to poor Pep4 delivery [PMID:31332264 "The results
  show that Vps10-mediated targeting of Pep4 limits the proteolytic capacity of the vacuole
  in a substrate-dependent manner."]. Vps10 does none of the work of mitophagy or pexophagy:
  the hydrolase it delivers does. MARK_AS_OVER_ANNOTATED (same approach as the VPS1 BIR row).
- Vti1 two-hybrid (IPI protein binding, PMID:9199167): the tail bait found Vti1, but the
  same paper could not confirm binding [PMID:9199167 "Specific binding between Vps10p and
  Vti1p could not be detected using either chemical crosslinking followed by
  immunoprecipitation or in vitro binding assays with the soluble cytosolic domains."].
  REMOVE under the protein-binding policy.
- Vacuole HDA row (SWAT library, PMID:26928762): NOP1-promoter, SP-GFP fusion, so
  overexpressed. Overexpressed Vps10 goes to the vacuole and is degraded [PMID:8534908
  "Immunofluorescence studies indicate that overexpressed receptor is delivered to the
  vacuole."], while native-promoter Vps10-GFP is punctate (Golgi/endosome) in wild-type
  cells [PMID:31337624]. A small pool does reach purified vacuoles (Eising 2022 detect it in
  WT vacuoles; it is depleted from gga1 gga2 vacuoles) and is retrieved [PMID:25512334].
  MARK_AS_OVER_ANNOTATED, not REMOVE.
- Cytosol (GO_REF:0000108, inferred from Golgi to endosome transport, which is_a cytosolic
  transport): wrong for an integral membrane protein. REMOVE.
- Vps10 is the cargo of retrograde endosome-to-Golgi transport, not a participant. No NEW
  row for GO:0042147: the participation test fails (retromer, Vps1 and Mvp1 do the work;
  Vps10 is what is moved). The tail signal is a property of the cargo.

## SGD description (PEP1-deep-research-sgd.md): claim check

1. "Type I transmembrane sorting receptor for multiple vacuolar hydrolases": verified
   (PMID:8187177, PMID:8636229, PMID:10095782, PMID:35175277).
2. "plays role in post-ER quality control in the Golgi, involved in protein targeting from
   the endoplasmic reticulum to the vacuole for degradation": supported by PMID:8909538
   (misfolded invertase-lambda repressor hybrids diverted to the surface in vps10 cells).
3. "cycles between late-Golgi and prevacuolar endosome-like compartments": verified
   (PMID:8636229, PMID:8534908).
4. "targeted to vacuole via AP-3 pathway": not traced to any paper (searches above), and
   contradicted. In vps35 cells Vps10 reaches the vacuole through the PVC and needs the PVC
   t-SNARE Pep12 [PMID:9105038], which the AP-3 route bypasses; QPrevail places Vps10 with
   the few endosomal-pathway (Gga-dependent) vacuolar proteins, in contrast to the AP-3
   cargoes [PMID:35175277]. Recorded as a WRONG_STATEMENT source defect, PROBABLE, CHECK.

## GO-CAMs

- `gocams/index.tsv` has no production GO-CAM containing S. cerevisiae PEP1/Vps10
  (SGD:S000000113, UniProtKB:P32319) or S. pombe vps10 (PomBase:SPBC16C6.06).
- S. pombe model 693b3c0900002174 "retrograde transport endosome to Golgi (GO:0042147)
  (partial)" has the retromer cargo-selective complex (GO:0030906; has_part SPCC777.13,
  SPAC15E1.06, SPAC4G9.13c) with GO:0140312 cargo adaptor activity, occurs_in endosome, and a
  retromer tubulation complex; no activity has a cargo has_input, so vps10 is absent.
- S. pombe model 6918f23700004102 has mvp1 (SPAC3A11.06) with cargo adaptor activity part_of
  GO:0042147.
- Human SORL1 appears in model 67086be200002981 with GO:0140318 protein transporter activity
  part_of GO:0042147, and in 68d5ebd600002260 with GO:0038024 cargo receptor activity. Mouse
  Sorl1 is in 62f58d8800001119. These are the nearest sortilin-family GO-CAM precedents.

## Facts for a yeast retromer module

- Vps10 is the reference cargo of yeast retromer: retrieval needs Vps35, Vps26, Vps29
  (CSC) and Vps5 and Vps17 (SNX-BAR) [PMID:9105038, PMID:9700157, PMID:31337624], and Vps1
  for carrier fission (VPS1 review; PMID:25512334).
- Cargo recognition: bipartite FGEIRL + YSSL tail signal read by Vps26 (F334, L285) and
  Vps35 [PMID:31337624]; Vps35 genetic suppression [PMID:11038177].
- Anterograde leg: clathrin/Gga-dependent TGN-to-PVC carriers [PMID:11179429,
  PMID:35175277].
- No disagreement with the VPS1 review was found: it describes Vps1 cutting retromer/Mvp1
  tubules that return Vps10, and recycling of Vps10 from vacuoles with retromer and Ypt7
  (PMID:25512334), which matches the PEP1 literature.

## Decisions summary (see review YAML)

- ACCEPT (9): GO:0010209 vacuolar sorting signal receptor activity (IMP); GO:0006623
  protein targeting to vacuole (IBA, IMP); GO:0006895 Golgi to endosome transport (IBA,
  TAS); GO:0006896 Golgi to vacuole transport (IBA); GO:0005794 Golgi apparatus (IBA, IDA,
  IEA; root organelle term kept, sub-compartment added beside it).
- TOO_GENERAL (5): GO:0016020 membrane (IBA, IEA); GO:0007034 vacuolar transport (IEA ARBA
  and IMP; the IMP row's evidence is already captured by the IMP protein targeting to
  vacuole row from the same paper, so both rows take TOO_GENERAL to stay consistent);
  GO:0016192 vesicle-mediated transport (IEA ARBA).
- MARK_AS_OVER_ANNOTATED (3): mitophagy and pexophagy (IMP, indirect via Pep4 delivery);
  fungal-type vacuole (HDA, overexpression screen).
- REMOVE (2): GO:0005515 protein binding (IPI, Vti1 two-hybrid not confirmed by the same
  paper); GO:0005829 cytosol (IEA GO_REF:0000108, wrong for an integral membrane protein).
- NEW (2, IC): GO:0032588 trans-Golgi network membrane; GO:0031902 late endosome membrane.
- Core function: GO:0010209 at GO:0032588, directly involved in GO:0006623, GO:0006896 and
  GO:0006895.
