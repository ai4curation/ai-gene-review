# E. coli Lol consultation, 2026-11-07

Reviewed five existing K-12 records: LolA P61316, LolB P61320, LolC P0ADC3,
LolD P75957 and LolE P75958. All 91 ordered annotation payloads are retained.
There were no historical NEW rows in these five records, and none are added,
removed or retired. Root's wider panel contains historical proposals belonging
to other records. Original qualifiers are unchanged and do not determine these
judgments. The baseline predates edits; `check_preservation.py` regenerates the
payload/source proof and action ledger.

## Primary evidence and limits

- **PMID10783239**, cached abstract: reconstituted E. coli LolCDE releases
  lipoproteins from membranes into LolA. The abstract explicitly distinguishes
  this from transmembrane substrate transport. **PMID11844772**, full cached
  text, Results and Discussion: conditional depletion blocks release and
  mislocalizes mature lipoproteins while leaving precursor translocation and
  processing intact. LolC and LolE are both required in that cellular system.
- **PMID17038124**, cached abstract: liganded LolCDE binds ATP with increased
  affinity; ATP binding weakens cargo contacts, whereas release from membranes
  requires hydrolysis. **PMID17509078**, cached abstract: isolated LolD ATPase
  and reconstitution establish positive ATP hydrolysis; LolD/LolE alone can
  reconstitute release in the reported in vitro system. This is not evidence
  that LolC is dispensable in ordinary cells. Publisher DOI full-text attempts
  for these papers were inaccessible; no extra methods are inferred.
- **PMID30012603**, full cached Results: the LolC periplasmic domain recruits
  LolA through Hook/Pad contacts; direct binding and functional perturbation
  support the recruitment subfunction. This is positive evidence of part of
  the release cycle, rather than a claim that binding alone proves an entire
  molecular function. **PMID19809197**, cached abstract: PhoA topology maps four
  membrane spans and a large periplasmic region in both LolC and LolE.
- **PMID41557797**, full cached Results/Discussion/Fig. 7: E. coli substrate
  structures contain joint LolC/LolE lipid-binding pockets, and a LolE cleft
  contacts a short segment of the cargo peptide. Do not turn the older
  Pal-crosslink preference for LolE (**PMID23187171**, abstract) into exclusive
  cargo binding by LolE. The ATP-dependent pivot/rotation and hydrolysis-reset
  sequence is a structural model; the wording preserves that epistemic limit.
  Both C and E contribute to the complete recognition/release activity.
- **PMID7628437**, cached abstract, and **PMID19307584**, full cached Results:
  purified periplasmic LolA carries lipidated cargo; cargo-binding and
  LolA/LolB cavity-contact experiments support loading/unloading. The 2009
  paper uses a soluble anchorless LolB derivative, which is not a native
  soluble localization. **PMID9384574**, cached abstract: native LolB is
  lipid-modified and outer-membrane localized; depleted membranes fail to
  incorporate Lpp, and soluble LolB accepts cargo from LolA. **PMID19716823**,
  cached abstract, directly measures cargo-transfer kinetics. PMC full-text
  attempts for the 1995/1997 papers returned browser challenges; the accessible
  abstracts make the retained positive claims explicitly.
- **PMID28416660**, new normal cache remains abstract-only. Independently
  acquired and read full PMC5422772 HTML at
  https://pmc.ncbi.nlm.nih.gov/articles/PMC5422772/?report=xml . The full text,
  response bytes and hashes are in the ignored consultation cache. Results and
  Discussion demonstrate a conditional LolAB bypass while LolCDE remains
  needed. This modifies an absolute essentiality statement, not the normal
  carrier/insertion functions, and does not establish generic wild-type
  dispensability or define an alternative molecular route. No bypass protocol
  is proposed here.
- **PMID11758943**, newly fetched abstract: a publication-linked UniProt
  suggestion of Rcs regulation rests on multicopy-induced signaling. This
  does not establish a direct native LolA regulatory activity. No process NEW
  is added. Transport is supported by the independent primary transport
  studies, not by this reference's appearance on a UniProt FUNCTION statement.
- Four proteomics/topology surveys (**15911532, 24140104, 17309111, 15919996**)
  are abstract-only; target tables were not re-extracted. Their source rows
  remain, but generic methods quotations are replaced with independent
  target-specific localization evidence. This avoids pretending that a broad
  proteome summary itself proves localization of the named target.

## Annotation and core decisions

1. **LolD ATP binding: two KEEP_AS_NON_CORE -> ACCEPT.** Binding is central to
   the measured nucleotide-dependent cycle, not peripheral merely because
   ATP hydrolysis is more informative. Existing ATPase core remains; no
   redundant binding core or NEW annotation is needed.
2. **LolB outer membrane: ACCEPT -> MODIFY GO0031241.** The lipid anchor and
   periplasm-facing domain support the already represented more specific
   location. The other periplasmic row already refines to the same location.
3. **LolC and LolE cores: contributes_to GO0140306.** Fresh QuickGO explicitly
   defines recognition and release mediated by the LolCDE complex. Joint
   substrate pockets, LolC carrier recruitment, LolE peptide contact and LolD
   ATPase coupling establish complementary subfunctions. The reasoning is
   positive division of labor, not the absence of isolated-subunit assays.
   Original annotation payloads and actions remain unchanged.
4. **LolC periplasmic compartment remains ACCEPT.** The exposed functional
   region is established by topology and structure, alongside the inner-
   membrane location. Removed the curator-authored qualifier-only source
   defect and old unrelated-gene precedent. No machine qualifier is edited.
5. **LolD GO0055085 REMOVE remains.** Extraction from the periplasmic leaflet
   is not transbilayer transport. An established type VII ABC complex remains
   a legitimate ABC-complex identity despite the generic GO0043190 definition
   describing the typical pore architecture. Family PTHR24220 judgments must
   preserve this member-specific mechanistic distinction; root owns families.
6. **LolB insertion NTR retained.** Current GO0140598 carrier activity specifies
   moving with cargo, while GO0140306 specifies inner-membrane release.
   Neither expresses LolB insertion; QuickGO search found no exact existing
   insertion MF. The proposal is already linked to the LolB core, with no new
   annotation row. No generic binding-only evidence is used to invent it.
7. **LolB PMID1052496 defect retained.** Its immutable cached record is the
   unrelated clinical paper "Ketotic hypoglycaemia". The biological annotation
   remains supported by independent LolB experiments. The intended replacement
   reference is still unresolved; no original reference identifier is changed.

## Research, validation and preservation

Five actual `just deep-research ECOLI <gene> --provider falcon` attempts returned
HTTP403 authentication errors. No provider artifact was manufactured. Logs are
under `.cache/module-audit-logs/lol-20261107/ecoli-consultation/`.

Fresh official QuickGO JSON for the relevant terms and insertion search is
archived there. Ontology interpretation and source access are recorded in
`source-provenance.json`. No original publication, GOA, UniProt or provider
bytes are rewritten. New publications 28416660 and 11758943 were acquired via
normal `ai-gene-review fetch-pmid` only.

PAINT loss checks find no lineage IRD/IKR for LolA/C/D/E. LolB has no PANTHER
family in its source record, so the helper cannot assess its lineage; this is
not reported as a verified absence of losses. Each changed review is validated
and rendered; append-only histories are generated with `just new-history`.
The final receipt records check outcomes and the frozen handoff hashes.
