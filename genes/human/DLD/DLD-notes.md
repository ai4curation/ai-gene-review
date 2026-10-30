# DLD (P09622) review notes

Human dihydrolipoyl dehydrogenase (DLD), the **E3** component. Shared, pleiotropic subunit.

## Verified core biology
- DLD is a FAD-dependent, NAD+-linked flavoenzyme (EC 1.8.1.4) that reoxidizes the
  dihydrolipoyl group on the lipoyl-bearing E2/H components, transferring electrons to
  NAD+ via its FAD. GO:0004148 dihydrolipoyl dehydrogenase (NADH) activity. Functions as a
  homodimer, one FAD per subunit; active site is a redox-active disulfide (Cys80-Cys85).
  [UniProt P09622 CATALYTIC ACTIVITY / COFACTOR / MISCELLANEOUS blocks]
- Shared E3 of FOUR complexes:
  - pyruvate dehydrogenase complex (PDH) — GO:0045254
  - 2-oxoglutarate (alpha-ketoglutarate) dehydrogenase complex (OGDH) — GO:0045252
  - branched-chain alpha-ketoacid dehydrogenase complex (BCKDH) — GO:0160157
  - glycine cleavage system as the L protein (GCSL / GcvL)
  - Also the 2-oxoadipate dehydrogenase complex (OADH, DHTKD1-E1) — GO:0160167
    [PMID:37701333 "including pyruvate dehydrogenase (PDH), alpha-ketoglutarate dehydrogenase
    (KGDH), branched-chain alpha-keto acid dehydrogenase (BCKDH), and 2-oxoadipate
    dehydrogenase (OADH)"; PMID:29191460 hE1a recruits hE2o and hE3 of OGDHc]
- Localization: mitochondrial matrix (main). Small nuclear fraction (~1-1.6%) as part of
  the nuclear α-KGDH complex that supplies succinyl-CoA to KAT2A for histone H3 succinylation
  [PMID:29211711].

## Moonlighting / secondary
- Cryptic serine protease activity when the homodimer is destabilized (S456-E431 dyad at
  interface); induced by disruption of the native dimer, which also inhibits the primary
  dehydrogenase activity [PMID:17404228]. Treat as non-core.
- Reported cilium/flagellum/acrosome localization by similarity (Q811C4, rodent), sperm
  capacitation/acrosome reaction — non-core, By similarity/IEA only.

## Disease
- DLD deficiency (DLDD, MIM 246900): combined deficiency of PDH + OGDH + BCKDH (and OADH).
  MSUD variant + lactic acidosis + alpha-ketoglutaric aciduria. [UniProt DISEASE; dismech
  Maple_Syrup_Urine_Disease.yaml "deficiency in the shared E3 subunit (DLD) produces..."]

## Annotation strategy
- Core MF: GO:0004148 (many EXP/IDA/IMP/IBA/TAS lines — ACCEPT).
- FAD binding GO:0050660 — ACCEPT (cofactor, direct).
- Complex membership (PDH GO:0045254, OGDH GO:0045252, BCKDH GO:0160157, OADH GO:0160167):
  all genuine, ACCEPT (or KEEP for OADH as it is a shared but less-central role).
- Processes: pyruvate decarboxylation to acetyl-CoA GO:0006086, 2-oxoglutarate
  decarboxylation to succinyl-CoA GO:0120551, branched-chain keto acid decarboxylation
  GO:0120552, TCA GO:0006099, 2-oxoglutarate metabolic GO:0006103, BCAA catabolic GO:0009083,
  L-lysine catabolic GO:0019477 — all genuine given shared E3 role. ACCEPT the specific ones;
  broad/parent ones KEEP_AS_NON_CORE.
- protein binding IPIs (GO:0005515) x9 from IntAct/interactome screens (PDHX O00330 is the
  physiological E3-binding-protein partner; HTT, ITGB1BP1, PRDX6, YWHAE, others are
  screen hits) — originally MARK_AS_OVER_ANNOTATED; re-actioned to REMOVE under the
  generic-protein-binding policy (2026-09): the PDHX contact is an assembly interaction
  captured by the PDH complex CC terms, the rest are screen hits, and none supports a more
  specific DLD MF. Removal does not mean the interactions are false.
- Localization: mitochondrion / mitochondrial matrix — ACCEPT. Nucleus/nucleoplasm — genuine
  minor pool (KEEP_AS_NON_CORE). Cilium/motile cilium/flagellum/acrosome/acrosomal
  vesicle/acrosomal matrix — By-similarity/IEA electronic; MARK_AS_OVER_ANNOTATED for human.
- oxidoreductase activity GO:0016491 (too general) — MODIFY -> GO:0004148.
  GO:0016668 (acting on sulfur group of donors, NAD(P) acceptor) — parent of GO:0004148,
  keep as accurate-but-general -> KEEP_AS_NON_CORE.

DR: falcon deep-research file did not land within the 8-minute poll window; grounded in
UniProt, cached publications, and dismech.

## Deep research (falcon) follow-up, 2026-09
The falcon file (`DLD-deep-research-falcon.md`) landed after the review was written. What it
adds, and what was done with each item:
- **Glycine cleavage system L protein.** The review described this role in prose but had no
  process annotation, and GOA has none for human or mouse DLD. Added NEW GO:0019464
  glycine decarboxylation via glycine cleavage system, because DLD catalyses the final step.
  Support: Reactome R-HSA-5694018 ["The last step in the glycine cleavage system is the
  reoxidation of the reduced lipoate (dihydrolipoyl group) attached to the H protein
  (GCSH:DHLL) catalysed by the L protein (mitochondrial dihydrolipoyl dehydrogenase, DLD)"].
  Comparator: yeast LPD1 and E. coli lpdA carry GO:0019464 in QuickGO. Added to
  core_functions.
- **Diaphorase / ROS moonlighting** (NADH oxidation with O2, Fe3+, NO or ubiquinone as
  acceptor; enhanced by dimer-interface disease variants). The deep research attributes this
  to Babady 2007 (PMID:17404228) and Vaubel 2011. The cached PMID:17404228 is abstract-only
  and its abstract does not mention diaphorase activity, so no annotation was made. Non-core
  in any case.
- **Cuproptosis.** The deep research reports DLD among the genes whose knockout blunts
  copper-induced death (Tsvetkov 2022). The cached abstract of that paper (PMID:35298263) does
  not name DLD. Even with full text this is necessity evidence: copper binds the *lipoylated*
  E2s (DLAT and others), and DLD is not lipoylated. No annotation.
- **KGDHc, BCKDHc, OADH, PDHc membership, and the E3BP tether.** Already covered by
  experimental rows (PMID:16442803, 29191460, 3593587, 15712224); nothing new.
- Disease-variant tables (G194C founder allele, dimer-interface variants) are consistent with
  the review's disease text. No GO consequence.


## 2026-10-17: current-source augmentation and superseding assessment

This entry supersedes the earlier action rationale without rewriting it. The prior seven generic-only binding removals are withdrawn under the [explicit project instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). Actual structures, exact interaction records and original screening Methods support eight contextual generic-binding rows. The additional binary ITGB1BP1 pair supports cytoskeletal regulatory protein binding because the partner regulates cytoskeletal organization; it does not assign that role to DLD. The HTT assay uses residues 1–88. Co-IP/AP-MS associations with PRDX6 or YWHAE are not automatically enzyme/adaptor recognition activities.

The review retains all 84 old annotation source objects, including the prior glycine-cleavage proposal. The genuine current fetch contributes five additional GOA rows. It also enriches 25 old normal-fetch source objects with supporting entities; those are retained as source provenance rather than overwriting the historical identities. One consciously new endopeptidase MF produces 90 total rows: 57 ACCEPT, 15 KEEP_AS_NON_CORE, 16 MODIFY and 2 NEW, of which one NEW is historical. Three natural products and all prior history remain intact. No additional biological process or protease location is proposed.

The two catalytic units are distinct. Lipoyl oxidation is reused across mitochondrial enzyme systems, including the performed regeneration step in glycine cleavage. Human recombinant WT/mutant experiments in [Babady et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC1851069/) and independent [DLD–IκBε cleavage experiments](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5746455/) support conditional endopeptidase activity. The latter cellular stress experiments are mouse N9/brain, while the purified preparations are human. Preparation/refolding and reaction-recipe limits remain explicit. Current serine-type term definitions require a triad, whereas the original mutagenesis supports a serine/glutamate dyad; GO:0004175 therefore captures the demonstrated chemistry. The earlier statement that proteolysis is merely non-core has been reconsidered with this independent evidence, without claiming constitutive protease physiology.

Canonical mitochondrial annotations are refined at the gene level to matrix, while preserving the individual sources’ organelle-only resolution. Nuclear/nucleoplasmic and inferred sperm pools remain contextual. The [sperm paper](https://pubmed.ncbi.nlm.nih.gov/15888450/) directly studies detailed hamster flagellar/matrix localization and mouse acrosomal staining; the human whole-PDH antibody result is not DLD-specific. Failed human anti-E3 staining does not prove absence. [HPA](https://www.proteinatlas.org/ENSG00000091140-DLD/subcellular) supplies supported nucleoplasm and uncertain principal-piece/primary-cilium staining. The former primary-location-based over-annotation judgments are replaced by scoped contextual retention.

Original source access was checked independently of cache flags. Several nominal full-text extracts omit critical Methods or repeat the abstract. The [evidence guide](DLD-evidence-guide.md) supplies public source locators, assay/species limitations, original-recovery status, phylogenetic placement and Reactome role distinctions. In particular, 20833797 does not provide a matrix-resolved assay in the available extraction; the refinement uses independent target-level evidence. The 29191460 and 3593587 full originals remain unavailable, so their explicit positive abstracts and established target biology support curator deference without invented details.

Original machine cache bytes, the previous notes prefix and historical session records are preserved. The normal provider attempt returned the earlier research body; it is not presented as a fresh independent source. Short exact quotations are placed once in the YAML and reused by reference elsewhere. The old long Reactome quotation remains part of the unchanged historical prefix and has not been repeated or enlarged.


### Genuine GOA refresh and historical source lifecycle

The normal current fetch returned 85 source records. Three former GO_REF:0000120 records (pyruvate process, OGDH complex and PDC complex; historical zero-based rows 22/25/26) are no longer in that snapshot; the same claims now occur under GO_REF:0000107 in rows 86/87/88. Their original term, evidence, reference and qualifier remain recorded. Only `retired: true` is added to those three old records to mark replacement, while their ACCEPT scientific verdicts remain unchanged. This is not biological withdrawal and does not relabel a fetched annotation as NEW.

The canonical GOA file uses the unedited normal-fetch output. The [prior TSV snapshot](DLD-bioinformatics/source-snapshots/DLD-goa-before-review.tsv) is preserved byte for byte, with [provenance](DLD-bioinformatics/source-snapshots/provenance.json) recording its commit/blob/hash and the current retrieval URL/time/hash. Initial ordinary validation failures against the old and new snapshots exposed the reciprocal source-reference mismatch; no fabricated union or validator bypass was used. Other machine caches remain unchanged. The computed review state is DRAFT because of eight explicit-policy generic-binding advisories and one unused-provider-support advisory; the biological review has no PENDING rows.


## 2026-10-17 — Follow-up: conditional activity, interactions and localization

This entry supersedes the earlier two-core synthesis and ITGB1BP1 refinement while preserving the underlying evidence and prior notes. The established core is the shared lipoyl-redox activity. The conditional endopeptidase NEW annotation remains supported; its uncertain native human deployment is now an explicit BIOLOGY knowledge gap with a matched experiment. The activity is not described as mutant-only: recombinant wild-type human DLD also cleaves substrate. IκBε is an experimentally supported candidate substrate mechanism, rather than an absence of any cellular substrate evidence.

For the abstract-only cached [Babady et al. original, PMID:17404228](https://pmc.ncbi.nlm.nih.gov/articles/PMC1851069/), the separately read indexed original locators are Results and Fig. 2C/D (wild type versus D444V and monomer-enriched fractions); Results and Fig. 3B–D (C-terminal fragment, inhibitor controls and mutant fluorogenic-peptide assay); the proposed dyad analysis associated with Fig. 4; and the proteolytic-assay subsection of Experimental Methods (human frataxin residues 56–210 and its 13-residue peptide). Fig. 3D specifies pH 8.0, 50 mM NaCl and measurements over hours. These are original text/legend reads, not a claim that the protected abstract cache contains the Methods or that figure pixels were examined. The later [PMID:29128334](https://pmc.ncbi.nlm.nih.gov/articles/PMC5746455/) Fig. 6H and the STAR Methods proteolytic-assay subsection describe human WT/mutant preparations, including HA purification, urea elution and refolding; the stress-associated cellular evidence is mouse N9/brain. Preparation and physiological scope remain material limits.

The HuRI DLD–ITGB1BP1 pair remains a positive binary association, supported by validated record EBI-24650155 and related screen records. It is now KEEP_AS_NON_CORE without GO:0005519. The partners’ usual matrix and cytosolic focal-adhesion contexts leave native encounter and biological function unresolved; compartment difference alone does not establish a false positive. This treatment follows the [explicit project binding instruction](https://github.com/ai4curation/ai-gene-review/blob/da7850aa314a89131f63dbfec98d7e4d983fba54/projects/CLINGEN_MENDELIAN.md#curation-instructions). The well-supported PDHX tether interaction also remains generic because evidence strength does not create a missing specific molecular-function term.

The four sperm/cilium reasons now start from positive homolog evidence in [PMID:15888450](https://pubmed.ncbi.nlm.nih.gov/15888450/): hamster anti-E3 localization to acrosome and flagellar principal piece with antigen-preabsorption controls (Fig. 2), mouse acrosomal staining (Fig. 3A/B), and hamster detergent/shearing/exocytosis experiments resolving acrosomal matrix (Fig. 4). The human anti-E3 experiment was unsuccessful; whole-PDH staining is not DLD-specific. HPA’s uncertain human principal-piece and primary-cilium observations are kept distinct. Rodent motile flagellar localization does not establish a human primary-cilium pool. All four contextual KEEP_AS_NON_CORE actions remain unchanged.

All source identities, the genuine current GOA, the exact archived predecessor and its provenance, three lifecycle-retirement flags, natural products and prior caches remain unchanged. No additional annotation or quote is added in this follow-up.
