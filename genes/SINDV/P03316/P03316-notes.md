# P03316 — Sindbis virus structural polyprotein (p130) — curation notes

## Provenance of this file

Deep research was **unavailable** for this gene: no deep-research API keys are
configured in this container, so `just deep-research` could not be run and no
`-deep-research-<provider>.md` file exists or should be created. These notes were
written directly from (a) the cached UniProt record `P03316-uniprot.txt`, (b) the
publications cached under `publications/`, and (c) two papers I fetched with
`just fetch-pmid` (PMID:12424249, PMID:1944569). The GONUTS wiki
(gowiki.tamu.edu), which normally records the CACAO student's evidence, is
offline (see `projects/CACAO.md`), so the three CACAO rows were judged from the
papers alone.

## Identity and gene symbol

UniProt entry `POLS_SINDV` / P03316, "Structural polyprotein", AltName p130.
**UniProt assigns no gene name** — the GOA file's `GENE NAME` column carries the
protein name "Structural polyprotein", not a symbol — so the folder and the
review's `gene_symbol` both use the accession `P03316`. This follows the
CLAUDE.md convention for entries with no gene symbol at all ("use the accession
as the folder name"). The stub's `gene_symbol: P03316` is therefore appropriate
and I have left it as seeded.

`alternative_products` (seeded) records the ribosomal-frameshift relationship to
P0DOK0 (the frameshifted structural polyprotein, i.e. the TF-containing product);
P0DOK0 is a separate UniProt entry and is not reviewed here.

## One entry, five mature chains

This is a polyprotein: every annotation on P03316 is really an annotation on one
of its cleavage products, and which chain a row belongs to is the main thing a
reviewer has to get right here.

| Chain | Residues | PRO id | Role |
|---|---|---|---|
| Capsid protein (C) | 1–264 | PRO_0000041321 | autoprotease; RNA binding; T=4 nucleocapsid; IRAK1 inhibition |
| Precursor of E3/E2 (p62/pE2) | 265–751 | PRO_0000226238 | ER/Golgi transit form of E3+E2 |
| Assembly protein E3 | 265–328 | PRO_0000041322 | signal sequence; pH protection of E1 in transit |
| Spike glycoprotein E2 | 329–751 | PRO_0000041323 | receptor attachment; capsid binding for budding |
| 6K protein | 752–806 | PRO_0000041324 | viroporin; glycoprotein transport; budding |
| Spike glycoprotein E1 | 807–1245 | PRO_0000041325 | class II fusion protein |

Processing order [file:SINDV/P03316/P03316-uniprot.txt "Capsid protein is
auto-cleaved during polyprotein translation, unmasking a signal peptide at the
N-terminus of the precursor of E3/E2"], then host signal peptidase in the ER
yields pE2, 6K and E1, and host furin cleaves pE2 to E3 + E2 in trans-Golgi
vesicles.

## Capsid protein

**Autoprotease.** The C-terminal domain is a chymotrypsin-like serine protease
that cleaves the capsid off the nascent polyprotein; UniProt records
EC 3.4.21.90 and the reaction "Autocatalytic release of the core protein from the
N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser-
bond" [file:SINDV/P03316/P03316-uniprot.txt]. The domain statement is tied to a
publication: "The C-terminus functions as a protease during translation to cleave
itself from the translating structural polyprotein (PubMed:1944569)". This is the
basis for GO:0004252 and, at the right granularity, for protein autoprocessing
rather than bare proteolysis.

**RNA binding and the T=4 nucleocapsid.** 240 copies form a T=4 icosahedral
capsid and bind the genomic RNA [file:SINDV/P03316/P03316-uniprot.txt "Forms an
icosahedral capsid with a T=4 symmetry composed of 240 copies of the capsid
protein"]. Cryo-EM of whole virions resolves the complementary capsid/envelope
lattices [PMID:3829124 "The lipid bilayer of the virus envelope is polyhedral and
surrounds a smooth T=3 nucleocapsid"] — note that this 1987 35 Å reconstruction
called the core T=3; the modern consensus (and the UniProt text) is T=4 for both
shells.

**Localization in infected cells.** Live imaging of a tetracysteine-tagged capsid
shows diffuse cytoplasm plus discrete foci, including foci at the plasma membrane
that are candidate assembly/egress sites [PMID:23785213 "Capsid puncta were also
observed at the PM."; "This staining was distributed diffusely in the cytoplasm
as before but also showed distinct foci"]. Nuclear shuttling is asserted only
by similarity to the VEEV capsid (Q8JUX5), via an N-terminal NLS plus a
supraNES; there is no SINV-specific measurement in any source I could read.

**Innate-immune evasion.** BioID2 proximity labelling from the SINV capsid
identified host IRAK1, and the interaction inhibits IRAK1-dependent TLR
signalling [PMID:33673546 "the alphaviral capsid protein specifically inhibits
IRAK1-dependent signaling"; "this capsid-IRAK1 interaction is conserved across
multiple alphavirus species"]. This is the basis for both the GO:0005515 row
(partner P51617 = IRAK1, a kinase) and the GO:0039722 row.

**Host-driven degradation.** The capsid is a selective-autophagy (virophagy)
cargo: the host HECT E3 SMURF1 co-immunoprecipitates with it and is required for
its delivery to autophagosomes [PMID:22020285 "Smurf1 and SIN capsid protein
co-immunoprecipitate in SIN-infected MEFs and HeLa cells"]. This is a host
activity directed *at* the capsid, not a viral function, which is why the two
GO:0044389 rows are kept but not treated as core.

## Spike glycoprotein E2 (and pE2/E3)

E2 is the attachment protein. Random-insertion mutagenesis of the PE2/E1 genes
followed by selection against binding-competent virus isolated mutants mapping
near the PE2 cleavage site and to E2 residues 69–74, all defective for binding
[PMID:7684466 "Both NB1 and NB2 were defective for binding to CEF and BHK-21
cells."; "these results implicate PE2 cleavage and domains in the N-terminal
portion of E2 as important determinants of alphavirus binding and penetration"].
The receptors were later identified as VLDLR/LRP8 [file:SINDV/P03316/P03316-uniprot.txt
"Plays a role in viral attachment to target host cell, by binding to the cell
receptors VLDLR or LRP8/APOER2 (PubMed:34929721)"].

E2 reaches the plasma membrane by the secretory pathway and is surface-exposed in
infected cells [PMID:875134 "Iodine was incorporated into E1 and E2 on the surface
of SVHR-infected cells in the same relative amounts as seen in iodinated virions."].

## 6K protein

6K is a small, palmitoylated, multi-pass membrane protein present in virions at
low stoichiometry [PMID:2408229 "the 6K protein can be detected in purified
preparations of virions"; "in virions the ratio of 6K to E1 + E2 ranged from 0.08
to 0.12"].

**Viroporin / channel activity.** 6K permeabilizes bacterial and mammalian
membranes, and interfacial-domain mutants lose that activity
[PMID:12424249 "Transfection of the construct with wild-type 6K strongly increased
permeability to the antibiotic hygromycin B."]. Functionally, SINV release is
sensitive to the Vpu channel blocker HMA and the Vpu channel helix complements 6K
[PMID:36191050 "the Vpu inhibitor 5-N, N-Hexamethylene amiloride (HMA),
significantly reduces SINV release, suggesting that the ion channel activity of
6K similar to Vpu, promotes virus budding"], and UniProt records the pharmacology
as curated activity regulation [file:SINDV/P03316/P03316-uniprot.txt "The channel
activity is blocked by 5-N, N-Hexamethylene amiloride."].

**Caveat worth recording.** Heterologous expression of 6K cRNA in Xenopus oocytes
found *no* intrinsic channel conductance; the currents seen were endogenous
oocyte channels upregulated downstream of ER calcium-store depletion
[PMID:17483865 "Although no intrinsic channel properties were seen, cell shrinkage
was observed within 24 h."; "6K upregulated endogenous currents"]. So the ion-channel
annotations rest on permeabilization, inhibitor pharmacology and heterologous
channel complementation, not on a recorded 6K single-channel conductance. The
oligomeric structure and conduction mechanism are explicitly open
[PMID:36191050 "While the oligomeric structures and mechanisms of ion channel
activity are well-established for M2 and P7, these remain unknown for 6K."].

**Localization and budding.** 6K traffics with E2 through the secretory pathway
[PMID:36191050 "6K localizes to ER and Golgi"; "6K and E2 colocalize on Golgi in
the secretory pathway"] and its channel function is required to make CPV-II from
the Golgi and to deliver spikes to the plasma membrane: "in the absence of 6K,
CPV-II, which originates from the Golgi apparatus, is not detected in infected
cells, with a concomitant reduction in the glycoprotein transport to the plasma
membrane" [PMID:36191050]. 6K is also at the plasma membrane in oocytes
[PMID:17483865 "6K was located at both the plasma and the endoplasmic reticulum
membranes."].

## Spike glycoprotein E1

E1 is a class II fusion protein held inactive by E2 in the mature virion. In a
receptor-free liposome system, SINV fusion is strictly low-pH dependent, needs
cholesterol plus sphingolipid in the target membrane, and is preceded by E1/E2
dissociation and formation of a trypsin-resistant E1 homotrimer
[PMID:10482600 "Fusion was optimal at pH 5.0, with a threshold at pH 6.0, and
undetectable at neutral pH, supporting a cell entry mechanism of SIN involving
fusion from within acidic endosomes."; "the E2/E1 heterodimeric envelope
glycoprotein of the virus dissociated, with formation of a trypsin-resistant E1
homotrimer, which kinetically preceded the fusion reaction, thus suggesting that
the E1 trimer represents the fusion-active conformation of the viral spike"].
E1 reaches the plasma membrane independently of pE2/E2 [PMID:2806407 "E1 is
efficiently transported to the plasma membrane in the absence of PE2/E2"], and is
surface-detectable in infected cells [PMID:875134].

## Where the spikes actually are

Both E1 and E2 sit in the **lipid envelope** that surrounds the nucleocapsid; the
80 trimeric spikes protrude from that bilayer, not from the capsid shell
[PMID:10482600 "The glycoproteins are organized in 80 hetero-oligomeric spikes; a
single spike consists of a trimer of E2/E1 heterodimers."] and
[PMID:3829124 "The spikes of the virus appear as columnar trimers arranged on a
T=4 lattice. The lipid bilayer of the virus envelope is polyhedral and surrounds a
smooth T=3 nucleocapsid."]. This matters for the CACAO row on GO:0098029
*icosahedral viral capsid, spike*, whose GO definition is "A short structure
attached to an icosahedral virion capsid, and used for attachment to the host
cell" and whose only ontology placement is `part_of GO:0019030 icosahedral viral
capsid` (checked against QuickGO, 2026-10-29). For an enveloped alphavirus the
spike is an envelope structure, so the GO term asserts the wrong compartment.
GO has no envelope-spike CC term (a QuickGO text search for "spike" returns only
GO:0098029 outside the neuroscience senses), which is why this review files one
under `proposed_new_terms`.

## CACAO rows at a glance

Three rows carry `ASSIGNED BY = CACAO`:

1. `GO:0019062 virion attachment to host cell` / IMP / PMID:7684466 — the paper's
   whole point is binding-defective E2/PE2 insertion mutants. Right protein,
   right process, right evidence code, right granularity (the paper does not
   identify a receptor, and the row does not claim one). **ACCEPT.**
2. `GO:0020002 host cell plasma membrane` / IDA / PMID:17483865 — supported by the
   abstract's own statement, but the assay is 6K cRNA injected into *Xenopus*
   oocytes, not an infected host cell, and the same sentence reports the ER
   equally. Independent infected-cell data (PMID:875134, PMID:2806407,
   PMID:2408229, PMID:23785213) carry the claim. **ACCEPT**, with the
   heterologous-expression caveat and the note that the student took one of two
   compartments from a single sentence.
3. `GO:0098029 icosahedral viral capsid, spike` / IDA / PMID:10482600 and
   `GO:0061025 membrane fusion` / IDA / PMID:10482600 — the paper is a liposome
   fusion study of E1. `GO:0061025` is the generic root of the fusion branch while
   the paper pins down the specific one (low-pH, endosome-like); `GO:0098029`
   puts the glycoprotein spike on the capsid. Both are term-choice problems, not
   evidence problems: **MODIFY** in each case.

Failure shapes for the CACAO taxonomy: one **parent-level restatement**
(`membrane fusion` where the paper establishes the endosomal fusion step), one
**wrong structural compartment** — a shape not yet in the taxonomy: the term names
the right supramolecular assembly (the spike) but attaches it to the wrong parent
structure (capsid rather than envelope), which only the term's ontology placement
reveals; and one **heterologous-system localization read as host localization**
(the oocyte row), a near-relative of the catalogued single-assay localization
problem.
