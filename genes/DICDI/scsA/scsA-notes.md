# scsA (Dictyostelium discoideum, UniProtKB:P36967) notes

Succinyl-CoA synthetase (SCS) alpha subunit, "p36". dictyBase DDB_G0289325. Written as a follow-up to the
evolutionary reviews of the alpha family PTHR11117 and the beta family PTHR11815.

## Session log, 2026-11-18

- `just fetch-gene DICDI scsA` wrote the UniProt and GOA files and then failed twice on a read timeout to
  the EBI Ontology Lookup Service, which the seeder uses only to fetch the NCBITaxon label. The stub was
  seeded by running the same `fetch-gene` command in-process with the label for NCBITaxon:44689
  ("Dictyostelium discoideum", as in every other `genes/DICDI` review) supplied; nothing else was changed.
- `just deep-research DICDI scsA --provider perplexity` failed: "Provider 'perplexity' not available.
  Available: asta, openscientist, claude_code". No provider deep-research file exists for this gene; the
  literature search below was done by hand.
- Depth of reading. PMID:8448193, PMID:7771809, PMID:8240297, PMID:8384004, PMID:8060491, PMID:2542944,
  PMID:2275752, PMID:2049873 and PMID:1664207 are abstract-only in the cache. PMID:8240297 and PMID:2542944
  have PMC records that hold only page scans, which the fetcher could not read. Only PMID:33923051 and PMID:35602934 (added in the follow-up, with its supplementary tables) were read in full. Every judgement on the 1989 to 1995 biochemistry therefore rests on abstracts.

## Identity

- 315-residue precursor; the mature protein starts at residue 17. The cDNA paper reports the presequence
  from direct protein sequencing [PMID:7771809 "Direct amino acid sequence data indicate that the first 16
  amino acids encoded by the cDNA comprise a mitochondrial targeting sequence."]. UniProt gives TRANSIT 1..16
  with experimental evidence from PMID:8448193 (peptide sequence 17-35) [file:DICDI/scsA/scsA-uniprot.txt
  "PROTEIN SEQUENCE OF 17-35; 67-75 AND 81-93, AND PHOSPHORYLATION."].
- The cDNA predicts 310 residues [PMID:7771809 "The coding region predicts a protein of 310 amino acids."];
  UniProt records a frameshift in that sequence (AAA85724.1), which accounts for the difference from 315.
- Identified by peptide sequence of the purified p36 band [PMID:8448193 "Partial peptide sequencing of this
  band revealed p36 to be homologous to the alpha-subunit of succinyl-CoA synthetase."].
- Single-copy gene [PMID:7771809 "In D. discoideum, the alpha subunit is a single copy gene that is
  developmentally regulated."].
- 75% identical to the rat liver alpha subunit and 62% to E. coli SucD [PMID:7771809 "shows 75% identity to
  that from rat liver, which represents a GTP-utilizing form of SCS, and 62% identity to the Escherichia coli
  protein, which is an ATP-utilizing form"].
- Catalytic histidine (His268), CoA-binding residues and the shared substrate site are HAMAP-rule features in
  UniProt, not experimental for this protein.

## Nucleotide use

- Crude preparations: both ATP and GTP phosphorylate p36 [PMID:8448193 "In crude sample preparations, p36
  could be phosphorylated by both ATP or GTP and in either case, its phosphorylation was stimulated by low
  concentrations of GDP."]. Same in plasma-membrane preparations, with more labelling from GTP [PMID:2275752
  "p36 can be phosphorylated when membranes are supplied either ATP or GTP as the phosphate donor, but that
  a greater level of p36 phosphorylation is achieved with GTP"], and in crude mitochondrial fractions from
  an independent laboratory [PMID:8384004 "p38 can be phosphorylated in vitro using either ATP or GTP as
  phosphoryl donors."].
- Partially purified protein: GTP, little or no ATP [PMID:8448193 "Partially purified p36 retained its
  ability to be phosphorylated with GTP while exhibiting little or no phosphorylation with ATP."].
- Later summary by the same laboratory [PMID:7771809 "We have previously shown that the enzyme purified from
  growing D. discoideum is a GTP-utilizing enzyme."].
- Reverse half-reaction with GDP gives GTP [PMID:8240297 "Dephosphorylation of p36 is induced by relatively
  high levels of GDP and is coincident with the formation of GTP. This indicates that, at high
  concentrations, GDP serves as a substrate of SCS."].
- The phosphorylation is the catalytic phosphoenzyme, formed from either side of the reaction [PMID:8060491
  "this phenomenon represents an enhanced catalytic capacity of SCS to form the phosphoenzyme intermediate.
  Low concentrations of GDP stimulate phosphoenzyme formation by either GTP, or succinyl-CoA and P(i)."].
  So UniProt's PTM comment ("Phosphorylated; stimulation by low concentration of GDP") and the Phosphoprotein
  keyword describe the catalytic intermediate, not a regulatory modification, and no autophosphorylation
  process term is warranted.
- What the abstracts do not show: the complete ligase reaction (succinyl-CoA formation or CoA-dependent
  nucleotide turnover) measured on the purified enzyme. The data are phosphoenzyme formation with GTP, and
  from succinyl-CoA plus phosphate, and GTP formation from GDP. Together these are the partial reactions of
  EC 6.2.1.4. The full text of PMID:8448193 was not read, so whether it contains a full assay is unknown.
- Why ATP works in crude preparations is not resolved by the abstracts. Candidates: a co-fractionating
  ADP-forming enzyme built on the same alpha subunit with the A-type beta subunit; or nucleotide
  interconversion (nucleoside-diphosphate kinase) making GTP from ATP and endogenous GDP. The earlier papers
  spoke of a "p36 kinase" with a relatively non-specific donor site [PMID:2049873 "the phosphate donor site
  of p36 kinase is relatively non-specific"], written before p36 was identified.

## Regulation by GDP

- Low GDP stimulates phosphoenzyme formation without acting at the catalytic site; proposed allosteric site
  [PMID:8240297 "We propose that GDP functions as an allosteric regulator of SCS"]; also seen with pig heart
  SCS [PMID:8060491 "is also observed with purified pig heart SCS"]. The site has not been located.
- The GDP stimulation is developmental: absent in membranes of vegetative cells [PMID:2275752 "the ability
  of GDP to stimulate p36 phosphorylation is not observed in vegetative cell membranes"].

## Quaternary structure

- Alpha-beta dimer on gel filtration [PMID:8240297 "Gel-filtration analyses indicate that SCS in our system
  behaves as a non-interacting alpha beta dimer"]. The beta subunit in the preparation was not identified.
- The genome has two beta genes: scsB (UniProtKB:Q869S7, Gln at the specificity position, SUCLG2 lineage)
  and scsC (UniProtKB:Q55AI5, Pro, SUCLA2 lineage); gene names checked in UniProt on 2026-11-18. Placement
  from `genes/yeast/LSC2/LSC2-bioinformatics/RESULTS.md`. Neither beta gene has an experimental
  molecular-function annotation (QuickGO, 2026-11-18); scsC carries a dictyBase ND for molecular function.
  One alpha gene and one beta gene of each type is the animal arrangement.

## Location

- First described in plasma-membrane and crude-membrane preparations, before it was identified [PMID:2542944
  "p36, a 36-kDa protein of Dictyostelium discoideum plasma membranes"; PMID:8448193 "in crude membranes from
  the amoeba Dictyostelium discoideum"]. This is the likely origin of dictyBase's `membrane` IDA
  (PMID:8448193). The abstract reports no topology or extraction experiment. A crude membrane pellet contains
  mitochondria. Not overruled, because the full text was not read: UNDECIDED.
- Mitochondrial: cleaved presequence (above); crude mitochondrial fraction [PMID:8384004 "The mitochondrial
  localization and other data presented on the characterization of this protein led us to the conclusion
  that p38 is the alpha subunit of succinic thiokinase."]; mass spectrometry of isolated mitochondria
  [PMID:33923051 "succinate-CoA ligase (XP_636263.1)"; XP_636263.1 is the RefSeq entry of P36967 per the
  UniProt record]. The 2021 preparation is a differential-centrifugation pellet with no reported ER marker
  check, so it supports the organelle only together with the presequence.
- Percoll-purified mitochondria (PMID:35602934, full text and supplementary tables S1 to S7 read on 2026-11-18;
  the tables are not part of the cached text) [PMID:35602934 "From AX2 axenic cultures, we prepared mitochondria
  isolates—both crude and highly purified—through Percoll gradient ultracentrifugation"]. Values for P36967
  (DDB_G0289325): Table S2 enrichment ratios 0.915 (crude/lysate), 1.021 (pure/lysate, the RER) and 1.115
  (pure/crude); Table S4 RER 1.021, probability 1 of the mitochondrial cluster; Table S7 in the compendium,
  discovery method "Proteomics", class "Energy metabolism"; Tables S1 and S5 TargetP-2.0 mTP. Cutoff
  [PMID:35602934 "We chose an RER cutoff of 0.392"]. Caveat: Table S3 lists P36967 among the 47 reference
  proteins, chosen from existing annotation, so the classification is not independent of prior annotation;
  the enrichment is still a measurement on the protein.
- That p38 of PMID:8384004 is the scsA product is an inference: the abstract gives no sequence, and the link
  rests on the alpha gene being single copy.
- Matrix: no sub-mitochondrial fractionation exists. Inferred from the cleaved presequence, the soluble
  alpha-beta dimer, the absence of any transmembrane feature in UniProt, and the TCA-cycle function. Proposed as a NEW IC row, as for yeast LSC1; S. pombe SPAC16E8.17c has an existing matrix annotation (IC, GO_REF:0000111), which its review accepts.
- There is no experimental GO row for mitochondrion on this gene although PMID:33923051, PMID:35602934 and the presequence would support one. This is a curation gap, noted here and not recorded as a knowledge gap.

## Expression

- mRNA highest in growing cells and falls after aggregation; protein level constant [PMID:7771809 "Highest
  levels of its mRNA are seen in growing cells"; "the level of the protein, as determined by Western blots,
  remains unchanged throughout development"].
- Mitochondrial proteome: SCS abundance changes about 2-fold between early developmental stages
  (PMID:33923051, Table 1; not quoted).
- p38 phosphorylation changes within seconds of cAMP stimulation (PMID:8384004); read by the authors as a
  readout of energy metabolism.

## PANTHER placement

- PTHR11117, subfamily SF2 (with human SUCLG1 and yeast LSC1). The IBA rows for GO:0004776, GO:0004775,
  GO:0006099 and GO:0009361 come from the LUCA node PTN000122012; GO:0005739 from the eukaryotic node
  PTN000122014 (`interpro/panther/PTHR11117/PTHR11117-paint.tsv`).
- scsA is one of the PAINT seeds for GO:0004776 at PTN000122012 (dictyBase:DDB_G0289325 in WITH/FROM). That
  is its own IDA used as descendant evidence, which is expected and not circular.
- scsA lies outside the branches the family review marks for pruning (fungal clade PTN000874203, SF24 clade
  PTN001671414, the Aquifex leaf, the Trichomonas clade).
- The research dossier reports the path below PTN000122014 from the PANTHER tree service (Unikont node, a
  Dictyostelium node holding scsA and the D. purpureum ortholog). Those node ids are not in the repository
  files and were not re-read here, so they are not cited in the review.

## Decisions

| Row | Action | Why |
|---|---|---|
| GO:0004776 IDA, IBA, IEA | ACCEPT | GTP-dependent phosphoenzyme, GTP from GDP, purified enzyme GTP-utilizing; abstracts only |
| GO:0004775 IBA, IEA | KEEP_AS_NON_CORE | inside the clade, A-type beta gene present, but no ADP-forming enzyme assayed; non-core because not shown in this organism, not because peripheral |
| GO:0009361 IBA | KEEP_AS_NON_CORE | follows GO:0004775 |
| GO:0003824 IEA | TOO_GENERAL | Both InterPro entries map only to catalytic activity; IPR005810 is SCS-alpha specific but the term it could support, GO:0004774, is an ancestor of GO:0004776, asserted by IDA. Same action as the other alpha subunits (changed back from MODIFY after PR review) |
| GO:0006099 IBA, IEA | ACCEPT | TCA-cycle step; no mutant in Dictyostelium |
| GO:0006104 TAS | ACCEPT | author statement; reaction interconverts succinyl-CoA and succinate |
| GO:0005739 IBA, IEA | ACCEPT | root organelle policy; presequence and two mitochondrial proteomes (PMID:33923051, PMID:35602934) |
| GO:0016020 IDA | UNDECIDED | fractionation observation in the abstract; full text not read |
| GO:0005759 IC | NEW | presequence, soluble dimer, TCA-cycle function |
| GO:0045244 IC (PMID:8240297) | NEW | alpha-beta dimer that forms GTP from GDP |

Also proposed as NEW: GO:0045244 succinate-CoA ligase complex (GDP-forming), part_of, from the alpha-beta
dimer that forms GTP from GDP (PMID:8240297, abstract only; beta partner not identified). It is a sibling
of GO:0009361 under GO:0042709, and animal SUCLG1 alpha subunits carry it (QuickGO by term id, 188 rows on
2026-11-18, so the query can return a positive). Not proposed: any autophosphorylation, GDP-binding or
regulation term.

## Literature search (2026-11-18)

Queries and counts as recorded in the research dossier for this review (PubMed E-utilities unless stated):

- succinyl-CoA synthetase Dictyostelium: 9 (PMID:9344470, 9099993, 7669763, 7771809, 8016083, 8060491,
  8240297, 8384004, 8448193)
- succinate-CoA ligase Dictyostelium: 7; succinate thiokinase Dictyostelium: 7
- p36 Dictyostelium phosphorylation GDP: 7 (adds PMID:1664207, 2049873, 2275752, 2542944)
- scsA Dictyostelium: 0; "DDB_G0289325": 0; Dictyostelium SUCLG1: 0
- Dictyostelium mitochondrial proteome: 16 (includes PMID:35602934, read in the follow-up; see Location); Dictyostelium mitochondria phosphoproteome: 1 (PMID:34769115,
  no mention of the enzyme in the main text)
- Europe PMC: "scsA" AND Dictyostelium: 5, of which only PMID:33923051 concerns this gene
- QuickGO by reference: PMID:8448193 has 3 annotations, all on P36967; the other papers above have none.

No genetic study (knockout, knockdown, mutant) of scsA, no recombinant protein study and no study of either
beta subunit was found. The nine-paper SCS set contains no genetic study.

Mutant queries run in the follow-up on 2026-11-18:

- Europe PMC: `(TITLE_ABS:"succinyl-CoA synthetase" OR TITLE_ABS:"succinate-CoA ligase" OR TITLE_ABS:"succinic
  thiokinase" OR TITLE_ABS:"succinyl-CoA ligase") AND TITLE_ABS:Dictyostelium AND (mutant OR knockout OR REMI
  OR disruption OR "null")`: 1 hit, PMID:8016083 (P. aeruginosa NDP kinase and SCS; not a Dictyostelium mutant).
- Europe PMC: `"DDB_G0289325"`: 0. `TITLE_ABS:scsA AND TITLE_ABS:Dictyostelium AND (mutant OR knockout OR REMI)`: 0.
- PubMed: `(succinyl-CoA synthetase OR succinate-CoA ligase OR succinic thiokinase) AND Dictyostelium AND (mutant
  OR knockout OR REMI OR disruption OR null)`: 0.
- dictyBase strain and phenotype records for DDB_G0289325 could not be retrieved (the gene page returned
  HTTP 404 to a scripted request), so the review says that no mutant was found in these searches and does
  not say that none exists.

Not on this gene, not cited: PMID:8016083 (P. aeruginosa SCS), PMID:7669763 (NDP kinase structures),
PMID:9099993 (rabbit p40), PMID:9344470 (E. coli SCS), PMID:20013782 (2-D DIGE mitochondrial proteome,
abstract does not name SCS).

## For the family reviews

- Nothing here contradicts `interpro/panther/PTHR11117/PTHR11117-review.yaml`,
  `interpro/panther/PTHR11815/PTHR11815-review.yaml` or the LSC2 RESULTS.md.
- Wording: "the enzyme purified from Dictyostelium uses GTP" is a retrospective sentence in PMID:7771809.
  The primary datum (PMID:8448193 abstract) is GTP-dependent phosphorylation of partially purified p36, a
  half-reaction.
- GO:0004775 for the Dictyostelium alpha subunit is inherited and unassayed; ATP labels p36 only in crude
  fractions (PMID:8448193, PMID:2275752, PMID:8384004). The family reviews do not discuss this.
- scsC (Q55AI5, A-type beta) carries a dictyBase ND for molecular function.
- GO:0005739 at PTN000122014 now has gene-level support in Amoebozoa (presequence by direct sequencing;
  PMID:33923051).
- UniProt cites HAMAP rule MF_03222 in evidence tags while the cross-reference line lists HAMAP MF_01988;
  the EC 6.2.1.4 evidence from PMID:8448193 is ECO:0000305 (curator inference), not ECO:0000269.
