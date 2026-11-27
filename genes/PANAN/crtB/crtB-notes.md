# crtB (P21683) — *Pantoea ananatis* 15-cis-phytoene synthase — curation journal

## 1. Identity check

The target is unambiguous. UniProt entry `CRTB_PANAN` / **P21683**, 309 aa,
reviewed (Swiss-Prot), evidence level `PE 1: Evidence at protein level`
[file:PANAN/crtB/crtB-uniprot.txt "Evidence at protein level"]. The recommended
name is [file:PANAN/crtB/crtB-uniprot.txt "Full=15-cis-phytoene synthase"] with
[file:PANAN/crtB/crtB-uniprot.txt "EC=2.5.1.32 {ECO:0000269|PubMed:9593819};"].

**Nomenclature caution that matters for reading the evidence:** the organism is
recorded by UniProt as [file:PANAN/crtB/crtB-uniprot.txt "Pantoea ananas (Erwinia
uredovora)."], NCBI taxon 553. Both cached primary papers say *Erwinia uredovora*
in their titles. That is the **same organism under its historical name**, not a
different species — so neither paper is an off-target citation. The GOA rows
likewise carry `TAXON NAME: Pantoea ananas`. I note this explicitly because the
CLAUDE.md rule about not dismissing a citation whose title names something else
applies in reverse here: the title looks wrong but is right.

## 2. What the cached literature actually shows

Both cached publications are **abstract-only** (`full_text_available: false`).
Neither is a case where I need the full text, because in each the abstract itself
states the result being annotated.

### PMID:9593819 (Neudert et al. 1998) — the source of both IDA rows

Abstract-only, but unusually informative. It is a direct in-vitro biochemical
characterisation of *this* protein:

- Heterologous overexpression: [PMID:9593819 "The crtB gene encoding phytoene
  synthase from the carotenogenic enterobacterium Erwinia uredovora was
  overexpressed to about 20% of the total cellular protein in Escherichia coli."]
- The catalysed conversion: [PMID:9593819 "A non-radioactive assay was developed
  that enabled the conversion of GGPP to phytoene."]
- Product identification: [PMID:9593819 "The reaction product was identified by
  co-chromatography with authentic standards on HPLC systems and comparison of
  spectral characteristics."] and [PMID:9593819 "The phytoene formed in vitro was
  present in both a 15-cis and all-trans isomeric configuration."]
- Cofactors: [PMID:9593819 "The essential cofactors required were ATP in
  combinations with either Mn2+ or Mg2+."]
- Kinetics: [PMID:9593819 "The Km value for GGPP was determined as 41 microM."]
- Inhibition: [PMID:9593819 "Phytoene synthesis was inhibited by phosphate ions
  and squalestatin."]

The 15-cis/all-trans mixture is not an ambiguity about the enzymatic product.
UniProt resolves it: [file:PANAN/crtB/crtB-uniprot.txt "The enzyme produces
15-cis-phytoene."], with the all-trans form arising non-enzymatically by
photoisomerisation. So GO:0046905 (15-cis-phytoene synthase activity) is the
correct specific term, not a generic phytoene synthase term.

**A detail from this abstract does a lot of curation work below.** Expressing
CrtB alone *poisoned* the host: [PMID:9593819 "Presumably inhibition of growth
arose from the depletion of the substrate geranylgeranyl pyrophosphate (GGPP)"],
and the fix was to supply more GGPP from a different enzyme: [PMID:9593819 "GGPP
levels were increased by co-expressing the isoprenoid biosynthetic genes crtE and
idi, encoding the Erwinia GGPP synthase and Rhodobacter isopentenyl pyrophosphate
isomerase, respectively."] CrtB therefore **consumes** GGPP, and the GGPP
*synthase* of this organism is a **different gene, crtE**. This is direct
experimental refutation of the GO:0004311 IEA row (section 4.1).

### PMID:2254247 (Misawa et al. 1990) — pathway context

Abstract-only. Cloned the six-gene cluster from this organism: [PMID:2254247 "Six
open reading frames were found and designated the crtE, crtX, crtY, crtI, crtB,
and crtZ genes in reference to the carotenoid biosynthesis genes of a
photosynthetic bacterium, Rhodobacter capsulatus"], from [PMID:2254247 "a
phytopathogenic bacterium, Erwinia uredovora 20D3 (ATCC 19321)"], and established
the pathway by [PMID:2254247 "analyzing carotenoids accumulated in E. coli
transformants in which some of these six genes were expressed"]. This is not a
GOA reference row for crtB; I use it only for pathway position and to establish
that crtE and crtB are separate genes with separate activities. Fetched with
`uv run ai-gene-review fetch-pmid 2254247`.

The abstract's inline pathway string is mangled by the text extraction (the
arrows and gene labels ran together), so I have deliberately **not** quoted it and
have taken no ordering claim from that fragment. The gene-cluster and
transformant-analysis sentences quoted above are clean.

## 3. UniProt's biochemistry, and the module

UniProt gives three experimentally-evidenced (`ECO:0000269|PubMed:9593819`)
reaction records, all one overall transformation split into its two half-steps:
the overall `RHEA:34475` (2 GGPP = 15-cis-phytoene + 2 diphosphate), the first
half `RHEA:22296` (2 GGPP = prephytoene diphosphate + diphosphate), and the second
half `RHEA:34479` (prephytoene diphosphate = 15-cis-phytoene + diphosphate). The
FUNCTION line describes the same two-stage mechanism. Pathway:
[file:PANAN/crtB/crtB-uniprot.txt "Carotenoid biosynthesis; phytoene
biosynthesis."]. Family: [file:PANAN/crtB/crtB-uniprot.txt "Belongs to the
phytoene/squalene synthase family."].

`modules/carotene_backbone_biosynthesis.yaml` lists this exact protein
(`UniProtKB:P21683`) as a representative member of the phytoene-synthesis step,
with required function GO:0046905 and `RHEA:34475` as evidence, in PANTHER family
PTHR31480. The UniProt record agrees: [file:PANAN/crtB/crtB-uniprot.txt "PANTHER;
PTHR31480; BIFUNCTIONAL LYCOPENE CYCLASE/PHYTOENE SYNTHASE; 1."] (the family name
reflects the fungal bifunctional members; bacterial CrtB is single-domain). The
review below is consistent with the module and asserts nothing beyond it.

## 4. Per-annotation reasoning

Eight GOA rows. No CC rows at all, no IBA rows, no `protein binding` row, no
negated rows, no isoform rows.

### 4.1 GO:0004311 geranylgeranyl diphosphate synthase activity — IEA, InterPro2GO — **REMOVE**

Verified definition (QuickGO): "Catalysis of the reaction: (2E,6E)-farnesyl
diphosphate + isopentenyl diphosphate = (2E,6E,10E)-geranylgeranyl diphosphate +
diphosphate." That is head-to-tail chain elongation **producing** GGPP.

CrtB does the opposite: GGPP is its **substrate**. Three independent lines:

1. Direct experiment. CrtB expression depleted host GGPP and had to be rescued by
   co-expressing crtE, the actual GGPP synthase [PMID:9593819 "Presumably
   inhibition of growth arose from the depletion of the substrate geranylgeranyl
   pyrophosphate (GGPP)"]. An enzyme cannot both deplete GGPP and be its synthase.
2. Gene-level separation in this very organism: crtE and crtB are distinct ORFs in
   the same cluster [PMID:2254247 "Six open reading frames were found and
   designated the crtE, crtX, crtY, crtI, crtB, and crtZ genes in reference to the
   carotenoid biosynthesis genes of a photosynthetic bacterium, Rhodobacter
   capsulatus"].
3. Chemistry: GGPP synthase is a 1'-4 head-to-tail prenyltransferase; CrtB is a
   1'-1 head-to-head condensing enzyme. Different bond, different product class.

The source signature is IPR044843, [file:PANAN/crtB/crtB-uniprot.txt "InterPro;
IPR044843; Trans_IPPS_bact-type."] — a **fold/superfamily-level** trans-isoprenyl
diphosphate synthase entry (cf. Gene3D 1.10.600.10 "Farnesyl Diphosphate Synthase"
and SSF48576 "Terpenoid synthases" on the same record). Mapping a shared all-alpha
terpenoid-synthase fold to one specific chain-elongation activity assigns the
**paralog's** activity (CrtE's) to CrtB. This is exactly the InterPro2GO
paralog-overannotation case the brief describes. REMOVE.

### 4.2 GO:0051996 squalene synthase [NAD(P)H] activity — IEA, InterPro2GO — **REMOVE**

Verified definition (QuickGO): "Catalysis of the reaction: 2 (2E,6E)-farnesyl
diphosphate + H+ + NAD(P)H = 2 diphosphate + NAD(P)+ + squalene." Every component
is wrong for CrtB: the substrate is FPP (C15) not GGPP (C20), the product is
squalene (C30) not phytoene (C40), and the reaction consumes NAD(P)H.

The NAD(P)H point is the decisive one and is mechanistically informative rather
than merely bookkeeping. Squalene synthase and phytoene synthase are genuine
homologues and both form a cyclopropylcarbinyl diphosphate intermediate by
head-to-head condensation (presqualene-PP and prephytoene-PP respectively — the
latter is explicit in UniProt's `RHEA:22296` record for this protein). The
families then **diverge at the second half-step**: squalene synthase reductively
opens the intermediate using NADPH, whereas phytoene synthase instead eliminates a
proton, installing the central double bond. That elimination is precisely why the
product is *15-cis*-phytoene and why no nicotinamide cofactor is needed. The
experimentally determined cofactor requirement for this protein contains no
NAD(P)H at all: [PMID:9593819 "The essential cofactors required were ATP in
combinations with either Mn2+ or Mg2+."] So the one feature that *names*
GO:0051996 is the step CrtB demonstrably does not perform.

The source signature IPR033904, [file:PANAN/crtB/crtB-uniprot.txt "InterPro;
IPR033904; Trans_IPPS_HH."], is the **shared head-to-head** trans-IPPS domain
(same record carries `CDD; cd00683; Trans_IPPS_HH`), common to both families by
construction, so it cannot discriminate between them. REMOVE.

**Counter-argument I considered and rejected.** CrtB is inhibited by squalestatin
[PMID:9593819 "Phytoene synthesis was inhibited by phosphate ions and
squalestatin."], and squalestatin is a squalene synthase inhibitor. Does that
support GO:0051996? No. Inhibitor cross-reactivity reports active-site similarity,
which is already explained by the shared fold and is the reason the InterPro
signature matches in the first place. Being inhibited by a drug aimed at a
homologue is not evidence of performing the homologue's reaction. Noted here so
the removal is made with the contrary evidence on the table, not around it.

### 4.3 GO:0016765 transferase activity, transferring alkyl or aryl (other than methyl) groups — IEA — **MODIFY**

Not wrong, just uninformative. I confirmed by QuickGO ancestor query that
GO:0046905 **is** a descendant of GO:0016765 (path: GO:0046905 -> GO:0004659
prenyltransferase activity -> GO:0016765 -> GO:0016740 transferase activity), so
the row is a true grandparent-level assertion. Its supporting signatures are
ARBA:ARBA00026321 and IPR019845, the latter being
[file:PANAN/crtB/crtB-uniprot.txt "InterPro; IPR019845;
Squalene/phytoene_synthase_CS."] — a conserved-*site* pattern shared across the
whole phytoene/squalene synthase family. A family-wide site pattern can only
license a family-wide statement, so the generic term is a reasonable *automatic*
output. But this protein has a directly demonstrated, EC- and Rhea-matched
activity, so retaining a term that says only "transfers some non-methyl alkyl
group to something" adds nothing. MODIFY to GO:0046905.

I weighed the annotation-reviewer guidance that broader IEAs may simply be
ACCEPTed. I judged this one too general to leave: it is two levels above even
prenyltransferase activity and conveys no substrate, no product, and no pathway.

### 4.4 GO:0046905 15-cis-phytoene synthase activity — IDA (PMID:9593819) and IEA (Rhea/EC) — **ACCEPT** (both)

The IDA is as clean as this evidence type gets: purified-enzyme in-vitro assay,
product confirmed against authentic standards, on the protein from this organism.
The IEA row is grounded in `RHEA:34475` and `EC:2.5.1.32`, which are the same
reaction and match UniProt's experimentally-evidenced catalytic-activity record
exactly. Duplicate GO IDs across evidence codes are expected and fine; I accept
both rather than collapsing them.

### 4.5 GO:0016117 carotenoid biosynthetic process — IDA (PMID:9593819) and IEA (ARBA) — **ACCEPT** (both)

Participation test: CrtB **catalyses a step** of this process — the committed
head-to-head condensation that makes the first C40 carotenoid. It is not merely
required for, consumed by, or acted on by the pathway. Passes cleanly; this is the
straightforward catalyst case, no scaffold/cofactor reasoning needed.

### 4.6 GO:0016120 carotene biosynthetic process — IEA, GO_REF:0000108 — **ACCEPT**

Inter-ontology logical inference from GO:0046905, which the gene holds with IDA.
Sound on the chemistry: GO:0016120 is defined (QuickGO) as "The chemical reactions
and pathways resulting in the formation of carotenes, hydrocarbon carotenoids",
and 15-cis-phytoene is exactly that — the C40 hydrocarbon precursor of every
downstream carotene.

*Ontology-structure note, recorded but deliberately not acted on.* I verified via
QuickGO that GO:0016120 is **not** currently a descendant of GO:0016117 (its
ancestors run through GO:0016119 carotene metabolic process and GO:0008299
isoprenoid biosynthetic process). The gene therefore legitimately holds both terms
and neither is redundant with the other. Per the brief I make no claim that one
subsumes the other and propose no ontology fix.

## 5. Why I proposed no NEW annotations

Three candidates were considered and all three were declined.

**Prephytoene diphosphate synthase activity.** UniProt records the first half-step
(`RHEA:22296`) as a separately evidenced catalytic activity, so a term for it
would be defensible in principle. There is no such term to use: GO:0016767
"geranylgeranyl-diphosphate geranylgeranyltransferase activity" was exactly this
reaction and I confirmed against QuickGO that it is **obsolete** (`isObsolete:
True`). GO has therefore already decided this half-step is not separately
annotated, and the overall GO:0046905 covers the transformation. Nothing to add.

**Metal ion binding (GO:0000287 / GO:0030145 / GO:0046872).** The cofactor
requirement is experimentally established for this protein [PMID:9593819 "The
essential cofactors required were ATP in combinations with either Mn2+ or Mg2+."]
and UniProt carries the `Metal-binding`, `Magnesium` and `Manganese` keywords. I
still declined. A cofactor requirement in a bulk assay does not by itself localise
the metal to the protein: divalent cations also chelate the diphosphate leaving
groups of the substrate. Decisively, the UniProt record contains **no `FT BINDING`
features at all** — only `FT CHAIN` and a disordered `FT REGION` — so UniProt's own
curators, with the full text, did not place a metal site on this sequence. The deep
research report reaches the same limit, noting that catalytic-residue assignments
here "should remain family-based predictions, not protein-specific experimental
facts". Asserting a binding term would be filling a slot the primary curators left
empty. Raised as a suggested experiment instead.

**A stress/photoprotection process term.** The literature associates *P. ananatis*
carotenoid production with oxidative-stress and toxoflavin tolerance, and a crtB
lesion would abolish all downstream carotenoids. This is necessity, not
participation: the protective chemistry is done by the coloured downstream
products (lycopene, beta-carotene, zeaxanthin), not by CrtB and not by its own
colourless product phytoene. Under the CLAUDE.md participation rule, knockout
abolishing an outcome establishes that the gene is *required*, which is precisely
what being the pathway's entry enzyme means, and cannot substitute for asking
which entity performs the step. CrtB performs the condensation step and nothing
else. Declined.

## 6. Localization — asserted nowhere, recorded as a gap

GOA has **no** cellular-component row for this protein, and I add none. There is no
localization experiment for P21683: the deep research report states plainly that
cytosolic or cytoplasmic-face placement [file:PANAN/crtB/crtB-deep-research-falcon.md
"remains inferred rather than experimentally demonstrated for P21683"]. The
sequence offers no positive signal either way — no signal peptide, no transmembrane
segment, the only feature besides the chain being a disordered C-terminal region.

Cytoplasm would be a low-risk guess for a bacterial soluble enzyme, and the module
asserts `GO:0016020 membrane` at its taxon-neutral root on substrate-hydrophobicity
grounds. Those two plausible answers point in different directions, which is itself
the reason not to pick one. I therefore left `locations` out of the core function
rather than manufacturing a component assertion, and recorded it as a `CC_DARK`
knowledge gap with a concrete resolution. Substrate-specificity breadth is recorded
as a second gap on the same basis ([file:PANAN/crtB/crtB-deep-research-falcon.md
"No rigorous alternative-substrate panel for P21683 was recovered."]).

## 7. Outcome

Action tally over 8 rows: **ACCEPT 5, MODIFY 1, REMOVE 2**. No UNDECIDED (both
cached papers are abstract-only, but each abstract states the result being
annotated, so nothing was unadjudicable) and no NEW. One core function.
