# cat-1 (Q9GNP0) — vesicular monoamine transporter — curation notes

## Identity

- UniProt Q9GNP0 (Q9GNP0_CAEEL, TrEMBL/unreviewed), WormBase W01C8.6, 553 aa, MFS profile
  domain (IPR011701, IPR020846). This is the correct accession for the WormBase gene cat-1
  (vesicular monoamine transporter), as listed in
  modules/synaptic_vesicle_neurotransmitter_loading.yaml — not the catalase ctl-2/Q27487.
  The UniProt record itself carries no functional description (SubName only), so the GOA
  rows and the primary literature carry the evidence.
- Orthologue of mammalian VMAT1/VMAT2 (SLC18A1/2) and paralogue of the vesicular
  acetylcholine transporter UNC-17 within the SLC18 family.

## Literature

### Duerr et al. 1999 (PMID:9870940, abstract only)

- "We have identified the Caenorhabditis elegans homolog of the mammalian vesicular
  monoamine transporters (VMATs); it is 47% identical to human VMAT1 and 49% identical to
  human VMAT2" [PMID:9870940]. "The C. elegans VMAT gene is cat-1" [PMID:9870940].
- Localization: "C. elegans VMAT is associated with synaptic vesicles in approximately 25
  neurons, including all of the cells reported to contain dopamine and serotonin, plus a few
  others" [PMID:9870940].
- Substrates (heterologous expression): "When C. elegans VMAT is expressed in mammalian
  cells, it has serotonin and dopamine transport activity; norepinephrine, tyramine,
  octopamine, and histamine also have high affinity for the transporter" [PMID:9870940].
  "The pharmacological profile of C. elegans VMAT is closer to mammalian VMAT2 than VMAT1"
  [PMID:9870940].
- Phenotype and rescue: "cat-1 knock-outs are totally deficient for VMAT immunostaining and
  for dopamine-mediated sensory behaviors, yet they are viable and grow relatively well"
  [PMID:9870940]; "The cat-1 mutant phenotypes can be rescued by C. elegans VMAT constructs
  and also (at least partially) by human VMAT1 or VMAT2 transgenes" [PMID:9870940].
- Interpretation: "It therefore appears that the function of amine neurotransmitters can be
  completely dependent on their loading into synaptic vesicles" [PMID:9870940].

### Sanyal et al. 2004 (PMID:14739932, full text cached)

- "Mutant strains deficient for the vesicular monoamine transporter ( cat-1 ), TH ( cat-2 )
  and GTP-cyclohydroxylase ( cat-4 ) have reduced levels of dopamine" [PMID:14739932] (HPLC
  measurement). The reduced dopamine content of cat-1 mutants reflects loss of vesicular
  sequestration (unstored cytosolic amine is degraded), not a role of CAT-1 in dopamine
  synthesis or catabolism.

## Assessment

- Core: monoamine:proton antiport across the synaptic vesicle membrane (GO:0015311), loading
  dopamine, serotonin, tyramine and octopamine into synaptic vesicles (GO:0015842,
  GO:0160311, GO:0160312) in aminergic neurons.
- Mechanism errors in the GOA set: GO:0005330 dopamine:sodium symporter activity and
  GO:0005335 serotonin:sodium:chloride symporter activity describe the plasma-membrane
  SLC6 reuptake transporters (DAT, SERT). VMAT-family transporters exchange two luminal
  protons for one cytosolic amine; PMID:9349821 explicitly contrasts VGAT with "a vesicular
  transporter for monoamines" on bioenergetic grounds. The IDA experiments in PMID:9870940
  measured amine transport in mammalian cells, not sodium coupling, so the essence (dopamine
  and serotonin transport) is right but the terms are not.
- Consequential errors: GO:0090494 dopamine uptake and GO:0051610 serotonin uptake are
  inferred automatically (GO_REF:0000108) from those symporter terms, and denote movement
  into a cell, which is the plasma-membrane reuptake step; for a vesicular transporter the
  correct process is loading into the synaptic vesicle.
