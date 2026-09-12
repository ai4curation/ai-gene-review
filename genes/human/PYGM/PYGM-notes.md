# PYGM (muscle glycogen phosphorylase) — review notes

UniProtKB:P11217, HGNC:9726, EC 2.4.1.1, 842 aa.

## Core biology (from UniProt P11217 + task brief)
- Muscle isoform of glycogen phosphorylase; rate-limiting enzyme of muscle glycogenolysis.
- Catalyzes phosphorolytic cleavage of alpha-1,4 glycosidic bonds at glycogen non-reducing
  ends, releasing alpha-D-glucose-1-phosphate (Rhea:RHEA:41732, EC 2.4.1.1). Stops ~4 residues
  from alpha-1,6 branch points.
  [file:UniProt CATALYTIC ACTIVITY, "Reaction=[(1->4)-alpha-D-glucosyl](n) + phosphate = [(1->4)-alpha-D-glucosyl](n-1) + alpha-D-glucose 1-phosphate"]
- Cofactor: pyridoxal 5'-phosphate (PLP) covalently attached at Lys-681
  [file:UniProt COFACTOR "Name=pyridoxal 5'-phosphate"; MOD_RES 681 "N6-(pyridoxal phosphate)lysine"].
- Homodimer (phosphorylase b); homotetramer for active phosphorylase A
  [file:UniProt SUBUNIT "Homodimer ... Homotetramer; to form the enzymatically active phosphorylase A"].
- Allosteric enzyme: activated by AMP; inhibited by ATP, ADP, glucose-6-phosphate
  [file:UniProt ACTIVITY REGULATION "activated by AMP and inhibited by ATP, ADP, and glucose-6-phosphate"].
- Covalent regulation: phosphorylation of Ser-15 by phosphorylase kinase (PHK) converts
  phosphorylase b (inactive) → phosphorylase a (active)
  [file:UniProt PTM "Phosphorylation of Ser-15 converts phosphorylase B (unphosphorylated) to phosphorylase A"].
- Cytosolic. Expressed skeletal-muscle-enriched (HPA: skeletal muscle, tongue).

## Disease
- GSD5 / McArdle disease [MIM:232600]: exercise intolerance, cramps, muscle weakness,
  recurrent myoglobinuria (rhabdomyolysis), "second wind" phenomenon.
  [file:UniProt DISEASE "myopathy characterized by exercise intolerance, cramps, muscle weakness and recurrent myoglobinuria"]

## Key experimental refs (cached)
- PMID:1150650 (Carty, Tu, Graves 1975): CATALYTIC ACTIVITY, ACTIVITY REGULATION, SUBUNIT,
  phosphorylation at Ser-15. Abstract confirms phosphorylase b/a interconversion, AMP
  regulation, dimer→tetramer association, glucose-6-P inhibition. Abstract-only. Basis of
  UniProt EC=2.4.1.1 experimental evidence and the IDA glycogen phosphorylase activity /
  glycogen catabolic process annotations.
- PMID:8316268 (Tsujino, Shanske, DiMauro 1993 NEJM): McArdle disease molecular genetics;
  UniProt tags this as FUNCTION + CATALYTIC ACTIVITY + GSD5 variants (R50X truncation, G205S,
  K543T). IMP for glycogen phosphorylase activity / glycogen catabolic process. Abstract-only.
- PMID:9633816 (Kubisch 1998): revised genomic structure of myophosphorylase gene, McArdle
  diagnosis. TAS source (ProtInc/PINC) for glycogen phosphorylase activity + glycogen
  metabolic process. Abstract is about genomic structure/mutation but paper concerns the
  muscle glycogen phosphorylase gene — TAS annotation to the enzyme's activity/process is
  appropriate.

## Localization annotations
- GO:0005829 cytosol — IBA + 3x TAS(Reactome). Correct; cytosolic enzyme.
- GO:0070062 extracellular exosome — HDA, PMID:23533145 (prostatic-secretion exosome
  proteomics). High-throughput MS detection in secreted vesicles; not the site of catalytic
  function. MARK_AS_OVER_ANNOTATED (per policy, not REMOVE for HDA MS detection).

## Protein binding IPIs (all GO:0005515, IPI, IntAct)
Large-scale interactome / IntAct screens. Bare "protein binding" is uninformative per
curation guidelines → MARK_AS_OVER_ANNOTATED (not REMOVE, per policy).
- PMID:24722188 O43741 (PRKAB2, AMPK beta2 subunit)
- PMID:25416956 O43741 (PRKAB2), Q96HA8 (NTAQ1)
- PMID:31515488 Q96HA8 (NTAQ1)
- PMID:32296183 O43741 (PRKAB2), P06737 (PYGL, liver phosphorylase), P11216 (PYGB, brain phosphorylase)
- PMID:33961781 P11216 (PYGB)
- PMID:36217029 P0DTD1-PRO_0000449633 (SARS-CoV-2 nsp12/rep; xeno)
UniProt INTERACTION lists PRKAB2, NTAQ1, PYGB, PYGL, and SARS-CoV-2 rep as interactors.
PRKAB2 (AMPK) interaction is biologically plausible (glycogen metabolism regulation); PYGB/PYGL
are paralogs (isoenzyme heterodimer detection in HT screens). None are informative MF terms.

## Core functions (author-supplied, strictly validated)
- MF: GO:0008184 glycogen phosphorylase activity
- BP (directly_involved_in): GO:0005980 glycogen catabolic process
- CC (locations): GO:0005829 cytosol
- cofactor / MF: GO:0030170 pyridoxal phosphate binding
