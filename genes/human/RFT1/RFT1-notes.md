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
