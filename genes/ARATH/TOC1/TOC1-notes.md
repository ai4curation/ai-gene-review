# TOC1 (APRR1 / PRR1) — research notes

Gene: TOC1 / APRR1 / PRR1 (At5g61380), UniProt Q9LKL2, *Arabidopsis thaliana* (NCBITaxon:3702).
Reviewer journal for the GO annotation review.

## Summary of biology

TOC1 (TIMING OF CAB EXPRESSION 1; also APRR1 / PRR1) is the founding member of the
Arabidopsis pseudo-response regulator (PRR) family and a core **evening-phased**
component of the plant circadian clock. It is a nuclear, DNA-binding transcriptional
**repressor** that occupies the promoters of the morning genes CCA1 and LHY and
represses their expression, completing the central transcriptional feedback loop in
which morning-expressed CCA1/LHY in turn directly repress *TOC1* transcription.

Domain architecture: an N-terminal **pseudo-receiver (PR / psREC) domain** (~aa 20–138)
and a C-terminal **CCT domain** (CONSTANS, CO-like, TOC1; ~aa 533–575).

### Key point on "phosphorelay / two-component" terms

Although TOC1 has a receiver-domain-like fold, it is a *pseudo*-response regulator:
> UniProt CAUTION: "Lacks the phospho-accepting Asp (here Glu-71), present in the
> receiver domain, which is one of the conserved features of the two-component response
> regulators (ARRs) family." [Q9LKL2 UniProt]

> [PMID:18055606 "The pseudo receiver domain shows high similarity to receiver domains of
> two-component response regulators but lacks the key Asp residue that accepts a phosphoryl
> group to modulate the activity of the protein."]

GO:0000160 "phosphorelay signal transduction system" is defined as a His-kinase
autophosphorylation → Asp phosphotransfer → response regulator cascade (QuickGO API,
2026-06-14). GO:0009736 "cytokinin-activated signaling pathway" is the cytokinin
two-component cascade ending in transcription (QuickGO API). TOC1 lacks the catalytic
Asp and is not part of cytokinin signaling; both IEA annotations are over-propagations
from the receiver-domain InterPro/ARBA signatures and are biologically incorrect for
TOC1. There is no experimental evidence linking TOC1 to cytokinin signaling.

## Molecular function: DNA-binding transcriptional repressor

> [PMID:22315425 "Purified TOC1 binds directly to DNA through its CCT domain, which is
> similar to known DNA-binding domains."]

> [PMID:22315425 "we use the Gal4/UAS system in Arabidopsis to show that TOC1 acts as a
> general transcriptional repressor, and that repression activity is in the
> pseudoreceiver domain of the protein."]

> [PMID:22315425 "Chemical induction and transient overexpression of TOC1 in Arabidopsis
> seedlings cause repression of CCA1 / LHY expression ... mutation or deletion of the CCT
> domain prevents this repression showing that DNA-binding is necessary for TOC1 action."]

TOC1 binds the T1ME element (TGTG core), and also ME and HUD motifs.

> [PMID:22315425 "TOC1 can bind a site [T1ME (TGTG)] that is part of the CO response
> element [TGTG(N2-N3)ATG] ( 16 ) and also binds the ME ( 22 ) and HUD ( 23 ) motifs"]

### Apparent contradiction with the 2009 NOT annotation

The 2009 CHE paper (PMID:19286557) carries a NOT annotation for GO:0000976
"transcription cis-regulatory region binding" because at that time direct TOC1 DNA
binding could not be detected and TOC1 was thought to lack DNA-binding domains:

> [PMID:19286557 "the TOC1 protein has no DNA binding domains, which suggests that it
> cannot directly regulate CCA1."]

> [PMID:19286557 "A direct interaction of TOC1 with the CCA1 promoter was investigated by
> electrophoretic mobility shift assays and the yeast one-hybrid system, but no binding
> was detected using these approaches (data not shown), suggesting that TOC1 is unable to
> bind directly to the CCA1 promoter."]

The 2009 study used the CHE/TCP-binding region of the CCA1 promoter and concluded TOC1
is recruited to that specific promoter region via CHE (a TCP transcription factor),
rather than binding it directly. In 2012, Gendron et al. (PMID:22315425) showed with
purified protein that full-length TOC1 *does* bind DNA directly through its CCT domain,
and that DNA binding is necessary for repression. The 2012 finding refines, but does not
fully overturn, the 2009 result: TOC1 binds T1ME/G-box/ME-type elements directly, while
its association with the specific TCP-binding-site region of the CCA1 promoter may be
CHE-mediated. The negated GO:0000976 annotation is therefore retained (it reflects a
genuine published negative result about a specific promoter region), but the positive
DNA-binding and DNA-binding-TF activity annotations from 2012 are the well-supported
current view.

## Direct target genes / repressor of morning genes and PIF4/5

TOC1/PRRs also directly bind and repress *PIF4* and *PIF5* promoters to control
photoperiodic hypocotyl growth:

> [PMID:32165445 "PRRs directly bind the promoters of PHYTOCHROME-INTERACTING FACTOR4
> (PIF4) and PIF5 to repress their expression, hence PRRs act as transcriptional
> repressors of the positive growth regulators PIF4 and PIF5"]

> [PMID:32165445 "mutation or truncation of the TIMING OF CAB EXPRESSION1 (TOC1) DNA
> binding domain, without compromising its physical interaction with PIFs, still caused
> long hypocotyl growth under short days"]

The IDA GO:0003677 DNA-binding annotation to PMID:32165445 is supported by the EMSA
evidence (PRRs binding G-box cis-elements of CCA1/PIF4/PIF5 promoters).

## Circadian clock role

> [PMID:10926537 "The toc1 mutation causes shortened circadian rhythms in light-grown
> Arabidopsis plants ... TOC1 is itself circadianly regulated and participates in a
> feedback loop to control its own expression."]

> [PMID:11100772 "all these members of the APRR1/TOC1 family (APRR1, APRR3, APRR5, APRR7,
> and APRR9) are subjected to a circadian rhythm at the level of transcription ... the
> APRR-mRNAs started accumulating sequentially after dawn ... in the order of
> APRR9-->APRR7-->APRR5-->APRR3-->APRR1."]

> [PMID:23638299 "two morning-phased Myb-like transcription factors, CIRCADIAN CLOCK
> ASSOCIATED 1 (CCA1) and LATE ELONGATED HYPOCOTYL (LHY), repressing expression of an
> evening-phased pseudo-response regulator, TIMING OF CAB EXPRESSION 1 (TOC1 or PRR1),
> which in turn represses expression of CCA1 and LHY"]

PMID:23638299 (RVE8 paper, IMP for regulation of gene expression) shows TOC1 expression
itself is activated by RVE8 and that TOC1 represses morning genes; the loss-of-clock-
function genetic context supports TOC1's role in regulation of gene expression.

## Subcellular location: nucleus

> [PMID:18562312 "Each PRR protein examined is nuclear-localized and is differentially
> phosphorylated over the circadian cycle."]

UniProt: SUBCELLULAR LOCATION: Nucleus (PROSITE-ProRule CCT NLS + PubMed:18562312).
Multiple independent IDA/TAS/ISM nucleus annotations.

## Protein–protein interactions (GO:0005515 IPI, IntAct)

TOC1 interacts with many partners; these IntAct-derived "protein binding" annotations
are individually true but uninformative as molecular function:
- PIF/PIL bHLH factors (PIF1, PIL2, PIF3, PIF4, PIL5, PIL6) [UniProt SUBUNIT; PMID:11828029 IntAct partner Q8L5W8 = PIL1].
- ADO1/ZTL (ZEITLUPE) F-box photoreceptor — targets TOC1 for SCF(ZTL) degradation
  [PMID:14654842; PMID:17704763]; ADO2/LKP2 [PMID:15310821].
- PRR3/APRR3 — protects TOC1 from ZTL degradation in the vasculature [PMID:18055606].
- PRR5 — promotes TOC1 nuclear import, phosphorylation, subnuclear foci [PMID:20407420].
- TCP21/CHE — recruits TOC1 to the CCA1 promoter [PMID:19286557].
- Large-scale interactome / phytohormone network screens [PMID:21798944; PMID:28650476;
  PMID:32612234].

> [PMID:20407420 "both proteins interact in vitro and in vivo through their conserved
> N-termini. TOC1-PRR5 oligomerization enhances TOC1 nuclear accumulation"]

> [PMID:18055606 "PRR3 was able to bind to TOC1 in yeast and in plants and to perturb TOC1
> interaction with ZEITLUPE (ZTL), which targets TOC1 for proteasome-dependent
> degradation."]

## Post-translational regulation

> [PMID:18562312 "The more highly phosphorylated forms of PRR5 and TOC1 interact best with
> the F-box protein ZTL (ZEITLUPE), suggesting a mechanism to modulate their proteolysis."]

TOC1 is phosphorylated during the day and degraded by SCF(ZTL)/26S proteasome; PRR3 and
PRR5 modulate its stability and nuclear accumulation.

## Output: circumnutation (clock output, non-core)

> [PMID:15908440 "toc1 appears to shorten the period ... in circumnutation speed in LL,
> suggesting that a common circadian clock may control both circumnutation speed and other
> circadian outputs."]

This is a downstream circadian output phenotype of clock disruption, not a core TOC1
molecular function — best kept as non-core.

## Annotation decision rationale (high level)

- DNA-binding TF / transcriptional repression / nucleus / circadian rhythm: ACCEPT as
  core (well supported experimentally).
- regulation of (DNA-templated) transcription, negative regulation of gene expression:
  ACCEPT/ keep (consistent with repressor activity).
- protein binding (GO:0005515): KEEP_AS_NON_CORE — true interactions but uninformative MF;
  do not endorse as core.
- phosphorelay signal transduction (GO:0000160) and cytokinin-activated signaling
  (GO:0009736), both IEA from receiver-domain signatures: REMOVE — TOC1 lacks the
  phospho-accepting Asp and has no role in cytokinin signaling.
- circumnutation (GO:0010031): KEEP_AS_NON_CORE (clock output phenotype).
- negated GO:0000976: retain negation (UNDECIDED/ACCEPT of negation as published).
