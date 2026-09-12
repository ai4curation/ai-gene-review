# IDI1 (Isopentenyl-diphosphate Delta-isomerase 1) — review notes

UniProt: Q13907 (IDI1_HUMAN), 227 aa, EC 5.3.3.2. Gene HGNC:5387, chromosome 10.

## Core biochemistry

IDI1 catalyzes the reversible 1,3-allylic rearrangement of isopentenyl diphosphate (IPP)
to dimethylallyl diphosphate (DMAPP), the electrophilic allylic isomer that primes
prenyl-chain elongation in the isoprenoid/mevalonate pathway.

- UniProt FUNCTION: "Catalyzes the 1,3-allylic rearrangement of the homoallylic substrate
  isopentenyl (IPP) to its highly electrophilic allylic isomer, dimethylallyl diphosphate
  (DMAPP)." [file:human/IDI1/IDI1-uniprot.txt, ECO:0000269|PubMed:8806705]
- CATALYTIC ACTIVITY: "Reaction=isopentenyl diphosphate = dimethylallyl diphosphate;
  ... EC=5.3.3.2" (RHEA:23284). [file:human/IDI1/IDI1-uniprot.txt]
- COFACTOR: Mg(2+), "Binds 1 Mg(2+) ion per subunit." [file:human/IDI1/IDI1-uniprot.txt,
  ECO:0000269|PubMed:8806705]. The crystal structure (PubMed:17250851) resolved the enzyme
  in complex with substrate and metal ions; UniProt binding-site annotations list Mg2+ at
  positions 40, 51, 146, 148. The GOA/UniProt DR block additionally records manganese ion
  binding (GO:0030145, IDA), consistent with type-1 IDI enzymes being metalloenzymes that
  can use divalent metals (Mg2+/Mn2+).
- PATHWAY: "Isoprenoid biosynthesis; dimethylallyl diphosphate biosynthesis; dimethylallyl
  diphosphate from isopentenyl diphosphate: step 1/1." [file:human/IDI1/IDI1-uniprot.txt]
  (UniPathway UPA00059, UER00104.)
- SUBUNIT: "Monomer." [file:human/IDI1/IDI1-uniprot.txt, ECO:0000269|PubMed:17250851]
- Family: "Belongs to the IPP isomerase type 1 family." Nudix hydrolase fold
  (PROSITE PS51462; Pfam PF00293 NUDIX; InterPro IPR011876 IsopentenylPP_isomerase_typ1).
  Active sites at residues 86 and 148. [file:human/IDI1/IDI1-uniprot.txt]

## Biochemical characterization (PMID:8806705, Hahn et al. 1996; abstract only)

Recombinant human IPP isomerase overproduced in E. coli, purified >90%; "The recombinant
protein catalyzed the isomerization of IPP to dimethylallyl diphosphate and was maximally
active at pH 7.0 in the presence of Mg2+. The Michaelis constant for IPP was 33 microM ...;
Vmax = 4.1 mumol min-1 mg-1." This is the experimental (IDA) basis for GO:0004452 and the
IC basis for cholesterol biosynthetic process (GO:0006695). Full text not in cache
(full_text_available: false).

## Subcellular localization

- UniProt SUBCELLULAR LOCATION: "Peroxisome" (ECO:0000250|UniProtKB:O35586, i.e. by
  similarity to rat Idi1). [file:human/IDI1/IDI1-uniprot.txt]
- C-terminal "Microbody targeting signal" motif at residues 225-227 (PTS1-type).
  [file:human/IDI1/IDI1-uniprot.txt]
- PMID:17180682 (Kovacs et al. 2007; abstract only): immunofluorescence/permeabilization
  study confirming the pre-squalene segment of the cholesterol biosynthetic pathway is
  localized to peroxisomes in human cells. Underlies the IDA peroxisome annotation.
- PMID:17202134 (Clizbe et al. 2007; abstract only): "Both isozymes, IDI1 and IDI2 are
  localized to the peroxisome by a PTS1-dependent pathway." Direct experimental support
  for peroxisomal localization of IDI1.
- Reactome (R-HSA-191382) treats the isomerase step as cytosolic and notes: "IPP isomerase
  may also be located in human peroxisomes but its function there is not clear." Hence the
  TAS cytosol annotations. Dual cytosol/peroxisome localization is well supported; both are
  kept as valid locations.

## Second isozyme context (PMID:17202134)

Humans/mice have a second IPP isomerase, IDI2, expressed only in skeletal muscle, regulated
independently (possibly via PPARalpha). IDI1 is the broadly-expressed housekeeping isozyme
(UniProt HPA: "Low tissue specificity"; Bgee: expressed in adrenal and 208 other tissues).

## Annotation review summary

- Core MF: **GO:0004452 isopentenyl-diphosphate delta-isomerase activity** — experimentally
  established (IDA, PMID:8806705); IBA and IEA duplicates ACCEPTed as the same core function.
- **GO:0016860 intramolecular oxidoreductase activity** (IEA, ARBA): a correct-but-general
  ancestor of GO:0004452 (verified via OLS: GO:0004452 → GO:0016863 → GO:0016860 → GO:0016853
  isomerase activity). MODIFY to the specific GO:0004452 rather than remove.
- Core BP: isoprenoid biosynthetic process (GO:0008299), dimethylallyl diphosphate
  biosynthetic process (GO:0050992), isopentenyl diphosphate biosynthetic process
  (GO:0009240), cholesterol biosynthetic process (GO:0006695, IC). All ACCEPT/KEEP.
  Note GO:0009240 (IPP *biosynthesis*) is arguably imprecise for an isomerase that
  interconverts IPP/DMAPP rather than synthesizing IPP de novo, but it is the standard
  PAN-GO/IBA term for this family and interconversion contributes to the IPP pool; kept.
- Core CC: peroxisome (GO:0005777, IDA x2 + ISS/IBA/IEA) and cytosol (GO:0005829, TAS x2).
  Both ACCEPT (peroxisome) / KEEP_AS_NON_CORE-then-ACCEPT (cytosol) as genuine locations.
- **GO:0035634 response to stilbenoid** (IEA, Ensembl Compara from mouse Idi1 P58044):
  peripheral orthology-transferred response annotation, not a core catalytic/pathway
  function → KEEP_AS_NON_CORE.

## Term-id verification (OLS4, 2026-07)

All non-obsolete: GO:0004452 (F, def "isopentenyl diphosphate = dimethylallyl diphosphate"),
GO:0050992 (P), GO:0016860 (F, isomerase branch — ancestor of GO:0004452), GO:0009240 (P),
GO:0008299 (P), GO:0006695 (P), GO:0005777 (C), GO:0005829 (C), GO:0035634 (P).
