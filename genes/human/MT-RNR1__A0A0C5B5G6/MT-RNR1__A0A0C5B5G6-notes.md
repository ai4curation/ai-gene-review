# MOTS-c (A0A0C5B5G6, UniProt gene symbol MT-RNR1) — curation notes

Folder follows the `<HOST>__<ACC>` convention for alternative-ORF peptides
(CLAUDE.md, "Alternative-ORF peptides"): MOTS-c is a separate UniProt entry
(A0A0C5B5G6, 16 aa, MOTSC_HUMAN) that UniProt files under the host locus symbol
`MT-RNR1`, the mitochondrial 12S rRNA gene. It is not an isoform or a cleavage
product of any MT-RNR1 product, so it cannot be modelled as a
`functional_isoform` of the host.

## 1. Origin of the peptide, and the one unusual thing about it

The ORF is 51 bp inside the mitochondrial 12S rRNA
[PMID:25738459 "An in silico search for potential sORFs within the human 12S rRNA revealed one consisting of 51 base pairs with a strong Kozak sequence"].
Critically, it cannot be made by the mitochondrial ribosome:
[PMID:25738459 "MOTS-c peptide translation obligatorily occurs in the cytoplasm using the standard genetic code because mitochondrial translation, using the mitochondria-specific genetic code, yields tandem start and stop codons"].
The authors therefore posit export of a polyadenylated mitochondrial transcript
to the cytosol, a route they concede is poorly understood. Nuclear NUMT copies
were excluded as the source of the exact peptide
[PMID:25738459 "we found that none of the putative NUMT-derived peptides shared complete homology with mitochondrial encoded MOTS-c"],
and mtDNA/mtRNA depletion (rho-0 HeLa, actinonin) removed the MOTS-c signal.

So: endogenous existence rests on antibody signal (immunofluorescence,
immunoblot of nuclear extracts), an in-house ELISA, and loss of signal on
mtDNA/mtRNA depletion. No peptide-level mass-spectrometric identification of
endogenous MOTS-c appears in the cached literature. The required cytosolic
translation of a mitochondrially transcribed rRNA-internal ORF remains the
unresolved mechanistic premise of the whole field. **Curation consequence:**
localisation and molecular-interaction annotations are retained where the assay
was done, but the physiological/metabolic phenotype terms that rest entirely on
injecting or adding synthetic peptide are flagged rather than treated as core.

## 2. What the peptide is reported to do, by evidence type

### Secreted/circulating pool (GO:0005576)
[PMID:25738459 "as well as in circulation in human and rodent plasma as determined with a MOTS-c specific ELISA"].
Exercise raises both muscle and plasma levels in human volunteers
[PMID:33473109 "Western blotting for endogenous MOTS-c in skeletal muscle revealed that relative levels (i.e. individual changes based on pre-exercise values) significantly increased after exercise (11.9-fold)"],
[PMID:32182209 — tissue/plasma levels, age-dependent]. This is endogenous-peptide
evidence and is the best-supported location claim.

### Mitochondrion / nucleus (GO:0005739, GO:0005634)
Partial mitochondrial co-localisation
[PMID:25738459 "HeLa and HEK293 cells showed a certain degree of mitochondrial co-localization"];
[PMID:29983246 "endogenous MOTS-c exhibited a predominantly extra-nuclear localization pattern with a certain degree of mitochondrial association"].
Nuclear pool, with endogenous detection and stress dependence
[PMID:29983246 "low levels of endogenous MOTS-c were detected in the nucleus under resting conditions by immunofluorescence microscopy"];
nuclear entry needs the hydrophobic core
[PMID:29983246 "to alanines (8YIFY11 to 8AAAA11) prevented EGFP-MOTS-c from entering the nucleus"].
Reynolds et al. only tracked exogenous FITC peptide
[PMID:33473109 "Using fluorescently labeled MOTS-c peptide (MOTS-c-FITC), we confirmed that exogenously treated MOTS-c also dynamically translocated to the nucleus in a time-dependent manner"],
which is weaker than the Kim 2018 endogenous data but concordant with it.

### Nuclear/ARE molecular activities — the strongest *molecular* claims
- Direct DNA binding by EMSA:
  [PMID:29983246 "we found that MOTS-c directly bound DNA sequences of ARE-containing promoter regions of NRF2 target genes, including HO-1, NQO1, UGT1A1, UGT1A6, TXN, FTL, and GPX2, in a concentration-dependent manner"].
  Caveat: the probe-binding assays used 0.5–6 µg synthetic peptide, and the
  control mutants (YIFY→AAAA, RKLR→AAAA) remove exactly the hydrophobic and
  cationic residues that would mediate non-specific peptide–nucleic-acid
  interaction. Loss of binding in those mutants therefore does **not** establish
  sequence specificity; GO:0003677 (DNA binding) is as far as the evidence goes,
  and a sequence-specific/cis-regulatory-region descendant would over-reach.
- Occupancy of ARE-containing promoters in cells (ChIP-qPCR):
  [PMID:29983246 "The binding of MOTS-c to promoter regions of HO-1 and NQO1 containing ARE sites significantly increased 3 hr after being challenged with GR and tBHP"].
- Transcription-factor binding (GO:0140297): NRF2/NFE2L2
  [PMID:29983246 "NRF2 co-immunoprecipitated with MOTS-c only from nuclear extracts of cells treated with GR and tBHP for 3 hr"];
  ATF1
  [PMID:29983246 "We found that MOTS-c co-immunoprecipitated with ATF1 in the nucleus and that their interaction was strengthened after GR (3 hr)"];
  NFE2L1/NRF1 is the weakest of the three
  [PMID:29983246 "Unlike NRF2, the interaction between MOTS-c and NRF1 was relatively unaltered after GR (3 hr) in nuclear extracts but was decreased in chromatin extracts"].
  All three partners are genuine DNA-binding transcription factors, so
  GO:0140297 is the informative replacement for the bare `protein binding` row
  that GOA also carries against NFE2L2 from the same paper.

### Metabolic effects (Lee 2015) are a cascade, not a molecular activity
Folate-cycle inhibition → AICAR accumulation → AMPK:
[PMID:25738459 "5Me-THF depletion was coupled with the blockade of de novo purine biosynthesis"],
[PMID:25738459 "resulting in an accumulation of endogenous AICAR (5-aminoimidazole-4-carboxamide ribonucleotide) to levels higher than 20-fold in MOTS-c-ST cells compared to control cells"],
[PMID:25738459 "MOTS-c treatment led to the phosphorylation of AMPKα (Thr172) and Akt (Ser473) in a time and dose-dependent manner"],
[PMID:25738459 "MOTS-c appeared to stimulate glucose utilization evidenced by increased glucose clearance and lactate accumulation in culture media"].
No direct molecular target in the folate cycle has been identified; the enzyme
that MOTS-c would inhibit is unknown. Hence:
- GO:0072522 `purine-containing compound biosynthetic process` (involved_in) is
  the wrong *direction*: MOTS-c blocks de novo purine synthesis. The honest term
  is negative regulation (GO:1900372).
- GO:0032147 `activation of protein kinase activity` describes a two-step
  metabolite-mediated consequence (AICAR is the AMPK activator, not MOTS-c), so
  it over-states a direct action on the kinase.

### Muscle / PTEN–AKT–FOXO1 (Kumagai 2021)
[PMID:33554779 "MOTS-c elevated the phosphorylation of AKT at Ser 473"],
[PMID:33554779 "MOTS-c increased the phosphorylation of the c-terminal cluster of PTEN"],
[PMID:33554779 "which stabilizes PTEN, resulting in increased protein abundance but suppressed PTEN phosphatase activity"].
Two problems with the GOA rows from this paper:
1. **GO:2001145 names the wrong enzyme chemistry.** PTEN is a
   phosphatidylinositol-3,4,5-trisphosphate **3**-phosphatase (GO:0016314);
   GO:2001145 is negative regulation of PIP3 **5**-phosphatase activity, the
   INPP5D/SHIP-family reaction. GO has no "negative regulation of PIP3
   3-phosphatase activity" term, so the defensible term is the parent
   GO:0010923 `negative regulation of phosphatase activity`.
2. The muscle-mass effect is marginal and pharmacological:
   [PMID:33554779 "We administered MOTS-c (0.5 mg/kg/day, ip injection) in HFD (60 kcal% fat)-fed mice for 3 wk and examined gastrocnemius, soleus, and plantaris muscle mass."],
   [PMID:33554779 "Although no differences were found between any of the three treatment groups when considering total, gastrocnemius, soleus, and plantaris absolute muscle mass, differences were more visible when performing an adjustment calculation with body weight."].
   GO:0048630 `skeletal muscle tissue growth` therefore rests on a
   body-weight-adjusted difference in injected mice — an over-annotation.

### Bone (two Eur Rev Med Pharmacol Sci papers)
Both are synthetic-peptide dose-response experiments on cultured cells, one in
rat BMSCs [PMID:30468456 "Rat BMSCs were isolated and cultured, followed by osteogenic and lipid differentiation."],
one in the hFOB1.19 line
[PMID:31081069 "Cell viability was significantly increased after treatment of 1.0 μM MOTS-c for 24 h or 0.5 μM MOTS-c for 48 h in a time-dependent manner."].
Neither tests endogenous MOTS-c; GO:0033687 `osteoblast proliferation` is in
fact a CCK-8 viability readout. Both are flagged as over-annotations: they
describe what the peptide does to cells when applied, not a process the
endogenous peptide is known to participate in.

### Antibacterial / host-defence activity — the one well-supported *direct* function not in GOA
[PMID:42611943 "We demonstrate that MOTS-c (mitochondrial open reading frame from the 12 S rRNA type-c) is a mitochondrial-encoded amphipathic and cationic peptide with direct antibacterial and immunomodulatory functions, consistent with the peptide chemistry and functions of known HDPs."],
[PMID:42611943 "MOTS-c targeted Escherichia coli and methicillin-resistant Staphylococcus aureus (MRSA), in part, by targeting their membranes using its hydrophobic and cationic domains. In a mouse model of acute peritonitis, MOTS-c fully neutralized MRSA infectivity. In human monocytes, interferon gamma (IFNγ), lipopolysaccharides (LPS), and differentiation signals each induced the expression of endogenous MOTS-c."].
An earlier, independent group reached the same in-vivo conclusion
[PMID:29096170 "we demonstrated that a Mitochondria-derived peptide (MOTS-c) could significantly improve the survival rate and decrease bacteria loads in MRSA-challenged mice"].

**Participation test (CLAUDE.md):** here the peptide itself does the work — it
aggregates and permeabilises bacteria. It is not merely required for, or a
substrate of, someone else's process. **Comparator check:** the canonical
secreted human antimicrobial peptide CAMP/LL-37 (P49913) carries exactly
GO:0019731 (IDA), GO:0061844 (IDA), GO:0050829 and GO:0050830 — so the
convention for a circulating cationic amphipathic peptide with direct killing
activity is to annotate these terms, and MOTS-c's absence from them is a gap,
not a convention. Proposed as NEW: GO:0061844, GO:0050829, GO:0050830.
Deliberately **not** proposed: GO:0140911 `pore-forming activity` — the papers
show aggregation and surface/membrane damage, not transmembrane pore formation.

## 3. Cross-cutting caveats recorded for the review

- **Dose and route.** Essentially every functional result uses synthetic peptide
  at 0.5–10 µM in culture (100 µM in the antibacterial assays) or 0.5–5 mg/kg/day
  i.p. in mice. Endogenous-level manipulations do not exist, because mtDNA cannot
  be knocked out gene-specifically; actinonin/rho-0 depletion removes all
  mitochondrial gene expression at once.
- **Species.** Most in-vivo work is mouse or rat; human data are correlative
  (plasma/muscle levels, the m.1382A>C / K14Q association [PMID:33468709]).
- **Lab concentration.** The large majority of mechanistic papers come from the
  Cohen/Lee groups. Independent corroboration exists for the anti-MRSA in-vivo
  effect [PMID:29096170] and for exercise/age-related expression
  [PMID:32182209], but not for the ARE/NRF2 nuclear mechanism.
- **Policy applied.** Following CLAUDE.md, no experimental row is REMOVEd for
  being hard to verify. The single REMOVE is the bare `protein binding` row,
  which the protein-binding policy directs to REMOVE because the same paper and
  the same partner already support the more informative GO:0140297.

## 4. Action summary (21 GOA rows)

- ACCEPT ×12: GO:0003677; GO:0006357; GO:0140297 ×3 (ATF1, NFE2L1, NFE2L2);
  GO:0005576 ×2 (IDA + the mirroring IEA); GO:0005634 ×3; GO:0005739 ×2.
- MODIFY ×3: GO:0072522 → GO:1900372 (direction reversed); GO:2001145 →
  GO:0010923 (wrong phosphatase chemistry); GO:0032147 → GO:0071902
  (regulation, not activation — AICAR, not MOTS-c, activates AMPK).
- KEEP_AS_NON_CORE ×2: GO:0043610 regulation of carbohydrate utilization;
  GO:0071902 positive regulation of protein ser/thr kinase activity (AKT, via
  the CK2–PTEN–mTORC2 cascade in injected mice).
- MARK_AS_OVER_ANNOTATED ×3: GO:0001649, GO:0033687, GO:0048630.
- REMOVE ×1: GO:0005515 protein binding.
- NEW ×3: GO:0061844, GO:0050829, GO:0050830.
