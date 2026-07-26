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

Affinage returned an empty record (`n_discoveries: 0`, `citation_count: 0`,
`gates_passed: True`). Per the campaign rules an empty provider record is not
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

The AADACL2 review (PR #2266) reported that PAINT's node placement for this family
is inverted: `GO:0017171 serine hydrolase activity` sits only at ortholog-level
nodes, while the shared family node `PTN009058713` carries `GO:0016020 membrane` —
yet it is the catalytic triad that transfers family-wide and the membrane anchor
that does not. I checked both halves of that against AADACL3's own record rather
than importing it, and it holds, with two differences worth stating.

**The mechanism half is confirmed, and quantified.** Section 7 of the
bioinformatics report reads the residue at the first annotated active site of every
WITH/FROM source on AADACL3's own hydrolase-activity IBA:

- [file:human/AADACL3/AADACL3-bioinformatics/RESULTS.md "Audited: GO:0016787 (IBA, GO_REF:0000033). 17 WITH/FROM tokens, 14 resolved to a protein, 14 with a readable nucleophile, of which **13 are serine**. Non-serine: HIDH_SOYBN T164."]

The amidohydrolase members are no obstacle to a mechanism term: mouse Afmid, a
formamidase, is itself a serine hydrolase with `S162`. (Yeast BNA7 and rat Aadac
could not be resolved to a single reviewed UniProt entry through the Alliance
record and are reported unresolved rather than counted either way, so the 13-of-14
figure is a count of what was readable.) The single obstacle at `PTN009058710` is
soybean HIDH, whose nucleophile is **Thr164** — so `GO:0017171` could be placed at
that node only if HIDH is excluded, whereas at the tighter `PTN009058713` there is
no obstacle at all. That is a sharper version of the recommendation: the term is
blocked by exactly one member, and it is nameable.

**Where AADACL3 differs from AADACL2 (1): it does inherit a molecular-function
term.** AADACL2/4 inherit no mechanism term, but AADACL3's GOA carries
`GO:0016787 hydrolase activity` IBA from `PTN009058710` — a *different* node from
the membrane row's `PTN009058713`. So for AADACL3 the defect is not absence but
granularity, which is why this review uses MODIFY with two replacements rather
than proposing a new annotation. `GO:0017171` and `GO:0052689` are independent
children of `GO:0016787` (verified against QuickGO: neither is an ancestor of the
other), so the generic term sits exactly at their join and both are needed.

**Where AADACL3 differs from AADACL2 (2): there is no topology contradiction to
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

**Family-wide claims audited.** The AADACL2 review had to retract several
overstatements. Checking mine: no family-wide specificity claim is made — the
review states explicitly that substrate must not be inferred from membership, and
cites the Say1Δ non-rescue result as the reason; the expression statements are
per-gene HPA records with the gene named (AADACL3 placenta/skin-enhanced, AADACL2
skin-enriched, AADACL4 choroid-enhanced) rather than a branch-level claim; and the
two formamidases in the WITH/FROM column are named as amidohydrolases in the
review rather than folded into an esterase generalisation.

**AADACL4 (PR #2263, already merged).** I queried its GOA directly rather than
taking the paralog framing on trust, and it is **row-for-row identical to
AADACL3's**: the same five annotations, the same terms, and the same WITH/FROM
sets, including `GO:0016787` IBA from `PTN009058710` with all seventeen sources and
`GO:0016020` IBA from `PTN009058713`. So the node-placement recommendation applies
to AADACL4 unchanged.

That also corrects one premise in the cross-gene framing: AADACL3 and AADACL4 do
**not** inherit "no mechanism term at all". They inherit `GO:0016787 hydrolase
activity` at a second node, `PTN009058710` — it is simply the uninformative parent
of the term that should be there, which is why MODIFY rather than a new annotation
is the right action for both.

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
| 1 | GO:0016787 hydrolase activity | IBA | MODIFY → GO:0017171 + GO:0052689 | correct but subsumed; the term sits at the join of a mechanism axis (triad, 13/14 sources serine) and a reaction axis (subfamily signature, EC 3.1.1.-) |
| 2 | GO:0016020 membrane | IBA `is_active_in` | ACCEPT | tight, topologically coherent source set; corroborated by concordant Phobius + TMHMM |
| 3 | GO:0016020 membrane | IEA `located_in` | ACCEPT | same conclusion from an independent pipeline; supported despite UniProt having no TRANSMEM feature |
| 4 | GO:0016787 hydrolase activity | IEA (IPR013094) | MODIFY → GO:0017171 + GO:0052689 | fold-derived and subsumed; the fold signature reaches outside the subfamily whose chemistry it asserts |
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
