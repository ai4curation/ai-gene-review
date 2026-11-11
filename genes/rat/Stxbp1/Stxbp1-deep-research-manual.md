# Stxbp1 (Munc18-1, nSec1, rbSec1, p67) - manual literature synthesis (rat, P61765)

No deep-research API was available for this review. This synthesis was written by the
reviewer from the cached publications in `publications/`, the UniProt record
(`Stxbp1-uniprot.txt`) and PubMed/PMC look-ups. Each statement carries inline provenance.

## Identity and family

- Rat Stxbp1 (UniProtKB P61765, RGD:3785, GeneID 25558), 594 aa, two splice isoforms
  (Munc18-1a, Munc18-1b). "Belongs to the STXBP/unc-18/SEC1 family" [UniProt CC SIMILARITY].
- Neuron- and neuroendocrine-enriched: "Brain and spinal cord. Highly enriched in axons."
  [UniProt CC TISSUE SPECIFICITY].
- Soluble protein that is cytosolic and recruited to membranes: "Membrane; Peripheral membrane
  protein." [UniProt CC SUBCELLULAR LOCATION]. Plasma-membrane recruitment depends on syntaxin-1:
  [PMID:12093152 "revealed syntaxin 1-dependent localization of Munc-18a in the plasma membrane"].

## Binding partners and binding modes

- Closed syntaxin-1 (binary complex, mode 1): crystal structure of the rat nSec1-syntaxin 1a
  complex [PMID:10746715 "Syntaxin 1a and neuronal Sec1 (nSec1) form an evolutionarily conserved
  heterodimer that is essential for vesicle trafficking and membrane fusion"]. Binds both
  syntaxin 1A and 1B [PMID:12093152 "Munc-18a significantly binds both isoforms of syntaxin 1
  (syntaxins 1A and 1B)"].
- Syntaxin-1 N-peptide (modes 2/3) [PMID:18337752 "the N-peptide of syntaxin 1a serves as a
  second binding site in the Munc18a/syntaxin 1a complex"]; crystal structure of Munc18-1 with
  the N-peptide [PMID:21193638].
- Assembled SNARE complexes [PMID:17301226 "We now show that Munc18-1 also binds tightly to
  assembled SNARE complexes containing syntaxin-1"]; and membrane-anchored syntaxin-1/SNAP-25
  heterodimers [PMID:18201107]. Munc18-1 and complexin-1 bind simultaneously to SNARE complexes
  [PMID:19255244].
- VAMP2 via helix 12 of domain 3a, the basis of its template activity [PMID:24532794 "A single
  point mutation (L348R) within helix 12 selectively abolishes VAMP2 binding and the stimulatory
  function of Munc18-1 in membrane fusion"].
- Other partners (peripheral to the core function): Mint1/Mint2 (APBA1/2)
  [PMID:9395480 "Mint proteins are part of a multimeric complex containing Munc18-1 and syntaxin"];
  Cdk5 and cytoskeletal proteins [PMID:12963086]; phospholipase D, which Munc18-1 inhibits
  [PMID:14744865 "PLD activity was potently inhibited by Munc-18-1 in vitro (IC50 = 2-5 nm)"];
  Rab3A, which Munc18-1 helps dissociate from vesicles [PMID:21689256]; Cab45b
  [PMID:17442889]. Syntaxin 11 in mast cells [PMID:23487749].

## Mechanism: dual inhibitory and stimulatory roles in SNARE assembly

- Inhibitory: when bound to closed syntaxin-1 (and its N-peptide), Munc18-1 blocks SNARE complex
  formation [PMID:18337752 "When the syntaxin 1a N-peptide is bound to Munc18a, SNARE complex
  formation is blocked"; PMID:12093152 three-hybrid inhibition of syntaxin-VAMP complexes;
  PMID:26030875 "Munc18-1 strongly inhibits SNARE complex formation, whereas addition of either
  MUN* or MUN933 equally facilitates SNARE complex assembly"]. Munc13-1 MUN domain opens syntaxin-1
  and drives the transition from the Munc18-1/closed syntaxin complex to the SNARE complex
  [PMID:26030875].
- Stimulatory/template: Munc18-1 domain 3a helix 12 templates VAMP2 and syntaxin, accelerating
  trans-SNARE (SNAREpin) assembly and liposome fusion [PMID:24532794 "the data suggest that helix 12
  provides a folding template for VAMP2, accelerating SNAREpin assembly and membrane fusion"]. In a
  GUV/SUV reconstitution, Syt1 docks vesicles first and Munc18-1 then accelerates SNAREpin assembly
  [PMID:22810233 "vesicle docking by synaptotagmin 1 is a prerequisite for Munc18-1 to accelerate
  trans-SNARE complex (SNAREpin) assembly and membrane fusion"]. Munc18-1 shifts syntaxin toward
  an open state when associated with SNAP25 [PMID:26876096 "a syntaxin/SNAP25:Munc18-1 complex is a
  likely starting point for SNARE assembly"].
- Chaperone of syntaxin-1: Munc18-1 stabilizes syntaxin-1 [PMID:15935055 "Munc18-1 directly
  promotes the stability of syntaxin 1, consistent with a chaperone function"] and supports its
  membrane delivery [PMID:17543282 "important role in stabilizing membrane delivery of Stx1A"];
  in its absence syntaxin-1 is retained in the ER [PMID:26359495].

## Physiological roles

- Synaptic vesicle priming and neurotransmitter release: lentiviral Munc18-1 rescues release in
  knockout neurons; point mutations that preserve closed-syntaxin binding but disrupt SNARE-complex
  binding "selectively impairs synaptic vesicle priming but not Ca(2+)-triggered fusion of primed
  vesicles" [PMID:19255244].
- Neuroendocrine dense-core vesicle exocytosis (PC12, chromaffin): in Munc18-silenced PC12 cells
  stimulated exocytosis is lost and wild-type Munc18 fully rescues it; the syntaxin N-peptide
  (mode 2/3) interaction raises the fusion probability of a post-docking vesicle pool ~5-fold
  [PMID:20801887 "We conclude that the presence of munc18 molecules, engaged in regulated mode 2/3
  interaction with syntaxin, exerts a strong positive effect on a specific postdocking pool of
  vesicles, increasing the probability of fusion by a factor of 5"]. Mutants modelled on
  invertebrate/yeast SM alleles alter chromaffin exocytosis kinetics [PMID:15563604].
- Non-neuronal regulated exocytosis (peripheral): mast-cell degranulation (with Munc18-2)
  [PMID:23487749]; human sperm acrosomal exocytosis [PMID:23091057 "this protein has an essential
  role in acrosomal exocytosis"]; platelets contain Munc18a but Munc18c dominates granule release
  [PMID:12773094 "suggest a dominant role for Munc18c in all three granule-release events"].
- Indirect/systemic: antisense knock-down in hypothalamus lowers glutamate release and delays
  puberty in female rats; hypothalamic expression rises with estrogen [PMID:16951547].
- Unusual localizations: nuclear/perinuclear Munc18-1 in PC12 and brain neurons
  [PMID:15869823]; association with cytoskeletal elements [PMID:12963086].

## Disease context

Human STXBP1 haploinsufficiency causes developmental and epileptic encephalopathy
(STXBP1 encephalopathy); not reviewed here in detail since this is the rat entry.
