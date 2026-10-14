---
title: "Zebrafish Genome Duplication: Background Research"
autolink_gene_symbols: false
---

# Zebrafish Genome Duplication: Background Research

[Back to project](../DANRE_DUPLICATION.md)

This page reviews what is known about the teleost-specific genome duplication (TGD)
and what happened to the function of the duplicated genes. Every claim is tied to a
cached publication in `publications/`. Each quote below was checked as an exact
substring of the cached file by `scripts/check_quotes.py` in this folder. The check
ignores differences in whitespace only, because some cached abstracts are
hard-wrapped. Some quotes are phrase fragments for the same reason.

**Terms used on this page**

- *Ohnolog:* a paralog that arose in a whole-genome duplication (WGD).
- *Co-orthologs:* the two zebrafish ohnologs that are both orthologous to one human
  gene.
- *Zebrafish "a"/"b" suffixes:* ZFIN's naming convention for such pairs. It does not
  say which copy is "ancestral" (see [the naming caveat](#6-caveats-for-choosing-pairs)).

## Summary

1. **The event.** One WGD happened in the stem lineage of teleosts, about
   320–350 Mya. It came after the teleost lineage split from gars and bowfin, and
   before the teleost radiation. It is the "3R" round, on top of the two vertebrate
   rounds ("2R") shared with humans.
2. **Most duplicates were lost, quickly.** Roughly 80–90% of loci went back to a
   single copy, and most losses fell in the first ~60 My. In zebrafish, about 26%
   of genes are still ohnologs (3,440 pairs). That is more than in other sequenced
   teleosts.
3. **Retention is biased.** Duplicate pairs that survive are enriched for
   developmental regulators, transcription factors, signalling and neural genes,
   and genes under strong purifying selection. Housekeeping genes are
   under-represented.
4. **Most retained pairs diverged in expression, not in protein function.** Whether
   those pairs count as "sub" or "neo" depends on method:
   - Using gar as an unduplicated outgroup, only 6.6% of zebrafish pairs show
     *clear* neofunctionalization and 0.8% *clear* subfunctionalization.
   - About 20% keep nearly identical expression (candidates for dosage retention
     or redundancy).
   - About two-thirds have uncorrelated tissue profiles that fit no clean category.
   - Earlier estimates that used mouse as the reference found far more
     "neofunctionalization". The authors say that approach is biased toward it.
5. **The members of a pair do not stay equal.** One copy often evolves faster.
   Expression of the two copies tends to fall until together they approximate the
   ancestral level (quantitative subfunctionalization or hypofunctionalization).
6. **Redundancy is real, but lab results can overstate or mask it.** Zebrafish
   mutants with premature stop codons can switch on paralogs through transcriptional
   adaptation. This hides phenotypes that morphants or RNA-less alleles reveal.
   Absence of a mutant phenotype is therefore weak evidence of redundancy.
7. **The fate of a pair can differ between lineages.** Ohnologs can be lost or kept
   independently in zebrafish and other teleosts. Subfunctions can split
   differently in different lineages. Part of the genome went through delayed
   rediploidization, so strict 1:1 ohnolog orthology between teleost lineages does
   not always exist.

## 1. The duplication event

### Discovery and dating

- **Hox clusters.** The first genome-scale evidence was that zebrafish have seven
  hox clusters, not four:
  [PMID:9831563 "This report shows that zebrafish have seven hox clusters. Phylogenetic analysis and genetic mapping suggest a chromosome doubling event, probably by whole genome duplication, after the divergence of ray-finned and lobe-finned fishes but before the teleost radiation."]
- **Duplicated chromosome segments.** These implied a genome duplication deep in
  teleost ancestry, with a substantial fraction of pairs retained:
  [PMID:11116085 "Duplicated chromosome segments suggest that a genome duplication occurred in ray-fin phylogeny, and comparative studies suggest that this event happened deep in the ancestry of teleost fish. Consideration of duplicate chromosome segments shows that at least 20% of duplicated gene pairs may be retained from this event."]
- **Phylogeny plus synteny across ~22,000 species.** This combination established
  that the event is shared by the teleosts:
  [PMID:12618368 "These phylogeny and synteny data suggest that the common ancestor of zebrafish and pufferfish, a fish that gave rise to approximately 22000 species, experienced a large-scale gene or complete genome duplication event and that the pufferfish has lost many duplicates that the zebrafish has retained."]
- **The Tetraodon genome** confirmed a WGD specific to the teleost lineage:
  [PMID:15496914 "Analysis of the Tetraodon and human genomes shows that whole-genome duplication occurred in the teleost fish lineage, subsequent to its divergence from mammals."]
- **Timing relative to other fish lineages.** Gene trees place the TGD after
  sturgeons and gars branched off, and before the Osteoglossiformes split:
  [PMID:15486693 "support the hypothesis that the fish-specific genome duplication event took place after the split of the Acipenseriformes and the Semionotiformes from the lineage leading to teleost fish but before the divergence of Osteoglossiformes."]
- **Nomenclature (3R).** Reviews call the event "3R", after the two earlier
  vertebrate rounds:
  [PMID:16108068 "a third genome duplication occurred-the fish-specific genome duplication (FSGD or 3R), leading, at least initially, to up to eight copies of the ancestral deuterostome genome."]
- **Dates.** Estimates range from about 306 to 350 Mya:
  - [PMID:27189481 "This teleost-specific round of WGD (TGD) occurred 320–350 million years ago (Mya), after the divergence between the holostean lineage, which includes Semionotiformes (gars) and Amiiformes (bowfin), and the lineage leading to teleost [9, 10]."]
  - [PMID:35961774 "All teleost fish species are paleopolyploids descended from an ancient round of whole-genome duplication (WGD), dated at approximately 320 Mya (Jaillon et al. 2004)."]
  - [PMID:26578810 "The teleost WGD is estimated to have occurred around 306 Mya."]

### Spotted gar as the unduplicated outgroup

The spotted gar (*Lepisosteus oculatus*) lineage diverged before the TGD. Gar therefore
stands in for the pre-duplication state of each zebrafish pair.

- **Gar diverged before the TGD, genome-wide:**
  [PMID:21828280 "This evidence shows on a genome-wide scale that gar and teleost lineages diverged before the TGD."]
- **One gar region matches two zebrafish chromosomes:**
  [PMID:21828280 "This includes the gar orthologs of human genes GRIN2C and SDK2, each of which has one co-ortholog on zebrafish Dre3 and the other co-ortholog on Dre12"]
- **Gar is proposed as the reference for ancestral function**, including for telling
  ancestral functions apart from post-TGD neofunctionalization:
  [PMID:21828280 "We conclude that spotted gar is the species of choice to serve as an experimentally accessible outgroup to teleosts to help infer ancestral, preduplicated functions of genes duplicated in teleosts."]
- **The "gar bridge"** recovers human–zebrafish orthologies that direct comparison
  misses (quote is a short fragment because the cached text is hard-wrapped):
  [PMID:26950095 "lost in teleosts. The ‘gar bridge’ (Fig. 4a) established hidden orthology from human to gar"]

This matters for the project. When we ask whether a zebrafish copy has a "new"
function, the comparison should be with gar (or a non-teleost fish), not only with
human or mouse. The tetrapod lineage has had its own ~430 My of change since the split.

### Delayed rediploidization

- **Homeologous chromosomes kept exchanging material long after the TGD:**
  [PMID:35961774 "Altogether, we provide the first evidence that entire chromosomes experienced delayed rediploidization in teleosts and continued to exchange genetic material between homeologs for at least 60 million years after the teleost whole genome duplication."]
- **This implies an autotetraploid ancestor:**
  [PMID:35961774 "This prolonged exchange of genetic material between duplicated chromosomes after the TGD strongly suggests that the teleost ancestor was an autotetraploid."]
- **Consequence for comparisons.** In regions where the ohnologs were resolved late
  and independently in each lineage (the "LORe" model), zebrafish "a" is not
  strictly orthologous to medaka "a":
  [PMID:35961774 "In the LORe model, because cytological rediploidization has not been resolved before speciation occurs, ohnologs share more sequence similarity within clades than across clades, and can therefore be misidentified as clade-specific duplications."]

## 2. How many duplicates survive, and which ones

### Zebrafish numbers

The zebrafish reference genome paper uses "TSD" for the TGD.

- **Protein-coding gene count:**
  [PMID:23594743 "Zebrafish possess 26,206 protein-coding genes6, more than any previously sequenced vertebrate"]
  [PMID:23594743 "Some of this increased gene number is likely to be a consequence of the TSD."]
- **Orthology with human:**
  [PMID:23594743 "First, 71.4% of human genes have at least one zebrafish orthologue, as defined by Ensembl Compara14 (Table 2). Reciprocally, 69% of zebrafish genes have at least one human orthologue."]
  [PMID:23594743 "Among the orthologous genes, 47% of human genes have a one-to-one relationship with a zebrafish orthologue."]
- **Ohnolog pairs:**
  [PMID:23594743 "We identified 3,440 pairs of such ohnologues (26% of the all genes), for a total of 8,083 genes when subsequent duplications are taken into account."]
  [PMID:23594743 "This number of ancestral genes retained as duplicates in zebrafish is higher, both in absolute number and in proportion, than in other fish genomes"]

### Loss was fast at first, then slowed

- **Most copies went back to singletons, when counted against gar:**
  [PMID:28944589 "In our study, a large majority (87% (10,415 out 12,021 in zebrafish, see Fig.1) and 88% (9,265 out of 10,580 in medaka, see Fig. 1)) of genes were retained only as singletons after the TGD, while less than 15% (12–13%, see Fig. 1) were kept in duplicate."]
- **Loss rates over time, from a nine-teleost model:**
  [PMID:26578810 "We found 82% [5,655/(5,655 + 1,237)] of those gene lineages [72% (11,091/15,353) without the BS 70% criterion] were rapidly lost during the initial 60 My (first phase)"]
  [PMID:26578810 "more than one-half (692/1,237) of the gene lineage pairs in the ancestor of the nine teleosts (node a ) persisted over the next 250 My"]
- **Long-term survivors appear to be under selection:**
  [PMID:19500364 "Instead, it appears that the genes which persisted for 275 MY have been maintained by selection."]
- **Retention depends on method and scope.** Estimates range widely: a strict 3–4%
  of loci in Kassahn 2009, 12–13% against gar, 26% of zebrafish genes by
  double-conserved synteny, and higher values from small pathway-focused samples.
  These are different measurements, not a contradiction. The project should
  state which definition of "TGD pair" it uses.
  [PMID:19439512 "This strategy identified some 680 gene pairs, or 3%–4% of protein-coding gene loci in each of the five fish genomes"]

### Which genes are kept in duplicate

- **Developmental, signalling and regulatory genes, under strong purifying
  selection; one copy often speeds up:**
  [PMID:16809621 "The subset of genes, which was retained in double after the genome duplication, is enriched in development, signaling, behavior, and regulation functional categories."]
  [PMID:16809621 "following duplication, there is an asymmetric acceleration of evolutionary rate in one of the paralogs."]
- **Neural and transcription-factor genes in zebrafish specifically:**
  [PMID:23594743 "In general, zebrafish ohnologous pairs are enriched in specific functions (neural activity, transcription factors) and are orthologous to mammalian genes under stronger evolutionary constraint than genes that have lost their second copy."]
- **Signalling and ion transport over-retained; housekeeping under-retained:**
  [PMID:26578810 "Most of the highly significant genes associated with the 141 terms were those of proteins involved in signaling (e.g., glutamate receptor signaling pathway) and ion transport (e.g., ion channel complex)."]
  [PMID:26578810 "These underrepresented genes included those for housekeeping functions such as RNA processing and DNA repair."]
- **Dosage balance** is the leading explanation for why transcription factors and
  signalling components are kept after WGD (as opposed to small-scale
  duplications):
  [PMID:35253876 "Dosage balance can mediate retention of specific classes of genes that are dosage sensitive to maintain their stoichiometric relationship with partners in multicomponent interactions."]

## 3. Models for why both copies are kept

| Fate | What happens | Key reference |
|------|--------------|---------------|
| Nonfunctionalization | One copy decays into a pseudogene or is deleted; this is the most common outcome | PMID:27189481, PMID:15831095 |
| Subfunctionalization (DDC) | Complementary degenerative mutations split the ancestral functions (often expression domains); both copies become necessary | PMID:10101175, PMID:10629003 |
| Quantitative subfunctionalization / hypofunctionalization | Both copies are expressed at lower levels and together supply the ancestral dosage | PMID:35253876, PMID:28944589 |
| Dosage-balance retention | Both copies are kept to preserve stoichiometry with interaction partners; likely to decay over time | PMID:35253876 |
| Neofunctionalization | One copy gains a function absent from the ancestor | PMID:15831095, PMID:27189481 |
| Redundancy / backup | Both copies keep the full ancestral function; considered unstable in theory | PMID:15831095, PMID:28704371 |

**Definitions and theory**

- **The DDC model** (Force et al. 1999) came partly from zebrafish work, including a
  new *engrailed* gene:
  [PMID:10101175 "The duplication-degeneration-complementation (DDC) model"]
  [PMID:10101175 "examples (including analysis of a new engrailed gene in zebrafish) that appear"]
- **Lynch & Force** formalized subfunctionalization:
  [PMID:10629003 "members of a pair experience degenerative mutations that reduce their joint"]
  [PMID:10629003 "levels and patterns of activity to that of the single ancestral gene. We"]
- **Birchler & Yang** gave compact definitions:
  [PMID:35253876 "Subfunctionalization is the division of function such that the two members of a pair confer only part of the functions of the progenitor singleton."]
  [PMID:35253876 "Neofunctionalization is the diversification of one member of a duplicate pair for a new function."]
  [PMID:35253876 "Hypofunctionalization involves the reduction in expression of both copies of a duplicate pair to a threshold level at which both copies are needed for the specific function of the gene and thus both copies are maintained."]
- **Simulations** suggest subfunctionalization is often a transition state rather
  than an end state. They also suggest that pure redundancy is not selectively
  maintained:
  [PMID:15831095 "However, with increasing time, subfunctionalization decreases in importance and its role seems to be to preserve duplicate copies for eventual neofunctionalization, a role as a transition state."]
  [PMID:15831095 "is no apparent selective pressure to maintain redundancy."]
- **Caution on over-calling subfunctionalization:**
  [PMID:35253876 "There is a tendency in the literature to ascribe subfunctionalization to any case in which duplicate genes have somewhat different expression patterns."]

## 4. Genome-wide evidence: neofunctionalization or backups?

This is the central question for the project. The answer depends heavily on the
reference used to define the ancestral state.

### Using mouse as the reference (Kassahn et al. 2009)

- **Most pairs differ in expression:**
  [PMID:19439512 "Of the 97 WGD-gene pairs, 87% differed in expression localization during at least one developmental stage, while only 13% shared the same expression domain during all developmental stages investigated thus far."]
- **Breakdown against the single mouse ortholog:**
  [PMID:19439512 "Of the remaining 38 gene pairs, 20 (53%) had novel expression domains not found in the mouse ortholog, supporting a model of neofunctionalization ( Table 6 )."]
  [PMID:19439512 "Four gene pairs (11%) had expression domains that were subsets of those of mouse, supporting a model of subfunctionalization, while 10 gene pairs (26%) showed evidence to support both neo- and subfunctionalization."]
  [PMID:19439512 "Finally, four zebrafish gene pairs (11%) showed the same expression pattern during this developmental time point, potentially indicating functional redundancy."]
- **The authors flag their own bias:**
  [PMID:19439512 "Our differential ability to identify these alternate evolutionary fates may, however, have biased our results in favor of neofunctionalization."]
- **Regulatory divergence is far more common than protein divergence:**
  [PMID:19439512 "In summary, 93% of the 138 gene pairs investigated differed in spatial and/or temporal expression ( Table 7 ). In contrast, only 24% of 545 gene pairs encoded proteins that differed in domain architecture and/or subcellular localization ( Table 7 )."]
  [PMID:19439512 "indicating that after some 400 Myr of evolution, duplicates retained after WGD either differ in regulatory control or in protein function, but not usually in both."]

### Using gar as the reference (Pasquier et al. 2017; Braasch et al. 2016)

- **Loss is the default fate:**
  [PMID:28944589 "Results demonstrate that in both zebrafish and medaka, the loss of one of the duplicate genes is the most common fate after TGD with a probability of about 80%."]
- **Clear neo- or subfunctionalization is rare:**
  [PMID:28944589 "a total of 51 (6.6%) and 6 (0.8%) cases could be identified in which TGD ohnolog pairs exhibited clear signatures of neofunctionalization or subfunctionalization following our criteria, respectively"]
- **About a fifth of pairs look unchanged** (candidates for dosage retention or
  backup):
  [PMID:28944589 "In both zebrafish and medaka, approximately 20% (18.8–21.9, Figure 6) of ohnologs exhibit a highly correlated expression profile and similar expression levels (HCSE)."]
- **About two-thirds are uncorrelated** and do not fall into a clean category:
  [PMID:28944589 "A large majority of genes were not significantly correlated (NC) with a total of 66.3% (37.1+29.2) and 66.5% (37.3+29.2) in the NC category for zebrafish and medaka, respectively."]
- **Dosage sharing:**
  [PMID:28944589 "suggesting that expression levels of retained ohnologs tend to decrease so that a duplicated gene pair together approximates the levels of the pre-duplication gene."]
- **Ohnologs are less alike in expression than orthologs between species:**
  [PMID:28944589 "Orthologs exhibited a significantly (p<0.001) higher correlation than ohnologs with correlation (r) of 0.34 and 0.57 for ohnologs and orthologs, respectively (Fig. 5)."]
- **Example of clean subfunctionalization (gpr22):**
  [PMID:28944589 "gpr22) exhibited clear subfunctionalization of TGD ohnologs with one ohnolog expressed in brain as in gar and the other ohnolog expressed in heart as in gar (Fig. 2G–I)."]

**Reading of the evidence**

- Retained TGD pairs are mostly not clean textbook cases of either model.
- Clear neofunctionalization is a minority, somewhere between ~7% (gar reference)
  and ~50% (mouse reference, admittedly biased).
- Clean subfunctionalization is rare when judged strictly.
- A sizeable minority (~20%) look like dosage-retained near-copies.
- The majority show partial, uncorrelated expression divergence. That is
  consistent with ongoing quantitative subfunctionalization or drift.
- Protein-level functional divergence is much less common than regulatory
  divergence.

For GO annotation, this is the key point: **in most retained pairs, both copies
probably keep the same molecular function**. The two copies differ mainly in
where, when and how much they are expressed, and therefore in which biological
processes each one is observed to take part in.

## 5. Case studies in zebrafish

### Subfunctionalization: expression split between the two copies

**mitfa/mitfb.** The expression of the single mammalian gene is split between the
pair, and the proteins are functionally interchangeable:

- [PMID:11543618 "melanogenic cells, perturb only neural crest melanocytes, suggesting redundancy"]
- [PMID:11543618 "zebrafish ortholog of the closely related gene tfe3, can rescue neural crest"]
- [PMID:11543618 "recapitulate the expression and functions of a single ancestral Mitf gene, and"]
- [PMID:11543618 "that mitfb may serve additional novel functions."]

**pax6a/pax6b.** Subfunctionalization through cis-regulatory divergence; only pax6b
is expressed in the pancreas:

- [PMID:18282108 "we observed multiple examples of subfunctionalization, or job-sharing, between pax6a and pax6b."]
- [PMID:18282108 "only pax6b is expressed in the pancreas isolated from 6 month old wild type and sri/sri fish, while eyes from the same individuals express both pax6a and pax6b"]
- [PMID:18282108 "We also showed that pax6a expression is not induced in the pancreas of the sunrise mutant."]

**sox9a/sox9b.** Subfunctions were split mostly before the zebrafish and stickleback
lineages separated, but partly differently in each lineage:

- [PMID:14579386 "between Sox9a and Sox9b before the divergence of stickleback and zebrafish"]
- [PMID:14579386 "lineages, but some ancestral expression domains were distributed differentially"]

**fabp1a/fabp1b (and fabp10).** Hierarchical subfunctionalization:

- [PMID:16857010 "genes imply a hierarchical subfunctionalization that may account for the"]

### Subfunctionalization followed by neofunctionalization

**elna/elnb.** elnb became restricted to the bulbus arteriosus and cannot be replaced
by elna or by the single-copy Polypterus gene:

- [PMID:26783159 "We found that elnb expression patterns were restricted to the BA, while elna was observed in various tissues in both medaka"]
- [PMID:26783159 "In contrast to this, injection of elnb MO and elna full-length mRNA did not rescue the elnb morphant phenotype"]
- [PMID:26783159 "both of these Polypterus eln mRNAs did not rescue the elnb morphant phenotype"]

### Neofunctionalization after an older duplication (not the TGD)

**RARs.** Neofunctionalization from the vertebrate 2R duplications, useful as a
contrast. The three RAR paralogs predate the teleost split:

- [PMID:16839186 "One vertebrate paralogue, RARβ, was constrained by natural selection and kept most of the ancestral functions, allowing the two other paralogues to take on new possible functions."]

### Zebrafish-specific loss of one ohnolog

**Androgen receptor.** Zebrafish has a single AR; AR-B was lost in basal
Clupeocephala:

- [PMID:19094205 "Importantly, the AR-B ortholog in the zebrafish could not be detected neither on chromosome Z14 nor on other locations in the whole genome."]

**Stress axis.** The zebrafish lineage recently lost duplicates of stress-axis genes
that other teleosts keep:

- [PMID:18930731 "have lost the duplicate CRH, ACTH and GR genes in the past 33 million years,"]
- [PMID:18930731 "after possessing two of each for the previous 300 million years. The"]

**Reciprocal loss between lineages** is common:

- [PMID:17275132 "We estimate that thousands of genes that remained duplicated when Tetraodon and zebrafish diverged underwent reciprocal loss subsequently in these two species, probably contributing to reproductive isolation between them."]

### Redundancy and genetic compensation: the "backup" question

In zebrafish, the backup question cannot be separated from a methodological one:
**mutants often lack the phenotypes seen in morphants**.

**Morphant versus mutant discrepancies (Rossi 2015).**
- [PMID:26168398 "show that egfl7 mutants do not show any obvious phenotypes while animals"]
- [PMID:26168398 "mutants but not morphants show an upregulation of vegfab."]

**Mechanism (El-Brolosy 2019).** Mutant mRNA decay upregulates related genes, often
the TGD paralog:
- [PMID:30944477 "hbegfa, vcla, hif1ab, vegfaa, egfl7 and alcama zebrafish mutants exhibit increased mRNA levels of a paralogue or family member (hereafter referred to as ‘adapting gene’), namely hbegfb, vclb, epas1a and epas1b, vegfab, emilin3a and alcamb, respectively"]
- [PMID:30944477 "Indeed, RNA-less alleles of hbegfa, vegfaa and alcama fail to upregulate hbegfb, vegfab and alcamb, respectively"]
- [PMID:30944477 "Therefore, use of RNA-less alleles can uncover phenotypes not observed in alleles exhibiting mutant mRNA degradation."]

**Independent confirmation (Ma 2019).** The response depends on a premature
termination codon (PTC) and on Upf3a/COMPASS, shown for capn3a and nid1a:
- [PMID:30944473 "Here, using zebrafish knockdown and knockout models of the capn3a and nid1a genes, we show that mRNA bearing a premature termination codon (PTC) promptly triggers a GCR that involves Upf3a and components of the COMPASS complex."]

**Background on robustness** (El-Brolosy & Stainier 2017):
- [PMID:28704371 "Genetic robustness may arise from redundant genes, whereby the loss of one gene may be compensated by another with overlapping functions and expression pattern"]

**Implications for this project**

1. A mild or absent zebrafish mutant phenotype does **not** by itself show that the
   gene is redundant with its ohnolog, or that it lacks a function. Allele type
   matters: PTC or NMD alleles differ from promoter or whole-locus deletions and
   from morphants.
2. Paralog upregulation in a mutant is a real, measurable signal that the two
   copies *can* substitute for each other at the molecular level. That is evidence
   for shared molecular function.
3. When a phenotype belongs to only one copy (pax6b in pancreas, elnb in the
   bulbus arteriosus), that is usually an expression partition. It is not
   evidence that the other copy lacks the molecular function.

## 6. Caveats for choosing pairs

- **The "a"/"b" suffixes are not phylogenetically consistent.** Parey et al. found
  that 43% would need reassigning to match polyploid history. A suffix does not
  tell you which homeolog a gene sits on, and does not say "a = ancestral":
  [PMID:35961774 "zebrafish “a” and “b” gene suffixes are not consistent with the polyploid history of the zebrafish genome (Fig. 4A): 43% of gene suffixes would have to be reassigned"]
- **Not every zebrafish paralog pair is a TGD pair.** Some are older (2R, e.g.
  cyp26a1/cyp26b1) and some are younger (lineage-specific tandem duplications).
  Pair selection should require evidence of TGD origin: double-conserved synteny
  with gar, or a gene-tree duplication node at the teleost root.
- **Asymmetric rates bias gene trees.** A fast-evolving ohnolog can be pulled to the
  base of the tree (long-branch attraction):
  [PMID:12618368 "suggests that the  fast-evolving, amino-acid positions (i.e., those most likely to lead to  LBA) were often responsible for the “basal” position of one set of  duplicates."]
- **Do not assume 1:1 orthology with human:**
  [PMID:12618368 "This means that comparative studies will have to be  designed that, as a starting point, do not assume a 1:1 ratio of  “orthologous” genes between human and model fish species."]

## 7. What this suggests for curating paralog pairs

These are working hypotheses for the pair reviews. They are not rules.

- **Molecular function (MF).** Expect both copies to share the ancestral MF unless
  there is specific evidence otherwise. Such evidence would include a lost
  catalytic residue, a domain loss, failure to rescue, or a distinct biochemical
  activity. Protein-level divergence is the minority case (~24% of pairs by
  domain or localization in PMID:19439512).
- **Biological process (BP) and cellular component (CC).** Differences between the
  copies usually reflect expression partition. An IMP on one copy is valid for that
  copy. Propagating it to the other copy (or up to human) should be done with care
  in both directions.
- **"Backup" claims.** Require positive evidence, such as double-mutant synergy,
  cross-rescue, or paralog upregulation in an RNA-less-vs-PTC comparison. Absence
  of a single-mutant phenotype is not enough.
- **Neofunctionalization claims.** Require a gar (or other pre-TGD) comparison.
  Human or mouse alone is not enough. Otherwise a function lost in the tetrapod
  lineage looks like a teleost innovation.
- **IBA propagation.** PANTHER trees normally place both TGD ohnologs under the same
  node. An IBA to both copies of a pair is therefore expected. Pair reviews are a
  good place to test whether that propagation holds for protein-level
  neofunctionalization cases.

## References

| PMID | Short citation | Role here |
|------|----------------|-----------|
| PMID:9831563 | Amores et al. 1998 Science, zebrafish hox clusters | Discovery of the TGD |
| PMID:10101175 | Force et al. 1999 Genetics, DDC model | Subfunctionalization theory |
| PMID:10629003 | Lynch & Force 2000 Genetics | Subfunctionalization theory |
| PMID:11116085 | Postlethwait et al. 2000 Genome Res | Duplicated chromosome segments |
| PMID:11543618 | Lister et al. 2001 Dev Biol, mitfa/mitfb | Case study |
| PMID:12618368 | Taylor et al. 2003 Genome Res | TGD shared by teleosts |
| PMID:14579386 | Cresko et al. 2003 Dev Dyn, sox9a/sox9b | Lineage-specific partitioning |
| PMID:15363902 | Postlethwait et al. 2004 Trends Genet | Review: subfunction partitioning |
| PMID:15486693 | Hoegg et al. 2004 J Mol Evol | Phylogenetic timing |
| PMID:15496914 | Jaillon et al. 2004 Nature, Tetraodon genome | Genome-scale confirmation |
| PMID:15831095 | Rastogi & Liberles 2005 BMC Evol Biol | Sub- to neofunctionalization model |
| PMID:16108068 | Meyer & Van de Peer 2005 BioEssays | Review: 2R to 3R |
| PMID:16109975 | Woods et al. 2005 Genome Res | Differential retention |
| PMID:16809621 | Brunet et al. 2006 Mol Biol Evol | Retention bias, asymmetric rates |
| PMID:16839186 | Escriva et al. 2006 PLoS Genet, RARs | Contrast: 2R neofunctionalization |
| PMID:16857010 | Sharma et al. 2006 FEBS J, fabp1a/b | Case study |
| PMID:17275132 | Sémon & Wolfe 2007 Trends Genet | Reciprocal loss |
| PMID:18282108 | Kleinjan et al. 2008 PLoS Genet, pax6a/b | Case study |
| PMID:18930731 | Alsop & Vijayan 2009 Gen Comp Endocrinol | Zebrafish-specific losses |
| PMID:19094205 | Douard et al. 2008 BMC Evol Biol, AR | Loss in zebrafish; late neofunctionalization |
| PMID:19439512 | Kassahn et al. 2009 Genome Res | Genome-wide fates (mouse reference) |
| PMID:19500364 | Sato et al. 2009 BMC Evol Biol | Temporal pattern of loss |
| PMID:21828280 | Amores et al. 2011 Genetics, gar map | Gar as outgroup |
| PMID:23594743 | Howe et al. 2013 Nature, zebrafish genome | Zebrafish ohnolog counts |
| PMID:25092473 | Glasauer & Neuhauss 2014 Mol Genet Genomics | Review |
| PMID:26168398 | Rossi et al. 2015 Nature | Genetic compensation |
| PMID:26578810 | Inoue et al. 2015 PNAS | Rapid early loss |
| PMID:26783159 | Moriyama et al. 2016 Nat Commun, elnb | Sub- then neofunctionalization |
| PMID:26950095 | Braasch et al. 2016 Nat Genet, gar genome | Gar bridge; expression partition |
| PMID:27189481 | Pasquier et al. 2016 BMC Genomics, PhyloFish | Fates; dating |
| PMID:28704371 | El-Brolosy & Stainier 2017 PLoS Genet | Review: genetic compensation |
| PMID:28944589 | Pasquier et al. 2017 J Exp Zool B | Genome-wide fates (gar reference) |
| PMID:30944473 | Ma et al. 2019 Nature | Genetic compensation mechanism |
| PMID:30944477 | El-Brolosy et al. 2019 Nature | Transcriptional adaptation |
| PMID:35253876 | Birchler & Yang 2022 Plant Cell | Definitions; dosage balance |
| PMID:35961774 | Parey et al. 2022 Genome Res | Delayed rediploidization; a/b caveat |
