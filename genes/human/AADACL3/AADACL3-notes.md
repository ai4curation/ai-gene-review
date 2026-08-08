# AADACL3 (Q5VUY0) — review notes

## Summary of the problem

AADACL3 is a genuinely dark gene whose entire GO record — five annotations, all
IBA or IEA — is derived from family and fold signatures. There is no experimental
annotation of any kind. The review therefore turns on a single question the
campaign has hit repeatedly: is the esterase assignment a *fold name propagating
into GO as an activity*, or is it a statement about catalytic machinery that is
actually conserved? The mirror-image error (dismissing a family assignment as
"fold without function" without checking the residues) is equally common, so both
directions were tested explicitly rather than argued.

Answer: **the catalytic machinery is intact.** The GO record is well founded, and
in one respect (membrane) it is better founded than UniProt's own feature table.

## What UniProt does and does not say

The entry is a stub. There is no FUNCTION, no CATALYTIC ACTIVITY, no SUBUNIT and
no SUBCELLULAR LOCATION comment. The only functional statements are the RecName
EC number and a family assignment:

- `DE            EC=3.1.1.-;`
  [file:human/AADACL3/AADACL3-uniprot.txt] — i.e. UniProt itself asserts a
  carboxylic-ester hydrolase EC class, which maps exactly onto GO:0052689.
- `CC   -!- SIMILARITY: Belongs to the 'GDXG' lipolytic enzyme family.`
  [file:human/AADACL3/AADACL3-uniprot.txt], with `{ECO:0000305}` — i.e. curator
  inference from sequence, not experiment.
- `PE   2: Evidence at transcript level;`
  [file:human/AADACL3/AADACL3-uniprot.txt]. Note this is PE **2**, not PE 1: the
  protein has never been detected, so unlike most genes in this campaign it is
  correct to say there is no protein-level evidence at all, not merely no
  functional data.
- `DR   Pharos; Q5VUY0; Tdark.` and
  `DR   HPA; ENSG00000188984; Tissue enhanced (placenta, skin).`
  [file:human/AADACL3/AADACL3-uniprot.txt]
- `DR   PAN-GO; Q5VUY0; 0 GO annotations based on evolutionary models.`
  [file:human/AADACL3/AADACL3-uniprot.txt] — the curated human PAN-GO reference
  set contains nothing for this gene, so the GO_REF:0000033 IBA rows come from
  the broader PAINT pipeline rather than from a PAN-GO curator's selection.

The two literature references in the entry are the FLJ full-length cDNA project
[PMID:14702039] and the chromosome 1 sequence, i.e. sequencing papers only.

The feature table does carry propagated catalytic annotations: `ACT_SITE 193`,
`347`, `377` (all `ECO:0000250|UniProtKB:Q8BLF1`, mouse Nceh1) and a
`MOTIF 119..121` oxyanion hole (`ECO:0000250|UniProtKB:Q5NUF3`, soybean HIDH).
These are inferences, so they cannot themselves be used to validate the
family-derived GO terms — they have the same provenance. Hence the sequence
analysis below.

## Literature: checked, and genuinely absent

Affinage returned an empty record (`n_discoveries: 0`, `citation_count: 0`, and no
`self_evaluation_pairwise` score). Per the campaign rules an empty provider record is not
evidence that literature is absent, so PubMed was searched directly. Seven
records mention AADACL3, and not one assays the protein or its activity: two
livestock body-weight association studies (Chinese Holstein cows, Chinese
fine-wool sheep), a Siberian sheep selection scan, a sarcoidosis exome study, a
1p36 duplication case report, a ductal-carcinoma-in-situ mutational-landscape
study, and a paper on AADACL1 in platelets that mentions the family name.

This is corroborated by the family's own review literature, which states the
position explicitly:

- [PMID:35736449 "Except for AADACL1, more commonly known as KIAA1363, all other
  members of the AADACL protein family, AADACL2, AADACL3, and AADACL4, have so
  far been only poorly investigated and no functional roles can be concluded."]

The same review gives the family's architecture and the characterised prototype:

- [PMID:35736449 "The arylacetamide deacetylase (AADAC) protein family name
  giving protein AADAC is a type II membrane glycoprotein, facing with its active
  side to the lumen of the endoplasmic reticulum (ER) [1]."]
- [PMID:35736449 "The AADAC family comprises five members, including AADAC and
  four AADAC-like (AADACL1-4) proteins."]
- [PMID:35736449 "AADAC substrates include neutral lipids such as diglycerides,
  but also several xenobiotics, including a number of clinical drugs, such as the
  antiandrogen drug flutamide, the analgesic antipyretic drug phenacetin, and the
  antituberculosis drug rifamycin [1,4,5,6,7]."]

and the caution that family membership does not fix substrate preference, since
even the two best-studied members diverge:

- [PMID:35736449 "This hypothesis has been tested in yeast, where KIAA1363
  (AADACL1) was unable to rescue the cholesterol acetate accumulation phenotype
  of the AADAC yeast ortholog Say1Δ-mutant [6], suggesting that the two enzymes
  have different substrate specificity, with the latter lacking sterol acetate
  hydrolase activity."]

The ER-lipase review [PMID:21531146] is abstract-only in the cache and covers
AADAC and KIAA1363 but not AADACL3; it is retained as family/compartment
background at LOW relevance rather than as support for any AADACL3 claim.

## Genomic context matters for how far the family inference can be trusted

HGNC places the five family members in two clusters: AADAC and AADACL2 are a
tandem pair at 3q25.1, NCEH1/AADACL1 is at 3q26.31, and **AADACL3 and AADACL4
are a tandem pair at 1p36.21**. So AADACL3's nearest relative is another
uncharacterised protein, and the nearest *characterised* enzyme is roughly a
third-identity relative on a different chromosome. The bioinformatics run
quantifies this: 55.0% identity to AADACL4 (uncharacterised) versus 33.9% /
33.4% / 33.3% to AADACL2, NCEH1 and AADAC.

That gap is the reason topology cannot simply be inherited: at essentially equal
distance, AADAC and NCEH1 are single-pass type II membrane proteins while
AADACL2 is **secreted**. The family gives contradictory answers, so the membrane
annotation needed independent support.

## Bioinformatics: what was tested and what came back

Script and full output: `AADACL3-bioinformatics/analyze.py`, `RESULTS.md`,
`results.json`. Everything is fetched live from UniProt, InterPro and PROSITE;
missing input is a hard error. A second run reproduces both output files byte for
byte.

**1. The Ser-Asp-His triad and the oxyanion loop are present.** Reading the
residues straight out of the sequence at the annotated positions:

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| 193 | S193 | S | yes |"]
- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "Oxyanion-hole motif 119-121 reads `HGG`; the nucleophile elbow 191-196 reads `GDSFGG`."]

**2. All three align to annotated active sites in every characterised relative.**
Global BLOSUM62 alignment maps AADACL3's triad onto the curated active sites of
AADAC, NCEH1 (human and mouse), AADACL2 and AADACL4 at 3/3, and the HGG oxyanion
loop is HGG in all six panel members including the distant soybean outgroup:

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| AAAD_HUMAN (P22760) | 33.3 | S193→S189/D347→D343/H377→H373 | 3/3 | `HGG` |"]
- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| NCEH1_HUMAN (Q6PIU2) | 33.4 | S193→S191/D347→D348/H377→H378 | 3/3 | `HGG` |"]

So GO:0052689 is not a fold name in disguise. It is the fold *plus* a complete
and correctly positioned catalytic apparatus, plus a subfamily-specific signature
(PIRSF037251 / IPR017157 "Arylacetamide deacetylase" spanning residues 19–403),
plus UniProt's own EC 3.1.1.- assignment.

**3. A trap worth recording: PROSITE PS01174 does not match AADACL3.** The
GDXG-family "putative serine active site" pattern hits AADAC, NCEH1 and AADACL2
but not AADACL3 — which, taken at face value, looks like exactly the loss of
catalytic machinery one would use to argue the annotation away. Walking the
pattern position by position shows the two mismatches are both *flanking*
positions, and that the D-S core and the catalytic serine (pattern position 7)
are intact:

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "Pattern (fetched from PROSITE): `[LIVM]-x-[LIVMF]-[SA]-G-D-S-[CAS]-G-[GA]-x-[LI]-[CAVT]`"]
- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| ADCL3_HUMAN (Q5VUY0) | no | - | pos 4 wants [SA], has C190, pos 8 wants [CAS], has F194 |"]

Cys190 and Phe194 replace Ser/Ala and Cys/Ala/Ser. Both sit in the acyl-binding
neighbourhood of the nucleophile rather than in the catalytic machinery, so the
right reading is a possible shift in substrate preference, not loss of activity.
This is a good illustration of why a signature miss must be resolved to
individual positions before it is allowed to change an action.

**4. Membrane: predicted concordantly, and missing from UniProt.** Phobius and
TMHMM both place transmembrane helices in AADACL3's N-terminal region and
neither SignalP nor Phobius calls a cleaved signal peptide; the catalytic domain
(residues 61–407) is assigned to the non-cytoplasmic side, matching the lumenal
orientation of AADAC. The discriminating control is AADACL2, where SignalP fires
and the curated location is "Secreted":

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| ADCL3_HUMAN (Q5VUY0) | - | - | - | [(6, 29), (41, 60)] | - | [(4, 26), (43, 60)] | - |"]
- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| ADCL2_HUMAN (Q6P093) | - | [(1, 18)] | Secreted | - | [(1, 19)] | - | [(1, 18), (1, 19)] |"]

The striking part is the comparison with the tandem paralog. AADACL4 is the same
length (407 aa), has the same numbered active sites and oxyanion motif, and gets
**identical** Phobius calls — yet UniProt annotates `TRANSMEM 5-25`, both
topological domains and "Single-pass type II membrane protein" on AADACL4 and
nothing at all on AADACL3:

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| ADCL4_HUMAN (Q5VUY2) | [(5, 25)] | - | Membrane; Single-pass type II membrane protein | [(6, 29), (41, 60)] | - | [(2, 24)] | - |"]

That is an inconsistency in UniProt's automatic-annotation coverage between two
paralogs with the same predicted architecture, and it means the GO `membrane`
annotations (InterPro/ARBA IEA and PAINT IBA) are *ahead of* the UniProt feature
table rather than downstream of it. It is worth reporting to UniProt. Note also
that GO:0016020 absorbed GO:0016021 "integral component of membrane" as a
secondary id, so a transmembrane-helix prediction now supports GO:0016020
directly.

One caveat recorded rather than smoothed over: both Phobius and TMHMM call *two*
helices in AADACL3 (6–29 and 41–60 / 4–26 and 43–60), not one, so "single-pass
type II" — UniProt's wording for AADACL4 — may itself be an under-call for this
pair. Since both topologies leave the catalytic domain non-cytoplasmic, the
functional reading is unaffected, and the safe GO statement remains the generic
`membrane`.

## Resolving the WITH/FROM sets

**GO:0016787 IBA (GO_REF:0000033)** cites a deliberately wide set:
`AGI_LocusCode:AT1G49660 | AT3G48690 | AT5G15860 | AT5G23530 | MGI:1915008 |
MGI:2443191 | MGI:2448704 | PANTHER:PTN009058710 | RGD:631440 | SGD:S000002836 |
UniProtKB:P22760 | P23872 | P71668 | P95125 | P9WK87 | Q5NUF3 | Q9HTI0`.
Resolved:

| accession | identity | characterised activity |
|---|---|---|
| MGI:1915008 / RGD:631440 / P22760 | mouse / rat / human AADAC | arylacetamide deacetylase, TG lipase |
| MGI:2443191 | mouse Nceh1 | acetyl-MAGE / cholesteryl ester hydrolase |
| MGI:2448704 | mouse **Afmid** | arylformamidase (an amidohydrolase, EC 3.5.1.9) |
| SGD:S000002836 | yeast **BNA7** | formylkynurenine formamidase (amidohydrolase) |
| P23872 | *E. coli* Aes | acetyl esterase |
| P71668 / P95125 / P9WK87 | *M. tuberculosis* LipI / LipN / NlhH | carboxylesterases |
| Q5NUF3 | soybean **HIDH** | bifunctional: carboxylesterase (EC 3.1.1.1) plus 2-hydroxyisoflavanone **dehydratase** (EC 4.2.1.105) |
| Q9HTI0 | *P. aeruginosa*, unreviewed | — |

The set mixes carboxylesterases, amidohydrolases and one bifunctional
esterase/dehydratase, which is precisely why the propagated term stopped at the
generic `hydrolase activity`: that is the most specific term that survives across
this clade. The weakest donor is HIDH, which UniProt annotates with both EC
3.1.1.1 and EC 4.2.1.105, so it does formally license a hydrolase term, but its
physiologically important reaction is the dehydration and its esterase activity
is described only as slight. Either way the term is *correct for AADACL3* but far
less informative than what the same GOA record already carries from the
subfamily signature.

**GO:0016020 IBA (GO_REF:0000033)** cites a much tighter set:
`MGI:1915008 | MGI:2443191 | PANTHER:PTN009058713 | UniProtKB:P22760` — mouse
Aadac, mouse Nceh1 and human AADAC, all three single-pass type II membrane
proteins with lumenal/extracellular catalytic domains. The secreted member
AADACL2 is *not* in the set, so the transfer is not indiscriminate. Note the
PANTHER node differs from the one used for the hydrolase row (PTN009058713 vs
PTN009058710); neither is AADACL3 itself, so neither IBA is self-referential.

**GO:0016020 IEA (GO_REF:0000120)** cites `ARBA:ARBA00028763 | InterPro:IPR017157`
and **GO:0016787 IEA / GO:0052689 IEA (GO_REF:0000002)** cite `InterPro:IPR013094`
and `InterPro:IPR017157` respectively. The distinction matters, and section 6 of
the bioinformatics report quantifies it. IPR013094 (Alpha/beta hydrolase fold-3)
is a *fold* signature: it constrains architecture, not the reaction, and it
reaches outside the subfamily whose chemistry is being asserted - it matches
soybean HIDH at 74–298 even though HIDH matches neither IPR017157 nor
PIRSF037251 nor even the family-level IPR050300, and HIDH's physiologically
important reaction is a dehydration. So IPR013094 → GO:0016787 is a
fold-to-activity mapping. IPR017157 (Arylacetamide deacetylase) is a *subfamily*
signature that matches AADACL3 across residues 19–403, with its PIRSF member
signature PIRSF037251 over the same span at 5.8e-82 and flagged representative,
so IPR017157 → GO:0052689 is a subfamily-to-activity mapping. Both land on a
defensible answer here, but only the second one is a well-grounded inference in
its own right.

## Reconciling with the parallel AADACL2 and AADACL4 reviews

*Superseded, and kept for its reasoning: written while AADACL2 and AADACL4 still encoded this row
differently. All three now record `EVIDENCE_CIRCULAR_OR_REDUNDANT` with no granularity failure
mode, and the 13-of-14 serine figure below is superseded by the shared node audit's 15 of 16,
which resolves BNA7 directly rather than through the Alliance record. Nothing here is
outstanding.*

The AADACL2 review (PR #2266) reported that PAINT's node placement for this family
is inverted: `GO:0017171 serine hydrolase activity` sits only at ortholog-level
nodes, while the shared family node `PTN009058713` carries `GO:0016020 membrane` —
yet it is the catalytic triad that transfers family-wide and the membrane anchor
that does not. I checked both halves of that against AADACL3's own record rather
than importing it, and it holds, with two differences worth stating.

**The mechanism half is confirmed, and quantified — but it does not license a
term swap on this row.** Section 7 of the bioinformatics report reads the residue at
the first annotated active site of every WITH/FROM source on AADACL3's own
hydrolase-activity IBA:

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "Audited: GO:0016787 (IBA, GO_REF:0000033). 17 WITH/FROM tokens, 14 resolved to a protein, 14 with a readable nucleophile, of which **13 are serine**. Non-serine: HIDH_SOYBN T164."]

The amidohydrolase members are no obstacle to a mechanism term: mouse Afmid, a
formamidase, is itself a serine hydrolase with `S162`. (Yeast BNA7 and rat Aadac
could not be resolved to a single reviewed UniProt entry through the Alliance
record and are reported unresolved rather than counted either way, so the 13-of-14
figure is a count of what was readable.)

**Crucially, that one exception is enough to stop a plain transfer.** `GO:0017171`
is defined by mechanism, so asserting it at a node propagates a serine nucleophile
to every descendant — and HIDH's `Thr164` makes that false for one of them. PAINT
does have a device for exactly this shape of problem: annotate the ancestral node
and mark the divergent descendant with a `NOT`, which would leave `GO:0017171` on
the AADACL paralogs while excluding HIDH. So HIDH is not structurally
disqualifying, and the recommendation below offers both that route and the
sub-node route. What it does mean is that the term cannot simply be moved to
`PTN009058710` as-is, which is what I had proposed. Nor can `GO:0052689` sit there,
because the two formamidases hydrolyse an amide rather than an ester bond. So
**`GO:0016787` genuinely is the lowest common ancestor of this donor set, and
PAINT's choice is correct curation rather than a term that stopped short.** I
initially proposed `GO:0017171` as a second replacement term on both hydrolase rows;
that was wrong for exactly this reason and has been withdrawn. The rows are
replaced on **redundancy** grounds only — AADACL3 already carries `GO:0052689` from
a subfamily-specific signature, which is stronger and more direct evidence for this
gene than a transfer from a clade that broad — so the propagation **root cause** is
`EVIDENCE_CIRCULAR_OR_REDUNDANT` rather than `TERM_SCOPING_PROBLEM`: the defect is
not that PAINT chose the wrong node. The **failure mode** `GRANULARITY_MISMATCH` is
kept, because the schema defines it as the parent term being true but uninformative
(`gene_review.yaml:2469`), which is a statement about how much the term tells you
about *this gene* and not an accusation about the node. Both readings are needed to
describe the row honestly: correct where it was asserted, uninformative where it
landed. The `GO:0017171` recommendation lives in `suggested_questions` as a
node-placement proposal for PAINT, where the HIDH obstacle can be named and worked
around.

The same test applies to the location term and gives the same answer. The membrane
IBA's donors resolve to **four distinct curated location strings** between them —
endoplasmic reticulum membrane and microsome membrane for AADAC, cell membrane and
microsome for Nceh1 — so refining `GO:0016020` would mean arbitrarily preferring one
donor. General is right in both cases. The rule I should have applied before
proposing a more specific term: *is this term the LCA of its donors?* The single obstacle at `PTN009058710` is
soybean HIDH, whose nucleophile is **Thr164** — so `GO:0017171` could be placed at
that node only if HIDH is excluded, whereas at the tighter `PTN009058713` there is
no obstacle at all. That is a sharper version of the recommendation: the term is
blocked by exactly one member, and it is nameable.

**The conflict with the merged AADACL2 review, since resolved.** *(Written when
AADACL2 and AADACL4 still disagreed with this review; the disagreement no longer
exists — all three now record the treatment argued for here. Kept because the
merges-two-existing-rows argument below is what settled it.)*

I checked the two records directly. `genes/human/AADACL2/AADACL2-goa.tsv` carries a
`GO:0016787` IBA whose WITH/FROM set is **identical token-for-token** to AADACL3's —
the same seventeen tokens, the same node `PTN009058710` (compared programmatically,
not by eye). AADACL2's review then resolved that row as `MODIFY → GO:0017171`,
reading its serine count as *supporting* the mechanism term, where this review read
the same count as *blocking* it because one member of that node — HIDH, `Thr164` — is
not a serine hydrolase. Both could not be right about the same row.

AADACL3's reading was the correct one, for a reason that is about the record rather
than about the argument: `GO:0052689` already exists on the GOA from an independent
subfamily signature, so a MODIFY toward it **merges two existing rows**, whereas
`GO:0017171` appears nowhere in the GOA and a MODIFY toward it would *introduce* a
claim that the cited node does not license. That argument is what the shared node
audit then confirmed against the donor chemistry, and AADACL2 and AADACL4 were
brought into line with it, so nothing is outstanding on either. Two details that were flagged for whoever picked that up, both since fixed: AADACL2's
notes described HIDH as "a dehydratase, not a hydrolase", which is the
characterisation corrected in `f50b47fcd` (UniProt gives it both EC 3.1.1.1 and EC
4.2.1.105); and AADACL2 and AADACL3 do *not* differ in whether they inherit a
molecular-function term, which is how I first framed it — they both inherit
`GO:0016787` from the same node.

**Where AADACL3 does differ from AADACL2: there is no topology contradiction to
adjudicate, so ACCEPT is correct rather than UNDECIDED.** AADACL2's location rows
were left UNDECIDED because a curated "Secreted" call collides with the family's
type-II anchor and measurement declined to break the tie. AADACL3 has no curated
subcellular location at all, no SignalP call, and concordant Phobius and TMHMM
helices — there is nothing in conflict. I did not use a topology argument to
remove anything, and the membrane rows are accepted on positive prediction plus
AADACL2 serving as the negative control that makes the absent SignalP call
informative.

**The mouse ortholog independently confirms the multi-pass point.** The AADACL2
review noted that mouse Aadacl3 has three plain helices rather than a type-II
anchor. Adding it to the panel confirms this from the curated record, and it
sharpens the UniProt-gap finding considerably:

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "| ADCL3_MOUSE (A2A7Z8) | [(2, 22), (46, 66), (109, 129)] | - | Membrane; Multi-pass membrane protein | [(42, 61), (111, 129)] | [(1, 26)] | [(2, 24)] | - |"]

UniProt curates the *mouse* ortholog of this very gene as `Membrane; Multi-pass
membrane protein` with three transmembrane helices, at 61.9% identity and with the
same triad (`S193→S194/D347→D348/H377→H378`, 3/3 on annotated sites), while the
human entry carries no transmembrane feature whatsoever. So the human gap is not
only inconsistent with the tandem paralog AADACL4, it is inconsistent with the
same gene in mouse. It also means "single-pass type II" is the wrong descriptor
for this branch, and `GO:0016020 membrane` is the right generic level for reasons
beyond not knowing which membrane.

**Two method points adopted.** First, the load-bearing condition for a
conservation claim is that a mapped residue lands on the target's *own annotated
active site* **and** is the same amino acid — either alone is too weak. The script
already required the annotated-site half; it now reports both counts separately, and
HIDH demonstrates why that matters: AADACL3's Ser193 does land on HIDH's annotated
site 164, but the residue there is a threonine, so HIDH scores 2/3 on the annotated
site and only **1/3** when identity is also required. Every real family member is
3/3 on both. Second, each WITH/FROM resolution is now verified against the resolved
entry's *own* cross-references — an MGI/RGD/SGD mapping must come back through the
entry's MGI/RGD/SGD cross-reference, and an Arabidopsis locus through its Araport
cross-reference — and a `self_test_resolution_guard()` run at the start of every
execution feeds the guard a deliberately wrong mapping (mouse Aadac's MGI id against
the human protein) and fails loudly if it is accepted, so the check cannot go
vacuous if a cross-reference database is renamed. No identity threshold is used
anywhere in the analysis, so there was nothing to re-derive from the distribution.

**Family-wide claims audited.** The AADACL2 review had to retract several
overstatements. Checking mine: no family-wide specificity claim is made — the
review states explicitly that substrate must not be inferred from membership, and
cites the Say1Δ non-rescue result as the reason; the expression statements are
per-gene HPA records with the gene named (AADACL3 placenta/skin-enhanced, AADACL2
skin-enriched, AADACL4 choroid-enhanced) rather than a branch-level claim; and the
two formamidases in the WITH/FROM column are named as amidohydrolases in the
review rather than folded into an esterase generalisation.

**AADACL4 (PR #2263, already merged).** I queried its GOA directly rather than
taking the paralog framing on trust: it carries the **same five annotations with the
same five terms**, and the WITH/FROM sets on both IBA rows are identical to
AADACL3's — `GO:0016787` from `PTN009058710` with all seventeen sources, and
`GO:0016020` from `PTN009058713`. It is *not* identical throughout, and the one
difference is the `SL-0162` token recorded below, so the blanket phrasing would
contradict this section's own finding. Scoped to the two IBA rows, the
node-placement recommendation applies to AADACL4 unchanged.

That also corrects one premise in the cross-gene framing: AADACL3 and AADACL4 do
**not** inherit "no mechanism term at all", and neither does AADACL2. All three
inherit `GO:0016787 hydrolase activity` at a second node, `PTN009058710`. That term
is the correct lowest common ancestor of that node's donors — it is not a parent
standing in for something better that PAINT should have chosen — but it is
uninformative *for these genes*, and it duplicates a more specific term that **all
three** of them already carry — `GO:0052689` IEA from `InterPro:IPR017157` appears on
AADACL2, AADACL3 and AADACL4 alike. That is why MODIFY on redundancy grounds, rather
than a new annotation, is the right action.

That count is not just arithmetic: it means the remedy this review relies on is
directly available to AADACL2 as well. Modifying `GO:0016787` toward `GO:0052689`
**merges two rows that already exist** on each of the three records, whereas
modifying it toward `GO:0017171` would introduce a term that appears on none of
them. So the #2266 follow-up has a concrete remedy to adopt, not merely a
disagreement to adjudicate.

One asymmetry in the two records is worth recording because it corroborates the
UniProt-gap finding from a different direction: AADACL4's `GO:0016020` IEA carries
`UniProtKB-SubCell:SL-0162` in its WITH/FROM alongside the ARBA rule and
IPR017157, and AADACL3's does not. The SubCell mapping can only fire for an entry
that has a curated subcellular location — which AADACL4 has and AADACL3 lacks. The
gap is visible in the GOA evidence, not just in the UniProt feature table.

AADACL4 has one peculiarity this analysis turned up that AADACL3 does not share:
its nucleophile elbow reads `GESVGG`, with glutamate where the family has the
structural aspartate of `GDSxGG`, so it fails PROSITE PS01174 at four positions
(4, 6, 8 and 12) against AADACL3's two. Whether that affects its catalytic
competence is a question for an amendment to that review, not this one.

## Actions taken

| # | term | evidence | action | why |
|---|---|---|---|---|
| 1 | GO:0016787 hydrolase activity | IBA | MODIFY → GO:0052689 | the correct LCA of a heterogeneous donor set, so not a bad node choice; replaced as redundant with the subfamily-derived term the record already carries |
| 2 | GO:0016020 membrane | IBA `is_active_in` | ACCEPT | tight, topologically coherent source set; corroborated by concordant Phobius + TMHMM |
| 3 | GO:0016020 membrane | IEA `located_in` | ACCEPT | same conclusion from an independent pipeline; supported despite UniProt having no TRANSMEM feature |
| 4 | GO:0016787 hydrolase activity | IEA (IPR013094) | MODIFY → GO:0052689 | fair for the fold it describes; replaced as redundant, and the fold signature reaches outside the subfamily whose chemistry it asserts |
| 5 | GO:0052689 carboxylic ester hydrolase activity | IEA (IPR017157) | ACCEPT | best-supported statement about the gene: subfamily signature + intact triad + UniProt EC 3.1.1.- |

No REMOVE and no MARK_AS_OVER_ANNOTATED. Nothing in the record over-reaches:
there is no annotation to a specific substrate, to a specific compartment, or to
a biological process, which for a gene with zero functional data is the correct
state. The two MODIFYs collapse redundant ancestors onto the specific term rather
than removing anything.

## Open questions carried into the review

1. Signal anchor or cleaved signal peptide — membrane-anchored like AADAC/NCEH1/
   AADACL4, or secreted like AADACL2?
2. Why does UniProt annotate a transmembrane signal-anchor on AADACL4 and nothing
   on AADACL3 when the predictions are identical? (Report to UniProt.)
3. Does Cys190/Phe194 in place of the PS01174-conforming Ser/Cys shift substrate
   preference relative to AADAC?
4. Placenta- and skin-enhanced expression is unusual for this family, whose
   characterised members are liver/intestine (AADAC) and brain/macrophage/
   platelet (NCEH1). HPA records AADACL2 (ENSG00000197953) as skin-*enriched* and
   AADACL4 (ENSG00000204518) as choroid-enhanced, so the two members with a skin
   signal are AADACL2 and AADACL3 rather than the 1p36.21 tandem pair. Is there a
   skin ester-hydrolase role for this branch of the family?

## Harmonised with AADACL2 and AADACL4 after #2264 merged

This review's verdict on the `PTN009058710` `GO:0016787` row was the correct one of the three
that were reached independently, and it is unchanged: the row is correct, correctly scoped and
validly transferred, and replaceable only as **redundant** with the `IPR017157`-derived
`GO:0052689` that the same GOA record carries. What changes here is the encoding and two donor
facts, so that AADACL2, AADACL3 and AADACL4 — which carry this row byte for byte, the same 17
`WITH/FROM` tokens in all three records — now say the same thing about it.

**The independent measurement.** `genes/human/AADACL2/AADACL2-bioinformatics/` holds a shared
node-level audit (`audit_node_PTN009058710.py` → `NODE_PTN009058710.md`) that resolves all 17
tokens and tests each candidate term against every donor, reading chemistry off each donor's own
EC numbers *and* its own curated GO annotations classified by fetched ontology ancestry, and the
nucleophile off its own `ACT_SITE` features:

```
GO:0016787 hydrolase activity:                  TRUE 16, FALSE 0, UNDETERMINED 0
GO:0052689 carboxylic ester hydrolase activity: TRUE 14, FALSE 2, UNDETERMINED 0
GO:0017171 serine hydrolase activity:           TRUE 15, FALSE 1, UNDETERMINED 0
```

That is this review's conclusion reached by a different route — `GO:0016787` is the exact LCA,
`GO:0052689` blocked by the two arylformamidases and `GO:0017171` by HIDH — and it also settles
the equality of the `WITH/FROM` sets across all three genes by measurement (QuickGO per
accession, plus the committed TSVs).

**1. `GRANULARITY_MISMATCH` removed from both hydrolase rows.** This review kept it on the
literal reading of the enum ("parent term is true but uninformative") while simultaneously
arguing that `GO:0016787` is the genuine LCA. Those two are in tension: `failure_modes` records
the *biological shape of a propagation issue*, and this propagation has none — the parent is
uninformative because the donor set is heterogeneous, not because the transfer could have been
more specific. `root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT` alone now carries the row, matching
AADACL2 and AADACL4. (The schema's enum description does not yet distinguish the two readings and
is worth clarifying; that is a repo question, raised in #2286.)

**1b. Superseded: the `IPR013094` assessment was aligned too.** This section originally kept
`SOURCE_EVIDENCE_WEAK` on the hydrolase rows and `source_status: SOURCE_WEAK_OR_INFERRED` on the
`IPR013094` source entity, calling the latter "a separate and still-correct judgment". Both are
now removed/changed, because the argument against the first applies unchanged to the second: the
root cause recorded on the row is **redundancy** with the `IPR017157`-derived `GO:0052689`, which
says nothing about source strength, and `IPR013094` — the alpha/beta-hydrolase fold-3 signature —
is not a weak source. This review's own comment on that entity already concludes the fold match
carries nothing ("the activity conclusion here is carried by the intact Ser-Asp-His triad and by
the subfamily signature IPR017157, not by this fold match"), which is precisely what
`CIRCULAR_OR_REDUNDANT` means. AADACL2 and AADACL4 make the identical fold-level argument and both
record `CIRCULAR_OR_REDUNDANT`; `IPR013094` appears in only these three reviews repo-wide, so that
is the complete comparison set. All six hydrolase rows and all three `IPR013094` source entities
now agree.

**2. Yeast BNA7 does resolve.** This gene's own audit reached `SGD:S000002836` through its
Alliance record, failed, and honestly reported the nucleophile as unresolved — hence its
13-of-14 serine count. `xref:sgd-S000002836` returns **Q04066** directly, whose `ACT_SITE 110`
UniProt labels the nucleophile and which reads as **Ser**. So the node-wide tally is **15 of 16
donors with a serine nucleophile**, and both arylformamidases are themselves serine hydrolases.
This strengthens the conclusion: the sole non-serine donor is still HIDH. `AADACL3-bioinformatics/
RESULTS.md` is deliberately left as generated — 13 of 14 is what its resolver really produced —
and the correction is recorded as a supersession citing the shared audit.

**3. HIDH is a bifunctional carboxylesterase, not a weakly inferred hydrolase.** Its
`source_status` moves from `SOURCE_WEAK_OR_INFERRED` to `SUPPORTS_TRANSFER`: `GO:0106435
carboxylesterase activity` is held by **IDA**, alongside the `GO:0033987` dehydratase IDA, so its
esterase activity is slight but not inferred. It genuinely supports the hydrolase parent, and its
role in the argument is unchanged — it is the single donor that refutes `GO:0017171`. Worth
noting that call rests on fold position rather than a UniProt label (`ACT_SITE 164` is annotated
"Proton acceptor", `ECO:0000305`), but the elbow pentapeptide corroborates it independently:
15 of 16 donors read G-x-S-x-G while HIDH alone reads `GETSG`, and a sensitivity analysis in the
shared audit shows `GO:0017171` fails at this node whether HIDH is scored FALSE or UNDETERMINED.

**4. The mechanism term's node placement.** Unchanged in substance from this review's
`suggested_questions`, and now measured: at the family node `PTN009058713` the three donors PAINT
cites — human AADAC, mouse Aadac and mouse Nceh1 — are all `IPR017157` members, all serine, all
ester hydrolases, and **all three hold `GO:0017171` by IDA**. All three blockers at the deep node
lie outside `IPR017157`. So the recommendation is a node move, not a term change on the row.

### Round-5: retiring the divergence statements this harmonisation made false

Extending the harmonisation to AADACL3 invalidated every statement in the three reviews that
described them as disagreeing — and the round-4 sweep grepped for the `two of them` phrasings but
not for those, which is how they survived a round.

- **AADACL3's `suggested_questions`** said the merged AADACL2 review resolves the same row as
  `MODIFY → GO:0017171` with `TERM_SCOPING_PROBLEM` + `GRANULARITY_MISMATCH`, that "both cannot be
  right about one row", and that "**PR #2266** needs a follow-up to settle it". None of that
  survives: AADACL2 now carries AADACL3's own verdict. Rewritten to ask PAINT only where the
  mechanism term should sit — the question that is genuinely still open — while keeping the
  merges-two-existing-rows argument, which is what settled the matter.
- **AADACL2's and AADACL4's row reasons** motivated the schema request with "since AADACL3's review
  reaches the same LCA conclusion while keeping the mode on the literal reading". That divergence
  no longer exists either. The request stands but the justification changes: all three paralogs now
  encode the row on the propagation-shape reading, which the enum text does not itself state, so
  the convention is carried by argument rather than by the schema.
- **The shared audit's "Why this audit exists"** section is explicitly marked *historical*, with a
  closing "Settled outcome" paragraph, so the one remaining mention of `TERM_SCOPING_PROBLEM`
  cannot be read as a live claim.
- **AADACL3's earlier conflict section** (in `AADACL3-notes.md`) is rewritten in the past tense
  with the resolution stated up front, rather than opening "This review now conflicts with the
  merged AADACL2 review … a curator reading both files today gets contradictory advice".
- **AADACL3's 13-of-14 serine count** now carries the pointer to the shared audit's 15 of 16 *at
  the place the count is stated* (`AADACL3-ai-review.yaml`, the analysis `review_notes`), not only
  in a `propagation_review` comment and a reference entry elsewhere in the file.

### The automation, which is the actual fix

Five items on this PR (9, 13, 17, 18, 22) were the same defect: a claim corrected in one place and
left standing in another, twice in a file that recorded the lesson. Round 5's own bullet asserted
two of these fixes that the tree did not contain. Being more careful demonstrably does not work, so
the checks are now a committed script:

`genes/human/AADACL2/AADACL2-bioinformatics/check_paralog_agreement.py`

It enforces two things across **AADACL2, AADACL3 and AADACL4** — the reviews, the notes files and
the audit prose:

1. **the agreement invariant** — for each of the six `GO:0016787` rows: `MODIFY` →
   `GO:0052689`, `root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT`, no `GRANULARITY_MISMATCH`,
   `supporting_entities` equal to that gene's own GOA `WITH/FROM` column, one shared 17-token set
   across all three genes, `core_functions` molecular function `GO:0052689`, and the shared audit
   cited;
2. **the stale-claim greps** — no live `TERM_SCOPING_PROBLEM`, "both cannot be right", "needs a
   follow-up", `IDA … two of them`, unqualified "every donor at the family node", "13 of 14"
   without a superseding pointer, or "not yet in the tree", in *any* of those files. Text
   explicitly marked historical is exempt, and the exemption is itself checked.

All **eleven** guards were verified by **deliberately breaking them**: `--self-test` copies the
tree to a temporary directory, applies one mutation at a time, and requires each to be caught. That
paid for itself immediately — the first run reported `superseding pointer removed from a count:
NOT caught`, and the cause was the *mutation*, which only reworded a lead-in and left the pointer
inside the search window, so nothing was actually broken and the guard was right to stay silent.
Reading the guard would not have found that; only trying to break it did. The mutation now deletes
the whole clause and raises if its target text has moved, so the self-test cannot silently pass
later.

Two design points worth recording. Curator-facing text (reviews, the audit prose, `RESULTS.md`) is
grepped wholesale, but **notes files are journals** — a journal recording "X was wrong, now fixed"
necessarily contains X, so a blanket grep is unusable there. They are scanned paragraph by
paragraph and a stale phrase is allowed only where the paragraph, or a marker at the top of its
section, marks the passage retrospective; an unqualified stale sentence in running prose fails,
which is exactly the shape of the AADACL3 section that survived four rounds. And the section-level
exemption requires a *strong* marker (superseded, historical, since resolved …) rather than any
past tense, so appending a new live claim to an old section is not laundered by its header — there
is a self-test mutation for precisely that.

Integration with `just` is out of scope for a gene PR, so it runs as
`uv run --no-project --with pyyaml python check_paralog_agreement.py` and is documented in the
audit file.

Generalisable lesson, and the reason this is a script rather than a resolution: **when a change
makes a claim false, grep for the claim, not for the sentence you remember writing** — and when the
change is "these two now agree", the claims to hunt are the ones asserting that they do not.
