# LYN curation notes

Gene: LYN (HGNC), UniProt P07948, human. Src-family non-receptor protein
tyrosine kinase (p56Lyn/LynA and p53Lyn/LynB isoforms). EC 2.7.10.2.

## Core identity and molecular function

LYN is a Src-family kinase (SFK) with the canonical SH4–unique–SH3–SH2–kinase(SH1)–
C-terminal-tail architecture. Its molecular function is ATP-dependent phosphorylation
of tyrosine residues in protein substrates (non-membrane-spanning protein tyrosine
kinase activity, GO:0004715).

- UniProt P07948 CATALYTIC ACTIVITY: "L-tyrosyl-[protein] + ATP = O-phospho-L-tyrosyl-[protein] + ADP + H(+) ... EC=2.7.10.2".
- Domains (UniProt FT): SH3 63–123, SH2 129–226, protein kinase 247–501; ATP binding 253–261 and K275; active site D367.
- Regulation: autophosphorylation of activation-loop Tyr397 (required for optimal activity); CSK/MATK phosphorylation of C-terminal Tyr508 is inhibitory (SH2 clamp / closed conformation); dephosphorylation by CD45/PTPRC activates. [UniProt ACTIVITY REGULATION]
- Membrane targeting: Gly2 N-myristoylation + Cys3 S-palmitoylation → plasma membrane cytoplasmic face and lipid rafts. Traffics via Golgi. [15173188, 20605918, 18817770; UniProt LIPID features]

## Substrate recognition and dual signaling role

LYN is a receptor-proximal signaling switch that phosphorylates BOTH activating ITAMs
and inhibitory ITIMs (dualistic role). [deep-research falcon; L'Estrange-Stranieri 2024 Front Immunol]

- ITAM/activating: "An initial signaling event following activation of the B cell antigen receptor is phosphorylation of the CD79a (Ig-alpha) ITAM by Lyn, a Src family protein-tyrosine kinase." [PMID:10748115]
- HS1/HCLS1 substrate: "p75HS1 showed rapid tyrosine phosphorylation and association with a Src-like kinase, Lyn, after crosslinking of membrane-bound IgM." [PMID:7682714]
- ITIM/inhibitory: phosphorylates CD22, FcγRIIB, PIR-B, SIRPα ITIMs → recruits SHP-1/SHP-2 and SHIP-1 phosphatases, restraining BCR/FcR signaling. UniProt: "Down-regulates signaling pathways by phosphorylation of immunoreceptor tyrosine-based inhibitory motifs (ITIM)". [UniProt FUNCTION]
- Dual: "Lyn appears to play a critical role in B cell receptor signaling due to its dual modulating capacity via activating or inhibiting downstream pathways" [PMID:35941532]

Substrates named in UniProt include BTK, CBL, CD5, CD19, CD22, CD72, CD79A, CD79B,
CSF2RB, DOK1, HCLS1, LILRB3/PIR-B, MS4A2/FCER1B, SYK, TEC, SIRPA, PTPN6, INPP5D, LPXN, SCIMP.

## Localization

- Plasma membrane (cytoplasmic face) / lipid rafts — principal functional location. [IBA is_active_in; 12670955; 11313396]
- Golgi apparatus and perinuclear region — biosynthetic trafficking. "Lyn ... is biosynthetically transported to the plasma membrane via the Golgi pool of caveolin along the secretory pathway." [PMID:15173188]; "After synthesis in the cytoplasm, Lyn accumulates on the Golgi and is subsequently transported to the plasma membrane." [PMID:20605918]
- Nucleus — DNA-damage/kinase-inhibited pool. "Lyn was definitely detected in purified nuclei by immunofluorescence and immunoblotting analyses." [PMID:18817770]; "The cellular response to DNA damage includes activation of the nuclear Lyn protein tyrosine kinase." [PMID:10891478]
- Cytosol — many Reactome TAS rows record reaction compartment; accurate but low information; kept non-core.

## Biological processes (mostly non-core / downstream)

- Immune-receptor signaling (BCR, FcεRI, FcγR, C-type lectin) — LYN executes proximal phosphorylation; treated as core-adjacent.
- DNA damage response / SAPK-JNK: "activation of SAPK by DNA damage is mediated in part by Lyn" [PMID:10891478]; "these two proteins physically and functionally interact to regulate DNA damage-induced apoptosis" (GADD34/PPP1R15A) [PMID:11517336].
- Integrin/adhesion & chemotaxis: "in chemokine-stimulated hematopoietic cells Lyn kinase is a positive regulator of cell movement while negatively regulating adhesion to stromal cells by inhibiting the ICAM-1-binding activity of beta(2) integrins" [PMID:16467205]; "in SDF-1alpha-stimulated monocytes, Lyn acts as a positive regulator of migration and a negative regulator of adhesion" [PMID:18802065].
- Hematopoiesis: mast cell (SCF/KIT) proliferation [PMID:11435302], eosinophil differentiation via IL-5R [PMID:11823534], thrombopoietin/erythropoietin responses.
- TLR: facilitates TLR4-TLR6 heterodimerization downstream of CD36 "these data support a role for CD36-Lyn kinase interactions ... in facilitating TLR4-TLR6 heterodimerization and signal initiation" [PMID:20037584]; TLR9 tyrosine phosphorylation [PMID:40980882].

## Disease

- Gain-of-function LYN (LAVLI): "two de novo truncating variants in the Src-family tyrosine kinase, LYN, p.Y508*, p.Q507* and a de novo missense variant, p.Y508F, that result in constitutive activation of Lyn kinase" causing cutaneous small-vessel vasculitis + liver fibrosis. [PMID:36932076; PMID:36122175]

## Curation decisions (summary)

- Core MF: GO:0004715 (and parent GO:0004713 protein tyrosine kinase activity) = ACCEPT; ATP binding, protein kinase activity, kinase activity ACCEPT (broad/correct).
- GO:0005515 protein binding (IPI, ~40 rows): REMOVE — uninformative; interactions may be real but convey no specific function (per repo policy: never MARK_AS_OVER_ANNOTATED for protein binding).
- Membrane/raft/Golgi/nucleus/cytoplasm CC: ACCEPT; Reactome-TAS cytosol and vesicle/lysosome reaction compartments = KEEP_AS_NON_CORE.
- Receptor-proximal immunoreceptor signaling processes + phosphorylation BP: ACCEPT.
- Downstream immune/hematopoietic/adhesion/DNA-damage/TLR/MAPK/differentiation processes: KEEP_AS_NON_CORE.
- Dubious rat-ortholog (GO_REF:0000107, UniProtKB:Q07014) electronic transfers to organelles/structures not supported for human LYN (mitochondrial crista/membrane, glutamatergic synapse, postsynaptic specialization, adherens junction, gamma-tubulin binding, glycosphingolipid binding, integrin alpha2-beta1 complex, PDGFR binding, enzyme/complex binding): REMOVE or KEEP_AS_NON_CORE as noted per-row.
- No NEW terms added: kinase MF and ITAM/ITIM immunoreceptor signaling are already present; participation + comparator tests give no missing supported core function.


## 2026-10-26 full annotation audit: evidence review in progress

The preserved acquisition baseline and raw-file hashes are in `.cache/module-audit-logs/b-cell-panel-baseline.json`. This review covers all annotations, including functions outside B-cell signaling. Normal acquisition and actual provider attempts are recorded in `b-cell-acquisition-report.md` and `b-cell-fetch/provider-publication-results.json`; provider failures are not research reports. Existing genuine exact-target reports, where available, are discovery aids. Original machine annotation payloads and raw source records will be preserved.


## 2026-10-26 completed full annotation audit

LYN is a non-receptor Src-family tyrosine kinase with activating and inhibitory receptor roles. The negative BCR core now rests on native Lyn-deficient B-cell CD22/SHP-1 evidence in full PMID:9480991. PMID:35941532 concerns the opposite regulatory direction in lymphoma and is not used as direct proof that LYN inhibits BCR signaling. The genuine pre-existing Falcon report is used only as corroborative synthesis alongside primary evidence; no report was manufactured.

Rat donor tracing restored supported noncanonical contexts: gamma-tubulin association (PMID:10545487), adherens junctions (PMID:1709169), neuronal postsynaptic signaling (PMID:14529711), dynamin/PKCδ binding (PMID:8757630/9692543) and the mitochondrial crista lumen (PMID:12007793). Crista localization does not establish integral mitochondrial membrane residence, so the latter remains unresolved. The alpha2beta1 integrin-complex term describes the actual heterodimer; a larger Lyn-containing signaling co-complex in full PMID:18234883 does not make Lyn a heterodimer subunit. Glycosphingolipid binding remains unresolved because the accessible association does not settle direct lipid binding versus a protein bridge.

PMID:24217950 supports EphA4 interaction/phosphorylation and feedback, with an actual publisher supplementary co-IP caption recovered. It does not settle the positive sign of APP catabolism merely by reporting fragment accumulation. The GO receptor-activator definition permits an activating interaction rather than requiring an extracellular ligand. The exact main-text assay remains access-limited.

The formerly generic rat-response reasons now name actual experiments: cholesterol depletion/repletion and cyclodextrin (PMID:10330413), drug-dependent cardiac LynA complex recruitment (PMID:17039281), 6-OHDA/L-DOPA expression responses (PMID:16529858), insulin-induced hepatic Lyn autophosphorylation distinct from leptin (PMID:12089355), burn-associated neutrophil activation rather than direct thermosensing (PMID:12372808), and CCK activation in pancreatic acini (PMID:16713446). Native mouse Lyn knockout supports microglial P2X4 induction after nerve injury (PMID:17918263). These are qualified comparative roles, not human-specific assays. Full PMID:32958780 explicitly uses mouse Lyn cDNA; the human membrane claim is independently corroborated rather than relabeling that construct as human. EPOR and thrombopoietin receptor are not called receptor tyrosine kinases; KIT supplies that distinct receptor-class context.

All 320 original annotation payloads, including qualifiers and any negation flags, were preserved; no NEW assertions were added. Normal source acquisition and actual provider outcomes are retained in the acquisition logs. Failed provider calls were not replaced with fabricated reports. Source-access limits are recorded above and in the individual row reasons; partial publisher pages and captcha responses were not treated as full articles. The six-member focused strict/schema, GO-term and source-quotation check passed with zero errors and warnings before final packaging; the final package reruns those checks after finding additions. Record-section backfill, HTML rendering, helper-generated Codex provenance and exact payload/raw-hash checks accompany the package.

Source-access provenance: the publisher page for PMID:24217950 was normally cached at `publications/url_https___link.springer.com_article_10.1007_s12035-013-8580-x.md`; it exposes the abstract and supplementary co-IP captions, not the full main article. Full PMC text for PMID:9113989 was normally recovered at `publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC20722_.md` during the PI3K source audit. Captcha pages and the scanned/abstract-only PMC359464 recovery were not treated as usable full-text evidence.
