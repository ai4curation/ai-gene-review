# gcvH (Q5FRY1, GOX1096) — Gluconobacter oxydans 621H — curation notes

Reviewer notes and journal for the ai-gene-review of the glycine cleavage system H
protein of *Gluconobacter oxydans* 621H. No deep-research provider was available for
this run (no API keys in the environment), so the literature work below is my own and
every assertion carries its source inline. Nothing here was taken from a generated
deep-research file, and no such file was created.

## 1. What the entry is

Q5FRY1 is an unreviewed (TrEMBL) entry, 119 AA, from the *G. oxydans* 621H reference
proteome UP000006375, locus tag GOX1096, sequenced in the 621H genome project
[PMID:15665824 "chromosome consists of 2,702,173 base pairs and contains 2,432 open
reading frames"]. The whole functional annotation of the entry comes from one curated
UniRule system, HAMAP MF_00272 (GcvH):

- Name and gene symbol: `RecName: Full=Glycine cleavage system H protein
  {ECO:0000256|HAMAP-Rule:MF_00272}`, `Name=gcvH {ECO:0000256|HAMAP-Rule:MF_00272}`.
- Function: [file:GLUOX/gcvH/gcvH-uniprot.txt "The glycine cleavage system catalyzes
  the degradation of glycine. The H protein shuttles the methylamine group of glycine
  from the P protein to the T protein"].
- Cofactor: [file:GLUOX/gcvH/gcvH-uniprot.txt "Binds 1 lipoyl cofactor covalently"],
  with `MOD_RES 59 /note="N6-lipoyllysine"` (HAMAP plus PIRSR617453-50).
- Subunit: [file:GLUOX/gcvH/gcvH-uniprot.txt "The glycine cleavage system is composed
  of four proteins: P, T, L and H"].

Independent signature support for family membership is strong and comes from several
resources that do not derive from one another: NCBIfam TIGR00527 (gcvH) and NF002270,
Pfam PF01597 (GCV_H), CDD cd06848 (GCS_H), PROSITE PS00189 (LIPOYL) and PS50968
(BIOTINYL_LIPOYL, as the 18..100 lipoyl-binding domain), SUPFAM SSF51230, PANTHER
PTHR11715, and HAMAP MF_00272 itself. `PE 3: Inferred from homology` — there is no
experimental work on this protein in this organism, and the `Lipoyl` keyword's other
evidence tag is ARBA, which is an unvetted prediction and is not quoted as support.

The only "SIMILARITY" line carries both ARBA and HAMAP evidence
(`{ECO:0000256|ARBA:ARBA00009249, ECO:0000256|HAMAP-Rule:MF_00272}`); I treat it as
usable because the HAMAP tag is a curated UniRule, not because of the ARBA tag.

## 2. Genomic context: the pathway is present, and that matters

I surveyed the 621H proteome for the glycine cleavage system and the lipoyl-attachment
machinery (`gcvH-bioinformatics/survey_gcs_and_lipoylation.py`, results in
`gcvH-bioinformatics/RESULTS.md`). Findings:

- All four GCS subunits are encoded: P = Q5FRY0 (gcvP / GOX1097), H = Q5FRY1 (gcvH /
  GOX1096), T = Q5FRY2 (GOX1095), L = Q5FNM2 (GOX2292, dihydrolipoyl dehydrogenase).
- GOX1095-GOX1096-GOX1097 are three consecutive locus tags, i.e. the canonical
  bacterial `gcvTHP` cluster. The H protein is in an operon with exactly the two
  subunits its lipoyl arm shuttles between.

This is what lifts the GO:0005960 and GO:0019464 annotations above bare family
membership: the partners each step needs are present, and the gene neighbourhood is
the one the pathway is normally found in.

- Lipoylation route: LipB-type octanoyltransferase Q5FUX5 (lipB / GOX0046) plus LipA
  lipoyl synthase Q5FNM1 (lipA / GOX2293) are present. No LipM or LipL could be found.

## 3. The one call I make differently from the existing METEA/gcvH review

`GO:0009249 protein lipoylation`, propagated onto Q5FRY1 by TreeGrafter from
PANTHER:PTN000196926, is marked over-annotated here. The existing review at
`genes/METEA/gcvH` ACCEPTed the same term on the grounds that GcvH carries the
lipoylated lysine. I do not follow that, for three reasons.

First, being lipoylated is being the **substrate** of lipoylation. CLAUDE.md's
participation test is explicit that "being the thing it acts on is not participation";
the enzymes that do the work of `protein lipoylation` are the octanoyltransferase and
the lipoyl synthase, i.e. LipB (GOX0046) and LipA (GOX2293) in this organism.

Second, GcvH *does* genuinely participate in lipoylation in one clade, and that clade
is defined by enzymes *G. oxydans* does not have. In *Bacillus subtilis*, LipM
octanoylates GcvH and LipL then amidotransfers the group onto the E2 subunits, which
makes octanoyl-GcvH a mandatory waypoint: [PMID:21338421 "GcvH was an obligate
intermediate in the modification of E2PdhC"], and the same paper puts it plainly that
[PMID:21338421 "GcvH is both a substrate and a required component of the lipoic acid
biosynthesis pathway"]. That relay is absent where a LipB is present: the authors
showed that [PMID:21338421 "the expression of the E. coli lipB gene in a ΔgcvH mutant
strain restored growth in minimal medium"] and concluded that [PMID:21338421 "the LipB
octanoyl transferase activity was sufficient to overcome the absence of GcvH"].
*G. oxydans* 621H has LipB and no detectable LipM/LipL, so the donor role does not
transfer to it.

Third, the comparator check agrees. *B. subtilis* GcvH (O32174), which runs the relay,
carries GO:0009249 by IMP from PMID:21338421 and also GO:0009107 lipoate biosynthetic
process. *E. coli* GcvH (P0A6T9), which does not, carries neither — its GOA has only
GO:0019464, GO:0005960, GO:0005829, GO:0005737 and GO:0006730 (QuickGO annotation
search for each accession, run 2026-10-28). The absence in *E. coli* is the convention,
not an oversight, and *G. oxydans* is on the *E. coli* side of the line.

The honest caveat, recorded in RESULTS.md too: my LipM/LipL search was by UniProt gene
and protein name within a TrEMBL proteome, not a profile-HMM search of the genome, so
"absent" means "not annotated as present". That is why the call is
`MARK_AS_OVER_ANNOTATED` and not `REMOVE`.

## 4. The process term: does GcvH do any of the work of glycine decarboxylation?

This is the question CLAUDE.md's participation test is for, and the answer is yes, by a
route that needs stating rather than assuming. GcvH catalyses nothing. But the
aminomethyl group released by the P protein's decarboxylation of glycine is not free in
solution at any point: it is transferred onto the distal sulfur of GcvH's covalently
bound lipoyl arm, carried as S-aminomethyl-dihydrolipoyl-GcvH, and presented to the T
protein, which consumes it with tetrahydrofolate. UniProt's HAMAP text states exactly
this relationship — the H protein "shuttles the methylamine group of glycine from the P
protein to the T protein" — and the cofactor that does the shuttling is GcvH's own
[file:GLUOX/gcvH/gcvH-uniprot.txt "Binds 1 lipoyl cofactor covalently"].

So GcvH supplies the cofactor activity that two of the pathway's steps depend on, and
holds the intermediate in position between two active sites. In CLAUDE.md's own
taxonomy of substrate exceptions that is the thyroglobulin/fibrin shape — scaffold and
cofactor — not the angiotensinogen shape. The comparator check points the same way:
*E. coli* GcvH and *B. subtilis* GcvH both carry GO:0019464, so GO's convention plainly
admits the H protein to this process. `ACCEPT`.

Note that this reasoning is also what distinguishes GcvH from the `genes/PSEPK/ureA`
precedent for complex subunits. ureA is a non-catalytic chain whose contribution is
structural, so it takes `structural molecule activity` plus `contributes_to` the
catalytic activity that lives on another chain. GcvH is not in that position: carrying
a substrate between active sites on a covalently tethered cofactor is a molecular
function of its own, with its own GO term (GO:0140104 molecular carrier activity),
and no catalytic activity of the P, T or L proteins should be attributed to it even by
`contributes_to`.

## 5. CMMMech grounding: Q5FRY1 is linked to the wrong locus

This is the finding with consequences outside this review. **CMMMech is read-only here
and I have not edited it; this section is the record.**

`CMMMech/data/records/neodymium.yaml` grounds a causal-graph node
`gcvh_glycine_cleavage_protein` to UniProtKB:Q5FRY1 with

> functional_role: Glycine cleavage system H protein GcvH (GOX1096 / GO_1096) targeted
> by transposon disruption and clean deletion in Gluconobacter oxydans B58 Mon2
> bioleaching assays.

and an `annotation_note` saying the 621H entry is "orthologous to the engineered B58
locus". The equation `GO_1096 = GOX1096` is the whole basis of the grounding, and it
does not hold. Marecos et al. identify their own locus explicitly:

- [PMID:40301604 "GO_1096 codes for the GTP-binding protein TypA which has been linked
  to stress response"]
- and in the abstract, [PMID:40301604 "δGO_1096, disruption of the gene encoding the
  GTP-binding protein TypA"].

TypA/BipA in *G. oxydans* 621H is **not** GOX1096. It is GOX0636 (UniProtKB:Q5FT83,
"Large ribosomal subunit assembly factor BipA … (GTP-binding protein BipA)"; UniProt
REST query on organism_id 290633, run 2026-10-28). The `GO_` tags are B58's numbering
and the `GOX` tags are 621H's; the two genomes differ in size and gene count (621H's
chromosome holds 2,432 ORFs [PMID:15665824], while the B58 QC collection alone covers
[PMID:40301604 "2733 non-essential genes in the G. oxydans B58 genome"]), so matching
the digits after the prefix is not an orthology assignment. B58 is not in UniProt, so
the mapping cannot be made that way either; it would need a reciprocal-best-hit or
synteny analysis against the B58 assembly.

What the paper actually reports for its GO_1096 also fits a stress-response GTPase
better than a GCS subunit: transposon disruption was the only hit that lowered
extraction — [PMID:40301604 "only one (δGO_1096) reduced extraction, suggesting that
this gene normally facilitates bioleaching"] — overexpression raised it
([PMID:40301604 "demonstrated a significant increase in extraction efficiency compared
to WT, with a 64% improvement"]), and the clean deletion did not reproduce the
disruption phenotype ([PMID:40301604 "ΔGO_1096 did not exhibit the same effects on
extraction efficiency"]). The authors read it through stress adaptation, not one-carbon
metabolism.

Consequences for CMMMech, for whoever maintains that record:

1. The protein example for the `gcvh_glycine_cleavage_protein` node should be Q5FT83
   (bipA / GOX0636), not Q5FRY1, and the node's label, `gene_symbol` and description
   should name TypA/BipA rather than GcvH — subject to the same orthology check,
   which still has to be done properly against the B58 assembly rather than by locus
   number.
2. Q5FRY1 has **no** experimental association with Nd bioleaching in this paper or, as
   far as I could find, anywhere. Its CMMMech `functional_role` is therefore stronger
   than the evidence supports in two separate ways: the identity is wrong, and even for
   the right protein the clean-deletion result does not support a requirement.
3. The same pattern should be checked for the sibling grounding in the same record:
   CMMMech lists GO_1598 as UniProtKB:Q5FQK7, GOX1598 "Putative oxidoreductase", while
   the paper's Table 2 calls GO_1598 "Orotate phosphoribosyltransferase (EC 2.4.2.10)".
   Two different enzymes, same locus-number coincidence.

None of this is recorded as a `review.source_defects` entry in the YAML: the defect is
in CMMMech's own grounding fields, not in GOA, UniProt or InterPro, and source_defects
is for upstream-resource errors.

## 6. Actions taken, in summary

| Term | Evidence | Action | One-line reason |
|---|---|---|---|
| GO:0005737 cytoplasm | IEA (TreeGrafter) | MODIFY → GO:0005829 | true but less specific than the cytosol row the gene already carries |
| GO:0005829 cytosol | IEA (TreeGrafter) | ACCEPT | soluble GCS; where the carrier function happens |
| GO:0005960 glycine cleavage complex | IEA (InterPro) | ACCEPT | HAMAP subunit statement plus a complete, co-operonic P/T/H |
| GO:0009249 protein lipoylation | IEA (TreeGrafter) | MARK_AS_OVER_ANNOTATED | GcvH is the lipoyl acceptor; the relay donor role needs LipM/LipL, absent here |
| GO:0019464 glycine decarboxylation via GCS | IEA (UniProt/UniRule) | ACCEPT | lipoyl arm carries the aminomethyl intermediate between the P and T active sites |
| GO:0140104 molecular carrier activity | IC (NEW) | NEW | the gene's core molecular function, unrepresented in GOA |

## 7. Open questions I could not close

- Whether *G. oxydans* actually runs glycine cleavage in the direction of degradation
  under acidogenic bioleaching conditions, or in the synthetic direction. The system is
  reversible and nothing measured here distinguishes them.
- Whether a GcvH-dependent lipoyl relay exists in Acetobacteraceae at all. A profile-HMM
  search for LipL/LipM homologues over the 621H genome would settle the negative that my
  name-based probe can only suggest.
- Lys-59 as the lipoylation site is HAMAP/PIRSR-predicted and has never been shown
  experimentally in this organism.
