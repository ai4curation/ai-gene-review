# fgf8a notes (DANRE, O57341)

## 2026-09-28 session log

- Deep research FAILED for this gene (Edison: 402 Payment Required; the OpenAI key is invalid).
  Not retried, per instructions. The literature research below was done by hand, from the
  GOA-cited cached publications plus Europe PMC REST searches
  (queries: `"fgf8b" AND zebrafish`; `(fgf8a AND fgf8b) AND (duplicat* OR paralog*)`;
  `"fgf17a" AND zebrafish`; `(fgf8b OR "fgf17a") AND zebrafish AND (morpholino OR mutant OR knockdown OR CRISPR)`;
  `fgf8a AND fgf8b AND zebrafish`).
- Newly cached PMIDs this session: 19562753 (Jovelin 2010, FgfD subfamily evolution, full text),
  17387144 (Kikuta 2007, genomic regulatory blocks, full text), 28873404 (FGF and somatic gonad,
  full text; TGD statement only), 26525676, 21506104, 34462605, 39055102, 40575596 (checked;
  little or nothing on the paralog pair, mostly not used). Caution: "Fgf8a/Fgf8b" in mammalian and
  some zebrafish papers (PMID:16961592, PMID:21506104, PMID:40575596) refers to the two SPLICE
  ISOFORMS of Fgf8, not to the two TGD paralogs. Do not conflate.
- Most GOA-cited papers are abstract-only in the cache. Full text available: PMID:12843251,
  15281067, 16754885, 17239227, 17448458, 18639539, 19164561, 19395641, 19823566, 20885782,
  23789101, 23946439, 24677486, 25142463, 27060628, 28493069, 32345657.

## Identity and naming

- fgf8a is the "uncontested" zebrafish FGF8 orthologue, the gene mutated in acerebellar (ace)
  [PMID:9609821 "we show that acerebellar is a zebrafish Fgf8 mutation that may inactivate Fgf8 function"].
- The paralogue fgf8b was first named fgf17 / fgf17a; it is a TGD co-orthologue of FGF8
  [PMID:17708537 "the teleost genes called fgf8 and fgf17a are duplicates of the tetrapod gene Fgf8, and thus should be called fgf8a and fgf8b"].
- Synteny: fgf8a on Dre13, fgf8b on Dre1
  [PMID:19562753 "The orthologs of a somewhat different set of human genes flanking FGF8 lie near fgf8a in zebrafish Dre13 and stickleback LG VI (Fig. 4D,E)."].
- TGD origin [PMID:28873404 "the fgf8 and fgf18 duplications are a result of the teleost-specific whole-genome duplication"].
- Protein: 210 aa, signal peptide 1-27 (UniProt O57341); 70.8% identity to fgf8b
  (compare_pair.py global alignment).

## Alleles (compensation relevance)

- ace ti282a: splice-site point mutation giving a frameshift and premature stop codon, i.e. a
  PTC allele that could trigger NMD and, in principle, transcriptional adaptation
  [PMID:17448458 "encodes a point mutation in the splice site following exon 2, causing a frame shift and introduction of a premature stop codon"].
  Described as a strong hypomorph [PMID:17239227 "acerebellarti282a, a strong hypomorphic allele of fgf8"].
- fgf8 x15 allele used in PMID:24677486 [PMID:24677486 "Mutant alleles fgf3t26212 and fgf8x15"].
- Many annotations rest on morpholinos (fgf8 MO), often combined with fgf3 MO.
- No RNA-less (promoter-deletion) fgf8a allele was found in the literature searched.

## Expression and function (key facts)

- MHB organizer: [PMID:9609821 "Homozygous acerebellar embryos lack a cerebellum and the midbrain-hindbrain boundary organizer."]
- Heart: [PMID:10603341 "These findings show that fgf8/acerebellar is required for induction and patterning of myocardial precursors."]
  Only fgf8a (not fgf8b) is expressed in the zebrafish heart; in stickleback the reverse
  [PMID:19562753 "In zebrafish, fgf8a is required for the expression of cardiac genes (Reifers et al., ‘00b), but fgf8b is not expressed in the heart; conversely, in stickleback, fgf8b but not fgf8a is expressed in the heart (Jovelin et al., ‘07)."]
- Gastrula D/V: [PMID:15151985 "we show that loss of Fgf8 function enhances the ventralisation of chordin-deficient embryos"].
  fgf8b is not expressed during gastrulation (UniProt Q805B2; PMID:11091072), so the gastrula roles
  (D/V, mesoderm, endoderm restriction) are fgf8a-only at the expression level.
- Otic induction with fgf3: [PMID:17522161 "Fgf8 is the primary factor responsible for otic induction in RA-depleted embryos"].
- Left-right / Kupffer's vesicle: [PMID:15932752 "We find that fgf8 is required for proper asymmetric development of the brain, heart and gut."]
  [PMID:19164561 "Cilia are also lost after suppression of FGF8, but can be rescued by injection of ier2 and fibp1 mRNA."]
- Ligand spreading, extracellular, lysosomal clearance: [PMID:15498491 "We find that spreading of epitope-tagged Fgf8 through target tissue is carefully controlled by endocytosis and subsequent degradation in lysosomes"].
- fgf8a-only expression domains at long-pec: telencephalon, olfactory epithelium, pharyngeal arches, fin AER
  [PMID:19562753 "new domains appear for fgf8a (but not fgf8b) in the telencephalon, olfactory epithelium, pharyngeal arches"].
- fgf8a keeps the fbxw4-intronic enhancers; the fgf8b block deleted fbxw4
  [PMID:19782672 "We conclude that fgf8a transcriptional regulation employs pan-vertebrate and teleost-specific enhancers dispersed over three genes in the zebrafish genome."]
  [PMID:17387144 "This block has retained NP_056263.1 and POLL , two genes that in the human genome are downstream from FGF8 , but has undergone deletion of fbxw4"].
- Redundancy test (the only one found): ace;noi double mutants (no fgf8a function, no fgf8b/fgf17
  expression) show no enhanced dopaminergic phenotype
  [PMID:12843251 "To reveal possible redundant functions of FGF8 and FGF17, we analyzed th and dat expression in ace noi double mutant embryos that lack expression of both FGF8 and FGF17 (data not shown)."].
- fgf8b expression at MHB depends on fgf8a for maintenance
  [PMID:11091072 "only maintenance of fgf17 expression is disturbed at the MHB of acerebellar/fgf8 mutants"].

## Decisions

- 120 GOA rows reviewed. MF (growth factor activity, FGFR1/FGFR2 binding), FGFR signaling and
  the extracellular location are accepted; the IBA cytoplasm row is marked over-annotated
  (secreted ligand with a signal peptide), matching the human FGF8 review.
- Experimental developmental rows are ACCEPTed when they describe the best-established
  organizer roles (MHB/cerebellum, heart precursors, otic placode, left-right/Kupffer's vesicle,
  gastrula D/V) and otherwise KEEP_AS_NON_CORE; they are consistently acts_upstream_of_or_within
  readouts of a signalling ligand.
- UNDECIDED where the cached abstract gives no support and the claim is not self-evident:
  positive regulation of Wnt signaling (PMID:14757644; the abstract describes Wnt8 acting
  upstream of Fgf, the reverse direction), and the Fgf19 paper rows (neuron fate specification,
  oligodendrocyte differentiation; PMID:16256099).
- MODIFY: endoderm development IDA (PMID:17026981) -> negative regulation of endodermal cell fate
  specification (GO:0042664), which is what the paper shows.
- MARK_AS_OVER_ANNOTATED: regulation of bone remodeling IEP (expression cannot establish
  regulation; the IMP row from the same paper is kept).
- No NEW terms.
