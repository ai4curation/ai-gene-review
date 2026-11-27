---
title: "tp53bp2a / tp53bp2b"
autolink_gene_symbols: false
---

# tp53bp2a / tp53bp2b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. The only functional study treated the two ASPP2 copies side by side and
found them to act the same way: both bind Irs-1, dampen Akt signaling and restrain embryonic growth.
Both keep the p53-binding ankyrin-SH3 module almost unchanged, although the proteins are only 61%
identical overall. Both are broadly expressed in adults, like the single gar gene. The one clear
difference is in timing: tp53bp2a is the main copy from gastrulation to larva, while tp53bp2b drops
close to background during that period. All functional data come from morpholinos and
overexpression. There are no mutants, no double knockdown that can be read from the abstract, and
no cross-rescue, so backup, dosage and a timing partition cannot be told apart.

**Sample record:** fate=UNRESOLVED; level=expression; evidence=experimental_both; identity=60.9%

| | tp53bp2a | tp53bp2b |
|---|---|---|
| UniProt | F1R419 (TrEMBL; RefSeq isoform X1, 1060 aa) | F1QWN1 (TrEMBL; RefSeq isoform X1, 1063 aa) |
| Human ortholog | TP53BP2 (ASPP2) | TP53BP2 (ASPP2) |
| Chromosome | 13 | 22 |
| ZFIN | ZDB-GENE-040516-8 | ZDB-GENE-050208-453 |
| Ensembl | ENSDARG00000009136 | ENSDARG00000054858 |
| Review | [genes/DANRE/tp53bp2a](../../../../genes/DANRE/tp53bp2a/tp53bp2a-ai-review.yaml) | [genes/DANRE/tp53bp2b](../../../../genes/DANRE/tp53bp2b/tp53bp2b-ai-review.yaml) |

This pair was drawn at random (batch 4, draw 29, seed 20260928) from the PANTHER `TGD_tree` 1:1
pairs and accepted because Ensembl Compara places the duplication at a teleost node
(`random_sample.tsv`, compara_level Osteoglossocephalai).

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR24131 (APOPTOSIS-STIMULATING OF P53 PROTEIN) | TP53BP2(LDO) / TP53BP2(O) | 1 (same gar gene for both) | 2 | (blank) |

PANTHER places the duplication after the split from gar and before the zebrafish-medaka split, with
one gar co-ortholog and two medaka copies.

**Ensembl Compara** places the tp53bp2a/tp53bp2b duplication at Osteoglossocephalai, a teleost node,
gives the gar gene (ENSLOCG00000015726) as a one-to-many orthologue of both, and gives each copy its
own one-to-one medaka orthologue (recorded in the gene notes). By my alignments each zebrafish copy
is closer to its own medaka orthologue (61.9% and 61.6%) than to the other medaka copy (53.5% and
57.3%) ([RESULTS.md](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/RESULTS.md)).

**Synteny (my check).**
([RESULTS.md](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/RESULTS.md), Synteny;
[gar_bridge_output.txt](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/gar_bridge_output.txt))

- *Direct comparison:* no paralogous neighbours shared by the two copies within 1.5 Mb (chr13 and
  chr22). The only chromosome-level hit that is not one expanded gene family is efemp1 near
  tp53bp2a, whose teleost-level paralogue is on chr22, 6 Mb from tp53bp2b.
- *Gar bridge:* gar TP53BP2 is on LG16. Orthologues of its neighbours sit near both copies, but
  different ones: polh, xpo5 and a GTPBP2 orthologue near tp53bp2a; sde2, mrps28 and four calpain
  genes about 2.4 Mb from tp53bp2b. chr13 and chr22 are two of the four zebrafish chromosomes
  that carry most orthologues of gar neighbours (with chr11 and chr17).
- No gar neighbour has been kept in duplicate beside both copies.

This is consistent with double conserved synteny, but weak.

**Literature.** No paper analyses the origin of the pair.

**Status.** A teleost-level duplication is supported by two independent gene-tree methods (PANTHER
and Compara), by the medaka orthology pattern, and weakly by the gar bridge. TGD origin is likely;
the synteny evidence alone would not establish it.

## 2. Protein-level comparison

- **Identity.** 60.9% identity and 72.9% similarity over 1100 columns
  ([annotation-comparison.md](annotation-comparison.md)). Each copy is about 60% identical to human
  TP53BP2 and 59-63% to gar.
- **Domains.** Both keep the full domain order of ASPP2: an N-terminal Ras-associating
  (ubiquitin-like) domain, a coiled coil, a long proline-rich middle region, four ankyrin repeats
  and an SH3 domain. The four ankyrin repeats are 90.6-100% identical to human TP53BP2 in both
  copies, and Trp1098 (needed for APC2 binding in human ASPP2) is kept in both. The differences
  between the copies lie mostly in the disordered middle region
  ([RESULTS.md](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/RESULTS.md)).
- **Rate.** Against gar, 115 changes are unique to tp53bp2a and 124 to tp53bp2b (not significant).
- **The ancestral p53 interface is kept.** In human ASPP2 the ankyrin repeats and SH3 domain are
  the p53-binding module:
  [PMID:8875926 "The crystal structure of the p53 core domain bound to the 53BP2 protein, which contains an SH3 (Src homology 3) domain and four ankyrin repeats, revealed that (i) the SH3 domain binds the L3 loop of p53 in a manner distinct from that of previously characterized SH3-polyproline peptide complexes, and (ii) an ankyrin repeat, which forms an L-shaped structure consisting of a beta hairpin and two alpha helices, binds the L2 loop of p53."]
  No one has tested whether either zebrafish protein binds Tp53.
- **Side-by-side functional test.** Both proteins bind Irs-1 and need the same domains for their
  growth effect:
  [PMID:24362258 "Zebrafish Aspp2a and Aspp2b physically bound with Irs-1, and the growth inhibitory effects of ASPP2/Aspp2 depend on the presence of their ankyrin repeats and SH3 domains."]
  Human ASPP2 behaves the same way in fish, which suggests the ancestral protein had this activity:
  [PMID:24362258 "Human ASPP2 had similar effects on body growth in zebrafish embryos."]

**Does each copy keep the ancestral molecular function?** As far as it has been tested, yes: both
keep the Irs-1/Akt activity, and both keep the ankyrin-SH3 module that binds p53 in mammals.
The cached source is an abstract, so I cannot compare the strength of the two proteins' effects.

## 3. Expression

- **Development (E-ERAD-475, whole embryo).** Both copies are present in the zygote (26 and 15 TPM),
  so both are maternally provided. From gastrulation on, tp53bp2a dominates: 91 versus 4 TPM at 50%
  epiboly and 39-75 versus 5-9 TPM through segmentation and pharyngula. tp53bp2b rises again to
  11-15 TPM in larvae
  ([RESULTS.md](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/RESULTS.md)).
- **Adult tissues (Bgee).** Both copies are called in almost the same set of organs (19 shared
  entities); tp53bp2a scores higher in 16 of them. The only calls for one copy alone are eye and
  liver (tp53bp2a) and tail (tp53bp2b). tp53bp2b's highest score is in retina.
- **ZFIN.** The two copies carry the same set of curated annotations from the growth paper: RT-PCR
  in ten adult organs and through development, and whole-organism in situ hybridization with no
  restricted domain recorded
  ([output.txt](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/output.txt), section 6).
- **Pre-duplication state.** Gar TP53BP2 has Bgee calls in 14 adult tissues, embryo and larva, from
  ovary and skin to brain and bone. Broad expression is therefore ancestral, and both copies keep
  it. No gar developmental time course was available, so the gastrula-to-pharyngula drop in
  tp53bp2b cannot be compared with the ancestor.

There is no copy-specific tissue. The difference is quantitative and mostly temporal.

## 4. Experimental evidence of function

**Alleles.** No mutant exists for either copy in the papers found. All knockdown data are from
morpholinos.

**Both copies (PMID:24362258, abstract only)**

- Growth without a change in developmental rate:
  [PMID:24362258 "Here, we show that zebrafish Aspp2a and Aspp2b negatively regulate embryonic growth without affecting developmental rate."]
- Akt signaling, with epistasis:
  [PMID:24362258 "Aspp2a and 2b inhibit Akt signaling. This inhibition was reversed by coinjection of myr-Akt1, a constitutively active form of Akt1."]
- ZFIN/GOA carry IMP annotations for each copy from this paper, which suggests each knockdown was
  scored on its own. I cannot see from the abstract whether single knockdowns gave the same effect
  as a double knockdown, or whether the paralog was upregulated.

**tp53bp2b only (PMID:25139857)**

- tp53bp2b was one of 50 Foxj1-induced genes chosen at random for a morpholino and GFP-fusion
  screen. Its per-gene results are in a supplementary table that is not in the cache; GOA records
  an IMP "cilium movement" and an IDA "cytoplasm" from it. The screen's general conclusion about
  such genes is:
  [PMID:25139857 "Therefore, it is likely that most of the FIGs encode novel membrane, cytoplasmic or nuclear regulators of cilia formation and function."]
  No ciliary role is known for ASPP2 elsewhere, tp53bp2a was not tested, and the result rests on
  one morpholino. I left the cilium row UNDECIDED.

**Compensation.** Not tested. With morpholinos only, transcriptional adaptation is not an issue,
but off-target effects are.

## 5. Fate classification

**UNRESOLVED; the observed difference is at the level of expression (timing). Confidence in any
fate: low.**

**Established (with the caveats above)**

- Both proteins keep the conserved ankyrin-SH3 module, and in the one side-by-side assay both show
  the same activity (Irs-1 binding, Akt inhibition, growth restraint).
- Both are broadly expressed in adults, like gar TP53BP2.
- tp53bp2a carries most of the expression between gastrulation and the larval stages.

**Not established**

- Whether knocking down either copy alone is enough to change growth, which would argue for
  DOSAGE rather than BACKUP.
- Whether the tp53bp2b dip during gastrulation and organogenesis is a partition of an ancestral
  pattern (no gar time course) or simply a lower-expressed copy.
- Whether the copies differ in p53-dependent apoptosis, the ancestral ASPP function; neither has
  been tested.
- Whether the tp53bp2b cilium phenotype is real and copy-specific (that would be INNOVATION or a
  partition of an unknown ancestral role).

**Why not a firm call**

- *PARTITION:* the only difference is quantitative timing; no tissue belongs to one copy only.
- *BACKUP / DOSAGE:* same activity in assays, but no stable mutant, no double mutant and no
  cross-rescue to show either redundancy or additive dose.
- *INNOVATION:* 61% overall identity reflects divergence in disordered regions; no new function is
  shown, except the unconfirmed cilium morphant row.

**What would change the call**

- Stable single and double mutants (with promoter-less alleles, to avoid transcriptional
  adaptation) scored for growth and Akt activity: an additive effect would support DOSAGE, a
  double-only effect BACKUP.
- A gar developmental time course: if gar TP53BP2 is steady through gastrulation, the tp53bp2b dip
  is a derived loss and the pair drifts toward a temporal PARTITION.
- A p53-dependent apoptosis assay for each copy, to see whether the ancestral function is kept
  in both.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** Every IBA and IEA row (p53 binding, intrinsic p53 apoptotic pathway,
adherens junction, nucleus, perinuclear cytoplasm, regulation of apoptosis) is on both copies and
was reviewed the same way on both. The IBA node is appropriate: both copies keep the p53-binding
module and nothing points to loss in either. Both copies also carry the two IMP rows from the
growth paper, which studied them together.

**Changes I made on both copies.** The IMP "chordate embryonic development" was modified to
negative regulation of multicellular organism growth (GO:0040015), because the paper reports a
growth effect and explicitly no change in developmental timing. The IEA "signal transduction" was
modified to the more specific PI3K/AKT term already carried by IMP. Insulin receptor substrate
binding (GO:0043560, IPI) was added as NEW to both, from the Irs-1 binding result.

**Asymmetries that come from which copy was studied.** cilium movement (IMP, UNDECIDED) and
cytoplasm (IDA, accepted) exist only on tp53bp2b because only tp53bp2b was in the Foxj1 screen.
The cytoplasm location almost certainly applies to both copies; the cilium row cannot be judged
without the supplementary data.

**Should be copy-specific:** nothing, on present evidence.
**Should be shared:** all current rows except the unconfirmed cilium row.

## 7. Open questions

- Do single stable mutants of either copy change body growth, or only the double mutant?
- Does either Aspp2 copy bind Tp53 and enhance p53-dependent apoptosis in zebrafish?
- Is the tp53bp2b cilium motility phenotype reproducible in a mutant?
- What does gar TP53BP2 expression look like through gastrulation and organogenesis?

## References

PMID:8875926, PMID:24362258, PMID:25139857. Also `panther_tgd_pairs.tsv`, `random_sample.tsv`,
[annotation-comparison.md](annotation-comparison.md),
[tp53bp2a-bioinformatics/RESULTS.md](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/RESULTS.md),
[output.txt](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/output.txt) and
[gar_bridge_output.txt](../../../../genes/DANRE/tp53bp2a/tp53bp2a-bioinformatics/gar_bridge_output.txt).
