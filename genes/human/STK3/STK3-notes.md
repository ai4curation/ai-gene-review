# STK3 (MST2) review notes

Automated deep research was unavailable for this review (no deep-research provider
keys), so no `*-deep-research-*.md` file exists. These notes are compiled by hand from
the cached publications in `publications/`, the UniProt record (Q13188) and the
cached GO-CAM index. Quotes are verbatim from the cached files.

## Identity

- Human STK3 / MST2, UniProt Q13188, 491 aa. STE20 group, GCKII subfamily
  (MST1/STK4 and MST2/STK3), ortholog of Drosophila Hippo.
- Domains (UniProt): protein kinase 27-278, SARAH 437-484, coiled coils 287-328
  and 442-475, caspase-3 site Asp-322.
- InterPro includes IPR036674 "p53_tetramer_sf" (fold-level structural
  superfamily that the SARAH helix matches), plus SARAH-specific IPR011524,
  IPR024205, IPR049568.
- Paralog STK4 (MST1): 78% identity [PMID:8566796 "MST2 is most similar to the previously identified MST1 protein kinase (78% identity, 88% similarity)"].
  Many papers (and many GOA rows) treat "MST1/2" jointly; attribution to MST2 must be
  checked per paper.

## Catalytic activity (core)

- First characterization: [PMID:8566796 "An in vitro kinase assay indicates that MST2 can phosphorylate an exogenous substrate, as well as itself, and phospho-amino-acid analysis indicates that it is a serine/threonine protein kinase"] (abstract only).
- Autoactivation: [PMID:15109305 "recombinant MST1/2 undergo a robust autoactivation in vitro, mediated by an intramolecular autophosphorylation of a single site [MST1(Thr183)/MST2(Thr180)] on the activation loop of an MST dimer"].
- Structural basis: [PMID:23972470 "Mst2 undergoes activation through transautophosphorylation at its activation loop, which requires SARAH-mediated homodimerization. RASSF5 disrupts Mst2 homodimer and blocks Mst2 autoactivation."]
- Mg2+ cofactor visible in the active site: [PMID:23972470 "the Mg2+ ion and AMP-PNP are clearly visible in the electron density map"].
- Substrates:
  - LATS1/LATS2: [PMID:15688006 "human Mst2, a STE20-family member and purported Hpo ortholog, phosphorylates and activates both Lats1 and Lats2"] (abstract only).
  - MOB1A/B: [PMID:18328708 "The MOBKL1A and MOBKL1B polypeptides, homologs of the Drosophila MATS polypeptide, are identified as preferred MST1/MST2 substrates in vitro"]; [PMID:18362890 "Thr74, but not Thr181, is phosphorylated by MST2 in vitro"].
  - SAV1: [PMID:16930133 "In vitro phosphorylation experiments indicate that the phosphorylation of Sav by Mst is direct."]
  - NEK2A (centrosome disjunction): [PMID:21076410 "Our data suggest that Mst2 phosphorylates Nek2A thereby recruiting Nek2A to centrosomes and promoting phosphorylation and displacement of centrosomal linker proteins."]
  - LC3B Thr-50 (with STK4), mentioned in [PMID:31857374 "LC3B is phosphorylated at Thr-50 within the LDS by serine/threonine kinase (STK) 3 and STK4."]
  - YAP is NOT a good direct MST2 substrate: [PMID:17974916 "Mst2 poorly phosphorylated GST-YAP2, even though it had much stronger autophosphorylation than that of Lats2"].

## Regulation / complexes

- SARAH heterodimers with SAV1: [PMID:29063833 "Our structural and biochemical studies reveal that SAV1 and MST2 heterodimerize through their SARAH domains. Two SAV1-MST2 heterodimers further dimerize through SAV1 WW domains to form a heterotetramer, in which MST2 undergoes trans-autophosphorylation."]
  Note: this is a genuine 2:2 tetramer containing MST2, but the dimer-of-dimers
  contact is made by SAV1 WW domains, not by the MST2 SARAH helix.
- SARAH homo/heterodimer crystal structures: [PMID:25004971 "the three-dimensional structures of an MST1-RASSF5 SARAH heterodimer and an MST2 SARAH homodimer were determined by X-ray crystallography"]; MST1 SARAH homodimer and conversion of tetrameric RASSF5 SARAH to dimers [PMID:17517604 "In cross-linking experiments, the major population of the free Rassf5 SARAH domain formed tetramers in solution. However, when the Mst1 SARAH domain was added, dimers were formed"].
- STRIPAK/SLMAP-PP2A inactivates MST2: [PMID:29063833 "SLMAP binding to autophosphorylated MST2 linker recruits STRIPAK and promotes PP2A-mediated dephosphorylation of MST2 at the activation loop."]; [PMID:30622739 "the knockdown of MST2 markedly decreased the phosphorylation of its substrate MOB1 (T35), leading to an enhanced YAP activity"].
- RASSF1A protects MST2 phosphorylation and stabilizes it [PMID:21199877 "In addition to preventing dephosphorylation, RASSF1A also stabilized the MST2 protein."]
- RASSF2 stabilizes MST2 and relocalizes [PMID:19525978 "whereas RASSF2 alone is nuclear, the presence of MST1 or MST2 results in colocalization in the cytoplasm"].
- Raf-1/AKT crosstalk [PMID:20086174 "Raf-1 binds and inhibits MST2 kinase"].
- DLG5 links MARK3 to MST1/2 and inhibits them [PMID:28087714].
- WWC proteins organize SAV1-MST1/2 activation of LATS1/2 [PMID:35429439 "SAV1, in turn, brings in MST1/2 to phosphorylate and activate LATS1/2"].

## Localization

- Full-length MST is cytoplasmic; caspase-cleaved kinase enters the nucleus in apoptosis
  [PMID:11278283 "Immunohistochemical analysis reveals that MST is localized in the cytoplasm. During Fas-mediated apoptosis, cleaved MST translocates into the nucleus before nuclear fragmentation is initiated"].
- Centrosome: Mst1/2 and hSav1 are centrosomal and recruit Nek2A [PMID:21076410].

## Processes

- Hippo signaling: core initiating kinase, MST1/2-SAV1 -> LATS1/2-MOB1 -> YAP/TAZ.
  GO:0035329 definition names STK4/MST1 and STK3/MST2 explicitly.
- Contact inhibition via YAP: [PMID:17974916 "Our observations demonstrate that YAP plays a key role in the Hippo pathway to control cell proliferation in response to cell contact."]
- Apoptosis: caspase substrate, proapoptotic upon overexpression [PMID:11278283].
- PPARgamma/adipogenesis with SAV1 [PMID:22292086 "This binding required the kinase activity of MST2 and was mediated by the WW domains of SAV1 and the PPYY motif of PPARγ."]; mechanism of PPARγ activation unresolved [PMID:22292086 "stimulation of PPARγ transactivation activity by MST2 and SAV1 requires other mechanism, such as recruitment of co-activators or phosphorylation"].
- Wnt crosstalk is via TAZ-DVL [PMID:20412773] (abstract only; indirect for STK3).
- FOXO / oxidative stress pathway described for MST1 [PMID:16751106] (abstract only; MST2 not mentioned in abstract).
- Autophagy: STK3 binds ATG8 family proteins via an LIR [PMID:31857374 "GST–pulldown assays using translated in vitro STK3 showed that STK3 interacted directly with several of the ATG8s, but most strongly with LC3C and GABARAP"].

## GO-CAM

`gocams/index.tsv` contains STK3 (UniProtKB:Q13188) in 8 human models:
- 7 Hippo models (e.g. 65a1f4f800003391 "Hippo signaling core components (Human).",
  65c57c3400001478 "Negative regulation of Hippo signaling by SLMAP-STRIPAK complex")
  all as GO:0004674 protein serine/threonine kinase activity, part of GO:0035329
  hippo signaling, occurs in GO:0005737 cytoplasm.
- 65039e8700001110 "TRIM69 activation of STK3 by ubiquitination leading to centrosome
  separation" as GO:0004674, part of GO:0071539 protein localization to centrosome,
  in GO:0005813 centrosome (NEK2 carries centrosome separation in that model).
This matches the core functions chosen here.

## Premetazoan context (ancestral vs animal-specific)

- Hippo kinase is the most ancient core Hippo component [PMID:38729842 "among the core Hippo pathway components, the Hippo kinase appears most ancient, and is present in amoebozoans such as Dictyostelium discoideum and Acanthamoeba castellanii"].
  The SARAH domain is lost in most fungal Hippo-like kinases [PMID:38729842 "the Hippo-like kinases in most fungal lineages do not contain a SARAH domain"].
- Capsaspora coHpo (repo review genes/CAPO3/coHpo): kinase domain + SARAH. Knockout makes
  coYki nuclear [PMID:38517944 "Loss of either kinase results in increased nuclear localization of coYki, showing that the regulatory activity of the Hippo kinase cascade is conserved."],
  does not change proliferation [PMID:38517944 "In adherent growth conditions, coWts-/- and coHpo-/- cells proliferated at similar rates as WT cells"],
  and increases a contractile/elongated cell state. In Drosophila cells coHpo
  phosphorylates Wts and Yki [PMID:22832104 "Interestingly, Co-Hpo also stimulated the phosphorylation of Dm-Wts and Dm-Yki"].
- S. rosetta hippo (repo review genes/SALRS/hippo): knockout slows proliferation but
  rosette size is unchanged [DOI:10.1101/2024.07.13.603360 "The size of hippopac1 and yorkiepac1 rosettes did not significantly differ from wild type"].
- Synthesis (Phillips, Zheng & Pan review): ancestral function is cytoskeletal; proliferation/
  tissue-size control is a later co-option [PMID:38729842 "The deep conservation of cytoskeletal regulation by the Hippo pathway indicates an ancestral role for the Hippo pathway in cytoskeletal regulation, implying a subsequent co-option of the pathway to constrain proliferation and tissue size in animals."]
- Conclusion for STK3:
  - Ancestral (pre-Holozoa for the kinase+SARAH architecture; Holozoa for the
    Hpo-Wts-Yki cascade): Ser/Thr kinase activity, SARAH-mediated dimerization,
    activation of the Warts/LATS kinase and cytoplasmic restraint of
    Yorkie/YAP (hippo signaling sensu GO:0035329).
  - Animal-specific recruitments: contact inhibition of proliferation, organ/tissue growth
    control, apoptosis (caspase-cleavage-dependent), crosstalk with Wnt/TGF-beta/PPARγ,
    adipogenesis, ER-alpha regulation; centrosome disjunction role unknown outside animals.

## Tetramerization row (InterPro2GO IPR036674)

Human STK3 carries the same IEA `GO:0051262 protein tetramerization` from IPR036674
(p53 tetramerisation superfamily) as coHpo. The structural evidence is that the MST2
SARAH domain forms homodimers and 1:1 heterodimers (PMID:23972470, PMID:25004971,
PMID:17517604). Unlike coHpo, human MST2 has one documented tetrameric assembly, the
2:2 SAV1-MST2 complex (PMID:29063833), but the dimer-of-dimers interface there is made by
SAV1 WW domains, not by STK3. So the InterPro2GO basis (a p53-like tetramerisation fold)
is still wrong; I marked it MARK_AS_OVER_ANNOTATED rather than REMOVE because a
STK3-containing tetramer does exist in human cells.

## Protein binding rows

93 IPI `protein binding` rows. Policy: MODIFY where the cited paper supports a more
informative MF (SARAH heterodimerization with SAV1 / RASSF5 shown in focused studies;
self-interaction -> protein homodimerization activity), otherwise REMOVE as uninformative
(the interactions themselves are not disputed). No GO term for "Atg8-family protein
binding" was found in QuickGO, so the ATG8-family rows are removed rather than modified.
