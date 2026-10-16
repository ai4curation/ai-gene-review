# GPR75 review notes

Gene: human GPR75 (UniProt O95800), class A rhodopsin-like GPCR, 540 aa, chr 2p16.
Reviewed as part of a contested-function batch (see also GPR158, GPR25).

## The contested annotation

GOA carries `GO:0016493` **C-C chemokine receptor activity** three times on human GPR75,
with **IBA**, **IEA (Ensembl ortholog transfer)** and **ISS** — and no experimental
evidence code anywhere. The paired process term `GO:0070098` chemokine-mediated
signaling pathway is carried on the same footing (IEA + ISS).

## Where the IBA actually comes from (checked, not assumed)

The brief's premise was that the IBA has no experimental donor. That is **not quite
right, and it matters**. The `WITH/FROM` field of the human IBA is
`MGI:MGI:2441843|PANTHER:PTN002796002`. MGI:2441843 resolves to **mouse Gpr75**
(confirmed at informatics.jax.org), and QuickGO shows that mouse Gpr75 carries
`GO:0016493` with **IDA from PMID:17001303**. So the IBD behind this IBA *is*
experimentally grounded — in exactly one descendant, the mouse orthologue.

Two consequences:

1. Per `CLAUDE.md`, donor count is not a proxy for evidential strength, and a node
   seeded by one well-characterised MOD gene can be sound. So the propagation is not
   *mechanically* defective, and `REMOVE` on "no experimental donor" grounds would have
   been wrong.
2. But because the only experimental descendant cited is the mouse orthologue, the IBA
   carries **no information beyond the mouse-to-human transfer already recorded twice**
   as ISS (UniProtKB:Q6X632) and as the Ensembl Compara IEA (also Q6X632). All four
   rows reduce to a single 2006 heterologous-expression study.

That study:
[PMID:17001303 "We show for the first time that RANTES activates the orphan G
protein-coupled receptor 75 (GPR75)."] and
[PMID:17001303 "The latter effect was blocked by the phospholipase-C inhibitor (PLC)
U73122 indicating that Gq proteins mediate GPR75 signaling."]

It was later supported in human neuroblastoma cells lacking the canonical CCL5 receptors:
[PMID:29772059 "Both qPCR and flow cytometry show that these cells express GPR75 but do
not express CCR5, CCR3 or CCR1 receptors."] and
[PMID:29772059 "knocking down GPR75 expression by a CRISPR-Cas9 approach inhibited the
ability of CCL5 to activate pERK in SH-SY5Y cells"], concluding
[PMID:29772059 "Therefore, we propose that GPR75 is a novel receptor for CCL5 that could
explain some of the pharmacological action of this chemokine."]

So the claim is not fabricated. It is, however, a *proposal* that the field has declined
to adopt.

## Why it is nevertheless an over-annotation

**1. IUPHAR still calls GPR75 an orphan.**
[PMID:40362321 "however, its definitive endogenous ligand remains unidentified, and
GPR75 is currently classified as an orphan receptor by International Union of Basic and
Clinical Pharmacology (IUPHAR)"] and
[PMID:40362321 "At present, the endogenous ligands, agonists, and antagonists for GPR75
have not been conclusively identified, and some controversy persists in this area."]

**2. Both candidate agonists are explicitly contested in 2025-2026 reviews.**
[PMID:40757922 "Recent studies have suggested several potential endogenous ligands for
GPR75, including 20-HETE and RANTES/CCL5, but their status as true receptor agonists
remains controversial."]
[PMID:40362321 "However, debate continues regarding GPR75’s endogenous ligands."]

**3. The 2026 cryo-EM structures argue against any orthosteric ligand, chemokine
included.**
[PMID:41545757 "Here we present the cryo-EM structures of human GPR75 in apo and
Gq-coupled states"] revealing
[PMID:41545757 "a completely collapsed extracellular domain eliminates the traditional
orthosteric binding pocket, raising critical questions about previously reported small
molecule ligands"], and the receptor is constitutively active without a ligand:
[PMID:41545757 "GPR75 assumes active-like conformation in both apo and G protein
complexed structures through unique molecular switches-the canonical DRY motif is
replaced by HRL, abolishing the ionic lock"]

A collapsed extracellular domain is a harder problem for an 8 kDa chemokine than for a
small molecule: chemokine receptors engage their ligands over a large N-terminal /
extracellular-loop surface (CRS1) before the ligand N-terminus inserts into the pocket
(CRS2). Neither site appears to exist here.

**4. GPR75 is not a chemokine receptor by descent.** Its closest relatives by
transmembrane sequence are peptide receptors of other families, not CCRs:
[PMID:40362321 "this receptor shares transmembrane domain homology with the neuropeptide
Y receptor in Caenorhabditis elegans, the rat galanin receptor type 3, and the porcine
growth hormone secretagogue receptor type 1b"]

## What GPR75 *is* solidly

A plasma-membrane, Gq-coupled class A GPCR:
[PMID:40362321 "More recent studies have classified GPR75 as a Gαq protein-coupled
receptor within the Class A rhodopsin-like family"], with a Gq-bound cryo-EM structure
(PMID:41545757), and the only thing GOA should confidently assert about its molecular
function is `GO:0004930`.

Its genetics are strong and independent of the ligand question: human loss-of-function
variants protect against obesity, and rodent knockouts are lean and insulin-sensitive.
Those are organismal phenotypes and do not license a molecular-function claim.

## Curation position taken

- `GO:0016493` C-C chemokine receptor activity (IBA, IEA, ISS — all three) →
  **MARK_AS_OVER_ANNOTATED**, with a `propagation_review` on the IBA recording that the
  IBD's only experimental descendant is mouse Gpr75 itself, so the phylogenetic
  annotation adds nothing over the ISS/Ensembl transfers it duplicates.
  Not `REMOVE`: the mouse IDA is a real experimental annotation whose full text was not
  read here, and three groups have reported CCL5-dependent, GPR75-dependent responses.
- `GO:0070098` chemokine-mediated signaling pathway (IEA, ISS) →
  **MARK_AS_OVER_ANNOTATED**, same footing, same reasoning.
- `GO:0004930` G protein-coupled receptor activity (IEA, ISS) → **ACCEPT, core**.
  Deliberately generic: this is the correct level of claim for a receptor IUPHAR still
  lists as orphan, and the Gq-coupled structure confirms it.
- `GO:0007186` GPCR signaling pathway (IBA, IEA, ISS) → **ACCEPT, core**.
- `GO:0005886` plasma membrane (IBA, IEA, IDA/HPA, IC, TAS) → **ACCEPT**.
- `GO:0016020` membrane (IEA) → **ACCEPT** (generic but correct).

## Unresolved

- Does CCL5 act on GPR75 directly, or through a co-receptor / transactivation route that
  would explain GPR75-dependence without GPR75 being the chemokine's receptor?
- If the orthosteric pocket is collapsed and the receptor is constitutively active, is
  GPR75 regulated by an allosteric ligand, by a protein partner, or by expression level
  alone?
- The 20-HETE claim is not annotated in GOA for human GPR75 and is not adjudicated here,
  but it is under the same cloud as the CCL5 claim.
