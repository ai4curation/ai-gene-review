# dehH1 (UniProtKB:Q7DI61, Delftia acidovorans) — curation notes

No deep-research provider was available for this review; the literature below was
assembled by hand from PubMed, PMC full text, UniProt and the PANTHER/PAINT data
already in this repository. This file is the journal for that work.

## 1. What the entry is

`Q7DI61_DELAC` is an **unreviewed (TrEMBL)** entry, 294 aa, derived from EMBL
`BAB85585.1` / `BAC81979.1`, gene `dehH1`, on plasmid pUO1 of *Delftia
acidovorans* strain B (NCBITaxon:80866). The record carries no EC number, no
curated comment blocks, and `PE 4: Predicted;`. Its only domain feature is
`AB hydrolase-1` (Pfam PF00561) spanning residues 27–276, and it is classified in
PANTHER `PTHR43798:SF33`.

Despite the bare record, this protein is one of the best-characterised C–F bond
cleaving enzymes in the literature. The key is that **the identical sequence also
exists as a curated Swiss-Prot entry**, `Q01398` / `DEH1_MORSB`.

## 2. Q7DI61 and Q01398 are the same protein (duplicate UniProt entries)

Both entries are 294 aa with identical CRC64 checksums
(`7BA7F07359182703`), identical sequence, the same gene name `dehH1` and the same
plasmid (`pUO1` / `POU1`); verified live against the UniProt REST API in
`dehH1-bioinformatics/` (see `RESULTS.md`, script `compare_entries.py`). They
differ only in organism name and taxon id:

| | Q7DI61 (TrEMBL) | Q01398 (Swiss-Prot) |
|---|---|---|
| entry name | `Q7DI61_DELAC` | `DEH1_MORSB` |
| organism | *Delftia acidovorans* (NCBITaxon:80866) | *Moraxella* sp. (strain B) (NCBITaxon:118147) |
| source EMBL | AB049198 / AB063332 | D90422 |
| EC | — | 3.8.1.3 |
| protein existence | Predicted (4) | Evidence at protein level (1) |

Strain B was originally described as *Moraxella* sp. and later reclassified; the
2002 plasmid paper describes the *same* two dehalogenase genes as being on
*Delftia acidovorans* plasmid pUO1 [PMID:11976102 "The two haloacetate
dehalogenase genes, dehH1 and dehH2, on the 65-kb plasmid pUO1 from Delftia
acidovorans strain B were found to be located on transposable elements."]. So the
two accessions are the same gene of the same strain deposited under the old and
the new organism name. This is recorded as a `source_defects` entry
(`defect_type: DUPLICATE_ENTRY`, resource `UNIPROT`) on the review.

The practical consequence for annotation is stark: Q01398 carries
`GO:0018785 haloacetate dehalogenase activity` (via its curated EC 3.8.1.3),
while the byte-identical Q7DI61 carries only `GO:0003824 catalytic activity`.
Nothing biological distinguishes them.

## 3. The enzyme: haloacetate dehalogenase H-1 / fluoroacetate dehalogenase

`dehH1` encodes haloacetate dehalogenase **H-1**, one of two unrelated
dehalogenases carried on the strain B plasmid. Kawasaki and colleagues sequenced
both genes and showed they share no homology, and that the two enzymes differ in
substrate range [PMID:1512562 "H-1 predominantly acts on fluoroacetate,"] —
whereas H-2 (`dehH2`, a HAD-superfamily 2-haloacid dehalogenase, UniProtKB:Q7DI63)
does not act on fluoroacetate. The same paper notes that DehH1's sequence
resembles the *Xanthobacter autotrophicus* haloalkane dehalogenase, placing it in
the alpha/beta-hydrolase fold, not the HAD superfamily.

The reaction is **hydrolytic** C–X bond cleavage: haloacetate + H2O → glycolate +
halide (EC 3.8.1.3, GO:0018785). Cleaving the C–F bond of fluoroacetate is the
distinguishing feature; this bond is among the strongest in organic chemistry
[PMID:15063312 "catalyzes cleavage of the carbon-fluorine bond of fluoroacetate,
whose dissociation energy is among the highest found in natural products."].

### Mechanism

The enzyme uses the canonical alpha/beta-hydrolase two-step mechanism with an
aspartate nucleophile. Working on the Moraxella sp. B enzyme — i.e. this protein
— Liu et al. showed by H2-18O turnover and tandem MS that Asp105 is the
nucleophile that displaces the halide and forms a covalent ester intermediate
[PMID:9812982 "Asp-105 was labeled with two 18O atoms."], and that His272 is the
base catalyst that activates water to hydrolyse that intermediate: an H272N
mutant was inactive yet still became alkylated by substrate [PMID:9812982 "mutant
enzyme was covalently alkylated with the substrate."]. Asp105 is essential;
replacing it with Asn abolishes dehalogenation, and the apparent residual activity
of the D105N mutant is due to deamidation regenerating wild-type enzyme
[PMID:15063312 "Asn105 of the fluoroacetate dehalogenase D105N mutant did not
function as a nucleophile to catalyze the dehalogenation."].

Both residues are present in the Q7DI61 sequence, Asp105 on a textbook nucleophile
elbow (G-H-**D**-R-G) — see `dehH1-bioinformatics/RESULTS.md`. There is no reason
to treat this entry as a degenerate or pseudoenzymatic copy.

### Substrate range beyond fluoroacetate

Dodge et al. re-purified the enzyme (expressed from a codon-optimised synthetic
gene) and compared it head-to-head with the well-studied *Rhodopseudomonas
palustris* FAcD, finding it the better catalyst with a wider substrate range
[PMID:38063407 "A soluble hydrolytic defluorinase from Delftia acidovorans
(formerly Moraxella sp.) strain B (28) and the well-studied FAcD from R. palustris
ATCC BAA-98 (15) were purified and compared, and the former was shown to be more
suitable due to higher reaction rates and broader substrate specificity."]. It
defluorinates non-natural 2-fluorocarboxylic acids — alpha-fluorophenylacetic acid
and 2-fluoropropionic acid — stereoselectively [PMID:38063407 "The Delftia enzyme
defluorinated α-fluorophenylacetic acid and 2-fluoropropionic acid, allowing us to
avoid the use of fluoroacetate, which is itself highly toxic."]. Chlorofluoroacetic
acid is also a substrate but the slowest one, and did not support growth.

## 4. Localization: the enzyme is soluble, not a membrane protein

GOA gives Q7DI61 `GO:0016020 membrane` (IEA, GO_REF:0000118, TreeGrafter, source
node `PANTHER:PTN008685326`). This is a propagation artefact:

- PTHR43798 is a very broad alpha/beta-hydrolase superfamily family (164,495
  members, 13 subfamilies per `interpro/panther/PTHR43798/PTHR43798-metadata.yaml`).
  The only `GO:0016020` IBD nodes in `PTHR43798-paint.tsv` are `PTN000177089`
  (seeded by `UniProtKB:P07000`, `SGD:S000001577`, `MGI:MGI:1346042`,
  `AGI_LocusCode:AT1G52760`, `UniProtKB:Q57U43`) and `PTN001661081` (seeded by
  `MGI:MGI:1913332`) — all **lipid-acting** enzymes (lysophospholipases,
  monoacylglycerol lipases) whose membrane association follows from acting on
  membrane lipids.
- DehH1 acts on a small, freely water-soluble carboxylic acid. The membrane
  association of the lipase branch has no reason to transfer with the fold.
- Dodge et al. describe it explicitly as a **soluble** enzyme and as acting in the
  **cytoplasm** [PMID:38063407 "Strain 12663 cells expressing the cytoplasmic
  Delftia defluorinase recombinantly grew on the fluorinated compounds and reached
  fluoride levels in the medium up to 50 mM."] — the entire premise of that paper
  is that fluoride is released *inside* the cell.
- Neither UniProt entry carries a signal peptide, transmembrane feature or lipid
  anchor, and a hydropathy screen finds no candidate TM segment
  (`dehH1-bioinformatics/RESULTS.md`).

So `GO:0016020` is removed, and `GO:0005737 cytoplasm` proposed in its place as a
`NEW`/IC row. The same wrong membrane row sits on Q01398, so the defect is
reported once against the TreeGrafter propagation rather than against this entry
alone.

## 5. What was deliberately *not* proposed

**No biological-process term.** It is tempting to add a haloacetate or
organofluorine catabolic process term, since DehH1 performs the first step that
lets strain B grow on haloacetate. Two things argue against it:

- GO has no fluoroacetate- or haloacetate-catabolism process term.
  `GO:0042206 halogenated hydrocarbon catabolic process` is defined over
  compounds "derived from hydrocarbons by replacing one or more hydrogen atoms
  with halogen atoms"; haloacetate is a halogenated carboxylic acid, and forcing
  it under that term would overstate the fit.
- Comparator check, per the `NEW` bar in CLAUDE.md. Of the 690 proteins carrying
  `GO:0018785`, the ones with the strongest evidence carry **no** process term:
  *R. palustris* FAcD `UniProtKB:Q6NAM1` has `GO:0018785` by EXP
  (PMID:21510690) and only MF rows; the (S)-2-haloacid dehalogenase
  `UniProtKB:Q53464` likewise has MF rows only; `UniProtKB:Q01398`, this same
  protein, has none. A systematic absence across well-studied dehalogenases is a
  curation convention, not an oversight to fill in.

This is recorded as a `suggested_questions` item instead.

**No fluoroacetate-specific MF term.** GO has no `fluoroacetate dehalogenase
activity` class; `GO:0018785 haloacetate dehalogenase activity` is the EC 3.8.1.3
term and covers the activity, including on fluoroacetate. No new term is proposed:
the existing one is adequate, and the fluorine preference is a specificity fact
better captured in `core_functions` prose than as a new class.

## 6. Checking CMMMech's claims about this protein

`/home/user/CMMMech/data/records/fluorine.yaml` grounds its
`recombinant_putida_defluorination` mechanism to `UniProtKB:Q7DI61`. Checked
against UniProt and the cited paper (Dodge et al. 2024, PMID:38063407):

**Correct.** The accession, entry name, entry status (TrEMBL), organism and
taxon id, protein name, gene symbol, InterPro ids (IPR000073, IPR029058,
IPR050266, IPR000639) and Pfam id (PF00561) all match the UniProt record. The
functional role — hydrolytic C–F cleavage of alpha-fluorophenylacetic acid and
2-fluoropropionic acid to mandelate/lactate plus fluoride, heterologously
expressed in *Pseudomonas putida* — is what the paper reports, and EC 3.8.1.3 is
correct for DehH1 (it is on the duplicate Swiss-Prot entry Q01398).

**Two provenance claims are not supported by the cited paper.** Both appear in
the `evidence.explanation` for Q7DI61 (and again for Q7DI63):

1. *"Purified from Delftia acidovorans strain B"*. Dodge et al. did not purify
   from *Delftia*. They synthesised a codon-optimised gene from the published
   sequence and purified the His-tagged product from a recombinant host
   [PMID:38063407 "Amino acid sequences of fluoroacetate dehalogenases from
   Rhodopseudomonas palustris strain CGA009 (RPA1163) (GenBank accession
   OPF91568.1) or Delftia acidovorans strain B (formerly Moraxella sp. strain B)
   (GenBank accession BAC81979.1) were used to generate codon-optimized gene
   sequences for expression in Pseudomonas putida"], specifically
   [PMID:38063407 "the Rhodopseudomonas and Delftia enzymes were purified from
   their E. coli BL21(DE3) or P. putida ATCC 12633 expression host,
   respectively."].
2. *"sequenced by LC-MS/MS in Dodge et al. (2024)"*. The paper contains no
   LC-MS/MS protein identification; the enzyme's identity rests on the GenBank
   accession used to design the synthetic gene. (The protein *was* sequenced, but
   by Edman degradation of material purified from the native strain, three decades
   earlier — PMID:1512562.)

Neither error changes the grounding: `BAC81979.1` is one of the two EMBL
cross-references of Q7DI61, so the accession assignment is right. They are
provenance wording to correct in the CMMMech record. Per the brief these are
CMMMech-side issues, so they are reported here and in the PR, **not** as
`source_defects` (which are reserved for GOA/UniProt/InterPro).

**One further CMMMech observation, on the sibling protein** (Q7DI63, reviewed
separately by another agent, so only noted): its `protein_name` and `ec_numbers`
say `(S)-2-haloacid dehalogenase` / `EC:3.8.1.2`, while its `functional_role` in
the same block says `Haloacetate dehalogenase H-2 (EC 3.8.1.3; dehH2)`. The two
EC numbers are inconsistent with each other within one entry.

**Finally**, CMMMech could usefully note that Q7DI61 is a TrEMBL duplicate of the
curated Q01398, which is the entry that actually carries the EC number, the
catalytic-site features and the protein-level evidence — and which is the
accession Dodge et al. themselves cite for the AlphaFold model
[PMID:38063407 "The pre-existing AlphaFold (37, 38) structure of the Delftia
defluorinase (UniProt accession Q01398) was used for modeling interactions between
the enzyme and different fluorinated ligands."]. Grounding to the Swiss-Prot entry
(or to both) would be stronger.

## 7. Annotation decisions

| Term | Evidence | Action | Why |
|---|---|---|---|
| GO:0003824 catalytic activity | IEA (InterPro) | MODIFY → GO:0018785 | true but maximally uninformative; the specific EC 3.8.1.3 activity is experimentally established for this exact sequence |
| GO:0016020 membrane | IEA (TreeGrafter) | REMOVE | lipase-branch propagation; enzyme is soluble/cytoplasmic |
| GO:0005737 cytoplasm | IC (new) | NEW | replaces the removed membrane call |

`GO:0018785` is introduced as the replacement term on the `GO:0003824` row rather
than as a separate `NEW` row, so the review asserts it once.
