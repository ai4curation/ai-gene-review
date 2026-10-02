# ATP7B (Wilson Disease Protein) - Research Notes

## Gene Identity
- **UniProt:** P35670 (ATP7B_HUMAN)
- **Gene symbol:** ATP7B (synonyms: PWD, WC1, WND)
- **Full name:** Copper-transporting ATPase 2 (EC 7.2.2.8)
- **Disease:** Wilson disease (WD) [MIM:277900]

## Core Function Summary

ATP7B is a P1B-type copper-transporting ATPase predominantly expressed in liver hepatocytes. Its two main physiological roles are:

1. **Copper incorporation into ceruloplasmin** at the TGN [PMID:12763797 "copper is incorporated into various cuproenzymes such as ceruloplasmin in hepatocytes (mediated by ATP7B)"]
2. **Biliary copper excretion** via vesicular sequestration and exocytosis [PMID:16472602 "the primary mechanism of biliary copper excretion involves ATP7B-mediated vesicular sequestration of copper rather than direct copper translocation across the canalicular membrane"]

## Key Structural Features

- Six N-terminal heavy metal-associated (HMA) domains, each with a GMXCXXC copper-binding motif [PMID:14709553 "six soluble N-terminal metal-binding domains containing a conserved CXXC metal-binding motif"]
- Eight transmembrane domains with a conserved CPC (Cys-Pro-Cys) motif essential for copper transport [PMID:9837819 "Mutation of the CPC motif resulted in a nonfunctional protein, which demonstrates that this motif is essential for copper transport by ATP7B"]
- Nucleotide-binding (N) domain, phosphorylation domain (DKTGTIT), phosphatase domain (TGE) [PMID:16567646]
- Can bind ~5.5 copper atoms per molecule [UniProt, PMID:20032459]

## Copper-Dependent Trafficking

ATP7B undergoes copper-responsive subcellular trafficking:
- **Low copper:** Resides at the TGN [PMID:16939419 "ATP7B...mediates the excretion of excess copper from hepatocytes into bile. Excess copper causes the protein to traffic from the TGN to subapical vesicles"]
- **High copper:** Redistributes to cytoplasmic/pericanalicular vesicles [PMID:16472602 "elevated copper levels stimulated trafficking of ATP7B to pericanalicular vesicles and not to the canalicular membrane"]
- **Copper removal:** Returns to TGN [UniProt CC, PMID:10942420]
- Trafficking is coupled to catalytic cycle: acyl-phosphorylation required for anterograde trafficking, dephosphorylation for TGN retrieval [PMID:16939419]

## Subcellular Localization Debate

There is a genuine controversy about the steady-state localization of ATP7B:
- **TGN model (majority view):** Most studies report TGN localization at basal copper, with copper-induced trafficking to vesicles [PMID:9837819, PMID:16472602, PMID:16939419, PMID:17919502]
- **Late endosome model (Harada group):** Harada et al. consistently report late endosome localization with Rab7 and NPC1 co-localization, arguing ATP7B is NOT a Golgi resident [PMID:15681833 "ATP7B is a late endosome-associated membrane protein...not a Golgi resident protein"]
- **Resolution:** The late endosome data may represent a post-Golgi compartment that ATP7B traffics through. The TGN model is more widely accepted and consistent with ceruloplasmin biosynthesis role.

## Important: ATP7B is NOT a Plasma Membrane Transporter

Key distinction: ATP7B primarily mediates copper excretion via **vesicular sequestration**, NOT direct translocation across the plasma membrane [PMID:16472602]. This is different from ATP7A which traffics to the basolateral plasma membrane [PMID:15269005].

## Protein Interactions

- **ATOX1 (copper chaperone):** Delivers copper to ATP7B N-terminal domains, stimulates catalytic activity [PMID:12029094 "Atox1 transfers copper to the purified amino-terminal domain of WNDP in a dose-dependent and saturable manner...leads to the stimulation of the WNDP catalytic activity"]
- **COMMD1/MURR1:** Interacts with ATP7B; mutations cause copper toxicosis in Bedlington terriers; involved in biliary copper excretion pathway [PMID:12968035, PMID:17919502]
- **DCTN4 (dynactin p62):** Copper-dependent interaction, may facilitate retrograde microtubule-mediated trafficking [PMID:16554302]
- **GRX1 (glutaredoxin):** Copper-dependent interaction, may facilitate copper binding by reducing disulphide bridges [PMID:16884690]
- **ZBTB16/PLZF:** Hepatocytic isoform interacts with C-terminus; connected to ERK signaling [PMID:16676348]

## Critical Issues with Current GO Annotations

1. **GO:0015677 copper ion import (IBA):** This is WRONG for ATP7B. ATP7B mediates copper EXPORT (into bile/vesicles/Golgi lumen), not import into the cell. This appears to be a phylogenetic inference error.

2. **GO:0005886 plasma membrane (IBA):** Questionable. ATP7B does NOT primarily traffic to the plasma membrane. It traffics to pericanalicular VESICLES. This is a key distinction from ATP7A [PMID:16472602].

3. **GO:1990961 xenobiotic detoxification by transmembrane export across the plasma membrane (IC):** The mechanism is vesicular sequestration, not direct plasma membrane export [PMID:16472602].

4. **GO:0005515 protein binding:** Multiple uninformative "protein binding" annotations should be replaced with specific interaction terms.

5. **GO:0016323 basolateral plasma membrane (IDA, PMID:15269005):** This paper is about ATP7A (Menkes), NOT ATP7B! This is a mis-annotation.

6. **GO:0005739 mitochondrion (IEA/HTP):** Based on a proteolytic fragment (WND/140 kDa) reported by one group [PMID:9600907]. Not widely reproduced. Dubious for the full-length protein.

7. **Redundant annotations:** Many terms appear with multiple evidence codes (e.g., GO:0140581 appears 6 times).

## Isoforms

- Isoform 1 (canonical): Golgi membrane localization
- Isoform 2: Lacks transmembrane domains, cytoplasmic localization, expressed in brain but not liver [PMID:9307043]
- Isoform 1 may be proteolytically cleaved to produce WND/140 kDa form (mitochondrial)

## Falcon deep research integration - 2026-05-12

Falcon deep research was added as `ATP7B-deep-research-falcon.md` and supports
the same core curation model: ATP7B is a P1B-type ATP-dependent Cu(I) transporter
whose central biology is copper export into the TGN and copper-induced
vesicular/pericanalicular trafficking for detoxification and biliary excretion
[file:human/ATP7B/ATP7B-deep-research-falcon.md "ATP7B encodes the Wilson disease
copper transporter, a **P1B-type (P-type) Cu(I)-transporting ATPase** whose
well-supported GO-relevant biology centers on: (i) **ATP-driven Cu(I) export from
the cytosol into the trans-Golgi network (TGN) lumen** for metallation of secretory
cuproproteins, and (ii) **copper-induced trafficking** to post-Golgi
vesicles/pericanalicular compartments to enable **cellular copper detoxification
and biliary copper excretion** in hepatocytes."].

The Falcon report also reinforces the key caveats already captured in the YAML:
ATP7B is not a copper importer [file:human/ATP7B/ATP7B-deep-research-falcon.md
"The supported directionality is **export from cytosol into TGN/vesicle lumen and
ultimately bile**, not import into cytosol."] and constitutive plasma membrane
annotation should be avoided in favor of condition-dependent TGN-to-vesicle or
apical/canalicular-associated trafficking [file:human/ATP7B/ATP7B-deep-research-falcon.md
"A cautious annotation should emphasize **copper-induced apical/canalicular-associated
trafficking** and/or “TGN → pericanalicular vesicles” rather than constitutive
“plasma membrane.”"].


---

# ATP7B prospective annotation consultation

This is a read-only, TMP consultation of the 61 existing source assertions, numbered from 1 in canonical YAML order. The prospective map proposes 48 ACCEPT, 10 KEEP_AS_NON_CORE and 3 UNDECIDED, one transport core and zero NEW annotations. All five existing alternative products are preserved; `products` is a separate, absent field. The canonical review, provider report, raw records and 23 normal caches have not been edited.

The fresh scope gate covers signed main `b5da4b785b3695367b47758e6538d20dac69e79e`, all 146 open PRs, 204 distinct head/base refs and 2,448 alias-directory objects. All six existing gene files and 23 normal references match main. The sole inherited PR3334 HTML difference was adjudicated from a new exact-head/base 53-path comparison and ATP7B tree; all five other gene files match. The initial strict refusal and its earlier helper are retained.

## Interpretation of the existing assertions

The core is ATP-driven Cu(I) movement from cytosol into Golgi/vesicular compartments. ATP binding, copper binding, hydrolysis and their valid broad parent annotations are parts of that same mechanism. Duplicate evidence codes do not make a core property non-core. Existing specific transport annotations already provide the desired detail, so replacing broader rows with another identical P-type term would not improve coverage.

Row 30 should be ACCEPT. The [official copper-ion import definition](https://amigo.geneontology.org/amigo/term/GO:0015677) includes entry into an organelle, which fits Golgi/vesicle uptake. The original cell-only interpretation was incorrect. The [copper-ion export definition](https://amigo.geneontology.org/amigo/term/GO:0060003) accommodates cellular export; the 16472602 vesicular-sequestration/exocytosis model supports direct ATP7B participation in that route. It does not prove that ATP7B always pumps directly across the plasma membrane.

Rows 20–24 report supported COMMD1, DCTN4, GRX1 and PLZF associations and are non-core. The user ActionEnum takes precedence over the skill's generic-binding removal guidance. No more specific ATP7B adaptor/enzyme function is manufactured from these interaction experiments.

The remaining uncertainties are row 34 (the exact plasma-membrane xenobiotic-export inference from 9837819), row 56 (the exact ATP7B basolateral location experiment in 15269005) and row 61 (the ATP7B MitoCoP target entry/product/evidence category). [GO:1990961](https://amigo.geneontology.org/amigo/term/GO:1990961) requires export to the cell exterior. Copper essentiality alone neither verifies nor refutes a xenobiotic role. No confident wrong-paralog or contamination claim is made.

For rows 40 and 45, the map explicitly retains the curator's copper-response and TGN assertions with independent ATP7B support, while disclosing that the original 15269005 target panels remain unverified. This is a deliberate curatorial-deference choice because the exact biological functions are independently established; it is not a claim that the ATP7A-focused paper was fully read. If root prefers source-specific uncertainty instead, those two choices should be adjudicated explicitly rather than restoring wrong-paralog REMOVE.

Rows 54–55 become non-core context-dependent surface localization. Independently read indexed original [38032054/PMC10729821](https://pmc.ncbi.nlm.nih.gov/articles/PMC10729821/) Results/Figure 1 text describes tagged ATP7B at a gp135-positive apical surface after copper treatment. The displayed Methods specify polarized MDCK cells and tagged constructs, but the donor species of the existing ATP7B plasmid is not resolved in that selected passage. No figure pixels, complete paper or direct surface copper-flux assay were inspected. The source is still uncached; the failed normal attempt is preserved and Source71 recovery belongs to AMER.

Row 60 becomes non-core processed-product localization. The curated UniProt record and AMER's original-paper consultation distinguish mitochondrial 140-kDa WND from the principal approximately 160-kDa form. Subsequently, during Source71 identity review, ALX independently read the complete official indexed abstract and displayed original Results/captions and Discussion of [9600907/PMC27575](https://pmc.ncbi.nlm.nih.gov/articles/PMC27575/). These describe HepG2 and human tissue mitochondrial experiments and acknowledge unresolved processing. No precise cleavage site, correspondence to any existing splice product, or mitochondrial transport function is inferred. This later reading supplements the already saved all61 map without changing its decisions.

## Actual reading boundaries

All 21 existing PMID abstracts and both complete cached Reactome summaries were read. The UniProt functional, interaction, localization and alternative-product sections were read. The original notes were read. The Falcon report's initial synthesis/table and selected mechanism sections were read as research leads; its entire bibliography was not independently verified. Its incorrect import and blanket mitochondrial exclusions are superseded here without editing that immutable provider output.

For 15681833, the complete cached Results include endogenous/tagged ATP7B, Rab7/NPC1 and U18666A localization comparisons. Methods and figure pixels were not inspected. Late-endosomal localization is supported within the cellular models, but imaging is not a direct lumenal copper-flux measurement.

For 16939419, the entire normal cache was read. Although its flag says full text is available, the actual extraction contains only abstract, introduction and discussion. It lacks Methods and Results. The paper's reported catalytic-mutant trafficking conclusions can be summarized with that explicit boundary.

For 17919502, the complete abstract, Methods and selected Results on COMMD1 association were read. ATP7B-Flag/COMMD1-GST precipitation uses cell lysates from human HEK293T/HepG2 cultures; residues 1–650 suffice in the tested construct. These are not purified binary binding measurements. Later degradation Results and the complete Discussion were not independently read.

For 22240481, the complete abstract, selected Methods on human ATP7B expression in Sf9 and microsomal-vesicle assays, and the first copper-transport Results were read. ATP-dependent copper accumulation was compared with mock, low temperature, vanadate and catalytically inactive D1027A controls. The membrane preparation is not a homogeneous purified-protein reconstitution. A combined display truncated a later catalytic-results passage, so no complete-Results or whole-paper claim is made.

The cached 16472602 abstract itself contains Methods/Results summaries of endogenous HepG2 localization and CHO wild-type/mutant vesicular sequestration. Its absence of surface localization under those conditions must not be universalized against later MDCK results. The complete article was not read in this consultation.

For 15269005, the complete cached abstract and root's bounded observation were available; the direct publisher request was denied. The exact ATP7B experiments were not recovered. For 19946888 and 34800366, target-table details were not verified. AMER's independently documented MitoCoP reading distinguishes the literature-derived fourth pool from experimental target detection.

The three proposed normal-cache quote candidates in the map are short, exact raw substrings and are each below 25 words. Final authorship must count all quotations cumulatively per source. No new source cache or availability claim was created. The local GO-CAM index has no ATP7B/P35670 hit; this is not a statement of global model absence.


## Prospective authorship and pending source closure

The preceding historical notes and immutable Falcon report are retained as provenance. Their old copper-import rejection, universal plasma-membrane exclusion, wrong-paralog REMOVE claims and blanket mitochondrial rejection are superseded by the evidence-specific consultation above. The prospective review retains all 61 source assertions and five alternative products, with 48 ACCEPT, 10 KEEP_AS_NON_CORE and 3 UNDECIDED, one copper-transport core and no NEW annotations. The three uncertainties are the plasma-membrane xenobiotic-export inference, the original basolateral target experiment and the MitoCoP target evidence/product. Generic interaction annotations remain non-core under the user action definitions.

Normal source recovery is pending for PMID:38032054 and PMID:9600907. They have been read externally with bounded scopes, but no normal-cache titles, availability flags or quotations are invented. Their top-level reference objects and final additional-reference links must be added only after verified Source71 import and canonical-byte equality. Existing UniProt provides the product-specific support for cytoplasm and WND/140-kDa mitochondrial localization in this interim draft. This proposal has passed only the typed model and exact preservation/quotation checks; canonical application, focused validation, rendering and history have not occurred.


### Final normal-reference closure

Source71 supplied the exact normal PMID38032054 and PMID9600907 caches. Their reference objects and explicit annotation links now accompany the previously reviewed plasma-membrane and processed-product mitochondrial interpretations. PMID38032054 is available as normal XML text; PMID9600907 remains abstract-only in the normal cache, while the earlier independent primary consultation of selected original Methods/Results/captions remains separately attributed. No new quote or stronger assay claim was introduced.

The concise core omits the generic cytoplasmic-vesicle location because the included late-endosomal location already provides a more specific vesicular compartment. The original vesicle annotation and the vesicular transport description are preserved. All 61 annotation decisions and five products remain unchanged by this final reference closure.


## 2026-09-29 — revised biological interpretation after review

This entry supersedes the earlier cell-only copper-import interpretation, blanket plasma-membrane and mitochondrial exclusions, and wrong-paralog claim about PMID:15269005. The previous entries remain above as an append-only journal. The current evidence and reading limits are summarized below.

### Identity and transport mechanism

Human ATP7B (UniProt P35670; Wilson disease protein, EC 7.2.2.8) is a P1B-type Cu(I)-transporting ATPase. Its six amino-terminal heavy metal-associated domains receive copper from ATOX1 and participate in regulation of the transport cycle. The transmembrane CPC motif is required for transport in the tested functional system. Loss of ATP7B causes Wilson disease (MIM:277900). The domain and disease identifiers are present in the immutable UniProt record; the metal-binding, nucleotide-binding and complementation experiments provide independent mechanistic support (PMID:9837819, PMID:12029094, PMID:14709553, PMID:15205462, PMID:16567646).

The principal activity is ATP-dependent copper translocation from the cytosol into Golgi and vesicular compartments. ATP binding, copper binding and ATP hydrolysis are mechanistic facets of this activity. ATOX1 transfer to isolated ATP7B amino-terminal domains and N-domain ATP binding are construct-level observations; they are not presented as purified full-length transport assays. Human ATP7B expressed in Sf9 cells supports ATP-dependent copper uptake into membrane vesicles, with mock, low-temperature, vanadate and catalytic-mutant controls. Those microsomes are not a homogeneous purified-protein reconstitution (PMID:22240481).

### Copper import, export and localization

Copper entry into the Golgi or a vesicle is organelle import. The official definition of [copper ion import](https://amigo.geneontology.org/amigo/term/GO:0015677) includes entry into an organelle and therefore fits this ATP7B-mediated step. Subsequent exocytosis moves copper out of the cell and contributes to [copper ion export](https://amigo.geneontology.org/amigo/term/GO:0060003). These describe different boundaries of the same route. Neither term requires the unsupported claim that ATP7B always pumps directly across the plasma membrane (PMID:16472602; Reactome:R-HSA-936895).

TGN and late-endosomal locations are retained with cell-model and copper-condition limits. PMID:15681833 reports endogenous and tagged ATP7B localization with late-endosomal markers. Imaging supports the compartment, but does not by itself measure lumenal copper flux or establish exclusive residence. Its location findings do not erase independently supported TGN localization. The ATP7B step in Reactome R-HSA-936895 specifically connects cytosolic Cu(I) to the Golgi lumen; R-HSA-936837 supplies broader P-type transport context.

The HepG2 and CHO findings summarized in PMID:16472602 support vesicular sequestration followed by exocytosis. Failure to see surface localization in those conditions is not a universal exclusion. Selected original Results and Figure 1 text from PMID:38032054 describe copper-dependent apical localization of tagged ATP7B in polarized MDCK cells. The selected Methods identify the host and tagged constructs, but do not resolve the donor species of the existing ATP7B plasmid. These observations support context-dependent surface localization, not a universal endogenous location or a direct surface copper-flux measurement.

### Specificity of the existing annotations

The broad electronic and functional transport assertions can be refined to the experimentally supported substrate and mechanism without declaring their ancestors false. Copper-transporter and ATPase-coupled cation-transporter rows propose P-type monovalent copper transporter activity; nucleotide and metal binding propose ATP and copper binding; the broad transport processes propose copper ion transmembrane transport. Repeated evidence for a specific term remains legitimate: these are refinements of existing assertions, not additional functions.

The nucleotide-binding refinement does not mean that ATP7B binds only ATP. The recombinant N-domain in PMID:15205462 also discriminates little among ATP, ADP and AMP. ATP binding is selected because it is directly supported and relevant to the transport cycle.

The electronic broad membrane row can use independent evidence to specify the TGN membrane. The HDA membrane annotation from PMID:19946888 is treated separately. Its YTS NK-cell target table has not been inspected, so the curator's membrane observation is retained as non-core context without substituting TGN localization as though that study measured it. The specific TGN location is independently represented elsewhere.

Correct associations with COMMD1, DCTN4, GRX1 and PLZF remain non-core interaction observations. Their generic labels do not make the underlying experiments false, and no unsupported adaptor or catalytic function is manufactured from them. The COMMD1 precipitation experiments use cell lysates and an ATP7B amino-terminal construct; they are not purified binary stoichiometry measurements (PMID:17919502).

Three assertions remain unresolved: the exact plasma-membrane xenobiotic-export inference linked to PMID:9837819; the ATP7B basolateral target experiment in PMID:15269005; and the ATP7B MitoCoP target evidence/product in PMID:34800366. The unread target panels do not establish wrong-gene attribution. Independently supported copper-response and TGN assertions linked to PMID:15269005 are retained with curatorial deference and an explicit source-reading limitation.

### Alternative products

All five supplied alternative-product objects are preserved. The curated UniProt record distinguishes cytoplasmic isoform 2 from the principal membrane transporter and describes mitochondrial WND/140-kDa material. Selected original mitochondrial experiments in PMID:9600907 involve human tissue and HepG2 material and leave processing unresolved. No cleavage site, correspondence to a particular splice product, or autonomous mitochondrial copper-transport function is inferred. These observations remain non-core product context.

### Source-reading boundaries

The recorded source assessment includes all available cached abstracts, both complete Reactome summaries, and UniProt functional, interaction, localization and alternative-product sections. Later normal records for PMID:38032054 and PMID:9600907 are now available. The former contains XML text; the latter remains abstract-only in the normal cache. Independent selected original reading for the mitochondrial study is attributed separately and does not turn its normal cache into a full article.

- **PMID:9837819 and PMID:26004889:** complete cached abstracts describe human ATP7B complementation in yeast ccc2 models. Growth or iron-uptake rescue is a functional copper-delivery readout, not purified copper flux. The original evidence-code tuples are preserved.
- **PMID:12029094, PMID:14709553, PMID:15205462 and PMID:16567646:** complete cached abstracts support copper transfer/binding and recombinant domain nucleotide-binding or structural observations. No whole-paper or full-length purified-transport reading is claimed from these abstracts.
- **PMID:15681833:** the earlier source consultation read complete cached Results, including endogenous/tagged ATP7B, Rab7/NPC1 and U18666A comparisons. Methods and figure pixels were not inspected. The follow-up rechecked the abstract used for the literal annotation anchor.
- **PMID:16939419:** the normal extraction contains abstract, introduction and discussion, despite its full-text-available flag. It has no Methods or Results section. The reported catalytic-mutant trafficking conclusions retain that boundary; the availability flag itself is unchanged.
- **PMID:17919502:** the recorded reading covers the complete abstract, Methods and selected COMMD1-association Results in HEK293T/HepG2 cells, including ATP7B residues 1–650. Later degradation Results and complete Discussion were not independently read. The follow-up rechecked the complete abstract and exact interaction anchor.
- **PMID:22240481:** the recorded reading covers the complete abstract, selected expression/vesicle-assay Methods and the first transport Results, plus bounded variant results. A prior combined display truncated a later catalytic passage; complete Results or whole-paper reading is not claimed. The follow-up rechecked the first transport result and its controls.
- **PMID:16472602:** the cached abstract includes explicit Methods/Results summaries for endogenous HepG2 localization and CHO wild-type/mutant copper sequestration. The complete article was not read. Annotation and core excerpts are taken from this abstract.
- **PMID:15269005, PMID:19946888 and PMID:34800366:** exact ATP7B target panels/tables remain unverified. Titles or abstracts foregrounding another protein or a broad survey are not evidence that the curator misidentified ATP7B.
- **PMID:38032054 and PMID:9600907:** selected original text supports the context and product distinctions above. No figure-pixel or whole-paper endorsement is implied. Normal cache identity, availability and provenance are preserved.

Annotation-level excerpts and the two core excerpts are exact normal-cache substrings. Repeated excerpts count separately toward a maximum of 25 quoted words per source; reference findings retain their substantive paraphrased summaries without duplicating those quotations. These notes use paraphrase rather than an additional layer of quoted text.

### Superseded historical interpretations

Earlier notes and the immutable Falcon report supplied useful leads but also made stronger claims than the inspected evidence supports. The cell-only interpretation of copper import, universal exclusion of plasma-membrane ATP7B, wrong-paralog assertion about PMID:15269005, blanket rejection of mitochondrial material, and guessed correspondence between WND/140-kDa processing and splice products are superseded by the source-specific interpretation above. The original published notes remain preserved with the prior curation history; the provider output and all normal sources are unchanged.

The local GO-CAM index had no ATP7B/P35670 match in the recorded search. This is a local-index observation, not a claim of universal model absence. One copper-transport core is retained, with no new annotations or disease-process assertions.


## ClinGen task instruction and generic-binding retention, 2026-10-02

The retained GO:0005515 decisions implement the user's explicit instruction for this ClinGen task: keep a supported, biologically correct interaction as KEEP_AS_NON_CORE when no defensible, more specific replacement has been established, rather than remove it solely for lacking functional information. This deliberately departs from the annotation-reviewer skill's informational-exclusion recommendation. That recommendation can remove an uninformative annotation without declaring the interaction false; the latest review is correct about that distinction. Earlier references here to the supplied ActionEnum are incomplete as an explanation of authority: the basis is the explicit instruction for this task, not the enum alone, a repository-wide policy change, an exemption granted by the agent, or an observed maintainer sign-off. No external approval comment is claimed.

The five retained rows remain the two MURR1/COMMD1 associations (PMID:12968035 and PMID:17919502), DCTN4 (PMID:16554302), GLRX1 (PMID:16884690), and the hepatocytic PLZF isoform (PMID:16676348). Their published reasons retain the assay limits: COMMD1 recovery from cell lysates is not purified binary stoichiometry, and the PLZF isoform lacks the BTB domain. Copper-dependent association does not give ATP7B glutaredoxin catalysis, and the trafficking context does not by itself establish an adaptor activity. This documentation update preserves those decisions; it does not make a new claim that every possible narrower binding term has been excluded.

All 61 original source and review objects, five alternative products, eight existing refinements and the single copper-transport core remain unchanged.

This addendum clarifies the authority and exclusion criterion for the existing decisions. It adds no primary-source reading, biological assertion or new annotation adjudication. Earlier journal entries and validation results remain historical; this clarification does not claim reviewer approval or PR completion.


## 2026-10-02 — separate ATOX1 and COMMD1 source assertions

The two immutable GOA records citing PMID:12968035 share protein binding, IPI evidence and the enables qualifier, but identify different partners: UniProtKB:O00244 (ATOX1) and UniProtKB:Q8N668 (COMMD1). The preceding published YAML represented that pair with one partner-unspecified object whose reason assessed COMMD1 only. This follow-up restores both existing source assertions as separate partner-specific objects. The added object is source recovery, not a NEW annotation. Raw identifiers, evidence, reference and source bytes are unchanged.

The complete cached abstract of PMID:12968035 explicitly reports human MURR1/COMMD1 interaction with the Wilson disease protein and its amino-terminal region. The existing COMMD1 judgment is retained exactly, with its source partner now explicit. That abstract does not expose the ATOX1 experiment, and no original full-paper or interaction-table inspection is claimed. The independently cached abstract of PMID:12029094 describes ATP7B–ATOX1 protein interactions and reports recombinant ATOX1 transfer of copper to purified ATP7B amino-terminal domains, plus regulation of full-length ATP7B catalytic activity. This independently supports the ATP7B–ATOX1 association. It does not certify what was assayed in the original PMID:12968035 experiment. ATOX1 is therefore retained as non-core with curatorial deference for that original IPI source and an explicit source-reading limitation. No ATP7B chaperone, adaptor or narrower binding activity is inferred from the copper donor's function.

The preceding five-retained-row and 61-object statements describe the earlier published state. The proposed current review has 62 existing annotation objects: 39 ACCEPT, 12 KEEP_AS_NON_CORE, eight MODIFY and three UNDECIDED, including six retained generic protein-binding objects. The other 60 review objects, all five alternative products, 34 reference objects, the single copper-transport core, description and DRAFT status remain unchanged. All existing quotations are unchanged; this follow-up adds no quotation or reference object. The standing task instruction for supported generic binding remains the authority already documented above; no new maintainer approval or global policy change is claimed.

This is a TMP proposal pending independent scientific review and canonical application. Standard validation, rendering and append-only history will be recorded at the corresponding application stage.


### 2026-10-02 — partner-restoration application closure

The independently reviewed source-restoration proposal above is now applied locally. Normal canonical validation passed with nine warnings: six supported generic-binding retentions under the standing task instruction, two preexisting distinctions between source contexts, and the deliberate absence of citations to the historical provider report. Targeted gene rendering and validation of the newly scaffolded session history passed. All 62 source objects are represented; the source TSV, UniProt record, publication caches, prior histories, five products, 34 reference objects, literal quotations and copper-transport core remain preserved. The earlier TMP-stage paragraph is historical. These checks do not claim GitHub reviewer approval, merge or campaign completion.
