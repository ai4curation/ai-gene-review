# ndhB1 notes

- Fetched with `just fetch-gene POPTR ndhB1`.
- Curated in parallel with ndhB2. Key decisions: modify respiratory-chain/ubiquinone annotations to chloroplast NDH/photosynthetic-chain equivalents, keep thylakoid localization, and treat ATP synthesis coupled electron transport as non-core relative to the direct NDH redox/proton-translocation role.

- Addressed PR #469 review on 2026-05-10: respiratory/light-reaction process review now points to NEW GO:0009778 cyclic photosynthetic phosphorylation. QuickGO defines GO:0009773 as photosynthetic electron transport in photosystem I, so GO:0009778 was used for the cyclic photophosphorylation process.

- Addressed PR #469 re-review on 2026-05-10: NEW annotation original_reference_id now points to the reviewed UniProt entry as the mechanistic source rather than a generic GO_REF.


## 2026-09-20 full IBA re-review

Reviewed every original source assertion and preserved all term/evidence/reference/qualifier fields. Ferredoxin-dependent plastoquinone reduction is supported by Arabidopsis primary PMID:21505067 and higher-plant proton-pumping PMID:28559282; spinach structure PMID:39856350 lacks the NADH-oxidizing module. Thus GO:0016655 remains the wrong donor class: its generic quinone acceptor does not repair the older NADH assignment. Use contributes_to GO:0016730, verified by live QuickGO (MF, current; its two children concern NAD(P) and dinitrogen acceptors and do not fit). The original source qualifiers remain untouched. GO:0010598 explicitly includes possible ferredoxin donation in its definition despite its historical label.

The current exact target lineage is reconstructed in plastid-energy-source-checks.json. Chloroplast localization does not exclude respiration under the actual GO definitions. Full tobacco PMID:27066014 compares ndhJK/ndhCJK disruptions, heat stress and PTOX inhibition; its fluorescence and P700 results support chlororespiratory involvement, without themselves directly measuring all proposed oxygen-coupled ATP generation. The older categorical respiratory exclusions are withdrawn pending one shared ndhD adjudication. The ATP-synthesis-coupled electron transport term is core because NDH actually performs electron transfer and energy-conserving proton translocation. Primary PMID:28559282 is cached abstract-only; no full-text-only experimental claim is attributed to that cache.

NdhK directly lines the plastoquinone cavity and binds a 4Fe–4S center in the spinach structure; this supports homologous NdhK binding beyond whole-complex substrate reasoning. NdhD is in the antiporter-like arm, so generic quinone binding cannot simply replace its ubiquinone assertion without subunit-specific evidence. Broad light-reaction/plastid/cofactor rows keep legitimate specific replacement recommendations where present. No NEW process assertions, substrate-role inferences or target-specific catalytic-residue claims are added.

The immutable UniProt/GOA files were not edited. Global OpenScientist query-cache exact accession/family and chloroplast-function search returned no matching report before the two shared requests were registered. Audit: projects/IBA_REVIEW/rereview-2026-09-20/plastid-energy-complexes.yaml.
