# SLC29A4 (PMAT / ENT4) curation notes
<!-- review written 2026-11-15 -->


UniProt: Q7RTT9 (S29A4_HUMAN), 530 aa, 11 TM domains, SLC29A/ENT family (TC 2.A.57),
PANTHER PTHR10332:SF10 (EQUILIBRATIVE NUCLEOSIDE TRANSPORTER 4). HGNC:23097.

## Core identity: an "uptake-2" polyspecific organic cation / monoamine transporter

Although classified in the SLC29/ENT (equilibrative nucleoside transporter) family and
named ENT4, PMAT is functionally NOT a nucleoside transporter. Its principal physiological
role is low-affinity, high-capacity, Na+/Cl--independent, membrane-potential-sensitive
(electrogenic), pH-sensitive transport of monoamine neurotransmitters and other organic
cations — i.e. an "uptake-2" transporter like the OCTs (SLC22A1-3).

- Cloned and named "plasma membrane monoamine transporter": transports serotonin
  (Km 114 uM), dopamine (Km 329 uM) and the neurotoxin MPP+ (Km 33 uM); "there is no
  significant interaction of PMAT with nucleosides or nucleobases"; "PMAT-mediated monoamine
  transport does not require Na(+) or Cl(-) but appears to be sensitive to changes in membrane
  potential" [PMID:15448143 "PMAT efficiently transports serotonin (K(m) = 114 mum), dopamine
  (K(m) = 329 mum), and the neurotoxin 1-methyl-4-phenylpyridinium (K(m) = 33 mum). In
  contrast, there is no significant interaction of PMAT with nucleosides or nucleobases"].
- Polyspecific organic cation transporter functionally similar to OCTs: transports TEA,
  guanidine, histamine; inhibited by cimetidine, quinidine; bidirectional
  [PMID:16099839 "PMAT transports classic OCT substrates, such as tetraethylammonium,
  guanidine, and histamine... we therefore conclude that PMAT can function as a polyspecific
  organic cation transporter"].
- Substrate selectivity hierarchy (uptake-2): "hPMAT is highly selective toward serotonin
  (5-HT) and dopamine, with the rank order of transport efficiency (V(max)/K(m)) being:
  dopamine, 5-HT >> histamine, norepinephrine, epinephrine"; PMAT is "a major uptake(2)
  transporter for 5-HT and dopamine" whereas OCT3 is "a major uptake(2) transporter for
  histamine, epinephrine, and norepinephrine" [PMID:20858707]. => DA and 5-HT are the core
  physiological substrates; NE and epinephrine uptake by PMAT is genuine but minor (OCT3
  dominates those) -> non-core.
- Electrogenic/membrane-potential driven, pH-sensitive: "establish the physiological
  inside-negative membrane potential as a driving force for PMAT-mediated OC transport"
  [PMID:22396231]. Activated at acidic pH [UniProt ACTIVITY REGULATION; PMID:17018840
  "PMAT-mediated MPP(+) uptake is strongly dependent on extracellular pH. Lowering
  extracellular pH from 7.4 to 6.6 greatly stimulated PMAT-mediated MPP(+) uptake"].

## Adenosine: genuine but secondary, pH-dependent

PMAT transports the purine nucleoside adenosine, but only adenosine among nucleosides, and
with ~10-fold lower efficiency than organic cations; relevant to cardiac/ischemic adenosine
regulation.
- "both human and mouse ENT4 exhibited a novel, pH-dependent adenosine transport activity
  optimal at acidic pH ... and absent at pH 7.4... ENT4-mediated nucleoside transport was
  adenosine selective" [PMID:16873718].
- "Among 12 naturally occurring nucleosides and nucleobases, only adenosine was significantly
  transported by PMAT... adenosine is transported by PMAT at an efficiency (V(max)/K(m)) at
  least 10-fold lower than that of the organic cation substrates... Functionally, PMAT should
  be viewed as a polyspecific organic cation transporter rather than an archetypical nucleoside
  transporter" [PMID:20592246].
- Bidirectional, allosteric at acidic pH [PMID:31537831 "both the influx and efflux of
  2-chloroadenosine by hENT4 are enhanced in an acidic environment"].
- UniProt MISCELLANEOUS: "Does not interact with nucleosides, nucleobases or nucleotides,
  other than a moderate activity for adenosine."

=> The generic GO term "nucleoside transmembrane transporter activity" (GO:0005337) and the
nucleoside-transport BP terms (GO:0015858, GO:1901642) OVER-STATE PMAT's actual adenosine-only
activity. The accurate specific MF is purine nucleoside transporter (GO:0015211) and the BP is
adenosine transport (GO:0032238, already annotated).

## PAINT phylogenetic evidence of nucleoside-transport loss

`just paint-losses human SLC29A4` reports an IRD at PANTHER node PTN000035835 for GO:0005337
(nucleoside transmembrane transporter activity), dated 2026-08-28, blocking the IBD at
PTN000035696, not re-annotated below. PTN000035835 is also the node from which PMAT's
GO:0008504 monoamine-transporter IBA descends. The PAINT curator judged that, in the
PMAT/monoamine clade, the ancestral nucleoside-transporter function diverged/was lost — exactly
consistent with the functional data above. This supports MARK_AS_OVER_ANNOTATED for the
residual nucleoside-transporter rows (which come from InterPro family IEA and Reactome TAS, not
from IBA — PAINT correctly did not propagate nucleoside transport to PMAT).

## Localization

Plasma membrane (the defining location). Polarized: APICAL in kidney epithelium
[PMID:17018840] and in choroid plexus (CSF-facing) epithelium [PMID:23255610 "PMAT protein is
localized to the apical (CSF-facing) membrane of the CP epithelium"]. At the BBB endothelium,
both luminal and abluminal (basolateral) [PMID:26376205 "Western blotting demonstrated its
localization at the luminal and abluminal sides of BMECs"].

## Physiological roles / substrate detoxification / barriers

- CNS monoamine homeostasis (uptake-2), especially 5-HT and DA [PMID:15448143, PMID:20858707].
- Astrocytic histamine clearance: PMAT is the major low-affinity histamine transporter in human
  astrocytes [PMID:23505051 "Drug inhibition assays and gene knockdown assays revealed the major
  contribution of PMAT and the minor contribution of OCT3 to histamine transport"].
- Choroid plexus / blood-CSF barrier: Slc29a4-/- mice show reduced CP uptake of monoamines and
  MPP+; "PMAT is a major transporter for CP uptake of bioactive amines and xenobiotic cations...
  PMAT may play an important role in protecting the brain from cationic neurotoxins"
  [PMID:23255610].
- Cationic neurotoxin / xenobiotic / drug handling at the BBB (MPP+, 1-benzyl-TIQ, amisulpride,
  metformin) [PMID:26376205, PMID:31842924]. Bidirectional -> can act as an efflux route for
  organic cations [PMID:16099839 trans-stimulation/efflux; PMID:31842924 amisulpride efflux].
- Cardiac adenosine regulation during ischemia (acidic pH) [PMID:16873718, PMID:31537831].
- Renal organic cation reabsorption (apical) [PMID:17018840].

## Over-annotations / issues identified

- GO:0005337 nucleoside transmembrane transporter activity (IEA InterPro, TAS Reactome x2),
  GO:0015858 nucleoside transport (IEA ARBA), GO:1901642 nucleoside transmembrane transport
  (IEA InterPro): too general; PMAT transports only adenosine. MARK_AS_OVER_ANNOTATED.
- GO:0008324 monoatomic cation transmembrane transporter activity (IEA/ISS from mouse Q8R139)
  and GO:0098655 monoatomic cation transmembrane transport (IEA/ISS): PMAT transports ORGANIC
  cations (monoamines, MPP+, TEA), not monoatomic/inorganic cations. These most likely descend
  from an old generic "cation transmembrane transporter" annotation on the mouse ortholog that
  was relabelled to "monoatomic cation" after GO split the cation branch. MODIFY to the organic
  cation branch (MF GO:0015651 quaternary ammonium group transmembrane transporter activity; BP
  GO:0015697 quaternary ammonium group transport). GO:0015695 organic cation transport and
  GO:0015101 organic cation transmembrane transporter activity are both OBSOLETE (QuickGO).
- GO:0022857 transmembrane transporter activity, GO:0016020 membrane, GO:0055085 transmembrane
  transport: bare root terms -> TOO_GENERAL (specific terms asserted elsewhere).
- GO:0098793 presynapse (IEA GO_REF:0000108, auto-inferred from serotonin uptake): no
  localization evidence; PMAT is an extraneuronal/uptake-2 transporter documented on apical
  epithelial, BBB-endothelial and astrocyte membranes. Over-reach -> MARK_AS_OVER_ANNOTATED.
- GO:0150104 transport across blood-brain barrier (NAS x2): the two NAS citations (PMID:26590417,
  PMID:30280653) are general BBB review articles that do not establish PMAT-specific BBB transport;
  the claim is nonetheless supportable from PMID:26376205 / PMID:31842924. KEEP_AS_NON_CORE.

## Core MF ids (QuickGO-verified non-obsolete 2026-11-15)

- GO:0008504 monoamine transmembrane transporter activity (primary) — obsolete=False
- GO:0005326 neurotransmitter transmembrane transporter activity — obsolete=False
- GO:0015651 quaternary ammonium group transmembrane transporter activity (organic cation) — obsolete=False
- GO:0015211 purine nucleoside transmembrane transporter activity (adenosine, non-core) — obsolete=False
- Obsolete (NOT used): GO:0015101 organic cation transmembrane transporter activity; GO:0015695 organic cation transport.
