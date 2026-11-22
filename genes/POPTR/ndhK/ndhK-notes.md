# ndhK notes

- Reviewed existing GOA annotations against `ndhK-uniprot.txt` and GOA provenance.
- Core interpretation: Chloroplast NDH complex subunit K, a 4Fe-4S protein in the plastid NAD(P)H-plastoquinone oxidoreductase system that couples photosynthetic electron transport to proton translocation.
- Main evidence source: [file:POPTR/ndhK/ndhK-uniprot.txt].


## 2026-09-20 full IBA re-review

Reviewed every original source assertion and preserved all term/evidence/reference/qualifier fields. Ferredoxin-dependent plastoquinone reduction is supported by Arabidopsis primary PMID:21505067 and higher-plant proton-pumping PMID:28559282; spinach structure PMID:39856350 lacks the NADH-oxidizing module. Thus GO:0016655 remains the wrong donor class: its generic quinone acceptor does not repair the older NADH assignment. Use contributes_to GO:0016730, verified by live QuickGO (MF, current; its two children concern NAD(P) and dinitrogen acceptors and do not fit). The original source qualifiers remain untouched. GO:0010598 explicitly includes possible ferredoxin donation in its definition despite its historical label.

The current exact target lineage is reconstructed in plastid-energy-source-checks.json. Chloroplast localization does not exclude respiration under the actual GO definitions. Full tobacco PMID:27066014 compares ndhJK/ndhCJK disruptions, heat stress and PTOX inhibition; its fluorescence and P700 results support chlororespiratory involvement, without themselves directly measuring all proposed oxygen-coupled ATP generation. The older categorical respiratory exclusions are withdrawn pending one shared ndhD adjudication. The ATP-synthesis-coupled electron transport term is core because NDH actually performs electron transfer and energy-conserving proton translocation. Primary PMID:28559282 is cached abstract-only; no full-text-only experimental claim is attributed to that cache.

NdhK directly lines the plastoquinone cavity and binds a 4Fe–4S center in the spinach structure; this supports homologous NdhK binding beyond whole-complex substrate reasoning. NdhD is in the antiporter-like arm, so generic quinone binding cannot simply replace its ubiquinone assertion without subunit-specific evidence. Broad light-reaction/plastid/cofactor rows keep legitimate specific replacement recommendations where present. No NEW process assertions, substrate-role inferences or target-specific catalytic-residue claims are added.

The immutable UniProt/GOA files were not edited. Global OpenScientist query-cache exact accession/family and chloroplast-function search returned no matching report before the two shared requests were registered. Audit: projects/IBA_REVIEW/rereview-2026-09-20/plastid-energy-complexes.yaml.
