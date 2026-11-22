# zic1 (Xenopus laevis, O73689) — curation notes

Project: `projects/NEURAL_CREST_ORIGINS.md`, Tier 2 (neural plate border specifiers).
Reviewer: claude-code, 2026-10-05.

## Identity
- O73689 = Zic1 / Opl / Zic-r1, 443 aa, GLI-like C2H2 zinc-finger protein (five C2H2 fingers 221-380; ZOC/ZF-N
  region; C-terminal regulatory region). Xenbase cross-reference in the UniProt record is `zic1.S`
  (XB-GENE-864815); the L homeolog `zic1.L` is unreviewed TrEMBL A0A1L8GAZ5 (443 aa) and carries no experimental
  GO rows. All experimental GO rows sit on O73689, while the reagents (mRNAs, the Sato 2005 morpholino) were
  generic "Zic1" reagents; not "fixed" here by assertion.
- Family: Zic1-5, sister to GLI/Ci within PANTHER PTHR45718. Drosophila ortholog = odd-paired (opa).

## Evidence synthesis (layer placement)

### 1. Expression
- Earliest: a neural (neuroectoderm) gene induced directly by BMP inhibition.
  [PMID:9435279 "Expression of the two genes is first detected widely in the prospective neuroectoderm at the beginning of gastrulation"]
  [PMID:19805078 "Conversely, we found that zic1 can be activated by BMP inhibition in the absence of translation."]
- Then refines to the neural plate border, before crest specifiers:
  [PMID:15843410 "Pax3 and Zic1 are expressed in an overlapping manner in the presumptive neural crest area of the Xenopus gastrula, even prior to the onset of the expression of the early bona fide neural crest marker genes Foxd3 and Slug."]
  [PMID:17409353 "Zic1 is expressed in the anterior region of the embryo, lateral to the neural crest and at the most rostral boundary of the neural plate, prospective region of the PE."]
- Later: dorsal neural tube / roof plate, forebrain-midbrain (UniProt tissue specificity).
  [PMID:9655809 "by neurula, opl expression is restricted to the dorsal neural tube and neural crest"]

### 2. Molecular activity
- Transcriptional activator with a C-terminal regulatory (inhibitory) domain.
  [PMID:9655809 "opl encodes a transcriptional activator, with a carboxy terminal regulatory domain, which when removed increases opl activity."]
- Sequence-specific DNA binding to a conserved snail1 upstream element (EMSA, mutant oligo control).
  [PMID:24360906 "Similarly, we showed that Zic1 binds to snail1 putative oligonucleotide but not to the snail1 oligonucleotide mutated on the putative binding site (Figure 4E and not shown)."]
  Mouse Zic1 binds a GLI-like site [PMID:11053430 "The selected sequence was almost identical to the GLI binding sequence."].
- => MF: `GO:0001228` DNA-binding transcription activator activity, RNA polymerase II-specific (NEW; existing MF rows
  stop at GO:0000981). No frog evidence for repressor activity, so no repressor term.

### 3. Direct targets
- snail1 (CHX-resistant induction + EMSA) [PMID:24360906 "Firstly, the main known neural crest specifiers, snail1, snail2 and twist1, were highly and reproducibly activated either by Pax3 (snail2, twist1) or by Zic1 (snail1) in the presence of cycloheximide."]
- With Pax3: snail1/2, foxd3, twist1, tfap2b [PMID:24360906 "We demonstrated that the neural border specifiers Pax3 and Zic1 are direct upstream regulators of neural crest specifiers Snail1/2, Foxd3, Twist1, and Tfap2b."]
- Independent screen: snail2, foxd3, gbx2, twist, sox8, sox9 [PMID:24360908 "Among the targets identified we found several well-characterized NC-specific genes, including snail2, foxd3, gbx2, twist, sox8 and sox9, which validate our approach."]
- Neural-plate targets: Xfeb [PMID:16871635 "We have identified a new direct downstream target gene of Zic1 that we have named Xfeb."];
  wnt1/4/8b [PMID:16892174 "Zic1 induces expression of several wnt genes, including wnt1, wnt4 and wnt8b."].

### 4. Gain of function
- Pax3 + Zic1 sufficient for full crest (induction through migration and differentiation):
  [PMID:23509273 "Thus, Pax3 and Zic1 cooperate and execute a transcriptional switch sufficient to activate full multipotent neural crest development and differentiation."]
  [PMID:15843410 "Misexpression of both Pax3 and Zic1 together efficiently induces ectopic neural crest differentiation in the ventral ectoderm, whereas overexpression of either one of them only expands the expression of neural crest markers within the dorsolateral ectoderm."]
- Zic1 alone: neural / preplacodal, not crest.
  [PMID:23509273 "when Zic1 alone was activated, only neural tissue was formed"]
  [PMID:17409353 "In these explants, a strong activation of the PE markers Six1 ( Figure 7 A) and Eya1 (data not shown) was observed in response to Zic1GR injection"]
  [PMID:9435279 "Zic-r1 mRNA injection activates the proneural gene Xngnr-1, and initiates neural and neuronal differentiation in isolated animal caps and in vivo."]

### 5. Loss of function
- Zic1 MO: loss of foxd3/slug, rescued by zic1 (Sato 2005; numbers in deep research); co-presence required:
  [PMID:15843410 "Loss-of-function studies in vivo and in the animal cap show that co-presence of Pax3 and Zic1 is essential for the initiation of neural crest differentiation."]
- Zic1 MO: loss of PE (Six1, preplacodal Sox2) and crest Snail2 induction:
  [PMID:17409353 "We also found that Six1 expression (75%; n = 74) and the preplacodal expression domain of Sox2 (89%; n = 59) were strongly inhibited in morpholino-injected embryos ( Figure 7 B)."]
  [PMID:17409353 "Snail2 induction in Noggin+Wnt-injected explants was abolished in the absence of Zic1 function"]
- Zic1+Zic3 jointly required for definitive neural fate:
  [PMID:19805078 "Finally, Zic1 and Zic3 are required together for definitive neural fate acquisition, both in ectopic and endogenous situations."]

### 6. Conservation / outgroups
- Amphioxus: Zic and Pax3/7 mark the neural plate border, but crest specifiers are not expressed there.
  [PMID:18562679 "Ectodermal Zic and Pax3/7 expression marks the neural plate border, and amphioxus SoxB1-a expression labels the entire neural plate."]
  [PMID:18562679 "In comparing the expression of amphioxus homologs of these genes, we found that they were expressed in broad and diverse patterns, but were absent from the amphioxus neural plate border"]
- Interpretation: Zic belongs to the ancestral chordate border (and neural plate) layer. The vertebrate innovation is
  the downstream wiring: a Zic1 site in the snail1 element and Pax3+Zic1 co-activation of snail/foxd3/sox8/twist1.
  Whether that is cis-regulatory (target elements) or protein change is untested (suggested experiment).
- Drosophila opa regulates wingless/engrailed; frog Zic1 -> wnt1 -> en-2 parallels this [PMID:16892174].
- Mouse: Zic1 mutants have cerebellar defects; mammalian crest induction does not rely on Zic1 alone (paralog
  redundancy) — deep research note; not used as evidence for annotations.

## Network-layer decision
Zic1 is a **neural plate border specifier** (Tier 2), not a crest specifier and not a competence factor:
- It is upstream of and directly activates the first-wave crest specifiers (snail1, sox8 via Pax3+Zic1).
- Alone it does not make crest; its output at the border depends on partner level (with Pax3 -> crest; without
  Pax3 -> preplacodal ectoderm). That is the definition of a border specifier.
- It also has an earlier, separate role as a BMP-inhibition-responsive neural plate gene (with Zic3) and later roles
  in dorsal neural tube and midbrain/hindbrain patterning (via Wnt). These are real but non-core relative to the
  project question; neural plate development is kept as core (the neural plate and its border are where all Zic1
  outputs are executed).

## NC-branch term decision (GO:0014029 vs GO:0014034 vs GO:0014036)
- `GO:0014029` neural crest formation = formation of the ectodermal region between neural plate and non-neural
  ectoderm. For a border specifier that is exactly the right level: **ACCEPT all four IMP rows + IEA**.
- `GO:0014034` neural crest cell fate commitment: Pax3+Zic1 are sufficient for full determination and directly
  activate specifiers; Zic1 does the work (DNA-binding activator of snail1). **ACCEPT the three rows** — matches
  pax3-a (parallel review) and foxd3-a.
- **Not** adding `GO:0014036` fate specification: it is part_of GO:0014034 (redundant), and the project convention
  reserves it for the downstream specifiers (sox8/9/10, snai2, twist1) that execute specification.
- `GO:0014033` neural crest cell differentiation (IMP PMID:9655809, gain-of-function marker induction) —
  MODIFY to GO:0014034: Zic1 initiates the program; differentiation is executed by downstream factors.

## Comparator check (QuickGO, 2026-10-05)
Query (experimental + TAS only, exact terms):
`https://www.ebi.ac.uk/QuickGO/services/annotation/downloadSearch?goId=GO:0014029,GO:0014034,GO:0014036,GO:0014033,GO:0014032,GO:0001755&goUsage=exact&evidenceCode=ECO:0000269,ECO:0000304&evidenceCodeUsage=descendants`
(805 rows), filtered for symbols matching zic|pax3|pax7|msx1|msx2|tfap2a|gbx2|hes4|dlx5:
- X. laevis zic1: GO:0014029 x4, GO:0014034 x3, GO:0014033 x1 (this gene).
- X. laevis zic2-a: GO:0014029 x2, GO:0014034 x1; zic3: GO:0014034; zic4: GO:0014029; zic5: GO:0014029.
- Zebrafish zic2a, zic2b: GO:0014032 neural crest cell development (IMP).
- X. laevis pax3-a/-b: GO:0014029, GO:0014034; hes4-a/-b: GO:0014029.
- Zebrafish tfap2a: GO:0014036 (16) and GO:0014032 (32); mouse Tfap2a: GO:0014032; mouse Pax3, Gbx2: GO:0001755.
- Mouse/human Zic1: no experimental NC-branch annotation.
Conclusion: Xenopus border specifiers (Zic family, Pax3, Hes4) are consistently at GO:0014029/GO:0014034 — no
Zic in any species carries GO:0014036. Keeping zic1 at GO:0014029 + GO:0014034 is consistent with the curation
convention for this layer. Only zebrafish tfap2a (a border/competence gene) sits at GO:0014036 — an
inconsistency to note for the TFAP2A review, not a reason to change zic1.

Preplacodal comparator (`GO:0060788` ectodermal placode formation, experimental, exact): zebrafish tfap2a, tfap2c,
gata3, foxi1, fgf8a; X. laevis tbx1-a, ripply3, lsm14a-a. Preplacodal competence/border factors do carry this term,
so a NEW GO:0060788 for Zic1 (necessary and sufficient for PE fate, PMID:17409353, full text) follows convention.
Participation: Zic1 is the transcription factor that activates the PE specifiers six1/eya1 (it does work in the
process). There is no "preplacodal ectoderm" term.

## GO gaps / questions
- No neural plate border formation/specification term (project-level; raise as question). GO:0021998 neural plate
  mediolateral regionalization exists but is only annotated to mouse/rat Bmpr1a; not proposed.
- PMID:9435279 (Mizuseki 1998) is the source of a GO:0014029 IMP row but its abstract only describes neural
  induction; full text not available here — ACCEPT deferring to curator (consistent with GoF neural crest data in
  sibling papers), flagged.

## Other row decisions (summary)
- Cytoplasm (IEA SubCell / ISS from mouse Zic1 P46684): mouse evidence is I-mfa-mediated cytoplasmic retention in
  cultured cells [PMID:15207726 "When Zic1-3 and I-mfa proteins were co-expressed in cultured cells, nuclear import of the Zic proteins was inhibited."];
  KEEP_AS_NON_CORE.
- Positive regulation of protein import into nucleus (ISS from mouse Zic1, PMID:11238441 Gli co-translocation on
  overexpression): MARK_AS_OVER_ANNOTATED — Zic acts as a binding partner that carries Gli, not a regulator of
  import machinery; no frog evidence.
- Positive regulation of Wnt signaling (IGI PMID:16892174): Zic1 transcriptionally induces wnt1/4/8b; KEEP_AS_NON_CORE
  (regionalisation output; mechanism is ligand gene expression).
- CNS development (IBA), D/V neural tube patterning, neurogenesis: KEEP_AS_NON_CORE.
