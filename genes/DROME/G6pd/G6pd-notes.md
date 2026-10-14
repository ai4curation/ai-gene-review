# G6pd notes

- 2026-10-09: Initial review of G6pd (Zw; P12646, Swiss-Prot), cytosolic glucose-6-phosphate
  dehydrogenase.
- SIK3: "SIK3 controls NADP+ reduction by phosphorylating and activating Glucose-6-phosphate
  dehydrogenase (G6PD), the rate-limiting enzyme of the pentose phosphate pathway." [PMID:28132818]
- Overexpression: "The G6PD enzymatic activity was increased, as were the levels of NADPH, NADH, and
  the GSH/GSSG ratio." [PMID:18809674]
- Allozymes: "The three forms of G6PD are characterized by different apparent Km values for
  glucose-6-phosphate but similar apparent Km values for NAPD+." [PMID:6422927]
- PMID:4149211 (Geer 1974) and PMID:38739777 are title/abstract-only; experimental rows accepted in
  deference to curators.
- Generic process rows (glucose metabolic process, PPP, G6P metabolic process) MODIFY -> oxidative
  PPP (GO:0009051); NADP+ metabolic process -> NADPH regeneration (module-wide convention).
- Falcon deep research (G6pd-deep-research-falcon.md, arrived after initial commit): classic
  fractionation found all G6PD activity in the 105,000 x g supernatant (supports cytosol); Zw-deficient
  adults retain <10% activity and block the oxidative shunt; hemocyte Zw RNAi reduces lamellocyte
  responses to parasitoids; neuronal G6PD affects sleep and is induced by JNK signalling. No
  annotation changes (consistent with existing decisions).
