# PA4505 (Q9HVR6) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE PA4505` (no gene symbol; locus tag used as
folder name). Accession Q9HVR6 matches the worklist (rank 101). Unreviewed
TrEMBL entry (PE 3). No deep-research provider was used. Reviewed for
consistency with genes/PSEAE/PA4503 and PA4504 (DppB, DppC; same paper) and
braF (ABC ATPase subunit).

### Identity

- DppD, ABC ATPase subunit; PANTHER PTHR43297:SF2 "DIPEPTIDE TRANSPORT
  ATP-BINDING PROTEIN DPPD"; Pfam PF00005 ABC_tran and PF08352 oligo_HPY;
  PROSITE ABC_TRANSPORTER_1/2; Walker A at 39-46. Peripheral inner-membrane
  protein.
- Pletzer et al. 2014 (PMID:25338022; full text cached), strain PA14:
  [PMID:25338022 "two encoding the hydrophilic nucleotide- and ATP-binding
  proteins PA14_58470 (dppD) and PA14_58490 (dppF)"]; PA14_58470 corresponds to
  PAO1 PA4505 by operon order.
  - [PMID:25338022 "Numerous dipeptides could not be used as N-source by the
    mutant lacking the DppBCDF transporter system"]
  - [PMID:25338022 "Our results demonstrate that PA14 is sensitive to
    phaseolotoxin and that it is specifically taken up by the dipeptide ABC
    transporter DppBCDF."]
  - [PMID:25338022 "The substrate specificity of ABC transporters is determined by
    its associated substrate-binding proteins (SBPs)."]

Evidence: deletion of the whole dppBCDF operon, Biolog and phaseolotoxin
sensitivity. No direct assay and no single dppD mutant, so the PseudoCAP IDA
should be IMP (as already flagged for PA4503 and PA4504). The claim holds for
DppD, whose ATPase powers the importer.

### Clade checks (cached PAINT IBD/leaf GAF; QuickGO 2026-10-28)

- PTN000656114 (GO:0071916 dipeptide transmembrane transporter activity; sole
  seed PA4505): 6 leaves in 5 taxa: E. coli DppD (P0AAG0), Salmonella DppD,
  Haemophilus influenzae DppD, Yersinia DppD and YPO3452, PA4505. All are DppD
  orthologs, unlike the mixed DppC node PTN000766696 (NikC, GsiD). E. coli DppD
  experimental annotations in QuickGO: plasma membrane (IDA), heme
  transmembrane transporter activity (IMP, PMID:16905647), iron-sulfur cluster
  binding (IDA). Heme uptake through Dpp uses a different binding protein and
  does not contradict the dipeptide term.
- PTN000656054 (GO:0022857 transmembrane transporter activity; 4 seeds:
  E. coli SapD P0AAH4, OppD P76027, DppD P0AAG0 and PA4505): 80 leaves, an
  OppD/DppD/SapD-type ATPase clade of mixed substrates; the general term suits
  it.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000656054 | GO:0022857 transmembrane transporter activity | 4 | 80 (31 taxa) | GO:0071916, IDA, PMID:25338022 (PseudoCAP) | SOUND | General transporter term for a mixed-substrate OppD/DppD/SapD ATPase clade; other seeds are characterised E. coli ATPases. |
| PTN000656114 | GO:0071916 dipeptide transmembrane transporter activity | 1 (sole) | 6 (5 taxa) | GO:0071916, IDA, PMID:25338022 (PseudoCAP) | SOUND | Sound for DppD (operon deletion loses dipeptide use and phaseolotoxin uptake), though the code should be IMP. The node holds only DppD orthologs of characterised dipeptide importers, so the term suits the clade. |

Defects filed: PSEUDOCAP WRONG_EVIDENCE_CODE (IDA -> IMP, CHECK) on the IDA row.
No GO_CENTRAL defect.

## Decisions summary

- ACCEPT: dipeptide transmembrane transporter activity (IBA, IDA; IDA with an
  evidence-code defect), ATP binding, ATP hydrolysis activity, plasma membrane.
- MODIFY: nucleotide binding -> ATP binding; peptide transport and dipeptide
  transmembrane transport -> dipeptide import across plasma membrane.
- NEW: part_of ABC transporter complex, substrate-binding subunit-containing
  (IC).
