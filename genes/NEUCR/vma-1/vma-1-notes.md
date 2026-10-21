# vma-1 manual review notes

- `vma-1` / `NCU01207` encodes UniProtKB `P11592`, a reviewed Neurospora V-type
  proton ATPase catalytic subunit A record in PANTHER family `PTHR43607`
  [file:genes/NEUCR/vma-1/vma-1-uniprot.txt].
- The PTHR43607 PAINT export is internally aligned with the seeded IBA rows and
  should be read as curated ancestral-node evidence rather than pairwise
  similarity. `PTN000389800` is the family-root node for
  `GO:0046961 proton-transporting ATPase activity, rotational mechanism` and
  `GO:1902600 proton transmembrane transport`; `PTN000389802` is the
  Eukaryota node for `GO:0000221 vacuolar proton-transporting V-type ATPase,
  V1 domain`; and `PTN001032540` is the Fungi node for
  `GO:0000329 fungal-type vacuole membrane`
  [file:interpro/panther/PTHR43607/PTHR43607-paint.tsv].
- The local UniProt record supports the same model by describing P11592 as the
  catalytic subunit of the V1 complex of the vacuolar V-ATPase, placing it at
  the cytoplasmic side of the vacuole membrane, and recording conserved ATPase
  alpha/beta-chain, InterPro, and PANTHER classifications
  [file:genes/NEUCR/vma-1/vma-1-uniprot.txt].
- PMID:8722770 was fetched only as an abstract. It directly supports the genetic
  importance of `vma-1` in Neurospora but does not add a more specific
  molecular function, complex, or localization term beyond the family-backed
  V-ATPase model.
- Searches for newer `Neurospora crassa` `vma-1`, `NCU01207`, and V-ATPase
  papers found the classic 1988 cloning and 2000 phenotyping work plus later
  microscopy papers that use VMA-1-tagged strains as vacuolar-system markers.
  I did not find a newer direct primary paper that changes the catalytic
  subunit A model or justifies a nonredundant `NEW` GO annotation for this
  review.
