# A0A5M3MM75 (Coniophora puteana CONPUDRAFT_105298) — curation notes

## Identity

UniProtKB:A0A5M3MM75, 364 aa, locus `CONPUDRAFT_105298` of *Coniophora puteana*
RWD-64-598-SS2 (brown-rot fungus), NCBITaxon:741705, reference proteome
UP000053558. Pfam PF13714 (PEP_mutase) only; no gene symbol, so the folder is
named by accession. It is the **only** PF13714 protein in the reference proteome.

## The "Isocitrate lyase (EC 4.1.3.1)" name is wrong

UniProt's name and EC come from PROSITE-ProRule PRU10119 alone. PS00161 is the
six-residue pattern `K-[KR]-C-G-H-[LMQR]` around the catalytic cysteine shared
across the PEP mutase/isocitrate lyase superfamily; in the analysis it matched
2,3-dimethylmalate lyase, *E. coli* 2-methylisocitrate lyase and the petal death
protein as readily as it matched the characterised oxaloacetases, so it cannot
discriminate. The `FT ACT_SITE 186` that the rule places on this entry is the
cysteine of that motif.

Three independent observations exclude isocitrate lyase:

- No ICL domain. Genuine ICLs carry Pfam PF00463 and are 428-590 aa; this
  protein has only PF13714 and is 364 aa.
- *C. puteana*'s own isocitrate lyases are elsewhere: A0A5M3N7P6 (552 aa) and
  A0A5M3MQD7 (539 aa) carry PF00463.
- Identity to real ICLs is background-level (31.0% to *A. nidulans* AcuD, 30.3%
  to *M. tuberculosis* Icl1), against 43.5-44.1% to characterised OAHs.

See [file:CONPW/A0A5M3MM75/A0A5M3MM75-bioinformatics/RESULTS.md] for the method
and the full residue table.

## What it probably is, and why the review stops short of asserting it

The protein has the OAH specificity serine aligned to Ser-308 of *C. parasitica*
OAH, the position where dimethylmalate lyase and methylisocitrate lyase carry a
proline [PMID:20558740 "OAH contains a serine residue, Ser-308, and DMML contains a proline residue instead, Pro-240"],
and whose mutation swaps the two activities in *B. cinerea* OAH
[PMID:20558740 "reduced its OAH activity 40-fold and increased the (2 R ,3 S )-dimethylmalate lyase activity 15-fold"].
Joosten et al. proposed that same serine as the superfamily marker for OAH
activity [PMID:17654546 "serine in family members correlates with presence of OAH activity whereas its"].
The whole metal-binding and catalytic set (Asp-126/155/157, Glu-184, Lys-190,
Cys-192, Glu-259, Asn-282, the Tyr-111/His-182 pair) is conserved, so this is a
functional superfamily enzyme, not a pseudoenzyme.

Brown-rot fungi do run this route: oxalate biosynthesis in the wood-rotting
basidiomycete *Fomitopsis palustris* assigns oxaloacetase a "pivotal role in
yielding oxalate from oxaloacetate via the acetate-recycling" routes
[PMID:11553780 "pivotal role in yielding oxalate from oxaloacetate via the acetate-recycling"],
and in *Postia placenta* and *Gloeophyllum trabeum* the oxaloacetase gene is
expressed distinctly from the "paralogous of isocitrate lyases"
[PMID:27543342 "paralogous of isocitrate lyases"] and is upregulated at the
advancing hyphal front [PMID:27543342 "oxaloacetase expression was up upregulated for both fungi"].
Consistent with that, this protein's closest relative in the comparison set is
the Ser-308-carrying PF13714 protein of *G. trabeum* (S7Q6Y6, 78.8% identical).
*G. trabeum* has a second PF13714 protein, S7Q148, with Pro at that position and
no PS00161 match (44.0% identical), so the Ser/Pro split tracks the branch inside
one basidiomycete genome and this protein sits on the Ser side.

Correction (PR #5631 review): an earlier version of this review said the
*Penicillium* paralog Pc18g05100 carries the serine yet gave no oxalate, and
used that as a counterexample to the marker. The analysis table says otherwise:
B6HBX9/Pc18g05100 has **Pro** at the 308 position (window `VIIFPFATL`, as in
DMML), so it lacks both the serine and the activity and corroborates the marker.

The evidence therefore leans towards OAH. What keeps the review from asserting
it: the marker was derived and tested on ascomycete and plant proteins, and no
basidiomycete oxaloacetase has ever been characterised at the protein level — the
*Fomitopsis* work is enzymology on cell extracts, not on a cloned gene. The two
other arguments once offered against OAH are weak. Global identity is higher to
*A. niger* 2,3-dimethylmalate lyase (51.5%) than to any characterised OAH
(43.5-44.1%), but this is a basidiomycete-to-ascomycete comparison without a
tree, and the queries may be outgroup to the ascomycete OAH/DMML split. The
Thr-113 to Ser difference is not diagnostic: DMML 3FA3 has Thr there and the
OAH-active petal death protein Q05957 has Ser. So the review removes the
isocitrate lyase claim, keeps the superfamily-level catalytic activity, states
that the sequence evidence leans towards oxaloacetase, and asserts no
EC 3.7.1.1, leaving it to the enzymology in `suggested_experiments`.

## Curation decisions

- `GO:0004451` isocitrate lyase activity (IEA, EC mapping): REMOVE, as a
  demonstrably wrong automatic mapping (see above).
- `GO:0003824` catalytic activity (IEA, InterPro): ACCEPT. It is as specific as
  the evidence allows, and the conserved catalytic machinery supports it.
- No NEW rows; the OAH candidacy is recorded in `suggested_questions` and
  `suggested_experiments` instead.
- Source defects filed against UNIPROT (name + EC) and the PROSITE/ProRule
  mapping (resource OTHER).

## CMMMech context

CMMMech (`humboldtine.yaml`, `malachite.yaml`) grounds *C. puteana* oxalate
production to malate dehydrogenase and pyruvate carboxylase, and states in
`annotation_note` that the basidiomycete "oahA homologs" A0A5M3MM75 and F8PSW8
are auto-annotated as isocitrate lyase. That note is accurate about the
auto-annotation. The implied identification of these two as *oahA* homologs is
reasonable but not established: it is a sequence inference about the branch of
the superfamily, and no basidiomycete OAH protein has been characterised. The
CMMMech evidence itself (Vlasov et al. 2023) is mineralogical, with no enzyme
assay or gene perturbation, so it cannot bear on this protein's substrate.
