# REL1 (TbMP52, RNA-editing ligase 1) — Trypanosoma brucei TREU927 — curation notes

**Automated deep research was unavailable in this environment (Falcon auth failure, invalid OpenAI key). These notes are a manual literature review** based on the UniProt record (P86927), the cached publications cited in GOA, and additional primary papers located by web search and verified against PubMed before caching.

## Identity
- UniProt P86927 (RLGM1_TRYB2), 469 aa, gene REL1, synonym MP52 / TbMP52, TriTrypDB Tb927.9.4360. N-terminal mitochondrial transit peptide 1..44 (UniProt FT TRANSIT). Belongs to the RNA ligase 2 (Rnl2) family (InterPro IPR012647 RNA_lig_RNL2), the nucleotidyltransferase superfamily shared with DNA ligases and mRNA capping enzymes; active-site lysine K87 forms the covalent ligase-AMP intermediate.
- Paralog REL2 (TbMP48) sits in the insertion subcomplex; REL1 sits in the deletion subcomplex.

## Function
- Identified as a component of the ~1,600 kDa editosome: [PMID:11134327 "These results suggest that TbMP52 and TbMP48 are components of the RNA editing complex."] The purified complex [PMID:11134327 "contains these activities and catalyzes deletion editing in vitro"].
- RNA ligase activity and essentiality: [PMID:11251122 "The TbMP52 protein is shown to be a component of this complex, to have RNA ligase activity, and to be one of two adenylatable proteins in the complex."] and [PMID:11251122 "Regulated repression of TbMP52 blocks editing, which shows that it is a functional component of the editing complex."]; lethal in bloodstream forms [PMID:11251122 "This repression is lethal in bloodforms of the parasite, indicating that editing is essential in the mammalian stage of the life cycle."]
- Structure: 1.2 A crystal structure of the catalytic domain with ATP and Mg2+ [PMID:15465048 "We report here the crystal structure of the catalytic domain of TbREL1 at 1.2 A resolution, in complex with ATP and magnesium."]; REL1 is essential in both life stages [PMID:15465048 "has been shown to be essential for survival of both insect and bloodstream forms of the parasite"]; no close human homolog [PMID:15465048 "the absence of any close homolog in the human genome"].
- Deletion subcomplex: [PMID:14536071 "A purified TbREL1 subcomplex catalyzed precleaved deletion editing in vitro, while a purified TbREL2 subcomplex catalyzed precleaved insertion editing in vitro."]; [PMID:14536071 "The TbREL1 subcomplex contained three to four proteins, including a putative exonuclease, and appeared to be coordinated by the zinc finger protein TbMP63."]

## Localization
- Mitochondrion (transit peptide; editosome purified from mitochondria [PMID:11134327 "was enriched from Trypanosoma brucei mitochondria"]). MitoCarta SVM prediction [PMID:20660476 "We present a novel computational method for genome-wide prediction of mitochondrial proteins"].
- TrypTag (GO_REF:0000109) gave kinetoplast and cytoplasm calls. Cytoplasm in GO includes the mitochondrion, so it is true but uninformative; a cytosolic signal could also be an N-terminal-tag artefact masking the transit peptide. Kinetoplast (sub-mitochondrial region around kDNA) is plausible given editing of maxicircle transcripts but the core site is the mitochondrial matrix.
- Complex map: REL1 was the bait in a TEV-elution pulldown [PMID:26991453 "TEV-elusion pull down of REL1 protein."]; [PMID:26991453 "17 are known to be involved in the core editosome complex"].

## Curation decisions (summary)
- Ligase activity (IEA) -> MODIFY to RNA ligase (ATP) activity GO:0003972 (already present; experimentally supported).
- RNA modification (IDA, IEA) -> MODIFY to mitochondrial mRNA modification GO:0080156 (OLS-verified; child of mRNA modification and mitochondrial RNA modification). GO merged "RNA editing" into "RNA modification"; U-insertion/deletion editing has no dedicated term.
- Cytoplasm (TrypTag IDA) -> MODIFY to mitochondrion.
- Editosome GO:0031019, mitochondrion, RNA ligase (ATP) activity -> ACCEPT. Kinetoplast -> KEEP_AS_NON_CORE. ATP binding -> KEEP_AS_NON_CORE.
- Protist checks: no animal/plant-only terms; no host-process terms; no paralog over-annotation (REL1 vs REL2 subcomplex distinction is not represented in GO and needs no term).
