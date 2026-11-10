# tssA / VC_A0119 (Q9KN46) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_CWQN01000007.1_75` (*Vibrio cholerae*, 475 aa),
  https://gene-annotate-dashboard.kbase.us/review/NZ_CWQN01000007.1_75
- Dashboard strata: Human Pathogen, Core, Annotation-Promoted, GLOB (DeepTMHMM: globular,
  cytoplasmic); homologs in 12 organisms across 6 genera.
- Prior names shown on the page: eggNOG "protein conserved in bacteria"; Pfam PF16989
  "Type VI secretion, EvfE, EvfF, ImpA, BimE, VC_A0119, VasJ"; KEGG K11910 "type VI
  secretion system protein VasJ".
- Mapping: 98.7% identity over 469 aligned residues (97.5% of the 475-residue query) to the
  N16961 reference-proteome entry Q9KN46 = VC_A0119. Source:
  `runs/20261030T212629Z-finalize-vibch-mapping/out/tables/final_mapping.tsv` in the BERIL
  hackathon project. The review is filed on Q9KN46.
- The dashboard call and page are frozen in `VC_A0119-dashboard-prediction-evidence/` from BERIL
  run `20261030T212646Z-dashboard-page-nz-cwqn01000007-1-75`.

## Gene directory naming

The directory is named by locus tag because UniProt gives no gene symbol, only `OrderedLocusNames=VC_A0119` (project rule: use the UniProt gene symbol when there is one, else the locus tag). An earlier draft filed it as `tssA`; it was moved back on 2026-10-30. The published name *tssA* (TssA<sub>VC</sub>; Schneider et al. 2019 Methods), and the database-era name `vasJ` (Pfam PF16989, KEGG K11910), is kept as an alias, together with `VCA0119` and the dashboard id.

## What the protein is

Class A TssA (= TssA2A in the Dix et al. 2018 clade scheme) of the V. cholerae T6SS:
ImpA_N (PF06812, residues 12–125) plus a C-terminal VasJ domain (PF16989). Direct
V. cholerae evidence:

- **Hcp secretion / killing.** In the O37 strain V52, a VCA0119 deletion removed Hcp from
  supernatants without changing cellular Hcp, and abolished E. coli killing
  (PMID:21909372).
- **Cap on the growing sheath.** In the O1 El Tor strain 2740-80, a functional chromosomal
  TssA-mNeonGreen fusion appears at T6SS initiation sites and then at the distal end of the
  polymerizing sheath; photobleaching shows the cap does not exchange with the cytosolic
  pool; brightness calibration gives 12 subunits (PMID:31403721).
- **Structure.** Cryo-EM of the purified protein gives a dodecameric six-pointed star
  (PDB 6RIU, 3.9 Å; ordered core = the C-terminal VasJ domains) that fits the cap density at
  the distal end of isolated V. cholerae sheaths (CC = 0.87).
- **Phenotype in O1 El Tor is partial.** Δ*tssA* polymerizes sheath at 3 nm/s instead of
  23 nm/s and kills prey more slowly, but is not null for T6SS function. Schneider et al.
  therefore call Class A TssAs sheath-tube assembly chaperones and propose the class name
  TsaC.

The *V. cholerae* protein did **not** reproduce the Hcp/baseplate interactions reported for
the E. coli orthologue in pulldown or two-hybrid assays, so its contact map is an open
question (recorded as a knowledge gap).

## Paralog signal flagged by the dashboard

The dashboard's paralog axis paired this protein with `NZ_WYBZ01000044.1_3`
("VasL/ImpA-family inner membrane protein associated with the type VI secretion system",
tier B) in PANTHER family PTHR37024. That is the second ImpA_N protein of the same cluster,
VCA0121 / TagA. It is a genuine paralog with an **opposite** role: a Class B, membrane-
localized hexamer that stops sheath polymerization at the far membrane and antagonizes TssA
(PMID:31403721). Zheng et al. (2011) already noted that both VCA0119 and VCA0121 carry
ImpA_N domains but that only VCA0119 is required for secretion, and speculated VCA0121 was a
degenerate duplicate. So ImpA_N alone cannot carry the TssA call; the dashboard call used
the C-terminal VasJ domain and the VCA0119-specific family signatures (IPR017739,
TIGR03362) and so landed on the right class.

## Verdict on the dashboard call

**Supported.** Both GO terms are COR (correct and novel — GOA for Q9KN46 is empty).
Qualifications, which concern the wording rather than the terms:

1. "Structural component" understates the role. The protein is a dynamic, non-exchanging
   dodecameric cap/chaperone that accelerates sheath-tube copolymerization; it is a machine
   component, but loss of it slows rather than abolishes assembly in O1 El Tor.
2. "Required for Hcp secretion" is true as stated for strain V52 (PMID:21909372) but
   strain-dependent: in 2740-80 the mutant still kills prey, just more slowly.
3. The call's evidence cites the 97.5%-identical homolog as the source of experimental
   support. That homolog is VCA0119 itself in a different V. cholerae genome assembly, so
   the transfer is essentially within-species, not cross-species.
4. GO currently has no term for the actual molecular role; a new MF term,
   "type VI secretion system sheath assembly chaperone activity", is proposed in the review.

## Tooling notes

- `just fetch-gene` was not rerun: the gene dir was seeded by the coordinator because EBI
  OLS was down and the taxon-label step fails (the taxon was resolved via `ubergraph:`).
- `just fetch-gene-pmids` found no PMIDs, because the seeded YAML had no references and the
  GOA file is empty (header only). Papers were found with PubMed search and cached with
  `just fetch-pmid`.
- `just fetch-fitness VIBCH VC_A0119` failed: "no FEBA data source was reachable" (no local
  FEBA database, and fit.genomics.lbl.gov was unavailable; it had returned 403 earlier in
  this batch). No fitness artifact was written.
- `just fetch-pmid` intermittently returns HTTP 429 from NCBI; retrying after a few seconds
  worked.
- `just validate VIBCH tssA` emits one warning: no annotation cites the deep-research file.
  That is intentional — the deep-research report is an AI synthesis, and every annotation
  cites the underlying primary papers instead.
