# LMAN2L (VIPL / VIP36-like protein), human — review notes

UniProt: Q9H0V9 (LMA2L_HUMAN). Gene symbol LMAN2L (HGNC:19263); synonym VIPL.
348 aa precursor; signal peptide 1-44; lumenal L-type lectin-like domain (49-274);
single-pass type I membrane protein (TM 314-336); short cytoplasmic tail (337-348)
ending in a C-terminal RKR di-arginine / KRFY ER-retention/retrieval motif.

## Family / identity

LMAN2L is an L-type (leguminous-type, ConA-like) lectin family member, a paralog of
LMAN2/VIP36 and related to LMAN1/ERGIC-53. It was identified by profile-based database
scanning for animal L-type lectins and named VIPL ("VIP36-Like")
[PMID:12609988 "the sequence of a novel family member related to VIP36, named VIPL for VIP36-like"].
It is ubiquitously expressed and evolutionarily older than VIP36
[PMID:12609988 "Sequence analysis suggests that VIPL is a ubiquitously expressed protein and appeared earlier in evolution than VIP36"].

## Subcellular localization — ER-resident (key distinction from VIP36)

Unlike VIP36 and ERGIC-53 (which cycle in the early secretory pathway), VIPL is a
**non-cycling resident protein of the ER**
[PMID:12609988 "Unlike VIP36 and ERGIC-53 that are predominantly associated with postendoplasmic reticulum (ER) membranes and cycle in the early secretory pathway, VIPL is a non-cycling resident protein of the ER"].
ER retention depends on a cytoplasmic RKR di-arginine signal
[PMID:12609988 "Mutagenesis experiments indicate that ER retention of VIPL involves a RKR di-arginine signal"];
UniProt records loss of ER retention on RKR->SSS mutagenesis (MUTAGEN 344..346).
A second study found VIPL "localized primarily to the ER and partly to the Golgi complex"
[PMID:12878160 "VIPL localized primarily to the ER and partly to the Golgi complex"],
consistent with the UniProt subcellular location ("Predominantly found in the endoplasmic
reticulum. Partly found in the Golgi"). Supports CC = ER membrane (IDA, core) and Golgi
apparatus (IDA, accepted, minor pool).

## Molecular function — D-mannose/lectin binding (by homology/domain, not directly shown)

VIPL is a **high-mannose type I membrane glycoprotein with the same domain organization as
VIP36** [PMID:12609988 "VIPL is a high-mannose type I membrane glycoprotein with similar domain organization as VIP36"].
The carbohydrate recognition domain (CRD) was used as the search string to identify it
[PMID:12878160 "the conserved carbohydrate recognition domain (CRD) as a search string"].
Neither cached abstract directly demonstrates D-mannose binding by VIPL itself; the
D-mannose binding (GO:0005537) assignment rests on the conserved L-type lectin CRD /
PROSITE L_LECTIN_LIKE profile and homology to VIP36 (whose mannose binding is
characterized). UniProt carbohydrate-binding residues (93, 128, 161-163, 188, 258-260) and
Ca2+ sites are annotated by PROSITE-ProRule (ECO:0000255), i.e. by similarity. Therefore
the TAS/IBA D-mannose binding annotations are best treated as KEEP_AS_NON_CORE /
homology-based rather than a directly demonstrated core MF. Avoid assigning any
mannosidase/glycosidase or catalytic activity — VIPL has no catalytic activity; it is a
lectin/regulator.

## Biological process — regulation of ER export of glycoproteins; regulator of ERGIC-53 (CORE)

UniProt FUNCTION: "May be involved in the regulation of export from the endoplasmic
reticulum of a subset of glycoproteins. May function as a regulator of ERGIC-53."
(ECO:0000269|PubMed:12878160).

Two complementary lines of evidence:
- Overexpression of VIPL redistributes ERGIC-53 to the ER, suggesting VIPL is a regulator
  of ERGIC-53 [PMID:12609988 "Overexpression of VIPL redistributed ERGIC-53 to the ER without affecting the cycling of the KDEL-receptor and the overall morphology of the early secretory pathway. The results suggest that VIPL may function as a regulator of ERGIC-53"].
- siRNA knock-down of VIPL slows secretion of two glycoproteins, indicating an ER export
  receptor role [PMID:12878160 "knock-down of VIPL mRNA using siRNA significantly slowed down the secretion of two glycoproteins (M(R) 35 and 250 kDa) to the medium, suggesting that VIPL may also function as an ER export receptor"].

This supports the core BP framing: regulation of ER export of a subset of glycoproteins /
ER-to-Golgi transport. The IMP (PMID:12878160, protein transport GO:0015031) and TAS
(PMID:12878160, ER-to-Golgi vesicle-mediated transport GO:0006888) annotations are core.
Note that "lectin-like membrane receptors" are thought to be required for efficient export
of glycoprotein subsets from the ER [PMID:12878160 "Subsets of glycoproteins are thought to require lectin-like membrane receptors for efficient export out of the endoplasmic reticulum (ER)"].

## protein folding (GO:0006457 NAS)

NAS assertion (PMID:12609988). VIPL is not a folding enzyme/chaperone; any role is in
glycoprotein quality-control/sorting context, not catalysis of folding. Over-annotation —
mark as MARK_AS_OVER_ANNOTATED / non-core.

## Protein interactions

UniProt INTERACTION block lists two binary partners:
- HTT (P42858) — huntingtin; from the neurodegenerative-disease interactome
  [PMID:32814053] (Y2H ND-focused screen). MalaCards/disease context but uninformative for core MF.
- MAL (P21145) — myelin and lymphocyte protein; from HuRI binary interactome [PMID:32296183].

These yield bare "protein binding" (GO:0005515 IPI) annotations. Per guidelines, avoid bare
protein binding as core → KEEP_AS_NON_CORE. (GOA WITH/FROM fields: PMID:32296183 -> MAL P21145;
PMID:32814053 -> HTT P42858.)

## Disease

- Intellectual developmental disorder, autosomal recessive 52 (MRT52; MIM:616887): homozygous
  missense R53Q segregating in a consanguineous Pakistani family
  [PMID:26566883], no effect on general protein glycosylation (UniProt VARIANT R53Q note).
- Intellectual developmental disorder, autosomal dominant 69 (MRD69; MIM:617863): dominant
  LMAN2L mutation causing intellectual disability with remitting epilepsy [PMID:31020005].

Disease links are not directly used to assign MF/CC/BP GO terms here but underscore the
gene's importance in neurodevelopment.

## Summary of action plan for annotations

- D-mannose binding (TAS 12609988; IBA): KEEP_AS_NON_CORE (homology/CRD-based, not directly shown).
- ER membrane (IDA 12609988; IBA, IEA): ACCEPT (ER-resident, core CC).
- Golgi apparatus (IDA 12878160), Golgi membrane (IBA, IEA): ACCEPT/KEEP_AS_NON_CORE (minor Golgi pool).
- ERGIC (IBA GO:0005793): ACCEPT (early secretory pathway, consistent localization).
- protein folding (NAS 12609988): MARK_AS_OVER_ANNOTATED.
- ER-to-Golgi vesicle-mediated transport (TAS 12878160; IBA), protein transport (IMP 12878160): ACCEPT (core BP).
- COPII vesicle (NAS 12878160; IBA GO:0030134): KEEP_AS_NON_CORE.
- generic membrane (GO:0016020 IEA, TAS): MARK_AS_OVER_ANNOTATED (ER/Golgi membrane more informative).
- protein binding (IPI 32296183, 32814053): KEEP_AS_NON_CORE.
