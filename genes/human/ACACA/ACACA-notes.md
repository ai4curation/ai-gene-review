# ACACA (Acetyl-CoA carboxylase 1 / ACC1 / ACC-alpha) — review notes

UniProt: Q13085 (ACACA_HUMAN). HGNC:84. Human, NCBITaxon:9606.

## Core identity and function

ACACA encodes acetyl-CoA carboxylase 1 (ACC1, ACC-alpha; EC 6.4.1.2), the
cytosolic, biotin-dependent multi-domain enzyme that catalyzes the committed,
rate-limiting step of de novo fatty acid biosynthesis: the ATP-dependent
carboxylation of acetyl-CoA to malonyl-CoA.

- "Cytosolic enzyme that catalyzes the carboxylation of acetyl-CoA to malonyl-CoA,
  the first and rate-limiting step of de novo fatty acid biosynthesis"
  [file:human/ACACA/ACACA-uniprot.txt CC FUNCTION].
- Reaction: hydrogencarbonate + acetyl-CoA + ATP = malonyl-CoA + ADP + phosphate + H+;
  RHEA:11308; EC=6.4.1.2 [file:human/ACACA/ACACA-uniprot.txt CC CATALYTIC ACTIVITY].
- Two-step mechanism: "This is a 2 steps reaction starting with the ATP-dependent
  carboxylation of the biotin carried by the biotin carboxyl carrier (BCC) domain
  followed by the transfer of the carboxyl group from carboxylated biotin to acetyl-CoA"
  [file:human/ACACA/ACACA-uniprot.txt CC FUNCTION]. This is the physical basis for the
  two catalytic sub-activities: biotin carboxylase (BC) domain (GO:0004075) and
  carboxyltransferase (CT) domain, plus a central biotinyl-binding (BCC) domain
  carrying the covalently attached biotin cofactor (N6-biotinyllysine at Lys-786).
- Confirmed by structural work: "Acetyl-CoA carboxylase catalyses the ATP-dependent
  carboxylation of acetyl-CoA, a rate-limiting step in fatty acid biosynthesis"
  [PMID:29899443 "Acetyl-CoA carboxylase catalyses the ATP-dependent carboxylation of
  acetyl-CoA, a rate-limiting step in fatty acid biosynthesis"].

## Domain architecture (UniProt FT)

- Biotin carboxylation (BC) domain: 117..618; ATP-grasp: 275..466 (ATP binding site
  315..320; Mg2+/Mn2+ at 424/437/439).
- Biotinyl-binding (BCC) domain: 745..819 (N6-biotinyllysine at 786).
- Carboxyltransferase (CT): 1576..2234 (CoA binding 1823, 2127, 2129).
- "Consists of an N-terminal biotin carboxylation/carboxylase (BC) domain ... The
  C-terminal carboxyl transferase (CT) domain catalyzes the transfer of the carboxyl
  group from carboxylated biotin to acetyl-CoA to produce malonyl-CoA"
  [file:human/ACACA/ACACA-uniprot.txt CC DOMAIN].

## Cofactors

- Biotin (covalently attached; required for catalysis): "The biotin cofactor is
  covalently attached to the central biotinyl-binding domain and is required for the
  catalytic activity" [file:human/ACACA/ACACA-uniprot.txt CC PTM].
- Mg2+/Mn2+: "Binds 2 magnesium or manganese ions per subunit"
  [file:human/ACACA/ACACA-uniprot.txt CC COFACTOR]. Basis for metal ion binding IEA.

## Localization

- Cytosol/cytoplasm: "SUBCELLULAR LOCATION: Cytoplasm, cytosol"
  [file:human/ACACA/ACACA-uniprot.txt CC SUBCELLULAR LOCATION]. Confirmed by HPA IDA
  (GOA line 25, GO:0005829, IDA, HPA).
- NOTE: the IBA GO:0005739 "mitochondrion" (is_active_in) is a paralog mis-propagation.
  The mitochondrion-anchored isozyme is ACC2/ACACB (Q13085 is the cytosolic ACC1). Per
  UniProt/Hunkeler 2018: "the metabolic, cytosolic ACC1, and ACC2, which is anchored to
  the outer mitochondrial membrane and controls fatty acid β-oxidation"
  [PMID:29899443 "the metabolic, cytosolic ACC1, and ACC2, which is anchored to the
  outer mitochondrial membrane"]. ACC1 acts in the cytosol; the mitochondrial
  annotation reflects the ACC family phylogenetic node including ACC2 orthologs.

## Regulation (activity regulation)

Highly regulated enzyme:
- Inhibited by AMPK phosphorylation: "Phosphorylation at Ser-80 by AMPK inactivates
  enzyme activity" [file:human/ACACA/ACACA-uniprot.txt CC PTM]. Also
  [PMID:38892011 "Active AMPK inactivates ACC1, which inhibits the de novo synthesis of
  fatty acids"].
- Citrate-induced polymerization into active filaments: "Citrate promotes
  oligomerization of the protein into filaments that correspond to the most active form
  of the carboxylase" [file:human/ACACA/ACACA-uniprot.txt CC ACTIVITY REGULATION];
  [PMID:20457939 "Polymerization of ACC increases enzymatic activity and is induced in
  vitro by supraphysiological concentrations of citrate"].
- Inhibited by long-chain acyl-CoA (palmitoyl-CoA)
  [file:human/ACACA/ACACA-uniprot.txt CC ACTIVITY REGULATION].
- MID1IP1/MIG12 promotes oligomerization and activity: "recombinant MIG12 induced
  polymerization of ACC ... and increased ACC activity by > 50-fold in the presence of
  1 mM citrate" [PMID:20457939]; the interaction basis for the MID1IP1/S14 annotations.

## Protein interactions (basis for GO:0005515 / GO:0042802 IPI)

- BRCA1 (P38398): binds the phosphorylated/inactive form, prevents dephosphorylation,
  inhibits lipogenesis. "BRCA1 interacts solely with the phosphorylated and inactive
  form of ACCA (P-ACCA) ... BRCA1 affects lipid synthesis by preventing P-ACCA
  dephosphorylation" [PMID:16326698]. Ser-1263 phosphorylation required
  [file:human/ACACA/ACACA-uniprot.txt CC PTM].
- MID1IP1/MIG12 (mouse Q9CQ20): [PMID:20457939], [PMID:20952656].
- AKR1B10 (O60218): stabilizes ACCA, "AKR1B10 associates with acetyl-CoA
  carboxylase-alpha (ACCA)" [PMID:18056116].
- SIRT1 (Q96EB6): identified as a SIRT1/SIRT3 interacting partner [PMID:19343720]
  (abstract does not name ACACA; annotation is IntAct-curated from full text).
- PIN1 (Q13526): "Pin1 interacts directly with ACC1 and inhibits ACC1 phosphorylation
  levels"; "the WW domain of Pin1 was essential for binding with ACC1" [PMID:38892011].
- TRB3/COP1 (Q8K4K2 = mouse Trib3): "TRB3 promoted ACC ubiquitination through an
  association with the E3 ubiquitin ligase ... COP1" [PMID:16794074]. ACACA is the
  substrate whose degradation is triggered; BHF-UCL IPI.
- Homooligomer/homotetramer (identical protein binding, GO:0042802): "Monomer,
  homodimer, and homotetramer ... Can form filamentous polymers"
  [file:human/ACACA/ACACA-uniprot.txt CC SUBUNIT]; [PMID:20457939].

## Disease / pharmacology

- ACACAD (autosomal recessive inborn error of de novo fatty acid synthesis, MIM:613933)
  [file:human/ACACA/ACACA-uniprot.txt CC DISEASE].
- Small-molecule allosteric inhibitor ND-630 inhibits both ACC isozymes, reduces hepatic
  steatosis [PMID:26976583]. This paper is cited as IDA for acetyl-CoA carboxylase
  activity (measures ACC enzymatic activity directly).

## Curation decisions summary

- Core MF: acetyl-CoA carboxylase activity (GO:0003989). Multiple redundant
  IDA/IBA/ISS/TAS annotations — ACCEPT the experimental (IDA) ones as core; the redundant
  IEA/TAS/ISS/IBA of the same correct MF are ACCEPT (own correct core function; policy:
  do not over-annotate a gene's own correct core MF).
- Core BP: fatty acid biosynthetic process (GO:0006633), malonyl-CoA biosynthetic
  process (GO:2001295), acetyl-CoA metabolic process (GO:0006084).
- protein binding (GO:0005515) IPI entries: bare, uninformative MF — MARK_AS_OVER_ANNOTATED
  per policy (never REMOVE an IPI); interactions themselves are real and recorded in notes.
- GO:0016874 ligase activity (IEA): parent of the specific ACC activity; less informative
  — MODIFY to acetyl-CoA carboxylase activity (GO:0003989).
- GO:0006637 acyl-CoA metabolic process (ARBA IEA): too generic / not the direct role
  (ACC makes malonyl-CoA, a specific acyl-CoA, but the specific term GO:2001295 is
  already annotated) — MARK_AS_OVER_ANNOTATED.
- GO:0046949 fatty-acyl-CoA biosynthetic process (Reactome TAS): pathway-context, ACC
  provides malonyl-CoA to the pathway; KEEP_AS_NON_CORE.
- GO:0005739 mitochondrion (IBA is_active_in): paralog mis-propagation (ACC2 is the
  mitochondrial isozyme) — MARK_AS_OVER_ANNOTATED.
- GO:0051289 protein homotetramerization (IEA/ISS): real (SUBUNIT: homotetramer);
  KEEP_AS_NON_CORE (regulatory oligomerization, not the core catalytic function).
