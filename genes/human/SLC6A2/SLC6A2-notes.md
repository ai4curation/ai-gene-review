# SLC6A2 (NET) curation notes

UniProt: P23975 (SC6A2_HUMAN). HGNC:11048. 617 aa. Gene synonyms NAT1, NET1, SLC5A5 (sic, listed NET1).
Family: sodium:neurotransmitter symporter (SNF) / SLC6 / NSS, TC 2.A.22, SLC6A2 subfamily.
PANTHER: PTHR11616 (SODIUM/CHLORIDE DEPENDENT TRANSPORTER), subfamily PTHR11616:SF320 (SODIUM-DEPENDENT NORADRENALINE TRANSPORTER).

## Core biology (verified)

NET is a plasma-membrane, Na+- and Cl--dependent (secondary-active) symporter that performs
presynaptic reuptake of norepinephrine (noradrenaline) at noradrenergic synapses, terminating
and recycling the signal. It also transports dopamine with comparable-to-higher affinity.

- Na+/Cl- dependence and NE transport: [PMID:2008212 "Expression of the cDNA clone in transfected HeLa cells indicates that noradrenaline transport activity is sodium-dependent and sensitive to selective noradrenaline transport inhibitors"]. Presynaptic reuptake framing: [PMID:2008212 "At most synapses, chemical signalling is terminated by a rapid reaccumulation of neurotransmitter into presynaptic terminals"].
- Na+ and Cl- both required; single Na+ for NE (vs >1 Na+ for DAT): [PMID:8125921 "All three transporters require external Na+ and Cl-. The Na+ concentration dependence suggests that a single Na+ ion is involved in transport catalyzed by norepinephrine and serotonin transporters while more than one Na+ ion participate in transport mediated by the dopamine transporter"].
- NET transports both NE and DA; lower KM (higher apparent affinity) for DA than NE: [PMID:8125921 "LLC-NET and LLC-DAT cells transported both NE and DA and both cell types exhibited a lower KM for DA transport than for NE transport"]. KM values (UniProt BIOPHYSICOCHEMICAL PROPERTIES): noradrenaline 0.29-2.12 uM; dopamine 0.24-0.52 uM.
- Cl-/Na+-dependence domain mapping using hDAT/hNET chimeras: [PMID:11093780] (IDA for DA:Na symport by hNET).
- UniProt CC FUNCTION: "Mediates sodium- and chloride-dependent transport of norepinephrine ... Is responsible for norepinephrine re-uptake and clearance from the synaptic cleft ... Can also mediate sodium- and chloride-dependent transport of dopamine".
- UniProt CATALYTIC ACTIVITY (Rhea RHEA:70923): (R)-noradrenaline(out) + chloride(out) + Na(+)(out) = (R)-noradrenaline(in) + chloride(in) + Na(+)(in); ChEBI (R)-noradrenaline = CHEBI:72587, Na+ = CHEBI:29101, chloride = CHEBI:17996. Dopamine reaction RHEA:70919/70931, dopamine = CHEBI:59905.
- Cryo-EM structures (2024): [PMID:39048818 "Molecular basis of human noradrenaline transporter reuptake and inhibition"] and [PMID:38750358 "Dimerization and antidepressant recognition at noradrenaline transporter"]. UniProt SUBUNIT: "Monomer (PubMed:39048818). Can form homodimers in the cell membrane; homodimerization is mostly mediated by cholesterol and lipids" — so NET is NOT an obligate heteromer; no SLC3 heavy chain. Do not model an in_complex heavy-chain row.
- 12 TM helices (UniProt FT TRANSMEM 1-12), N-glycosylated (Asn184/192/198), palmitoylated (Cys44; [PMID:39395208]).

NET's physiological role is NE reuptake; it does not itself execute downstream behavioural/
cardiovascular/cognitive processes. Na+ and Cl- are the driving co-substrates of the amine
symport, not independent transport functions.

## Disease / pharmacology
- Orthostatic intolerance (ORSTI, MIM 604715): Ala457Pro loss-of-function variant: [PMID:10684912], characterized in [PMID:11875370 "the maximum rate (V(max)) of norepinephrine uptake by the Ala(457)Pro variant was slightly reduced"]. NET deficiency -> POTS.
- NET is the target of psychomotor stimulants (cocaine, amphetamines) and NRI antidepressants (reboxetine, atomoxetine, desipramine); UniProt MISCELLANEOUS "target of psychomotor stimulants such as amphetamines or cocaine". Inhibited by mazindol, desipramine, nomifensine, nortriptyline [PMID:2008212].

## Interactors (functionally meaningful; recorded instead of bare protein-binding rows)
- PICK1 / PRKCABP (Q9NRD5): PDZ-domain protein, regulates surface localization of monoamine transporters [PMID:11343649 "an interaction between the PDZ domain-containing protein PICK1 and monoamine neurotransmitter transporters in vitro and in vivo"]. UniProt SUBUNIT "Interacts with PRKCABP".
- alpha-synuclein / SNCA (P37840): modulates NET trafficking/activity; attenuates NET activity [PMID:17156375], and cytoskeleton-regulated interactions [PMID:18331289 "the first direct demonstration of NET activity being regulated via actin and modulated by interactions with alpha-Syn"].
- beta-actin (ACTB, P60709) and microtubule (alpha/beta tubulin) cytoskeleton regulate NET surface expression/activity [PMID:18331289 "Protein interactions between NET, beta-actin, and alpha-Syn were modified, along with levels of surface transporters"].
- IRIP (ischemia/reperfusion-inducible protein): inhibits NET (and other monoamine transporter) activity [PMID:16024787 "the activities of exogenous organic cation transporters (OCT2 and OCT3), organic anion transporter (OAT1), and monoamine transporters were also inhibited by IRIP"].

## Ontology notes (checked via QuickGO is_a, 2026-11)
- GO:0005334 norepinephrine:sodium symporter activity is_a GO:0008504 monoamine transmembrane transporter activity AND is_a GO:0015378 sodium:chloride symporter activity (co-transports Na+ + Cl-). It is NOT currently an is_a descendant of GO:0005328 neurotransmitter:sodium symporter activity or GO:0005326 neurotransmitter transmembrane transporter activity. Same for GO:0005330 dopamine:sodium symporter activity.
  -> GO:0008504 and GO:0015378 are correct is_a ancestors of the core MF => TOO_GENERAL.
  -> GO:0005328 / GO:0005326 are true of NET but are NOT formal ancestors of GO:0005334, so they cannot be marked TOO_GENERAL (no is_a descendant accepted); kept as ACCEPT (correct, coarser MF statements). The apparent gap (NE:Na symporter not classified under neurotransmitter:sodium symporter despite NE being a neurotransmitter) is noted as a suggested_question.
- BP: GO:0098810 neurotransmitter reuptake is_a GO:0006836 neurotransmitter transport (=> GO:0006836 TOO_GENERAL). GO:0051620 norepinephrine uptake is_a GO:0090493 catecholamine uptake (=> GO:0090493 TOO_GENERAL). GO:0090494 dopamine uptake and GO:0051583 are_a GO:0090493. Note GO:0051620 NE uptake is NOT under GO:0006836 neurotransmitter transport in current GO.
- PANTHER family PTHR11616: PAINT data present, no FamilyReview. `just paint-losses human SLC6A2`: no IRD/IKR on this lineage.

## Action rationale highlights
- GO:0006865 amino acid transport (IBA, node PTN000907004): REMOVE. NET is a monoamine (NE/DA) transporter; it does not transport amino acids. The IBD node spans amino-acid-transporting SLC6 paralogs (B0AT/GAT/glycine-proline subfamilies); the term over-propagates onto the monoamine subfamily. No experimental amino-acid transport for NET.
- GO:0030672 synaptic vesicle membrane (IEA, rat ortholog): MARK_AS_OVER_ANNOTATED. NET is a plasma-membrane reuptake transporter; vesicular monoamine loading is VMAT1/2. Likely reflects recycling vesicle/endosome trafficking pools, not a functional vesicular localization.
- bare GO:0005515 protein binding (PICK1, SNCA x2): REMOVE per protein-binding policy; meaningful interactions recorded above and in reasons.

## Paralog propagation (NET/DAT/SERT)
Close paralogs: SLC6A2/NET (NE), SLC6A3/DAT (DA), SLC6A4/SERT (5-HT). All Na+/Cl--dependent SNF transporters.
Substrate specificity differs but overlaps: NET transports both NE and DA (DA with comparable/higher affinity, lower KM: PMID:8125921); DAT does not efficiently transport NE in most contexts; SERT is 5-HT selective. NE:Na IBA node PTN000178374 is NE-transporter-specific and self-grounded on P23975. DA:Na IBA node PTN000746001 is a monoamine-transporter clade node shared with invertebrate DAT-like transporters; NET's DA transport is experimentally grounded (P23975 appears in its own WITH/FROM = grounding, not circular).
