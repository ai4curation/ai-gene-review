# pab1 (SPAC227.07c, UniProt Q12702) — curation notes

Schizosaccharomyces pombe PP2A regulatory subunit B (PR55/B55). Orthologue of
S. cerevisiae Cdc55 and human PPP2R2A. Sole B55-type subunit in fission yeast;
holoenzyme = Paa1 (A/PR65 scaffold) + Ppa1 or Ppa2 (C) + Pab1 (B55).

Inputs used: `pab1-uniprot.txt`, `pab1-goa.tsv` (25 rows), the Falcon/Edison
deep-research report `pab1-deep-research-falcon.md`, and the cached
publications. Full text is cached only for PMID:25487150, PMID:28041796 and
PMID:28103117; PMID:9078365, PMID:16823372, PMID:20876564, PMID:26776736 and
PMID:29079657 are abstract-only. Where a PomBase experimental row rests on the
uncached full text I accepted/deferred rather than second-guessed (CLAUDE.md
"do not overrule curators from incomplete evidence").

## Identity and architecture

- Cloned with paa1+ by Kinoshita et al. 1996: [PMID:9078365 "We isolated fission
  yeast genes paa1+ and pab1+ encoding the regulatory subunits PR65 and PR55,
  respectively."]. paa1+ is essential; pab1+ is not required at 26-33 degrees C.
- 463 aa, six annotated WD repeats (UniProt), phosphoserine at Ser134 (large-scale
  phosphoproteome, PMID:18257517). InterPro IPR000009 PP2A_PR55; PANTHER PTHR11871.
- Non-catalytic: the deep research frames it correctly —
  [file:SCHPO/pab1/pab1-deep-research-falcon.md "Its primary molecular role is to
  select and position phosphoprotein substrates for dephosphorylation by the
  associated catalytic subunit and to influence holoenzyme localization."]
- PP1-docking-site mutants of Pab1 leave holoenzyme stoichiometry unchanged in
  Paa1-TAP purifications: [PMID:25487150 "We conclude that the PP1 docking site
  mutations do not alter the integrity of the PP2A-B55 or PP2A-B56 holoenzyme
  complexes."]

## Null phenotype

[PMID:9078365 "Gene disrupted delta pab1 cells were pear- or round-shaped, and
lost the polar distributions of actin and microtubules."]; [PMID:9078365 "delta
pab1 cells were defective in cell wall synthesis and sporulation at permissive
temperatures."]; osmoremedial ts phenotype and delayed cytokinesis at restrictive
temperature; chromosome segregation normal. Lahoz et al. add that
[PMID:20876564 "Pab1 is also required to activate polarized cell growth."].
Lucena et al.: [PMID:28103117 "pab1Δ cells had a significantly longer cell cycle:
whereas wild type cells required 120 min to complete the cell cycle (i.e. the
time from the first peak of septation to the second peak), pab1Δ cells required
180 min."]

## Function 1 — CDK-antagonising phosphatase restraining mitotic entry (core)

- Chica et al. 2016 (abstract only): [PMID:26776736 "In the presence of
  nutrients, greatwall (Ppk18) protein kinase is inhibited by TORC1 and PP2A·B55
  is active."]; [PMID:26776736 "High levels of PP2A·B55 prevent the activation of
  mitotic Cdk1·Cyclin B, and cells increase in size in G2 before they undergo
  mitosis."]; on nitrogen limitation [PMID:26776736 "the activation of greatwall
  (Ppk18) leads to the phosphorylation of endosulfine (Igo1) and inhibition of
  PP2A·B55, which in turn allows full activation of Cdk1·CyclinB and entry into
  mitosis with a smaller cell size."]
- Mechanism (Lucena et al. 2017, full text): [PMID:28103117 "Both proteins
  undergo dramatic cell cycle-dependent changes in phosphorylation that are
  dependent upon PP2A associated with the regulatory subunit Pab1."];
  [PMID:28103117 "Thus, pab1Δ largely eliminated cell cycle-dependent changes in
  phosphorylation of Wee1 and Cdc25."]; Wee1 stays partially phosphorylated,
  Cdc25 stays hyperphosphorylated; protein-level oscillations unaffected.
  No reconstitution with purified holoenzyme, so direct-substrate status of
  Wee1/Cdc25 is inferred, not shown. Hence GO:0019888 (regulator activity,
  contributes_to) is the right MF level for that row.
- Martin et al. summarise: [PMID:28041796 "PP2A-B55Pab1 inhibits entry into
  mitosis through the dephosphorylation of Wee1 and Cdc25"].
- Note the sign difference from budding yeast: PP2A-Cdc55 promotes mitotic entry
  in S. cerevisiae (see genes/yeast/CDC55), whereas PP2A-B55(Pab1) restrains it,
  as in metazoa. Both IEA (ARBA) and IMP rows for GO:0010972 accepted.

## Function 2 — Nutrient-gated repression of TORC2-Gad8 signalling (core)

Martin et al. 2017 (full text):
- [PMID:28041796 "Under nutrient-rich conditions, PP2A-B55Pab1 dephosphorylates
  Gad8 Ser546, repressing its activity."]
- Direct: [PMID:28041796 "PP2A-B55Pab1 could proficiently reduce the
  phosphorylation of Gad8 at Ser546"] (in vitro, reverted by okadaic acid);
  [PMID:28041796 "strongly suggest that PP2A-B55Pab1 can directly repress the
  activity of the TORC2-Gad8 module through the direct dephosphorylation of Gad8
  at Ser546."]; [PMID:28041796 "Co-precipitation assays showed that PP2A-B55Pab1,
  Tor1, and Gad8 could be found together in the cell"].
- Acute depletion: [PMID:28041796 "addition of thiamine and auxin rapidly led to
  the almost complete disappearance of B55Pab1, which was accompanied by an
  increase in the phosphorylation of Gad8 at Ser546, cell shortening, and the
  induction of mei2 expression"] — cell-cycle distribution unchanged, so the
  differentiation effect is not a G1-arrest artefact.
- Gating: [PMID:28041796 "TORC1 promotes the activity of PP2A-B55Pab1 through the
  repression of the PP2A-B55Pab1 inhibitory module constituted by the kinase
  Greatwall and its substrate Endosulfin (Igo1 in fission yeast)"];
  [PMID:28041796 "TORC1 inactivation upon starvation leads to the inactivation of
  PP2A-B55Pab1 through the Greatwall-Endosulfin pathway."]
- Mating read-out: [PMID:28041796 "Strikingly, in the pab1Δ culture, mating
  products could be observed earlier and to a higher extent than in the WT
  strain, indicating an exacerbated response in this mutant"].
- Decision: GO:1903939 regulation of TORC2 signaling (EXP) → MODIFY to
  GO:1903940 negative regulation of TORC2 signaling (sign is explicit in the
  paper). GO:0031138 negative regulation of conjugation (IMP, two rows) →
  KEEP_AS_NON_CORE: real phenotype, but conjugation is the downstream
  physiological read-out of the Gad8/TORC2 repression (via Ste11), not the step
  Pab1 performs.
- Laboucarie et al. 2017 (abstract only) extend the same logic to the SAGA
  subunit Taf12: [PMID:29079657 "Taf12 phosphorylation increases early upon
  starvation and is controlled by the opposing activities of the PP2A
  phosphatase, which is activated by TORC1, and the TORC2-activated Gad8AKT
  kinase."]. The PomBase complex IDA, activator EXP and conjugation IMP rows from
  this paper rest on uncached full text; assessed by consistency with the other
  papers.
- Localisation from this paper: [PMID:28041796 "PP2A-B55Pab1-GFP localizes
  throughout the cell and is particularly enriched in the nucleus"]. No nucleus
  row exists in GOA; I did not add one (CC would need a curated observation, and
  PomBase has the paper).

## Function 3 — PP1-docking node of the mitotic phosphatase relay (core)

Grallert et al. 2015 (full text):
- [PMID:25487150 "PP1 first reactivates PP2A-B55; this enables PP2A-B55 in turn
  to promote the reactivation of PP2A-B56 by dephosphorylating a PP1-docking site
  in PP2A-B56, thereby promoting the recruitment of PP1."]
- Pab1 has an RVxF motif (R52/V54/F56): [PMID:25487150 "we found that both
  B55Pab1 and B56Par1 associated with PP1Dis2 in immunoprecipitation assays"];
  [PMID:25487150 "The interaction between PP1Dis2 and B55Pab1 was abolished by
  mutating the PP1 docking consensus motif"]; [PMID:25487150 "We conclude that
  both B56Par1 and B55Pab1 contain genuine PP1Dis2 docking motifs."]
- PP1(Dis2) on Pab1 peaks at metaphase; on Par1 at telophase.
- Output: [PMID:25487150 "PP2A-B55Pab1 removed B56-Phos reactivity from B56Par1
  in an in vitro assay"]; [PMID:25487150 "purified PP1Dis2 enhanced the B56-Phos
  activity of purified PP2A-B55Pab1 in a docking site dependent manner"].
- Phenotype: [PMID:25487150 "Blocking PP1Dis2 recruitment to either B55Pab1 or
  B56Par1 in synchronised divisions generated significant errors in chromosome
  segregation and delayed the metaphase/anaphase transition"].
- The GOA rows from this paper are only "protein binding" (dis2 x2, paa1).
  Removed per the protein-binding policy (Pab1 is the docking target of a
  regulator; the paa1 contact is holoenzyme assembly already expressed by
  GO:0000159). The biology is carried in core_functions[2]. The BP used there,
  GO:0006470 protein dephosphorylation, has no GOA row (validator warning);
  human PPP2R2A carries it (IDA/IMP) but I did not add a NEW row — conservative.

## Function 4 — SIN antagonism at the SPB (core)

Lahoz et al. 2010 (abstract only, PMC2998309 exists):
- [PMID:20876564 "Here we show that a mutation in the pab1 gene, which encodes
  the B-regulatory subunit of the protein phosphatase 2A (PP2A), suppresses
  mutations in the etd1 gene."]; [PMID:20876564 "Interestingly, the loss of Pab1
  function restored the activity of Spg1 in Etd1-deficient cells."];
  [PMID:20876564 "The loss of pab1 function also rescues the lethality of mutants
  of other genes in the SIN cascade such as mob1, sid1, and cdc11."]
- [PMID:20876564 "Two-hybrid assays indicate that Pab1 physically interacts with
  Mob1, Sid1, Sid2, and Cdc11, suggesting that the phosphatase 2A B-subunit is a
  component of the SIN complex."]; [PMID:20876564 "Together, our results indicate
  that PP2A-Pab1 plays a novel role in cytokinesis, regulating SIN activity at
  different levels."]
- Decisions: GO:0031030 negative regulation of septation initiation signaling
  (IGI etd1) ACCEPT. The four two-hybrid "protein binding" rows (sid2, sid1,
  mob1, cdc11) REMOVE — no substrate identified (Spg1 inhibition is inferred and
  Spg1 is not a two-hybrid partner), so no informative MF can be derived.
  SPB (GO:0044732) and mitotic spindle (GO:0072686) IDA rows ACCEPT, deferring
  to PomBase on the imaging (the deep research also records spindle
  localisation from this paper). Later work (Chica et al. 2022, per the deep
  research) confirms PP2A-B55 restrains untimely septation in metaphase-arrested
  cells.

## Molecular-function rows

- GO:0019888 protein phosphatase regulator activity, EXP (PMID:28103117,
  contributes_to) and IEA: ACCEPT.
- GO:0072542 protein phosphatase activator activity, EXP (PMID:29079657):
  MODIFY → GO:0140767 enzyme-substrate adaptor activity. A B55 subunit does not
  raise the catalytic rate of the C subunit (the A-C dimer is active); it confers
  substrate selection ([PMID:28041796 "B55 (also known as Pab1) and B56 (also
  known as Par1), which provide substrate specificity to the complex."]). Same
  term used in the CDC55 and PPP2R2A reviews.
- GO:1902531 regulation of intracellular signal transduction, IEA (ARBA):
  MODIFY → GO:1903940 + GO:0031030 (the specific, experimentally supported
  pathways).

## Localisation rows

- GO:0005829 cytosol HDA (ORFeome atlas, [PMID:16823372 "we determined the
  localization of 4,431 proteins, corresponding to approximately 90% of the
  fission yeast proteome, by tagging each ORF with the yellow fluorescent
  protein."]) and IBA (tws donor): ACCEPT; consistent with the whole-cell
  GFP distribution and with a cytoplasmic substrate (Gad8).

## Action tally (25 rows)

ACCEPT 13; KEEP_AS_NON_CORE 2 (conjugation IMP x2); MODIFY 3 (activator EXP,
TORC2 EXP, generic signalling IEA); REMOVE 7 (all protein-binding IPI rows);
UNDECIDED 0; NEW 0.

## Open questions

- Which SIN component is dephosphorylated by PP2A-Pab1?
- How is PP2A-B55(Pab1) inactivated at mitotic commitment (Grallert et al.:
  "currently unclear"), and how does Igo1 partition between the nutrient and
  mitotic cycles?
- Are Wee1/Cdc25 direct substrates docking on the conserved B55 helix-binding
  surface (Kruse et al. 2024, per deep research)?
- Role of the Ser134 phosphosite.
