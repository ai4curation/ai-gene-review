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
| Q5NUF3 | soybean **HIDH** | 2-hydroxyisoflavanone **dehydratase** (a lyase) |
| Q9HTI0 | *P. aeruginosa*, unreviewed | — |

The set mixes carboxylesterases, amidohydrolases and a lyase, which is precisely
why the propagated term stopped at the generic `hydrolase activity`: that is the
most specific term that survives across this clade. The inclusion of HIDH, whose
characterised primary activity is a dehydratase rather than a hydrolase, is a
mild inconsistency in the supporting set (though HIDH does retain slight
carboxylesterase activity). Either way the term is *correct for AADACL3* but far
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
and `InterPro:IPR017157` respectively. The distinction matters: IPR013094
(Alpha/beta hydrolase fold-3) is a *fold* domain whose members include
non-hydrolases such as HIDH, so IPR013094 → GO:0016787 is a fold-to-activity
mapping. IPR017157 (Arylacetamide deacetylase) is a subfamily signature and
matches AADACL3 across residues 19–403 with PIRSF037251 scoring 5.8e-82, so
IPR017157 → GO:0052689 is a subfamily-to-activity mapping. Both land on a
defensible answer here, but only the second one is a well-grounded inference in
its own right.

## Actions taken

| # | term | evidence | action | why |
|---|---|---|---|---|
| 1 | GO:0016787 hydrolase activity | IBA | MODIFY → GO:0052689 | correct but subsumed by a term GOA already carries; clade heterogeneity explains the generic level |
| 2 | GO:0016020 membrane | IBA `is_active_in` | ACCEPT | tight, topologically coherent source set; corroborated by concordant Phobius + TMHMM |
| 3 | GO:0016020 membrane | IEA `located_in` | ACCEPT | same conclusion from an independent pipeline; supported despite UniProt having no TRANSMEM feature |
| 4 | GO:0016787 hydrolase activity | IEA (IPR013094) | MODIFY → GO:0052689 | fold-derived and subsumed; the specific term comes from the subfamily signature instead |
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
