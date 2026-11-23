# IRAK1 notes

## Literature search (2026-11-04)

No deep-research provider was available. Sources checked:

- All GOA-cited publications, cached with `just fetch-gene-pmids human IRAK1` (36 papers).
- PubMed E-utilities searches: "Mutant cells that do not respond to interleukin-1 reveal a novel
  role for IL-1 receptor-associated kinase" (found PMID:10373513), "Knop J[au] AND IRAK[ti]"
  (PMID:10217414), "Maschera B[au] AND IRAK" (PMID:10191251), "Kollewe C[au] AND IRAK"
  (PMID:14625308), "IRAK1 kinase-inactive knock-in mice" (PMID:20599782, a review).
- UniProt FUNCTION references fetched: PMID:15767370, 14684752, 15084582, 17997719, 20400509,
  16690127, 18347055; Myddosome structure PMID:20485341; MYD88 recruitment PMID:9430229.
- Web search for "IRAK1 kinase activity dispensable IL-1 signaling kinase-dead" (returned the same
  primary papers plus later mouse knock-in reports on TLR7/9-driven IFN-alpha).

## Kinase versus scaffold

IRAK1 is a catalytically active Ser/Thr kinase (Pelle subfamily of TKL kinases).

- Sequential autophosphorylation: [PMID:14625308 "First, IRAK-1 is phosphorylated at Thr209."]
  and [PMID:14625308 "Second, Thr387 in the activation loop is phosphorylated, leading to full enzymatic activity."]
- Of the IRAKs only IRAK1 and IRAK4 retain the catalytic motifs:
  [PMID:33238146 "IRAK1 and IRAK4 are catalytically active members of the IRAK family"].
- Substrates: Pellino E3 ligases [PMID:17997719 "we demonstrate that IRAK1 and IRAK4 phosphorylate Pellino isoforms in vitro and that phosphorylation greatly enhances Pellino's E3 ubiquitin ligase activity"];
  IRF7 [PMID:15767370 "IRAK-1 directly bound and phosphorylated IRF7 in vitro."];
  TIRAP/Mal [PMID:20400509 "We have found that both IRAK1 and IRAK4 can directly phosphorylate Mal."].

But for IL-1 to NF-kappaB/JNK, the catalytic activity is dispensable:

- [PMID:10373513 "IRAK-K239A was still phosphorylated upon IL-1 stimulation and, surprisingly, still complemented all the defects in the mutant cells."]
- [PMID:10217414 "This strongly suggests that the intrinsic kinase activity is not required for downstream signaling via IRAK."]
- [PMID:10191251 "suggesting that the kinase activity of IRAK is not required outside of the IL-1R complex"]
- Redundancy with IRAK4: [PMID:15084582 "only the impairment of the kinase activity of both IRAK and IRAK4 efficiently abolished the IL-1 pathway"].
- Scaffold/organizer: [PMID:12242293 "functioning as an organizer and transporter in IL-1-dependent signaling"];
  autophosphorylation regulates release: [PMID:14625308 "Thus, IRAK-1 regulates its own availability as an adapter molecule by sequential autophosphorylation."]
- K63-ubiquitinated IRAK1 recruits NEMO: [PMID:18347055 "only ubiquitinated IRAK-1 bound NEMO, the regulatory subunit of IkappaB kinase (IKK)"].

Kinase activity is required in the TLR7/9-IRF7 branch:
[PMID:15767370 "The kinase activity of IRAK-1 was necessary for transcriptional activation of IRF7."]
and [PMID:15767370 "TLR7- and TLR9-mediated IFN-alpha production was abolished in Irak-1-deficient mice, whereas inflammatory cytokine production was not impaired."]

Conclusion: IRAK1 has two separable core activities — (1) a signalling scaffold that links the
Myddosome to TRAF6 (and, once K63-ubiquitinated, to NEMO), for which catalysis is largely
dispensable in IL-1/TLR NF-kappaB signalling and is redundant with IRAK4 and IRAK2; and (2)
protein Ser/Thr kinase activity that is required for IRF7 activation in pDCs and acts on Pellino,
Mal and itself. Both are kept as core. This refines the IL-1 module's knowledge gap: the data
argue the IL-1 step is scaffold-typed, while the kinase is essential in TLR7/9-IRF7.

## Redundancy with IRAK2

[PMID:38961291 "IRAK1 and IRAK2 appeared to be redundant, as double (but not single) knockouts abolished all responses to LPS"].

## Location

Cytoplasm/cytosol, receptor-proximal membrane complex in IL-1 signalling
[PMID:22851693 "It is important to note that the modified IRAK1 is always membrane associated and detected in membrane-bound receptor complex I and II (IRAK-TRAF6-TAK1-TAB2-TAB3)."];
nucleus when sumoylated [PMID:16690127 "IRAK1 could also undergo sumoylation which was responsible for its translocation into the nucleus"].

## Inflammasome

Review PMID:36865541 discusses IRAK1 in rapid (non-transcriptional) NLRP3 priming, with
conflicting positive and negative roles: [PMID:36865541 "While IRAK1 appears to stimulate NLRP3 activity in the context of rapid inflammasome activation, it can also act as a negative regulator in other conditions."]

## Not run

`just paint-losses human IRAK1` was killed (out of memory) when the container restarted; IBA rows
were judged on biology without it.
