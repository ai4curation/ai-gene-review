# STING1 (TMEM173) review journal

Reviewer: AI review, 2026-09-17. UniProt Q86WV6, HGNC:27962 (STING1; TMEM173 retired).
250 GOA rows / 64 distinct GO terms. Strategy: one decision per GO term, applied to all rows
of that term (project rule: same term -> same action regardless of evidence code).

## 1. Settled baseline (uncontested)

STING1 is a four-transmembrane ER membrane protein with a cytosolic ligand-binding /
signalling domain. It is the receptor for cGAS-derived 2'3'-cGAMP and for bacterial cyclic
dinucleotides; ligand binding drives high-order oligomerisation, COPII-dependent ER exit to the
ERGIC/Golgi, TBK1 recruitment and phosphorylation of the STING C-terminal tail, IRF3 docking,
and type I IFN plus NF-kB transcriptional output.

- Direct CDN sensing: [PMID:21947006 "We demonstrate that STING binds directly to radiolabelled
  cyclic diguanylate monophosphate (c-di-GMP), and we show that unlabelled cyclic dinucleotides,
  but not other nucleotides or nucleic acids, compete with c-di-GMP for binding to STING."]
- High-affinity endogenous ligand: [PMID:23747010 "This molecule, termed 2'3'-cGAMP, is unique in
  that it binds to the adaptor protein STING with a much greater affinity than cGAMP molecules
  containing other combinations of phosphodiester linkages."]
- Adaptor mechanism: [PMID:25636800 "Phosphorylated MAVS and STING then bind to a positively
  charged surface of interferon regulatory factor 3 (IRF3) and thereby recruit IRF3 for its
  phosphorylation and activation by TBK1."]
- Oligomerisation mechanism: [PMID:30842659 "This rotation is coupled to a conformational change
  in a loop on the side of the ligand-binding-domain dimer, which leads to the formation of the
  STING tetramer and higher-order oligomers through side-by-side packing."]
- TBK1/IFN-independent autophagy: [PMID:30842662 "Here we report that STING also activates
  autophagy through a mechanism that is independent of TBK1 activation and interferon induction."]

## 2. The contested/new question: is there a genuine phosphoinositide-binding MF?

**Answer: yes, and GOA already carries it.** `GO:0080025 phosphatidylinositol-3,5-bisphosphate
binding` is already present as IDA from both 2026 Nature papers, so this is not a term I had to
introduce. What I added as NEW is `GO:0005546 phosphatidylinositol-4,5-bisphosphate binding`,
which the companion structural paper establishes with the same rigour but which GOA has not
captured.

Evidence, paper by paper:

- Tan et al. 2026 Nature [PMID:41639454 "Proteomic analyses identified a constitutive interaction
  between STING and PIKFYVE, an enzyme that produces PtdIns(3,5)P2 in mammalian cells. Deletion of
  PIKFYVE blocked STING trafficking from the ER and TBK1 activation."] and
  [PMID:41639454 "These results indicate that STING directly binds to PtdIns(3,5)P2."]
  Direct binding is by FRET with BODIPY TMR-PtdIns(3,5)P2 against full-length STING-mEGFP; the
  isolated C-terminal fragment does not bind, i.e. the TMD is required
  [PMID:41639454 "A purified C-terminal fragment (CT) of STING showed no phosphoinositide binding
  in PIP strips assays (Extended Data Fig. 6a), suggesting potential requirement of its
  transmembrane domain (TMD) in lipid binding."]
- Li et al. 2026 Nature (companion) [PMID:41639452 "Here we demonstrate that cGAMP-induced
  high-order oligomerization of STING is enhanced strongly by phosphatidylinositol
  3,5-bisphosphate (PtdIns(3,5)P2 and PtdIns(4,5)P2, and by PtdIns4P to a lesser extent."] with
  cryo-EM: [PMID:41639452 "Our cryo-electron microscopy structures reveal that PtdInsPs together
  with cholesterol bind at the interface between STING dimers, directly promoting the high-order
  oligomerization."]
- PI(4,5)P2 specifically: [PMID:41639452 "Our lipid binding, native PAGE and cryo-EM studies
  together indicate that both PI(3,5)P2 and PI(4,5)P2 are able to strongly bind STING and
  effectively induce high-order STING oligomerization."]
- Cholesterol at the same interface: [PMID:41639452 "Our results show that STING wild type (WT)
  binds to most PIP lipids, cholesterol and its derivatives, but not several other types of lipids
  such as non-phosphorylated phosphatidylinositol (PI), phosphatidylethanolamine (PE) and
  phosphatidylserine (PS)."]

### How much weight should companion papers from one group carry?

These are **co-submitted companion papers with overlapping authorship** (Tan JX, Chen ZJ and Bai XC
appear on both; the cryo-EM structure quoted in the Tan paper *is* the Li paper). Tan et al. say so
explicitly: [PMID:41639454 "To understand how PtdIns(3,5)P2 binds to STING, we solved the cryo-EM
structure of full length human STING in complex with PtdIns(3,5)P2 (Li et al., co-submitted)."]
So the two papers are **corroboration within one research programme, not independent replication**.
No second laboratory has yet reproduced the direct lipid binding.

Three considerations nevertheless argue for accepting the MF rather than holding it as UNDECIDED:

1. **The evidence is multi-modal within the programme, not a single assay.** Direct binding (FRET;
   lipid strips), structure (cryo-EM density at a defined dimer-dimer groove), structure-guided
   loss-of-function (K20E/R71H abolish PIP binding; S80I reduces cholesterol binding), in vitro
   liposome reconstitution, and cell-based phenotypes (trafficking and pS366/pTBK1/pIRF3 loss,
   PIKFYVE deletion phenocopy). A single artefact does not explain all of these.
2. **It converges on pre-existing, independent human genetics.** R71 is part of the common HAQ
   allele: [PMID:41639452 "It is worth mentioning that R71H is a part of the STING HAQ
   (R71H-G230A-R293Q) variant, which is one of the prevalent human STING alleles with impaired
   immune functions40,41. Our cryo-EM results show that R71 forms a salt bridge with the
   5-phosphate group of PI(3,5)P2 or PI(4,5)P2, which provides a structural explanation for its
   critical role in STING activation."] The hypofunction of HAQ was known long before and from
   other groups; the lipid site explains it.
3. **A lipid role in STING activation was already reported independently.** The authors frame their
   work as mechanism for prior observations: [PMID:41639452 "Indeed, several lines of evidence
   suggest that STING may directly interact with and be modulated by phosphatidylinositol
   phosphates (PIPs) and cholesterol, which exhibit different distributions in the ER, Golgi and
   endosomes12-16,28-30."] and [PMID:41639452 "Our cryo-EM structures suggest that PIPs and
   cholesterol in an inter-dependent manner strengthen the dimer-dimer interaction in the STING
   oligomer, supporting previous studies that cholesterol plays a role in STING activation and
   regulation13-16."]

Two independent commentaries treat the finding as established rather than contested:
[PMID:41997109 "Tan et al.1 and Li et al.2 identify PtdIns(3,5)P₂ and cholesterol as key lipids
that stabilize STING oligomers and enable TBK1 activation, explaining why STING must traffic from
the ER to the Golgi to initiate immune signaling."] and [PMID:41997116 "In two articles recently
published in Nature, Li et al.1 and Tan et al.2 show that phosphoinositides and cholesterol
cooperate to support canonical and non-canonical STING functions by potentiating agonist-dependent
activation through oligomerization and trafficking."] Commentaries are not replication either, but
they establish that the field has not raised a methodological objection.

**Caveat I am recording rather than resolving:** PtdIns(4,5)P2 binds the same groove with similar
potency in vitro, yet it is a plasma-membrane-enriched lipid and activated STING does not traffic
to the plasma membrane. The authors themselves flag this: [PMID:41639452 "PI(4,5)P2 is enriched in
the plasma membrane, but also present in the Golgi and endosomes at much lower levels35,37.
PI(3,5)P2 is mostly localized to late endosomes and lysosomes35. Upon cGAMP binding, STING traffics
to Golgi and Golgi-derived endosomes, but not plasma membrane."] So GO:0005546 is a well-supported
*binding* capability whose physiological occupancy is not established; I annotate the binding and
say so in the reason rather than inflating it into a process claim.

**Term choice.** I used the two specific terms that match the two lipids actually assayed
(GO:0080025, GO:0005546) rather than the parent GO:1902936 `phosphatidylinositol bisphosphate
binding`, because both specific species were tested individually and separately structurally
resolved. GO:1902936 remains the right fallback if a curator prefers one annotation over two.
PtdIns4P was explicitly the weak/likely-indirect case and I did NOT annotate it:
[PMID:41639452 "It is possible that this effect of PI(4)P is indirect, as changes in the
concentration of PI(4)P could affect other PIP species such as PI(4,5)P2 and PI(3,5)P2."]

### Publisher Correction PMID:41721038 — what I could and could not establish

PMID:41721038 is `Publisher Correction: PtdIns(3,5)P(2) is an endogenous ligand of STING in innate
immune signalling`, Nature 2026 Mar;651(8105):E11, doi 10.1038/s41586-026-10280-6, erratum for
PMID:41639454. **I could not retrieve what it corrected.** PubMed carries only the erratum notice
with no descriptive text; Europe PMC returns no abstract for it; the Nature page is behind an
authentication redirect and the aggregator copies reproduce only the title. The only substantive
thing I can say without guessing is categorical: Springer Nature reserves "Publisher Correction"
for errors *introduced in production by the publisher* (as opposed to "Author Correction" for
author-introduced errors and "Retraction" for invalidating problems), so on its face it is not a
correction to the data or conclusions. I have deliberately NOT inferred what was changed, and the
annotations do not lean on the correction either way.

## 3. Proton channel activity (GO:0015252) — scrutinised, and it holds

This is a genuinely non-obvious assignment for an ER adaptor, so I checked what it rests on. It is
**not** a single-lab claim, unlike the lipid finding:

- Origin, Hacohen lab (Broad/MIT): [PMID:37535724 "On the basis of structural analysis, we
  hypothesized that human STING is a proton channel. Indeed, we found that STING activation induced
  a pH increase in the Golgi and that STING reconstituted in liposomes enabled transmembrane proton
  transport."] Reconstitution into liposomes is the key point: proton flux is a property of the
  purified protein, not an indirect cellular readout. Specificity comes from C53, which binds the
  putative channel interface and blocks flux.
- Tan lab (Pittsburgh), independent: [PMID:39423796 "STING-mediated TFEB activation is independent
  of TBK1, but it requires STING trafficking and its conserved proton channel."]
- Miner lab (Penn/WashU), independent: [PMID:39947179 "Recent discoveries revealed that STING also
  functions as a proton channel that deacidifies the Golgi apparatus."] — and that paper's whole
  design is the identification of ArfGAP2 as a regulator of the channel.
- Nan Yan lab (UTSW), independent, in lysosomal storage disease models (PMID:40185098, Mol Cell
  2025): STING-TFEB lysosomal quality control "requires STING's proton channel function".
- The channel interface has become a *drug* site: a first-in-class allosteric agonist series binds
  "within a hydrophobic transmembrane proton channel formed by intertwined helices of two STING
  monomers" (PMID:42336656, J Immunother Cancer 2026).

I searched PubMed for a refutation and found none. Four labs and a medicinal-chemistry programme
converge; GO:0015252 is accepted and treated as a **second core molecular function**, distinct from
the adaptor activity and responsible for a separable output branch (LC3B/GABARAP lipidation,
inflammasome, TFEB-driven lysosome biogenesis). Note the contrast with the *other* gene in this
batch, TMEM175, where the proton-channel claim is genuinely contested; for STING1 it is not.

## 4. Transcription coactivator activity (GO:0003713) — the one MF I demoted

`GO:0003713 transcription coactivator activity` (IDA, PMID:18818105, Zhong et al. 2008 Immunity,
the MITA paper) is wrong for a four-pass ER membrane protein. GO defines a transcription
coactivator as a coregulator that acts on a DNA-bound transcription factor at the promoter; STING
never enters the nucleus. The underlying observation is real and is an IDA I have no grounds to
delete — MITA overexpression activates IFN-beta reporters and MITA binds IRF3
[PMID:18818105 "MITA also interacted with IRF3 and recruited the kinase TBK1 to the VISA-associated
complex."] — but that is adaptor/scaffold behaviour. Action: **MODIFY** to `GO:0035591 signaling
adaptor activity`, which GOA already carries from six other papers. Same reasoning demotes
`GO:0045944 positive regulation of transcription by RNA polymerase II` (same paper) to
`GO:0032481 positive regulation of type I interferon production`.

The related `GO:0061629 RNA polymerase II-specific DNA-binding transcription factor binding` (IPI,
same paper) is *not* wrong — IRF3 is exactly such a factor — so it is kept, as non-core.

## 5. Mitochondrial outer membrane (GO:0005741) — over-annotation, not removal

Six rows, four of them EXP (PMID:18724357, PMID:19285439, PMID:19433799, PMID:19776740) and one IDA
(PMID:18818105); UniProt still lists "Mitochondrion outer membrane" with four ECO:0000269 refs. All
date from 2008-2009. The modern consensus, including the same UniProt entry's own FUNCTION block
and every structural/trafficking paper since, is that STING is an ER membrane protein that exits to
ERGIC/Golgi. Project rules forbid REMOVE on experimental annotations whose full text I have not
read, and mitochondria-associated ER membrane (MAM) contact sites plausibly explain a genuine
mitochondrial-fraction signal in the original work. Action: **MARK_AS_OVER_ANNOTATED** on all six.

## 6. Other locations

- `GO:0005777 peroxisome` is the one CC I removed. It is IEA only, by Ensembl Compara transfer from
  mouse (`GO_REF:0000107`, WITH `UniProtKB:Q3TBT3|ensembl:ENSMUSP00000111393`). Human UniProt's
  SUBCELLULAR LOCATION block lists ERGIC, ER, perinuclear cytoplasm, Golgi, TGN, autophagosome,
  endosome, lysosome, mitochondrion outer membrane and cell membrane — no peroxisome. Nothing in
  the STING literature places it there. This is exactly the "demonstrably wrong electronic
  inference" case REMOVE is for.
- `GO:0005886 plasma membrane` is ISS/IEA/TAS only and traces to `ECO:0000250|UniProtKB:Q3TBT3`
  (by similarity from mouse) in UniProt — no human experimental support, and the lipid paper above
  states positively that activated STING does not traffic to the plasma membrane.
  MARK_AS_OVER_ANNOTATED, as are `GO:0030667 secretory granule membrane` (a single generic Reactome
  neutrophil-degranulation TAS) and `GO:0005829 cytosol` (STING is polytopic; only its C-terminal
  domain faces the cytosol).
- Generic parents were modified to the specific compartment already supported: `GO:0005737
  cytoplasm` and `GO:0005783 endoplasmic reticulum` -> `GO:0005789`; `GO:0005794 Golgi apparatus`
  -> `GO:0000139`; `GO:0005768 endosome` -> `GO:0010008`; the ten Reactome `GO:0030659 cytoplasmic
  vesicle membrane` rows -> `GO:0033116` ERGIC membrane.

## 7. IBA handling

Eleven terms carry an IBA row (GO:0000045, GO:0002218, GO:0005776, GO:0005789, GO:0016239,
GO:0032481, GO:0035438, GO:0045087, GO:0051607, GO:0061507, GO:0061709). All are biologically
defensible for human STING1 and I did not inspect the PANTHER tree (PTN005046674) beyond the
WITH/FROM lists, so all are ACCEPTed rather than downgraded — downgrading would require
`propagation_review` metadata I would have to invent. The one I am least comfortable with is
`GO:0061709 reticulophagy`; UniProt supports it only "By similarity" (c-di-GMP-triggered
reticulophagy), so the reason records that it is the weakest member of the autophagy cluster.

## 8. Review-based NAS annotations (PMID:40861013)

Four terms come as NAS from one 2025 review, "Beyond interferons: Non-canonical roles of
MITA/STING" [PMID:40861013 "These non-canonical roles of MITA are increasingly recognized for their
involvement in critical processes such as antiviral activity, senescence, autophagy, metabolism,
lysosomal biogenesis, and the development of neurological disorders."]. `GO:0006914 autophagy` is
redundant with the better-supported `GO:0016239` and was modified to it; `GO:0090398 cellular
senescence` is well grounded elsewhere in the literature and is kept as non-core;
`GO:0045820 negative regulation of glycolysis` and `GO:0055088 lipid homeostasis` are downstream
metabolic consequences asserted only in review prose and are marked as over-annotation.

## 9. Validation

`uv run --no-dev ai-gene-review validate --verbose --terms genes/human/STING1/STING1-ai-review.yaml`
prints `✓ Valid` (no warnings). 251 annotations over 65 terms: 165 ACCEPT, 40
MARK_AS_OVER_ANNOTATED, 31 MODIFY, 13 KEEP_AS_NON_CORE, 1 REMOVE (GO:0005777 peroxisome),
1 NEW (GO:0005546 PtdIns(4,5)P2 binding). No GO term carries two different actions.

## 10. Core vs non-core, as decided

**Core**: cGAMP/CDN binding (GO:0061507, GO:0035438) -> signaling adaptor activity (GO:0035591)
at ER/ERGIC/Golgi membranes, driving GO:0140896, GO:0032481 and GO:0043123; and proton channel
activity (GO:0015252) driving the non-canonical autophagy/lysosome branch. Lipid binding
(GO:0080025, GO:0005546, GO:0015485) is recorded as a core-adjacent activation requirement — it is
a genuine MF of the protein but it gates the adaptor function rather than constituting a third
output.

**Non-core**: senescence, TORC1 regulation, lysosome organization, cytokine production in general,
dsRNA responses, ubiquitin-ligase binding, IRF3 (TF) binding, self-oligomerization as a BP.
