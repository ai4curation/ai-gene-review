# tnr3 (SPAC6F12.05c, UniProt P41888) notes

Fetch: `just fetch-gene SCHPO tnr3` fetched the correct accession (TNR3_SCHPO, P41888, 569 aa).

## Naming
- "tnr" = thiamine-negative-regulator: tnr3 was first found as a regulatory mutant
  [PMID:1551569 "Mutants expressing derepressed levels of the enzyme in the presence and absence of thiamine map in three genes, tnr1, tnr2 and tnr3"].
  It is in fact the TPK, orthologue of S. cerevisiae THI80. There is no S. cerevisiae "TNR3" homologue relationship to worry about,
  but the regulatory name hides an enzyme.
- Domain architecture: N-terminal Nudix domain (Pfam PF00293) fused to TPK catalytic and B1-binding domains [UniProt:P41888].
  S. cerevisiae THI80 lacks the Nudix domain; its free-standing yeast homologue is YJR142W.

## Evidence
- TPK: [PMID:7499352 "tnr3 mutants have reduced levels of intracellular thiamine diphosphate, show impaired TPK activity, which is enhanced by introducing the tnr3 wild type gene on a plasmid, and can be complemented by the S. cerevisiae TPK-encoding gene TH180"]; [PMID:7499352 "Disruption of the tnr3 gene is lethal"].
  UniProt kinetics: KM 6 uM thiamine, 1.9 mM ATP (from PMID:7499352).
- Regulatory phenotypes: [PMID:1551569 "The tnr3 mutants reveal a 10-20-fold higher intracellular thiamine level than tnr1 and tnr2 mutants and wild type"];
  pho1 derepression and constitutive mating (PMID:7499352). Interpreted as loss of the ThDP signal.
- Nudix domain: [PMID:23834287 "recombinant Tnr3 and its Saccharomyces cerevisiae, Arabidopsis and maize Nudix homologues lacked thiamin monophosphate phosphatase activity, but were active against ThDP, and up to 60-fold more active against diphosphates of the toxic thiamin degradation products oxy- and oxo-thiamin"].
- Cytoplasm/cytosol: ORFeome (PMID:16823372).

## GO-CAM
- gomodel:66c7d41500000963: tnr3 enables GO:0004788, cytosol, part_of GO:0009229. Agrees.
  The model does not include the Nudix activity (it is outside the biosynthetic pathway).

## Decisions
- Core MF GO:0004788 / BP GO:0009229 / cytosol (consistent with genes/yeast/THI80).
- NEW GO:0004787 thiamine diphosphate phosphatase activity (IDA, PMID:23834287) as second core function (Nudix domain).
- 8-oxo-dGDP phosphatase (IDA/IEA): abstract does not mention it; deferred to curator, KEEP_AS_NON_CORE.
- thiamine salvage (EXP/IBA): loose fit for damaged-ThDP hydrolysis; KEEP_AS_NON_CORE (THI80 review marked the IBA over-annotated because THI80 lacks the Nudix domain; tnr3 is the experimental donor).
- thiamine biosynthetic process IMP (PMID:1551569): MARK_AS_OVER_ANNOTATED (indirect derepression; THI80 review rejected same process).
- thiamine metabolic process / thiamine-containing compound metabolic process: MODIFY -> GO:0009229.
- Module note: the module says the Tnr3 Nudix domain does not hydrolyse TMP (correct per PMID:23834287) - consistent.
