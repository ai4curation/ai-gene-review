---
title: "exoc3l2a / exoc3l2b"
autolink_gene_symbols: false
---

# exoc3l2a / exoc3l2b

[Back to pairs](../README.md)

**Bottom line:** UNRESOLVED. Both genes are co-orthologs of EXOC3L2, not of EXOC3L4 as the PANTHER table says.
Double conserved synteny with gar supports origin in the teleost duplication. The proteins have diverged a
good deal: they are 50.9% identical, and exoc3l2a has changed about twice as fast as exoc3l2b. Both
keep a full Sec6 domain. There are hints of an expression split. exoc3l2a is endothelial at 24 hpf. A 2010 probe that
ZFIN assigns to exoc3l2b ("sec6") marks premigratory neural crest, and mouse Exoc3l2 is expressed in both tissues. But
the two copies have never been compared in one experiment, adult bulk RNA-seq shows both in largely the same
tissues, and neither copy has any functional data.

**Sample record:** fate=UNRESOLVED; level=both; evidence=expression_only; identity=50.9%

| | exoc3l2a | exoc3l2b |
|---|---|---|
| UniProt | A0A8N7TEH3 (TrEMBL; RefSeq, 932 aa) | A0A8M9Q5H9 (TrEMBL; RefSeq isoform X1, 917 aa) |
| Human ortholog | EXOC3L2 (PANTHER table: EXOC3L4) | EXOC3L2 (PANTHER table: EXOC3L4) |
| Chromosome | 5 | 15 |
| ZFIN | ZDB-GENE-060526-343 | ZDB-GENE-100728-5 |
| Ensembl | ENSDARG00000008414 | ENSDARG00000030782 |
| Review | [genes/DANRE/exoc3l2a](../../../../genes/DANRE/exoc3l2a/exoc3l2a-ai-review.yaml) | [genes/DANRE/exoc3l2b](../../../../genes/DANRE/exoc3l2b/exoc3l2b-ai-review.yaml) |

This pair was drawn at random (draw 4, seed 20260928) from the PANTHER `TGD_tree` 1:1 pairs, and accepted after
Ensembl Compara placed the duplication at a teleost node (`random_sample.tsv`). It was first skipped because of a
lookup bug, since fixed.

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR21292 (EXOCYST COMPLEX COMPONENT SEC6-RELATED) | EXOC3L4(O) / EXOC3L4(O) | 1 (same gar gene for both) | 2 | (blank) |

The PANTHER accession for exoc3l2b in that row, A0A8M3B147, is now inactive in UniProt ("Deleted from sequence
source (RefSeq)"). The review uses the current entry A0A8M9Q5H9 (see
[exoc3l2b-notes.md](../../../../genes/DANRE/exoc3l2b/exoc3l2b-notes.md)).

**Ensembl Compara** (`random_sample.tsv`, and my script): the duplication is at the Osteoglossocephalai node.
There is one gar ortholog (ENSLOCG00000014731, LG2) for both copies, one medaka one-to-one ortholog for each, and
human EXOC3L2 is a one-to-many ortholog
([RESULTS.md](../../../../genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md)).

**Synteny (my check).** Paralogous genes sit right next to both copies: ppp1r14aa is 0.02 Mb from exoc3l2a and its
paralogue ppp1r14ab 0.01 Mb from exoc3l2b; dlb is 0.06 Mb from exoc3l2a and dlc 0.27 Mb from exoc3l2b. Both
neighbourhoods map to the region around the single gar gene: 13 exoc3l2a neighbours and 5 exoc3l2b neighbours have
their gar orthologue within 5 Mb of it, among them mark4 and ckm (exoc3l2a side) and spint2 (exoc3l2b side). Three
exoc3l2a neighbours (MARK4, KPTN, SLC8A2) have human orthologues within 5 Mb of EXOC3L2 at 19q13.32
([RESULTS.md](../../../../genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md)). This is double conserved synteny.

**Literature.** I found no paper on the origin of this pair; `exoc3l2a OR exoc3l2b` returns four papers in Europe
PMC, none about the duplication.

**Status.** TGD origin is well supported: a PANTHER `TGD_tree` call, a Compara teleost-level node with one gar
ortholog, and double conserved synteny against gar.

## 2. Protein-level comparison

**Which ortholog?** PANTHER lists EXOC3L4 for both copies, and its HMM puts them in subfamilies named after TNFAIP2
(SF18, SF17). Human EXOC3L2 is in SF7. Sequence does not support that placement. Each copy is 35-36% identical to
human EXOC3L2 and 19.7-21.9% to EXOC3, EXOC3L1, EXOC3L4 and TNFAIP2. Zebrafish also has its own exoc3l4, tnfaip2a,
tnfaip2b and exoc3l1 genes, each only about 17-22% identical to either copy. Gar and medaka orthologs show the same
pattern, and the exoc3l2a neighbourhood maps to the EXOC3L2 region of human chromosome 19, not to EXOC3L4 or TNFAIP2
on chromosome 14 ([RESULTS.md](../../../../genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md)). ZFIN's
names are right; the PANTHER orthology call is not. Mouse work lists these paralogs as separate vertebrate genes:
[PMID:36362885 "Notably, Exoc3 has four homologous genes, called Exoc3-like 1 (Exoc3l1), Exoc3-like 2 (Exoc3l2), Exoc2-like 3 (Exoc3l3, also called tumor necrosis factor, alpha-induced protein 2, Tnfaip2) and Exoc3-like 4 (Exoc3l4) in vertebrates."]

**Identity.** 50.9% identity, 63.6% similarity over 992 columns
([annotation-comparison.md](annotation-comparison.md)). The whole EXOC3L2 lineage evolves fast: neither copy nor gar is more than 39% identical to human EXOC3L2.

**Domains.** Both copies keep a full-length Sec6 domain (human EXOC3L2 residues 270-719: 43.1% and 44.4% identical)
and the N-terminal region (43.5% and 43.1%). Neither copy is truncated
([RESULTS.md](../../../../genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md)).

**Rate asymmetry.** With gar as outgroup, 138 aligned positions changed only in exoc3l2a and 71 only in exoc3l2b
(chi2 = 21.5, P < 0.05). exoc3l2b is closer to gar (56.2% vs 47.5% identity). exoc3l2a is the faster-evolving copy.
This fits relaxed constraint or adaptive change in exoc3l2a, but does not show a change in function.

**Biochemistry.** None for either zebrafish protein. For human EXOC3L2:
[PMID:21566143 "Myc-tagged EXOC3L2 co-precipitates with the exocyst protein EXOC4, and immunofluorescence detection of EXOC3L2 shows partial subcellular colocalization with EXOC4 and EXOC7."]
Whether EXOC3L2 replaces EXOC3 in the complex or acts separately is open:
[PMID:30086153 "Therefore, it will be relevant to determine whether EXOC3 paralogs, particularly M-Sec and EXOC3L2, are interchangeable subunits that are selectively assembled into different functional variants of the exocyst complex, or independent operators."]

**Does each copy keep the ancestral molecular function?** Probably. Both keep the domains of the family, but no
activity has been measured for either, and the ancestral molecular function of EXOC3L2 is itself not established.

## 3. Expression

**exoc3l2a: endothelium.** An endothelial TRAP-seq screen found exoc3l2a enriched, and whole-mount in situ
hybridization confirmed it:
[PMID:40613926 "In situ hybridization for three of these genes– exoc3l2a, slc22a7b.1, and bpifc–, confirmed their endothelial-specific expression pattern"]
[PMID:40613926 "Whole mount in situ hybridization of 24 hpf wild type zebrafish probed for exoc312a"] (the legend's
spelling). It is also part of the endothelial signature of the caudal hematopoietic tissue niche:
[PMID:37119815 "There are numerous genes identified by this study that were not previously associated with the HSPC niche, including several with activities related to endocytosis and membrane trafficking: ap1b1, dab2, pxk, exoc3l2a and snx8."]

**exoc3l2b: neural crest, dorsal hindbrain, pharyngeal arches.** The only curated in situ data come from a study of
Ovo1 that calls the gene "sec6". ZFIN assigns these data to exoc3l2b (ZDB-PUB-100518-8; RESULTS.md, section 6).
[PMID:20463035 "Surprisingly, we found that rab3c, rab12, rab11fip2 and sec6 were all highly enriched in premigratory NC cells at 12 hpf, the same stage at which we performed the microarray and first detected the Ovo1 morphant phenotype ( Fig. 5B-E )."]
[PMID:20463035 "At earlier stages, expression of all four genes was ubiquitous throughout the embryo but later became enriched in the NC at 12 hpf and in the dorsal hindbrain and pharyngeal arches at 24-72 hpf (data not shown)."]
The later-stage pattern was not shown. I have not seen the probe sequence, so I cannot confirm it is specific to
exoc3l2b rather than exoc3 or exoc3l2a.

**Neither study looked at the other copy.** No published in situ exists for exoc3l2b in endothelium or for exoc3l2a
in neural crest.

**Bulk data.** In the whole-embryo time course (E-ERAD-475) both copies are near zero through gastrulation, turn on
during segmentation and pharyngula, and reach 7-13 TPM by 3-5 days. exoc3l2a starts slightly earlier. In Bgee, 14 of
the 16 exoc3l2a and 17 exoc3l2b tissue calls are shared (intestine, gill, kidney, heart, liver, skin, bone, muscle,
granulocytes and others). exoc3l2a alone has swim bladder (its top score) and early embryo; exoc3l2b alone has
mesonephros, spleen and ovary. Gar exoc3l2 is called in a similar broad set of tissues. None of this is cell-type
resolved ([RESULTS.md](../../../../genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md)).

**Pre-duplication state.** Mouse Exoc3l2 is expressed in both of the tissues the zebrafish copies are reported in:
[PMID:21566143 "The brain sections were stained for EXOC3l2 together with PECAM and expression of EXOC3l2 was detected in endothelial cells, particularly in the larger vessels"]
[PMID:36362885 "GFP expression was also observed in non-endothelial cells, which are most likely cranial neural crest cells (Figure 1c)."]
If endothelium plus cranial neural crest is the ancestral pattern, the zebrafish reports fit a split of those two
domains between the copies. No cell-resolved gar data exist to test this, and the zebrafish evidence is two
single-copy studies, one of them with a probe I cannot check.

## 4. Experimental evidence of function

**Zebrafish:** none for either copy. No mutant, morphant or overexpression study of exoc3l2a or exoc3l2b has been
published. In the Ovo1 study, "sec6" (exoc3l2b per ZFIN) was only measured as a target gene, up-regulated in Ovo1
morphants and after blocking Wnt/Tcf:
[PMID:20463035 "Interestingly, we also found significant upregulation of rab3c, rab11fip2 and sec6 in embryos overexpressing the dnTcf3 transgene when compared with wild-type controls ( Fig. 5F )."]
Its function was not tested.

**Mammalian single-copy ortholog (context).**

- Human endothelial cells: [PMID:21566143 "Finally, we show that exoc3l2 silencing inhibits VEGF receptor 2 phosphorylation and VEGFA-directed migration of cultured endothelial cells."]
- Mouse knockout: [PMID:36362885 "Most of the Exoc3l2 KO embryos died in utero and showed hemorrhage, abnormal heart and brain development."]
  Deletion in the endothelial and hematopoietic lineages reproduces this:
  [PMID:36362885 "Conditional KO animals lacking Exoc3l2 in hematopoietic and endothelial lineages showed similar phenotypes, such as hemorrhage and heart defects, indicating that Exoc3l2 in hematopoietic and endothelial lineages is responsible for normal cardiovascular development."]
  It is not needed for postnatal retinal angiogenesis:
  [PMID:36362885 "Inducible KO in endothelial cells during postnatal retinal development resulted in normal angiogenesis in the retina, indicating that Exoc3l2 is dispensable for postnatal angiogenesis in the retina."]
- Human patients: [PMID:30327448 "We propose that biallelic EXOC3L2 mutations lead to a novel syndrome that affects hindbrain development, kidney and possibly the bone marrow."]

These show what the ancestral gene did in mammals, not how the work is divided between the zebrafish copies.

## 5. Fate classification

**UNRESOLVED. Level of the candidate divergence: both (expression and protein). Evidence: expression only. Confidence
that some divergence exists: moderate. Confidence in any particular fate: low.**

**Established**

- TGD origin (PANTHER, Compara, double conserved synteny).
- Both copies are EXOC3L2 orthologs with an intact Sec6 domain.
- The proteins are only 50.9% identical, and exoc3l2a evolves significantly faster than exoc3l2b.
- exoc3l2a is expressed in endothelium at 24 hpf.

**Suggestive, not shown**

- An expression split, with exoc3l2a in endothelium and exoc3l2b in neural crest. Each half comes from a different
  study that looked at one gene. The exoc3l2b half rests on a 2010 probe named "sec6", and its later-stage pattern
  was "data not shown". Mouse Exoc3l2 is expressed in both tissues, so this split would be a PARTITION.
- Protein-level change in exoc3l2a, from the rate asymmetry. Faster evolution can mean relaxed constraint, which is
  common after a split, or new function. Sequence alone cannot tell these apart.

**Why not the other fates**

- *BACKUP or DOSAGE:* cannot be tested without mutants. The broad adult co-expression in Bgee would fit it, but
  bulk tissue calls cannot separate cell types.
- *INNOVATION:* no function has been measured for either protein.

**What would settle it**

- Two-colour HCR for both copies with kdrl (endothelium) and sox10 (neural crest) at 12-48 hpf. If exoc3l2b is
  absent from endothelium and exoc3l2a from neural crest, the call would be PARTITION at the expression level.
- Single and double mutants, including RNA-less alleles to avoid transcriptional adaptation, scored for hemorrhage,
  vascular patterning, CHT hematopoiesis and craniofacial or neural-crest defects.
- Cross-rescue: express Exoc3l2b in exoc3l2a-mutant endothelium, to test whether the faster-evolving copy has
  changed function.
- Cell-resolved gar data (endothelium vs neural crest) to fix the ancestral pattern.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** Exocyst (GO:0000145) is on both copies (IBA and IEA on exoc3l2a, IEA on exoc3l2b) and
was accepted on both. The evidence is association of mammalian EXOC3L2 with EXOC4, not proof that it is a
stoichiometric subunit. Exocytosis (GO:0006887) is on both and was kept as non-core on both: it is plausible for an
exocyst-associated protein, but no exocytosis assay exists for EXOC3L2 in any species.

**Asymmetric only because of an accession artefact.** exoc3l2a has three IBA rows from the EXOC3/Sec6 family node
PTN000480155, and exoc3l2b has none. The difference is not biological. The PANTHER tree holds exoc3l2b under
A0A8M3B147, a UniProt entry that has since been deleted, so the IBAs did not carry over to the current entry.

**Questionable on the copy that has it.** SNARE binding (GO:0000149, IBA) on exoc3l2a rests only on yeast Sec6. The
EXOC3L2 lineage is only about 20% identical to EXOC3/Sec6, and no EXOC3-like paralog has been tested for SNARE
binding. It was marked as over-annotated, with a propagation_review (root cause UNRESOLVED).

**A PANTHER problem that affects the pair.** Human EXOC3L2 has no IBA rows from PTN000480155, while human EXOC3,
EXOC3L1, EXOC3L4 and TNFAIP2 do (QuickGO, 2026-09-28; noted in
[exoc3l2a-notes.md](../../../../genes/DANRE/exoc3l2a/exoc3l2a-notes.md)). The zebrafish copies sit beside the paralogs
in PANTHER, not beside EXOC3L2. That matches the EXOC3L4 orthology call, which sequence and synteny contradict.

**Missing from both.** Nothing that the evidence supports. An endothelial or vascular process term would need
zebrafish loss-of-function data. The mouse knockout shows the gene is needed, which is not the same as doing some
of the work, and it cannot say which zebrafish copy carries the role.

**Should be copy-specific, if the expression split holds:** vascular and endothelial roles (exoc3l2a) and
neural-crest roles (exoc3l2b). **Should be shared:** exocyst association and any molecular function.

## 7. Open questions

- Are the two copies expressed in complementary cell types (endothelium versus neural crest), or do they overlap?
  No experiment has probed both at once.
- Is the "sec6" probe of PMID:20463035 specific to exoc3l2b?
- Does the faster evolution of exoc3l2a reflect relaxed constraint or a new function?
- Do zebrafish exoc3l2 mutants show the hemorrhage and cardiovascular defects of mouse Exoc3l2 knockouts, and in
  which copy?
- Should PANTHER's PTHR21292 tree be revised, given that it places the zebrafish EXOC3L2 co-orthologs with EXOC3L4
  and TNFAIP2?

## References

PMID:20463035, PMID:21566143, PMID:30086153, PMID:30327448, PMID:36362885, PMID:37119815, PMID:40613926. Also
`panther_tgd_pairs.tsv`, `random_sample.tsv`, [annotation-comparison.md](annotation-comparison.md),
[exoc3l2a-bioinformatics/RESULTS.md](../../../../genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md) and
[output.txt](../../../../genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/output.txt).
