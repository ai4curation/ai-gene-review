# acl1 (SPBC1703.07, UniProt Q9P7W3) notes

Fetch: `just fetch-gene SCHPO acl1` FAILED ("Could not find any UniProt ID ... for gene acl1 in SCHPO";
UniProt has no gene name for this entry, only ORFNames=SPBC1703.07). Fetched with
`uv run ai-gene-review fetch-gene SCHPO acl1 -u Q9P7W3 -o genes` and moved into genes/SCHPO/acl1.
Accession verified: ACL1_SCHPO, Q9P7W3, 615 aa.

## Evidence (all homology-based)
- [UniProt:Q9P7W3] "Catalyzes the formation of cytosolic acetyl-CoA, which is mainly used for the biosynthesis of fatty acids and sterols" (ECO:0000250);
  EC 2.3.3.8; "Composed of two subunits" (ECO:0000250); belongs to the succinate/malate CoA ligase alpha subunit family.
- Domains: CoA_binding (PF02629), Ligase_CoA (PF00549), Citrate_synt (PF00285) => C-terminal half of animal ACLY / plant ACL-B.
  Partner acl2 (SPAC22A12.16, O13907) is the N-terminal (ATP-grasp) half; PANTHER places it in a different family (module note).
- Localization: ORFeome HDA cytosol + nucleus (PMID:16823372).
- No S. pombe enzymology cached. S. cerevisiae has no ACL orthologue (uses ACS1/ACS2) - no budding-yeast review to align to;
  aligned to genes/human/ACLY instead (core MF GO:0003878, cytosol; catalytic activity / GO:0046912 parents handled the same way).

## GO-CAM
- gomodel:678073a900002931: acl1 (6792e70800000110) and acl2 (6792e70800000118) each enable GO:0003878 in cytosol, part_of GO:0006633. Agrees.

## Decisions
- Core MF GO:0003878, BP GO:0006085, cytosol, in_complex GO:0140615 (ATP-dependent citrate lyase complex).
- catalytic activity -> MODIFY to GO:0003878; GO:0046912 MARK_AS_OVER_ANNOTATED (parent); nucleus KEEP_AS_NON_CORE.
