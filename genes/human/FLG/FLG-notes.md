# FLG (human, UniProt P20930) — review notes

## Provenance note on deep research

Automated deep research could not be run for this gene: every configured provider
was unavailable in this environment on 2026-08-26.

- `falcon` (Edison): HTTP 402 — the `EDISON_API_KEY` is set but the account has no credits.
- `perplexity-lite` / `asta` / `consensus`: no API key present.
- `openai`: `OPENAI_API_KEY` present but rejected as `invalid_api_key`.
- `openscientist`: working; used for the focused molecular-function hypotheses below
  (`FLG-hypotheses/`).

Also note that the `deep-research-client` pin (`0.2.7rc1`) requires Python >=3.12 while
the repo venv is 3.11.15, so `just deep-research-*` fails at dependency resolution; the
runs here used `uvx --python 3.12`.

Per repository policy no self-authored file is named `*-deep-research-*.md`. Everything
below is my own literature work, with verbatim provenance.

## Gene / protein overview

Filaggrin is synthesised as **profilaggrin**, a ~400 kDa, heavily phosphorylated
polyprotein that is the major structural component of keratohyalin granules (KGs) in the
epidermal stratum granulosum. UniProt P20930 (4061 aa) is annotated with:

- two N-terminal EF-hand domains (residues 6–43 and 49–84) inside an S100-like "A domain";
- Ca(2+) `BINDING` sites at residues 62, 64, 66, 68 and 73 — i.e. **only in EF-hand 2**;
- 23 tandem `Filaggrin` `REPEAT` features (residues 258–3872), the whole region 255–3971
  flagged `Disordered` by MobiDB-lite. **These are not the filaggrin monomers.** Each is a
  49–56 aa Pfam PF03516 match (`DR Pfam; PF03516; Filaggrin; 23.`), and they occur in
  pairs: the two matches *within* a pair start 119 aa apart (116 for the first pair), and
  *consecutive pairs* start ~324 aa apart (observed 321–325, modal 324). That is two
  signature matches per ~324-residue filaggrin unit, so the 23 matches are 11 complete
  pairs plus an unpaired tail (`3821..3872`) — i.e. the ~11–12 units the literature
  describes, not 23 monomers;
- family assignment "Belongs to the S100-fused protein family" (PANTHER PTHR22571:SF51).

The domain architecture matters for MF curation: **the EF-hands and the filaggrin repeats
are on different proteolytic products.** Profilaggrin is cleaved during terminal
differentiation, releasing (a) the N-terminal S100/A+B fragment and (b) ~10–12 free
filaggrin monomers. They have different molecular functions and different locations.

## Molecular function

### 1. Intermediate-filament / keratin-filament binding (the aggregation activity)

This is the founding, directly-demonstrated activity, and it belongs to the **repeat
unit**, not the S100 domain.

[PMID:6170061 "We describe a class of cationic structural proteins that associate
specifically with intermediate filaments (IF) but not with other types of cytoskeletal
proteins."] and [PMID:6170061 "They interact in vitro with the IF several different types
of cells to form large fibers or macrofibrils in which many IF are highly aligned in
parallel arrays. Stoichiometric analyses suggest that two molecules of filaggrin bind to
each three-chain building block of the IF, possibly by ionic interactions with the
coiled-coil alpha-helical regions of the IF."]

Mechanism (the "ionic zipper"):
[PMID:7687298 "Filaggrins of mammalian epidermis represent archetypical examples of
intermediate filament-associated proteins that can bind large numbers of intermediate
filaments in vitro (and keratin filaments in vivo) into macrofibrils."] The binding is
via the filament **rod** domains, not the end domains:
[PMID:7687298 "However, the lysine-labeled rod domains of the filaments in macrofibrils
were considerably more constrained than in filaments alone."] and
[PMID:7687298 "These data support the hypothesis that filaggrins bind filaments by way of
simple ionic and/or H-bonding interactions between the conserved positive and negative
charges on the beta-turns of filaggrins and the conserved distributions of negative and
positive charges along the packed rod domains of intermediate filaments, as in an ionic
zipper."]

Two curation-relevant consequences:

- The *in vitro* activity is **intermediate filament binding** in general — the same paper
  reports binding of type III vimentin/desmin as well as type I/II keratin
  ([PMID:7687298 "were as effective as full length filaggrin in binding large numbers of
  both type I/II keratin and type III vimentin/desmin filaments, as judged by electron
  microscopy"]).
  *In vivo* the partner is keratin, so **GO:1990254 keratin filament binding** is the
  physiologically correct child term, with **GO:0019215 intermediate filament binding**
  as the demonstrated in-vitro superclass.
- Binding is **charge/β-turn-driven and sequence-degenerate**: a 20–26-residue synthetic
  peptide with ≥5 β-turns and net charge +2 was as effective as full-length filaggrin
  [PMID:7687298 "Of a series of synthetic peptides, those of 20 to 26 residues (about 2
  segments) containing at least five beta-turns with a net charge of +2 (that is, about
  40% of the turns are positively charged) were as effective as full length filaggrin"].
  This is a *binding* activity of a disordered polycation, not the behaviour of an
  architectural subunit with a defined fold.

Secondary literature states the activity the same way:
[PMID:19386895 "the approximately 400 kDa profilaggrin polyprotein is dephosphorylated and
rapidly cleaved by serine proteases to form monomeric filaggrin (37 kDa), which binds to
and condenses the keratin cytoskeleton and thereby contributes to the cell compaction
process that is required for squame biogenesis."]

### 2. Molecular condensate scaffold activity (keratohyalin granule assembly)

The modern mechanistic account of what KGs *are* and what filaggrin does to make them:

[PMID:32165560 "Here, we found that filaggrin assembles KGs through liquid-liquid phase
separation."] and [PMID:32165560 "The dynamics of phase separation governed terminal
differentiation and were disrupted by human skin barrier disease-associated mutations."]

Supporting detail from the same paper:

- [PMID:32165560 "Filaggrin and its less-studied (often less-abundant) paralogs are
  intrinsically disordered repeat proteins with a low-complexity (LC) sequence."]
- Repeat number sets the critical concentration — i.e. the tandem array is the functional
  unit: [PMID:32165560 "Over a wide range of expression levels, disease-associated
  mutations with ≤4 repeats exhibited a large increase (~130 to >1500 μM) in critical
  concentration required for phase separation"].
- The S100 domain contributes by dimerising: [PMID:32165560 "The S100 domain is known to
  dimerize (29), and when fused to filaggrin variants, it reduced the critical
  concentration for phase separation"], and [PMID:32165560 "Moreover, because the S100
  domain is cleaved during terminal differentiation, its function is likely to optimize
  phase separation at earlier stages when filaggrin amounts are low and KGs just begin to
  form."]
- Condensates and keratin bundles are reciprocally organising, which is the modern
  restatement of "filaggrin aggregates keratin": [PMID:32165560 "Our findings suggest a
  model whereby reciprocal density-dependent interactions between LC domains of terminal
  differentiation–specific keratins and KGs structure the cytoplasm to form an elaborate,
  interwoven network of stabilized liquid-like KGs and keratin filament bundles."]
- Dissolution is pH-triggered by the His-rich repeats at the granular→corneum transition:
  [PMID:32165560 "Thus, the pH shift appears to function specifically in altering the
  material properties of histidine-rich KGs, which in turn promote chromatin compaction,
  enucleation, and skin barrier establishment."]

**GO:0140693 molecular condensate scaffold activity** ("Binding and bringing together two
or more macromolecules in contact, permitting those molecules to organize as a molecular
condensate") is a precise fit and is not currently annotated to FLG.

### 3. Calcium ion binding — real, but only in the N-terminal S100 domain

Experimentally demonstrated, not merely inferred from the signature:
[PMID:8417356 "It contains two alpha-helical regions, termed EF-hands, that bind calcium
in vitro. This is the first example of functional calcium-binding domains fused to a
structural protein."]

Note that the 1992 gene paper that GOA/UniProt cite for the domain was explicitly
*speculative* about function — [PMID:1429717 "The presence of an S-100-like domain
suggests that profilaggrin binds calcium and that the calcium binding domain is
functionally significant"] — so PMID:8417356 (and the structure below) are the load-bearing
references, not PMID:1429717.

Structure confirms it, and also shows the EF-hands are not equivalent
([PMID:25760235], PDB 4PCW, 2.2 Å; full text PMC4466033):
each monomer "binds two calcium ions", one at "an N-terminal pseudo/S100 (non-canonical)
calcium binding loop" and one at a canonical C-terminal EF-hand. That matches UniProt,
which places Ca(2+) `BINDING` residues only at 62–73 (EF-hand 2).
[PMID:25760235 "The profilaggrin S100 domain formed a stable dimer, which contained two
hydrophobic pockets that provide a molecular interface for protein interactions."]

So GO:0005509 is correct, but it is a property of profilaggrin / the cleaved N-terminal
fragment, **not of mature filaggrin**, which contains no EF-hand.

### 4. Transition metal ion binding — not supported

GO:0046914 comes solely from InterPro2GO on IPR034325 (S-100 domain) via GO_REF:0000002.
Canonical S100 proteins bind Zn2+/Cu2+ at a *secondary* site at the dimer interface, but:

- the dedicated structural study of this exact domain reports only calcium — no zinc or
  other transition metal is discussed anywhere in [PMID:25760235] / PMC4466033;
- UniProt P20930 lists **no** transition-metal `BINDING` site, only the five Ca(2+) sites;
- no primary experiment demonstrating metal binding by FLG was found.

This is a signature-level over-propagation. (OpenScientist hypothesis run below tests it
independently.)

### 5. "protein binding" (GO:0005515, IPI with KLK5)

The interaction is enzyme–substrate, not a functional partnership of FLG:
[PMID:23629652 "we searched for profilaggrin-processing protease(s) by partial
purification of epidermal extracts and found KLK5 as a possible candidate"] and
[PMID:23629652 "KLK5 knockdown in normal cultured human epidermal keratinocytes resulted
in higher levels of profilaggrin, indicating that KLK5 potentially functions in
profilaggrin cleavage."] Per repo curation guidance, bare `protein binding` conveys no
functional information and should not stand as a core MF.

The N-terminal domain *does* have genuine, pocket-mediated protein partners
([PMID:25760235] — annexin II/p36, stratifin/14-3-3σ, HSP27), which would be the
informative thing to capture if anything.

### 6. Is "structural molecule activity" the right MF?

GO:0005198 is defined as "The action of a molecule that contributes to the structural
integrity of a complex"; GO:0030280 as "The action of a molecule that contributes to the
structural integrity of an epidermal cutaneous structure."

There are two distinct claims that must be kept apart:

- **The keratin-aggregation role is a binding activity, not a structural one.** Mature
  filaggrin is an intrinsically disordered polycation that transiently condenses
  pre-formed keratin filaments and is then completely proteolysed to free amino acids
  ([PMID:8417356 "Later, filaggrin itself is degraded to free amino acids that participate
  in maintenance of epidermal flexibility."]). It does not persist as an architectural
  subunit of the structure it organises.
- **The cornified-envelope role genuinely is structural.** Filaggrin is covalently
  isodipeptide cross-linked into the CE: [PMID:7543090 "In addition, cross-links involving
  loricrin and keratins 1, 2e, and 10 or filaggrin were recovered in both levels. The data
  establish for the first time that these several proteins are indeed cross-linked protein
  components of the CE structure."] That is the fact behind the IDA to GO:0030280, and it
  survives review — GO:0030280 (the specific epidermal child) is the better term than the
  bare GO:0005198 IEA.

### 7. Terminal catabolism to natural moisturising factor

Not an MF of FLG itself (FLG is the substrate) but essential context for why the barrier
phenotype exists:
[PMID:21654840 "In wild-type stratum corneum, FLG is degraded into free amino acids, some
of which contribute to generation of the natural moisturizing factors (NMFs) that maintain
epidermal hydration."] and [PMID:21654840 "we show that the defective FLG degradation in
caspase-14-deficient skin results in substantial reduction in the amount of NMFs, such as
urocanic acid and pyrrolidone carboxylic acid."] Deiminated (citrullinated) filaggrin is
broken down by bleomycin hydrolase [PMID:19286660]; FLG is citrullinated in vivo
[PMID:8780679].

## Localisation

- **Keratohyalin granule (GO:0036457)** — the defining location of profilaggrin.
  [PMID:1429717 "It is synthesized as a large precursor protein, profilaggrin, that
  consists of multiple filaggrin units and is localized in keratohyalin granules."]
  UniProt: "In the stratum granulosum of the epidermis, localized within keratohyalin
  granules (PubMed:1429717)."
- **Cornified envelope (GO:0001533)** — covalently cross-linked component [PMID:7543090].
- **Nucleus (GO:0005634)** — genuine, but for the *cleaved N-terminal domain in
  keratinocytes*, and **not** established by the sperm-nuclear-proteome dataset GOA cites.
  [PMID:9800950 "Antibodies specific for the amino-terminal domains of profilaggrin showed
  localization in keratohyalin granules in the granular cells, but stained the nucleus in
  transition cells."] The NLS is functional:
  [PMID:12230510 "The nuclear localization signals in human and mouse profilaggrin were
  shown to be functional by transfection of epithelial cells and depended on the absence
  of filaggrin sequences."]
- **HPA "cytoplasmic bodies" → GO:0036464** is a mapping artefact. HPA reports FLG
  localised to *cytoplasmic bodies* in **HaCaT keratinocytes** (Enhanced reliability,
  antibodies HPA027505/HPA030188). In HaCaTs those FLG-positive cytoplasmic puncta are
  KG-like condensates — this is the exact cell line and structure characterised in
  [PMID:32165560] — not ribonucleoprotein granules. GO:0036464 requires RNP content;
  filaggrin has no RNA-binding function. The correct term is GO:0036457.
- **Extracellular matrix (GO:0031012)** from a multiple-myeloma **bone-marrow** ECM
  proteome [PMID:28344315] is not credible for a 4061-aa intracellular epidermal protein;
  keratin/skin-derived contamination is the standard confounder in such datasets.

## Phylogenetic context (the IBAs)

The three IBAs (GO:0001533, GO:0036457, GO:0061436) come from PAINT node
PANTHER:PTN002503122 in PTHR22571 ("S100-fused Epidermal Structural Protein"). Donors
resolve to the S100-fused-type protein (SFTP) clade: human FLG (P20930, the target
itself), human HRNR/hornerin (Q86YZ3), human FLG2 (Q5D862), mouse *Hrnr* (MGI:3046938)
and mouse *Flg2* (MGI:3645678). This is a coherent, tight clade with shared
architecture (S100 A-domain + tandem LC repeats) and shared epidermal-barrier biology, and
FLG appearing in its own `WITH/FROM` is the expected marker that experimental grounding
exists on the target. All three IBAs are consistent with the direct evidence above.

## OpenScientist hypothesis runs

Three focused MF hypotheses were dispatched (see `FLG-hypotheses/`):

1. `function-hypothesis-go-0005509` — does the N-terminal S100 domain really bind Ca2+,
   and is EF-hand 1 a degenerate pseudo-EF-hand?
   **Verdict: SUPPORTED.** Convergent structural, biochemical, sequence and evolutionary
   evidence; EF-hand 2 (62–73) is a textbook canonical loop with the hallmark bidentate
   Glu73, EF-hand 1 is the S100-type pseudo-EF-hand. Recommends retain + upgrade IEA→IDA
   on PMID:25760235, with a scope note that this is the N-terminal domain's property, not
   the repeat's. Surfaced [PMID:32893105], which shows the A+B domains bind annexin II and
   keratin IFs calcium-dependently — now cited in the review.
2. `mf-keratin-binding-vs-structural` — is the mature repeat unit's MF keratin-filament
   binding rather than `structural molecule activity`?
   **Verdict: SUPPORTED, with a qualifier.** Independent sequence biophysics found every
   repeat region intrinsically disordered (Uversky charge–hydropathy, Chou–Fasman below
   average for *both* helix and sheet, TOP-IDP disorder fraction 0.92–0.98), strongly
   hydrophilic, and cationic only at acidic skin pH. Recommends GO:0019215/GO:1990254 as
   the primary MF and reframing GO:0030280 as a distinct, secondary, cornified-envelope
   role — which is exactly how this review wires it. Surfaced [PMID:6195345], the direct
   in vitro demonstration of keratin bundling, now cited.
3. `function-hypothesis-go-0046914` — is the InterPro2GO transition-metal-binding call
   warranted for this protein?
   **Verdict: over-annotated / refuted as a direct function.** A HETATM audit of 4PCW
   finds 8 calcium atoms and zero transition-metal atoms; residues 1–91 contain only two
   histidines (His60, His65) and no cysteines, lacking the His3Asp/His4–6 or Cys-cluster
   chemistry that characterised metal-binding S100 proteins use, and those histidines sit
   8–15 Å from any calcium site. A comparative audit shows all six human SFTPs (FLG, FLG2,
   HRNR, RPTN, TCHH, CRNN) carry GO:0046914 as IEA:InterPro with no member-specific
   evidence, while genuinely Zn-binding S100s (S100A7/A8/A9/B) carry the specific child
   GO:0008270 with experimental evidence. Caveat recorded in the review: no direct
   Zn/Cu binding assay has been done on this domain, so the case is structural, sequence
   and comparative rather than a direct negative experiment.

All three runs were launched blind to this notes file and agreed with the independent
reading above; where they diverged from my initial framing it was to sharpen it (the
GO:0030280 "secondary structural role" split), not to overturn it.

Operational note for the skill: `--as-function-hypothesis` **silently discards
`--context`** (`build_function_hypothesis_record` in
`scripts/gene_hypothesis_deep_research.py` rebuilds `term_context` from the annotation
alone). To pass scoping context, use a free-text `--hypothesis` with `--focus-type
function-support`, which does honour `--context`.
