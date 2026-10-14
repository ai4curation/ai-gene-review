---
title: "tmc2a / tmc2b"
autolink_gene_symbols: false
---

# tmc2a / tmc2b

[Back to pairs](../README.md)

**Bottom line:** PARTITION, at the level of expression, lopsided and overlapping. Both copies encode pore-forming
subunits of the hair-cell MET channel and are expressed only in hair cells, but in different proportions. tmc2b is
the dominant copy in the lateral line and in peripheral (extrastriolar) inner-ear hair cells. tmc2a is dominant in
central (striolar) inner-ear hair cells, in the upper layer of the cristae and in the saccule, and is present in only
one orientation class of lateral-line hair cells. Each single mutant loses transduction in the cells where its copy
predominates, and the double mutant is more severe than either single mutant where both are expressed. A Tmc2b
transgene restores transduction in every end organ of tmc1/tmc2a/tmc2b triple mutants. So the Tmc2b protein can
do the job wherever it is expressed. The reverse test has not been done. Whether Tmc2a gives the channel different
properties (larger responses, a broader frequency range) is suggested but not separated from cell type. TGD origin
rests on the PANTHER tree; both copies are on zebrafish chromosome 5 and synteny support is partial.

**Sample record:** fate=PARTITION; level=expression; evidence=experimental_both; identity=68.0%

| | tmc2a | tmc2b |
|---|---|---|
| UniProt | E7FFT2 (Swiss-Prot, 916 aa) | F1QZE9 (Swiss-Prot, 892 aa) |
| Human ortholog | TMC2 | TMC2 |
| Chromosome | 5 (55.2 Mb) | 5 (25.6 Mb, 5 kb from tmc1) |
| ZFIN | ZDB-GENE-060526-280 | ZDB-GENE-060526-262 |
| Review | [genes/DANRE/tmc2a](../../../../genes/DANRE/tmc2a/tmc2a-ai-review.yaml) | [genes/DANRE/tmc2b](../../../../genes/DANRE/tmc2b/tmc2b-ai-review.yaml) |

## 1. Evidence the pair comes from the TGD

**PANTHER.** The row in `panther_tgd_pairs.tsv` is:

| tgd_call | branch | class | family | human orthologs (a / b) | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|---|
| TGD_tree | Neopterygii\|Teleostei | 1:1 | PTHR23302 (TRANSMEMBRANE CHANNEL-RELATED) | TMC2(LDO) / TMC2(O) | 1 (same gar gene for both) | 2 | (blank) |

(The ZFIN id column for tmc2a is empty in the table; the Ensembl and UniProt records give ZDB-GENE-060526-280.)

**Literature.** The pair was named by Maeda et al. 2014. Later papers attribute it to the teleost duplication by
citation, not by analysis:
[PMID:25114259 "There are two zebrafish tmc2 genes in the Ensembl genome database (release 73), and we designated the paralogous gene isolated in the screen as tmc2a , and the gene duplicate as tmc2b ."]
[PMID:33490059 "Tmc2a and tmc2b paralogs are the result of a whole-genome duplication that occurred in teleost fish between 300 and 450 million years ago (Taylor et al., 2001)."]
Both copies, and tmc1, are on one chromosome:
[PMID:25114259 "All three genes are located on chromosome 5, with tmc1 and tmc2b directly adjacent to one another ( Fig. S2 )."]
[PMID:29269857 "To determine if tmc2a and tmc2b genetically interact to enable mechanotransduction, we successfully lesioned both of these genes, which reside on Chromosome 5, separated by ~39.9 centiMorgans."]

**My check** ([RESULTS.md](../../../../genes/DANRE/tmc2a/tmc2a-bioinformatics/RESULTS.md)).

- Ensembl Compara joins the two copies at the Osteoglossocephalai node, with one gar orthologue for both. The
  one-to-one medaka orthologues are on different medaka chromosomes (12 and 9).
- The gar tmc2 gene sits next to gar tmc1 on LG2, in a block whose human orthologues are on 9q21 (the TMC1 region).
  Human TMC2 is on 20p13, outside that block, so human synteny is uninformative here.
- tmc2b keeps the ancestral block: 14 of its 30 neighbours have gar orthologues within 5 Mb of gar tmc2, tmc1 among
  them.
- tmc2a has only one such neighbour (prune2). Twelve more of its neighbours map elsewhere on gar LG2, and its
  neighbourhood contains other human 9q21 genes (PRUNE2, GNAQ, GNA14, NTRK2).
- Both neighbourhoods also share a second ancestral block (gar LG21, human 9q34).

So the two zebrafish segments are built from the same two ancestral blocks, as expected for duplicated segments, but
the tmc2a segment has been rearranged and its micro-synteny is weak.

**Status.** The duplication predates the zebrafish-medaka split (PANTHER, Ensembl Compara, two medaka copies) and
postdates the split from gar (one gar gene). That fits the TGD. Two things are unusual for TGD ohnologs and are not
resolved: both copies are on the same zebrafish chromosome, and the synteny support around tmc2a is weaker than
around tmc2b. A small-scale duplication in the teleost stem cannot be excluded with the data here.

## 2. Protein-level comparison

- **Identity.** 68.0% identity and 78.5% similarity over 937 columns
  ([annotation-comparison.md](annotation-comparison.md)); published: [PMID:29269857 "Tmc2a and Tmc2b have a 69% amino acid sequence similarity."]
- **Against the outgroup.** Tmc2a is closer to gar TMC2 than Tmc2b is (71.8% versus 67.2% identity; RESULTS.md). Ensembl
  Compara gives the same picture against medaka: tmc2a is 77% identical to its one-to-one medaka orthologue, tmc2b
  68% to its own (RESULTS.md). Tmc2b has changed more since the duplication. What
  those changes do is unknown.
- **Architecture.** Both are full-length TMC proteins with the TMC domain (InterPro IPR012496) and the TM helices of
  the family (UniProt entries).
- **Partner binding.** The Tmc2a N-terminus binds the Pcdh15a cytoplasmic domain; Tmc2b binding was not tested:
  [PMID:25114259 "Tmc2a interacted with both CD1 and CD3 isoforms of Pcdh15a, demonstrating that binding is not restricted to a particular Pcdh15a isoform."]
- **Rescue.** A hair-cell Tmc2b transgene rescues all end organs of the triple mutant:
  [PMID:32371604 "The results described above (1) confirm the expectation that concurrent disruption of tmc1/2a/2b leads to complete loss of MET activity and (2) reveal that exogenous Tmc2b-mEGFP can rescue auditory/vestibular deficits and restore FM labeling in all mechanosensory end organs."]
  The reciprocal test was attempted and failed for technical reasons:
  [PMID:32371604 "The Tg(myo6b:tmc2a-mEGFP-pA) construct failed to express Tmc2a-mEGFP."]
- **Possible functional difference.** Neuromast hair cells that also express Tmc2a respond more strongly than cells
  with Tmc2b alone, and the difference disappears in tmc2a mutants:
  [PMID:36905930 "This idea is supported by our results, as we show that the calcium signals in hair bundles expressing both Tmc2b and Tmc2a are larger compared to those expressing just Tmc2b (Figure 6)."]
  [PMID:36905930 "Molecular mechanisms that may permit P-to-A sensitive hair cells to have enhanced responses are Tmc2a and Tmc2b homomerization or Tmc2a and Tmc2b heteromerization within mechanotransduction channels (Figure S6)."]
  This could be a property of the Tmc2a protein or simply more channel subunits in those cells; the data do not
  separate the two.

**Does each copy keep the ancestral molecular function?** Yes, both are MET channel subunits: each is required for
transduction in some hair cells, and Tmc2b alone can support transduction in every organ. Whether Tmc2a alone can
do the same is untested.

## 3. Expression

- **Hair cells only, both copies.**
  [PMID:25114259 "In contrast to the broad expression pattern of pcdh15a in the larval brain and sensory hair cells ( 5 ), expression of tmc1 , tmc2a , and tmc2b genes was restricted to hair cells of the inner ear and lateral line organ"]
- **Organ bias.**
  [PMID:25114259 "However, semiquantitative PCR with larval tissues suggests that tmc2a is expressed predominantly in the inner ear, whereas tmc1 and tmc2b appear to be more abundant in lateral-line hair cells."]
  [PMID:25114259 "In the lateral-line neuromasts, only tmc2b was robustly detected by in situ hybridization"]
- **Within the lateral line.** tmc2a is only in hair cells of one orientation:
  [PMID:36905930 "Interestingly, Tmc2b and Tmc2a proteins, which constitute the mechanotransduction channels in neuromasts, distribute asymmetrically so that Tmc2a is expressed in hair cells of only one orientation."]
- **Within the ear (HCR, 1-15 dpf).** Zonal split with overlap:
  [PMID:38035267 "tmc1, tmc2b, and cib3 are largely expressed in peripheral or extrastriolar hair cells, whereas tmc2a and cib2 are enriched in central or striolar hair cells."]
  [PMID:38035267 "Our data indicate that the top layer largely expresses tmc2a, whereas the bottom layer of hair cells expresses all three tmc paralogues (Figure 4E)."]
  [PMID:37952940 "The expression of tmc2b was also observed in a subset of hair cells within the striolar region that overlapped with tmc2a expression ( Fig. 3 C )."]
- **Different regulators.** tmc2a behaves as an ear gene that prdm1a represses in the lateral line; tmc2b does not:
  [PMID:40825768 "In prdm1a mutants all lateral line hair cells express tmc2a, suggesting that mutant lateral line hair cells acquired an ear hair cell fate (Fig. 2p)."]
  [PMID:40825768 "On the other hand, the paralog tmc2b is highly expressed in the sibling and prdm1a mutant lateral line hair cells, suggesting that it is not regulated by prdm1a (Supplementary Fig. 2l)."]
  Esrp1/2 stabilize tmc2a but not tmc2b mRNA:
  [PMID:40086870 "Meanwhile, our data demonstrated that Esrp1/2 regulates the mRNA stability of tmc1 and tmc2a but not tmc2b ."]
- **Public resources.** ZFIN curated records place both copies in the ear and neuromasts; Bgee has no calls for tmc2a
  and three for tmc2b (neuromast hair cell by in situ; low bulk RNA-seq calls in muscle and tail that are not
  hair-cell resolved) ([expression_output.txt](../../../../genes/DANRE/tmc2a/tmc2a-bioinformatics/expression_output.txt)).
- **Pre-duplication state.** Not measured in gar. In mouse, Tmc2 is expressed in vestibular hair cells, at lower
  levels than Tmc1, and is not detected in adult cochlear hair cells. Mammals have no lateral line.
  [PMID:39773557 "Tmc2 expression increases during development but remains below Tmc1 levels in both type I and type II hair cells upon maturation (Figure 1C)."]
  [PMID:39484049 "Tmc2 is not detected in adult mouse HCs; however, both tmc2a and tmc2b are highly expressed in zHCs with expression values greater than tmc1."]

The copies overlap in many cells. The difference is in which cells each dominates, and it is set by different
regulators (prdm1a, Esrp1/2).

## 4. Experimental evidence of function

**Alleles**

| Gene | Allele | Lesion | Type | Source |
|---|---|---|---|---|
| tmc2a | cwr3 | CRISPR 2-bp deletion, exon 6 | PTC | PMID:29269857 |
| tmc2a | cwr6, cwr7 | CRISPR indels | PTC | PMID:32167554, PMID:33490059 |
| tmc2a | Ex4 −23bp | TALEN deletion, exon 4 | frameshift/PTC | PMID:32371604 |
| tmc2b | TALEN allele | frameshift, predicted 148-aa product | PTC | PMID:29269857 |
| tmc2b | cwr2, cwr8 | CRISPR deletions | PTC | PMID:29269857, PMID:32167554 |
| tmc2b | sa8817 | ENU nonsense | PTC | PMID:32371604 |

None of these alleles was characterized for mutant mRNA decay. No RNA-less allele exists for either gene.

**tmc2a**

- Hearing: reduced saccular microphonics; the main hearing Tmc:
  [PMID:32371604 "Interestingly, the tmc2a single mutants ( n = 8) had significantly reduced microphonic signals compared with WT siblings ( n = 7) and were the only single-gene mutants with such a deficit"]
  [PMID:32371604 "Together, these results demonstrate a Tmc2a > Tmc2b > Tmc1 hierarchy in the detection of sound."]
- Cristae: upper-layer hair cells need Tmc2a:
  [PMID:32371604 "Together, our experiments reveal that, in cristae, hair cells stratify into an upper, Tmc2a-dependent layer of teardrop-shaped cells, and a lower, Tmc1/2b-dependent tier of gourd-shaped cells."]
- Utricle: high-frequency sensitivity:
  [PMID:37952940 "We found that Tmc2a function correlates with the broadest range of frequency sensitivity, whereas Tmc2b mainly contributes to lower-frequency responses."]
- Lateral line: loss of the response asymmetry between hair-cell orientations:
  [PMID:36905930 "Remarkably, loss of Tmc2a does not impact hair cell orientation but abolishes the functional asymmetry as measured by recording extracellular potentials and calcium imaging."]

**tmc2b**

- Lateral line: most hair cells lose transduction, hearing is normal:
  [PMID:29269857 "94 ± 1.2% (n = 55) of control hair cells loaded fluorophore; in contrast, 35 ± 1.8% (n = 48) of tmc2b −/− hair cells loaded (Fig. 3d), confirming Tmc2b is absolutely required for a subpopulation of hair cells within a single neuromast."]
  [PMID:29269857 "In mutants, no defects in hair bundle morphology (Supplementary Fig. 2a–d) or hearing (Supplementary Fig. 2f, g) were observed."]
- Vestibular: the main copy for the utricle:
  [PMID:32371604 "The two double-mutant combinations that gave rise to a deficit included the tmc2b sa8817 allele, suggesting that Tmc2b is the primary contributor to vestibular end organ function."]

**Both copies**

- Lateral line: the double mutant abolishes all transduction, and the residual activity of tmc2b mutants depends on
  tmc2a:
  [PMID:29269857 "Overall, these findings indicate that the residual activity in the tmc2b −/− mutant is dependent on Tmc2a."]
  [PMID:32167554 "Since it is known that lateral line function is wholly dependent on Tmc2a and Tmc2b, our results demonstrate that normal hearing uses at least one protein beyond that used by the lateral line, Tmc1 ( Fig. 10 )."]
- Ear: the double mutant hears intermittently, and the triple (with tmc1) is deaf:
  [PMID:32167554 "By examining tmc2b cwr2 tmc2a cwr3 double and tmc2b cwr8 tmc1 cwr4 tmc2a cwr6 triple mutants, we demonstrate that the double mutant has attenuated hearing attributable to diminished mechanotransduction, but the triple mutant is deaf owing to extinguished mechanotransduction"]
  [PMID:32371604 "While tmc2b single mutants do not have a significant reduction in microphonic potentials, the reduction in tmc2a/2b double mutants ( p = 0.0001; n = 6; t = 6.77; df = 8.43) is more severe than when tmc2a alone is disrupted ( Fig. 7 A )."]
- Compensation: no upregulation of tmc2a or tmc1 in tmc2b mutants, and none of tmc2a or tmc2b in tmc1 mutants:
  [PMID:29269857 "These findings indicate that these genes are not upregulated in response to genetic inactivation of tmc2b."]
  [PMID:32167554 "Expression of tmc2a mRNA or tmc2b mRNA in the tmc1 mutants did not increase and was similar to controls ( Supplementary Material, Figure S2 )."]
  Paralog upregulation in tmc2a mutants was not reported.

## 5. Fate classification

**PARTITION, at the expression level, with overlap and shared work in co-expressing cells. Confidence: moderate.**

**Established**

- Each copy has hair-cell populations that depend mainly on it: tmc2b for most lateral-line cells and utricular
  low-frequency function; tmc2a for upper-layer crista cells, saccular hearing and utricular high frequencies.
- These populations match where each copy is expressed, and the two copies are set by different regulators.
- In cells that express both, the copies share the work: double mutants are worse than either single mutant in the
  lateral line and saccule.
- The Tmc2b protein can support transduction in all end organs.

**Inferred, not shown**

- That the Tmc2a protein is equivalent to Tmc2b. The only reciprocal construct failed to express, and Tmc2a-bearing
  cells have larger responses. If Tmc2a proves to change channel properties, the pair becomes MIXED.
- That the ancestral gene was expressed in all of these cells (no gar data).
- TGD origin (see section 1).

**Why not the other fates**

- *Backup:* each single mutant has its own deficit.
- *Dosage:* the copies are not co-expressed at similar levels in the same cells; single-mutant defects map to
  expression domains, not to a uniform dose reduction.
- *Innovation:* no function outside the ancestral MET role.

**What would change the call**

- A working Tmc2a transgene that fails to rescue Tmc2b-only neuromast cells, or single-channel recordings showing that
  Tmc2a changes conductance, would add a protein-level component (MIXED).
- Gar tmc2 expression restricted to the ear would make the lateral-line domain of tmc2b a gain.

## 6. GO annotation consistency across the pair

Source: [annotation-comparison.md](annotation-comparison.md), after both reviews.

**Shared, and handled the same way on both copies.**

- The IBA rows from the PANTHER TMC nodes: mechanosensitive ion channel activity (ACCEPT), sound detection (ACCEPT),
  plasma membrane (ACCEPT), vestibular reflex (KEEP_AS_NON_CORE) and voltage-gated calcium channel activity (MODIFY
  to GO:0140135, mechanically gated; same change as in the human TMC1 review, with a propagation_review). The IEA
  rows (membrane, calcium and ion transport) were treated alike.
- Same-node IBA is appropriate for this pair: both copies are MET channel subunits. The zebrafish genes appear among
  the IBA sources for sound detection, which is expected.
- The GO:0050910 rows from Chou et al. 2017 (tmc2a/tmc2b double mutant on both copies; tmc2b single mutant) were
  modified to GO:0050974 on both. That paper tested the lateral line, which detects water motion, not sound, and
  found that tmc2b single mutants hear normally.

**Asymmetric, and correctly so.**

- tmc2a carries the cellular response to mechanical stimulus IMP (crista short hair cells) and the Pcdh15a binding
  IPI (modified to cadherin binding). The binding was only tested for Tmc2a.
- tmc2b gets the NEW stereocilium tip location (IDA). Tmc2b-GFP has been imaged at stereocilia tips; the Tmc2a
  transgene never expressed.

**Asymmetries that come from which copy was studied.**

- The ISS rows from mouse Tmc2 (calcium channel activity, mechanosensitive ion channel activity) are on tmc2a only,
  because UniProt curated only the tmc2a entry by similarity. Both apply to tmc2b equally.
- Both reviews record the channel function as `contributes_to_molecular_function` (GO:0140135); the comparison table
  lists no core molecular functions because the script reads only the `molecular_function` slot.

- IEP-based development rows (lateral line development, inner ear receptor cell development on tmc2a; inner ear
  morphogenesis, inner ear development, neuromast development on tmc2b) were all removed. They record expression, not
  developmental roles, and hair bundles form normally in tmc triple mutants.
- The hearing-specific experimental rows are thin on both copies. The strongest data (PMID:32371604, PMID:32167554)
  are not in GOA for either gene.

**Should be copy-specific:** none at the GO term level. The partition is between hair-cell types, which GO process
terms (hearing, lateral line, vestibular) capture only coarsely. Both copies take part in all three to different
degrees.
**Should be shared:** channel activity, stereocilium tip location, mechanosensory detection.

## 7. Open questions

- Can a stable Tmc2a transgene rescue tmc2b mutant lateral-line cells, and the tmc triple mutant?
- Do Tmc2a and Tmc2b form heteromeric channels, and does Tmc2a change conductance or calcium permeability?
- Are the medaka copies on different chromosomes, and does a gar-anchored double-conserved-synteny analysis support
  the TGD for this pair?
- Is tmc2a upregulated in tmc2b mutants (not tested), or tmc2b in tmc2a mutants?
- Where is tmc2 expressed in gar (ear only, or also the lateral line)?

## References

PMID:25114259, PMID:29269857, PMID:32167554, PMID:32371604, PMID:33490059, PMID:36905930, PMID:37952940,
PMID:38035267, PMID:40086870, PMID:40825768. Also `panther_tgd_pairs.tsv`,
[annotation-comparison.md](annotation-comparison.md),
[tmc2a-bioinformatics/RESULTS.md](../../../../genes/DANRE/tmc2a/tmc2a-bioinformatics/RESULTS.md) and
[expression_output.txt](../../../../genes/DANRE/tmc2a/tmc2a-bioinformatics/expression_output.txt).
