# nqo1 (Q56222, Thermus thermophilus HB8) notes

Reviewed 2026-11-02 as the reference protein of PANTHER:PTHR43578 for the
bacterial_respiratory_complex_i module. Deep-research providers are unavailable in
this environment (no API keys), so the review rests on the curated UniProt record
and the cached abstract of the peripheral-arm structure paper.

- Nqo1 is the NADH/FMN subunit: "The Nqo1 subunit contains the NADH-binding site and
  the primary electron acceptor FMN." [file:THET8/nqo1/nqo1-uniprot.txt, CC FUNCTION,
  ECO:0000269 PubMed:16469879]
- The acceptor of T. thermophilus NDH-1 is menaquinone [same CC FUNCTION], so the
  ubiquinone-specific GO:0008137 from InterPro2GO is modified to GO:0016655.
- FMN within electron transfer distance of cluster N3 [PMID:16469879 "The primary
  electron acceptor, flavin-mononucleotide, is within electron transfer distance of
  cluster N3"].
- The ARBA hydrogenase term GO:0016696 (H2 donor) is removed.
