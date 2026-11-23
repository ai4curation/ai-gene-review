# rnc / RNase III (Escherichia coli K-12, P0A7Y0) — curation notes

Curation journal for the gene review. Every assertion carries inline provenance.
Deep research via the `deep-research` command was not possible in this environment (no
provider API keys configured), so this file is the research record.

## Identity

- UniProt `RNC_ECOLI` (P0A7Y0), 226 aa, reviewed, `EC=3.1.26.3`. Gene `rnc`, locus b2567;
  encoded in the `rnc-era-recO` operon [file:ECOLI/rnc/rnc-uniprot.txt].
- Architecture: N-terminal RNase III nuclease domain (6..128) plus a C-terminal
  double-stranded RNA-binding domain (155..225); active sites at Asp45 and Glu117;
  Mg(2+)/metal ligands at 41, 114 and 117 [file:ECOLI/rnc/rnc-uniprot.txt].
  [PMID:15699182 "E.coli RNase III functions as a homodimer, with the subunit polypeptide
  (226 amino acids) containing an N-terminal nuclease domain and a C-terminal
  dsRNA-binding domain (dsRBD)"]
- This is the founding member of the RNase III superfamily, the bacterial counterpart of
  Dicer and Drosha: [PMID:15699182 "E.coli RNase III is a member of a structurally
  distinct superfamily that includes Dicer, a central enzyme in the mechanism of RNA
  interference."]

## Core activity

A double-strand-specific endoribonuclease that cleaves duplex RNA, leaving
5'-phosphate/3'-OH ends, and acts as a homodimer so that two half-sites form the
composite catalytic centre.

- [PMID:15699182 "Escherichia coli ribonuclease III (RNase III; EC 3.1.24) is a
  double-stranded(ds)-RNA-specific endonuclease with key roles in diverse RNA
  maturation and decay pathways."]
- End chemistry, measured directly:
  [PMID:1091644 "Direct analysis shows that both activities cleave RNA chains to yield
  5'-phosphate and 3'-hydroxyl termini."] The same preparation study separated the
  dsRNA-cleaving/T7-processing activity from a contaminating activity on the RNA strand of
  DNA:RNA hybrids [PMID:1091644 "RNase III preparations contain three activities: one
  which solubilizes stable RNA:RNA duplexes; one which solubilizes the RNA of DNA:RNA
  hybrids; and one which processes the polycistronic mRNA of bacteriophage T7 in a manner
  identical with sizing factor."], and UniProt records the resulting specificity as
  "Digests double-stranded RNA formed within single-strand substrates, but not RNA-DNA
  hybrids" [file:ECOLI/rnc/rnc-uniprot.txt]. That separation is worth noting, because it
  is exactly the opposite of the Cas3 case reviewed alongside this gene: Cas3's hybrid
  activity is real, RNase III's is a contaminant.
- Homodimer: [PMID:932008 "Chromatography on Sephadex G-100 is consistent with a
  molecular weight of 50,000, suggesting that the native enzyme is a dimer."]
- Two catalytic metal ions, by kinetics and by a two-metal-ion-specific inhibitor:
  [PMID:15699182 "The measured Hill coefficient (n (H)) is 2.0 +/- 0.1, indicative of the
  involvement of two Mg2+ ions in phosphodiester hydrolysis."]

## Biological roles

**rRNA maturation** is the canonical one. RNase III makes the first cuts that liberate the
16S and 23S precursors from the single 30S primary transcript.

- [PMID:6364133 "RNase III makes the initial cleavages that excise Escherichia coli
  precursor 16S and 23S rRNA from a single large primary transcript."]
- The requirement is absolute for 23S maturation but, strikingly, not for ribosome
  function: [PMID:6364133 "In mutants deficient in RNase III, no species cleaved by RNase
  III are detected and the processing of 23S rRNA precursors to form mature 23S rRNA fails
  entirely."] and the aberrant subunits "function well enough to participate in protein
  synthesis and permit cell growth". This is why an `rnc` null is viable (UniProt
  disruption phenotype: slower growth, extended 23S in the ribosome)
  [file:ECOLI/rnc/rnc-uniprot.txt].
- In vivo cleavage of the rRNA precursor and of phage T7 early RNA from the same study:
  [PMID:4587248 "RNase III cleavage seems to be part of the normal pathway for producing
  at least the 16S and 23S ribosomal RNAs in vivo."] and
  [PMID:4587248 "the normal pathway for producing the T7 early messenger RNAs in vivo
  appears to involve endonucleolytic cleavage by RNase III"].
- A spatial dimension was added later: the 5' pre-rRNA leader associates with the
  nucleoid in an RNase III-dependent manner, and RNase III contributes to rapid rRNA
  operon induction [PMID:23893733 "Moreover, RNase III plays a role in the rapid induction
  of ribosomal operons during outgrowth and is essential in the absence of the
  transcriptional regulator Fis, suggesting a linkage of transcription and RNA processing
  for ribosomal operons in E. coli."]

**mRNA decay and its own regulon.** RNase III cleavage at the 5' end of the `pnp`
transcript is the committing step of that mRNA's turnover.

- [PMID:3308454 "The transcripts covering pnp, the gene encoding polynucleotide
  phosphorylase, are processed by ribonuclease III."] and
  [PMID:3308454 "the sequence involved in the stabilization of the pnp mRNA is located at
  the 5' end of the message and that the RNase III processing triggers the decay of the
  transcripts downstream"]. The half-life goes from 1.5 min to more than 40 min in the
  mutant, with an 11-fold rise in steady-state level, and PNPase is 10-fold
  over-expressed — i.e. RNase III cleavage is a quantitative regulator of gene expression,
  not merely a maturation step.
- UniProt adds autoregulation: the enzyme "Processes the 5' end of its own transcript
  leading to mRNA instability" [file:ECOLI/rnc/rnc-uniprot.txt].

**Regulation of the enzyme itself.** RNase III activity is dialled down by a protein
partner and by growth state.

- [PMID:19141481 "We show that YmdB functions by interacting with a site in the RNase III
  catalytic region, that expression of YmdB is transcriptionally activated by both
  cold-shock stress and the entry of cells into stationary phase, and that this activation
  requires the sigma-factor-encoding gene, rpoS."]

**Localization.** Cytoplasmic/cytosolic, loosely ribosome-associated
[file:ECOLI/rnc/rnc-uniprot.txt]; detected in the cytosolic fraction by two independent
proteomic surveys of E. coli K-12 (PMID:15911532, PMID:18304323).

## The CRISPR connection, and why it is NOT annotated here

This gene is the mirror image of `ygcB`/Cas3. Cas3 is a dedicated Cas protein with no
function outside CRISPR. RNase III is a housekeeping enzyme that a *different class* of
CRISPR system borrows. The module's own framing is right on this point: it "is not a Cas
protein and is not encoded in the cas locus"
[file:modules/crispr_cas_adaptive_immunity.yaml].

What the literature actually establishes, in order of how close it gets to E. coli:

1. **Type II crRNA maturation needs host RNase III — demonstrated in *Streptococcus
   pyogenes*.** [PMID:21455174 "We show that tracrRNA directs the maturation of crRNAs by
   the activities of the widely conserved endogenous RNase III and the CRISPR-associated
   Csn1 protein; all these components are essential to protect S. pyogenes against
   prophage-derived DNA."] The paper is explicit that this is a *host factor* being
   recruited: [PMID:21455174 "Our study reveals a novel pathway of small guide RNA
   maturation and the first example of a host factor (RNase III) required for bacterial
   RNA-mediated immunity against invaders."] The organism is S. pyogenes, not E. coli.
2. **The E. coli protein can do the job, in a heterologous host.** Karvelis et al.
   transplanted the *S. thermophilus* DGCC7710 CRISPR3 (type II) system into E. coli and
   compared `rnc+` and `rnc-` hosts:
   [PMID:23535272 "To probe whether the E. coli RNase III is able to replace St-RNase III
   in the crRNA processing and contribute to the St-CRISPR3-Cas mediated immunity in the
   heterologous E. coli host, we performed pSP1 plasmid transformation assay in the rnc+
   (E. coli RR1) and rnc- (E. coli HT115) strains"]. The result was conditional:
   [PMID:23535272 "The rnc- strain carrying a wild-type CRISPR array became permissive for
   pSP1 plasmid transformation while the rnc- strain carrying a minimal CRISPR array was
   non-permissive to pSP1 transformation (Fig. 3B). This indicates that RNase III is not
   necessary for the maturation of pre-crRNA containing a single CRISPR spacer."]
   UniProt records both halves of this as experimental findings of the entry: complementing
   the pre-crRNA processing defect of an S. pyogenes `rnc` deletion, and loss of
   plasmid immunity in E. coli HT115 [file:ECOLI/rnc/rnc-uniprot.txt].
3. **E. coli K-12's own CRISPR system does not use RNase III.** E. coli K-12 has a type
   I-E system, in which the repeat cleavage is done by the Cas6e/CasE subunit of Cascade,
   not by a host RNase: [PMID:23535272 "During the RNA maturation step in type I and type
   III CRISPR systems, pre-crRNA is cleaved within the repeat sequence by Cas6
   endonucleases."] UniProt makes the same point about the complementation experiment —
   the E. coli strain used "does not have the corresponding CRISPR locus"
   [file:ECOLI/rnc/rnc-uniprot.txt].

**Conclusion: no CRISPR process term on P0A7Y0.** Point 2 is a demonstration of
*capability* in an engineered context, not of a role in E. coli K-12 biology. A
`GO:0099048` or crRNA-processing annotation on this protein would assert that E. coli
RNase III participates in CRISPR-Cas immunity in E. coli, which point 3 contradicts: the
native system routes that step through Cas6e. GOA carries no CRISPR annotation for `rnc`
and should not — this is a curator decision to respect, not a gap. The capability is
recorded here, in `suggested_questions`, and in the `review.reason` of the
ribonuclease III activity rows, which is where scoped prose belongs.

Note also that this is *not* a case of adding an annotation because "every other
participant has it": the other participants in type II maturation are Cas9/Csn1 and the
tracrRNA, and the relevant comparator for the host enzyme is the *S. pyogenes* RNase III,
which is the protein the S. pyogenes result is about.

## Module cross-check: `modules/crispr_cas_adaptive_immunity.yaml`

The `rnase_iii_processing_activity` annoton inside `rnase_iii_tracrrna_route` is sound in
substance. Three observations:

1. **The family descriptor is honest.** `family.preferred_term: bacterial RNase III
   family` carries no `term` id, with `representative_members: [UniProtKB:P0A7Y0]`. Given
   that this is a descriptor for "the housekeeping enzyme a type II system recruits"
   rather than for a specific PANTHER/InterPro grouping, asserting no id is the right
   call. `GO:0004525` as the `required_function` and `function` is exactly correct and is
   independently supported for P0A7Y0 by IDA, IBA and IEA.
2. **The exemplar description understates the evidence, and that is the one thing I would
   change.** It currently reads: "Escherichia coli K-12 rnc, the reviewed exemplar of the
   family; the type II processing reaction itself was characterised in Streptococcus
   pyogenes." That is true of PMID:21455174, the only evidence the annoton cites, but it
   is not the whole picture: the E. coli protein has itself been shown to carry out this
   reaction, in the heterologous system of PMID:23535272. "Characterised in S. pyogenes"
   reads as though P0A7Y0 were a bare sequence stand-in, when in fact it is the one
   bacterial RNase III besides the S. pyogenes enzyme with direct functional data on a
   type II pre-crRNA:tracrRNA substrate. I would add PMID:23535272 as a second
   `EvidenceItem` on the annoton's `function` and reword the member description to say
   that the reaction was characterised in S. pyogenes *and* reconstituted with the E. coli
   enzyme in a heterologous host.
3. **A substrate caveat worth recording.** The annoton's `substrates` is "pre-crRNA:tracrRNA
   double-stranded region", which is right, but the RNase III requirement is array-length
   dependent: a minimal single-spacer array matures without RNase III
   [PMID:23535272 "This indicates that RNase III is not necessary for the maturation of
   pre-crRNA containing a single CRISPR spacer."]. The route is therefore not an obligate
   step of every type II system's biogenesis, which is useful context for a module
   `notes` field.

Nothing in the module suggests annotating the E. coli protein with a CRISPR process term,
and nothing in this review supports doing so.

## Annotation adjudication summary

The 23 GOA rows divide cleanly:

- **Core, accept as-is:** `GO:0004525` ribonuclease III activity (three rows: IDA, IBA,
  IEA), `GO:0003725` double-stranded RNA binding (IBA), `GO:0000287` magnesium ion
  binding (IDA), `GO:0042803` protein homodimerization activity (IPI), `GO:0006364` rRNA
  processing (IMP + IEA), `GO:0006397` mRNA processing (IMP + IEA), `GO:0019899` enzyme
  binding (IPI, YmdB), the three `GO:0005829` cytosol IDA rows and the `GO:0005829` IBA.
- **True but one level too general, replaced by the specific child already supported for
  this protein:** `GO:0003723` RNA binding (IEA) → `GO:0003725`; `GO:0042802` identical
  protein binding (IEA, ARBA) → `GO:0042803`; `GO:0005737` cytoplasm (IEA) → `GO:0005829`.
- **Uninformative binding term:** `GO:0005515` protein binding (IPI with RNase II/`rnb`
  P30850, from a genome-scale tagging study) → `GO:0019899` enzyme binding, following
  project guidance to avoid `protein binding`. The interaction itself is in UniProt's
  INTERACTION block with NbExp=2, so the row is kept rather than removed.
- **Non-core:** `GO:0010468` regulation of gene expression (IBA). RNase III does modulate
  gene expression — the `pnp` result is a textbook case and it autoregulates — but this is
  a downstream consequence of the nuclease activity and sits at a very general level.
- **Kept at the general level on purpose:** all three `GO:0006396` RNA processing rows.
  The IBA is a deliberate family-level placement spanning bacterial RNase III through
  Dicer/Drosha orthologs, whose substrates are not shared, so the general term is the
  most specific statement true across the clade. The IMP (PMID:4587248) is kept because
  that paper's scope is both rRNA and phage T7 early mRNA, which the cellular rRNA/mRNA
  terms do not jointly cover. The IEA from InterPro was initially marked `MODIFY` to
  `GO:0006364`/`GO:0006397`, but both of those are already annotated to the gene by IMP,
  so the refinement would be pure duplication; it is accepted as a correct umbrella
  instead. (The best-practices validator independently flags mixed actions across rows
  for the same term, which is the same conclusion reached from the biology.)

**No `NEW` is proposed for this gene.** Two candidates were considered and both declined.

- `GO:0099048` CRISPR-cas system / any crRNA-processing term — declined for the reasons
  set out above: the only E. coli-protein evidence is a heterologous reconstitution, and
  E. coli K-12's native type I-E system routes that step through Cas6e.
- `GO:0006402` mRNA catabolic process — this one is tempting and nearly survives. The
  comparator is good: RNase E (P21513) carries `GO:0006402` (IEA and IMP) and `GO:0006401`
  RNA catabolic process (QuickGO annotation query on UniProtKB:P21513), so a bacterial
  endoribonuclease that makes the committing cleavage of an mRNA's turnover does
  conventionally get the term, and RNase III performs that cleavage itself rather than
  merely being required for it [PMID:3308454 "the sequence involved in the stabilization
  of the pnp mRNA is located at the 5' end of the message and that the RNase III
  processing triggers the decay of the transcripts downstream"]. What stops it is the
  redundancy rule in CLAUDE.md: a QuickGO ancestor query on `GO:0006402` returns
  `GO:0010468` among its ancestors (via `GO:0010629` negative regulation of gene
  expression), and `GO:0010468` is already annotated to `rnc` by IBA. Proposing a
  descendant of a term the gene already carries is a refinement for a curator to make on
  the existing row, not a gap for this review to fill, so it is raised in
  `suggested_questions` instead.
