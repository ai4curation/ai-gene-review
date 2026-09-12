# AP5S1 (sigma-5) — research notes

Working notes for the review of human AP5S1 (UniProt Q9NUS5). Provenance is inline as
`[PMID:NNNN "verbatim quote"]`; structural measurements made for this review are cited as
`file:human/AP5S1/AP5S1-bioinformatics/RESULTS.md`.

## 1. Identity, and what the record actually says

`AP5S1-uniprot.txt` is Q9NUS5 = `AP5S1_HUMAN`, 200 aa, RecName "AP-5 complex subunit
sigma-1", AltName "Sigma5", gene `AP5S1` with synonym `C20orf29`. So the protein the
literature calls **sigma-5 / σ5** and the protein the older papers call **C20orf29** are
the same entry, and both names have to be searched. PANTHER assigns it to
`PTHR16120:SF0` (AP-5 COMPLEX SUBUNIT SIGMA-1) — *not* to `PTHR11753`, the family that
holds the AP-1/AP-2/AP-3/AP-4 sigma subunits. Pfam `PF15001`, InterPro `IPR029392`, both
of which are AP5S1-specific rather than pan-sigma. Two cryo-EM structures are listed,
`8YAB` and `8YAH`, with chain C = residues 1–200, i.e. the whole protein.

UniProt's own summary of the function is hedged: "As part of AP-5, a probable fifth
adaptor protein complex it may be involved in endosomal transport", and the subunit
composition line reads "Probably part of the adaptor protein complex 5 (AP-5) a tetramer
composed of AP5B1, AP5M1, AP5S1 and AP5Z1." Pharos rates the protein **Tdark**. That is
the right expectation to start from: this is a genuinely under-characterised subunit of a
sparsely-characterised complex.

## 2. The affinage record is empty, and that is itself a finding

`AP5S1-deep-research-affinage.md` reports `n_discoveries: 0`, `citation_count: 0` and the
body "No mechanistic discoveries found in literature." The trust gates passed
(`.affinage.log`: "trust gates clear"), which is consistent with the campaign note that
affinage's gates measure precision, not recall — with zero citations returned there was
nothing to be imprecise about. Every paper used in this review was found independently.

What affinage missed, all of it findable from Europe PMC in one pass on "AP5S1", "AP-5
adaptor", "AP-5 SPG11 SPG15":

| PMID | What it supplies for this gene |
|---|---|
| 20613862 | discovery of the KIAA0415/SPG11/SPG15/C20orf29/DKFZp761E198 complex; the C20orf29 HR-repair knockdown |
| 22022230 | names C20orf29 as σ5, localises it, shows the knockdown phenocopy and the co-IP |
| 23825025 | the six proteins co-IP at ~1:1:1:1:1:1 and all six knockdowns phenocopy |
| 26085577 | loss of AP-5 gives aberrant, storage-filled endolysosomes |
| 29381698 | AP-5 works in late endosome-to-Golgi retrieval (AP5Z1 knockout + proteomics) |
| 33464297 | recruitment by PI3P + Rag GTPases; the explicit statement that AP-5's sorting-signal domains are different |
| 40175557 | cryo-EM of AP5–SPG11–SPG15; the super-open conformation; PI3P binding and membrane remodelling |
| 40081374 | AP-5 subunit variants cause macular dystrophy — and AP5S1 is the one subunit with no disease yet |

(`27392064`, HIV-2 Gag release depends on AP-5, and `37871017`, spatacsin promotes AP5Z1
degradation, are AP-5 papers that do not test σ5: the first knocks down AP5M1, the second
works on AP5Z1 and spastizin. Context, not evidence for this gene.)

## 3. How σ5 came to be called a subunit at all

Słabicki et al. pulled the complex out of a DNA-repair screen. Tagged KIAA0415 (now
AP5Z1/SPG48) co-immunoprecipitated four partners
[PMID:20613862 "Immunoprecipitation experiments followed by spectrometric identification of co-isolated proteins revealed interactions of KIAA0415-LAP with SPG11, SPG15, C20orf29, and DKFZp761E198"],
and reciprocal pulldowns with three different tagged baits confirmed a five-protein core.

Hirst et al. then argued from structure prediction and knockdown phenotype that C20orf29
is the small subunit of a fifth AP complex: it is 200 aa, its HHpred hits are σ2 (96.8%),
ζ-COP (95.9%) and σ1 (95.8%), and
[PMID:22022230 "C20orf29 has a similar predicted secondary structure to the σ subunits, but with longer loops connecting the folded domains"].
The naming is explicit
[PMID:22022230 "we are calling the small subunit (C20orf29) σ5"].

Three independent lines put σ5 inside the complex:

* **Co-IP from the σ5 side.** GFP-tagged C20orf29 pulls down μ5 and β5
  [PMID:22022230 "the anti-GFP antibody not only brings down the construct itself, but also C14orf108 and DKFZp761E198"].
* **Knockdown phenocopy.** [PMID:22022230 "knocking down either KIAA0415/SPG48 or C20orf29 produces the same phenotype as knocking down μ5 or β5"] — the
  CIMPR and the retromer subunit Vps26 collapse into larger, brighter, fewer perinuclear
  puncta.
* **Stoichiometry.** All six proteins co-IP at ~1:1:1:1:1:1 from both cytosol and
  detergent-extracted membranes, and all six knockdowns trap the CIMPR in early-endosome
  clusters (PMID:23825025, abstract only — `full_text_available: false`).

## 4. Localisation

σ5 is not a resident membrane protein; it cycles. For μ5, fractionation showed the
protein partitions roughly equally between membrane and cytosol and is absent from
clathrin-coated vesicles. For σ5 specifically the evidence is imaging: GFP-tagged
C20orf29 overlaps LAMP1
[PMID:22022230 "0.789±0.003 for C20orf29-GFP and LAMP1"], versus 0.565 for the CIMPR, and
the paper's conclusion for the complex is
[PMID:22022230 "these observations suggest that the site of action of AP-5 is the late endosome and/or lysosome, as defined by the presence of LAMP1"].
The GOA IDA rows for lysosome and late endosome, and the HPA IDA for cytosol, all sit on
that. UniProt's membrane-side statements (late endosome membrane, lysosome membrane,
peripheral, cytoplasmic side) are `ECO:0000305` — curator inference from the same paper,
not separate observations. That is worth recording but is not a reason to reject them:
a peripheral cytosolic-face assignment is exactly what a cycling adaptor looks like.

Hirst et al. 2021 later resolved the localisation question properly: recruitment is
coincidence detection on PI3P (through the SPG15 FYVE domain) plus Rag GTPases, is
enhanced by starvation, and is ARF1-independent — unlike AP-1, AP-3 and AP-4
(PMID:33464297).

## 5. What the complex does — and what of that is attributable to σ5

The pathway assignment rests on complex-level experiments. Hirst et al. 2018 knocked out
**AP5Z1** (not AP5S1) with CRISPR and used organellar mapping plus vesicle-fraction
proteomics: retromer redistributes, Golgi proteins GOLIM4 and GOLM1 are depleted from
vesicle fractions, and retrieval of the CIMPR, GOLIM4 and GOLM1 from endosomes back to
the Golgi is impaired, worsened by knocking retromer down as well (PMID:29381698). Loss
of AP-5 in patient fibroblasts and knockdown cells produces enlarged, multilamellar,
storage-filled endolysosomes (PMID:26085577). The 2025 cryo-EM work adds an in vitro
activity for the hexamer: it binds PI3P, senses curvature and remodels membrane, and is
placed upstream of autolysosome tubulation (PMID:40175557).

**Grading which of this tests σ5.** Only Hirst 2011 and Hirst 2013 knock down σ5 itself,
and both read out the same CIMPR/Vps26 phenotype as the other subunits. The AP5Z1
knockout proteomics, the patient fibroblasts, the reconstituted membrane-remodelling
assays and the mouse models are complex-level or other-subunit experiments. So for GO the
honest position is: σ5 participates in the endosomal transport pathway (subunit-level
IMP evidence exists), while the specific late-endosome-to-Golgi retrieval assignment
belongs to the complex and reaches σ5 by complex membership rather than by its own
perturbation.

## 6. Does σ5 contribute a cargo-binding site? No — and the structure gives a reason

This is the question the sibling sigma reviews raise, because σ1/σ2/σ3 build half of the
acidic dileucine ([DE]xxxL[LI]) site with their large adaptin, and because the AP1S1
analysis showed that residue conservation at that pocket does **not** discriminate
binders from the verified non-binder σ4. For σ5 the answer has to come from somewhere
other than conservation scoring, and it does.

The people who discovered AP-5 have said twice that AP-5 cannot be assumed to read the
canonical signals:
[PMID:22022230 "In addition, the lack of key residues in μ5 for binding YXXΦ motifs indicates that, if AP-5 is an adaptor, it must be recognising some other type of sorting signal"]
and, a decade later,
[PMID:33464297 "Even highly conserved regions of the subunits, such as the domains that bind to sorting signals, are different in AP-5, indicating that cargo recognition (assuming it occurs) must be by a different molecular mechanism."]
In the same group's 2018 work the cargo-binding capacity in this system is attributed to
the accessory protein SPG15, not to the heterotetramer
[PMID:29381698 "The ability of SPG15 to bind cargo supports this possibility, because the only known cargo-binding subunits of COPI are associated with the protocoatomers, not the core heterotetramer"].

I tested this structurally rather than by sequence
(`AP5S1-bioinformatics/`, `sigma5_structure.py`). Method: define the dileucine site
*empirically* as the σ2 residues within 4.5 Å of the bound CD4 dileucine peptide in the
AP-2 core co-crystal 2JKR (19 residues, no list typed in), then carry those positions
onto σ5 (8YAB chain C) by sequence-independent structural superposition, with the second
σ2 copy as positive control and the β5 solenoid as negative control. Results:

* The fold is there —
  [file:human/AP5S1/AP5S1-bioinformatics/RESULTS.md "of 19 sigma2 residues that contact the dileucine peptide, 18 have a structurally equivalent position in sigma-5"] —
  at RMSD 3.53 Å versus 0.03 Å (identical control) and 6.08 Å (unrelated fold).
* The chemistry is not. Only 3 of the 18 equivalent positions carry the same residue.
  The substitutions are precisely at the functional positions: σ2 V88 → σ5 T143 and σ2
  V98 → σ5 R151 replace hydrophobic pocket lining with polar and basic side chains, and
  σ2 R15 — the basic patch that reads the acidic residue of the motif, and the FHH3
  hotspot — is σ5 Y25. The functional weight of those particular positions is not my
  inference: they are the ones whose substitution kills binding in the AP-2 co-crystal
  study [PMID:19140243 "Mutation of a number of these to hydrophilic residues (σ2L65S, σ2V88D, σ2V98S or σ2L103S), or filling in the pocket by replacement of σ2A63 or σ2N92 with tryptophan, strongly inhibited binding of recombinant AP2 core complexes to different dileucine motifs"],
  and Arg15 is the one that carries a Mendelian disease
  [PMID:23222959 "missense mutations of AP2 σ subunit (AP2S1) affecting Arg15, which forms key contacts with dileucine-based motifs of CCV cargo proteins, result in familial hypocalciuric hypercalcemia type 3 (FHH3)"].
* And the surface is not free: three of the equivalent positions (L120, L152, S156) are
  in contact with the ζ N-terminus (ζ residues 1–10) in the assembled core. In AP-2 that
  surface is blocked by the β2 N-terminus in the *closed* state and released on
  activation; in AP-5 the deposited structure is the open, SPG11-bound form and the
  equivalent surface is still covered, by ζ instead.

That last point independently reproduces what the structure paper's authors report in
their own words (bioRxiv 2024.06.14.598999, the preprint of PMID:40175557: "the σ5
binding site is plugged by the nearby N-terminus of ζ"). I record it here as a
cross-check on my own measurement, not as a citable source — the published version is
abstract-only in our cache.

The sequence control matters for how this is written up: every pairwise alignment of σ5
against a human sigma paralog scores negative and within a few SD of shuffled sequence
(best z = 3.09 against σ1A, 1.98 against σ2), so no residue-level claim about σ5 could
have been made from pairwise sequence alignment at all. Hirst et al. needed HHpred, not
BLAST, to see this homology in the first place. The MAFFT-based alignment in the AP2S1
review reports AP5S1 sharing only the R15 and L65 columns with σ2 out of eight pocket
positions; my structure-based mapping disagrees with it at R15 (structurally, σ5 has Y25
there), which is what one expects when a MAFFT column is asked to carry a 20%-identity
pair. The structural mapping is the one to trust.

**Conclusion for annotation:** no cargo-signal binding function for σ5, no `GO:0140312`
cargo adaptor activity on the subunit, and the bare `GO:0005515` rows cannot be upgraded
to an informative MF because the informative MF does not exist and would not be true if
it did.

## 7. What σ5 *does* contribute, structurally

The same analysis gives a positive result. In 8YAB, σ5 buries
[file:human/AP5S1/AP5S1-bioinformatics/RESULTS.md "Sigma-5 is the zeta-adaptin partner: it buries 2621.8 A^2 against the zeta trunk over 60 residues, and touches neither beta5 nor mu5."]
— so σ5 is the ζ partner in the ζ/σ5 hemicomplex, exactly the position σ1/σ2/σ3 hold in
their complexes. It additionally contacts the SPG11 WD40-hairpin over 20 residues (755
Å² buried), which none of the other AP sigma subunits does, because no other AP complex
has a stable SPG11-like partner. This is the structural counterpart of the biochemistry
in the 2025 paper, whose abstract states
[PMID:40175557 "the N-terminal region of SPG11 is required for AP5 complex interaction and assembly"].

So the defensible subunit-level statement is structural, not catalytic or
cargo-recognising: σ5 is an obligate small subunit that forms the ζ/σ5 hemicomplex and
contributes part of the surface through which SPG11 clamps the two arms of AP-5
together. GO has no term for "small subunit of an adaptor heterotetramer" specifically,
but it does have `GO:0005198` structural molecule activity, whose definition — "the
action of a molecule that contributes to the structural integrity of a complex" — covers
exactly this, and which the sibling AP-4 small subunit review adopted for the same role.
That is the one MF asserted here, as a NEW row with IDA from the structure, and it is
asserted with its limit stated: sigma-5 has never been removed from cells, so "is
required for AP-5 to exist" is *not* claimed, only "is an integral structural component
of it". No cargo-recognition or adaptor activity is asserted at all.

Note also that the IntAct interaction behind the GOA IPI row with mouse Ap5z1 (Q3U829,
from PMID:40175557) is not a stray two-hybrid hit: it is the co-expressed, purified,
3.26 Å-resolved ζ/σ5 pair. It is the best-evidenced interaction on this gene.

## 8. The DNA-repair annotation

AP5S1 carries `GO:0000724` twice, as IMP from PMID:20613862 and as IEA from
InterPro:IPR029392. The IMP is real and on-target: C20orf29 was not a primary screen hit,
but when the KIAA0415 interactors were tested in the DR-GFP assay,
[PMID:20613862 "significant reduction of GFP positive cells were observed upon silencing of C20orf29 and SPG15 with two independent esiRNAs"].
Two things temper it. Within the same experiment the effect is not a property of the
complex: [PMID:20613862 "Knockdown of SPG11 and DKFZp761E198, however, did no have an effect on the percentage of GFP positive cells."] (*sic*). And the AP-5 discoverers argued
the phenotype is likely indirect, noting that the screen also returned a Rho GEF and that
signalling perturbations can affect repair; their own data (endosomal localisation,
endosomal knockdown phenotypes, no helicase motifs) point away from a nuclear role. In
the fifteen years since, no follow-up has connected AP-5 to recombination, while five
papers have connected it to endolysosomal sorting. `KEEP_AS_NON_CORE` for the IMP.

The IEA is a different matter. I fetched IPR029392 from the InterPro API: its GO mapping
is `GO:0000724`, `GO:0016197`, `GO:0030119`, and its description reads "It is required
for efficient homologous recombination DNA double-strand break repair", cited to
`PUB00067710` = PMID:20613862. So the IEA on AP5S1 is that single HeLa esiRNA result
coming back to the same gene through a family signature — it supplies nothing the IMP has
not already supplied, and the same mapping propagates a human cell-line phenotype
family-wide: the InterPro API reports 790 proteins across 2,294 taxa for IPR029392, and
the PANTHER family it is built on, PTHR16120, reports 830 proteins across 2,269 taxa in
its own metadata. `EVIDENCE_CIRCULAR_OR_REDUNDANT` on this row;
the family-wide over-reach goes to `suggested_questions` for InterPro.

## 9. The five IBAs

All five come from one node. The PAINT slice
(`interpro/panther/PTHR16120/PTHR16120-paint.tsv`, five rows) shows node
**PTN000413531** carrying IBDs for `GO:0005764`, `GO:0005770`, `GO:0005829`,
`GO:0030119` and `GO:0016197`, each with a single seed: `UniProtKB:Q9NUS5` — AP5S1
itself. The GOA WITH/FROM on each row is `PANTHER:PTN000413531|UniProtKB:Q9NUS5`, i.e.
the node plus the target. That is the self-referential pattern the campaign brief calls
valid and expected, and it is unusually clean here: the family has one subfamily
(`PTHR16120:SF0`) and one human member, so the node's assertion is "this is the
eukaryote-wide σ5 orthology group, and what was measured on the human protein is the
group's ancestral property". No AP-1/AP-2/AP-3 sigma terms leak in — there is no
clathrin-related term anywhere in the slice, which is the right outcome for a
non-clathrin complex and is a direct consequence of σ5 sitting in its own PANTHER family
rather than in PTHR11753.

The five terms are each independently grounded on the human protein: lysosome and late
endosome by IDA (PMID:22022230), cytosol by IDA (HPA), AP-type complex by IDA
(PMID:22022230 co-IP), endosomal transport by IMP (PMID:22022230 knockdown). No IRD or
IKR exists anywhere in the slice. Root cause `NO_FAILURE_CORE` on all five, with the
`GO:0005829` one downgraded in my summary to a real-but-non-core location (the cytosolic
pool is the unrecruited pool).

Two caveats I checked rather than assumed. `GO:0030119` is the AP-type parent whose
definition is written around clathrin — "Any of several heterotetrameric complexes that
link clathrin (or another coat-forming molecule, as hypothesized for AP-3 and AP-4) to a
membrane surface" — but the specific child `GO:0044599` (AP-5 adaptor complex) exists and
is in `GO:0030119`'s descendant closure (QuickGO ancestors of GO:0044599 include
GO:0030119), so the right action for the direct-evidence row is MODIFY to the child, not
removal of the parent. And the mouse ortholog Q9D742 is 170 aa against the human 200 aa,
so the family is genuinely divergent even between rodent and primate — consistent with
Hirst's observation that human and mouse β5 are only 85% identical while β2 differs by a
single residue.

## 10. Where GO cannot express this biology

1. **The hexamer has no term.** ComplexPortal curates `CPX-20045`
   "AP5-Spastizin-spatacsin complex" (AP5Z1:AP5B1:ZFYVE26:SPG11:AP5M1:AP5S1, built from
   CPX-5181 + CPX-26503) and it carries **no GO cross-reference**, while CPX-5181 (the
   tetramer) maps to GO:0044599, GO:0005770, GO:0016192 and GO:0140312. QuickGO text
   search for "spatacsin", "spastizin" and "AP-5" returns no complex term other than
   GO:0044599. The consequence is visible in this gene's own annotation set: the
   ComplexPortal rows sourced from the hexamer paper (PMID:40175557) reach AP5S1 as
   `located_in lysosome`, `located_in late endosome` and `involved_in lysosome
   organization` — not as `part_of` anything, because there is nothing to be part of.
2. **No molecular function fits.** `GO:0140312` cargo adaptor activity requires "Binding
   directly to the structural scaffolding elements of a vesicle coat (such as clathrin or
   COPII), and bridging the membrane, cargo receptor, and membrane deformation
   machinery". AP-5 binds no clathrin, and its cargo-receptor bridging is the step that is
   explicitly unestablished. ComplexPortal asserts GO:0140312 on CPX-5181 anyway; no
   subunit carries it, and I am not adding it.
3. **Autophagic lysosome reformation has no term.** QuickGO searches on "autolysosome",
   "autophagic lysosome", "reformation" and "membrane tubulation" return
   GO:0170064 lysosome fission, GO:0097749 membrane tubulation and the autolysosome CC
   terms, but nothing for ALR as a process. This is the process the 2025 structure paper
   places AP-5 upstream of.

## 11. Decisions

28 GOA rows. Summary of the actions taken in `AP5S1-ai-review.yaml`:

* **Locations** (lysosome ×3, late endosome ×4, cytosol ×3, lysosomal membrane,
  late endosome membrane): accept, with cytosol kept as non-core (the unrecruited pool)
  and the two SubCell membrane IEAs kept as non-core because they are ECO:0000305
  inferences from the same imaging.
* **Complex**: `GO:0044599` accept; the three `GO:0030119` rows — the IDA is MODIFY to
  the specific child, the IBA and IEA are accepted as correct-but-general parents.
* **Process**: `GO:0016197` endosomal transport accept (IBA, IEA, IMP);
  `GO:0016192` vesicle-mediated transport accept as the true parent; `GO:0007040`
  lysosome organization keep as non-core (complex-level NAS); `GO:0000724` HR repair
  keep as non-core for the IMP and mark the InterPro IEA as redundant.
* **`GO:0005515` ×5**: over-annotated as bare protein binding. Four of them (AP5Z1,
  AP5B1, SPG11, ZFYVE26) are within-complex partnerships already stated better by
  `GO:0044599`; the fifth (mouse Ap5z1) is the structural ζ/σ5 pair. None is upgraded to
  a binding-specificity MF, because "cargo adaptor activity" would be false; the
  architectural MF that *is* warranted is added as its own NEW row rather than by
  rewriting these.
* **NEW ×2**: `GO:0005198` structural molecule activity (IDA from the cryo-EM structure —
  no AP-5 subunit currently carries any MF beyond bare protein binding), and `GO:0034499`
  late endosome to Golgi transport, the pathway this complex is now assigned to, which no
  AP-5 subunit and neither SPG11 nor ZFYVE26 currently carries.
