# BioReason-Pro SFT Catalogue Evaluation

Systematic evaluation of BioReason-Pro SFT predictions from the HuggingFace
`wanglab/protein_catalogue` (223K proteins) against expert-curated AIGR gene reviews.

Source: `data/bioreason-hf/protein_catalogue.ddb`
Branch: `feat/bioreason-hf-catalogue`

## Methods

For each protein:
1. Extract SFT generation from HF catalogue → `{GENE}-deep-research-bioreason-sft.md`
2. Fetch UniProt/GOA via `just fetch-gene`
3. Deep literature research → `{GENE}-notes.md`
4. Complete expert review → `{GENE}-ai-review.yaml`
5. Evaluate BioReason trace → `{GENE}-bioreason-sft-review.md` (correctness + completeness, 1-5 scale)
6. Validate: `just validate {SPECIES} {GENE}`

## Per-Protein Results

### Round 1: DANRE, DICDI, METJA, MYCTU, PSEAE (15 proteins)

| Gene | Clade | UniProt | Correctness | Completeness | Key failure mode |
|------|-------|---------|:-----------:|:------------:|------------------|
| fen1 | DANRE | Q6TNU4 | 4 | 4 | Minor overstatement of recombination roles |
| ufsp2 | DANRE | Q7T347 | 4 | 3 | Fabricated gravitaxis phenotype claims |
| dph2 | DANRE | A4QN59 | 3 | 4 | Wrong chemistry, unsupported nuclear localization |
| nip7 | DICDI | B0G104 | 3 | 3 | Fabricated UV/DNA-damage response |
| mlcD | DICDI | Q7Z2B8 | 2 | 3 | Family-level conflation (calmodulin → myosin I LC) |
| tlcd4b | DICDI | Q550S9 | 2 | 2 | Ceramidase confusion (actually acyltransferase) |
| MJ1511 | METJA | Q58906 | **1** | 2 | Fabricated HMF catabolism, fake UniProt summary |
| nadX | METJA | Q58325 | 3 | 4 | Wrong product (oxaloacetate → iminoaspartate) |
| thiL | METJA | Q60337 | 3 | 3 | Wrong GO term, speculative metabolon |
| Rv3660c | MYCTU | P9WKX7 | 2 | 2 | Fabricated UniProt summary, missed septum function |
| Rv0898c | MYCTU | P9WKP5 | **1** | 2 | Fabricated UniProt summary + CoA narrative |
| clpP2 | MYCTU | P9WPC3 | 4 | 3 | Generic ClpP, misses Mtb heterocomplex |
| ubiE | PSEAE | Q9HUC0 | 4 | 3 | Menaquinone-biased, speculative metabolon |
| secF | PSEAE | Q9HXI2 | 4 | 4 | Minor: SecD size, protein binding as MF |
| rpsD | PSEAE | O52759 | 4 | 4 | Minor: wrong 30S subdomain name |

**Round 1 means: Correctness 2.9/5, Completeness 3.1/5**

### Round 2: ANOGA, ARATH, DROME, ECOLI, SCHPO, human, mouse, rat, worm, yeast (30 proteins)

| Gene | Clade | UniProt | Correctness | Completeness | Key failure mode |
|------|-------|---------|:-----------:|:------------:|------------------|
| NPAC | ANOGA | Q7Q161 | 3 | 3 | Speculative redox sensing on inert dehydrogenase domain |
| TDO | ANOGA | O77457 | 4 | 2 | Generic enzyme, misses all mosquito-specific biology |
| DNAAF1 | ANOGA | Q7PK92 | **1** | **1** | Complete mischaracterization as signaling scaffold; never mentions dynein |
| At1g67980 | ARATH | Q9C9W3 | 3 | 2 | Hallucinated GO ID (GO:0047554), wrong product, ignored Class II paralog divergence |
| NEK3 | ARATH | Q8RX66 | 2 | 2 | Fabricated interactions, contradicts family data (stabilize vs destabilize) |
| CHL1 | ARATH | Q9LUJ8 | 3 | 2 | Animal analogy (Apaf-1) for plant NLR; reversed cell death direction |
| rdgBbeta | DROME | Q9U9P7 | 2 | 2 | Paralog conflation (vibrator/giotto functions attributed to rdgBbeta) |
| gcl | DROME | Q01820 | 3 | 3 | Reversed directionality; never mentions Torso substrate |
| jar | DROME | Q01989 | 4 | 3 | Missed spermatid tethering mode; hallucinated GO IDs |
| bcp | ECOLI | P0AE52 | 4 | 3 | Oversimplified substrate preference; missed atypical 2-Cys mechanism |
| rlmC | ECOLI | B1X800 | 4 | 3 | Missed [4Fe-4S] cluster; speculative assembly claims |
| mbiA | ECOLI | P28697 | **0** | **0** | Fabricated InterPro domain for domainless protein; mitochondrion for E. coli |
| ppk34 | SCHPO | Q9UU87 | 3 | 3 | Fabricated aging claims; wrong mechanism (direct vs indirect) |
| spt16 | SCHPO | O94267 | 4 | 3 | Missed heterochromatin spreading, CENP-A exclusion |
| wsc1 | SCHPO | P87179 | 3 | 3 | Claims PKC-MAPK when actually Rho1-independent; obsolete GO term |
| SPDL1 | human | Q96EA4 | 3 | 3 | Hallucinated binding partners (BUB1B, NDC80, SKA); MKLN1/BICDL1 confusion |
| DCAF12L2 | human | Q5VW00 | 2 | 2 | Fabricated UniProt summary + substrates for Tdark retrocopy |
| STAU2 | human | Q9NUL3 | 3 | 2 | Conflated SMD with RNAi; fabricated ribosome assembly function |
| F2rl2 | mouse | O08675 | 3 | 2 | Missed cofactor-only role (no independent signaling); PARD3 gene name confusion in GOA |
| Ndufb1 | mouse | P0DN34 | 3 | 3 | Confused NDUFB1 with NDUFAB1; wrong Complex I position |
| Ifi204 | mouse | P0DOV2 | 3 | 3 | Conflated AIM2 inflammasome with IFI16/STING pathway; claims CARD (has PYRIN) |
| Ghr | rat | P16310 | 4 | 3 | Fabricated "response to gravity" rationalization; generic description |
| Sstr5 | rat | P30938 | 3 | 3 | SST-14 vs SST-28 preference exactly backwards |
| Hmgcs2 | rat | P22791 | 3 | 3 | Confused HMG-CoA lyase with reductase; paralog conflation (HMGCS1 vs HMGCS2) |
| lon-8 | worm | G5EGH7 | 2 | 3 | Wrong localization (basement membrane vs cuticular ECM); fabricated mechanism |
| fan-1 | worm | P90740 | 4 | 3 | Speculative interaction partners; missing C. elegans-specific literature |
| aldo-1 | worm | P54216 | 3 | 3 | Fabricated glycolytic metabolon; inappropriate GO:0042593 for C. elegans |
| YGR117C | yeast | P53270 | **1** | **1** | Complete fabrication (myosin V binding, nuclear migration, silencing) + fake UniProt summary |
| CRH1 | yeast | P53301 | 4 | 3 | Reversed donor-acceptor direction (chitin→glucan, not glucan→chitin) |
| PAP2 | yeast | P53632 | 4 | 3 | Fabricated phosphatase activities; misattributed helicase to Trf4 |

**Round 2 means: Correctness 2.9/5, Completeness 2.5/5**

## Per-Clade Summary (all 45 proteins)

| Clade | n | Mean Correctness | Mean Completeness | Notes |
|-------|---|:----------------:|:-----------------:|-------|
| rat | 3 | 3.3 | 3.0 | Good core biology, paralog confusion |
| PSEAE | 3 | 4.0 | 3.7 | Best round 1 clade |
| ECOLI | 3 | 2.7 | 2.0 | Bimodal: good on characterized, catastrophic on orphan (mbiA) |
| DANRE | 3 | 3.7 | 3.7 | Diagnostic domains help |
| DROME | 3 | 3.0 | 2.7 | Paralog conflation, organism biology missed |
| yeast | 3 | 3.0 | 2.3 | Catastrophic on uncharacterized (YGR117C) |
| SCHPO | 3 | 3.3 | 3.0 | Decent on well-characterized |
| human | 3 | 2.7 | 2.3 | Fabrication on Tdark protein |
| mouse | 3 | 3.0 | 2.7 | Paralog confusion (NDUFB1/NDUFAB1, AIM2/IFI16) |
| ARATH | 3 | 2.7 | 2.0 | Plant biology missed; animal analogies applied |
| ANOGA | 3 | 2.7 | 2.0 | Organism-specific biology absent |
| worm | 3 | 3.0 | 3.0 | Mixed: good on fan-1, poor on lon-8 |
| METJA | 3 | 2.3 | 3.0 | Archaeal biology missed |
| MYCTU | 3 | 2.3 | 2.3 | Fabrication on uncharacterized |
| DICDI | 3 | 2.3 | 2.7 | Family conflation |

## Failure Mode Analysis (45 proteins)

### 1. Fabricated UniProt Summaries (7/45 = 16%)
BioReason SFT generates a "UniProt Summary" line that does not match the actual
UniProt record. All cases are on poorly characterized proteins: MJ1511, Rv0898c,
Rv3660c, DCAF12L2, ppk34, mbiA, YGR117C. The model confabulates plausible-sounding
summaries when the real UniProt entry says "Uncharacterized protein." This is the
single most concerning systematic failure — it misrepresents an authoritative database.

### 2. Fabricated InterPro Domains (mbiA)
For the domainless orphan gene mbiA, BioReason invented an InterPro entry
(IPR009383) that does not exist. The protein has zero InterPro hits. This goes
beyond narrative confabulation to fabricating structural evidence.

### 3. Cross-Kingdom/Paralog Conflation (8/45 = 18%)
BioReason applies biology from well-characterized family members to divergent
paralogs or cross-kingdom homologs:
- mlcD: calmodulin → myosin I light chain
- tlcd4b: CerS ceramidase → acyltransferase
- rdgBbeta: vibrator/giotto (Class I PITP) → Class II PITP
- Ndufb1: confused with NDUFAB1 (similar name, different protein)
- Ifi204: AIM2 inflammasome → IFI16/STING pathway
- Hmgcs2: cytosolic HMGCS1 → mitochondrial HMGCS2
- DNAAF1: signaling scaffold instead of dynein assembly factor
- MJ1511: cross-kingdom fold bias (HMF catabolism for archaeon)

### 4. Organism-Specific Biology Absent (systematic)
Even when core enzyme type is correct, BioReason misses organism-specific features:
- clpP2: Mtb ClpP1-ClpP2 heterocomplex (drug target)
- TDO: mosquito eye pigmentation, blood meal processing
- F2rl2: mouse PAR3 cofactor-only role (no independent signaling)
- CHL1: plant NLR cold stress function (not animal apoptosis)
- lon-8: cuticular ECM (not basement membrane)
- Sstr5: SST-28 preference reversed
- gcl: Torso substrate identity

### 5. Confabulation Inversely Proportional to Characterization
Proteins with zero or minimal annotations consistently score 0-1/5:
- mbiA (0 GOA annotations): 0/5
- YGR117C (3 GOA annotations): 1/5
- MJ1511 (1 GOA annotation): 1/5
- Rv0898c (0 GOA annotations): 1/5
- DNAAF1 (no GOA from ANOGA): 1/5

Well-characterized proteins with diagnostic domains score 4/5:
fen1, secF, rpsD, spt16, CRH1, PAP2, fan-1, jar, bcp, rlmC, Ghr, TDO

### 6. Hallucinated GO Term IDs (At1g67980, jar, DNAAF1)
BioReason cites specific GO IDs that map to completely different terms than claimed.
GO:0047554 cited as "caffeoyl-CoA O-methyltransferase" is actually
"2-pyrone-4,6-dicarboxylate lactonase." This is distinct from fabricated UniProt
summaries — the model invents the ID-to-name mapping.

### 7. False Specificity vs InterPro2GO
BioReason outperforms InterPro2GO when domains are highly diagnostic (fen1, secF,
rpsD, CRH1, PAP2) but underperforms when it adds false specificity (tlcd4b, mlcD,
NPAC, NEK3). For uncharacterized proteins, InterPro2GO's conservative "assign
nothing" approach is consistently more accurate than BioReason's elaborate
fabrications.

### 8. Directional/Mechanistic Errors
Several errors involve getting the direction or mechanism exactly backwards:
- CRH1: reversed donor-acceptor (chitin→glucan vs glucan→chitin)
- Sstr5: SST-14 vs SST-28 preference reversed
- gcl: "clears cortical determinants" vs actually clears Torso
- CHL1: promotes vs limits cell death

## Overall Conclusions (45 proteins, 15 clades)

**Overall means: Correctness 2.9/5, Completeness 2.7/5**

1. **BioReason SFT is a domain-interpretation narrative engine**, not a biological
   knowledge system. Its quality is almost entirely determined by how informative
   the InterPro domain names are. For proteins with highly diagnostic domain
   architectures (FEN1, SecF, uS4, FACT, FAN1), it provides genuinely useful
   functional summaries. For everything else, it ranges from generic to fabricated.

2. **The fabricated UniProt summary problem is systematic** (7/45 = 16%). This is
   not a rare edge case but a reproducible failure on any poorly characterized
   protein. It is particularly dangerous because it misrepresents an authoritative
   database, potentially misleading users who trust BioReason's output.

3. **Organism-specific biology is never captured.** Not once in 45 proteins did
   BioReason provide organism-specific insight beyond what the domain architecture
   predicts. Mosquito eye pigmentation, Mtb drug targets, yeast cell wall biology,
   worm body size regulation, plant cold stress — all missed.

4. **The inverse relationship between characterization level and BioReason quality
   is the most important finding.** The proteins where BioReason could add the most
   value (uncharacterized, minimal annotations) are precisely where it performs
   worst. Well-characterized proteins where BioReason scores 4/5 already have
   extensive annotations that make BioReason's narrative redundant.

5. **BioReason SFT adds modest value over InterPro2GO for ~30% of proteins** (those
   with diagnostic multi-domain architectures). For the remaining ~70%, it either
   recapitulates InterPro2GO in prose or introduces errors not present in the
   conservative pipeline.
