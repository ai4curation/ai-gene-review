# TRAF3 (Q13114) — curation notes

Working journal for the TRAF3 GO annotation review. Provenance is recorded inline as
`[PMID:xxxx "verbatim supporting text"]`. Quotes are taken from the cached records in
`publications/`; where only an abstract is cached this is noted.

## 1. Identity and architecture

- UniProt `Q13114`, `TRAF3_HUMAN`, 568 aa, HGNC:12033. EC 2.3.2.27 (RING-type E3 ubiquitin
  transferase) with `ECO:0000269|PubMed:25847972`.
- Historical names reflect its discovery as a CD40-tail binder: CRAF1, CD40BP/CAP-1, and
  LAP1 (LMP1-associated protein 1).
- Domain layout (UniProt): N-terminal RING-type zinc finger, several TRAF-type zinc fingers,
  a coiled-coil (TRAF-N) region, and a C-terminal MATH/TRAF-C domain.
  `DOMAIN: The MATH/TRAF domain binds to receptor cytoplasmic domains.`
  `DOMAIN: The Ring-type zinc finger domain is required for its function in down-regulation
  of NFKB2 proteolytic processing.`
- Two annotated isoforms: Q13114-1 (canonical) and Q13114-2 (VSP_040040). No isoform-specific
  GO annotations are present in GOA, and none of the literature reviewed here assigns a
  distinct function to isoform 2.

The two original cloning papers already establish the adaptor architecture:

- [PMID:7527023 "One such interacting protein, designated CD40-binding protein, has a
  N-terminal RING finger motif that is found in a number of DNA-binding proteins, including
  the V(D)J recombination activating gene RAG1."] (abstract only)
- [PMID:7530216 "The CAP-1 protein contains a C-terminal domain that shares strong amino acid
  sequence homology with a unique domain found recently in two putative signal transducing
  proteins that bind to the TNF-R2 cytosolic tail, TRAF1 and TRAF2."] (abstract only)

Quaternary structure: TRAF3 homotrimerises and also forms heterotrimers with TRAF2/TRAF5.
[PMID:15383523 "A novel flow cytometric FRET analysis utilizing a two-step approach to achieve
linked FRET from CFP to YFP to HcRed established that TRAF2 and -3 constitutively form homo-
and heterotrimers."] (abstract only)

## 2. Two opposite-sign core roles

TRAF3 is unusual among TRAFs in being a *negative* regulator of one NF-κB branch and a
*positive* regulator of the type I interferon branch. Both are strongly supported.

### 2.1 Constitutive brake on non-canonical NF-κB (NIK/MAP3K14 turnover)

This is the best-established TRAF3 function and it is **absent from the current GOA set**.

- TRAF3 binds NIK and targets it for proteasomal degradation:
  [PMID:15084608 "TRAF3 physically associates with NIK via a specific sequence motif located
  in the N-terminal region of NIK; this molecular interaction appears to target NIK for
  degradation by the proteasome."] (abstract only)
- The brake operates inside a TRAF2–TRAF3–cIAP1/2 assembly, with TRAF3 supplying NIK
  recruitment and TRAF2 supplying the cIAPs:
  [PMID:18997794 "we demonstrated that the degradation of NIK occurs upon assembly of a
  regulatory complex through TRAF3 recruitment of NIK and TRAF2 recruitment of cIAP1 and
  cIAP2."]
  Note the same paper shows the genetic epistasis: `the lethality of TRAF3 deficiency in mice
  could be rescued by a single NIK gene`.
- The complementary study reaches the same architecture from the TRAF2 side
  (PMID:18997792, "Nonredundant and complementary functions of TRAF2 and TRAF3 in a
  ubiquitination cascade that activates NIK-dependent alternative NF-kappaB signaling").
- TRAF3 also restrains **canonical** NF-κB downstream of LTβR, and its loss de-represses
  the non-canonical pathway autonomously:
  [PMID:20185819 "TRAF3 knock-down also increased mRNA and protein expression of several
  non-canonical NFkappaB components, including NFkappaB2/p100, RelB, and NIK, accompanied by
  processing of NFkappaB2/p100 into p52. These effects of TRAF3 depletion did not require
  LTBR signaling and were consistent with autonomous activation of the non-canonical NFkappaB
  pathway."]
- Loss-of-function of TRAF3 is a recurrent, selected event in multiple myeloma, exactly as
  expected for a constitutive brake on this pathway (PMID:17692805, "Promiscuous mutations
  activate the noncanonical NF-kappaB pathway in multiple myeloma").
- UniProt states the same: `Also acts as a constitutive negative regulator of the alternative
  NF-kappa-B pathway, which controls B-cell survival and lymphoid organ development.` and
  `Promotes ubiquitination and proteasomal degradation of MAP3K14.`

Curation consequence: propose **GO:1901223 negative regulation of non-canonical NF-kappaB
signal transduction** and **GO:0043161 proteasome-mediated ubiquitin-dependent protein
catabolic process** as NEW annotations. The existing GO:0030162 (regulation of proteolysis,
IMP from PMID:20185819) is the vague shadow of this.

### 2.2 Positive, non-redundant driver of type I interferon induction

- TRAF3 is required for IFN induction by several TLRs and by cytosolic virus sensing, and it
  bridges TLR adaptors to the IRF kinases:
  [PMID:16306936 "we show that TRAF3 associates with the TLR adaptors TRIF and IRAK1, as well
  as downstream IRF3/7 kinases TBK1 and IKK-epsilon, suggesting that TRAF3 serves as a
  critical link between TLR adaptors and downstream regulatory kinases important for IRF
  activation."] (abstract only)
- The division of labour with TRAF6 is explicit, and gives the TRIF/TBK1 mechanism:
  [PMID:16306937 "TRAF3 is also recruited to the adaptor TRIF (Toll/IL-1 receptor
  domain-containing adaptor-inducing IFN-beta) and is required for marshalling the protein
  kinase TBK1 (also called NAK) into TIR signalling complexes, thereby explaining its unique
  role in activation of the IFN response."] (abstract only)
- On the RLR arm, TRAF3 is recruited to mitochondrial MAVS through a TRAF-interacting motif,
  and this contact is required:
  [PMID:16858409 "Cardif-mediated IFNalpha induction occurs through a direct interaction
  between the TRAF domain of TRAF3 and a TRAF-interaction motif (TIM) within Cardif."]
  and [PMID:21200404 "A consensus TRAF-interacting motif (TIM), 455-PEENEY-460, within this
  site is required for TRAF3 binding and activation of IFN antiviral response genes, whereas
  mutation of the TIM eliminates TRAF3 binding and the downstream IFN response."]
- Human genetics confirms non-redundancy in vivo:
  [PMID:20832341 "TRAF3 deficiency is associated with a clinical phenotype limited to HSE
  resulting from the impairment of TLR3-dependent induction of IFN."]
  UniProt records this as Immunodeficiency 132A (MIM:614849), with a second, distinct
  dominant disorder IMD132B (MIM:621096).
  Note the mechanism is **dominant-negative, not haploinsufficiency**: the paper's own
  results section is headed "The TRAF3 mutant allele is dominant-negative", and patient
  cells retain [PMID:20832341 "only about 17.5% the amount of TRAF3 present in controls"] -
  well below the ~50% a null allele would leave - because R118W destabilises the product of
  the wild-type allele through heterotrimer formation
  [PMID:20832341 "although the R118W allele is a loss-of-expression allele, it may exert a
  dominant-negative effect, by destabilizing proteins produced from the WT allele"].

### 2.3 The ubiquitin switch that separates the two outputs

The sign of TRAF3's output is set by which chain type it carries:

[PMID:19898473 "Degradative ubiquitination of TRAF3 during MyD88-dependent TLR signaling was
essential for the activation of mitogen-activated protein kinases (MAPKs) and production of
inflammatory cytokines. In contrast, TRIF-dependent signaling triggered noncanonical TRAF3
self-ubiquitination that activated the interferon response."]

Upstream and downstream of that switch:

- cIAP1/2 place the degradative marks: [PMID:20097753 "we demonstrated that cIAP1- and
  cIAP2-mediated virus-triggered ubiquitination of TRAF3 and TRAF6."]
- DUBA removes the activating K63 chains: [PMID:17991829 "DUBA selectively cleaved the
  lysine-63-linked polyubiquitin chains on TRAF3, resulting in its dissociation from the
  downstream signaling complex containing TANK-binding kinase 1."] Note this abstract also
  states directly: `TRAF3 is an E3 ubiquitin ligase that preferentially assembled
  lysine-63-linked polyubiquitin chains.`
- PTPN22 promotes the activating marks: [PMID:23871208 "PTPN22 directly associated with TNF
  receptor-associated factor 3 (TRAF3) and promotes TRAF3 lysine 63-linked ubiquitination."]
- DDX3 scaffolds two successive K63 waves on TRAF3 downstream of MAVS:
  [PMID:27980081 "Interestingly, we observed two waves of K63-linked TRAF3 ubiquitination
  following RIG-I activation by Sendai virus (SeV) infection, both of which were suppressed by
  DDX3 knockdown."]
- Triad3A/RNF216 imposes the K48 off-switch: [PMID:19893624 "we demonstrate that Triad3A
  negatively regulates the RIG-I RNA sensing pathway through Lys48-linked, ubiquitin-mediated
  degradation of the tumor necrosis factor receptor-associated factor 3 (TRAF3) adapter."]
- NEDD4L and FBXO11 add further, non-degradative marks
  (PMID:33608556 K29-linked; PMID:36897010 K63-linked, NEDD8-dependent).
- ATP1B1 and TRIM35 are positive regulators acting through TRAF3 ubiquitination
  (PMID:34011520; PMID:32562145).

Most of this is *TRAF3 as substrate*, not TRAF3 as enzyme, and should not be mistaken for
TRAF3 molecular function during curation.

### 2.4 TRAF3 as enzyme: direct substrates

The clearest direct-substrate evidence is ASC:

[PMID:25847972 "In particular, TNFR-associated factor 3 was found to be a direct E3 ligase for
ASC. Ubiquitination of ASC at Lys(174) was critical for speck formation and inflammasome
activation."] (abstract only; this is the EC 2.3.2.27 evidence in UniProt)

Plus TRAF3 self-ubiquitination (PMID:19898473, above) and the NIK degradation route
(§2.1). Supports **GO:0070534 protein K63-linked ubiquitination** as a NEW annotation.

## 3. Receptors and localisation

- Receptor engagement is via the MATH/TRAF-C domain, to CD40 (the founding interaction,
  PMID:7527023, PMID:7530216), LTβR, BAFF-R, BCMA, OX40, CD30, EDAR, and the EBV oncoprotein
  LMP1. Fn14/TweakR also recruits it: [PMID:11728344 "The TweakR cytoplasmic domain binds
  TRAFs 1, 2, and 3."] (abstract only)
- LIGHT–LTβR death signalling is TRAF3-dependent: [PMID:10799510 "LTbetaR, not HveA, recruits
  TNF receptor-associated factor-3 (TRAF3), and LIGHT-induced death is blocked by a dominant
  negative TRAF3 mutant."] (abstract only; dominant-negative evidence, so an indirect,
  context-restricted claim on apoptosis).
- Endosomal pool on the TLR4/TRAM route: [PMID:18222170 "The internalized signaling complex
  consisting of TLR4 and TRAM colocalizes with TRAF3, a signaling molecule downstream of TRIF,
  in endosome/lysosome."] (abstract only)
- Mitochondrial pool: via MAVS (PMID:16858409, PMID:21200404) and co-localisation with TRIM35
  (PMID:32562145). UniProt: `Mitochondrion {ECO:0000269|PubMed:32562145}` and `Co-localized to
  mitochondria with TRIM35`.
- A K33-linked mark connects TRAF3 to vesicle trafficking:
  [PMID:27438768 "Toll-like receptor (TLR) 4 signals emanating from bacteria-containing
  vesicles (BCVs) were found to trigger K33-linked polyubiquitination of TRAF3 at Lys168,
  which was then detected by RalGDS, a guanine nucleotide exchange factor (GEF) that
  precipitated the assembly of the exocyst complex."] This is real but narrow (bladder
  epithelial cells, bacterial expulsion) — non-core.

## 4. Notes on specific GOA rows

Points where the review departs from GOA, with the reasoning:

- **GO:0008063 "Toll signaling pathway" (IEA, InterPro2GO).** The GO definition is the
  *Drosophila* Toll receptor pathway: "The series of molecular signals initiated by an
  extracellular ligand binding to the receptor Toll on the surface of a target cell". Human
  TRAF3 acts in TLR pathways; MODIFY to GO:0002224.
- **GO:0060337 "type I interferon-mediated signaling pathway" (NAS, PMID:25847972).** Defined
  as signalling *initiated by type I interferon binding to its receptor*. TRAF3 acts upstream,
  on IFN *production*; the correct term (GO:0032481) is already annotated. REMOVE.
- **GO:0016020 "membrane" (IEA, ARBA).** TRAF3 has no TM segment; it is a cytosolic protein
  transiently recruited to membrane-proximal complexes, which GO:0009898 and GO:0010008
  already capture precisely. REMOVE.
- **GO:0005739 "mitochondrion" IDA anchored to PMID:19898473.** The cached full text of
  Tseng et al. (73 kB, `full_text_available: true`) contains no occurrence of "mitochond".
  The *term* is nevertheless correct and independently supported (PMID:32562145 EXP;
  PMID:16858409 IC via MAVS), so the term is accepted and the citation discrepancy is recorded
  in that row's `reason` rather than by deleting an experimental annotation whose figures and
  supplement are not in the cache.
- **GO:0004842 "ubiquitin-protein transferase activity" (2× Reactome TAS, 1× IDA).** Parent of
  GO:0061630, which is annotated from the same evidence. MODIFY to GO:0061630.
- **GO:0007166 "cell surface receptor signaling pathway" (IBA) is left as ACCEPT, not
  narrowed.** The first draft of this review proposed GO:0023035 (CD40 signaling pathway) as
  a replacement. That is wrong for an IBA: the row's WITH set is
  `FB:FBgn0265464|MGI:...|RGD:...|UniProtKB:O00463|UniProtKB:Q12933|UniProtKB:Q9Y4K3`, i.e.
  it spans *Drosophila* and TRAF2/TRAF5/TRAF6, and CD40 is vertebrate-specific — so a CD40
  pathway term cannot be what is conserved across that PANTHER clade. The broad term is the
  phylogenetically honest one here. The CD40-specific proposal is instead attached to the
  human-experimental GO:0007165 TAS row anchored to PMID:7530216, where it belongs.
- **GO:0031996 "thioesterase binding" / GO:0031625 "ubiquitin protein ligase binding"
  (IPI, PMID:11279055).** That paper is a bioinformatics-driven survey in which the isolated
  TRAF domains of MUL/TRIM37 and USP7 bound *all six* TRAFs in vitro
  ["MUL and USP7 are capable of binding in vitro via their TDs to all of the previously
  identified TRAF family proteins (TRAF1, TRAF2, TRAF3, TRAF4, TRAF5, and TRAF6)"], i.e. a
  pan-TRAF, non-selective interaction. Kept, but non-core. (Independently, TRAF3 genuinely
  binds ubiquitin thioesterases OTUB1/OTUB2/OTUD5 (= DUBA), so the term itself is not wrong.)
- **GO:1902554 "serine/threonine protein kinase complex" (NAS, PMID:24622840).** From the
  STING–TRAF3–TBK1 complex. TRAF3 is a transient adaptor within a signalling complex that
  contains a kinase, not a stoichiometric subunit of a kinase complex. Marked over-annotated.
- **GO:0006915 "apoptotic process" (TAS, PMID:10799510).** Rests on a dominant-negative TRAF3
  blocking LIGHT-induced death; TRAF3 is upstream signalling, not part of the apoptotic
  execution programme. Marked over-annotated (the regulatory parent GO:0042981 is kept as
  non-core).
- **GO:0005515 "protein binding" (25 IPI rows).** Uninformative per project guidance; the
  informative content is preserved by GO:0005164, GO:0035591, GO:0019901, GO:0019903 and the
  proposed K63-ubiquitination terms.

## 5. Gaps

Added to the review as **NEW annotations** (terms absent from GOA entirely):

| Term | Why |
|---|---|
| GO:1901223 negative regulation of non-canonical NF-kappaB signal transduction | TRAF3's flagship function; not in GOA at all |
| GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process | mechanism of the above (NIK turnover) |
| GO:0070534 protein K63-linked ubiquitination | the chain type TRAF3 actually builds (ASC, self) |

Recommended as **`proposed_replacement_terms` on MODIFY rows** (the term is already
represented in GOA, but by a parent that is too general or unsigned):

| Existing row | Replacement | Why |
|---|---|---|
| GO:0007165 signal transduction (both rows: TAS/PMID:7530216 and IEA/GO_REF:0000002) | GO:0023035 CD40 signaling pathway | the founding receptor context, currently only generic "signal transduction". The proposal is justified by the direct human evidence on the TAS row and recommended for the gene's annotation set; the IEA row is an InterPro2GO mapping from the pan-TRAF signature IPR012227 and has no anchoring publication of its own, so the term is not something that rule could have picked out. Contrast the GO:0007166 IBA, which is left broad (see §4) - the difference is that GO:0007165 is also carried by direct human experimental evidence here, whereas the IBA row is family-level only. |
| GO:0032648 regulation of interferon-beta production | GO:0032728 positive regulation of interferon-beta production | GOA has only the unsigned parent |
| GO:0032479 regulation of type I interferon production | GO:0032481 positive regulation of type I interferon production | ditto |
| GO:0050688 regulation of defense response to virus | GO:0002230 positive regulation of defense response to virus by host | ditto |
| GO:0008063 Toll signaling pathway (IEA) | GO:0002224 toll-like receptor signaling pathway | wrong lineage (see §4) |
| GO:0004842 ubiquitin-protein transferase activity | GO:0061630 ubiquitin protein ligase activity | parent also covers E1/E2 |

Proposed as a **new ontology term** (nothing suitable exists): a
`lymphotoxin beta receptor signaling pathway` term, as a sibling of GO:0023035 under
GO:0007166. Checked against OLS — GO has lymphotoxin terms only for the ligand and its
production (GO:0032641, GO:0032681, GO:0062048), none for LTBR-initiated signalling.

## 6. Open questions

- Is the "negative regulator of canonical NF-κB / MAPK" role a *direct* TRAF3 activity or
  purely a consequence of NIK-level and cIAP-level effects? The LTβR data (PMID:20185819)
  argue for a receptor-complex-composition mechanism (TRAF3 excludes TRAF2/IKK1), which would
  be a genuine adaptor function. This is why GO:0043122 is kept as the unsigned parent rather
  than being narrowed to GO:0043124 (negative regulation): signing the term would assert a
  mechanism the current evidence does not distinguish. Suggested experiment 1 in the review
  is designed to settle it.
- Isoform 2 (Q13114-2) has no functional data at all in the reviewed literature.
- Which substrates besides ASC does TRAF3 ubiquitinate directly? Most published "TRAF3
  ubiquitination" work is TRAF3-as-substrate.
