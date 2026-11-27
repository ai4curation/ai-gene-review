# PSY (PSY1, At5g17230, UniProt P37271) - research notes

Arabidopsis thaliana phytoene synthase 1, chloroplastic. Single-copy PSY in
Arabidopsis; EC 2.5.1.32; module exemplar in
`modules/carotene_backbone_biosynthesis.yaml` (part 1, `psy_activity`,
PANTHER:PTHR31480).

## 1. Identity and what UniProt says

- Precursor of 422 aa with a predicted chloroplast transit peptide 1-70
  [file:ARATH/PSY/PSY-uniprot.txt "TRANSIT 1..70 /note=\"Chloroplast\""].
- Function: "Catalyzes the reaction from prephytoene diphosphate to phytoene"
  (evidence PubMed:25675505) [file:ARATH/PSY/PSY-uniprot.txt].
- Catalytic activities (all ECO:0000269|PubMed:25675505): overall
  RHEA:34475 (2 GGPP = 15-cis-phytoene + 2 diphosphate, EC 2.5.1.32); half
  reactions RHEA:22296 (2 GGPP -> prephytoene diphosphate + PPi) and
  RHEA:34479 (prephytoene diphosphate -> 15-cis-phytoene + PPi)
  [file:ARATH/PSY/PSY-uniprot.txt "Xref=Rhea:RHEA:34475, ChEBI:CHEBI:27787,"].
- Subunit: monomer (by similarity); interacts with OR (PubMed:25675505,
  PubMed:26224804) and ORLIKE (PubMed:25675505).
- Subcellular location: "Plastid, chloroplast membrane"; peripheral membrane
  protein [file:ARATH/PSY/PSY-uniprot.txt "SUBCELLULAR LOCATION: Plastid,
  chloroplast membrane"].
- Family: "Belongs to the phytoene/squalene synthase family."
  InterPro: IPR002060 Squalene/phytoene synthase (family), IPR019845
  Squalene/phytoene synthase conserved site, IPR033904 Trans-isoprenyl
  diphosphate synthases head-to-head (domain), IPR044843 Trans-isoprenyl
  diphosphate synthases bacterial-type (family), IPR008949 isoprenoid
  synthase domain superfamily. PANTHER PTHR31480 "BIFUNCTIONAL LYCOPENE
  CYCLASE/PHYTOENE SYNTHASE" (family name dominated by the fungal
  bifunctional members; plant PSY is single-domain).
- Original cDNA: Scolnik & Bartley 1994 [PMID:8016277 "Nucleotide sequence of
  an Arabidopsis cDNA for phytoene synthase."] - cached record is title-only
  (no abstract text available), so it can only be cited for the cloning.

## 2. Cached publications: what each actually shows

### PMID:25675505 (Zhou et al. 2015 PNAS) - full text available

The key experimental paper behind the IDA rows (GO:0046905, GO:0016117,
GO:0009507) and the IPI rows (protein binding with OR Q8VYD8 and OR-like
Q9FKF4).

- Pathway position: [PMID:25675505 "Phytoene synthase (PSY) catalyzes the
  first committed step in carotenoid biosynthesis and controls carbon flux
  into the carotenoid biosynthetic pathway"].
- Localization: PSY identified as an OR co-IP partner; [PMID:25675505 "Among
  these proteins, PSY was the only one exclusively localized in chloroplasts
  as shown in a previous report ( 27 ) and the current study ( SI Appendix ,
  Fig. S1 )."]; BiFC of OR-PSY: [PMID:25675505 "Such interactions occurred in
  chloroplasts, which was in good agreement with the plastid localization of
  these proteins ( 27 ) ( SI Appendix , Fig. S1 )."].
- Direct enzyme assay on isolated Arabidopsis chloroplast membranes:
  [PMID:25675505 "PSY activity was about 50% higher in the AtOR
  -overexpressing lines than in WT."]. The assay design is itself informative
  for the InterPro-derived GGPP synthase row: [PMID:25675505 "Here PSY
  activity was exclusively found membrane bound and required addition of
  active GGPP synthase for in vitro assay."] - i.e. PSY does not itself make
  GGPP.
- In vivo activity: [PMID:25675505 "Overexpression of PSY – GFP led to about a
  twofold increase of phytoene in NFZ-treated etiolated seedlings ( Fig. 4 C
  ), indicating that PSY – GFP functioned properly in the transgenic lines."].
- Interaction: split-ubiquitin Y2H, co-IP in N. benthamiana, BiFC:
  [PMID:25675505 "Both Arabidopsis OR proteins interacted directly with PSY (
  Fig. 1 A )."]; OR/OR-like control PSY protein abundance post-
  transcriptionally: [PMID:25675505 "The results indicated that AtOR and
  AtOR-like were sufficient and required to regulate PSY protein levels in
  vivo, and that AtOR and AtOR-like were functionally redundant."].
- The paper explicitly declines to call OR a chaperone: [PMID:25675505
  "Although the OR proteins carry a DnaJ cysteine-rich zinc figure domain,
  they are not molecular chaperones due to the lack of the DnaJ-like defining
  J domain."] - so GO:0051087 chaperone binding is NOT supported by this paper
  as a MODIFY target for the protein-binding rows.

### PMID:26224804 (Yuan et al. 2015 Plant Physiol) - fetched this session, full text

Cited by UniProt for interaction with OR and subcellular location. Confirms
AtOR(His) variant also interacts with PSY by BiFC: [PMID:26224804 "Such
interactions occurred in chloroplasts, consistent with the plastidial
localizations of these proteins"]. Pathway statement: [PMID:26224804 "The
first committed step in the carotenoid biosynthesis pathway is the
condensation of two geranylgeranyl diphosphate molecules to phytoene catalyzed
by phytoene synthase (PSY)."]. Not in GOA; used as a corroborating reference.

### PMID:37966976 (Iglesias-Sanchez et al. 2024 Plant Physiol) - full text available

Behind the IPI (protein binding with FBN6, AT5G19940) and IDA chloroplast rows.

- Interaction: FBN6 pulled down with PSY-GFP (Welsch et al. 2018), confirmed by
  co-IP in N. benthamiana; [PMID:37966976 "Arabidopsis FBN6 was found to be
  among the proteins co-immunoprecipitated with a GFP-tagged version of
  phytoene synthase (PSY), the first and main rate-determining enzyme of the
  carotenoid pathway (Welsch et al. 2018)."].
- Localization: [PMID:37966976 "When analyzing the co-immunoprecipitation
  assays, we noticed that the PSY-GFP protein concentrated in fluorescent dots
  within chloroplasts (Fig. 2A)."]; [PMID:37966976 "indicating that FBN6 and
  PSY co-localize within chloroplasts, as expected for interacting
  proteins."]. Importantly the paper notes that FBN6 is NOT a plastoglobule
  protein but is in thylakoid and envelope membranes, and that PSY is found in
  envelope proteomes: [PMID:37966976 "FBN6 is the only FBN enriched in purified
  envelope fractions where PSY is also found (Ferro et al. 2010; Bouchnak et
  al. 2019)."]. This bears on the plastoglobule IDA (below).
- FBN6 stimulates plant PSY catalysis without changing PSY amount:
  [PMID:37966976 "Strains co-transformed with such constructs harboring
  Arabidopsis PSY and FBN6 sequences were found to produce significantly more
  β-carotene than those expressing only PSY or co-expressing PSY and FBN4
  (Fig. 3, B and C), despite that PSY protein levels remained very similar in
  all the cases (Fig. 3D)."]; in planta [PMID:37966976 "While phytoene was not
  detected in control or FBN6 samples, it was present in PSY samples, and it
  increased in samples agroinfiltrated with both FBN6 and PSY (Fig. 4A)."].
  Conclusion: [PMID:37966976 "our data support the conclusion that FBN6 plays
  a physiologically relevant role in carotenoid biosynthesis in Arabidopsis
  chloroplasts by physically binding to PSY to promote its enzymatic
  activity."].
- The E. coli complementation (pAC-85b lacking crtB, rescued by His-tagged
  Arabidopsis PSY lacking its transit peptide) is an independent demonstration
  that P37271 has phytoene synthase activity.

### PMID:23023170 (Shumskaya et al. 2012 Plant Cell) - full text available

Behind the plastoglobule IDA (GO:0010287).

- Method: transient expression of fluorescent-protein fusions in leaf
  protoplasts; At-PSY-RFP was expressed in cowpea (dicot) protoplasts, i.e. a
  heterologous host, not Arabidopsis. [PMID:23023170 "Arabidopsis has only one
  At-PSY."].
- Result: [PMID:23023170 "These PSYs localized to chloroplasts in specific
  fixed speckles, distributed inside the plastid and attached to areas that
  displayed red chlorophyll fluorescence indicative of prolamellar bodies or
  thylakoids."]; speckles identified as plastoglobuli by colocalization with a
  maize fibrillin (shown directly for Zm-PSY2/3): [PMID:23023170 "Merging of
  both signals confirmed colocalization of PSYs with Zm-PG2; thus, we consider
  the speckles to be plastoglobuli."]; the authors extend the conclusion to
  Arabidopsis: [PMID:23023170 "Arabidopsis PSY localized to plastoglobules (as
  did maize PSY2 and 3 and rice PSY1, 2, and 3)."].
- Caveat recorded by the authors themselves: [PMID:23023170 "Chloroplast
  suborganellar localization of the key pathway enzyme, PSY , has yet to be
  detected by proteomic analysis."].
- Assessment: genuine IDA, but from overexpressed fusion protein in a
  heterologous protoplast; the FBN6 paper shows an identical punctate pattern
  for a partner that proteomics places in envelope/thylakoid membranes rather
  than plastoglobules, and envelope proteomics detects PSY. I therefore keep
  the plastoglobule row but as non-core, and treat "chloroplast membrane"
  (envelope / thylakoid-associated, peripheral) as the functional location.
  The sub-plastid site is a genuine open question (see suggested_questions).

### PMID:12805607 (Lindgren et al. 2003 Plant Physiol) - full text available

Behind the IMP GO:0016117 and TAS GO:0046905 rows.

- The gene overexpressed is the endogenous Arabidopsis PSY cloned by RT-PCR
  homologous to the Scolnik & Bartley cDNA, i.e. At5g17230/P37271:
  [PMID:12805607 "An endogenous phytoene synthase was sequenced and cloned by
  RT-PCR from Arabidopsis homologous to the gene cloned by Scolnik and Bartley
  ( 1994 )."].
- TAS statement: [PMID:12805607 "Phytoene synthase catalyzes the dimerization
  of two molecules of geranylgeranyl pyrophosphate to phytoene and has been
  shown to be rate limiting for the synthesis of carotenoids."].
- Phenotype (napA seed-specific overexpression): 43-fold beta-carotene,
  increased lutein, violaxanthin, lycopene, alpha-carotene, chlorophyll, ABA;
  delayed germination [PMID:12805607 "In the present paper, we show that
  seed-specific overexpression of an endogenous Arabidopsis phytoene synthase
  gene results in significant increases of the levels of β-carotene, luteins,
  and violaxanthin."]. Gain-of-function rather than loss-of-function, but a
  clean demonstration that PSY flux drives carotenoid biosynthesis in planta.
  The germination/ABA effects are downstream consequences (xanthophyll ->
  ABA) and are not annotated to PSY; I do not propose them.

### PMID:18431481 (Zybailov et al. 2008 PLoS One) - full text available

Behind the HDA chloroplast row. Large-scale chloroplast proteome
[PMID:18431481 "which unambiguously identified 1325 proteins"]. The cached
text (main body) does not name At5g17230; the identification list is in
supplementary tables not in the cache. The HDA is consistent with all direct
evidence, so ACCEPT, deferring to the TAIR curator for the table entry.

## 3. GO_REF / electronic rows

- GO_REF:0000002 InterPro2GO:
  - IPR044843 "Trans-isoprenyl diphosphate synthases, bacterial-type" ->
    GO:0004311 GGPP synthase activity. Verified on the InterPro API this
    session: the entry's GO mapping is GO:0004311. PSY consumes GGPP
    (head-to-head condensation of two C20 units); it does not perform the
    head-to-tail FPP + IPP -> GGPP elongation. Direct experimental argument:
    the Arabidopsis PSY assay required exogenous GGPP synthase
    [PMID:25675505 "required addition of active GGPP synthase for in vitro
    assay"]. REMOVE.
  - IPR033904 "Trans-isoprenyl diphosphate synthases, head-to-head" ->
    GO:0051996 squalene synthase [NAD(P)H] activity. The domain is shared by
    squalene synthase and phytoene synthase (same fold, same head-to-head
    chemistry), but squalene synthase condenses two FPP and reduces the
    presqualene intermediate with NAD(P)H; PSY condenses two GGPP and releases
    phytoene without a reductive step (RHEA:34475 has no NAD(P)H). The mapping
    assigns the paralog's activity. REMOVE.
  - IPR019845 "Squalene/phytoene synthase, conserved site" -> GO:0016765
    transferase activity, transferring alkyl or aryl (other than methyl)
    groups. Correct parent of EC 2.5.1.32 (GO:0046905). KEEP_AS_NON_CORE as a
    generic grandparent.
- GO_REF:0000033 IBA (PANTHER:PTN000770577): GO:0046905 and GO:0016117.
  The target AT5G17230 appears in its own WITH/FROM, which is expected (its
  IDA is one of the descendant evidences for the IBD). Donors include the
  Neurospora al-2 P37295, Synechococcus/cyanobacterial and plant PSYs. Node
  placement is sound: phytoene synthase activity is the ancestral function of
  the CrtB/PSY family. ACCEPT both.
- GO_REF:0000108 inter-ontology inference: GO:0046905 -> GO:0016120 carotene
  biosynthetic process. Phytoene is a C40 hydrocarbon carotene, so this is
  correct. Note (per brief): GO:0016120 is not currently a descendant of
  GO:0016117; GO:1901174 phytoene biosynthetic process IS a descendant of
  GO:0016120 (checked via QuickGO ancestors this session) and is the most
  precise process for core_functions. Not proposed as NEW because it is a
  descendant of a carried term (redundancy rule).
- GO_REF:0000120 (ARBA00027384 / RHEA:34475 / EC 2.5.1.32) -> GO:0046905:
  correct. ACCEPT.
- GO_REF:0000044 UniProt SubCell SL-0053 -> GO:0031969 chloroplast membrane:
  matches UniProt "Plastid, chloroplast membrane; Peripheral membrane
  protein" and the membrane-bound activity in PMID:25675505. ACCEPT.
- GO_REF:0000122 AtSubP -> GO:0009507 chloroplast: sequence-based prediction
  consistent with the transit peptide and with all IDA evidence. ACCEPT.

## 4. Protein-binding rows (GO:0005515)

Three IPI rows (OR, OR-like, FBN6). All three interactions are real and
biologically important, but on the PSY side they describe PSY being
regulated (stabilised by OR/OR-like; catalytically stimulated by FBN6). No
more informative MF for PSY is supported: the OR paper explicitly says OR is
not a molecular chaperone, so "chaperone binding" is not licensed, and there
is no GO MF for "being an activated enzyme". Per policy: REMOVE as
uninformative; the informative annotations belong on OR/OR-like and FBN6
(enzyme regulator / activator side). Removal does not deny the interactions.

## 5. Deep research report (retrieval support only)

`PSY-deep-research-falcon.md` points to additional non-GOA literature I did
not cache: Alvarez et al. 2016 (5'UTR splice variants controlling PSY
translation), Welsch et al. 2018 (Clp protease and OR control PSY
proteostasis; PSY-GFP co-IP that first found FBN6), Maass et al. 2009
(constitutive AtPSY overexpression: leaves unchanged, roots/callus with
carotenoid crystals), Zhou et al. 2022 review, and a 2023 preprint on
hypomorphic PSY variants and a cis-carotene-derived signal. None of these
are used for identifiers or quotes here; they inform the description and the
suggested questions.

## 6. Decisions summary

| Term | Evidence | Action |
|---|---|---|
| GO:0004311 GGPP synthase activity | IEA IPR044843 | REMOVE |
| GO:0005515 protein binding (OR) | IPI 25675505 | REMOVE |
| GO:0005515 protein binding (OR-like) | IPI 25675505 | REMOVE |
| GO:0005515 protein binding (FBN6) | IPI 37966976 | REMOVE |
| GO:0009507 chloroplast | HDA 18431481 | ACCEPT |
| GO:0009507 chloroplast | IDA 25675505 | ACCEPT |
| GO:0009507 chloroplast | IDA 37966976 | ACCEPT |
| GO:0009507 chloroplast | ISM GO_REF:0000122 | ACCEPT |
| GO:0010287 plastoglobule | IDA 23023170 | KEEP_AS_NON_CORE |
| GO:0016117 carotenoid biosynthetic process | IBA | ACCEPT |
| GO:0016117 carotenoid biosynthetic process | IDA 25675505 | ACCEPT |
| GO:0016117 carotenoid biosynthetic process | IMP 12805607 | ACCEPT |
| GO:0016120 carotene biosynthetic process | IEA GO_REF:0000108 | ACCEPT |
| GO:0016765 transferase (alkyl/aryl) | IEA IPR019845 | KEEP_AS_NON_CORE |
| GO:0031969 chloroplast membrane | IEA GO_REF:0000044 | ACCEPT |
| GO:0046905 15-cis-phytoene synthase activity | IBA | ACCEPT |
| GO:0046905 15-cis-phytoene synthase activity | IDA 25675505 | ACCEPT |
| GO:0046905 15-cis-phytoene synthase activity | IEA GO_REF:0000120 | ACCEPT |
| GO:0046905 15-cis-phytoene synthase activity | TAS 12805607 | ACCEPT |
| GO:0051996 squalene synthase [NAD(P)H] activity | IEA IPR033904 | REMOVE |

No NEW annotations proposed. GO:1901174 phytoene biosynthetic process (a
descendant of the carried GO:0016120) is the most precise process term, but per
the redundancy rule it is neither proposed as NEW nor placed in core_functions;
core_functions uses the two carried process terms GO:0016117 and GO:0016120 and
names phytoene biosynthesis in its description.
