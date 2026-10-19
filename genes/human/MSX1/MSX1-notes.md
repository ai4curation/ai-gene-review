# MSX1 (human, P28360) review notes

Project context: `projects/NEURAL_CREST_ORIGINS.md`, Tier 2 (neural plate border
specifiers). Human MSX1 is used as the proxy because there is no reviewed
*X. laevis* Msx1 entry (frog msx1.L/msx1.S are TrEMBL: A5D8L7, A0A8J0Q853,
A0A1L8HKV3, Q3B8L1, Q642R5).

## 2026-10-05 — initial review

### Identity and molecular activity

- Msh/Msx homeodomain transcription factor (UniProt: Msh homeobox family;
  InterPro HD, IPR050674 Msh_Homeobox_Regulators). UniProt function text is
  mostly "By similarity" to mouse P13297: transcriptional repressor that binds
  C/TAAT cores.
- Mouse Msx1 is a potent repressor, and repression can be independent of its
  own DNA sites, via contacts with the core machinery
  [PMID:7823952 "Msx-1 is a potent repressor of transcription and can function through both TATA-containing and TATA-less promoters"]
  [PMID:7823952 "Msx-1 represses transcription in vitro in a purified reconstituted assay system and interacts with protein complexes composed of TBP and TFIIA"].
- Msx1 and Msx2 bind the same consensus and both repress; Msx1 is the stronger
  repressor [PMID:8861098 "both MSX-1 and MSX-2 function as repressors and share the distinct property that they do so independently of their consensus DNA binding sites"].
- Target selectivity in vivo via PIAS1 and nuclear-periphery localisation, MyoD
  CER [PMID:16600910 "PIAS1 enables Msx1 to bind selectively to a key regulatory element in MyoD, the CER, in myoblast cells"].
- Context-dependent activation: Msx1 binds Stra8 regulatory sequences and
  stimulates Stra8 transcription in germ cells [PMID:22071108 "In F9 cells, Msx1 can bind to Stra8 regulatory sequences and Msx1 overexpression stimulates Stra8 transcription."].
- Human MSX1 binds DNA in methyl-SELEX (Yin 2017, IDA row for GO:1990837)
  [PMID:28473536 "By analysis of 542 human TFs with methylation-sensitive SELEX"].
- Human R31P (homeodomain) allele is inactive and acts by haploinsufficiency
  [PMID:9742121 "it exhibits little or no ability to interact with DNA or other protein factors or to function in transcriptional repression"].
- Partners: Tbx2/3/5 (Cx43 repression in heart cell lines) [PMID:18285513 "Msx1 and Msx2 can function in concert with the T-box proteins to suppress Cx43 and other working myocardial genes."];
  p53 (cancer-cell overexpression study) [PMID:15705871 "The homeodomain of Msx1 functions as a protein-protein interacting motif rather than a DNA-binding domain"];
  RBPMS (HuRI Y2H, PMID:32296183 — no functional content).

### Mammalian biology (craniofacial, tooth, nail)

- Mouse null: cleft secondary palate, tooth arrest, nasal/frontal/parietal and
  malleus defects [PMID:7914451 "All Msx1- homozygotes manifest a cleft secondary palate, a deficiency of alveolar mandible and maxilla and a failure of tooth development."].
  Note: the abstract reports the *malleus in the middle ear*; the human rows to
  `GO:0048839 inner ear development` are transferred from a mouse IMP to this
  paper. Mouse P13297 also carries `GO:0042474 middle ear morphogenesis`. Left
  UNDECIDED (full text not seen) and raised as a question.
- Tooth: Msx1 needed in dental mesenchyme up to cap stage; BMP4 rescues
  [PMID:11023873 "through the E14.5 cap stage of tooth development, Msx1 is required in the dental mesenchyme for tooth formation"].
  Later, Msx1 keeps dental mesenchyme proliferating and undifferentiated by
  repressing Bmp2/Bmp4/Lef1 [PMID:24028588 "MSX1 may promote proliferation and prevent the differentiation of dental mesenchymal cells by the inhibition of Bmp2 and Bmp4 expression"].
- Human genetics: selective tooth agenesis (R31P) [PMID:8696335], tooth agenesis
  plus clefting (S105X) [PMID:10742093, title only in cache], Witkop tooth-and-nail
  syndrome (S202X) [PMID:11369996 "Msx1 is critical for both tooth and nail development"];
  cleft association studies [PMID:11332647, PMID:12651933].
- Mouse `GO:0001837 epithelial to mesenchymal transition` (source of a human IEA)
  is sourced to PMID:11023873, which is about epithelial–mesenchymal
  *interactions* (tissue recombination), not EMT. Human IEA REMOVED.

### Neural crest / neural plate border biology

- Bmp-gradient target at the border; intermediate Bmp gives msx1; msx1 induces
  snail, slug, foxd3; dominant-negative blocks all crest markers; msx1 is upstream
  of snail/slug [PMID:14627721 "msx1 expression is able to induce all other early neural crest markers tested (snail, slug, foxd3) at the time of neural crest specification"]
  [PMID:14627721 "msx1 is upstream of snail and slug in the genetic cascade that specifies the neural crest in the ectoderm"].
- Msx1 acts upstream of Pax3 and Zic, mediates FGF8 (not WNT-only) signals
  [PMID:15691759 "Msx1 induces Pax3 and ZicR1 cell autonomously, in turn, Pax3 combined with ZicR1 activates Slug in a WNT-dependent manner."]
  [PMID:15691759 "In neuralized ectoderm, Msx1 is sufficient to induce multiple early neural crest genes."].
- Msx1/Msx2 morphants: both required for Slug, mutually compensating
  [PMID:16586351 "These results indicate that Msx1 and Msx2 are both essential for neural crest development, but that the two genes have the same function in this tissue."].
- Gbx2 is upstream of Pax3 and Msx1 [PMID:19736322 "demonstrate that Gbx2 is upstream of the neural fold specifiers Pax3 and Msx1."].
- Msx1+Pax3 is the second-best pair for crest induction from animal caps, after
  Pax3+Zic1 [PMID:23509273 "Because Msx1 coinjected with Pax3 was the second best combination to activate early NC development from animal caps"].
- Mouse Msx1/Msx2 double mutants: crest forms, but cranial/cardiac crest is
  mispatterned and dies [PMID:16221730 "We show that Msx1/2 mutants exhibit profound deficiencies in the development of structures derived from the cranial and cardiac neural crest."].
  So in mammals the requirement is later (crest patterning/survival), with
  Msx1/Msx2 redundancy; frog evidence is the basis for the border role.

**Network layer.** Border specifier, one step above Pax3/Zic1: BMP (intermediate
level) → Msx1 → Pax3 + Zic → snail2/foxd3. It is necessary and in neuralized
ectoderm sufficient for early crest genes, but it works through Pax3/Zic rather
than specifying crest itself; Msx1 is also expressed in the epidermal side of the
border and non-crest tissues. Same layer as pax3-a, zic1, gbx2, hes4-a.

**Term choice.** `GO:0014029` neural crest formation (formation of the border
region of ectoderm), as for the other border genes. Not `GO:0014036` (fate
specification, reserved for specifiers). Not adding `GO:0014034` commitment
either: unlike Pax3+Zic1, which directly activate the specifier enhancers
[PMID:24360906], there is no evidence that Msx1 binds crest specifier enhancers;
it acts upstream, through Pax3/Zic.

### Comparator checks (QuickGO, 2026-10-05)

1. Downloaded all QuickGO annotations (any evidence, incl. IEA) to `GO:0014029`,
   `GO:0014034`, `GO:0014036`, `GO:0014033`, `GO:0014032`, `GO:0001755` with
   descendants (`goUsage=descendants`, is_a/part_of; `downloadLimit=100000`;
   rows 1912/458/195/45255/43111/40414). Filtered symbols matching
   `^msx|^msh|^hmx`: **zero hits**. Sanity check: pax3.L, ZIC1, zebrafish tfap2a
   present in the same files.
2. Pulled all annotations for Msx proteins directly: human MSX1 P28360 (65),
   MSX2 P35548 (69), mouse Msx1 P13297 (165), Msx2 Q03358 (125); chicken
   MSX1 P28361, MSX2 P28362; zebrafish msxa/b/c/d (Q03357, Q03356, Q01703,
   Q01704), msx1a/msx1b/msx2a/msx2b/msx3 (TrEMBL); X. laevis msx1.L/.S, msx2.L/.S;
   X. tropicalis msx1/msx2. **No crest, neural plate or ectoderm term on any of
   them.** Xenopus msx entries carry only IBA rows (GO:0000977, 0000981, 0005634,
   0006357, 0048598); X. tropicalis msx1 has GO:0036268 swimming (IMP).
   Zebrafish msxb/msxc/msx1a/msx3 carry otic placode/fin regeneration terms.
   Chicken MSX1 carries GO:0030509 BMP signaling pathway (IDA, PMID:19850029).
3. Same-layer peers (from the project notes, verified by the earlier Tier 2
   reviews): pax3-a, zic1, hes4-a carry `GO:0014029` by IMP.

Interpretation: the Msx absence is family-wide and includes the frog genes where
the border work was done (Tribulo 2003, Monsoro-Burq 2005, Khadka 2006). Since
peers in the same role carry the term, this is an uncurated literature gap, not
a convention (the frog msx genes are TrEMBL and were never curated). NEW
`GO:0014029` on the human proxy is by ISS from the frog literature; ideally the
frog entries should carry the IMP rows. Raised as a question.

### Evolution / outgroups

- Amphioxus Msx is expressed in epidermal ectoderm and extends into the edge of
  the neural plate; BMP shifts it [PMID:18562679 "whereas Msx is expressed not only in the epidermal ectoderm, but extends more medially into the neural ectoderm at the edges of the neural plate."].
  The border layer (Msx, Zic, Pax3/7, Dlx) is ancestral to chordates; most crest
  specifiers are absent there.
- Lamprey: msx-A expression rises monotonically into late crest, unlike the
  frog dynamics of border factors [PMID:39060477 "Notably, a number of other neural plate border factors, including myc, pax3, msx1, zic1, and klf17 displayed these dynamics in Xenopus but not in lamprey."].
- So the Msx border role is ancestral; what vertebrates added is the link
  Msx1 → Pax3/Zic → crest specifiers.

### Decisions summary

- Core: Pol II-specific repressor (GO:0001227) in nucleus; tooth development
  (GO:0042475, negative regulation of odontoblast differentiation); palate/face
  morphogenesis; neural plate border (GO:0014029, NEW).
- p53 cluster (PMID:15705871, one overexpression study in cancer cells):
  p53 binding, protein stabilization, apoptotic signaling kept as non-core;
  cell morphogenesis, cell growth, protein localization to nucleus and the IC
  DNA-damage row marked over-annotated.
- protein binding (RBPMS, HuRI): REMOVE (uninformative).
- EMT IEA: REMOVE (source paper is about epithelial–mesenchymal interaction).
- inner ear development: UNDECIDED (abstract says middle ear).
