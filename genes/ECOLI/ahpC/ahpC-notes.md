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


## 2026-10-26 — native AhpC/AhpF module re-review

Re-reviewed every original annotation against native E. coli evidence and cross-species donor comparisons. The 53 ordered original annotation payloads and four raw UniProt/GOA files are preserved; no NEW rows are added. Actual Falcon plus perplexity-lite fallback attempts failed, as did FEBA retrieval (no reachable local or remote source); publication retrieval succeeded. Logs are in `.cache/module-audit-logs/alkyl-hydroperoxide-classical/`. No generated provider report or fitness result was fabricated.

The current raw P35340 record gives `GN Name=ahpF`. The historical `genes/ECOLI/AhpF/AhpF-*` artifacts are relocated to `genes/ECOLI/ahpF/ahpF-*`, retaining raw bytes. Earlier journal references to the uppercase folder describe the prior state and are superseded by this update. Existing history identity is frozen and `superseded_by` records the new canonical target. Dependent PANTHER family citations and three project machine indexes are updated as a necessary rename consequence; this is not a new family or taxon assignment.

Native E. coli work establishes the NADH→AhpF→AhpC relay [PMID:28270505, “The mutants also exhibited a decrease in H2O2 reduction by the AhpF-AhpC ensemble.”]. The peroxide-attacking AhpC and NADH-oxidizing AhpF perform different chemical steps. Existing reviews retain explicit individual molecular functions and record contribution to the overall NADH-dependent reaction. This is judged from the chemistry, not an ordinary GOA relationship string. The GO convention for assigning the whole-system MF to the catalytic subunit remains a question. No arbitrary thioredoxin or AhpF partner from another species is substituted into the native route.

Native genetics distinguishes low endogenous peroxide removal from high-peroxide catalase capacity [PMID:11717276, “These data demonstrate that in wild-type cells Ahp rather than catalase is the primary scavenger of an endogenous inducer of the OxyR regulon.”]. Broad oxidative response is refined to both hydrogen-peroxide and alkyl-hydroperoxide responses, rather than keeping a common ancestor as non-core. Core cell-redox homeostasis is retained as direct maintenance of the peroxide environment; it is not simply an ancestor of cellular oxidant detoxification. QuickGO definitions and children were retrieved on 2026-10-26 and saved with the actual lookup logs.

### Corrections to the previous peripheral-annotation conclusions

Full PMID:23042987 was recovered normally as `publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC3510565_.md`. Results Figures 8–12 show BW25113 deletion/complementation, reduced DHB/enterobactin, rescue by entC or metabolic supplements, and a resolving-cysteine mutant separating peroxide resistance from the iron phenotype. The authors explicitly conclude that “the peroxidase activity of AhpC is not sufficient for AhpC to participate in cellular iron metabolism.” Thus the earlier suggested simple peroxide-protection explanation is retired. The biochemical step remains unresolved: the Discussion considers direct or indirect FMN reduction for chorismate synthesis, without measuring it. GO:0019290 is now UNDECIDED rather than confidently over-annotated; no new FMN-reductase activity is asserted. The proposed experiment now tests a separate redox contribution rather than assuming peroxide scavenging explains the phenotype.

Sulfate-starvation, membrane, and peptidyl-histidine-phosphorylation experimental annotations are also UNDECIDED. Full Wiley and ScienceDirect recovery was attempted but failed; the accessible abstracts do not expose the exact AhpC observations. A soluble cytosolic pool does not exclude membrane association. Sulfate/cysteine repression is real curated context but does not resolve the experimental process basis. Detection as a modified substrate would not establish phosphorylation catalysis, but the abstract alone cannot establish that this is all the curator saw. No confident misattribution or contamination claim is retained.

PMID:7499381 mainly describes Tpx but explicitly contrasts its localization with AhpC: “whereas the 24-kDa AhpC resides mainly in the matrix.” This is independent support for the intracellular AhpC pool, not evidence that AhpC has Tpx's periplasmic localization. The soluble localization, dynamic oligomeric state and native AhpF relay are kept separate from high-throughput associations. Bare protein-binding removals retain the reported interactions and follow the uninformative-binding policy.

### Final paired-reaction decision after annotation-reviewer consultation

The preceding historical MODIFY treatment of GO:0102039 is superseded. Native E. coli genetics and reconstitution establish the AhpCF coupled reaction, and the ordinary GOA relationship string is inert in this review. Both AhpC rows and the AhpF row are ACCEPT, consistent with the separately reviewed Salmonella and Bacillus components. This accepts the real coupled activity without asserting that an isolated subunit catalyzes both half-reactions. The individual molecular functions and `contributes_to_molecular_function` core representation remain explicit. H. pylori's NADH rows are a different biological question because the tested native donor is NADPH through thioredoxin, not AhpF.
