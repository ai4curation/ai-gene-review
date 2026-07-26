# ACTL7A (Q9Y615) — review notes

Reviewer working notes for the PAINT + affinage round. Provenance is inline; every quoted
string is verbatim from the cited source.

## 1. What the gene is

ACTL7A ("actin-like protein 7A"; also **Arp7A**, **T-actin 2**, **Tact2**) belongs to a small set
of largely testis-restricted actin-related proteins, though ACTL7A itself is the least restricted
of them: HPA calls it "Tissue enriched (testis)" rather than testis-specific, and the original
human survey detected its message broadly — [PMID:10373328 "ACTL7A is expressed in a wide variety
of adult tissues, while the ACTL7B message was detected only in the testis and, to a lesser
extent, in the prostate."]. Mouse work states the opposite for the ortholog
[PMID:21278383 "Molecular analysis in mice indicates that Arp7A is only expressed in testis (18,
19)."], so the breadth of ACTL7A expression is not settled; every *functional* observation is in
germ cells. It is 435 aa, intronless, and sits head-to-head with its paralogue ACTL7B on
chromosome 9q31 [PMID:10373328 "Genomic analysis revealed ACTL7A and ACTL7B to be intronless genes
contained on a common 8-kb HindIII fragment in a "head-to-head" orientation."].

Its distinguishing architectural feature is a **64–65 residue N-terminal extension** in front of
the actin fold, which UniProt records as disordered (`REGION 1..64 /note="Disordered"`) and which
Pfam models separately as `PF16840 ACTL7A_N`. The actin fold itself is unusually intact for an
Arp: [PMID:21278383 "the sequence of Arp7A has no major deletions or insertions within its
predicted actin fold and has 43% sequence identity to β-actin, which is higher than that of
Arp3"].

Note the naming trap that this review had to resolve: **the family is a mixture.** The PANTHER
family that ACTL7A belongs to (`PTHR11937 ACTIN`) also contains the *nuclear* Arps that are
subunits of chromatin-remodelling complexes: [PMID:21278383 "a number of evolutionarily conserved
Arps (Arp4, -5, -6, and -8) have no apparent association with the cytoskeleton but are in fact
found in the nucleus as components of chromatin-remodeling complexes"]. Several of ACTL7A's
IBA WITH/FROM sources are exactly those proteins (see §4).

## 2. Where it acts — acroplaxome, not acrosome

The single most consequential localisation fact for curation is that ACTL7A sits in the
**subacrosomal layer (acroplaxome)**, i.e. *between* the acrosome and the nuclear envelope, and
that this was an explicit correction of the earlier "nucleus"/"acrosome" reading:

[PMID:21278383 "Previous observations have shown that Arp7A is expressed in testis and is
associated with the nucleus of spermatids (18, 19). We have now extended these earlier studies
and shown that Arp7A is actually localized in the subacrosomal layer, which is also known as the
acroplaxome (40)."]

GO's `GO:0033011 perinuclear theca` definition already covers this region — "It shows two distinct
regions, a subacrosomal layer and, continuing caudally beyond the acrosomic system, the
postacrosomal sheath" — so GO:0033011 is the correct, if coarse, term. GO has **no** term for
the acroplaxome (OLS/QuickGO searches for "acroplaxome" and "subacrosomal" return nothing; the
only child of GO:0033011 is `GO:0033150 cytoskeletal calyx`, which is the *postacrosomal* part).
That asymmetry is the ontology gap proposed in this review.

Other locations, all real but secondary:

- **Golgi apparatus**, transiently during acrosome biogenesis: [PMID:21278383 "Closer examination
  of the testis sections reveals that that Arp7A is also associated with an additional structure,
  which was identified as the Golgi apparatus based on its labeling with the Golgi-specific
  protein GM130 (Fig. 2B). Arp7A is associated with the Golgi apparatus prior to and throughout
  the biogenesis of the acrosome"].
- **Nucleus** of germ cells. Originally reported for mouse T-ACTIN-2 [PMID:12672658 "Although the
  cellular locations of these two proteins are quite different (T-ACTIN-1 was found in the
  cytoplasm and T-ACTIN-2 was located in the nucleus)"], and confirmed by 3D confocal imaging in
  the knock-out study [PMID:36734600 "Our intracellular localization data show ACTL7A to be
  dynamically present within the nucleus and subacrosomal space and later associated with
  postacrosomal regions of developing spermatids."]. Human evidence is a sperm-nucleus proteome
  [PMID:21630459] — worth noting that those preparations were made to exclude the acrosome
  ("sperm nuclei were obtained through CTAB treatment and isolated to over 99.9% purity without
  any tail fragments, acrosome or mitochondria") but the perinuclear theca is nuclear-adherent by
  construction, so PT carry-over cannot be excluded from a nuclear proteome alone. The mouse IF
  data are what make the nuclear pool credible. No nuclear *function* has been demonstrated.

## 3. What it does — and the crucial thing it does not do

Mouse knock-out is the decisive experiment: [PMID:36734600 "Significantly, we found a complete
loss of subacrosomal filamentous actin (F-actin) structures in knock-out spermatids suggesting a
regulatory role for subacrosomal F-actin."] and, importantly, the effect is *local*:
[PMID:36734600 "The KO spermatids did not lose F-actin in other cellular regions, indicating that
ACTL7A is not globally required for F-actin formation within developing spermatids and emphasizing
that ACTL7A is a hyperspecialized ARP, required for F-actin formation, regulation, and/or
stability in the subacrosomal space."]

Whether ACTL7A is itself the filament is explicitly **open**: [PMID:36734600 "As such, it is not
yet clear whether ACTL7A may be the filament-forming actin in the acroplaxome, or whether its role
is to nucleate, stabilize formation, and/or anchor F-actin formed by conventional ARPs to the
nuclear surface."] The 2011 paper closes with the same open question: [PMID:21278383 "Future
studies will be required to establish the role of the Arp7A·Tes·Mena complex in the formation and
function of the acroplaxome and whether it binds to and/or induces actin filament
polymerization."]

And there is a direct, if unillustrated, cell-biological negative on self-polymerisation:
[PMID:21278383 "In contrast, when expressed in HeLa cells, GFP-Arp7A is cytoplasmic and does not
assemble into filaments or co-localize with and/or affect the localization of Tes and Mena at
focal adhesions (data not shown)."]

Partners (all in the perinuclear theca / acroplaxome orbit):

- **TES (testin)** — direct, structurally defined. UniProt: `Interacts (via N-terminus) with TES
  (via LIM domain 2).` The crystal structure `2XQN` is of ACTL7A 1–65 bound to TES LIM2-3 with the
  ENAH EVH1 domain [PMID:21278383 "residues 28-49 of Arp7A contact the LIM2-3 domains of Tes"],
  and single alanine-to-tyrosine substitutions in ACTL7A abolish it (`MUTAGEN 31 A->Y: Abolishes
  interaction with TES.`; same for residue 41). This is a **LIM-domain-binding** activity, not
  generic protein binding.
- **ACTL9** [PMID:33626338], **CYLC1/cylicin-1** [PMID:38573307], both PT proteins whose own loss
  causes PT/acrosome-attachment defects.
- **ZPBP, ARP2, MYO6, PFN4, ACTN1, DCTN1** by co-IP from the KO study; ACTRT2 was tested and was
  *negative* [PMID:36734600 "Surprisingly, ACTL7A interaction with ACTRT2 was not detectable by
  Co-IP"].
- **FNDC8** and **CCIN**, in mouse PT [PMID:41169243 "ACTL7A, another essential PT protein, is
  required for acrosome biogenesis and mediates the tethering of the acrosomal outer membrane to
  the nucleus."].

## 4. WITH/FROM resolution and source evidence (the high-yield check)

Every WITH/FROM token in `ACTL7A-goa.tsv`, resolved, with what QuickGO says the source itself
carries for the propagated term.

| row | term | WITH/FROM token | resolves to | source's own evidence for the term |
|---|---|---|---|---|
| IBA | GO:0005634 nucleus | `CGD:CAL0000196900` | Q5A9X7, *Candida albicans* **Arp9** (SWI/SNF-type complex subunit), **unreviewed/TrEMBL** | IDA for `GO:0016586` (RSC-type complex), PMID:33151931; nucleus only by IBA/IEA |
| IBA | GO:0005634 | `SGD:S000004636` | Q05123, *S. cerevisiae* **ARP9** — SWI/SNF complex component | nucleus **IDA** PMID:11011149; SWI/SNF + RSC complex IDA ×6 |
| IBA | GO:0005634 | `MGI:MGI:1343051` | Q9QY84, mouse **Actl7a** (the true ortholog) | nucleus **EXP** PMID:12672658, **EXP** PMID:21278383, **IDA** PMID:36734600; `GO:0001673 male germ cell nucleus` **IDA** PMID:12672658 |
| IBA | GO:0005634 | `UniProtKB:Q57ZL0` | *Trypanosoma brucei* protein, **unreviewed/TrEMBL**, no assigned name | nucleus **IDA** PMID:28727848 |
| IBA | GO:0005634 | `PANTHER:PTN008986520` | PANTHER internal tree node — not a protein | n/a |
| IBA | GO:0005737 cytoplasm | `MGI:MGI:1343051` | mouse Actl7a | cytoplasm **EXP** PMID:12672658, **IDA** PMID:21278383, **IDA** PMID:36734600 |
| IBA | GO:0005737 | `MGI:MGI:1343053` | Q9QY83, mouse **Actl7b** (paralogue) | cytoplasm **IDA** PMID:12672658 |
| IBA | GO:0005737 | `RGD:1304697` | Q641W9, rat **Actl7a** | cytoplasm **EXP** PMID:21278383 |
| IBA | GO:0005737 | `UniProtKB:Q9Y615` | **ACTL7A itself** — self-referential IBA, a PAINT curator judging the function core | valid by construction |
| IBA | GO:0005198 structural molecule activity | `PANTHER:PTN000940351`, `PANTHER:PTN008986528` | both PANTHER internal tree nodes — **neither is a protein** | n/a |
| IEA/ISS (all) | acrosome, nucleus, cytoplasm, Golgi, PT, acrosome assembly, spermatid development, fertilization | `UniProtKB:Q9QY84` (+ `ensembl:ENSMUSP00000092692`) | mouse Actl7a, the true ortholog | acrosome assembly **IMP** PMID:32923619 + PMID:36734600; spermatid development **IMP** PMID:37667331; fertilization **IMP** PMID:32923619 + PMID:35921706; perinuclear theca **IDA** PMID:41169243; Golgi **IDA** PMID:21278383 |
| IEA | GO:0007010 | `GO:0005200` | not a gene product — an **inter-ontology MF→BP link** from the gene's own TAS MF row | inherits whatever GO:0005200 rests on, i.e. PMID:10373328 |
| IPI | GO:0005515 | `UniProtKB:Q9UGI8` | **TES** (testin), human | structurally characterised, PDB 2XQN, mutagenesis |
| IPI | GO:0005515 | `UniProtKB:P35663` | **CYLC1** (cylicin-1), human | co-IP, PMID:38573307 |
| IPI | GO:0005515 | `UniProtKB:Q8TC94` | **ACTL9**, human | co-IP, PMID:33626338 |

Two things fall out of this table.

1. **The `nucleus` IBA is not a fold artefact, even though the family is mixed.** I expected the
   ARP9 sources to be the whole story; they are not. The mouse ortholog carries its *own* IDA/EXP
   nucleus evidence, and even a specific term (`GO:0001673 male germ cell nucleus`) from the same
   1999–2003 T-actin work. So the term is right; what is not established is any nuclear
   *activity*, which is what `is_active_in` asserts.
2. **The `structural molecule activity` IBA has no protein source at all.** Both WITH/FROM tokens
   are internal PANTHER nodes, and across the whole ACTL7 orthologue set (human ACTL7A, mouse
   Actl7a/Actl7b, rat Actl7a) the *only* non-IBA support for GO:0005198 or any descendant is the
   human gene's own `GO:0005200` **TAS** row — which cites the 1999 cloning paper.

## 5. The 1999 TAS row is a name-derived annotation

`GO:0005200 structural constituent of cytoskeleton` / `TAS` / `PMID:10373328` (source: ProtInc).
The cited paper is a positional-cloning paper: cDNA selection, genomic sequencing, linkage
mapping, and Northern expression analysis. Its abstract contains no functional or biochemical
experiment; the only structural statement is homology-based ("Two novel human actin-like genes,
ACTL7A and ACTL7B, were identified by cDNA selection and direct genomic sequencing"). The
"structural constituent of cytoskeleton" claim therefore comes from the *name* "actin-like", not
from data — the exact failure mode this campaign keeps finding, where a fold or domain name is
promoted to an activity.

It then propagates: `GO:0007010 cytoskeleton organization` is attached by GO_REF:0000108, whose
WITH/FROM is literally `GO:0005200` — an inter-ontology MF→BP link. So one 1999 name-based
inference produces both an MF and a BP row.

Notably, the *conclusion* is largely defensible on 2011–2025 evidence (the acroplaxome and PT are
cytoskeletal structures — GO:0033011 is itself a descendant of `GO:0005856 cytoskeleton` — and the
KO does lose subacrosomal F-actin). But the cited evidence does not support it, and the BP that
falls out of it is far less specific than what the mouse KO actually shows.

## 6. Structure-guided audit of the fold (this review's own analysis)

Full method and tables: `ACTL7A-bioinformatics/RESULTS.md`, regenerated by
`uv run --script actin_fold_audit.py`. Contact residues are computed by neighbour search from
PDB **2BTF** (profilin–β-actin, ATP) and PDB **8A2S** (cryo-EM F-actin, Mg-ADP-Pi, 5 protomers)
and mapped through a MAFFT alignment; nothing is hard-coded, and every position is shown in a
gap-free alignment window so the mapping can be checked.

Three results matter for curation.

- **The nucleotide cleft is largely retained.** ACTL7A is 63.2% identical to actin across the 19
  positions within 4.0 Å of ATP or the divalent cation (66.7% at the phosphate contacts). The
  calibration: conventional actins 96.5%, Arp2/Arp3 79.0%, and the genuinely divergent yeast
  SWI/SNF Arps (Arp7/Arp9) 36.9%. ACTL7A is nowhere near the "lost it" end of the family.
  [file:human/ACTL7A/ACTL7A-bioinformatics/RESULTS.md "* **Nucleotide cleft largely retained.** ACTL7A is 63.2% identical to actin across the 19 G-actin cleft positions (66.7% at the phosphate contacts), against 96.5% for conventional actins, 79.0% for Arp2/Arp3 and 36.9% for the divergent SWI/SNF Arps."]
- **The ATP-hydrolysis trigger is not retained.** Of the five literature-defined catalytic
  positions (Asp11, Gln137, Asp154, Val159, His161 — PMID:37009486, PMID:30622175) ACTL7A keeps
  three: `DQEVY`. Asp154→Glu is conservative; **His161→Tyr is not**, and His161 is precisely the
  residue whose side-chain flip on filament incorporation triggers hydrolysis. Every conventional
  actin and Arp1/Arp2/Arp3 in the panel keeps all five. ACTL7B keeps His161; ACTL7A and ACTL9 do
  not. The alignment here is anchored on an identical `PIYEGY` motif on the C-terminal side, so
  this is not an alignment artefact.
- **The filament interface is not retained.** Across the 79 inter-protomer contact positions of
  F-actin, ACTL7A matches actin at 42.3%, versus 93.2% for conventional actins and 55.7% for
  Arp1, which *does* form a filament (in dynactin). This is quantitatively consistent with the
  cell-biological negative in PMID:21278383.

And a fourth result that guards against the opposite error — writing the pocket off as vestigial:
**reported patient variants cluster in the cleft.** 20 of ACTL7A's 435 residues (4.6%) align to a
cleft position, yet 2 of 5 variants reported in SPGF86 patients land there (`G246A` ↔ actin
Gly182; `G362R` ↔ actin Gly301, a phosphate contact), against 0 of 4 population polymorphisms;
exact binomial p = 0.019. A third, `D75A` (PMID:36574082), maps to actin **Asp11**, part of the
divalent-cation site, just outside the 4.0 Å shell. The sample is small and biased, and UniProt
flags A245T/G246A/G362R as "uncertain significance" — but the pocket is clearly not decorative.

**Synthesis.** ACTL7A is not a canonical actin and not an emptied-out fold. It most likely still
*binds* nucleotide (pocket conserved, disease variants concentrated there) while being unable to
run actin's hydrolysis cycle (His161 lost) and unable to build a canonical filament (interface
degenerate, plus the direct negative in cells). That is exactly the profile of a **structural /
scaffolding actin-fold protein**, which is what the acroplaxome phenotype demands. Nothing here
justifies annotating polymerisation; nothing here justifies asserting the pocket is dead either.
No ATP-binding assay on ACTL7A exists, so no MF annotation is proposed — it goes in
`suggested_experiments`.

## 6b. ACTL7A versus ACTL7B — the paralogue pair, checked rather than assumed

ACTL7A and ACTL7B are head-to-head neighbours with >65% identity to each other
[PMID:10373328], which makes them the obvious candidates for annotation cross-transfer. Mouse
Actl7b (`MGI:MGI:1343053`) is in fact already a WITH/FROM donor on ACTL7A's `GO:0005737`
cytoplasm IBA row. So the pair was checked on every axis where this review makes a claim, rather
than assumed to behave alike. They are separable on all four.

| axis | ACTL7A | ACTL7B |
|---|---|---|
| ATP-hydrolysis catalytic set (D11/Q137/D154/V159/H161) | `DQEVY` — **His161 lost** | `DQEVH` — **His161 retained** |
| nucleotide cleft identity to actin | 63.2% | 68.4% |
| phosphate-contact identity | 66.7% | 75.0% |
| F-actin protomer interface identity | 42.3% | 36.4% |
| expression | broad by Northern; testis-enriched | testis and prostate only [PMID:10373328] |
| localisation, mouse germ cells | nucleus; present in sperm heads **and** tails | cytoplasm; **not** in sperm |
| N-terminal extension | binds TES LIM2-3 (PDB 2XQN) | "distinct" from ACTL7A's |

Three consequences.

1. **The `GO:0005737` cytoplasm IBA rests partly on the paralogue's half of the experiment.**
   PMID:12672658's localisation sentence — [PMID:12672658 "Although the cellular locations of
   these two proteins are quite different (T-ACTIN-1 was found in the cytoplasm and T-ACTIN-2 was
   located in the nucleus)"] — is only usable with the naming key: [PMID:12672658 "The mRNA sizes
   and deduced molecular masses of t-actin 1/mACTl7b and t-actin 2/mACTl7a were 2.2 kilobases (kb)
   and 1.8 kb, and Mr 43.1 x 10(3) and Mr 47.2 x 10(3), respectively."] T-ACTIN-1 is **ACTL7B**.
   So that paper's cytoplasm evidence belongs to the paralogue and its nucleus evidence to ACTL7A.
   The cytoplasm transfer survives only because mouse Actl7a has *independent* cytoplasm IDAs
   (PMID:21278383, PMID:36734600). The donor is now marked `SUPPORTS_SOURCE_BUT_NOT_TARGET`.
2. **`GO:0030274 LIM domain binding` must not be assumed to transfer to ACTL7B.** The TES
   interaction is carried entirely by ACTL7A's N-terminal extension, and that extension differs
   between the two: [PMID:21278383 "In addition, we have found that Arp7B, whose N-terminal
   extension is distinct from that of Arp7A (16), is also strongly enriched in the acroplaxome."]
   Both proteins reach the acroplaxome; only ACTL7A is known to get there partly via TES.
3. **The His161 split is the sharpest single discriminator in the family.** ACTL7B keeps actin's
   hydrolysis trigger; ACTL7A and ACTL9 replace it with tyrosine. That is a within-paralogue
   functional difference, not shared drift, and it means a "cannot run actin's hydrolysis cycle"
   argument made for ACTL7A does **not** carry over to ACTL7B.

## 7. Human disease genetics, and the GO gap it exposes

Bi-allelic ACTL7A variants cause **spermatogenic failure 86 (SPGF86, MIM:620499)**, presenting as
normal-looking semen with total fertilization failure or early embryonic arrest after IVF/ICSI
[PMID:32923619; PMID:34727571; PMID:36593593; PMID:37004249]. The mechanistic through-line is
**oocyte activation**: [PMID:34727571 "Protein expression of ACTL7A and phospholipase C zeta, a
key sperm-borne oocyte activation factor, was significantly reduced in the affected sperm compared
to healthy controls, suggesting that the ACLT7A variants lead to an oocyte activation deficiency
and TFF."] and the defect is rescued pharmacologically: [PMID:34727571 "AOA by calcium ionophore
(A23187) after ICSI successfully rescued the TFF and achieved a live birth for the patient with
ACTL7A variants."] The same axis is reported in mouse [PMID:32923619 "the sperm from
ACTL7A/Actl7a-mutated men and mice showed reduced expression and abnormal localization of PLCζ as
a potential cause of embryonic arrest and failure of fertilization."] and for the G402S knock-in
[PMID:35863052 "The mutant sperm failed to activate the oocyte, and sperm-borne oocyte activation
factor phospholipase C zeta (PLCζ) discharge accompanied by ACTL7A was observed, leading to total
fertilization failure (TFF)."].

GOA's most specific process term for ACTL7A is `GO:0009566 fertilization`. `GO:0007343 egg
activation` exists and *is* a descendant of GO:0009566, and human **PLCZ1** carries it as
`IMP PMID:26721930` — i.e. GO already uses this term for a sperm-borne factor whose loss causes
oocyte-activation failure in patients. ACTL7A is the same case and does not have it. That is the
main annotation gap proposed here.

## 8. Missing process term for the F-actin phenotype

Neither human ACTL7A nor mouse Actl7a has any annotation to `GO:0030036 actin cytoskeleton
organization`, `GO:0007015 actin filament organization`, or any descendant (checked by QuickGO
`goUsage=descendants` on Q9QY84 and Q9Y615) — even though the central result of PMID:36734600 is
total loss of subacrosomal F-actin in the KO. The only actin-process row present is the
inter-ontology `GO:0007010 cytoskeleton organization`, which arrived via the 1999 TAS MF. Moving
that row to `GO:0030036` puts the correct, evidenced process in place of a parent that was reached
by the wrong route.

## 9. Decisions and their rationale

| action | n | rows |
|---|---|---|
| ACCEPT | 10 | **GO:0005200 TAS** (the core MF); acrosome assembly ×2; spermatid development ×2; fertilization ×2; perinuclear theca ×2; protein-containing complex IDA |
| KEEP_AS_NON_CORE | 15 | nucleus IBA/IEA/ISS/HDA; cytoplasm IBA/IEA/ISS; Golgi IEA/ISS ×2; cytoskeleton IEA + TAS; **GO:0005198 IBA** (parent of the core MF); protein binding (CYLC1, ACTL9) |
| MODIFY | 5 | acrosomal vesicle IEA/IMP/IDA → perinuclear theca; cytoskeleton organization → actin cytoskeleton organization; protein binding (TES) → LIM domain binding |
| NEW | 1 | GO:0007343 egg activation, IMP |
| MARK_AS_OVER_ANNOTATED | 0 | — |
| REMOVE | 0 | — |

**How the two structural MF rows were resolved (revised after review).** The first draft flagged
`GO:0005200` as over-annotated on provenance grounds while `ACCEPT`ing its vaguer parent
`GO:0005198` and promoting *that* to the core molecular function — which is incoherent, since the
draft's own reason argued GO:0005200's term was defensible and needed only re-sourcing, and
`core_functions[0].description` literally began "Structural constituent of the acroplaxome". The
provenance criticism and the term's correctness are separable judgements and are now recorded
separately: **`GO:0005200` is `ACCEPT`ed and is the core MF** (the acroplaxome is an F-actin and
keratin plate; GO:0033011 is a GO:0005856 descendant; the KO loses subacrosomal F-actin; the
structure audit finds a structural, non-polymerising profile), with the inadequate 1999 TAS
citation and its GO_REF:0000108 knock-on argued inside `reason`. **`GO:0005198` is
`KEEP_AS_NON_CORE`**, as a true but redundant parent — the same treatment given to the `cytoplasm`
and `cytoskeleton` parents. Nothing now carries `MARK_AS_OVER_ANNOTATED`: on inspection no term on
this gene actually overshoots, and the defect was always the *citation* and the *inference chain*,
not the terms.

Why the three `GO:0001669` rows get the same MODIFY, including the two experimental ones. The
argument is definitional rather than a challenge to anyone's data. GO:0001669 is "A structure in
the head of a spermatozoon that contains acid hydrolases ... derived from the lysosome", with
exact synonyms "acrosome" and "acrosomal granule" — a membrane-bounded vesicle. ACTL7A is a
cytosolic cytoskeletal protein sitting on the *nuclear* side of the inner acrosomal membrane, so
`located_in` that vesicle is a category error regardless of how good the immunofluorescence is;
what the IF shows is an acrosomal-*region* signal, which at light-microscope resolution
necessarily includes the acroplaxome underneath. The same paper that reports the human
`G402S` phenotype describes wild-type ACTL7A as *attached to the acroplaxome*. `MODIFY` (not
`REMOVE`) is the right instrument: the observation is real and the intended compartment is one
step away. Both reasons say explicitly that a curator with figure access should confirm.

Why no REMOVE anywhere. The other two candidates were the `GO:0005200` TAS row and the
`GO:0005198` IBA. In both cases the *term* survives scrutiny even though its *evidence* does not:
GO:0005200's claim is supportable by post-2011 work (the PT/acroplaxome is a cytoskeletal
structure and GO:0033011 is a GO:0005856 descendant), so `MARK_AS_OVER_ANNOTATED` — which needs no
positive argument — is the right instrument; and GO:0005198, despite having no protein-level
source, states something the KO phenotype supports.

Why the four `nucleus` rows are all `KEEP_AS_NON_CORE` rather than refined to `GO:0001673`. The
mouse source of the ISS row carries `GO:0001673 male germ cell nucleus` by IDA, so refining is
tempting and is recorded as a suggested question. Two things held it back: the rows would then
disagree with each other unless all four were changed, and PMID:10373328 reports ACTL7A message
"in a wide variety of adult tissues", so a somatic nuclear pool has not been formally excluded.
The substantive point about the nucleus is not its granularity but that **no nuclear activity has
been demonstrated**, which `KEEP_AS_NON_CORE` states directly.

Two evidence-code observations, recorded here rather than in row summaries. `GO:0001669` /
**IMP** / PMID:34727571 uses an IMP code for a *location*; the underlying data are
immunofluorescence on patient sperm, which is an IDA-shaped observation. And the mouse-derived
rows are correctly ISS/IEA rather than IDA/IMP — the mouse knock-out and knock-in phenotypes
justify ortholog transfer to the human gene, not direct-assay codes on it.

## 10. Affinage deep-research record

`gates_passed: True`, faith 83.3%, 14 citations. The narrative is broadly accurate and its PLCζ
framing is confirmed against the primary papers. Two cautions applied here:

- One citation, `PMID:bio_10.1101_2025.03.27.645694`, is a **bioRxiv DOI in a PMID-shaped field**,
  not a PubMed record; the ACTRT1/ACTRT2/ARPM1/ZPBP co-IP claim resting on it is excluded from
  this review.
- `PMID:38464253` is a preprint (bioRxiv); its HDAC1/HDAC3 and INO80/SWI-SNF HSA-domain-docking
  claims are interesting but in-silico/preliminary and are not used to support any annotation.
  They are the reason the nuclear pool is flagged as a knowledge gap rather than dismissed.

Its own GO grounding lists `GO:0008092 cytoskeletal protein binding` and `GO:0005198 structural
molecule activity` as the molecular activities and `GO:0005634 nucleus, GO:0005856 cytoskeleton`
as localisation — coarse, and it misses the acroplaxome/PT entirely, so it was not imported.

## 11. Review round log

**Round 2 (PR #2271, `ai4c-agent` CHANGES_REQUESTED).** Two IMPORTANT items, both correct, both
fixed:

1. *A supporting quote that argued the opposite.* The `GO:0005737` cytoplasm IBA row cited
   PMID:12672658's "T-ACTIN-1 was found in the cytoplasm and T-ACTIN-2 was located in the nucleus".
   Since T-ACTIN-2 **is** mACTL7A, that sentence is evidence for the *nucleus* on this gene and for
   the *cytoplasm* on the paralogue. Replaced with PMID:21278383 and PMID:36734600 quotes that
   actually bear on ACTL7A, the naming key added as a reference finding, and the paralogue donor
   `MGI:MGI:1343053` downgraded to `SUPPORTS_SOURCE_BUT_NOT_TARGET`. The general lesson: in a paper
   that studies a paralogue *pair* under aliases, the alias-to-gene key is part of the evidence and
   has to be quoted alongside the claim.
2. *Flagging the specific MF down while promoting its vague parent.* Resolved as described in §9.

Non-blocking items also taken: `core_functions[2]` now says why it asserts no molecular function
rather than leaving the slot silently empty; the `GO:0001669` IMP row records that `UNDECIDED` was
considered and why `MODIFY` was preferred; and the `GO:0001673` deferral no longer leans on an mRNA
Northern survey to hedge a protein-localisation question — the real reasons are donor heterogeneity
on the phylogenetic row and the absence of any somatic-nucleus experiment either way.

Also added this round, at the coordinator's prompt, the systematic ACTL7A/ACTL7B comparison in §6b.
That was worth doing independently of the review: it turned up the paralogue-donor problem on the
cytoplasm row from the other direction, and it establishes that `GO:0030274 LIM domain binding`
should **not** be assumed to transfer to ACTL7B, whose N-terminal extension is a different
sequence.
