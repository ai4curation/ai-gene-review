# Adar (Adenosine deaminase acting on RNA) notes

Gene: Adar, FBgn0026086, CG12598 (synonym hypnos-2), X chromosome 2B6-7. UniProt Q9NII1
(Swiss-Prot, 669 aa, displayed isoform N), the accession that carries all 41 GOA rows.
PANTHER PTHR10910 (ADAR family), subfamily SF62. Two dsRBDs (54-120, 190-265) and the
A-to-I editase (adenosine deaminase) domain (341-665); zinc ligands His365, Cys423, Cys486
and proton donor Glu367 by similarity to human ADAR2 (UniProt FT lines). Dsrbd1 has an
NMR structure (PDB 2LJH).

## Sources and searches (2026-11-17)

- Cached GOA references: 14 PMIDs. Full text cached for PMID:21622951, 22037499, 22531175,
  22658416, 24137011, 24561617, 26896675, 32221286, 38891830; the older papers
  (PMID:10917596, 10966106, 11254668, 15920480, 21078670) are abstract-only.
- FlyBase hand-written description (`Adar-deep-research-flybase.md`), fetched 2026-11-17.
  No Falcon/Perplexity deep research for this batch.
- PubMed (E-utilities) searches run: "Drosophila tRNA-specific adenosine deaminase ADAT1"
  (1 hit, PMID:10629039); "Tad1p yeast tRNA-specific adenosine deaminase ADAR1 ADAR2"
  (PMID:10430867); "Drosophila Adar cytoplasmic" (10 hits, none showing
  cytoplasmic fly Adar); "Drosophila ADAR subcellular localization" (2 hits, reviews);
  "Drosophila Adar tRNA" (3 hits, none testing Adar on tRNA); "Caenorhabditis ADR-2
  nuclear localization" (PMID:39036970; also PMID:18780728, not cached); "Drosophila ADAR dsRBD solution
  structure" (PMID:22210494); "Drosophila Adar oxidative stress" (PMID:15530657);
  "Drosophila Adar heat temperature editing"; "Drosophila Adar glucose", "dADAR glucose",
  "Drosophila ADAR RNA editing metabolism insulin" (no relevant hit); "Adar R-loop
  Drosophila" (PMID:40660165). WebSearch: "Drosophila Adar RNA editing mutant glucose
  metabolism insulin" and a second glucose/hemolymph sugar query (no Adar paper found).
- Newly cached: PMID:10629039, 10430867 (ADAT papers, abstract-only),
  PMID:22210494 (dsRBD1 structure, full text), PMID:39036970 (worm ADR-2 localization,
  full text), PMID:15530657 (ROS, abstract),
  PMID:40660165 (R-loops, full text), PMID:12756328 (4f-rnp editing, abstract).
- PAINT/PANTHER analysis: `Adar-bioinformatics/RESULTS.md`.

## Identity and evolution

- dADAR is the fly ortholog of vertebrate ADAR2 (ADARB1); insects lost ADAR1
  [PMID:21622951 "The strong functional similarity of human ADAR2 and Drosophila Adar
  suggests rather that these are true orthologs."]; [PMID:21622951 "The ADAR1 gene has been
  lost several times, including during the evolution of insects and crustacea."].
- Earliest characterisation [PMID:10917596 "dADAR is most homologous to the mammalian RNA
  editing enzyme ADAR2, the enzyme that specifically edits the Q/R site in the pre-mRNA
  encoding the glutamate receptor subunit GluR-B."].
- tRNA A37 inosine in flies is made by a separate enzyme, dADAT1 (Adat1, FBgn0028658),
  which has no dsRNA activity [PMID:10629039 "The enzyme has no activity on dsRNA
  substrates but is a tRNA deaminase with specificity for adenosine 37 of insect alanine
  tRNA."]. The ADAT1 enzymes are the functional homologues of yeast Tad1p
  [PMID:10430867 "It represents the functional homologue of the recently identified yeast
  protein Tad1p"], and human ADAT1 "does not modify adenosines residing in double-stranded
  RNA or in pre-mRNAs that serve as substrates for ADAR1 or ADAR2" (PMID:10430867). The
  two enzyme classes share a deaminase domain and probably an ancestor
  [PMID:10629039 "dADAT1 shows greater similarity to vertebrate ADARs than to yeast Tad1p,
  supporting the hypothesis of a common evolutionary origin for ADARs and ADATs."].
- No paper found that assays fly Adar (or any animal ADAR) on tRNA (PubMed "Drosophila Adar
  tRNA", 3 hits, none an assay; see Sources).

## PAINT (PTHR10910, PANTHER 19.0; details in Adar-bioinformatics/RESULTS.md)

- All seven IBA rows come from the eukaryotic root PTN000098822. Losses are only on three
  single leaves (worm adr-1, fly cg12493, one Tribolium gene).
- GO:0008251 tRNA-specific adenosine deaminase: seeds are Arabidopsis TAD1 (AT1G01760, in
  the Bikont clade) and fly Adat1. PANTHER 19 places fly Adat1 inside the ADAR2 clade as a
  Drosophila-specific duplicate of Adar; InterPro's HMM classifies it (Q9V3R6) in
  PTHR46516 with human ADAT1 (Q9BUB4). With no loss on the ADAR clades, all ADARs inherit
  the tRNA term. Verdict: not inherited by Adar.
- GO:0005737 cytoplasm: seeds are ADAR1-clade proteins (human ADAR P55265, mouse Adar
  MGI:1889575, mouse Adad2 MGI:1923023) plus worm adr-1 and adr-2. Human ADARB1 is not a
  seed. Verdict: over-annotation for fly Adar (see Localization).
- GO:0003725 dsRNA binding: seeds human and rat ADARB1 (P78563, RGD:2033), fly Adar's
  orthologs. Verdict: inherited, and supported directly (dsRBD1 structure and RNA binding).

## Activity

- In vitro deaminase activity on dsRNA [PMID:10917596 "Partially purified dADAR expressed
  in Pichia pastoris has robust nonspecific A-to-I deaminase activity on synthetic dsRNA
  substrates."]. Site-specific in vitro editing of fly and mammalian substrates compared
  with human ADARs in PMID:21622951 (Figure 1) and PMID:22210494 (GluR-2 R/G site).
- Catalytic-dead knock-in AdarE374A [PMID:32221286 "We demonstrate that Adar adenosine
  deamination activity is necessary for normal locomotion and prevents age-dependent
  neurodegeneration."].
- In vivo: deletion abolishes all known site-specific editing [PMID:10966106 "Correspondingly,
  all known Drosophila site-specific RNA editing (25 sites in three ion channel transcripts)
  is abolished."]; editing is largely cotranscriptional [PMID:22658416 "We conclude that
  ADAR-mediated editing is more widespread than previously indicated and largely occurs
  cotranscriptionally."].
- dsRNA binding: dsRBD1 NMR structure and RNA titration [PMID:22210494 "Here, we report the
  solution structure of the N-terminal dsRNA binding domain (dsRBD) of dADAR and use NMR
  chemical shift perturbations to identify the protein surface involved in RNA binding."].
- Auto-editing: Adar edits its own transcript (S/G site near the active site; residue 430
  of the displayed isoform), and the edited isoform is less active [PMID:15920480 "We show
  that editing restricts ADAR function since the edited isoform of ADAR is less active in
  vitro and in vivo than the genome-encoded, unedited isoform."].
- pri-miRNA editing: let-7-Complex [PMID:24561617 "Here we show that RNA editing by
  Drosophila ADAR modulates the expression of three co-transcribed miRNAs encoded by the
  evolutionarily conserved let-7-Complex (let-7-C) locus."].
- Editing-independent roles: high-level catalytically inactive Adar rescues
  neurodegeneration and Adar loss induces Dicer-2-dependent innate immune gene expression
  (PMID:32221286); catalytically inactive Adar suppresses R-loops and genome instability
  [PMID:40660165 "Strikingly, a catalytically inactive Adar mutant (E374A), which lacks
  A-to-I editing activity, retained its ability to suppress R-loop accumulation and
  preserve genome integrity."].

## Localization

- Nuclear, with nucleolar enrichment and extra-nucleolar nuclear punctae [PMID:22531175
  "All endogenous HA-tagged dADARs co-localized with the nucleolus to a degree that was
  independent of auto-editing status"]; [PMID:22037499 "Whereas dADAR primarily resides in
  the nucleus where A-to-I deamination normally occurs, FMRP is mostly observed in the
  cytoplasm despite containing nuclear localization and export signals"].
- Human ADAR1 isoforms tested in flies: the nuclear p110 form, not the cytoplasmic p150,
  suppresses neurodegeneration [PMID:21622951 "suggesting that suppression of
  neurodegeneration is associated with nuclear localization of the ADAR proteins"].
- No fly paper reports cytoplasmic Adar (PubMed "Drosophila Adar cytoplasmic", 10 hits;
  "Drosophila ADAR subcellular localization", 2 hits; checked 2026-11-17). The isoforms
  differ at the N-terminus (two promoters) and in the dsRBD1-dsRBD2 spacer (exon 3a,
  residues 147-184); no isoform has been reported to be cytoplasmic.
- The worm cytoplasm seeds are mainly nuclear too; ADR-2 is cytoplasmic only when ADBP-1 is
  lost [PMID:39036970 "Additionally, both ADARs are mainly in the nucleus."];
  [PMID:39036970 "In adbp-1 mutant worms, ADR-2 is mislocalized, while ADR-1 is not"].

## Physiology (phenotypes; necessity, mostly downstream of editing of neuronal transcripts)

- Behaviour: locomotor uncoordination, temperature-sensitive paralysis, tremors and
  age-dependent neurodegeneration in nulls (PMID:10966106); circadian motor patterns and
  male courtship in hypomorphs (PMID:21078670); auto-editing alters behaviour
  (PMID:22531175).
- Hypoxia and heat: hypnos-2 mutants [PMID:11254668 "dADAR, for which there are mammalian
  homologues, is essential for adaptation to altered environmental stresses such as O2
  deprivation and for the prevention of premature neuronal degeneration"].
- Oxidative stress: Adar mutants resist paraquat (PMID:15530657, Chen et al. 2004).
- Neuronal excitability [PMID:24137011 "Adar-overexpressing larval motor neurons show reduced
  excitability whereas Adar(5G1) null mutant or targeted Adar knockdown motor neurons
  exhibit increased excitability."].
- Male germline: endogenous Adar in GSCs and spermatocytes; loss expands the
  transit-amplifying region via BMP signalling (PMID:38891830).

## FlyBase description check

Text: "Adenosine deaminase acting on RNA (Adar) encodes an RNA editing enzyme. It is involved
in behaviour, glucose metabolism and response to several stresses such as heat, hypoxia and
oxidative stress."

- RNA editing enzyme: correct (PMID:10917596, 10966106).
- Behaviour: correct (PMID:10966106, 21078670, 22531175).
- Heat, hypoxia: correct (PMID:11254668). Oxidative stress: correct (PMID:15530657).
- Glucose metabolism: not traced. No paper linking fly Adar to glucose or sugar metabolism
  was found (searches above); FlyBase may hold an unpublished or phenotype-level basis.
- Missing: the nervous-system focus, ion-channel recoding, the ADAR2 orthology and
  nuclear localization.

## UniProt FUNCTION check

"Has A-to-I RNA editing activity on extended dsRNA: edits RNA-binding protein Rnp4F. ...
Essential for adaptation to environmental stresses, such as oxygen deprivation, and for the
prevention of premature neuronal degeneration, through the editing of ion channels as
targets." Rnp4F editing is cited to PMID:12756328 (not a GOA reference; abstract cached: it inferred dADAR editing of 4f-rnp/sas-10 duplexes from A-to-G changes, without an Adar mutant test). The
rest is traced to PMID:10917596, 10966106 and 11254668. No defect recorded.
