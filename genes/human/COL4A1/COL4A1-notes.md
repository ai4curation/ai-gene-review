# COL4A1 (collagen alpha-1(IV) chain, human, P02462) review notes

Automated deep research was unavailable for this review (no provider keys), so no
`-deep-research-*.md` file exists. These notes are based on the UniProt record, the GOA rows
and the cached publications in `publications/`. Full text was available for PMID:12011424,
16107487, 19949034, 23065703, 28418331 and 24344311 (and the proteomics papers 23658023,
23979707, 25037231, 27068509, 27559042, 28327460, 28675934, which mostly list COL4A1 only in
supplementary tables). PMID:18160688, 20818663, 8900172, 14718574, 22261194, 28344315 and
29853175 are abstract-only.

## Core biology

- Collagen IV protomers form the basement membrane network: "Triple-helical collagen IV
  protomers associate through their N- and C-termini forming a three-dimensional network,
  which provides basement membranes with an anchoring scaffold and mechanical strength."
  [PMID:12011424]
- Chain composition: "The major collagen IV protomers detected in all basement membranes
  consist of two α1(IV) chains and one α2(IV) chain" [PMID:12011424]; "Type IV collagen α1 and
  α2 chains form the widely expressed α1α1α2(IV) heterotrimers." [PMID:19949034]
- NC1 hexamer and cross-link: "The trimer–trimer interaction is further stabilized by a
  previously uncharacterized type of covalent cross-link between the side chains of a Met and a
  Lys residue of the α1 and α2 chains from opposite trimers" [PMID:12011424]. The bond is a
  sulfilimine made by peroxidasin: "Peroxidasin, a heme peroxidase embedded in the basement
  membrane, produces hypohalous acid intermediates that oxidize methionine, forming the
  sulfilimine cross-link." [PMID:24344311]
- UniProt: proteolytic processing releases the NC1 fragment arresten, reported to be
  anti-angiogenic (PMID:10811134, PMID:18775695 per UniProt; not cached, not read; no GOA row,
  so not used in the review).

## Human genetics (BM organization rows)

- HANAC: "Histologic analysis revealed complex basement-membrane defects in kidney and skin."
  [PMID:18160688, abstract]
- HANAC skin: "Replication of the lamina densa was observed at the dermoepidermal junction in
  the affected subjects of the 3 families" [PMID:19949034]
- Haploinsufficiency: "thickening of the capillary basement membrane in the skin was
  documented" [PMID:23065703]; "a clear reduction in COL4A1 protein in both families"
  [PMID:23065703]
- Porencephaly: glycine mutations "predicted to result in abnormal collagen IV assembly"
  [PMID:16107487]. The same paper attributes porencephaly to perinatal vascular accidents and
  basement-membrane fragility, not to a primary role in brain development: "Porencephaly
  (cystic cavities of the brain) is caused by perinatal vascular accidents from various
  causes." and "compatible with abnormalities of the vascular basement membrane as a result of
  COL4A1 mutations." [PMID:16107487]. So `brain development` is downstream/over-annotated.
- HANAC mutations cluster in CB3[IV], "which encompasses major integrin-binding sites"
  [PMID:20818663, abstract]. Retinal arterial tortuosity supports a retinal vessel morphogenesis
  phenotype; the abstract does not mention vessel branching (full text not available), so
  `branching involved in blood vessel morphogenesis` is left UNDECIDED.

## Other rows

- `collagen fibril organization` (NAS, PMID:29853175): the cited review is about fibrillar
  collagens ("Collagen fibrils are the major mechanical component..."). Collagen IV is a
  network-forming collagen, not a fibril-forming one, so REMOVE.
- `protein binding` (IPI, PMID:12011424, with COL4A2): the interaction is chain assembly into the
  alpha1alpha1alpha2 protomer/NC1 hexamer, already captured by `collagen type IV trimer` (IPI,
  same paper). REMOVE as uninformative.
- `platelet-derived growth factor binding` (IDA, PMID:8900172, abstract): PDGF binds collagens
  I-VI "and their constituent chains", with medium affinity (KD 4-22 nM). Kept as non-core.
- `epithelial cell differentiation` (IEA, Ensembl Compara from rat): no human or direct
  evidence; a structural BM protein is at most permissive. Over-annotated.
- ER lumen (ARBA, Reactome procollagen assembly/secretion): biosynthetic transit compartment
  where chains fold and trimerise. Kept as non-core.
- ECM `HDA` rows and `RCA`/`HDA` rows for `GO:0030020` come from matrisome proteomics; they show
  presence in ECM, not tensile function. Function itself is well established (PMID:12011424,
  IBA), so ACCEPT and note the weak evidence type.

## GO-CAM

`gocams/index.tsv` has no COL4A1 entry (checked 2026-10-01).

## Premetazoan context (verified from cached full text)

- Collagen IV is absent from unicellular relatives of animals: "Moreover, collagen IV is absent
  in unicellular sister-groups." [PMID:28418331]; "unicellular protists (Choanozoa,
  Filasterea, Amoebozoa, Apusozoa) do not contain collagen IV as determined by genomic analyses"
  [PMID:28418331]. Choanoflagellates do have fragments: "collagenous GXY repeats were identified
  in Monosiga, Salpingoeca, and Dictyost[elium]", and "Laminin architecture appears to be
  present in choanoflagellates" [PMID:28418331].
- Present in early-branching animals: ctenophores ("We identified basement membrane (BM) and
  collagen IV in Ctenophora"), placozoans ("Placozoa contains the necessary components for a BM,
  including collagen IV, laminin, perlecan, and nidogen"), homoscleromorph sponges ("the ECM of
  homoscleromorph sponges contains basement membranes (Boute et al., 1996), with collagen IV and
  laminin"); demosponges and hexactinellids lack both collagen IV and a basement membrane
  [PMID:28418331].
- Sulfilimine cross-link: "the cross-link is conserved throughout Eumetazoa and arose at the
  divergence of Porifera and Cnidaria over 500 Mya" [PMID:24344311]; ctenophore collagen IV
  lacks the Met/Lys pair and uses a different cross-link [PMID:28418331].
- PMID:29848444 (animal stem lineage gene families) was checked: it does not discuss collagen IV
  or basement membrane specifically (only fibrillar collagen loss in fly/worm), so it is not
  cited for these claims.
- Conclusion: COL4A1's structural function in a basement membrane is an animal innovation; there
  is no ancestral unicellular function to separate out. Some building blocks (GXY repeats,
  laminin-like domains, integrins in Capsaspora) predate animals, but the collagen IV protomer
  and its NC1 domain do not appear before Metazoa on current genomic evidence.
- Unverified background (not used in YAML): whether the alpha1/alpha2 (odd/even) chain split
  dates to the cnidarian-bilaterian ancestor; Fidler 2017 notes paired head-to-head genes in
  Nematostella and Trichoplax.

## Decisions summary

See `COL4A1-ai-review.yaml`. Core function: `GO:0030020` ECM structural constituent conferring
tensile strength, in `GO:0005587` collagen type IV trimer, at `GO:0005604` basement membrane,
directly involved in `GO:0071711` basement membrane organization. No NEW rows.
