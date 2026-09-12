# IVD (Isovaleryl-CoA dehydrogenase, mitochondrial) — review notes

UniProtKB: P26440 | HGNC:6186 | Gene 3712 | Chr 15q15 | EC 1.3.8.4 (also 1.3.8.1)

## Core biology (verified)

IVD is a mitochondrial-matrix, FAD-dependent flavoenzyme of the acyl-CoA dehydrogenase
(ACAD) family. It catalyses the third step of leucine catabolism, downstream of the
branched-chain alpha-ketoacid dehydrogenase (BCKDH) complex: the alpha,beta-dehydrogenation
of isovaleryl-CoA (3-methylbutanoyl-CoA) to 3-methylcrotonyl-CoA (3-methylbut-2-enoyl-CoA),
transferring electrons via its FAD to the electron-transfer flavoprotein (ETF).

- Reaction / substrate specificity established biochemically on purified human liver enzyme
  [PMID:3597357 "IV \ndehydrogenase/isovaleryl-CoA reactions were identified as crotonyl-CoA, ... 3-methylcrotonyl-CoA"];
  same paper shows ETF/PMS as electron acceptors and homotetrameric structure with 1 mol FAD/subunit.
- Catalytic mechanism / active-site glutamate (E254 in mature numbering; Glu-286 in precursor)
  identified by mutagenesis [PMID:7640268 "The E254G and E254Q mutant IVDs had no detectable \nenzymatic activity"].
  This paper is the UniProt evidence for FUNCTION and the EC assignments (1.3.8.4, 1.3.8.1).
- Cofactor FAD and homotetramer confirmed by X-ray structure at 2.6 A [PMID:9214289] (UniProt COFACTOR/SUBUNIT).
- Mitochondrial matrix localization: NAS [PMID:2063866 "isovaleryl-CoA dehydrogenase (IVD), a mitochondrial matrix enzyme"];
  precursor imported and processed from 45 kDa to 43 kDa mature form (transit peptide 1-32, cleaved after Ala-32).
- Chromosome 15 assignment and cDNA cloning: [PMID:3446585] (rat cDNA + human chr15 mapping).

## Disease
Isovaleric acidemia (IVA; MIM:243500; MONDO:0009475), the first recognised organic acidemia,
autosomal recessive; "sweaty feet" odor. Deficiency blocks leucine catabolism -> accumulation of
isovaleric acid, 3-hydroxyisovaleric acid, isovalerylcarnitine (C5), isovalerylglycine; secondary
hyperammonemia (isovaleryl-CoA inhibits NAGS). Corroborated by disorder KB
(~/repos/dismech/kb/disorders/Isovaleric_Acidemia.yaml; MONDO:0009475).

## GOA annotation review summary

- MF core: GO:0008470 (3-methylbutanoyl-CoA dehydrogenase activity = isovaleryl-CoA dehydrogenase
  activity, EC 1.3.8.4). Multiple IDA (PMID:7640268, PMID:3597357), TAS (Reactome, PMID:3446585),
  IBA, ISS, IEA — all ACCEPT (core). Current ontology label is "3-methylbutanoyl-CoA dehydrogenase activity".
- GO:0050660 FAD binding (IEA InterPro) — ACCEPT, supported by X-ray/COFACTOR.
- GO:0006552 L-leucine catabolic process — core BP; IDA/IBA/ISS/IEA — ACCEPT.
- GO:0009083 branched-chain amino acid catabolic process (IDA) — ACCEPT (parent process; leucine is BCAA).
- CC: GO:0005759 mitochondrial matrix (NAS/ISS/TAS/IEA) — ACCEPT core; GO:0005739 mitochondrion
  (IBA/IEA/IDA-HPA/HTP) — ACCEPT (broader but correct).
- GO:0003995 acyl-CoA dehydrogenase activity (IEA InterPro) — parent MF; KEEP but generalization of the
  specific 0008470 — MARK_AS_OVER_ANNOTATED / ACCEPT as family-level. Keep as ACCEPT (correct, less specific).
- GO:0016627 oxidoreductase acting on CH-CH (IEA) — grandparent MF, ACCEPT (correct, general).
- GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity (IEA, EC 1.3.8.1) — IVD does have minor
  short-chain acyl-CoA (butanoyl/pentanoyl) activity (EC 1.3.8.1 in UniProt) — ACCEPT as non-core / MARK_AS_OVER_ANNOTATED
  (secondary "to a lesser extent" activity, not physiological core).
- GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity (IEA RHEA hexanoyl-CoA) — hexanoyl-CoA is
  medium-chain (C6); UniProt lists hexanoyl-CoA as a minor substrate. This is a promiscuous in-vitro
  side activity, not the physiological function -> MARK_AS_OVER_ANNOTATED.
- GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase (IDA PMID:3597357) — IVD's short-chain
  activity is a minor contribution to FA beta-oxidation; keep as non-core.
- GO:0005515 protein binding (IPI, HuRI PMID:32296183; ACTN3, GPSM3) — bare "protein binding", high-throughput
  Y2H binary interactome; uninformative -> MARK_AS_OVER_ANNOTATED (do NOT REMOVE per policy).
- GO:0042802 identical protein binding (ISS from rat P12007) — homotetramer, self-association is real
  (structure PMID:9214289) -> ACCEPT/KEEP_AS_NON_CORE.

Deep research (falcon) was requested but the file did not appear within the poll window;
review grounded in UniProt P26440, GOA, cached PMIDs, and the Isovaleric_Acidemia disorder KB.
