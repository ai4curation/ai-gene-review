# pax3-a (Xenopus laevis, Q645N4) — curation notes

Project: `projects/NEURAL_CREST_ORIGINS.md`, Tier 2 (neural plate border specifiers).
Homeolog: `pax3-b` (Q0IH87; Xenbase pax3.L/.S). Q645N4 is the pax3.S gene (Xenbase XB-GENE-482744, chromosome 5S).

## 2026-10-05 — initial review

### Identity and molecular activity
- Paired-domain (aa 34-161, PAI + RED subdomains) plus paired-type homeodomain (aa 220-279) transcription factor;
  Pax3/7 subgroup of the paired box family (UniProt; PANTHER PTHR45636:SF17).
- Direct, sequence-specific DNA binding and activation in frog: Pax3 binds a predicted site in the snail2 promoter
  (mutation abolishes, anti-Pax3 supershifts) [PMID:24360906 "We showed that Pax3 binds efficiently to snail2 oligonucleotide but much less to the oligonucleotide mutated in the putative binding site (Figure 4D)"].
- Positive autoregulation [PMID:24360906 "These data show that Pax3 exerts a positive autoregulation on its own transcription and suggest new putative regulatory elements mediating this regulation."].
- Immediate-early direct targets (cycloheximide-resistant) include the crest specifiers [PMID:24360906 "We demonstrated
  that the neural border specifiers Pax3 and Zic1 are direct upstream regulators
  of neural crest specifiers Snail1/2, Foxd3, Twist1, and Tfap2b."]. Independent screen
  [PMID:24360908 "Among the targets identified
  we found several well-characterized NC-specific genes, including snail2, foxd3,
  gbx2, twist, sox8 and sox9"].
- In vivo occupancy (X. laevis, stage 14 Pax3-FLAG ChIP-seq) [PMID:38683994 "(B) Pax3 ChIP-seq analysis identified 657 candidate direct targets, among which 475 expressed in NC."].
- All frog evidence is for activation; mammalian Pax3 can also repress (mouse Pax3 carries GO:0000122 IGI), but no frog
  repressor evidence found. MF chosen: GO:0001228 (activator) as NEW. Comparator: human PAX3 (P23760) and mouse Pax3
  (P24610) both carry GO:0045944 by IDA (QuickGO, see below), so the activator interpretation is family-consistent.

### Expression (network layer)
- Induced in lateral/posterior neural plate by Wnt from posterior non-axial mesoderm [PMID:10433827 "Pax-3 inductive signals from posterior nonaxial mesoderm are
Wnt-dependent."]. This makes Pax3 a Wnt *target*, relevant to the Wnt-pathway rows.
- Co-expressed with Zic1 at the presumptive crest before foxd3/slug [PMID:15843410 "Pax3 and Zic1 are expressed in an overlapping manner in the
presumptive neural crest area of the Xenopus gastrula, even prior to the onset
of the expression of the early bona fide neural crest marker genes Foxd3 and
Slug."].
- Also in hatching gland progenitors [PMID:17409353 "In addition, Pax3 is expressed
in progenitors of the hatching gland"].
- Border specifiers are "not always maintained in the neural crest progenitors themselves" [PMID:24360906].

### Gain of function
- Pax3+Zic1 together induce ectopic crest in ventral ectoderm; either alone only expands within dorsolateral ectoderm [PMID:15843410].
- Pax3+Zic1 sufficient for full NC determination: migration and differentiation of derivatives [PMID:23509273 "coactivating transcription
factors Pax3 and Zic1 not only initiate neural crest specification from various
early embryonic lineages in Xenopus and chicken embryos but also trigger full
neural crest determination."].
- Pax3 alone: hatching gland [PMID:17409353 "Pax3 and Zic1 are necessary and sufficient to
promote hatching gland and preplacodal fates, respectively, whereas their
combined activity is essential to specify the neural crest."].

### Loss of function
- MO knockdown: Pax3 required for NC, acts downstream of Msx1, mediates Wnt/FGF8 [PMID:15691759 "Msx1 and Pax3 are both required for neural crest
formation, display overlapping but nonidentical activities, and that Pax3 acts
downstream of Msx1."].
- Homeolog note: the GOA experimental rows are duplicated on pax3-a and pax3-b (Q0IH87) — the same PMIDs/ECOs
  (QuickGO, below). The MOs/mRNAs are generic "Pax3"; abstracts do not say which homeolog was targeted. Treat the
  evidence as applying to Xenopus Pax3 activity, shared by both homeologs.

### Network layer decision
Pax3 is a **neural plate border specifier** (upstream of Snail/Foxd3/Sox8/Twist), induced by Wnt/FGF via Msx1, that
with Zic1 directly switches on the crest specifiers. It therefore does work at two levels:
1. Forming the border region — `GO:0014029` neural crest formation (definition: "formation of the specialized region of
   ectoderm between the neural ectoderm (neural plate) and non-neural ectoderm") — the correct level for a border
   specifier under the pending project convention. ACCEPT both experimental rows.
2. Initiating crest fate — Pax3+Zic1 directly activate the specifiers and are sufficient for full determination.
   `GO:0014034` neural crest cell fate commitment (already on the gene, IMP/IGI PMID:15843410) captures this.
   Did NOT add `GO:0014036` fate specification: it is a descendant (part_of) of GO:0014034 which the gene already
   carries, and the specification proper is executed by the downstream specifiers (sox8/sox9/sox10/snai2 narrowed to
   GO:0014036 in Tier 1). Pax3 is the upstream inducer, so the commitment-level term (which includes induction of
   the fate) is the better level, consistent with foxd3-a (also GO:0014034).
- Hatching gland: a separate border fate driven by Pax3 alone; KEEP_AS_NON_CORE (real, but frog/fish-specific border
  derivative). Myogenesis/melanocyte roles (mammalian Pax3) have no frog annotation here; not added.
- FGF and Wnt signaling pathway rows: Pax3 is a transcriptional target/integrator downstream of the signals (its
  expression is Wnt-induced; FGF8 acts via Msx1 and Pax3), not a component of the signal transduction cascade.
  MARK_AS_OVER_ANNOTATED.

### Comparator check (QuickGO, 2026-10-05)
Query: `https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?goId=GO:0014029&goUsage=descendants&goUsageRelationships=is_a,part_of`
(1911 rows), filtered for symbols matching `pax`. Results:
- X. laevis pax3-a (Q645N4) and pax3-b (Q0IH87): GO:0014029 IMP/IGI and GO:0014034 IMP/IGI/IEA (identical sets).
- X. tropicalis pax3 (Q28DP6): GO:0014029 and GO:0014034 by ISS.
- All other Pax3/Pax7 hits (many TrEMBL incl. pax7.L/.S, PAX3/PAX7 of other vertebrates) are GO:0014034 IEA (ARBA).
- Human PAX3 (P23760), mouse Pax3 (P24610), zebrafish pax3a/pax7: **no** annotation in the GO:0014029 subtree.
  Mouse Pax3 instead carries GO:0001755 neural crest cell migration (IMP) and GO:0048066 developmental pigmentation
  (IMP), plus GO:0045944 (IDA) and GO:0000122 (IGI). Human PAX3 carries GO:0045944 and GO:0045893 by IDA.
So the NC-formation/commitment terms are frog-specific in experimental annotation; mammalian Pax3 crest annotation is
at the migration level (Splotch). This is a coverage difference, not a convention against border genes carrying NC terms
(Pax3 in mouse does carry an NC-branch term). No NEW NC term proposed.

### Evolution / outgroups
- Pax3/7 border expression and BMP responsiveness are conserved in amphioxus [PMID:18562679 "Ectodermal Zic and Pax3/7 expression marks the neural plate border, and amphioxus SoxB1-a expression labels the entire neural plate."],
  while most crest specifiers are absent from the amphioxus border [PMID:18562679 "In comparing the expression of amphioxus homologs of these genes, we found that they were expressed in broad and diverse patterns, but were absent from the amphioxus neural plate border"].
- So Pax3/7 belongs to the ancestral chordate border layer; what is vertebrate-specific is the downstream wiring
  (Pax3+Zic1 -> snail2/foxd3/sox8/twist1). Lamprey deploys the upstream border factors conservedly [PMID:17765683].
- Open: whether amphioxus Pax3/7 can bind/activate vertebrate snail2/foxd3 regulatory elements (protein vs cis change).

### GO gaps
- No neural plate border formation/specification term exists (project notes); raised as a suggested question.
