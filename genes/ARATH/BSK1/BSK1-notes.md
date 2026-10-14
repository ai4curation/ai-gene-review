# BSK1 (At4g35230, UniProtKB:Q944A7) curation notes

Session 2026-10-05/06 (brassinosteroid_signaling module curation).

- Identity checked: BSK1_ARATH, Q944A7.
- Falcon deep research attempted; HTTP 402, no report.
- BRI1 substrate [PMID:18653891 "The BSKs are phosphorylated by BRI1 in vitro and interact with BRI1 in vivo."]
- Relay to BSU1 [PMID:19734888 "phosphorylation of BSK1 (BR-signalling kinase 1) by the BR receptor kinase BRI1 (BR-insensitive 1) promotes BSK1 binding to the BSU1 (BRI1 suppressor 1) phosphatase"]; but no direct activation of BSU1 in vitro [PMID:19734888 "we did not detect an effect of BSK1 on BSU1 activity in vitro"].
- Kinase vs pseudokinase: BSK1 kinase activity in vitro, required for immune function [PMID:23532072 "displays kinase activity in vitro; this kinase activity is required for its function"]; BSK8 structure suggests pseudokinase [PMID:23911552 "BSKs represent constitutively inactive protein kinases"]. Kinase MF annotations accepted with caveat; no "phosphatase activator" MF proposed because activation not reconstituted in vitro.
- Immunity: FLS2 association, PTI [PMID:23532072] -> non-core.
- PM targeting by S-acylation [PMID:38315835].
- Protein binding IPIs: kinase partners -> MODIFY to GO:0019901; BSK paralogs/PATs -> REMOVE (uninformative).
