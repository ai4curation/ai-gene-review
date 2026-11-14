# ligd manual review

Reviewed 9 ordered source annotations; no new rows or retirements. Raw UniProt, GOA and seed snapshots remain unchanged.

The exact target descends from its seeded IBD node in the official PANTHER tree. Broad family membership is not a grant of every LigD domain, primase process, or partner interaction. No donor-count or self-source objection is used.

GO:0045027 DNA-end binding is a distinct branch from duplex-binding3690; both describe real Ku properties. GO:0140078 captures AP beta-lyase cleavage; GO:0051575 captures terminal5′-dRP elimination. These are distinct from PE-mediated3′phosphatase0046403. No BER process NEW is inferred from necessity or a purified reconstitution.

The seeded folder and UniProt primary symbol ligd are preserved. SubtiWiki uses ligD as the canonical display spelling; this is an alias/nomenclature difference, not a different gene or protein. No raw files were renamed.

Primase-process IBA GO:0006269 is ACCEPT: its definition explicitly includes DNA-damage priming, the exact target inherits PTN001627042, and no target-specific catalytic loss is established. A lack of direct target de novo assays is not evidence against this inference. The native conditions of use remain a legitimate question.

Bacillus LigD lacks the PE domain. PMID:41957403 and PMID:30976810 place LigDom at residues1–320 and PolDom C-terminal; the immutable UniProt similarity-section N/C order is reversed and is not used as architectural evidence. PMID:41957403 uses Ku beginning at the annotated strain168 position18, expressed in E.coli with a His tag; native damage protection is separately supported by PMID:17293412.

The recent Mycobacterium POL-regulation result PMID:42953966 is not transferred as a universal sign to these proteins. The shared Falcon authentication failure is documented in the prior session; this file is manual synthesis, not a fabricated provider report.

- PMID:17293412: Full primary uses Bacillus168-derived repair mutants and spores; it supports native Ku/LigD repair relevance under specified damaging treatments, not an isolated-enzyme activity or a universal essentiality claim.
- PMID:26826709: Full primary biochemistry directly tests Bacillus LigD dCTP gap filling and 5′-dRP lyase, and confirms 5′-dRP lyase in purified P. aeruginosa LigD. Native Bacillus strain168-derived spore experiments suggest overlapping repair with Nfo but do not alone prove the proposed full BER role.
- PMID:30976810: Full primary shows Bacillus LigD PolDom AP lyase at recessed5′ ends, borohydride-trapped intermediate and coupling to incoming-primer extension/ligation. AP processing is a beta-lyase mechanism despite its metal/nucleotide-dependent precatalytic arrangement. It is not PE-domain activity.
- PMID:41957403: Full primary text: recombinant B. subtilis LigD/Ku coordinates AP incision, ribonucleotide insertion and joining. KuBs corresponds to strain168 NP_389224.1 beginning at annotated position18; proteins/truncations/chimeras were expressed in E. coli. No native exact occupancy or universal cross-species interaction is inferred. The primary places LigDom N-terminal and PolDom C-terminal, contrary to reversed UniProt similarity-section prose.

Final RNA-chemistry scope: GO:0003887 core is restricted to dNTP incorporation. Bacillus PMID:41957403 directly shows template-selected single rNMP addition to a DNA3′ end. GO:0003899 requires extension of an RNA strand, so the more cautious supported nucleotidyltransferase genus GO:0016779 is used for this separate core. No NEW annotation row was added.

Recovery provenance (2026-11-07): reconstructed from the preserved historical curation helper and recorded final edits after deletion of the prior uncommitted worktree. Fresh seed bytes match the historical observed seeds; raw sources were reacquired by root and are frozen independently. Validation, renders and generated histories are new recovery outputs; the lost historical handoff is not recreated.


## 2026-11-08 — recovery PR review follow-up

Replace functional methods-only quotes with result statements; retain construct provenance in reference findings and notes. Original annotation payloads and raw-source files remain unchanged.


## 2026-11-08 — source-specific evidence follow-up

Strengthen ATP, duplex/end-binding and multistep rNMP-extension support where applicable; remove duplicate evidence entries. Explicit NEW MF proposals record measured AP/5′-dRP chemistry without assigning a general native BER process. Abstract-only PMID:17293412 is scoped to the quoted mutant-spore phenotype, with no unverified strain details. Original source annotation payloads are unchanged. See the evidence-followup-20261108 receipt for the exact file scope.
