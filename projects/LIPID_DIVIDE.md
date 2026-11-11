---
title: "The Lipid Divide: enzymes that cross it"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [BACSU, ECOLI, METJA, METTH, AERPE, GEOSE, FLAJ1]
genes: [egsA, pcrB, plsY, plsC, gpsA, carS]
---

# The Lipid Divide: enzymes that cross it

**Bottom line:** The "lipid divide" is the textbook claim that Archaea build
membranes from isoprenoid chains ether-linked to *sn*-glycerol-1-phosphate
(G1P), while Bacteria and Eukarya use fatty acids ester-linked to
*sn*-glycerol-3-phosphate (G3P), and that the two cannot be mixed. A 2026
review by García-Domínguez and Devos [PMID:42965973] argues that the divide
is crossable. Bacteria with mixed lipids exist in at least eight phyla, the
"archaeal" enzymes are found in many bacteria, and mixed membranes are stable
in liposomes and in engineered *E. coli*. For GO, this matters because
annotation pipelines tend to treat the divide as a taxonomic rule: G1P and
isoprenoid-ether chemistry is read as archaeal, and G3P and fatty-acid ester
chemistry as bacterial. This project reviews the enzymes at the boundary,
the bacterial G1P and ether-lipid enzymes and the bacterial acyltransferases
that accept both glycerol-phosphate enantiomers, to see whether their GO
annotations describe what they actually do.

This project is a companion to [ARCHAEA](ARCHAEA.md), whose theme A6 covers
the archaeal ether-lipid pathway in *M. jannaschii* (GGGPS MJ1250, DGGGPS
MJ0279, CarS). Here the focus is the bacterial side and the enzymes found on
both sides.

## What the paper says

García-Domínguez R, Devos DP. *Prokaryotes bridging the lipid divide.* FEMS
Microbiol Rev 2026, doi:10.1093/femsre/fuag056 (PMID:42965973). Source: the
accepted manuscript PDF.

The divide has four separable parts: glycerol stereochemistry (G1P vs G3P),
hydrophobic chains (isoprenoid vs fatty acid), the linkage (ether vs ester),
and organisation (monolayer of membrane-spanning lipids vs bilayer). Every
one of the four has bacterial exceptions:

- **G1P backbone.** G1P lipids were detected in *Bacillus subtilis*,
  *B. amyloliquefaciens*, *Geobacillus stearothermophilus* and *Clavibacter
  michiganensis* (Palyzová et al. 2022). G1P dehydrogenase (G1PDH, EgsA/AraM)
  is found in Firmicutes, Actinomycetes, Planctomycetes and
  Deltaproteobacteria. In phylogenies of G1PDH the bacterial sequences branch
  basal to the archaeal ones, which argues against acquisition by lateral
  transfer from archaea (Peretó et al. 2004; Carbone et al. 2015).
- **Ether links.** Bacterial ether lipids occur in Thermotogae, Acidobacteria,
  *Aquifex*, Clostridia, sulfate reducers, *Rhodothermus*, anammox
  Planctomycetota and Myxococcota (*M. xanthus* ElbD, Lorenzen et al. 2014).
  FCB-group bacteria and *Ca.* Cloacimonadota MAGs carry an archaeal-type
  isoprenoid-ether pathway (Villanueva et al. 2021).
- **Membrane-spanning lipids (MSLs).** Bacteria in about ten phyla can make
  branched MSLs, and ether- and ester-linked MSLs have been found in
  Thermotogales, Acidobacteria and Bacillota (Sahonero-Canavesi et al. 2022,
  2026).
- **Isoprenoid chains.** Isoprenoid synthesis is universal, but the
  incorporation of isoprenoids into bacterial phospholipids is poorly
  established. No natural bacterium has a fully archaeal-type membrane.

The key mechanistic point for GO comes from Rieche et al. 2026
(PMID:42286214): the bacterial PlsY–PlsC pathway processes both G1P- and
G3P-derived substrates. If so, the supply of G1P, not the specificity of the
acyltransferases, limits heterochiral lipid production.

On the archaeal side, evidence for native bacterial-type lipids is weak.
Asgard G3P/ester lipid capacity is predicted from MAGs only, and the first
cultured Asgard archaeon has ordinary archaeal lipids (Imachi et al. 2020).
One Halobacteriota cardiolipin synthase makes ether, ester and mixed
cardiolipins (Exterkate et al. 2021).

The paper also reports:

- A Pfam/HMM presence–absence survey over 5,343 proteomes (Fig. 2). PlsY is
  common in Asgard (65 of 78 genomes), but a strict PlsC model finds no
  Asgard hits. Thermoplasmatota (Poseidoniia) often lack G1PDH and carry a
  bacterial-type G3PDH, and many Asgard and Halobacteriota genomes have
  neither enzyme, which implies unknown routes to G1P and/or G3P.
- Serinophospholipids in the verrucomicrobium *Limisphaera ngatamarikiensis*,
  with an (S)-serinol core equivalent to G1P and amide-linked fatty acids
  (Vyssotski et al. 2025). Their biosynthetic pathway is unknown.
- Mixed G1P/G3P liposomes are stable, and *E. coli* engineered to make up to
  30% archaeal-type lipid is viable.
- Evolutionary implications: one argument against a membrane-bound LUCA is
  removed, as is one argument for Archaea as a primary domain, and a lipid
  switch in Asgard-host eukaryogenesis models becomes plausible.

The paper's survey is presence/absence only and relies on HMM sensitivity.
The authors say themselves that lateral transfer cannot be excluded for most
mixed genes.

## Why this matters for GO annotation

1. **Taxon-shaped expectations.** Pipelines and curators may treat G1P,
   isoprenoid-ether chemistry as archaeal and decline or "correct" such
   annotations on bacterial proteins, or propagate them only within Archaea.
   We test this on the bacterial G1P and ether-lipid enzymes.
2. **Missing stereo-alternative MF terms.** GO has
   `GO:0043772` acyl-phosphate glycerol-3-phosphate acyltransferase activity
   (PlsY) and `GO:0003841` 1-acylglycerol-3-phosphate O-acyltransferase
   activity (PlsC). An OLS search found no G1P counterparts. Whether to propose
   them depends on whether G1P use is a physiological activity or substrate
   promiscuity, which is a judgement under the tiers in
   [ENZYME_SPECIFICITY](ENZYME_SPECIFICITY.md). Note that *B. subtilis* does
   make G1P lipids.
3. **No process terms for archaeal-type membrane lipids.** GO has
   `GO:0008611` ether lipid biosynthetic process. Its definition centres on
   a single ether-linked alcohol at C-1, and an OLS search found no terms for
   tetraether, GDGT or membrane-spanning lipid biosynthesis. Bacterial
   heptaprenylglyceryl phosphate synthase (PcrB) is annotated only to the
   generic `GO:0046474` glycerophospholipid biosynthetic process.
4. **Family-level mis-mappings, confirmed.** The *Flavobacterium johnsoniae*
   GGGPS (A5FJK8, an FCB bacterium with an experimentally supported
   GGGP synthase activity, EXP, PMID:24684232) also carried
   `GO:0000107` imidazoleglycerol-phosphate synthase activity by PANTHER IEA
   (PTN001846602). Checking the node confirmed the mis-mapping: the review
   removes the row and reports a `WRONG_TERM` defect to PANTHER. Shared
   TIM-barrel architecture is not shared catalysis, and TreeGrafter transferred
   the histidine-biosynthetic reaction across that divide.

## Review targets

All accessions were checked against UniProt REST, and every entry is reviewed
(Swiss-Prot). None of these genes has a review in this repository yet.

### Part A. Bacterial enzymes with "archaeal" chemistry

| Code | Gene | UniProt | Protein | Why |
|---|---|---|---|---|
| BACSU | egsA (araM) | P94527 | Glycerol-1-phosphate dehydrogenase [NAD(P)+] | Bacterial G1PDH; *B. subtilis* makes G1P lipids. GOA is IEA only. |
| GEOSE | egsA (araM) | B3EYN8 | Glycerol-1-phosphate dehydrogenase [NAD(P)+] | Second bacterial G1PDH from a species with G1P lipids |
| BACSU | pcrB | O34790 | Heptaprenylglyceryl phosphate synthase | Bacterial G1P–isoprenoid ether enzyme. IDA/EXP for `GO:0120536` |
| FLAJ1 | Fjoh_1584 | A5FJK8 | Geranylgeranylglyceryl phosphate synthase | FCB-group GGGPS (Villanueva et al. 2021 context); suspect `GO:0000107` row |

### Part B. Acyltransferases that accept both enantiomers

| Code | Gene | UniProt | Protein | Why |
|---|---|---|---|---|
| BACSU | plsY | Q45064 | Acyl-phosphate:G3P acyltransferase | Rieche et al. 2026 report G1P use. GOA is IBA/IEA only. |
| BACSU | plsC | O07584 | 1-acyl-G3P acyltransferase | Same paper; also check the IBA from eukaryotic AGPATs |
| ECOLI | plsY | P60782 | Acyl-phosphate:G3P acyltransferase | Host for engineered archaeal-lipid strains |
| ECOLI | plsC | P26647 | 1-acyl-G3P acyltransferase | As above |

### Part C. Archaeal reference enzymes (shared with ARCHAEA A6)

| Code | Gene | UniProt | Protein |
|---|---|---|---|
| METTH | egsA | P72010 | Glycerol-1-phosphate dehydrogenase (archaeal comparator) |
| AERPE | egsA | Q9YER2 | Glycerol-1-phosphate dehydrogenase (structural work, Carbone et al. 2015 lineage) |
| ECOLI | gpsA | P0A6S7 | Glycerol-3-phosphate dehydrogenase (G3P comparator) |
| METJA | carS | Q58995 | CDP-archaeol synthase (also listed in ARCHAEA A6) |

MJ1250 (GGGPS) and MJ0279 (DGGGPS) stay under ARCHAEA A6 and are not
repeated here.

### Deferred: enzymes without a reviewed entry

These are central to the paper but have no Swiss-Prot entry, or no accession
we could confirm, so they are not targets yet:

- Bacterial membrane-spanning lipid synthase (Mss) of Thermotogales and
  Acidobacteria (Sahonero-Canavesi et al. 2022), and the archaeal
  tetraether synthase Tes. Only unreviewed Tes entries were found.
- *Myxococcus xanthus* ElbD (Lorenzen et al. 2014). The MXAN locus tag
  for it has not been confirmed.
- The promiscuous archaeal cardiolipin synthase (Exterkate et al. 2021).
- *Ca.* Cloacimonadota ether-lipid genes (MAG-derived).

## Modules

Two modules have been built for this project:

- [bacterial_phosphatidic_acid_synthesis](../modules/bacterial_phosphatidic_acid_synthesis.yaml):
  the PlsX/PlsY and PlsB routes to lysophosphatidic acid, then PlsC to
  phosphatidic acid, ending where the CDP-DAG modules begin. The modelled
  chemistry stays G3P; the G1P capability of PlsY is a knowledge gap, confined
  to the PlsY branch because PlsB is strictly G3P-specific.
- [bacterial_heptaprenylglyceryl_ether_lipid](../modules/bacterial_heptaprenylglyceryl_ether_lipid.yaml):
  the archaeal-type ether lipid route of Bacillales. EgsA supplies G1P, PcrB
  forms the ether bond, an unassigned phosphatase and YvoF finish the carrier,
  and LhaT transfers its acetyl group to lipoproteins. The unassigned
  phosphatase and the unproven in vivo G1P supply are modelled as gaps rather
  than asserted.

## Plan

1. **Scoping (this page).** Done.
2. **Part A: done.** egsA and pcrB are reviewed and complete. Two reviewer
   critiques of the earlier draft plans were settled rather than carried over:
   egsA's `MODIFY` of `GO:0006650` is now grounded on the enzyme's ~170-fold
   kinetic bias toward DHAP reduction and on the GO convention shown by *E.
   coli* GpsA, not on the undemonstrated claim that EgsA supplies PcrB; and the
   planned `GO:0042158` row on pcrB was dropped, because PcrB contributes no
   atom to the modified lipoprotein and a comparator sweep over donor-making
   enzymes (FDPS, GGPS1, MAT2A, ACLY, bioB) shows none carries the term for the
   modification that consumes its product.
3. **Part B acyltransferases: done.** plsY and plsC are reviewed and complete.
   G1P use was recorded as a proposed term plus knowledge gaps, not as a
   function: the near-equal in vitro result is from detergent, PlsY prefers G3P
   in a membrane, no kinetics exist, and the in vivo G1P source is unidentified.
4. **A5FJK8 `GO:0000107`: done, and the suspicion was right.** The
   [Fjoh_1584](../genes/FLAJ1/Fjoh_1584/Fjoh_1584-ai-review.yaml) review removes
   the row and records a `WRONG_TERM` source defect against
   `PANTHER:PTN001846602`. The TreeGrafter node transfers the glutamine-dependent
   histidine-biosynthetic reaction across divergent TIM-barrel activities, while
   the curated FUNCTION evidence on this protein specifies GGGPS chemistry.
5. **Ontology questions** for GO, now four: an `sn`-glycerol 1-phosphate
   biosynthetic process term (GO has `GO:0046167` for the G3P enantiomer only);
   process terms for archaeal-type (isoprenoid ether, G1P) and for
   membrane-spanning (GDGT, brGDGT, iso-diabolic acid) lipid biosynthesis;
   whether `GO:0008611`'s C-1 wording should be clarified, since pcrB's row is
   its first prokaryotic use; and whether excluding carrier- and
   donor-synthesising enzymes from the process terms they feed is deliberate
   practice, given that UppS and human/DPM1 are annotated the other way.
6. **Modules: two built** (above). A G1P/G3P backbone-choice module could
   still link the bacterial and archaeal halves once both sides are reviewed.
7. **Follow-ups from the modules.** YvoF (O34993) and LhaT/YpjA (P54392) are
   both reviewed and complete, so the ether-lipid module's four assigned steps
   now all have gene reviews behind them. Bacterial CdsA (PA to CDP-DAG) remains
   the open item: it is the single reaction joining
   [bacterial_phosphatidic_acid_synthesis](../modules/bacterial_phosphatidic_acid_synthesis.yaml)
   to the CDP-DAG modules, and had no bacterial gene review anywhere in the
   repository.

## Open questions

- **Settled by the pcrB review:** `GO:0008611`'s definition centres the ether
  linkage on C-1, while HepGP's is on C-3 of G1P. The objection dissolves: C-3
  is the carbon distal to the phosphate, the same physical position as C-1 in
  the mirror-image G3P numbering used for plasmalogens, and the number differs
  only because `sn` numbering is fixed by backbone stereochemistry. The
  definition's two "normally" hedges cover it, so no new term is needed for
  ether-bond formation as such.

- Is G1P acylation by PlsY/PlsC a physiological activity in *B. subtilis*,
  where G1P lipids occur, or only in vitro promiscuity?
- Does GO want separate MF terms for the G1P-using reactions, or broader
  stereo-neutral parent terms?
- How do PAINT nodes for G1PDH (and for GGGPS/PcrB) handle the bacterial
  members? Is the function placed at a node that includes both domains?
