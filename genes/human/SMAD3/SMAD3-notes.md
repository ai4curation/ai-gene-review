# SMAD3 annotation audit, 2026-10-25

Reviewed all 349 original rows for human SMAD3 (P84022), preserving each seeded term, evidence code and original reference identifier. No new process annotations were added. The annotation-reviewer workflow used the existing Falcon report, curated UniProt text, all cached original PMID records, targeted full-text reading and 22 additional primary donor/binding papers. Existing provider authentication/quota failures were already documented in the parent project; the available Falcon report was reused rather than rerun.

## Biological synthesis

SMAD3 is an R-SMAD DNA-binding transcription factor shared by TGF-beta, activin and nodal signaling. It is a receptor kinase substrate, not a kinase enzyme. It can regulate a kinase (PDPK1) through a protein interaction without catalyzing phosphorylation itself [PMID:17327236]. Its MH1 domain binds regulatory DNA and coordinates zinc [PMID:12686552]; phosphorylated SMAD3 assembles with SMAD4 in a two-R-SMAD/one-SMAD4 heterotrimer [PMID:15350224]. SMAD3/TTF1 transcription and microprocessor responses can be SMAD4 independent [PMID:25060702; PMID:18548003]. The core functions now separate direct transcriptional regulation from co-SMAD binding; a redundant third DNA-binding core was removed.

The activin receptor evidence is PMID:9892009: “Smad2 and Smad3 are released into the cytoplasm where they interact with the common partner Smad4.” PMID:15150278 is a nodal/ALK7 trophoblast study, not by itself activin-ligand evidence. These functions cannot be generalized to every member of the full SMAD family. The older distinction that full-length SMAD2 cannot bind DNA is not supported by the full-length structural/biochemical study PMID:31582430.

## Material corrections

- Ortholog transfers were traced to rat/mouse primary publications rather than dismissed for lacking human assays. Collagen binding is an actual two-hybrid/GST result [PMID:14559231], and beta-catenin binding/protection from degradation is experimentally reported [PMID:20097766]. These are non-core contexts, not canonical extracellular collagen sensing or a universal Wnt role.
- Restored specific secondary outputs: IL-1beta and TGFB3 production, chemotaxis, stress fibers, focal adhesions, cocaine-associated neuronal plasticity, and pulmonary-cell calcium regulation. Model species and assay scope are explicit in each review. Calcium regulation does not mean SMAD3 is a calcium channel.
- The full text of PMID:25605017 explicitly calls the MIR29C promoter site a sterol regulatory element. Its result is SMAD3-dependent repression of miR29c and downstream Wnt activation, not transcriptional activation at that locus. The activator annotation remains true on independent evidence, with the citation mismatch documented. No cholesterol-homeostasis process was inferred.
- PMID:12874272 concerns HIPK2/SKI, not CDK8/CDK9. Kinase binding is refined on independent receptor, CK1gamma2 and PDPK1 evidence. Being phosphorylated does not establish kinase catalysis.
- Bare protein binding remains unaccepted. Where the original paper resolves the interaction class, 14 rows now propose a supported specific binding function. Other bare binding rows remain removed as uninformative, not because the experiments were considered false.
- General transcription/DNA-binding/metal/enzyme terms are refined to supported terms already present or specific binding descendants. Broad multi-context cellular locations and differentiation remain legitimate when a narrower replacement would erase scope.

## Access limits and unresolved claims

Most caches contain abstracts, not full text. No experimental annotation was rejected because a title foregrounded another gene. Sixteen claims remain UNDECIDED: MAPK cascade, JNK cascade, ureteric bud development, cytochrome-c release, gamma-radiation response, adrenal development, osteoblast proliferation, PDGF response, mitochondrial membrane-potential regulation, glucose response, alcohol response, reduced TGF-beta production, positive regulation of SMAD signaling, mineralocorticoid-receptor binding, ubiquitin binding and homodimerization. Specific stoichiometry cannot be inferred from generic homomeric association; covalent ubiquitination cannot establish noncovalent ubiquitin binding.

Targeted full-text retrieval was attempted for the uncertain receptor/ubiquitin interactions; Europe PMC returned HTTP 500 for some full-text endpoints, and publisher access was unavailable for others. The manuscript of PMID:25605017 was read online for the SRE/repression result; its local cache remains abstract-only and was not edited. No invented supporting quotation was added for that uncached passage.

PMID:16751101 has PubMed-linked 2016 editorial concern/update notices [PMID:27058669; PMID:27610577]. Their full publisher text could not be accessed. The reference is marked DISPUTED without claiming a retraction or a specific invalidated figure. Independent MTMR4 coimmunoprecipitation/dephosphorylation evidence [PMID:20061380] supports the protein-phosphatase-binding class; no new catalytic activity was assigned to SMAD3.

## Coverage and verification

Final actions: ACCEPT 167, KEEP_AS_NON_CORE 69, MODIFY 43, REMOVE 54, UNDECIDED 16. All 349 rows have decisions; no PENDING or NEW rows.

All original row fields other than review were compared programmatically before writing. The final validation and history validation results are recorded below.

## Annotation audit ledger

Row numbers are one-based YAML order. The ledger makes the review coverage and source choices inspectable.

| Row | GO term | Decision | Independent supporting sources |
|---|---|---|---|
| 1 | GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:12686552, PMID:9732876, PMID:31582430 |
| 2 | GO:0009653 anatomical structure morphogenesis | KEEP_AS_NON_CORE | PMID:11585338, PMID:21035443 |
| 3 | GO:0030154 cell differentiation | KEEP_AS_NON_CORE | PMID:11585338, PMID:19816956, PMID:21035443 |
| 4 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:9892009, PMID:12844345 |
| 5 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | ACCEPT | PMID:9732876, PMID:32141990 |
| 6 | GO:0060395 SMAD protein signal transduction | ACCEPT | PMID:9311995, PMID:8774881, file:human/SMAD3/SMAD3-deep-research-falcon.md |
| 7 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:8774881, PMID:9311995 |
| 8 | GO:0071144 heteromeric SMAD protein complex | ACCEPT | PMID:15350224, PMID:9311995 |
| 9 | GO:0045944 positive regulation of transcription by RNA polymerase II | ACCEPT | PMID:9732876 |
| 10 | GO:0070411 I-SMAD binding | ACCEPT | PMID:26555259 |
| 11 | GO:0003677 DNA binding | MODIFY | PMID:12686552, PMID:9732876 |
| 12 | GO:0005634 nucleus | ACCEPT | PMID:9311995 |
| 13 | GO:0005667 transcription regulator complex | ACCEPT | PMID:25060702 |
| 14 | GO:0005737 cytoplasm | ACCEPT | PMID:9311995 |
| 15 | GO:0006355 regulation of DNA-templated transcription | MODIFY | PMID:9732876, PMID:32141990 |
| 16 | GO:0032502 developmental process | MODIFY | PMID:11585338, PMID:21035443 |
| 17 | GO:0046872 metal ion binding | MODIFY | PMID:12686552 |
| 18 | GO:0071363 cellular response to growth factor stimulus | ACCEPT | PMID:9311995, PMID:9892009 |
| 19 | GO:0141091 transforming growth factor beta receptor superfamily signaling pathway | MODIFY | PMID:9311995, PMID:9892009, PMID:15150278 |
| 20 | GO:0005515 protein binding | MODIFY | PMID:11278756 |
| 21 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 22 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 23 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 24 | GO:0005515 protein binding | MODIFY | PMID:12857746 |
| 25 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 26 | GO:0005515 protein binding | MODIFY | PMID:15084259 |
| 27 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 28 | GO:0005515 protein binding | MODIFY | PMID:15350224 |
| 29 | GO:0005515 protein binding | MODIFY | PMID:15527767 |
| 30 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 31 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 32 | GO:0005515 protein binding | MODIFY | PMID:18548003 |
| 33 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 34 | GO:0005515 protein binding | MODIFY | PMID:19032343 |
| 35 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 36 | GO:0005515 protein binding | MODIFY | PMID:20061380 |
| 37 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 38 | GO:0005515 protein binding | MODIFY | PMID:21258410 |
| 39 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 40 | GO:0005515 protein binding | MODIFY | PMID:21532621 |
| 41 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 42 | GO:0005515 protein binding | MODIFY | PMID:21828274 |
| 43 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 44 | GO:0005515 protein binding | MODIFY | PMID:22045334 |
| 45 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 46 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 47 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 48 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 49 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 50 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 51 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 52 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 53 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 54 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 55 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 56 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 57 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 58 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 59 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 60 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 61 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 62 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 63 | GO:0042802 identical protein binding | ACCEPT | PMID:9111321, PMID:15350224 |
| 64 | GO:0042802 identical protein binding | ACCEPT | PMID:9111321, PMID:15350224 |
| 65 | GO:0000122 negative regulation of transcription by RNA polymerase II | ACCEPT | PMID:32141990 |
| 66 | GO:0000165 MAPK cascade | UNDECIDED | PMID:18802055 |
| 67 | GO:0000977 RNA polymerase II transcription regulatory region sequence-specific DNA binding | ACCEPT | PMID:9732876 |
| 68 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | ACCEPT | PMID:9732876 |
| 69 | GO:0001649 osteoblast differentiation | KEEP_AS_NON_CORE | PMID:11585338 |
| 70 | GO:0001657 ureteric bud development | UNDECIDED | PMID:14656760 |
| 71 | GO:0001836 release of cytochrome c from mitochondria | UNDECIDED | PMID:11839804 |
| 72 | GO:0003682 chromatin binding | ACCEPT | PMID:21828274 |
| 73 | GO:0003690 double-stranded DNA binding | MODIFY | PMID:12686552, PMID:9732876 |
| 74 | GO:0003700 DNA-binding transcription factor activity | MODIFY | PMID:9732876, PMID:32141990 |
| 75 | GO:0005518 collagen binding | KEEP_AS_NON_CORE | PMID:14559231 |
| 76 | GO:0005886 plasma membrane | KEEP_AS_NON_CORE | PMID:9311995 |
| 77 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:9311995 |
| 78 | GO:0007254 JNK cascade | UNDECIDED | PMID:18802055 |
| 79 | GO:0008013 beta-catenin binding | KEEP_AS_NON_CORE | PMID:20097766 |
| 80 | GO:0008285 negative regulation of cell population proliferation | KEEP_AS_NON_CORE | PMID:14555988 |
| 81 | GO:0010332 response to gamma radiation | UNDECIDED | PMID:34036875 |
| 82 | GO:0010467 gene expression | MODIFY | PMID:20182440, PMID:9732876, PMID:32141990 |
| 83 | GO:0019899 enzyme binding | MODIFY | PMID:18794808, PMID:16751101, PMID:15781469, PMID:20061380 |
| 84 | GO:0023019 signal transduction involved in regulation of gene expression | ACCEPT | PMID:9732876 |
| 85 | GO:0030325 adrenal gland development | UNDECIDED | PMID:12844345 |
| 86 | GO:0030335 positive regulation of cell migration | KEEP_AS_NON_CORE | PMID:17545585 |
| 87 | GO:0030501 positive regulation of bone mineralization | KEEP_AS_NON_CORE | PMID:12096832 |
| 88 | GO:0031490 chromatin DNA binding | ACCEPT | PMID:21828274 |
| 89 | GO:0032332 positive regulation of chondrocyte differentiation | KEEP_AS_NON_CORE | PMID:21035443 |
| 90 | GO:0032731 positive regulation of interleukin-1 beta production | KEEP_AS_NON_CORE | PMID:16371439 |
| 91 | GO:0032916 positive regulation of transforming growth factor beta3 production | KEEP_AS_NON_CORE | PMID:16891311 |
| 92 | GO:0032993 protein-DNA complex | ACCEPT | PMID:12686552 |
| 93 | GO:0033689 negative regulation of osteoblast proliferation | UNDECIDED | PMID:21035443 |
| 94 | GO:0036120 cellular response to platelet-derived growth factor stimulus | UNDECIDED | PMID:30066831 |
| 95 | GO:0042110 T cell activation | KEEP_AS_NON_CORE | PMID:10064594 |
| 96 | GO:0042177 negative regulation of protein catabolic process | KEEP_AS_NON_CORE | PMID:20097766 |
| 97 | GO:0042220 response to cocaine | KEEP_AS_NON_CORE | PMID:26030849 |
| 98 | GO:0042802 identical protein binding | ACCEPT | PMID:9111321, PMID:15350224 |
| 99 | GO:0043066 negative regulation of apoptotic process | KEEP_AS_NON_CORE | PMID:14517210 |
| 100 | GO:0043565 sequence-specific DNA binding | MODIFY | PMID:9732876, PMID:10823886 |
| 101 | GO:0045429 positive regulation of nitric oxide biosynthetic process | KEEP_AS_NON_CORE | PMID:27038547 |
| 102 | GO:0045944 positive regulation of transcription by RNA polymerase II | ACCEPT | PMID:9732876 |
| 103 | GO:0050728 negative regulation of inflammatory response | KEEP_AS_NON_CORE | PMID:20935647 |
| 104 | GO:0050776 regulation of immune response | KEEP_AS_NON_CORE | PMID:10064594, PMID:20935647 |
| 105 | GO:0050821 protein stabilization | KEEP_AS_NON_CORE | PMID:20097766 |
| 106 | GO:0050927 positive regulation of positive chemotaxis | KEEP_AS_NON_CORE | PMID:15987742 |
| 107 | GO:0051496 positive regulation of stress fiber assembly | KEEP_AS_NON_CORE | PMID:15987742 |
| 108 | GO:0051881 regulation of mitochondrial membrane potential | UNDECIDED | PMID:11839804 |
| 109 | GO:0051894 positive regulation of focal adhesion assembly | KEEP_AS_NON_CORE | PMID:15987742 |
| 110 | GO:0060290 transdifferentiation | KEEP_AS_NON_CORE | PMID:15987742 |
| 111 | GO:0060395 SMAD protein signal transduction | ACCEPT | PMID:9311995 |
| 112 | GO:0061001 regulation of dendritic spine morphogenesis | KEEP_AS_NON_CORE | PMID:26030849 |
| 113 | GO:0061045 negative regulation of wound healing | KEEP_AS_NON_CORE | PMID:21035443 |
| 114 | GO:0061629 RNA polymerase II-specific DNA-binding transcription factor binding | ACCEPT | PMID:9732876 |
| 115 | GO:0061767 negative regulation of lung blood pressure | KEEP_AS_NON_CORE | PMID:27038547 |
| 116 | GO:0071333 cellular response to glucose stimulus | UNDECIDED | PMID:32065356 |
| 117 | GO:0071560 cellular response to transforming growth factor beta stimulus | ACCEPT | PMID:9311995 |
| 118 | GO:0090263 positive regulation of canonical Wnt signaling pathway | KEEP_AS_NON_CORE | PMID:20097766 |
| 119 | GO:0097191 extrinsic apoptotic signaling pathway | KEEP_AS_NON_CORE | PMID:15334054 |
| 120 | GO:0097305 response to alcohol | UNDECIDED | PMID:31628824 |
| 121 | GO:0098586 cellular response to virus | KEEP_AS_NON_CORE | PMID:18802055 |
| 122 | GO:1903243 negative regulation of cardiac muscle hypertrophy in response to stress | KEEP_AS_NON_CORE | PMID:27038547 |
| 123 | GO:1990841 promoter-specific chromatin binding | ACCEPT | PMID:18802055 |
| 124 | GO:0005654 nucleoplasm | ACCEPT | PMID:15799969 |
| 125 | GO:0006355 regulation of DNA-templated transcription | MODIFY | PMID:9732876, PMID:32141990 |
| 126 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:35359452 |
| 127 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:9892009, PMID:12844345 |
| 128 | GO:0005634 nucleus | ACCEPT | PMID:20935647 |
| 129 | GO:0005737 cytoplasm | ACCEPT | PMID:20935647 |
| 130 | GO:0006355 regulation of DNA-templated transcription | MODIFY | PMID:9732876, PMID:32141990 |
| 131 | GO:0031665 negative regulation of lipopolysaccharide-mediated signaling pathway | KEEP_AS_NON_CORE | PMID:29789615 |
| 132 | GO:0050728 negative regulation of inflammatory response | KEEP_AS_NON_CORE | PMID:27060871 |
| 133 | GO:0071635 negative regulation of transforming growth factor beta production | UNDECIDED | PMID:20935647 |
| 134 | GO:0061450 trophoblast cell migration | KEEP_AS_NON_CORE | PMID:34432647 |
| 135 | GO:0045596 negative regulation of cell differentiation | KEEP_AS_NON_CORE | PMID:19816956 |
| 136 | GO:0060391 positive regulation of SMAD protein signal transduction | UNDECIDED | PMID:15107418 |
| 137 | GO:0097190 apoptotic signaling pathway | KEEP_AS_NON_CORE | PMID:15107418 |
| 138 | GO:0030279 negative regulation of ossification | KEEP_AS_NON_CORE | PMID:22155034 |
| 139 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:8774881 |
| 140 | GO:0060395 SMAD protein signal transduction | ACCEPT | PMID:30729664 |
| 141 | GO:1901203 positive regulation of extracellular matrix assembly | KEEP_AS_NON_CORE | PMID:30729664 |
| 142 | GO:1902895 positive regulation of miRNA transcription | KEEP_AS_NON_CORE | PMID:30729664 |
| 143 | GO:1990776 response to angiotensin | KEEP_AS_NON_CORE | PMID:30729664 |
| 144 | GO:0060395 SMAD protein signal transduction | ACCEPT | PMID:9732876 |
| 145 | GO:0031625 ubiquitin protein ligase binding | KEEP_AS_NON_CORE | PMID:15781469, PMID:19122240 |
| 146 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:9311995 |
| 147 | GO:0060395 SMAD protein signal transduction | ACCEPT | PMID:9311995 |
| 148 | GO:0001222 transcription corepressor binding | ACCEPT | PMID:14612439 |
| 149 | GO:0003700 DNA-binding transcription factor activity | MODIFY | PMID:9732876, PMID:32141990 |
| 150 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:10823886 |
| 151 | GO:0060395 SMAD protein signal transduction | ACCEPT | PMID:10823886 |
| 152 | GO:0060395 SMAD protein signal transduction | ACCEPT | PMID:9111321 |
| 153 | GO:0000987 cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:32141990 |
| 154 | GO:0003700 DNA-binding transcription factor activity | MODIFY | PMID:9732876, PMID:32141990 |
| 155 | GO:1902894 negative regulation of miRNA transcription | KEEP_AS_NON_CORE | PMID:32141990 |
| 156 | GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:12686552, PMID:9732876, PMID:31582430 |
| 157 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | ACCEPT | PMID:24378993 |
| 158 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | ACCEPT | PMID:24378993 |
| 159 | GO:0010629 negative regulation of gene expression | KEEP_AS_NON_CORE | PMID:24378993 |
| 160 | GO:1902895 positive regulation of miRNA transcription | KEEP_AS_NON_CORE | PMID:24378993 |
| 161 | GO:1902895 positive regulation of miRNA transcription | KEEP_AS_NON_CORE | PMID:24378993 |
| 162 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 163 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 164 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 165 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | ACCEPT | PMID:9732876 |
| 166 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | ACCEPT | PMID:9732876, PMID:24378993 |
| 167 | GO:0032810 sterol response element binding | KEEP_AS_NON_CORE | PMID:25605017 |
| 168 | GO:0061629 RNA polymerase II-specific DNA-binding transcription factor binding | ACCEPT | PMID:9732876 |
| 169 | GO:0140297 DNA-binding transcription factor binding | MODIFY | PMID:21828274 |
| 170 | GO:0016922 nuclear receptor binding | KEEP_AS_NON_CORE | PMID:31023188 |
| 171 | GO:0008285 negative regulation of cell population proliferation | KEEP_AS_NON_CORE | PMID:14555988 |
| 172 | GO:1902893 regulation of miRNA transcription | MODIFY | PMID:25605017 |
| 173 | GO:0000122 negative regulation of transcription by RNA polymerase II | ACCEPT | PMID:28467929 |
| 174 | GO:0001217 DNA-binding transcription repressor activity | ACCEPT | PMID:28467929 |
| 175 | GO:0003677 DNA binding | MODIFY | PMID:12686552, PMID:9732876 |
| 176 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:28467929 |
| 177 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 178 | GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific | ACCEPT | PMID:26311719 |
| 179 | GO:1902895 positive regulation of miRNA transcription | KEEP_AS_NON_CORE | PMID:26311719 |
| 180 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 181 | GO:0005634 nucleus | ACCEPT | PMID:23723426 |
| 182 | GO:0005829 cytosol | ACCEPT | PMID:23723426 |
| 183 | GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:12686552, PMID:9732876, PMID:31582430 |
| 184 | GO:0005634 nucleus | ACCEPT | PMID:21145499 |
| 185 | GO:0005737 cytoplasm | ACCEPT | PMID:21145499 |
| 186 | GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:12686552, PMID:9732876, PMID:31582430 |
| 187 | GO:0001223 transcription coactivator binding | ACCEPT | PMID:16777850 |
| 188 | GO:0000987 cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:21828274 |
| 189 | GO:0000785 chromatin | ACCEPT | PMID:21828274 |
| 190 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | ACCEPT | PMID:9732876, PMID:32141990 |
| 191 | GO:0000981 DNA-binding transcription factor activity, RNA polymerase II-specific | ACCEPT | PMID:9732876, PMID:32141990 |
| 192 | GO:0042307 positive regulation of protein import into nucleus | ACCEPT | PMID:15799969 |
| 193 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 194 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:18548003 |
| 195 | GO:0017151 DEAD/H-box RNA helicase binding | KEEP_AS_NON_CORE | PMID:18548003 |
| 196 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 197 | GO:0031962 nuclear mineralocorticoid receptor binding | UNDECIDED | PMID:12902338 |
| 198 | GO:0035259 nuclear glucocorticoid receptor binding | KEEP_AS_NON_CORE | PMID:12902338 |
| 199 | GO:0071560 cellular response to transforming growth factor beta stimulus | ACCEPT | PMID:12902338 |
| 200 | GO:0045429 positive regulation of nitric oxide biosynthetic process | KEEP_AS_NON_CORE | PMID:27038547 |
| 201 | GO:0051481 negative regulation of cytosolic calcium ion concentration | KEEP_AS_NON_CORE | PMID:27038547 |
| 202 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 203 | GO:0005634 nucleus | ACCEPT | PMID:25893292 |
| 204 | GO:0045599 negative regulation of fat cell differentiation | KEEP_AS_NON_CORE | PMID:19816956 |
| 205 | GO:1901203 positive regulation of extracellular matrix assembly | KEEP_AS_NON_CORE | PMID:21307346 |
| 206 | GO:0005634 nucleus | ACCEPT | PMID:16007207 |
| 207 | GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:12686552, PMID:9732876, PMID:31582430 |
| 208 | GO:0006357 regulation of transcription by RNA polymerase II | MODIFY | PMID:9732876, PMID:32141990 |
| 209 | GO:0045944 positive regulation of transcription by RNA polymerase II | ACCEPT | PMID:14555988 |
| 210 | GO:0010628 positive regulation of gene expression | MODIFY | PMID:21307346 |
| 211 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 212 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 213 | GO:0070412 R-SMAD binding | ACCEPT | PMID:9311995 |
| 214 | GO:0000785 chromatin | ACCEPT | PMID:21828274 |
| 215 | GO:0043425 bHLH transcription factor binding | ACCEPT | PMID:21828274 |
| 216 | GO:0071144 heteromeric SMAD protein complex | ACCEPT | PMID:15350224, PMID:9311995 |
| 217 | GO:0097191 extrinsic apoptotic signaling pathway | KEEP_AS_NON_CORE | PMID:15334054 |
| 218 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 219 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 220 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 221 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 222 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 223 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 224 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 225 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 226 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 227 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 228 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 229 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 230 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 231 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 232 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 233 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 234 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 235 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 236 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 237 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 238 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 239 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 240 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 241 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 242 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 243 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 244 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 245 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 246 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 247 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 248 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 249 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 250 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 251 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 252 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 253 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 254 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 255 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 256 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 257 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 258 | GO:0005654 nucleoplasm | ACCEPT | PMID:9311995, PMID:15799969 |
| 259 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 260 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 261 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 262 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 263 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 264 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 265 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 266 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 267 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 268 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 269 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 270 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 271 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 272 | GO:0000987 cis-regulatory region sequence-specific DNA binding | ACCEPT | PMID:21947082 |
| 273 | GO:0003700 DNA-binding transcription factor activity | MODIFY | PMID:9732876, PMID:32141990 |
| 274 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 275 | GO:0005634 nucleus | ACCEPT | PMID:21947082 |
| 276 | GO:0005667 transcription regulator complex | ACCEPT | PMID:21947082 |
| 277 | GO:0005737 cytoplasm | ACCEPT | PMID:21947082 |
| 278 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:21947082 |
| 279 | GO:0071141 SMAD protein complex | ACCEPT | PMID:21947082 |
| 280 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 281 | GO:0010718 positive regulation of epithelial to mesenchymal transition | KEEP_AS_NON_CORE | PMID:21307346 |
| 282 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 283 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 284 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 285 | GO:0032924 activin receptor signaling pathway | ACCEPT | PMID:9892009, PMID:12844345 |
| 286 | GO:0038092 nodal signaling pathway | ACCEPT | PMID:15150278 |
| 287 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 288 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 289 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 290 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 291 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 292 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 293 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 294 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 295 | GO:0005829 cytosol | ACCEPT | PMID:9311995, PMID:15799969 |
| 296 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 297 | GO:0043130 ubiquitin binding | UNDECIDED | PMID:18794808 |
| 298 | GO:0005515 protein binding | MODIFY | PMID:17469184 |
| 299 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 300 | GO:0045944 positive regulation of transcription by RNA polymerase II | ACCEPT | PMID:18832382 |
| 301 | GO:0071141 SMAD protein complex | ACCEPT | PMID:18832382 |
| 302 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 303 | GO:0008270 zinc ion binding | ACCEPT | PMID:12686552 |
| 304 | GO:0019902 phosphatase binding | MODIFY | PMID:16751101, PMID:20061380 |
| 305 | GO:0061629 RNA polymerase II-specific DNA-binding transcription factor binding | ACCEPT | PMID:9732876 |
| 306 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 307 | GO:0031625 ubiquitin protein ligase binding | KEEP_AS_NON_CORE | PMID:15781469, PMID:19122240 |
| 308 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 309 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 310 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 311 | GO:0005637 nuclear inner membrane | KEEP_AS_NON_CORE | PMID:15647271 |
| 312 | GO:0005515 protein binding | MODIFY | PMID:19049980 |
| 313 | GO:0019901 protein kinase binding | MODIFY | PMID:9311995, PMID:18794808, PMID:17327236 |
| 314 | GO:0010718 positive regulation of epithelial to mesenchymal transition | KEEP_AS_NON_CORE | PMID:18505915 |
| 315 | GO:0045216 cell-cell junction organization | KEEP_AS_NON_CORE | PMID:18505915 |
| 316 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 317 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 318 | GO:0070410 co-SMAD binding | ACCEPT | PMID:9311995, PMID:15350224 |
| 319 | GO:0070410 co-SMAD binding | ACCEPT | PMID:9311995, PMID:15350224 |
| 320 | GO:0070410 co-SMAD binding | ACCEPT | PMID:9311995, PMID:15350224 |
| 321 | GO:0070410 co-SMAD binding | ACCEPT | PMID:9311995, PMID:15350224 |
| 322 | GO:0070412 R-SMAD binding | ACCEPT | PMID:9311995 |
| 323 | GO:0000976 transcription cis-regulatory region binding | MODIFY | PMID:9732876, PMID:10823886 |
| 324 | GO:0003700 DNA-binding transcription factor activity | MODIFY | PMID:9732876, PMID:32141990 |
| 325 | GO:0007179 transforming growth factor beta receptor signaling pathway | ACCEPT | PMID:9732876 |
| 326 | GO:0045893 positive regulation of DNA-templated transcription | MODIFY | PMID:9732876, PMID:10823886 |
| 327 | GO:0003700 DNA-binding transcription factor activity | MODIFY | PMID:9732876, PMID:32141990 |
| 328 | GO:0005160 transforming growth factor beta receptor binding | ACCEPT | PMID:9311995 |
| 329 | GO:0005634 nucleus | ACCEPT | PMID:9311995 |
| 330 | GO:0005737 cytoplasm | ACCEPT | PMID:9311995 |
| 331 | GO:0031053 primary miRNA processing | KEEP_AS_NON_CORE | PMID:18548003, PMID:19018011 |
| 332 | GO:0042060 wound healing | KEEP_AS_NON_CORE | PMID:19018011 |
| 333 | GO:0045893 positive regulation of DNA-templated transcription | MODIFY | PMID:9732876, PMID:10823886 |
| 334 | GO:0045893 positive regulation of DNA-templated transcription | MODIFY | PMID:9732876, PMID:10823886 |
| 335 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 336 | GO:0031625 ubiquitin protein ligase binding | KEEP_AS_NON_CORE | PMID:15781469, PMID:19122240 |
| 337 | GO:0006955 immune response | KEEP_AS_NON_CORE | PMID:20935647, PMID:29789615, PMID:10064594 |
| 338 | GO:0005515 protein binding | REMOVE | Protein-binding policy; original study retained |
| 339 | GO:0000122 negative regulation of transcription by RNA polymerase II | ACCEPT | PMID:32141990 |
| 340 | GO:0000122 negative regulation of transcription by RNA polymerase II | ACCEPT | PMID:32141990 |
| 341 | GO:0045944 positive regulation of transcription by RNA polymerase II | ACCEPT | PMID:8774881 |
| 342 | GO:0001666 response to hypoxia | KEEP_AS_NON_CORE | PMID:12411310 |
| 343 | GO:0032909 regulation of transforming growth factor beta2 production | KEEP_AS_NON_CORE | PMID:12411310 |
| 344 | GO:0005634 nucleus | ACCEPT | PMID:12446380 |
| 345 | GO:0005737 cytoplasm | ACCEPT | PMID:12446380 |
| 346 | GO:0030308 negative regulation of cell growth | KEEP_AS_NON_CORE | PMID:8774881 |
| 347 | GO:0042803 protein homodimerization activity | UNDECIDED | PMID:9111321, PMID:15350224 |
| 348 | GO:0043235 receptor complex | KEEP_AS_NON_CORE | PMID:8774881 |
| 349 | GO:0043565 sequence-specific DNA binding | MODIFY | PMID:9732876, PMID:10823886 |

Final checks: `just backfill-record-sections genes/human/SMAD3` made no changes; `just validate human SMAD3` passed without warnings. All 349 seeded non-review row objects match HEAD exactly. History schema validation also passed for the new audit record.
