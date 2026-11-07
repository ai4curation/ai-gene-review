# mtrA1 (MTH_1159, O27227) notes

Methanothermobacter thermautotrophicus Delta H, tetrahydromethanopterin
S-methyltransferase subunit A (Mtr step 6 of hydrogenotrophic methanogenesis).
Round 7 of the ARCHAEA project. Kept consistent with genes/METJA/mtrA.

## Literature search (2026-11-07)

Deep-research providers were unavailable, so no `-deep-research-*.md` file was made.
PubMed E-utilities searches: "MtrA AND Methanothermobacter";
"methyltetrahydromethanopterin coenzyme M methyltransferase thermoautotrophicum";
"mtrH AND methanogen". WebSearch: "Harms Thauer MtrA histidine 84 mutation";
"MTH1062 / MTH_1062 / mtrA2 cytoplasmic MtrA homologue" (no hits on MTH_1062 itself).
Cached and read: PMID:27324530 and PMID:38530900 (full text); PMID:11248186,
PMID:10338124, PMID:8898900, PMID:9461302, PMID:9801157, PMID:7737157, PMID:8001564,
PMID:8223548, PMID:7929010, PMID:27342374 (abstracts only).

## Strain caution

Almost all biochemistry is on "Methanobacterium thermoautotrophicum strain Marburg",
now Methanothermobacter marburgensis, a different species from strain Delta H.
The Delta H mtrA1 product (O27227) is 99.2% identical (236/238) to Marburg MtrA (P80184)
[file:METTH/mtrA1/mtrA1-bioinformatics/RESULTS.md], so the results transfer with high
confidence, but annotations are ISS, not IDA, for Delta H.

## Name caution: "MtrA1" in PMID:8898900 is not the locus mtrA1

Harms & Thauer 1996 call their soluble deletion construct "MtrA1"
[PMID:8898900 "MtrA1 [des-(214-239)-MtrA], which is a deletion mutant of MtrA that lacks the
last 25 C-terminal hydrophobic amino acids"]. This is a construct name for the Marburg
operon MtrA, not the Delta H locus name mtrA1 (which UniProt uses to distinguish the operon
copy from the paralog mtrA2).

## Biology

- Eight subunits, operon mtrEDCBAFGH in strain Marburg [PMID:7737157 "the eight mtr genes
  organized in a 4.9-kbp gene cluster in the order mtrEDCBAFGH"]. In Delta H the mtr operon
  is immediately downstream of mcr [PMID:7929010 "The MRI-encoding mcr operon (mcrBDCGA) has
  been located immediately upstream from the mtr operon (mtrEDCBA)"]. MTH_1159 (mtrA1) lies
  in the MTH_1156-1163 mtr cluster.
- MtrA carries the corrinoid that is methylated and demethylated; MtrH does the methylation
  [PMID:10338124 "The 23 kDa subunit MtrA harbors a corrinoid prosthetic group which is
  methylated and demethylated in the catalytic cycle."].
- Catalytic mechanism: cob(I)amide attacks the N5-methyl of methyl-H4MPT; enzyme-bound
  methyl-cob(III)amide is the intermediate; Na+ stimulates [PMID:8001564 "methyl transfer
  from CH3-H4MPT to coenzyme M proceeds via nucleophilic attack of the cobalt(I) on the
  N5-methyl substituent of CH3-H4MPT, forming an enzyme-bound CH3-corrinoid as
  intermediate"].
- Demethylation is the Na+-dependent step [PMID:11248186 "demethylation being sodium
  ion-dependent"].
- Native cofactor 5-hydroxybenzimidazolyl cobamide (factor III)
  [PMID:8001564 "enzyme-bound Co-methyl-5'-hydroxybenzimidazolyl cob(III)amide was formed"];
  base-off/His-on [PMID:8898900 "the corrinoid is bound to MtrA1 in the base-off form and
  that the Co(II) of the prosthetic group is coordinated by a histidine residue of the
  apoprotein"]; His84 by mutagenesis [PMID:9461302 "This active site histidine was now
  identified by site-directed mutagenesis to be His84"; PMID:9801157 "His84 rather than His35
  is the axial ligand to the cobamide in MtrA"]. O27227 residue 84 is His.
- Membrane anchor: C-terminal single TM helix (UniProt FT TRANSMEM 219..237; deletion of the
  C-terminal 25 hydrophobic residues makes it soluble, PMID:8898900). Stupperich et al. 1993
  predicted the helix "near the N-terminus" [PMID:8223548], which was superseded; their
  immunogold localisation at the cytoplasmic face of the membrane is consistent with later
  topology [PMID:8223548 "the corrinoid-dependent membrane protein was detectable at the
  cytoplasmic face of the membranes"].
- Cryo-EM of M. marburgensis Mtr (PMID:38530900): MtrA C-terminal helix in the Mtr(ABFG)3
  stalk; soluble B12 domain mobile and unresolved; Na+ and CoM in MtrCDE; MtrAs proposed to
  shuttle between MtrH and MtrCDE.

## mtrA2 (MTH_1062, O27134)

183 aa, outside the mtr operon. Aligns to mtrA1 only over the soluble cobamide domain,
~60% identity, no C-terminal juxtamembrane/TM segment
[file:METTH/mtrA1/mtrA1-bioinformatics/RESULTS.md]. It belongs to the "cytoplasmic MtrA
homologue" class [PMID:27324530 "These cytoplasmic MtrA homologues consist only of a soluble
cobalamin-binding domain of 170–180 amino acids"], which M. marburgensis also has. No paper
on MTH_1062 itself was found; its function is unknown. Its UniProt entry nevertheless
carries the HAMAP MF_01093 MtrA-subunit annotations (cell membrane, single-pass, EC 7.2.1.4,
complex membership) with a TRANSMEM at 102..118 inside the soluble domain; these look like
rule over-propagation to a soluble paralog (not part of this review; flagged in
suggested_questions). Nothing in this review rests on mtrA2 data: the cytoplasmic homologue
structure in PMID:27324530 is from Methanothermus fervidus and is cited only as a structural
model for the cobamide-binding mode.

## Decisions (mirroring METJA/mtrA)

- GO:0005886 ACCEPT; GO:0006730 ACCEPT; GO:0019386 ACCEPT.
- GO:0006814 MODIFY -> GO:0035725; GO:0035725 KEEP_AS_NON_CORE.
- GO:0030269 MARK_AS_OVER_ANNOTATED (pattern 16); contributes_to in core functions.
- GO:0050897 MODIFY -> GO:0031419 (pattern 17).
- NEW GO:0044677 complex (ISS from strain Marburg).
- Rhea RHEA:53492 (EC 7.2.1.4, sole Rhea reaction for that EC). No PANTHER DR line in O27227.
