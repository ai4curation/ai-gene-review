# neur (Neuralized, P29503) — curation notes

Drosophila melanogaster, FBgn0002932, CG11988. 754 aa (isoform 1). Domains: two NHR
(neuralized homology repeat) domains (NHR1 ~106-260, NHR2 ~368-523), C-terminal RING
(C3HC4) zinc finger (701-742). PANTHER PTHR12429 (NEURALIZED), subfamily PTHR12429:SF6
(PROTEIN NEURALIZED).

## Role in Notch signalling: ligand E3 ubiquitin ligase (signal-sending cell)

- RING-type E3 ligase: [PMID:11740940 "In this report, we present genetic and biochemical
  evidence that Neur is a RING-type, E3 ubiquitin ligase."]; [PMID:11696324 "its RING finger
  domain acts as an E3 ubiquitin ligase"].
- Substrate Delta; promotes its endocytosis/degradation: [PMID:11740940 "Collectively, our
  data indicate that Neur is a ubiquitin ligase that positively regulates the N pathway by
  promoting the endocytosis and degradation of Dl."]
- Also Serrate: [PMID:16093323 "Neuralized physically associates with Serrate and stimulates
  its endocytosis and signaling activity."]
- Redundancy with Mib1: [PMID:16093323 "Simultaneous absence of neuralized and mib1 completely
  abolishes Notch signaling in both aforementioned contexts"]; Neur and Mib1 are
  structurally unrelated with similar activities but distinct developmental domains
  [PMID:15760269 "D-mib and Neur are two structurally distinct proteins that have similar
  molecular activities but distinct developmental functions in Drosophila."]
- Docking: NHR1 binds Dl [PMID:17065551 "the NHR1 domain of Neuralized is both necessary and
  sufficient to bind Delta"]; the Dl ICD NXXN motif mediates binding and endocytosis
  [PMID:19580805 "Neur-dependent endocytosis of Dl requires the integrity of its NXXN motif"].
- Distinct docking/lysine preferences from Mib1; ubiquitylation of the Dl ICD correlates with
  signalling [PMID:22162135 "The two enzymes use distinct docking sites and displayed
  different acceptor lysine preferences on the Dl ICD."]; product is multi/poly-ubiquitylated
  [PMID:22162135 "these E3 ligases catalyze preferentially the multi- or polyubiquitylation of Dl"].
- Ubiquitylation-independent Dl activation by Neur in some lateral inhibition contexts
  [PMID:28960177 "Neur ... was shown to be able to activate Dl in an ubi-independent manner."]
- Membrane targeting via phosphoinositide-binding motif, required downstream of
  ubiquitination for Dl endocytosis [PMID:18061562].

## Regulation

- Bearded-family proteins (Brd, Tom, E(spl)-C BFMs, Ocho etc.) bind Neur via NXXN motifs and
  compete with Dl, inhibiting Neur in non-SOP cells [PMID:16459303; PMID:19580805].
- Asymmetric segregation to pIIb [PMID:12852858].

## Other substrates / roles
- Stardust isoforms (NBM-containing) -> Crumbs endocytosis [PMID:28400441].
- Long-term memory in MB alpha/beta neurons [PMID:18794519] (mechanism undefined).

## Pathway-variant relevant biology
- Neur is restricted largely to neural precursors (SOPs) and a few other contexts;
  Mib1 is the broadly-used ligand E3. Two structurally unrelated ligand E3s is a conserved
  metazoan feature (vertebrates have NEURL1/1B and MIB1/2). Neur-specific
  antagonism by Bearded-family proteins is an insect/crustacean feature [PMID:19580805
  "conserved between insects and crustaceans"].

## Annotation decisions
- REMOVE: GO:0005634 nucleus (IEA from UniProt ECO:0000305 location, contradicted by
  membrane localization data); GO:0005515 protein binding (x10 IPI, Bearded-family binding;
  uninformative).
- Developmental processes kept as non-core.

## Deep research
- `just deep-research-falcon DROME neur --fallback perplexity-lite` launched; see status in
  review references (file present only if it completed).
