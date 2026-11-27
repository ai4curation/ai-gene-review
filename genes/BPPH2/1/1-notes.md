# Bacillus phage phi29 gene 1 (P03679, protein p1 / gp1) — curation notes

## Provenance of this review

No deep-research provider was available in this container (no API keys), so
`just deep-research` was **not** run and no `-deep-research-<provider>.md` file
exists for this gene. The literature below was assembled by hand from the
cached `publications/PMID_*.md` records, the UniProt flat file, and web
retrieval of two sources that are not in the cache (the 1976 *Eur. J. Biochem.*
full text and the Meijer/Horcajadas/Salas phi29 review). Every cached record
used here is **abstract-only** (`full_text_available: false`), so the
curator-deference rule applies throughout: no experimental row was removed on
the strength of an abstract.

GONUTS (`gowiki.tamu.edu`) was retried for this gene on 2026-11-01 and is still
down: both `https://gowiki.tamu.edu/wiki/index.php/Gene:P03679` and the site
search returned HTTP **410 Gone**. The CACAO row's wiki-side rationale therefore
could not be read, exactly as in batches 1–2.

## What the protein is

86 aa (mature chain 2–86) early protein, two products from the same ORF by
alternative in-phase initiation: the 10 kDa "Long" form (P03679-1) and a 6 kDa
"Short"/delta-1 form (P03679-2) lacking residues 1–34
[PMID:2526779 "indicating that the 10-kDa protein is the product of gene 1."],
[PMID:2526779 "corresponds to an internal in-phase initiation event in ORF-6."].
The same paper mapped gene 1 to ORF-6 by sequencing the ochre mutation in
sus1(629) [PMID:2526779 "indicating that this ORF corresponds to gene 1."].

Sequence features (UniProt P03679): predicted coiled coil 38–67, hydrophobic
C-terminus, no transmembrane helix — it is a **peripheral** membrane protein, not
an integral one [file:BPPH2/1/1-uniprot.txt "Peripheral membrane protein"].

## Core biology: a membrane scaffold that compartmentalises phi29 replication

p1 self-polymerises into protofilament sheets resembling tubulin/FtsZ polymers
[PMID:9774353 "These structures resemble eukaryotic tubulin and"], and the
authors conclude it is a structural component of a viral-encoded,
membrane-associated structure
[PMID:9774353 "propose that protein p1 is a component of a viral-encoded structure that"]
that supplies an [PMID:9774353 "anchoring site for the viral DNA replication machinery."].

Assembly determinants are mapped: the coiled-coil residues Leu46/Met53/Leu60
are required for sheet formation
[PMID:11283004 "demonstrate that residues Leu(46), Met(53), and Leu(60), but not Leu(39), are"],
and seven single substitutions in the coiled-coil or hydrophobic region block
formation of large complexes [PMID:15883018 "required for the self-assembly of gp1."].
Membrane attachment maps to the hydrophobic C-terminus
[PMID:9193003 "association of protein p1 with membranes was abolished when the C-terminal 43"].

In infected cells p1 is membrane-associated
[PMID:11032825 "associated in Bacillus subtilis-infected cells."], has a
peripheral location by immunoEM
[PMID:12904294 "immunoelectron microscopy studies reveal that p1 has a peripheral"],
and assembles into membrane-associated multimers
[PMID:12904294 "cells into multimeric structures that are associated with the bacterial"].
Those structures form independently of the rest of the replisome and are
functional: plasmid-borne p1
[PMID:12904294 "and supports DNA replication of a p1-lacking mutant phage, suggesting that the"].
The model is that [PMID:12904294 "assembled on the cell membrane provides a specific site for 29 DNA replication."].

p1 binds the primer terminal protein (TP) directly — and the TP-binding and
membrane/self-assembly functions are separable, since the C-terminally truncated
p1DeltaC43 still [PMID:11032825 "can interact with the primer terminal protein (TP)"].
In membrane vesicles from infected cells p1, free TP and a little DNA polymerase
co-fractionate [PMID:9193003 "role of protein p1 for in vivo phi29 DNA replication, led us to conclude that a"],
giving the membrane-associated multiprotein initiation complex model.
The replisome is proposed to attach to this platform
[PMID:11032825 "attaches to a membrane-associated p1-based structure."].

Host side: p1-YFP localises to midcell, colocalises with and associates with
host FtsZ [PMID:23836667 "protein p1 colocalizes with the B. subtilis cell division protein FtsZ and"],
and midcell targeting is lost without FtsZ. The same paper restates the
replication phenotype [PMID:23836667 "protein p1, phage 29 DNA replication is impaired."].

## Is p1 required for phi29 DNA replication? Yes, quantitatively

- sus1(629) restrictive infection: [PMID:2526779 "29 protein p1 is needed for the viral DNA replication."]
- p1 is described as [PMID:9774353 "membrane-associated protein required for in vivo viral DNA replication."]
- [PMID:12904294 "protein p1 enhances the rate of in vivo viral DNA replication."]
- The requirement is temperature-dependent, not absolute: the Meijer et al.
  phi29 review (Microbiol Mol Biol Rev 2001, PMC99027) states replication "was
  severely affected in sus1(629) phage-infected nonsuppressor cells" at 37 °C
  but only slightly lower at 30 °C. An excess of p1 is also inhibitory
  [PMID:11032825 "of phi29 DNA replication in vivo in a dosage-dependent manner."].

So the honest statement is: p1 is a replication protein whose loss severely
impairs (but does not formally abolish at all temperatures) viral DNA synthesis.
This matters for the choice between `involved_in` and
`acts_upstream_of_or_within_positive_effect`, and the latter — which the CACAO
row uses — is the more cautious and arguably better-fitting qualifier.

## Second, less-corroborated activity: translational repression via mRNA binding

One group (Sophia University; Hirokawa/Makino lab) reports that gp1 represses
the upstream *dna* genes post-transcriptionally. mRNA level and integrity are
unchanged [PMID:9480849 "of the polycistronic mRNA were not influenced by the presence of gene 1."],
gp1 binds RNA in vitro
[PMID:9480849 "the RNA binding ability of gp1 was demonstrated by in vitro system"],
and the conclusion is that translation of
[PMID:9480849 "the dna genes was affected by gp1 through binding to mRNA."].
The follow-up links self-assembly to this activity
[PMID:15883018 "to be necessary for the efficient binding to RNA and the translational"]
and restates that gp1
[PMID:15883018 "suppresses the synthesis of phi29 DNA polymerase and primer protein in the"].
UniProt curates this as the RNA-binding keyword (refs 6 and 10 of the entry).

Caveat recorded for the reviewer: this is a single laboratory, the target
transcript is the phi29 *dna* operon mRNA, and the Salas lab's extensive p1 work
never tested it. It is cited here to justify refining the RNA-binding term to
mRNA binding and to support one new regulatory BP row, flagged as
single-provenance in the row's `reason`.

## The CACAO row and the predicted failure shape (screen 1)

The CACAO row is `GO:0039693 viral DNA genome replication`,
`acts_upstream_of_or_within_positive_effect`, IMP, PMID:820555 (Carrascosa et
al. 1976). The screen predicted an adjacent-locus / one-paper-many-genes
failure: a single multi-gene mutant survey spread across many phi29 entries,
whose abstract (all that is cached) says only
[PMID:820555 "Mutants in six genes do not synthesize phage DNA."] without naming
the six.

**The prediction is wrong for this gene.** The 1976 full text was retrieved
(Eur. J. Biochem. 66:229–241, DOI 10.1111/j.1432-1033.1976.tb10512.x; OCR copy
via scispace) and it names gene 1 three separate times:

- Results: "Other mutants which did not synthesize phage DNA were sus1(629),
  ts6(1360), sus6(626) and sus17(112) (Tables 1 and 2)."
- Discussion: "Cistrons 1, 2, 3, 5, 6 and 17 are involved in phage-specific DNA
  synthesis (Fig. 13)."
- "The protein products of cistrons 1, 3, 6 and 17, involved in DNA synthesis,
  have been characterized as early proteins."

So the six DNA-negative cistrons are 1, 2, 3, 5, 6 and 17, gene 1 is one of
them, and the paper individually establishes the annotated term for this gene by
a named suppressor-sensitive mutant (sus1(629)) scored for phage DNA synthesis —
a textbook IMP. The same mutant allele is the one Prieto et al. later sequenced
to prove ORF-6 = gene 1 [PMID:2526779 "indicating that this ORF corresponds to gene 1."],
which independently confirms that the 1976 "sus1" is this locus and not a
neighbour. These full-text sentences are **not** quoted in the review's
`supported_text` fields, because the cached publication record is abstract-only
and quotes must be verbatim substrings of the cached source; they are recorded
here instead and summarised in the row's `reason`.

## Annotation decisions

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0033644 host cell membrane (EXP, IDA, IEA) | 11032825 / 12904294 / SL-0380 | ACCEPT ×3 | peripheral host-membrane location, directly shown |
| GO:0039693 viral DNA genome replication (IDA, IEA, IMP/CACAO) | 11032825 / KW-1194 / 820555 | ACCEPT ×3 | core; CACAO row verified against full text |
| GO:0003723 RNA binding (IEA KW) | GO_REF:0000043 | MODIFY → GO:0003729 mRNA binding | target is the *dna* operon mRNA |
| GO:0006260 DNA replication (IEA) | GO_REF:0000120 | MODIFY → GO:0039693 | lateral fix: GO:0039693 is **not** a descendant of GO:0006260 (checked in QuickGO), so this row asserts cellular DNA replication, which p1 does not do |
| GO:0016020 membrane (IEA InterPro) | GO_REF:0000002 | MODIFY → GO:0033644 | GO:0033644 sits under host cellular component, not under GO:0016020, so this is a lateral refinement to the host-scoped term already carried by IDA |
| GO:0016032 viral process (IEA InterPro) | GO_REF:0000002 | TOO_GENERAL | GO:0039693 is a descendant (GO:0039693 → GO:0019079 → GO:0019058 → GO:0016032) and is asserted in this review |
| GO:0017148 negative regulation of translation | NEW (IDA, 9480849) | NEW | single-lab provenance flagged in `reason` |

Ontology checks run against the QuickGO ancestors endpoint on 2026-11-01:
`GO:0039693` ancestors include `GO:0016032` but **not** `GO:0006260`;
`GO:0033644` ancestors are `GO:0033643`/`GO:0044217`/`GO:0018995` and do **not**
include `GO:0016020`.

## Open questions carried into the review

- Does p1 act on replication only as a structural platform, or does the
  FtsZ/divisome association also time replication to the cell cycle?
- Is the mRNA-binding/translational-repression activity reproducible outside the
  Sophia lab, and is it a distinct function of the 6 kDa delta-1 form?
- No host-scoped GO term exists for "host cell division site / host FtsZ ring",
  which is where p1 actually concentrates; GO:0033644 is the closest available.
