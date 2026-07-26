# AADACL2 (Q6P093) — review notes

Human arylacetamide deacetylase-like 2, HGNC:24427, chromosome 3, 401 aa, `PE 1: Evidence at
protein level`, Pharos `Tdark`. Reviewed 2026-07-25 for the PAINT + affinage campaign.

## What the record contains

Seven GOA rows, **no experimental evidence of any kind**: 2 IBA (PANTHER) and 5 IEA
(InterPro ×2, ARBA ×2, UniProt SubCell ×1). Three rows are activities at three levels of
generality; three are locations, two of which are mutually exclusive.

| term | evidence | source |
|---|---|---|
| GO:0016787 hydrolase activity | IBA | PANTHER PTN009058710 (+16 protein sources) |
| GO:0016020 membrane (`is_active_in`) | IBA | PANTHER PTN009058713, AADAC, mouse Aadac, mouse Nceh1 |
| GO:0003824 catalytic activity | IEA | ARBA:ARBA00027533 |
| GO:0005576 extracellular region | IEA | UniProtKB-SubCell:SL-0243 |
| GO:0016020 membrane (`located_in`) | IEA | ARBA:ARBA00028763, InterPro:IPR017157 |
| GO:0016787 hydrolase activity | IEA | InterPro:IPR013094 (Alpha/beta hydrolase fold-3) |
| GO:0052689 carboxylic ester hydrolase activity | IEA | InterPro:IPR017157 (Arylacetamide deacetylase) |

## Literature: genuinely absent for function, present for genetics

PubMed returns 6 hits for `AADACL2`; none characterises the protein. The affinage record came
back empty (`n_discoveries: 0`, `citation_count: 0`, `gates_passed: True`), and in this case
the emptiness is corroborated rather than taken on trust — the only literature statement
about AADACL2's function is that there isn't one:

- [PMID:35736449 "The AADAC family comprises five members, including AADAC and four AADAC-like (AADACL1-4) proteins."]
- [PMID:35736449 "all other members of the AADACL protein family, AADACL2, AADACL3, and AADACL4, have so far been only poorly investigated and no functional roles can be concluded"]

The three UniProt `RN` references are all large-scale sequencing (PMID:17974005 German cDNA
consortium, which supplied isoform 2; PMID:16641997 chromosome 3; PMID:15489334 MGC, which
supplied the Ser-186 variant). None assays the protein. Note the campaign rule: `PE 1` means
the protein is *detected*, so the honest statement is that there are no
functional/biochemical data, not that there are no data.

Two genetic associations exist and neither supports a GO annotation:

- Psoriasis exome-indel screen in 32,043 Chinese Han individuals:
  [PMID:31078570 "identified KIAA0319, RELN, NCAPG, ABO, AADACL2, LMAN1, FLG, HERC5, CCDC66, LEKR1, AFF3, ABCG2, ANXA7, SYTL2,GIPR, METTL1, and FYCO1 as unreported genes for psoriasis"]
- SIREN ischemic-stroke GWAS in indigenous Africans:
  [PMID:38317187 "We observed genome-wide significant (P-value < 5.0E-8) SNPs associations near AADACL2 and miRNA (MIR5186) genes in chromosome 3"], with
  [PMID:38317187 "The putative genes near AADACL2, MIR5186, and MIR4458 genes were protective and novel"]

The stroke signal is explicitly *near* the gene, not in it. A skin-expressed gene surfacing
in a psoriasis screen is at least tissue-coherent; a locus association is not a function.

## Family context

AADAC is the characterised member: a liver/intestine enzyme that hydrolyses both amide bonds
of arylacetamide xenobiotics and ester bonds of diglycerides, and it is
[PMID:35736449 "AADAC is a type II membrane glycoprotein, facing with its active side to the lumen of the endoplasmic reticulum (ER)"].
AADACL1/NCEH1/KIAA1363 is the other characterised member and is likewise membrane-anchored:
[PMID:35736449 "KIAA1363 contains a putative N-terminal transmembrane domain consisting of a 23 amino acid"]-long
hydrophobic stretch. The review also notes
[PMID:35736449 "the conserved structural homologies of the catalytic domain of KIAA1363, as well as AADAC to that of HSL"]
(hormone-sensitive lipase) — the GDXG / HSL-like α/β-hydrolase clan that AADACL2 belongs to
per [file:human/AADACL2/AADACL2-uniprot.txt "Belongs to the 'GDXG' lipolytic enzyme family."].

Expression: HPA reports AADACL2 as skin-restricted (`Tissue enriched (skin)`,
"detected in single", 10.1 nTPM in skin) — the most tissue-restricted member of the family
after AADACL4. AADACL3 is also skin/placenta-expressed, so the paralogous cluster looks like a
skin-associated expansion of the AADAC family.

## Three things worth curating

### 1. The activity is real machinery, not a fold-derived label

The campaign's standing warning is that a domain's *name* becomes an activity in GO. The
mirror-image error is to dismiss such a call without checking the residues. Here the residues
are present:
[file:human/AADACL2/AADACL2-uniprot.txt "FT   ACT_SITE        189"], 341 and 371 (Ser-Asp-His),
an oxyanion-hole motif at
[file:human/AADACL2/AADACL2-uniprot.txt "FT   MOTIF           111..113"], a `GDSSG` nucleophile
elbow at 187-191, a conserved 116-338 disulfide, and a PROSITE `PS01174` GDXG-lipase-serine
match. The reciprocal alignment test in
[file:human/AADACL2/AADACL2-bioinformatics/RESULTS.md "Eight of the fifteen sources with annotated active sites map all three residues onto"]
AADACL2's own annotated triad. Those eight are the seven closest sources plus *M. tuberculosis*
LipN at 26.1% identity, and every source that fails lies at 26.5% identity or below, where the
global alignment loses register in the C-terminal half. They include three independently
characterised *M. tuberculosis* carboxylesterases and the 51.6%-identical human paralog AADAC.

That licenses **GO:0017171 serine hydrolase activity**, whose definition is exactly a serine
nucleophile activated by an acid/base proton relay. GOA currently gives AADACL2 only
`GO:0016787 hydrolase activity` and `GO:0003824 catalytic activity` from the mechanism side,
which is a strictly weaker statement than the protein's own feature table supports.

### 2. The PANTHER node placement is inverted, and it affects three genes

From `RESULTS.md` section 5: `GO:0017171` sits only at the ortholog-specific nodes
`PTN002745055` (AADAC) and `PTN002745068` (NCEH1), so AADACL2/3/4 inherit no mechanism term.
What they *do* inherit at the shared family node `PTN009058713` is `GO:0016020 membrane`.
This is backwards with respect to what transfers safely: the catalytic triad is conserved in
all five human members; the type-II signal anchor is not (12 of the 14 reviewed `IPR017157`
entries carry one, and AADACL2 is the only one whose equivalent segment is annotated as a
cleaved signal peptide instead). Moving `GO:0017171` down to
`PTN009058713` and dropping `GO:0016020` from it would correct AADACL2, AADACL3 and AADACL4
in one edit.

### 3. Where I stopped short: the localisation is genuinely unresolved

My first read was "membrane is a paralog artefact; secreted is right". Measurement did not
support that, and this is recorded here so the reasoning is auditable:

- UniProt's cleavage site (after residue 18) puts **His at -1**, which signal peptidase I
  essentially does not accept (-1 is small/neutral A/S/C/G/T in the great majority of sites).
- The hydrophobic core is *more* hydrophobic than AADAC's experimentally confirmed type-II
  signal anchor (peak KD-19 mean 1.94 vs 1.81), and the two N-termini are homologous over the
  whole segment with the same downstream `TP.PDN.EE.W` motif. Hydropathy cannot tell a
  cleaved signal peptide from a signal anchor here.
- HPA's predictor vote does put AADACL2 (and only AADACL2) in the secreted class, but the same
  HPA pipeline **fails to classify AADAC as a membrane protein**, so it cannot be used as
  independent corroboration.
- All four observed peptides lie in the catalytic domain (earliest residue 124). Mass
  spectrometry establishes expression and says nothing about the N-terminal fate.

So both `GO:0005576` and `GO:0016020` are unsupported computational readings of the same
segment, and neither can be accepted or removed on present evidence. Actions: `UNDECIDED` for
all three location rows, with the experiment that would settle it recorded in
`suggested_experiments`. Recording the *contradiction* is the deliverable here; picking a
winner would have been a guess dressed as a finding.

## Isoform note

Isoform 2 (Q6P093-3) replaces residues 47-53 and deletes 54-401, and UniProt flags it as
likely NMD-degraded:
[file:human/AADACL2/AADACL2-uniprot.txt "premature stop codon in the mRNA, leading to nonsense-mediated mRNA"]
decay. It cannot be catalytically active (it stops before Ser189), so no annotation should be
attributed to it. All annotations here concern isoform 1 (Q6P093-1), the MANE-Select product.

## Curiosity, not evidence

The UniProt record carries two DrugBank cross-references, `DB07814 Gibberellic acid` and
`DB07815 Gibberellin A4`. The plant gibberellin receptor GID1 is a derivative of this same
GDXG/HSL-like carboxylesterase clan, so these are almost certainly structure-similarity
mappings rather than any claim about human ligands. Not used for anything in the review.

## Actions taken

| term | evidence | action |
|---|---|---|
| GO:0016787 hydrolase activity | IBA | MODIFY → GO:0017171 serine hydrolase activity |
| GO:0016020 membrane (`is_active_in`) | IBA | UNDECIDED |
| GO:0003824 catalytic activity | IEA | MODIFY → GO:0017171 serine hydrolase activity |
| GO:0005576 extracellular region | IEA | UNDECIDED |
| GO:0016020 membrane (`located_in`) | IEA | UNDECIDED |
| GO:0016787 hydrolase activity | IEA | MODIFY → GO:0017171 serine hydrolase activity |
| GO:0052689 carboxylic ester hydrolase activity | IEA | ACCEPT |
