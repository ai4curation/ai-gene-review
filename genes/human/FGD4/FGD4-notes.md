# FGD4 evidence notes

## Biological interpretation

Frabin is a CDC42 exchange-factor family member with an N-terminal actin-associated region, a DH–PH module, a FYVE zinc finger and a second PH domain. Its conserved exchange activity is supported by actual family placement, target domain matches and curated CDC42 catalyst membership. The retained cellular phenotypes concern actin-rich protrusions and cell shape; they do not make frabin a filament-polymerizing enzyme. Recessive human FGD4 variants cause CMT4H, but disease necessity alone does not establish every proposed myelination mechanism. [PMID:17564959; PMID:17564972]

All 25 imported annotation contexts have database provenance. The eleven ISS contexts cite FGD1 proteins: P98174 is human FGD1 and P52734 is mouse Fgd1. These are paralog donors. Their shared exchange mechanism is distinguishable from their different N-terminal targeting regions. Positive FGD4 cellular evidence corroborates conserved signaling and protrusion formation while leaving ruffle, Golgi and lamellipodial residence unresolved. [PMID:8969170; PMID:12913069]

## Original studies and experimental boundaries

The Delague study explicitly uses rat full-length Frabin-GFP and engineered rat 1–297 and 1–249 fragments in rat motoneurons and RT4 cells. Full-length frabin colocalizes with F-actin in neurite tips, growth cones and microspikes and increases microspike formation. Truncations retain colocalization but produce fewer protrusions. The human patient fibroblast comparison found no significant cytoskeletal differences in that context. Those observations neither demonstrate a universal loss of cytoskeletal function nor measure activities of the recorded human splice products. [PMID:17564959, Expression Constructs; Results; Figures 5–7 and Discussion]

The Stendel study shows endogenous frabin expression in rodent nerve and rat Schwann cells, and altered shape with filopodia and lamellipodia after tagged full-length frabin expression. The inspected text does not specify the transfected protein's species. Inducing a lamellipodium does not by itself establish residence within that compartment. The paper presents phosphoinositide-dependent regulation as a hypothesis requiring further measurement. [PMID:17564972, expression/overexpression Results and Figure 3]

The Chen study supplies human epithelial-cell evidence for endogenous frabin recruitment and a contribution upstream of CDC42 signaling. Tagged constructs are separately identified; their species is not explicit in the inspected Methods. Cellular CDC42-GTP measurements are distinguished from a purified frabin exchange assay. None of these three inspected studies supplies a direct actin-binding measurement that would justify adding that molecular function here. [PMID:15133042, Methods and localization/signaling Results]

The normal publication caches are preserved unchanged. Separate genuine original texts were available for the three studies above; their review flags reflect that access. Figure captions and stated Results were read, but original figure pixels and supplements were not independently inspected. No provider report was produced by the genuine automated research attempt.

## Natural products

UniProt records Q96M96-1, Q96M96-2 and Q96M96-3. Exact curated sequence edits reconstruct lengths of 766, 280 and 188 residues. The 280-residue product contains only parts of the canonical DH and first PH domains; the 188-residue product lacks a complete DH domain. Sequence reconstruction establishes their encoded sequence, not translation, stability or exchange activity. No functional-product assertions are assigned to the shorter products.

The rat experimental truncations and human disease-associated transcript predictions in the Delague study are separate entities. Additional predicted transcripts are not mapped to official product identifiers without an exact sequence join. The canonical UniProt CHAIN feature describes the full protein and is not evidence for cleavage into natural processed products. See [product evidence](FGD4-product-evidence.yaml).

## Provenance-only bibliography

The cDNA studies provide sequence provenance rather than functional assays. The Ota abstract was available; the exact FGD4 clone row was not checked. The Bechtel full-ORF article is cached, but a literal target-name/accession search did not recover an exact FGD4 row in its body. The Bian abstract describes a broad human liver phosphoproteome; the target peptide/site assignment was not checked. These limits are recorded in the complete reference assessments. [PMID:14702039; PMID:17974005; PMID:24275569]

No new annotation or publication quotation is proposed. Evidence locators and explicit uncertainty follow the [ClinGen project instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions).

The current ontology explicitly includes an exchange-defined process, GO:0090630 activation of GTPase activity, as a strict descendant of GO:0043087. It describes activation by replacing GDP with GTP, so the existing row 19 is refined to that term without asserting GAP activity or faster GTP hydrolysis. The core uses GO:0032489 regulation of Cdc42 protein signal transduction, a strict descendant of the broader GO:0051056 already retained in the imported rows. Actual target CDC42 catalyst membership supports this specificity. No new annotation is added, and no historical term-merge claim is inferred from IDs absent from the API response. See [ontology evidence](FGD4-ontology-evidence.yaml).

## 2026-10-27: PR review follow-up

Make the existing human UniProt FUNCTION and PMID:15133042 cellular evidence explicit in the exchange-activity reviews and core, preserving the distinction from purified biochemical assays. Refine the existing Reactome process row to GO:0032489 and retain the positive is_active_in cytoplasm IBA separately from located_in cytosol coverage. The 25 imported source objects, 17 prior references, three splice records and source caches remain unchanged; the sole additional reference is the existing UniProt file. No new annotation or quotation is added.

Computed status remains DRAFT with two advisory action differences. The cytoplasm decisions distinguish is_active_in from located_in. The process decisions distinguish the specific Reactome CDC42 catalytic route, refined to GO:0032489, from the broader ARBA assertion. These source/relation distinctions are retained rather than forcing identical decisions solely to remove warnings.
