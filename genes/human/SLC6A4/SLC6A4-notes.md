# SLC6A4 (SERT / 5-HTT, UniProt P31645) — curation notes

Batch 10 canonical-surfaceome backfill. Human serotonin transporter.

## Identity and family

- UniProt P31645 (SC6A4_HUMAN), 630 aa, 12 transmembrane helices (LeuT/NSS fold),
  cytoplasmic N- and C-termini. HGNC:11050, gene on chr 17q11.2.
- SNF/NSS family (TC 2.A.22), SLC6A4 subfamily: [file:human/SLC6A4/SLC6A4-uniprot.txt "Belongs to the sodium:neurotransmitter symporter (SNF) (TC 2.A.22) family. SLC6A4 subfamily"]. PANTHER PTHR11616:SF105 "SODIUM-DEPENDENT SEROTONIN TRANSPORTER".
- Paralogs in the monoamine branch of SLC6: DAT (SLC6A3), NET (SLC6A2). The wider
  SLC6 family also contains amino-acid and GABA/glycine transporters — relevant to
  an over-broad "amino acid transport" IBA (below).

## Core molecular function: serotonin:Na+:Cl- symporter (secondary active)

- Core MF = **GO:0005335 serotonin:sodium:chloride symporter activity** (verified real,
  non-obsolete; QuickGO is_a ancestry — OLS getAncestors was returning glitched byte-identical
  lists this session — shows it runs through both the symporter / solute:Na+ / sodium:chloride
  branch AND GO:0008504 monoamine transmembrane transporter activity; it is NOT under
  GO:0005326 neurotransmitter transmembrane transporter activity).
- Na+- and Cl--dependent, secondary-active symport driven by the Na+ (and Cl-) gradient;
  K+ counter-transport in the cycle; overall electroneutral. Not an antiporter, not a
  uniporter, not heteromeric.
- UniProt FUNCTION: [file:human/SLC6A4/SLC6A4-uniprot.txt "Serotonin transporter that cotransports serotonin with one Na(+) ion in exchange for one K(+) ion and possibly one proton in an overall electroneutral transport cycle. Transports serotonin across the plasma membrane from the extracellular compartment to the cytosol thus limiting serotonin intercellular signaling"] and [file:human/SLC6A4/SLC6A4-uniprot.txt "Na1(+) and Cl(-) ions remain bound throughout the transport cycle"].
- Rhea RHEA:75839: serotonin(out) + K+(in) + Na+(out) + H+(in) = serotonin(in) + K+(out) +
  Na+(in) + H+(out). ChEBI serotonin(1+) = CHEBI:350546, Na+ = CHEBI:29101, K+ = CHEBI:29103,
  H+ = CHEBI:15378; Cl- (co-transported, CHEBI:17996) is retained throughout the cycle.
- Original human cloning [PMID:7681602 "A Na(+)- and Cl(-)-coupled serotonin (5-hydroxytryptamine, 5HT) transporter is expressed on human neuronal, platelet, placental, and pulmonary membranes"]; [PMID:7681602 "Transfection of one of these cDNAs into HeLa cells yields a high-affinity (Km = 463 nM), Na(+)- and Cl(-)-dependent 5HT transport activity"].
- Mechanism/structure: X-ray [PMID:27049939 "The serotonin transporter (SERT) terminates serotonergic signalling through the sodium- and chloride-dependent reuptake of neurotransmitter into presynaptic neurons"]; cryo-EM full cycle [PMID:34851672 "The serotonin transporter (SERT) terminates serotonin signaling by using sodium and chloride gradients to drive reuptake of serotonin into presynaptic neurons"]; Cl- bound throughout [PMID:27756841 "our data suggest that Cl- is bound to SERT during the entire catalytic cycle"]; Cl--coupling determinant Asn-101 [PMID:21730057].
- KM for serotonin ~0.3–1.9 uM across studies (UniProt BIOPHYSICOCHEMICAL PROPERTIES).

## Physiological roles

- **Presynaptic 5-HT reuptake** terminating serotonergic transmission in brainstem raphe
  neurons: [file:human/SLC6A4/SLC6A4-uniprot.txt "acts primarily in brainstem raphe neurons to mediate serotonin uptake from the synaptic cleft back into the pre-synaptic terminal thus terminating serotonin signaling at the synapse"]. Bona fide reuptake transporter → GO:0098810 neurotransmitter reuptake, GO:0051610 serotonin uptake ACCEPT.
- **Platelet / peripheral 5-HT uptake**: SERT loads 5-HT from plasma into platelets (stored
  in dense granules via VMAT) [file:human/SLC6A4/SLC6A4-uniprot.txt "Regulates blood serotonin levels by ensuring rapid high affinity uptake of serotonin from plasma to platelets"]; [PMID:17506858 "SERT is a major mechanism that regulates plasma 5HT levels to prevent vasoconstriction and thereby secure a stable blood flow"]. Expressed in platelets at protein level. Enterocyte/gut mucosal 5-HT clearance; SERT downregulated in cholera [PMID:17575980 "Five other transporters were downregulated; aquaporin 10, SLC6A4, TRPM6, SLC23A1 and SLC30A4"].
- **Developmental trophic roles** (via 5-HT tone): cortical/sensory-circuit organization
  and enteric neurogenesis [file:human/SLC6A4/SLC6A4-uniprot.txt "Required for enteric neurogenesis and gastrointestinal reflexes"]. These are real but non-core (SERT sets 5-HT levels; it does not execute neurogenesis/morphogenesis steps).
- Pharmacology: target of SSRIs, tricyclics, cocaine and amphetamines [file:human/SLC6A4/SLC6A4-uniprot.txt "This protein is the target of psychomotor stimulants such as amphetamines or cocaine"]. 5-HTTLPR promoter polymorphism linked to depression/anxiety susceptibility.

## Secondary / non-core activities and locations

- Uncoupled serotonin-gated cation channel conductance [file:human/SLC6A4/SLC6A4-uniprot.txt "displays serotonin-induced channel-like conductance for monovalent cations, mainly Na(+) ions. The channel activity is uncoupled from the transport cycle and may contribute to the membrane resting potential or excitability"] → supports GO:0005261 cation channel activity (KEEP_AS_NON_CORE) and GO:0051899 membrane depolarization (KEEP_AS_NON_CORE).
- K+ counter-transport underlies GO:0015297 antiporter activity IDA (KEEP_AS_NON_CORE): the
  K+ antiport limb is part of the symport cycle, not a separate dedicated antiporter function.
- Na+ binding (Na1/Na2 sites) and serotonin binding are mechanistic sub-features of the
  symporter (GO:0031402, GO:0051378 → KEEP_AS_NON_CORE).
- Location: core at **plasma membrane** (ACCEPT) of presynaptic terminals / serotonergic
  synapses / neuron projections; intracellular pools in endosome membrane / endomembrane
  system / Golgi reflect biosynthesis, trafficking and SCAMP2-dependent recycling
  [PMID:16870614 "endogenous SERT co-localizes with SCAMP2 in discrete structures also containing the lipid raft marker flotillin-1 and the SNARE protein syntaxin 1A"] → membrane raft (KEEP_AS_NON_CORE). Postsynaptic membrane IEA is an over-propagation (SERT is presynaptic).

## Protein interactions (meaningful; bare GO:0005515 rows removed per policy)

- SCAMP2 (O15127) — retains SERT intracellularly [PMID:16870614]; UniProt SUBUNIT direct interaction.
- ITGAV:ITGB3 integrin (P05106 = ITGB3) — regulates SERT trafficking/activity and platelet
  aggregation [PMID:18317590 "integrin alphaIIbbeta3 interacts directly with the C terminus of SERT"]. Supports specific GO:0005178 integrin binding (KEEP_AS_NON_CORE).
- NOS1/nNOS — reduces surface SERT [UniProt SUBUNIT] → GO:0050998 NOS binding (KEEP_AS_NON_CORE).
- PICK1 (Q9NRD5) [PMID:11343649], TGFB1I1/Hic-5 (O43294) [PMID:12177201, PMID:16803896],
  alpha-synuclein/SNCA (P37840) [PMID:16882008], STX1A, filamentous actin — all trafficking/
  regulatory partners. The bare GO:0005515 "protein binding" rows citing these are REMOVE
  (uninformative) per the protein-binding policy; the informative facets are kept via the
  specific binding terms above.
- Homo-oligomerization [file:human/SLC6A4/SLC6A4-uniprot.txt "Monomer or homooligomer"] → GO:0042802 identical protein binding (KEEP_AS_NON_CORE).
- Retracted interactions (VIM, RAB4) explicitly flagged CAUTION in UniProt — not used.

## Systematic handling of downstream behavioral / drug-response / physiological IEA set

Participation test (CLAUDE.md): SERT *performs* 5-HT reuptake. For organismal behaviors,
development, and "response to X" processes it only sets serotonergic tone; another entity
executes the process. Necessity ≠ participation. Therefore:
- **MARK_AS_OVER_ANNOTATED** (SERT does not execute; pleiotropic/indirect, mostly Ensembl IEA
  from rat P31652 / mouse Q60857): response to hypoxia, serotonin receptor signaling pathway,
  response to nutrient, memory, circadian rhythm, locomotory behavior, male mating behavior,
  conditioned place preference, behavioral response to cocaine, response to xenobiotic
  stimulus, response to toxic substance (IDA; SERT is a regulated target in cholera),
  response to estradiol, cellular response to retinoic acid, response to oxidopamine,
  vasoconstriction, positive regulation of gene expression, negative regulation of
  dopaminergic synaptic transmission, negative regulation of cerebellar granule cell
  precursor proliferation, negative regulation of neuron differentiation, positive
  regulation of cell cycle, negative regulation of organ growth, regulation of thalamus size
  (IMP from 5-HTTLPR–thalamic-volume association [PMID:18378990], not a molecular function).
- **KEEP_AS_NON_CORE** (genuine, directly supported but non-core role of the reuptake
  activity): positive regulation of serotonin secretion (fills releasable platelet/enterocyte
  stores), platelet aggregation [PMID:18317590 "we have established a role for constitutive SERT expression in efficient ADP- and thrombin-triggered platelet aggregation"], enteric
  nervous system development, brain morphogenesis, cellular response to cGMP (SERT
  activity/trafficking is cGMP/PKG-regulated [file:human/SLC6A4/SLC6A4-uniprot.txt "Phosphorylation at Thr-276 increases 5-HT uptake and is required for cGMP-mediated SERT regulation"]), membrane depolarization.

## IBA / paralog propagation notes

- Serotonin-specific node PTN002481010 (serotonin symporter, serotonin binding, serotonin
  uptake, synapse, neuron projection): correct clade; P31645 appears in its own WITH/FROM =
  experimental grounding on the target, not circular. ACCEPT/KEEP as appropriate.
- Broad SLC6 node PTN000177662 (plasma membrane, sodium ion transmembrane transport): fine.
- **GO:0006865 amino acid transport IBA (node PTN000907004)** → MARK_AS_OVER_ANNOTATED: this
  node spans the amino-acid-transporting SLC6 members (B0AT/glycine/proline/GABA branches);
  SERT's monoamine clade (SERT/DAT/NET) transports serotonin, not amino acids. Over-broad
  substrate propagation to the wrong clade. Recorded as a propagation_review.

## Actions applied to transporter MF granularity

- GO:0008504 (monoamine transmembrane transporter) IS an is_a ancestor of the accepted
  GO:0005335 (QuickGO-verified), so its rows are TOO_GENERAL, harmonized with the NET
  (SLC6A2) and DAT (SLC6A3) treatment. GO:0005326 (neurotransmitter transmembrane
  transporter) is NOT an is_a ancestor (parallel branch), so TOO_GENERAL cannot apply and
  those rows are ACCEPT as a true, broader classification.
- GO:0016020 membrane → MODIFY → GO:0005886 plasma membrane.
- GO:0012505 endomembrane system → MODIFY → GO:0010008 endosome membrane (the specific
  intracellular location the gene carries, supported by SCAMP2/recycling-endosome data).
- GO:0006836 neurotransmitter transport → TOO_GENERAL (entailed by the accepted GO:0098810
  neurotransmitter reuptake / GO:0051610 serotonin uptake rows the gene carries).

No proposed_new_terms (core term exists). No source_defects found (retracted papers already
flagged by UniProt CAUTION; not annotated in GOA).
