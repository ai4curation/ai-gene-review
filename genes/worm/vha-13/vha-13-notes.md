# vha-13 (Q9XW92) — V-type proton ATPase catalytic subunit A — curation notes

## Identity

- UniProt Q9XW92 (VATA_CAEEL, reviewed), WormBase Y49A3A.2, 606 aa, EC 7.1.2.2.
- Orthologue of human ATP6V1A / yeast Vma1. Belongs to the ATPase alpha/beta chains
  family; carries the F1/V1/A1 alpha/beta N-terminal domain (IPR004100), the
  nucleotide-binding domain (IPR000194) and the ATPase alpha/beta signature (IPR020003).
- Subunit A is the catalytic nucleotide-binding subunit of the cytosolic V1 sector; three
  A/B heterodimers form the hexameric ring in which ATP is hydrolysed at the A–B interface
  (UniProt, by similarity to mammalian ATP6V1A).

## Experimental literature

### Bohnert & Kenyon 2017 (PMID:29168500, full text cached)

- An RNAi screen of ~60 fertility/proteostasis genes identified vha-13 as required for the
  sperm-triggered clearance of protein aggregates in oocytes: "This gene, vha-13, encodes a
  catalytic subunit of the V-ATPase, a lysosomal proton pump" [PMID:29168500].
- The phenotype is shared by the holoenzyme: "Knockdown of other V-ATPase subunits produced
  similar protein-aggregation phenotypes" [PMID:29168500].
- vha-13 is required for lysosomal acidification in the proximal germline: "hermaphrodite,
  but not female, germlines exhibited acidic lysosomes (Fig. 2d, e; Extended Data Fig. 4a)
  that accumulated specifically in maturing, proximal oocytes in a V-ATPase-dependent
  manner" [PMID:29168500].
- Localization: "GFP-tagged VHA-13 was present in proximal, but not distal, germ cells" and
  "As V-ATPase puncta developed, they co-localized with LMP-1::GFP-positive vesicles"
  (LMP-1 = LAMP orthologue, i.e. lysosomes) [PMID:29168500].
- Conclusion: "we conclude that sperm trigger V-ATPase accumulation in proximal oocytes,
  thereby inducing lysosome acidification" [PMID:29168500].
- Translational control: vha-13 mRNA is repressed distally by GLD-1; a tbb-2 3'UTR reporter
  extends GFP::VHA-13 expression distally [PMID:29168500].
- Downstream effects (mitochondrial remodelling, drop in ATP:ADP ratio) are consequences of
  lysosomal activation, not additional molecular functions of vha-13.

### Liegeois et al. 2006 (PMID:16785323, not cached)

- UniProt cites this paper for a role of vha-13 in receptor-mediated endocytosis (the paper
  is primarily about the V0 sector, vha-5/vha-6, and apical exosome secretion in the
  epidermis). Not in the GOA rows for vha-13; not cached, so not used for review decisions.

## Assessment

- All V-ATPase functional annotations (GO:0046961 proton-transporting ATPase activity,
  rotational mechanism; GO:1902600 proton transmembrane transport; V1 domain membership;
  lysosomal membrane) are consistent with the identity of the protein and with the
  experimental lysosome-acidification phenotype.
- The IMP annotation GO:0007042 lysosomal lumen acidification is directly supported by the
  full-text evidence above.
- GO:0046034 ATP metabolic process (IEA from InterPro) is technically true but is a
  by-product of the coupled ATPase; over-annotation relative to the informative transport
  terms.
- Synaptic-vesicle acidification: vha-13 is the sole catalytic A subunit gene in C. elegans,
  so the neuronal V-ATPase that acidifies synaptic vesicles necessarily uses VHA-13, but no
  vha-13-specific neuronal experiment is in the GOA set; no NEW annotation proposed.

## Deep research

- `vha-13-deep-research-falcon.md` (Edison Scientific Literature) corroborates the review:
  it assigns VHA-13 the catalytic A subunit role ("It hydrolyzes MgATP within an A3B3
  catalytic head, and the resulting rotary motion powers V0-mediated proton transport."),
  notes that no purified Q9XW92 kinetics exist, and adds later work not in the GOA set
  (miR-1 regulation of vha-13 in muscle proteostasis; V-ATPase association with HDA-1/NuRD
  during asymmetric division). None of it contradicts the annotation decisions taken here,
  and none of it is used as the sole basis for an action.
