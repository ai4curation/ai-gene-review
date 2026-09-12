# hip-1 (C. elegans) — research notes

UniProt: G5EE04 (G5EE04_CAEEL). WormBase: WBGene00011735 / T12D8.8. Chromosome III.
Gene symbol: hip-1. Product: STI1 domain-containing protein = **Hsc70-interacting protein (HIP)**,
ortholog of mammalian **Hip/ST13** (FAM10 family). Evidence at protein level (PE1; PeptideAtlas).

## Identity confirmation (task sanity check)

The UniProt record IS the HSP70-interacting co-chaperone, not an unrelated gene:
- UniProt FUNCTION (ARBA): "One HIP oligomer binds the ATPase domains of at least two HSC70
  molecules dependent on activation of the HSC70 ATPase by HSP40. Stabilizes the ADP state of
  HSC70 that has a high affinity for substrate protein."
- Domain architecture matches Hip/ST13: Hip_N (IPR034649, N-terminal dimerization), STI1/HOP_DP
  (IPR041243, C-terminal DP domain), STI1_HS-bd (IPR006636), TPR repeats (IPR019734), TPR-like
  helical superfamily (IPR011990); Pfam HipN (PF18253), STI1-HOP_DP (PF17830), TPR_16 (PF13432);
  SMART STI1 + 3×TPR.
- PANTHER PTHR45883 "HSC70-INTERACTING PROTEIN" (subfamily SF2). "Belongs to the FAM10 family."
- NOTE: distinct from C. elegans **sti-1** (the HOP/Stip1 ortholog); both carry STI1-type domains
  but occupy different positions in the Hsp70/Hsp90 network
  [file:worm/hip-1/hip-1-deep-research-falcon.md "It is important to distinguish this protein from
  the *C. elegans* **sti-1** gene, which encodes the ortholog of HOP"].

## KNOWN (well-established, conserved biochemistry from mammalian orthologs)

- **Hsp70/Hsc70 co-chaperone; binds the ATPase (nucleotide-binding) domain.** Hip is a TPR
  protein that binds the N-terminal ATPase domain of Hsc70
  [PMID:7585962 "One Hip oligomer binds the ATPase domains of at least two Hsc70 molecules
  dependent on activation of the Hsc70 ATPase by Hsp40."]. Binding is exclusive to the ATPase
  domain [PMID:9528774 "Hip interacts exclusively with the amino-terminal ATPase domain of Hsc70."],
  which is separate from the Hsp40/Hop sites [PMID:9528774 "Hsc70 possesses separate nonoverlapping
  binding sites for Hsp40, Hip, and Hop."].
- **Stabilizes the ADP-bound (high substrate-affinity) state of Hsp70 — an "attenuator" of the
  cycle.** [PMID:7585962 "Hip stabilizes the ADP state of Hsc70 that has a high affinity for
  substrate protein."]. Structurally, the TPR core forms a bracket over the ATPase domain that
  locks ADP in [PMID:23812373 "the TPR core of Hip interacts with the Hsp70 ATPase domain through
  an extensive interface, to form a bracket that locks ADP in the binding cleft."]. Hip and
  nucleotide-exchange factors (NEFs, e.g. BAG-1) compete: [PMID:23812373 "Hip and NEF binding to
  Hsp70 are mutually exclusive, and thus Hip attenuates active cycling of Hsp70-substrate
  complexes."]. Thus Hip biases the system toward folding/holding over release/degradation.
- **Domain-specific binding via the TPR domain.** [PMID:8999928 "the Hsc70-binding site of Hip was
  mapped to a domain comprising multiple tetratricopeptide repeats and flanking charged
  alpha-helices."].
- **Homo-oligomerizes (tetramer / dimer of dimers) via an N-terminal domain.** [PMID:8999928
  "a domain required for homo-oligomerization was identified at the extreme amino terminus of Hip."]
  [PMID:9183013 "the chaperone forms a tetramer similar to what has been reported for the native
  protein from rat liver cytosol"]. Self-association gives avidity for multiple Hsp70 molecules.
- **Intrinsic holdase activity but no independent foldase / no ATPase.** Binds non-native protein
  but cannot refold it and does not hydrolyze ATP [PMID:9183013 "The role of Hip as a molecular
  chaperone has been confirmed by its ability to strongly bind to the reduced, carboxymethylated
  form of alpha-lactalbumin."; "Hip inhibited the refolding of alkaline phosphatase and malic
  dehydrogenase. Inhibition occurred at near stoichiometric levels of Hip and could not be reversed
  by the addition of ATP."]. In the context of the Hsp70 cycle this "holdase" behavior translates
  into anti-aggregation, not refolding-inhibition.
- **Cooperates with Hsc70 in folding of nascent chains and conformational maturation of signaling
  clients** [PMID:8999928 "The homo-oligomeric Hip protein cooperates with the 70-kDa heat shock
  cognate Hsc70 in the folding of newly synthesized polypeptide chains and in the conformational
  regulation of signaling molecules known to interact with Hsc70 and Hsp90."].
- **Cytosolic** co-chaperone of the cytosolic Hsp70 machinery (mammalian immunolocalization; falcon)
  [file:worm/hip-1/hip-1-deep-research-falcon.md "Hip/ST13 is predominantly a **cytosolic
  protein**"].

## KNOWN (C. elegans-specific, in vivo)

- **HIP-1 (T12D8.8) suppresses α-synuclein aggregation in an Hsp70-dependent manner in vivo.**
  Roodveldt et al. 2009 used a transgenic worm αSyn-aggregation model and RNAi.
  [PMID:19875982 "Such a co-aggregation phenomenon can be prevented in vitro by the co-chaperone
  Hip (ST13), and the hypothesis that it might do so also in vivo is supported by studies of a
  Caenorhabditis elegans model of αSyn aggregation."]
  [PMID:19875982 "our results with an in vivo αSyn aggregation model of C. elegans strongly support
  the hypothesis derived from the in vitro experiments, indicating that Hip is indeed required for
  suppression of αSyn inclusion formation in an Hsp70-dependent manner"].
  Genetic epistasis: knocking down Hip alone gave MORE inclusions than knocking down Hip+Hsp70
  together — i.e. Hip acts through Hsp70
  [PMID:19875982 "The observation in our C. elegans model that the absence of Hip alone could give
  rise to more inclusions than when both Hip and Hsp70 are absent is consistent with a scenario in
  which there is a redundancy of chaperone pathways"].
  Falcon summary of the same figures (paraphrase, cite primary for verbatim): hip-1 RNAi increased
  αSyn inclusions ~2.3-fold; double hsp-70+hip-1 RNAi reduced inclusions ~60% vs hip-1 alone
  [file:worm/hip-1/hip-1-deep-research-falcon.md].
- **Muscle localization (moderate/high-throughput GFP overexpression screen).** T12D8.8::GFP driven
  by a muscle-specific promoter localized to category 6 = dense bodies, thick filaments/M-lines, and
  ER/SR [PMID:21611156 "The GFP-tagged proteins in category 6 are located in several places
  throughout the cell. They appear to be in the dense bodies, M-line and/or thick filaments, as well
  as the ER or SR"]. This is the source of the GO HDA CC annotations (GO:0005783 ER, GO:0030017
  sarcomere, GO:0055120 striated muscle dense body). The authors explicitly caution that C-terminal
  GFP tagging + overexpression can perturb localization
  [PMID:21611156 "the presence or perhaps over expression of the GFP-tagged protein may be
  disruptive"] — so these muscle localizations are treated as non-core relative to the cytosol.
  (Biologically, chaperone machinery does associate with the Z-disk/dense body for sarcomeric
  protein quality control, so a genuine muscle-QC role is plausible but unconfirmed for HIP-1.)

## NOT known / dark (worm-specific)

- **Endogenous physiological clients/substrates of C. elegans HIP-1 are unidentified.** All in vivo
  worm evidence uses a heterologous, overexpressed aggregation-prone reporter (human α-synuclein);
  the native folding clients that require HIP-1 in the worm are undefined.
- **Loss-of-function phenotype under normal (non-transgenic) conditions is undescribed** — no
  reported hip-1 mutant phenotype for development, lifespan, stress resistance, or muscle
  maintenance. (Contrast the HOP ortholog sti-1, whose loss shortens lifespan
  [file:worm/hip-1/hip-1-deep-research-falcon.md].)
- **Native subcellular localization of endogenous HIP-1 in the worm is not directly measured**
  (only overexpression GFP in muscle). Cytosol is inferred from orthologs.
- Whether the recently proposed mammalian St13 role in **mitochondrial precursor import** (Juszkiewicz
  et al. 2025, MBoC) is conserved in the worm is untested
  [file:worm/hip-1/hip-1-deep-research-falcon.md].

## GOA annotation set (9 rows) — review plan

1. GO:0006457 protein folding — IBA (GO_REF:0000033) — ACCEPT (core BP).
2. GO:0030544 Hsp70 protein binding — IBA (GO_REF:0000033) — ACCEPT (core, defining MF).
3. GO:0005634 nucleus — IEA (ARBA GO_REF:0000117) — REMOVE (unsupported ML CC; Hip is cytosolic).
4. GO:0046983 protein dimerization activity — IEA (InterPro GO_REF:0000002) — MARK_AS_OVER_ANNOTATED
   (self-association is a structural property, not the informative MF; real but not core).
5. GO:0070013 intracellular organelle lumen — IEA (ARBA GO_REF:0000117) — REMOVE (unsupported ML CC).
6. GO:1902494 catalytic complex — IEA (ARBA GO_REF:0000117) — MARK_AS_OVER_ANNOTATED (generic;
   Hip itself is non-catalytic; binds catalytic Hsp70 but "catalytic complex" is uninformative).
7. GO:0005783 endoplasmic reticulum — HDA (PMID:21611156) — KEEP_AS_NON_CORE (muscle overexpression).
8. GO:0030017 sarcomere — HDA (PMID:21611156) — KEEP_AS_NON_CORE (muscle overexpression).
9. GO:0055120 striated muscle dense body — HDA (PMID:21611156) — KEEP_AS_NON_CORE (muscle overexpr.).

Core MF = GO:0030544 Hsp70 protein binding; core BP = GO:0006457 protein folding + GO:1903334
positive regulation of protein folding; core CC = GO:0005829 cytosol.

## Final review decisions (completed)

All 9 GOA annotations resolved; 3 NEW proposed annotations added. Every supporting_text
was grep/normalization-verified as a verbatim substring of the cached publication.

- GO:0006457 protein folding (IBA) — ACCEPT (core BP).
- GO:0030544 Hsp70 protein binding (IBA) — ACCEPT (core, defining MF).
- GO:0005634 nucleus (IEA/ARBA) — REMOVE (unsupported ML CC; Hip is cytosolic).
- GO:0046983 protein dimerization activity (IEA/InterPro) — KEEP_AS_NON_CORE (revised
  from the earlier MARK_AS_OVER_ANNOTATED plan: homo-oligomerization is experimentally
  real [PMID:8999928, PMID:9183013] and functionally relevant for avidity, so it is a
  correct non-core MF rather than an over-annotation).
- GO:0070013 intracellular organelle lumen (IEA/ARBA) — REMOVE (unsupported ML CC).
- GO:1902494 catalytic complex (IEA/ARBA) — MARK_AS_OVER_ANNOTATED (HIP-1 is itself
  non-catalytic [PMID:9183013 "did not catalyze the hydrolysis of ATP"]).
- GO:0005783 ER / GO:0030017 sarcomere / GO:0055120 dense body (HDA, PMID:21611156) —
  KEEP_AS_NON_CORE (muscle GFP overexpression; authors caution tagging may be disruptive).
- NEW GO:0005829 cytosol (ISS) — core site of action, inferred from orthologs.
- NEW GO:0051082 unfolded protein binding (ISS) — intrinsic holdase activity.
- NEW GO:1903334 positive regulation of protein folding (ISS) — attenuator mechanism
  biases folding [PMID:23812373 "enhances aggregation prevention by Hsp70"].

Knowledge gaps recorded (top-level): (1) endogenous worm clients + LoF phenotype are
undefined (only a heterologous overexpressed αSyn reporter was assayed in vivo)
[RESIDUAL_SUBGAP]; (2) native subcellular localization of endogenous HIP-1 unmeasured;
worm data are muscle GFP-overexpression only [CC_DARK].

Note: the "no annotation references the deep research file" validation WARNING is left
unresolved because the pre-edit hook resolves `file:` references against a temp-dir copy
and cannot see the (real, present) falcon file; this is a non-blocking warning only.

## References with PMIDs (all cached in publications/)
- PMID:7585962 Höhfeld et al. 1995 Cell — original Hip; ADP-state stabilization (abstract-only).
- PMID:8999928 Irmer & Höhfeld 1997 JBC — TPR = Hsc70-binding site; N-term oligomerization.
- PMID:9528774 Demand et al. 1998 MCB — Hip binds ATPase domain exclusively; separate cofactor sites.
- PMID:9183013 Bruce & Churchich 1997 EJB — tetramer; holdase; no ATPase; no independent foldase.
- PMID:23812373 Li, Hartl & Bracher 2013 NSMB — crystal structures; bracket locks ADP; NEF-exclusive.
- PMID:19875982 Roodveldt et al. 2009 EMBO J — C. elegans αSyn model; Hip required Hsp70-dependently.
- PMID:21611156 Meissner et al. 2011 PLoS One — body-wall-muscle GFP localizome (T12D8.8 category 6).
