# pcrB (yerE; BSU06600; O34790) notes

## Provenance of this review

- No deep-research provider key was available, so no
  `pcrB-deep-research-*.md` file exists.
- `just mod-description-deep-research BACSU pcrB` was run and skipped:
  "no MOD provider configured for organism 'BACSU'".
- PubMed search via MCP (2026-11-02):
  `(heptaprenylglyceryl OR PcrB OR AraM OR "glycerol-1-phosphate dehydrogenase") AND Bacillus`
  gave 11 hits; relevant: PMID:22614947, PMID:23322418, PMID:27226549,
  PMID:40626731, PMID:35767906, PMID:18558723. Also read PMID:21761520,
  PMID:24684232, PMID:21214173 (full text) and PMID:23322418 (full text).
- PMID:21761520 (Guldan 2011, source of the IDA rows) and PMID:24684232
  (source of the EXP row) are abstract-only in the cache.

## Activity

- HepGP synthase: transfers heptaprenyl (C35) from HepPP to the C3 hydroxyl of
  sn-G1P, forming an ether bond [PMID:21761520 "PcrB, the bacterial homologue
  of the archaea-specific geranylgeranylglyceryl phosphate synthase, produces
  heptaprenylglyceryl phosphate in bacillales"]. Group I GGGPS-family enzymes
  are HepGP synthases, group II are GGGP synthases [PMID:24684232].
- Acceptor strictly G1P, not G3P or 3PG; C10 and C20 donors are also used in
  vitro, FPP poorly [PMID:21214173 "PcrB uses G1P (1) exclusively as an
  acceptor"]. The native donor is C35 HepPP; dimerisation is needed to accept
  the long chain [PMID:22614947].
- Mg2+ is required: no product with EDTA or without MgCl2 [PMID:23322418 "No
  product was found, indicating that Mg2+ is likely essential for catalysis."].
- Crystal structures with bound G1P (3VZY, 3W00) [PMID:23322418].
- The C10/C20 use is in vitro substrate range for a C35 enzyme; not
  annotated separately (no GOA rows for it anyway).

## In vivo fate and physiological role of the product

- HepGP is dephosphorylated (by PhoB or another non-specific phosphatase) and
  acetylated by YvoF to HepG and Ac-HepG [PMID:21761520; PMID:27226549].
  These are minor lipids; the pathway does not build a bulk archaeal-type
  membrane lipid (no second prenyl chain is added) [PMID:27226549 "In
  Bacillales, heptaprenylglyceryl phosphate does not become linked to a second
  polyprenyl moiety like ether lipids in Archaea but is dephosphorylated and
  acetylated."].
- Physiological role (Komazin 2025, PMID:40626731, full text): Ac-HepG is the
  acetyl donor for N-terminal acetylation of lipoproteins by the membrane
  enzyme LhaT (YpjA). Deletion of pcrB, yvoF or ypjA abolished lipoprotein
  N-acetylation (loss of 42 Da on the FrxB N-terminal peptide) and back
  complementation restored it; the pathway was reconstituted in vitro with
  PcrB, phosphatase, YvoF and LhaT [PMID:40626731 "Only pcrB, yvoF, and ypjA
  fully suppressed TLR2 activity, indicating these genes are strictly
  required for Ac-LP synthesis."]. The authors argue for a carrier role
  rather than a structural membrane lipid role [PMID:40626731 "A catalytic
  role as a transient carrier for acetyl groups, as opposed to being a
  structural membrane building block for an archeal-type lipid with
  ether-linked isoprenoid chains, is more consistent with the low overall
  abundance of HepG/Ac-HepG observed in B. subtilis membranes (28)."].
- Open: how Ac-HepG/HepG crosses the membrane; whether HepG is recycled; other
  roles of Ac-HepG, since PcrB is more widely distributed than LhaT
  [PMID:40626731].
- Substrate supply: G1P from EgsA (AraM) is the presumed source, but I found no
  accessible data from an egsA mutant on HepG levels. The egsA gene was not
  among the reported Tn-screen hits for lipoprotein N-acetylation
  [PMID:40626731] (my reading of the hit list, not a claim of the paper).

## GO term choices

- GO:0120536 HepGP synthase activity: core MF; EXP/IDA/IEA all ACCEPT.
- GO:0004659 prenyltransferase (IBA, IEA) and GO:0016765 (IEA): correct
  parents of GO:0120536; MODIFY to GO:0120536.
- GO:0046474 glycerophospholipid biosynthetic process (IBA, IDA, IEA) and
  GO:0006650 (IEA): HepGP is formally a glycerophospholipid (O-alkyl
  glycerophosphate), but it is a transient intermediate; the in vivo
  products HepG/Ac-HepG are neutral glycerol ether lipids. GO:0008611 ether
  lipid biosynthetic process (definition: one lipid alcohol in ether
  linkage to glycerol) describes the pathway PcrB actually catalyses (it
  forms the ether bond). MODIFY all to GO:0008611.
- GO:0000287 magnesium ion binding: KEEP_AS_NON_CORE (catalytic cofactor).
- NEW GO:0042158 lipoprotein biosynthetic process (IMP, PMID:40626731):
  PcrB makes the carrier that supplies the acetyl group for lipoprotein
  N-acetylation (cofactor/carrier case). Comparator check (QuickGO,
  2026-11-02): E. coli Lgt (P60955) and Lnt (P23930) carry GO:0042158 (IMP,
  IDA, IBA); E. coli LspA (P00804) does not. For the carrier-synthase
  analogy, E. coli UppS/IspU (P60472), which makes the undecaprenyl carrier,
  carries GO:0009252 peptidoglycan biosynthetic process by IMP. Kept as a
  non-core NEW row.
- No GO term exists for lipoprotein N-acetylation specifically; GO:0006474
  N-terminal protein amino acid acetylation was considered but LhaT, not
  PcrB, performs the transfer.

## Review session 2026-11-06: resolution of the two reviewer critiques

Both open questions from the merged PR review of the plan above were re-tested
before the review was written. Both changed the plan.

### 1. The planned `NEW GO:0042158 lipoprotein biosynthetic process` row: DROPPED

Asked explicitly which entity performs the step. LhaT transfers the acetyl
group to the lipoprotein; the acetyl group itself comes from acetyl-CoA via
YvoF; the HepG carrier is released and reloaded, so PcrB's product contributes
no atom to Ac-LP. PcrB is three steps upstream and supplies a regenerated
cofactor. The Δ*pcrB* result is necessity evidence, which is what being
required for a process looks like whether or not the gene participates in it.

The earlier comparator check was the wrong comparison. Lgt and Lnt modify the
lipoprotein themselves, so they do the work. Re-run against gene products in
the *same role* - enzymes that make a donor or carrier consumed by a
protein-modification process (QuickGO annotation API, biological_process,
2026-11-06):

| Donor/carrier synthase | Consumer modification | Carries the consumer's process term? |
|---|---|---|
| FDPS P14324 (makes FPP) | protein farnesylation | No; isoprenoid/cholesterol biosynthesis only |
| GGPS1 O95749 (makes GGPP) | protein geranylgeranylation | No |
| MAT2A P31153, metK P0A817 (make SAM) | protein/DNA methylation | No; `GO:0006556` only |
| ACLY P53396, ACSS2 Q9NR19 (make acetyl-CoA) | protein acetylation | No |
| bioB P12998, bioF P12999 (make biotin) | protein biotinylation | No; `GO:0009102` only |
| UppS P60472 (makes Und-P) | peptidoglycan biosynthesis | Yes, `GO:0009252` IMP |
| DPM1 O60762 (makes Dol-P-Man) | GPI/O-mannosylation | Yes, `GO:0006506` IDA, `GO:0035269` IDA |

So the two precedents the notes leaned on are the two exceptions, and both
differ from PcrB in the way CLAUDE.md's thyroglobulin/fibrin/C3 cases differ
from angiotensinogen: Und-P and Dol-P-Man are themselves glycosylated
intermediates that carry the growing product, whereas HepG only ferries an
acetyl group it does not contribute. The term is dropped; the reasoning is
recorded as a `suggested_questions` entry asking GO whether the
carrier-synthase exclusion is deliberate practice. This also keeps the gene
consistent with the merged module, which puts `GO:0042158` on the LhaT annoton.

**Correction (2026-11-06, from the PR #6063 review).** DPM1 does not belong in
the table as a counterexample at all. It *charges* the carrier with the group it
donates (GDP-Man to Dol-P-Man), which makes it the analogue of YvoF, not of
PcrB. PcrB builds the carrier *backbone*, so its matched-role comparators are
DHDDS/NUS1 (dolichol), HepS/HepT (the C35 donor PcrB itself consumes) and UppS.
That leaves UppS as the single genuine counterexample, which strengthens the
drop rather than weakening it. The repository already holds the matched-role
precedent: `modules/bacterial_undecaprenyl_phosphate_carrier_supply.yaml` models
UppS with `GO:0016094` polyprenol biosynthetic process alone and no downstream
glycan process. The `suggested_questions` entry was rewritten accordingly.

### 2. `GO:0008611 ether lipid biosynthetic process`: USED, but as an added row, not a replacement

Definition (OLS, 2026-11-06): "lipids that contain (normally) one lipid alcohol
in ether linkage to one of the carbon atoms (normally C-1) of glycerol."

The C-3 objection dissolves on inspection. In HepGP the ether is on the
glycerol carbon *distal to the phosphate*. That is the same physical position
as C-1 in the mirror-image sn-glycerol-3-phosphate numbering used for
plasmanyl/plasmenyl lipids; the number differs only because sn numbering is
fixed by backbone stereochemistry. The two hedged "normally" clauses cover
exactly this. UniProt independently calls the reaction an ether-bond-formation
step, and the family survey states the family forms "an ether bond between
glycerol-1-phosphate and polyprenyl diphosphates" [PMID:24684232]. No new term
is needed for ether-bond formation as such.

But the planned MODIFY was wrong on a different ground, which the plan had not
checked: `GO:0008611` is **not** a descendant of `GO:0046474`. Its parents are
`GO:0008610` lipid biosynthetic process, `GO:0046485` ether lipid metabolic
process and `GO:0046504` glycerol ether biosynthetic process (OLS). Replacing
`GO:0046474` with it would therefore *discard* a true claim (HepGP is a
glycerophospholipid; UniProt's PATHWAY line says so) rather than refine it.

Comparator check on the process term (QuickGO + UniProt REST, 2026-11-06):

- `GO:0008611` has ~5192 annotations; a `taxonId` query returns **0** in
  Archaea (NCBITaxon:2157) and **0** in Bacillota (NCBITaxon:1239). Every one
  sampled is a eukaryotic plasmalogen enzyme (GNPAT, AGPS and orthologues).
- Every reviewed archaeal GGGPS (P0C882, O26652, O29844, Q9HSF8, A2BIS8,
  A3CTK2, A3DN81, A5UJF1, A8A9K6, Q2FQM4, A1RRN9, A2SSK1 and others) carries
  `GO:0046474` and none carries `GO:0008611` - these are the enzymes that form
  the identical ether bond on the identical acceptor.
- That absence is *explained*, not conventional: those rows all come from the
  single HAMAP rule MF_00112 (the same rule that annotates PcrB), whose GO
  mapping offers no ether term, and no curator has yet reviewed a prokaryotic
  ether-lipid enzyme. It is not a twenty-year curatorial decision about what
  the term means.

Resolution adopted: `GO:0046474` rows (IBA, IDA, IEA) are **ACCEPT**ed as core,
since no descendant of that term names heptaprenylglyceryl phosphate or any
archaeal-type ether lipid, so the general term is already as precise as the
evidence allows. `GO:0006650` is **MODIFY**ed to `GO:0046474` (parent to the
specific child the gene already carries). `GO:0008611` is added as a **NEW**
row (IDA, PMID:21761520) because it states the one thing the glycerophospholipid
terms do not - that PcrB forms the ether linkage - and PcrB performs that step
itself. This would be the term's first prokaryotic use, which is noted in the
row. The ontology question (clarify the definition; add a child for isoprenoid
or archaeal-type ether lipid biosynthesis) is recorded in
`suggested_questions`, not as `proposed_new_terms`, since the existing term is
usable as written. The module's `GO:0008611` assertion on the PcrB step is
therefore upheld.

### Other decisions

- `GO:0004659` (IBA, IEA) and `GO:0016765` (IEA) MODIFY to `GO:0120536`, as
  planned; all three are ancestors of a term the gene already carries by IDA and
  EXP. The IBA rows carry `propagation_review` blocks; no PAINT slice for
  PTN002219408 is cached locally, so the node was assessed from the donor set
  (all Bacillales group I HepGP synthases: O34790, Q53726 PCRB_STAA8, Q8Y6C8
  PCRB_LISMO, verified against UniProt REST) and the family literature.
- `GO:0120536` (EXP, IDA, IEA) ACCEPT as the core molecular function.
- `GO:0000287` KEEP_AS_NON_CORE, as planned; the Mg2+ requirement is
  experimental [PMID:23322418] but is a catalytic accessory, not the selected
  function.
- Added `NEW GO:0005737 cytoplasm` (IC). The gene had no cellular-component row
  at all; the enzyme is soluble with no TM or signal peptide, both substrates
  are cytoplasmic, PMID:40626731 places the carrier-synthesizing half of the
  pathway in the cytosol, and every reviewed GGGPS family member carries this
  term.
- The in vitro C10/C20 donor range is left unannotated, as planned: the C35
  donor is what the dimer is built for and the C35 product is what accumulates
  in vivo.
