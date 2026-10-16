# RIPK2 (RIP2/RICK/CARDIAK) — curation notes

UniProt O43353. Human. Gene symbol RIPK2 (HGNC).

## Provenance / workflow notes
- `just fetch-gene-pmids human RIPK2` cached 47 publications (all GOA PMIDs).
- Deep research via falcon is known to fail (402 payment). Not attempted. No
  `-deep-research-PROVIDER.md` was hand-written (per CLAUDE.md).
- Extra PMIDs cached for the kinase-vs-scaffold question: PMID:22607974
  (Damgaard/Gyrd-Hansen XIAP-LUBAC), PMID:26320862 (Canning type II inhibitors),
  PMID:22607974. All verified by cached title.

## Domain architecture
N-terminal Ser/Thr/Tyr kinase domain (~1-294) + intermediate (IM) region +
C-terminal CARD (~435-526). CARD mediates CARD-CARD recruitment by NOD1/NOD2 and
homotypic filament (RIPosome) assembly. Kinase catalytic residues: ATP-binding
Lys47; catalytic Asp146 (HRD->HHD motif) [PMID:30026309 "the catalytic aspartate
146 in the “HRD” motif (HHD in human RIPK2)"; "K47 and D146 are catalytic
residues for ATP hydrolysis."].

## (a) Does RIPK2 have bona fide protein kinase activity? YES.
- Ser/Thr autophosphorylation: Ser176 is a regulatory autophosphorylation site;
  S176A abolishes autophosphorylation and significantly decreases catalytic
  activity [PMID:16824733 "Mutation of S176 to alanine not only abolishes
  autophosphorylation of RIP2 but also significantly decreases its catalytic
  activity."]. UniProt EC 2.7.11.1 catalytic activity is ECO:0000269|PubMed:16824733.
- Tyr autophosphorylation: RIP2 autophosphorylates on Tyr474; originally
  classified Ser/Thr but also has tyrosine kinase activity [PMID:21123652
  "we find that RIP2 also has tyrosine kinase activity. RIP2 undergoes
  autophosphorylation on Tyr 474 (Y474). This phosphorylation event is necessary
  for effective NOD2 signaling"]. UniProt EC 2.7.10.2 is ECO:0000269|PubMed:21123652.
- Structural: autophosphorylation coupled to dimerization, BRAF-like
  [PMID:28545134 "RIP2 kinase auto-phosphorylation is intimately coupled to
  dimerization, similar to the case of BRAF."]. Active state = stable dimer with
  disordered phosphorylated activation segment.
- So both the Ser/Thr (GO:0004674 / GO:0106310) and Tyr (GO:0004713) autokinase
  activities are experimentally supported. These are bona fide and ACCEPT-worthy
  as molecular functions. The non-membrane-spanning tyr kinase IEA (GO:0004715,
  EC2.7.10.2 mapping) is defensible but the EXP GO:0004713 is the stronger one.

## (b) Is catalysis REQUIRED for NOD1/NOD2 -> NF-kB signaling? NO (catalysis dispensable).
This is the crux and the literature converges (despite older claims):
- Kinase-dead K47M/K47A still activates NF-kB (Inohara 2000, cited in
  [PMID:18079694 "the K47M kinase-inactive mutant of RICK still activates NF-kappaB
  (Inohara et al , 2000), suggesting that the kinase domain of RICK mediates a
  critical function, other than phosphorylation"]).
- RICK K63-polyUb (K209) does not require kinase activity; it is the step that
  recruits TAK1 [PMID:18079694 "RICK polyubiquitination did not require the kinase
  activity of RICK"; "the residue critical for kinase activity is not essential for
  NF-kappaB activation, polyubiquitination of RICK and interaction of RICK with
  NEMO"].
- Decisive reconstitution: two independent kinase-dead mutants (K47R, D146N)
  restore NOD2 signaling to WT level [PMID:30026309 "introduction of both
  kinase‐dead RIPK2 mutants restored NOD2 signaling and CXCL8 production to a
  similar level as with WT RIPK2 in two independent RIPK2 KO clones, showing that
  the catalytic function is not needed for RIPK2's role in NOD2‐dependent
  inflammatory signaling"; abstract "RIPK2 kinase activity is dispensable for NOD2
  inflammatory signaling"].
- Why inhibitors "work": kinase inhibitors block signaling by antagonizing XIAP
  binding, not by blocking catalysis [PMID:30026309 "RIPK2 inhibitors function
  instead by antagonizing XIAP‐binding and XIAP‐mediated ubiquitination of
  RIPK2. We map the XIAP binding site on RIPK2 to the loop between β2 and β3 of
  the N‐lobe of the kinase, which is in close proximity to the ATP‐binding
  pocket."]. Confirmed independently [PMID:29452636 "We also establish that the
  kinase activity of RIP2 is dispensable for NOD2 signaling. Rather, the
  conformation of the RIP2 kinase domain functions to regulate binding to the
  XIAP-BIR2 domain."].
- Caveat / dissent: Tigno-Aranjuez reported Y474 autophosphorylation "necessary
  for effective NOD2 signaling" [PMID:21123652]. This is the tyrosine-kinase
  requirement claim. The weight of kinase-dead reconstitution (K47R + D146N, which
  abolish both Ser/Thr and the ATP chemistry needed for any autophosphorylation)
  showing FULL rescue (PMID:30026309) indicates catalysis per se is not required;
  inhibitor phenotypes are explained by XIAP-binding disruption. Y474 may matter
  as a conformational/structural feature of the kinase domain rather than as a
  catalytic output. Older inhibitor-based "kinase required" claims
  (Windheim 2007; Nembrini 2009; Tigno-Aranjuez 2010) are reinterpreted this way
  [PMID:30026309 "Initial notions that RIPK2 kinase activity facilitates NOD1 and
  NOD2 signaling were in part based on the finding that kinase activity may be
  required for RIPK2 stability in cells, and in part, on the fact that kinase
  inhibitors could inhibit productive NOD1 and NOD2 signaling"].

Position: RIPK2 is a genuine autokinase, but its catalytic activity is NOT the
essential step for NOD1/NOD2 -> NF-kB/MAPK output. The essential role is the
CARD-scaffold + ubiquitin-scaffold function.

## (c) Real core function: CARD adaptor + ubiquitinated scaffold
1. CARD-CARD recruitment to NOD1/NOD2. NOD1/NOD2 oligomerize on ligand (iE-DAP /
   MDP) and recruit RIPK2 via CARD-CARD [PMID:11087742 "Nod2 interacted with the
   serine-threonine kinase RICK via a homophilic CARD-CARD interaction"; PMID:17054981
   "RICK is recruited by NOD1 through interaction of their respective CARDs."].
   GO:0050700 CARD domain binding (IDA/IPI). GO:0035591 signaling adaptor activity
   (IDA; also the GO-CAM MF for RIPK2 in models 641ce4dc00000050/214).
2. Filament/RIPosome assembly: RIPK2 CARD self-oligomerizes into helical filaments
   nucleated by NOD2 2CARD / NOD1 CARD; polymerization required for NF-kB signaling
   [PMID:30279485 "full-length RIP2 can form long filaments mediated by its caspase
   recruitment domain (CARD)"; "we demonstrate the importance of RIP2 polymerization
   for the activation of NF-κB signalling by NOD2"]. GO:0051260/GO:0042803.
3. Ubiquitinated scaffold. RIPK2 is K63-polyubiquitinated (K209 in kinase domain)
   by XIAP (primary E3), BIRC2/3; M1/linear chains added by LUBAC recruited via
   XIAP [PMID:18079694 K209 K63-Ub recruits TAK1; PMID:22607974 "XIAP ubiquitylates
   RIPK2 and recruits the linear ubiquitin chain assembly complex (LUBAC) to NOD2";
   PMID:19667203 XIAP BIR2 binds RIP2; PMID:23818254; PMID:23806334 RIPK2 is the
   predominant NOD2-regulated Met1-Ub substrate]. These chains dock TAB2/TAB3 ->
   recruit TAK1 (MAP3K7) and NEMO/IKK [PMID:18079694 "polyubiquitination of RICK
   was found to mediate the recruitment of TAK1"; UniProt FUNCTION].
   GO:1902523 positive regulation of protein K63-linked ubiquitination (IDA,
   PMID:17562858); GO:0031398 pos reg protein ubiquitination.
4. Output: positive regulation of canonical NF-kB (GO:0043123), NOD1/NOD2 signaling
   (GO:0070427/GO:0070431), innate immune / defense response to bacterium, cellular
   response to MDP. Also TLR2/3/4, IL-1/IL-18, and TCR (BCL10) signaling, and
   adaptive immunity [PMID:11894098]. Cytosol/plasma-membrane localization; NOD2
   recruits RICK to the plasma membrane [PMID:17355968].

## MAP3K7 (TAK1) consistency check
MAP3K7 review (not edited): treats TAK1 as the ubiquitin-activated MAP3K
downstream of RIPK2 ubiquitination; "TAK1 is required for NOD2-mediated NF-kappaB
activation downstream of RIPK2 ubiquitination". Consistent with this review:
RIPK2 is the K63/M1-ubiquitinated scaffold that recruits TAK1-TAB; TAK1 does the
kinase work on IKK/MAP2Ks. No disagreement. MAP3K7 also handles generic
protein binding by MODIFY->ubiquitin protein ligase binding / REMOVE with the real
interaction captured elsewhere; I follow the same practice here.

## nlr_signaling module check (not edited; recommendations only)
modules/nlr_signaling.yaml RIPK2 adaptor annoton (ripk2_ripk2_kinase_adaptor):
- States "RIPK2 catalytic activity is dispensable for NOD2 signaling... so no
  kinase function is asserted for RIPK2 in this module." AGREE on dispensability
  for the NF-kB output, and with asserting the scaffold (GO:0035591) role as the
  module function. The module's position is consistent with (b)/(c) here.
- Two minor points to report (NOT edit):
  1. The annoton label has been relabelled "RIPK2 adaptor/scaffold" in the module (the annoton id
     is unchanged to keep edges stable), since the module asserts no kinase function.
  2. PANTHER family: the module's PTHR44329 grounding is correct. RIPK2's UniProt record gives
     PTHR44329:SF9 (RECEPTOR-INTERACTING SERINE_THREONINE-PROTEIN KINASE 2), and its IBA anchors
     PTN001908418, PTN002892787 and PTN002892800 are all PTHR44329 nodes
     (interpro/panther/PTHR44329/PTHR44329-paint.tsv). An earlier draft of this note wrongly
     placed those nodes in another family. The deep research "contributes" wording for kinase
     activity is superseded by PMID:30026309/29452636 (dispensable); the module's current
     edit is the better-supported position.
