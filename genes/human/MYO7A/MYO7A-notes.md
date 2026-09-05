# MYO7A (human, Q13402, USH1B) — curation notes

Journal of research done while reviewing the GOA annotations. Provenance is given inline
as [PMID:NNNN "verbatim quote"] or [file:...] where a quote comes from a cached
publication or the deep-research report.

## 1. Identity and architecture

Unconventional myosin-VIIa, HGNC:7606, disease alias USH1B. Domain layout: N-terminal
motor domain, neck with five IQ motifs, a single-alpha-helix (SAH) lever-arm extension,
then a long tail of two MyTH4-FERM modules separated by an SH3 domain.

[PMID:21687988 "The human myosin-7a heavy chain is composed of the N-terminal motor
domain, a neck region with 5 IQ motifs, and a complex tail region."]

[PMID:11964381 "The tail begins with a dimerization domain, followed by two large repeats
of ∼460 aa, each containing a myosin tail homology 4 (MyTH4) and a 4.1, ezrin, radixin,
moesin (FERM) domain, separated by a src homology type 3 (SH3) domain"]

The InterPro FERM/Band-4.1 signatures on this entry therefore describe the cargo-binding
tail, not an acyl-CoA-binding enzyme — worth noting because the deep-research prompt
listed only FERM domains.

## 2. Motor biochemistry — the human protein

Heissler & Manstein characterised the isolated human motor domain fused to an artificial
lever arm. The key facts for annotation are a rate-limiting ADP release step, high duty
ratio, and high F-actin affinity:

[PMID:21687988 "A rate-limiting, slow ADP release step causes long lifetimes of strong
actin-binding intermediates and results in a high duty ratio."]

[PMID:21687988 "Our results show that human myosin-7a is a slow motor with a
rate-limiting ADP release step from actomyosin and a high affinity for F-actin, even in
the presence of ATP."]

[PMID:21687988 "These specific kinetic adaptations indicate that human myosin-7a is a slow
molecular motor with a high duty ratio, suitable for moving cargoes and mediating tension
in the cytoskeleton."]

[PMID:21687988 "Under the assumption that human myosin-7a has a load-dependent ADP
release, the kinetic properties are compatible with myosin-7a acting as tension sensor,
as defined by Nyitrai and Geeves"]

Free Mg2+ in the physiological range switches the motor between cargo-moving and
tension-bearing modes. This is the biochemical basis for treating MYO7A as a
tension-holding motor rather than a fast transporter, and it justifies ACCEPTing
GO:0000146, GO:0051015, GO:0005524 and GO:0030048 as core.

Caveat recorded in the reference review: the construct is a motor domain plus artificial
lever arm, so these numbers describe the motor module, not the autoinhibited full-length
molecule. Full-length human MYO7A is monomeric and folded until cargo adaptors open it
(Holló et al. 2023, JBC 299:105243, via the deep-research report; not separately cached).

## 3. Hair cells — upper tip-link density (UTLD)

The functionally decisive site is the UTLD of mature stereocilia, not the base:

[PMID:21709241 "we now show that MYO7A and sans, a MYO7A-interacting protein, cluster at
the UTLD"]

[PMID:21709241 "Analysis of the immunofluorescence intensity indicates that eight or more
MYO7A molecules are present at each UTLD, consistent with a direct role for MYO7A in
maintaining tip-link tension."]

[PMID:21709241 "In this complex, MYO7A is likely the motor element that pulls on CDH23 to
exert tension on the tip-link."]

The tripartite MYO7A–sans(USH1G)–harmonin-b(USH1C) complex was demonstrated by
co-transfection in COS7 cells; the hair-cell localisation is rodent. Hence the new
GO:1990435 annotation was entered as ISS rather than IDA for the human protein.

This is a tension-bearing complex of the *mature* bundle — deliberately distinguished in
the review from the transient ankle-link/USH2 complex of developing bundles.

UniProt states the same network at the level of function:
"Motor protein that is a part of the functional network formed by USH1C, USH1G, CDH23 and
MYO7A that mediates mechanotransduction in cochlear hair cells."
(MYO7A-uniprot.txt, FUNCTION block, ECO:0000269|PubMed:21709241.)

## 4. RPE — melanosomes, phagosomes, lysosomes

MYRIP is the RAB27A effector that couples melanosomes to the motor:

[PMID:11964381 "Taken together, these results demonstrate that MyRIP specifically binds to
myosin VIIa."]

[PMID:11964381 "In the retinal pigment epithelium cells, MyRIP, myosin VIIa and Rab27A are
associated with melanosomes."]

[PMID:11964381 "We propose that a molecular complex composed of Rab27A, MyRIP and myosin
VIIa bridges retinal melanosomes to the actin cytoskeleton and thereby mediates the local
trafficking of these organelles."]

Human loss-of-function evidence for the melanosome role (basis for the NEW GO:0032400
annotation, IMP):

[PMID:19643958 "RNAi knockdown studies showed that MYO7A functions to constrain rapid,
long-range movements of melanosomes."]

[PMID:19643958 "Melanosome motility was also comparable, and, after RNAi knockdown,
consisted of longer-range fast movements characteristic of melanosomes in shaker1 RPE."]

Note the direction of the effect: the motor *constrains* long-range (microtubule-driven)
movement, i.e. it captures and retains melanosomes on apical cortical actin. That is why
GO:0032400 melanosome localization was preferred over GO:0032402 melanosome transport.

Lysosomes:

[PMID:16001398 "Myosin-VIIa copurified with lysosomes on density gradients, and
fractionation and extraction experiments suggested that it was tightly associated with the
lysosome surface."]

[PMID:16001398 "These studies suggest that myosin-VIIa is a lysosome motor."]

The same paper summarises the phagosome literature: myosin-VIIa is not needed for ROS
binding or ingestion, only for later steps —
[PMID:16001398 "both in vivo and in primary culture, the RPE lacking myosin-VIIa exhibited
normal adhesion and ingestion of ROS"] and
[PMID:16001398 "The transport of the ingested ROS out of the apical region of the cell was
inhibited in shaker-1 mice"].

This is the reason GO:0007040 *lysosome organization* was MODIFYed to GO:0032418 *lysosome
localization* on both the IDA and the ARBA IEA: the demonstrated activity is positioning
of the organelle, not biogenesis.

## 5. Photoreceptors, connecting cilium and opsin transport

[PMID:8842737 "In the adult human retina, myosin VIIA was present in both cell types."]
(pigment epithelium and photoreceptors) — and crucially the species difference that
explains why shaker-1 mice have no retinal phenotype:
[PMID:8842737 "in mouse, only pigment epithelium cells expressed the protein throughout
development and adult life"].

Sub-cellular distribution in human photoreceptors:
[PMID:8842737 "in the photoreceptor cells, myosin VIIA is mainly localized in the inner and
base of outer segments as well as in the synaptic ending region where it is co-localized
with the synaptic vesicles"]

Opsin transport and the spectrin betaV scaffold:
[PMID:23704327 "We identified spectrin βV, the mammalian β-heavy spectrin, as a myosin
VIIa- and rhodopsin-interacting partner in photoreceptor cells."]
[PMID:23704327 "A failure of the spectrin βV-mediated coupling between myosin VIIa and
opsin molecules thus probably accounts for the opsin transport delay in myosin
VIIa-deficient mice."]

Both of the vague "intracellular protein localization" (GO:0008104) annotations — the
Ensembl IEA and the curator ISS, both from mouse P97479 — were MODIFYed to GO:0036372
opsin transport on this basis.

## 6. Judgement calls recorded during the review

- **GO:0042462 eye photoreceptor cell development (IC)**. The IC is drawn from
  GO:0001917 (inner segment localisation). Presence of a protein in a developing cell does
  not establish a developmental role, and the paper's own interpretation is about renewal
  and trafficking:
  [PMID:8842737 "we suggest that myosin VIIA might play a role in the trafficking of
  ribbon-synaptic vesicle complexes and the renewal processes of the outer photoreceptor
  disks"]. USH1B retinopathy is progressive and post-developmental. MODIFY →
  GO:0045494 photoreceptor cell maintenance.

- **PMID:11398101 cited for two MYO7A IMP annotations.** Full text is cached and is
  entirely an experimental study of PCDH15/USH1F; MYO7A appears only as background:
  [PMID:11398101 "Mutations in MYO7A / Myo7a are found in patients with DFNB2 , USH1B ,
  DFNA11 , and in shaker-1 ( sh1 ) mice"]. The *claims* (hearing, light perception) are
  correct and independently supported by PMID:7870171, so both annotations were ACCEPTed
  rather than removed, per the "do not overrule curators" rule, and the citation problem
  was recorded in `reference_review` as MISCITED / LOW relevance instead.

- **Bare GO:0005515 protein binding (×2, CIB2 and MYRIP)** → MARK_AS_OVER_ANNOTATED.
  Both interactions are real and well demonstrated, but the term carries no functional
  information. Interesting detail for the CIB2 one: MYO7A is *not* required for CIB2
  targeting — [PMID:23023331 "We observe no mislocalization of CIB2 in stereocilia of
  homozygous Myo7a and whrn mutant mice"] — so this is not a recruitment relationship.

- **GO:0019904 protein domain specific binding** → MARK_AS_OVER_ANNOTATED for the same
  reason (uninformative binding term).

- **GO:0048666 neuron development (ARBA)** → MARK_AS_OVER_ANNOTATED. Hair cells are
  mechanosensory epithelial cells, not neurons; the photoreceptor role is maintenance and
  transport in a differentiated cell. Not strictly false (photoreceptors are neurons) but
  a large over-generalisation from an unsupervised rule.

- **GO:0005829 cytosol.** Both the ARBA IEA and the IDA (PMID:15300860) were set to
  KEEP_AS_NON_CORE for consistency. The IDA comes from a study that expressed MYO7A IQ5
  peptides in smooth muscle cells of microarteries — a heterologous system — and full text
  is not cached, so the curator's call is not challenged; but cytosol is not a functional
  site for this motor.

- **GO:0120044 stereocilium base** (IEA + ISS) → KEEP_AS_NON_CORE. Myosin-VIIa is
  distributed along stereocilia including the basal/ankle-link region of developing
  bundles, so the mouse-derived annotation stands; but the decisive site in the mature
  bundle is the UTLD, which is why GO:1990435 was added rather than substituted.

- **IBA block.** No IBA was challenged. Two points followed the project's IBA guidance:
  MYO7A appearing in its own WITH/FROM for GO:0000146, GO:0030048 and GO:0007605 is
  expected (its own experimental annotation seeded the IBD) and is *not* circular; and the
  short donor list for GO:0007423 (FBgn0000317 crinkled, MGI:104510 Myo7a, PTN000321046)
  is not weak evidence.

## 7. Calmodulin / light chains

[PMID:15300860 "We identified a novel heterozygous missense mutation (c.2557C>T; p.R853C)
in a family with autosomal dominant non-syndromic hearing loss that changes an
evolutionarily invariant residue of the fifth IQ motif (IQ5), a putative calmodulin (CaM)
binding domain, of MYO7A."]

[PMID:15300860 "analysis of calmodulin-dependent vasoconstriction suggests constitutive
binding of CaM to the wildtype, but not the p.R853C-mutated IQ5 motif at all
physiologically relevant Ca2+ concentrations"]

GO:0005516 calmodulin binding accepted as core: the IQ-bound light chains are the lever
arm, and Ca2+-dependent CaM dissociation is how the motor is switched off. UniProt also
records CALML4 as a Ca2+-insensitive light chain (PubMed:32209652), which may preserve
lever-arm integrity when Ca2+ rises.

## 8. Open questions for the core-functions / experiment sections

- Is the human retinal disease driven primarily by RPE melanosome/phagosome dysfunction,
  by a direct photoreceptor ciliary transport defect, or both? The deep-research report
  flags this explicitly as unresolved.
- Does the N-terminal splice isoform difference (long vs short) tune tip-link tension along
  the tonotopic axis, as proposed by Holló et al. 2023? Currently a model, not established
  human physiology.
- No GO term currently expresses "maintenance of tip-link resting tension"; GO:1990435
  captures the location but the process is only implicit in GO:0007605 /
  GO:0050910-adjacent terms. Worth raising as a proposed new term.
