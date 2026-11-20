# Bacillus phage phi29 gene 17 / protein p17 (UniProtKB:P03686)

Curation notes for the CACAO review project (batch 3, screen 1: adjacent-locus /
one-paper-many-genes).

**Method note.** No deep-research provider API keys exist in this container, so
`just deep-research` was not run and no `-deep-research-<provider>.md` file was
created. Everything below comes from the cached `publications/PMID_*.md` records,
NCBI E-utilities abstracts (papers then cached with `just fetch-pmid`), the
UniProt flat file, QuickGO and OLS.

**GONUTS is now retired, not merely offline.** `https://gowiki.tamu.edu/` returns
HTTP 410 with the page "GONUTS, the GO wiki, has been retired ... The GO wiki that
was at gowiki.tamu.edu is no longer online." The Wayback Machine has no snapshot of
`BPPH2:GP17` or of the `PMID:820555` paper page. The student-evidence check the
CACAO project plan relies on is therefore permanently unavailable, and the
abstract-only CACAO rows have to be judged under curator deference for good.

## What p17 is

A 166-residue early protein encoded by the first gene of phi29's right-side early
operon (the C2-promoter operon, which also contains gene 16.7), expressed very early
after infection and repressed later by p6 [PMID:17526715 "This operon contains genes
17 and 16.7 and four additional open reading frames"]. It is a homodimer with a
putative coiled-coil region and interacts with the viral architectural/origin-binding
protein p6 [PMID:12480935 "one hand, on the study of protein p17 dimerization and the
role of a putative"]. It is conserved across all phi29-like phages and was used as a
phylogenetic marker, described there as "an accessory component of bacteriophage DNA
replicating machinery" [PMID:9929388 "terminal proteins and of the gene 17 protein
product, an accessory component of"].

**p17 is not itself a membrane protein.** Within the right-side early operon only
gene 16.7 encodes one [PMID:17526715 "Interestingly, 16.7 appears to be the only gene
present in the right-side operon to encode a membrane protein"], and the
membrane-associated early replication protein of phi29 is p1, not p17
[PMID:15576790 "Protein p1 is a membrane-associated viral protein, proposed to attach
the viral genome to the cell membrane"]. p17 participates in processes that are
membrane-associated (in vivo phi29 replication, the pull step of ejection) without
being a membrane component itself, and UniProt P03686 carries no membrane keyword,
transmembrane feature or subcellular-location block. Phrasings that call p17
"membrane-associated" conflate it with p1 or p16.7.

## Role 1: viral DNA genome replication

The oldest evidence is the 1976 survey of phi29 gene products and functions, a bulk
nonsense-mutant screen: [PMID:820555 "Mutants in six genes do not synthesize phage
DNA."]. The abstract does not name the six, but the same laboratory named them seven
years later while describing the mutant extracts it used: [PMID:6402761 "extracts from
B. subtilis infected with phi29 mutants in genes 2, 3, 5, 6 and 17, involved in DNA
synthesis, have been used"]. With gene 1, which also carries a DNA-replication
annotation from the 1976 paper, that is the set of six. Gene 17 is therefore genuinely
one of the DNA-synthesis cistrons of PMID:820555, and the attribution is independent of
anything in the abstract. Later work restates it as settled: [PMID:10650217 "Gene 17 of
Bacillus subtilis bacteriophage Phi29 is an early gene playing a role"] in DNA
replication; and [PMID:9858710 "The gene 17 of the Bacillus subtilis phage phi29 is
known to be involved in the"] viral DNA replication in vivo.

The same 1983 in vitro work shows the role is *not* in the initiation reaction itself:
the p3-dAMP initiation complex forms without p17 [PMID:6402761 "The products of genes
5, 6 and 17 do not seem to be needed in the formation of the initiation complex"].

The direct evidence is Crucitti et al. 1998, which cloned gene 17, purified p17 and
showed a stimulatory effect in vitro: [PMID:9858710 "A stimulatory effect of protein p17
was demonstrated under in vitro conditions required to amplify phi29 DNA"], specifically
"starting with a low amount of input DNA". In vivo the requirement is conditional on
multiplicity of infection — [PMID:9858710 "protein p17 is required when phage infection
occurs at a low multiplicity of infection (moi), which is probably the natural condition
for infection, but is"] dispensable at high moi — with the proposal that p17 recruits
limiting initiation factors at the origins early in infection and becomes dispensable
once the other replication proteins reach optimal concentration.

The mechanism proposed from the 2003 interaction study is that p17 acts through p6:
[PMID:12480935 "p17 function is to optimize binding of protein p6 at the viral DNA ends,
thus"] favouring initiation of replication and negatively modulating its own
transcription. In vivo this is supported by chromatin immunoprecipitation in
sus17-infected cells, where p6 binding is reduced along the whole genome; the authors'
own reading is topological and therefore indirect [PMID:15576790 "proteins p1 and p17
could be required to restrain the proper topology of phi29 DNA"].

Importantly, the replication role survives controlling for the ejection defect below:
[PMID:17526715 "the absence of p17 was also shown to drastically affect the level of φ29
DNA replication once the entire sus17 genome was internalized"].

## Role 2: the pull step of phi29 genome ejection into the host

Not represented in GOA at all, and the better-documented of p17's two roles. phi29
injects its linear genome right-to-left in two steps; the first ~65% is pushed in by
capsid pressure, and the remainder is actively pulled in by machinery that includes p17:
[PMID:15066038 "second step at least one of the viral early proteins, p17, participates
in the"] molecular machinery that pulls the remaining DNA inside the cell. The pull step
needs an electrochemical proton gradient, and p17 is where the energy enters:
[PMID:16517096 "p17 suggests that this protein is essential for energy transduction"],
in a motor "that comprises at least viral protein p17, encoded by the right early
operon". X-ChIP measurements of left-end internalisation in non-p6-producing cells
confirm it and rank it against p16.7: [PMID:17526715 "These results corroborate earlier
findings that protein p17 is required for efficient ejection of the left half of the φ29
genome"], and the absence of p16.7 "affects the pull step less drastically than the
absence of protein p17".

This is participation, not mere necessity: p17 is a component of the pulling machinery
and the energy-transduction step is attributed to it, with azide having no effect in its
absence.

## Reading of the four GOA rows

| term | code | reference | assigned by |
|---|---|---|---|
| GO:0006260 DNA replication | IEA | GO_REF:0000043 (KW-0235) | UniProt |
| GO:0039693 viral DNA genome replication | IDA | PMID:9858710 | UniProt |
| GO:0039693 viral DNA genome replication | IEA | GO_REF:0000120 (IPR035184, KW-1194) | UniProt |
| GO:0039693 viral DNA genome replication | IMP | PMID:820555 | CACAO |

GO:0006260 is not an ancestor of GO:0039693 (checked against QuickGO's is_a/part_of
ancestor set for GO:0039693: GO:0006259, GO:0071897, GO:0019079, GO:0141187 and up, no
GO:0006260), so the keyword row is a lateral, less informative statement of the same
claim rather than a strict parent restatement. MODIFY to GO:0039693, which the gene
already carries three times.

## The predicted failure shape (screen 1), tested

Prediction: PMID:820555 is a multi-gene survey cited across most of phi29's numbered
genes, so gene 17's CACAO row might be the T4 gp5.4 shape — one paper's finding
misattributed to a neighbouring numerically-named gene.

**Absent.** The paper's "six genes" really do include gene 17, named by the same
laboratory in PMID:6402761, and the claim is confirmed by three later papers. The
abstract is the only thing that is silent; the attribution is not a guess.

What the full CACAO row set for phi29 does show (QuickGO, `assignedBy=CACAO`,
`taxonId=2884424`, 24 rows) is a single Feb–Apr 2025 campaign that read PMID:820555
once and distributed it across the phage:

- GO:0039693 IMP on genes 1, 2, 3, 6 and 17 — the DNA-synthesis cistrons, correct;
- GO:0044659 viral release from host cell by cytolysis IMP on genes 4 *and* 15, from a
  paper whose abstract reports **one** such cistron ("A cistron, probably involved in
  the final lysis of the infected bacteria, has been found"). Gene 15 is the endolysin;
  gene 4 is the late-gene transcription activator. That pair, not gene 17, is where this
  paper's one-to-many distribution looks over-extended; it belongs to the gene 4 review.
- Every 2025-dated phi29 row (10 of them) carries
  `acts_upstream_of_or_within_positive_effect`, while the same organism's 2012–2017 rows
  use `involved_in`/`enables`/`part_of`. So screen 3's qualifier shape is present here
  as a campaign-wide habit — but on this gene it is the *defensible* choice, not a
  defect: the evidence is a bulk nonsense-mutant screen with no demonstration of direct
  participation, and the modern literature shows a large part of the sus17 replication
  defect is indirect (failed genome internalisation, altered DNA topology, reduced p6
  binding). The conservative qualifier is more honest here than `involved_in` would be.
