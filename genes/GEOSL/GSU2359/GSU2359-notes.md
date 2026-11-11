# GSU2359 (Q74AJ5) notes

LBNL hackathon, alpha-glucan batch (branch `hackathon/alpha-glucan-batch`), 2026-10-30.
Dashboard gene DPAK01000005.1_6 (exact UniParc match to Q74AJ5, 817 aa, 100% identity and coverage).

## Dashboard call

"Glycoside hydrolase family 57 protein containing a DUF3536 domain, substrate specificity
undetermined." (tier B). GO:0016798 (high), GO:0016052 (medium).

- GO:0016798 hydrolase activity, acting on glycosyl bonds: **COR** (not in GOA, which has only GO:0003824 and GO:0005975).
- GO:0016052 carbohydrate catabolic process: **UNC**. The extractor derived it from the
  words "glycoside hydrolase". Whether the enzyme's net role is catabolic (glycogen
  breakdown) or biosynthetic (feeding TreY/TreZ trehalose synthesis, or glucan remodelling
  by 4-alpha-glucanotransfer) is untested.
- **Verdict: under-called.** Paste-in correction: "GH57 subfamily 6 (DUF3536-type)
  alpha-1,4-glucan-active glycoside hydrolase/4-alpha-glucanotransferase; catalytic
  Glu154/Asp263 conserved; encoded in a treZ-GSU2359-treY-treS(maltokinase) cluster, so
  probably acts on glycogen-derived maltooligosaccharides alongside the TreY/TreZ
  trehalose pathway; exact reaction untested; not an alpha-mannosidase."

## Key evidence

- Catalytic residues (run `gh57-catalytic`): Glu154 (nucleophile, CSR-3 WLAETA) and Asp263
  (proton donor, CSR-4 ATDGETYGHH), at the PF03065 HMM columns where four characterized GH57
  enzymes place theirs (T. litoralis 4AGT Glu123/Asp214, PMID:12618437; Thermococcus,
  Thermus and Pyrococcus branching enzymes). Glu conserved in 583/583 and Asp in 582/583
  aligned UniProtKB DUF3536 proteins, so DUF3536 proteins are not a catalytically dead
  "like" group (cf. PMID:29998051, PMID:32096055). No branching-enzyme CSR-4 fingerprint.
- Subfamily (run `gh57-cazy`): CAZy GH57_6, the "non-specified amylase" subfamily
  [PMID:40187459 "GH57_6, non-specified amylases"]. The characterized GH57_6 members are
  alpha-amylases Pcal_0672, Amo45 (PMID:24829536) and Amy_GH57 (PMID:21455739), and PoGH57.
- Closest characterized relative (run `gh57-identity`): Pontibacter sp. SGAir0037 PoGH57,
  49.4% identity over 806 residues, same DUF3536 domain [PMID:38930854 "The GH57 enzyme
  (further referred to as PoGH57) is predicted to be a DUF3536 (domain of unknown
  function)-containing protein when using BLAST."]. It is active on amylose and MD18, mainly
  hydrolytic, with possible 4-alpha-glucanotransferase activity [PMID:38930854 "The combined
  action of both enzymes indicated that PoGH57 predominantly played a hydrolytic role"].
  Its locus also holds TreS, GlgE, TreZ (GH13_10), TreY (GH13_26) and a GH77. The dashboard
  model saw the 50.7%-identical P. actiniarum homolog but not this characterization.
- Neighbourhood (run `gh57-synteny`, BERDL kbase.ke_pangenome, 1369 DUF3536 clusters, one
  genome per species, 1257 species): treZ(-1)-GSU2359-treY(+1)-treS/mak(+2) in both
  G. sulfurreducens genomes and in G. metallireducens; Pontibacter (5 species) has
  treZ-GH57-treY with malQ and glgB nearby. Family-wide, both treY and treZ are within 5
  genes in only 9.6% of species (either one in 14.6%), and some alpha-glucan marker in
  40.3%; no Cyanobacteriota DUF3536 gene (259) sits near treY/treZ. The trehalose link is
  lineage-specific.
- TreY fusion (run `gh57-fusion-check`): none. All 1369 clusters are DUF3536 + Glyco_hydro_57
  only, none at or above 1200 aa (median 807). The 128 clusters eggNOG labels with the TreY KO
  K06044 are normal length and lack a GH13 domain (KO-transfer artefact).
- Alpha-mannosidase question: no characterized GH57 enzyme (41 in CAZy) has an
  alpha-mannosidase EC; the ECs are 3.2.1.1, 3.2.1.41, 2.4.1.25, 2.4.1.18, 3.2.1.133,
  3.2.1.54, 3.2.1.22. The COG1449 "alpha-mannosidase" and the Gene3D "GH38 N-terminal" hit
  come from fold similarity [PMID:12618437 "domain I of TLGT shares some structural features
  with the catalytic domain of Golgi alpha-mannosidase from Drosophila melanogaster, which
  belongs to glucoside hydrolase family 38"].
- DUF3536: still annotated "functionally uncharacterised" by Pfam/InterPro; in practice it
  marks GH57_6 proteins. Its role (substrate binding, specificity) is unknown.

## Full review decisions

- GO:0003824 IEA: MODIFY to GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds.
  Not alpha-amylase or 4-alpha-glucanotransferase: PoGH57 showed both modes, GSU2359 not assayed.
- GO:0005975 IEA: MODIFY to GO:0030978 alpha-glucan metabolic process. Trehalose
  biosynthetic process and glycogen catabolic process were considered and not proposed.
- Core function: GO:0004553 in GO:0030978.

## Caveats

- Everything is inferred (subfamily, catalytic residues, gene context, one characterized
  relative with low activity). No experiment on GSU2359.
- The ISB network portal assigns GSU2359 a computational "4-alpha-glucanotransferase
  activity" (reported in the deep research); not used, no experimental basis.
- No FEBA/RB-TnSeq fitness data: `just fetch-fitness GEOSL GSU2359` found no local FEBA data
  and the bulk download found none either, so no fitness evidence is available.
- Deep research: falcon and perplexity providers unavailable; the claude-code report was used
  and serves both genes of the family (A2cp1_1916 reuses it). Errors in that report: it
  calls the A2cp1_1916 strain "Anaeromyxobacter sp. K" (it is A. dehalogenans 2CP-1) and
  says its neighbours include a tyrosinase (the pangenome shows ThiD, MarC, a GDSL lipase,
  ABC transporter genes); it says no DUF3536 protein has been characterized, missing PoGH57
  (PMID:38930854) and Amo45 (CAZy GH57_6). It did correctly find Glu154/Asp263 by motif
  matching and the treZ-treY-treS neighbourhood.
- PaperBLAST's only GSU2359 hit (PMID:20667132) is a comparative-genomics mention
  (high-histidine-demand gene), not functional.

## Files and runs

- BERIL runs (projects/hackathon): `20261030T234043Z-gh57-catalytic`,
  `20261030T234824Z-gh57-identity`, `20261030T234844Z-gh57-cazy`,
  `20261030T233053Z-gh57-synteny`, `20261030T234618Z-gh57-fusion-check`. Scripts in
  `src/gh57/`, copied to `GSU2359-bioinformatics/scripts/`.
- QC: validate, validate-references, validate-terms, validate-predictions, render,
  validate-history all pass.
