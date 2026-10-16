# NSUN7 (Q8NE18) — review notes

## Summary of the position taken

NSUN7 is the **pseudoenzyme** of the NSUN (NOL1/NOP2/Sun) m5C RNA methyltransferase family.
It retains the canonical NSUN fold and the sequence motifs that the family uses for catalysis,
but it has lost the key SAM-contacting aspartate of motif IV, does not bind SAM, and its loss
does not change RNA m5C levels in the tissue where it is actually expressed. Its demonstrable
biochemical activity is **RNA (chiefly mRNA) binding**, and its physiological role is
post-transcriptional regulation in elongated spermatids supporting sperm flagellum assembly
and progressive motility.

Consequently the only molecular-function annotation GOA carries — `GO:0008168 methyltransferase
activity`, IEA from InterPro `IPR001678` — is argued down (`REMOVE`). This is exactly the case
CLAUDE.md permits: an electronic, family-signature-derived inference that direct biochemistry
on the protein itself contradicts. UniProt itself has already added a CAUTION to the same effect
(see below).

## Catalytic inactivity — the direct evidence

Li et al. 2025 (Nat Commun) is the decisive study. They measured SAM binding by ITC on purified
protein and measured m5C transcriptome-wide in knockout testis:

- [PMID:41381527 "Intriguingly, we found that the NSUN domain of mouse NSUN7 does not bind SAM at all"]
- [PMID:41381527 "Consistent with the result of mouse NSUN7, the NSUN domain of human NSUN7 also failed to bind SAM"] — so this is not a mouse-specific quirk.
- [PMID:41381527 "sequence variations in motif IV and the critical SAM-binding residue change from Asp to Leu render it incapable of SAM binding and consequently inactive for RNA m5C methylation"]
- [PMID:41381527 "Through transcriptome-wide m5C mass spectrometry and ultrafast bisulfite sequencing, we found that Nsun7 knockout has no impact on RNA m5C modification."]

Independent genetic corroboration from a different laboratory, using a catalytic-site point
mutant rather than a null: Guseva et al. 2025 (Biochimie) knocked in the putative catalytic
cysteine substitution C382A and saw **no phenotype at all**:

- [PMID:40545153 "Contrary to predictions based on the typical reaction mechanism of NOP2/Sun family methyltransferases, Nsun7C382A mice did not exhibit any phenotypical characteristics of knockouts and had normal fertility, sperm motility, and longitudinal column positioning, similar to wild-type mice."]
- [PMID:40545153 "These findings allow us to assume that NSUN7 may have an essential function in the spermatogenesis of mice independent on its methyltransferase activity."]

This is a strong design: if the phenotype were caused by loss of methyl transfer, a catalytic
mutant should phenocopy the null. It does not. The same paper reports structural modelling
showing a re-arranged catalytic site with an abnormally long motif IV–motif VI cysteine distance.

UniProt has already acted on this (`genes/human/NSUN7/NSUN7-uniprot.txt`):

> CAUTION: In contrast to other NSUN family members, NSUN7 lacks RNA cytosine C5-methyltransferase
> activity, due to sequence variations in S-adenosyl-L-methionine(SAM)-binding residues.
> Substitution of the conserved SAM-binding Asp-373 with Leu-373 abolishes SAM binding and likely
> renders the enzyme catalytically inactive.

The UniProt keyword list also already carries `RNA-binding` but no `Methyltransferase`/`Transferase`
keyword. The stale piece is the InterPro2GO mapping (`IPR001678` → `GO:0008168`), which fires on
the fold, not on the catalytic residues.

## What NSUN7 actually does

Guseva et al. 2025 (RNA) did UV CLIP-seq from testis and RNA-seq of the knockout:

- [PMID:40032361 "We identified m5C-specific NSUN7 RNA methyltransferase as a protein present in elongated spermatids and interacting with RNAs specific for this type of spermatozoid's precursor cells."]
- [PMID:40032361 "The CLIP-seq experiment performed on testes extract allowed us to identify multiple NSUN7 binding RNAs. The majority of those belong to mRNAs, although several noncoding RNAs have also been identified."]
- [PMID:40032361 "Inactivation of the Nsun7 gene in mice leads to upregulation of its RNA interactors, thus indicating that NSUN7 downregulates a set of RNAs in the elongated spermatids."]

Notably, the same paper's own bisulfite sequencing failed to find NSUN7-dependent methylation
that tracked with binding:

- [PMID:40032361 "However, differential methylation sites demonstrated little correlation with NSUN7 binding sites revealed by CLIP-seq and have little statistical support due to the low coverage of sites demonstrating differences in methylation between the WT and Nsun7i2/i2 mice."]

Li et al. independently observed RNA-dependence of NSUN7 protein stability:

- [PMID:41381527 "Our results show that RNase treatment has an impact on NSUN7 protein stability, further indicating that the association of NSUN7 with RNA contributes to maintaining its protein stability."]
- [PMID:41381527 "During the preparation of this manuscript, a study reported that NSUN7 binds to specific mRNAs, suggesting NSUN7 possesses RNA-binding capability"]

So **mRNA binding (GO:0003729)** is the informative molecular function to put in its place —
and it is exactly the sort of replacement CLAUDE.md asks for when removing an uninformative or
wrong MF term.

### An unresolved conflict in the *direction* of the effect

The two groups disagree about the sign of NSUN7's post-transcriptional effect:

- Guseva et al.: knockout **up**regulates NSUN7-bound transcripts → NSUN7 destabilises them.
- Li et al.: knockout **down**regulates cilium-organisation mRNAs — [PMID:41381527 "Single-cell RNA sequencing shows that Nsun7 knockout decreases the levels of a cohort of mRNAs related to cilium organization in elongated spermatids."]

Li et al. are explicit that they cannot separate cause from effect, since the knockout also has
gross structural defects that could secondarily perturb mRNA storage and stability. For this
reason I have **not** asserted `GO:0061157 mRNA destabilization` (or an mRNA-stabilisation term)
in `core_functions`; only the binding activity and the flagellar assembly process, both of which
both groups agree on. The direction is recorded as a `suggested_question`.

A third study (proteomics of sorted spermatid populations) favours a protein-complex-stabilising
model rather than an RNA-turnover model:

- [PMID:41516134 "Our findings support a model in which NSUN7 primarily stabilizes protein complexes and coordinates flagellar assembly."]
- [PMID:41516134 "We showed that NSUN7 is present at all stages of spermiogenesis and is most abundant in round spermatids"]

## Localisation and phenotype (basis of the ISS annotations)

The human ISS annotations are transferred from mouse Nsun7 (UniProtKB:Q14AW5) and are well grounded:

- [PMID:41381527 "Thus, our results showed that NSUN7 is predominantly enriched in adult mouse testis, with specific localization to the flagella of elongated spermatids"]
- [PMID:41381527 "Nsun7 deficiency impairs sperm progressive motility, accompanied by defects in axonemes and mispositioning of longitudinal columns."]
- [PMID:40032361 "A physiologic consequence of Nsun7 gene knockout is male infertility, which is mechanistically explained by the observed mispositioning of longitudinal columns relative to the axonemal microtubular doublets leading to a motility defect."]

The original ENU forward-genetic identification:

- [PMID:17442852 "Positional cloning of Ste5Jcs1 led to the identification of a mutation in a novel gene called Nsun7, which encodes a protein with a Sun domain that is homologous to tRNA and rRNA cytosine methyltransferases."]
- [PMID:17442852 "Mutant sperm exhibited depressed progressive motility associated with a rigid flagellar midpiece (but not principal piece) segment"]

Human genetic association with asthenozoospermia:

- [PMID:24384068 "Direct sequencing of polymerase chain reaction (PCR) products, along with their analysis, confirmed C26232T-transition and T26248G-transversion mutations in asthenospermic men."]

## Weighing the counter-claims that NSUN7 deposits m5C

Three recent disease papers assert NSUN7-catalysed m5C. All three are **knockdown/knockout plus
MeRIP-or-bisulfite correlation** studies: none of them tests catalysis directly (no SAM binding,
no purified-enzyme in vitro methylation, no catalytic-dead rescue).

- PNAS 2026, kidney injury — [PMID:41871257 "Both global and kidney-specific deletion of Nsun7 in mice reduced m5C abundance, attenuated inflammatory responses, and decreased macrophage infiltration"]. Abstract-only in our cache. A reduction in bulk m5C after deleting a protein is equally consistent with an indirect effect (e.g. via expression or stability of a genuine NSUN enzyme, or via the inflammatory state itself), and the study does not distinguish these.
- Sci Rep 2025, PCOS granulosa cells — [PMID:41062800 "Moreover, NSUN7 knockdown inhibited m5C methylation of NLRP3 and reduced NLRP3 mRNA stability."]
- J Transl Med 2025, glioblastoma — [PMID:41275291 "NSUN7 catalyzes m5C modification of circNTRK2."] The word "catalyzes" is used of a knockdown-plus-MeRIP result.

A further tissue-expression problem: NSUN7 is strongly testis-restricted
([PMID:41381527 "Thus, our results showed that NSUN7 is predominantly enriched in adult mouse testis, with specific localization to the flagella of elongated spermatids"]),
yet these studies place it as a dominant m5C writer in kidney, ovary and brain tumours.

**Weighting.** Evidence that directly interrogates the catalytic mechanism (ITC SAM binding on
purified protein; a catalytic-residue knock-in mouse with no phenotype; transcriptome-wide m5C
mass spectrometry in the knockout) beats evidence that assumes catalysis and measures a
downstream correlate. The three positive claims are therefore recorded but do not rescue
`GO:0008168`.

## Annotation decisions

| Term | Evidence | Action | Why |
|---|---|---|---|
| GO:0008168 methyltransferase activity | IEA (InterPro IPR001678) | REMOVE | No SAM binding (ITC, mouse and human); catalytic-site mutant mouse is normal; KO does not change m5C; UniProt CAUTION agrees. Electronic fold-based inference, contradicted by direct biochemistry. |
| GO:0031514 motile cilium | IEA | ACCEPT | Sperm flagellum is a motile cilium; the more specific GO:0036126 is also present. |
| GO:0036126 sperm flagellum | ISS | ACCEPT | Core location. |
| GO:0005737 cytoplasm (x2) | IEA, ISS | ACCEPT | Correct, if general. |
| GO:0030317 flagellated sperm motility | ISS | ACCEPT | Core process. |
| GO:0120316 sperm flagellum assembly | ISS | ACCEPT | Core process. |

New MF proposed in `core_functions`: `GO:0003729 mRNA binding`.

## Reusable principle applied here

*A family signature is not a catalytic assay.* Where an IEA molecular function comes from a
domain/family signature (InterPro2GO, PANTHER family) and direct experiment on the protein shows
the catalytic requirements are not met — cofactor not bound, catalytic residue substituted, no
change in product on loss of function — the IEA should be removed and replaced by whatever the
protein is actually shown to do. Do not leave the catalytic term in place merely because the
protein belongs to an enzyme family.
