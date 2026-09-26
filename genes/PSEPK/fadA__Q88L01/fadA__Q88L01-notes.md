# Curation notes: *Pseudomonas putida* KT2440 fadA (Q88L01, PP_2136)

These notes record the reasoning behind the two non-routine curation actions in
`fadA__Q88L01-ai-review.yaml`: the `REMOVE` of GO:0010124 and the `NEW`
GO:0036125. No OpenScientist deep-research report was generated for this gene, so
everything below is anchored to the cached UniProt records and GOA tables already
in the repository.

## Identity and family assignment

The reviewed UniProt entry is a HAMAP-rule-typed FadA: the rule `MF_01620` names
the protein *3-ketoacyl-CoA thiolase*, assigns EC 2.3.1.16 and Rhea RHEA:21564,
places it in the fatty acid beta-oxidation pathway, and calls it the
"Fatty acid oxidation complex subunit beta"
[file:PSEPK/fadA__Q88L01/fadA__Q88L01-uniprot.txt "HAMAP; MF_01620; FadA; 1."].

Critically, the PANTHER assignment is to the **FadA-specific subfamily**, not to
the family root:

- `PANTHER; PTHR43853:SF11; 3-KETOACYL-COA THIOLASE FADA; 1.`
- `PANTHER; PTHR43853; 3-KETOACYL-COA THIOLASE, PEROXISOMAL; 1.`

So both UniProt's rule-based typing and its subfamily assignment describe a
beta-oxidation thiolase, and neither mentions aromatic-compound catabolism.

## Why GO:0010124 (phenylacetate catabolic process) is removed

The annotation is a TreeGrafter electronic inference — GOA records it as
`IEA`/`GO_REF:0000118` with `WITH/FROM` = `PANTHER:PTN002466592`
[file:PSEPK/fadA__Q88L01/fadA__Q88L01-goa.tsv]. There is no experimental,
author, or curator-reviewed evidence behind it, so per the repository's guidance
this is an over-propagated electronic inference that may be argued against on
biological grounds rather than a curator judgment to defer to.

The decisive biological argument is that **KT2440 runs phenylacetate catabolism
through a dedicated *paa* operon that has its own thiolase**, curated separately
in this repository:

| Gene | Accession | Locus | Product | GO:0010124 source |
|------|-----------|-------|---------|-------------------|
| paaJ | Q88HS3 | PP_3280 | 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase (EC 2.3.1.174) | TreeGrafter, `PANTHER:PTN001291485` |
| paaH | Q88HS1 | PP_3282 | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) | InterPro2GO, `InterPro:IPR011967` |
| paaF | Q88HR9 | PP_3284 | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) | — (carries GO:0006635 only) |

Two points follow. First, the thiolase step of the phenylacetate route is already
carried out by a different protein: paaJ/PP_3280 is a distinct gene product with
its own EC number and its own beta-oxidation-like chemistry on the ring-cleavage
intermediates. Second, and more telling, paaJ receives GO:0010124 from a
**different TreeGrafter node** (`PTN001291485`) than the one that put the term on
fadA (`PTN002466592`). The phenylacetate term therefore reaches fadA through
thiolase-fold propagation rather than through the node that represents the
phenylacetate pathway itself.

Taken together: the dedicated *paa* route thiolase exists and is separately
annotated, fadA's own subfamily assignment is the FadA beta-oxidation subfamily,
and its HAMAP rule confines it to fatty acid beta-oxidation. GO:0010124 on fadA is
family-wide electronic propagation across the thiolase fold and should be removed
rather than merely flagged.

The paralog context matters for the same reason and is recorded here for
auditability: thiolase-fold propagation of pathway-specific terms is expected to
hit multiple KT2440 thiolases, so the presence of GO:0010124 on this entry is not
evidence of a fadA-specific phenylacetate role.

## Why GO:0036125 (fatty acid beta-oxidation multienzyme complex) is added

UniProt states the quaternary structure explicitly:
"Heterotetramer of two alpha chains (FadB) and two beta chains (FadA)"
[file:PSEPK/fadA__Q88L01/fadA__Q88L01-uniprot.txt]. The corresponding alpha
subunit is curated in this repository as `genes/PSEPK/fadB`. GOA carries no
cellular-component term for this complex on Q88L01 — only GO:0005737 cytoplasm —
so the `part_of` complex annotation is a genuine gap rather than a
re-statement of an existing term, and it is asserted at the level UniProt
actually supports (complex membership, not a new molecular function).

## Open point

The chain-length range over which the FadBA complex operates, relative to the
other KT2440 thiolase paralogs, is not established by any record consulted here;
it is carried in `suggested_questions` rather than asserted.
