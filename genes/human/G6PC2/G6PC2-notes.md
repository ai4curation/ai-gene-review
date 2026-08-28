# G6PC2 (Q9NQR9) — research notes

Human glucose-6-phosphatase catalytic subunit 2, historically IGRP (islet-specific
glucose-6-phosphatase catalytic subunit-related protein). HGNC:28906, chr 2q31.1,
355 aa, EC 3.1.3.9.

Journal-style notes, appended as research proceeded. Every assertion carries inline
provenance in the form `[PMID:xxxxxxx "verbatim supporting text"]`. Quotes were
checked as verbatim substrings of the cached `publications/PMID_*.md` records.

---

## 1. Identity, paralogy and tissue restriction

G6PC2 is one of three human glucose-6-phosphatase catalytic subunits. G6PC1 is the
liver/kidney gluconeogenic enzyme, G6PC3 is ubiquitous, G6PC2 is islet-restricted
[PMID:32569842 "The G6PC gene family is comprised of three members, namely G6PC1, G6PC2
and G6PC3 [1]. G6PC1 is predominantly expressed in liver and kidney where it catalyzes
the terminal step in the gluconeogenic and glycogenolytic pathways, whereas G6PC3 is
widely expressed, with especially high expression in kidney, testis, skeletal muscle and
brain"].

It was cloned from mouse insulinoma by subtractive hybridisation and shown to be ~50%
identical to the liver enzyme with the catalytic residues conserved
[PMID:10078553 "structurally related (50% overall identity) to the liver
glucose-6-phosphatase and exhibited similar predicted transmembrane topology,
conservation of catalytically important residues, and the presence of an endoplasmic
reticulum retention signal"]. Expression is islet/beta-cell dominated
[PMID:10078553 "the mRNA was highly expressed in pancreatic islets and expressed more in
beta-cell lines than in an alpha-cell line"], confirmed later at the protein level in
human and mouse [PMID:32569842 "G6PC2 is predominantly expressed in pancreatic islet beta
cells."]. Human and mouse promoters are islet-active; the rat orthologue is a pseudogene
[PMID:11297555 "the rat IGRP gene does not appear to encode a protein as a result of a
series of deletions and insertions in the coding sequence"]. Note the rat exception when
reading rodent literature.

Isoform note: three UniProt isoforms (Q9NQR9-1/-2/-3); isoforms 2 and 3 truncate at
residues 103 and 155 respectively and so lose the His-174 nucleophile. Alternative
splicing differs between pancreas and lymphoid tissue (PMID:16520917, title-level only —
not used to support any annotation here).

## 2. Subcellular location and topology

Experimentally an ER-membrane multipass glycoprotein
[PMID:15044018 "IGRP is a glycoprotein, held in the endoplasmic reticulum by nine
transmembrane domains, which is degraded in cells predominantly through the proteasome
pathway that generates the major histocompatibility complex class I-presented peptides"].
UniProt records `SUBCELLULAR LOCATION: Endoplasmic reticulum membrane
{ECO:0000269|PubMed:15044018}; Multi-pass membrane protein`, N-glycosylation at Asn-92,
and a C-terminal (352-355) "Prevents secretion from ER" motif. Active site residues are
annotated at His-115 (proton donor) and His-174 (nucleophile) — the latter is the
phosphohistidine acceptor shared with G6PC1.

So GO:0005789 (ER membrane) is the informative location; GO:0005783 (ER) and GO:0016020
(membrane) are true but generic parents.

## 3. The catalytic-activity question — this is the contested part

**Round 1 (1999-2001): no activity detectable.** The cloning paper explicitly failed to
demonstrate catalysis [PMID:10078553 "the IGRP failed to show glucose phosphotransferase
or phosphatase activity with p-nitrophenol phosphate, inorganic pyrophosphate, or a range
of sugar phosphates hydrolyzed by the liver enzyme"], concluding
[PMID:10078553 "While the metabolic function of the enzyme is not resolved"]. Two years
later the same group still wrote [PMID:11297555 "Its catalytic activity, however, has not
been defined."]. As late as 2004 the topology paper opened with
[PMID:15044018 "The islet-specific glucose-6-phosphatase-related protein (IGRP) has no
known catalytic activity"].

**Round 2 (2004): activity demonstrated on overexpression.** Petrolonis et al. expressed
IGRP in insect cells and measured G6P hydrolysis
[PMID:14722102 "IGRP overexpressed in insect cells possesses enzymatic activity comparable
to the previously described G-6-Pase activity in islets."], with
[PMID:14722102 "The K(m) and V(max) values determined using glucose-6-phosphate as the
substrate were 0.45 mm and 32 nmol/mg/min by malachite green assay"] and a selective
inhibitor that did not touch the liver enzyme
[PMID:14722102 "this inhibitor did not affect LG-6-Pase activity, while conversely
LG-6-Pase inhibitors did not affect IGRP activity"], concluding
[PMID:14722102 "These data demonstrate that IGRP is likely the authentic islet-specific
glucose-6-phosphatase catalytic subunit"]. This is the annotation source for GOA's EXP
GO:0004346 and for UniProt's `CATALYTIC ACTIVITY ... ECO:0000269|PubMed:14722102`.

**Round 3: activity is real but weak, and that weakness is the recurring technical
obstacle.** The activity is genuine but far below G6PC1's, which is exactly why the early
assays failed and why later work needed engineered overexpression systems:
[PMID:34954144 "Previous attempts to characterize such SNPs were limited by the very low
inherent G6Pase activity and expression of G6PC2 protein in islet-derived cell lines."];
side-by-side at matched protein levels [PMID:34954144 "G6PC1 exhibited much higher G6Pase
activity than G6PC2 in these in vitro assays"]; and as a general statement of the field
[PMID:32213654 "because both G6PC1 (Lei, et al. 1993) and G6PC3 (Shieh et al. 2003) have
much higher catalytic activity than G6PC2 (Petrolonis, et al. 2004)"].

**Round 4: mechanism confirmed genetically and structurally.** The His-174 nucleophile is
required [PMID:34954144 "mutation of the equivalent AA in G6PC2, histidine 174, abolished
phosphatase activity"]. The PAP2 phosphatase motif is required
[PMID:38095063 "residues forming part of a type 2 phosphatidic acid phosphatase (PAP2)
motif are critical for enzyme activity"]. And the structural basis for the G6PC1/G6PC2
activity gap has been localised to the substrate cavity
[PMID:38095063 "these data demonstrate that differences in the putative substrate cavity
contribute to the markedly higher G6Pase activity of G6PC1 relative to G6PC2"]. A
selective small-molecule inhibitor now exists [PMID:38431189 "We show that VU0945627
preferentially inhibits human G6PC2 versus human G6PC1 but activates human G6PC3."].

**Round 5: activity is required in vivo.** Islets from G6pc2-null mice lose the activity
[PMID:23274894 "Glucose-6-phosphatase activity was reduced, whereas basal cytoplasmic
calcium levels were elevated in islets isolated from G6pc2 KO mice."] and lose glucose
cycling [PMID:32213654 "in isolated islets, glucose-6-phosphatase activity and glucose
cycling are abolished and glucose-stimulated insulin secretion (GSIS) is enhanced at
submaximal but not high glucose"].

**Net reading for curation.** GO:0004346 is correct for G6PC2 — the annotation should be
kept, not removed. What should *not* be asserted is that its activity is comparable to
G6PC1's, or that the earlier negative reports were simply wrong: they reflect a genuinely
low specific activity that only became measurable with overexpression systems. The claim
"weak/largely absent" is half right — largely undetectable in the original assays, weak
but physiologically decisive in vivo.

## 4. What the enzyme actually does: a futile cycle, not gluconeogenesis

The islet is not a gluconeogenic tissue and G6PC2 does not release free glucose to the
blood. Its hydrolysis of G6P runs *against* glucokinase inside the beta cell:
[PMID:32569842 "G6PC2 hydrolyzes glucose-6-phosphate to glucose and inorganic phosphate,
thereby creating a futile substrate cycle that opposes the action of glucokinase."] and
[PMID:23274894 "This glucokinase/G6pc2 futile substrate cycle is predicted to reduce
glycolytic flux and hence insulin secretion."]. The consequence is a shift in the glucose
set point of secretion [PMID:32213654 "a glucokinase/G6PC2 futile cycle, rather than
glucokinase alone, determines the rate of beta cell glycolytic flux and hence the
sensitivity of GSIS to glucose"].

Directionality: G6PC2 *restrains* insulin secretion
[PMID:23274894 "G6pc2 represents a novel, negative regulator of basal GSIS that acts by
hydrolyzing glucose-6-phosphate, thereby reducing glycolytic flux"]. Loss of the gene
lowers, not raises, fasting glucose — the opposite of what a gluconeogenic enzyme would
give [PMID:17265032 "a small but significant decrease in blood glucose was observed in
both male (-14%) and female (-11%) G6pc2 (-/-) mice"], and the effect is islet-autonomous
[PMID:32213654 "In adult mice, beta cell-specific deletion of G6pc2 was sufficient to
reduce FBG without changing FPI."].

There may be a physiological reason for keeping a futile cycle: it buffers against
hypoglycaemia [PMID:32569842 "blood glucose fell to 70 mg/dl or less in G6pc2 KO but not
WT mice, suggesting that G6PC2 may have evolved, in part, to prevent hypoglycemia"].

Curation consequence: the three GO:0006094 (gluconeogenesis) rows in GOA are inherited
from the G6PC1-like ancestral/pathway context, not from G6PC2 biology. Reactome's own
pathway summary states gluconeogenesis "is confined to cells of the liver and kidney"
(reactome/R-HSA-70263.md), while the G6PC2 reaction it assigns to that pathway is
explicitly the islet one (R-HSA-3266566 "G6PC2 hydrolyzes G6P to form Glc and Pi
(islet)"). GO:0051156 (glucose 6-phosphate metabolic process) is the honest replacement —
and is also what PAN-GO asserts for Q9NQR9 (UniProt cross-reference "PAN-GO; Q9NQR9; 4 GO
annotations based on evolutionary models"; the UniProt GO cross-reference block lists
`GO:0051156; P:glucose 6-phosphate metabolic process; IBA:GO_Central`).

## 5. Human genetics: fasting plasma glucose

The GWAS finding is robust and repeatedly replicated. Discovery
[PMID:18451265 "SNP rs560887 maps to intron 3 of the G6PC2 gene, which encodes
glucose-6-phosphatase catalytic subunit-related protein (also known as IGRP), a protein
selectively expressed in pancreatic islets"] with the mechanism proposed at the time
[PMID:18451265 "We speculate that G6PC2 regulates FPG by modulating the set point for
glucose-stimulated insulin secretion in pancreatic beta cells."] — a speculation the mouse
work above subsequently confirmed. Importantly the same SNP
[PMID:18451265 "was associated with FPG (linear regression coefficient beta = -0.06
millimoles per liter per A allele, combined P = 4 x 10(-23)) and with pancreatic beta cell
function (Homa-B model, combined P = 3 x 10(-13)) in three populations; however, it was
not associated with type 2 diabetes risk"].

Replication with secretion phenotypes (this is the GOA IMP reference)
[PMID:20668700 "GCK rs1799884, G6PC2 rs16856187 and MTNR1B rs10830963 showed associations
to fasting glucose"] and [PMID:20668700 "G6PC2 rs16856187 showed evidence for association
to first-phase insulin secretion (p = 0.0108), and second-phase insulin secretion under a
dominant genetic model (p = 0.0431)."]. Note this is human association data, not a
laboratory perturbation; the GOA evidence code is IMP, which is generous, but the
conclusion is independently corroborated by the mouse knockouts.

Promoter variants are functional [PMID:20622168 "The rs13431652-A allele is associated
with increased FPG and elevated promoter activity, consistent with the function of G6PC2
in pancreatic islets."]. Coding variation matters too — 16 of 22 nonsynonymous SNPs
destabilise the protein and four more impair activity, with
[PMID:34954144 "Electronic health record-derived phenotype analyses showed an association
between high-impact SNPs and FBG, but not other diseases/metabolites."] — i.e. the human
phenotypic footprint of G6PC2 is confined to glycaemia.

## 6. Alpha cells too (recent)

G6PC2 is not purely a beta-cell story: an inducible alpha-cell-specific knockout shows
[PMID:39742505 "this gene plays a critical role in controlling glucose suppression of
amino acid-stimulated glucagon secretion independent of alterations in insulin output,
islet hormone content, or islet morphology, findings that we confirmed in primary human
alpha cells"], concluding [PMID:39742505 "our data demonstrate that G6PC2 affects glycemic
control via its action in alpha cells"]. Mechanistically the same set-point logic
[PMID:39742505 "G6PC2 in alpha cells affects glucagon secretion by modulating the set
point for glucose sensing and glucose-suppressed glucagon secretion (GSGS)"].

This justifies GO:0070092 (regulation of glucagon secretion) as a genuine, if newer,
biological process for G6PC2.

## 7. Type 1 diabetes autoantigen (IGRP)

The reason the protein is famous outside metabolism
[PMID:12815107 "we reveal that the autoantigen targeted by a prevalent population of
pathogenic CD8+ T cells in nonobese diabetic mice is islet-specific glucose-6-phosphatase
catalytic subunit-related protein (IGRP)"], with the human relevance flagged in the same
paper [PMID:12815107 "The human IGRP gene maps to a diabetes susceptibility locus,
suggesting that IGRP also may be an antigen for pathogenic T cells in human type 1
diabetes"]. Its degradation route feeds MHC-I presentation
[PMID:15044018 "degraded in cells predominantly through the proteasome pathway that
generates the major histocompatibility complex class I-presented peptides"].

Crucially, being an autoantigen is **not** a molecular function of the protein and it is
not causally required for disease [PMID:21896930 "The absence of G6pc2 did not affect the
time of onset, incidence, or sex bias of type 1 diabetes in NOD/ShiLtJ mice."], although
[PMID:21896930 "G6pc2 is an important driver for the selection and expansion of
islet-reactive CD8(+) T cells infiltrating NOD/ShiLtJ islets"]. So: describe it in the
gene summary, but do not propose a GO biological-process annotation for it. The
autoantigenicity is a property of the peptides a beta-cell-restricted, proteasomally
degraded protein happens to present, not an evolved activity.

## 8. Things G6PC2 does *not* do

- It does not supply blood glucose by gluconeogenesis or glycogenolysis (§4).
- It does not detectably influence 11beta-HSD1/glucocorticoid signalling despite sharing
  the ER G6P pool with H6PD [PMID:37855366 "These data suggest that HSD11B1 activity is
  not significantly affected by the presence or absence of G6PC1 or G6PC2."].
- It has no established role outside islets: [PMID:32213654 "Even if G6pc2 is expressed at
  trace levels in these non-pancreatic tissues, because both G6PC1 (Lei, et al. 1993) and
  G6PC3 (Shieh et al. 2003) have much higher catalytic activity than G6PC2 (Petrolonis, et
  al. 2004), these results suggest that G6PC2 is highly unlikely to directly affect
  metabolism in these tissues."]. (UniProt records lower-level testis expression and HPA
  calls the gene "Group enriched (pancreas, retina)"; no function is attached to either.)

## 9. Curation decisions taken

| GOA row | Evidence | Action | Rationale |
|---|---|---|---|
| GO:0005783 ER (is_active_in) | IBA | KEEP_AS_NON_CORE | true but generic vs GO:0005789 |
| GO:0006094 gluconeogenesis | IBA | MODIFY → GO:0051156 | ancestral G6PC1 function; islet divergence (§4) |
| GO:0004346 G6Pase activity | IBA | ACCEPT | core MF; Q9NQR9 in WITH/FROM = own experimental grounding |
| GO:0016020 membrane | IBA | MODIFY → GO:0005789 | root-level; ER membrane is the real location |
| GO:0004346 | IEA | ACCEPT | core MF, matches RHEA:16689/EC 3.1.3.9 |
| GO:0005789 ER membrane | IEA | ACCEPT | core location, experimentally backed |
| GO:0005783 ER | IEA | KEEP_AS_NON_CORE | generic parent |
| GO:0006094 | TAS Reactome | MODIFY → GO:0051156 | pathway-membership artefact (§4) |
| GO:0006094 | IEA UniPathway | REMOVE | mechanical map from a by-similarity PATHWAY line |
| GO:0004346 | EXP PMID:14722102 | ACCEPT | direct kinetic demonstration |
| GO:0005789 | TAS Reactome | ACCEPT | core location |
| GO:0042593 glucose homeostasis | IMP | ACCEPT | core; corroborated by mouse KO |
| GO:0050796 reg. insulin secretion | IMP | MODIFY → GO:0061178 | glucose-stimulated specifically |

Only the UniPathway row is removed outright: the other two gluconeogenesis rows carry a
defensible kernel (G6P hydrolysis) that MODIFY preserves, whereas UPA00138 asserts
pathway membership with no G6PC2-specific evidence behind it.

## 10. Open questions

- What sets the ~order-of-magnitude activity gap between G6PC1 and G6PC2 beyond the
  substrate-cavity residues already identified (§3, PMID:38095063)? Is low kcat itself
  adaptive for a set-point cycle?
- Is the rs492594 V219L CRAC-motif variant functionally consequential in vivo? The in
  vitro answer depends on whether cholesterol is present (PMID:38095063), which is exactly
  the kind of context-dependence that could explain the disputed human association.
- Does G6PC2 require SLC37A4 to supply luminal G6P, as G6PC1 does? Relevant because the
  VU0945627 inhibitor also hits SLC37A4 (PMID:38431189).
- Retina: HPA lists retina alongside pancreas as enriched, and one of the UniProt cDNA
  clones (isoform 2) is retinal. No functional work found.
