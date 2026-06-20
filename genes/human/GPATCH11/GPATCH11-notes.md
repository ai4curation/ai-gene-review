# GPATCH11 (human) — review notes

UniProt: Q8N954 (GPT11_HUMAN). Also called CCDC75 and "centromere protein Y / CENP-Y"
(the latter from the 2010 Ohta et al. proteomic screen, not the protein's established role).
HGNC:26768. Member of the GPATCH family of G-patch-domain RNA/spliceosome regulators.

## Context for the review

The annotation review is prompted by **geneontology/go-annotation#6450**, which flags the
IBA `is_active_in kinetochore` annotation (propagated from the 2010 IDA) as likely incorrect.
The upstream curator notes the 2010 image is low-resolution and that the 2024 *Nat Commun*
patient study explicitly does *not* observe kinetochore localization, instead reporting
diffuse nucleoplasmic and centrosomal localization plus a clear pre-mRNA splicing role.
A new (2026) *Sci Rep* paper on the *S. pombe* ortholog Sap34 corroborates the splicing role.

## Established function (from current literature)

- **Pre-mRNA splicing regulator via the G-patch / DEAH-helicase axis.** GPATCH11 belongs
  to the GPATCH family, whose hallmark glycine-rich G-patch motif activates DEAH-box RNA
  helicases on spliceosomal/RNP substrates [PMID:39572588 "Through their protein-protein
  and protein-nucleic acid interactions, they contribute significantly to RNA metabolism
  by regulating the remodeling of RNAs and ribonucleoprotein complexes by the DEAH-box
  RNA helicases with which they associate"]. The fission yeast ortholog Sap34 binds U2
  snRNP and U4/U6·U5 tri-snRNP components and activates Prp43 via its G-patch domain;
  `sap34Δ` causes a global splicing defect with increased intron retention
  [PMID:42260140 "Sap34 forms a complex with components of the U2 small nuclear
  ribonucleoprotein (snRNP) and the U4/U6 × U5 tri-snRNP", "deletion of sap34 leads to a
  global reduction in splicing efficiency, predominantly associated with increased intron
  retention"]. Human GPATCH11 patient retina shows dysregulated splicing in proteomics
  and transcriptomics [PMID:39572588 "Proteomic analysis of mouse retina confirms the
  roles GPATCH11 plays in RNA processing, splicing, and transcription regulation"].

- **Subcellular localization: nucleoplasm + centrosome.** The 2024 patient study reports
  "a diffuse presence in the nucleoplasm, as well as centrosomal localization, suggesting
  potential functions in RNA and cilia metabolism" [PMID:39572588]. No kinetochore signal
  is reported. This is consistent with the gene's GPATCH/spliceosome identity.

- **Disease association.** Biallelic loss-of-function variants (recurrent c.328+1G>T splice
  variant that removes the G-patch domain) cause a syndrome of early-onset retinal
  dystrophy with neurological impairment and skeletal abnormalities
  [PMID:39572588]. OMIM #621183.

## Reassessing the kinetochore annotation

The original IDA (PMID:20813266, Ohta et al. 2010) is part of the **MCCP** large-scale
mitotic chromosome proteomics screen that "identified approximately 4000 polypeptides in
highly purified chromosomes" and confirmed only a subset by GFP tagging. GPATCH11 was named
"CENP-Y" in that paper as a *predicted* centromere-associated protein based on the screen.
The upstream curator (go-annotation#6450) explicitly states the image supporting the
kinetochore call is "quite low resolution" and that subsequent high-resolution localization
work in the 2024 patient study reports nucleoplasm + centrosome with no kinetochore signal.

CLAUDE.md cautions against overruling experimental IDA from incomplete evidence, but here:
- the GO curator who maintains GO-annotation is themselves recommending removal,
- the 2010 IDA came from a low-resolution screening assay whose authors flagged ~97 of
  4,000 hits as "uncharacterized" candidates needing follow-up,
- the 2024 paper directly contradicts the localization with better microscopy in
  multiple cell types and a mouse model,
- the centromere-association nickname "CENP-Y" has not been adopted in any downstream
  functional literature.

Action: `MARK_AS_OVER_ANNOTATED` for both the IDA and the IBA kinetochore terms, with
proposed replacement terms `GO:0005654 nucleoplasm` and `GO:0005813 centrosome`. Using
`MARK_AS_OVER_ANNOTATED` rather than `REMOVE` because the 2010 proteomic evidence is
real (the protein was detected in purified mitotic chromosome fractions) but does not
support a *specific* kinetochore role; per the CLAUDE.md spirit, we flag rather than
silently delete an experimental annotation while citing the contradicting evidence.

## Other annotations

- `GO:0003676 nucleic acid binding` (IEA from InterPro G-patch IPR000467) — supported in
  spirit; the G-patch motif is an RNA-binding/helicase-cofactor module. Accept as a
  general molecular function; propose a more specific MF capturing the G-patch role
  (`GO:0003724 RNA helicase activity` would be wrong — GPATCH11 is not a helicase; better:
  the regulator role via Prp43 binding, GO:0008386 → not applicable). Keep as is; flag
  `pre-mRNA binding` (GO:0036002) as a more informative successor candidate.

- `GO:0005515 protein binding` (IPI from PMID:25416956 / IntAct, partners O00560 SDCBP and
  O60242 ADGRB3) — these are Y2H/AP-MS partners with no clear functional relevance to
  splicing or cilia. Mark as `KEEP_AS_NON_CORE` because the binding events themselves are
  empirically supported but "protein binding" is uninformative per project guidance.

## Core functions to propose

1. **Pre-mRNA splicing regulator within the spliceosomal U2/tri-snRNP environment**, via
   G-patch-dependent activation of DEAH helicase Prp43 (paralog: GPATCH1/2). Supported by
   PMID:42260140 (Sap34 ortholog) and PMID:39572588 (human/mouse phenotype + proteomics).

2. **Nucleoplasmic + centrosomal localization**, consistent with roles in RNA metabolism
   and primary cilia function (PMID:39572588).

## Suggested new GO terms / queries

- `GO:0000398 mRNA splicing, via spliceosome` (BP) — propose as IBA-promotable when the
  Sap34 paper is curated.
- `GO:0005654 nucleoplasm` (CC) — IDA-supportable from PMID:39572588.
- `GO:0005813 centrosome` (CC) — IDA-supportable from PMID:39572588.
- `GO:0005686 U2 snRNP` / `GO:0046540 U4/U6 × U5 tri-snRNP` (CC) — supported in fission
  yeast (PMID:42260140); human evidence indirect.

## Suggested questions for experts

- Does human GPATCH11 bind a specific DEAH helicase (e.g., DHX15, the human Prp43 ortholog)?
- Does the centrosomal localization reflect a primary cilium role or a moonlighting role?

## Upstream issue link

geneontology/go-annotation#6450
