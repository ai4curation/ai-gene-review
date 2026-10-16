# ahpC (E. coli K-12, P0AE08) notes

## 2026-10-16 initial review (issue #4032)

Symbol check: UniProt P0AE08 `GN   Name=ahpC; OrderedLocusNames=b0605, JW0598`, so
the folder is `genes/ECOLI/ahpC/` (lowercase, unlike the partner `genes/ECOLI/AhpF/`
folder, which follows its own UniProt record).

No deep-research file was generated for this gene; the review is built from the
UniProt record, the cached publications seeded from GOA, and the existing
`genes/ECOLI/AhpF` and `genes/PSEPK/ahpC` reviews.

### Function

- AhpC is the 2-Cys peroxiredoxin (AhpC/Prx1 subfamily) half of the AhpC/AhpF
  alkyl hydroperoxide reductase. [file:ECOLI/ahpC/ahpC-uniprot.txt "Thiol-specific
  peroxidase that catalyzes the reduction of hydrogen peroxide and organic
  hydroperoxides to water and alcohols, respectively."]
- Peroxidatic Cys47 and resolving Cys166 form an intersubunit disulfide in the
  oxidized enzyme [file:ECOLI/ahpC/ahpC-uniprot.txt "Interchain (with C-166); in
  linked form"]; AhpF reduces that disulfide using NADH
  [PMID:28270505 "AhpF is a flexible multidomain protein that enables a series of
  electron transfers among the redox centers by accepting reducing equivalents
  from NADH."].
- Seaver and Imlay showed Ahp is the primary scavenger of endogenous H2O2; Ahp
  plus catalase mutants cannot scavenge H2O2 and accumulate it
  [PMID:11717276 "Thus, Ahp provides the scavenging activity that persists in
  catalase null mutants."].
- Decameric ring structure; AhpF binds the ring
  [PMID:25372677 "EcAhpC (3.3 Å resolution) forms a decameric ring"].

### Donor-scope decision (GO:0102039)

GO:0102039 NADH-dependent peroxiredoxin activity (EC 1.11.1.26, RHEA:62628) is
the overall NADH + hydroperoxide reaction. NADH is consumed by AhpF, not AhpC;
AhpC carries out the peroxide-reducing half reaction. Following the PSEPK ahpC
precedent and the AhpF review (which records GO:0102039 as
`contributes_to_molecular_function`), both AhpC GO:0102039 rows are MODIFY to
GO:0051920 peroxiredoxin activity, and the core function records
`contributes_to_molecular_function: GO:0102039`. The EXP row (PMID:11717276)
is not disputed biologically: the paper shows that the AhpCF system scavenges
H2O2 in vivo with NADH as the reductant; the change is only about which subunit
the single-gene-product MF should name. This is raised as a suggested question.

### Peripheral rows

- Sulfate starvation (PMID:8774726): AhpC is SSI8, induced on non-sulfate S
  sources; expression change only.
- Peptidyl-histidine phosphorylation (PMID:35636362): AhpC was detected as an
  N-phosphoprotein in a phosphoproteomics method paper; being a substrate does not
  make it a participant in the phosphorylation process.
- Siderophore biosynthesis (PMID:23042987): ahpC deletion lowers enterobactin;
  the authors place the defect at EntC or chorismate supply, mechanism unknown;
  kept as non-core.
- Membrane HDA (PMID:16858726): complexome BN-PAGE; conflicts with the soluble
  cytosolic localization supported by several IDA/HDA rows.

### Module

Added the AhpC peroxide-reduction annoton to
`modules/bacterial_alkyl_hydroperoxide_reductase.yaml`, linked from the AhpF
annoton with PROVIDES_INPUT_FOR (reduced AhpC), and dropped the CURATION-only
knowledge gap that tracked the missing ahpC review.

### Review follow-up (PR #5069)

- GO:0033194 (IMP, PMID:7733872) refined to GO:0033195: the rescue evidence is
  alkyl-hydroperoxide specific.
- Siderophore biosynthesis IMP moved to MARK_AS_OVER_ANNOTATED (indirect, no
  AhpC-performed step).
- The AhpC/AhpF system also reduces peroxynitrite
  [PMID:28270505 "to detoxify ROS such as hydrogen peroxide, organic
  hydroperoxide, and peroxynitrite"]; not annotated here because no E. coli
  AhpC-specific peroxynitrite assay is cached.
