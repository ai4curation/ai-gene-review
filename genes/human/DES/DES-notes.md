# DES curation notes

## 2026-10-17 — Evidence review

The ordinary gene fetch seeded 108 annotation rows from 111 GOA records. All source fields are preserved. DES is HGNC:2770, UniProt P17661, 470 residues, with no named alternative products in the official record. The configured deep-research provider attempt failed authentication/quota checks and produced no report; the review is based on the genuine source records and original literature described in the [evidence guide](DES-evidence-guide.md).

The initial assessment contains 23 ACCEPT, 46 KEEP_AS_NON_CORE, 34 MODIFY and 5 TOO_GENERAL decisions, one structural core and no NEW annotation. Generic binding retention follows the user's explicit [ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions). The partner/assay assessments establish support individually; this is not an automatic conversion of all binding rows to non-core.

The core unites desmin filament assembly with its structural function around Z discs and intercalated discs. Human purified desmin in PMID:28470624 is distinguished from the hamster constructs in PMID:9736733. PMID:9697706 provides human genetic context rather than a force assay. Limited access to PMID:24200904, PMID:26724190 and PMID:9415431 does not justify overriding established experimental locations; independent human ultrastructural and assembly evidence is recorded explicitly.

Interaction refinements describe the bound protein class. Binding a cytoskeletal protein does not by itself demonstrate recognition of an assembled filament, and binding a kinase, ligase or transcription factor does not assign that activity to DES. BioPlex associations remain qualified as co-purification. Partner fragments and named isoforms are retained in the rationale, including the short ZMYM5 product, extended NEK6 product and divergent UBE2I sequence.

The rodent nuclear observations were read in full originals where available. Nuclear entry is developmentally restricted in PMID:26787680; nuclear-envelope and cell-end anchoring in PMID:35959657 is examined under PKP2 perturbation. PMID:31822208 directly tests rat desmin depletion and supports mechanical organization of the nuclear envelope. These are contextual conserved structural roles, not additional nuclear catalytic functions.

Five additional publications were fetched through the repository's normal publication fetcher: PMID:26787680, PMID:35959657, PMID:11732910, PMID:11694502 and PMID:31822208. All original seed caches, UniProt, GOA, family records and prior history remain unchanged. No provider-labelled content was authored. Canonical publication and the new append-only history record are handled separately after independent review.

### Independent-read refinements

After independent review, the final scientific draft contains 23 ACCEPT, 40 KEEP_AS_NON_CORE and 45 MODIFY decisions. The five broad terms now carry explicit supported replacements, consistent with the annotation guidance, rather than stopping at TOO_GENERAL. Typed current GO paths were checked for intermediate filament cytoskeleton → cytoskeleton, intercalated disc → cell-cell junction, intermediate filament organization → cytoskeleton organization, and intermediate filament → supramolecular fiber.

The plectin pair is refined to cytoskeletal protein binding using its independently established structural class while keeping the original-access limitation. The BioPlex cytoskeletal associations receive that same class refinement: the term does not add a claim of direct molecular contact, and all AP-MS limitations remain. DDX6 binding is narrowed to ATPase binding using the current GO definition and official ATP-hydrolysis assignment; that partner annotation is not represented as a newly read purified-enzyme assay. Source-specific propagation blocks record actual ancestral nodes, the mouse donor and the current rule reconstruction limits.


## Source-specific follow-up, 2026-10-17

Desmin self-association and binding to cytoskeletal partners are components of one filament assembly and linkage activity. Human muscle electron microscopy places desmin around Z-lines (PMID:11353857), while recombinant assembly and nebulin-binding assays support the structural mechanism (PMID:28470624; PMID:23615443). The core therefore describes these mechanisms together, rather than assigning separate regulatory activities from binding alone. Human cardiac myofilament measurements support a cardiac-myofibril location without attributing troponin-dependent force changes to DES (PMID:25771144).

Normal skeletal-muscle MTM1–desmin colocalization at the sarcolemma is reported independently of disease-variant aggregation (PMID:21135508). The R350P human biopsy observations remain explicitly distinct from normal localization and from the mouse R349P model (PMID:25394388). The sarcolemma action difference records those biological contexts; no original isoform or source field is changed.

Binding to an established partner class does not mean that DES performs or regulates that partner's activity. The validated binary pairs and their tested constructs remain positive evidence with native-context limits (PMID:25416956; PMID:32296183). The DUX4 pull-down supports a DNA-binding transcription-factor partner, not a DES transcriptional mechanism (PMID:26816005). The structured source-evidence file supplies exact pair links, public original locators and bounded quotations. Original-only passages are distinguished from abstract-only caches.

Mitochondrial positioning remains an explicit mechanistic question: perturbing the MTM1–desmin connection changes the filament system and mitochondrial dynamics, but physical tethering should be separated from secondary architectural or metabolic effects (PMID:21135508). No new process annotation is proposed.


## 2026-10-17 sarcolemma consistency follow-up

All three GO:0042383 annotations now ACCEPT the established gene-level peripheral sarcolemmal location, consistent with the structural core. The PMID:25394388 row retains its human R350P biopsy, mutation-specific antibody and subsarcolemmal-aggregate scope; it is not recast as normal membrane-insertion evidence. Independently recovered PMID:21135508 supports normal skeletal-muscle localization, with its abstract-only cache and mouse/human figure distinctions preserved in the source evidence.

The evidence guide now links the structured source-assessment table instead of duplicating it, removes the prior round’s changelog and avoids undated live-database record counts. The structured sarcolemma interpretation is aligned with the gene-level action. All 108 source dictionaries, partner-class refinements, core terms, product scope and existing quotations are unchanged. Counts are 24 ACCEPT, 39 KEEP_AS_NON_CORE and 45 MODIFY; no NEW annotation is added.
