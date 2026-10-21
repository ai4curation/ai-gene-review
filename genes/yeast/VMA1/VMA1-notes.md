# VMA1 review notes

## Scope

`VMA1` / `TFP1` encodes the catalytic A subunit of the *S. cerevisiae*
V-type H+-ATPase. The `P17255` primary translation product is unusual: a
PI-SceI/VDE homing-endonuclease intein interrupts the V-ATPase A subunit, and
protein splicing joins the N- and C-terminal exteins to produce the mature
69-kDa V1 catalytic subunit [PMID:2139027, PMID:2146742].

The review therefore separates two real activities that are present in the same
translated precursor:

- mature Vma1p: ATP hydrolysis in the peripheral V1 motor, coupled to VO proton
  translocation in vacuolar and Golgi/endosomal V-ATPase holoenzymes;
- PI-SceI/VDE: the excised intein endonuclease, which accounts for the
  InterPro-derived DNA-binding, endonuclease, and intein-protein-splicing rows.

## PAINT/IBA rows

The PTHR43607 PAINT rows fit VMA1 and do not need pruning.

- `PTN000389800` is the PTHR43607 root call for `GO:0046961
  proton-transporting ATPase activity, rotational mechanism` and `GO:1902600
  proton transmembrane transport`. Yeast Vma1p is the catalytic A subunit of a
  rotary V-ATPase, and there is no evidence of subactivity loss.
- `PTN000389802` is the eukaryotic node for `GO:0000221 vacuolar
  proton-transporting V-type ATPase, V1 domain`. This is directly supported by
  yeast V1/V1VO structural and biochemical work.
- `PTN001032540` is the fungal node for `GO:0000329 fungal-type vacuole
  membrane`, seeded by *Candida albicans* TFP1 and *S. cerevisiae* VMA1; this
  is correct for the Vph1-containing yeast V-ATPase.

## Annotation decisions

- Accepted V1-domain, V-type ATPase complex, rotary ATPase, proton-transport,
  fungal-type vacuole membrane, vacuolar acidification, endosomal acidification,
  and Golgi acidification rows.
- Changed broad `GO:0005774 vacuolar membrane` rows to `MODIFY` with
  `GO:0000329 fungal-type vacuole membrane`, because the fungal child term is
  already directly supported.
- Kept the PI-SceI/VDE intein `GO:0003677 DNA binding`, `GO:0004519
  endonuclease activity`, and `GO:0016539 intein-mediated protein splicing`
  rows as non-core precursor/intein activities.
- Changed the broader `GO:0030908 protein splicing` row to `MODIFY` toward
  `GO:0016539 intein-mediated protein splicing`.
- Kept `GO:0005524 ATP binding` as a non-core catalytic-site subactivity, not
  as a separate core function.
- Kept the high-throughput `GO:0003729 mRNA binding` row as non-core. The
  cached full text reports Vma1 among unexpected mRNA-interactome hits under
  glucose deprivation, but its Vma1-specific RNA biology remains speculative.
- Removed the generic `GO:0005515 protein binding` rows for Rav1p and Vma6p.
  The physical interactions are plausible and in several cases expected, but
  they do not state a molecular function more specific than the accepted
  V-ATPase catalytic activity and complex-membership rows.
- Marked the InterPro-derived `GO:0046034 ATP metabolic process` row as
  over-annotated. The ATP turnover is the chemical driver of proton pumping, not
  an informative VMA1 biological-process context.

## Newer literature search

The 2022 cryo-EM paper on V1/VO reversible dissociation
(`PMID:35469063`) fetched successfully as an abstract-only cached publication
and was added as newer structural context.

PubMed/PNAS searches also identified the 2024 RAVE/V1 cryo-EM paper
`PMID:39625975` / `PMCID:PMC11648922`, "Structure of yeast RAVE bound to a
partial V1 complex". It is relevant to the Rav1p/Vma1p interface and to RAVE
reassembly of the V1 sector with VO, but `just fetch-pmid 39625975` hit an
NCBI `429 Too Many Requests` response during this pass, so the paper was not
added to the YAML.
