---
title: "Fatty-acyl-CoA Synthase Activity — Proposed Obsoletion of GO:0004321"
maturity: SCOPING
tags: [OBSOLETION]
species: [yeast, SCHPO, rat, mouse, human, PSEPK, METS5, BACSU]
genes: [FAS1, FAS2, fas1, fas2, Acsm4, ACSM4, PP_2213, Msed_0406, ytcI]
autolink_exclude: [FAS]
last_reviewed: 2026-11-02
---

# Fatty-acyl-CoA Synthase Activity — Proposed Obsoletion of GO:0004321

**Bottom line:** `GO:0004321 fatty-acyl-CoA synthase activity` turns EC
2.3.1.86, the fungal fatty acid synthase *system* (a two-chain α6β6
multienzyme), into a single-reaction molecular function that no single gene
product performs. Only about a fifth of its 17,305 annotations are on fungal FAS
subunits. The rest reach acyl-CoA ligases, bacterial polyketide synthases and
unrelated proteins by several independent routes, most of them a
synthase/synthetase or system/reaction confusion. Rhea and Swiss-Prot do not
use the overall reaction, and expert curators already annotate fungal FAS to
the animal system term instead. We propose obsoleting it, together with the
complex term defined only through it, and pointing curators to the component
activities, the FAS complex and the process.
[Draft go-ontology ticket](FATTY_ACYL_COA_SYNTHASE_OBSOLETION/go-ontology-ticket.md).

## Overview

This project began with one wrong annotation. *Pseudomonas putida* PP_2213, an
AMP-forming acyl-CoA synthetase, carried GO:0004321 by TreeGrafter. The trail
led to a PAINT IBD on the PTHR43605 root (PTN001944787), whose only seed is an
RGD IDA on rat Acsm4 from a paper that measured acyl-CoA *synthetase* (ligase)
activity; UniProt curated the same paper to the ligase reactions
(RHEA:48340 and others, GO:0031956). That case is reported as
[geneontology/go-annotation#6642](https://github.com/geneontology/go-annotation/issues/6642)
and reviewed in the PTHR43605 family review
(`interpro/panther/PTHR43605/PTHR43605-review.yaml`).

Auditing every annotation to the term then showed that the problem is the term,
not one seed.

### What the term represents

GO:0004321 is defined from EC 2.3.1.86. IUBMB's accepted name is
"fatty-acyl-CoA synthase system", with "yeast fatty acid synthase" as an
alternative name, and its comment describes the fungal enzyme as "a
multi-functional protein complex composed of two subunits" whose subunits carry
out EC 2.3.1.38, 2.3.1.39, 2.3.1.41, 1.1.1.100, 4.2.1.59, 1.3.1.10 and
1.1.1.279. In the fungal complex "the alpha and beta polypeptide chains form
the six catalytic domains required for fatty acid synthesis"
([PMID:17431175](https://pubmed.ncbi.nlm.nih.gov/17431175/)), and the acyl
carrier domain shuttles intermediates between the active sites
([PMID:17431182](https://pubmed.ncbi.nlm.nih.gov/17431182/)). The EC
equation is the net of that cycle, not a reaction catalysed at one site.

Reaction-level resources treat it that way:

- Rhea has the equation as RHEA:22896, with no EC number linked and no
  UniProtKB entries annotated to it; a Rhea query for ec:2.3.1.86 returns
  nothing.
- Swiss-Prot's S. cerevisiae FAS1 (P07149) and FAS2 (P19097) give the
  2.3.1.86 reaction as free text without a Rhea cross-reference, while every
  partial reaction they list carries one.
- All 30 Swiss-Prot entries with EC 2.3.1.86 are fungal FAS subunits: yeast
  FAS1/FAS2 and the dedicated FAS pairs of fungal secondary metabolism
  (aflatoxin hexA/hexB, sterigmatocystin stcJ/stcK, HC-toxin TOXC/TOXH and
  others).

GO's own definition has also drifted from its source: it has "2n NADH + 2n
NADPH" where the current EC equation uses NADPH only.

## Usage audit

All annotations to GO:0004321 from QuickGO, joined to their UniProtKB entries
(release 2026_03), retrieved 2026-11-01. Reproduce with
[`audit_go0004321.py`](FATTY_ACYL_COA_SYNTHASE_OBSOLETION/audit_go0004321.py);
the output is [`usage_summary.yaml`](FATTY_ACYL_COA_SYNTHASE_OBSOLETION/usage_summary.yaml).

| Annotations | Proteins | Route | Verdict |
|---:|---|---|---|
| 12,690 | PTHR43605 acyl-CoA ligases | PAINT root IBD seeded by RGD Acsm4; IBA, TreeGrafter, ISO, Ensembl | wrong |
| 3,674 | Fungal FAS subunits | EC2GO from UniProt EC 2.3.1.86; UniProt ISS | correct use |
| 10 | Fungal FAS, curated | SGD RCA, PomBase NAS, ComplexPortal IDA | correct use |
| 520 | Bacterial modular PKS and PUFA synthases (*Streptomyces*, Bacteroidetes) | EC2GO; EC 2.3.1.86 added by ARBA00048237 | wrong |
| 163 | Other bacterial acyl-CoA ligases | EC2GO; EC 2.3.1.86 typed by submitters | wrong |
| 39 | Other acyl-CoA ligases | IDA, IMP, ISO; EnsemblPlants projections | probably wrong |
| 83 | Oomycete and other non-fungal FAS-like proteins | EC2GO | uncertain |
| 7 | Unrelated proteins | EC2GO from submitter EC | wrong |
| 119 | Entries not returned by the UniProt query | EC2GO | not resolved |

Three independent routes put the term on proteins that are not fungal FAS:

1. **PAINT.** One IDA confusing synthetase with synthase, placed at the family
   root (go-annotation#6642).
2. **Genome submitters.** EC 2.3.1.86 typed on acyl-CoA ligase records, e.g.
   "Long-chain-fatty-acid--CoA ligase, EC=2.3.1.86" (ECO:0000313).
3. **An ARBA rule.** ARBA00048237 adds the 2.3.1.86 reaction to 4,017
   unreviewed entries. Six of its seven condition sets are limited to fungi,
   eukaryotes or a fungal FAS family; the first (two phosphopantetheinyl
   transferase signatures plus the thiolase-like superfamily) has no taxon or
   family limit, and the *Streptomyces* PKS entries sampled get the EC from
   this rule.

### Expert curation already uses the other system term

SGD (FAS1, FAS2; IMP) and PomBase (fas1, fas2; IDA) annotate fungal FAS to
`GO:0004312 fatty acid synthase activity`, the animal system (EC 2.3.1.85,
which releases free fatty acid), and InterPro2GO maps the fungal FAS families
IPR003965 and IPR026025 to GO:0004312 as well. The EC distinction between the
two systems is not being used.

## Proposal

Obsolete GO:0004321 with no `replaced_by`, and `consider` the component
activities (GO:0004313, GO:0004314, GO:0004315, GO:0004316, GO:0019171,
GO:0141148), the complex (GO:0005835 fatty acid synthase complex) and the
process (GO:0006633 fatty acid biosynthetic process). Obsolete GO:0005836
fatty-acyl-CoA synthase complex, which has no annotations and is defined only
as "a protein complex that possesses fatty-acyl-CoA synthase activity",
`consider` GO:0005835. Retire the EC2GO, Rhea and MetaCyc mappings to the term.

A taxon constraint (only in Fungi) was considered and rejected: a molecular
function term should name a reaction, and the problem is that this one names a
system. Restricting it by taxon would keep the system/reaction conflation and
need its own justification that the net reaction never occurs outside fungi.

One gap: the fungal MPT domain's final transfer of the acyl chain from ACP to
CoA, which makes the product an acyl-CoA, has no specific MF term (SGD uses
the generic GO:0016409 palmitoyltransferase activity).

`GO:0004312 fatty acid synthase activity` (EC 2.3.1.85, "fatty-acid synthase
system") has the same character but is not part of this proposal; in animals
one multifunctional polypeptide performs the whole cycle.

## Upstream tickets

- Annotation ticket: [geneontology/go-annotation#6642](https://github.com/geneontology/go-annotation/issues/6642)
  (PTHR43605 root IBD and the RGD seed)
- Ontology ticket: not yet filed; draft at
  [go-ontology-ticket.md](FATTY_ACYL_COA_SYNTHASE_OBSOLETION/go-ontology-ticket.md)
- Prior discussion: [geneontology/go-ontology#8102](https://github.com/geneontology/go-ontology/issues/8102)
  (2010–2015, closed as out of date: whether the term is a process),
  [geneontology/go-ontology#7662](https://github.com/geneontology/go-ontology/issues/7662)
- To report to UniProt: condition set 1 of ARBA00048237, and submitter EC
  2.3.1.86 on acyl-CoA ligases.

## Impact on this repo

| Review | GO:0004321 rows | Current action | After obsoletion |
|---|---|---|---|
| yeast FAS1 | IEA, RCA ×5 | ACCEPT | migrate to component terms / complex |
| yeast FAS2 | IEA, RCA | ACCEPT | migrate |
| SCHPO fas1 | IEA, NAS | ACCEPT | migrate |
| SCHPO fas2 | IEA | ACCEPT | migrate |
| rat Acsm4, mouse Acsm4, human ACSM4 | IDA, IBA, ISO, IEA | REMOVE | none |
| PSEPK PP_2213, METS5 Msed_0406, BACSU ytcI | IEA, IBA | REMOVE | none |

The four fungal reviews also MODIFY their GO:0004312 rows *to* GO:0004321.
Those replacements would need revisiting. All four already state their core
functions as component activities (for example FAS1: GO:0004314, GO:0004313,
GO:0019171, GO:0141148), so no core function changes.

The module `modules/fatty_acid_de_novo_synthesis.yaml` uses GO:0004321 as the
function of its fungal FAS node, with the component activities as sub-parts,
and its chaining note relies on the term's acyl-CoA product. The S. pombe
GO-CAM (gomodel:678073a900002931) uses it the same way, as the activity of the
FAS complex. That complex-level use is the strongest argument for keeping a
term. The alternative to obsoletion is to redefine it explicitly as the
activity of the fungal type I FAS complex, annotated only with `contributes_to`
on subunits and never to single ligase-like proteins. If GO obsoletes the term
instead, the module node would describe the complex through its parts.

## Status

- 2026-11-02: usage audit and draft ontology ticket written; annotation ticket
  go-annotation#6642 filed.
- Next: file the ontology ticket; report ARBA00048237 to UniProt; revisit the
  fungal FAS reviews once GO decides.
