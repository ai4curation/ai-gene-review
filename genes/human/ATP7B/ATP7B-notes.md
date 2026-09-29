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
