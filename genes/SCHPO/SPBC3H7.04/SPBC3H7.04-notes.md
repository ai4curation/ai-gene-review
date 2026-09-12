# SPBC3H7.04 (mS42 / bot1) — S. pombe mitoribosomal small subunit protein

## Identity

- **UniProt**: O74379 (RT26_SCHPO), 220 aa
- **UniProt name**: Small ribosomal subunit protein mS42; AltName: 37S ribosomal
  protein S26B, mitochondrial
- **PomBase**: SPBC3H7.04 — "mitochondrial ribosomal protein subunit S43a"
  (characterisation_status: biological role inferred; no gene symbol assigned)
- **PANTHER**: PTHR43595 (37S RIBOSOMAL PROTEIN S26, MITOCHONDRIAL);
  subfamily PTHR43595:SF2 = SMALL RIBOSOMAL SUBUNIT PROTEIN MS42
- **S. cerevisiae ortholog**: SGD:S000003862 (Rsm26p / MrpS35p family)

The S43a / mS42 dual naming reflects historical nomenclature: the
Amunts et al. 2014 cryo-EM structure of the S. cerevisiae mitoribosome named
this component mS42; some earlier annotations refer to it as mtSSU S43. Both
refer to the same protein — a mitochondrion-specific small ribosomal subunit
protein with no bacterial small-subunit homolog.

## Why this gene matters (context — geneontology/go-annotation#6474)

ValWood (2026-07-11, `geneontology/go-annotation#6474`) flagged **IPR019832**
(Iron/manganese superoxide dismutase, C-terminal domain) as producing incorrect
InterPro2GO annotations on **RSM26/mS42** — the mitoribosomal small-subunit
protein. She writes:

> RSM26 (mS42) is structurally classified in the SOD superfamily — but doesn't
> have SOD activity. This is a fold-reuse situation, not an enzyme. The
> Fe/Mn-SOD fold is an ancient bacterial structural scaffold. Because
> mitochondria are derived from bacteria, several mitoribosomal proteins retain
> this fold by ancestry but have been repurposed over evolution purely as
> ribosomal structural components — the metal-coordinating catalytic residues
> needed for actual dismutase chemistry aren't necessarily intact or
> functional.

The specific problematic chain in GOA is:

- `IEA with IPR019832 → GO:0004784 superoxide dismutase activity` (MF)
- `IEA with IPR019832 → GO:0006801 superoxide metabolic process` (BP)
- `IEA with IPR019832 → GO:0046872 metal ion binding` (MF)
- and, by inter-ontology logical inference from `GO:0004784`:
  `IEA GO_REF:0000108 → GO:0019430 removal of superoxide radicals` (BP)

All four are incorrect for the pombe protein: it is a mitoribosomal structural
subunit, not a superoxide dismutase.

## Evidence that mS42 is a mitoribosome component, not a SOD

### From UniProt (O74379)

- **FUNCTION** (`ECO:0000250|UniProtKB:P10662`, i.e. by-similarity to the
  S. cerevisiae ortholog): *"Component of the mitochondrial ribosome
  (mitoribosome), a dedicated translation machinery responsible for the
  synthesis of mitochondrial genome-encoded proteins... The mitoribosomes are
  attached to the mitochondrial inner membrane and translation products are
  cotranslationally integrated into the membrane."*
- **SUBUNIT** (`ECO:0000250|UniProtKB:P10662`): *"Component of the mitochondrial
  small ribosomal subunit (mt-SSU). Mature yeast 74S mitochondrial ribosomes
  consist of a small (37S) and a large (54S) subunit... mS43 forms a dimer with
  mS42, building a large protuberance adjacent to the mRNA channel exit in the
  mt-SSU body."*
- **SUBCELLULAR LOCATION** (`ECO:0000250|UniProtKB:P10662`): *"Mitochondrion."*
- **SIMILARITY** (`ECO:0000305`): *"Belongs to the mitochondrion-specific
  ribosomal protein mS42 family."*
- **KEYWORDS**: `Mitochondrion; Reference proteome; Ribonucleoprotein;
  Ribosomal protein.` — importantly, **no** `Cytoplasm` / `Superoxide dismutase`
  / `Metal-binding` / `Oxidoreductase` keywords, consistent with the manually
  curated view that this protein is a structural ribosomal component and not
  a metalloenzyme.

### From the InterPro / domain signatures (via UniProt cross-references)

Only *SOD-fold* signatures match — no SOD-*catalytic-site* signatures:

- `Gene3D 3.55.40.20` — Iron/manganese SOD C-terminal domain *fold*.
- `SUPFAM SSF54719 / SSF46609` — Fe,Mn SOD C-/N-terminal domain *structural*
  superfamily.
- `InterPro IPR019832 (Mn/Fe_SOD_C)`, `IPR036324`, `IPR036314` — all
  homologous-superfamily / structural-fold entries.
- `Pfam PF02777 (Sod_Fe_C)` — the SOD C-terminal Pfam.

There is **no** match to a PROSITE Mn/Fe-SOD active-site pattern (PS00088 —
Mn/Fe superoxide dismutase signature). PROSITE patterns require the canonical
catalytic residues **and** their flanking context to be preserved; failing the
pattern while matching the fold is the classic pseudoenzyme signature (see
`projects/PSEUDOENZYMES.md`, Pattern 2 and Pattern 6). This mirrors the
Cu/Zn-SOD pseudoenzyme detections in `projects/PSEUDOENZYMES.md` and in
`genes/RAMVA/RvY_13070/` (RvSOD15) — SOD fold present, SOD activity absent.

The PANTHER subfamily assignment resolves the ambiguity: **PTHR43595:SF2 —
SMALL RIBOSOMAL SUBUNIT PROTEIN MS42.** IEA-via-PANTHER goes to a subfamily and
correctly does not propagate any SOD MF/BP terms. The InterPro2GO mapping fails
because InterPro2GO is a per-entry blanket rule with no subfamily resolution
(see `projects/INTERPRO.md` — "no subfamily resolution" failure mode).

### From experimental / manual curation

- **PMID:18245278** (Wiley et al. 2008, *Eukaryot Cell*) — characterizes the
  S. pombe protein Bot1p (identified in the paper as related to
  S. cerevisiae MrpS35p, a mitoribosomal component). The paper shows Bot1p
  *"localizes to the mitochondria in live cells and cofractionates with
  purified mitochondrial ribosomes"* and *"is required for mitochondrial
  protein synthesis."* ComplexPortal (CPX-10315, 37S mitochondrial small
  ribosomal subunit) has curated SPBC3H7.04 into this complex and cites this
  paper as NAS for `GO:0005763 mitochondrial small ribosomal subunit` and
  `GO:0032543 mitochondrial translation`. The Bot1p / SPBC3H7.04 identity is
  supported by the paper's characterization of Bot1p as the S. pombe
  MrpS35p-family mitoribosomal protein — the same functional group as mS42.
- **PomBase HDA** (in `SPBC3H7.04-uniprot.txt`): `GO:0005634 nucleus`,
  `GO:0005737 cytoplasm`, `GO:0005829 cytosol` — these are high-throughput
  direct-assay localizations (mass-spec / imaging screens) that often pick up
  mitochondrial matrix proteins as "cytoplasmic". They are consistent with
  the mitochondrial matrix localization: mitoribosomal proteins are inside the
  mitochondrion but topologically the matrix is (loosely) a cytoplasmic
  compartment, and whole-cell / soluble-fraction mass-spec screens frequently
  pick them up. These HDA localizations do not appear in the QuickGO/GOA
  download used as this review's baseline; they are recorded in UniProt
  cross-references only and are not part of the twelve `existing_annotations`
  under review.
- **ComplexPortal CPX-10315** — the 37S mitochondrial small ribosomal subunit —
  includes SPBC3H7.04 as a subunit.

### The IBA `GO:0005737 cytoplasm` annotation

The IBA `cytoplasm` annotation propagates from the PANTHER family
PTHR43595 (Iron/Manganese Superoxide Dismutase). The `with_from` list is
telling — it includes canonical Fe/Mn-SOD paralogs (`SGD:S000002755` = SOD2 in
yeast, `UniProtKB:P00448` = SodA in *E. coli*). The family has both bona fide
SODs and the mitochondrion-specific mS42/mS43 mitoribosomal branch; IBA
propagates `cytoplasm` from the SOD side. For the mitoribosomal branch, the
specific location is `mitochondrial small ribosomal subunit`, not generic
cytoplasm, and mitochondrion is **not** a child of cytoplasm in the GO
cell-component hierarchy — so the IBA `cytoplasm` here is a taxonomically
plausible but sub-cellularly wrong annotation.

## Summary — review actions

The IEA InterPro2GO / logical-inference chain
(SOD activity, superoxide metabolic process, removal of superoxide radicals,
metal ion binding) is a **paradigmatic fold-reuse pseudo-SOD over-annotation**
of the mitoribosomal mS42/mS43 branch — the same annotation-error class as
Cu/Zn-SOD pseudoenzymes documented in `projects/PSEUDOENZYMES.md`. It should be
`REMOVE`d (all four terms).

The IBA `cytoplasm` is family-level noise from the SOD paralogs in PTHR43595;
`REMOVE` with a proposed replacement of the mitochondrial-ribosome location
that is already independently supported by NAS/ISO.

The NAS (PMID:18245278) and ISO annotations to
`GO:0005763 mitochondrial small ribosomal subunit`,
`GO:0032543 mitochondrial translation`,
`GO:0003735 structural constituent of ribosome`, and `GO:0005739 mitochondrion`
are **the correct, core-function annotations** and should be `ACCEPT`ed.

## Cross-references within this repo

- `projects/PSEUDOENZYMES.md` — pseudoenzymes framework; this case adds a new
  category: **mitoribosomal fold-reuse of an ancestral bacterial enzyme fold**
  (mitochondria are of bacterial origin, so mitoribosomal proteins that
  co-opted enzyme folds are a systematic source of pseudoenzyme
  over-annotations).
- `projects/INTERPRO.md` — IPR019832 appears in the per-entry priority table
  (7 reviewed / 5 suspect verdicts). Every existing verdict was on a real Fe/Mn
  SOD (MISSI/MnSOD, PSEPK/sodB, RAMVA/RvY_01767, yeast/SOD2); this review adds
  the first **exception member** for the entry — a protein whose SOD IEAs are
  not just non-core but outright incorrect. This shifts the entry from
  "SOD activity terms are broadly true but over-broad" toward "SOD activity
  terms are wrong for the mitoribosomal subfamily and should be demoted at the
  entry level with a `skos:broadMatch` (or an exact-match + `predicate_modifier:
  Not`) predicate in `INTERPRO/interpro2go.sssom.yaml`."
