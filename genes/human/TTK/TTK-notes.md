# TTK (Mps1, P33981) — curation notes

Working journal for the human TTK gene review. Append new entries at the end.

## 2026-09-25 — initial full review of the GOA seed (35 annotations)

### Identity check

UniProt P33981 `TTK_HUMAN`, 857 aa, "Dual specificity protein kinase TTK",
EC 2.7.12.1, synonyms MPS1 / MPS1L1. Kinase domain 525–791, active site Asp647,
ATP-binding 531–539 and Lys553. This is unambiguously the human Mps1 checkpoint
kinase, not a receptor tyrosine kinase despite the "TTK" (threonine/tyrosine
kinase) historical name. The deep research report independently confirmed the
identity [file:human/TTK/TTK-deep-research-falcon.md "The requested target is
human **TTK protein kinase**, UniProt **P33981**, also called **MPS1**, **hMPS1**,
or **MPS1L1**."].

### Core biology as synthesised

1. **Apical SAC kinase.** TTK is recruited to unattached kinetochores and
   phosphorylates the KNL1 MELT repeats to create the docking mark for Bub1–Bub3
   [PMID:22660415 "MPS1/Mph1 kinase locating at the unattached kinetochores
   initially creates a mark, which is crucial for SAC activation and chromosome
   bi-orientation. This mechanism seems to be conserved in human cells."]. The
   MELT-phospho → BUB recruitment step is confirmed in human cells in the Ska
   paper's introduction [PMID:28441529 "Bub1 and BubR1 interact with
   Mps1-phosphorylated MELT motifs in KNL1 (CASC5), a large scaffold protein at
   the kinetochore"]. Downstream, BUB1 Thr461 (after CDK1 priming of Ser459) and
   MAD1 Thr716 are TTK substrates that drive MAD1–MAD2 recruitment and CDC20
   capture into the MCC [file:human/TTK/TTK-deep-research-falcon.md
   "It phosphorylates KNL1, BUB1, and MAD1 in sequence, thereby catalyzing
   production of the mitotic checkpoint complex (MCC)."]. UniProt records the
   MAD1L1 phosphorylation and the MAD1L1/MAD2L1 interactions
   (PubMed:29162720, not cached locally).

2. **Attachment sensing via NDC80C.** The mechanism that makes TTK an
   *attachment* sensor rather than a constitutive kinase is competitive binding:
   [PMID:26068854 "Both interactions involved the microtubule-binding surfaces of
   Ndc80C and were directly inhibited in the presence of microtubules."] and
   [PMID:26068854 "Competition between Mps1 and microtubules for Ndc80C binding
   thus constitutes a direct mechanism for the detection of unattached
   kinetochores."]. Consistent with this, [PMID:28441529 "Mps1 cycles between the
   cytoplasm and unattached or mal-oriented kinetochores, but is largely excluded
   from bi-oriented kinetochores"], and activity is highest where it matters
   [PMID:28441529 "While Mps1 was recruited to unattached and tensionless
   kinetochores with similar efficiency, its auto-phosphorylation and
   trans-phosphorylation of substrates were significantly higher at the former"].
   This is what justifies ACCEPTing the GO:0043515 `kinetochore binding`
   Ensembl-transferred row rather than treating it as a low-information
   binding term: the binding event *is* the sensing mechanism.

3. **Error correction.** Two independent routes, at different confidence levels.
   Borealin/CDCA8: [PMID:18243099 "Borealin/DasraB, a member of the complex that
   regulates the Aurora B kinase, is directly phosphorylated by Mps1 on residues
   that are crucial for Aurora B activity and chromosome alignment"] and
   [PMID:18243099 "cells lacking Mps1 kinase activity fail to efficiently align
   chromosomes due to impaired Aurora B function at centromeres, leaving improper
   attachments uncorrected"]. The Ska route is the stronger and later account, and
   it explicitly challenges the generality of the Borealin model: [PMID:28441529
   "However, neither MPS1-null cells nor mitotic cells treated with Mps1
   inhibitors exhibit decreased phosphorylation of canonical Aurora B substrates
   such as histone H3 or CENP-A"], while showing a direct, Aurora-B-independent
   effect [PMID:28441529 "Epistasis experiments reveal that kinetochore-localized
   Mps1 can destabilize microtubule attachments directly, even if Aurora B is
   inhibited."] mediated by SKA3 Ser34 [PMID:28441529 "We also identify the Ska
   complex as a key effector of Mps1 at the kinetochore-microtubule interface, as
   mutations that mimic constitutive phosphorylation destabilized K fibers in
   vivo"], opposed by PP2A-B56.
   → Both IDA rows for GO:0140273 were ACCEPTed; the tension between the two
   papers was recorded in the Borealin row's `reason` rather than used as grounds
   to downgrade either annotation.

4. **Secondary roles.** MCRS1/KIF2A spindle morphology [PMID:30785839 "Mps1 binds
   and phosphorylates MCRS1. This mechanism enables KIF2A localization to the
   minus end of spindle microtubules."], with the site mapped and
   inhibitor-validated [PMID:30785839 "the antibody could detect in vitro
   phosphorylation of wild-type MCRS1 protein after Mps1 kinase assay, but
   recognized the S65A mutant much less efficiently, indicating that S65 is an
   Mps1 site in vitro"]. Interphase nuclear pore pool [PMID:19273613 "Like Tpr,
   Mad1, Mad2, and Mps1 localize at the NPC during interphase in human cells."].
   MPS1-dependent BLM Ser144 phosphorylation in mitosis [PMID:16864798 "BLM is
   associated with the SAC kinase MPS1 and is phosphorylated at S144 in a
   MPS1-dependent manner."] — noted for completeness; there is no GOA row for it,
   and I did not propose one (see "NEW terms considered" below).

### Per-annotation decisions and reasoning

**Kinase activity family (8 rows).** Ser/Thr kinase activity (GO:0004674, ×4:
IBA, 2× IDA, TAS) and serine kinase activity (GO:0106310, ×2: EXP, Rhea IEA) all
ACCEPT — every documented physiological substrate is a Ser/Thr site (Borealin,
KNL1 MELT, BUB1 T461, MAD1 T716, SKA3 S34, MCRS1 S64/S65, autophosphorylation
pT33/pS37 and pT360/pS363 [PMID:28441529 "we generated antibodies against two
separate clusters of Mps1 autophosphorylation sites (pT33/pS37 and pT360/pS363),
as well as the newly identified phosphosites in KNL1 (pS1831/pS1834), Rod
(pT13/pS15), and Ska3 (pS34)"]). GO:0004672 `protein kinase activity`
(InterPro2GO) ACCEPT as a correct broad parent. GO:0004712
`protein serine/threonine/tyrosine kinase activity` (IBA + IEA) ACCEPT — this is
the right level at which to record the family's dual specificity.

**Tyrosine kinase activity (GO:0004713, ×2) → MARK_AS_OVER_ANNOTATED.** The only
evidence is in vitro and marginal: the human kinase domain in E. coli gives
"markedly elevated" phosphoSer/phosphoThr but only "slightly increased"
phosphotyrosine [PMID:1639825], and the TAS row's support is the *yeast* enzyme
[PMID:7737118 "this kinase can phosphorylate serine, threonine and tyrosine
residues"]. No physiological tyrosine substrate is known. The deep research makes
the same point [file:human/TTK/TTK-deep-research-falcon.md "The nomenclature
therefore should not be taken to mean that tyrosine phosphorylation is equally
prominent in its established SAC function."]. This is exactly
MARK_AS_OVER_ANNOTATED territory — not wrong, but a stand-alone tyrosine-kinase
MF invites grouping TTK with real tyrosine kinases, and GO:0004712 already
carries the capability at the appropriate level. Deliberately *not* REMOVE, since
the in vitro activity is real.

**GO:0008284 positive regulation of cell population proliferation (TAS) →
REMOVE.** This is the one substantive REMOVE. The cited paper reports an
*expression* correlation [PMID:1639825 "all rapidly proliferating cell lines
tested expressed TTK mRNA"] — the expected pattern for any mitotic kinase, since
transcript abundance tracks mitotic index. The annotation converts a correlation
into a regulatory function. Applying the participation test from CLAUDE.md: which
entity performs a step of proliferation-promoting signalling? TTK performs no such
step; it restrains anaphase and corrects attachments. The deep research is
independently sceptical of the oncogenic reading: high TTK "often tracks
proliferation and mitotic fraction". Removal does not dispute the expression data.

**GO:0016020 membrane (HDA) → MARK_AS_OVER_ANNOTATED.** One HTP membrane-fraction
detection in YTS cells, where the authors themselves caution [PMID:19946888 "The
remaining species were largely involved in cellular processes and molecular
functions that could be predicted to be transiently associated with membranes."].
TTK has no TM segment, signal peptide or lipid anchor in the UniProt feature
table, and no membrane function is described anywhere. Chose
MARK_AS_OVER_ANNOTATED over REMOVE because the peptide detection itself is not
in doubt — the interpretation as a localization is.

**GO:0005515 protein binding (IPI, TPR) → REMOVE.** Repository policy for bare
GO:0005515: resolve to an informative MF if the evidence supports one, otherwise
REMOVE as uninformative without asserting the interaction is false. Here the
paper's finding is that TPR/Megator acts as a *spatial regulator* delivering Mps1
to kinetochores [PMID:19273613 "Tpr, Mad1, Mad2, and Mps1 coimmunoprecipitate in
mitotic enriched HeLa cell extracts prepared in the presence of nocodazole"] —
that is a property of TPR, not a molecular activity of TTK, so no informative
replacement MF can be justified. The interaction is recorded in UniProt and is
not disputed; the interphase NPC localization it reports is instead used to
support the nucleus row.

**GO:0005819 spindle (TAS) → MODIFY to GO:0000776 kinetochore.** The cited paper
is a locus-mapping and mutation-screening study whose only TTK content is
[PMID:10366450 "We determined the chromosomal localization of it and other
spindle checkpoint genes, including MAD1L1, MAD2, BUB3, TTK (MPS1L1), and
CDC20."] — no localization data at all. The structure TTK acts on is the
kinetochore, so the accurate CC is the term GOA already has by IBA/IEA.

**GO:0007051 spindle organization (TAS) → MODIFY to GO:0007052 mitotic spindle
organization.** Same uninformative reference, but unlike the spindle-localization
row the *process* is genuinely supported by later human work (MCRS1/KIF2A), so
MODIFY to the mitosis-specific descendant rather than REMOVE. GO:0007052 itself
(TAS from the yeast SPB paper) → KEEP_AS_NON_CORE: supported in human cells by
PMID:30785839 but secondary to the checkpoint role.

**GO:0000280 nuclear division (ARBA IEA) → MODIFY.** Correct but at a uselessly
high altitude; proposed the two mitosis-specific descendants GOA already carries.

**Non-core keeps.** GO:0007059 chromosome segregation (IBA) and GO:0098813
nuclear chromosome segregation (ARBA) are accurate outcome-level parents —
KEEP_AS_NON_CORE, with the mechanism captured by GO:0007094/GO:0140273.
GO:0005634 nucleus (IBA) and GO:0005737 cytoplasm (IDA) are real pools but not
sites of characterised function — KEEP_AS_NON_CORE. GO:0042802 identical protein
binding: self-association is genuine (trans-autophosphorylation [PMID:28441529
"thereby enabling ligand-dependent relocalization (Fig. S1) and activation of
Mps1 via trans autophosphorylation"]) but low-information — KEEP_AS_NON_CORE.
GO:0033316 meiotic SAC (IBA from fly + mouse) — KEEP_AS_NON_CORE: sound
phylogenetic inference from characterised metazoan orthologues, no human data.

**GO:0060391 positive regulation of SMAD protein signal transduction (TAS) →
UNDECIDED.** The cited reference is an abstract-only *perspective* piece on
noncanonical Smad roles that does not mention TTK in the cached text
[PMID:19018011 "The number of reports demonstrating the interactions of Smads
with proteins outside of canonical TGF-beta signaling is increasing, although the
functional relevance of these interactions is not known."]. The underlying
primary claim (Mps1 phosphorylation of Smad2/3) is not in the cache and is not
corroborated by the deep research. Per the enum, inability to access the relevant
publication → UNDECIDED, not REMOVE.

### IBA rows — how they were handled

All five IBA rows (GO:0000776, GO:0004674, GO:0004712, GO:0007059, GO:0007094,
GO:0033316) were treated as considered PAINT node placements, not similarity
transfers. Note that TTK's own accession `UniProtKB:P33981` appears in the
WITH/FROM of the GO:0004674, GO:0007059 and GO:0007094 IBA rows. Per CLAUDE.md
this is **correct and expected** — TTK's own experimental annotations are among
the descendant evidences the PAINT curator used to place the IBD — so this was
recorded as a marker of experimental grounding on the target, never flagged as
circular. No `propagation_review` blocks were added: none of the IBA rows has a
propagation defect to classify.

Two nodes are in play: `PTN001122082` (the tighter Mps1/SAC node, cited for
kinetochore, Ser/Thr/Tyr kinase activity, mitotic and meiotic SAC) and
`PTN000540737` (a deeper node including plant AT5G20930, worm, trypanosome and
other kinases, cited for Ser/Thr kinase activity, nucleus and chromosome
segregation). The nucleus IBA comes from the deeper node, which is part of why it
was graded non-core rather than accepted as a site of action.

### NEW terms considered and rejected

- `GO:0007100 mitotic centrosome separation` / centrosome-duplication terms.
  Budding-yeast Mps1 is essential for SPB duplication [PMID:7737118 "The MPS1
  gene has been previously identified by a mutant allele that shows defects in
  spindle pole body (SPB) duplication and cell cycle control."], and the deep
  research notes a centrosomal pool, but also flags the human claim as
  contested/secondary. No cached human primary evidence; not proposed.
- DNA-damage-response terms from the BLM Ser144 work (PMID:16864798). The paper
  shows MPS1-dependent BLM phosphorylation and a checkpoint-maintenance
  phenotype, i.e. the phenotype is mitotic-arrest failure, not DNA repair. TTK
  performs no step of a repair process here; it phosphorylates a helicase. Not
  proposed (participation test fails).
- `GO:0034501 protein localization to kinetochore`. Tempting, since TTK
  recruitment of BUB1/BUB3/MAD1 is well documented and the mph1 review carries
  this term. Not proposed for human TTK because the recruitment is a
  *consequence* of the MELT phosphorylation already captured by GO:0007094, and
  adding it would duplicate the checkpoint-signalling assertion rather than add
  coverage. Flagged here in case a future reviewer wants to argue for it with
  human-specific tethering data.

`proposed_new_terms: []`.

### Core functions chosen

Three, all at the kinetochore:
1. Ser/Thr kinase activity → mitotic SAC signalling (the MELT→BUB→MAD1→MCC cascade).
2. Kinetochore binding (GO:0043515) → mitotic SAC signalling — the NDC80C-competitive
   binding that makes the kinase an attachment sensor. Kept as a separate core
   function because it is a distinct, mechanistically essential activity, not a
   restatement of the catalysis.
3. Ser/Thr kinase activity → repair of mitotic kinetochore microtubule attachment
   defect (SKA3 Ser34, Borealin).

No `in_complex`: TTK is a kinase that acts on kinetochore substrates rather than a
stoichiometric subunit of a named GO complex. MCC (GO:0033597) would be wrong —
TTK catalyses its assembly but is not a component.

### Validation

`just validate human TTK` → Valid, 0 errors, 0 warnings (the initial
"no annotations reference available deep research files" warning was cleared by
adding `file:human/TTK/TTK-deep-research-falcon.md` support to the GO:0007094 IBA
and GO:0004713 IEA rows). Two references not in the GOA seed were added to
`references` because they are cited in `supported_by`: PMID:22660415 (KNL1 MELT)
and PMID:26068854 (NDC80C competition). Every reference carries a
`reference_review`; PMID:19018011 is the only `UNVERIFIED` one.

Status set to `COMPLETE`.
