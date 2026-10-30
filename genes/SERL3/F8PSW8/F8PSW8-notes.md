# F8PSW8 (Serpula lacrymans SERLA73DRAFT_105238) — curation notes

## Identity

UniProtKB:F8PSW8, 358 aa, locus `SERLA73DRAFT_105238` of *Serpula lacrymans*
var. *lacrymans* strain S7.3 (dry rot fungus), NCBITaxon:936435, reference
proteome UP000008063. Pfam PF13714 (PEP_mutase) only; no gene symbol, so the
folder is named by accession. It is the only PF13714 protein in the proteome.

This entry is the *S. lacrymans* counterpart of *C. puteana* A0A5M3MM75: the two
are the same basidiomycete gene (each the only PF13714 protein of its proteome), and the reasoning below is the same
analysis applied to this sequence.

## The "Isocitrate lyase (EC 4.1.3.1)" name is wrong

The name and EC come from PROSITE-ProRule PRU10119 alone. PS00161
(`K-[KR]-C-G-H-[LMQR]`) is the superfamily catalytic-cysteine motif and matched
2,3-dimethylmalate lyase, *E. coli* 2-methylisocitrate lyase and the petal death
protein as well as the characterised oxaloacetases, so it does not discriminate;
the `FT ACT_SITE 180` placed by the rule is that cysteine.

- No ICL domain: genuine ICLs carry PF00463 and are 428-590 aa; this is 358 aa
  with PF13714 only.
- *S. lacrymans*' real isocitrate lyases are F8QF23 (547 aa) and F8PZU2 (539 aa).
- Identity to real ICLs is background-level (28.2% to *A. nidulans* AcuD, 29.5%
  to *M. tuberculosis* Icl1) against 44.6-46.9% to characterised OAHs.

Method and residue table: [file:CONPW/A0A5M3MM75/A0A5M3MM75-bioinformatics/RESULTS.md].

## What it probably is, and why the review stops short of asserting it

The OAH specificity serine (Ser-308 in *C. parasitica* numbering) is present,
the position where dimethylmalate lyase and methylisocitrate lyase have a proline
[PMID:20558740 "OAH contains a serine residue, Ser-308, and DMML contains a proline residue instead, Pro-240"];
swapping it in *B. cinerea* OAH "reduced its OAH activity 40-fold and increased
the (2 R ,3 S )-dimethylmalate lyase activity 15-fold"
[PMID:20558740 "reduced its OAH activity 40-fold and increased the (2 R ,3 S )-dimethylmalate lyase activity 15-fold"],
and Joosten et al. proposed it as the superfamily marker for OAH activity
[PMID:17654546 "serine in family members correlates with presence of OAH activity whereas its"].
The metal-binding and catalytic residues (Asp-126/155/157, Glu-184, Lys-190,
Cys-192, Glu-259, Asn-282, Tyr-111/His-182) are all conserved, and the family
requires a divalent metal
[PMID:20558740 "All PEPM/ICL superfamily members require Mg 2+ or Mn 2+ for activity"].

The physiology fits: oxalate biosynthesis in wood-rotting basidiomycetes runs
through oxaloacetase, which has a "pivotal role in yielding oxalate from
oxaloacetate via the acetate-recycling" routes in *Fomitopsis palustris*
[PMID:11553780 "pivotal role in yielding oxalate from oxaloacetate via the acetate-recycling"],
and in two brown-rot fungi "oxaloacetase expression was up upregulated for both
fungi" near the hyphal front, separately from the "paralogous of isocitrate lyases"
[PMID:27543342 "oxaloacetase expression was up upregulated for both fungi"]
[PMID:27543342 "paralogous of isocitrate lyases"]. The nearest relative in the
comparison set is the Ser-308-carrying *G. trabeum* protein S7Q6Y6 (82.1%
identical). *G. trabeum* has a second PF13714 protein, S7Q148, with Pro at that
position and no PS00161 match (42.6% identical), so the Ser/Pro split tracks the
branch inside one basidiomycete genome and this protein sits on the Ser side.

Correction (PR #5631 review): an earlier version of this review said the
*Penicillium* paralog Pc18g05100 carries the serine yet gave no oxalate, and
used that as a counterexample to the marker. The analysis table says otherwise:
B6HBX9/Pc18g05100 has **Pro** at the 308 position (window `VIIFPFATL`, as in
DMML), so it lacks both the serine and the activity and corroborates the marker.

The evidence therefore leans towards OAH. What keeps the review from asserting
it: the marker was derived and tested on ascomycete and plant proteins, and no
basidiomycete oxaloacetase has been characterised as a cloned protein. The two
other arguments once offered against OAH are weak. Global identity is higher to
*A. niger* 2,3-dimethylmalate lyase (51.9%) than to any characterised OAH
(44.6-46.9%), but this is a basidiomycete-to-ascomycete comparison without a
tree. The Thr-113 to Ser difference is not diagnostic: DMML 3FA3 has Thr there
and the OAH-active petal death protein Q05957 has Ser. The review therefore
removes the isocitrate lyase claim, keeps the superfamily-level catalytic
activity, states that the evidence leans towards oxaloacetase, and asserts no EC.

Independent concurrence, not evidence: the GOA file's gene-name column for this
entry reads "Oxaloacetate acetylhydrolase" (apparently the submitter name from
the genome submission, EMBL EGO00826.1), although UniProt's own DE line is the
PRU10119 "Isocitrate lyase". Submitter-imported names (ECO:0000313 class) are
not used as support, but the genome annotators reached the same branch call.

## Curation decisions

- `GO:0004451` isocitrate lyase activity (IEA, EC mapping): REMOVE.
- `GO:0003824` catalytic activity (IEA, InterPro): ACCEPT.
- No NEW rows; OAH candidacy recorded in `suggested_questions` /
  `suggested_experiments`.
- Source defects against UNIPROT (name + EC) and the PROSITE/ProRule mapping
  (resource OTHER).

## CMMMech context

CMMMech's `humboldtine.yaml` and `malachite.yaml` describe A0A5M3MM75 and F8PSW8
as basidiomycete "oahA homologs" auto-annotated as isocitrate lyase. The
auto-annotation statement is accurate; the oahA identification is a defensible
sequence inference, not an established fact, and the mineralogical evidence cited
there (Vlasov et al. 2023) includes no enzyme assay or gene perturbation that
could test it.
