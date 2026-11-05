# PA4504 (Q9HVR7) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE PA4504` (UniProt read timeouts on early
attempts; a re-run completed). Accession Q9HVR7 matches the worklist (rank 75).
The entry is unreviewed (PE 3), named "Probable permease of ABC transporter",
with no gene symbol, so the folder uses the locus tag. No deep-research provider
was used. Reviewed together with PA4503 (DppB); see
`genes/PSEAE/PA4503/PA4503-notes.md` for the shared literature analysis.

### Identity

- PA4504 is DppC, the second permease subunit of the DppBCDF dipeptide ABC
  importer; PA14 ortholog PA14_58450 [PMID:25338022 "two encoding the
  hydrophobic permeases PA14_58440 and PA14_58450 (dppC), and two encoding the
  hydrophilic nucleotide- and ATP-binding proteins PA14_58470 (dppD) and
  PA14_58490 (dppF)"]. The PAO1/PA14 mapping follows operon order (PA4503-PA4506).
- Domains: Pfam PF00528 BPD_transp_1 and PF12911 OppC_N; PROSITE PS50928
  ABC_TM1; seven UniProt-predicted TM helices (the authors' TOPCONS analysis
  gives six) [PMID:25338022 "Topology analysis of the two ABC-type permeases
  DppB and DppC using the TOPCONS prediction software [33] revealed the typical
  six α-helical transmembrane spanning domains"]; PANTHER PTHR43386 (official
  name "OLIGOPEPTIDE TRANSPORT SYSTEM PERMEASE PROTEIN APPC"), subfamily SF1.

### Literature and evidence type

PMID:25338022 (Pletzer et al. 2014, full text cached) deleted the whole
dppBCDF operon in PA14 [PMID:25338022 "In order to investigate the substrate
profile of the ABC transporter DppBCDF, a deletion mutant of the dppBCDF operon
was constructed"] and scored dipeptide use as N source by Biolog
[PMID:25338022 "Numerous dipeptides could not be used as N-source by the mutant
lacking the DppBCDF transporter system"] and phaseolotoxin sensitivity
[PMID:25338022 "Our results demonstrate that PA14 is sensitive to phaseolotoxin
and that it is specifically taken up by the dipeptide ABC transporter
DppBCDF."]. There was no direct transport, binding or ATPase assay, no
single-gene dppC mutant and no complementation of the operon deletion. The
evidence is therefore IMP-type, not IDA. The claim that DppC is part of the
dipeptide transporter is still sound: the two permeases form the translocation
pathway (they do the work of moving the substrate), and DppC is the only
OppC-type permease in the operon.

Qualifier: transport is a property of the DppA-BCDF complex, so contributes_to
is the strict GO qualifier for a subunit; E. coli DppB/DppC (EcoCyc) and
NikB/NikC use enables, so the existing rows are kept as enables and
contributes_to is used in core_functions.

### Clade check for PTN000766696 (QuickGO, 2026-10-28)

The 12 leaves (6 taxa; cached PAINT leaf GAF) are E. coli DppC, DdpC, NikC and
GsiD; Salmonella DppC and GsiD; Haemophilus DppC; Yersinia (two), Vibrio (two)
and PA4504. Experimental MF annotations of these leaves in QuickGO:
- NikC (P0AFA9): nickel transmembrane transporter activity (IMP, EcoCyc).
- GsiD (P75799): glutathione transmembrane transporter activity (EXP, EcoCyc).
Nickel and glutathione (a tripeptide) are not dipeptides, so the node term is
over-specific for this mixed-specificity clade, in which the binding protein
sets the substrate [PMID:25338022 "The substrate specificity of ABC
transporters is determined by its associated substrate-binding proteins
(SBPs)."]. The parent PTN000765620 carries GO:0022857 transmembrane transporter
activity (5 seeds: PA4504, E. coli GsiD, NikC and two others), which suits a
clade of 96 leaves in 31 taxa.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000766696 | GO:0071916 dipeptide transmembrane transporter activity | 1 (sole) | 12 (6 taxa) | GO:0071916, IDA, PMID:25338022 (PseudoCAP) | OVER-SPECIFIC | Sound for PA4504 (DppC), though the evidence is an operon-deletion phenotype (IMP, not IDA). The node also contains NikC (nickel) and GsiD (glutathione) permeases with experimental annotations for those substrates; in this family the binding protein sets substrate specificity. |
| PTN000765620 | GO:0022857 transmembrane transporter activity | 5 | 96 (31 taxa) | GO:0071916, IDA, PMID:25338022 (PseudoCAP) | SOUND | A general transporter term suits an OppC-type permease clade; other seeds are experimentally characterised E. coli permeases. |

Defects filed: PSEUDOCAP WRONG_EVIDENCE_CODE (IDA should be IMP) on the IDA row;
GO_CENTRAL WRONG_TERM (CHECK) for the PTN000766696 IBD on the IBA row. The IBA
on PA4504 itself remains correct.

## Decisions summary

- ACCEPT: plasma membrane (IBA, IEA), dipeptide transmembrane transporter
  activity (IBA, IDA; the IDA with an evidence-code defect).
- MODIFY: membrane -> plasma membrane; dipeptide transmembrane transport and
  transmembrane transport -> dipeptide import across plasma membrane; ABC
  transporter complex -> ABC transporter complex, substrate-binding
  subunit-containing.
