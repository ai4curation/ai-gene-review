# VPS1 (YKR001C, P21576) curation notes

## Session 2026-11-17: provenance of the research

- `just deep-research-falcon yeast VPS1 --fallback perplexity-lite` failed: neither the
  falcon nor the perplexity provider is configured in this environment
  ("Provider 'falcon' not available. Available: openscientist, claude_code").
  No `VPS1-deep-research-*.md` file exists; everything below is my own reading of the
  cached publications.
- `just mod-description-deep-research yeast VPS1` failed twice: the Alliance API
  (www.alliancegenome.org) timed out. No SGD description file was written.
- Literature search: PubMed esearch queries "Varlakhanova[au] Vps1",
  "Arlt[au] Vps1 retromer", "Smaczynska-de Rooij[au] Vps1",
  "Hoepfner[au] Vps1 peroxisome", "Vps1 phosphatidylinositol". From the results I
  cached PMID:30087125, PMID:25512334, PMID:31009484, PMID:11733545, PMID:26711254
  and PMID:22082017 in addition to the 18 GOA references.
- PAINT losses (`gene_paint_losses yeast VPS1`): "No IRD or IKR loss on this gene's
  lineage." PTHR11566 paint.tsv has no IRD/IKR rows at all.

## Identity and domain architecture

- 704 aa dynamin-related protein (DRP); synonyms LAM1, SPO15. UniProt: Dynamin-type G
  domain 26..336 and GED 618..704; InterPro Dynamin_GTPase, Dynamin_stalk, GED; no PH
  domain and no proline-rich domain (PRD).
- "it does not contain a pleckstrin homology domain (PH domain)" [PMID:31009484]. In
  place of the PH domain it has "Insert B", which binds lipids directly
  [PMID:31009484 "the region Insert B, located in a position equivalent to the dynamin PH domain, is able to bind directly to lipids"].
- "Unlike classical dynamins, Vps1 does not have a proline-arginine domain that could
  interact with SH3 domain-containing proteins" [PMID:22082017]; it instead has a
  single type I SH3-binding motif that binds the Rvs167 SH3 domain [PMID:22082017].
- One of three yeast DRPs (Vps1, Dnm1, Mgm1); the only one acting in membrane
  trafficking [PMID:25772449 "Vps1 is one of three dynamin-like proteins in yeast but is the only one of these dynamins that functions in membrane trafficking pathways."].
- Structure: "The Vps1 helix is more open and flexible than that of dynamin"; a novel
  GTPase-GTPase interface replaces dynamin's BSE-stalk contacts, and disrupting it
  abolishes function in vivo [PMID:30087125].

## Molecular function: a membrane-scission GTPase

- Binds and hydrolyses GTP [PMID:8299420 "As predicted from the sequence, Vps1p binds and hydrolyses GTP."].
- Cell-free reconstitution [PMID:42477131 "Vps1 assembles into scaffolds on membrane tubules, and uses GTP hydrolysis to force tubule constriction and fission"]:
  - basal turnover ~0.6 min-1; ~30-fold stimulation by PC:PS:PI(3)P vesicles;
  - no fission with GDP, GppNHp or no nucleotide;
  - K42A (no hydrolysis) and G436D (self-assembly) mutants bind membranes normally,
    fail to cut, and do not rescue Vps10 retrieval in vivo;
  - fission requires phosphoinositides but is promiscuous for headgroup; a lysine-rich
    "3K" motif (591-593) is "a generic, non-specific phosphoinositide-binding motif"
    and a phenylalanine-rich "4F" motif (579-587) drives self-assembly.
- **Disputed point.** Varlakhanova et al. found "only modest lipid-stimulated GTP
  hydrolysis" [PMID:30087125] (with PS liposomes and PS/PI3P nanotubes, using purified
  Chaetomium thermophilum Vps1, which rescues S. cerevisiae vps1Δ), and PMID:42477131
  cites this as the challenge it resolves. The 2026 paper reports strong stimulation
  only when phosphoinositides are present in a PS-rich membrane.
- GO: GO:1990606 "membrane scission GTPase motor activity" (is_a GTPase motor
  activity is_a GTPase activity; checked in OLS) fits the 2026 data. It is the term the
  S. pombe Vps1 GO-CAM uses (gocams/index.tsv, gomodel:6918f23700004722).
- Lipid binding: GO:1901981 "phosphatidylinositol phosphate binding" is supported by
  PMID:42477131 (binding to PI(3)P, PI(4)P, PI(3,5)P2 and PI(4,5)P2, lost in the Δ3K
  mutant) and PMID:31009484 (Insert B binds lipids; KKK-AAA reduces PI(4,5)P2 binding).
  Proposed as NEW.
- Actin: Vps1 binds F-actin (Kd ~1.9 µM for yeast actin) and bundles filaments in
  vitro; the RR457-458EE stalk mutant binds actin more weakly, cannot bundle, and is
  defective only in endocytic scission [PMID:25772449]. E461K binds actin like wild
  type but does not form actin-induced double rings or bundles [PMID:26478779].

## Biological roles

1. **Endosome-to-Golgi retrograde transport (best supported).**
   - Vps1 "primarily localizes to and functions at the endosomal compartment"
     [PMID:30087125]; it colocalizes with FYVE-labelled endosomes [PMID:30087125] and
     is present at the late endosome [PMID:23385815].
   - "Vps1 is required for fission of cargo-containing, SNX-BAR–coated tubules from the
     endosome" [PMID:24567361]; Mvp1 (SNX8 homologue) promotes Vps1 association with
     the endosome; cargo export "completely fails in vps1-null cells".
   - Recycling of Vps10 from vacuoles needs retromer, Vps1 and Ypt7, and "Retromer and
     Vps1 leave the vacuole together with the cargo" [PMID:25512334].
   - Proteomics of vps1Δ vacuoles show "a broad range of Golgi and plasma membrane
     proteins that mis-sort to the vacuole without Vps1" [PMID:42477131].
   - The classic VPS phenotype (CPY mis-sorting, [PMID:8299420]) and late-Golgi
     membrane protein retention defects (UniProt FUNCTION, PubMed:8344247; grd screen
     PMID:8649377) are consequences of this retrieval role.
2. **Endocytic invagination and scission.**
   - Transient burst of localisation to endocytic sites; vps1 mutants have invagination
     defects [PMID:20841380].
   - Works with amphiphysin Rvs161/Rvs167: SH3-motif interaction, and "an
     Rvs161/Rvs167 heterodimer can disassemble Vps1 oligomers" [PMID:22082017].
   - Scission needs the actin interaction [PMID:25772449], Insert B PI(4,5)P2 binding
     [PMID:31009484] and Pho85-dependent S599 phosphorylation [PMID:26711254]. Each of
     these mutants is defective only in endocytosis, which argues for a direct role.
   - The role was long debated [PMID:26478779 "While its function in endocytosis has previously been controversial this is likely due to some redundancy in its fission function with the amphiphysins (Rvs161/Rvs167)"].
3. **Peroxisome fission.**
   - vps1Δ cells have one or two giant peroxisomes [PMID:11733545].
   - Vps1 and Dnm1 are independent, partly redundant fission machineries; Vps1-dependent
     fission is independent of Fis1/Mdv1/Caf4, contributes most on glucose, and Vps1
     overexpression does not rescue mitochondrial fission in dnm1Δ [PMID:18445678].
   - A fraction of Vps1 fractionates with peroxisomes, stabilised by Pex19 binding at
     residues 509-523 [PMID:16520372].
4. **Atg9 trafficking in autophagy.**
   - vps1Δ blocks bulk autophagy as strongly as atg9Δ (Pho8Δ60) and impairs the Cvt
     pathway; GTPase-dead mutants do not rescue [PMID:37060997].
   - "In the absence of Vps1, Atg9 fails to reach the sites of autophagosome formation"
     [PMID:37060997].
   - Location: BiFC between Vps1 and Atg9 persists in atg11Δ and atg17Δ cells that lack
     a PAS, so "the Vps1–Atg9 interactions indeed occurs at the Atg9 reservoirs"; there
     was only minimal colocalisation of Vps1 with Atg9 [PMID:37060997]. This argues
     against the IMP "is_active_in phagophore assembly site" row.
5. **Vacuole fusion and fission.** Vps1 polymers on the vacuole couple t-SNAREs; Sec18
   and the t-SNARE release Vps1 at the onset of fusion [PMID:15550248, abstract only].
6. **Break-induced replication (screen hit).** The VPS1 deletion was in the "Cellular
   Trafficking (33)" group of PMID:41398407 Supplementary Data 3.1, with "Decrease" in
   both the ectopic (AM3422) and Chr III disomic systems. Supplementary Data 2.1/2.2
   give vps1Δ BIR efficiency 0.21 (AM3422) and 0.11 (YSJ131). The main text does not
   discuss VPS1, and no mechanism is proposed. Supplementary xlsx files were downloaded
   to the scratchpad only and are not retained.

## Location summary

- Cytosolic pool plus punctate membrane structures: endosomes (FYVE, late endosome,
  SNX-BAR tubules), endocytic actin patches (transient), peroxisomes (a fraction),
  vacuole membrane, and Atg9 reservoirs.
- Mitochondria: only in organelle proteomics (HDA, PMID:24769239, PMID:16407407). No
  function there (PMID:18445678). Treated as likely co-purification of a peripheral
  membrane-binding dynamin.
- Microtubules: the SPO15-era UniProt FUNCTION text says "it binds microtubules", but
  "no requirement for microtubules was found for Vps1p function in protein sorting"
  [PMID:8299420]. Vps1 lacks the PRD that carries MT binding in classical dynamin.

## Decisions summary (see review YAML)

- GTPase activity: ACCEPT (IBA, IEA, IDA 8299420). MODIFY to GO:1990606 where the row's
  own evidence is the 2026 reconstitution paper (IDA/IMP PMID:42477131).
- Over-annotations: microtubule and microtubule binding (IBA), mitochondrion and MOM
  (HDA), phagophore assembly site (IMP), BIR (HMP).
- General terms refined: vacuolar transport → protein targeting to vacuole; autophagy →
  autophagosome assembly; peroxisome organization (IDA/IMP) → peroxisome fission.
