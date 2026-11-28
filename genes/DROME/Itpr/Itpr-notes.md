# Itpr (Inositol 1,4,5-trisphosphate receptor) notes

Gene: Itpr (synonyms dip, InsP3R, Itp-r83A), FBgn0010051, CG1063. UniProt P29993 (Swiss-Prot,
ITPR_DROME, 2837 aa, isoform B "head" displayed; isoform A "embryo" lacks residues 980-988).
This is the only fly UniProt entry for the gene (UniProt query xref:flybase-FBgn0010051 returns
only P29993), so the review covers every GOA row on the gene (51 rows).

## Sources and searches (2026-11-17)

- Cached GOA references: 20 PMIDs. Full text available for PMID:16216922, PMID:19680544,
  PMID:22928859, PMID:23471909, PMID:25306920, PMID:26544939, PMID:27605706, PMID:28660247,
  PMID:29017032, PMID:29444420. The rest are abstract-only (PMID:1322910, PMID:10833300,
  PMID:11333238, PMID:12398933, PMID:15356199, PMID:16540404, PMID:16899722, PMID:20107057,
  PMID:28726639).
- FlyBase hand-written description (`Itpr-deep-research-flybase.md`), fetched 2026-11-17. No
  Falcon/Perplexity deep research was run for this batch.
- PubMed queries run (E-utilities, 2026-11-17):
  - `Srikanth S[au] AND Drosophila AND trisphosphate receptor` (5 hits; found the bilayer study
    PMID:15189860).
  - `Drosophila AND (InsP3 receptor OR IP3 receptor OR itpr) AND (muscle OR sarcoplasmic reticulum)`
    (15 hits; PMID:7556937 muscle expression, PMID:28726639 muscle RNAi; no fly study localises the
    receptor to the sarcoplasmic reticulum by name).
  - `Drosophila AND (InsP3 receptor OR IP3 receptor OR itpr) AND plasma membrane` (30 hits; none
    reports a plasma-membrane pool of the fly receptor; hits concern ER-PM junctions, SOCE and
    PIP2 resynthesis).
  - `Drosophila AND (InsP3 receptor OR IP3 receptor OR itpr) AND (secretory granule OR dense core
    vesicle OR secretory vesicle)` (2 hits: PMID:33155978 presynaptic IP3R in dopaminergic neurons,
    PMID:26544939 vesicle-mediated ecdysone secretion; neither places the receptor on a granule
    membrane).
  - `Drosophila AND (InsP3 receptor OR IP3 receptor OR itpr) AND (phosphatidylinositol
    4,5-bisphosphate OR PIP2 binding)` (12 hits; none tests binding of a phosphoinositide lipid to
    the fly receptor).
- Newly cached and quoted: PMID:15189860 (Srikanth et al. 2004, abstract), PMID:7556937 (Raghu and
  Hasan 1995, abstract), PMID:9208856 (Acharya et al. 1997, abstract).
- PANTHER tree (PANTHER 19 treeinfo for PTHR13715, downloaded to scratch, not committed) used to place
  the PAINT nodes; PAINT IBD rows from `interpro/panther/PTHR13715/PTHR13715-paint.tsv` in the
  coordinator checkout.

## Channel biochemistry

- Cloned fly receptor binds IP3 [PMID:1322910 "The polypeptide encoded by the cDNA was functionally
  expressed and showed characteristic InsP3-binding activity."]. Fly has one IP3R gene
  [PMID:16216922 "Drosophila possesses a single insect-specific InsP3 receptor isoform"].
- Single-channel recordings of the head and embryo splice forms in planar bilayers
  [PMID:15189860 "the major functional properties of DmInsP(3)R (conductance, gating, and
  sensitivity to InsP(3) and Ca(2+)) are remarkably conserved with the mammalian InsP(3)R1"];
  a coupling-domain mutant changes Ca2+ regulation [PMID:15189860 "wc703 channels have increased
  sensitivity to modulation by Ca(2+)"]. So the fly channel is gated by IP3 and regulated by
  cytosolic Ca2+, as mammalian IP3Rs are; IP3Rs have no EF-hand, and the Ca2+ sites in mammalian
  cryo-EM structures are in the cytoplasmic region (seed PMID:37898605 on human ITPR3).
- IP3 injection releases Ca2+ in syncytial embryos [PMID:16216922 "Fig. 3 A shows that InsP3
  receptors are functional in early embryos; the microinjection of InsP3 leads to calcium
  release."].
- GPCR-PLC coupling in S3 cells: the GBP cytokine raises Ins(1,4,5)P3 and its Ca2+ mobilisation needs
  Itpr [PMID:22928859 "The addition of dsRNA (double-stranded RNA) to knock down expression of the
  Drosophila Ins(1,4,5)P3 receptor almost completely eliminated mobilization of intracellular Ca2+
  stores by dGBP."]. In the prothoracic gland a Gq-PLC-IP3R axis controls ecdysone release
  [PMID:26544939 "these results indicate that the calcium mobilization from intracellular stores
  through IP3R is regulated by GPCR(s) in the PG"].

## Localization

- ER: GFP-IP3R (functional; rescues the null) labels intracellular membranes and is used as a
  smooth-ER marker in neurons [PMID:27605706 "we generated an additional SER marker, a GFP-tagged
  IP3 receptor (UAS-GFP-IP3R)"]; [PMID:27605706 "Thus the tagged IP3R is functional."]; it moves to
  regenerating axon tips with the smooth ER [PMID:27605706 "After axotomy, GFP-IP3R was often seen to
  accumulate near the regenerating axon tip"].
- Muscle: protein in proliferating myoblasts [PMID:7556937 "Our results suggest that in Drosophila
  the IP3 signalling pathway is used during muscle development, primarily when myoblasts undergo
  rapid multiplication, in both embryos and pupae."]; mRNA abundant in legs and thorax
  (PMID:1322910); muscle-specific RNAi reduces mitochondrial Ca2+ uptake (UniProt DISRUPTION
  PHENOTYPE, PMID:28726639). Together these place the receptor in the muscle ER (the sarcoplasmic
  reticulum), but no fly study names the SR or co-stains an SR marker.
- No fly evidence for a plasma-membrane pool or a secretory-granule pool (searches above).

## Physiology (Ca2+ release in specific cells)

- Flight: mutants flightless; rescued in aminergic neurons [PMID:15356199 "Drosophila mutants for
  the inositol 1,4,5-trisphosphate (InsP(3)) receptor gene (itpr) are flightless."];
  [PMID:16899722 "In Drosophila, InsP3R activity is required in aminergic interneurons during pupal
  development for normal flight behavior."]; insulin-producing neurons also rescue
  (PMID:20107057).
- Larval feeding and growth via insulin-producing cells (PMID:19680544); adult obesity and
  hyperphagia (PMID:23471909); fat-body IP3R needed for starvation-induced lipolysis and Upd2
  release control (PMID:29017032).
- Ecdysone release from the prothoracic gland (PMID:26544939); molting interaction with rut
  (PMID:11333238).
- Autophagy in dying salivary glands (PMID:25306920); ethanol tolerance in perineurial glia
  (PMID:29444420); ER-to-mitochondria Ca2+ transfer in oxidative stress, with MCU (PMID:28726639);
  sugar taste (PMID:16540404).
- Not phototransduction: [PMID:10833300 "These results indicate that InsP(3)R-mediated store
  depletion does not underlie TRP and TRPL activation in Drosophila photoreceptors."];
  [PMID:9208856 "demonstrate that phototransduction, a model PLC pathway thought to require InsP3R,
  does not require InsP3R for signaling."]; [PMID:28660247 "we found no effect of IP3R RNAi or
  mutation on photoreceptor responses or Ca2+ signals, indicating that the IP3R plays little or no
  role in Drosophila phototransduction."].

## PAINT nodes (PTHR13715, PANTHER 19 tree)

Note: UniProt's PANTHER cross-reference gives PTHR45816:SF4 ("MIR domain-containing protein"), but
the PANTHER 19 tree of PTHR45816 has no fly leaf, and the IBA nodes are in PTHR13715. Path from the
root to fly Itpr: PTN000346458 (Eukaryota) > PTN008550775 (Unikonts) > PTN008550776 (duplication)
> PTN008550777 (Metazoa-Choanoflagellida, SF102) > PTN008550778 (Eumetazoa DUPLICATION: RyR clade
PTN008550779 vs IP3R clade) > PTN001010185 (Eumetazoa IP3R clade) > PTN000346545 (Bilateria) >
PTN008550794 (Ecdysozoa) > PTN008550795 (Arthropoda) > PTN008550796 > PTN000346644 (Diptera) > fly leaf.

- PTN001010185 (IP3R clade): ER membrane, IP3-gated channel, IP3 binding, PLC-GPCR pathway (all
  seeded with fly Itpr or with mammalian ITPR1-3), and the four non-duplicative terms: calcium ion
  binding (rat Itpr2/Itpr3, human ITPR3 IDA PMID:37898605, a Ca2+-bound cryo-EM study), plasma
  membrane (rat Itpr1/Itpr3, human ITPR2/ITPR3; human seeds PMID:10828023 platelet surface biotinylation and
  PMID:21062895 TIRF at ER-PM junctions), secretory granule membrane (human ITPR1, bovine ITPR2 Q8WN96) and
  phosphatidylinositol binding (mouse Itpr1/2/3; their MGI IDA rows cite PMID:17327232, PMID:8663526
  and PMID:8063813, and UniProt adds PMID:20813840 on mouse Itpr1. By title (QuickGO and PubMed,
  2026-11-17; papers not read): isoform-specific IP3-binding affinity; mutational analysis of the IP3
  binding site; IP3R mRNA isoform ratios by PCR; Tyr-167/Trp-168 coupling of ligand binding to
  opening. None is about phosphoinositide lipids; the two binding studies are about soluble IP3).
  GO:0070679 (IP3 binding) is under alcohol binding, not under GO:0035091, so the lipid term names a
  different ligand.
- PTN008550778 (the duplication node above both RyR and IP3R clades): sarcoplasmic reticulum,
  seeded only by mammalian IP3Rs (mouse Itpr1/Itpr2, rat Itpr1/Itpr2, human ITPR2).
- PTN008550777: release of sequestered calcium ion into cytosol (seeded with fly Itpr).
- No PAINT loss on the arthropod or insect IP3R branch.

## FlyBase description check

"Inositol 1,4,5,-trisphosphate receptor (Itpr) encodes an intracellular ligand gated calcium channel.
It functions downstream of G-protein coupled receptors that activate Gq/PLCbeta signaling and generate
inositol tris-phosphate. Itpr depletion affects ecdysone release, response to nutritional stress, lipid
metabolism and flight."

- Channel: PMID:1322910, PMID:15189860. Downstream of Gq/PLC GPCRs: PMID:22928859, PMID:26544939.
  Ecdysone release: PMID:26544939. Nutritional stress and lipid metabolism: PMID:23471909,
  PMID:29017032. Flight: PMID:15356199, PMID:16899722. All traced; nothing wrong. Missing: ER
  location, larval feeding/growth, the negative phototransduction result.

## UniProt FUNCTION check

- "Receptor for inositol 1,4,5-trisphosphate ... release of intracellular calcium" - correct.
- "Together with MCU, has a role in oxidative stress-induced ER-mitochondria calcium transfer" -
  matches PMID:28726639.
- "May be involved in visual and olfactory transduction, and myoblast proliferation
  (PubMed:1322910)" - the visual part is outdated: mosaic and null photoreceptors transduce light
  normally (PMID:9208856, PMID:10833300, PMID:28660247). The myoblast part is an expression-based
  suggestion that comes from the later antibody study (PMID:7556937), not from PMID:1322910, and no
  later study tested it. The olfactory part is an expression-based hedge.
- "May be involved in ethanol tolerance" - matches PMID:29444420.
