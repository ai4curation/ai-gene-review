# FANCA (human) — gene review notes

UniProt: O15360 (FANCA_HUMAN), 1455 aa. Gene on 16q24.3. Synonyms FAA, FACA, FANCH.
Accounts for ~60-65% of Fanconi anemia cases.

## Summary of function
FANCA is one of the eight Fanconi anemia (FA) proteins (FANCA, B, C, E, F, G,
L/PHF9, M) that assemble into the multisubunit **FA core complex** (FA nuclear
complex; GO:0043240; ComplexPortal CPX-6263 "Fanconi anemia ubiquitin ligase
complex"). The core complex is a nuclear E3 ubiquitin-ligase assembly (catalytic
RING subunit = FANCL, E2 = UBE2T/FANCT) that, in response to DNA interstrand
crosslinks (ICLs) encountered during replication, monoubiquitinates the
FANCD2-FANCI (ID2) heterodimer. Monoubiquitinated ID2 is loaded onto chromatin
and coordinates downstream nucleolytic incision, translesion synthesis (TLS), and
homologous-recombination repair. FANCA itself is not the catalytic subunit; it is
a large scaffolding/docking subunit and the principal protein-protein interaction
hub of the core complex.

## Key provenance

### Positional cloning / identity
- [PMID:8896564 "The gene encodes a protein of 1,455 amino acids that has no significant homology to any other known proteins, and may therefore represent a new class of genes associated with the prevention or repair of DNA damage."]

### Nuclear complex membership (GO:0043240)
- [PMID:9398857 "we demonstrate the FAA and FAC bind each other and form a complex"] and
  [PMID:9398857 "the FAA-FAC complex is found in similar abundance in both cytoplasm and nucleus"]
- [PMID:11063725 "FANCF was found predominantly in the nucleus, where it complexes with FANCA, FANCC and FANCG"]
- [PMID:12649160 "The FANCA, FANCC, FANCE, FANCF, and FANCG proteins form a nuclear complex required for the monoubiquination of the FANCD2 protein"]
- [PMID:22343915 "We show that FAAP20 is an integral component of the FA nuclear core complex. We identify a region on FANCA that physically interacts with FAAP20, and show that FANCA regulates stability of this protein."]
- [PMID:22266823 "We identified Fanconi anemia-associated protein (FAAP20), an integral subunit of the multisubunit Fanconi anemia core complex. FAAP20 binds to FANCA subunit and is required for stability of the complex and monoubiquitination of FANCD2."]
- UniProt SUBUNIT: "Belongs to the multisubunit FA complex composed of FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL/PHF9 and FANCM."

### Interstrand cross-link repair (GO:0036297) / DNA repair (GO:0006281)
- [PMID:19965384 "A central event in the activation of the Fanconi anemia pathway is the mono-ubiquitylation of the FANCI-FANCD2 complex"] — FANCA is a core-complex subunit required for this activation.
- [PMID:22266823 "the FA proteins cooperate in a DNA damage response (DDR) pathway required for DNA interstrand crosslink repair"] and
  [PMID:22266823 "Eight of the FA proteins comprise the FA core complex, a multisubunit complex required for DNA damage recognition at a stalled replication fork"]

### Subcellular location
- Nucleus (major functional form) and cytoplasm (minor form):
  UniProt SUBCELLULAR LOCATION "Nucleus. Cytoplasm. Note=The major form is nuclear. The minor form is cytoplasmic."
- [PMID:9398857 "Although unbound FAA and FAC localize predominantly to the cytoplasm, the FAA-FAC complex is found in similar abundance in both cytoplasm and nucleus"]
- Nuclear localization + phosphorylation required for function (UniProt refs PMID:9742112, PMID:9789045; NLS motif 18-34).
- Chromatin loading is DNA-damage-induced: [PMID:22343915 "the FAAP20-UBZ domain ... is required for DNA-damage-induced chromatin loading of FANCA and the functional integrity of the FA pathway"]

### Protein interactions (all GO:0005515 protein binding — uninformative MF; scaffold/hub role)
FANCA is the central interaction hub of the core complex. Verified partners in cached lit:
- FANCG (O15287): [PMID:10627486 "found a strong interaction between FANCA and FANCG proteins"];
  [PMID:10652215 "a high level of activation was found when FANCA was co-expressed with FANCG, indicating strong, direct interaction between these proteins"];
  [PMID:12649160 "FANCG was shown to interact with both the amino-terminus of FANCA"]
- FANCF (Q9NPI8): [PMID:11063725 "complexes with FANCA, FANCC and FANCG"]
- FAAP24 (via FANCM), FAAP100 (Q0VG06): [PMID:17396147 "FAAP100 is essential for activation of the Fanconi anemia-associated DNA damage response pathway"]; [PMID:17289582] FAAP24 targets FANCM.
- FAAP20/C1orf86 (Q6NZ36): [PMID:22343915], [PMID:22705371 "FAAP20, a component of the FA core complex"], [PMID:22266823 "FAAP20 binds to FANCA subunit"]
- SMARCA4/BRG1 (P51532), SWI/SNF: [PMID:11726552 "We identified an interaction between the FA protein, FANCA and brm-related gene 1 (BRG1) product"]; [PMID:11726552 "we demonstrated co-localization in the nucleus between transfected FANCA and BRG1"]
- ERCC4/XPF (Q92889) + nonerythroid αII-spectrin: [PMID:12571280 "alphaSpIISigma*, FANCA and XPF co-immunoprecipitate with each other from normal human nuclear proteins"]
- GRB2 (P62993): SH3 peptide-array screen [PMID:17474147] — high-throughput, peripheral.
- Large-scale interactome / proteomics screens (FANCG or FAAP100 baits): PMID:16189514, PMID:28514442, PMID:32814053, PMID:33961781, PMID:35271311, PMID:37398436, PMID:40205054 — high-throughput, uninformative.

### regulation of regulatory T cell differentiation (GO:0045589, IBA)
Phylogenetic (PANTHER/GO_Central) inference seeded from mouse Fanca (MGI:1341823).
Peripheral/pleiotropic; not a core molecular function of the DNA-repair scaffold.
Treat as non-core.

### protein-containing complex assembly (GO:0065003, TAS PMID:9398857)
FANCA is required for formation/stability of the FA core complex (binds FANCG/FANCF/FAAP20;
regulates FAAP20 stability). Genuine but essentially a restatement of complex membership.

## Structure
Cryo-EM structures of the human FA core complex: PDB 7KZP/7KZQ/7KZR/7KZS/7KZT/7KZV
(1-1455). FANCA is largely α-helical (Pfam FANCA_arcN, FANCA_helical, FANCA_CTD, Fanconi_A_N).

## Action plan for annotations
- GO:0043240 FA nuclear complex (IBA/IEA/NAS/IDA x7): ACCEPT (core; must be consistent).
- GO:0005515 protein binding (all IPI): MARK_AS_OVER_ANNOTATED (uninformative; hub role captured in core_functions/notes).
- GO:0036297 ICL repair (IEA/NAS): ACCEPT (core BP).
- GO:0006281 DNA repair (TAS): ACCEPT (correct broader BP).
- GO:0005634 nucleus (IEA/IDA/TAS): ACCEPT (functional location).
- GO:0005654 nucleoplasm (IDA/TAS x10): ACCEPT.
- GO:0000785 chromatin (IDA): ACCEPT (DNA-damage-induced loading).
- GO:0005737 cytoplasm (IEA/TAS): KEEP_AS_NON_CORE (minor/inactive form).
- GO:0005829 cytosol (TAS): KEEP_AS_NON_CORE.
- GO:0065003 complex assembly (TAS): ACCEPT.
- GO:0045589 Treg differentiation (IBA): KEEP_AS_NON_CORE (pleiotropic, mouse-ortholog-derived).


## 2026-10-25 — preserved acquisition and lane chronology

The following acquisition and lane checkpoints are historical. Their counts, scope limits and status labels describe those stages; the final integration entry below supersedes the database-only nucleus refinement and inherited core wording. The earlier journal is retained byte-for-byte above.

# Agent-authored FANCA intake notes

2026-10-25: Preserved the complete existing review and journal before an isolated source refresh. The fresh PENDING seed is a mechanical comparison only. The inherited 49 imported reviews, three NEW proposals, 40 reference objects, 32 quotation anchors, three products and one core await explicit manual review.

The current source resolves three formerly broad binding contexts into distinct partner contexts. Both old and current coordinates are retained; no decision or quotation is copied, reset or silently reassigned. The source-family proof verifies actual ancestry without deciding the biology of either ancestral annotation.

The genuine default provider/fallback attempt failed. The old affinage research remains an unchanged historical input, and no replacement provider text was authored. No original scientific article reading or new annotation judgment occurred at this stage. See REPORT.md and the machine-readable alignment/partition before assigning review work.


## 2026-10-25 database augmentation checkpoint

This checkpoint reviews 18 current database contexts against their exact legacy mapping. It preserves the legacy annotation order, all unassigned reviews, the three inherited NEW rows, all 32 quotation/reference/path associations, natural products, description, core and inherited status. The COMPLETE label above is historical; no whole-gene status was recomputed here.

The lane recommends 14 ACCEPT, one nucleus-to-nucleoplasm MODIFY and three KEEP_AS_NON_CORE decisions. HPA antibody scope, actual target-specific Reactome compartments and the valid PAINT target path are documented in [FANCA source guide](FANCA-source-guide.md). Cytoplasmic and PKR-associated cytosolic pools are positive context rather than uniformly inactive preassembly. The mouse Treg inference remains valid and non-core: differentiation includes acquisition of mature functional features, and unchanged counts do not refute the suppressive-function phenotype.

Human nuclear complex/assembly evidence from PMID:22343915 is separated from Xenopus ID2 pathway reconstitution in PMID:19965384. The latter's inherited quotation remains exact. PMID:24501220 was genuinely fetched into a protected copied runtime and recovered as full main text; PMID:15299030 already existed and remains byte-exact. Earlier acquisition failures and bounded author-page reads remain recorded. Cache availability flags and external original reading are explicitly distinct.

Twenty-one whole-reference assessments are proposed separately, including two additional reference objects. No publication quotation was added, moved or rewritten. The private candidate retains all 40 original references until these proposals are applied; the companion candidate contains 42 references. Two private GeneReview schemas and strict legacy-GOA comparison passed. This checkpoint is not a canonical installation, fresh whole-gene approval or history publication.


## 2026-10-25 — agent-authored direct-evidence reassessment

This entry follows a frozen legacy baseline and does not rewrite the earlier journal. Historical action counts, COMPLETE status, core description and quotation wording above are preserved provenance, not a completed whole-gene conclusion from this lane. The 52 legacy objects contain 49 imported annotations and three inherited NEW proposals; the fresh acquisition has 52 imported contexts because three partner contexts expand. Both representations and their exact mapping are retained privately rather than replacing historical source objects with refreshed source fields.

The current direct lane contains 34 contexts: 10 ACCEPT, one MODIFY, 20 KEEP_AS_NON_CORE and three UNDECIDED. The three inherited NEW objects are separately retained with revised, narrower rationales and unchanged quotation associations. This is not an automatic endorsement of their old wording or a new quotation insertion. The 18 database contexts are outside this lane; their legacy reviews remain exact, and their current acquisition reviews remain PENDING.

Human FANCA supplies bounded physical organization in core assembly: restoring FAAP20 abundance alone does not restore partner coassociation in FANCA-deficient cells, and distinct FANCA regions support FANCG and FAAP20 contacts (PMID:22343915, Figures 2I and 3). The negative adaptor comparator result is retained; no curator omission is claimed. FAAP20 supplies the Rev1/ubiquitin bridge (PMID:22266823), while FANCL supplies ubiquitin-transfer catalysis. Purified FANCA ssDNA binding (PMID:22194614) and annealing linked to human SSA reporter rescue (PMID:30057198) independently support the other two inherited proposals at their measured scope. The broad DNA-repair source is refined only to ICL repair, avoiding a duplicate SSA replacement.

Nuclear localization is retained broadly because independent HPA nucleoplasm and experimental chromatin-associated pools are both positive. The narrower nucleoplasm definition excludes chromosomes; its evidence does not erase the chromatin pool. Cytoplasmic residence is also positive and is not declared universally inactive. This breadth is flagged for explicit reconciliation with the separate sealed database localization proposal. The legacy core and standalone description are deliberately unchanged here and still require whole-gene synthesis; in particular, the old direct FANCA–FANCF wording is not established by the present coassociation evidence.

Supported generic-binding assertions are retained as non-core under the campaign exception. More informative terms were considered, but partner identity alone does not justify assigning adaptor, ATPase-regulator, SH3-mediated cellular signaling or heterodimer activity. BRG1, XPF and GRB2 remain access-limited UNDECIDED, with positive reports retained. The 32814053 validation source is not HuRI, and the 37398436 preprint identifier remains valid despite the later journal-version link.

All three natural products (1455, 297 and 1424 residues), the single historical core and all 32 inherited supporting-text paths/text/reference associations remain unchanged. No product equivalence, new publication quotation, source-cache rewrite or provider-authored file is introduced. The [direct source guide](FANCA-source-guide.md) records public paper/figure/table locators and distinguishes cache availability, external access and actual reading.


## 2026-10-25 — accepted-lane integration and core synthesis

Integrated the two accepted lanes while retaining all 49 historical imported source objects and three separately reassessed inherited NEW objects, in their exact order. The final historical view contains 25 ACCEPT, one MODIFY, 20 KEEP_AS_NON_CORE, three UNDECIDED and three inherited NEW. The fresh source audit has 52 imported contexts: 25 ACCEPT, one MODIFY, 23 KEEP_AS_NON_CORE and three UNDECIDED. Three partner pairs account for the difference; their two full current-context reasons remain labeled in the corresponding historical binding review. Neither old GOA nor old source objects were silently replaced with the fresh WITH fields.

The sole accepted-lane review overlay changes database current index 24 (historical index 2) from narrower nucleoplasm refinement to ACCEPT nucleus. Human chromatin-associated FANCA and independent HPA nucleoplasm support genuine nuclear breadth; nucleoplasm excludes chromosomes. The corresponding GO_REF:0000044 manual note is corrected consistently. All other lane reviews, including the three access-limited BRG1/XPF/GRB2 decisions and three inherited NEW reassessments, remain exact.

All 40 original reference identities, titles and findings survive; the two database additions produce 42 references. Four shared whole-reference assessments retain both complete labeled reading notes. PMID:19965384 relevance is explicitly adjudicated MEDIUM for executed Xenopus ID2 pathway context, with both input assessments retained privately. Cache flags and actual external original reading remain separate facts.

The standalone biological description and two core units distinguish FANCA-mediated protein organization in FA-complex assembly/ICL repair from directly measured DNA annealing in SSA repair. The first core retains its two historical quotation objects at the same exact paths. The second uses current GO:1990814 DNA/DNA annealing activity; ssDNA binding and measured ATP-independent strand exchange are described within that unit without redundant ancestor units or new annotation rows. The biochemical and U2OS results do not establish a FANCA nuclease/ATPase, universal RAD52 independence, direct FANCA–FANCF interface, or equivalence of the three natural products.

Two question/experiment pairs address coordination of assembly and DNA-directed activities and the natural-product differences. All 32 inherited quotation/reference/path associations remain exact, and no publication quotation is added. Historical COMPLETE is preserved as an input field pending ROOT's canonical recomputation, not newly asserted from this private packet. No canonical validator, renderer, history scaffold or Git mutation was run here.

The [FANCA source guide](FANCA-source-guide.md) gives public original/figure/table, HPA, Reactome, PAINT and typed ontology locators, with source and read-scope limitations. The private packet separately records exact input pins, split-context mapping, four reference unions, explicit overlays and executed focused validation.


## 2026-10-25 — PR 5521 feedback reassessment

The prior assembly interpretation is retained but its MF subtype is corrected: current GO:0030674 explicitly redirects integral protein-complex scaffolds to GO:0140378. Human FANCA-dependent FAAP20/FANCG/FANCM assembly and separable contact regions in PMID:22343915 support this specific structural role. Positive current human scaffold annotations to CCDC6 and CHIC2 were checked as convention examples, with comparator abstracts only; the older negative selected-FA adaptor snapshot is not a universal exclusion.

The inherited NEW ssDNA-binding row is refined to DNA/DNA annealing (GO:1990814), a verified is_a descendant, with PMID:30057198 as its primary IDA source. The two older PMID:22194614 quotations are preserved verbatim at their exact original paths/reference associations and serve only as binding context. No additional row or quotation is introduced. The two core units remain scaffold organization and directly performed annealing. The broad DNA-repair refinement now lists both independently supported ICL and SSA branches; this does not attribute SSA experiments to the old TAS paper. Partner context labels are replaced by names, and the HPA row gains a bare GO_REF:0000052 support citation.

All 49 imported source objects, all 42 complete references and flags, three natural products and all 32 quotation associations remain unchanged. The two inherited authored NEW term objects are deliberately superseded as described; the SSA NEW source object is unchanged. Historical journal entries above remain historical. Actual main-text rereading, current typed ontology, exact before/after changes and validation receipts are retained in the private feedback packet. See the current [source guide](FANCA-source-guide.md) for source-specific evidence and access boundaries.


## 2026-10-25 — reproducible scaffold comparators

The current exact human GO:0140378 annotations to CCDC6 and CHIC2 are confirmed by the original 14:33 UTC QuickGO response and independent 15:04 UTC gene-specific queries. The unfiltered CHIC2 response also contains its same scaffold IDA record. The [public comparator snapshot](FANCA-scaffold-comparators.json) includes literal response bodies, identifiers, references, retrieval timestamps and hashes; the [source guide](FANCA-source-guide.md#assembly-repair-and-molecular-activities) explains the scope. The older repository CHIC2 machine file remains unchanged, and its precise fetch date is not inferred. These comparator records illustrate annotation usage; FANCA-specific assembly experiments remain the biological basis for its scaffold activity.

The scaffold term, both core units, every imported source object, three natural products and all complete reference assessments remain unchanged. No publication quotations are added, moved or reassigned. The inherited binding quotations remain at their original paths as explicitly labeled context, and the existing scaffold IPI source is retained alongside the independently cited physical-assembly evidence. No clinical prevalence or universal complex stoichiometry is inferred from the comparator check. Earlier journal entries and existing history records remain historical.
