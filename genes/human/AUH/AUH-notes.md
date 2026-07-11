# AUH (methylglutaconyl-CoA hydratase, mitochondrial) — review notes

UniProtKB: Q13825 (AUHM_HUMAN); HGNC:890; gene ID 549; chromosome 9.
339 aa precursor; TRANSIT 1..67 (mitochondrion); CHAIN 68..339. Homohexamer.
Enoyl-CoA hydratase/isomerase (crotonase) superfamily. EC 4.2.1.18 (and 4.2.1.56).

## Bifunctional / moonlighting protein — two genuine functions

### 1. Metabolic enzyme: 3-methylglutaconyl-CoA hydratase (core catalytic function)
- Catalyzes the fifth step of leucine degradation: reversible hydration of
  (E)-3-methylglutaconyl-CoA (3-MG-CoA) to (S)-3-hydroxy-3-methylglutaryl-CoA (HMG-CoA).
  EC 4.2.1.18; RHEA:21536. Physiological direction is hydration (right-to-left in RHEA),
  i.e. 3-MG-CoA -> HMG-CoA; reverse reaction runs at much lower rate in vitro.
  [UniProt Q13825 CATALYTIC ACTIVITY / FUNCTION; PMID:16640564]
- Kinetics (PMID:16640564): best substrates (E)-3-MG-CoA (Vmax 3.9 U/mg, Km 8.3 uM,
  kcat 5.1 /s) and (E)-glutaconyl-CoA (Vmax 1.1 U/mg, Km 2.4 uM). Abstract states:
  "giving strong evidence that the AUH gene encodes for the major human 3-MG-CoA
  hydratase in leucine degradation." Also acts on 3-methylcrotonyl-CoA, crotonyl-CoA,
  3-hydroxybutanoyl-CoA in vitro (broad crotonase-family promiscuity; missing carboxylate
  reduces affinity).
- MGCA1 missense A240V produces enzyme with only 9% of wild-type activity
  [PMID:16640564 abstract; PMID:12655555].
- Disease: 3-methylglutaconic aciduria type I (MGCA1, MIM 250950), autosomal recessive
  inborn error of leucine metabolism [UniProt DISEASE; PMID:12434311; PMID:12655555].
  Note: the local dismech disorder file 3-Hydroxy-3-Methylglutaric_Aciduria.yaml is about
  HMGCL (the DOWNSTREAM lyase), not AUH; it confirms the pathway context (leucine
  degradation, HMG-CoA cleavage to acetyl-CoA + acetoacetate) but AUH's own disease is MGCA1.

### 2. AU-rich element (ARE) RNA-binding protein (second, moonlighting function)
- Original identification: affinity-purified on an AUUUA matrix; recombinant protein
  binds specifically to AU-rich transcripts (IL-3, GM-CSF, c-fos, c-myc 3'UTRs).
  Name AUH = AU-binding protein / enoyl-CoA Hydratase. [PMID:7892223]
- AREs direct rapid mRNA degradation / deadenylation. Hydratase and AU-binding functions
  are on distinct domains of a single polypeptide (immobilized protein still enzymatically
  active) [PMID:7892223].
- Crystal structure (PDB 1HZD, 2ZQQ, 2ZQR): homohexamer; single-stranded RNA-binding homolog
  of enoyl-CoA hydratase; RNA-binding region 105..119; mutagenesis K105N/K109E/K113Q abolishes
  RNA-binding [PMID:11738050; UniProt FT REGION 105..119 + MUTAGEN].

### 3. Possible itaconyl-CoA hydratase activity (C5-dicarboxylate / itaconate detox)
- May convert itaconyl-CoA to (S)-citramalyl-CoA (EC 4.2.1.56; RHEA:13785) in the
  C5-dicarboxylate catabolism pathway that detoxifies macrophage-derived itaconate
  (an anti-microbial metabolite / B12-poisoning precursor) [UniProt FUNCTION;
  PMID:29056341 states the itaconyl-CoA<->citramalyl-CoA hydration is catalyzed by AUH].
  Evidence is TAS/inference (ECO:0000303) — a secondary, context-dependent activity.

## Localization
- Mitochondrion / mitochondrial matrix. N-terminal transit peptide 1..67.
  [UniProt SUBCELLULAR LOCATION; Reactome R-HSA-70785, R-HSA-9914271; PMID:34800366 HTP
  mito proteome]. Note PMID:34800366 full text is a large proteome dataset; AUH not found
  by simple grep of the cached markdown (supplementary/table-based); rely on UniProt +
  Reactome for the matrix localization. Use TAS/HTP annotations as ACCEPT (matrix is the
  more specific, correct compartment).

## Annotation strategy
- CORE MF: GO:0004490 methylglutaconyl-CoA hydratase activity (IDA PMID:16640564 + IBA/IEA).
- GO:0004300 enoyl-CoA hydratase activity: parent/family-level activity; the IDA (PMID:7892223)
  is the historical "low degree of enzymatic activity" observation — real but less precise than
  the physiological 3-MG-CoA hydratase. Keep, mark as over-annotated / accept as family-level.
- GO:0003730 mRNA 3'-UTR binding (IDA PMID:7892223): genuine second function — ACCEPT.
  GO:0003723 RNA binding (IEA): parent, accept.
- GO:0006552 L-leucine catabolic process (IMP PMID:16640564, IEA): core BP — ACCEPT.
- GO:0009083 branched-chain amino acid catabolic process (IEA): parent of leucine catabolism,
  correct, less specific — accept.
- GO:0006635 fatty acid beta-oxidation (IBA): AUH is a crotonase-family member but its
  physiological role is leucine catabolism, NOT fatty-acid beta-oxidation; the IBA is a
  family-level over-propagation (the enoyl-CoA hydratase step of FAO is done by ECHS1/EHHADH,
  not AUH). MARK_AS_OVER_ANNOTATED.
- GO:0050011 itaconyl-CoA hydratase activity (IEA + TAS PMID:29056341) and
  GO:0110052 toxic metabolite repair (TAS PMID:29056341): keep as non-core (secondary,
  inferred activity in itaconate detox).
- GO:0170035 obsolete L-amino acid catabolic process (IEA): term is OBSOLETE -> REMOVE.
- GO:0003824 catalytic activity (IEA, InterPro): uninformative root-level MF, subsumed by
  the specific hydratase term. MARK_AS_OVER_ANNOTATED.
- GO:0005739 mitochondrion (multiple) — accept; GO:0005759 mitochondrial matrix (TAS) is the
  more specific correct compartment — ACCEPT as core location.
