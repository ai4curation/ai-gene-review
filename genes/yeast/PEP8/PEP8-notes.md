# PEP8 / VPS26 (YJL053W, P40335) curation notes

## Session 2026-11-21: provenance of the research

- Hosted deep research (falcon, perplexity) is not configured in this environment, so
  no `PEP8-deep-research-<provider>.md` file exists and `just deep-research*` was not run.
  Everything below is my own reading of the cached publications and the UniProt record.
- `just mod-description-deep-research yeast PEP8` succeeded and wrote
  `PEP8-deep-research-sgd.md` (SGD hand-written description, fetched 2026-11-21). Its
  claims are checked in the review's `reference_review` for that file.
- `just paint-losses yeast PEP8`: "No IRD or IKR loss on this gene's lineage."
- PubMed E-utilities searches (esearch + esummary):
  - `(Vps26[tiab] OR Pep8[tiab]) AND (yeast[tiab] OR cerevisiae[tiab])` (39 hits)
  - `Vps29[tiab] AND (yeast[tiab] OR cerevisiae[tiab] OR Saccharomyces[tiab])` (34 hits)
  - `retromer[tiab] AND (yeast[tiab] OR cerevisiae[tiab]) AND (Vps35[tiab] OR Vps10[tiab]
    OR Snx3[tiab] OR Grd19[tiab] OR Ypt7[tiab] OR Atg18[tiab] OR Mvp1[tiab] OR tubul*[tiab])`
    (72 hits)
  - `Kovtun O[au] AND retromer[tiab]`, `Leneva N[au] AND retromer`, `Harrison MS[au] AND retromer`
- Cached for this review (beyond the GOA references): PMID:7926738, PMID:11598206,
  PMID:17696874, PMID:17892535, PMID:9105038, PMID:17420293, PMID:36644906, PMID:38598303,
  PMID:35574911, PMID:42135947, PMID:34524084 (new files), and PMID:21062894,
  PMID:22593205, PMID:28100638, PMID:30224749, PMID:40234461 (already in the repository).
  Abstract only: PMID:7926738, PMID:11598206, PMID:17696874, PMID:17892535, PMID:21062894,
  PMID:15965486, PMID:16429126, PMID:18467557, PMID:8649377, PMID:25512334.

## Identity

- 379 aa; SGD standard name PEP8, aliases VPS26, GRD6, VPT4. Belongs to the VPS26 family
  (Pfam PF03643, InterPro IPR028934 Vps26-related, arrestin-like Ig E-set fold;
  PANTHER PTHR12233). Mouse homologue H-beta-58 (Vps26a).
- First cloned as PEP8 [PMID:7926738 "The gene, PEP8, plays a role in the delivery of proteins to the vacuole."];
  the deletion is viable [PMID:7926738 "Disruption of the gene did not affect cell viability."].
- Allelism: [PMID:9700157 "VPS26 is allelic to the PEP8 gene, and is also required for correct sorting of CPY to the vacuole (Bachhawat et al., 1994)."]
  and [PMID:9700157 "grd9 is allelic to vps35, grd6 is allelic to vps26, and grd1 is allelic to vps1."]
- A yeast/mouse chimera is functional [PMID:7926738 "a Pep8p-H < beta > 58 fusion protein in which the carboxy-terminal 85 amino acids of Pep8p were replaced by the carboxy-terminal 115 amino acids of H < beta > 58 was functional"].

## Complex membership (retromer)

- Retromer was defined with Pep8/Vps26 as the p50 subunit
  [PMID:9700157 "This complex, designated here as the retromer complex, assembles from two distinct subcomplexes comprising (a) Vps35p, Vps29p, and Vps26p; and (b) Vps5p and Vps17p."].
  Cross-linking with tagged Vps26 [PMID:9700157 "More recently, cross-linking experiments using a strain expressing an epitope-tagged Vps26p have confirmed that Vps26p does indeed interact with Vps35p, Vps29p, Vps5p, and Vps17p in a large complex (data not shown)."].
  Caveat: there was no Vps26 antiserum, so Vps26 in the trimer was inferred
  [PMID:9700157 "It is possible that Vps26p is also part of the Vps35p/Vps29p complex, although the lack of antiserum against Vps26p precludes direct testing of this hypothesis."].
- Vps26 binds the N-terminal part of Vps35: [PMID:17892535 "the R(98) residue, which is part of a conserved PRLYL motif, is critical for Vps35p binding to Vps26p, while both R(98) and residues 733-944 are needed for efficient binding to Vps29p."]
  and [PMID:17696874 "we have identified a highly-conserved region of Vps35p/VPS35 that is essential for the interaction with Vps26p/VPS26 and for assembly of the retromer complex."].
- Vps26 couples the cargo-selective trimer to the SNX-BAR dimer
  [PMID:11598206 "These domain swap experiments have shown that Vps26p promotes the interactions between the cargo-selective component Vps35p and the structural components Vps5p/Vps17p."].
  Structural view (Chaetomium thermophilum proteins, cryo-ET):
  [PMID:30224749 "The bases of the arches connect to each other and to Vps5 through Vps26"],
  [PMID:30224749 "Vps5 binds to Vps26 at a position analogous to the previously described cargo- and Snx3-binding site"].
  Note: S. cerevisiae genetics say the SNX-BAR association needs Vps29 rather than
  Vps26 [PMID:40234461 "previous studies in S. cerevisiae that have shown the interaction of Retromer with the Vps5–Vps17 proteins requires Vps29 but not Vps26"];
  in vps26Δ Vps35 still co-precipitates Vps5/Vps17/Vps29
  [PMID:9700157 "It is interesting to note that Vps35p continues to coimmunoprecipitate with Vps5p, Vps17p, and Vps29p, suggesting that Vps26p is not essential for formation of the complex."].
  So Vps26 contacts Vps5 in the coat, but the Vps5 N-terminus-to-Vps29 contact is what
  holds the pentamer together biochemically. Both statements should be kept distinct.
- Vps26 stabilises Vps35 and keeps it on membranes
  [PMID:9700157 "Interestingly, a significant proportion of Vps35p becomes soluble in vps26Δ cells (data not shown)"];
  [PMID:22593205 "Vps35 is degraded if it does not associate with Vps26 (Reddy and Seaman, 2001; Restrepo et al., 2007)"].
  Conversely Vps26 needs Vps35 to reach membranes
  [PMID:22593205 "In contrast, Vps26-GFP localizes solely to the cytosol in vps35Δ cells (Figure 4C), indicating that Vps26 requires incorporation into the CSC to target it to membranes in vivo."].
- Vps26 dimerises in the coat; a Vps26-Vps26 interface may hold retromer dimers
  [PMID:36644906, yeast proteins].
- Ypt7 (Rab7): [PMID:21062894 "We also show that Ypt7-GTP specifically binds to the retromer cargo-recognition subcomplex"];
  the Ypt7-binding segment is on Vps35 [PMID:22593205], and
  [PMID:22593205 "Deletion of VPS26 (vps26Δ), which is required for Ypt7 recognition by CSC in vitro (Balderhaar et al., 2010), rescues the morphology of vacuoles when combined with a deletion of VPS17"].
  SNX-BARs displace Ypt7 from cargo-bound CSC during tubulation [PMID:28100638].
- CROP complex (CSC + PROPPIN Atg18):
  [PMID:35466426 "Also, three proteins from the retromer complex (Vps26, Vps35, and Vps29) bound Atg18 more strongly upon triggering vacuole fission."];
  Vps26 and Atg18 puncta partly overlap on the vacuole membrane; CSC mutants have fewer,
  larger vacuoles; vps26Δ suppresses the vps17Δ hyper-fragmentation; CROP formed from pure
  Atg18 and yeast CSC; CROP potentiates Atg18 fission of GUVs [PMID:35466426].
  An Atg18-retromer complex was found independently [PMID:35574911], and an Atg21-retromer
  complex in 2026 [PMID:42135947 "We now found that Atg21 interacts with Pep8/Vps26, Vps29 and Vps35, the components of the cargo selective complex of the retromer."].
- Snx3/Grd19-retromer: the CSC also works with Snx3 for Ftr1 recycling [PMID:17420293].

## Molecular function: cargo recognition

- Pure recombinant Vps26 binds the Chs3 N-terminal YYL sorting signal
  [PMID:28362258 "Binding of Vps26 to GST-Chs3(1-52) is saturable, with an estimated equilibrium dissociation constant, KD, of 19 μM (Figure 6D)."];
  loop 6 (phosphorylated; dephosphorylated by the CDC25-family phosphatase Mih1) tunes the
  affinity; loop-6 deletion or phosphomimetic substitution raises it to ~5 µM
  [PMID:28362258].
- GO:0038024 cargo receptor activity is defined for membrane-spanning receptors ("Cargo
  receptors span membranes"); Vps26 is a peripheral membrane protein
  [PMID:7926738 "Biochemical fractionation indicated that the protein was peripherally bound to membranes."].
  The function is better described as GO:0140312 cargo adaptor activity (is_a
  protein-macromolecule adaptor activity), executed by the CSC as a whole; the PAINT IBAs
  for VPS29 and VPS35 carry it as contributes_to, and the S. pombe GO-CAM uses it for the
  CSC complex (see below).

## Biological processes

1. Endosome-to-Golgi retrieval (core). [PMID:9700157 "In vps26Δ cells ∼90% of Vps10p is found in the vacuole-enriched P13."];
   "phenotype very similar to the vps29 or vps35 mutants" [PMID:9700157].
2. Recycling of endocytosed plasma-membrane proteins (Ftr1, Chs3, Mup1, Can1). In yeast this
   goes through the Golgi [PMID:17420293 "After export from the endosome, Fet3p-Ftr1p transits through the Golgi apparatus for resecretion."].
   [PMID:28362258 "These results indicate that Chs3 is exported from the endosome via a retromer-dependent recycling pathway."].
3. Retention of late-Golgi membrane proteins (grd6 = pep8) [PMID:8649377, PMID:9700157], a
   consequence of the retrieval role.
4. Retrieval from the vacuole membrane, with Vps1 and Ypt7 [PMID:25512334].
5. Vacuole fission through CROP [PMID:35466426].

## Location

- Punctate endosomes in wild type
  [PMID:22593205 "GFP-tagged forms of Vps35 and Vps26 (unpublished data) localize predominantly to punctate endosomes"].
- Vacuole membrane: immunogold [PMID:7926738 "Immuno-gold electron microscopy indicated that the Pep8p localized to vacuolar membranes."],
  partial overlap with Atg18 on the vacuole [PMID:35466426], strong vacuole-membrane
  signal when SNX-BARs are absent [PMID:22593205], and retrieval from vacuoles [PMID:25512334].
- Cytosol: requires Vps35 for membrane association, so there is a soluble pool [PMID:22593205].

## GO-CAMs

- `gocams/index.tsv` has no production GO-CAM containing S. cerevisiae Pep8 (SGD:S000003589,
  P40335) or Vps29 (SGD:S000001054, P38759).
- S. pombe model gomodel:693b3c0900002174 "retrograde transport endosome to Golgi
  (GO:0042147) (partial)" (PomBase): activity 693b3c0900002175 is GO:0140312 cargo adaptor
  activity enabled by the complex GO:0030906 retromer, cargo-selective complex, with has_part
  vps35 (SPCC777.13), vps29 (SPAC15E1.06) and vps26 (SPAC4G9.13c); occurs_in GO:0005768
  endosome; part_of GO:0042147; causally upstream (RO:0012009) of activity 693b3c0900002185,
  GO:0180020 membrane bending activity enabled by GO:0030905 retromer, tubulation complex.
  Evidence on that activity is GO_REF:0000111 (ECO:0000305) with GO:0030906.
  A snx3 (SPBC887.06c) activity, GO:0043495 protein-membrane adaptor activity, is also in
  the model. No S. cerevisiae counterpart model exists.

## Decisions summary

- ACCEPT: retromer complex, cargo-selective complex, endosome, retrograde transport endosome
  to Golgi (all codes), intracellular protein transport (IBA, IEA), CROP complex.
- MODIFY: cargo receptor activity (IDA, PMID:28362258) -> GO:0140312 cargo adaptor activity
  (lateral correction: Vps26 is not a transmembrane receptor).
- KEEP_AS_NON_CORE: vacuole membrane (HDA), cytoplasm (HDA), cytosol (IEA), endosome to
  plasma membrane transport (NAS; route is via the Golgi in yeast), protein retention in
  Golgi (IMP).
- TOO_GENERAL: endomembrane system (NAS); entailed by endosome and retromer complex.
- REMOVE: six bare protein-binding IPI rows (interactions with Vps5 and Vps17 are real and
  are captured by the retromer complex rows).
- No NEW rows. GO:0140572 vacuole fission was considered for the CROP role and not proposed:
  QuickGO lists no S. cerevisiae annotation to it at all (the same query returns 29 yeast
  rows for GO:0030904, so it works), and SGD gives Atg18, the fission-active PROPPIN, only
  GO:0090148 membrane fission. Raised as a suggested question.

## Points for a yeast retromer module (and the VPS1 review)

- Chi et al. 2014 describe retrograde carriers "coated by retromer and Mvp1" and Vps1
  cutting them [PMID:24567361]. Suzuki et al. 2021 instead describe an Mvp1 pathway
  that is distinct from retromer, and find no co-immunoprecipitation between Mvp1 and
  retromer subunits [PMID:34524084 "Here, we reveal that the SNX-BAR protein, Mvp1, mediates an endosomal recycling pathway that is mechanistically distinct from the retromer and Snx4 pathways."],
  [PMID:34524084 "Conversely, when we immunoprecipitated Mvp1-FLAG, retromer subunits Vps5, Vps17-HA, Vps26, Vps29, and Vps35 were not coimmunoprecipitated"].
  The VPS1 review follows Chi et al. ("retromer/Mvp1-coated tubules"). That is not wrong
  for the 2014 data, but a module should present retromer-SNX-BAR and Mvp1 carriers as
  possibly separate routes that both use Vps1.
- Assemblies containing the Vps35-Vps26-Vps29 trimer in S. cerevisiae: pentameric
  retromer with Vps5-Vps17 [PMID:9700157]; Snx3-retromer [PMID:17420293]; CROP with
  Atg18 [PMID:35466426, PMID:35574911]; Atg21-retromer [PMID:42135947]; Ypt7-GTP binding
  [PMID:21062894, PMID:22593205]. PROPPINs and SNX-BARs compete for the trimer
  [PMID:35466426, PMID:35574911].
