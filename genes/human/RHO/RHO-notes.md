# RHO (rhodopsin, UniProt P08100) review notes

Journal of what was read and what was decided. Quotes are verbatim from the cached file
named in the bracket. Species of each experiment is stated because most classic
rhodopsin biochemistry is on the bovine protein (P02699), not the human one.

## 1. Inputs read

- `genes/human/RHO/RHO-uniprot.txt` (OPSD_HUMAN, entry version 250).
- `genes/human/RHO/RHO-ai-review.yaml`: 75 seeded rows.
- GOA-cited publications in `publications/` (18 PMIDs; which are abstract-only is listed in
  section 3).
- Reactome cache entries cited by the 19 Reactome TAS rows.
- `modules/visual_phototransduction.yaml`, `gocams/6918f23700000035/` (section 6).
- `genes/human/RHO/RHO-deep-research-openscientist.md` used as a literature lead only
  (section 7).

## 2. UniProt record (what it says and on what evidence)

- Function, publication-backed (`ECO:0000269`): a G protein-coupled photoreceptor that
  activates the transducin pathway in response to light; essential for dim-light
  image-forming vision; required for photoreceptor viability. Activation is by
  photoisomerization of covalently bound 11-cis-retinal to all-trans-retinal. Signal
  termination is by receptor phosphorylation and arrestin (SAG) binding.
- Absorption maximum 496 nm (PubMed:6140680, human retinal microspectrophotometry).
- Subcellular location: photoreceptor outer segment membrane, multi-pass membrane
  protein (PubMed:25664179, 19934218, 26200343, 28753425). Note: synthesized in the rod
  inner segment before vectorial transport to disc membranes of the outer segment.
- Subunit: homodimer "By similarity"; GRK1 and SAG interactions are publication-backed
  (PubMed:28524165, 26200343, 28753425); the ASAP1/ARF4/RAB11A/Rabin8/RAB11FIP3
  trafficking complex is "By similarity" to bovine P02699 and mouse P15409.
- PTM: retinylidene Schiff base at Lys-296 and palmitoylation at Cys-322/323 are
  by similarity to bovine P02699; phosphorylation at Ser-334, Thr-336, Ser-338 and
  N-glycosylation at Asn-15 are publication-backed (PubMed:28753425).
- Disease: retinitis pigmentosa 4 (RP4) and autosomal dominant congenital stationary
  night blindness 1 (CSNBAD1); G90D, T94I, A292E are the constitutively active CSNB
  alleles.
- Similarity: G protein-coupled receptor 1 family, opsin subfamily (PROSITE rule).

## 3. GOA-cited publications: what each one shows for rhodopsin

Abstract-only in the cache: 11284701, 11767049, 12566452, 12754272, 1418997, 17693260,
2218504, 23704327, 6140680, 8107847, 8253795. Full text in the cache: 19934218
(Introduction and Discussion only), 25664179, 26200343, 28753425, 31380578, 31730232,
32296183.

- PMID:6140680 (Dartnall 1983). Human retinas, microspectrophotometry of rod and cone
  outer segments. [PMID:6140680 "rods, 496.3 +/- 2.3 nm (n = 39)"]. Direct human
  evidence that the rod pigment absorbs visible light in outer segments.
- PMID:11284701 (Brueggemann 2001). Human rod opsin expressed in cells, early receptor
  current. [PMID:11284701 "all-trans-retinal can form a visual pigment with opsin,
  through both protonated and unprotonated Schiff base linkages and likely within the
  native ligand binding pocket at lysine-296"]. Human protein, heterologous cells.
- PMID:8107847 (Rao 1994). [PMID:8107847 "the mutation Gly 90-->Asp (G90D) in the second
  transmembrane segment of rhodopsin, which causes congenital night blindness, also
  constitutively activates opsin"]. In vitro transducin activation. The abstract does
  not say whether the mutant was made in bovine or human opsin; the Oprian laboratory
  used a synthetic bovine opsin gene in this period, so the species is not verified
  from the cache.
- PMID:2218504 (Franke 1990). [PMID:2218504 "Three mutant opsins with alterations in
  their cytoplasmic loops bound 11-cis-retinal to yield pigments with native rhodopsin
  absorption spectra, but they failed to stimulate the guanosine triphosphatase
  activity of Gt"]. Khorana laboratory, synthetic bovine opsin gene (species not stated
  in the abstract). Evidence that the second and third cytoplasmic loops are needed to
  activate transducin.
- PMID:8253795 (Sung 1993). Human rhodopsin cDNA in 293S cells. [PMID:8253795 "Three of
  the mutant proteins (G51V, V345M, and P347S) resemble the wild type in yield,
  regenerability with 11-cis-retinal, and accumulation in the plasma membrane (class
  I)"]. Human protein, heterologous cells: wild type reaches the plasma membrane and
  regenerates with 11-cis-retinal.
- PMID:12566452 (Noorwez 2003). P23H opsin in cells; rescued protein
  [PMID:12566452 "forms pigment, acquires mature glycosylation, and is transported to
  the cell surface"].
- PMID:1418997 (Olsson 1992). Human wild-type and P23H RHO transgenes in mice.
  [PMID:1418997 "overexpression of wild-type human rod opsin leads to a remarkably
  similar photoreceptor degeneration"]. A disease-model paper; it does not assay
  phototransduction by the human protein.
- PMID:19934218 (Kosmaoglou 2009). EDEM1 and rod opsin. Cached text has no Results.
  [PMID:19934218 "EDEM1 was detected in rod photoreceptor inner segments and
  EndoH-sensitive rod opsin co-immunoprecipitated with EDEM1 from retina, suggesting
  that rod opsin is a physiological EDEM1 client"].
- PMID:12754272 (Chapple 2003). HSJ1b (DNAJB2 isoform) and rhodopsin-GFP in SK-N-SH
  cells. [PMID:12754272 "The expression of HSJ1b, but not HSJ1a, inhibited the normal
  cellular processing of wild-type rhodopsin-GFP, which co-localized with HSJ1b at the
  ER"]. The abstract reports co-localization and recruitment to inclusions; it does not
  describe a binding assay.
- PMID:17693260 (Chuang 2007). SARA (ZFYVE9) and rhodopsin vesicle targeting.
  [PMID:17693260 "This membrane coupling is regulated by the FYVE domain-containing
  protein, SARA, through its direct interaction with PI3P, rhodopsin, and SNARE protein
  syntaxin 3"].
- PMID:23704327 (Papal 2013). Spectrin betaV, mouse photoreceptors (abstract-only).
- PMID:25664179 (Chuang 2015). Immuno-EM of endogenous rhodopsin in CD1 mouse rods and
  an HRP-rhodopsin-GFP-1D4 reporter electroporated into rat rods.
  [PMID:25664179 "As predicted [44], the OS discs were heavily labeled by rhodopsin
  immunogolds"]. The cached text does not state the species of the rhodopsin cDNA in
  the reporter.
- PMID:26200343 (Kang 2015). [PMID:26200343 "We used human rhodopsin and mouse visual
  arrestin-1 in this study"]. Crystal structure of constitutively active human
  rhodopsin (E113Q/M257Y) fused to mouse arrestin; the G-alpha C-terminal peptide binds
  the same receptor.
- PMID:28753425 (Zhou 2017). Phosphorylated human rhodopsin C-terminal tail bound to
  arrestin; phosphates detected at S334, T336, S338.
- PMID:11767049: see section 5.
- PMID:31380578, PMID:31730232, PMID:32296183: see section 5.

## 4. Rules applied (from CLAUDE.md and projects/ORGANELLES.md)

- Rows sharing a term get consistent actions; a true but broad term is never REMOVE.
- `membrane` rows are MODIFY to the specific supported descendant.
- Golgi rows: transit is not residence (ORGANELLES rule 7).
- Bare protein binding: MODIFY only if the paper supports a specific function,
  otherwise REMOVE as uninformative.

## 5. Rows flagged for care

### 5.1 PMID:11767049 rows (photoreceptor outer segment, inner segment, Golgi apparatus; IDA; MGI)

- The cached record for PMID:11767049 is abstract-only. The abstract is a kidney study:
  [PMID:11767049 "Fibrotic degeneration was examined in the kidneys of ICR-derived
  glomerulonephritis (ICGN) mice"]. It names laminin, collagens, tenascin and integrin
  subunits; it does not mention rhodopsin, the retina or photoreceptors.
- QuickGO, queried 2026-11-16 for every annotation citing PMID:11767049, returns eight
  rows. Four are mouse Itga1, Itga2, Itga6 and Tnc (MGI, dated 20110204), which fit the
  abstract. Four are human: RHO to GO:0001750, GO:0001917 and GO:0005794, and RP1
  (P56715) to GO:0032391 photoreceptor connecting cilium (MGI, all dated 20110207).
- On the same day (20110207) MGI made ISO annotations on mouse Rho (P15409) to
  photoreceptor outer segment and inner segment, with UniProtKB:P08100 in WITH/FROM,
  citing PMID:11773008. That paper is Liu et al. 2002, cached by me:
  [PMID:11773008 "The subcellular location of RP1 in human and mouse retinas was
  determined by immunostaining retinal sections"] and [PMID:11773008 "both the human RP1
  and mouse Rp1 proteins are specifically localized in the connecting cilia of rod and
  cone photoreceptors"]. This is exactly the human RP1 annotation that sits on
  PMID:11767049.
- Conclusion: the three human RHO rows are keyed to the wrong reference. The intended
  paper is very probably PMID:11773008. Recorded as `source_defects` (WRONG_REFERENCE,
  resource MGI, confidence PROBABLE). Not CONFIRMED because the abstract of PMID:11773008
  does not name rhodopsin and I could not read its full text (PMC1963488 is
  publisher-restricted: `just fetch-pmid` got 403 on HTML and the PMC XML carries only
  front matter).
- Actions judge the claims, which stand on other evidence: outer segment ACCEPT, inner
  segment KEEP_AS_NON_CORE (biosynthetic pool), Golgi apparatus KEEP_AS_NON_CORE (transit
  pool, direct-evidence code on the human protein).

### 5.2 Plasma membrane IDA rows citing the opsin 3 papers

- PMID:31380578 (human dermal fibroblasts). Rhodopsin (OPN2) was stained with a
  commercial antibody: [PMID:31380578 "Our results showed that OPN1, OPN2, OPN3, OPN4 and
  OPN5 are expressed in NHDFs (Fig. 1a, b) and immunofluorescence results showed that
  OPNs stained positively in NHDFs (Fig. 1c)"], and the legend says
  [PMID:31380578 "The left panel represents the localization of opsins (green) at the
  plasma membrane"]. So the row is not mis-keyed: the paper does report OPN2 staining at
  the plasma membrane of cultured skin fibroblasts. There is no knockdown or other
  specificity control for the OPN2 antibody, and the Discussion itself notes that another
  study did not detect OPN2 in cultured dermal fibroblasts.
- PMID:31730232 (human epidermal melanocytes). The text reports immunofluorescence
  [PMID:31730232 "with specific antibodies against OPNs (yellow)"] but states a membrane
  location only for opsin 3: [PMID:31730232 "Melan-A–positive NHMs showed a strong
  staining of OPN3 in the cell membrane (Fig. 1E)"]. I could not see the figure panels, so
  I cannot say what the OPN2 panel shows.
- Both rows are weak evidence for the claim, in a cell type where rhodopsin has no
  established role. The claim itself (rhodopsin in the plasma membrane) stands on human
  rhodopsin expressed in 293S cells (PMID:8253795) and on the rod outer segment plasma
  membrane. All plasma membrane rows are KEEP_AS_NON_CORE: true, as precise as each assay
  allows, not the core site (sealed rod discs are not plasma membrane in GO).

### 5.3 Ensembl Compara IEA rows from mouse Rho (P15409)

QuickGO, queried 2026-11-16 for the mouse donor rows:

- sperm midpiece (GO:0097225) and sperm head plasma membrane (GO:1990913): mouse IDA,
  PMID:31924821 (Roy 2020, cached by me, full text). Mouse sperm were stained with a
  knockout control: [PMID:31924821 "A quantitative analysis revealed specific staining
  with anti-rhodopsin antibody in the acrosome, equatorial ring, postnuclear cap and
  midpiece (Fig. 3)"]. Human sperm were stained too, without a control:
  [PMID:31924821 "While we cannot validate, in the absence of a similar negative control
  for human sperm cells, the locations of these opsins in human cells"]. The paper never
  says "plasma membrane" for the sperm head; that term is the curator's reading of head
  staining. Midpiece: KEEP_AS_NON_CORE. Sperm head plasma membrane: MARK_AS_OVER_ANNOTATED.
- cell-cell junction (GO:0005911): mouse IDA, PMID:23793062, a T cell paper:
  [PMID:23793062 "Engagement of TCR-CD28 at the immunological synapse resulted in the
  colocalization of CD28 with both wild-type and mutant Rltpr proteins"]. QuickGO lists 65
  annotations on this PMID; about 40 are `located_in cell-cell junction` rows (MGI,
  20140306-07) on T cell signalling proteins: Lat, Lck, Zap70, Itk, Vav1, Was, Cdc42,
  Cfl1, Coro1a, Actr3 and so on. "Rho" sits in that list beside Cdc42. This is a set of
  imaged T cell signalling and actin regulators, in which "Rho" almost certainly means the
  Rho GTPase, not the rhodopsin gene whose mouse symbol is Rho. Probable symbol collision
  at MGI, propagated to the human gene by Ensembl Compara. Human row: REMOVE, with a
  `source_defects` entry (WRONG_GENE_PRODUCT, resource MGI, PROBABLE; the cache is
  abstract-only so the full text was not read).
- photoreceptor outer segment and inner segment: the mouse rows rest on many MGI IDA
  papers for the outer segment and on PMID:10399916 (UniProt IDA) for the inner segment.

### 5.4 PAINT

`just paint-losses human RHO` (2026-11-16): "No IRD or IKR loss on this gene's lineage."
