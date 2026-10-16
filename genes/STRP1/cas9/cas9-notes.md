# cas9 (Csn1), *Streptococcus pyogenes* M1 / SF370 — curation notes

UniProt: Q99ZW2 (CAS9_STRP1, reviewed, 1368 aa). Type II-A subtype.
Taxon: NCBITaxon:301447 (*Streptococcus pyogenes* serotype M1).

No deep-research provider was available in this environment (no API keys), so this
file is the research journal. Every assertion below carries an inline verbatim quote
from a cached publication.

## Scope decision made at the outset

SpCas9 is the most heavily used genome-editing reagent in biology and the great
majority of the literature (and of the UniProt reference list — `BIOTECHNOLOGY IN
HUMAN CELLS`, zebrafish, *E. coli*, PAM re-engineering) concerns that application.
None of it is a biological function of this gene. The review therefore confines
`description` and `core_functions` to what the protein does inside *S. pyogenes*:
the interference step of type II-A CRISPR-Cas immunity, plus its two further roles
in crRNA biogenesis and in spacer acquisition. Nothing requiring a heterologous host
is annotated.

## 1. Interference: crRNA:tracrRNA-guided, PAM-licensed double-strand cleavage

Cas9 is catalytically inert as an apoprotein and requires a two-part guide:

- [PMID:22745249 "the mature crRNA that is base-paired to trans-activating crRNA (tracrRNA) forms a two-RNA structure that directs the CRISPR-associated protein Cas9 to introduce double-stranded (ds) breaks in target DNA"]
- [PMID:22745249 "mature crRNA alone was incapable of directing Cas9-catalyzed plasmid DNA cleavage"]
- [PMID:22745249 "The cleavage reaction required both magnesium and the presence of a crRNA sequence complementary to the DNA"]

Target *binding* is likewise guide-dependent, measured directly by EMSA with
catalytically dead Cas9:

- [PMID:22745249 "Addition of tracrRNA substantially enhanced target DNA binding by Cas9, whereas little specific DNA binding was observed with Cas9 alone or Cas9-crRNA"]

PAM recognition is the licensing step for both binding and catalysis:

- [PMID:22745249 "Mutation of either G in the PAM sequence substantially reduced the affinity of Cas9-tracrRNA:crRNA for the target DNA"]
- [PMID:22745249 "This finding argues for specific recognition of the PAM sequence by Cas9 as a prerequisite for target DNA binding"]
- [PMID:24476820 "We show that both binding and cleavage of DNA by Cas9-RNA require recognition of a short trinucleotide protospacer adjacent motif (PAM)"]
- [PMID:24476820 "sequences fully complementary to the guide RNA but lacking a nearby PAM are ignored by Cas9-RNA"]
- [PMID:24476820 "DNA strand separation and RNA-DNA heteroduplex formation initiate at the PAM and proceed directionally towards the distal end of the target sequence"]
- [PMID:24476820 "PAM interactions trigger Cas9 catalytic activity"]

Substrate range includes both relaxed and supercoiled DNA, unlike type I Cascade-Cas3:

- [PMID:22745249 "Cas9 cleaves both linearized and supercoiled plasmids"]

## 2. The dual-nuclease architecture (HNH + RuvC) — one function or two?

The division of labour is unambiguous:

- [PMID:22745249 "the Cas9 HNH nuclease domain cleaves the complementary strand, whereas the Cas9 RuvC-like domain cleaves the noncomplementary strand"]
- [PMID:22745249 "Plasmid DNA cleavage produced blunt ends at a position three base pairs upstream of the PAM sequence"]

I considered modelling these as two core functions. Two lines of evidence argue
against splitting them, and for one core function plus prose:

1. **The two centres are allosterically coupled, not independent.** In the
   meningococcal orthologue the catalytic HNH conformation is what switches RuvC
   on: [PMID:31668930 "The HNH active conformation activates the RuvC domain"].
   A GO model with two independent `DNA endonuclease activity` nodes would assert
   something the mechanism denies.
2. **Occluding HNH alone abolishes cleavage outright** rather than converting Cas9
   into a nickase: [PMID:28844692 "AcrIIC1 is a broad-spectrum Cas9 inhibitor that prevents DNA cutting by multiple divergent Cas9 orthologs through direct binding to the conserved HNH catalytic domain of Cas9"],
   [PMID:28844692 "AcrIIC1 blocks DNA cleavage by multiple Cas9 orthologs without impacting DNA binding, effectively transforming catalytically active Cas9 into catalytically inactive dCas9"].

That second result also cuts the other way and is the single most useful datum for
the module pair: AcrIIC1 **separates recognition from cleavage**, leaving DNA
binding intact while removing catalysis. Recognition and cleavage are therefore
genuinely two activities of this protein, even though the two *nuclease domains* are
one. Hence the review's two interference core functions: guide-directed recognition
(no GO term — see §5) and DNA endonuclease activity (GO:0004520).

GO has no vocabulary for "which domain of a multidomain nuclease", so the HNH/RuvC
distinction is recorded as prose in `description` and in the core-function
descriptions. It matters for the counterpart review (`genes/NEIME/acrIIC1`): the Acr's
target is a *domain*, not the protein, and the suppression module records that gap
explicitly.

## 3. GO:0008408 3'-5' exonuclease activity — adjudication

My prior was that this is a domain-based inference (HNH and RuvC are both
endonucleolytic and the canonical product is a blunt DSB), but that is wrong. It is a
**direct observation in the cited paper**:

- [PMID:22745249 "the non-complementary strand is first cleaved endonucleolytically and subsequently trimmed by a 3’-5’ exonuclease activity"]

UniProt stands behind it independently: the Q99ZW2 reference block carries
`FUNCTION AS AN EXONUCLEASE` against PMID:22745249, the `FUNCTION` comment states
"The target strand not complementary to crRNA is first cut endonucleolytically, then
trimmed 3'-5' exonucleolytically", and the entry carries the `Exonuclease` keyword.
The IDA is therefore correctly sourced and must not be removed.

It is nonetheless not a core function:

- it acts on a product the enzyme has already cut, i.e. it is a secondary trimming
  step, not the activity that destroys the invader;
- the decisive biological output is the near-blunt double-strand break
  (`"Plasmid DNA cleavage produced blunt ends at a position three base pairs upstream of the PAM sequence"`);
- no distinct exonuclease active site has been assigned — UniProt annotates exactly
  two catalytic residues (ACT_SITE 10, RuvC; ACT_SITE 840, HNH), so the trimming is
  most parsimoniously further RuvC action on the already-nicked non-target strand
  rather than a third activity;
- it was observed in vitro on short duplexes (fig. S4B) and is not part of the
  cleavage signature used to define Cas9 chemistry anywhere since.

Action: `KEEP_AS_NON_CORE`. Not `REMOVE` (the evidence is real and curator-read),
not `ACCEPT`-as-core (it is a side reaction).

## 4. GO:0043571 maintenance of CRISPR repeat elements — adjudication

This one looks wrong on its face (Cas9 is the interference effector; maintaining the
array sounds like Cas1/Cas2 work) and is right for two reasons that only appear once
you read the term definition. GO:0043571 sits under GO:0043570 *maintenance of DNA
repeat elements* (DNA metabolism), **not** under defence, and its definition reads:
"Any process involved in sustaining CRISPR repeat clusters, including capture of new
spacer elements, expansion or contraction of clusters, ... transcription of the
CRISPR repeat arrays into RNA and processing". Cas9 does work in two of those limbs.

**(a) Transcription/processing limb — crRNA biogenesis.** Cas9 (as Csn1) is required
for mature crRNA production, non-catalytically:

- [PMID:21455174 "tracrRNA directs the maturation of crRNAs by the activities of the widely conserved endogenous RNase III and the CRISPR-associated Csn1 protein; all these components are essential to protect S. pyogenes against prophage-derived DNA"]
- [PMID:21455174 "In-frame deletions of any of the operon’s four genes then revealed Csn1 as the only Cas protein required for the production of mature crRNAs and concomitant tracrRNA cleavage"]
- [PMID:21455174 "Csn1 acts as a molecular anchor facilitating the base-pairing of tracrRNA with pre-crRNA"]
- [PMID:21455174 "the strongly reduced accumulation of tracrRNA in the absence of csn1"]

The role is explicitly non-catalytic — RNase III does the cutting:

- [PMID:24270795 "demonstrating that none of the catalytic motifs is involved in dual-RNA maturation by RNase III"]
- [PMID:24270795 "Cas9 seems to have a stabilizing function on dual-RNA"]

**(b) Spacer-capture limb — adaptation.** Cas9 is a member of the acquisition
machinery and its PAM-binding motif decides which protospacers enter the array:

- [PMID:25707807 "Here we show that Cas9 selects functional spacers by recognizing their PAM during spacer acquisition"]
- [PMID:25707807 "Cas9 associates with other proteins of the acquisition machinery (Cas1, Cas2 and Csn2), presumably to provide PAM-specificity to this process"]
- [PMID:25707807 "these results indicate that Cas1 and Cas9 are part of a complex dedicated to spacer acquisition which requires Cas1 nuclease activity and Cas9 PAM-binding properties for the selection of new spacer sequences"]
- [PMID:25707807 "whereas spacers acquired in the presence of dCas9 displayed correct PAMs, those acquired in the presence of Cas9PAM matched DNA regions without a conserved flanking sequence"]
- [PMID:25707807 "These results establish a new function for Cas9 in the genesis of prokaryotic immunological memory"]

Note the dissociation that makes this *participation* and not mere necessity: Cas9's
own nuclease activity is dispensable for acquisition, while its PAM-binding motif is
what performs the selection step — [PMID:25707807 "the nuclease activity and PAM-binding function of Cas9 are dispensable for this process"]
(dispensable for acquisition *occurring*; the PAM mutant still acquires spacers, but
acquires the wrong ones). The step being performed by Cas9 is PAM recognition, which
is the test CLAUDE.md asks for: name the entity that does the work. It is Cas9.

Action: `ACCEPT` on both rows (the IDA and the UniRule IEA). Caveat recorded in
`review.reason`: the IDA's cited reference (PMID:22745249) is the interference paper
and does not itself establish array maintenance; the real grounding is PMID:21455174
(biogenesis, same lab, prior year) and PMID:25707807 (adaptation). Both are added via
`additional_reference_ids` and quoted in `supported_by`. Per CLAUDE.md the curator's
call is not overruled on a reference-choice quibble.

## 5. The ontology gap: no MF term for guide-RNA-directed recognition

Searched QuickGO for `guide RNA binding`, `crRNA`, `CRISPR`, `RNA-guided`. The only
CRISPR-related terms in GO are process terms (GO:0099048, GO:0043571, GO:0098672 and
two obsoletes). There is **no** molecular-function term for programmable,
guide-RNA-directed target recognition — the defining property of every Cas effector,
and the property that distinguishes Cas9 from any ordinary restriction endonuclease.
`GO:0003676`/`GO:0003677`/`GO:0003690` describe the binding but say nothing about
where the specificity comes from.

The host module records this as an open ontology gap
(`modules/crispr_cas_adaptive_immunity.yaml`, `knowledge_gaps[0]`) and asserts no id.
This review goes one step further and proposes the term, since it would serve every
Cas effector (Cas9, Cas12a, Cas13a, Cascade, Csm/Cmr) rather than only this gene:

- **proposed_name**: `guide RNA-directed nucleic acid target recognition activity`
- **proposed_parent**: GO:0003676 nucleic acid binding
- the asserted content is *where the specificity lives*: in a separate,
  non-covalently bound guide RNA, so that changing the guide changes the target with
  no change to the polypeptide.

Deliberately **not** in the definition: PAM dependence (protein-encoded, and specific
to Cas9/Cas12a; Cas13a has a PFS, Cascade a different motif) and the chemistry of what
happens next (covered by GO:0004520, GO:0004521, GO:0004530). Two children are
suggested in the justification rather than proposed here.

Scope caveat worth flagging to GO: as defined, the term would also fit Argonaute-family
slicers, which are guide-directed in exactly this sense. I think that is a feature —
the concept is "specificity by dissociable nucleic-acid guide" and it is one concept —
but it is a decision for the ontology editors, so it is raised in
`suggested_questions` rather than resolved here.

## 6. Other annotation calls

- **GO:0003676 nucleic acid binding** (IEA, InterPro IPR036397 = RNase H-like
  superfamily). Root-level and uninformative. The DNA half of Cas9's nucleic-acid
  binding is already carried by the IDA GO:0003677 row (refined below), so this row
  is modified to the half that GOA is missing entirely: guide RNA binding
  (GO:0003723), which UniProt annotates experimentally from the ternary structures.
- **GO:0003677 DNA binding** (IDA, PMID:22745249) → `MODIFY` to GO:0003690
  double-stranded DNA binding. The EMSA substrates were duplex DNA and plasmid, and
  PAM recognition requires the duplex: Cas9 does not recognise a PAM on single-stranded
  DNA.
- **GO:0004519 endonuclease activity** (IEA) → `MODIFY` to GO:0004520 DNA endonuclease
  activity, the child already present with IDA. Too-general parent per the action enum.
- **GO:0004520 DNA endonuclease activity** (IDA) → `ACCEPT`; core.
- **GO:0046872 metal ion binding** (IEA, UniRule) → `MODIFY` to GO:0000287 magnesium
  ion binding. UniProt's COFACTOR block names only Mg(2+) (ChEBI:18420), cleavage
  requires magnesium [PMID:22745249 "The cleavage reaction required both magnesium and the presence of a crRNA sequence complementary to the DNA"],
  and the orthologue structures place a Mg2+ ion in the HNH pocket
  [PMID:31668930 "The HNH domains of Cas9 orthologs use a metal ion cofactor to catalyze TS cleavage between nts 3 and 4 of the protospacer"].
- **GO:0051607 defense response to virus** (IEA, UniRule) → `ACCEPT`. Unlike the
  meningococcal orthologue, phage immunity is directly demonstrated for this locus:
  [PMID:25707807 "the Cas9 nuclease inactivates infective phages using crRNAs as guides to introduce double-strand DNA breaks into the viral genome"],
  and the adaptation assays were phage-challenge assays with ϕNM4γ4 using the cloned
  *S. pyogenes* type II-A locus. The native substrate set is wider than virus
  (prophage-derived DNA and plasmids — PMID:21455174), which is why a `NEW` GO:0099048
  row is added rather than leaving GO:0051607 to carry the whole process.
- **NEW GO:0099048 CRISPR-cas system**. The pathway term, absent from GOA for this
  protein. Covers the plasmid/prophage substrates that GO:0051607 does not, and sits
  under GO:0099046 clearance of foreign intracellular nucleic acids. Not an ancestor
  or descendant of GO:0051607 or GO:0043571 (checked: GO:0043571 is under
  GO:0090304/GO:0043570, a DNA-metabolism branch; GO:0099048 is under GO:0099046).

## 7. Things deliberately not annotated

- Genome editing, base editing, dCas9 transcriptional control, PAM re-engineering,
  gene drives, diagnostics — all heterologous-host applications.
- `GO:0005515 protein binding` for the Cas9–Cas1–Cas2–Csn2 association. The
  informative content is PAM selection, which is captured as sequence-specific DNA
  binding in the adaptation core function; a bare binding term would discard it.
- Any `involved_in` for DNA repair or NHEJ. Those are the *host* responses to the
  break in editing applications, not Cas9's activity, and there is no bacterial
  counterpart in evidence.
- Single-turnover vs multiple-turnover kinetics: PMID:22745249 reports multiple
  turnover, PMID:24476820 reports that Cas9:RNA stays bound to both cleaved ends and
  "acts as a single-turnover enzyme". Not an annotation-level question; left out.
