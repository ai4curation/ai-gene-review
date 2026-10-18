# EBP (Q15125) review notes

Deep-research provider (falcon) was OUT OF CREDITS (HTTP 402) at the time of review, so
no `EBP-deep-research-falcon.md` was generated. This review is grounded in the cached
UniProt record (`EBP-uniprot.txt`), the seeded GOA (`EBP-goa.tsv`), cached
`publications/PMID_*.md`, and cached `reactome/R-HSA-*.md`.

## Core biology

EBP = 3-beta-hydroxysteroid-Delta(8),Delta(7)-isomerase (sterol Delta8-Delta7 isomerase;
EC 5.3.3.5), historically identified as the emopamil-binding protein. It is a multi-pass
ER-membrane enzyme of the post-lanosterol cholesterol biosynthesis pathway.

- Catalyzes isomerisation of the Delta(8) double bond of sterol intermediates to Delta(7):
  zymostenol -> lathosterol (modified Kandutsch-Russell) and zymosterol ->
  cholesta-7,24-dien-3beta-ol (Bloch pathway).
  [PMID:8798407 "This endoplasmic reticulum-resident membrane protein catalyzes the conversion of delta8-sterols to their corresponding delta7-isomers"]
- Activity demonstrated by heterologous yeast complementation of erg2 deficiency and by
  Ala-scanning mutagenesis identifying catalytic residues (H77, E81, E123, T126, N194, W197).
  [PMID:9894009 "The human emopamil binding protein (hEBP) exhibits sterol Delta8-Delta7 isomerase activity (EC 5.3.3.5)"]
- 4 predicted transmembrane helices; EXPERA domain (PROSITE PS51751); EBP family.
- Localises to ER membrane and nuclear envelope; redistributes to cytoplasmic vesicles at
  mitosis. [PMID:10406945 "hSI and SR-BP-1 were associated with the endoplasmic reticulum and with the outer and inner membranes of the nuclear envelope"; "delocalized during the cell cycle at the mitosis step when the nuclear membranes disappeared"]

## Disease

- CDPX2 (X-linked dominant chondrodysplasia punctata / Conradi-Hunermann-Happle syndrome):
  loss of isomerase activity; accumulation of 8-dehydrocholesterol and 8(9)-cholestenol.
  [PMID:10391219 "defects in sterol-delta8-isomerase cause CDPX2 and suggest a role for sterols in bone development"]
  [PMID:10391218 delta8-delta7 sterol isomerase = Ebp mutated in tattered mouse / CDPX2]
- MEND syndrome (hypomorphic hemizygous male variants), from UniProt DISEASE.

## AEBS / ChEH (secondary/context activity)

EBP is a component of the microsomal antiestrogen binding site (AEBS), a hetero-oligomeric
complex with DHCR7, that carries cholesterol-5,6-epoxide hydrolase (ChEH) activity.
[PMID:20615952 "The AEBS, a hetero-oligomeric complex composed of 3beta-hydroxysterol-Delta8-Delta7-isomerase (D8D7I) and ... cholesterol-5,6-epoxide hydrolase (ChEH)"]
UniProt notes: "The precise role of each component of this complex has not been described yet."
So GO:0033963 cholesterol-5,6-oxide hydrolase activity is a genuine (complex-level, tamoxifen/AEBS)
activity but is not the isomerase's own core catalytic function -> KEEP_AS_NON_CORE.

## GO:0047750 cholestenol delta-isomerase activity

This is EC 5.3.3.5, exactly the enzyme's function (lathosterol <-> 5alpha-cholest-8-en-3beta-ol).
The three EXP annotations (PMID:8798407, 9894009, 12760743) plus the IEA(EC) all support this.
It is essentially synonymous/closely related to the C-8 sterol isomerase (GO:0000247) /
steroid Delta-isomerase (GO:0004769) grouping. ACCEPT.

## Protein-binding IPIs

GO:0005515 (x2, PMID:25910212, PMID:32296183) and GO:0042802 identical protein binding
(PMID:32296183, homodimer, consistent with UniProt Q15125-Q15125 IntAct self-interaction
and PMID:12760743 "Chemical cross-linking induced homodimerization of EBPL and EBP").
Bare "protein binding" IPIs from large-scale interactome screens are uninformative ->
MARK_AS_OVER_ANNOTATED per policy (do not REMOVE experimental IPIs). Identical protein
binding is corroborated by the documented homodimer, so ACCEPT (KEEP_AS_NON_CORE).

## Localization annotations

- ER / ER membrane: strongly supported (IDA PMID:10406945; IBA; UniProt). Core CC = ER membrane.
- nuclear envelope / nuclear membrane: supported by PMID:10406945 IDA -> KEEP_AS_NON_CORE.
- cytoplasmic vesicle: only during mitosis (PMID:10406945) -> KEEP_AS_NON_CORE.
- membrane (GO:0016020, IEA InterPro): correct but uninformative parent -> MARK_AS_OVER_ANNOTATED.

## Ossification / bone (GO:0043931 IMP PMID:10391219)

Downstream/indirect: the CDPX2 skeletal phenotype reflects the sterol defect, not a direct
role of EBP in ossification machinery. The paper says sterols play "a role ... in bone
development" -> KEEP_AS_NON_CORE (secondary developmental consequence).

## Revision 2026-10-09: isomerase term choice

Checked the GO definitions in OLS rather than relying on term labels:

- GO:0047750 cholestenol delta-isomerase activity = "5-alpha-cholest-7-en-3-beta-ol =
  5-alpha-cholest-8-en-3-beta-ol", which is exactly UniProt's RHEA:15281 reaction for EBP
  ("Reaction=lathosterol = 5alpha-cholest-8-en-3beta-ol", EC 5.3.3.5) and carries three EXP
  annotations (PMID:8798407, 9894009, 12760743). This is now the core MF.
- GO:0000247 C-8 sterol isomerase activity = "fecosterol = episterol", the fungal ergosterol
  pathway reaction of yeast ERG2 (structurally unrelated to EBP). Fecosterol is not an
  intermediate in human cholesterol synthesis. IBA, ISS and IEA annotations -> MODIFY to GO:0047750.
- GO:0004769 steroid Delta-isomerase activity = "a 3-oxo-delta(5)-steroid = a
  3-oxo-delta(4)-steroid" (EC 5.3.3.1, steroidogenic KSI). It is NOT a parent of the sterol
  Delta8-Delta7 reaction (both are siblings under GO:0016863). The earlier KEEP_AS_NON_CORE
  calls treated it as a grouping term; all six (IBA, EXP x2, IDA x2, IMP) -> MODIFY to GO:0047750.
- Bare protein binding IPIs -> REMOVE (no informative MF; interaction not disputed).

Alignment: dismech X-linked_Chondrodysplasia_Punctata_2 used GO:0000247 on its molecular node;
changed there to GO:0047750 to match. MEND_Syndrome already used GO:0047750.


## Source-specific reassessment, 2026-10-18

EBP has one established physiological catalytic unit: sterol Delta8-to-Delta7 isomerization at the ER membrane during cholesterol biosynthesis. The purified human enzyme and structure establish five transmembrane helices, superseding the historical four-helix prediction (PMID:31165728). Current Q15125 has 230 residues and H76/E80/E122/W196; the earlier mutagenesis abstract uses H77/E81/E123/W197 (PMID:9894009). The cause of that historical numbering difference is unestablished. Met1 removal and chain 2–230 are processing annotations, not an additional splice product.

Human recombinant sterol isomerase also turns over fecosterol in the substrate panel and yields the corresponding Delta7 product. This positive chemistry is retained as non-core substrate breadth; it does not demonstrate an endogenous human fecosterol pathway. The substrate comparison used bacterial homogenates, while yeast-purified kinetics and oligomer estimates are separate experiments (PMID:12133002). The current GO:0004769 definition describes a different steroid reaction, so affected broad labels are refined to GO:0047750. The production GO-CAM explicitly supplies zymosterol and cholesta-7,24-dien-3beta-ol despite its GO:0000247 activity label; the modeled human substrate pair is preserved as evidence of a term-scope discrepancy. Reactome's corresponding explicit reaction chains are likewise retained.

Cooperative EBP/DHCR7 cholesterol-5,6-epoxide hydrolysis is positive evidence. The main original shows human-protein coexpression in COS-7 and depletion in human MCF-7 cells; it does not isolate autonomous EBP hydrolase catalysis (PMID:20615952; supporting abstract PMID:15175332). This complementary role remains non-core. A fresh full-text copy was read separately; the preexisting abstract-only repository cache and its flags remain unchanged.

Native human microscopy supports ER and nuclear-envelope membranes plus vesicle redistribution during mitosis (PMID:10406945). HPA independently scores both ER and nuclear membrane as supported, with a multiple-gene antibody caution. Nuclear membranes and mitotic vesicles remain positive non-core pools. The original microscopy text and Figure8 caption disagree about some panel letters; no panel-specific assignment or unseen pixel inspection is claimed.

The interaction review distinguishes verified pair identity from partner-class interpretation and from physiological mechanism. The historical HuRI aggregate contains 524 records; the complete selected union adds 3 records from the disease-variant screen. The three literal self-pair records require EBP on both sides. Individual partner refinements identify a supported binding class without transferring a partner's activity to EBP or requiring an active-site interface. Current and archived sequence checks retain assayed fragment limits, including the historical SLC3A2 isoform designation. Nine IntAct-only clone-side occurrences remain unresolved. See the [executed source audit](EBP-bioinformatics/source-audit/RESULTS.md) and its [manual partner-class table](EBP-bioinformatics/source-audit/partner-classes.md).

Supported generic binding is retained as non-core where no justified specific class was established, following the explicit [ClinGen curation instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). This supersedes the informational-exclusion rationale in the older notes without rewriting that historical text. The PAINT review uses literal IBD/IRD nodes and the exact target lineage, not donor count or target self-grounding as alleged error; EBPL-branch losses do not occur on the EBP path.

The review preserves 40 historical assertions and adds 172 genuine normal-source contexts, mostly individual interaction contexts. None is an authored NEW annotation. The genuine current GOA export has 210 raw contexts. Only historical indices 5 and14 are retired because their exact source contexts are absent from that export; their positive biological reviews remain visible. The exact prior 209-context export is retained in [source snapshots](source-snapshots/source-provenance.json). Every original publication, family and GO-CAM cache remains unchanged, as do inherited excerpts and this notes prefix.

Configured Falcon research failed with HTTP 403 authentication, and the genuine perplexity-lite fallback failed with HTTP 401 insufficient quota. No provider report was fabricated. Manual source reading and database analyses supply the documented evidence. Access limits, exact original locators and the distinction between cache availability and separately read originals are recorded in the [source guide](EBP-source-guide.md).
