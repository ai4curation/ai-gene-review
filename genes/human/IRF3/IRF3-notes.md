# IRF3 (Interferon regulatory factor 3, Q14653) — curation notes

## Provenance note
`just deep-research human IRF3 --provider perplexity` failed (perplexity provider not
configured in this environment; only `falcon` and `openscientist` available). A
`falcon` run was attempted. These notes are compiled manually from the cached UniProt
record (`IRF3-uniprot.txt`) and cached publications under `publications/`, with inline
provenance. No `-deep-research-<provider>.md` file was fabricated.

## Summary of function
IRF3 is a constitutively expressed transcription factor of the interferon regulatory
factor (IRF) family and the master activator of the type I interferon (IFN-alpha/beta)
response to viral infection. It is the terminal, signal-integrating transcription factor
of the cytosolic nucleic-acid–sensing pathways (RIG-I/MDA5-MAVS for RNA; cGAS-STING for
DNA) and the TLR3/TLR4-TRIF pathway.

- Constitutively expressed, single-copy gene; ISRE-binding; activates ISG15 promoter
  [PMID:8524823 "The IRF-3 gene encodes a 50-kDa protein that binds specifically to the
  IFN-stimulated response element (ISRE)... Overexpression of IRF-3 stimulates expression
  of the IFN-stimulated gene 15 (ISG15) promoter, an ISRE-containing promoter."].
- In resting cells IRF3 is a cytoplasmic, autoinhibited monomer. Upon infection the
  adaptors MAVS/STING/TRIF are phosphorylated on a conserved pLxIS motif by TBK1/IKBKE,
  which recruits IRF3 to the adaptor, licensing IRF3 phosphorylation by TBK1
  [PMID:25636800 "Phosphorylated MAVS and STING then bind to a positively charged surface
  of interferon regulatory factor 3 (IRF3) and thereby recruit IRF3 for its
  phosphorylation and activation by TBK1. We further show that TRIF... activates IRF3
  through a similar phosphorylation-dependent mechanism."].
- The recruitment/activation mechanism is shared across STING, MAVS and TRIF via the
  pLxIS motif; the same motif drives IRF3 dimerization and CBP binding
  [PMID:27302953 "The adaptor proteins STING... MAVS... and TRIF... mediate the
  recruitment of IRF-3 through a conserved pLxIS motif... the pLxIS motif also mediates
  IRF-3 dimerization and activation."].
- Phospho-IRF3 dimerizes, translocates to the nucleus, binds ISRE/PRD elements and
  recruits CBP/p300 to form the DRAF1/enhanceosome complex driving IFN-beta and ISG
  transcription. Four IRF3 molecules bind the PRDIII-I element of the IFN-beta enhancer
  [PMID:17560375 "four IRF-3 molecules bind in tandem to, variably spaced, consensus and
  nonconsensus IRF sites on the composite element... all four IRF sites are required for
  gene activation in vivo."].
- Ser-386 pyrophosphorylation by UAP1 (following TBK1 phosphorylation) promotes robust
  type I IFN responses; Uap1-deficient mice are susceptible to lethal viral infection
  [PMID:36603579 "UDP-N-acetylglucosamine pyrophosphorylase 1 (UAP1)... catalyzing the
  pyrophosphorylation of interferon regulatory factor 3 (IRF3) at serine (Ser) 386 to
  promote robust type I interferon (IFN) responses."].

## Activation cascade / regulation
- Reviews frame IRF3 (with IRF7) as the major modulator of IFN gene expression, activated
  by TBK1/IKKε phosphorylation [PMID:16846591 "Two members of the interferon regulatory
  factor (IRF) family - IRF-3 and IRF-7 - are the major modulators of IFN gene
  expression. Activation of IRF-3 and IRF-7 by TBK1/IKKvarepsilon mediated
  phosphorylation promotes IFN gene expression"; PMID:16979567 "a family of transcription
  factors, interferon regulatory factors (IRFs), plays central roles" in type I IFN
  induction].
- Heavily regulated post-translationally: phosphorylation (TBK1/IKBKE at Ser-385/386/396),
  pyrophosphorylation (UAP1), ISGylation (HERC5, activating), ubiquitination (RBCK1,
  TRIM21, UBE3C — degradative), deubiquitination (USP5), acetylation (KAT8, inhibitory),
  deamidation (CTPS1, inhibitory), and caspase-3 cleavage (inactivating during apoptosis)
  [IRF3-uniprot.txt PTM section].

## Negative regulators acting on DNA-binding / coactivator recruitment
- LYAR binds phospho-IRF3 and impedes its DNA-binding capacity, suppressing IFN-beta/ISG
  transcription [PMID:31413131 "LYAR interacts with phosphorylated IFN regulatory factor 3
  (IRF3) to impede the DNA binding capacity of IRF3, thereby suppressing the transcription
  of IFN-β and downstream IFN-stimulated genes (ISGs)."].
- ILRUN/C6orf106 interacts with IRF3 and blocks its recruitment to type I IFN promoters
  and reduces nuclear p300/CBP [PMID:29802199 "C6orf106 interacts with IRF3 and inhibits
  IRF3 recruitment to type I IFN promoter sequences while also reducing the nuclear levels
  of the coactivator proteins p300 and CREB-binding protein (CBP)."].

## Apoptosis (secondary, non-transcriptional role)
- On mitochondria IRF3 can act in a transcription-independent apoptotic pathway: recruited
  by TOMM70:HSP90AA1 and forming a TOMM70:HSP90AA1:IRF3:BAX complex to induce apoptosis
  [IRF3-uniprot.txt FUNCTION: "is recruited by TOMM70:HSP90AA1 to mitochondrion and forms
  an apoptosis complex TOMM70:HSP90AA1:IRF3:BAX inducing apoptosis (PubMed:25609812)"].
- The active form of IRF-3 induces cell death in macrophages [PMID:16846591 "the active
  form of IRF-3 led to induction of cell death"].
- PBLD study links IRF3 to virus-triggered mitochondrial apoptosis (K313/315-dependent,
  separable from transcriptional S385/386 function) [PMID:39362857 "PBLD mediates
  virus-triggered mitochondrial apoptosis through its dependence on IRF3 (K313/315)...
  facilitated virus-induced apoptosis by recruiting the Puma protein to the mitochondria
  via IRF3."].
- Caspase-3 cleaves IRF3 (with cGAS, MAVS) to limit cytokine overproduction; this is
  regulation OF IRF3, i.e. IRF3 as substrate, not IRF3 executing apoptosis
  [PMID:30878284 "activated caspase-3 cleaved cGAS, MAVS, and IRF3 to prevent cytokine
  overproduction."].

## Disease
- Autosomal dominant/recessive functional IRF3 deficiency causes herpes simplex
  encephalitis (IIAE7, MIM:616532); the p.R285Q (GLN-285) variant is characterized
  [IRF3-uniprot.txt DISEASE + PubMed:26216125, PubMed:40973797]. Rare IRF3 variants are
  also associated with life-threatening COVID-19 [PubMed:32972995].

## Molecular architecture (for MF review)
- N-terminal DNA-binding domain (residues ~1-113), an IRF tryptophan pentad-repeat that
  recognizes the GAAA-containing ISRE/IRF consensus (5'-AANNGAAA-3' half-sites)
  [IRF3-uniprot.txt DNA_BIND 5..111].
- C-terminal IRF-association domain (IAD) / regulatory domain (~175-427) mediating
  autoinhibition, phospho-triggered dimerization and CBP/p300 binding
  [IRF3-uniprot.txt; PMID:27302953].
- Original report noted IRF3 lacks an intrinsic Gal4-fusion transactivation domain, i.e.
  it activates transcription through coactivator (CBP/p300) recruitment rather than an
  autonomous AD [PMID:8524823 "Expression of IRF-3 as a Gal4 fusion protein does not
  activate expression of a... reporter gene... indicating that this protein does not
  contain the transcription transactivation domain."]. Functionally it nonetheless acts
  as a sequence-specific DNA-binding transcriptional activator of ISRE-containing genes.

## Curation reasoning notes
- Core MF: sequence-specific dsDNA binding at RNA Pol II cis-regulatory (ISRE) regions +
  DNA-binding transcription activator activity (Pol II specific). Phospho-induced
  homodimerization is a genuine, structurally documented MF.
- Core BP: positive regulation of type I IFN production (and IFN-alpha/beta specifically),
  antiviral innate immune response, cytosolic PRR signaling (RIG-I/MAVS, cGAS/STING),
  TRIF-dependent TLR signaling.
- Core CC: nucleus (active site of transcription), cytoplasm/cytosol (resting, activation).
- `GO:0005515 protein binding`: uninformative; per CLAUDE.md/skill policy, REMOVE the bare
  generic ones (removal does not deny the interaction). Where a paper supports a specific
  informative MF (e.g. CBP binding → not a distinct MF term needed here; homodimerization
  is already captured by GO:0042803), handle via the specific term rather than inventing one.
- `GO:0000122 negative regulation of transcription by RNA pol II` (IEA from GO:0001227
  repressor mapping): IRF3 is fundamentally an activator; the repressor mapping is a
  weakly supported ortholog/Ensembl inference. Mark down.
- Apoptosis process terms: real but secondary/non-core (KEEP_AS_NON_CORE).
- IBA annotations (DNA-binding TF activity, Pol II cis-reg binding, nucleus, immune system
  process, regulation of transcription by Pol II) sit at the right level for the IRF family
  and include Q14653 in their own WITH/FROM (expected experimental grounding) — ACCEPT.
