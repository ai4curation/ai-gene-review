# MC4R (melanocortin 4 receptor) curation notes

Deep research: `MC4R-deep-research-falcon.md` (Falcon) completed and is consistent with this review;
this review was written from cached publications, UniProt P32245 and PubMed searches.

## Core biology

- Brain-expressed melanocortin receptor that raises cAMP on agonist stimulation
  [PMID:8392067 "this receptor is expressed primarily in the brain"].
- Mouse knockout: hyperphagic maturity-onset obesity
  [PMID:9019399 "Inactivation of this receptor by gene targeting results in mice that develop a maturity onset obesity syndrome associated with hyperphagia, hyperinsulinemia, and hyperglycemia."].
- Human loss-of-function variants: commonest monogenic obesity, codominant, severity tracks residual
  signalling [PMID:12646665 "The correlation between the signaling properties of these mutant receptors and energy intake emphasizes the key role of this receptor in the control of eating behavior in humans."].
- Gs coupling; cryo-EM of MC4R-Gs with setmelanotide
  [PMID:33858992 "we present the cryo-electron microscopy (cryo-EM) structure of the human MC4R-Gs signaling complex bound to the agonist setmelanotide"].
- Primary cilium localisation with ADCY3 is required for body-weight control
  [PMID:29311635 "We demonstrate that MC4R colocalizes with ADCY3 at the primary cilia of a subset of hypothalamic neurons"].
- AgRP antagonises melanocortin receptors to stimulate feeding
  [PMID:15927146 "AgRP is a neuropeptide that stimulates food intake through inhibition of central melanocortin receptors (MCRs)."].

## Curation approach

- Core MF: melanocyte-stimulating hormone receptor activity (GO:0004980); core BP: adenylate
  cyclase-activating GPCR signaling pathway (GO:0007189) and negative regulation of appetite
  (GO:0032099); CC: plasma membrane and non-motile cilium membrane.
- Generic terms (GPCR activity, GPCR signaling, membrane, feeding behavior) modified to the
  specific terms above.
- Protein-binding IPIs (MRAP, MRAP2, DNAJB2) removed as uninformative; POMC/ACTH binding modified
  to melanocortin receptor activity.
- ACTH (corticotropin receptor activity) and bone resorption kept as non-core.
