# TFP1 curation notes

## Family and PAINT

TFP1 encodes C. albicans Q5AJB1, a 617 aa V-type proton ATPase catalytic subunit
A. PANTHER places it in PTHR43607:SF1, "H(+)-TRANSPORTING TWO-SECTOR ATPASE",
alongside S. cerevisiae VMA1, S. pombe vma1, and N. crassa vma-1.

For PTHR43607, the IBA rows in the seeded review correspond to three PAINT node
assertions:

- `PTN000389800`, the family root, carries `GO:0046961`
  proton-transporting ATPase activity, rotational mechanism and `GO:1902600`
  proton transmembrane transport.
- `PTN000389802`, the eukaryotic node, carries `GO:0000221` vacuolar
  proton-transporting V-type ATPase, V1 domain.
- `PTN001032540`, the fungal node, carries `GO:0000329` fungal-type vacuole
  membrane and is seeded by both CGD:CAL0000187512 and SGD:S000002344.

All three PAINT placements match Tfp1 biology. Tfp1 has no apparent
lineage-specific loss or retargeting relative to these nodes, and the C.
albicans experimental record is one of the fungal-node sources rather than a
circular defect.

## Local and web literature check

`just fetch-pmid 25220074` initially hit an NCBI 429 during seeding; I retried
it once and cached the PubMed record successfully. The publication is still
abstract-only locally (`full_text_available: false`), so exact YAML quotes from
Jia et al. 2014 are limited to the PubMed abstract rather than the full
ScienceDirect article. The abstract identifies Tfp1 as a putative V-ATPase
subunit and states that "Tfp1 played an essential role in vacuolar acidification
and endocytic trafficking" [PMID:25220074].

I also searched for later TFP1-focused work and cached two abstract-only
follow-ups from the same group. Jia et al. 2015 found that `TFP1` deletion
perturbed iron, copper, calcium, fluconazole, and GlcNAc physiology, including
"generation of an iron starvation signal and reduced total iron content" that
the authors connected to copper-dependent Fet34p mislocalization
[PMID:26255859]. Jia et al. 2018 used a `tfp1` background to examine PMC1 and
reported that deleting the vacuolar calcium pump in the `tfp1` mutant "led to
more severe dysregulation of calcium homeostasis" [PMID:29086141].

## Annotation decisions

The core retained activity is ATP hydrolysis by Tfp1 in the peripheral V1
sector, contributing to the V-ATPase holoenzyme's rotary proton-pumping activity
at the fungal vacuole membrane. I accepted the PAINT root/eukaryotic/fungal node
assertions because they place conserved functions at the right depth: rotary
proton pump contribution and proton transport are ancestral to PTHR43607, the V1
sector is eukaryotic, and fungal-type vacuole membrane is a fungal
specialization.

The generic `GO:0033180` V-type ATPase V1-domain row should be refined to the
vacuolar V1 term `GO:0000221`, and the generic `GO:0005774` vacuolar membrane
rows should be refined to `GO:0000329`. The InterPro `GO:0046961` row shares the
same term as the accepted PAINT row and should be kept consistently; the PAINT
`contributes_to` row is the one that precisely scopes Tfp1 as the
ATP-hydrolyzing A subunit that contributes to the proton-transporting ATPase
activity of the complete V1-V0 pump.

The `GO:0006897` endocytosis and `GO:0034599` cellular response to oxidative
stress IMP rows from Jia et al. 2014 look phenotype-driven. They are useful
readouts of failed vacuolar/endosomal acidification and pH-ion homeostasis, but
the abstract does not support Tfp1 directly executing an endocytic trafficking
step or the oxidative-stress response. I marked both over-annotated rather than
removing the rows.
