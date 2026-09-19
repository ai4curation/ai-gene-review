# ARHGEF19 (WGEF, Ephexin-2) — review notes

Human, UniProt Q8IW93, 802 aa, HGNC:26604, chromosome 1p36.13.
Domain architecture (UniProt): DH 376–560, PH 592–704, SH3 715–776, with a long
disordered N-terminal region (1–~340) that carries the autoinhibitory module.

## Headline: this is a coverage problem, not an over-annotation problem

Thirteen GOA rows, of which three are IBA, one IEA, five TAS from Reactome, one
NAS from a review, two IPI `protein binding`, and one IGI. The measured gap:

- **11 of 14 primary experimental papers on this gene have produced no GO
  annotation of any gene in any species.**
- **12 of 14 have produced no GO annotation of ARHGEF19 in any species.**
- Exactly **one** has produced an ARHGEF19 annotation to anything other than
  `GO:0005515 protein binding`, and that paper (PMID:20643356) is a mouse
  genetics study whose subject is GRHL3.

Method and full table: `ARHGEF19-bioinformatics/RESULTS.md` §2, reproducible via
`go_coverage_by_reference.py` (QuickGO by reference, all species; paper list
assembled independently from the Affinage record and a live PubMed sweep).

Two external sources say the same thing in prose. The Ephexin-family review:
"Studies on Ephexin2 have not extensively been done compared with Ephexin1."
[PMID:30682817]. And the family's structural paper notes that the biological
functions of Ephexin2 and Ephexin3 remain elusive although they are known to
activate RhoA (PMID:33597305, full text via PMC7923574 — the locally cached copy
is abstract-only, so that sentence is not quoted as `supporting_text`).

### Retrieval: everything affinage missed has the same shape

Affinage's trust gates were clear and all eleven of its citations resolve to real
papers about this gene — its *precision* is fine. Its eleven citations
nevertheless omit three of the fourteen primary papers plus one commentary, and
in every case the title does not name the gene:

| missed | title | why it matters |
|---|---|---|
| PMID:20643356 | *"Epidermal wound repair is regulated by the planar cell polarity signaling pathway"* | the **only** paper that has produced an informative GO annotation for this gene in any species |
| PMID:18537266 | *"...regulation of **Tim** and related Dbl-family proteins"* — a paralogue | one of only two papers that assay Wgef autoinhibition directly |
| PMID:34813497 | *"ARHGEF19 promotes the growth of breast cancer..."* | the third independent MAPK tumour type |
| PMID:21686262 | *"Grhl3 and **GEF19** in the front rho"* | no `ARHGEF19` or `WGEF` query returns it — the title abbreviates the symbol |

PMID:20643356 is the sharp one: a clean gate on a record that omits the single
most annotation-productive paper on the gene. Gates certify the citations given,
not the ones withheld.

## Molecular function: RhoA, and specifically not Rac1 or Cdc42

The first characterisation reported a broad specificity: "WGEF was shown to
activate RhoA, Cdc42, and Rac1 by pulldown assay, and forced expression of WGEF
resulted in marked rearrangement of the actin cytoskeleton" [PMID:15485661].

Four years later the same three GTPases were re-tested side by side, with an
internal positive control, and the answer narrowed:

- RhoA: "Expression of hWGEF and XWGEF increased the level of active RhoA,
  whereas expression of hWGEFΔGEF did not" [PMID:18256687, Fig. 2A].
- Rac1/Cdc42: "we find that hWGEF and XWGEF did not activate Rac or Cdc42 above
  control levels, whereas Ephexin did" [PMID:18256687, Fig. 2B]. Ephexin-1 is the
  positive control in the same panel, so this is a real negative and not a failed
  assay.
- Binding mirrors activity: "We found that hWGEF and XWGEF strongly
  co-precipitated with RhoA at a level comparable to Ephexin, whereas hWGEFΔGEF
  did not" and "hWGEF but not XWGEF showed a very weak interaction with Rac-1,
  and neither WGEF bound to Cdc42" [PMID:18256687, Fig. 2C].

**Both papers used human WGEF, and the 2008 experiment is the better controlled
one.** The review treats RhoA as the substrate and records the 2004 Cdc42/Rac1
claim as superseded rather than as a second opinion. Note the consequence for
curation: the 2004 paper is the evidence Reactome cites for placing ARHGEF19 in
the RHOA-GEF set ("ARHGEF19 (Wang et al. 2004; Müller et al. 2020)",
R-HSA-8980691), so Reactome's TAS rests on the paper GO never annotated.

Loss of function in human cells: "depletion of WGEF with the aid of RNA
interference (RNAi) attenuates Rho activation in response to Wnt-1"
[PMID:18256687, Fig. 5B; MCF-7 cells].

### GO cannot say "RhoA GEF" any more

This matters for how the review is written. Checked across three independent
services (EBI OLS4, the GO API, QuickGO) plus this repo's own `cache/go/terms.csv`:

| term | status |
|---|---|
| GO:0005089 Rho guanyl-nucleotide exchange factor activity | **obsolete**, merged into GO:0005085 |
| GO:0005088 Ras GEF activity | **obsolete**, merged into GO:0005085 |
| GO:0030676 Rac GEF activity | **obsolete**, merged into GO:0005085 |
| GO:0017048 Rho GTPase binding | **obsolete**, merged into GO:0031267 |
| GO:0017016 Ras GTPase binding | **obsolete**, merged into GO:0031267 |
| GO:0005085 guanyl-nucleotide exchange factor activity | current; **no `is_a` children** (OLS4 0; QuickGO's only children are `capable_of` / `negatively_regulates`) |
| GO:0031267 small GTPase binding | current; no children in either service |

QuickGO alone would have been misleading in both directions: it silently resolves
the merges and returns GO:0005085's live record for the obsolete ids, so querying
`GO:0005089` there returns a non-obsolete term. The repo's local ontology cache
has no row for any of the merged ids, which is the third, offline confirmation.

So `GO:0005085` is already the most specific MF term available and there is
nothing to MODIFY it to. The best-established fact about this protein — that it
is a RhoA GEF and *not* a Rac1/Cdc42 GEF — is currently inexpressible in a plain
GAF term and would need an annotation extension or a GO-CAM `has_input(RHOA)`.
That is recorded as a knowledge gap, not as a proposed term.

## Regulation: a doubly autoinhibited GEF

- **N-terminal inhibitory helix, relieved by tyrosine phosphorylation.** "Here we
  show that two other Dbl-family proteins, Ngef and Wgef, which like Tim contain a
  C-terminal SH3 domain, are also activated by tyrosine phosphorylation of a
  blocking helix." [PMID:18537266]. The residue is **Y295** in human numbering:
  "This particular tyrosine (Y353xWGEF/295hWGEF) of hWGEF is present in NID and
  locks the GEF by interacting with its DH domain." [PMID:38714795]. Position 295
  of Q8IW93 is indeed Y (checked in `dh_competence_check.py`).
- **C-terminal SH3 mode.** "we show that the C-terminal SH3 domain binding to a
  polyproline region N-terminal to the DH domain of the Tim subgroup of
  Dbl-family proteins provides a unique mechanism of regulated autoinhibition of
  exchange activity" [PMID:18537266]. The family-wide structural treatment
  (PMID:33597305) calls this the C-terminal (SH3–HC) inhibitory mode and shows it
  is relieved in Ephexin4 and SGEF by PDZ proteins binding a *C-terminal* PDZ
  motif; ARHGEF19 has no such C-terminal motif, and the paper explicitly leaves
  the activating input for the other Ephexins undefined.
- **Dvl2 supplies the missing input, via an internal motif.** PMID:38714795 maps
  Dvl2-PDZ binding to an "internal PDZ-binding motif" and reports GEF assays in
  which PDZ binding relieves autoinhibition.

### Two published disagreements, both unresolved

1. **Where Dvl binds.** PMID:18256687 mapped it to the N-terminus: "We found that
   hWGEFΔN and hWGEFDH–PH could not bind Dvl, whereas the other mutants tested,
   in particular the N-terminal domain itself, retained binding activity"
   (deletion constructs; ΔN = residues 1–213 removed). PMID:38714795 says
   otherwise and says so explicitly: "This observation is contrary to the previous
   study in which the Dvl2PDZ binding was mapped towards the N-terminus of hWGEF
   (between amino acid residues 1–213)17, whereas the motif identified by us is
   present between amino acid residues 349–359 of hWGEF."
2. **What was actually measured on the human protein in 2024.** The exchange
   assays in PMID:38714795 are on *Xenopus* protein: "Since some of these hWGEF
   constructs were found to be insoluble and/or poorly expressed in E. coli, we
   used WGEF from Xenopus laevis (xWGEF) as a surrogate system for further
   studies." The human contribution is peptide/fragment binding.

UniProt lists PDB **8YR7** under Q8IW93, which reads as "there is a structure of
human ARHGEF19". There is not, in the useful sense: 8YR7 is a Dvl2-PDZ construct
with the WGEF peptide fused to its C-terminus, and the authors report the fusion
did not work — "Even this approach failed to produce the WGEFpep–Dvl2PDZ complex
structure (PDB ID: 8YR7)". The deposited entity carries `TFSLWQDIP` (unique in
Q8IW93, at 351) but 30 of 109 residues are unmodelled. No ARHGEF19 coordinates
should be relied on.

## Is the DH–PH module competent? Both directions

Full analysis in `ARHGEF19-bioinformatics/RESULTS.md` §1.

Yes, as a module: ARHGEF19 spans 24 of the 25 DH positions that contact RhoA in
*both* solved RhoA complexes (1X86 LARG:RhoA, 1LB1 Dbs:RhoA), matching the
weakest verified-active comparator in the panel and beating it in one case. Its
PF00621 bitscore (137.0) sits inside the 134.6–166.9 range spanned by five GEFs
that have both a substrate co-crystal and measured exchange activity.

But the same analysis refuses to go further, and this is the important half.
Identity at the exchange surface is 36% for ARHGEF19 against LARG and **36% for
Tiam1**, which is a GEF for a different GTPase. A measure that cannot separate a
RhoA GEF from a Rac1 GEF cannot be used to assign substrate. And the truncation
control shows that a Pfam DH hit means very little on its own: ARHGEF19 isoform 2
(Q8IW93-2, which deletes 484–783 and so loses half the DH domain plus all of PH
and SH3) still clears the Pfam gathering threshold at 65.5 bits while spanning
only 5 of the 25 contact positions.

So: no residue-level reason to suspect a pseudo-GEF, and no residue-level licence
to claim exchange activity either. The claim rests on the biochemistry.

## Biological process

- **Wnt/PCP and convergent extension.** The core result, in Xenopus with human
  rescue: WGEF binds Dvl (via the Dvl PDZ domain) and Daam1, overexpression
  activates RhoA and rescues dnWnt-11, depletion blocks CE and is rescued by
  RhoA/Rok [PMID:18256687]. Human hWGEF mRNA rescues the Xenopus morphant, so the
  human protein is functionally interchangeable in this assay.
- **Epidermal wound repair via GRHL3.** "we identified RhoGEF19, a homolog of a
  RhoA activator involved in PCP signaling in Xenopus, as a direct target of
  GRHL3" and "Knockdown of Grhl3 or RhoGEF19 in keratinocytes induced defects in
  actin polymerization, cellular polarity, and wound healing, and re-expression of
  RhoGEF19 rescued these defects in Grhl3-kd cells" [PMID:20643356]. This is the
  source of the human IGI (`GO:0032956`, with GRHL3) and of the mouse Arhgef19
  IMP for `GO:0042060` that the human IBA projects back from — MGI:1925912 is
  mouse *Arhgef19* itself, so the wound-healing IBA is a one-to-one ortholog
  transfer, not a paralogue guess.
- **Renal ciliogenesis.** "Additionally, the Daam1 partner, ArhGEF19, is also
  required for proper cilia formation in MDCKII cells" [PMID:31469868]. Dog and
  mouse lines; the same paper reports that Xenopus kidney knockdown did *not*
  reproduce the cilia loss, so the effect is not obviously conserved.
- **Pronephric tubulogenesis.** Daam1/WGEF/Rho branch required, in Xenopus and
  zebrafish [PMID:21804089].
- **Adipogenesis.** Demethylation of exon 1 CpGs during 3T3-L1 differentiation;
  forced WGEF inhibits the adipogenic programme [PMID:19503838]. Mouse only.
- **A published negative.** "WGEF shRNA had no apparent effect on Dvl-induced
  neurite retraction in N1E-115 cells" and "other Rho-GEFs, including WGEF, are
  not related to this process in N1E-115 cells" [PMID:20810787]. Mouse cells, so
  this does not license a human NOT annotation, but it does mean the Wnt→Dvl→RhoA
  role is context-dependent rather than universal.

## A second, RhoA-independent branch: MAPK/ERK in cancer

Three independent human studies:

- NSCLC: "ARHGEF19 activated the mitogen-activated protein kinase (MAPK) pathway
  in a RhoA-independent manner: ARHGEF19 interacted with BRAF and facilitated the
  phosphorylation of its downstream kinase MEK1/2; both the Dbl homology (DH) and
  Pleckstrin homology (PH) domains of ARHGEF19 were indispensable for the
  phosphorylation of MEK1/2." [PMID:29164615]
- SCLC: "ARHGEF19-DH and -PD domain interacts with HRAS and activates the
  MAPK/ERK pathway in SCLC cells and SCLC xenografts." [PMID:32993957] (the
  abstract's "-PD" is a typographical error for the PH domain)
- Breast: "we found that ARHGEF19 could activate the MAPK pathway in breast cancer
  cells" [PMID:34813497]

Caveats worth carrying: the NSCLC and SCLC papers share an institution, the
breast paper is in a low-visibility journal, and no structural or direct-binding
work supports a DH–PH:BRAF interface. Two of the three name the same domains as
necessary, which is at least a mechanistic commitment rather than a correlation.
Taken together this is enough to propose `GO:0070374 positive regulation of ERK1
and ERK2 cascade` as a new IDA-grade annotation, but not enough to call it core.

## Partners

| partner | evidence | in GO? |
|---|---|---|
| RHOA (P61586) | co-IP + GST pulldown, human [PMID:18256687]; interaction increases on ANKK1 knockdown in SH-SY5Y [PMID:39409035] | yes, as `GO:0005515 protein binding` |
| PAK5 (Q9P286) | binary interactome screen, 3 experiments [PMID:32296183; UniProt `NbExp=3`] | yes, as `GO:0005515 protein binding` |
| DVL2 | co-IP via the Dvl PDZ domain [PMID:18256687]; peptide/fragment binding [PMID:38714795] | **no** |
| DAAM1 | co-IP with N-Daam-1 but not C-Daam-1 [PMID:18256687] | **no** |
| ANKK1 (Q8NFD2) | "Co-IP and PLA experiments confirmed ANKK1–WGEF interaction" in human SH-SY5Y [PMID:39409035] | **no** |
| BRAF | co-IP, NSCLC [PMID:29164615] | **no** |
| HRAS | co-IP, SCLC [PMID:32993957] | **no** |

## Localisation

There is no human localisation experiment worth annotating. The three
`GO:0005829 cytosol` rows are Reactome compartment assignments attached to GEF
*sets*, not measurements on this protein. The only positive data are Xenopus —
"XWGEF is associated with the plasma membrane in the Xenopus embryo"
[PMID:18256687] — and a qualitative human observation that WGEF shows "a broad
cellular distribution" in proliferating SH-SY5Y and localises to neurites on
differentiation [PMID:39409035]. `GO:0005886 plasma membrane` is the biologically
expected site (a GEF must meet membrane-anchored RhoA) but is not supported for
human, so it goes in the gaps, not in `core_functions[].locations`.

One of the three cytosol rows deserves a flag rather than a shrug.
R-HSA-205039 is *"p75NTR indirectly activates RAC and Cdc42 via a
guanyl-nucleotide exchange factor"*; its catalyst is a generic
`guanyl-nucleotide exchange factor activity of GEFs [cytosol]` set and its output
is RAC1:GTP. ARHGEF19 reaches that reaction only by set membership, and human
WGEF does not activate Rac1 [PMID:18256687, Fig. 2B]. The `cytosol` term is not
false, but the route by which ARHGEF19 acquired it is.

## What I deliberately did not do

- Did not propose a Rho-specific MF term: it does not exist any more (three
  services agree), and a failed GO text search would not have been evidence
  either way — the branch was walked.
- Did not propose `GO:0005886 plasma membrane`: Xenopus only.
- Did not propose a `NOT` annotation for Rac1/Cdc42 GEF activity: with the
  substrate-specific GEF terms merged away, `NOT enables GO:0005085` would read
  as "is not a GEF at all", which is the opposite of the finding.
- Did not propose cilium or ciliogenesis terms: MDCKII (dog) and IMCD3 (mouse),
  and the paper's own Xenopus arm disagreed.
- Did not propose an Eph-receptor term. "Ephexin-2" is a name given by homology;
  the family review is explicit that an Eph receptor interacting with Ephexin2
  has not been identified.
