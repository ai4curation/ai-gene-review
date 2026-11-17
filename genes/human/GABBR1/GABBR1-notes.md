# GABBR1 (Q9UBS5) review notes

## Deep research status (2026-11-17)

`just deep-research-falcon human GABBR1 --fallback perplexity-lite` was run twice and
failed both times. The first attempt failed because the sparse worktree lacked
`templates/` (`Template file not found: templates/gene_research_go_focused.md`); after
adding `templates/` to the sparse checkout the second attempt failed with
`Provider 'falcon' not available. Available: openscientist, claude_code` and the
perplexity-lite fallback with `Provider 'perplexity' not available`. No provider file
was written. The literature research below was done by hand from PubMed records cached
under `publications/`.

Literature search (PubMed E-utilities, 2026-11-17): queries "Vigot R[au] AND GABAB",
"globus pallidus AND GABA(B1) AND GABA(B2) AND immunogold", "Kaupmann K[au] AND 1998
AND heteromeric", "Biermann B[au] AND sushi", "Gassmann M[au] AND 2004 AND GABA(B1)",
"trafficking checkpoint GABA(B) heterodimerization", "Gassmann M[au] AND Bettler B[au]
AND Nat Rev Neurosci", plus the PMIDs cited in the GOA file and the UniProt record.
Newly cached: PMID:11498050, PMID:15174078, PMID:16701209, PMID:20107064, PMID:9872317,
PMID:9844003, PMID:9872315, PMID:10939334, PMID:22595784.

## GOA fetch note

`just fetch-gene human GABBR1` first produced an empty GOA file because the QuickGO
annotation search returned HTTP 500 whenever `includeFields=taxonName` was requested
("I/O error on GET request for .../proteins/api/taxonomy/id/9606/node: Connection
refused"). The GOA file was regenerated with the same `ai-gene-review fetch-gene` code
path, dropping only the `taxonName` include field and filling "Homo sapiens" for taxon
9606; all 79 annotations and every other column come from QuickGO unchanged.

## Identity and architecture

- GABA-B receptor subunit 1, class C GPCR, 961 aa (isoform 1a). Signal peptide 1-19,
  extracellular Venus-flytrap (VFT) ligand-binding domain, 7 TM helices (592-854),
  C-terminal coiled coil (869-925). Isoform 1a carries two N-terminal sushi domains
  (30-96, 98-159); isoform 1b lacks them. Isoform 1e (truncated) is the ectodomain only.
- Orthosteric GABA/baclofen site is in the GBR1 VFT [PMID:24305054 "The agonists and
  antagonists are anchored in the interdomain crevice of GBR1 by an overlapping set of
  residues"]; [PMID:22660477 "GBR1 is responsible for ligand-binding and GBR2 is
  responsible for G protein coupling"].

## Obligate heterodimer with GABBR2

- [PMID:9872316 "Upon expression with GABA(B)R2 in HEK293T cells, GABA(B)R1 is terminally
  glycosylated and expressed at the cell surface"; "Co-expression of the two receptors
  produces a fully functional GABA(B) receptor at the cell surface"].
- [PMID:9872317 "co-expression of these receptors yields a robust coupling to activation
  of Kir3 channels"; "GABA(B)R2 and GABA(B)R1a/b proteins immunoprecipitate and localize
  together at dendritic spines"].
- [PMID:9872315 "the combination of GABA(B)R1 and GABA(B)R2 confers robust stimulation of
  channel activity"].
- [PMID:10075644 "GABA mediated a functional response in cells coexpressing gb1a and gb2
  but not in cells expressing either receptor individually"].
- ER retention checkpoint: [PMID:10939334 "We found that expression of the GB1 subunit on
  the cell surface is prevented through a C-terminal retention motif RXR(R)"].
- [PMID:15617512 "while GBR1/GBR1 homodimers are retained in the endoplasmic reticulum and
  endoplasmic reticulum-Golgi intermediate compartment, both GBR2/GBR2 homodimers and
  GBR1/GBR2 heterodimers are present at the plasma membrane"].
- Full-length cryo-EM: [PMID:32555460 "its functional entity comprises an obligate
  heterodimer that is composed of the GB1 and GB2 subunits"].

## Effectors

- [PMID:9844003 "Presynaptic GABABRs inhibit neurotransmitter release by down-regulating
  high-voltage activated Ca2+ channels, whereas postsynaptic GABABRs decrease neuronal
  excitability by activating a prominent inwardly rectifying K+ (Kir) conductance that
  underlies the late inhibitory postsynaptic potentials"].
- Adenylyl cyclase: [PMID:9069281 "The cloned receptors negatively couple to adenylyl
  cyclase"].
- The channel effects are mediated by released G-beta-gamma (Reactome R-HSA-1013012,
  R-HSA-1013013, R-HSA-1013020); GABBR1 is not itself a channel or channel regulator.

## In vivo requirement (mouse)

- [PMID:11498050 "This demonstrates that GABA(B(1)) is an essential component of pre- and
  postsynaptic GABA(B) receptors"; null mice "exhibit spontaneous seizures, hyperalgesia,
  hyperlocomotor activity, and memory impairment"]. SynGO annotated mouse Gabbr1 from this
  paper (GPCR neurotransmitter receptor activity at GABAergic and Schaffer collateral-CA1
  synapses); human GABBR1 carries Ensembl projections of those rows, which are
  biologically sound.

## Isoforms 1a/1b, presynaptic targeting

- [PMID:16701209 "At hippocampal CA3-to-CA1 synapses, GABAB1a assembles heteroreceptors
  inhibiting glutamate release, while predominantly GABAB1b mediates postsynaptic
  inhibition"]; autoreceptors use either isoform [PMID:16701209 "suggesting that both
  GABAB1a and GABAB1b can efficiently participate in autoreceptor function"].
- Sushi domains are axonal targeting signals [PMID:20107064 "the sushi domains are axonal
  targeting signals that redirect GABA(B1a) protein from its default dendritic
  localization to axons"].
- Review: [PMID:22595784 "The principal subunits regulate the surface expression and the
  axonal versus dendritic distribution of these receptors"].
- Isoform 1e: secreted/membrane-associated ectodomain that binds GABBR2 but does not
  signal [PMID:10906333].

## Synaptic sublocalization (rat globus pallidus, PMID:15174078)

Abstract-only here; the SynGO audit (branch claude/syngo-fulltext-verdicts) read the full
text. Findings: GABA(B1) mostly intracellular in perikarya ("the majority of GABA(B1)
labeling was localized within the cytoplasm"); at symmetric GABAergic synapses labelling
"was found in the main body of both pre- and postsynaptic specializations"; at
asymmetric glutamatergic synapses labelling "was found at perisynaptic sites of both pre-
and postsynaptic specializations". The authors conclude "the existence of presynaptic
GABA(B) auto- and heteroreceptors and postsynaptic GABA(B) receptors". SynGO filed these
GABA(B1) observations on rat Gabrb1 (a GABA-A subunit) instead of Gabbr1.

Decision: no NEW annotation from this paper. Human GABBR1 already carries presynaptic
membrane (GO:0042734), presynapse (GO:0098793), postsynaptic membrane (GO:0045211),
GABA-ergic synapse (GO:0098982) and glutamatergic synapse (GO:0098978) rows, all accepted
here; PMID:15174078 is cited as additional support. A presynaptic active zone or
postsynaptic specialization term would be wrong for the glutamatergic synapses, where
labelling is perisynaptic, and is not added.

## Disease

- NEDLC (MIM:620502), autosomal dominant, de novo missense variants:
  [PMID:36103875 "GABA fails to efficiently activate the variant receptors"; "p.Glu368Asp
  is located near the orthosteric binding site and reduces GABA potency and efficacy at
  the receptor"].

## Reference defect

- ComplexPortal rows cite PMID:987231, a 1976 phenol-methylation chemistry paper (title
  "[Methylation of phenols using metal-salt catalysts (author's transl)]."). Same defect
  as recorded on GABBR2. PMID:9872316 is a plausible but unverified intended citation.
