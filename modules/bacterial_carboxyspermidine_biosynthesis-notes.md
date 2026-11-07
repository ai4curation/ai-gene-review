# Bacterial carboxyspermidine biosynthesis audit notes

## 2026-11-05 comparative-audit foundation

The existing two-reaction boundary is retained for investigation: putrescine + aspartate semialdehyde to carboxyspermidine, then spermidine. Diamine supply and transport are inputs, and the agmatine/CAPA route needs a distinct boundary. The initial four representative reviews and eight raw files were snapshotted before any acquisition; no existing raw source was refreshed. They contain 23 annotation rows, including five inherited authored NEW proposals, whose provenance must remain distinct from newly proposed annotations.

The inherited claim that no kinetic comparison exists is contradicted by [PMID:37437886, Kinetic and structural characterization of carboxyspermidine dehydrogenase of polyamine biosynthesis](https://pubmed.ncbi.nlm.nih.gov/37437886/): the authors compare putrescine and 1,3-diaminopropane in purified Bacteroides fragilis and Clostridium leptum enzymes. BfCASDH favors putrescine in catalytic efficiency, whereas ClCASDH shows similar measured efficiencies for those two substrates. Cooperativity and physiological substrate supply are separate questions; the old open-gap statement cannot stand unchanged.

[PMID:40074085, New routes for spermine biosynthesis](https://pubmed.ncbi.nlm.nih.gov/40074085/) supplies a second, consequential refinement. Some CASDH/CASDC pairs support onward spermine/thermospermine synthesis, and the Clostridium leptum pair participates in agmatine-dependent chemistry in the authors' heterologous reconstruction. Thus the 2023 putrescine/DAP assays cannot establish the preferred native substrate against untested agmatine. Candidate Clostridium proteins A7VSG1/A7VSG2 are currently treated as specificity comparators, not automatically as a positive native putrescine-route panel. Physiological pathway assignment, isolated enzyme promiscuity and reconstructed chemistry must be reported separately.

[PMID:39887002, Structure of Clostridium leptum carboxyspermidine decarboxylase and comparison to homologs prevalent within the human gut microbiome](https://pubmed.ncbi.nlm.nih.gov/39887002/) provides structural and PLP-binding evidence for the assayed EDO61992.1 protein. Structural resemblance alone does not settle substrate preference. The paper's functional naming must be evaluated together with the 2025 pathway reconstruction.

Review literature searched includes [PMID:27268252, Polyamines in Eukaryotes, Bacteria, and Archaea](https://pubmed.ncbi.nlm.nih.gov/27268252/), [PMID:30254075, Polyamine function in archaea and bacteria](https://pubmed.ncbi.nlm.nih.gov/30254075/) and [PMID:35648468, Polyamine metabolism and transport in gut microbes](https://pubmed.ncbi.nlm.nih.gov/35648468/). The first was fetched with full text; the latter two currently have abstract-only cached records. These reviews orient comparative diversity; primary experiments determine individual enzyme claims. Growth and biofilm phenotypes do not define universally conserved direct enzyme roles.

The audit will retain the experimentally characterized Vibrio and inferred Pseudomonas pair, resolve target identities for Campylobacter, Helicobacter, Bacteroides and alphaproteobacterial examples, and review their individual evidence. The intended sample is provisional until proteins are linked to actual assays, taxon/strain identities and official family assignments. No PANTHER/PTN id will be inferred from a plausible protein name.

QuickGO searches on 2026-11-05 returned active GO:0102143 for carboxynorspermidine dehydrogenase and obsolete GO:0102144 for carboxyspermidine dehydrogenase II. No specific decarboxylase term was returned by those name searches; authoritative definitions and broader searches still need checking before final term choices.

Default Falcon module research was attempted through the normal recipe and failed with HTTP 403 authentication error. This notebook is manual research; the existing OpenScientist file remains unchanged and no Falcon-branded report was fabricated. The baseline, API identity candidates and provider log are under the ignored `.cache/module-audit-logs/carboxyspermidine-20261105/` directory. The scientific curation, family/member checks and PR are not complete.


## 2026-11-06 integrated evidence and scope

The module now has 14 manually reviewed references, including three comparative reviews. PMID:30254075 is now available in normally fetched full text. The precise putrescine-to-spermidine two-reaction pathway remains CONCRETE, with Bacteria as its shared context; a broad taxon does not mean every genome carries the route. Thirteen reaction representatives are distinguished from five reviewed candidates or substrate comparators in `analysis/module_audits/bacterial_carboxyspermidine_biosynthesis/member-panel.yaml`. No complete native pathway is inferred by mixing proteins across organisms.

The putrescine and DAP kinetic comparison in PMID:37437886 replaces the obsolete claim that none exists. PMID:40074085 establishes reconstructed tetraamine and hybrid routes, so universal replacement of S-adenosylmethionine chemistry is withdrawn. The CASDC leaf names the exact RHEA:34095 reaction without inventing a GO id or using broad carboxy-lyase as a precise reaction label; its gene cores use proposed activities.

Three candidates have no asserted core: BT_4612, Cj0172c and HP_1507. The HP_1507 structural comparison finds missing NADP-proximal N-terminal residues in the short 26695 reference; this warrants withholding transfer, not claiming inactivity. Native C. jejuni 81116 CASDH deletion raises spermidine, and the 81116 CASDC biochemical construct was repaired to E184 while the current A8FNH9 canonical sequence contains K184. These details prevent a strain name or family label from substituting for actual assay identity.

The two related family reviews were reconciled with these results: SF4 activity is not asserted, family-wide spermidine participation is unresolved, and SF1 gene cores use reaction-specific proposals. Experimental capability on additional substrates is retained in findings without declaring it a conserved native core.

## 2026-11-06 — PR6089 scientific review follow-up

CAMJ8 now consistently represents its measured dual-substrate decarboxylase activity and retains homodimerization as non-core. BT_0674 is restricted to its demonstrated carboxyspermidine reaction. The different proposal scopes reflect measured substrate evidence, not inconsistent use of family names. The ontology may ultimately provide a shared disjunctive term, but this audit does not infer an unassayed substrate panel from that possibility.

Eight authored spermine/thermospermine BP proposals were withdrawn from the four alphaproteobacterial reviews. Positive native tetraamine context is now cited, including DFMO-associated accumulation and the absence of the competing canonical enzymes, but native pools were not isomer-resolved and these data do not establish each locus's isomer-specific flux. Supported tetraamine molecular activities remain.

HP_1507 now records a SUSPECTED start-site issue without claiming a corrected gene model. CAMJ8 exposes the UniProt kinetic-note discrepancy as a structured source defect. Vibrio rationale blocks are annotation-specific. The exact EDO61992 CASDC/CAPADC naming discrepancy is recorded in the relevant reference assessments. The BT_0674 publisher figure is retrievable from its recorded URL with a pinned hash, without bundling the image in the PR.

The three uncertain upstream candidates still assert no core functions. Cj0172c already has a machine-supplied catalytic row to adjudicate, and its qualified homology-based replacement does not imply a demonstrated native pathway. BT_4612 and HP_1507 have no seeded rows: conservatively declining NEW assertions is not a contradictory judgment about an existing annotation.

All 64 seeded payloads, five inherited NEW rows and 36 raw sources remain unchanged. Nine new proposals remain after withdrawal of eight authored rows. The 22 production compiler cases still pass. Fresh review and CI are required after publication of this follow-up; the earlier requested-changes verdict is not approval.


## 2026-11-07 — substrate-assignment review follow-up

The preceding 2026-11-06 member counts and Cj0172c refinement describe the earlier audit snapshot and are superseded here. HP_0020/O24865 is withdrawn from the putrescine-route reaction representatives and retained as a reviewed comparator. The panel now has 12 reaction representatives and six reviewed comparators, with the same 18 gene reviews. PMID:37878710 identifies the synthesized H. pylori upstream dehydrogenase WP_000557673 and reports CAPA production plus preference for agmatine across the tested orthologs. This undermines a putrescine-specific route inference but does not assay the HP_0020 decarboxylase. Neither exact substrate is assigned from the upstream result. Cj0172c's substrate-specific refinement is likewise provisional; SF2 membership includes CAPADH and does not by itself establish GO:0102143 chemistry.

The historical member panel, withdrawn representative and new compiler results are recorded additively under `analysis/module_audits/bacterial_carboxyspermidine_biosynthesis/substrate-followup-20261107/`. The checker now explicitly rejects HP_0020 alone as an established carboxyspermidine decarboxylation witness and the Helicobacter candidates as a complete putrescine-route panel. This is an evidence-coverage result, not a claim that either enzyme is inactive. Raw publications, historical validation receipts and frozen manifests are retained unchanged. Full validation of the revised scientific content remains pending.

Reaction proposal granularity remains evidence-dependent: the slash-named decarboxylase proposal records two measured activities, while the narrower proposal records one. A future ontology request should state the RHEA:34095/RHEA:34099 relation explicitly; the slash notation does not by itself invalidate demonstrated chemistry. No new GO id or substrate specificity is invented in this follow-up.
