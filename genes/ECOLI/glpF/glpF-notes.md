# glpF notes

E. coli `glpF` encodes an inner-membrane aquaglyceroporin/glycerol facilitator
that conducts glycerol through a passive pore. The crystal structure placed
glycerol molecules in single file in the GlpF channel and showed three and a
half membrane-spanning helices in each repeat [PMID:11039922, "We report the
crystal structure of the Escherichia coli glycerol facilitator (GlpF) with its
primary permeant substrate glycerol"]. A follow-up structure modeled GlpF with
bound water and explained the aquaporin-family selectivity architecture
[PMID:11964478, "We have determined the structure of the Escherichia coli
aquaglyceroporin GlpF with bound water"].

Classic E. coli genetics and transport work supports the GO biological-process
annotation to glycerol transmembrane transport: wild-type cells have an
inducible system that "catalyzes facilitated diffusion of glycerol into the
cell", and `glpF+` improves growth at millimolar glycerol independently of the
ATP-dependent glycerol kinase GlpK [PMID:4563976].

Substrate-specificity assays showed that the E. coli glycerol facilitator
passes glycerol and some related small uncharged solutes but not analogous
sugars, and the temperature-insensitive xylitol transport led Heller et al. to
conclude that "the facilitator behaves as a membrane channel" [PMID:6998951].
Abrami et al. used GlpF-injected Xenopus oocytes in glycerol-flux inhibitor
assays and showed phloretin inhibition of glycerol uptake through GlpF
[PMID:8584435]. The PMID:8584435 GOA NOT rows for water-channel activity and
water transport are in tension with later structures that place ordered water in
the pore, while the cached Abrami abstract does not show the underlying water
assay, so they are left UNDECIDED pending a full-text recheck.

The `GO:0071288 cellular response to mercury ion` row from PMID:8584435 should
be removed. The evidence is an inhibitor experiment with
p-chloromercuribenzene sulphonate in oocyte glycerol-flux assays, not evidence
that GlpF performs an E. coli cellular mercury-response process.

## 2026-11-03 review completion

- No deep-research provider file exists for this gene; the review rests on the
  cached PubMed records (all abstract-only), the UniProt record and the PAINT
  file for PTHR43829 (node PTN000440994 carries the GO:0005886, GO:0015254 and
  GO:0015793 IBDs, with P0AER0 as a seed).
- NOT water rows (GO:0005372, GO:0006833; PMID:8584435) changed from UNDECIDED
  to REMOVE, with source_defects (UNIPROT, CHECK). UniProt's own curated
  FUNCTION text says GlpF is "less well permeated by water (PubMed:11226336)",
  the structure/MD paper shows a water single file and a mutant with increased
  water permeability [PMID:11964478 "an increased water permeability for the
  W48F/F200T mutant"], and the PubMed abstract of PMID:11226336 (not cached;
  checked on PubMed) reports purified GlpF raising proteoliposome water
  permeability up to 10-fold. A positive water-channel term was not proposed;
  recorded as a suggested question.
- Generic InterPro2GO rows (channel activity, membrane, transmembrane
  transport) changed from MARK_AS_OVER_ANNOTATED to MODIFY toward GO:0015254,
  GO:0005886 and GO:0015793. GO:0015168 rows stay MODIFY to GO:0015254.
- GO:0071288 cellular response to mercury ion kept as REMOVE; added a
  WRONG_TERM source defect (UNIPROT).
- Every row now has verbatim supported_by quotes; status set to COMPLETE.

## 2026-11-04 (PR #5936 review follow-up)

- Cached PMID:11226336 (abstract). Its proteoliposome result (water permeability up to 10-fold over control liposomes) and the UniProt FT MUTAGEN 236..237 PL->FW quote (no detectable water or glycerol permeability; ECO:0000269 PubMed:11226336) now support both NOT-water REMOVE rows. The same weak-but-measurable water conduction is why the PTHR43829 family review withholds water channel activity from bacterial GlpF members.


## 2026-11-07 comparative glycerol audit

Rechecked all 21 rows, including both negated water claims. Later purified reconstitution contradicts absence of water permeation, even though glycerol transport is the physiological core. Retained the supported glycerol/channel/topology refinements. The mercury-response IDA is now UNDECIDED: the accessible PMID8584435 abstract does not expose the target mercury experiment, and reagent sensitivity alone does not settle functional participation in a cellular response. Removed reasoning based on inert source qualifiers. No positive water or metalloid assertion was manufactured.

Default Falcon attempted via normal workflow and failed HTTP403 authentication; no provider output was fabricated. All original ordered annotation payloads are preserved, with no new GO rows. Focused validation, source preservation, and helper-history results are recorded in analysis/module_audits/bacterial_glycerol_uptake_catabolism/existing-member-consultation/. COMPLETE denotes completed adjudication, including explicit unresolved claims.


## PR6162 review follow-up (2026-11-07 UTC)

Reassessed mercury response against the current GO definition and publisher abstract. Channel inhibition alone does not prove a cellular-response role; the specific full experiment remains inaccessible, so UNDECIDED is retained without a categorical source-defect claim.

Original ordered annotation payloads, raw/provider/publication bytes and historical NEW assertions are preserved. No new GO row was added.
