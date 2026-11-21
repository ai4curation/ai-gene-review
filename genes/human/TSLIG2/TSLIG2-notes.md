# TSLIG2 (ASW / Ashwin / C2orf49, UniProt Q9BVC5) — curation notes

## Provenance of this file

No deep-research provider was reachable in the environment where this review was
started (`just deep-research human Q9BVC5 --alias TSLIG2 --provider perplexity`
exited with "No research providers available" — no `OPENAI_API_KEY`,
`PERPLEXITY_API_KEY`, `ASTA_API_KEY` or `EDISON_API_KEY`). Per `CLAUDE.md` these
notes are therefore hand-written from the cached publications rather than named
`-deep-research-<provider>.md`. If a provider becomes available, a real
deep-research file can be added alongside this one.

## Nomenclature: why the folder is `TSLIG2`

HGNC has renamed this gene and its partners around the tRNA-splicing ligase
complex (tRNA-LC), apparently in the wake of PMID:42754615:

| UniProt | old symbol | HGNC approved symbol | HGNC name |
|---|---|---|---|
| Q9BVC5 | C2orf49 (ASW/Ashwin) | **TSLIG2** (HGNC:28772) | tRNA splicing ligase complex subunit 2 |
| Q8IWT0 | ZBTB8OS (Archease) | TSLIG1 | tRNA splicing ligase complex subunit 1 |
| Q8NCA5 | FAM98A | TSLIG3A | tRNA splicing ligase complex subunit 3A |
| Q52LJ0 | FAM98B | TSLIG3B | tRNA splicing ligase complex subunit 3B |
| Q17RN3 | FAM98C | TSLIG3C | tRNA splicing ligase complex subunit 3C |
| Q9Y3I0 | RTCB | RTCB (unchanged) | RNA 2',3'-cyclic phosphate and 5'-OH ligase |
| Q9Y224 | RTRAF / CGI-99 | RTRAF (unchanged) | RNA transcription, translation and transport factor |
| Q92499 | DDX1 | DDX1 (unchanged) | DEAD-box helicase 1 |

Verified against the HGNC REST API
(`rest.genenames.org/fetch/uniprot_ids/Q9BVC5` → `symbol: TSLIG2`,
`prev_symbol: [C2orf49]`, `alias_symbol: [MGC5509, asw]`).

UniProt has **not** yet adopted the new symbol: Q9BVC5 still carries
`GN Name=C2orf49; Synonyms=ASW;`, and GOA rows are keyed on `C2orf49`.
Consequently `just fetch-gene human TSLIG2` **fails** ("Could not find
Swiss-Prot UniProt ID for gene TSLIG2 in human"). Re-fetch this gene with the
accession plus an alias instead:

```
just fetch-gene human Q9BVC5 --alias TSLIG2
```

The emitted stub takes `gene_symbol` from UniProt, so it says `C2orf49`; the
review sets it to the HGNC symbol `TSLIG2` per `CLAUDE.md` ("For human, should
be HGNC symbols") and keeps `C2orf49`/`ASW`/`Ashwin` in `aliases`.

## What the protein is

232 aa, no catalytic domain, no recognised fold beyond the family-defining
Ashwin region (Pfam PF15323, InterPro IPR024887, PANTHER PTHR28359 "ASHWIN").
UniProt annotates two long disordered regions (113–136 and 157–232,
`ECO:0000256|SAM:MobiDB-lite`) with basic/acidic and basic compositional bias,
and heavy mitotic phosphorylation (Ser-112, Ser-143, Ser-182, Ser-184, Ser-189,
Ser-193, Thr-197, Thr-198). So it is essentially a small, largely disordered,
basic-tailed accessory subunit.

It is the fifth subunit of the metazoan tRNA-splicing ligase complex, alongside
the catalytic subunit RTCB and the accessory DDX1, RTRAF/CGI-99 and FAM98B
[UniProt:Q9BVC5 "Component of the tRNA-splicing ligase core complex composed of
the catalytic subunit RTCB and the accessory proteins DDX1, C2orf49/Ashwin/ASW,
FAM98B and RTRAF/CGI-99."].

## History of the annotations

1. **Identification in the complex (2011).** Activity-guided purification of
   tRNA ligase from HeLa extracts identified HSPC117/RTCB as the essential
   subunit, with ASW among the co-purifying proteins
   [PMID:21311021 "Using activity-guided purification of tRNA ligase from HeLa cell extracts, we identified HSPC117, a member of the UPF0027 (RtcB) family, as the essential subunit of a tRNA ligase complex."].
   This is the source of the `part_of GO:0072669` and `involved_in GO:0006388`
   IDA rows, and of ComplexPortal's CPX-6411 nucleus/cytoplasm NAS rows.
2. **Function still unassigned (2014).** The orthologous-groups paper that found
   Archease and DDX1 states the point explicitly
   [PMID:24870230 "The functions of the additional complex components ASW (also known as C2orf49), CGI-99 (also known as C14orf166), FAM98B and the DEAD-box helicase DDX1 in the context of RNA ligation have remained unclear."].
3. **Nuclear localisation (2008).** The `located_in GO:0005634` IDA is from a
   proteomic screen for nuclear, mitotic microtubule-binding proteins whose
   headline gene is EML3 but which "revealed 50 poorly characterised human gene
   products" [PMID:18445686 "Here, we used a proteomic approach to selectively identify proteins of this category and revealed 50 poorly characterised human gene products, among them the echinoderm microtubule-associated-protein-like gene product, EML3."].
   UniProt cites it as `ECO:0000269|PubMed:18445686` for `SUBCELLULAR LOCATION:
   Nucleus`. The full text is not in our cache, so the specific ASW data are not
   visible here; the conclusion is independently confirmed by PMID:42754615 and
   by HPA immunofluorescence (nucleoplasm), so the row is accepted.

## The 2026 paper: ASW is the nuclear import factor of the tRNA-LC

PMID:42754615 (Kleinwächter et al., Nat Commun 2026; full text cached) is the
first paper to assign ASW a molecular role, and it is the reason issue #3089 was
filed. Key results:

- **ASW is vertebrate-specific.** Across 812 metazoan genomes,
  [PMID:42754615 "While RTCB, DDX1, CGI-99, and FAM98B – core subunits of the tRNA-LC – occur widely throughout metazoans, ASW appears restricted to vertebrates"],
  and the same transition brought the FAM98 expansion
  [PMID:42754615 "Our analysis indicates that, concurrently with the emergence of ASW, the FAM98 gene evolved into three paralogs of different length, FAM98A, FAM98B and FAM98C."].
- **ASW binds only the FAM98B-containing complex**
  [PMID:42754615 "With ASW assembling into the tRNA-LC in exclusive association with FAM98B"],
  which is why only FAM98B-containing complexes reach the nucleus.
- **ASW is required for nuclear localisation of the whole complex.** Endogenous
  mNeonGreen-tagged RTCB, CGI-99 and DDX1 are nuclear in WT cells but
  [PMID:42754615 "mNG-RTCB, mNG-CGI-99, and mNG-DDX1 were barely detectable in the nucleus of ASW KO cells but rather accumulated in the cytoplasm, indicating that ASW is indeed required for the nuclear localization of the tRNA-LC"],
  and
  [PMID:42754615 "Expression of FLAG-tagged WT ASW, but not ASW Δ56-69, re-imported the tRNA-LC to the nucleus"]
  — i.e. the rescue requires ASW to be able to join the complex.
- **Two autonomous NLSs do the work.**
  [PMID:42754615 "We therefore conclude that ASW harbors two functional NLSs, with NLS1 spanning residues 97–117 and NLS2 spanning residues 201–225"],
  and both act independently on a heterologous GST-mNG-mNG reporter.
- **The pre-tRNA splicing defect tracks nuclear localisation, not ligase
  activity.** ASW KO cells accumulate 5′ tRNA fragments
  [PMID:42754615 "Indeed, we also detected accumulation of 5’ tRNA fragments in ASW KO cells, similar to those detected upon inhibition of the tRNA-LC with menadione"];
  the complex-binding-deficient mutant does not rescue
  [PMID:42754615 "indicating that ASW supports pre-tRNA splicing via its association with the tRNA-LC"];
  and across all mutants
  [PMID:42754615 "all mutants that were unable to redirect the tRNA-LC to the nucleus, were also unable to abrogate the accumulation of 5’ tRNA fragments"].
  Crucially, ASW is dispensable for catalysis itself
  [PMID:42754615 "ASW is not required for the activity of the tRNA-LC in vitro"],
  and nuclear localisation achieved any other way suffices
  [PMID:42754615 "Restoring the nuclear localization of the tRNA-LC through other means than ASW, either FAM98C overexpression or adding an NLS to RTCB, also rescued pre-tRNA splicing, indicating that nuclear localization of the tRNA-LC, independently of how it is achieved, is what matters for efficient pre-tRNA splicing."].
- **ASW is not needed for the UPR arm.**
  [PMID:42754615 "As in FAM98B KO cells, XBP1-mRNA splicing remained unaffected in ASW KO cells"],
  consistent with cytoplasmic XBP1-mRNA splicing being served by the
  FAM98A-containing (cytoplasmic) complexes.

Summary sentence from the paper:
[PMID:42754615 "ASW, which exclusively binds to FAM98B-containing tRNA-LC, enables the nuclear localization of the complex through two independent, conserved NLSs."]

## Why `involved_in GO:0048598 embryonic morphogenesis` is an over-annotation

The row is `IEA` from `InterPro:IPR024887` (GO_REF:0000002). InterPro's
IPR024887 description is explicitly built on the Xenopus *ashwin* work —
"Ashwin is a developmental protein that is expressed in the neural plate, and
later in the embryonic brain, eyes, and spinal cord ... It may be involved in
the regulation cell survival and anteroposterior patterning" (InterPro API,
entry IPR024887, which maps IPR024887 → GO:0048598 and → GO:0072669).

That description traces to PMID:16680723, a *Xenopus laevis* expression +
morpholino/overexpression study
[PMID:16680723 "Morpholino oligonucleotide-mediated reduction in ashwin expression leads to lethality or abnormalities in gastrulation, as well as significant apoptosis in midgastrula embryos."],
whose own conclusion is hedged
[PMID:16680723 "Our results suggest that ashwin regulates cell survival and anteroposterior patterning."].
The same paper is where the two NLSs were first noticed, untested
[PMID:16680723 "Ashwin has no previously characterized domains, although two nuclear localization signals can be identified."].

Two reasons to call the human row an over-annotation rather than a core process:

1. It is a **domain-level electronic transfer of a frog morphant phenotype** to
   the human protein, with no human (or mammalian) developmental data behind it.
2. Even taking the frog phenotype at face value, it is the expected downstream
   consequence of impaired tRNA biogenesis, not a separate developmental
   activity. PMID:42754615 reports that human ASW KO cells have only a mild
   splicing defect with no growth phenotype
   [PMID:42754615 "As in FAM98B KO cells, XBP1-mRNA splicing remained unaffected in ASW KO cells (Fig. 3C) and we did not observe anomalies in cell growth"],
   which argues against a dedicated morphogenetic role for the protein itself.

Hence `MARK_AS_OVER_ANNOTATED` (the frog data are real, so `REMOVE` would
overstate the case) rather than `ACCEPT`/`KEEP_AS_NON_CORE`.

## The new annotation proposed, and the comparator check behind it

Proposed: `involved_in GO:0006606 protein import into nucleus` (IMP,
PMID:42754615).

`CLAUDE.md` requires naming the entity that performs the step and running a
comparator check before proposing a `NEW` process term.

- **Who does the work?** ASW. The NLSs are on ASW, not on RTCB/DDX1/CGI-99/
  FAM98B; deleting ASW strands those four in the cytoplasm; re-expressing ASW
  re-imports them; and point mutations in ASW's own basic clusters abolish the
  import. ASW is cargo *and* carrier, but its carrier role for the other four
  subunits is directly demonstrated, so this is not the "necessary therefore
  participating" trap.
- **Comparator check** (QuickGO, human, experimental evidence for GO:0006606,
  58 annotations): the term is carried not only by the receptor/machinery
  (IPO4/5/9/13, KPNA2, KPNA4, KPNB1, TNPO1, RAN, NUTF2, NUP188, TPR) but by
  small adaptors that ferry a specific partner in — **AKIRIN2** (imports the
  20S proteasome), **HIKESHI** (imports HSP70), **HEATR3** (imports ribosomal
  proteins), **RPAIN** (imports RPA), GPN1, EIF4ENIF1. AKIRIN2 is the closest
  comparator to ASW: a small protein that confers nuclear import on a large
  multi-subunit complex, annotated `involved_in GO:0006606` by IDA. The check
  therefore *passes* — this is an established role-shape for the term, not a
  gap that curators have deliberately left empty.

`GO:0034504 protein localization to nucleus` is the parent and would also fit
("transports or maintains the localization of another protein to the nucleus"),
but GO:0006606 is the supported specific child: directed cytoplasm→nucleus
movement is what the rescue experiments show.

## Why no molecular-function term is asserted

GO has no MF term for a subunit that confers nuclear import on its partners by
*supplying* an NLS:

- `GO:0061608 nuclear import signal receptor activity` requires "Combining with
  a nuclear import signal (NIS) on a cargo to be transported" — ASW does the
  opposite; it *carries* the signal rather than reading one.
- `GO:0030674 protein-macromolecule adaptor activity` would require bringing
  the complex together with a second macromolecule (the import receptor).
  PMID:42754615 never tests karyopherin binding — the NLSs were mapped by
  prediction plus mutagenesis — so asserting an adaptor activity goes past the
  data.
- `GO:0008565 protein transporter activity` is **obsolete** ("obsoleted because
  is has been inconsistently used").

So the review proposes a new MF term (`nuclear localization signal-bearing
subunit activity`) under `proposed_new_terms`, references it from
`core_functions[0].proposed_molecular_function`, and leaves
`molecular_function` unset, as `CLAUDE.md` prescribes for a core activity GO
has no term for. ASW explicitly does **not** contribute to the complex's ligase
activity (not required in vitro), so `contributes_to_molecular_function` is
deliberately empty too.

## Open questions / what remains for issue #3089

- The target module `modules/trna_biogenesis.yaml` named in issue #3089 **does
  not exist**, and none of the other tRNA-LC subunits (RTCB, DDX1, RTRAF,
  TSLIG1/Archease, TSLIG3A/B/C, PYROXD1) has a gene review in this repo yet.
  `grep -l RTCB modules/*.yaml` returns nothing relevant; the closest existing
  module, `modules/er_unfolded_protein_response.yaml`, models the IRE1/XBP1 arm
  but stops before the ligation step. So "should ASW and the FAM98 paralogs be
  added to the tRNA biogenesis module?" cannot be answered as posed — the
  module has to be built first. This review is the first subunit.
- Which karyopherin reads the ASW NLSs is unknown (see knowledge gaps).
- The function of the FAM98A- and FAM98C-containing complexes is unresolved
  [PMID:42754615 "While we have unveiled a function of the FAM98B/ASW-containing tRNA-LC, the roles of the other tRNA-LC populations remain partially unclear."].
- How invertebrates, which lack ASW, import their tRNA-LC is unknown
  [PMID:42754615 "In turn, it remains to be determined how nuclear localization of the tRNA-LC is achieved in invertebrates."].
- The heavy mitotic phosphorylation of the ASW basic tail (Ser-189/Ser-193/
  Thr-197/Thr-198, six independent phosphoproteomic datasets in UniProt) sits
  immediately beside NLS2 (residues 201–225). Whether it regulates import is
  untested.
