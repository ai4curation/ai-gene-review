# PFRC (Q26789, Trypanosoma brucei brucei) – curation notes

**Automated deep research was unavailable for this gene** (Falcon authentication failed and the
OpenAI key was invalid in this environment). These notes are a manual literature review built
from the UniProt record, PubMed searches and the cached publications in `publications/`. No
`*-deep-research-*.md` file exists for this gene.

## Identity and naming (important)

- UniProt Q26789 (PFR2_TRYBB), "73 kDa paraflagellar rod protein", AltName PFR-C/PFR-D, 595 aa.
  The entry covers two near-identical tandem ORFs, PFRC and PFRD (they differ by DV -> EL at
  145-146) [file:TRYBB/PFRC/PFRC-uniprot.txt].
- **Naming trap.** The UniProt mnemonic is PFR2_TRYBB, but in the modern T. brucei literature the
  73 kDa protein PFRC is called **PFR1**, and the 69 kDa protein PFRA is called **PFR2**. The snl-2
  / snl4 RNAi lines target PFRA, which Portman et al. call PFR2 [PMID:19888464 "We compared the
  phenotype of snl4 with the previously described snl2 PFR2 knock down mutant"]; snl-2 is the PFRA
  RNAi line of Bastin et al. [PMID:10954429 "We have generated an inducible mutant trypanosome cell
  line (snl-2) that expresses linked inverted copies of a PFRA gene"]. So in this review:
  PFRC = 73 kDa = PFR1; PFRA = 69 kDa = PFR2. Literature about "PFR2" phenotypes in T. brucei is
  about PFRA, not this entry.
- Gene cloning: [PMID:7961827 "The present study reports the characterization of the genes coding
  for the 73-kDa PFR protein from T. brucei. Their gene product, PFR-C, is closely related to, but
  clearly distinct from, the 69 kDa species PFR-A."] The abstract describes four tandem genes per
  locus [PMID:7961827 "PFR-A and PFR-C are each coded for by a similarly organized cluster of four
  closely spaced, tandemly arranged genes"], whereas UniProt names two ORFs (PFRC, PFRD). Not a
  functional issue.

## Function

- The PFR is a lattice-like extra-axonemal structure restricted to euglenozoans and
  dinoflagellates [PMID:7961827 "Its occurrence is limited to a few groups of unicellular
  eukaryotes, the Euglenoids, Dinoflagellates, and Kinetoplastids."]. It is built mainly from the
  69 and 73 kDa proteins, proposed to form heteropolymers [PMID:7961827 "This finding indicates
  that the PFR fibers of the flagellum might represent heteropolymers formed by PFR-A and PFR-C"].
- Two major proteins [PMID:10954429 "The PFR is composed of 2 major proteins, PFRA and PFRC."];
  both flagellum-restricted [PMID:10567544 "PFRA and PFRC are abundant, and their localization is
  restricted to the flagellum."]. The PFR is assembled at the distal tip and forms a stable
  cytoskeletal structure [PMID:10954429 "The PFR is constructed by a polar assembly process at the
  distal end of the flagellum resulting in a stable cytoskeletal structure with low turn-over."];
  see also [PMID:32295845 "is assembled via PFR1 and PFR2 subunit incorporation at the distal tip
  of the growing flagellum"].
- A seven-residue distal-tip addition motif is conserved in PFRA and PFRC [PMID:10567544 "This
  seven-amino-acid sequence is conserved in all PFRA and PFRC proteins"].
- Co-dependence of the two major subunits: when PFRA is ablated (snl-1), PFRC still enters the
  flagellum but fails to assemble, piling up at the tip [PMID:10523512 "other PFR proteins such as
  the second major constituent, PFRC, accumulated at the distal tip of the growing flagellum"]
  [PMID:10523512 "This was not assembled as filaments and was removed by detergent-extraction."].
  This indicates PFRC requires PFRA to polymerise, consistent with heteropolymer assembly.
- Non-redundant structural requirement: [PMID:34257277 "despite sharing high-percentage amino acid
  identity, PFR1 and PFR2 are essential and non-redundant components of the PFR"]; [PMID:32295845
  "The two most abundant proteins in the PFR, PFR1 and PFR2, are critical for its assembly."];
  [PMID:19888464 "perhaps PFR1 and PFR2 (the only proteins that have been shown to localise to the
  PFR whose ablation results in a failure of PFR assembly)"]. Cryo-ET models the distal zone as
  scissors-shaped densities connected by coiled-coil "wires" to which PFR1/PFR2 helices may
  contribute (PMID:34257277; identity of densities not resolved).
- PFRC RNAi was performed (Durand-Dubief 2003), described as targeting motility-required flagellar
  proteins [PMID:12798502 "PFRA and PFRC genes, which code for flagellar proteins required for cell
  motility"]; the abstract reports only the PFRA results, so the PFRC-specific phenotype is not
  verifiable from the cache.
- Motility: PFR loss (via PFRA RNAi) paralyses procyclic cells (PMID:9468133, PMID:10954429);
  PFRC is implicated in motility only through its structural role.

## Calmodulin

- UniProt marks a predicted CaM-binding region 317-337 (ECO:0000255) and the IEA "calmodulin
  binding" comes from the Pfam Flagellar_rod (IPR007824) InterPro2GO mapping.
- Ridgley et al. 2000 (PMID:10960180, "Calmodulin-binding properties of the paraflagellar rod
  complex from Trypanosoma brucei") – no abstract in cache; cited by Portman et al. as
  [PMID:19888464 "There is also evidence for either direct or indirect interactions between the
  major PFR components and calmodulin"]. CaM resides in the PFR and is needed for its assembly
  [PMID:23787017 "calmodulin (CaM) is found within the paraflagellar rod (PFR)"] [PMID:23787017
  "CaM depletion resulted in total and catastrophic failure in PFR assembly"].
- Direct, PFRC-specific CaM binding is therefore plausible but not established in sources I can
  read. Treated as non-core.

## Annotation decisions

| Term | Evidence | Call |
|---|---|---|
| GO:0005516 calmodulin binding | IEA InterPro | KEEP_AS_NON_CORE |
| GO:0005856 cytoskeleton | IEA SubCell | MODIFY -> GO:0097740 paraflagellar rod |
| GO:0031514 motile cilium | IEA | ACCEPT |
| GO:0005198 structural molecule activity | NEW (IMP) | core MF |
| GO:0060285 cilium-dependent cell motility | NEW (IMP) | via structural role in PFR |
| GO:0120268 paraflagellar rod assembly | not annotated | moved to suggested_questions |

- GO:0097740 paraflagellar rod is used for >170 T. brucei TREU927 gene products in QuickGO
  (IDA/HTP), so it is the established CC for PFR proteins.
- GO:0120268 paraflagellar rod assembly currently has no annotations in QuickGO, so there is no
  comparator convention against it; PFRC passes the participation test as a polymerising
  structural subunit of the rod (like a filament subunit in its own polymer assembly), not as a
  substrate or regulator.
- No animal/plant-only terms, no host-process terms, no organelle mismatch beyond the generic
  cytoskeleton term. PFRA (69 kDa paralog, genes/TRYBB/PFRA) carries the identical three IEA rows.

## Revision (harmonisation with PFRA)

- GO:0097740 paraflagellar rod has only supramolecular complex as its OLS is_a parent and is not
  under cytoskeleton, so GO:0005200 (which occurs_in cytoskeleton) is ill-fitting; switched to
  GO:0005198 structural molecule activity, matching genes/TRYBB/PFRA.
- GO:0120268 is not annotated. A structural subunit incorporated into the rod is arguably what
  is assembled rather than an agent of assembly, so this is raised as a suggested question.
- NEW GO:0060285 cilium-dependent cell motility (IMP). PFRC-specific support is weaker than for
  PFRA: [PMID:12798502 "PFRA and PFRC genes, which code for flagellar proteins required for cell
  motility"], plus PFR1/PFR2 non-redundancy (PMID:34257277) and paralysis on PFR loss
  [PMID:10954429 "PFR construction was affected, resulting in cell paralysis"].
- The cytoskeleton -> paraflagellar rod MODIFY is a lateral correction, not a descendant
  refinement.

## Revision 2 (review-fix round, PR #5029)

PFRC and PFRA carry row-for-row identical GOA files, so divergent actions on shared rows need
a reason. Two were corrected.

- **GO:0031514 motile cilium: ACCEPT -> MODIFY -> GO:0097740.** The earlier ACCEPT called the
  term "non-redundant" with the paraflagellar rod assertion made in the same review. It is not:
  QuickGO's ancestors of GO:0097740 (relations is_a + part_of) are GO:0120025, GO:0031514,
  GO:0097740, GO:0099080, GO:0005929, GO:0110165, GO:0043226, GO:0005575, GO:0042995,
  GO:0097729, GO:0043227 -- i.e. paraflagellar rod is part_of GO:0097729 9+2 motile cilium and
  hence of GO:0031514 motile cilium. (The OLS `getAncestors` call returns only the is_a chain,
  which stops at GO:0099080 supramolecular complex; that is why the part_of link is invisible
  there and the QuickGO ancestors call is the one to use.) The row is therefore correct but
  general, which is MODIFY, and the replacement matches what PFRA does with the identical row.
- **core_functions.locations:** dropped GO:0031514, which was listed alongside its own
  descendant GO:0097740. PFRA lists only GO:0097740.
- **GO:0005516 calmodulin binding: KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED.** The old reason
  rested on "no evidence contradicts it", which is not support. What exists is (i) an
  InterPro2GO transfer off IPR007824, a *structural* Flagellar_rod domain shared by both major
  subunits, so protein-nonspecific; (ii) an ECO:0000255 predicted region at 317-337; (iii)
  complex-level "direct or indirect" interactions from the PFR interaction map. The one piece
  of biochemistry, Ridgley et al. (PMID:10960180, abstract not cached), is accessible only
  through the Portman and Gull review, which states it was run on a bulk PFR protein pool and
  does not resolve PFR1 from PFR2: [PMID:19879876 "This suggests that there are two pools of
  PFR proteins that are differentiated by their ability to bind calmodulin, although the
  presence in the preparations of proteins of similar molecular weight such as PAR1 and PAR4
  homologues may also explain these results."]. PMID:19879876 was added to the reference list
  and the row's supported_by so the judgement rests on that evidence rather than on absence of
  contradiction. MARK_AS_OVER_ANNOTATED rather than REMOVE, since calmodulin is a resident,
  assembly-critical PFR protein and the claim is plausible at the complex level; it is an
  over-annotation only as a statement about PFRC.
- Divergence from PFRA on the calmodulin row is deliberate: PFRA's row cites the
  calmodulin-Sepharose experiment and UniProt's predicted 335-355 region directly and is kept
  as KEEP_AS_NON_CORE. The pool-level caveat applies to both paralogs, so if the two reviews
  are harmonised again this is the row to revisit; it is flagged here rather than silently
  equalised.
