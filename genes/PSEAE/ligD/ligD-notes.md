# ligD manual review

Reviewed 13 ordered source annotations; no new rows or retirements. Raw UniProt, GOA and seed snapshots remain unchanged.

The exact target descends from its seeded IBD node in the official PANTHER tree. Broad family membership is not a grant of every LigD domain, primase process, or partner interaction. No donor-count or self-source objection is used.

GO:0045027 DNA-end binding is a distinct branch from duplex-binding3690; both describe real Ku properties. GO:0140078 captures AP beta-lyase cleavage; GO:0051575 captures terminal5′-dRP elimination. These are distinct from PE-mediated3′phosphatase0046403. No BER process NEW is inferred from necessity or a purified reconstitution.

Primase-process IBA GO:0006269 is ACCEPT: its definition explicitly includes DNA-damage priming, the exact target inherits PTN001627042, and no target-specific catalytic loss is established. A lack of direct target de novo assays is not evidence against this inference. The native conditions of use remain a legitimate question.

PAO1 target evidence is kept separate from PA14 LigD-independent NHEJ in PMID:42306942. The latter is not a PAO1 deletion experiment. Ku-(1–253) end protection, full-length stimulation and other truncation assays are distinguished in PMID:20018881. PMID:25355514 explicitly clones Ku from PAO-1 genomic DNA.

The recent Mycobacterium POL-regulation result PMID:42953966 is not transferred as a universal sign to these proteins. The shared Falcon authentication failure is documented in the prior session; this file is manual synthesis, not a fabricated provider report.

- PMID:15520014: Abstract-only positive biochemical evidence for purified P. aeruginosa LigD polymerase and ATP-ligase domains. No negative conclusion about an unexamined primase assay is drawn.
- PMID:15897197: Abstract-only direct P. aeruginosa LigD terminal-ribonucleotide resection evidence. The preferred substrate is a DNA primer bearing a short 3′ ribonucleotide tract, not bulk cellular RNA. Sequential nucleoside removal and 3′-phosphate hydrolysis are distinguished.
- PMID:16046407: Abstract explicitly reports P. aeruginosa LigD phosphatase activity on an all-DNA primer-template. This supports the DNA substrate in GO:0046403; RNA-terminal phosphatase activity alone would not establish it. Full Figure5 was not independently inspected here.
- PMID:20018881: Full primary text: recombinant P. aeruginosa Ku/LigD, DNA gap filling with dNTPs, and Ku stimulation of LigD. End protection used Ku-(1–253); full-length and other truncations were separately tested. This is not a native PA14 or KT2440 assay.
- PMID:26826709: Full primary biochemistry directly tests Bacillus LigD dCTP gap filling and 5′-dRP lyase, and confirms 5′-dRP lyase in purified P. aeruginosa LigD. Native Bacillus strain168-derived spore experiments suggest overlapping repair with Nfo but do not alone prove the proposed full BER role.

Final RNA-chemistry scope: GO:0003887 core is restricted to dNTP incorporation. PAO1 PMID:20018881 shows multiple templated rNMP additions and rNTP gap closure, supporting GO:0003899 for extension of the nascent RNA tract. This is not a transcription claim. No NEW annotation row was added.

Recovery provenance (2026-11-07): reconstructed from the preserved historical curation helper and recorded final edits after deletion of the prior uncommitted worktree. Fresh seed bytes match the historical observed seeds; raw sources were reacquired by root and are frozen independently. Validation, renders and generated histories are new recovery outputs; the lost historical handoff is not recreated.


## 2026-11-08 — recovery PR review follow-up

Replace functional methods-only quotes with result statements; retain construct provenance in reference findings and notes. Separate measured AP/dRP lyase capabilities from unproven native process assignments. Original annotation payloads and raw-source files remain unchanged.
