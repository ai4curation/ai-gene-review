# VC_A0218 / Q9KMV0 (Vibrio cholerae O1 El Tor N16961) — curation notes

Started 2026-11-06. Entered as a leaf test of the `genes/PSEAE/estA` argument that the
PANTHER PTN005219546 IBD for GO:0008610 lipid biosynthetic process does not fit its clade.
The estA review listed this gene among the leaves, with the remark that its name
"thermolabile hemolysin" is submitter-supplied (ECO:0000313) rather than curated. The point
of this review was to test that remark against evidence rather than names. The result
inverts one half of it and confirms the other.

## 1. Starting state of the record

UniProt Q9KMV0 is a bare TrEMBL entry, 418 aa, `PE 4: Predicted`, with a single reference:
the N16961 genome paper (PMID:10952301). The name is indeed uncurated:

- `DE   SubName: Full=Thermolabile hemolysin {ECO:0000313|EMBL:AAF96130.1};`
- `GN   OrderedLocusNames=VC_A0218 {ECO:0000313|EMBL:AAF96130.1};`

No `CC FUNCTION`, no publications beyond the genome. Features: SignalP signal peptide 1–19,
Pfam PF00657 (Lipase_GDSL) plus PF31273 (VDLT_N), PROSITE PS01098 LIPASE_GDSL_SER,
CDD cd01846 `fatty_acyltransferase_like`, PANTHER PTHR45642 / SF141.

So on the face of the record, nothing is known. That is wrong — the protein has been
cloned, expressed, assayed and knocked out twice, under two other names.

## 2. The protein IS the characterised V. cholerae lecithinase (Lec)

Fiore et al. 1997 cloned a *V. cholerae* phospholipase they called `lec`
[PMID:9234762 "Sequence analysis revealed a 1,254-bp open reading frame (lec) encoding a
418-amino-acid protein with a predicted molecular weight of 47,600"]. Q9KMV0 is also 418 aa
with 47,703 MW. I checked this properly rather than by arithmetic: the Fiore protein is
GenBank AAA92960.1 (U50074, strain E7946 El Tor), and a full-length global alignment to
Q9KMV0 is gap-free with **exactly two mismatches** (M230/R231 vs I230/A231) —
99.5% identity, i.e. ordinary El Tor strain polymorphism
[file:VIBCH/VC_A0218/VC_A0218-bioinformatics/RESULTS.md].

Genomic context corroborates it independently. Fiore et al. mapped `lec` next to the
haemolysin and lipase genes [PMID:9234762 "revealed that lec, hlyA (hemolysin), and hlyC
(lipase) are adjacent on the V. cholerae chromosome"], and in N16961 `hlyA` is VCA0219 —
the immediate neighbour of VCA0218. Syed et al. state the arrangement in N16961 locus-tag
terms [PMID:19717600 "the tlh gene is adjacent to and divergently transcribed from the hlyA
gene"].

What Fiore et al. actually showed, for this protein:

- Secreted/diffusible lecithinase activity: [PMID:9234762 "with enzyme production
  visualized as a zone of clearing around colonies plated on egg yolk agar"].
- Phospholipase activity of the gene product itself, in two hosts:
  [PMID:9234762 "Polyacrylamide gel electrophoresis combined with an egg yolk agarose
  overlay demonstrated phospholipase activity migrating at a relative molecular weight of
  45,000 in preparations of V. cholerae and the Escherichia coli clone"].
- Loss-of-function: [PMID:9234762 "The resulting mutant lacked lecithinase activity on egg
  yolk agar but had undiminished reactivity in rabbit ligated ileal loop assays"].
- A predicted signal sequence and lipid-binding motif
  [PMID:9234762 "A potential signal sequence exists in the predicted amino acid sequence,
  as does a lipid binding motif found in prokaryotic and eukaryotic phospholipases and
  lipases"].

Only the abstract of PMID:9234762 is cached (`full_text_available: false`), so the
substrate class (A1 / A2 / B) was not determined here as far as I can see, and I have not
assumed one.

## 3. The hemolysin name IS supported — by work on this V. cholerae protein

This is where the estA review's leaf-level remark needs correcting. The name arrived in
UniProt uncurated, but it is not merely inherited from *V. parahaemolyticus*: Syed et al.
2009 identify VCA0218 as *V. cholerae*'s thermolabile haemolysin and demonstrate the
phenotype genetically.

- The identification: [PMID:19717600 "VCA0218 encodes a thermolabile hemolysin, Tlh, which
  has phospholipase and lecithinase activity"] — their citation 14 for the activity is
  Fiore et al., which the later remark about "a previous study with rabbits ( 14 )" (the
  ileal loop assay) confirms.
- They built the mutant themselves: [PMID:19717600 "Splicing-by-overlap-extension (SOE) PCR
  ( 26 ) was used to generate the deletion mutations in tlh , cdgD , and frhC"].
- The genetic test: [PMID:19717600 "Importantly, the hemolytic activity of the fliA strain
  is abrogated when tlh is inactivated, demonstrating that the flagellum-regulated
  hemolysin is the thermolabile hemolysin Tlh"], restated in the Discussion
  [PMID:19717600 "inactivation of tlh in these mutants renders them nonhemolytic, thus
  identifying thermolabile hemolysin as the flagellum-regulated hemolysin"].
- Target cell: human type O erythrocytes [PMID:19717600 "The rpoN , flrA , flrC , and fliA
  flagellar regulatory mutants also demonstrate increased hemolysis of human type O
  erythrocytes"]. They were able to attribute the lysis to Tlh partly because the classical
  strain they used is HlyA-negative [PMID:19717600 "VCA0219 encodes the “El Tor” hemolysin
  HlyA, and the O395 strain used in these studies contains a deletion in hlyA that renders
  this strain HlyA − ( 19 ); thus, HlyA cannot be the flagellum-regulated hemolysin"], and
  the third candidate does not lyse human cells [PMID:19717600 "VCA0594 encodes a
  hemolysin, Hlx, which was determined to lyse sheep but not human erythrocytes ( 45 )"].
- Regulation: `tlh` is repressed by the flagellar hierarchy
  [PMID:19717600 "we can conclude that the flagellar regulatory hierarchy represses the
  transcription of tlh"], with the qRT-PCR fold changes reported only as a range across
  seven genes [PMID:19717600 "ranging from approximately twofold for tcpA to approximately
  eightfold for hlyA"] — so no specific number for `tlh`.
- Not a dominant colonisation factor, and the paper is internally inconsistent about how
  small the defect was: Results say [PMID:19717600 "the tlh V. cholerae strain colonized
  only slightly worse than the wild-type parent (competitive index, 0.67; P = 0.029)"]
  while the Discussion says [PMID:19717600 "The tlh mutant colonized infant mice similarly
  to the wild-type strain"]. Either way: [PMID:19717600 "This indicates that thermolabile
  hemolysin does not play a critical role in colonization of the intestine, at least in
  this particular animal model"]. Consistent with Fiore's undiminished ileal loop response.

Caveat worth keeping: Syed et al. worked in the classical biotype strain O395 while using
N16961 locus tags; Fiore worked in El Tor E7946. Q9KMV0 is El Tor N16961. Given 99.5%
identity to the E7946 protein these are the same gene, but no experiment was done in
N16961 itself.

## 4. The V. parahaemolyticus TLH story, and whether it transfers

It does, as a family-level expectation, and the orthology is real rather than nominal:
Q9KMV0 is 63.2% identical over all 418 residues to Q68CM4, the *V. parahaemolyticus*
`tlh` product (also exactly 418 aa)
[file:VIBCH/VC_A0218/VC_A0218-bioinformatics/RESULTS.md].

What is established for that orthologue is a specific and unusual enzymology. Shinoda et
al. purified LDH from an *E. coli* transformant and showed it hydrolyses both acyl esters
of phosphatidylcholine [PMID:1791426 "The LDH was a phospholipase hydrolysing both fatty
acid esters of phospholipid, i.e. it hydrolysed phosphatidylcholine (PC) to
lysophosphatidylcholine (LPC) and then LPC to glycerophosphorylcholine (GPC)"], and
explained the haemolysis mechanistically — the haemolytic agent is the lysophospholipid
intermediate, which accumulates because the two steps run at similar rates
[PMID:1791426 "Phospholipase B, however, does not usually show haemolytic activity, because
the intermediate (LPC), which is the actual haemolytic agent, is immediately hydrolysed to
the final product (GPC)"]. Their conclusion [PMID:1791426 "LDH of V. parahaemolyticus is an
atypical phospholipase to be designated as phospholipase A2/lysophospholipase"].

The same two activities travel together across the family, which is what makes the transfer
to *V. cholerae* reasonable rather than speculative:

- *V. alginolyticus* TLH, 94% identical to *V. parahaemolyticus* LDH/TLH, purified
  recombinant: [PMID:20662368 "TLH purified by the nickel-nitrilotriacetic acid (Ni-NTA)
  His-Bind Resin method showed phospholipase activity on an egg yolk emulsion plate and
  hemolytic activity against flounder erythrocytes"], and it carries the same fold
  [PMID:20662368 "The sequence analysis also indicated that it contained a GDSL lipase
  domain like VHH"].
- *Photobacterium damselae* PPP, 53–55% identical to the Vibrio proteins, with a knockout:
  [PMID:17958612 "The culture supernatant of wild-type P. damselae ssp. piscicida showed
  phospholipase activity, while that of a PPP gene knockout mutant did not"] and
  [PMID:17958612 "The rPPP also showed lecithin-dependent haemolytic activity against
  mammalian erythrocytes and direct haemolytic activity against fish erythrocytes"].
  Note that paper also puts GCAT at arm's length: [PMID:17958612 "while it showed low
  identities (23-26%) with glycerophospholipid cholesterol acyltransferase of Aeromonas
  spp."].
- *Vibrio* sp. MA3 Vhe1: [PMID:37458864 "A BLAST homology search indicated that Vhe1 belongs
  the lecithin-dependent hemolysin/thermolabile hemolysin (LDH/TLH) family"], and both
  activities reside in the one protein [PMID:37458864 "the optimal temperature for both the
  hemolytic and phospholipase activities of Vhe1 was 50 °C"].
- The catalytic machinery is the SGNH triad, not anything exotic:
  [PMID:36136547 "Multiple sequence alignment of LDH of V. parahaemolyticus against other
  Vibrio species showed that LDH has well-conserved GDSL and SGNH motifs, characteristic of
  the hydrolase/esterase superfamily"] and [PMID:36136547 "the homology model showed that
  the conserved catalytic triad His-Ser-Asp was in the LDH active site"]. Q9KMV0 has the
  motif at residues 153–156, catalytic Ser155
  [file:VIBCH/VC_A0218/VC_A0218-bioinformatics/RESULTS.md].
- The V. harveyi/V. mimicus members were recognised as the same thing as the cholerae
  lecithinase from the start [PMID:11425736 "The VHH protein shows homology to the
  lecithinase of V. mimicus and V. cholerae"]; the *V. mimicus* phl is 74.4% identical to
  `lec` [PMID:9767128 "the deduced amino acids sequence showed 74.4% identity with
  phospholipase gene (lec) from V. cholerae El Tor"].

One historical claim needs flagging as superseded: Taniguchi et al. reported
[PMID:3886626 "No homologous DNA sequences to TSD and thermolabile hemolysin genes were
detected in the chromosomes of Vibrio cholerae, Vibrio vulnificus, non-O1 V. cholerae, and
Vibrio anguillarum"]. At 63% amino-acid identity that is a Southern-blot stringency
artefact, superseded by the cloning of `lec` itself.

What does NOT transfer: the precise phospholipase class. Shinoda's A2/lysophospholipase
assignment was made on the *V. parahaemolyticus* enzyme, and nobody has repeated the
positional analysis on the *V. cholerae* protein. So GO:0004620 glycerophospholipase
activity is the defensible level here, not GO:0004623.

## 5. GO:0008610 lipid biosynthetic process — the IBA does not hold

Reporting what the evidence shows, in both directions.

For it: nothing on this gene. The row's `WITH/FROM` is
`PANTHER:PTN005219546|UniProtKB:O33407` — the node plus EstA, the single seed, whose own
support is a rhamnolipid-deficient deletion phenotype of unknown mechanism (argued in
`genes/PSEAE/estA/estA-ai-review.yaml`). The only other thing in the whole record pointing
away from hydrolysis is the CDD hit `cd01846 fatty_acyltransferase_like`, which names a
clade containing *Aeromonas* GCAT, the one superfamily member with a documented
transacylase activity. That is a clade name, not a result, and GCAT is only 29.1% identical
to Q9KMV0 — no closer than ChoE (29.0%) or EstA (26.4%)
[file:VIBCH/VC_A0218/VC_A0218-bioinformatics/RESULTS.md]. So the acyltransferase reading has
no support specific to this protein.

Against it: positive, gene-specific evidence of the opposite chemistry. The *V. cholerae*
protein hydrolyses phosphatidylcholine (section 2), its 63%-identical orthologue hydrolyses
both ester positions of PC to GPC (section 4), and every experimentally characterised
bacterial member of this clade — *V. parahaemolyticus* LDH, *V. alginolyticus* TLH,
*P. damselae* PPP, *Vibrio* sp. Vhe1, *V. cholerae* Lec — is a phospholipase. Hydrolysis of
a lipid is lipid catabolism. No step of any lipid biosynthetic pathway has been attributed
to any of them.

This is the evidence the estA argument wanted and did not have: the bacterial side of
PTN005219546 is not merely uncharacterised (as the plant leaves are), it is characterised,
and characterised as hydrolytic. The leaf-level verdict is REMOVE, and the defect is at the
node, already reported from the estA review.

## 6. What remains genuinely unknown

- The positional specificity of the *V. cholerae* enzyme (A1 vs A2 vs B) has not been
  measured; only the family-level A2/lysophospholipase assignment on the
  *V. parahaemolyticus* orthologue exists.
- Its physiological substrate and role. Fiore's deletion mutant was normal in ileal loops
  and Syed's barely affected colonisation, so the function it was retained for is not the
  one those assays test. Whether it serves nutrient acquisition from environmental
  phospholipid, membrane remodelling, or anti-eukaryotic defence in the aquatic niche is
  open.
- Its secretion route. The SignalP signal peptide and the diffusible egg-yolk clearing show
  it leaves the cytoplasm, but whether it is released by the Eps type II system (which
  secretes the *V. cholerae* lipase, per PMID:19717600's reference to eps-secreted "lipase")
  has not been tested for this protein. I did not assert a secretion-system-specific term.

## 7. Review decisions

- Three MF rows (GO:0052689 IBA, GO:0016298 IEA, GO:0016788 IEA) are all correct but
  general; each MODIFY to GO:0004620 glycerophospholipase activity, the specific supported
  descendant, per the "correct but general is MODIFY" rule.
- GO:0006629 lipid metabolic process (IEA) MODIFY to GO:0046475 glycerophospholipid
  catabolic process — the direction of the chemistry is known.
- GO:0008610 lipid biosynthetic process (IBA) REMOVE, with a `propagation_review`
  (`SOURCE_BAD`, `ROLE_CONFLATION`) and no new source defect: the node defect is already
  filed from `genes/PSEAE/estA`.
- Two NEW rows. GO:0019836 symbiont-mediated haemolysis of host erythrocyte (IMP,
  PMID:19717600) passes the comparator check: the only two experimental annotations to that
  term in GOA are *V. parahaemolyticus* `tdh` (O87079, IDA) and *Salmonella* `hlyE`
  (Q8Z727, IMP), i.e. GO does annotate a Vibrio haemolysin this way, and here the protein
  performs the lysis itself rather than merely being required for it (the LPC it generates
  is the lytic agent). GO:0005576 extracellular region (IC) rests on two independent lines:
  the SignalP signal peptide 1–19 and the diffusible lecithinase activity around intact
  colonies.
