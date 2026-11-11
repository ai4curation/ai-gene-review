# SCHPO vma1 curation notes

## Summary

S. pombe vma1 encodes the catalytic A subunit of the vacuolar H+-ATPase V1
sector. The core biology is straightforward: Vma1 binds and hydrolyzes ATP in
the peripheral V1 sector and, as a subunit of the assembled V1/V0 V-ATPase at
the fungal vacuole membrane, contributes to rotary ATP-driven proton pumping
that acidifies the vacuole.

## Cached S. pombe evidence

- PMID:14735354 is the direct S. pombe disruption paper, but the cached text is
  abstract-only. The abstract states that Iwaki et al. disrupted "the gene vma1
  encoding subunit A or vma3 encoding subunit c", that the two deletion mutants
  "lost the capacity for vacuolar acidification in vivo", and that FM4-64
  delivery to the vacuolar membrane and Lucifer Yellow CH accumulation were
  strongly inhibited in the vma1 and vma3 mutants. This supports vma1's role in
  vacuolar acidification/proton pumping, but the full text would be needed to
  independently verify PomBase's exact V1-domain orthology-transfer row.
- The UniProtKB P31406 flat file consistently places vma1 in the V-ATPase
  catalytic subunit family: PTHR43607/SF1 and InterPro signatures for the
  V1-complex A subunit, the F1/V1/A1 ATPase nucleotide-binding domain, and
  V-ATPase subunit A.

## PAINT nodes

The three VMA1 PAINT nodes inherited by fission yeast are well aligned with the
protein's family placement and with the experimental S. pombe acidification
phenotype.

- PTN000389800 is at the PTHR43607 family root and assigns
  `GO:0046961` proton-transporting ATPase activity, rotational mechanism and
  `GO:1902600` proton transmembrane transport.
- PTN000389802 is at Eukaryota and assigns `GO:0000221` vacuolar
  proton-transporting V-type ATPase, V1 domain.
- PTN001032540 is at Fungi and assigns `GO:0000329` fungal-type vacuole
  membrane.

The S. pombe protein is in the same PTHR43607:SF1 A-subunit family as the seed
fungal VMA1 proteins, so none of the PAINT rows need pruning.

## Newer literature search

I searched PubMed and the web for newer primary papers with combinations of
`Schizosaccharomyces pombe`, `vma1`, `SPAC343.05`, and `V-ATPase`. The later
hits I found use vma1 deletion as the established V-ATPase-defective /
acidification-defective comparator in vacuolar pH, Btn1/CLN3, cell-wall,
vacuolar amino-acid-pool, and other physiology studies. I did not find a newer
primary paper that revises the direct molecular assignment made here: Vma1 is
the conserved catalytic V1 A subunit of the vacuolar V-ATPase.

## Annotation decisions

- Accepted the PAINT `GO:0046961` and `GO:1902600` root-node assertions.
  Vma1 contributes the catalytic A subunit to the V1/V0 proton pump, and the
  2004 disruption phenotypes support a direct role in vacuolar acidification.
- Added `GO:0007035` vacuolar acidification as a `NEW` row because Iwaki et
  al. directly observed loss of vacuolar acidification after vma1 deletion and
  the term is complementary to, rather than an ancestor of, the existing
  `GO:1902600` proton transmembrane transport rows.
- Accepted `GO:0000221` V1-domain membership from the Eukaryota PAINT node and
  from PomBase ISO to budding yeast. The cached PMID is abstract-only, so the
  review defers to PomBase for the exact full-text support.
- Accepted the fungal `GO:0000329` vacuole membrane PAINT row. It is more
  precise than the generic `GO:0005774` vacuolar membrane rows, which were
  marked `TOO_GENERAL`.
- Accepted ATP binding and ATP hydrolysis as core subunit-A activities.
- Modified the electronic `GO:0033180` parent complex to the more precise
  `GO:0000221` vacuolar V-type V1 domain.
- Marked `GO:0046034` ATP metabolic process as over-annotated: the ATPase
  reaction is the energy-coupling step for vacuolar proton transport, not a
  gene-level role in ATP metabolism.
