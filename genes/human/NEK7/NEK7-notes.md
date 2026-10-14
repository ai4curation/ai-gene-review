# NEK7 (human, Q8TDX7) curation notes

**Provenance note:** Provider deep research for NEK7 was not available (Falcon returned
402 Payment Required; Perplexity is not configured). No `NEK7-deep-research-<provider>.md`
file exists. This notes file is a manual literature synthesis that replaces it. Every claim
below is anchored to a cached publication in `publications/` with a verbatim quote.

## Identity and family

- NEK7 is a 302-aa NIMA-related serine/threonine kinase, closest paralog NEK6
  [PMID:11701951 "Its open reading frame encodes a 302-amino acid protein and is 77% identical to human NEK6 protein."].
- Almost the whole protein is the kinase domain; NEK6/NEK7 "have little noncatalytic sequence
  but bind to the carboxyl-terminal noncatalytic tail of Nercc1/Nek9" [PMID:12840024].

## Catalytic activity and its regulation (NEK9 -> NEK7 cascade)

- NEK9 (Nercc1) activates NEK7 in vitro [PMID:12840024 "Nercc1 activates Nek7 in vitro in a similar manner"].
- NEK7 is intrinsically autoinhibited by Tyr97 ("Tyr-down"); NEK9 C-terminal binding releases it
  [PMID:19941817 "Strikingly, Nek9-CTD did not significantly increase the activity of Nek7-Y97A, suggesting that the mechanism of Nek7 activation occurs through release of Tyr97 autoinhibition."].
  Note: in this paper NEK9 is the activator and NEK7 the activated kinase; NEK7 itself is not shown to activate anything.
- NEK9 binds the NEK7 C-lobe, induces back-to-back dimerization and trans-autophosphorylation
  [PMID:26522158 "In this study we elucidated the structural basis of the Nek7–Nek9 interaction, which occurs at an unexpected site on the C-lobe of Nek7, and discovered that dimeric Nek9 stimulates Nek7 autophosphorylation."].
- First physiological substrate with mapped sites: EML4 Ser144/Ser146
  [PMID:31409757 "The mitotic kinases NEK6 and NEK7 phosphorylated the EML4 N-terminal domain at Ser144 and Ser146 in vitro, and depletion of these kinases in cells led to increased EML4 binding to microtubules in mitosis."].

## Mitotic/centrosomal role (catalytic)

- Centrosome-enriched, microtubule-independent
  [PMID:17101132 "We show here that the endogenous Nek7 protein is enriched at the centrosome in a microtubule-independent manner."].
- Required for centrosomal microtubule nucleation and spindle assembly
  [PMID:17586473 "NEK7 knockdown by RNAi caused a prometaphase arrest of the cell cycle with monopolar or disorganized spindle."]
  [PMID:17586473 "we observed a decrease in the centrosomal gamma-tubulin levels and reduction of the microtubule re-growth activity in the NEK7-suppressed cells."].
- Activated in mitosis; inactive mutants/depletion give fragile spindles; spindle pole localisation
  [PMID:19414596 "while both kinases localize to spindle poles, only Nek6 obviously localizes to spindle microtubules"].
- Chromosome congression via EML4 phosphorylation [PMID:31409757].
- Mouse knockout: late embryonic/early postnatal lethality, cytokinesis failure, polyploidy, cilia defects
  [PMID:20473324 "We show that absence of Nek7 leads to lethality in late embryogenesis or at early post-natal stages and to severe growth retardation."].
- He et al. state spindle function requires catalytic activity
  [PMID:26814970 "Nek7 regulates microtubule dynamic instability and spindle assembly which required the catalytic activity of Nek712,13,22,23."].

## NLRP3 inflammasome licensing (non-catalytic, scaffold)

- Genetic screens in mouse identified NEK7 as essential for NLRP3 activation
  [PMID:26553871 title "...Screen Identifies NEK7 as an Essential Component of NLRP3 Inflammasome Activation"];
  [PMID:26814970 "We have shown that Nek7 is an essential factor that specifically and non-redundantly functions downstream of potassium efflux to regulate the activation of the NLRP3 inflammasome."].
- Direct binding to NLRP3 LRR; kinase-dead NEK7 (K64M) rescues
  [PMID:26642356 "These results indicate that the kinase activity of NEK7 is nonessential for activation of the NLRP3 inflammasome."]
  [PMID:26814970 "In contrast, the catalytic activity of Nek7 is not required for NLRP3 activation."].
- Mutual exclusivity with mitosis
  [PMID:26642356 "Thus, NEK7 acts as a switch between mitosis and inflammasome activation competence, both of which require NEK7."].
- Cryo-EM NLRP3-NEK7 structure; NEK7 bridges NLRP3 subunits; NEK9- and NLRP3-binding surfaces overlap
  [PMID:31189953 "In NLRP3, the LRR itself is too short to reach the adjacent LRR in the hypothetical oligomer, and NEK7 bridges the gap between adjacent NLRP3 subunits."].
- Active disc structure contains ten NLRP3 + ten NEK7; NEK7 opens the inactive cage at the MTOC
  [PMID:36442502 "whereas LRR is required for the inactive cage structure, its interaction with NEK7 at the MTOC disrupts the cage to allow formation of the active NLRP3 disc."]
  [PMID:36442502 "centrosomal NIMA-related kinase 7 (NEK7), important in mitosis, has been identified as a scaffolding protein in NLRP3 activation independent of its kinase activity"].
- LATS1/2 phosphorylation of NLRP3 at the MTOC promotes NEK7 binding [PMID:39173637].
- HCMV US18 associates with NEK7 and NLRP3 [PMID:40450990].

### Species/context caveat

- In human myeloid cells (BLaER1, THP-1), NLRP3 can be activated independently of NEK7 via an
  IKKβ-dependent priming route; mouse macrophages rely predominantly on NEK7
  [PMID:36384135 "Although this IKKβ-dependent priming signal is the default pathway by which human cells engage the NLRP3 inflammasome, murine macrophages predominantly rely on NEK7 for NLRP3 priming."]
  [PMID:36384135 "In line with the results obtained in BLaER1 cells, THP-1 cells deficient in NEK7 showed no attenuation of Nigericin-triggered inflammasome activation"].
  Human NEK7 can still prime NLRP3 when expressed
  [PMID:36384135 "showing that hsNEK7 is capable of priming NLRP3"].

## Other

- ANKS3 binds NEK7 and keeps it cytoplasmic [PMID:26188091 "Importantly, Anks3 retained Nek7 in the cytoplasm"].
- Large-scale interactome screens (HuRI PMID:32296183; Haenig et al. Y2H PMID:32814053; kinase AP-MS PMID:32707033)
  report many binary partners; individually uninformative for function.
- Telomerase RNAi screen (PMID:21531765) – abstract does not mention NEK7; full text not available.

## Curation decisions summary

- Core MF 1: protein serine/threonine kinase activity (mitotic spindle assembly, centrosome/spindle pole).
- Core MF 2: non-catalytic activator of NLRP3 (GO:0140677 with has_input NLRP3) -> positive regulation
  of NLRP3 inflammasome complex assembly; NEK7 is a stoichiometric subunit of the active NLRP3 disc.
- Do not combine kinase activity with inflammasome licensing: catalytic activity is dispensable there.
- GO:0140677 IDA from PMID:19941817 appears inverted (that paper shows NEK9 activating NEK7).
- 74 generic protein binding rows: REMOVE, except NLRP3 IPI from PMID:26814970 -> MODIFY to GO:0140677.
