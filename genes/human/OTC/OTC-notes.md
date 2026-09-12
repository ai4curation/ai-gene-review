# OTC (Ornithine transcarbamylase / ornithine carbamoyltransferase, P00480) — review notes

## Core biology (verified)
- X-linked, nuclear-encoded, mitochondrial-matrix urea-cycle enzyme; EC 2.1.3.3.
- Catalyzes: carbamoyl phosphate + L-ornithine -> L-citrulline + phosphate + H(+) (Rhea:RHEA:19513).
  - UniProt: "Catalyzes the second step of the urea cycle, the condensation of carbamoyl phosphate with L-ornithine to form L-citrulline (PubMed:2556444, PubMed:6372096, PubMed:8112735)." Some sources number this the third step; either way it is the OTC-catalyzed condensation.
- Pathway (UniProt): "Nitrogen metabolism; urea cycle; L-citrulline from L-ornithine and carbamoyl phosphate: step 1/1."
- Subunit (UniProt): "Homotrimer." (PubMed:10813810, PubMed:9852088)
- Localization (UniProt): "Mitochondrion matrix" (PubMed:3895227).
- Family (UniProt): "aspartate/ornithine carbamoyltransferase superfamily. OTCase family."
- Tissue: "Mainly expressed in liver and intestinal mucosa."
- PTM/regulation: acetylation at Lys-88 negatively regulates activity in response to nutrient signals (PubMed:19318352).

## Import / precursor processing
- Nuclear-encoded precursor with 32-aa N-terminal leader (4 arginines, no acidic residues); leader cleaved after import into the matrix.
  - [PMID:6372096 "We have deduced the complete primary structure of the precursor of a human mitochondrial matrix enzyme, ornithine transcarbamylase (OTC)"]
  - [PMID:6372096 "The amino-terminal leader peptide of OTC is 32 amino acids in length and contains four arginines but no acidic residues."]
- Basic arginine residues in the leader are required for import and proteolytic cleavage.
  - [PMID:3895227 "we demonstrate a critical role for one or more of the basic arginine residues in the leader peptide of the subunit precursor for the human mitochondrial matrix enzyme, ornithine transcarbamoylase"]
  - [PMID:3895227 "The altered ornithine transcarbamoylase precursor failed to be taken up by intact mitochondria in vitro."]

## Enzyme activity / disease functional evidence
- Missense mutations abolish/reduce OTC activity; expression in Cos1 cells confirms causality.
  - [PMID:2556444 "the specific activity of mutant OTC was 100-fold lower than that of wild type"]
  - [PMID:2556444 "Ornithine transcarbamylase (OTC) is an important enzyme in the detoxification of ammonia to urea, and its deficiency is the most common inborn error of ureagenesis in humans."]
  - [PMID:8112735 "Predicted OTC activities of mutant OTC cDNAs ranged from 0% to 8.9% of the normal level"]
  - [PMID:8112735 "The predicted enzyme activities account for the clinical phenotype of the disease."]

## OTC deficiency (OTCD; MONDO:0010703)
- Most common urea cycle disorder; deficiency -> impaired citrulline synthesis -> hyperammonemia.
  - dismech: "OTCD typically leads to mitochondrial enzyme dysfunction, preventing the synthesis of citrulline from carbamoyl phosphate and ornithine"
  - dismech: "carbamoylphosphate synthetase 1 and ornithine transcarbamylase are present in the mitochondrial matrix" (confirms matrix)

## Localization proteomics
- [PMID:34800366] MitoCoP high-confidence mitochondrial proteome (HTP) — supports mitochondrial localization.

## Annotation judgments
- Strong experimental core kept ACCEPT: GO:0004585 (MF), GO:0000050 (urea cycle), GO:0019240 (L-citrulline biosynthetic), GO:0005759 (matrix), GO:0097272 (ammonium homeostasis).
- GO:0006526 (L-arginine biosynthetic process) — IBA; urea cycle is the biosynthetic route to arginine in some contexts; KEEP_AS_NON_CORE (downstream pathway role, not OTC's direct product).
- GO:0006593 (L-ornithine catabolic process) — IDA; ornithine is the consumed substrate; KEEP_AS_NON_CORE (accurate but a substrate-centric framing of the same MF).
- GO:0042802 (identical protein binding) — IEA Ensembl; reflects homotrimer; MODIFY toward homotrimerization/structural constituent role; keep non-core.
- Ensembl Compara (GO_REF:0000107) transfers from rat P00481 that are over-annotations for human OTC: liver development, midgut development, response to xenobiotic/zinc/insulin/nutrient/biotin, phospholipid binding, monoatomic anion homeostasis, phosphate ion binding, mitochondrial inner membrane (wrong compartment; OTC is matrix). -> MARK_AS_OVER_ANNOTATED / REMOVE (inner membrane REMOVE: wrong compartment).
- Cytosol TAS (Reactome R-HSA-9956513/9956502/9959881) reflects precursor/mutant-trafficking + gene-expression modeling, not the mature enzyme localization -> REMOVE/MARK_AS_OVER_ANNOTATED as a steady-state location claim.
- GO:0016597 (amino acid binding), GO:0042301 (phosphate ion binding) reflect substrate/product binding within catalysis; keep non-core (subsumed by MF).

## Deep research
- falcon deep-research file was NOT present within the ~12 min poll window; review grounded in UniProt, GOA, dismech disorder file, and cached publications.
