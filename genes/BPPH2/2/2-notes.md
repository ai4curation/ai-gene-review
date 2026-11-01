# Bacillus phage phi29 gene 2 (DNA polymerase, p2 / gp2) - curation notes

UniProt: P03680 (DPOL_BPPH2), 575 aa, `PE 1: Evidence at protein level`.
Taxon: NCBITaxon:2884424, *Bacillus phage phi29*. Host: *Bacillus subtilis*.

**Provenance caveat.** No deep-research API keys exist in this container, so
`just deep-research` was not run and there is no `2-deep-research-*.md` file.
The literature below was assembled directly: from the cached publications in
`publications/`, from the curated UniProt record (which cites ~50 primary
papers on this protein), and from PubMed/EuropePMC lookups. Every cached
publication used here is **abstract-only** (`full_text_available: false`)
except PMID:16511564.

## What the protein is

phi29 DNA polymerase is the single-subunit, 575-residue family-B
("alpha-like") replicase that carries out the whole of phi29 genome
replication. UniProt gives it two EC numbers, each with experimental
evidence: EC 2.7.7.7 from PMID:3863101 and EC 3.1.11.- from PMID:2790959
[file:BPPH2/2/2-uniprot.txt "EC=2.7.7.7 {ECO:0000269|PubMed:3863101};"].

Three catalytic activities in one chain, per the curated FUNCTION line
[file:BPPH2/2/2-uniprot.txt "This polymerase possesses three enzymatic
activities: DNA synthesis (polymerase), primer terminal protein (TP)
deoxynucleotidylation, which is the formation of a covalent linkage
(phosphoester) between the hydroxyl group of a specific serine residue in TP
and 5'-dAMP, a reaction directed by the second T at the 3' end, and 3' to 5'
exonuclease activity"]:

1. **DNA-templated DNA polymerisation.** Highly processive and strand
   displacing with no accessory proteins: >70 kb products on primed M13
   [PMID:2498321 "the phi 29 DNA polymerase is able to synthesize DNA chains
   greater than 70 kilobase pairs"], and
   [PMID:2498321 "the phi 29 DNA polymerase is highly processive in the
   absence of any accessory protein; 2) the polymerase itself is able to
   produce strand displacement coupled to the polymerization process"]. The
   crystal structure explains both: a tunnel too narrow for duplex DNA forces
   strand separation ahead of the active site, and the enzyme encircles both
   downstream template and upstream duplex
   [PMID:15546620 "This tunnel is too small to accommodate double-stranded DNA
   and requires the separation of template and nontemplate strands"],
   [PMID:15546620 "The high processivity of phi29 DNA polymerase may be
   explained by its topological encirclement of both the downstream template and
   the upstream duplex DNA"].
2. **Terminal-protein deoxynucleotidylation (protein-primed initiation).**
   The polymerase forms a heterodimer with free terminal protein p3 and
   covalently attaches the first dAMP to the hydroxyl of p3 Ser-232. This is
   catalysis performed *by the polymerase*, on a protein acceptor, and it
   happens even without DNA
   [PMID:1730646 "the phi 29 DNA polymerase, in the absence of DNA, is able
   to catalyze the formation of a covalent complex between the phi 29 terminal
   protein (TP) and 5'-dAMP"], with the same linkage chemistry and the same
   Ser232/YCDTD-motif requirements as genuine initiation
   [PMID:1730646 "the same specificity for TP Ser232 as the OH donor and the
   involvement of the YCDTD amino acid motif"]. Initiation is directed by an
   internal template thymine, with sliding-back recovery of the terminal
   nucleotides [PMID:19011105 "the DNA polymerase, in a template-instructed
   reaction, adds 5'-dAMP to a molecule of terminal protein (TP) to form the
   initiation product TP-dAMP"]. The polymerase:TP structure shows the TP
   priming domain occupying the cleft duplex DNA will later use, which is
   also why initiation is confined to the genome ends
   [PMID:16511564 "a third domain containing the priming serine occupying the
   same binding cleft in the polymerase as duplex DNA does during elongation"],
   [PMID:16511564 "this heterodimer of polymerase and terminal protein cannot
   accommodate upstream template DNA, thereby explaining its specificity for
   initiating DNA synthesis only at the ends of the bacteriophage genome"].
   **GO has no molecular function term for this activity.** Searches of
   QuickGO found only `GO:0018175 protein nucleotidylation` (a BP) and
   `GO:0018117 protein adenylylation`; neither is a nucleotidyltransferase MF
   and neither is template-directed. Filed as `proposed_new_terms`.
3. **3'-5' exonuclease / proofreading.** A separate N-terminal active site,
   identified by site-directed mutagenesis of the conserved Exo motifs
   [PMID:2790959 "Site-directed mutagenesis at the predicted exonuclease
   active site of the phi 29 DNA polymerase, a model enzyme for prokaryotic
   and eukaryotic alpha-like DNA polymerases, specifically
   inactivated the 3'----5' exonuclease activity of the enzyme"]. UniProt localises it to
   residues 1-191 [file:BPPH2/2/2-uniprot.txt "The N-terminus contains the
   3'-5' exonuclease activity and strand displacement ability"], and editing
   is intramolecular, the primer travelling between the two active sites
   without dissociating [file:BPPH2/2/2-uniprot.txt "DNA polymerase edits the
   polymerization errors using an intramolecular pathway as the primer
   terminus travels from one active site to the other without dissociation
   from the DNA"]. The substrate is a free 3' terminus of single-stranded
   DNA, and separate metal sites serve the two activities
   [PMID:1310035 "The results obtained support the existence of independent
   metal binding sites for the synthetic and degradative activities of phi 29
   DNA polymerase"].

Mg2+ is the cofactor, with eight curated `FT BINDING` sites (145, 169, 249,
250, 456, 458), several marked catalytic and backed by PDB 1XI1/2PYJ and by
PMID:9784372. Protein-primed initiation specifically prefers Mn2+
[PMID:1310035 "the initiation of DNA polymerization using a protein as a
primer, a special synthetic activity carried out by phi 29 DNA polymerase,
exhibited a strong preference for Mn2+ as metal activator"].

## The two CACAO papers

Both are abstract-only in the cache, and both are **multi-gene phi29 survey
papers** shared with other numerically-named phi29 entries (`grep` over
`genes/BPPH2/*/*-goa.tsv`: PMID:820555 is cited on genes 1, 2, 3, 4, 6 and
15; PMID:6402761 on genes 2 and 3).

- **PMID:6402761** (Blanco, Garcia, Penalva & Salas 1983, NAR) is *titled*
  for this gene and its headline result is about this gene
  [PMID:6402761 "The formation of the initiation complex is completely
  dependent on the presence of a functional gene 2 product, in addition to
  protein p3 and phi29 DNA-protein p3 as template."]. The design is
  mutant-extract complementation
  [PMID:6402761 "extracts from B. subtilis infected with phi29 mutants in
  genes 2, 3, 5, 6 and 17, involved in DNA synthesis, have been used"], which
  is what makes IMP the right evidence code. The paper also *excludes* genes
  5, 6 and 17 from the initiation step, so it is a differentiating survey, not
  a blanket one [PMID:6402761 "The products of genes 5, 6 and 17 do not seem
  to be needed in the formation of the initiation complex."].
- **PMID:820555** (Carrascosa et al. 1976, Eur J Biochem) is the cistron-to-
  protein mapping paper [PMID:820555 "Mutants in six genes do not synthesize
  phage DNA."], [PMID:820555 "The protein products of 10 out of the 17
  cistrons detected in the genome of phage phi29 have been identified."]. It
  does not name gene 2 in the abstract, but gene 2 is beyond question one of
  the DNA-synthesis cistrons: the companion in vitro work used gene 2 mutant
  extracts and showed the requirement directly (PMID:6402761), and the
  purified protein alone replicates the genome (PMID:3863101).

The third CACAO row re-uses PMID:6402761 for the same term with a different
ECO refinement: `ECO:0007161` nonsense mutation phenotypic
evidence (2025-02-08) and `ECO:0006099` temperature-sensitive mutant
phenotypic evidence (2025-02-17). Both collapse to IMP in the GAF. phi29 has both *sus* (nonsense)
and *ts* mutant collections, and PMID:2118623 is specifically about ts mutants
of this polymerase, so the two rows may record two mutant classes in the same
paper rather than a duplicate; the abstract does not say which mutants were
used, and the full text is unavailable (EuropePMC returns a 500 for PMC325798;
the 1983 PMC copy is scanned images).

**GONUTS is now retired, not offline.** `gowiki.tamu.edu` returns HTTP 410
with "GONUTS, the GO wiki, has been retired" and "The GO wiki that was at
gowiki.tamu.edu is no longer online." The Internet Archive has no snapshot of
either the protein page or the per-paper pages (`archive.org/wayback/available`
returns `{"archived_snapshots": {}}` for both
`.../Bacillus_phage_phi29:2` and `.../PMID:6402761`). So the figure-level
evidence behind every abstract-only CACAO row in this project is now
permanently unverifiable, and the CACAO.md note that the check should be
re-tried "when GONUTS returns" needs updating.

## Qualifiers

All three CACAO rows carry `acts_upstream_of_or_within_positive_effect`. This
gene product *performs* replication initiation and genome replication: it is
the enzyme that makes the phosphodiester bonds and the TP-dAMP linkage, and
UniProt's own rows for the same process use `involved_in`
(`2-goa.tsv`: `involved_in GO:0039693 ... IDA ... UniProt`). `involved_in` is
the correct qualifier; recorded as a `WRONG_QUALIFIER` source defect on each
of the three rows, exactly as for AcrIIA5 in batch 2.

## An InterPro2GO defect

IPR014416 "DNA-directed DNA polymerase, family B, phi29-like virus" maps to
`GO:0001882 nucleoside binding` (checked against the InterPro API). In GO,
nucleoside binding is **not** an ancestor of nucleotide binding: `GO:0000166`
sits under `GO:1901265 nucleoside phosphate binding`, while `GO:0001882`
descends from `GO:0097367 carbohydrate derivative binding` and its children
are all unphosphorylated nucleosides (`GO:0032546 deoxyribonucleoside
binding` etc., checked via QuickGO ancestors/descendants). The polymerase
binds dNTPs, not nucleosides; nothing in the literature or in the curated
`FT BINDING` features (5-methyl-UTP at 254, 371, 383, 458) shows nucleoside
binding. The mapping looks like a slip for nucleotide binding and propagates
to every phi29-like family-B polymerase. Filed as a `source_defects` entry
against InterPro.

Separately, GO offers no generic "deoxyribonucleoside triphosphate binding"
term, so `GO:0000166 nucleotide binding` is the most specific statement
available for the dNTP site; raised in `suggested_questions`.

## Relation to the rest of the phage

Protein-primed replication needs only p2 and p3 in vitro
[PMID:3863101 "A system that replicates bacteriophage phi 29 DNA with protein
p3 covalently attached to the two 5' ends, using as the only proteins the phi
29 DNA polymerase and the terminal protein, is described."], and the same
paper shows p2 is responsible for both the initiation complex and elongation
to full length [PMID:3863101 "the phi 29 DNA polymerase functions, not only
in the formation of the p3-dAMP covalent initiation complex but also in the
elongation of the latter, as the only DNA polymerase to produce full-length
phi 29 DNA"]. Host DNA polymerase III, gyrase and RNA polymerase inhibitors do
not affect initiation [PMID:6402761 "Inhibitors of the host DNA polymerase
III, DNA gyrase or RNA polymerase had no effect on the formation of the
protein p3-dAMP complex"], so the phage replicase is genuinely autonomous.
In vivo, p5 (SSB) and p6 (nucleoid protein) stimulate replication, but
neither is needed for initiation (PMID:6402761, above).

## Term choices made in the review

- `GO:0003887` is the canonical MF; the ancestors `GO:0034061`, `GO:0016779`
  and `GO:0016740` are modified to point at it. `GO:0008310 single-stranded
  DNA 3'-5' DNA exonuclease activity` replaces the three hydrolytic
  keyword rows (`GO:0004518`, `GO:0004527`, `GO:0016787`).
- `GO:0006260 DNA replication` is modified to `GO:0006270` plus `GO:0006271
  DNA strand elongation involved in DNA replication`, both descendants and
  both separately shown for this protein in PMID:3863101. `GO:0039693` is
  **not** a descendant of `GO:0006260` (checked with QuickGO ancestors), so it
  does not by itself make that row redundant.
- One `NEW` row is proposed: `GO:0045004 DNA replication proofreading`,
  defined as "Correction of replication errors by DNA polymerase using a
  3'-5' exonuclease activity". The comparator check (QuickGO) shows the term
  is annotated to the proofreading exonucleases and polymerases of other
  systems (dnaQ, polC), i.e. to gene products in the same role, so its
  absence here is a gap rather than a convention. GOA records the activity
  but not the process it serves.
- No GO-CAM model and no module touches this gene (`gocams/index.tsv` holds
  no phi29 entry).
