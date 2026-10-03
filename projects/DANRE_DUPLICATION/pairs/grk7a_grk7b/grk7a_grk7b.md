---
title: "grk7a / grk7b"
autolink_gene_symbols: false
---

# grk7a / grk7b

[Back to pairs](../README.md)

**Bottom line:** MIXED, and asymmetric. At the expression level the copies are
partitioned among photoreceptor types: grk7a is expressed in all cones and makes up
essentially all Grk7 protein in the larval retina, while grk7b is enriched in adult UV
cones. At the protein level both copies keep the ancestral domain architecture and
rhodopsin kinase activity. Recombinant Grk7b, however, phosphorylates rhodopsin more
than 30-fold more slowly than Grk7a. That figure comes from a later paper's summary of
Wada et al. 2006, not from the cached Wada abstract. The functional data are asymmetric too. grk7a knockdown
or knockout slows cone and pineal photoresponse recovery. Knocking down grk7b alone has
no clear effect, and grk7b contributes only when grk7a is also removed (pineal). So
grk7a looks like the "generalist" that keeps the ancestral cone role, and grk7b like a
UV-cone-biased, lower-activity copy. The pre-duplication (gar) expression pattern is
unknown, so a strict sub- vs neofunctionalization call cannot be made. The pair itself is
a clean TGD pair.

| | grk7a | grk7b |
|---|---|---|
| UniProt | Q49HM9 (Swiss-Prot) | Q1XHL7 (Swiss-Prot) |
| Other names | GRK7-1, zGRK7-1, grk7-1 | GRK7-2, zGRK7-2, grk7-2 |
| Human ortholog | GRK7; PANTHER least-diverged ortholog (LDO) | GRK7 (O) |
| Length | 549 aa | 548 aa |
| Review | [genes/DANRE/grk7a](../../../../genes/DANRE/grk7a/grk7a-ai-review.yaml) | [genes/DANRE/grk7b](../../../../genes/DANRE/grk7b/grk7b-ai-review.yaml) |

**Naming.** Map every name before using it as evidence.

- Wada et al. 2006 cloned GRK7-1 and GRK7-2. Their mRNAs, AB212995 and AB212996, are
  cross-referenced in the grk7a and grk7b UniProt entries. The entries list `grk7-1` and
  `grk7-2` as synonyms (`genes/DANRE/*/*-uniprot.txt`). So **GRK7-1 = grk7a** and
  **GRK7-2 = grk7b**.
- The pineal study uses AY900004, the Rinner 2005 mRNA held on Q49HM9, as its GRK7a probe
  and AB212996 as its GRK7b probe:
  [PMID:33579376 "GRK7a (bases 60 to 1060 of the coding sequence, accession number, AY900004), and GRK7b (bases 60 to 1059 of the coding sequence, accession number, AB212996)"]
- It also restates the mapping directly:
  [PMID:33579376 "rhodopsin phosphorylation activity of GRK7a (GRK7–1) is more than 30-fold faster than those of GRK1a, GRK1b, and GRK7b (GRK7–2 [29])"]
- **GRK1A/Grk1a** (rod kinase) and **GRK1B/Grk1b** (cone kinase) are a different pair. They
  are paralogs of each other, not of grk7a/grk7b. Grk1b is the other kinase in zebrafish
  cones, and it is the main source of redundancy with grk7a (section 4).
- **Antibody caveat.** Several "anti-Grk7" antibodies recognize both paralogs, for
  example: [PMID:30372740 "We generated a rabbit polyclonal antibody that recognizes both paralogs of zebrafish Grk7 (Grk7a and Grk7b)."]
  Unqualified "Grk7" immunostaining therefore cannot be assigned to one copy unless a
  knockout or knockdown control is used.

## 1. Evidence the pair comes from the TGD

**PANTHER v19** (row in `../../panther_tgd_pairs.tsv`):

| tgd_call | duplication_branch | pair_class | family | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR24355 (G PROTEIN-COUPLED RECEPTOR KINASE/RIBOSOMAL PROTEIN S6 KINASE) | 1 (shared by both copies) | 2 | no |

PANTHER places the duplication on the TGD branch itself: after the gar split and before
the zebrafish–medaka split. Both copies share a single gar co-ortholog, and medaka keeps
two co-orthologs. This is the strongest PANTHER call, which only 778 clean 1:1 pairs
receive. The human ortholog labels (GRK7 LDO for grk7a, GRK7 ortholog for grk7b) mean
that PANTHER finds grk7b the more diverged copy in sequence.

**Published phylogenetic and genome work**

- A phylogenetic analysis of all zebrafish phototransduction genes assigns this pair to
  the TGD:
  [PMID:34462505 "All differentially partitioned genes except for opn1sw1 and opn1sw2 arose during the teleost-specific whole-genome duplication (arr3a/arr3b, cnga3a/cnga3b, grk7a/grk7b, gngt2a/gngt2b, and rcvrn2/rcvrn3) or later"]
- An earlier survey of vertebrate phototransduction genes reached the same conclusion:
  [PMID:19720650 "Teleost fishes have duplicates of both GRK1 and GRK7 that seem to agree with 3R."]
- The knockout paper states it as background:
  [PMID:30372740 "As a result of a genome duplication event that occurred in teleosts millions of years ago, zebrafish possess many gene duplicates (e.g., grk1a and grk1b, and grk7a and grk7b)."]
- Jawed vertebrates otherwise have a single GRK7, so the teleost pair is not an older
  paralog pair:
  [PMID:29321241 "It is also clear that, following 2R WGD, jawed vertebrates retained two GRK1 isoforms but only a single GRK7, whereas agnathan vertebrates retained two GRK7 isoforms but only a single GRK1."]
- The zebrafish paralogs are much less similar than the Xenopus laevis GRK7 pair from
  that species' recent allotetraploidy. This fits an old duplication:
  [PMID:18803695 "laevis GRK7 (GRK7a and GRK7b), which were found to be 94% identical at the amino acid level."]
  [PMID:18803695 "In comparison, the 2 zebrafish GRK7 proteins, zGRK7-1 and zGRK7-2 are only 73% identical at the amino acid level, suggesting their duplication and divergence occurred much earlier."]

**What is and is not established**

- *Established.* The duplication happened in the teleost stem. Tree placement
  (PANTHER TGD branch, a shared gar co-ortholog, two medaka copies) and an independent
  phylogenetic analysis (PMID:34462505) agree on this.
- *Not checked here.* Double-conserved synteny against the gar GRK7 region. Given the
  strong tree evidence, this is a confirmation, not an open question.

## 2. Protein-level comparison

- **Identity.**
  - Global alignment: 73.2% identity, 83.7% similarity (`annotation-comparison.md`).
  - This matches the published 73% (PMID:18803695, quoted above).
  - Both copies are about equally distant from human GRK7:
    [PMID:18803695 "The average identity between the XGRK7 paralogs and human GRK7 is 68%, whereas the average identity between human and zebrafish GRK7 is 58–59%."]
- **Domains.** Both copies have the full GRK architecture: an N-terminal RGS-homology
  domain, a protein kinase domain, and an AGC-kinase C-terminal domain. UniProt maps
  these domains to equivalent positions in each (grk7a: RGS 53–171, kinase 186–449;
  grk7b: RGS 53–172, kinase 187–446) (`*-uniprot.txt`). No domain has been gained or lost.
- **Key motifs.** Both are conserved in both copies (sequence inspection of the two
  UniProt records):
  - *The PKA site.* It lies at Ser33 in both (grk7a `KKRRRS33`, grk7b `KKRRCS33`). This
    is the site that GRK7 regulation by cAMP depends on:
    [PMID:36273582 "the antibody against phosphorylated Grk7 showed cAMP-dependent phosphorylation of GRK7 at Ser36 (Ser33 in zebrafish) in vivo in multiple vertebrates"]
  - *The C-terminal CAAX motif.* Both end in `...CTLL`, which specifies the
    geranylgeranyl anchor typical of GRK7s:
    [PMID:29321241 "This indicates that, whereas the GRK1As are anchored by a farensyl moiety, the GRK1Bs and the GRK7s are anchored by a geranylgeranyl moiety."]
- **Kinase activity.** This is the one reported protein-level difference.
  - Recombinant GRK7-1 (grk7a) is a very fast rhodopsin kinase:
    [PMID:16787417 "The recombinant GRKs phosphorylated light-activated rhodopsin, and the Vmax value of the major cone subtype, GRK7-1, was 32-fold higher than that of the rod kinase, GRK1A."]
  - A later paper by a different group (Shen et al. 2021), citing Wada 2006, reports
    that GRK7-2 (grk7b) is as slow as the GRK1s:
    [PMID:33579376 "A previous comparison of the initial rates of rhodopsin phosphorylation by recombinant GRKs in zebrafish revealed that rhodopsin phosphorylation activity of GRK7a (GRK7–1) is more than 30-fold faster than those of GRK1a, GRK1b, and GRK7b (GRK7–2 [29])."]
  - Caveats:
    - The GRK7-2 figure is not in the Wada 2006 abstract. It is known here only from
      this secondary statement. The full text of PMID:16787417 was not available.
    - The substrate was bovine-type rhodopsin, not a cone opsin. UV opsin would be the
      natural substrate for grk7b.
    - UniProt nevertheless curates both copies as catalytically active (EC 2.7.11.14,
      ECO:0000269 from PMID:16787417); only the grk7a entry carries kinetic
      parameters.
- **Binding partners.** Recoverins bind all four zebrafish opsin kinases, including both
  Grk7s:
  [PMID:33385424 "Further, we investigated the interaction between recoverin and opsin kinase variants by surface plasmon resonance spectroscopy indicating interaction of recoverin 1a and recoverin 2b with all opsin kinases."]
- **Cross-rescue.** Not tested for either direction.

**Conclusion (protein level)**

- *Established:* both copies keep the ancestral molecular function (rhodopsin kinase
  activity), the domain architecture, the PKA regulatory site and the membrane anchor.
  There is no evidence of a new activity in either copy.
- *Reported but weakly documented:* grk7b's kinase is more than 30-fold slower in vitro.
  If this is confirmed with cone opsins, it is quantitative protein-level divergence in
  grk7b (reduced function), not innovation.

## 3. Expression

**Retina: cone subtypes**

- Adult single-cell RNA-seq separates the copies among cone subtypes:
  [PMID:34462505 "Additionally, we found multiple pairs of paralogous genes that were differentially enriched between UV cones (grk7b, cngb3.2, and guca1e) and other cone types (grk7a, cngb3.1, and guca1e.2)."]
- grk7b is one of the few genes specific to a single cone subtype:
  [PMID:34462505 "This analysis also showed that genes that are highly specific to single cone subtypes are quite rare (Fig. S1C and Supplementary Data S1) and include tbx2a (UV), grk7b (UV), tgfa (UV), mpzl2b (blue), fibcd1a (green), angptl4 (green), and glis3 (red)."]
- grk7b belongs to the UV-cone gene program that Samd7 represses in long-wavelength
  cones:
  [PMID:39531499 "UV-cone genes are up-regulated in samd7−/− hybrid red/UV cones including tbx2a, tbx2b, opn1sw1, arr3b, mir729, tgfa, and grk7b (5)."]
- A review summarizes the split as pan-cone vs UV-only. The UV-only claim rests partly
  on unpublished data:
  [PMID:33598728 "grk1a is expressed exclusively in rods, grk1b and grk7a in all cones, and grk7b only in UV cones [152, 196] (unpublished data)."]
- grk7a is also functional in UV cones. Its knockdown slows the UV-driven ERG:
  [PMID:26246494 "We confirmed that the response recovery is significantly delayed in the absence of Grk7a not only under normal ERG [14] but also in UV spectrum ERG"]
- *Conflicting data point.* An immunostaining abstract reports Grk7b in double cones
  (red/green), not only in UV cones:
  [PMID:33385424 "In contrast, recoverin 2b was only detected in double cones and co-localized with opsin kinases 1b, 7a and 7b."]
  The full text was not available to check antibody specificity.

**Retina: developmental stage and abundance**

- Wada 2006 localized GRK7-1 (grk7a) to cone outer segments and called it the "major
  cone subtype". The abstract does not report an outer-segment localization for GRK7-2:
  [PMID:16787417 "In situ hybridization and immunohistochemical studies localized both GRK1B and GRK7-1 in the cone outer segments and GRK1A in the rod outer segments."]
- In 5-dpf larvae, an antibody that detects both paralogs finds no Grk7 at all in grk7a
  knockouts. Larval retinal Grk7 protein is therefore essentially all Grk7a, and grk7b
  protein is below detection:
  [PMID:30372740 "Analysis of grk7a−/− larvae at 5 dpf show undetectable levels of Grk7 compared to wildtype (Fig. 2A, 2B)."]
  [PMID:30372740 "Immunocytochemical analysis also confirms knockout of Grk7 expression in grk7a−/− larvae, with no anti-Grk7 immunoreactivity compared to wildtype (Fig. 2C, middle column)."]

**Pineal organ (shared domain)**

- All three cone-type kinases are expressed in the adult pineal:
  [PMID:33579376 "The pineal organ in adult zebrafish was reported to express three types of GRKs: the cone-related GRKs GRK1b and GRK7a, as well as GRK7b, a paralog of GRK7a [29]."]
  [PMID:33579376 "We confirmed the expression of these GRKs in the pineal organ of zebrafish via in situ hybridization (Fig. S1)."]

**Temporal regulation (shared)**

- Both transcripts oscillate in phase over the day:
  [PMID:34550876 "Although many ohnologs (paralogs generated in a whole-genome duplication event), such as grk7a and grk7b, share a similar circadian phase or oscillatory amplitude, others, such as rcv1a and rcv1b, show an almost anti-phasic relationship."]

**Ancestral state**

- The single-copy GRK7 of other vertebrates is a cone kinase:
  [PMID:30372740 "GRK1 is expressed in all vertebrate rods, while GRK7 is expressed in cones in all species examined to date except for mice and rats, which express only GRK1 in cones."]
- No study found here resolves the cone-subtype distribution of the single GRK7 in gar,
  or of the two medaka copies. Whether pre-duplication GRK7 was in all cone types, and
  so whether grk7b's UV restriction is derived, is therefore not established.

**Summary.**

- *Shared domains:* UV cones (grk7a is functional there, and grk7b is enriched there),
  the pineal organ, and circadian phase.
- *Copy-specific:* grk7a in the non-UV cones (red, green, blue), and grk7a as the
  dominant larval Grk7.
- *No grk7b-only domain has been shown.* grk7b's UV enrichment is relative, since grk7a
  also acts in UV cones.
- The pattern is therefore **asymmetric**, like cryaba/cryabb. One copy (grk7a) keeps
  the broad, pan-cone ancestral-looking pattern. The other (grk7b) is restricted.
- That is consistent with degenerative loss of expression domains in grk7b, but it is
  not a reciprocal DDC split. Caution applies here:
  [PMID:35253876 "There is a tendency in the literature to ascribe subfunctionalization to any case in which duplicate genes have somewhat different expression patterns."]

## 4. Experimental evidence of function

**grk7a**

- *Morpholino (Rinner 2005)*, ZDB-MRPHLNO-050824-1: strong cone recovery and behavioral
  defects:
  [PMID:16039565 "Photoresponse recovery in Grk7a-deficient larvae was delayed in electroretinographic measurements, and temporal contrast sensitivity was reduced, particularly under bright-light conditions."]
- *TALEN knockout (Chrispell et al. 2018)*: an exon-1 PTC allele (7-bp deletion/6-bp
  insertion, truncation at 53 aa) with no detectable Grk7 protein. The phenotype is
  milder than in the morphant:
  [PMID:30372740 "A logarithmic linear regression of the non-saturating portion of the response shows a recovery half-life of 1.7 seconds for wildtype larvae, versus 2.3 and 3.0 seconds for grk1b−/− and grk7a−/− larvae, respectively (Fig. 4B, inset)."]
  [PMID:30372740 "These contrasting results may be due to side effects of morpholino knockdown, which have been reported to give variable results.35"]
- *Redundancy with Grk1b, not with grk7b.* The authors attribute the mild knockout to
  the other cone kinase:
  [PMID:30372740 "The grk1b−/− and grk7a−/− larvae were similar to wildtype larvae, suggesting that these Grks functionally substitute for each other."]
- *cAMP regulation (Chrispell 2022)*: loss of grk7a abolishes the forskolin-induced
  delay in cone recovery:
  [PMID:36273582 "These data suggest that the delay in cone recovery brought about by increased levels of cAMP is mediated by Grk7a rather than Grk1b in zebrafish larvae."]
- *Pineal*: grk7a is the dominant kinase for inactivating the parapinopsin photoproduct:
  [PMID:33579376 "We found that GRK7a knockdown slowed recovery of the response of parapinopsin photoreceptor cells, whereas GRK1b knockdown or GRK7b knockdown did not have a remarkable effect"]
- *Ectopic expression in rods (Vogalis 2011).* The abstract does not name the paralog. A
  review (Zang & Neuhauss 2021) identifies it as grk7a:
  [PMID:33598728 "Ectopic expression of cone grk7a in rods resulted in cone-like rod responses [194]."]
  [PMID:21486791 "exogenous GRK7 in GRK7-tg animals led to lowered rod sensitivity, as occurs in cones, but surprisingly to slower response kinetics."]

**grk7b**

- *No mutant* has been reported.
- *Single morpholino knockdown*: no remarkable effect in the pineal assay (PMID:33579376,
  quoted above).
- *Combined morpholinos (pineal, 2025)*: grk7b contributes when grk7a is also depleted.
  This is residual backup capacity:
  [PMID:39925416 "Similarly, a contribution to the response termination processes in GRK7a/1b double-knockdown fish is suggested based on GRK7b (Figure 3E, yellow closed diamond)."]
  [PMID:39925416 "These observations suggest that GRK7b and also presumably GRK1b contribute to the response termination processes in addition to GRK7a in control fish."]
- *No retinal loss-of-function data*, including UV-cone recordings.

**Compensation**

- There is no evidence that grk7b rises when grk7a is lost. In the grk7a PTC knockout,
  total Grk7 detected by a both-paralog antibody is undetectable in larvae
  (PMID:30372740, quoted in section 3).
- Adults and mRNA levels were not examined in those mutants, so transcriptional
  adaptation has not been directly tested:
  [PMID:30944477 "Therefore, use of RNA-less alleles can uncover phenotypes not observed in alleles exhibiting mutant mRNA degradation."]

## 5. Fate classification

**MIXED: asymmetric expression partition (grk7a pan-cone and dominant; grk7b
UV-cone-enriched), with reported protein-level weakening of grk7b's kinase rate, and
backup by grk7b only when grk7a is removed (pineal).**

| Level | Call | Evidence | Confidence |
|---|---|---|---|
| Molecular function | Conserved in both (not INNOVATION) | Same domains, PKA site and CAAX anchor; both phosphorylate rhodopsin (PMID:16787417); both bind recoverins (PMID:33385424) | High |
| Protein tuning | grk7b kinase >30-fold slower than grk7a | PMID:33579376 citing PMID:16787417; rhodopsin, not cone opsin, used as substrate | Medium-low (secondary report, non-native substrate) |
| Expression (retina) | Asymmetric partition. grk7a in all cones; grk7b enriched in UV cones, undetectable as protein in larvae | PMID:34462505, PMID:39531499, PMID:33598728, PMID:30372740; a conflicting double-cone report (PMID:33385424) | Medium. Judged within zebrafish; no gar data |
| Cone function | grk7a carries the Grk7 role; redundancy is with Grk1b, not grk7b | PMID:30372740, PMID:36273582 | High for grk7a; grk7b untested in retina |
| Pineal | Shared expression; grk7a dominant, grk7b a minor backup | PMID:33579376, PMID:39925416 (morpholinos) | Medium |
| BACKUP | Weak, pineal only | Only in multiple-knockdown backgrounds | Low to medium |

Distinguishing what is established from what is inferred:

- **Established:**
  - The pair is a TGD pair.
  - Both proteins keep the complete GRK7 architecture and rhodopsin kinase activity.
  - grk7a is expressed in all cone types and provides essentially all larval retinal
    Grk7.
  - grk7b transcripts are enriched in adult UV cones.
  - Loss of grk7a slows cone and pineal photoresponse recovery.
  - Grk7a mediates the cAMP effect on cone recovery.
  - Single grk7b knockdown has no clear pineal effect.
- **Inferred:**
  - That grk7b's UV-cone restriction is a derived loss rather than an ancestral UV-cone
    specialization. No gar or medaka cone-subtype data exist.
  - That grk7b is a weaker enzyme in vivo. The >30-fold figure is secondary and was
    measured on rhodopsin.
  - That grk7b tunes UV-cone shut-off kinetics. This is a hypothesis only.
  - Whether the cAMP/PKA regulation shown for Grk7a also applies to Grk7b. The site is
    conserved, but this is untested.

**Why not a cleaner call?**

- *Subfunctionalization (DDC)* requires each copy to lose something the other keeps.
  grk7a has lost nothing identifiable: it is in all cones, including UV cones, and in the
  pineal. So the split is one-sided.
- *Neofunctionalization* would need a new function in grk7b and a pre-duplication
  comparison. Neither exists.
- *Backup* is contradicted in the retina, where grk7b protein is absent from larvae. In
  the pineal it is only partial.
- The profile (one copy restricted and less active, the other keeping the ancestral role)
  fits the quantitative subfunctionalization or hypofunctionalization end of the
  spectrum. However, that fate is not among the project's categories, and its key
  evidence (the rate difference) is weak.

**What would change the call**

- *Cone-subtype expression of GRK7 in spotted gar* (and of the two medaka copies). If
  gar GRK7 is UV-restricted, grk7a gained expression in the other cones, which would
  make the call innovation at the expression level. If gar GRK7 is pan-cone, grk7b lost
  domains.
- *Kinetic comparison of Grk7a and Grk7b on UV opsin (opn1sw1) and on a red/green opsin.*
  This would show whether the rate difference is real and substrate-specific.
- *A grk7b mutant*, ideally RNA-less, with UV-cone-isolated ERG, and a grk7a;grk7b
  double mutant.
- *Cross-rescue*: grk7b coding sequence driven by a pan-cone promoter in grk7a knockouts.

## 6. GO annotation consistency across the pair

This section summarizes `annotation-comparison.md`, regenerated after the review edits.

- **MF: rhodopsin kinase activity (IBA, IDA, IEA on both; ISS on grk7b only; ACCEPT on
  both).**
  - Symmetric and justified: the activity is retained by both copies. Both IDAs come
    from the same paper (PMID:16787417).
  - The reported rate difference is a quantitative property that GO does not capture. It
    is recorded in the review text instead.
  - The ISS on grk7b (from human GRK7) with no counterpart on grk7a is an artefact of
    which copy UniProt chose for sequence-similarity transfer. grk7a has direct evidence.
  - The IBA comes from one GRK7 node (PTN002806910) whose WITH/FROM lists both zebrafish
    paralogs, so PANTHER treats the pair as equivalent. That is correct for the MF.
- **MF: broad kinase terms and ATP binding (IEA, both).** Same actions on both (MODIFY
  to GO:0050254; ATP binding non-core). Consistent.
- **MF: photoreceptor activity (IMP, grk7a only; REMOVE).**
  - This is an asymmetry of study, not of biology: ZFIN typed the Rinner 2005 knockdown
    as an MF.
  - The term (absorbing light) does not describe a kinase. It should not be propagated
    to grk7b, and it has been removed from grk7a.
- **BP: photoresponse recovery (GO:0036368; IMP ×2), phototransduction, visible light
  (IMP), visual perception (IMP): grk7a only.**
  - These asymmetries are justified by the evidence: all genetic data are for grk7a.
    Larval ERG and behavior depend on grk7a, since grk7b protein is not detectable in
    larvae (PMID:30372740).
  - These terms should **not** be copied to grk7b by ISO or ISS. grk7b has no retinal
    loss-of-function data, and its single knockdown has no pineal effect.
  - A photoresponse recovery role for grk7b in UV cones is plausible but untested.
- **BP: G protein-coupled opsin signaling pathway (GO:0016056; NEW, grk7b only).**
  - This was proposed in the earlier grk7b review and was left as is. It rests on the
    shared in vitro activity plus UV-cone expression. PMID:34462505 has now been added
    as a primary source for the UV-cone expression.
  - grk7a's equivalent process coverage comes through its GOA terms (phototransduction
    and photoresponse recovery), so the pair differs in *which* term is used more than
    in *what* is claimed. Harmonizing on GO:0036368 for both would need grk7b-specific
    functional evidence, which does not exist yet.
- **BP: regulation of signal transduction (IBA, both; ACCEPT) and signal transduction
  (IEA, both; non-core).** Consistent.
- **CC: membrane (IEA and ISS on both) and cytoplasm (IBA on both).** Consistent.
- **CC: cone photoreceptor outer segment (GO:0120199; NEW, grk7a only).**
  - Proposed from the Wada 2006 immunolocalization of GRK7-1 (PMID:16787417) and
    supported by the knockout control (PMID:30372740).
  - It is not added to grk7b. No paralog-resolved localization of Grk7b protein exists,
    and the only immunostaining report for it (PMID:33385424, abstract only) cannot be
    checked for antibody specificity.
- **Missing, and appropriately so:** there is no annotation to a UV-cone-specific
  process or location for grk7b. GO has no cone-subtype outer-segment terms, and the
  expression partition is not itself a GO-annotatable function.
- **IBA treatment overall.** Both copies descend from the same GRK7 node and receive
  identical IBA sets. This is correct for this pair, because the molecular function is
  conserved and none of the IBA terms needs to be copy-specific.

**Edits made in this pair review** (see the history records under
`history/genes/DANRE/grk7a/` and `history/genes/DANRE/grk7b/`):

- **grk7a.** New full review. The IMP "photoreceptor activity" is set to REMOVE. A NEW
  annotation to cone photoreceptor outer segment is added.
- **grk7b.** Targeted edits only:
  - Added primary references PMID:34462505 (UV-cone enrichment) and PMID:33579376
    (the >30-fold lower rate; pineal knockdown), which had been cited only through the
    falcon report.
  - Added the rate caveat to the IDA rhodopsin kinase activity row.
  - Extended the description with the paralog context.
  - Corrected the UniProt FUNCTION quote, which had been paraphrased ("shutoff of the
    phototransduction cascade"), to the verbatim current text.

## 7. Open questions

1. Is grk7b a slower kinase on its native substrate? The >30-fold figure comes from
   rhodopsin assays reported secondhand (PMID:33579376). Kinetics on UV opsin are needed.
2. What was the cone-subtype pattern of the single pre-duplication GRK7 (gar)? Did the
   medaka copies partition in the same way? The answer decides between loss in grk7b and
   gain in grk7a.
3. Is Grk7b protein present in double cones (PMID:33385424) or only in UV cones
   (PMID:34462505, PMID:33598728)? Answering this needs a paralog-specific antibody
   validated on a grk7b mutant.
4. Does grk7b tune UV-cone shut-off? No UV-cone-isolated recording from a grk7b
   loss-of-function animal exists.
5. Is Grk7b phosphorylated at Ser33 by PKA, like Grk7a? The site is conserved, but the
   phospho-antibody data (PMID:36273582, PMID:18803695) are not paralog-resolved.

## References

| PMID / file | Citation | Role here |
|---|---|---|
| PMID:16039565 | Rinner et al. 2005, Neuron | grk7a morpholino; two grk7 orthologs cloned |
| PMID:16787417 | Wada et al. 2006, J Neurochem | Cloning of GRK7-1/7-2; GRK7-1 in cone outer segments; Vmax |
| PMID:18803695 | Osawa et al. 2008, J Neurochem | 73% paralog identity; Xenopus contrast; phospho-GRK7 in zebrafish cones |
| PMID:19720650 | Larhammar et al. 2009, Philos Trans R Soc B | Teleost GRK7 duplicates fit 3R |
| PMID:21299656 | Renninger et al. 2011, Eur J Neurosci | Grk7a morphant comparator (visual perception IMP) |
| PMID:21486791 | Vogalis et al. 2011, J Physiol | Ectopic GRK7 in rods |
| PMID:26246494 | Zang et al. 2015, Open Biol | grk7a acts in UV cones |
| PMID:29321241 | Lamb et al. 2018, Open Biol | Single GRK7 in jawed vertebrates; geranylgeranyl anchor |
| PMID:30372740 | Chrispell et al. 2018, IOVS | grk7a TALEN knockout; the larval Grk7 is Grk7a; Grk1b redundancy |
| PMID:33385424 | Ahrens et al. 2021, BBA (abstract) | Recoverin binding to all Grks; Grk7b in double cones |
| PMID:33579376 | Shen et al. 2021, Zoological Lett | Pineal knockdowns; secondary report of the GRK7-2 rate |
| PMID:33598728 | Zang & Neuhauss 2021, Pflugers Arch (review) | Summary: grk7a in all cones, grk7b in UV cones |
| PMID:34462505 | Ogawa & Corbo 2021, Sci Rep | Adult scRNA-seq: grk7b UV, grk7a other cones; TGD origin |
| PMID:34550876 | Zang et al. 2021, eLife | Circadian co-oscillation |
| PMID:36273582 | Chrispell et al. 2022, J Biol Chem | Grk7a mediates the cAMP effect; PKA Ser33 |
| PMID:39531499 | Volkov et al. 2024, PNAS | grk7b in the UV-cone gene program |
| PMID:39925416 | Shen et al. 2025, iScience | grk7b backup in multiple knockdowns |
| PMID:35253876, PMID:30944477 | Background (see the project background page) | Caution on subfunctionalization; RNA-less alleles |
| `annotation-comparison.md` | `compare_pair.py` | Protein identity; GO annotation table |
