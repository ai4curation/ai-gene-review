# VCL (vinculin, human, UniProt P18206) -- review notes

Automated deep research was unavailable for this gene (no deep-research provider
keys in this environment). These notes were written manually from the UniProt
entry (VINC_HUMAN), the cached publications cited by GOA (see
`full_text_available:` in each `publications/PMID_*.md`), and three cached
papers on premetazoan vinculin (PMID:29880641, PMID:32857975, PMID:20479219).

## Identity and structure

- 1134-aa metavinculin (isoform 2, displayed) / 1066-aa vinculin (isoform 1);
  member of the vinculin/alpha-catenin family (PANTHER PTHR46180; InterPro
  IPR006077, IPR017997). Single gene on 10q
  [PMID:2116004 "the human vinculin gene was mapped to chromosome 10q11.2-qter"].
  Metavinculin (68-residue tail insert) is muscle-specific (UniProt).
- Head (Vh, D1-D4) + proline-rich hinge + tail (Vt). Head-tail interaction
  autoinhibits; the tail carries the F-actin binding site
  [PMID:7816144 "an intramolecular association between the 95K head and 30K tail domains of vinculin masks an F-actin binding site present in the carboxy-terminal tail domain"];
  [PMID:7816144 "Vinculin itself neither cosediments with nor crosslinks F-actin."].

## Molecular activities

- **Actin filament binding** (tail; cryptic in the closed molecule)
  [PMID:7816144 "Cosedimentation and crosslinking assays, and direct visualization by transmission electron microscopy, reveal an interaction between F-actin and a bacterially expressed fusion protein containing amino acids 811-1066 of vinculin"].
  GOA has only generic `actin binding` (IDA, PMID:16803572, abstract-only) and a
  NOT `actin binding` (IDA, PMID:7816144). The NOT row reflects the
  autoinhibited full-length protein in vitro; the same paper establishes a
  cryptic F-actin site, so the NOT row misrepresents the gene product. Proposed
  NEW `actin filament binding` (GO:0051015).
- **Talin binding** (D1 head; activates vinculin)
  [PMID:15070891 "all of talin VBSs activate vinculin by provoking helical bundle conversion of the Vh domain, which displaces the vinculin tail (Vt) domain"];
  review [PMID:10320934 "Talin has two or more actin-binding sites, and three binding sites for the cytoskeletal protein vinculin."].
- **alpha-actinin binding** (D1)
  [PMID:15988023 "alpha-Actinin interacts with vinculin through the binding of an alpha-helix (alphaVBS) present within the R4 spectrin repeat of its central rod domain to vinculin's N-terminal seven-helical bundle domain (Vh1)"].
- **alpha-catenin binding**
  [PMID:9700171 "The 326-509 internal domain was found to bind vinculin."].
- **beta-catenin binding** (requires vinculin A50; binds beta-catenin N-terminus)
  [PMID:20086044 "the reduced surface E-cadherin expression could be rescued by introduction of vinculin, but not of a vinculin A50I substitution mutant that is defective for β-catenin binding"].
- **Arp2/3 complex binding** (hinge)
  [PMID:12473693 "Binding of the Arp2/3 complex to vinculin is direct and does not depend on the ability of vinculin to associate with actin."].
- **SH3 domain binding** (proline-rich hinge binds SoHo-family adaptors)
  [PMID:9885244 "The interaction between vinexin and vinculin was mediated by two SH3 domains of vinexin and the proline-rich region of vinculin."];
  CAP/SORBS1 [PMID:17082770 "The interactions, which occur at cell–ECM adhesions, require the first two SH3 domains of CAP and the proline-rich motifs of paxillin and vinculin."].
- Pathogen mimicry of talin: Shigella IpaA and Rickettsia Sca4 bind and activate
  vinculin [PMID:17932491 "Talin, alpha-actinin, and the invasin IpaA of Shigella flexneri sever vinculin's head-tail interaction by inserting an alpha-helix into vinculin's N-terminal four-helical bundle"];
  [PMID:21841197 "sca4 binds to and activates vinculin through two vinculin binding sites"].
  Real, but host-pathogen; generic `protein binding` rows removed.
- No GO term exists for paxillin binding (QuickGO search 2026-10-01), so the
  paxillin IPI row (PMID:9054445) cannot be converted.
- Cadherin binding: vinculin reaches cadherins through alpha- and beta-catenin,
  not by binding the cadherin tail itself
  [PMID:20086044 "Vinculin, a well-known component of cell-matrix adhesions, is also present at the cytoplasmic domains of cadherins"].
  `cadherin binding` (HDA from the E-cadherin proximity interactome, ISS) is an
  over-annotation.

## Processes and locations

- Cell-matrix adhesions: focal adhesions, costameres, podosomes; strengthens
  integrin-talin-actin linkage
  [PMID:21423176 "We find that myosinII promotes enrichment of proteins that strengthen the integrin-actin linkage (migfilin, filamins, vinculin)."].
  Not required to assemble focal adhesions
  [PMID:10320934 "whereas vinculin (-/-) ES cells are able to do so"]; regulates
  adhesion dynamics and migration
  [PMID:15494027 "whereas vinculin appears to be important in regulating adhesion dynamics and cell migration"].
- Cell-cell junctions: required for E-cadherin surface stability in MCF10A cells
  via beta-catenin [PMID:20086044 "Thus, vinculin regulates cell-surface E-cadherin expression by binding to β-catenin."];
  alpha-catenin-vinculin interaction organizes the apical junctional complex
  [PMID:9700171 "These results indicate that the alphaE-catenin-vinculin interaction plays a role in the assembly of the apical junctional complex in epithelia."].
  Note PMID:9700171 genetics was in mouse F9 vinculin-null cells; binding data used
  chick gizzard lysate.
- Endothelium: force-dependent partitioning between FA (talin) and AJ
  (VE-cadherin) [PMID:26923917 "Thrombin stimulated the vinculin association with FA protein talin and suppressed the interaction with AJ protein, VE-cadherin."];
  [PMID:25753039 "ZO-1 down-regulation triggered redistribution of vinculin from cell–cell junctions to focal adhesions"].
- Lamellipodial protrusion via Arp2/3 recruitment
  [PMID:12473693 "Compared with WT vinculin, expression of this mutant in vinculin-null cells results in diminished lamellipodial protrusion and spreading on fibronectin."].
- Platelet aggregation HMP (PMID:23382103) is correlative (lower vinculin in MDS
  platelets among many proteins) -> over-annotation.
- Maintenance of blood-brain barrier NAS (PMID:30280653): the cached full text of
  this review does not mention vinculin at all -> over-annotation.
- Reactome granule-lumen / extracellular-region TAS rows derive from
  degranulation/platelet-release proteomics; vinculin is a cytoplasmic protein
  without a signal peptide -> over-annotation.

## GO-CAM

`gocams/index.tsv` has no row for VCL (human P18206) or mouse/rat Vcl
(checked 2026-10-01). No GO-CAM role to reconcile.

## IBA rows

All IBA rows come from PANTHER node PTN005285701 (vinculin/alpha-catenin
family node with Dictyostelium donors). Locations (cytoplasm, cytoskeleton,
plasma membrane, focal adhesion, adherens junction, cell-cell contact zone) and
cell adhesion are well grounded, and P18206 itself appears among the donors for
several -- expected, not circular. The beta-catenin binding IBA has P12003
(chicken vinculin) and a Dictyostelium member as donors; Dictyostelium
alpha-catenin-like proteins bind the beta-catenin homolog Aardvark, so the node
may be capturing an alpha-catenin-type activity. Human vinculin has its own
experimental support (Peng 2010), so the IBA is accepted for VCL, but the node
placement is worth checking because sponge vinculin did not bind a
beta-catenin peptide (below).

## Premetazoan / evolutionary context

- Vinculin/alpha-catenin family proteins predate animals
  [PMID:29880641 "VIN proteins link actin filaments to membrane proteins at the plasma membrane and are found in all animals and their close outgroups (choanoflagellates, chytridomycetes, apusozoa, amoebozoa)"].
- Integrin adhesome scaffolds are ancient
  [PMID:20479219 "Many of the scaffolding proteins (talin, vinculin, paxillin) most likely evolved in the common ancestor of amoebozoans and opisthokonts, where they had ancestrally different functions (as in present day amoebozoans)."].
- Capsaspora (unicellular filasterean): vinculin localizes with integrin beta2 in
  adhesive filopodia (abstract-only; antibody specificity not inspectable)
  [PMID:32857975 "We show that integrin β2 and its associated protein vinculin localize as distinct patches in the filopodia."].
- Sponge Oscarella pearsei vinculin (repo review genes/OSCPE/VIN1/): binds talin,
  talin peptide releases F-actin binding
  [PMID:29880641 "Thus, binding of talin to Op vinculin D1 releases autoinhibition for F-actin binding, similar to the behavior of vertebrate vinculin."];
  did not bind a beta-catenin peptide
  [PMID:29880641 "Moreover, Op vinculin bound talin but not β-catenin"];
  localizes to cell-cell contacts and filopodia in tissue.
- Caveat on the beta-catenin negative: the sponge beta-catenin peptide
  corresponded to the alpha-catenin-binding region of beta-catenin, whereas human
  vinculin binds the beta-catenin N-terminus (PMID:20086044, M8P mutant). So the
  sponge result does not directly test the vinculin-beta-catenin interface
  characterised in mammals.

**Synthesis (ancestral vs animal-specific):**
- Ancestral (premetazoan): talin-activated, autoinhibited actin filament binding
  and the talin/integrin cell-substrate linkage (sponge biochemistry; Capsaspora
  filopodial co-localization with integrin; adhesome gene content).
- Animal-specific (plausible, not demonstrated): coupling to cadherin-catenin
  junctions via alpha-catenin and beta-catenin, apical junction assembly, and
  tissue-level roles (endothelial barrier, intercalated disc, costamere with
  metavinculin). Sponge vinculin sits at cell-cell contacts, so recruitment to
  cell-cell junctions dates at least to the sponge-bilaterian ancestor; the
  beta-catenin interface is untested outside bilaterians in a matched assay.

## Decisions summary

See VCL-ai-review.yaml. Key: protein binding rows converted to talin binding,
alpha-actinin binding, Arp2/3 complex binding, SH3 domain binding where the
paper supports it; others removed. NOT actin binding removed; NEW actin filament
binding. Cadherin binding marked over-annotated (indirect via catenins).
