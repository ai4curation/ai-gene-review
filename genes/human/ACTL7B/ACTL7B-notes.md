# ACTL7B (human, Q9Y614) — review notes

Reviewed as part of the PAINT + affinage campaign. All provenance below is either a
verbatim quote from a cached publication, a line from `ACTL7B-uniprot.txt`, or a number
produced by `ACTL7B-bioinformatics/analyze.py` (report: `ACTL7B-bioinformatics/RESULTS.md`).

## 1. What the gene is

Human ACTL7B is a 415-residue, intronless, testis-restricted member of the actin family.
UniProt asserts family membership only ("SIMILARITY: Belongs to the actin family.
{ECO:0000305}") and gives it **no FUNCTION comment at all**. Its only subcellular-location
statement is by similarity: "SUBCELLULAR LOCATION: Cytoplasm, cytoskeleton
{ECO:0000250}." — an inference, not data. The entry is nonetheless `PE   1: Evidence at
protein level;` and HPA records it as "HPA; ENSG00000148156; Tissue enriched (testis)."
so the protein is detected; what is missing is *functional* characterisation of the human
protein, not detection.

The gene arose with its paralogue ACTL7A in a head-to-head intronless pair
[PMID:10373328 "Genomic analysis revealed ACTL7A and ACTL7B to be intronless genes contained on a common 8-kb HindIII fragment in a \"head-to-head\" orientation."],
and the paralogues differ in expression: ACTL7B "was detected only in the testis and, to a
lesser extent, in the prostate." whereas "ACTL7A is expressed in a wide variety of adult tissues"
[PMID:10373328]. In mouse the two proteins were originally described as T-ACTIN 1
(= Actl7b) and T-ACTIN 2 (= Actl7a) and were reported to occupy *different* compartments:
"the cellular locations of these two proteins are quite different (T-ACTIN-1 was found in the cytoplasm and T-ACTIN-2 was located in the nucleus)"
[PMID:12672658]. That paper also noted, presciently for section 3, that
"The T-ACTINs contained some of the conserved regions seen in other actins."
[PMID:12672658] — *some*, not all.

## 2. What is actually known about function (all of it from mouse)

Two independent `Actl7b`-null mouse lines were published in 2023 and agree. Only one of them
is in the affinage record (`ACTL7B-deep-research-affinage.md`, trust gates clear at fetch time); the
other, PMID:37800308, was found by a plain PubMed search of the gene symbol and turns out to
carry the only informative molecular partner ACTL7B has. Affinage's own GO grounding for this
gene proposes `GO:0008092 cytoskeletal protein binding` as the molecular activity, which no
measurement supports — the same fold-to-activity leap as the legacy TAS annotations.

- Clement et al.: "In mice, ACTL7B specifically localises to the developing acrosome, within the nucleus of early spermatids, and to the flagellum connecting region."
  and "KO mice were infertile, with severe and variable oligoteratozoospermia (OAT) and multiple morphological abnormalities of the flagellum (MMAF) and sperm head."
  concluding "In conclusion, this work identifies ACTL7B as a key regulator of spermiogenesis that is required for male fertility."
  [PMID:36617158]. The same paper is explicit that the family was uncharacterised:
  "Multiple testis-specific ARPs are well conserved among mammals, but their functional roles are unknown."
- Merges et al.: "Severe spermatid defects, such as detached acrosomes, disrupted membranes and flagella malformations start to appear after spermiogenesis step 9"
  in `Actl7b`-null mice [PMID:37800308].

Merges et al. also supply the **only informative molecular partner ACTL7B has**:
"To identify ACTL7B-protein interactions, anti-ACTL7B antibody was coupled to Dynabeads and used for co-immunoprecipitation on protein extracts from whole wild-type testes."
→ "In the co-immunoprecipitation using the anti-ACTL7B-coupled beads, we identified LC8 light chains, dynein light chain 1 (DYNLL1) and its paralog dynein light chain 2 (DYNLL2)."
with a reciprocal pull-down:
"In the eluate of the co-immunoprecipitation using anti-DYNLL2-coupled beads, DYNLL2 and ACTL7B were detected, further supporting the ACTL7B-DYNLL2 interaction."
and a functional consequence:
"Taken together, these results suggest that the localization of DYNLL1 and DYNLL2 is altered in the absence of ACTL7B, whereas the amount of protein is unchanged."
plus a gain-of-function counterpart in heterologous cells:
"This supports the notion that ACTL7B interacts with and controls DYNLL1 and DYNLL2 localization in the cell."
[all PMID:37800308]. This is endogenous, native-level, reciprocal, and orthogonally
corroborated — the strongest interaction evidence in the ACTL7B literature. **It is not in
human GOA.**

A nuclear pool is now reported for ACTL7B itself, refining the 2003 cytoplasm-only
assignment: "ACTL7B is detected in the cytoplasm and at lesser amounts in the nucleus of round and elongating spermatids"
[PMID:37800308], and a preprint "confirms the intranuclear presence of ACTL7B in spermatocytes and round spermatids"
and "identifies a putative nuclear localization sequence conserved across mammalian ACTL7B"
[PMID:38464253]. That preprint further reports "Additionally, in the absence of ACTL7A or ACTL7B there is a loss of intranuclear localization of HDAC1 and HDAC3"
but its chromatin-complex mechanism is explicitly computational:
"models, ACTL7A and ACTL7B were found capable of binding to INO80 and SWI/SNF nucleosome remodeler family members in a manner akin to nuclear actin and ACTL6A."
[PMID:38464253]. Treated here as a hypothesis, not evidence.

Human-side genetics remains negative/inconclusive: "Although we could not determine whether these SNPs cause infertility"
[PMID:31310081].

## 3. Does the actin fold buy ACTL7B the actin annotations? (bioinformatics)

Question posed properly: not "is it actin-like" but "does it retain the residues actin uses
to bind nucleotide and to polymerise". Residue sets were computed from structures (1ATN
G-actin·ATP; 8A2S F-actin Mg-ADP-Pi, 5 protomers) and scored across a panel spanning
conventional actins, the ATP-binding cytoplasmic ARPs (Arp2/Arp3), and the nucleotide-poor
nuclear ARPs (ACTL6A, ACTR5, ACTR8, yeast Arp7/Arp9). Full tables in
`ACTL7B-bioinformatics/RESULTS.md`.

**Nucleotide pocket — degenerate but not dead.** 13/20 8A2S nucleotide contacts identical
in ACTL7B (65%), versus 90–100% for conventional actins, 85% for Arp2, 70% for Arp3, and
35–50% for the nuclear ARPs. ACTL7B keeps the P-loop core (S14→S58, K18→K62), the catalytic
Gln137 (→Q181), the 156/158/159 glycine-rich loop, K213 and K336; it loses G15→Q59 (bulk
introduced into P-loop 1), D157→H201, R210→E253 (charge reversal), T303→C345 and Y306→L348
[file:human/ACTL7B/ACTL7B-bioinformatics/RESULTS.md
"Per-position nucleotide contacts in ACTL7B (8A2S numbering -> ACTL7B): G13->G57, S14->S58, G15->Q59, L16->Y60, K18->K62, Q137->Q181"].
**Conclusion: nucleotide binding is untested, and cannot be either assumed or excluded.**
Note that GOA does *not* annotate ATP binding for ACTL7B, so nothing here needs correcting;
this is the control that stops the review from asserting "fold without function".

**Polymerisation interface — not conserved.** Of the 74 positions that the middle protomer
of the 8A2S filament uses to contact its neighbours, only 26 are identical in ACTL7B and 34
differ non-conservatively
[file:human/ACTL7B/ACTL7B-bioinformatics/RESULTS.md
"| ACTL7B (Homo sapiens) | query (human ACTL7B) | 42.9 | 26 | 13 | 34 | 1 | 35.1 | 52.7 |"].
35% identity puts ACTL7B alongside Arp2 (43%
[file:human/ACTL7B/ACTL7B-bioinformatics/RESULTS.md
"| ACTR2 (Homo sapiens) | cytoplasmic ARP (Arp2/3 complex) | 48.3 | 32 | 11 | 31 | 0 | 43.2 | 58.1 |"])
and the nuclear ARPs (20–41%), and nowhere near any conventional actin (84–100%). The
decisive detail is the largest contact segment, actin 38–45 — the DNase-I-binding "D-loop",
the principal longitudinal inter-protomer contact — which is **entirely replaced**:
`PRHQGVMV` → `RCPEAADA`, 0/8 identical, against 8/8 for ACTB
[file:human/ACTL7B/ACTL7B-bioinformatics/RESULTS.md "| 38-45 | 8 | PRHQGVMV | RCPEAADA | 0/8 | 1/8 | 8/8 |"].
The adjacent 60–66 segment is 1/7 and the hydrophobic-plug segment 267–270 is 1/4.

So ACTL7B is an actin-*fold* protein that has lost the actin polymerisation surface. It
cannot be assumed to be a filament subunit, and "actin cytoskeleton" as a location and
"structural constituent of cytoskeleton" as an activity are not purchasable from the fold.
This does **not** exclude ACTL7B being a component of a sperm cytoskeletal structure or an
actin-binding protein — it excludes the specific inference that produced those annotations.
CDD already recognises the divergence with a clade-specific model,
"CDD; cd10214; ASKHA_NBD_ACTL7; 1." rather than a generic actin model.

## 4. Where each existing annotation comes from (propagation audit)

All 11 GOA rows and all 18 WITH/FROM tokens were resolved and each protein source was asked,
via QuickGO, what evidence *it* carries for the term being propagated. **Every protein
source carries its own experimental evidence for its own annotation** — so no row here can
be dismissed as "the source was only guessing". Where I disagree, the defect is in the
propagation or in the term, not in the source.

- **GO:0005634 nucleus (IBA)** — seeds: mouse Actl7a (Q9QY84, Swiss-Prot, own EXP+IDA),
  *S. cerevisiae* ARP9 (Q05123, Swiss-Prot, own IDA+IPI), *C. albicans* ARP9 (Q5A9X7,
  **TrEMBL/unreviewed**, own IDA), *T. brucei* actin-like (Q57ZL0, **TrEMBL/unreviewed**,
  own IDA+HTP). Note what is *absent*: the true orthologue, mouse Actl7b. So the
  propagation path is paralogue + deep nuclear-ARP, at a node with taxon constraint 2759.
  Yet the conclusion is independently right for ACTL7B (section 2). Weak path, correct
  destination.
- **GO:0005737 cytoplasm (IBA)** — node PTN001377938, seeds mouse Actl7a, mouse **Actl7b**
  (Q9QY83, own IDA), rat Actl7a, human ACTL7A. Orthologue-anchored and clade-restricted;
  the best-founded row in the set.
- **GO:0005198 structural molecule activity (IBA)** — WITH/FROM is two PANTHER *nodes*, no
  proteins. Reading the cached PAINT table shows why, and it is the most interesting fact in
  this review: node PTN000940351 carries `GO:0005200` IBD seeded from conventional actins and
  Arp2/Arp3, and node PTN008986528 (ancestral to ACTL7B) carries `GO:0005198` IBA *plus*
  `GO:0005200` as an **IRD with `negated=true`**
  [file:human/ACTL7B/ACTL7B-bioinformatics/RESULTS.md "| PTN008986528 | GO:0005200 | F | IRD (NEGATED) | PANTHER:PTN000940351 |"].
  PAINT curators deliberately refused to propagate "structural constituent of cytoskeleton"
  into this clade and let only the generic parent through. My structural analysis reaches the
  same verdict independently.
- **GO:0005856 cytoskeleton (IEA, GO_REF:0000044)** — from `UniProtKB-SubCell:SL-0090`,
  which comes from the UniProt CC line that is itself `{ECO:0000250}` by similarity. A
  by-similarity statement laundered into an IEA annotation.
- **GO:0007010 cytoskeleton organization (IEA, GO_REF:0000108)** — WITH/FROM is literally
  `GO:0005200`: an MF→BP inter-ontology inference whose sole input is the legacy TAS row
  below, i.e. the term PAINT has negated for this clade.
- **GO:0005515 protein binding ×4 (IPI, PMID:32814053)** — HIP1, LAMP2-2, CASP6, RAN, all
  from one screen: "candidate interactions and is generated by systematic yeast two-hybrid interaction screening of ∼500 ND-related proteins"
  in a study that "connects ∼5,000 human proteins via ∼30,000" candidate interactions
  [PMID:32814053]. A testis-restricted spermatid protein appearing as prey in a
  neurodegeneration Y2H matrix, with no orthogonal assay and no follow-up. UniProt records
  them at face value, e.g. "Q9Y614; P55212: CASP6; NbExp=3; IntAct=EBI-25835070, EBI-718729;".
- **GO:0005200 (TAS) and GO:0015629 (TAS), both PMID:10373328** — the 1999 cloning paper.
  Reading it settles them: "Two novel human actin-like genes, ACTL7A and ACTL7B, were identified by cDNA selection and direct genomic sequencing"
  followed by mapping, Northern expression, and mutation screening. There is no protein-level
  experiment in it at all. These two annotations restate the paper's *name* for the genes.
  This is the campaign's recurring defect in its purest form: a fold name entering GO as an
  activity and as a location.

## 5. ACTL7A vs ACTL7B are distinguishable, and the review should keep them apart

By the global BLOSUM62 alignment used here they are 58.6% identical over the whole chain
(58.1% for the mouse paralogue); the 1999 paper reports proteins "that show greater than 65% amino acid identity to each other."
[PMID:10373328] and the 2003 mouse paper "The two deduced amino acid sequences had 60% homology, and they had approximately 40% homology with other actins."
[PMID:12672658] — the spread reflects alignment method and identity-vs-similarity, not a
conflict; either way they are clearly distinct proteins. Expression differs (testis+prostate
vs many tissues, section 1); the 2003 mouse work put them in different compartments; and
their phenotypes differ in the literature (ACTL7A: acrosome/acroplaxome attachment and
subacrosomal F-actin, human fertilisation failure; ACTL7B: OAT/MMAF with DYNLL1/2
mislocalisation). Of the eight protein-level WITH/FROM tokens across ACTL7B's two CC IBA
rows, **four are ACTL7A orthologues** (mouse Actl7a twice, rat Actl7a, human ACTL7A) and only
**one is a true ACTL7B orthologue** (mouse Actl7b); the remaining three are ARP9/actin-like
proteins from yeast, Candida and trypanosome. The pair is therefore a live transfer risk.
Concretely: human ACTL7A carries
GO:0033011 (perinuclear theca) by IDA, which *is* a descendant of GO:0005856 cytoskeleton;
ACTL7B's reported locations (acrosomal vesicle GO:0001669, sperm head-tail coupling
apparatus GO:0120212, nucleus) are **not** cytoskeletal in the ontology. The cytoskeleton
annotation would be defensible for ACTL7A and is not for ACTL7B.

## 6. Actions taken

| GOA row | term | action | one-line reason |
|---|---|---|---|
| 1 | GO:0005634 nucleus | KEEP_AS_NON_CORE | localisation corroborated in mouse ortholog, but no nuclear activity known; `is_active_in` overstates |
| 2 | GO:0005737 cytoplasm | ACCEPT | orthologue-anchored IBA; correct but uninformative |
| 3 | GO:0005198 structural molecule activity | ACCEPT | PAINT's deliberate generalisation; the only defensible MF today |
| 4 | GO:0005856 cytoskeleton | MARK_AS_OVER_ANNOTATED | by-similarity UniProt CC laundered into IEA; ACTL7B's reported compartments are not cytoskeletal |
| 5 | GO:0007010 cytoskeleton organization | REMOVE | mechanical inference from the row-10 TAS; no independent support |
| 6–9 | GO:0005515 protein binding ×4 | MARK_AS_OVER_ANNOTATED | single unreplicated Y2H matrix, no tissue rationale, uninformative term |
| 10 | GO:0005200 structural constituent of cytoskeleton | REMOVE | TAS from a paper with no protein-level experiment; PAINT IRD-negated; D-loop 0/8 |
| 11 | GO:0015629 actin cytoskeleton | REMOVE | same paper, no localisation experiment; term requires an actin-composed structure |

New annotations proposed (all ISS from mouse Actl7b, Q9QY83): GO:0045503 dynein light chain
binding, GO:0007286 spermatid development, GO:0001669 acrosomal vesicle, GO:0032880
regulation of protein localization.

## 7. Curation debts noticed elsewhere

- **Mouse Actl7b (MGI:1343053 / Q9QY83) has only 5 GO annotations** and none from either 2023
  knockout paper. The mouse record should carry the IMP/IPI/IDA annotations from
  PMID:36617158 and PMID:37800308; the human ISS annotations proposed here depend on them.
- UniProt Q9Y614 has no FUNCTION comment despite two 2023 knockout papers, and its
  subcellular location is still `{ECO:0000250}`.
- The four IntAct/Y2H interactions are recorded in UniProt without any indication that they
  come from a single neurodegeneration-focused screen of a protein not expressed in brain.
- The same legacy ProtInc TAS pair from PMID:10373328 sits on the paralogue: human ACTL7A
  carries `GO:0005200 TAS PMID:10373328` and `GO:0005856 TAS PMID:10373328`. So this is a
  systematic ProtInc-era artefact of one 1999 cloning paper affecting both genes, not a
  one-off. (ACTL7A is being reviewed in parallel; noted here for cross-reference only, no
  files touched.)
