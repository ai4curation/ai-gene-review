# ARHGEF15 (Ephexin-5 / Vsm-RhoGEF) — review notes

UniProt O94989, 841 aa, HGNC:15590, chr17. Dbl-family RhoGEF: one DH domain (417–601) and
an ephexin-type PH domain (CDD `cd01221 PH_ephexin`; InterPro IPR047270). PANTHER
PTHR12845:SF7 within the ephexin family PTHR12845.

Quotation convention in this file: every quotation is immediately followed by its source in
square brackets, and `ARHGEF15-bioinformatics/check_quotes.py` verifies each one verbatim
against the cached publication or repository file — including `file:` sources, which the
repo's own reference validator does not check. An unattributed quotation is reported as a
problem by that checker, not silently ignored.

## The short version

The protein is a Dbl-family exchange factor whose exchange machinery is intact and whose
**substrate identity is contested between the systems it has been studied in** — and GO can
no longer express substrate identity on the molecular-function side in any case. Several
literatures run in parallel and must not be used to argue each other:

| system | substrate reported | key evidence |
|---|---|---|
| vascular smooth muscle (human/rat) | RhoA | EphA4-dependent enhancement of exchange activity, PMID:12775584 |
| endothelium (mouse retina, HUVEC) | Cdc42, plus potentiated RhoJ inactivation | PMID:23029280 |
| hippocampal neuron (mouse) | RhoA in 2010; RhoA **and** Cdc42 in 2025 | PMID:21029865, PMID:40138406 |
| disease, vascular and bone (human variants, mouse knock-in) | RhoA/ROCK2 | PMID:36929019 |
| family-wide specificity screen (human, HEK-based) | **RhoA + and Cdc42 +, Rac1 −** | PMID:32203420, Supplementary Table 2 |

The last row is the single most decision-relevant measurement for this gene, it is on the
**human** protein at full length (Supplementary Table 1 row 56: `Human`, 841 aa, cDNA
BAA74938.3/AAH36749.1), and it is **absent from GOA**. Müller et al. 2020 screened all 145 human RhoGEFs/RhoGAPs against RhoA,
Rac1 and Cdc42; Reactome cites this paper for placing ARHGEF15 in both `RHOA GEFs activate
RHOA` and `CDC42 GEFs activate CDC42`. The paper is paywalled with no PMC record, but its
supplementary tables are free, which is how the row was read
(`ARHGEF15-bioinformatics/muller2020_specificity.py`). Affinage did not return it, and
neither does a symbol search: its title is
"Systems analysis of RhoGEF and RhoGAP regulatory proteins reveals spatially organized RAC1 signalling from integrin adhesions"
[PMID:32203420] — named for RAC1, the one GTPase ARHGEF15 does *not* act on. It surfaced
only by following Reactome's own citation out of the cached `R-HSA-9013159` entry.

One caveat that the analysis itself produced: ITSN1, a textbook Cdc42 GEF, scores negative
for all three GTPases in the same screen. So a `−` in that table means "not detected here",
not "does not act on". The Rac1 `−` for ARHGEF15 is nevertheless corroborated independently
by PMID:21029865 and by UniProt's reading of PMID:36929019.

## Existing GO record (31 GOA rows)

Every molecular-function row is `GO:0005085 guanyl-nucleotide exchange factor activity`.
There is no substrate-specific MF row, and there **cannot** be one — see the ontology
section. Provenance of the MF rows:

- **IDA** from PMID:12775584, the human VSMC paper.
- **IMP** from PMID:36929019, the BSVD5 variants.
- **IBA** from `PANTHER:PTN002656129`. The PAINT file
  (`interpro/panther/PTHR12845/PTHR12845-paint.tsv`) shows the underlying **IBD** placed at
  `taxon:2759` (Eukaryota), seeded by `MGI:MGI:3045246`, `O94989` itself, `Q12774` ARHGEF5,
  `Q5VV41` ARHGEF16 and `Q8N5V2` NGEF. `MGI:MGI:3045246` was resolved against
  informatics.jax.org, whose record for that accession is Arhgef15, Rho guanine nucleotide
  exchange factor 15 (mouse); it is not quoted here because MGI pages are not part of the
  repository's checkable reference cache. The target appearing in its own WITH/FROM is the
  expected marker that experimental grounding exists on the target itself; it is not
  circular.
- **ISS** from `UniProtKB:Q5FWH6` (mouse Arhgef15), whose own `GO:0005085` is **IDA from
  PMID:21029865** — a measurement, not a chain of inferences.
- **IEA** GO_REF:0000120 citing `InterPro:IPR000219` (DH domain) and `IPR047271`
  (Ephexin-like). Weakest of the five, but it points at the right domain: IPR000219 *is* the
  catalytic DH domain, not an unrelated fold that merely shares a name.

The two ISS rows from `UniProtKB:D3ZPJ8` (rat Arhgef15) deserve a note. The rat entry's
`GO:0005737` and `GO:0051496` are both **IDA from PMID:12775584**, the same paper that is the
human IDA source. Those rows are not independent corroboration of the human record; they are
the same experiments curated against the rat protein, and the human ISS is a curator
recognising that.

## What the literature says, by system

### Vascular smooth muscle — the original human identification

PMID:12775584 (Ogita et al. 2003, Circ Res) named the protein Vsm-RhoGEF and reported it as
VSMC-specific:
"a novel VSMC-specific guanine nucleotide exchange factor (GEF) for Rho (Vsm-RhoGEF/KIAA0915) was expressed specifically in VSMCs of several organs including the heart, aorta, liver, kidney, and spleen"
[PMID:12775584]. The mechanism is receptor-coupled:
"tyrosine phosphorylation of Vsm-RhoGEF induced by EphA4 upon ephrin-A1 stimulation enhanced the Vsm-RhoGEF activity for RhoA"
[PMID:12775584], and the downstream requirement rests on two independent perturbations:
"The requirement of Vsm-RhoGEF for ephrin-A1-induced assembly of actin stress fibers in VSMCs was shown by the overexpression of a dominant-negative form of VSM-RhoGEF and by the depletion of Vsm-RhoGEF using RNA interference."
[PMID:12775584]. The cache is **abstract-only**; the GOA IDA rests on the full text.

### Endothelium — a different substrate, and a contradicted expression claim

PMID:23029280 (Itoh et al. 2012, PLoS ONE) found Arhgef15 as an endothelial-cell-enriched
RhoGEF in mouse retina and reported Cdc42 rather than RhoA:
"In 293T cells, ectopically expressed Arhgef15 as well as its truncated DH-PH proteins induced activation of endogenous Cdc42 (Figure 2A)."
[PMID:23029280]. One of the two experiments is in human cells:
"VEGF-induced activation of Cdc42 was abrogated by Arhgef15 knockdown in human umbilical vascular ECs (HUVECs, Figure 2B and Figure S4)."
[PMID:23029280], so this is not dismissible as a mouse-only observation.

The same paper directly contradicts Ogita's tissue claim, in mouse retina:
"lacZ expression was undetectable in neurons, astrocytes, and vascular smooth muscle cells (vSMCs), ensuring the endothelial specificity of Arhgef15 expression in mouse retinas"
[PMID:23029280]. Different tissue, different species, different assay — recorded as a real
tension, not as a refutation of either. UniProt still carries Ogita's TISSUE SPECIFICITY line
unqualified:
"Expressed in the vascular smooth muscle of coronary artery."
[file:human/ARHGEF15/ARHGEF15-uniprot.txt].

### Neuron — where the substrate claim was made, and where it was later revised

PMID:21029865 (Margolis et al. 2010, Cell) is the paper the mouse ISS and Ensembl rows come
from, and **affinage did not return it** — its title names EphB and `Ephexin5`, never
ARHGEF15. It reports the substrate panel, with Ephexin1 as the positive control for Rac1 and
Cdc42 in the same GST-PBD pulldown:
"We conclude that E5 activates RhoA but not Rac1 or Cdc42 (Fig S2A)."
[PMID:21029865]. Critically, the RhoA assignment was **prompted by a sequence criterion, not
discovered by assay**:
"Structure-function studies of GEFs identified amino acid residues in the activation domain of Rho family GEFs that specifically identify the GEFs as activators of RhoA rather than Rac or Cdc42."
[PMID:21029865]. The same criterion produced the GEF-dead control:
"we mutated these three conserved amino acids (L562, Q566, and R567) to alanine (E5-LQR)"
[PMID:21029865]. The paper also establishes the EphB2 phosphosite, in its own section
heading:
"EphB mediates phosphorylation of Ephexin5 at tyrosine-361"
[PMID:21029865].

PMID:40138406 (Petshow et al. 2025, Sci Adv) revises the substrate claim in the same system,
and affinage missed this one too:
"Here, we show that Ephexin5 activates both RhoA and Cdc42 in the brain."
[PMID:40138406], with
"The selectivity of Ephexin5 for Cdc42 activation is regulated by tyrosine phosphorylation, which is regulated by neuronal activity."
[PMID:40138406]. The switch is the residue Margolis identified:
"a mutation of a key tyrosine residue on E5, Y361, enhances E5-dependent activation of Cdc42"
[PMID:40138406]. They use Margolis's own construct as their GEF-dead control for Cdc42 —
"either E5WT, E5Y361F, or GEF-dead E5 (E5LQR)"
[PMID:40138406] — which is what makes the triad exchange machinery rather than a substrate
selector.

PMID:28185854 (Hamilton et al. 2017) grounds the mouse synapse rows that Ensembl Compara
projects into human:
"We found that reducing Ephexin5 levels increased spine outgrowth, and increasing Ephexin5 levels decreased spine outgrowth in a GEF-dependent manner, suggesting that Ephexin5 acts as an inhibitor of spine outgrowth."
[PMID:28185854].

### Disease — including the one measurement on the human protein outside PMID:12775584

PMID:36929019 (Ding et al. 2023, Acta Neuropathol) established BSVD5:
"In vitro experiments indicated that ARHGEF15 mutations resulted in RhoA/ROCK2 inactivation-induced F-actin cytoskeleton disorganization in vascular smooth muscle cells and endothelial cells and osteoblast dysfunction by inhibiting the Wnt/β-catenin signaling pathway in osteoblast cells."
[PMID:36929019]. UniProt additionally records from this paper that the protein
"Does not activate RAC1 or CDC42"
[file:human/ARHGEF15/ARHGEF15-uniprot.txt] — a statement in the full text, not the abstract;
the cache is abstract-only, so I do not second-guess it.

PMID:23647072 (Veeramah et al. 2013, Epilepsia) is in UniProt's reference list but **absent
from GOA entirely**, and it contains a direct assay on the **human** protein:
"We find that RhoA activation by R604C is reduced by ~46% compared to WT (Figure 3A)."
[PMID:23647072]. It also states the human-to-mouse residue correspondence that the alignment
here recomputes independently:
"We also find that a homologous amino acid in mouse Ephexin5 at Arg612Cys (R612C) shows a ~47% reduction as compared with mouse WT protein (Figure 3B)."
[PMID:23647072]. This paper cannot be added as a `NEW` row, because `GO:0005085` is already
in GOA and `NEW` is rejected for a term already present; it is cited as supporting evidence
on the rows that exist.

## Bioinformatics (`ARHGEF15-bioinformatics/RESULTS.md`)

1. **Every published functional residue is retained in the human protein.** Mouse
   L562/Q566/R567 map to human **L554/Q558/R559** and mouse Y361 to human **Y353**, which is
   the residue UniProt already annotates as the EphB2 site by similarity. The three
   disease/uncertain variants map cleanly to mouse (R21→R21, V360→**V368**, R604→**R612**)
   and all lie outside the DH domain. The V360/V368 mapping resolves the apparent mismatch
   between UniProt's human V360M and the paper's mouse `Arhgef15-e(V368M)` line, and the
   R604/R612 mapping is confirmed independently by PMID:23647072's own sentence quoted above.
2. **The triad does not discriminate substrate in a twelve-protein panel.** 0/3
   RhoA-specific GEFs (p115RhoGEF, PDZ-RhoGEF, LARG) carry it; 2/3 Cdc42-specific GEFs
   (FGD1, ITSN1) do. Q and R are near-invariant across all twelve DH domains, so only the
   first column discriminates at all, and there human Ephexin5 groups with the Cdc42-specific
   GEFs. Summary sentence from the results file:
   "The signature points the wrong way in this panel."
   [file:human/ARHGEF15/ARHGEF15-bioinformatics/RESULTS.md]

   This is not a refutation of Margolis et al., whose comparison set was structure-based and
   different; it is a failure to reproduce the discrimination, which is enough to stop the
   residues being used to infer human substrate specificity. Residue identity and measured
   substrate are decoupled here in **both** directions: retention does not establish activity,
   and the signature does not establish specificity.

## Ontology limitation (cross-checked on QuickGO **and** OLS4)

`GO:0005089 Rho guanyl-nucleotide exchange factor activity` no longer exists as a term. It,
together with `GO:0005086` (ARF), `GO:0005087` (Ran), `GO:0005088` (Ras) and `GO:0008321`
(Ral), has been **merged into `GO:0005085`** — agreed by both services, zero disagreements.
`GO:0005085` has zero `is_a` children; the substrate names survive only as synonyms of the
general term. This mirrors the GAP side exactly, where GO:0005097/0005099/0005100/0008060
merged into `GO:0005096` (verified the same way, both services).

Two services were used because neither is reliable alone: QuickGO silently returns the
*successor's* record for a merged id, so its `isObsolete: false` is ambiguous between
"current" and "merged away", while OLS4 reports `is_obsolete` and `term_replaced_by` against
the id actually requested.

The **biological-process** branch was not flattened: `GO:0007266`, `GO:0032488`, `GO:0035023`,
`GO:0035025`, `GO:0032489`, `GO:0035020` and `GO:0035022` are all current on both services.
Substrate identity is therefore expressible for this gene only as a BP statement, with two
caveats that matter here:

- `GO:0032488 Cdc42 protein signal transduction` is an `is_a` descendant of `GO:0007266 Rho
  protein signal transduction`, so `GO:0035025` — which ARHGEF15 already carries — is
  satisfied by activating either RhoA or Cdc42 and does not distinguish them.
- `GO:0032489 regulation of Cdc42 protein signal transduction` has **zero children on both
  services**: there is no *positive* regulation of Cdc42 signal transduction term, while Rho
  and Rac both have signed children. A sibling ephexin already sits on the unsigned parent —
  ARHGEF16/Ephexin4 (`Q5VV41`) carries `GO:0032489` by IDA (PMID:21139582) and by IBA from
  `PANTHER:PTN002656172`, a *different* PAINT node from ARHGEF15's `PTN002656129`. PAINT has
  therefore already judged the Cdc42 link to be Ephexin4-specific, and PMID:40138406 is new
  information for that judgement, in mouse.

## Provider assessment (affinage)

`self_evaluation_pairwise: win`, 11 citations, trust gates clear — and the gates are a
**precision** statement only. The report missed three of the papers this review turns on:

- **PMID:21029865** — the Cell paper behind every mouse-derived GO row and the source of the
  RhoA-specificity claim, the triad and the GEF-dead mutant. Titled for EphB and `Ephexin5`.
- **PMID:40138406** — the 2025 Sci Adv paper that revises the substrate claim to RhoA **and**
  Cdc42.
- **PMID:28185854** — the paper grounding the mouse postsynapse, glutamatergic synapse and
  regulation-of-postsynapse-assembly rows that Ensembl projects into human.
- **PMID:32203420** — the family-wide specificity screen that measures the substrate range
  directly. Titled for RAC1 and integrin adhesions.

The first three are reachable by searching the alias `Ephexin5` rather than the HGNC symbol,
the same recall failure already recorded for ADGB, ADAMTSL1 and ACTG2. The fourth is not
reachable by any gene-name search at all, because the gene is named nowhere in the title,
abstract or PMC-indexed text — only in a supplementary spreadsheet. It was found by
following a citation out of the **cached Reactome entry** for a GOA TAS row, which is worth
recording as a retrieval route: the TAS rows other reviews treat as low-value provenance
were the only pointer to the best measurement available for this gene.

What affinage did contribute that nothing else surfaced: the endothelial Cdc42/RhoJ
literature (PMID:23029280) and the Sertoli-cell work, neither of which is in GOA. Its
`mechanism_profile` GO grounding is empty for molecular activity and localization, so nothing
was imported from it.

## Decisions taken

- **MF.** All `GO:0005085` rows accepted. The activity is real, measured on the human protein
  in two independent transfected-cell assays (PMID:12775584 IDA; PMID:23647072, not in GOA),
  and the exchange machinery is intact. Substrate identity is carried in
  `core_functions[].substrates` and in `RO:0002233 has_input` extensions, because GO's MF
  branch cannot carry it.
- **`GO:0005515` protein binding.** Eight IPI rows. Seven come from binary-interactome
  screens across five distinct partners (PIN1, LASP1, CEP55 x3, PRKG1, GORASP2;
  PMID:25416956, PMID:26871637, PMID:32296183) and are `REMOVE`. My first pass used
  `MARK_AS_OVER_ANNOTATED` and argued that a reproducible screen hit is not a refuted
  finding; `.claude/skills/annotation-reviewer/SKILL.md:187-199` forbids that action for this
  term and pre-empts that argument in its final clause. The problem with a bare `GO:0005515`
  is that it carries no functional information, not that it overstates the evidence, so the
  policy routes to `MODIFY` when the paper supports a better MF and otherwise to `REMOVE` —
  and removal says the annotation is uninformative, not that the interaction is false. The
  five partners are named in `suggested_questions` so the removals do not lose them. The
  eighth row, EPHA4 (PMID:12775584), is the `MODIFY` branch of the same policy:
  `GO:0046875 ephrin receptor binding`, the receptor-coupling step, a term NGEF/Ephexin1
  already carries for the same role.
- **Neuronal rows.** Kept as non-core. Every one traces to a mouse experiment
  (PMID:21029865, PMID:28185854) with no human measurement, while the human tissue evidence is
  vascular and adipose. `KEEP_AS_NON_CORE` is the honest position: the mouse evidence is
  strong and the human relevance is unestablished.
- **No `NEW` rows.** Everything the missed literature adds is either already covered by an
  existing term (`GO:0005085`, `GO:0035025`, `GO:0032956`) or inexpressible — there is no
  positive-regulation-of-Cdc42 term. The Cdc42 evidence is mouse brain and mouse retina plus
  one human knockdown; that is a knowledge gap and a `suggested_questions` item, not an
  assertion.
