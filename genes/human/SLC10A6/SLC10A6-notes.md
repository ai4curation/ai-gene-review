# SLC10A6 (SOAT) curation notes

UniProt: Q3KNW5 (SOAT_HUMAN), 377 aa, 7 transmembrane domains, glycosylated.
Gene: SLC10A6, synonym SOAT. Taxon: NCBITaxon:9606.

**Deep research was not available in this container** (Falcon returned HTTP 402,
OpenAI HTTP 401, perplexity not registered), so no `-deep-research-*.md` file was
generated. The literature synthesis below was assembled by hand from PubMed and
the cached `publications/PMID_*.md` records.

## Literature synthesis

### Core activity: sodium-coupled uptake of sulfated steroids

SOAT was cloned and characterized by Geyer and colleagues. In stably transfected
HEK293 cells it mediates sodium-dependent uptake of the three canonical steroid
sulfates with low-micromolar affinity
[PMID:17491011 "We established a stable SOAT-HEK293 cell line that showed
sodium-dependent transport of dehydroepiandrosterone sulfate, estrone-3-sulfate,
and pregnenolone sulfate with apparent K(m) values of 28.7, 12.0, and 11.3
microm, respectively."].
UniProt records the symport stoichiometry as 2 Na+ per steroid sulfate
(e.g. Rhea:RHEA:71083 for estrone 3-sulfate).

The substrate spectrum was extended by LC-MS/MS-based transport assays to
17alpha-hydroxypregnenolone sulfate, 17beta-estradiol-17-sulfate, androsterone
sulfate, epiandrosterone sulfate, testosterone sulfate, epitestosterone sulfate
and 5alpha-dihydrotestosterone sulfate, and the structural requirements were
defined [PMID:28951227 "The sodium-dependent organic anion transporter SOAT/Soat
shows highly specific transport activity for sulfated steroids."],
[PMID:28951227 "SOAT substrates from the group of sulfated steroids are
characterized by a planar and lipophilic steroid backbone in trans-trans-trans
conformation of the rings and a negatively charged mono-sulfate group at
positions 3' or 17' with flexibility for alpha- or beta- orientation."] — note
that a second sulfate group abolishes recognition (17beta-estradiol-3,17-disulfate
is not transported).

Beta-estradiol-3-sulfate and androstenediol-3-sulfate were added as substrates in
the testis study [PMID:23667501 "Additionally, β-estradiol-3-sulfate and
androstenediol-3-sulfate were identified as novel SOAT substrates."], and the
placental estriol precursor 16alpha-OH-DHEAS is a low-affinity substrate
[PMID:24717977 "stably transfected SOAT- and NTCP-HEK293 cells showed uptake only
under sodium conditions with Km of 319.0 ± 59.5 μM and Vmax of 1465.8 ± 118.8
pmol/mg protein/min for SOAT"].

The current review of the field states the specificity plainly
[PMID:37373074 "The sodium-dependent organic anion transporter (SOAT, gene symbol
SLC10A6) specifically transports 3'- and 17'-monosulfated steroid hormones, such
as estrone sulfate and dehydroepiandrosterone sulfate, into specific target
cells."].

### Bile acids: the decisive specificity question for this review

SOAT sits in the bile acid:sodium symporter (BASS, SLC10) family and is the
closest paralog of ASBT (48% identity), but the canonical bile acids are **not**
substrates [PMID:17491011 "Although bile acids, such as taurocholic acid, cholic
acid, and chenodeoxycholic acid, were not substrates of SOAT, the sulfoconjugated
bile acid taurolithocholic acid-3-sulfate was transported by SOAT-HEK293 cells in
a sodium-dependent manner and showed competitive inhibition of SOAT transport with
an apparent K(i) value of 0.24 mum."],
[PMID:34079822 "In addition, sodium-dependent organic anion transporter SOAT
specifically transports sulfated steroid hormones, but not bile acids."].

Reactome itself makes the same point in the summary of the very reaction that
grounds its TAS annotations
[Reactome:R-HSA-433089 "Unlike the other SLC10A gene products, SOAT shows no
affinity for binding bile acids. However, SOAT is able to transport
sulpho-conjugated bile acids such as taurolithocholate 3-sulphate (Geyer J et al,
2007)."].

**However, the bile-acid terms are not simply false for SOAT.** The systematic
three-carrier comparison found that taurolithocholic acid — an unsulfated,
taurine-conjugated bile salt — *is* a sodium-dependent SOAT substrate, with Km
19.3 uM, comparable to NTCP (18.4 uM) and ASBT (5.9 uM)
[PMID:34079822 "Surprisingly, SOAT showed significant sodium-dependent uptake of
TLC and, therefore, TLC is the only common substrate of all three carriers NTCP,
ASBT and SOAT, identified so far."]. The restriction is positional: additional
7'/12' hydroxylation abolishes it
[PMID:34079822 "This is, however, not possible when TLC is additionally
hydroxylated at the 7′ and/or 12’ positions, as it is the case for the BAs TCA,
TCDCA, or TDCA, which all are not transported by SOAT."].

Crucially for reviewing the IBA rows, the authors explicitly leave the
evolutionary question open
[PMID:34079822 "However, the question if TLC was also a substrate of the common
NTCP/ASBT/SOAT ancestor or if all three carriers later acquired the TLC transport
function cannot be finally answered."].

**Consequence for the IBA node placement.** The IBA rows for GO:0008508 and
GO:0015721 derive from PANTHER:PTN000040761, the node ancestral to the
Na+-dependent SLC10 clade (human SLC10A1/A2/A4/A6 all receive rows from it),
seeded by the rat descendants RGD:3681 (Slc10a1/Ntcp) and RGD:3682
(Slc10a2/Asbt). I did **not** find grounds to reject that node placement for
SLC10A6: SOAT retains sodium-coupled symport of a genuine bile salt (TLC), so
the inherited activity has been narrowed rather than lost, and the literature
states that whether TLC transport is ancestral or convergent cannot currently be
decided. The honest reading is therefore "retained but narrowed, and not the core
function" — i.e. `KEEP_AS_NON_CORE`, not `REMOVE`. What is wrong is only the
implication that this is what SOAT is *for*.

### Localization

Sorting studies place the protein at the plasma membrane
[PMID:37373074 "Sorting studies in transfected HEK293 cells clearly localized the
SOAT protein to the plasma membrane [1,13,35,36]."],
[PMID:28743544 "SOAT (gene name SLC10A6 in man and Slc10a6 in mice) is a plasma
membrane transporter for sulfated steroids, which is highly expressed in germ
cells of the testis."].
In placenta, SOAT is at the apical (maternal-facing microvillous) membrane of
syncytiotrophoblasts and in vessel endothelium
[PMID:24717977 "Immunohistochemical studies and in situ hybridization of formalin
fixed and paraffin embedded sections of human late term placenta showed expression
of SOAT in syncytiotrophoblasts, predominantly at the apical membrane as well as
in the vessel endothelium."].
All functional assays are uptake assays on intact cells, which independently
require the carrier to be in the plasma membrane. UniProt records only the generic
`Membrane` location (multi-pass), consistent with the IEA GO:0016020 row.

### Expression and physiology

Testis-dominant, with placenta and pancreas next
[PMID:17491011 "SOAT mRNA is most highly expressed in testis. Relatively high SOAT
expression was also detected in placenta and pancreas."]. In testis the protein is
in germ cells (zygotene/pachytene spermatocytes, round spermatids), and expression
is reduced in disorders of spermatogenesis
[PMID:23667501 "Only SOAT was significantly lower expressed in biopsies showing
hypospermatogenesis."].

The proposed physiological role is delivery of circulating, biologically inert
steroid sulfates into target cells for intracrine reactivation by steroid
sulfatase. Note that the knockout does **not** support a required role in
reproduction
[PMID:28743544 "However, the Slc10a6-/- knockout mice were fertile, produced
normal litter sizes, and had normal spermatogenesis and sperm vitality."], although
male knockouts have raised serum cholesterol sulfate
[PMID:28743544 "Interestingly, male Slc10a6-/- knockout mice showed significantly
higher serum levels for cholesterol sulfate compared to their wildtype controls."].
This is the reason no spermatogenesis or hormone-biosynthesis process term is
proposed here.

A disease-relevant consequence of the transport activity: SOAT expression renders
breast cancer cells responsive to estrone-3-sulfate
[PMID:30186172 "Hormone-dependent breast cancer T47D cells, stably transfected
with SOAT, showed significant proliferation after incubation with E1S at
physiologically relevant concentrations."]. This is a downstream consequence of substrate
uptake, not a separate SOAT activity, so it is not annotated.

### Protein interactions

SOAT homo- and heterodimerizes within the SLC10 family
[PMID:31256060 "Heterodimerization was observed for most of the SLC10 carrier
combinations."]. With NTCP it co-localizes and co-immunoprecipitates, but unlike
SLC10A4 it does not impair NTCP transport
[PMID:22029531 "SLC10A4 and SLC10A6 co-immunoprecipitated with NTCP, demonstrating
that heteromeric complexes can be formed between SLC10A family members in vitro."],
[PMID:22029531 "whereas expression of SLC10A6 or NTCP E257N, an inactive mutant,
did not affect NTCP function."].
This is targeted, informative interaction evidence — and it is not the source of
any GOA row. The 144 `GO:0005515 protein binding` rows all come from the HuRI
proteome-scale binary interactome map [PMID:32296183], give no functional
information, and are removed under the repository's generic-protein-binding
policy. Removal is not a claim that any interaction is false.

## Ontology work

Verified against OLS4 (`ols4/api/ontologies/go/terms/...`):

- `GO:0008508` bile acid:sodium symporter activity — current. Definition is the
  symport reaction `bile acid(out) + Na+(out) = bile acid(in) + Na+(in)`. Parents:
  `GO:0005343` organic acid:sodium symporter activity, `GO:0015125` bile acid
  transmembrane transporter activity, `GO:0015355` secondary active monocarboxylate
  transmembrane transporter activity. The monocarboxylate parentage is one reason
  this term cannot represent steroid-sulfate symport.
- `GO:0015721` bile acid and bile salt transport — current.
- `GO:0043251` sodium-dependent organic anion transport — current; sole parent
  `GO:0055085` transmembrane transport (so it is neither ancestor nor descendant of
  `GO:0015721`). This is the correct and best-available BP for SOAT.
- `GO:0043252` sodium-independent organic anion transport — current (not applicable).
- `GO:0015711` organic anion transport — **obsolete**.
- `GO:0008514` organic anion transmembrane transporter activity — **obsolete**,
  `term replaced by GO:0022857` transmembrane transporter activity (uninformative).
- `GO:0005886` plasma membrane, `GO:0016020` membrane — current.

**Gap:** there is no molecular-function term for sodium-coupled steroid-sulfate
symport. Searching GO via OLS for "steroid sulfate", "estrone sulfate" and
"organosulfate" returns only sulfotransferase/sulfatase activities and ChEBI
chemicals; the children of `GO:0015370` solute:sodium symporter activity cover
amino acids, sugars, nucleosides, bile acids, monocarboxylates, taurine,
ascorbate, inositol, choline and inorganic ions, with nothing for sulfate esters
of steroids. A new term `steroid sulfate:sodium symporter activity` under
`GO:0015370` is therefore proposed, and the core function uses
`proposed_molecular_function` rather than forcing `GO:0008508`.

## Review decisions

| Rows | Term | Evidence | Action |
|---|---|---|---|
| 144 | GO:0005515 protein binding | IPI (HuRI) | REMOVE (uninformative) |
| 1 | GO:0005886 plasma membrane | IBA GO_REF:0000033 | ACCEPT |
| 1 | GO:0005886 plasma membrane | TAS Reactome | ACCEPT |
| 1 | GO:0016020 membrane | IEA GO_REF:0000120 | ACCEPT |
| 1 | GO:0043251 sodium-dependent organic anion transport | IEA GO_REF:0000107 | ACCEPT (core) |
| 1 | GO:0008508 bile acid:sodium symporter activity | IBA GO_REF:0000033 | KEEP_AS_NON_CORE |
| 1 | GO:0008508 bile acid:sodium symporter activity | TAS Reactome:R-HSA-433089 | KEEP_AS_NON_CORE |
| 1 | GO:0015721 bile acid and bile salt transport | IBA GO_REF:0000033 | KEEP_AS_NON_CORE |
| 1 | GO:0015721 bile acid and bile salt transport | TAS Reactome:R-HSA-9958517 | KEEP_AS_NON_CORE |

No `NEW` annotation rows were added. The one genuine gap is a molecular function
with no GO term, which is raised as a `proposed_new_terms` entry instead.
