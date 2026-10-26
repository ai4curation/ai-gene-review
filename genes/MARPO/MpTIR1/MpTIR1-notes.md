# MpTIR1 review notes


## Auxin receptor audit, 2026-10-26

Every original annotation row was assessed; source/evidence/qualifier/term payloads are preserved against `.cache/module-audit-logs/auxin-panel-baseline.json`. No assigned target has a negated original row. Current Falcon requests failed authentication, and the Perplexity-lite fallback returned 401 insufficient quota (logs in `.cache/module-audit-logs/auxin-fetch/`). No provider report was fabricated. Manual research used primary publications and curated sequence/family records; previous valid reports remain discovery aids.

Actual PANTHER IBD assertions were inspected in `interpro/panther/PTHR16134/PTHR16134-paint.tsv`: PTN008357904 supplies Embryophyta auxin-receptor/signaling assertions; PTN009029653 supplies older F-box SCF/adaptor/proteolysis assertions. The latter's mixed donor taxa do not transfer auxin specificity. A target in its own descendant evidence is expected, not circular support. The broad official family label is F-BOX/TPR REPEAT PROTEIN POF3; its name does not restrict the verified receptor subfamilies to Pof3-like physiology.

A separate annotation-reviewer consultation agreed that integral cofactor binding is core, that SCF substrate recruitment differs from independent ubiquitin-transfer catalysis, that nuclear imaging does not exclude vacuolar residence, and that AC activity must distinguish assayed receptor/construct from family inference.

Identity is A0A0K2QW32, UniProt locus MARPO_0035s0062 and Gramene Mp6g02750.1, matching the exact accession section of PMID36529527 (Mp6g02750/Mapoly0035s0062). PANTHER placement PTHR16134:SF148 is verified from UniProt; its surprising official label S-PHASE KINASE-ASSOCIATED PROTEIN 2, ISOFORM A is not a reason to guess a different family or transfer mammalian cell-cycle function.

All five original IBA claims are ACCEPT with native corroboration and explicit phylogenetic boundaries. Full PMID36529527 Fig2A/B uses plant-expressed MpTIR1-3xFLAG and E. coli-expressed C-terminal MpIAA fragments: “The MpTIR1-3xFLAG proteins showed interactions with MpIAA only when auxin was added to the mixture.” Auxin dose dependence and the MpIAA DII mutation support receptor/adaptor specificity. Fig2C/D shows stabilization of the DII reporter after conditional MpTIR1 loss. This directly supports native turnover but is not a reconstituted ubiquitination/proteasome assay. Full native SCF composition remains a conserved architectural/PAINT inference; no direct native SKP1/CUL1 copurification is claimed.

A complementing native-promoter MpTIR1-tdTomato fusion accumulates “at nucleus-like regions in most of the sporeling cells soon after germination” (text describing Supplemental Fig14), rather than relying on the separately NLS-tagged DII reporter. Nuclear localization is described with the authors' resolution; no NEW location term was needed. Knockouts survive as cell masses while losing normal organogenesis. Thus the native result does not support a universal requirement for cell viability or angiosperm-specific organ programs. Auxin-induced and auxin-repressed transcripts both occur; receptor activation does not imply all downstream genes are positively regulated.

No NEW AC activity. The discussion explicitly says “It would be interesting to examine whether MpTIR1 has adenylate cyclase activity.” Arabidopsis and Physcomitrium results do not become a measured Marchantia capacity. Suggested experiments retain this as an open question.
