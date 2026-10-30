# HHAT (human, Q5VTY9) — curation notes

Working journal for the GO annotation review. PMIDs marked `[not cached]` are
not in this repository's `publications/` cache; for those I record only what a
machine-readable source (UniProt entry, QuickGO annotation row, PANTHER PAINT
slice, cached Reactome entry) states, and I do not quote them.

## 1. What the protein is

HHAT (Hedgehog acyltransferase, UniProt Q5VTY9, HGNC:18023, 493 aa, chromosome
1) is a polytopic endoplasmic-reticulum membrane enzyme of the membrane-bound
O-acyltransferase (MBOAT) superfamily. UniProt's recommended name is
**Protein-cysteine N-palmitoyltransferase HHAT**, and UniProt assigns it to the
"membrane-bound acyltransferase family, HHAT subfamily"
[file:human/HHAT/HHAT-uniprot.txt "Belongs to the membrane-bound acyltransferase family. HHAT"].
PANTHER places it in family PTHR13285 (official name `ACYLTRANSFERASE`),
subfamily PTHR13285:SF20 `PROTEIN-CYSTEINE N-PALMITOYLTRANSFERASE HHAT`
(`interpro/panther/panther.obo`,
`interpro/panther/PTHR13285/PTHR13285-entries.csv`). The same family holds
Drosophila Rasp (Q9VZU2, subfamily SF18), the HHAT paralog HHATL (Q9HCP6,
SF19), the yeast MBOATs GUP1/GUP2, and the bacterial DltB/AlgI acyltransferases.

Topology: ten transmembrane domains plus two reentrant loops, with the catalytic
His and Asp on opposite faces of the ER membrane
[PMID:25505265 "We show that HHAT is comprised of ten transmembrane domains and
two reentrant loops with the critical His and Asp residues on opposite sides of
the endoplasmic reticulum membrane."], and the protein is itself palmitoylated on
several cytosolic cysteines. Mutating the conserved catalytic His abolishes
activity [PMID:25505265 "mutation of the conserved His residue in the
hypothesized catalytic domain results in a complete loss of HHAT
palmitoylation"]. A bound heme b is required for function
[PMID:34890564 "revealing a heme group bound to HHAT that is essential for HHAT
function"].

Seven isoforms are annotated (Q5VTY9-1 … Q5VTY9-7); no GOA row is
isoform-specific, so no `isoform` field is set.

## 2. The reaction, and why the GO molecular-function term is chemically off

HHAT transfers palmitate from palmitoyl-CoA onto the **alpha-amino group** of the
N-terminal cysteine of Hedgehog proteins, forming an **amide (N-linked)** bond -
not a thioester on the cysteine sulfur. This was established biochemically
[PMID:18534984 "We provide direct biochemical evidence that Hhat is a PAT with
specificity for attaching palmitate via amide linkage to the N-terminal cysteine
of Shh."] and then visualised directly in the product complex
[PMID:34112694 "including density for the amide linkage to the N-terminal
cysteine (C24) of Hedgehog, indicates that the palmitoylation reaction has
occurred"]. UniProt encodes it as RHEA:59528,
`N-terminal L-cysteinyl-[protein] + hexadecanoyl-CoA = N-terminal
N-hexadecanoyl-L-cysteinyl-[protein] + CoA + H(+)`, and a second reaction
(RHEA:59580) for the cholesterylated substrate.

**The problem.** GOA annotates this with **GO:0019706
protein-cysteine S-palmitoyltransferase activity**, whose definition is explicit
about the acceptor atom: "Catalysis of the transfer of a palmitoyl (systematic
name, hexadecanoyl) group to a **sulfur** atom on the cysteine of a protein
molecule" (OLS). That is the wrong linkage for HHAT.

**Why I did not modify the term.** There is no existing GO molecular-function
term for N-terminal-cysteine N-palmitoylation. Searching GO for
`N-palmitoyltransferase` returns only the peptidyl-lysine N6 terms (GO:0018031,
GO:0140771, GO:0140772), and `GO:0140186 protein N-acyltransferase activity` is
defined on lysine N6 as well. The nearest correct ancestors are GO:0016409
palmitoyltransferase activity and GO:0019707 protein-cysteine S-acyltransferase
activity - and GO:0019707 has the same sulfur problem. Five independent GOA rows
(four IDA from four different papers, plus one Ensembl-Compara IEA) use
GO:0019706, and those curators had no better option. So GO:0019706 is accepted
as the closest available term, and the gap is recorded in `proposed_new_terms`
as *protein-cysteine N-palmitoyltransferase activity* - which is, verbatim, both
UniProt's recommended protein name and PANTHER's subfamily name for HHAT.

Notably GO **does** make the distinction on the biological-process side:
`GO:0018009 N-terminal peptidyl-L-cysteine N-palmitoylation` ("The covalent
attachment of a palmitoyl group to a nitrogen (N) atom in an N-terminal cysteine
residue to form N-palmitoyl-L-cysteine") sits beside
`GO:0018230 peptidyl-L-cysteine S-palmitoylation`. See section 5.

## 3. Where it acts

The ER membrane is the site of catalysis. Every structural and biochemical study
agrees:
[PMID:34112694 "HHAT is an endoplasmic reticulum (ER) membrane protein that
catalyzes the transfer of a palmitoyl lipid from palmitoyl-CoA to the N-terminal
cysteine of Hedgehog precursor proteins"];
[PMID:31875564 "Shh palmitoylation is catalyzed on the luminal side of the
endoplasmic reticulum (ER) by Hedgehog acyltransferase (Hhat), an ER-resident
enzyme."];
[PMID:25505265 "Hedgehog acyltransferase (HHAT) is the enzyme in the endoplasmic
reticulum that palmitoylates Hedgehog proteins"].
The active site is membrane-embedded, reached by palmitoyl-CoA from the cytosolic
leaflet and by the Hedgehog peptide from the lumen
[PMID:34890564 "Our multidisciplinary analysis provides a detailed view of the
mechanism by which HHAT adapts the membrane environment to transfer an acyl chain
across the endoplasmic reticulum membrane."].

Golgi localisation is a weaker, secondary claim. The abstract of the primary
paper says only that the modification happens en route through the secretory
system [PMID:18534984 "Both the Shh precursor and mature protein are
N-palmitoylated by Hhat, and the reaction occurs during passage through the
secretory pathway."], and UniProt records the Golgi assignment as a **curator
inference** rather than a direct observation
(`Golgi apparatus membrane {ECO:0000305|PubMed:18534984}`, and
`Note=Co-localizes with SHH in the ER and Golgi membrane.
{ECO:0000305|PubMed:18534984}`). The cache holds only the abstract of
PMID:18534984, so I have not tried to adjudicate the imaging; the two Golgi rows
(GO:0005794 IDA, GO:0000139 IEA) are kept and marked non-core, because the ER
membrane is where all the characterised chemistry happens.

## 4. The palmitoyl-CoA conduit — a second activity, deliberately not annotated

Asciolla and Resh reported that HHAT also moves its own acyl donor across the ER
membrane, and that this is separable from catalysis:
[PMID:31875564 "Reconstitution of purified Hhat into liposomes provided further
evidence that palmitoyl-CoA uptake activity is an intrinsic property of Hhat."]
and [PMID:31875564 "implying that Hhat serves a dual function as a palmitoyl
acyltransferase and a conduit to supply palmitoyl-CoA to the luminal side of the
ER."] UniProt states it as a FUNCTION with ECO:0000269 from three papers:
`Promotes the transfer of palmitoyl-CoA from the cytoplasmic to the luminal side
of the endoplasmic reticulum membrane, where hedgehog palmitoylation occurs
(PubMed:31875564, PubMed:34112694, PubMed:34890564)`.

I considered proposing a transport annotation and decided against it, on two
grounds.

1. **Comparator check.** No MBOAT in this family carries a transport term
   anywhere. QuickGO for mouse Hhat (Q8BMT9) and Drosophila rasp (Q9VZU2)
   returns only acyltransferase, localisation, palmitoylation and Hedgehog
   pathway terms - no transporter activity, no lipid transport process. A
   systematic absence across the family is a convention, not an oversight.
2. **The 2021 structures reinterpret the phenomenon as part of catalysis.** They
   show palmitoyl-CoA entering an "archway" and a membrane-embedded reaction
   chamber within the enzyme, i.e. substrate access to the active site rather
   than net transport of a cargo released on the far side
   [PMID:34112694 "The attached lipid is required for downstream signaling and is
   structurally recognized by the Hedgehog receptor Patched1"] is the ligand-side
   claim; the mechanism claim is
   [PMID:34890564 "Our multidisciplinary analysis provides a detailed view of the
   mechanism by which HHAT adapts the membrane environment to transfer an acyl
   chain across the endoplasmic reticulum membrane."]

Also, the only GO MF term close to the claim, `GO:0015607 ABC-type
fatty-acyl-CoA transporter activity`, is wrong by construction (HHAT is not an
ABC transporter). I raise the question in `suggested_questions` instead of
asserting an annotation.

## 5. The one gap worth filling: GO:0018009

`GO:0018009 N-terminal peptidyl-L-cysteine N-palmitoylation` is the biological
process HHAT performs, named at exactly the chemistry HHAT does. Human HHAT does
not carry it. Both of its closest relatives do:

| gene product | GO:0018009 evidence | reference |
|---|---|---|
| Drosophila rasp (Q9VZU2) | IDA, IDA, IMP | PMID:11509241, PMID:11861468, PMID:11486055 `[all not cached]` |
| mouse Hhat (Q8BMT9) | ISO, `WITH/FROM UniProtKB:Q5VTY9` | GO_REF:0000119 |
| human HHAT (Q5VTY9) | **absent** | — |

The mouse row is the decisive detail: GO_Central transferred GO:0018009 **to**
mouse Hhat **from human HHAT** by ISO. A curator therefore already judged that
human HHAT has this function, and the human row is missing from the GOA
snapshot rather than deliberately withheld. (Source: QuickGO
`downloadSearch?goId=GO:0018009`.)

Applying the two `NEW` tests from CLAUDE.md:

- **Participation.** HHAT catalyses the step. The term's ancestors are
  GO:0018345 protein palmitoylation, GO:0006498 N-terminal protein lipidation,
  GO:0006497 protein lipidation and GO:0043543 protein acylation - all
  attachment processes, which name the enzyme that does the attaching, not the
  substrate. This is the mirror image of the Drosophila `hh` case, where the
  ligand is the substrate and the acyltransferase activity is not the ligand's
  function: here the acyltransferase is the actor.
- **Comparator.** rasp carries the term with three experimental rows, and mouse
  Hhat carries it by transfer from human. This is a gap, not a convention.
- **Non-redundancy.** GO:0018009 is neither an ancestor nor a descendant of
  GO:0051604 protein maturation (protein maturation is not among its ancestors),
  nor of GO:0045880, nor of the molecular-function terms on the record.

So GO:0018009 is added as the single `NEW` row, with IDA on PMID:34112694 (the
product complex resolving the amide bond) and PMID:18534984 / PMID:31875564 as
additional references.

## 6. Pathway role, and the substrate-versus-actor line

HHAT's product is what licenses Hedgehog reception. The palmitate is not
decoration: it is structurally read by Patched
[PMID:34112694 "The attached lipid is required for downstream signaling and is
structurally recognized by the Hedgehog receptor Patched1"], and palmitoylation
is required for signalling at both ranges
[PMID:18534984 "Palmitoylation of Sonic Hedgehog (Shh) is critical for effective
long- and short-range signaling."] and
[PMID:31875564 "Attachment of palmitate to the N terminus of Sonic hedgehog
(Shh) is essential for Shh signaling."]. Reactome makes the loss-of-function
side of the same point [Reactome:R-HSA-5358343 "Mutation or depletion of the HHAT
enzyme and mutation of the palmitoyl acceptor cysteine in Hh itself abrogates
palmitoylation of the ligand and reduces Hh signaling"].

GOA expresses this as **GO:0045880 positive regulation of smoothened signaling
pathway** (three human IDA rows plus an Ensembl-Compara IEA; mouse Hhat has two
IDA rows for the same term). I accepted it, and the reasoning matters because it
is where the substrate/actor distinction bites:

- HHAT is *not* a component of the smoothened signaling pathway - it never
  touches the receptor, and it acts before the ligand is even released. A bare
  `GO:0007224 smoothened signaling pathway` row on HHAT would be an
  over-annotation. (Mouse Hhat does carry GO:0007224 by IMP, and Drosophila rasp
  carries GO:0007225 patched signaling pathway by IMP; the human record, which
  uses the regulation term instead, has this better.)
- But HHAT *does* perform the act that raises pathway output: it covalently
  modifies the ligand into its high-activity form. "Positive regulation of"
  is precisely GO's way of saying that something acts on a pathway from outside
  it, and the work of that regulation is the palmitoyl transfer HHAT catalyses.

The narrower, mechanistically direct processes are GO:0018009 (the chemistry) and
GO:0051604 protein maturation (the ligand-maturation step the GO-CAM uses). All
three are treated as core; nothing further downstream is.

**Where the GO-CAM sits.** `gocams/index.tsv` gives HHAT exactly one activity:
model 696022cd00000016, "Protein maturation of SHH by autocleavage,
autocholesterylation and palmitoylation by HHAT (Human)", activity
696022cd00000016/696022cd00000024 = GO:0019706 `part_of` GO:0051604 `occurs_in`
GO:0005789. My core function reproduces that triple and adds GO:0018009 and
GO:0045880 as the processes GOA and the ortholog records also carry.

**Module consistency.** `modules/hedgehog_signaling.yaml` models HHAT as annoton
`hh_n_palmitoylation` of the ligand-biogenesis part, with the family selector
PANTHER:PTHR13285 (label `ACYLTRANSFERASE`, which matches
`interpro/panther/panther.obo` verbatim), representative members HHAT (human) and
rasp (Drosophila), function GO:0019706, substrates cholesterylated Hedgehog
signaling domain and palmitoyl-CoA, location GO:0005789. My review agrees on all
of these. The module's `role_description` - "the palmitate is the dominant
contact in the Patched interface, so this step licenses reception rather than
merely decorating the ligand" - is the same judgement I use to accept GO:0045880.
The one thing my review adds that the module does not carry is GO:0018009; that
is a candidate addition to the annoton's `processes`, not a disagreement.

## 7. Phylogenetic propagation (IBA)

`interpro/panther/PTHR13285/PTHR13285-paint.tsv` resolves both IBA rows:

| node | term | taxon scope | IBD seeds |
|---|---|---|---|
| PTN000328646 | GO:0005783 endoplasmic reticulum | taxon:2759 Eukaryota | MGI:1922020 (mouse Hhatl), MGI:2444681 (mouse Hhat), SGD:S000003052 (GUP1), SGD:S000006110 (GUP2), UniProtKB:Q5VTY9 (human HHAT) |
| PTN000998821 | GO:0016409 palmitoyltransferase activity | taxon:6072 Eumetazoa | FB:FBgn0024194 (rasp), MGI:2444681 (mouse Hhat), UniProtKB:Q5VTY9 |

Both placements read correctly. ER residence is a property of the whole
eukaryotic MBOAT group including the yeast GUPs, so a Eukaryota-scoped node is
right; palmitoyltransferase activity is restricted to the Hedgehog-acylating
metazoan clade, so a Eumetazoa-scoped node is right. Human HHAT appearing in its
own `WITH/FROM` for both is expected, not circular: its experimental rows are
among the descendant evidences the PAINT curator used, and the IBA then adds the
claim that the property is inherited.

Note that the same slice contains `PTN002665109 GO:0016409 IRD` (negated) and
`PTN002665109 GO:0016746 IRD` at taxon:117571 - the curator explicitly recorded
**loss** of acyltransferase activity in the HHATL branch. That is a useful
control: it shows the curator distinguished HHAT from its catalytically
compromised paralog rather than blanketing the family, which strengthens the
GO:0016409 node placement on HHAT.

`GO:0016409` is the direct parent of `GO:0019706` and, unlike its child, says
nothing about the linkage atom - so for HHAT it is the more chemically accurate
of the two, which is one more reason to accept rather than deepen it.

## 8. The two Reactome TAS rows for GO:0016747

`GO:0016747 acyltransferase activity, transferring groups other than amino-acyl
groups` is three levels above GO:0019706 (GO:0019706 -> GO:0016409 -> GO:0016747)
and says nothing specific about HHAT. Both rows come from cached Reactome
reactions whose own text is far more specific than the term they export:
[Reactome:R-HSA-5358343 "the N-terminal fragment of Hh (Hh-Np) is also
palmitoylated by the O-acyltransferase HHAT"] and the disease-mutant reaction
[Reactome:R-HSA-5483229 "the mutant protein is unable to palmitoylate SHH or DHH
in an in vitro assay"]. Both are modified to GO:0016409 palmitoyltransferase
activity - the most specific existing term that is chemically correct for HHAT.

## 9. The one GO:0005515 row

A single IPI row from HuRI with partner SDCBP (O00560, syntenin-1). HuRI is a
systematic yeast two-hybrid screen
[PMID:32296183 "We screened this search space a total of nine times with a panel
of three Y2H assay versions"] whose authors state that
[PMID:32296183 "the cellular function of most individual PPIs remains to be
elucidated"]. Syntenin-1 is a PDZ-domain adaptor of the syndecan/exosome axis and
appears in no described HHAT mechanism; there is no follow-up and no more
informative molecular function to modify to. Removed as uninformative, which is
not a claim that the interaction is false.

## 10. Disease

Biallelic HHAT variants cause **Nivelon-Nivelon-Mabille syndrome**
(NNMS, MIM:600092): progressive microcephaly, cerebellar vermis hypoplasia and
skeletal dysplasia, with variable early seizures, growth retardation,
chondrodysplasia and micromelia, and 46,XY gonadal dysgenesis
(`file:human/HHAT/HHAT-uniprot.txt`, DISEASE block; PubMed:24784881,
PubMed:30912300, PubMed:34890564, PubMed:35045414, PubMed:36303863,
PubMed:40326711 - only PMID:34890564 is cached). The G287V allele is the one
Reactome models
[Reactome:R-HSA-5483229 "A G287V loss-of-function mutation in HHAT was
identified in a rare case of Syndromic 46, XY Disorder of Sex Development, which
results in testis dysgenesis."]. HHAT is also a cancer drug target; the inhibitor
IMP-1575 occludes the active site
[PMID:34890564 "A structure of HHAT bound to potent small-molecule inhibitor
IMP-1575 revealed conformational changes in the active site that occlude
substrate binding."]. Disease terms are not GO annotations and no action follows.

## 11. Substrate specificity

Worth recording because it bounds the annotation: HHAT acylates Hedgehog proteins
and apparently nothing else.
[PMID:18534984 "Other palmitoylated proteins (e.g. PSD95 and Wnt) are not
substrates for Hhat, and Porcupine, a putative Wnt PAT, does not palmitoylate
Shh."] and
[PMID:34112694 "The enzyme displays exquisite selectivity for Hedgehog proteins,
which are thought to be its only substrates"]. The acceptor consensus is the
Hedgehog N-terminal `CGPGR` motif. This is why the MF and BP terms can be tied
to the Hedgehog pathway without the enzyme being a pathway component.
