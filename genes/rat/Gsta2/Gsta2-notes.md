# Gsta2 review notes

## Evidence summary
- [UniProtKB:P04903] UniProt summarizes Gsta2 as catalyzing conjugation of glutathione to diverse electrophilic compounds.
- [PMID:17112229] The fetched GOA file uses this publication for glutathione transferase activity, cytosolic localization, glutathione binding, and xenobiotic catabolism.

## Bromobenzene evidence direction (PMID:17112229)
This paper is often read as evidence that Gsta2 detoxifies bromobenzene metabolites. It shows the
opposite direction of causality: GSTA1/GSTA2 are *targets* of arylation, not catalysts acting on
bromobenzene metabolites. The GST here was simply an abundant hepatic protein recovered on a
GSH-agarose column.
- [PMID:17112229 "Here we report that treatment of rats with bromobenzene results in the site-specific
  modification of Cys-111 in cytosolic glutathione transferase subunits A1 and A2 by bromobenzoquinone."]
- [PMID:17112229 "although the effect of Cys-111 alkylation on the activity of GSTA1 and A2 is not known,
  the distance from this residue to the active site suggests that its modification would not be likely to
  affect catalysis adversely"]

Neither UniProtKB:P04903 nor this paper establishes GSTA2-catalysed conjugation of bromobenzene-derived
epoxides or quinones, so `description` and `core_functions[0]` state the adduction finding rather than a
substrate claim.

## Provenance for the ISO propagation reviews
The five `propagation_review` blocks argue that RGD's mouse-to-rat ISO transfers here are **cluster-level
rather than 1:1**. That claim is verifiable from files in this repo, without relying on MGI subunit
nomenclature (Ya/Yc naming for the mouse donors is *not* sourced in-repo and is deliberately not used as
evidence):
- `genes/rat/Gsta2/Gsta2-goa.tsv` — rat Gsta2 receives ISO from **two** mouse donors, `MGI:MGI:1095417`
  and `MGI:MGI:95863`. Two mouse genes seeding one rat gene is already a many-to-one mapping, not 1:1.
- `genes/rat/Gsta1/Gsta1-goa.tsv` — `MGI:MGI:95863` seeds ISO onto rat *Gsta1* as well, for the **identical
  five terms** it seeds onto rat Gsta2: `GO:0005739`, `GO:0005829`, `GO:0004364`, `GO:0009617`,
  `GO:0035634`. One mouse gene, two rat genes, the same five terms.

Correction (2026-08-07): an earlier revision of these notes claimed rat Gsta1 "receives ISO from nearly the
same mouse donor set (`MGI:95856`, `95861`, `95862`, `95863`, `95864`, `95865`, `1095417`)". That was wrong
— those seven identifiers are the `WITH/FROM` set of rat Gsta1's **IBA** rows under `GO_REF:0000033`, not
ISO donors. Rat Gsta1's only mouse ISO donor is `MGI:MGI:95863`, and `MGI:MGI:1095417` appears in no rat
Gsta1 ISO row at all. Verify with:
`awk -F'\t' '$9=="ISO"{print $5"\t"$11}' genes/rat/Gsta1/Gsta1-goa.tsv`.

Donor identities (checked against the Alliance of Genome Resources API, `https://www.alliancegenome.org/api/gene/MGI:1095417`
and `.../MGI:95863`, retrieved 2026-08-07): `MGI:1095417` = mouse *Gsta1*, "glutathione S-transferase, alpha
1 (Ya)"; `MGI:95863` = mouse *Gsta2*, "glutathione S-transferase, alpha 2 (Yc2)". The Ya/Yc2 subunit naming
in those full names is recorded here only as retrieved provenance; the propagation reviews deliberately do
**not** rest on it, and argue from the GOA donor overlap above instead.

Cluster-level transfer matters asymmetrically by term type, which is why the file's actions differ on the
*same* donors: the class-defining catalytic term `GO:0004364` transfers safely (every alpha-class member has
that activity), whereas compartment (`GO:0005739`) and stimulus-response (`GO:0009617`, `GO:0035634`,
`GO:0061771`) terms are member-specific and do not. Note that the target's own `GO:0004364` IDA row
(PMID:17112229, CAFA) is *not* independent confirmation of catalysis — that paper assays adduction of the
protein and states the effect on activity "is not known".

## Curation decisions
- Core function: glutathione S-transferase alpha-2 (glutathione transferase activity, GO:0004364).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-04

**GOA changes.** Eight new seeded rows. Five are donor splits from mouse Gsta2 (MGI:MGI:95863) of terms previously reviewed with mouse Gsta1 (MGI:MGI:1095417) as donor: glutathione transferase activity, mitochondrion, cytosol, response to bacterium, response to stilbenoid (all ISO, GO_REF:0000121). One is a further cytosol ISO split from human GSTA2 (UniProtKB:P09210). Two are new terms: phospholipid-hydroperoxide glutathione peroxidase activity (GO:0047066, ISS from human GSTA2) and cellular oxidant detoxification (GO:0098869, IEA GO_REF:0000108, inferred from GO:0047066). No retired rows. Total 27 rows.

**Actions.**
- Mouse Gsta2-donor rows: PENDING -> same action as their mouse Gsta1-donor siblings (GST activity ACCEPT; cytosol KEEP_AS_NON_CORE; mitochondrion, response to bacterium, response to stilbenoid MARK_AS_OVER_ANNOTATED). The MGI:MGI:95863 `propagation_review.source_entities` entries that had been written on the sibling rows were moved to the new rows, so each row now carries only its own donor.
- Cytosol ISO from human GSTA2: PENDING -> KEEP_AS_NON_CORE (location confirmed for rat GSTA2 [PMID:17112229 "site-specific modification of Cys-111 in cytosolic glutathione transferase subunits A1 and A2 by bromobenzoquinone"]).
- GO:0047066 ISS from human GSTA2: PENDING -> KEEP_AS_NON_CORE. Donor activity is measured [PMID:10395737 "the catalytic efficiency of hGSTA2-2 for PC-hydroperoxide and PE-hydroperoxide was 317.5 and 353 s-1 mM-1, respectively"]; not measured on rat GSTA2, and secondary to conjugation. PMID:10395737 was fetched and added to references.
- GO:0098869 IEA: PENDING -> KEEP_AS_NON_CORE, following GO:0047066 [PMID:10395737 "the alpha-class GSTs contribute a major portion of GPx activity toward lipid hydroperoxides in human liver"].
- No action changed on existing rows. Donors are now named on the cytosol, GST ISO and GST ISS (mouse Gsta2, P10648) siblings; IDA rows from PMID:17112229 now quote the Cys-111/cytosolic A1/A2 sentence rather than a background sentence; UniProt FUNCTION / SUBCELLULAR LOCATION lines added as positive support.

**Open questions.** Has selenium-independent peroxidase activity toward phospholipid hydroperoxides been measured for purified rat GST A2-2 (Ya2 homodimer)? Which mouse alpha-class gene is the true one-to-one orthologue of rat Gsta2 (both mouse Gsta1 and Gsta2 donate ISO rows)?
