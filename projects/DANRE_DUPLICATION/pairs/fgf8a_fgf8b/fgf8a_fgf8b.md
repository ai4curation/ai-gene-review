---
title: "fgf8a / fgf8b"
autolink_gene_symbols: false
---

# fgf8a / fgf8b

[Back to pairs](../README.md)

**Bottom line:** PARTITION (subfunctionalization) at the expression level, and a lopsided one.
The two proteins look equivalent: fgf8b acts like fgf8a when injected. fgf8a kept most of the
ancestral FGF8 expression domains: the gastrula, the heart, the telencephalon, the pharyngeal
arches and the fin bud. fgf8b is expressed only in a subset of them (the midbrain-hindbrain
boundary, somites and ear), and only from mid-somitogenesis. The two copies have different sets of
conserved non-coding elements, and stickleback split the heart domain the opposite way. Both facts
fit reciprocal, lineage-specific loss of regulatory elements. In zebrafish, however, no domain
unique to fgf8b has been reported, and fgf8b has never been knocked out. Whether fgf8b does anything
that fgf8a cannot is therefore untested.

| | fgf8a | fgf8b |
|---|---|---|
| UniProt | O57341 (Swiss-Prot) | Q805B2 (Swiss-Prot) |
| Human ortholog | FGF8 | FGF8 |
| Former names | fgf8, acerebellar (ace) | fgf17, fgf17a |
| Chromosome | 13 | 1 |
| Length | 210 aa | 212 aa |
| Review | [genes/DANRE/fgf8a](../../../../genes/DANRE/fgf8a/fgf8a-ai-review.yaml) | [genes/DANRE/fgf8b](../../../../genes/DANRE/fgf8b/fgf8b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree_no_gar | Euteleostomi\|Teleostei | 1:1 | PTHR11486 (FIBROBLAST GROWTH FACTOR) | FGF8(LDO) / FGF8(O) | 0 (no gar gene in the tree) | 2 | (blank; not assessed for this call) |

PANTHER places the duplication on a branch that ends at Teleostei. Because the tree contains no gar
fgf8, it cannot show directly that the duplication came after the gar split. The two medaka
co-orthologues fit a duplication shared by teleosts.

**Naming history.** fgf8b was first described as zebrafish fgf17, and was then reassigned as an
FGF8 duplicate:

- [PMID:11091072 "In spite of a slightly higher aminoacid similarity to Fgf8, expression analysis and mapping to a chromosome stretch that is syntenic with mammalian chromosomes shows that this gene is orthologous to mammalian Fgf17."]
- [PMID:17708537 "We found that fgf17b is the ortholog of tetrapod Fgf17, whereas the teleost genes called fgf8 and fgf17a are duplicates of the tetrapod gene Fgf8, and thus should be called fgf8a and fgf8b."]

**Synteny and phylogeny (established).**

- Each copy sits in a block of genes that flank human FGF8:
  [PMID:19562753 "Orthologs of six genes surrounding human FGF8 in a 2.16 Mb region on chromosome Hsa10q (Fig. 4C) are located in a 0.4 Mb region on zebrafish chromosome Dre1 containing fgf8b (Fig 4B)."]
  [PMID:19562753 "The orthologs of a somewhat different set of human genes flanking FGF8 lie near fgf8a in zebrafish Dre13 and stickleback LG VI (Fig. 4D,E)."]
- The neighbouring genes were duplicated along with them, which points to a block duplication
  rather than a single-gene one:
  [PMID:19562753 "indicating that that these duplicated loci also originated in the R3 genome duplication"]
- Phylogeny: [PMID:17708537 "Phylogenetic analysis supports the view that the Fgf8/17/18-subfamily expanded during the ray-fin fish genome duplication."]
- Later papers state the TGD origin as settled:
  [PMID:28873404 "Although this subfamily is conserved in mammals, the fgf8 and fgf18 duplications are a result of the teleost-specific whole-genome duplication [24]."]
- Both copies are kept in several teleost lineages:
  [PMID:19562753 "the fgf8a and fgf8b paralogs have co-existed from R3 to the present in several lineages"]

(Jovelin et al. call the TGD "R3".)

**Status.** The TGD origin is established by double-conserved synteny with human and stickleback,
together with teleost-wide retention. The gar orthology bridge has not been applied to this pair in
the sources found, and PANTHER has no gar fgf8 in the tree.

## 2. Protein-level comparison

- **Identity.** 70.8% identity and 83.5% similarity over 212 alignment columns
  ([annotation-comparison.md](annotation-comparison.md)). Both proteins have a signal peptide
  (residues 1–27 in UniProt) and the FGF core domain (Pfam PF00167). fgf8b has one predicted
  N-glycosylation site (UniProt Q805B2).
- **Biochemistry.** No side-by-side receptor-binding or signalling assay of the two proteins has
  been published. The only direct comparison is a gain-of-function assay. Injected fgf8b (then
  called fgf17) acts like fgf8 at a stage when fgf8b is not normally expressed:
  [PMID:11091072 "Using an mRNA injection assay, we show that fgf17 can act similar to fgf8 during gastrulation, when fgf17 is not normally expressed."]
- **Naming caveat.** "Fgf8a" and "Fgf8b" are also the names of two splice isoforms of Fgf8, and
  zebrafish fgf8a makes both:
  [PMID:16961592 "zebrafish fgf8 encodes two splicing variants, corresponding to Fgf8a and Fgf8b"]
  Papers on the "Fgf8b isoform" are not about the fgf8b paralogue.

**Does each copy keep the ancestral molecular function?** Probably yes. The protein domains are
intact, and fgf8b behaves like fgf8a in the injection assay. That rests on one gain-of-function
experiment, not on cross-rescue of the ace mutant. The GO molecular-function terms (FGFR binding,
growth factor activity) are therefore kept on both copies.

## 3. Expression

- **Shared domains (mid-somitogenesis): MHB and somites.**
  [PMID:19562753 "At mid-segmentation stages (40 hpf stickleback and 16 hpf zebrafish) (Kimmel et al., ‘95), the expression of fgf8a and fgf8b are similar in zebrafish and stickleback (Reifers et al., ‘98, Reifers et al., ‘00a, Draper et al., ‘03, Jovelin et al., ‘07), with strong expression of both genes in both species in the midbrain-hindbrain border (MBH) and somites (Fig. 6A–H)."]
- **fgf8a-only domains.**
  - Dorsal diencephalon and tailbud:
    [PMID:19562753 "In addition, fgf8a is expressed in the dorsal diencephalon and the tailbud in both species."]
  - Telencephalon, olfactory epithelium, pharyngeal arches and the fin bud AER, at 48 hpf:
    [PMID:19562753 "new domains appear for fgf8a (but not fgf8b) in the telencephalon, olfactory epithelium, pharyngeal arches"]
    [PMID:19562753 "fgf8b is not expressed in the AER of fish pectoral appendages (Jovelin et al., ‘07)"]
  - The gastrula. fgf8a acts in dorsoventral patterning and mesendoderm formation during
    gastrulation (section 4). fgf8b is not expressed then: its first expression is at the
    8-somite stage, in the MHB and anterior somites (UniProt Q805B2, from PMID:11091072; quoted
    above, "when fgf17 is not normally expressed").
- **Heart: opposite choices in zebrafish and stickleback.**
  [PMID:19562753 "In zebrafish, fgf8a is required for the expression of cardiac genes (Reifers et al., ‘00b), but fgf8b is not expressed in the heart; conversely, in stickleback, fgf8b but not fgf8a is expressed in the heart (Jovelin et al., ‘07)."]
- **Ear: also resolved differently.**
  [PMID:19562753 "The anterior sensory patch shows strong expression of sfgf8b in stickleback and its paralog zfgf8a in zebrafish, while expressing zfgf8b only weakly (Fig. 8D, F, H)."]
- **Dependence of fgf8b on fgf8a at the MHB.** fgf8b expression at the MHB is maintained by
  fgf8a and depends on the dose of pax2a:
  [PMID:11091072 "In contrast, only maintenance of fgf17 expression is disturbed at the MHB of acerebellar/fgf8 mutants."]
  [PMID:11091072 "Analysis of zebrafish MHB mutants demonstrates a gene-dosage dependent requirement of fgf17 expression for the no isthmus// pax2.1 gene"]
- **Cis-regulation: each copy kept different ancestral elements.**
  - In teleosts, fgf8a is regulated by enhancers spread over its neighbouring genes:
    [PMID:19782672 "We conclude that fgf8a transcriptional regulation employs pan-vertebrate and teleost-specific enhancers dispersed over three genes in the zebrafish genome."]
  - The fgf8b block lost one of those neighbours, fbxw4:
    [PMID:17387144 "This block has retained NP_056263.1 and POLL , two genes that in the human genome are downstream from FGF8 , but has undergone deletion of fbxw4"]
  - Across teleosts, each paralogue has its own set of conserved non-coding elements (CNEs):
    [PMID:19562753 "fgf8a and fgf8b orthologs have unique sets of CNEs, some of which are shared with human as it would be expected if subfunctions have been partitioned among paralogs."]
  - Surprisingly, the two paralogues share few CNEs with each other:
    [PMID:19562753 "Despite their similarity in expression patterns (Fig. 8A–H, 9A–D), fgf8a shares fewer CNEs with fgf8b than it does with fgf17, fgf18a and fgf24 (Fig. 10C)."]
- **The pre-duplication state.** No gar fgf8 expression data were found. The ancestral state is
  inferred from mouse and from the other FgfD genes. The heart, MHB, somite, ear and eye domains
  are inferred to be ancestral:
  [PMID:19562753 "If the hypothesis is true that expression domains shared by all four FgfD genes were present in the last pre-R1-duplication FgfD gene, then that vertebrate ancestor would have had expression domains appropriate for eyes, ears, pharyngeal arches, somites, and MHB."]
  Olfactory epithelium expression is proposed to be a teleost gain in the fgf8 clade, and it is
  carried by fgf8a:
  [PMID:19562753 "These include segmental plate only in teleost fgf17 genes, telencephalon only in Fgf8 of teleosts and tetrapods, olfactory epithelium only in teleost fgf8 genes, and spinal neurons only in fgf18a of teleosts."]

## 4. Experimental evidence of function

**fgf8a** (about 120 GOA rows; most rest on the ace mutant or on morpholinos)

- *acerebellar* (ace ti282a). This is a splice-site mutation that shifts the reading frame and
  introduces a premature stop codon, so it could trigger NMD:
  [PMID:17448458 "For this study we used mutants that carried the ace ti282a allele, which encodes a point mutation in the splice site following exon 2, causing a frame shift and introduction of a premature stop codon ( Reifers et al., 1998 )."]
  It is described as a strong hypomorph rather than a null:
  [PMID:17239227 "acerebellarti282a, a strong hypomorphic allele of fgf8"]
  A second allele, x15, is also used [PMID:24677486 "Mutant alleles fgf3t26212 and fgf8x15"].
- MHB organizer and cerebellum:
  [PMID:9609821 "Homozygous acerebellar embryos lack a cerebellum and the midbrain-hindbrain boundary organizer."]
- Heart precursors, with rescue by RNA or bead:
  [PMID:10603341 "Cardiac gene expression is restored in acerebellar mutant embryos by injecting fgf8 RNA, or by implanting a Fgf8-coated bead into the heart primordium."]
- Gastrula dorsoventral patterning:
  [PMID:15151985 "we show that loss of Fgf8 function enhances the ventralisation of chordin-deficient embryos"]
- Left-right asymmetry and Kupffer's vesicle:
  [PMID:15932752 "We find that fgf8 is required for proper asymmetric development of the brain, heart and gut."]
- Otic induction, shared with fgf3:
  [PMID:17522161 "fgf8 mutants depleted of RA signaling produce few otic cells, and these cells fail to form a vesicle, indicating that Fgf8 is the primary factor responsible for otic induction in RA-depleted embryos"]
- Several phenotypes are mild in single mutants and appear only with fgf3 loss (the fgf3 gene
  is from an older duplication, not from the TGD):
  [PMID:14651935 "Inhibition of Fgf8 alone has variable, but mild, effects. However, inhibition of both Fgf3 and Fgf8 together causes a complete absence of pharyngeal cartilages and the near-complete loss of the neurocranial cartilage."]
- The fin is spared. That fits the fact that fgf24, not fgf8a, carries the teleost fin-bud role:
  [PMID:9609821 "Also, in spite of the prominent role suggested for Fgf8 in limb development, the pectoral fins are largely unaffected in the mutants."]
  [PMID:19562753 "fgf24 is required for paired pectoral appendage development in zebrafish but fgf8a is not"]

**fgf8b**

- No mutant, morphant or CRISPR phenotype has been published in the sources searched. Europe PMC
  searches for fgf8b or fgf17a loss-of-function found none (see the fgf8b notes).
- The only functional data are the injection assay and the regulatory hierarchy above
  (PMID:11091072). The authors proposed a supporting role at the MHB:
  [PMID:11091072 "Taken together, our results argue that Fgf8 and Fgf17 act as hierarchically organized signaling molecules during development of the MHB organizer and possibly other organizers in the developing nervous system."]

**Both copies**

- One experiment removes both. Double mutants for ace and noi (pax2a) lose fgf8a function and fgf8b
  expression. Their dopaminergic neurons were no worse than in the single mutants:
  [PMID:12843251 "To reveal possible redundant functions of FGF8 and FGF17, we analyzed th and dat expression in ace noi double mutant embryos that lack expression of both FGF8 and FGF17 (data not shown)."]
  [PMID:12843251 "Among 100 progeny from an intercross of ace noi double heterozygous fish, we found none with a CA phenotype more severe than that of ace or noi single mutant embryos"]
  This is a narrow test: one cell type, data not shown, and a double mutant that also removes pax2a.

**Compensation.** No direct evidence either way. ace ti282a is a PTC allele, so transcriptional
adaptation (upregulation of fgf8b) is possible in principle, but it has not been tested. It is
limited in any case because fgf8b expression at the MHB depends on fgf8a (above). No RNA-less
fgf8a allele and no fgf8b allele exist in the literature found.

## 5. Fate classification

**PARTITION (subfunctionalization), at the expression level. Confidence: moderate.**

**Established**

- The protein-level activity is shared (injection assay; conserved domains; 70.8% identity).
- The expression domains differ, and fgf8a keeps most of them. The gastrula, heart, dorsal
  diencephalon, tailbud, telencephalon, olfactory epithelium, pharyngeal arches and AER domains
  are fgf8a-only in zebrafish. The MHB and somites are shared.
- Each copy kept a different subset of ancestral cis-regulatory elements (unique CNEs; loss of
  fbxw4 from the fgf8b block). This is the mechanism the DDC model predicts.
- Stickleback split the heart domain the opposite way, and the ear domain differently too. So the
  partition was resolved separately in each lineage after the TGD:
  [PMID:17708537 "Moreover, direct comparison of stickleback and zebrafish embryonic expression patterns of fgf8 co-orthologs suggested lineage-specific independent subfunction partitioning and the acquisition or the loss of ortholog functions."]
  [PMID:19562753 "Following the ray-fin fish genome duplication, independent evolution of regulatory elements in lineages leading to zebrafish and stickleback led to the differential partitioning of fgf8 subfunctions in heart development between paralogs so that orthologous genes in the two species have come to express different functions (Jovelin et al., ‘07)."]

**Inferred, not shown**

- *Reciprocity in zebrafish.* The DDC model requires each copy to keep something the other lost.
  In zebrafish, fgf8b's reported domains lie within fgf8a's. The case for reciprocity rests on
  CNEs and on the lineage comparison, not on a zebrafish domain unique to fgf8b. If none exists,
  the zebrafish pair is better described as a nested partition. fgf8b would then be a reduced copy
  that is either quietly redundant at the MHB and somites, or kept for dosage there.
- *fgf8b function.* It has never been tested by loss of function. Its role at the MHB is inferred
  from expression and from the regulatory hierarchy.

**Not supported**

- *Innovation.* No copy has a function absent from single-copy FGF8. Olfactory epithelium
  expression may be a teleost gain, but it belongs to fgf8a, and its timing relative to the TGD is
  not established.
- *Pure backup.* This is ruled out for most of the fgf8a domains, because fgf8b is absent from
  them and ace phenotypes appear there. It cannot be ruled out for the shared MHB and somite
  domains.

**What would change the call**

- An fgf8b null (ideally RNA-less) with its own phenotype, or a domain unique to fgf8b, would
  confirm reciprocal partition.
- fgf8a;fgf8b double mutants that are worse than ace at the MHB or in somites would add a backup or
  dosage component in the shared domains.
- Failure of fgf8b to rescue ace when expressed from the fgf8a locus would add a protein-level
  component.
- Expression data for single-copy gar fgf8 would anchor the ancestral state directly.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and correctly so.** The molecular function terms are accepted for both copies: growth
factor activity (GO:0008083) and FGFR1/FGFR2 binding (GO:0005105, GO:0005111), plus fibroblast
growth factor receptor binding (GO:0005104, NAS) on fgf8b. So are the FGF receptor signaling pathway
(GO:0008543), positive regulation of the MAPK cascade (GO:0043410) and the extracellular region
(GO:0005576). The broad IBA process terms (neurogenesis, regulation of cell migration, positive
regulation of cell population proliferation) are kept as non-core on both. The cytoplasm IBA is
marked as over-annotated on both, because both are secreted ligands with signal peptides; this
matches the human FGF8 review. For these terms, treating the copies as equivalent is right.

**Asymmetric, and correctly so.**

- All gastrula-stage process terms stay on fgf8a only: dorsoventral patterning, mesoderm
  development, negative regulation of endodermal cell fate specification, and anterior/posterior
  patterning.
  - On fgf8b the dorsal/ventral pattern formation IBA (GO:0009953) was **marked as
    over-annotated**. The PAINT node is sound, and fgf8b protein could do the job when injected.
    But fgf8b is not expressed when the D/V axis is set. This is the one place in the pair where
    IBA propagation treats the copies as equivalent and the expression data do not.
  - The ARBA negative regulation of endodermal cell fate specification (GO:0042664) was
    **removed from fgf8b**. It is a gastrula event and fgf8b is absent then.
  - The ARBA mesoderm development and A/P pattern specification rows were marked as
    over-annotated on fgf8b. On fgf8a the same terms are kept as non-core.
- The heart terms (cardioblast differentiation, heart morphogenesis, ventricular cardiomyocyte
  differentiation) are fgf8a-only. That is correct: fgf8b is not expressed in the zebrafish heart.
  They must **not** be carried to fgf8b by orthology, even though stickleback fgf8b is the heart
  copy.
- The left-right, Kupffer's vesicle, thyroid, pharyngeal and taste-bud terms are fgf8a-only.
  They come from ace or morphant data in domains where fgf8b is absent, or where its expression
  has not been reported.

**Asymmetries caused by which copy was studied.** The MHB, cerebellum, somite/muscle and otic
terms (all ACCEPTed or kept on fgf8a) rest on fgf8a loss of function alone. fgf8b shares the
MHB, somite and otic vesicle expression, but has no loss-of-function data. On fgf8b, MHB
development (GO:0030917) is kept as non-core from the NAS. No other shared-domain terms were added
to fgf8b as NEW. With no loss-of-function data, adding them would assert a participation that has
not been tested.

**Should be copy-specific:** heart, gastrula (D/V, mesendoderm) and fin/pharyngeal terms belong to
fgf8a.

**Should be shared:** molecular function, the FGFR pathway, and the extracellular location. MHB and
somite roles may be shared once fgf8b is tested.

**Other review notes.** Three fgf8a rows were left UNDECIDED because the cached abstracts do not
support them: positive regulation of Wnt signaling (PMID:14757644) and two rows from an Fgf19
paper (PMID:16256099). One IDA row, endoderm development (PMID:17026981), was modified to
GO:0042664.

## 7. Open questions

- Does fgf8b have any loss-of-function phenotype? Is there any zebrafish domain unique to fgf8b?
- Is fgf8b upregulated in ace (a PTC allele), and would an RNA-less fgf8a allele give a stronger
  MHB or somite phenotype?
- Would fgf8b coding sequence, expressed from the fgf8a locus, rescue ace? That would be a
  protein-equivalence test in vivo.
- What is the expression of single-copy gar fgf8, especially in the heart and the gastrula?
- Which of the fgf8a-specific CNEs in fbxw4 drive its heart and gastrula expression? Did the
  stickleback fgf8b locus keep the cardiac element?

## References

PMID:9609821, PMID:10603341, PMID:11091072, PMID:12843251, PMID:14651935, PMID:15151985,
PMID:15932752, PMID:16961592, PMID:17239227, PMID:17387144, PMID:17448458, PMID:17522161,
PMID:17708537, PMID:19562753, PMID:19782672, PMID:24677486, PMID:28873404. Also the files
`panther_tgd_pairs.tsv` and [annotation-comparison.md](annotation-comparison.md), and the gene
notes `genes/DANRE/fgf8a/fgf8a-notes.md` and `genes/DANRE/fgf8b/fgf8b-notes.md`.
