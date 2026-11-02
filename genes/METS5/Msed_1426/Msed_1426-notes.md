# Msed_1426 (A4YGN2, ACAR_METS5) — curation notes

Metallosphaera sedula DSM 5348. ARCHAEA project gene; grounds the acryloyl-CoA reductase
step of `modules/hydroxypropionate_hydroxybutyrate_cycle.yaml`.

**Provenance note:** automated deep research was unavailable in this session; no
`-deep-research-*.md` file was created. Literature was searched manually (Europe PMC REST
search for "Msed_1426" and "acryloyl-CoA reductase Sulfolobales"; NCBI E-utilities was
returning backend errors) and read from cached full texts. PMIDs 20008169 (transcriptomics)
and 40192334 (Pyrococcus 1-propanol engineering) were found but could not be cached
(`just fetch-pmid` failed), so they are not cited.

## Identity and evidence

- Swiss-Prot, EC 1.3.1.84, RHEA:26454 (propanoyl-CoA + NADP+ = acryloyl-CoA + NADPH + H+).
  Zinc-containing alcohol dehydrogenase (MDR) family; InterPro IPR053496
  Acryloyl-CoA_Reductase_Zn-ADH; NCBIfam NF041172 AcrlCoa_red_Thmprot; PANTHER PTHR42940:SF8.
- Native enzyme enriched >200-fold from autotrophic M. sedula; the 40 kDa band was first
  matched to S. tokodaii ST0480 and, when the genome appeared, to Msed_1426:
  [PMID:19429610 "Reinterpretation of the fingerprint mass spectrometry data identified the same gene (Msed_1426) in M. sedula as a best hit (100% identity and 73% coverage)."]
- Recombinant work in PMID:19429610 used the **S. tokodaii ortholog** (ST0480, Q975C8):
  [PMID:19429610 "A gene encoding a protein with 76% amino acid sequence identity to the identified acryloyl-CoA reductase of S. tokodaii is present in the genome of M. sedula (gi 146304192; Msed_1426)."]
  So kinetics, cofactor specificity, monomer state and zinc content are from ST0480; UniProt
  marks these as ECO:0000250 from Q975C8. The activity of the native M. sedula enzyme is direct
  (Msed_1426-containing fraction).
- Recombinant **M. sedula** Msed_1426 was later obtained by co-expression with Msed_1424
  and assayed: [PMID:27771364 "ACR could not be expressed in soluble, active form in E. coli, even though several vectors and different expression conditions were tried."]
  [PMID:27771364 "For ACR, the Vmax for acryloyl-CoA was 7.6 μmol min−1 mg−1, compared to the previously reported values of 3.0 μmol min−1 mg−1 for the native M. sedula ACR and 18.7 μmol min−1 mg−1 for the version from S. tokodaii (Teufel et al., 2009)."]
- Reaction: [PMID:19429610 "Acryloyl-CoA reductase (E.C. 1.3.1.x) catalyzes the following irreversible reaction: acryloyl-CoA + NADPH + H + → propionyl-CoA + NADP + ."]
- Cofactor specificity: **no NADH activity**:
  [PMID:19429610 "The enzyme did not act on either NADH or crotonyl-CoA."]
  [PMID:19429610 "The enzyme does not require cofactors and does not use NADH as an electron donor."]
  Not acting on crotonyl-CoA matters physiologically (crotonyl-CoA is an intermediate of the
  second half of the cycle).
- Zinc: [PMID:19429610 "a metal analysis (27 elements) of acryloyl-CoA reductase by plasma emission spectroscopy revealed the presence of 0.8 mol of Zn 2+ per mol of enzyme monomer, whereas other metals could not be detected."]
  Catalytic GHE motif with Cys38/Cys146; structural site with Asp90 replacing the first Cys:
  [PMID:19429610 "An alignment of the acryloyl-CoA reductase with the well-studied horse liver alcohol dehydrogenase shows the presence of the strictly conserved sequence motif GHE of the catalytic zinc binding side (amino acid position 59 to 61) with two flanking cysteines (amino acids 38 and 146)."]

## Role in the 3HP/4HB cycle

- Autotrophic up-regulation: [PMID:19429610 "The reductase activity may limit the conversion rate and clearly is more than 10-fold downregulated in heterotrophically grown cells."]
- [PMID:19429610 "These results are consistent with the proposed function in autotrophic CO 2 fixation."]
- Three separate enzymes (HPCS Msed_1456, HPCD Msed_2001, ACR Msed_1426) replace the
  trifunctional Chloroflexus propionyl-CoA synthase, so the archaeal and Chloroflexus cycles
  evolved independently:
  [PMID:19429610 "Acryloyl-CoA reductase, a member of the zinc-containing alcohol dehydrogenase family, reduces acryloyl-CoA with NADPH to propionyl-CoA."]
- Kinetic model of the cycle uses Msed_1426 as acr:
  [PMID:27771364 "The genes hpcs (Msed_1456), hpcd (Msed_2001), acr (Msed_1426), mcr (Msed_0709), and ssr (Msed_1424) were amplified from genomic DNA using the primers listed in Supplementary Table S1."]

## GO term choices

- GO:0043957 acryloyl-CoA reductase (NADPH) activity (EXP and IEA from RHEA:26454): ACCEPT;
  the definition (acryloyl-CoA + NADPH + H+ = propionyl-CoA + NADP+) is exactly the reaction.
  The module's MF term therefore fits.
- GO:0043958 acryloyl-CoA reductase (NADH) activity, IDA from PMID:19429610: the paper
  (full text cached and read) explicitly says the enzyme does not use NADH. Since the
  acryloyl-CoA reductase part is right and only the cofactor is wrong, MODIFY laterally to
  GO:0043957 rather than REMOVE. Likely a term-selection slip by the annotator (the NADH term
  is for the Clostridium propionicum fermentation enzyme, which the same paper says is
  unrelated).
- GO:0004022 alcohol dehydrogenase (NAD+) activity (TreeGrafter, PTN000191633): REMOVE. This
  is the ancestral MDR/zinc ADH activity. Msed_1426 reduces a C=C bond of an enoyl-CoA
  (EC 1.3.1), not a CH-OH group, and does not use NAD(H). Zinc-ADH-family over-annotation.
- GO:0008270 zinc ion binding: ACCEPT (Zn measured in the ortholog; ligands conserved).
- GO:0005737 cytoplasm: ACCEPT (soluble enzyme of a cytosolic pathway; no TM/signal).
- GO:0016491 oxidoreductase activity: MODIFY to GO:0043957.
- NEW GO:0015977 carbon fixation (IDA, PMID:19429610); proposed 3HP/4HB cycle term reused
  verbatim from Msed_0709. GO:0043427 (Chloroflexus cycle) not used.
