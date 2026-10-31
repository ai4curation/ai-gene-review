# PPP1R15A (GADD34) — curation notes

UniProt: O75807 (PR15A_HUMAN), 674 aa, PE 1 (evidence at protein level).
Gene aliases: GADD34, MYD116 homolog.
Family: PPP1R15 family; PANTHER PTHR16489 ("Protein Phosphatase 1 Regulatory
Subunit 15"), subfamily PTHR16489:SF14; Pfam PF10488 (PP1c_bdg);
InterPro IPR051254, IPR019523.

Fetched 2026-10-30 with `just fetch-gene human PPP1R15A` (54 GOA rows, 21 seeded
references). Automated deep research was **not** available in this environment
(`just deep-research human PPP1R15A --provider perplexity` fails: no provider API
keys configured), so this file is a hand-built synthesis from the cached
publications and the UniProt record, per the CLAUDE.md instruction never to write
my own content under a `-deep-research-<provider>.md` name.

## One-paragraph summary

PPP1R15A/GADD34 is the stress-inducible, non-catalytic targeting subunit of one of
the two mammalian eIF2alpha holophosphatases. It binds the protein phosphatase 1
catalytic subunit (preferentially PP1alpha/PPP1CA) through a bipartite C-terminal
module, binds its substrate eIF2alpha through a separate central region, and
thereby assembles a PP1 holoenzyme that is selective for phospho-Ser51 of
eIF2alpha. Because GADD34 is itself an ATF4/CHOP target translated only when
eIF2alpha is phosphorylated, this constitutes the negative-feedback arm of the
integrated stress response: it terminates the translational shut-off and the
PERK-mediated UPR signal, and restores cap-dependent initiation. An N-terminal
amphipathic helix inserts monotopically into the cytoplasmic leaflet of the ER
membrane (and, via the polar face of the same helix, the mitochondrial outer
membrane), so the phosphatase is assembled on the ER surface and PP1alpha is
recruited there. The same scaffolding chemistry is reused for other
enzyme-substrate pairs (Smad7-directed dephosphorylation of TGFBR1; CK1epsilon-directed
phosphorylation of TDP-43 under oxidative stress), and the protein is turned over
rapidly by the proteasome so that cells regain stress sensitivity.

## Core mechanism: the GADD34:PP1 eIF2alpha holophosphatase

- GADD34 forms a complex with PP1c that is selective for eIF2alpha, and the
  PP1-binding interaction is required for the function
  [PMID:11381086 "GADD34 formed a complex with the catalytic subunit of protein phosphatase 1 (PP1c) that specifically promoted the dephosphorylation of eIF2alpha in vitro."]
  and
  [PMID:11381086 "Mutations that interfered with the interaction with PP1c prevented the dephosphorylation of eIF2alpha and blocked attenuation of CHOP by GADD34."].
  Note this first paper is mouse GADD34 expressed in CHO cells; GOA cites it as
  ISS for the human gene.
- The regulation is substrate-directed, not a general activation of PP1:
  [PMID:11564868 "While GADD34 inhibited PP1-catalyzed dephosphorylation of phosphorylase a, the GADD34-bound PP1 was an active eIF-2alpha phosphatase."].
  PP1 docks near the C terminus
  [PMID:11564868 "affinity isolation of cellular GADD34/PP1 complexes showed that PP1 bound near the C terminus of GADD34 (amino acids 483 to 619), a region that shows sequence homology with the virulence factors ICP34.5 of herpes simplex virus and NL-S of avian sarcoma virus"].
- Human GADD34 reverses stress-induced eIF2alpha phosphorylation in cells, and the
  PP1-docking element is bipartite
  [PMID:12556489 "we show that the expression of human GADD34 in cultured cells reversed eIF-2 alpha phosphorylation induced by thapsigargin and tunicamycin, agents that promote protein unfolding in the endoplasmic reticulum (ER)"]
  [PMID:12556489 "Structure-function studies identified a bipartite C-terminal domain in GADD34 that encompassed a canonical PP1-binding motif, KVRF, and a novel RARA sequence, both of which were required for PP1 binding."].
  UniProt records the matching mutagenesis: `VRF 556-558 -> ARA: Impairs PP1
  activation`; `R612K + R614K` and `R618D` reduce PP1 binding.
- Structurally, PP1 and eIF2alpha bind GADD34 independently — i.e. GADD34 is a
  scaffold/adaptor rather than an allosteric activator
  [PMID:26095357 "The data highlight independent interactions of PP1 and eIF2α with GADD34, demonstrating that GADD34 functions as a scaffold both in vitro and in cells."],
  and the complex is described as the obligatory recovery phosphatase
  [PMID:26095357 "The growth-arrest- and DNA-damage-induced transcript 34 (GADD34) bound to the serine/threonine protein phosphatase 1 (PP1) is the necessary eIF2α phosphatase complex that returns mammalian cells to normal protein synthesis following stress."].
- The substrate-binding region has been mapped and behaves as a substrate trap
  [PMID:34847777 "We show that substrate recruitment is encoded by an evolutionary conserved region in R15s, R15A325-554 and R15B340-639."]
  [PMID:34847777 "Fragments containing the substrate-binding regions but lacking the PP1-binding motif trapped the phospho-substrate and caused accumulation of phosphorylated eIF2α in unstressed cells."].
  The same paper states the two-subunit architecture explicitly
  [PMID:34847777 "The phosphatases are composed of the catalytic subunit PP1 and one of two related non-catalytic subunits, PPP1R15A or PPP1R15B (R15A or R15B)."]
  and removes G-actin from the specificity model
  [PMID:34847777 "G-actin, which has been proposed to confer selectivity to R15 phosphatases, does not bind these regions, indicating that it is not required for substrate binding."].

Taken together these support a specific molecular function:
**enzyme-substrate adaptor activity (GO:0140767)** — "an adaptor that brings
together an enzyme and its substrate... contributing to substrate selection and
specificity" — which is a better fit than the bare `molecular adaptor activity`
(GO:0060090) that GOA currently carries, and a better mechanistic description than
`protein phosphatase regulator activity` (GO:0019888), which is true but
non-directional.

## Localization

- An N-terminal amphipathic helix (UniProt INTRAMEM 22-39) targets the ER via its
  hydrophobic face and the mitochondria via its polar face, and the insertion is
  monotopic:
  [PMID:21518769 "Deletion of N-terminal sequences in GADD34-GFP proteins highlighted an amphipathic helix, whose hydrophobic surface, specifically valine 25 and leucine 29, mediated endoplasmic reticulum (ER) localization."]
  [PMID:21518769 "Substitution of leucines for three arginines on the polar surface indicated that the same helix also mediated the association of GADD34 with mitochondria."]
  [PMID:21518769 "Fluorescence protease protection and chemical modification of cysteines substituted in the membrane-binding domain pointed to a monotopic insertion of GADD34 into the outer layer of the ER membrane."].
- GADD34 brings PP1alpha with it to the ER
  [PMID:12556489 "Imaging of green fluorescent protein (GFP)-GADD34 proteins showed that the N-terminal 180 residues directed the localization of GADD34 at the ER and that GADD34 targeted the alpha isoform of PP1 to the ER."].
- There is a genuine soluble pool as well as the membrane pool
  [PMID:21518769 "Stress-induced endogenous and ectopically expressed GADD34 proteins were present both in the cytoplasm and in membranes, with their membrane association showing similar biochemical properties."].
- Golgi co-localization is reported but marginal, in the authors' own words
  [PMID:21518769 "suggested that although the majority of GADD34 was localized at the ER, a smaller fraction may also be present at the mitochondria with even smaller fraction showing overlap with the Golgi marker"].
  The GOA `Golgi apparatus` IDA row rests on this.
- Membrane association is not required for phosphatase function: the largely
  cytosolic V25R mutant still works
  [PMID:21518769 "Both WT GADD34 and the mutant, V25R, effectively scaffolded the α-isoform of protein phosphatase-1 (PP1α) and enabled eIF2α dephosphorylation."],
  but ER association does control turnover and ER morphology.

## Regulation of GADD34 itself

- Expression is strictly stress-dependent and downstream of the eIF2alpha kinases
  [PMID:11381086 "Expression of GADD34 is stress dependent, and was absent in PERK(-)/- and GCN2(-)/- cells."].
- Translation is gated by a 5'UTR uORF so that protein appears only when eIF2alpha
  is phosphorylated
  [PMID:19131336 "The human GADD34 5'UTR contains two non-overlapping upstream open reading frames (uORFs), whereas the mouse version contains two overlapping and out of frame uORFs."]
  [PMID:19131336 "we show that the downstream uORF mediates repression of basal translation and directs translation during eIF2alpha phosphorylation"].
- Rapid proteasomal turnover resets stress sensitivity, accelerated by Tyr262
  phosphorylation and opposed by PTPN2
  [PMID:24092754 "Active proteasomal degradation of GADD34 protein then reestablishes the sensitivity of cells to subsequent bouts of stress."]
  [PMID:24092754 "Phosphorylation at tyrosine 262 enhanced the rate of the GADD34 protein turnover."].
- NOX4 is induced downstream of ATF4 and inhibits the GADD34-bound PP1 locally,
  prolonging eIF2alpha phosphorylation
  [PMID:26742780 "we show that the reactive oxygen species-generating NADPH oxidase-4 (Nox4) is induced downstream of ATF4, binds to a PP1-targeting subunit GADD34 at the endoplasmic reticulum, and inhibits PP1 activity to increase eIF2α phosphorylation and ATF4 levels"].
- The holophosphatase is the pharmacological target of salubrinal
  [PMID:15705855 "we identified salubrinal, a selective inhibitor of cellular complexes that dephosphorylate eukaryotic translation initiation factor 2 subunit alpha (eIF2alpha)"].

## Other substrate pairs scaffolded by GADD34 (same chemistry, different clients)

- TGF-beta receptor: Smad7 recruits GADD34:PP1c to dephosphorylate TGFBR1
  [PMID:14718519 "We found Smad7 interacts with growth arrest and DNA damage protein, GADD34, a regulatory subunit of the protein phosphatase 1 (PP1) holoenzyme, which subsequently recruits catalytic subunit of PP1 (PP1c) to dephosphorylate TbetaRI."].
  This is the basis of the two Reactome-sourced `cytosol` rows in GOA.
- TDP-43: under chronic oxidative stress GADD34 scaffolds a *kinase* and its
  substrate
  [PMID:29109149 "In response to oxidative stress, but not ER stress, GADD34 recruited TDP-43, and enhanced"]
  [PMID:29109149 "GADD34-bound CK1ϵ catalyzed TDP-43 phosphorylations"].
- hSNF5/INI1 (SMARCB1) forms a stable heterotrimer with GADD34 and PP1
  [PMID:12016208 "hSNF5/INI1 and PP1 do not compete for binding to GADD34 but rather form a stable heterotrimeric complex with GADD34."].

## Downstream physiology

- Autophagy during starvation: TFEB induces GADD34, which tunes translation so that
  the lysosomal programme can be built
  [PMID:32978159 "We found that the main regulator of the starvation-induced transcriptional program, TFEB, counteracts protein synthesis inhibition by directly activating expression of GADD34, a component of the protein phosphatase 1 complex that dephosphorylates eIF2α."]
  [PMID:32978159 "We discovered that GADD34 plays an essential role in autophagy by tuning translation during starvation, thus enabling lysosomal biogenesis and a sustained autophagic flux."].
  **Not proposed as a GO annotation here**: GADD34 performs no step of autophagy;
  it permits translation of the proteins that do. This is the indirect/downstream
  case CLAUDE.md asks reviewers not to turn into a `NEW` process term.
- ER-stress apoptosis: restoring translation is what lets pro-apoptotic proteins
  accumulate
  [PMID:22934019 "Suppression of the translational block by GADD34 allows for the synthesis of pro-apoptotic proteins like CHOP."].
  So the pro-apoptotic role is real but is a consequence of the translational
  function and is context-dependent (GADD34 is protective in other settings, e.g.
  PMID:24092754 in PTPN2-null MEFs).
- Antiviral restriction: GADD34 is an NF-kB-stimulated gene downstream of STING and
  restricts influenza A
  [PMID:41747053 "Among these NSGs, growth arrest and DNA damage-inducible protein 34 (GADD34) was crucial for IAV restriction."],
  and attenuates HIV-1 by a mechanism that does *not* need the phosphatase
  [PMID:31778897 "GADD34 N-terminal ER-binding-helix amino acid region 1-192 alone was found to be sufficient for the inhibition of HIV-1 replication whereas protein-phosphatase -1-binding domain and eIF-2α-phosphatase activity of GADD34 were not crucial for anti-HIV-1 activity."].
  Conversely enterovirus 71 exploits GADD34 for IRES activity (UniProt
  CC:FUNCTION, PubMed:34985336) — so the virus-facing effects are not a single
  conserved "antiviral" function.
- Genotoxic stress / growth arrest: the original cloning paper is correlative
  [PMID:9153226 "The association of GADD34 expression with certain types of apoptosis and its homology with a known apoptosis regulator suggests that GADD34 may play a role in apoptosis as well."],
  and Lyn binding modulates the overexpression phenotype
  [PMID:11517336 "Lyn negatively regulated the proapoptotic function of GADD34 in a kinase-dependent manner."].
- p53: a single 2003 overexpression study
  [PMID:14635196 "Transfected Myc-tagged p53 was dose-dependently phosphorylated at Ser15 by increasing the amount of GADD34."].
  No kinase or mechanism was identified, no replication found, and UniProt hedges
  ("May promote apoptosis by inducing p53/TP53 phosphorylation on 'Ser-15'"). Treated
  as an over-annotation in the review.

## GO-CAM cross-check (`gocams/index.tsv`)

Three production models contain O75807:

- `61e0e55600000407` "SP_GADD34- PPP1CA": PPP1R15A activity typed
  `GO:0060090 molecular adaptor activity`, `occurs_in GO:0005783`. This is the row
  the GOA `molecular adaptor activity` IDA mirrors. The review proposes refining
  that to `GO:0140767 enzyme-substrate adaptor activity`; if accepted, the model's
  MF typing should be refined to match.
- `69d8496c00001576` and `69d8496c00001701` (STING/influenza M1): PPP1R15A typed
  `GO:0140870 RNA polymerase inhibitor activity`, `part_of GO:0044828`. Both GOA
  rows come from PMID:41747053, whose full text is not in the cache
  (`full_text_available: false`), so the review defers to the curator and keeps
  both as non-core.

## Decisions taken in the review (summary)

- `GO:0000164` protein phosphatase type 1 complex (5 rows) — ACCEPT; this is the
  GADD34:PP1 holoenzyme.
- `GO:0008157` PP1 binding (4 rows), `GO:0071074` eIF2 binding, `GO:0072542`
  protein phosphatase activator activity — ACCEPT; the two docking activities that
  define the holophosphatase.
- `GO:0060090` molecular adaptor activity — MODIFY to `GO:0140767`
  enzyme-substrate adaptor activity.
- `GO:0019888` protein phosphatase regulator activity (5 rows) — MODIFY to
  `GO:0072542`, the directional descendant the gene already carries.
- `GO:0005515` protein binding (6 rows) — per the protein-binding policy, MODIFY
  the PPP1CA rows to `GO:0008157`, the TARDBP row to `GO:0140767`, and REMOVE the
  two uninformative rows (PPP1R1A; CTBP2 from a large-scale liver interactome).
- `GO:0006446` and `GO:0043558` — MODIFY to `GO:0032058`, which the gene already
  carries and which states the direction (positive).
- `GO:0016020` membrane — MODIFY to `GO:0005789` + `GO:0005741`.
- `GO:0005737` cytoplasm — MODIFY to `GO:0005829` cytosol.
- `GO:0005783` ER (4 rows), `GO:0005789` ER membrane (2 rows) — ACCEPT (root
  organelle plus its established sub-compartment, per `projects/ORGANELLES.md`).
- `GO:0005739` mitochondrion, `GO:0005741` mitochondrial outer membrane,
  `GO:0005794` Golgi, `GO:0005829` cytosol — KEEP_AS_NON_CORE.
- `GO:0051246` regulation of protein metabolic process (ARBA) — TOO_GENERAL.
- `GO:0006915` apoptotic process — TOO_GENERAL (entailed by the retained
  `GO:0070059`).
- `GO:0051726` regulation of cell cycle, `GO:1901798` p53-mediated signalling —
  MARK_AS_OVER_ANNOTATED.
- `GO:0006974` DNA damage response — KEEP_AS_NON_CORE (genuine genotoxic
  inducibility, no role in repair or checkpoint).
- No `NEW` annotations proposed. The autophagy and lysosomal-biogenesis effects
  are downstream of translational tuning, not steps GADD34 performs.
