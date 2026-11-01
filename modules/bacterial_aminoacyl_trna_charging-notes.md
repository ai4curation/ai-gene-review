# Bacterial aminoacyl-tRNA charging: comparative evidence audit

## Boundary and interpretation

The module retains the reusable production program for twenty canonical aminoacyl-tRNA outputs. Its forty activity leaves include direct synthetases, native-species GatCAB alternatives and the rare bacterial SepRS/SepCysS chemistry. Twenty output roles are required; a separate THEVB ND-GluRS comparator is optional. The 42 proteins include all 26 original representatives. KT2440 is the only fully sampled reference panel; missing outputs in the other sampled panels do not establish biological absence from those organisms.

The Boolean compiler accepts an external context predicate. The committed route check explicitly requires one organism context and every named subunit of a complex. The generic compiler alone neither enforces taxonomy nor expands complex active units. Consequently, an arbitrary union of proteins from different organisms is not a defensible native pathway witness. Tests distinguish native-context compatibility from proof of measured cellular flux.

## Mechanistic distinctions

Direct synthetases activate amino acids with ATP and esterify tRNA. GatCAB and SepCysS modify an amino acid already attached to tRNA; they do not create the initial ester. The 2026-10-29 term-by-term QuickGO and pinned GO source evidence verifies all 22 disputed terms as obsolete; the exact migration metadata and all 56 affected rows are documented in [ontology-review.md](bacterial_aminoacyl_trna_charging-analysis/ontology-review.md). Author-supplied direct charging processes use GO:0006418; charged-tRNA amino-acid modification uses GO:0019988. Original machine annotation payloads retain their fetched identifiers and labels.

Class I Borrelia LysRS and class II KT2440 LysRS are alternatives. Thermus homodimeric GlyRS differs from KT2440 GlyQ/GlyS alpha2-beta2 architecture. GlyS is not considered inert: the E. coli structure in PMID:34390350 places beta-subunit residues in substrate coordination. The KT2440 PheS/PheT complex separates alpha catalytic and beta recognition/editing contributions. These are assembled enzyme functions, not independent whole-complex activities assigned to every subunit. Editing remains in gene reviews; this charging boundary does not require a universal separate editing enzyme.

## Native amide routes

Full PMID:14729703 establishes discriminating PAO1 GluRS, nondiscriminating AspRS, direct GlnRS capacity and GatCAB-dependent Asn-tRNA formation. PAO1 GatCAB can amidate supplied heterologous Glu-tRNA(Gln), but its native GluRS does not supply that substrate. PMID:25548166 reconstructs the PAO1 transamidosome and supports dynamic substrate handoff, not a universally permanent oligomer.

Full PMID:9342321 directly establishes Bacillus glutamyl-tRNA transamidation and the distinct GatA glutaminase, GatB synthetase and GatC assembly roles. The original operon disruption and recombinant subunit assays are different evidence contexts. PMID:26804570 explicitly demonstrates Bacillus ND-AspRS despite AsnRS, correcting the older assumption that their coexistence is impossible. The Bacillus Asn branch combines separately supported enzyme capabilities; the accessed sources do not establish native matched-pair flux. Its continuity is marked UNVERIFIED. KT2440 indirect Asn chemistry is also a qualified homolog inference, supported by its curated enzyme assignments and the direct PAO1 mechanism.

The earlier THEVB GluRS-to-KT2440 GatCAB chain was a mixed-species construction. The repaired indirect Gln route is matched Bacillus. THEVB Q8DLI5 remains visible both for direct Glu charging and independently assayed Glu-tRNA(Gln) formation, without importing an unreviewed native partner. Current taxonomy is Thermosynechococcus vestitus BP-1, historically T. elongatus, not Thermus.

GatC fidelity regulation is compatible with its structural role. Full PMID:34225495 and PMID:33072044 show mycobacterial perturbations affecting translational errors. These support conserved scaffold inference in the comparative gene reviews, not native PAO1/Bacillus error-rate or antibiotic assays. GO:0006450 does not require direct ribosome modulation.

## Bacterial cysteine chemistry and archived identities

PMID:28487430 experimentally characterizes the DG_74_2 metagenomic-bin SepRS and SepCysS sequences. UniSave A0A0S7X285 v20 and A0A0S7X265 v18 match the published KPJ56532/KPJ56533 constructs through UniParc sequence identity. Current entries are deleted for reference-proteome collection reasons; that is not loss of the biological function. The initial normal fetch produced empty UniProt files, so literal authoritative archive bytes were acquired and independently baselined before curation. No raw source was manually rewritten.

SepRS aminoacylated tRNA(Cys) variants at low yield. The high SepCysS percentage describes conversion of the available phosphoseryl intermediate, not charging of all input tRNA. Critically, the coupled SepCysS assay used Chloroflexi SepRS; the native matched Parcubacteria pair was not reconstituted. Sulfide/PLP-containing anaerobic assays and an engineered E. coli tRNA(Sec) reporter do not establish native sulfur donation or a cultured isolate phenotype. The module records this as an inferred biochemical pairing, not a complete experimentally reconstructed native system. The 2022 comparative study PMID:35047015 confirms that bacterial indirect cysteine chemistry is real and cannot be excluded by an archaea-only boundary.

## Grounding and validation

Every concrete selector uses an exact accession and taxon. PANTHER labels are copied from the official ontology and checked against the corresponding unedited UniProt cross-reference. These classifications do not assert all-family conservation of substrate discrimination, editing, metal binding or oligomeric architecture. The archived SepRS has no asserted family identifier where none was established. `bacterial_aminoacyl_trna_charging-analysis/check_module.py` uses a bounded, independently read membership map; no release-wide index was built.

The module's actual Falcon and perplexity-lite attempts failed authentication/quota; no provider report was invented. The inherited OpenScientist report is retrieval background and is not quoted as primary evidence. All comparative gene publication jobs succeeded, while actual provider and fitness attempts failed without producing usable reports or phenotypes. Full-text access versus abstract-only evidence is stated in the references and individual notes.

`check_routes.py` tests 44 cases, including complete KT2440, loss of individual required subunits, partial comparators, class/architecture alternatives, mixed-species rejection and both steps of the bacterial Cys route. Family-function coverage advisories are retained where no applicable family-wide adjudication exists; no family function is invented to silence them. All original gene payloads and raw hashes are independently checked in the scoped preservation report.

## 2026-10-27 independent final scientific QA

Checked the integrated 42-member program and its comparative source boundaries after the member reviews were finalized. The modeled chemistry and retained uncertainty are coherent. Added exact-target curated UniProt function evidence directly to the KT2440 indirect-Asn and PheRS activities and the Bacillus Asn-forming GatCAB activity, beside the comparative primary papers; the PANTHER classifications alone do not establish those substrate-specific assignments. No participant, family, function, route, chaining status or gene annotation was changed. The 54 module reference entries comprise 12 assessed literature references and 42 curated target records. Current editing-term checks confirm the specific ThrS Ser-tRNA(Thr) hydrolase term, while the inspected ontology provides no exact IleS/ValS/PheT editing term. Existing fidelity terms are retained, so no X-involved-in-Y decomposition is introduced.


## 2026-10-29 — PR #5616 follow-up

The original source snapshot omitted the obsolete terms named in the review. The expanded normal QuickGO response and unedited term stanzas from a pinned GO commit now make the claim reproducible. All 56 affected rows across 40 reviews were checked: 45 direct-charging rows follow explicit GO:0006418 replacements; 11 GatCAB rows retain the independently justified GO:0019988 modification process. No machine annotation payload or action is changed. The three GatA localization reviews now quote native Bacillus S100 evidence, with Pseudomonas localization explicitly inferred by conserved function. GatA broad-activity refinement and the PSEPK glutaminase summary are corrected without removing supported complex contributions.


## Dependent-review migration follow-up

The refreshed BP enum exposed four pre-existing authored core terms outside the module panel: human AARS1, POPTR ALARS, POPTR GATC and METTP gatC. Their dependent processes and adjacent obsolete replacement suggestions are migrated with separate gene histories. METTP also required correcting a wrong-organism manual-report attribution and unsupported subunit-based rejections; eight machine rows are preserved and two inherited authored proposals are archived. These dependency repairs do not expand the 42-member module. Both BP and generic GO enum caches now exclude the 22 verified obsolete terms.
