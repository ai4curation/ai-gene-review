# RFT1 (human, Q96AA3) — curation notes

Started 2026-08-23. Re-review triggered by the RFT1 "flippase controversy", cross-referenced
against the disease-mechanism curation in
[monarch-initiative/dismech PR #9261](https://github.com/monarch-initiative/dismech/pull/9261)
("curate(RFT1-CDG): new entry, with the flippase attribution curated as contested"), which
records two competing mechanistic models (CANONICAL: RFT1 as flippase; ALTERNATIVE: RFT1
plays an essential but non-flippase accessory role) rather than asserting the flippase role.

## The controversy, in order

This is a genuinely unresolved, 24-year-old dispute. It is *not* the case that a single 2024
paper closed it, and the prior version of this review said so incorrectly.

### 1. Genetics says flippase (2002)

Helenius et al. depleted yeast Rft1 and saw cytosolic accumulation of M5GN2-PP-Dol
[PMID:11807558, "Here we provide evidence that yeast RFT1 encodes an evolutionarily conserved
protein required for the translocation of Man5GlcNAc2-PP-Dol from the cytoplasmic to the
lumenal leaflet of the ER membrane."]. Note the wording is "required for", not "catalyses".

### 2. Biochemistry says no (2008–2013)

- Frank/Sanyal/Rush/Waechter/Menon, Nature Brief Communication Arising: reconstituted
  vesicles flip M5GN2-PP-Dol without Rft1 [PMID:18668045, "We now show that a specific ER
  protein(s), but not Rft1, is required to flip Man(5)GlcNAc(2)-PP-Dol in reconstituted
  vesicles."] and "Rft1 may have a critical accessory role in translocating
  Man(5)GlcNAc(2)-PP-Dol in vivo, but the Man(5)GlcNAc(2)-PP-Dol flippase itself remains to
  be identified."
- Sanyal & Menon PNAS 2009 [PMID:19129492] characterised a specific, ATP-independent
  M5-DLO flippase activity in ER vesicles.
- Rush et al. JBC 2009: Rft1-depleted sealed yeast microsomes retain flippase activity
  [PMID:19494107, "no difference was seen in the level of M5-DLO flippase activity in sealed
  wild type and Rft1-depleted microsomal vesicles"] and "although Rft1 may play a critical
  role in vivo, depletion of this protein does not impair the transbilayer movement of M5-DLO
  in sealed microsomal fractions prepared from disrupted cells."
- Jelk et al. JBC 2013: *Trypanosoma brucei* is a eukaryote that lives without Rft1
  [PMID:23720757, "We report that TbRft1-null procyclic trypanosomes grow nearly normally."
  and "They have normal steady-state levels of mDLO and significant N-glycosylation,
  indicating robust M5-DLO flippase activity."]. Their proposal: "rather than facilitating
  M5-DLO flipping, Rft1 facilitates conversion of M5-DLO to mDLO by another mechanism,
  possibly by acting as an M5-DLO chaperone."

### 3. Reconstitution says yes — *in vitro* (June 2024)

Chen et al. Nat Commun [PMID:38886340] built a fully reconstituted assay and showed purified
protein suffices. Critically for this review, they tested **human** RFT1, not only yeast:
"In addition to yeast Rft1 (FLAG-ScRft1), recombinant human Rft1 (HsRft1-FLAG) was also
tested (Fig. 2c, f). As with ScRft1, proteoliposomes reconstituted with HsRft1 showed almost
90% conversion of M5GN2 to M3GN2 after 2 h of incubation." So the human IDA in GOA is
legitimately about the human protein.

**But the activity is ATP-independent.** The reactions were run "without ATP", and
"Translocation was ATP-independent, occurred with similar kinetics for both dolichol or
phytanol lipid carriers, and importantly, was dependent on addition of purified Rft1 or
archaeal Agl23". This matters for term choice — see below.

### 4. The dispute survives the reconstitution (2024–2026)

- Hirata et al. JBC 2024 [PMID:39025454], published *after* Chen et al., still frames the
  cellular role as open: "It is therefore not known what essential role Rft1 plays in
  N-glycosylation." They also establish human Rft1 topology directly: "We show that it is a
  multispanning membrane protein located in the ER, with its N and C termini facing the
  cytoplasm. It is not N-glycosylated."
- Chiduza et al. Protein Sci 2026 [PMID:42417535] is the current state of the art and
  concedes the *in vitro* activity while separating it from the *in vivo* essential role:
  "While this activity has been demonstrated in liposomes reconstituted with purified Rft1,
  biochemical evidence of additional M5-DLO scramblases and the viability of Rft1-null
  Trypanosoma brucei suggest that scrambling may be a moonlighting function of Rft1 rather
  than its essential cellular role." Their mutagenesis is the decisive new datum:
  "Strikingly, the portal-blocking mutant which is predicted to lack scramblase activity
  supported robust growth. These data suggest that while M5-DLO binding is important for
  Rft1's essential function, scrambling activity is dispensable." They again favour a
  chaperone model: "We speculate that Rft1's essential role may be as an M5-DLO chaperone,
  capturing and routing M5-DLO propitiously on the cytoplasmic side of the ER to coordinate
  DLO biosynthesis."

### Where that leaves GO

Two distinct claims must be kept apart, and the GOA rows conflate them:

1. **Human RFT1 can translocate M5GN2-PP-Dol across a bilayer.** Directly demonstrated with
   purified human protein (Chen 2024). This is a sound MF/BP annotation.
2. **That translocation is the essential in-vivo function underlying RFT1-CDG.** Contested;
   the portal-blocking mutant grows (Chiduza 2026), Rft1-null trypanosomes glycosylate
   (Jelk 2013), Rft1-depleted microsomes still flip (Rush 2009). What is *not* in dispute is
   that loss of RFT1 blocks the pathway at M5GN2-PP-Dol in patients (Haeuptle 2008
   [PMID:18313027]; Vleugels 2009 [PMID:19701946]).

## Term-choice problem: GO:0034202 requires ATP

QuickGO definition of **GO:0034202 glycolipid floppase activity**: "Catalysis of the movement
of a glycolipid from the cytosolic to the exoplasmic leaflet of a membrane, using energy from
the hydrolysis of ATP."

RFT1's demonstrated activity is explicitly ATP-independent (Chen 2024, above), and the
Menon-lab literature calls it a **scramblase**, not a floppase. So GO:0034202 is a
definitional mismatch on the energetics, regardless of how the flippase controversy is
settled. Checked alternatives:

| Term | Verdict |
|---|---|
| GO:0034202 glycolipid floppase activity | wrong — requires ATP hydrolysis |
| GO:0140327 flippase activity | wrong — requires ATP, and wrong direction (exoplasmic→cytosolic) |
| GO:0017128 phospholipid scramblase activity | right energetics ("by an ATP-independent mechanism") but wrong substrate class |
| GO:0140303 intramembrane lipid transporter activity | correct and safe: "Enables the transport of a lipid from a region of a membrane to a different region on the same membrane"; ATP-agnostic parent of both the flippase and scramblase branches |

GO:0140303 is also exactly the wording UniProt uses for Q96AA3: "Intramembrane glycolipid
transporter that operates in the biosynthetic pathway of dolichol-linked oligosaccharides".
Note UniProt is itself hedged and has not yet incorporated Chen 2024: "RFT1 could mediate the
translocation of the cytosolically oriented intermediate DolPP-GlcNAc2Man5 ... However, the
intramembrane lipid transporter activity could not be confirmed in vitro (By similarity)."

Recommendation: MODIFY both GO:0034202 rows (the MGI IDA and the Reactome TAS) to
GO:0140303, and propose a new child term "glycolipid scramblase activity" (ATP-independent,
bidirectional) so the demonstrated activity can be stated at its real specificity.

## Other annotation notes

- **GO:0034203 glycolipid translocation (IGI, PMID:18313027)** — the evidence is
  complementation of yeast Δrft1 by human RFT1 cDNA. That restores pathway flux; it does not
  discriminate transport from chaperoning, which is precisely the step Rush 2009 and Jelk 2013
  show is separable. The genetic evidence supports pathway involvement (GO:0006488); the
  transport step is separately and better supported by the Chen 2024 IDA row. MODIFY.
- **GO:0005515 protein binding (IPI, PMID:32296183)** — nine interactors from the HuRI
  all-by-all Y2H map (AQP6, BEST2, CNR2, CREB3L1, ERGIC3, MUC1, RNF144A, TMX2, TSPAN12). All
  are membrane proteins; none has a role in LLO assembly. Uninformative term, no functional
  follow-up. REMOVE per project curation guidelines.
- **GO:0005789 ER membrane** — safe across every evidence line, and now with direct human
  topology data (Hirata 2024). Note UniProt's own CC SUBCELLULAR LOCATION is still
  `ECO:0000250|UniProtKB:P38206` (by similarity to yeast).
- **GO:0016020 membrane (IEA)** — correct but subsumed by GO:0005789; non-core.

## Provenance / caching done in this session

Newly cached: PMID:11807558, PMID:18668045, PMID:19129492, PMID:19494107, PMID:19701946,
PMID:23720757, PMID:38617304 (bioRxiv preprint), PMID:39025454 (JBC version), PMID:41427416
(bioRxiv preprint), PMID:42417535 (Protein Sci 2026).

## OpenScientist run (2026-08-24)

Commissioned an independent structural run to test whether the RFT1-CDG residues
discriminate the two models:
`genes/human/RFT1/RFT1-hypotheses/scramblase-vs-binding-cavity/openscientist.md`
(1290 s, 3 iterations; artifacts include a residue-classification CSV and an evidence
matrix). Framed deliberately with Model A and Model B stated symmetrically — the
auto-derived hypotheses from `just gene-hypothesis-list` were **not** used, because they
embed this review's own rationale verbatim and would have made the run a confirmation
exercise.

### Result: the premise was wrong, and that is the useful part

Computed on AF-Q96AA3-F1 v6 (mean pLDDT 90.4), Shrake-Rupley SASA plus pore-axis geometry:

| residue | rSASA | radial from axis | side-chain orientation | conservation (9 orthologs) | call |
|---|---|---|---|---|---|
| R67  | 0.13 | 9.1 Å  | opens inward (−0.21)  | Arg invariant 9/9   | central-cavity-lining (high) |
| K152 | 0.26 | 12.6 Å | inward/neutral (−0.09)| basic K/R 7/9       | inner vestibule (moderate) |
| E298 | 0.46 | 13.8 Å | opens outward (+0.44) | acidic E/D 9/9      | neither cavity nor portal |

Reference clouds: axis-facing TM residues median exposure-radial-out −0.07, lipid/portal-facing
+0.75. "No disease residue lines the lateral dolichol portal."

The run's own conclusion is that this **cannot** discriminate the models: "model, so
cavity-localised disease mutations do not discriminate them" — headgroup binding is
required for transport under Model A just as much as it is required for chaperoning under
Model B. That is a correction to the premise I gave it, and it kills my original framing of
suggested experiment 3 (allele *position* is uninformative; only a measured dissociation
between binding and transport is). Recorded rather than dropped.

Two genuinely new observations worth keeping:

- The MOP/MATE inverted-topology two-lobed fold is present in the human model (internal C2
  repeat, 40 Cα at 3.07 Å RMSD), but "the apo human model's innermost lining is net-acidic"
  (net −2). The cationic cavity in the current mechanistic model is a property of
  *substrate-docked yeast* models. So the electrostatics of the resting state are unverified —
  now a suggested cryo-EM experiment.
- E298 is a conserved, exposed, outward-facing acidic residue. Its role is unexplained by
  either model.

### One claim from the run that is wrong — do not import

It flags human **Q9NWF4** and mouse **Q9D8F3** as "divergent ~450-aa RFT1 paralogs" at risk of
transitive annotation. Checked against UniProt: Q9NWF4 is **SLC52A1** (S52A1_HUMAN, 448 aa,
riboflavin transporter) and Q9D8F3 is **Slc52a2** (S52A2_MOUSE, 450 aa). Both list `RFT1` as a
legacy **gene-symbol synonym** (SLC52A1 synonyms: GPR172B, PAR2, RFT1). They are not paralogs
of Q96AA3 at all — the 26% identity is noise.

The hazard the run pointed at is nonetheless real, just misdiagnosed: **`RFT1` is an ambiguous
symbol.** Any literature search, ortholog set or text-mined annotation for "RFT1" can silently
pick up riboflavin-transporter papers. Always anchor on Q96AA3 / the 541-aa
Man(5)GlcNAc(2)-PP-dolichol translocation protein, never on the bare symbol.

### Where it leaves the review

Convergent with the curation already made: keep the MF at GO:0140303 anchored to the
PMID:38886340 IDA, flag the debate, and do not assert the translocase mechanism as settled.
Nothing in the run required a change of action on any annotation.

### Framing correction: what of this bears on evolved function

The run was anchored on the three RFT1-CDG missense positions, which is a disease-first
framing and the wrong entry point for this repo. Disease alleles matter here only where they
illuminate the evolved function, and by the run's own conclusion the allele *mapping* does
not — substrate binding is required under both models, so where the alleles sit cannot
separate them. Splitting the output on that criterion:

**Bears on wild-type function (disease-independent):**

- The MOP/MATE inverted-topology alternating-access fold is present in the human protein: a
  two-lobed bundle enclosing a central pore axis geometrically separable from the lipid-facing
  periphery, internal C2 repeat 40 Cα @ 3.07 Å RMSD. This is a statement about the architecture
  the family evolved, and it is the structural basis for GO:0140303.
- The near-axis basic positions are deeply conserved — an invariant Arg 9/9 and a conserved
  basic K/R 7/9 across human → fungi → Dictyostelium. Deep conservation of buried, inward-facing
  basic residues at the narrowest point of the axis marks the substrate-binding site as a
  *selected* feature. This holds whether the selected activity is transport or capture-and-routing,
  and it is independent of the fact that two of those positions happen to be mutated in patients.
- The apo human axis lining is net-acidic (net −2). The cationic cavity of the published
  mechanism is a property of substrate-docked yeast models, so the resting-state electrostatics
  of the wild-type protein are unverified.
- Position 298 is a conserved exposed acidic residue. Conservation of a solvent-exposed position
  is the interesting part — exposed residues are usually less constrained, so this looks like a
  functional interface rather than a folding requirement. Unexplained by either model.

**Disease-only, no bearing on evolved function:** the pathogenicity of R67C/K152E/E298K, and
the whole cavity-vs-portal-discriminates-the-models premise (which failed anyway).

Consequently the review now states this gap in terms of *which activity RFT1 evolved to
perform*, not *which activity's loss causes CDG*, and suggested experiment 3 is framed around
the conserved substrate-site positions, with the CDG substitutions demoted to what they
actually are here — convenient ready-made reagents at those positions.

**Better question for a follow-up run, WT-first:** which positions in the family are most
constrained across a deep MSA, and do they line the central cavity, the lateral portal, or
neither? That asks what evolution actually conserved and where it sits in the transport
machinery, with no disease input at all. The run itself flags the missing deep MSA as a
limitation (it used pairwise Needleman-Wunsch against 9 orthologs).
