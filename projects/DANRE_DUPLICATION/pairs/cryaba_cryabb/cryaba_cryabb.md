---
title: "cryaba / cryabb"
autolink_gene_symbols: false
---

# cryaba / cryabb

[Back to pairs](../README.md)

**Bottom line:** MIXED. At the expression level the split is asymmetric. In adults,
cryaba is lens-restricted, while cryabb keeps the broad, stress-inducible expression
of the single tetrapod gene. At the protein level, both copies keep the ancestral
sHSP chaperone function, but its strength differs between them, and the direction
of that difference depends on the assay. In the lens, the two copies share one
dosage-sensitive job rather than backing each other up: each single null mutant has
lens defects, heterozygotes are affected, and there is no transcriptional
compensation. Neither INNOVATION nor BACKUP is supported. Whether the pair comes
from the TGD is not settled. The duplicate is older than zebrafish, since
otomorph fishes also have both copies, but percomorphs keep only the cryaba-type
copy. The pre-duplication (gar) expression pattern is unknown, so a strict
sub- vs neofunctionalization call cannot be made.

| | cryaba | cryabb |
|---|---|---|
| UniProt | Q9PUR2 | A0A8M9Q8E3 |
| Other names | alphaB1-crystallin, αBa, cryab, hspb5a | alphaB2-crystallin, αBb, cryab2, zgc:91937, hspb5b |
| Human ortholog | CRYAB (HSPB5); PANTHER least-diverged ortholog | CRYAB (HSPB5) |
| Chromosome (Ensembl 116) | 15 | 5 |
| Length | 168 aa | 180 aa |
| Review | [genes/DANRE/cryaba](../../../../genes/DANRE/cryaba/cryaba-ai-review.yaml) | [genes/DANRE/cryabb](../../../../genes/DANRE/cryabb/cryabb-ai-review.yaml) |

**Naming.** The literature uses several names for each copy. The first zebrafish
alphaB-crystallin to be cloned (Posner 1999) is cryaba. Its mRNA, AF159089 /
AAD49096, is cross-referenced in the cryaba UniProt entry
(`genes/DANRE/cryaba/cryaba-uniprot.txt`). The lens proteome table gives the same
protein accession for αBa
[PMID:18449354 "αBa2.56±0.25 4AAD49096"]. The second copy, cryab2 or alphaB2
(Smith 2006), is cryabb. "cryab2" and "zgc:91937" are synonyms in the cryabb UniProt
entry (`genes/DANRE/cryabb/cryabb-uniprot.txt`). Elicker & Hutson 2007 call the
pair hspb5a/hspb5b. We map hspb5a to cryaba and hspb5b to cryabb by inference: the
paper's synteny statements (section 1) match those that Posner et al. make for
cryaba and cryabb.

## 1. Evidence the pair comes from the TGD

**PANTHER v19** (row in `../../panther_tgd_pairs.tsv`):

| tgd_call | duplication_branch | pair_class | family | gar co-orthologs | medaka co-orthologs | medaka parallel dup |
|---|---|---|---|---|---|---|
| TGD_or_lineage | Teleostei\|DANRE | 1:1 | PTHR45640 (HEAT SHOCK PROTEIN HSP-12.2-RELATED) | 1 (shared by both copies) | 1 | no |

PANTHER puts the duplication on the zebrafish terminal branch. Both copies share a
single gar co-ortholog, and medaka has one gene. PANTHER samples only zebrafish
and medaka among teleosts, so it cannot tell a TGD with loss in medaka apart from
a duplication in the zebrafish lineage alone.

**Ensembl Compara (release 116)**, from `ensembl_check.py` → `ensembl_check.md` in
this folder:

- Compara places the cryaba–cryabb duplication node at **Clupeocephala**. It is
  not a zebrafish-specific duplication (`ensembl_check.md`).
- **Both copies**, as 1:1 orthologs of each, are found in Atlantic herring
  (Clupeiformes), Mexican tetra and red-bellied piranha (Characiformes), and
  channel catfish (Siluriformes). Common carp, which had its own extra WGD, has
  two of each. So the pair is shared across Otomorpha.
- **Percomorphs** (medaka, stickleback, fugu, tilapia) have a single gene. Compara
  calls it the 1:1 ortholog of **cryaba**, which means the cryabb-type copy was
  lost on the lineage leading to percomorphs. This agrees with PANTHER's single
  medaka co-ortholog.
- The two osteoglossomorphs (Asian arowana, elephantfish) and spotted gar each have
  one gene that is one-to-many with both zebrafish copies. In other words, it falls
  outside the duplication in the Compara tree.
- **Double-conserved synteny:** none detected. Among the 52 protein-coding genes
  within ±1.5 Mb of cryaba, none has a teleost-level zebrafish paralog within
  ±1.5 Mb of cryabb. This scan was not validated against a known TGD pair, so it is
  weak negative evidence.

**Published synteny and gene-family work:**

- cryabb sits in the ancestral CRYAB neighbourhood (next to hspb2); cryaba does not:
  [PMID:36572168 "One of the protein paralogs, αBb-crystallin, retains the broad expression of the mammalian ortholog in adults, shares 58.2% amino acid identity with humans and its gene (cryabb) shares the syntenic relationship with the neighboring small heat shock protein hspb2"]
  [PMID:36572168 "The second zebrafish paralog, αBa-crystallin, is expressed primarily in the lens of adults, unlike its mammalian ortholog, is 61.7% identical to the human protein and does not share its syntenic relationship"]
- The genome-wide sHSP survey found the same thing, and still supported orthology
  of the hspb5a region at a larger scale:
  [PMID:17888590 "while zebrafish hspb5b and human HSPB5 share the same two immediate neighbors, zebrafish hspb5a and human HSPB5 share only one of two nearby neighbors."]
  [PMID:17888590 "Of the six genes that map to within 100kbp of zebrafish hspb5a , however, five are within 6.7Mbp of HSPB5 , supporting the argument for their orthology."]
- This is the only sHSP gene with two zebrafish co-orthologs:
  [PMID:17888590 "that only HSPB5 has paired orthologs in the zebrafish."]
- The original report described the pair as unique:
  [PMID:16420472 "Zebrafish is the first species known to express two different alphaB-crystallins."]
- A 2025 review states TGD origin as fact. It cites Smith 2006 and Mishra 2018,
  neither of which tests it:
  [PMID:40206405 "However, there are two cryab genes, cryaba and cryabb, due to ancestral teleost genome duplication"]

**What is and is not established**

- *Established.* The duplication happened before the zebrafish lineage split from
  other otomorphs. Percomorphs kept only the cryaba-type copy. Only cryabb keeps the
  ancestral hspb2 neighbourhood.
- *Not established.* Whether the duplication is the TGD itself, or an early post-TGD
  duplication in the ancestor of Clupeocephala. Three observations bear on this:
  - The Compara node (Clupeocephala, with the osteoglossomorph genes outside it)
    fits a post-TGD duplication.
  - It is also the gene-tree signature expected when homeologs were resolved
    separately in each lineage after delayed rediploidization:
    [PMID:35961774 "In the LORe model, because cytological rediploidization has not been resolved before speciation occurs, ohnologs share more sequence similarity within clades than across clades, and can therefore be misidentified as clade-specific duplications."]
  - cryaba sits on a chromosome segment without detectable double-conserved
    synteny, which could also reflect a transposition.

  Treat the pair as a **probable TGD or early-teleost pair**. The
  otomorph/percomorph distribution rules out a young zebrafish-specific tandem
  duplicate, but it is not formal TGD support.

## 2. Protein-level comparison

- **Identity.**
  - Global alignment between the copies: 46.3% identity, 63.3% similarity
    (`annotation-comparison.md`).
  - Published figures for identity with human CRYAB are 61.7% for αBa and 58.2%
    for αBb. The copies are about 50% identical to each other:
    [PMID:16420472 "The deduced protein sequence was 58.2% and 50.3% identical with human alphaB-crystallin and zebrafish alphaB1-crystallin, respectively."]
  - Note that Koteiche et al. say αBb is closer to human than αBa is, but they
    give only the αBb figure:
    [PMID:26378715 "Interestingly, αBb is more similar to human αB (58% identity) than to its paralog αBa (50% identity)."]
  - With αBa at 61.7% (PMID:36572168, quoted above), **neither copy is clearly
    the more diverged in sequence**.
- **Domains.** Both have the full sHSP architecture: the N-terminal crystallin
  region, the α-crystallin domain, and the C-terminal extension (UniProt, InterPro
  entries in both `*-uniprot.txt` files). There is no domain gain or loss.
- **Motifs.**
  - cryaba lacks C-terminal residues implicated in partner binding and has
    substitutions at phosphorylation sites:
    [PMID:10542326 "The deduced amino acid sequence of zebrafish alphaB-crystallin revealed that it lacked four residues in the C-terminus implicated in protein-protein interactions in other vertebrate species."]
    [PMID:10542326 "In addition, the sequence contained two substitutions at sites implicated in phosphorylation in other vertebrate species."]
  - The copies keep different numbers of the three phospho-switch sites:
    [PMID:26378715 "Zebrafish αBa and αBb contain only one and two of the three consensus phosphorylation sites found in human αB62, respectively (Figure S1)."]
  - Neither copy is detectably phosphorylated in the adult lens:
    [PMID:18449354 "No phosphorylated αBa- or αBb-crystallin was found."]
- **Chaperone activity.** Both copies are active chaperones, but studies disagree
  on the direction of the difference between them. That disagreement is the key
  protein-level issue for this pair.
  - *Aggregation-suppression assays* reported that αBa (then called
    "alphaB-crystallin") is weak:
    [PMID:15692462 "The chaperone-like activities of the two zebrafish alpha-crystallins were highly divergent, with alphaA-crystallin showing much greater activity than alphaB-crystallin."]
  - The same kind of assay found αBb stronger than human CRYAB at the zebrafish's
    physiological temperature:
    [PMID:16420472 "At 25 degrees C and 30 degrees C, zebrafish alphaB2 showed greater chaperone-like activity than human alphaB-crystallin, and at 35 degrees C and 40 degrees C, the human protein provided greater protection against aggregation."]
  - *Equilibrium substrate-binding assays* (destabilized T4 lysozyme) reversed the
    αBa ranking. Both paralogs bind more strongly than human αB, and αBa binds most
    strongly:
    [PMID:26378715 "The zebrafish paralogs showed substantially elevated binding with respect to human αB (Figure 5b)."]
    [PMID:26378715 "However, variations in activity within the zebrafish αB chains were also apparent in which αBa-S bound the destabilized substrate with an order of magnitude higher affinity and with greater capacity than αBb (Table 5)."]
    [PMID:26378715 "Both of these observations disagree with previously reported results47, 55."]
  - The authors propose that αBa lost its phosphorylation switch and became
    constitutively activated:
    [PMID:26378715 "In light of results presented here, significant variations in the primary sequence of zebrafish αBa may have resulted in the loss of a phosphorylation “switch” and contributed to the generation of a chaperone with constitutively enhanced activity."]
  - The "nonchaperone" reading of αBa in Smith 2006 therefore rests on
    aggregation-assay data that a later binding assay contradicts:
    [PMID:16420472 "zebrafish alphaB2 maintained the widespread protective role also found in mammalian alphaB-crystallin, while zebrafish alphaB1 adopted a more restricted, nonchaperone role in the lens."]
    [PMID:26378715 "This led to the hypothesis that αBa has little utility as a chaperone in the lens."]
- **Cross-rescue.** Not tested. The only rescue reported is same-copy: a
  lens-specific cryabb transgene partly rescued cryabb mutants (section 4).

**Conclusion (protein level).**

- *Established:* both copies keep the ancestral molecular function, ATP-independent
  holdase chaperone activity. There is no evidence of loss of function or of a new
  activity.
- *Inferred:* the chaperone has been quantitatively tuned (oligomer size,
  phospho-sites, possibly constitutive activation of αBa). This is modification of
  an existing function, not a new one, and its direction depends on the assay.

## 3. Expression

**Adult tissues**

- cryaba is essentially lens-restricted:
  [PMID:10542326 "Northern analysis and semi-quantitative RT-PCR indicate that zebrafish alphaB-crystallin is expressed at extremely low levels outside of the lens."]
  [PMID:16420472 "We previously reported that zebrafish alphaB-crystallin is not constitutively expressed in nervous or muscular tissue and has reduced chaperone-like activity compared with its human ortholog."]
- cryabb is mostly in the lens, with the broad tissue distribution of mammalian
  CRYAB:
  [PMID:16420472 "RT-PCR showed that alphaB2-crystallin is expressed predominantly in lens but, reminiscent of mammalian alphaB-crystallin, also has lower constitutive expression in heart, brain, skeletal muscle and liver."]
- Other authors describe the partition the same way:
  [PMID:26378715 "Whereas αBa expression is limited to the lens in adults, αBb mimics the ubiquitous extra-lenticular expression pattern of human αB, which suggests varying physiological roles."]

**Lens protein abundance**

- αBa is more abundant than αBb in the adult lens:
  [PMID:18449354 "Total α-crystallin content in the lens was 7.8% with a 6.4:3.6:1 ratio of αA:αBa:αBb"]
  [PMID:18449354 "The higher expression of the lens specific αBa-crystallin compared to the ubiquitous αBb-crystallin (2.56% and 0.72%, respectively) suggests that αBa-crystallin plays a more prominent role in the zebrafish lens."]
- The two published estimates for αBb differ (0.72% here, 0.16% below):
  [PMID:16420472 "2D gel electrophoresis indicated that alphaB2-crystallin makes up approximately 0.16% of total zebrafish lens protein."]

**Embryos and larvae.** The adult partition is not seen early in development.

- Both copies are expressed in the lens, heart, brain and otic vesicle at 2 dpf:
  [PMID:29162721 "As expected, we observed the expression of αBa and αBb in the lens of 2-dpf embryos, as well as in the hearts, albeit with lower staining signal"]
  [PMID:29162721 "In addition, both genes were broadly expressed in the brain region and showed particularly enriched expression in the otic vesicles"]
- Single-cell data put both mainly outside the eye until about 5 dpf:
  [PMID:40206405 "In contrast cryaba and cryabb genes are predominantly expressed in non-ocular tissues during the zebrafish embryonic and (0–72 hpf) early larval (72–120 hpf) phases"]
  [PMID:40206405 "In zebrafish embryos, while cryaa is predominantly expressed in the developing lens, cryaba and cryabb are expressed in other cells including muscle progenitor cells and the primordial heart by 48 hpf"]
- Lens expression of both rises only after 10 dpf:
  [PMID:38705506 "with 5 and 6 dpf lenses expressing cryaa almost exclusively, and expression of cryaba and cryabb becoming more prominent after 10 dpf"]
- The EST distribution is lens-dominated for both:
  [PMID:17888590 "Not surprisingly, the lens α-crystallins, hspb4, hspb5a , and hspb5b are found predominantly in lens libraries."]

**Stress regulation (a copy-specific difference)**

- Only cryabb responds to oxidative or glucocorticoid stress:
  [PMID:37577747 "we uncovered a transcriptional relationship that leads to a substantial increase in αBb-crystallin transcripts in the heart in response to compromised function of Nrf2."]
  [PMID:37577747 "Taken together, these results suggested a transcriptional link between nrf2 and cryabb but not cryaba."]
  [PMID:37577747 "Our data suggest that cryabb functions as a stress–response gene regulated by both glucocorticoid stress and oxidative stress."]
- Neither copy was among the sHSPs induced by heat shock in embryos:
  [PMID:17888590 "Five of the thirteen sHSPs, hspb1, hspb4, hspb8, hspb9 , and hspb11 , were found to be upregulated by heat shock."]

**Ancestral state**

- The tetrapod single-copy gene is broadly expressed:
  [PMID:29162721 "αB-crystallin (Cryab or HspB5) is a small heat shock protein (sHSP) 3 that is expressed in multiple tissues and organs, including the lens, heart, and skeletal muscles"]
- No gar, osteoglossomorph or percomorph cryab expression data were found in the
  literature searched. The percomorph single copy is the cryaba ortholog, so its
  expression would be a useful test of whether lens restriction is specific to the
  cryaba lineage or to zebrafish.

**Summary.** Shared domains are the lens (both, at all stages examined) and the
embryonic heart and brain (both). Copy-specific: adult extra-lenticular
expression and stress inducibility belong to cryabb. cryaba has no domain of its
own. Measured against tetrapods, this is **asymmetric**. cryabb looks like the
"generalist" that keeps nearly all ancestral domains, and cryaba like a lens
"specialist" that lost adult extra-lenticular expression. That fits
degenerative loss in cryaba (the partition side of DDC), but cryabb has not
reciprocally lost anything identifiable. Caution is warranted:
[PMID:35253876 "There is a tendency in the literature to ascribe subfunctionalization to any case in which duplicate genes have somewhat different expression patterns."]

## 4. Experimental evidence of function

**cryaba**

- *CRISPR mutant (Mishra 2018):* first-exon frameshift (35-bp deletion). The mRNA
  escaped NMD, but no protein was detected.
  [PMID:29162721 "Unexpectedly, results from qRT-PCR suggested that the mRNAs encoded by the α B mutant alleles did not undergo significant NMD despite premature stop codons introduced in the first exons."]
- *Mishra 2018, lens:* defects in about 75% of homozygous larvae, and
  heterozygotes are also affected:
  [PMID:29162721 "We observed lens abnormalities in the mutant lines of both genes, and the penetrance of the lens phenotype was higher in αBa than αBb mutants."]
  [PMID:29162721 "Interestingly, a gene dosage effect was observed in α Ba and α Bb genes."]
- *Mishra 2018, heart:* pericardial edema under crowding or glucocorticoid stress,
  similar to cryabb mutants (see the shared phenotypes below).
- *Posner 2023, second CRISPR line:* no early lens defects:
  [PMID:36572168 "Loss of αBa-crystallin produced no substantial lens defects."]
- *Aging:* loss of cryaba increases cataract:
  [PMID:38705506 "Surprisingly, unlike mouse knockout models, we found that the loss of the αBa-crystallin gene cryaba led to an increase in lens opacity compared to cryaa null fish at 24 months of age."]
- *Interaction with nrf2:* in the lens, nrf2 loss suppresses the cryaba lens
  phenotype through cholesterol synthesis:
  [PMID:37577747 "In the lens, the concomitant loss of function of Nrf2 and αBa-crystallin leads to upregulation of the cholesterol biosynthesis pathway"]

**cryabb**

- *CRISPR mutant (Mishra 2018):* first-exon frameshift (10-bp deletion). Lens
  defects in about 50% of larvae, and the heart shows a baseline effect.
  [PMID:29162721 "We found that, compared with the WT, α Bb mutants exhibited a slower heart rate (∼10% decrease) at 1 dpf"]
  [PMID:29162721 "In contrast, treatment with dexamethasone significantly reduced (∼50%) the ventricular shortening fraction of the α Bb mutants when compared with non-treated α Bb mutants"]
- *Same-copy rescue:* a lens-specific cryabb transgene partly rescued the lens
  defect:
  [PMID:29162721 "Finally, lens-specific expression of zebrafish αBb (Tg[ cryabb ]) also partially alleviated the lens defects of αBb mutant embryos ( Fig. 6 B )"]
- *Posner 2023:* its cryabb allele makes a truncated protein and had no lens
  phenotype. The allele may be hypomorphic:
  [PMID:36572168 "Our cryabb mutant produced a truncated αBb-crystallin protein and showed no substantial change in lens development."]

**Shared phenotypes and double mutants**

- *Heart stress:* both single mutants are hypersensitive, and the lens/heart
  ranking of the two copies is reversed:
  [PMID:29162721 "The αB-crystallin mutants exhibited hypersusceptibility to develop pericardial edema when challenged by crowding stress or exposed to elevated cortisol stress, both of which activate glucocorticoid receptor signaling."]
  [PMID:29162721 "Interestingly, a difference in sensitivity to loss of αBa and αBb was also observed in the heart that is opposite to the lens phenotype ( Fig. 3 B )."]
  [PMID:29162721 "This may be a consequence of the higher level of αBb compared with αBa in the cardiomyocytes at 4-dpf embryos ( 77 )."]
  - Nrf2 loss makes the edema more penetrant:
    [PMID:37577747 "By contrast, abrogation of Nrf2 function accentuates the penetrance of a heart edema phenotype characteristic of embryos of αB-crystallin knockout lines."]
- *Double mutant (lens):* only a modest increase over the cryaba single mutant.
  This is weak synergy, not strong redundancy.
  [PMID:29162721 "Compared with the single mutant, particularly α Ba −/− , the frequency of major lens defects increased moderately in α Ba /α Bb double mutants (by about 10%), but the overall penetrance was not significantly changed"]
- *Viability:* double mutants are viable and fertile.
  [PMID:29162721 "Indeed, αB-crystallin double mutant fishes (α Ba −/− ; α Bb −/− ) are viable and fertile as adults."]
- *Muscle:* the morpholino phenotypes were not reproduced in the mutants.
  - Bührdel et al. reported that morpholino knockdown of MFM genes, including the
    cryab genes, caused muscle and heart failure:
    [PMID:25866181 "Consistently, targeted ablation of MFM genes in zebrafish led to compromised skeletal muscle function mostly due to myofibrillar degeneration as well as severe heart failure."]
  - The CRISPR nulls, including the double, had no skeletal-muscle phenotype:
    [PMID:29162721 "we conclude that αB-crystallin genes are largely dispensable for muscle and heart development during embryogenesis"]
    [PMID:29162721 "Furthermore, we found no evidence of compromised skeletal muscle functions in both αB-crystallin mutants, unlike the severe muscular phenotypes shown in a previous study using morpholino knockdown strategies ( 48 )."]

**Compensation (none at the transcript level)**

- Mishra 2018:
  [PMID:29162721 "However, we observed no significant change (<1.6 cycle difference ( 46 )) of αBb expression in αBa mutant embryos and vice versa"]
- Posner 2023:
  [PMID:36572168 "Mutation of each α-crystallin gene did not alter the mRNA levels of the remaining two, suggesting a lack of genetic compensation."]
- Posner 2024:
  [PMID:38705506 "None of the three α-crystallin mutants showed a compensatory increase in the expression of the remaining two crystallins"]
- The only hint of compensation is a small rise in αBa protein in cryabb mutant
  lenses:
  [PMID:29162721 "suggesting a possible compensatory response to the loss of αBb protein"]

**Allele caveats.**

- All alleles are PTC-type (first-exon frameshifts). None is RNA-less.
  [PMID:36572168 "The cryaba and cryabb mutant lines were not produced by deleting the promoter and start codon but instead were produced with a single gRNA producing frame shift mutations and early stop codons"]
- Mishra's mRNAs escaped NMD, which should limit the transcriptional-adaptation
  route described for NMD-triggering alleles
  [PMID:30944477 "Therefore, use of RNA-less alleles can uncover phenotypes not observed in alleles exhibiting mutant mRNA degradation."]
- The two labs disagree on the larval lens phenotype, and the reason is unknown:
  [PMID:36572168 "The reason for the discrepancy in our present CRISPR work and the past study identifying lens defects in cryaba and cryabb knockout zebrafish (Mishra et al., 2018) is unclear."]

## 5. Fate classification

**MIXED: asymmetric expression partition, plus shared dosage in the lens, with
protein-level tuning of a conserved function.**

| Level | Call | Evidence | Confidence |
|---|---|---|---|
| Molecular function | Conserved in both (not INNOVATION) | Both copies bind and hold destabilized substrates, and both do so more strongly than human αB (PMID:26378715); both have chaperone-like activity (PMID:15692462, PMID:16420472) | High |
| Protein tuning | Quantitative divergence; direction depends on assay | αBa is weakest in aggregation assays (PMID:15692462) but strongest in binding assays (PMID:26378715); the copies retain different phospho-sites (PMID:26378715) | Medium for "they differ"; low for the direction |
| Expression | Asymmetric partition. cryaba is an adult lens specialist; cryabb keeps broad, stress-inducible expression | PMID:10542326, PMID:16420472, PMID:37577747. Early embryonic expression overlaps (PMID:29162721, PMID:40206405) | Medium. Judged against tetrapods, not gar |
| Lens | Shared, dosage-sensitive role (DOSAGE/partition) | Each single mutant is affected and heterozygotes are affected; the double mutant is only modestly worse; no compensation (PMID:29162721, PMID:36572168, PMID:38705506) | Medium. Contested by the negative larval data in PMID:36572168 |
| Heart | Shared stress-tolerance role, weighted towards cryabb | Both single mutants get edema; only cryabb is stress-inducible (PMID:29162721, PMID:37577747) | Low to medium |
| BACKUP | Not supported | No cross-rescue test, no paralog upregulation, and each single mutant has a phenotype | Medium |

Distinguishing what is established from what is inferred:

- **Established:**
  - Both copies make an active sHSP chaperone.
  - In adults, cryaba is expressed at very low levels outside the lens, while
    cryabb is broadly expressed.
  - Only cryabb transcription responds to Nrf2 loss and glucocorticoid.
  - Loss of either copy affects the lens in at least one lab's hands.
  - Neither copy's transcript rises when the other is mutated.
- **Inferred:**
  - That cryaba's lens restriction is a degenerative loss after duplication, as
    in DDC. The comparison is to tetrapods; no gar or percomorph expression data
    exist.
  - That αBa's constitutively "activated" chaperone state is an adaptation for the
    lens (PMID:26378715 proposes this).
  - That the heart sensitivity difference reflects expression level (PMID:29162721
    proposes this).
  - Smith 2006's conclusion that αBa has a "nonchaperone" role should be treated
    as **superseded** at the protein level by PMID:26378715 and PMID:29162721.

**Why not a cleaner call?** The pair fails the project's criteria for both clean
fates:

- *Neofunctionalization* would need a pre-duplication comparison (section 7 of the
  background page). None exists here, and no new molecular function has been shown.
- *Subfunctionalization (DDC)* needs reciprocal loss. Only cryaba has lost
  identifiable domains, and cryabb still covers the lens.

**What would change the call**

- Expression of the single-copy cryab in gar or in a percomorph (medaka or
  stickleback, whose copy is the cryaba ortholog). If the percomorph gene is
  broadly expressed, cryaba's lens restriction is specific to the zebrafish
  lineage. If it is lens-restricted, the specialization is older, and its loss of
  broad expression would call for a closer look at the cryabb lineage.
- Cross-rescue: lens- or heart-specific expression of cryaba in cryabb mutants,
  and the reverse.
- RNA-less (promoter-deletion) alleles of both copies, which would also settle the
  Mishra vs Posner larval-lens discrepancy.
- Chaperone assays run side by side on both paralogs with both methods, under the
  same conditions.

## 6. GO annotation consistency across the pair

This section summarizes `annotation-comparison.md`, regenerated after the edits
listed at the end.

- **MF: unfolded protein binding (IBA and IDA on both; MODIFY on both).**
  - Symmetric, and justified: the MF is conserved.
  - The cryaba review had described cryaba as having a "nonchaperone" or secondary
    chaperone role, and supported the cryaba IBA with a Smith 2006 sentence about
    alphaB2, which is cryabb. That was a wrong-copy citation. **Edited:** the
    cryaba review now cites PMID:26378715 and PMID:29162721 and records that the
    activity comparison is assay-dependent.
- **MF: structural constituent of eye lens (IEA).**
  - Core (ACCEPT) for cryaba; KEEP_AS_NON_CORE for cryabb.
  - The asymmetry in *emphasis* is justified: αBa is about 3.5 times more abundant
    in the adult lens (PMID:18449354), and only cryaba is lens-restricted. Both are
    lens proteins, so the term is correct on both. No edit.
- **MF: structural molecule activity (IEA, cryabb only).**
  - This is an ARBA artefact of which copy the model was applied to. It is not
    biology.
  - It is redundant with GO:0005212 on both. No edit (outside the pair question).
- **BP: maintenance of lens transparency (IMP, PMID:38705506, on both).**
  - It was ACCEPT for cryaba and KEEP_AS_NON_CORE for cryabb. The pair literature
    does not support that asymmetry.
  - Mishra 2018 shows lens defects in cryabb nulls, a dosage effect in
    heterozygotes, and partial rescue by a lens-specific cryabb transgene
    (PMID:29162721). That is stronger, copy-specific genetic evidence than the
    cryabb review cited.
  - Degree differs (αBa has greater penetrance), but the process is a core role of
    both. **Edited:** cryabb is now ACCEPT, with PMID:29162721 support, and the
    term was added to its core function.
- **BP: skeletal muscle tissue development and myofibril assembly (IMP,
  morpholino, PMID:25866181, on both).**
  - They were ACCEPT and core for cryabb, but KEEP_AS_NON_CORE for cryaba. The
    asymmetry rested on expression, not on the evidence, which is one morpholino
    paper that treated both copies the same way.
  - CRISPR nulls of each copy, and the double mutant, show no muscle phenotype
    (PMID:29162721). The morpholino result is therefore contradicted for both
    copies.
  - **Edited:** cryabb is now KEEP_AS_NON_CORE for both terms, matching cryaba, and
    both are removed from cryabb's core functions. Both reviews now cite
    PMID:29162721.
  - REMOVE was not used, because paralog-independent compensation by other sHSPs
    in muscle cannot be excluded (PMID:29162721 raises this itself).
- **BP: heart contraction (IMP, PMID:25866181).**
  - ACCEPT for cryabb; KEEP_AS_NON_CORE for cryaba. The asymmetry is partly
    justified.
  - Heart-rate and shortening-fraction data exist only for cryabb nulls
    (PMID:29162721). cryabb is the stress-inducible copy in the heart
    (PMID:37577747).
  - The edema phenotype, however, is shared, and it depends on stress.
  - **Edited:** the cryabb annotation keeps ACCEPT, now also supported by the
    PMID:29162721 null-mutant data. cryaba is unchanged, with PMID:29162721 added
    for its stress-induced edema.
- **BP: locomotory behavior (morpholino).** Non-core on both. Consistent.
- **BP: response to heat (IBA, ACCEPT, core on both).**
  - Symmetric, as expected for IBA.
  - Neither transcript is heat-inducible in embryos (PMID:17888590), but the term
    covers the holdase's protective role and not only transcriptional induction.
    No edit; flagged below.
- **BP: negative regulation of apoptotic process (IBA, non-core on both; extra ARBA
  IEA on cryabb).** Consistent.
- **CC: cytoplasm and nucleus (IBA, on both).** Consistent.
- **CC: plasma membrane (IDA, cryaba only, PMID:18406404).**
  - The asymmetry comes from which copy was studied: only αBa was immunostained.
  - Nothing shows that αBb is absent from fiber-cell membranes. It should not be
    propagated without data.
- **IBA treatment overall.** PANTHER places both copies under the same family node,
  and they receive an identical IBA set. That is correct for this pair, because the
  molecular function is conserved. None of the IBA terms needs to be copy-specific.

**Edits made in this pair review:** see the history records under
`history/genes/DANRE/cryaba/` and `history/genes/DANRE/cryabb/`.

- **cryaba.**
  - Corrected wrong-copy statements in the description and the PMID:16420472
    finding. The 0.16% lens abundance and the broad heart/brain/muscle/liver RT-PCR
    expression are data for alphaB2, which is cryabb.
  - Replaced the wrong-copy supporting quote on the IBA unfolded protein binding
    annotation.
  - Added PMID:26378715, PMID:29162721 and PMID:18449354.
  - Updated the chaperone core-function description.
- **cryabb.**
  - Maintenance of lens transparency: KEEP_AS_NON_CORE → ACCEPT.
  - Skeletal muscle tissue development and myofibril assembly: ACCEPT →
    KEEP_AS_NON_CORE.
  - Added PMID:29162721 support.
  - Updated core_functions and the description.

## 7. Open questions

1. Is the pair a TGD ohnolog pair? Answering this needs double-conserved synteny
   using the gar region around CRYAB/HSPB2, together with the otomorph genomes that
   keep both copies. The osteoglossomorph singleton outside the Compara duplication
   node needs to be explained, either by gene-tree error, by LORe, or by a
   post-TGD duplication.
2. What is the ancestral expression pattern? The single cryab of gar and of
   percomorphs (the cryaba ortholog) has not been profiled.
3. Which chaperone ranking is physiologically relevant, aggregation suppression
   (PMID:15692462) or equilibrium binding (PMID:26378715)? Can either copy
   substitute for the other in the lens or the heart (cross-rescue)?
4. Why do the Mishra 2018 and Posner 2023 larval lens phenotypes disagree? The
   candidates are allele structure (Posner's cryabb allele is truncated rather than
   null), genetic background, and scoring.
5. Should `response to heat` stay core on both copies, given that neither
   transcript is heat-inducible in embryos (PMID:17888590)? Or is
   `response to glucocorticoid` / `response to oxidative stress` a better
   cryabb-specific process? At present only transcript regulation supports those
   (PMID:37577747), which is not enough for an annotation.

## References

| PMID / file | Citation | Role here |
|---|---|---|
| PMID:10542326 | Posner et al. 1999, BBA | cryaba cloning; lens-restricted expression; C-terminal and phospho-site changes |
| PMID:15692462 | Dahlman et al. 2005, Mol Vis | αBa aggregation assay (weak) |
| PMID:16420472 | Smith et al. 2006, FEBS J | cryabb discovery; broad expression; chaperone activity; "separation of functions" |
| PMID:17888590 | Elicker & Hutson 2007, Gene | sHSP family survey; synteny; no heat induction of either copy |
| PMID:18449354 | Posner et al. 2008, Mol Vis | Lens proteome: αBa > αBb abundance; no phosphorylation |
| PMID:25866181 | Bührdel et al. 2015, BBRC | Morpholino muscle and heart phenotypes |
| PMID:26378715 | Koteiche et al. 2015, Biochemistry | Binding assays: αBa is an activated chaperone; both copies bind more strongly than human αB |
| PMID:29162721 | Mishra et al. 2018, JBC | CRISPR single and double nulls: lens, heart stress, muscle negative, no compensation |
| PMID:36572168 | Posner et al. 2023, Exp Eye Res | CRISPR nulls: no early lens defects; synteny statement |
| PMID:37577747 | Park et al. 2023, Front Mol Biosci | Nrf2 and glucocorticoid regulation of cryabb only; heart edema |
| PMID:38705506 | Posner et al. 2024, Exp Eye Res | cryaba and age-related cataract; ontogenetic shift |
| PMID:40206405 | Rossen et al. 2025, Front Cell Dev Biol (review) | Embryonic single-cell expression summary |
| PMID:35253876, PMID:30944477, PMID:35961774 | Background (see the project background page) | Caution on subfunctionalization; RNA-less alleles; LORe |
| `ensembl_check.md` (from `ensembl_check.py`) | Ensembl REST, release 116 | Duplication node, per-species orthologs, synteny scan |
| `annotation-comparison.md` | `compare_pair.py` | Protein identity; GO annotation table |
