# CTNNA1 (alpha-E-catenin, human P35221): review notes

Automated deep research was unavailable for this gene (no deep-research provider
keys in this environment). These notes were written by hand from the cached
publications in `publications/`, the UniProt entry (`CTNNA1-uniprot.txt`) and a
PANTHER tree query (`CTNNA1-bioinformatics/`). They are part of Track B of the
Origins of Multicellularity project: a normal GO review of the human gene, plus
which functions are ancestral and which are animal recruitments.

## Molecular function

- **Beta-catenin / plakoglobin binding (N-terminal domain).** Direct binding:
  [PMID:7890674 "the amino-terminal half independently binds alpha-catenin"];
  [PMID:7890674 "Plakoglobin, also known as gamma-catenin, directly binds to both APC and alpha-catenin"];
  the plakoglobin site maps to its first armadillo repeat
  [PMID:7650039 "the alpha-catenin-binding region maps within the first repeat"].
- **Not a direct cadherin or APC binder.** Alpha-catenin reaches cadherin through
  beta-catenin [PMID:16184169 "the cytoplasmic domain binds beta-catenin, which then recruits alpha-catenin"]
  and APC through beta-catenin
  [PMID:7890674 "alpha-Catenin cannot directly bind APC but associates with it by binding to beta-catenin"].
  So the cadherin binding rows (IPI/HDA/IEA) are marked over-annotated, not removed.
- **Monomer/dimer switch** (mouse protein, in vitro):
  [PMID:16325583 "Monomeric alpha-catenin binds more strongly to E-cadherin-beta-catenin, whereas the dimer preferentially binds actin filaments."];
  [PMID:16325583 "alpha-catenin directly regulates actin-filament organization by suppressing Arp2/3-mediated actin polymerization"].
  The complex does not bind actin in solution
  [PMID:16325582 "alpha-catenin does not interact with actin filaments and the E-cadherin-beta-catenin complex simultaneously"].
  Human alpha-catenin crystallizes as an asymmetric homodimer
  [PMID:23292143 "α-catenin forms an asymmetric dimer where the four-helix bundle domains of each subunit engage in distinct intermolecular interactions"].
- **Force-dependent F-actin binding (catch bond):**
  [PMID:25359979 "the minimal cadherin-catenin complex formed stable bonds with an actin filament under force"];
  [PMID:25359979 "Bond dissociation kinetics can be explained by a catch-bond model in which force shifts the bond from a weakly to a strongly bound state."].
- **Vinculin binding (M domain):**
  [PMID:9700171 "All these results indicate that αE-catenin can directly bind to the head domain of vinculin at the 326–509 domain."];
  needed for the apical junctional complex
  [PMID:9700171 "the alphaE-catenin-vinculin interaction plays a role in the assembly of the apical junctional complex in epithelia"].
- **Other junctional adaptor partners** (no specific GO binding terms, so the
  generic protein binding rows were removed):
  - EPLIN [PMID:18093941 "an actin-binding protein, couples with alpha-catenin and, in turn, links the cadherin-catenin complex to F-actin"]
  - centralspindlin and ECT2 [PMID:22750944 "We therefore conclude that α-catenin serves as a cortical anchor for centralspindlin at the zonula adherens, to thereby support the Ect2-Rho signalling pathway."]
  - CAP350 [PMID:25764135 "A two-hybrid screen for centrosomal protein partners revealed a consistent high-confidence interaction of CAP350 with the adhesion protein α-catenin."]
  - IkappaB-alpha in E-cadherin-negative basal-like breast cancer cells [PMID:24509793 "Mechanistically, α-catenin interacts with the IκBα protein, and stabilizes IκBα by inhibiting its ubiquitylation and its association with the proteasome."]
- **PDZ fragmentomics rows (PMID:36115835, 21 rows).** These are PDZ-domain AP-MS
  hits. CTNNA1 has no known PDZ-binding motif, and the authors note that
  cadherin-complex proteins co-purify via beta-catenin's PBM
  [PMID:36115835 "E-cadherin and GIT1 proteins, both repeatedly identified by our PDZ-AP-MS assays, do not have any identifiable C-terminal PBM; they probably indirectly co-precipitate via their respective partners β-catenin (CTNNB1) and β-Pix (ARHGEF7)"].
  Removed as generic protein binding; PDZ domain binding was not proposed.

## Isoforms

The N-terminally truncated neural isoform 3 (CTNNA1b) lacks the beta-catenin
binding domain yet is at the membrane
[PMID:21708131 "N-terminally truncated CTNNA1 and CTNNA2 proteins lacking the β-catenin interaction domain are produced from these alternative CTNNA mRNAs"].

## GO-CAM

`gocams/index.tsv` has no row for CTNNA1 (P35221) (checked 2026-10-01). No GO-CAM
role to reconcile. Reactome models CTNNA1 in the CDH1 adherens junction pathway
(R-HSA-9817330 "CDH1:CTNNB1 complex binds CTNNA1", R-HSA-9934294 "CDH1-associated
CTNNA1 binds VCL", R-HSA-9934486 "CDH1-associated CTNNA1 binds F-actin").

## IBA rows and PANTHER placement

All six CTNNA1 IBAs cite PTN001052343. A PANTHER v19 tree query
(`CTNNA1-bioinformatics/panther_nodes.py`, RESULTS.md) shows this is the root of
PTHR18914 (ALPHA CATENIN), at the **Eumetazoa** level: its leaves are Nematostella
and bilaterians only. So the IBAs assert inheritance only within animals; all
were accepted (cell migration kept as non-core). CTNNA1 is among its own donors
for beta-catenin binding and catenin complex. That is expected, not circular.

The Dictyostelium alpha-catenin (ctnnA, Q54MH2, dictyBase DDB_G0285939) is in
PANTHER family PTHR46180 (VINCULIN), whose root PTN005285701 is at the Unikonts
level. That is the "Dictyostelium donor" on the human VCL beta-catenin binding
IBA noted in `genes/human/VCL/`. PANTHER therefore sends the amoebozoan
beta-catenin-type activity to vinculins, not to the animal alpha-catenins. Whether
ctnnA is a true alpha-catenin ortholog or a pre-split family member is open (see
suggested questions).

## Premetazoan / evolutionary context

- VIN family proteins predate animals
  [PMID:29880641 "VIN proteins link actin filaments to membrane proteins at the plasma membrane and are found in all animals and their close outgroups (choanoflagellates, chytridomycetes, apusozoa, amoebozoa)"];
  [PMID:29880641 "homologs of the vinculin/α-catenin family are widespread in eukaryotes including the social amoeba Dictyostelium discoideum"].
- Sponges already have a distinct alpha-catenin
  [PMID:29880641 "Op α-catenin grouped with other animal α-catenin sequences"];
  animal alpha-catenins share beta-catenin and actin binding
  [PMID:29880641 "but all α-catenins characterized to date bind β-catenin and F-actin at the AJ and developmental disruption of α-catenin leads to morphological abnormalities and death"].
  Sponge vinculin binds talin but not a beta-catenin peptide
  [PMID:29880641 "Moreover, Op vinculin bound talin but not β-catenin"].
  So in sponges the beta-catenin interface already looks alpha-catenin-specific.
  Sponge alpha-catenin itself was not tested.
- **Dictyostelium (non-animal, aggregative multicellularity).** PMID:21393547
  (Dickinson, Nelson & Weis 2011 Science; PubMed-verified, fetched with
  `just fetch-pmid`, read):
  - [PMID:21393547 "Although D. discoideum lacks a cadherin homolog"]
  - [PMID:21393547 "we identify an α-catenin ortholog that binds a β-catenin-related protein"]
  - F-actin co-sedimentation [PMID:21393547 "High-speed pelleting assay demonstrating binding of 5 μM full-length (FL) or the isolated tail domain of Dd α-catenin to 5 μM F-actin."]
  - [PMID:21393547 "Both proteins are essential for formation of the epithelium, polarized protein secretion and proper multicellular morphogenesis."]
  - [PMID:21393547 "the role of the catenins in cell polarity predates the evolution of Wnt signaling and classical cadherins"]
  - Follow-up, PMID:22902739: [PMID:22902739 "The polarity and morphology of the tip epithelium require an α-catenin ortholog and the β-catenin-related protein Aardvark that co-localize to the basolateral plasma membrane"].
- Caveats: Dictyostelium is an amoebozoan. Its tip epithelium arose
  independently of animal multicellularity (aggregative, not clonal), so these
  data show the catenin module is older than animals. They do not show that it
  worked in an epithelium of the animal ancestor. I found no experimental data
  on alpha-catenin in choanoflagellates or Capsaspora in the cached literature.

**Synthesis (ancestral vs animal-specific):**
- *Ancestral (pre-Amorphea, on Dictyostelium evidence):* a VIN-family protein
  that binds an armadillo beta-catenin-like protein and F-actin, and organizes
  cell polarity and polarized secretion in a multicellular context, without
  cadherins.
- *Animal-specific (on current evidence):* coupling to classical cadherins via
  beta-catenin (classical cadherins are animal-restricted); the sponge-level
  split into separate alpha-catenin and vinculin with distinct partners;
  force-dependent catch-bond actin coupling and tension-gated vinculin
  recruitment (only shown in vertebrate proteins); zonula adherens adaptor roles
  (EPLIN, centralspindlin/ECT2, CAP350); YAP/SMAD nuclear restraint; and all
  tissue and disease roles (gastric cancer, macular dystrophy).

## Decisions summary

- 53 protein binding IPI rows: 10 MODIFY (6 to beta-catenin binding, 3 to
  gamma-catenin binding, 1 to vinculin binding); 43 REMOVE as uninformative
  (including 21 PDZ fragmentomics rows).
- Totals over 129 rows: ACCEPT 48, REMOVE 48, MODIFY 14, KEEP_AS_NON_CORE 11,
  MARK_AS_OVER_ANNOTATED 8, NEW 0.
- Cadherin binding (5 rows) MARK_AS_OVER_ANNOTATED: the binding is indirect, via beta-catenin.
- Rat IEP-derived BP transfers (ovarian follicle development, male gonad
  development, odontogenesis, response to estrogen, axon regeneration) REMOVE.
- Structural molecule activity -> cytoskeletal adaptor activity;
  cytoskeletal protein binding -> actin filament binding; identical protein
  binding -> protein homodimerization activity.
- No NEW annotations. Negative regulation of Arp2/3-mediated actin nucleation
  was considered but left as a question: the evidence is mouse protein in vitro.


## 2026-10-13: source-specific augmentation

The preceding journal is preserved as historical content. The decisions and interpretation below supersede its generic-binding removals, PDZ screen description, automatic rejection of the five rat developmental/hormonal transfers, and blanket rejection of cadherin-associated binding. All 129 original annotation objects, qualifiers, supporting entities and omissions remain exact. The 64 original reference identities and findings are retained. The curated summary is in [CTNNA1-source-evidence.yaml](CTNNA1-source-evidence.yaml); it provides public or repository locators without publishing the raw reconstruction packet.

The genuine isolated gene fetch and publication caching completed. The actual Falcon request timed out, as did its configured perplexity-lite fallback. No provider report was produced or manually impersonated. The current research uses preserved official records, genuine cached/original sources and manual source-specific analysis. Existing main caches and old target/history bytes were protected; richer external originals and unsuccessful retrieval responses remain distinct from the selected cache version.

### Junctional activity and products

One integrated core describes performed membrane–cytoskeleton anchoring and cell-cell adhesion. The primary evidence distinguishes unloaded mouse/chicken reconstitutions in PMID:16325582/16325583 from the force-dependent mouse/zebrafish optical-trap experiment in PMID:25359979. These conditions reconcile the earlier negative simultaneous-binding result. PMID:23292143 uses human alpha-catenin 82–906 and vinculin 1–840; PMID:9700171 combines mouse constructs in human DLD-1, chicken material and mouse F9 rescue. Neither establishes an invariant full-length native stoichiometry. EPLIN, CAP350 and centralspindlin/ECT2 recruitment contribute to the junctional organizational picture without transferring the partners’ actin, microtubule, GAP or GEF activities to alpha-catenin.

Official product reconstructions match 906, 930 and 536 residues. Isoform 2 has the VSP_017494 insertion; isoform 3 removes residues 1–370, including the beta-catenin-binding interval. Sequence reconstruction is not functional equivalence. The short-product membrane attribution in PMID:21708131 is retained with curator deference because the complete assay was unavailable; beta-catenin recruitment is not offered as its mechanism. Gene-level source assertions retain their original absence of an isoform field.

### Binding and source limits

The campaign’s standing positive-binding instruction retains genuine generic associations as non-core when a supported, informative partner-class refinement is unavailable. This replaces the old uninformative-term removal rationale. Literal interaction records preserve mutation/fragment, host, role, expansion and negative fields. Co-immunoprecipitation, proximity and spoke-expanded AP-MS are not automatically purified binary interactions. The cadherin associations are retained with these limits rather than denied solely because the common linkage uses beta- or gamma-catenin.

PMID:36115835 contributes 24 source assertions, not the 21 described earlier in this journal. The actual experiment uses the native CTNNA1 terminal decapeptide and isolated tagged PDZ domains; it is not simply indirect PDZ AP-MS through beta-catenin. The original Dataset 1 contains 133 CTNNA1 measurements. All 71 literal curated fragment records map to values below the 0.05 DAPF detection threshold with composite pKd zero. The authors explicitly distinguish these censored values from noninteractions. Twenty-three source assertions remain unresolved rather than removed. DLG3 is a separate gene-level case: worksheet row 16323 measures PDZ2 weakly above threshold, once by DAPF, without an orthogonal FP result. This supports a PDZ-domain-binding refinement while leaving the curated PDZ1/3 records unresolved. The complete correction body (PMID:36477203) concerns Figure 2/4/5 presentation and does not replace Dataset 1. No new assertions are proposed for the other measured domains.

PMID:22658674 Supplementary Table S1, Excel row 28, directly identifies CTNNA1 in the UV-crosslinked mRNA interactome. Its ion-count adjusted p 0.0030253 meets the study’s either-method criterion despite DESeq 0.236597; the RNA-contact evidence is retained as contextual without inventing a transcript or regulatory function. The actual PMID:24509793 original supports IκBα co-association in specified breast-cell contexts and beta-catenin co-IP, not purified binary interfaces.

### Propagation, cellular context and access

All six actual PAINT IBDs are on the human path from PTN001052343 in the 168-node PTHR18914 tree, whose target MSA reconstructs 906 residues. Experimental target self-evidence is legitimate. Eleven complete donor queries, 679 records and 71 literal joins preserve original identifiers and aliases. Separate current Dictyostelium family classification is not itself a rejection of its genuine catenin-like biology or a resolution of deep orthology. Three ARBA rules were evaluated across 216 actual branches and each has a matching target branch.

The five rat IEP-derived developmental/hormonal assertions are UNDECIDED. The donor evidence is real, all four source abstracts explicitly concern rat, and full originals remained inaccessible. Expression context neither proves nor disproves performed participation. Estrogen-response terms do not require intrinsic sensing, and ameloblast experiments are not excluded from dentin-containing tooth development. In contrast, the original indole-3-carbinol experiment (PMID:10868478) was recovered and Figure 5 inspected: modest alpha-catenin abundance changes without target-specific functional separation leave that particular process assertion overextended.

The independent nuclear/flotillin source assessment recovered the Nature original for PMID:16184169 and inspected Figure 2a. Alpha-catenin nuclear-region signal in Caco-2 cells supports retaining the curator’s contextual localization; prose about ARHGAP10 is not reattributed. For PMID:24046456, original Results/Figure 1 caption text and exact mouse IDA support flotillin-complex association with curator deference, without an unseen-band or direct-binary claim. For PMID:21145499, coauthor Samavarchi-Tehrani’s authentic thesis reproduces the original study; Chapter 2 Figure 6C and its Methods/Results show that mouse Eph4 Ctnna1 knockdown enhances nuclear TAZ/YAP and TGF-beta-dependent SMAD2/3. This supports the two existing contextual regulation transfers without making CTNNA1 a transporter or kinase.

HPA antibody/cell-line records support nonexclusive plasma-membrane and junction localization; no image pixels or isoform-exclusive stain interpretation were added. Actual Reactome reconstruction finds 41 target paths through 178 objects across 13 cited events. Cytosolic component 191697 can sit within a membrane-associated complex, while the three older membrane events use 191735. Event titles do not assign another participant’s catalysis to CTNNA1. The selected GO-CAM index has no exact target hit.

### Review provenance and preserved quotation boundary

Manual owner read ledgers distinguish selected original paragraphs, complete abstracts, actual workbook measurements, literal records and external consultation. The independently read core 20, nonjunction 4, endocrine 5, PDZ 24 and context 4 consultations were fully reviewed and their read-only checkers reproduced before integration. Their actual primary-reading scope is attributed; it is not silently converted into a claim that the owner read every full paper or figure. A cache marked full-text available can still contain only selected sections. Target-table gaps remain explicit in reference assessments.

The original 10,071-byte journal prefix is unchanged. It already contains long and repeated historical quotations, some above the current per-source budget. No new primary-paper quotation is added by this augmentation, and old findings are preserved rather than duplicated in a new evidence mirror. The new index uses locators and paraphrased scope. Previous raw packets, failures and authored source boundaries remain in the research archive.


### Independent whole-review precision addendum

The original FERMT2, ABI1 isoform-2 and focal-adhesion assertions are now UNDECIDED because their specific target assays remain unresolved. The campaign's positive generic-binding exception does not establish an inaccessible target pair, and general cytoskeletal/junctional biology does not establish a separate focal-adhesion compartment. These decisions preserve the curated positive source objects without inferring false binding or absent localization. PMID:18093941 was read as its complete available abstract and selected Discussion, not operative main Results/Methods; positive EPLIN evidence remains, while the separate ABI1 assay is unresolved. The review's access flag and compact index now state that distinction.

Two source-description errors are corrected: the adherens-junction mapping lists UniProt location and mouse/rat inputs without InterPro, and P26231/ENSMUSP00000049007 is mouse in the homodimerization transfer. The standalone description retains the short product's N-terminal deletion fact; its recruitment evidence limit stays in the source-specific review, notes and questions. All 129 original source objects, three product objects, quotations and core terms remain unchanged. No new source or biological assertion is added.


## 2026-10-13 — donor bibliography and source-specific review follow-up

The bibliography now includes the nine donor papers previously named only in review prose, plus the actual complex-binding source, PMID:8834786. Complete cached abstracts were read for all ten. PMID:11025210 distinguishes the mouse catenin zonula adherens from the tight junction; PMID:12577316 reports the rat cardiomyocyte calcium-switch and anti-alpha-catenin intervention affecting Cx43 redistribution; PMID:17535849 explicitly places alphaE-catenin at intercalated discs. The specific alpha/beta-catenin assay in PMID:12960056 and alpha-catenin lamellipodial image in PMID:14657280 remain unverified. Those references disclose the target-assay limit instead of treating their whole papers as personally verified.

The four rat expression papers (PMIDs:10864803, 7507830, 12387456 and 10681393) establish positive ovarian, testicular, neural and tooth-development context. Their full originals remain unavailable. The five inherited process assertions therefore remain UNDECIDED. IEP is an evidence type, not a verdict: the GO best-practice discussion of expression studies (https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/) allows some response annotations but cautions that an abundance change need not establish participation. The separately recovered indole-treatment study was assessed from its actual experiments, including the absence of a target-specific functional test. Its overannotation judgment is not a universal rejection of expression evidence.

The RNA-binding conclusion remains non-core. The original HeLa interactome protocol uses UV crosslinking, stringent oligo(dT) capture and RNase release; its selection accepts significance by either quantification method. CTNNA1 qualifies in Table S1, Excel row 28, by ion counts despite the nonsignificant DESeq result. This supports RNA contact without establishing sequence preference, an RNA-regulatory role or a particular isoform. Protein abundance, an unfamiliar domain architecture and the age of a positive assay do not by themselves negate that result.

Broad complex binding is now non-core, supported by the two separable N-cadherin/alpha-catenin complexes described in PMID:8834786. Specific partner binding and junctional anchoring remain the informative principal activities. The BRAF refinement retains the actual tagged residue-600-mutant assay boundary. IM-29493-66/-154, -13764 and -932 record complementation, pull-down and BRET, respectively; their differing mutation-strength features do not establish a universal wild-type interaction. A focused question records the unresolved comparison.

All ten donor-cache files were genuine outputs of the earlier normal publication fetch. Three cited caches and the newly explicit complex-binding cache had been omitted from the publication plan: PMIDs 11025210, 12577316, 12960056 and 8834786 are now selected from those exact archived bytes. No source cache is rewritten or labeled as newly recovered full text. The complete earlier notes, machine annotation fields, three product identities and inherited source objects remain preserved. No additional verbatim excerpt is introduced in this bibliography/prose amendment; the separately prepared evidence-anchor amendment is composed by the publisher.


### Junctional anchoring and the cadherin-free actin pool

The core summary now separates junctional anchoring from cadherin-free actin organization. At junctions, N-terminal beta-catenin/plakoglobin engagement recruits alpha-catenin and force-dependent C-terminal F-actin binding reinforces its linkage to the cortex. Vinculin, EPLIN and centralspindlin support organization of the apical adhesion belt. CAP350 occupies basal portions of lateral contacts rather than the zonula adherens (PMID:25764135); these partner assemblies should not be assigned one identical location. The cytosolic homodimer binds and bundles actin and can restrain Arp2/3-mediated branching (PMID:16325583). Comparative Dictyostelium binding to Aardvark and F-actin (PMID:21393547) remains evolutionary context rather than a separate human function or a precise dating claim.

The cadherin interaction decisions retain the informative partner class of their source assays. Co-immunoprecipitation and affinity capture support a cadherin-associated assembly without mapping an isolated alpha-catenin–cadherin interface. A blanket substitution with beta-catenin binding would change the measured partner and, in PMID:7650039, the actual plakoglobin intermediary. The BioID-derived assertion retains curator deference and independent complex evidence; its inaccessible target assay is not claimed as verified. The revised core makes the recruitment and actin-binding activities explicit while retaining their existing annotation decisions.

Twenty-eight selected annotation excerpts and six core excerpts from the earlier repository review have been restored after checking their relevance and verbatim cache correspondence. Independent mechanistic support is distinguished from each original assay. The old PDZ passage concerns other proteins and has not been restored; the old UniProt nuclear-accumulation snippet does not match the current cache. Quantitative supplementary evidence and figure-only results keep their source locators without invented quotations. These restored excerpts supersede the earlier blanket omission described above.


### Indole response: expression evidence and participation

The positive alpha-catenin abundance response to indole-3-carbinol in PMID:10868478 is retained. GO:0071681 includes expression changes, and the GO best-practice guidance permits some response annotations based on expression patterns while also distinguishing expression from a demonstrated contribution. The source’s 24-hour human MCF-7/MDA-MB-468 experiment and Figure 5 show modest alpha-catenin increases alongside broader adhesion-protein and cellular changes. The authors propose a joint E-cadherin/catenin mechanism, without resolving an alpha-catenin-performed step. OVER is retained at that source-specific participation scope, not because expression annotations are categorically invalid or CTNNA1 must sense the compound. The original IDA field and inherited excerpt remain unchanged. Public source: https://link.springer.com/article/10.1007/s001090000088; guidance: https://pmc.ncbi.nlm.nih.gov/articles/PMC3706743/, expression-study section.


### 2026-10-14: cadherin-complex terminology and explicit beta-catenin binding

This entry supersedes the historical Molecular function bullet that assigned cadherin-binding rows as over-annotated and the later blanket ACCEPT disposition. Its statement about indirect recruitment describes an interface mechanism, not a prohibition on retaining positive complex-association annotations. The five existing GO:0045296 assertions (rows 114–118) are now KEEP_AS_NON_CORE: they retain a cadherin-associated partner class while the performed core is represented by beta-catenin binding, junctional anchoring and cadherin-free actin organization. This annotation-level designation does not imply that the cadherin junction is peripheral to alpha-catenin biology.

The four E-cadherin generic-binding refinements (rows 5, 11, 14 and 28) remain MODIFY because their original assays or literal curated records identify a cadherin partner. The mixed CDH26/beta-catenin row 26 also retains both source-supported replacements. The same evidential standard retains the three APC associations (rows 13, 21 and 23); no supported narrower APC partner-class term has been established, so those remain generic KEEP_AS_NON_CORE. Neither disposition transfers APC activity or claims that every association is a purified binary interaction.

Three sole mechanistic bridging excerpts in rows 5, 11 and 28 have been replaced with a short positive-complex excerpt from PMID:8834786. That complete abstract concerns cultured adult rat cardiomyocytes and N-cadherin complexes containing alpha-catenin with beta-catenin or plakoglobin. It corroborates the complex-association interpretation; it does not verify the original human E-cadherin screen, mutant construct or direct interface. The original IPI tuples, literal assay identities and access limits remain unchanged. The earlier PMID:16184169 bridge biology remains valid and is preserved in the historical notes and immutable previous review. The three replacement quotations contribute 24 words in total from PMID:8834786; no new quotation is added to these notes.

GO:0008013 is now an explicit third core molecular function, supported by the already present PMID:7890674 excerpt relocated from the anchoring core without duplication, plus the reconstitution literature (PMID:16325582). This restores machine-readable coverage of the four accepted beta-catenin-binding assertions without manufacturing a NEW annotation or repeating a biological-process assertion. Product 3 lacks residues 1–370, including the mapped N-terminal interface; equal beta-catenin recruitment across all three products is not asserted.

The optional FERMT2 and ABI1 reassessment leaves rows 4 and 9 UNDECIDED. Their exact curated source objects are preserved, but the inspected current export contains no matching source-partner record for either assertion, and the available original passages do not resolve either pair. The absence of a record is not negative binding evidence. Positive pair-specific PAR-3 and BRAF records remain separately supported with their existing assay and construct locators; generic screen-scale or unrelated nuclear prose has not been turned into a target-specific quotation. All other annotation actions, source fields, references, products and source-cache bytes remain unchanged.


### 2026-10-14: correction of interaction-partner identities

The earlier FERMT2 and ABI1 descriptions of rows 4 and 9, including the preceding reassessment, were incorrect. Q96KN1 is human LRATD2, historically BCMP101/FAM84B; Q9ERG0-2 is mouse Lima1/EPLIN-alpha. Row 4 remains UNDECIDED because its original target-specific assay is unresolved. Row 9 now refines to cytoskeletal protein binding from the original EPLIN assays; its partner isoform stays in WITH/FROM. No target isoform field is added.

Selected original indexed PMID:18093941 Methods/Results distinguish purified human alpha-E-catenin/mouse EPLIN-alpha binding from endogenous human DLD-1 association. Complete offline text and supplementary figures remain unavailable. Current exports lack the exact historical pair; this does not invalidate the original experiment. Official sequences reconstruct the 593-residue mouse alpha product by deleting residues 1–160 from the 753-residue beta product.

A bounded identity audit covered all 48 UniProt accessions across 95 supporting-entity occurrences in 90 rows, separating interaction partners from experimental donors. No additional name/species mismatch was found; historical NHERF3/PDZK1, Inadl/PATJ and DFNB31/WHRN names were reconciled as aliases. This corrects labels rather than rewriting curated accessions or repeating the full annotation review.

This entry also supersedes the historical statement that generic protein-binding rows were removed. Supported contextual associations remain KEEP_AS_NON_CORE under the standing project instruction; unresolved assertions remain UNDECIDED, and supported specific classes use MODIFY. The current review has no REMOVE actions. The three comparative cadherin caveats are shortened without changing their rat N-cadherin evidence scope. All inherited supporting-text excerpts remain byte-for-byte unchanged; no new quotation is added here or to row 9. All 129 source objects, 81 reference identifiers, three target products, three core functions and prior notes/history remain preserved.
