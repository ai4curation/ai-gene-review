# TFAP2A (AP-2alpha, P05549) review notes

## 2026-10-05 — initial review (claude-code)

### Identity and molecular activity

- AP-2alpha is a sequence-specific transcription factor of the AP-2 family. It binds GCC(N3)GGC sites as a homo- or
  heterodimer formed through a C-terminal helix-span-helix (HSH) domain that sits next to a basic DNA-binding region.
  [PMID:1998122 "AP-2 required a dimerization domain and an adjacent region of net basic charge to achieve a sequence-specific protein:DNA interaction."]
  [PMID:7555706 "consensus to the sequence G/CCCN3GGC"]
- It acts mainly as an activator. Examples: IGFBP5 [PMID:7559606 "Cotransfection with AP-2 significantly elevated IGFBP-5 promoter activity."],
  CDKN1A/p21 [PMID:21084835 "Maximal expression of CDKN1A requires TFAP2A which binds to two regions of the promoter"],
  and FXN [PMID:20808827 "We found that the transcription factors SRF and TFAP2 bind directly to FXN promoter sequences."].
  It needs the CITED2 and p300/CBP coactivators for this
  [PMID:12586840 "interactions among TFAP2A, CITED2, and p300/CBP are necessary for TFAP2A-mediated transcriptional activation"].
- It also represses some promoters, and repression depends on DNA binding. Examples: Mn-SOD
  [PMID:11278550 "Repression of Mn-SOD by AP-2 was dependent on DNA binding"], C/EBPalpha in preadipocytes
  [PMID:9520389 "in preadipocytes the C/EBPalpha gene is repressed by AP-2alpha/CUP"], and c-myc
  [PMID:20066163 "Chromatin immunoprecipitation assays demonstrated that AP-2 proteins bound to a cluster of AP-2 binding sites"].
  The corepressor NPM1 is recruited [PMID:17318229 "unveils a hitherto unrecognized transcriptional corepressor function of the NPM protein"],
  and KCTD1 and KCTD15 inhibit the activation domain [PMID:19115315 "KCTD1 specifically acts as a negative regulator of AP-2alpha"],
  [PMID:23382213 "Kctd15 binds specifically to the activation domain of AP-2α"].
- MF conclusion: the core terms are GO:0001228, plus context-dependent GO:0001227, GO:0000978/0000977 cis-regulatory
  binding, and GO:0042803 homodimerization (via the HSH domain). The "pioneer" chromatin-opening activity comes from chick work
  [PMID:31848212 "Consistent with the pioneer function of TFAP2A, regions occupied by the transcription factor showed enriched chromatin accessibility and H3K27ac signal"].
  GO has no pioneer-factor MF term. The ISS `chromatin binding` row is the closest existing term.

### Network layer: border specifier AND crest specifier (reiterative)

- Expression. AP-2 is expressed in non-neural ectoderm and the neural plate border at gastrula stages, then in premigratory
  and migratory crest. Mouse: [PMID:1989904 "The principle part of this expression occurs in neural crest cells and their major derivatives"].
  Chick: [PMID:31848212 "During gastrulation (Hamburger and Hamilton stage [HH] 5), TFAP2A expression was detected in the neural plate border region and the nonneural ectoderm"].
  Frog: AP2a is the earliest border gene [PMID:21169220 "As the earliest known NB specifier, AP2a mediates Wnt signals to initiate the NB and activate pax3"].
- Gain of function (frog). It is sufficient to induce crest genes ectopically
  [PMID:12511599 "Ectopic expression of AP2alpha is sufficient to activate high-level expression of NC-specific genes such as Slug and Sox9"],
  and to set up a border-like pattern in neuralized ectoderm
  [PMID:21169220 "AP2a initiates NB patterning and is sufficient to elicit a NB-like pattern in neuralized ectoderm"].
- Loss of function. Frog morphants lose the crest territory
  [PMID:12511599 "Loss-of-function experiments with antisense AP2alpha morpholino oligonucleotides result in severe reduction in the NC territory."].
  Zebrafish lockjaw disrupts specification [PMID:14534133 "neural crest specification and migration are disrupted in low mutant embryos"].
  The mont blanc allele does not [PMID:14985255 "Neural crest induction and specification are not hindered in mob(m610) mutant embryos"].
  This difference is explained by redundancy with tfap2c
  [PMID:17258188 "simultaneous inhibition of tfap2a and tfap2c utterly prevents neural crest induction, supporting a conserved role for Tfap2-type activity in neural crest induction"].
  In mouse, crest induction is normal in nulls [PMID:17258188 "neural crest induction occurs normally in zebrafish tfap2a and mouse Tcfap2a mutant embryos"],
  but crest-derived structures fail [PMID:8622766 "the AP-2 knockout mice exhibit anencephaly, craniofacial defects and thoraco-abdominoschisis"],
  and crest-specific deletion confirms a cell-autonomous crest role
  [PMID:14975722 "Neural crest-specific disruption of tcfap2a results in frequent perinatal lethality associated with neural tube closure defects and cleft secondary palate."].
- Direct targets and partner switch (chick). TFAP2A/C heterodimers activate the border program, and TFAP2A/B heterodimers activate the specification program
  [PMID:31848212 "According to this model, TFAP2A/C heterodimers mediate neural plate border induction, whereas TFAP2A/B heterodimers promote neural crest specification."].
- Human. Heterozygous TFAP2A mutations cause branchio-oculo-facial syndrome (BOFS), a neurocristopathy-like disorder
  [PMID:18423521 "We conclude BOFS is caused by mutations involving TFAP2A."],
  [PMID:21204207 "are evidence for BOFS as a neurocristopathy"].
- **Placement.** AP-2alpha is the clearest case in the network of a gene that spans two layers. In frog it acts *first* as a
  border specifier, upstream of pax3, and *again* within the crest as a specifier
  [PMID:21169220 "as a NC specifier, AP2a regulates further NC development independent of and downstream of NB patterning"].
  It is also a non-neural ectoderm/epidermis factor, which is its ancestral deployment (see evolution below).

### Choice of NC process term (project convention)

- Human TFAP2A has **no** NC-branch GO term in GOA at all, so any NC term is NEW.
- Under the pending project convention, GO:0014029 is kept for border-acting genes and GO:0014036 for crest specifiers.
  AP-2alpha does both. GO:0014036 is part_of GO:0014034, which is part_of GO:0014029 (checked via the QuickGO ancestors
  API: GO:0014036 has GO:0014029 as an ancestor). Proposing both would assert an ancestor plus its descendant, which
  CLAUDE.md rejects as redundant. **Decision: one NEW, GO:0014029 neural crest formation.** It covers the border-forming
  step (de Crozé 2011), which GO:0014036 would miss, and the specification step is part_of it. The zebrafish IMP
  GO:0014036 rows support the narrower claim in that species.
  Evidence code is ISS: human TFAP2A has no direct experiment, and frog/chick/zebrafish/mouse data are transferred by
  orthology because human is the proxy here.
- Participation test: AP-2alpha is a DNA-binding TF that directly occupies border and crest enhancers (chick CUT&RUN) and
  is sufficient to induce border and crest genes. It does part of the work; it is not a substrate or a mere requirement.

### Comparator check (QuickGO, recorded 2026-10-05)

Query: QuickGO `annotation/downloadSearch?geneProductId=<all UniProt accessions for tfap2a/b/c/d/e in human 9606,
mouse 10090, rat 10116, zebrafish 7955, X. laevis 8355, X. tropicalis 8364, chicken 9031 (153 accessions from UniProt
REST)>&goId=GO:0014029,GO:0014034,GO:0014036,GO:0014032,GO:0014033,GO:0001755,GO:0014031&goUsage=descendants`.
Result (76 rows):
- Zebrafish tfap2a: GO:0014036 IMP (PMID:14534133), GO:0014036 IGI (PMID:20885782), GO:0014032 IGI (PMID:17258188,
  17724731, 19439494, 19955371, 21963426, 22241841).
- Zebrafish tfap2c: GO:0014036 IGI (PMID:20885782), GO:0014032 IGI (several).
- Mouse Tfap2a (P34056): GO:0014032 IMP (PMID:8622766). Rat Tfap2a: GO:0014032 ISO.
- **Human TFAP2A/B/C, X. laevis and X. tropicalis tfap2a, chicken TFAP2A: none.**

So orthologs in two vertebrate MODs carry NC terms. Absence in human and frog is a coverage gap: the frog border papers
(Luo 2003, de Crozé 2011) were never curated to the unreviewed frog entries. It is not a convention. This is
the same pattern found for myc-a and pax3-a.

### Evolution / outgroups

- Amphioxus has a single AP-2. It is expressed in non-neural ectoderm, not at the border or in the dorsal neural tube.
  Lamprey AP-2 is expressed in crest
  [PMID:12397104 "Isolation and comparison of amphioxus, lamprey and axolotl AP-2 reveals its extensive expansion in the vertebrate dorsal neural tube and pharyngeal arches, implying co-option of AP-2 genes by neural crest cells early in vertebrate evolution."],
  [PMID:12397104 "Expression in non-neural ectoderm is a conserved feature in amphioxus and vertebrates, suggesting an ancient role for AP-2 genes in this tissue."].
- Interpretation: the ectodermal/epidermal role is ancestral (chordate). Crest expression is a vertebrate co-option
  through changed expression, as for Id and SoxE. The family expanded to five paralogs in vertebrates, and the
  border (A/C) versus crest (A/B) heterodimer partner switch fits subfunctionalisation after duplication
  [PMID:17724731 "The Tfap2 family arose from a single ancestral gene in a chordate ancestor that underwent gene duplication to give up to five family members in living vertebrates."].
  So AP-2 is a border gene in vertebrates but *not* a border gene in amphioxus. That is unlike Pax3/7 and Zic, whose border
  expression is ancestral. AP-2 is therefore a candidate for the "new border input" that made the border crest-competent.

### Annotation decisions (summary)

- MF core: GO:0001228 (ACCEPT), GO:0001227 (ACCEPT, context-dependent), cis-regulatory binding rows (ACCEPT).
- protein binding (15 rows): CITED2/EP300 → GO:0001223 transcription coactivator binding (MODIFY). NPM1, KCTD1 →
  GO:0001222 transcription corepressor binding (MODIFY; KCTD1 itself carries GO:0003714 IDA from PMID:19115315).
  UBC9 (x2), HT screens and MAPT → REMOVE as uninformative. **MYO6 (PMID:11447109) → REMOVE.** The cached full text
  describes the clathrin *adaptor protein complex AP-2*, not transcription factor AP-2. This is name confusion that can
  be verified from the full text in hand.
- identical protein binding (PMID:1998122) → MODIFY to GO:0042803 protein homodimerization activity.
- Developmental processes from mouse ISS and BOFS IMP (eye, ear, palate, limb, kidney, skeleton, cranial nerves):
  KEEP_AS_NON_CORE. These are crest- and ectoderm-derived outputs. Embryonic cranial skeleton morphogenesis ACCEPTED
  as the main crest output.
- Over-annotated: sensory perception of sound (BOFS deafness is structural), retina layer formation (IEP),
  cellular response to iron ion (mRNA change only), negative regulation of ROS metabolic process (indirect, via MYC),
  positive regulation of neuron apoptotic process and regulation of cell differentiation (overexpression in
  retinoblastoma lines).

### Open issues

- GO has no neural plate border term. AP-2alpha is the best example of a gene that needs one, because it initiates the border.
- Pioneer factor activity has no GO MF term.
- Epidermis/non-neural ectoderm development is the ancestral role. Human/mouse evidence for TFAP2A alone is confounded by
  TFAP2C redundancy, and no paper establishing it was cached, so it was raised as a question and not added.
