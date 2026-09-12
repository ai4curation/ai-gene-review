# AP1S1 (sigma1A) — review notes

UniProt P61966, 158 aa, `AP1S1_HUMAN`. Accession asserted against the fetched record:
`ID   AP1S1_HUMAN             Reviewed;         158 AA.` / `AC   P61966;` — this is the
expected protein, not a merged accession returning something else. PANTHER family
PTHR11753 (ADAPTOR COMPLEXES SMALL SUBUNIT FAMILY), the family shared with AP1S2,
AP1S3, AP2S1, AP3S1, AP3S2, AP4S1.

GOA seeded 53 rows: one IBA, no IDA/IMP/IPI on the human gene at all, and a large
block of Reactome TAS and ComplexPortal NAS rows. The whole experimental base for
human AP1S1 in GOA is thin; almost everything interesting about this protein is in
papers GOA has not used.

## 1. What the protein is

sigma1A is the small subunit of AP-1, the clathrin adaptor that works at the TGN and
endosomes. The GO definition of GO:0030121 names it explicitly, which settles the
complex-membership annotations without argument: "A heterotetrameric AP-type membrane
coat adaptor complex that consists of beta1, gamma, mu1 and sigma1 subunits ... In at
least humans, the AP-1 complex can be heterogeneric due to the existence of multiple
subunit isoforms encoded by different genes (gamma1 and gamma2, mu1A and mu1B, and
sigma1A, sigma1B and sigma1C)."

UniProt's own FUNCTION is subunit-level and cautious: "Subunit of clathrin-associated
adaptor protein complex 1 that plays a role in protein sorting in the late-Golgi/trans-Golgi
network (TGN) and/or endosomes." Localisation is `Golgi apparatus`, `Cytoplasmic vesicle
membrane; Peripheral membrane protein; Cytoplasmic side` and `Membrane, clathrin-coated
pit`, all `ECO:0000269|PubMed:9733768`.

The three sigma1 paralogs are not interchangeable in expression but are in biochemistry:
[PMID:20203623 "The ubiquitously expressed AP-1-sigma1A complex mediates protein sorting
between the trans-Golgi network and early endosomes."] and [PMID:27411398 "Tissues express
σ1A and one of the σ1B and σ1C isoforms."]. sigma1A is the ubiquitous one; sigma1B is the
neuron-enriched one whose loss causes X-linked intellectual disability.

There is a solved structure containing this exact protein: PDB 4P6Z, 3.0 A, with
`S=1-158` mapped to P61966 in the UniProt cross-references — the AP-1 core bound to
HIV-1 Vpu and BST2 [PMID:24843023]. This matters below.

## 2. The molecular function: sigma1A is half of the dileucine cargo-signal site

This is the substantive finding of the review and it is entirely absent from GOA.

Cargo sorting signals come in two flavours and they bind different parts of AP-1.
Tyrosine-based YXXØ motifs bind mu1. Dileucine-based `[DE]XXXL[LI]` motifs bind
**neither subunit alone** — they bind the gamma-sigma1 hemicomplex:

- [PMID:14691137 "We have used a yeast three-hybrid assay to demonstrate that
  [DE]XXXL[LI]-type signals from the human immunodeficiency virus negative factor protein
  and the lysosomal integral membrane protein II interact with combinations of the gamma
  and sigma1 subunits of AP-1 and the delta and sigma3 subunits of AP-3, but not the
  analogous combinations of AP-2 and AP-4 subunits."]
- [PMID:17360967 "the gamma/sigma1 or alpha/sigma2 hemicomplexes bound the dileucine-based
  motifs of several proteins quite strongly, whereas binding by the beta1/mu1 and beta2/mu2
  hemicomplexes, and the individual beta or mu subunits, was extremely weak or undetectable."]
- [PMID:21097499 "(D/E) XXX L(L/I) signals, on the other hand, do not bind to any single AP
  subunit but to combinations of γ-σ1, α-σ2, and δ-σ3 subunits, as demonstrated by the use
  of yeast three-hybrid (Y3H) and in vitro binding assays"]

The "not any single subunit" clause is exactly what the `contributes_to` qualifier is for,
and it is why the core function below uses `contributes_to_molecular_function` rather than
`molecular_function`.

Crucially the evidence is on **sigma1A specifically**, not on AP-1 generically — which is
the distinction the review is supposed to draw:

- Point mutants of sigma1A itself kill the binding: [PMID:21097499 "This is evidenced by
  the loss of signal binding by the σ2 V88D or L103S substitutions and the homologous σ1A
  V88D and I103S and σ3A V94D and L109S substitutions."]
- Mismatched hemicomplexes do not bind: [PMID:39269494 "These experiments showed that
  σ1AWT, in combination with γ1 but not with the homologous AP-2 αC and AP-3 δ subunits,
  interacted with the cytosolic tail of LIMP-II and tyrosinase"].
- The structure puts the cargo mimic on sigma1 directly: [PMID:24843023 "E62 forms a salt
  bridge with R15 of AP1 γ subunit, fulfilling the role of the 'acidic residue' within the
  sorting motif, while L66 and V67 embed into the hydrophobic pocket on AP1 σ1 that
  accommodates the canonical dileucine residues"]. That is the 4P6Z structure, whose
  chain S is this protein.

All three sigma1 paralogs bind these signals — [PMID:21097499 "we show that the AP-1
γ1-σ1A, γ1-σ1B, and γ1-σ1C hemicomplexes recognize all (D/E) XXX L(L/I) signals tested,
whereas γ2-σ1A and γ2-σ1B have a more restricted specificity."] — so this is a shared
sigma1 function, not an AP1S1-private one. It is still a function of AP1S1.

**There is no GO term for it.** GO has GO:0089710 `endocytic targeting sequence binding`
for the tyrosine-based motif ("a specific peptide sequence, of 4-6 amino acids with an
essential tyrosine (Y) ... which directs internalization by clathrin-coated pits") but no
counterpart for the dileucine motif. Searched QuickGO for "dileucine" (zero hits),
"sorting signal binding", "targeting sequence binding", "leucine motif binding" and the
MF children of GO:0140312 `cargo adaptor activity` (only GO:0035615). Hence a
`proposed_new_terms` entry, and an ONTOLOGY knowledge gap. This is a real gap, not an
artefact of one empty search.

## 3. Bioinformatics: the site is retained, but retention is not the evidence

`AP1S1-bioinformatics/` (`uv run python dileucine_site.py`) fetches nine sigma subunits
live from UniProt, asserts their lengths, and maps the structurally defined sigma2 pocket
onto each by pairwise alignment. Results in
`file:human/AP1S1/AP1S1-bioinformatics/RESULTS.md`.

Two useful outcomes and one deliberately unflattering one:

1. All five literature-named sigma1A positions verify against the live P61966 sequence:
   R15, A63, V88, I103, and L90 (the MEDNIK variant position).
2. The alignment independently reproduces every homology the paper asserts
   (sigma2 88 -> sigma1A 88, sigma2 103 -> sigma1A 103, sigma2 88 -> sigma3A 94,
   sigma2 103 -> sigma3A 109). The mapping method is therefore sound.
3. **The negative control defeats the conservation argument.** sigma4 (AP4S1, Q9Y587) is
   in the same PANTHER family and the epsilon-sigma4 hemicomplex demonstrably does *not*
   bind these signals [PMID:14691137, PMID:21097499], yet it scores 4/5 identical at the
   pocket — the same score as sigma1A, sigma1B and sigma1C.

So "AP1S1 retains the dileucine pocket" is true but carries no weight on its own. The
claim rests on direct sigma1A mutagenesis and on the sigma1-containing structure. I have
recorded the residues as `RETAINED`/`SUBSTITUTED` residue_claims anyway, because that is
the checkable form, but the propagation reasoning is not residue-based and says so.

This is worth stating plainly because the mirror error — inferring function from a
retained fold — is as common as inferring loss from a missing residue, and this family
is a case where the fold genuinely does not predict the function.

## 4. The IBA: one row, a deep pan-AP-sigma node, and the right LCA term

The single IBA is GO:0016192 `vesicle-mediated transport`, `GO_REF:0000033`,
WITH/FROM listing 11 donors plus `PANTHER:PTN000204281`.

I fetched the family PAINT slice (`interpro/panther/PTHR11753/PTHR11753-paint.tsv`,
already present). PTN000204281 carries two IBD assertions:

| node | term | aspect | seeds |
|---|---|---|---|
| PTN000204281 | GO:0043231 intracellular membrane-bounded organelle | C | 13 seeds incl. `UniProtKB:P61966` (AP1S1 itself) |
| PTN000204281 | GO:0016192 vesicle-mediated transport | P | 10 seeds |

Note AP1S1's own accession seeds the GO:0043231 IBD but **not** the GO:0016192 one, so
this is not a self-referential IBA and there is no question of redundancy either way.
(GO:0043231 does not appear as an IBA row in AP1S1's GOA, so there is nothing to review
for it.)

Every donor resolved (UniProt xref search, plus the GO API for the worm gene):

| WITH/FROM | resolves to | subunit |
|---|---|---|
| CGD:CAL0000182525 | Q59QC5 *C. albicans* APS3 | AP-3 sigma |
| FB:FBgn0039132 | *D. melanogaster* AP-1sigma | AP-1 sigma |
| FB:FBgn0043012 | *D. melanogaster* AP-2sigma | AP-2 sigma |
| MGI:MGI:1098244 | P61967 mouse Ap1s1 | AP-1 sigma1A |
| MGI:MGI:1889383 | Q9DB50 mouse Ap1s2 | AP-1 sigma1B |
| PomBase:SPAP27G11.06c | Q9P7N2 pombe vas2 | AP-1 sigma1 |
| RGD:620188 | P62744 rat Ap2s1 | AP-2 sigma |
| SGD:S000003561 | P47064 yeast APS3 | AP-3 sigma |
| SGD:S000004160 | P35181 yeast APS1 | AP-1 sigma1 |
| UniProtKB:P53680 | human AP2S1 | AP-2 sigma |
| WB:WBGene00000157 | *C. elegans* aps-2 (F02E8.3, Q19123) | AP-2 sigma |

That is 11 gene-level donors spanning AP-1, AP-2 and AP-3 sigma subunits across fungi,
nematode, fly, rodent and human. The node is the deep pan-AP-sigma ancestor, not an AP-1
node.

**This makes GO:0016192 the correct term, not a granularity failure.** The tempting
review is "vesicle-mediated transport is vague; AP-1 does TGN-to-endosome sorting, so
MODIFY to something specific". That would be wrong. `GRANULARITY_MISMATCH` applies only
when the donors agree and a more specific term was available. Here the donors do not
agree on a pathway: AP-1 sigmas work at the TGN/endosome, AP-2 sigmas in endocytosis at
the plasma membrane, AP-3 sigmas in lysosome/LRO delivery. `vesicle-mediated transport`
is precisely their least common ancestor, and placing a compartment-specific term at that
node would over-propagate it to the AP-2 and AP-3 members. Verdict: `NO_FAILURE_CORE`.

Supporting detail: the mouse 1:1 ortholog Ap1s1 is itself among the donors, and the term
is genuinely core for AP1S1 (it is what the protein does). I checked the donors' own GO
records via QuickGO; each carries the same IBA plus independent grounding
(e.g. yeast APS1 GO:0006896 IMP PMID:17003107, *C. albicans* APS3 GO:0006896 IMP
PMID:20870878, pombe vas2 GO:0042147 and GO:0099638 IDA PMID:19624755).

## 5. The Ensembl Compara rows, and a trap I did not fall into

Two rows come from `GO_REF:0000107` with `supporting_entities: UniProtKB:P61967` +
`ensembl:ENSMUSP00000106709`: GO:0043195 `terminal bouton` and GO:0098793 `presynapse`.

**P61967 is mouse Ap1s1, not AP1S2.** I checked (`AP1S1_MOUSE`, gene `Ap1s1`,
*Mus musculus*, Swiss-Prot) rather than assuming the "sigma" donor of a synaptic
annotation must be the neuronal paralog. So these are 1:1 ortholog transfers, the
cleanest kind.

QuickGO shows the mouse source rows are `IDA` from **PMID:20203623**, which is titled
"AP-1/sigma1B-adaptin mediates endosomal synaptic vesicle recycling, learning and
memory" — a sigma1B paper. The tempting move is to call this a paralog mix-up and
REMOVE. That would be the exact error CLAUDE.md warns about: the cached record is
abstract-only (`full_text_available: false`), MGI curators read the full text, and the
paper self-evidently assays both isoforms since its own abstract contrasts them
("The ubiquitously expressed AP-1-sigma1A complex mediates protein sorting between the
trans-Golgi network and early endosomes"). Deferring to the curator. Graded
`KEEP_AS_NON_CORE` — real, but a neuronal-context localisation, not the core function of
a ubiquitously expressed adaptor subunit.

## 6. The one annotation that is actually wrong: receptor-mediated endocytosis

GO:0006898 `receptor-mediated endocytosis`, TAS, PMID:9733768.

The term definition is unambiguous about compartment: "A specific receptor on the cell
surface binds tightly to the extracellular macromolecule (the ligand) that it recognizes;
the plasma-membrane region containing the receptor-ligand complex then undergoes
endocytosis". This is a plasma-membrane process, and AP-1 is not a plasma-membrane
adaptor — AP-2 is. AP-1 recruitment is Arf1-GTP- and PI4P-dependent at the TGN
[PMID:15377783 "TGN localization of AP-1 depends on the small GTPase, Arf1, and the
phosphoinositide, PI-4-P."] and [PMID:23415225 "AP-1 is a clathrin adaptor complex that
sorts cargo between the trans-Golgi network and endosomes. AP-1 recruitment to these
compartments requires Arf1-GTP."]. The current statement of AP-1's scope is the same
[PMID:39269494 "AP-1 is a clathrin-associated complex that mediates sorting of
transmembrane proteins between the trans-Golgi network (TGN) and endosomes in all cells,
as well as polarized sorting to the basolateral surface of epithelial cells and the
somatodendritic domain of neurons"].

And the cited paper contains no endocytosis experiment: it is a gamma2-adaptin
identification paper whose sigma1A content is a yeast two-hybrid interaction and whose
localisation result is paranuclear/Golgi. TAS is a traceable author statement, not an
experimental annotation, so the CLAUDE.md protection for IDA/IMP/IPI curator judgment
does not apply, and the argument here is positive and biological rather than
"the abstract is about another gene". REMOVE.

Note the contrast with GO:0005905 `clathrin-coated pit`, which looks like the same error
and is not. Its definition explicitly extends past the plasma membrane: "Coated pits form
on the plasma membrane, where they are involved in receptor-mediated selective transport
of many proteins and other macromolecules across the cell membrane, **in the trans-Golgi
network, and on some endosomes**." Decided from the definition, not the label: ACCEPT.

## 7. Disease and cargo biology

MEDNIK / IDEDNIK syndrome (MIM 609313), autosomal recessive. Originally a founder splice
mutation [PMID:19057675 "Here, we describe the first mutation in the human AP1S1 gene,
encoding the small subunit sigma1A of the AP-1 complex. This founder splice mutation,
which leads to a premature stop codon, was found in four families"], with zebrafish
knockdown rescued by WT but not truncated human AP1S1 mRNA — a clean loss-of-function
demonstration in vivo, in both perturbation directions.

The 2024 paper is the mechanistically decisive one and reframes the disease: the L90P
missense allele, previously thought to cause a distinct non-syndromic enteropathy, causes
full MEDNIK, and it does so by failing at exactly the two sigma1A jobs identified above
[PMID:39269494 "The σ1A L90P variant is largely unable to assemble into the AP-1
complex."] and [PMID:39269494 "Importantly, we observed that the L90P substitution
completely abolished the interaction of the γ1-σ1A hemicomplex with the LIMP-II and
tyrosinase tails in the Y3H assay"]. It also shows sigma1A is required to get AP-1 onto
membranes at all: [PMID:39269494 "Expression of myc-tagged σ1AWT rescued TGN/endosomal γ1
staining, whereas expression of myc-tagged σ1AL90P did not"] in triple sigma1-KO cells.

Cargo: copper pumps ATP7A/ATP7B [PMID:24754424], tight-junction ZO-1 and claudin-3 in
intestinal epithelium [PMID:32306098], EGFR recycling versus lysosomal degradation
[PMID:37659097]. Tyrosinase is a directly demonstrated gamma1-sigma1A dileucine cargo
[PMID:21097499, PMID:39269494], which is the mechanistic link that makes the
ComplexPortal NAS `melanosome assembly` row defensible rather than a bare complex-level
projection.

sigma1A also has a non-coat role in endosome maturation, but the evidence is mouse
synaptosomes: [PMID:27411398 "AP-1/σ1A-ArfGAP1-Rabex-5 complex formation leads to more
endosomal Rabex-5 and enhanced, Rab5(GTP)-stimulated Vps34 PI3-kinase activity"]. Note a
nuance affinage flattened: Rabex-5 binds sigma1B, not sigma1A, directly — "Unexpectedly,
Rabex-5 binds σ1B, not σ1A" — the sigma1A link is indirect via ArfGAP1. Because this is
mouse-only I have not created a human NEW row for it; it is a knowledge gap instead.

## 8. Affinage record

Trust gate tripped: `self_evaluation_pairwise: tie` (not `win`), flagged in
`.affinage.log`. Marked `LOW_QUALITY` in `reference_review` and every claim I used from
it was re-verified against its PMID. On re-checking, the narrative is substantially
accurate — it found PMID:39269494, PMID:19057675, PMID:32306098, PMID:27411398 and
PMID:37659097, which is a good haul. Two imprecisions: it reports PMID:2040623 as though
the cDNA were human, when that paper sequenced **rat** AP17 and **mouse** AP19; and it
compresses the ArfGAP1/Rabex-5 result as though sigma1A bound Rabex-5, which the paper
explicitly denies. Citation list is all numeric PMIDs, no bioRxiv ids.

**What affinage missed** — and it is the whole molecular-function story: the entire
dileucine literature. PMID:14691137, PMID:17360967 and PMID:21097499 are the three papers
that establish what sigma1A actually *does*, and none appear in its citation list. Nor
does the structure containing this protein (PMID:24843023 / PDB 4P6Z), nor the AP-1 core
structure (PMID:15377783), nor the Arf1 activation mechanism (PMID:23415225). This is the
documented failure mode exactly: the decisive papers are titled for the complex, the
partner subunit, or a virus, never for AP1S1. Found by searching Europe PMC on
"dileucine signal AP-1 gamma sigma1 hemicomplex" and by resolving PDB 4P6Z through the
RCSB API rather than by searching the gene symbol.

## 9. Annotation dispositions

- AP-1 complex membership (GO:0030121 x4): ACCEPT. The GO term definition names sigma1A.
- TGN membrane / Golgi membrane / Golgi / cytoplasmic vesicle membrane / clathrin-coated
  pit: ACCEPT — this is where AP-1 works and where sigma1A is required to put it.
- cytosol (Reactome x9): KEEP_AS_NON_CORE. True of the unassembled/uncoated pool; the
  Reactome rows are steps of coat assembly/disassembly cycles, so the cytosolic state is
  half of a real cycle rather than a functional location.
- lysosomal membrane, early endosome: KEEP_AS_NON_CORE — endpoints of AP-1 routes.
- vesicle-mediated transport / protein transport / intracellular protein transport:
  ACCEPT; these are correct and the IBA one is at the right node.
- membrane (HDA): KEEP_AS_NON_CORE, root-ish and the assay cannot say which membrane.
- response to virus (IEP): MARK_AS_OVER_ANNOTATED. One microarray in one cell line,
  AP1S1 not named in the abstract, no functional follow-up.
- receptor-mediated endocytosis: REMOVE (section 6).
- melanosome assembly, platelet dense granule organization, basolateral protein
  secretion: KEEP_AS_NON_CORE — cell-type-restricted, complex-level, NAS.
- terminal bouton, presynapse: KEEP_AS_NON_CORE (section 5).
- clathrin-cargo adaptor activity: ACCEPT, but see the definition caveat — GO:0035615 is
  defined as "responsible for the formation of endocytic vesicles", which does not
  describe AP-1. Raised as a suggested question rather than acted on, since GO_Central
  itself applies this term to AP-1 sigma subunits (pombe vas2 carries it as IC
  `contributes_to` GO:0030121).
- NEW: one row, GO:0005198 `structural molecule activity`, IMP, PMID:39269494. GOA gives
  this gene exactly one MF term and it is complex-level and IEA-derived; the subunit's own
  contribution -- holding AP-1 together -- is demonstrated in human cells in both
  directions (wild-type sigma1A co-IPs with gamma1, restores gamma1 levels and restores
  gamma1 membrane staining in triple-sigma1-KO cells; L90P does none of these, dropping
  gamma1 co-IP to 0-13%) and is annotated nowhere. Coded IMP, not IDA, because the readouts
  come from transfected constructs in a knockout background. The *more* interesting
  subunit-level MF -- dileucine sorting-signal binding -- gets no NEW row because no GO term
  exists for it; that is the `proposed_new_terms` entry and the ONTOLOGY knowledge gap
  attached to the first core function.

## 10. Final counts (all scripted, none asserted from memory)

- 53 GOA rows, 53 seeded review rows, reconciled one-to-one on
  (GO id, evidence code, reference, normalized WITH/FROM) by `.scratch/reconcile.py`.
- Actions: ACCEPT 32, KEEP_AS_NON_CORE 19, REMOVE 1, MARK_AS_OVER_ANNOTATED 1, NEW 1 (54 total).
- 13 rows carry WITH/FROM; all 13 have `supporting_entities` and all 13 have a
  `propagation_review`, whose 27 `source_entities` are generated from those lists rather
  than typed, so they cannot drift.
- 53 references, every one with a `reference_review`. 175 `supporting_text` quotes, all
  verbatim per `checkquotes.py`.
- 4 residue claims, all resolving against the live sequences.
