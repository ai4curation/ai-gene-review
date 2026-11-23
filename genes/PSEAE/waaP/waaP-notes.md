# waaP (PA5009, Q9HUF7) — review notes

Tier-3 PseudoCAP review. `waaP` was added to batch 5 as an LPS gene carrying `GO:0016301
kinase activity`, the most general kinase term there is, and it turned out to be the
"measured activity is not automatically function" case plus an ontology gap.

## The gene

Swiss-Prot **reviewed** (WAAP_PSEAE, 268 aa), unusually richly curated — the record carries
`ACTIVITY REGULATION`, `BIOPHYSICOCHEMICAL PROPERTIES`, `COFACTOR`, `DISRUPTION PHENOTYPE`,
`DOMAIN`, `MASS SPECTROMETRY`, `PATHWAY`, `SUBUNIT` and two EC numbers.

`[file:PSEAE/waaP/waaP-uniprot.txt "Kinase involved in the biosynthesis of the core oligosaccharide region of lipopolysaccharide (LPS)"]`
`[file:PSEAE/waaP/waaP-uniprot.txt "Catalyzes the phosphorylation of heptose I (HepI), the first heptose added to the Kdo2-lipid A module"]`

That reaction is `EC=2.7.1.235 {ECO:0000269|PubMed:11741974}`, and it is essential:
the disruption phenotype is *"Lack of viability"*, with WaaP depletion producing LPS lacking
core sugars and all core phosphates. Family: `KdkA/RfaP`, signature
`[file:PSEAE/waaP/waaP-uniprot.txt "DR   InterPro; IPR017172; Lsacc_core_hep_kinase_RfaP."]`

## Two activities, and only one of them is the function

The same curated `FUNCTION` continues:

`[file:PSEAE/waaP/waaP-uniprot.txt "Also has protein-tyrosine kinase activity: autophosphorylates on all Tyr residues; in vitro can phosphorylate poly(Glu,Tyr)"]`

carrying `EC=2.7.10.2`. The naming paper puts both in its title — "WaaP of Pseudomonas
aeruginosa is a novel eukaryotic type protein-tyrosine kinase **as well as** a sugar kinase
essential for the biosynthesis of core lipopolysaccharide" (PMID:11741974).

So the protein-tyrosine kinase activity is real and curator-accepted, not something to dispute.
But what the evidence amounts to is **autophosphorylation** plus phosphorylation of
**poly(Glu,Tyr)**, a generic artificial substrate. No physiological protein substrate is
identified, autophosphorylation is common among kinases and does not establish a protein-kinase
function, and the activity that is *essential* — the one whose loss kills the cell — is the
sugar kinase.

That places it exactly in the middle tier of the project's promiscuous-activity rule: a genuine
secondary activity would be `KEEP_AS_NON_CORE`, noise-level paralog activity would be `REMOVE`,
and **real in vitro activity of unknown relevance is `MARK_AS_OVER_ANNOTATED`**. The rule says
explicitly that this tiering applies even on a direct-evidence row, so the `EXP` code does not
change it.

Applied to both rows that assert it, for consistency:

- `GO:0004713 protein tyrosine kinase activity` (EXP, IEA) → `MARK_AS_OVER_ANNOTATED`
- `GO:0004715 non-membrane spanning protein tyrosine kinase activity` (IEA from `EC:2.7.10.2`)
  → `MARK_AS_OVER_ANNOTATED`; verified in OLS as a child of `GO:0004713`, so the same judgement
  has to cover it.

No EC-class conflict arises from keeping these marked rather than removed: `EC 2.7.10.2` is on
the record, so the `ec_class_conflict` check has nothing to fire on.

## An ontology gap: the physiological activity has no GO term

`GO:0016301 kinase activity` is as general as the kinase branch gets — it does not say what is
phosphorylated. The specific activity is EC 2.7.1.235, phosphorylation of heptose I within the
assembled Kdo2-lipid A core. **GO has no term for it.** Searched in OLS:

- `GO:0033785 heptose 7-phosphate kinase activity` is a *different* reaction — D-glycero-D-manno-heptose
  7-phosphate to the 1,7-bisphosphate, a step of nucleotide-sugar synthesis (HldE/GmhB),
  not phosphorylation of a heptose already incorporated into LPS.
- No "lipopolysaccharide heptose kinase" or "lipopolysaccharide core kinase" term exists, and a
  QuickGO text search returns only unrelated or upstream terms (`GO:0033786`
  heptose-1-phosphate adenylyltransferase, `GO:0008713` ADP-heptose-LPS heptosyltransferase,
  `GO:0008712` ADP-glyceromanno-heptose 6-epimerase).

So the four `GO:0016301` rows are `MODIFY`ed with an `NTR` replacement and a top-level
`proposed_new_terms` entry, which is the mechanism the project rules prescribe when a core
activity has no term: the `core_functions` entry sets `proposed_molecular_function` and leaves
`molecular_function` unset.

All four rows take the same action, as rows sharing a term must. The IEA row's own evidence is
`IPR017172`, the WaaP/RfaP family signature, which is substrate-specific, so even that row's
evidence reaches the proposed activity rather than stopping at "kinase".

## Routine calls

- `GO:0009244 lipopolysaccharide core region biosynthetic process` (IDA, IEA, IMP) → `ACCEPT`,
  core process. Participation, not necessity: WaaP performs the phosphorylation step.
- `GO:0009103 lipopolysaccharide biosynthetic process` (IEA) → `TOO_GENERAL`. `GO:0009244` is a
  descendant (verified in OLS) and is accepted here, and "LPS biosynthesis" does not say which
  part — lipid A, core or O antigen. This is the same call batch 4 made for `wbpX`/`wbpY` on
  this exact term, which is the point of keeping the two consistent.
- `GO:0005737 cytoplasm` (EXP, IEA) → `ACCEPT`. Fits the biology: core phosphorylation happens
  on the cytoplasmic face before the molecule is flipped and exported.
