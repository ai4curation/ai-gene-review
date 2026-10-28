# PA4503 (Q9HVR8) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE PA4503` (first attempts hit UniProt read
timeouts; a re-run completed). Accession Q9HVR8 matches the worklist (rank 41).
The entry is unreviewed (PE 3) with the submitter name "Probable permease of ABC
transporter"; there is no gene symbol, so the folder uses the locus tag. No
deep-research provider was used; this file is my own literature research.

### Identity

- PA4503 is DppB, the first of the two integral-membrane permease subunits of the
  DppBCDF dipeptide ABC importer. Its PA14 ortholog PA14_58440 was renamed DppB
  by Pletzer et al. [PMID:25338022 "Since the protein sequence of PA14_58440 shows
  a high degree of homology to other dipeptide ABC transporters, we suggest
  renaming this protein as DppB and refer to the operon as the dppBCDF operon."]
- Operon: PAO1 PA4503-PA4506 = dppB, dppC (PA4504), dppD, dppF; the PA14 operon
  is [PMID:25338022 "two encoding the hydrophobic permeases PA14_58440 and
  PA14_58450 (dppC), and two encoding the hydrophilic nucleotide- and ATP-binding
  proteins PA14_58470 (dppD) and PA14_58490 (dppF)"]. The PAO1/PA14 locus
  correspondence is from the operon order and the PseudoCAP curator's choice; it
  is not stated with PAO1 locus tags in the paper.
- Domains: Pfam PF00528 BPD_transp_1 and PF19300 BPD_transp_1_N; PROSITE PS50928
  ABC_TM1; six predicted TM helices; PANTHER PTHR43163 (DppB-related), subfamily
  SF6; "OppBC subfamily" of binding protein-dependent permeases. Topology was also
  predicted by the authors [PMID:25338022 "Topology analysis of the two ABC-type
  permeases DppB and DppC using the TOPCONS prediction software [33] revealed the
  typical six α-helical transmembrane spanning domains"].

### Literature

Only one paper addresses the P. aeruginosa Dpp system directly (PMID:25338022,
Pletzer et al. 2014, PLoS One, full text cached). A second (PMID:29416528, Lee et
al. 2018) studies the DppA1 binding protein in biofilm/Pf5 prophage control and
does not test DppB.

What PMID:25338022 did:
- Constructed a 3.95-kb deletion of the whole dppBCDF operon in PA14
  [PMID:25338022 "In order to investigate the substrate profile of the ABC
  transporter DppBCDF, a deletion mutant of the dppBCDF operon was constructed"].
- Biolog phenotype microarrays (respiration on di/tripeptides as sole N source)
  [PMID:25338022 "Numerous dipeptides could not be used as N-source by the mutant
  lacking the DppBCDF transporter system"], covering 107 of the 162 dipeptides
  used by the wild type.
- Phaseolotoxin (a tripeptide toxin) sensitivity [PMID:25338022 "Our results
  demonstrate that PA14 is sensitive to phaseolotoxin and that it is specifically
  taken up by the dipeptide ABC transporter DppBCDF."]
- An SBP penta mutant (dppA1-A5) phenocopies the operon deletion, showing that
  the system is binding protein-dependent.

What it did not do: no radiolabelled uptake, binding, or ATPase assay; no
single-gene dppB mutant; no complementation of the operon deletion. The evidence
for PA4503 is therefore a mutant phenotype (loss of dipeptide utilization and of
toxin sensitivity) of a deletion covering all four genes. That is IMP-type
evidence, not IDA. It still supports the claim that DppB is a component of the
dipeptide transporter, because the permease subunits are the translocation
channel of an ABC importer (they do part of the work), and DppB is the only
OppB-type permease in the operon.

### Qualifier: enables vs contributes_to

Transport activity of a binding protein-dependent ABC importer is a property of
the assembled DppA-DppB-DppC-DppD-DppF complex; no single subunit transports
dipeptides on its own. By the GO qualifier definitions, `contributes_to` is the
precise qualifier for a subunit. In practice, comparators use `enables`: E. coli
DppB (P0AEF8) and DppC (P0AEG1) carry `enables GO:0071916` (EcoCyc RCA), and
EcoCyc uses `enables` for NikB/NikC nickel transporter activity. I therefore keep
the `enables` rows (the claim is correct and matches convention), and record
`contributes_to` in core_functions.

### Clade check for PTN000765601 (QuickGO, 2026-10-28)

Leaves of PTN000765601 (25 in 9 taxa, from the cached PAINT leaf GAF) include
E. coli DppB, DdpB, NikB and SapB; Salmonella and Haemophilus DppB and SapB;
Yersinia, Vibrio, Shewanella and Helicobacter members; and nine Bradyrhizobium
japonicum paralogs. The experimental MF annotations of these leaves (QuickGO):
- NikB (P33591): nickel transmembrane transporter activity (IMP, EcoCyc).
- SapB (P0AGH3): putrescine transmembrane transporter activity (IMP, PMID:27803167,
  EcoCyc); the Sap system exports putrescine in E. coli.
- DdpB (P77308): only the IBA.
So the node term "dipeptide transmembrane transporter activity" is propagated to
paralogous permeases whose established substrate is nickel or putrescine. In the
OppBC family the substrate is set by the binding protein, not by the permease;
the node is a mixed-specificity clade and the dipeptide term is over-specific for
it. The parent node PTN002455499 (GO:0022857 transmembrane transporter activity,
4 seeds incl. PA4503) carries a term that suits such a clade.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000765601 | GO:0071916 dipeptide transmembrane transporter activity | 1 (sole) | 25 (9 taxa) | GO:0071916, IDA, PMID:25338022 (PseudoCAP) | OVER-SPECIFIC | The claim is sound for PA4503 (DppB of the DppBCDF dipeptide importer), but the evidence is an operon-deletion growth/toxin phenotype (IMP, not IDA). The node also contains NikB (nickel) and SapB (putrescine export) and nine B. japonicum paralogs with unknown substrates; in this family the binding protein sets the substrate, so a dipeptide term does not suit the clade. |
| PTN002455499 | GO:0022857 transmembrane transporter activity | 4 | 29 (16 taxa) | GO:0071916, IDA, PMID:25338022 (PseudoCAP) | SOUND | A general transporter term suits an OppB-type permease clade; PA4503 is one of four seeds, alongside E. coli experimentally characterised permeases. |

Defects filed: PSEUDOCAP WRONG_EVIDENCE_CODE (IDA should be IMP) on the IDA row;
GO_CENTRAL WRONG_TERM (CHECK) for the PTN000765601 IBD on the IBA row. The IBA on
PA4503 itself remains correct.

## Decisions summary

- ACCEPT: plasma membrane (IBA, IEA), dipeptide transmembrane transporter
  activity (IBA, IDA; the IDA with an evidence-code defect).
- MODIFY: membrane -> plasma membrane; dipeptide transmembrane transport and
  transmembrane transport -> dipeptide import across plasma membrane; ABC
  transporter complex -> ABC transporter complex, substrate-binding
  subunit-containing.
