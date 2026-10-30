---
title: "ctdspl2a / ctdspl2b"
autolink_gene_symbols: false
---

# ctdspl2a / ctdspl2b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED; the data fit BACKUP or DOSAGE, but no function has been tested. These are the two copies of
the nuclear HAD phosphatase CTDSPL2 (SCP4). Both keep the catalytic DxDx(T/V) motif (DLDET) and a phosphatase domain at
least 96% identical to the human one. Both are maternally loaded and expressed in every tissue and stage sampled, as
gar CTDSPL2 is. ctdspl2a is expressed at two to three times the level of ctdspl2b. The copies differ mainly in the
N-terminal regulatory region, and no zebrafish experiment exists for either.

**Sample record:** fate=UNRESOLVED; level=none; evidence=expression_only; identity=70.9%

| | ctdspl2a | ctdspl2b |
|---|---|---|
| UniProt | Q08BB5 (Swiss-Prot CTL2A_DANRE, 469 aa) | A4QNX6 (Swiss-Prot CTL2B_DANRE, 460 aa) |
| Human ortholog | CTDSPL2 (SCP4) | CTDSPL2 (SCP4) |
| Chromosome | 25 | 7 |
| ZFIN | ZDB-GENE-061013-647 | ZDB-GENE-030131-1809 |
| Mutant alleles | none characterized | none characterized |
| Review | [genes/DANRE/ctdspl2a](../../../../genes/DANRE/ctdspl2a/ctdspl2a-ai-review.yaml) | [genes/DANRE/ctdspl2b](../../../../genes/DANRE/ctdspl2b/ctdspl2b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR12210 (DULLARD PROTEIN PHOSPHATASE) | CTDSPL2(O) / CTDSPL2(LDO) | 1 (same gar gene for both) | 2 | (blank) |

PANTHER places the duplication after the split from gar and before the zebrafish-medaka split. Both copies share one
gar co-ortholog, and there are two medaka copies.

**Ensembl Compara** (random_sample.tsv, and my script) dates the duplication to the Osteoglossocephalai node. It gives
one gar orthologue (ENSLOCG00000013760) for both copies. Medaka keeps two copies, and each is a one-to-one orthologue
of a different zebrafish copy (ENSORLG00000005035 of ctdspl2a, ENSORLG00000006288 of ctdspl2b). Both copies have been
kept in both lineages ([RESULTS.md](../../../../genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/RESULTS.md)).

**Synteny.** ctdspl2a is on chr25 and ctdspl2b on chr7. My script looked at genes within 1.5 Mb of each copy. It
found five named neighbour pairs whose members are teleost-level paralogues, one member next to each copy: eif3j,
apba2, tjp1, tln2 and isl2. The same pairs are found whichever copy the search starts from. This is double-conserved
synteny ([RESULTS.md](../../../../genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/RESULTS.md)).

**Literature.** I found no paper on the origin of this pair.

**Status.** A teleost-specific duplication is supported by two independent gene-tree methods (PANTHER and Compara), and
the orthology to the two medaka copies is one-to-one. Double-conserved synteny with five flanking ohnolog pairs adds independent support. TGD origin is well
supported.

## 2. Protein-level comparison

- **Identity.** 70.9% identity and 79.0% similarity over 477 columns
  ([annotation-comparison.md](annotation-comparison.md)). ctdspl2a is 73.2% identical to human CTDSPL2 and ctdspl2b
  69.7%; against gar the figures are 74.4% and 71.0%.
- **Phosphatase domain.** The FCP1-homology domain (human 283-442) is 97.5% (ctdspl2a) and 96.2% (ctdspl2b) identical
  to human; gar is 98.8%. Most of the difference between the copies is in the disordered N-terminal region (47-52%
  identical to human), which in the human protein carries the nuclear localization sequences:
  [PMID:35021089 "This result suggests that a function of the SCP4 N-terminal segment is to promote nuclear localization of the full-length protein."]
- **Catalytic motif (DXDX(T/V)).** Human CTDSPL2 uses two aspartates in this motif:
  [PMID:35021089 "In addition, we cloned point mutations of SCP4 that changed aspartate residues in the putative DxDx(V/T) catalytic motif to alanine."]
  [PMID:35021089 "Despite similar expression levels to the wild-type protein, SCP4D293A, SCP4D295A, and SCP4D293A/D295A mutants were unable to support MOLM-13 growth (Figures 3G and 3H)."]
  Changing D295 to N makes the enzyme phosphatase-dead:
  [PMID:42315649 "doxycycline (Dox)-inducible expression of wild-type SCP4 (SCP4-WT) in HeLa cells reduced H3pT3 levels, whereas a phosphatase-dead mutant (SCP4-DN, with a D295N substitution in the catalytic loop) had no effect"]
  - Both zebrafish copies have the same motif, DLDET: ctdspl2a at 296-300 and ctdspl2b at 287-291.
  - Each aligns exactly to human D293-L294-D295-E296-T297.
  - Gar CTDSPL2 also has DLDET
    ([RESULTS.md](../../../../genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/RESULTS.md)).
- **Rates.** With gar as the outgroup, 38 changes are unique to each copy (chi2 = 0).
- **Biochemistry.** No zebrafish protein has been assayed. Human CTDSPL2 dephosphorylates the Pol II CTD in vitro:
  [PMID:26920047 "SCP4 exhibited Ser5-preferential CTD phosphatase activity in vitro, while small interfering RNA-mediated SCP4 knockdown in HeLa cells increased phosphorylation levels of Pol II at Ser5 and Ser7, but not at Ser2."]

**Does each copy keep the ancestral molecular function?** Probably yes for both. The catalytic motif is intact and the
phosphatase domain is nearly invariant, so there is no sign of pseudoenzyme decay in either copy. Whether the
divergent N-terminal regions change nuclear targeting or substrate docking has not been tested.

## 3. Expression

Sources: my script ([RESULTS.md](../../../../genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/RESULTS.md);
[output.txt](../../../../genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/output.txt)).

- **Timing (E-ERAD-475 whole embryos).** Both copies are maternal. Both peak in cleavage and blastula stages
  (ctdspl2a 246 TPM, ctdspl2b 96 TPM), then fall to a steady level (ctdspl2a 50-60 TPM, ctdspl2b about 20 TPM).
  The two profiles have the same shape; ctdspl2a is two to three times higher at every stage.
- **Bulk tissues (Bgee).** Each copy has 27 calls, nearly all in shared tissues: early embryo, ovarian follicle,
  testis, brain, eye and retina, granulocyte, spleen, head kidney, gill, swim bladder, skin, muscle, bone, intestine
  and liver. The only one-copy RNA-seq entities are heart (ctdspl2a) and "head" (ctdspl2b); both have Affymetrix calls
  for cardiac ventricle.
- **ZFIN.** No curated in situ records exist for either copy.
- **Pre-duplication state.** Gar CTDSPL2 is called in 14 tissues, from brain and gonads to liver and gill. It is a
  broadly expressed gene, like both zebrafish copies.

No expression partition is detectable at this resolution. Cell-type or regional differences inside tissues would not
show up in these data.

## 4. Experimental evidence of function

- **Zebrafish.** No mutant, morphant, rescue or overexpression data exist for either copy.
- **Mammals (context for the shared annotations).**
  - SCP4 dephosphorylates FoxO1/3a and promotes gluconeogenesis; knockout neonates are hypoglycemic:
    [PMID:28851713 "Moreover, we demonstrated that gene ablation of SCP4 led to hypoglycemia in neonatal mice."]
  - SCP4 also acts on Smad1/5/8 in BMP signalling:
    [PMID:28506762 "We identified that SCP4 not only dephosphorylated Smad1/5, but also influenced FoxOs’ phosphorylation status."]

## 5. Fate classification

**UNRESOLVED. Level: none detected. Confidence in "no divergence detected": moderate. Confidence in any specific fate:
low.**

**Observed**

- Both copies keep an intact catalytic motif and a nearly identical phosphatase domain.
- Both are expressed broadly and in parallel, like the unduplicated gar gene, with a steady two- to three-fold dosage
  difference.
- Both copies are kept one-to-one in medaka.
- Neither copy is evolving faster.

**Consistent with**

- *BACKUP:* redundant enzymes.
- *DOSAGE:* retention because the summed dose matters. Keeping both copies in both lineages fits this.
- *PARTITION:* a subtler split at the level of cell type or substrate. The divergent N-terminal regions are the most
  likely place for this.

**Not supported**

- *INNOVATION:* no new domain, motif change or new expression domain.

**What would resolve it**

- Single and double mutants, with transcriptional adaptation checked. For example, look for BMP-dependent
  dorsoventral patterning defects, fasting glycemia and cartilage defects.
- Cross-rescue with each copy and with catalytic-dead forms.
- Paralog-resolved single-cell expression.
- A comparison of summed zebrafish expression against gar levels.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md).

- **Shared, and correctly so.** Both copies carry the same four rows, and I made the same call on each:
  - phosphoprotein phosphatase activity: IBA and IEA, accepted. The IBA node PTN000258719 includes human CTDSPL2
    among its sources. The core function is recorded as this MF.
  - phosphatase activity: IEA, accepted.
  - nucleus: IEA, accepted.
  - positive regulation of gluconeogenesis: ARBA IEA, kept as non-core. The mammalian evidence is direct (FoxO
    dephosphorylation), but it comes from one lab and has not been tested in fish.
- **Bookkeeping asymmetry.** ctdspl2a has an extra root ND cellular_component row. It was accepted as a placeholder.
- **Missing from both.** Human CTDSPL2 has experimental rows for RNA polymerase II CTD heptapeptide repeat
  phosphatase activity (IDA) and protein serine/threonine phosphatase activity (IMP). Neither has been propagated
  to the zebrafish copies. I did not add them as NEW rows, because no zebrafish protein has been assayed. Both
  would apply equally to the two copies.
- **Should be copy-specific:** nothing, on current evidence.

## 7. Open questions

- Is summed ctdspl2a + ctdspl2b expression similar to gar CTDSPL2 in matched tissues? That would be the expected
  signature of a dosage-balanced pair.
- Do the divergent N-terminal regions still carry functional nuclear localization signals in both copies? Do both
  copies bind the STK35/PDIK1L kinases, the SCP4 partners found in human leukemia cells?
- Does loss of both copies disturb early BMP-dependent patterning, which would be the most likely zebrafish phenotype?

## References

PMID:26920047, PMID:28506762, PMID:28851713, PMID:35021089, PMID:42315649. Also `panther_tgd_pairs.tsv`,
`random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[ctdspl2a-bioinformatics/RESULTS.md](../../../../genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/ctdspl2a/ctdspl2a-bioinformatics/output.txt).
