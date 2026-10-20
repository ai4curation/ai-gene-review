# ppa2 (SPBC16H5.07c, UniProt P23636) - curation notes

Working journal for the GO annotation review of the *Schizosaccharomyces pombe*
major PP2A catalytic subunit Ppa2. Inputs: `ppa2-uniprot.txt`, `ppa2-goa.tsv`,
`ppa2-deep-research-falcon.md` (Edison/Falcon literature synthesis) and the cached
publications under `publications/`. Full text is cached only for PMID:22267499
(Goyal & Simanis 2012), PMID:33888556 (Ma et al. 2021), PMID:22119525
(Singh et al. 2011), PMID:25487150 (Grallert et al. 2015) and PMID:27398807
(Nie et al. 2016); the remaining references are abstract-only in the cache
(Europe PMC / NCBI full-text fetches for PMC5709762 returned only front matter,
so PMID:29079657 was reviewed from its abstract).

## Identity

- Ppa2 is the *major* PP2A catalytic subunit; Ppa1 is the minor ~80%-identical
  paralog. Neither single deletion is lethal, but the double deletion is
  [PMID:2170029 "Only double gene disruption of both PP2A genes results in lethality, as is the case for PP1 genes."].
- ppa2 deletion removes most extractable PP2A activity and reduces cell size;
  ppa1 deletion has little effect
  [PMID:22267499 "The major subunit is encoded by ppa2 ; deletion of ppa1 has little effect upon the cell, while ppa2–Δ cells are reduced in size"].
- The ppa2-6 allele (D70N) hits a catalytic-metal ligand; the equivalent lambda
  phosphatase mutation reduces kcat >10,000-fold, and ppa2-6 is synthetically lethal
  with ppa1-delta, indicating the mutant protein has little residual activity
  [PMID:22267499 "The mutation found in ppa2-6 affects an amino acid involved in coordinating the metal ion required for catalysis and the equivalent mutation reduces the activity ( k cat ) of λ phosphatase >10,000-fold"].
- A third, divergent catalytic subunit Ppa3 works with Paa1 in the SIN-inhibitory
  phosphatase (SIP) complex; SIP findings must not be transferred to Ppa2
  [PMID:22119525 "suggesting that Ppa1p and Ppa2p do not directly participate in the generation of Cdc7p asymmetry"].
- UniProt: 322 aa, EC 3.1.3.16, two Mn2+ ions per subunit (by similarity),
  C-terminal Leu322 methyl ester (by similarity), PANTHER PTHR45619, InterPro
  IPR047129 (PPA2-like).

## Holoenzyme membership

- Tandem-affinity purification of the Paa1 scaffold co-purifies Ppa1, Ppa2 and the
  B55/Pab1 and B56/Par1 regulatory subunits
  [PMID:25487150 "Catalytic CPpa1 and CPpa2 and the scaffolding APaa1 subunits of PP2A were detected with commercial antibodies."].
- Pab1 co-immunoprecipitates Ppa2, and the pab1-1 mutation weakens that association
  [PMID:27398807 "the pab1-1 mutation indeed destabilizes Pab1 and furthermore, appears to weaken its association with the PP2A catalytic subunit Ppa2"].
- Sgo1 recruits a specific PP2A (B56/Par1-containing) form to meiotic centromeres
  [PMID:16541024 "Here we show in both fission and budding yeast that Sgo1 recruits to centromeres a specific form of protein phosphatase 2A (PP2A)."].
- Conclusion: the `GO:0000159 protein phosphatase type 2A complex` IDA row is well
  supported; Ppa2 is the catalytic subunit of both the PP2A-B55 (Pab1) and PP2A-B56
  (Par1/Par2) heterotrimers built on Paa1.

## Catalytic activity

- Direct: extracts from ppa2-delta lose PP2A-type phosphatase activity measured
  against phosphorylase a / histone H1
  [PMID:2170029 "By fractionating and assaying PPases in wild-type, various deletion, and point mutant strains, the decrease of PP1 or PP2A activity is shown to cause mitotic defects"].
- Direct: Par1-containing PP2A immunoprecipitates dephosphorylate CK1-phosphorylated
  Rec8 in vitro
  [PMID:33888556 "we reconstituted Rec8 dephosphorylation in vitro using immunoprecipitated Par1-containing PP2A complexes"].
- Genetic/pharmacological: ppa2 is the locus determining okadaic-acid sensitivity
  and ppa2-delta reproduces the okadaic-acid hyperphosphorylation pattern
  [PMID:8389306 "We show that ppa2 is the genetic locus controlling okadaic acid sensitivity."].
- The GO:0004721 (phosphoprotein phosphatase activity) IMP row from 2005 is the
  parent of GO:0004722; the assays measured Ser/Thr phosphoprotein substrates, so
  MODIFY to the specific term (which PomBase already carries with IMP/EXP/IBA).

## Cell-cycle function: negative regulation of mitotic entry

- ppa2-delta is lethal with wee1-50 and partially suppresses cdc25-22; cells are
  short (wee-like)
  [PMID:8389306 "ppa2+ interacts genetically with the cell cell regulators cdc25+ and wee1+, as a ppa2 deletion is lethal when combined with wee1-50 but partially suppresses the conditional lethality of cdc25-22 mutation"].
- [PMID:8389306 "Evidence that ppa2+ negatively controls the entry into mitosis, possibly through the regulation of cdc2 tyrosine phosphorylation, is presented."]
- Cold-sensitive PP2A point mutant gives premature mitosis
  [PMID:2170029 "cold-sensitive mutations in the same amino acid lesion of PP1 and PP2A produce chromosome nondisjunction and premature mitosis, respectively"].
- The holoenzyme responsible is PP2A-B55 (Pab1), which is gated by
  TORC1-Greatwall(Ppk18)-Endosulfine(Igo1) to couple nutrients to cell size at
  division
  [PMID:26776736 "High levels of PP2A·B55 prevent the activation of mitotic Cdk1·Cyclin B, and cells increase in size in G2 before they undergo mitosis."].
- Overexpression of ppa2 arrests cells in interphase (opposite phenotype)
  [PMID:8389306 "Overproduced ppa1 or ppa2 proteins accumulate in the cytoplasm near the nuclear periphery, and cells arrest in interphase."].
- Mitotic exit: PP1 reactivation reactivates PP2A-B55 then PP2A-B56, both of which
  contain Ppa2 as the major catalytic subunit
  [PMID:25487150 "PP1 reactivation is required for the reactivation of both PP2A-B55 and PP2A-B56 to coordinate mitotic progression and exit in fission yeast"].
- Decision: the three GO:0010972 rows (IGI with cdc25 and wee1; IMP from the
  Greatwall paper) are ACCEPTed as the core process. The generic IBA
  `GO:0000278 mitotic cell cycle` is a correct family-level placement and is
  ACCEPTed, with the specific function carried by GO:0010972.

## Cytokinesis / septation initiation network

- ppa2-delta and ppa2-6 rescue several temperature-sensitive SIN mutants (cdc7,
  cdc11, sid2, mob1), are strongly synthetically negative with the SIN inhibitor
  cdc16-116, and do not bypass the SIN requirement
  [PMID:22267499 "Since Ppa2-6p has little, if any, activity, these data are consistent with PP2A being an inhibitor of the SIN, as suggested by the analysis of regulatory subunit mutants (see Introduction)."].
- ppa2 mutants fail to establish Cdc7p SPB asymmetry in late anaphase (Goyal &
  Simanis), whereas Singh et al. saw no effect with a different tag
  [PMID:22267499 "Late anaphase ppa2–Δ (14 of 85) and ppa2-6 cells (10 of 70), also showed a failure to establish Cdc7p asymmetry"]
  [PMID:22119525 "it is possible that Ppa2p might play a minor role in SIN inactivation, since ppa2Δ ppa3Δ double mutants, but not ppa1Δ ppa3Δ double mutants, showed a modest increase in the number of septated interphase cells"].
- Chica et al. 2022 (deep-research summary; not in the GOA seed) show that under
  prolonged metaphase arrest ppa2-delta cells septate prematurely, with PP2A-B55
  preventing and PP2A-B56 facilitating septation. Because the catalytic subunit
  serves holoenzymes with opposite effects on the SIN, the unsigned
  `GO:0031029 regulation of septation initiation signaling` is the right term for
  Ppa2; ACCEPT rather than MODIFY to the negative-regulation child.
- Morphology: ppa2 mutants misplace septa, delocalize actin patches and have
  abnormal microtubule arrays
  [PMID:22267499 "We conclude that PP2A–Ppa2p activity is required to maintain normal microtubule arrays and for positioning the division plane, cell morphology, and mitotic progression."].
  These are pleiotropic holoenzyme-level phenotypes; no GOA row exists for them and
  none is proposed (pab1/par1 carry the specific morphogenesis terms).

## Meiosis: centromeric cohesion protection

- Sgo1 recruits PP2A to centromeres; inactivation causes loss of centromeric cohesin
  at anaphase I
  [PMID:16541024 "Its inactivation causes loss of centromeric cohesin at anaphase I and random segregation of sister centromeres at the second meiotic division."]
  [PMID:16541024 "Artificial recruitment of PP2A to chromosome arms prevents Rec8 phosphorylation and hinders resolution of chiasmata."].
- The kinase opposed is CK1 (Hhp1/Hhp2), not Polo
  [PMID:20383139 "the balance between Rec8 phosphorylation and its dephosphorylation by Sgo1-PP2A regulates the step-wise loss of chromosomal cohesion in meiosis"].
- Meikin (Moa1)-Plo1 phosphorylation of Rec8 S450 potentiates PP2A-dependent removal
  of the CK1 phosphates; reconstituted in vitro with Par1 immunoprecipitates
  [PMID:33888556 "Shugoshin (Sgo1) and PP2A collaboratively antagonize casein kinase 1 (CK1)-dependent Rec8 phosphorylation, a prerequisite for cleavage by separase, thus protecting cohesion at the centromeres"].
- The GO-CAM model gomodel:66187e4700001744 already places ppa2's
  Ser/Thr phosphatase activity at the centromeric region in GO:1990813
  (`gocams/index.tsv`). Both GO:1990813 rows and the GO:0000775 IDA row are
  ACCEPTed. Ppa2 does the work here (it is the catalytic subunit that removes the
  Rec8 phosphates), so this is participation, not mere necessity.

## Nutrient signalling (TORC1 -> PP2A-B55 -> Taf12 / differentiation)

- PP2A, activated by TORC1, dephosphorylates the SAGA subunit Taf12 and prevents
  premature commitment to sexual differentiation
  [PMID:29079657 "Taf12 phosphorylation increases early upon starvation and is controlled by the opposing activities of the PP2A phosphatase, which is activated by TORC1, and the TORC2-activated Gad8AKT kinase."]
  [PMID:29079657 "Mutational analyses suggest that Taf12 phosphorylation prevents cells from committing to differentiation until starvation reaches a critical level."].
- The full text (which presumably uses ppa2-delta for the IMP rows) is not in the
  cache; the abstract is consistent with the PomBase IMP annotations for
  GO:0004722 and GO:0031138. The catalytic activity row is ACCEPTed; the
  conjugation row is KEEP_AS_NON_CORE (a real but peripheral, holoenzyme-level
  regulatory role of PP2A-B55 relative to the core cell-cycle catalytic function).

## Localization

- Immunofluorescence with a ppa2-delta control: abundant, granular cytoplasmic
  signal with little nuclear staining
  [PMID:8389306 "ppa2 phosphatase is abundant in the cytoplasm, in contrast to the type 1-like phosphatase dis2, which is enriched in the nucleus."].
- The IBA `cytosol` placement (PTN001705142; human PPP2CA, mouse Ppp2ca,
  Arabidopsis, Dictyostelium) is consistent: Ppa2 is a soluble enzyme with no
  membrane anchor, eluting in ~200 kDa holoenzyme fractions. ACCEPT; the pombe direct
  evidence resolves only to "cytoplasm".
- Centromeric localization is meiosis I-specific and Sgo1-dependent (above).

## Summary of decisions

| Term | Evidence | Action |
|---|---|---|
| GO:0000159 PP2A complex | IDA | ACCEPT |
| GO:0000278 mitotic cell cycle | IBA | ACCEPT (generic; specific role in GO:0010972) |
| GO:0000775 centromeric region | IDA | ACCEPT |
| GO:0004721 phosphoprotein phosphatase activity | IEA, IMP | MODIFY -> GO:0004722 (both rows treated alike) |
| GO:0004722 Ser/Thr phosphatase | EXP x3, IBA, IEA, IMP | ACCEPT |
| GO:0005737 cytoplasm | IDA | ACCEPT |
| GO:0005829 cytosol | IBA | ACCEPT |
| GO:0010972 neg. reg. G2/M | IGI x2, IMP | ACCEPT |
| GO:0016787 hydrolase activity | IEA | ACCEPT (uninformative parent) |
| GO:0031029 reg. of SIN signaling | EXP | ACCEPT |
| GO:0031138 neg. reg. conjugation | IMP | KEEP_AS_NON_CORE |
| GO:1990813 meiotic centromeric cohesion protection | EXP, IMP | ACCEPT |

No REMOVE calls; no NEW annotations proposed (candidate morphogenesis /
microtubule-organisation terms fail the "does the catalytic subunit do the work
of this specific process" test at the current level of mechanistic evidence and are
better placed on the regulatory subunits).
