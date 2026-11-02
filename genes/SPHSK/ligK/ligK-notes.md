# ligK (G2IQQ8, Sphingobium sp. SYK-6) - curator notes

Deep research could not be run for this session; these notes were written by hand from the
cached publications and the UniProt record. No `-deep-research-*.md` file exists.

## Identity
- LigK = 4-carboxy-4-hydroxy-2-oxoadipate (CHA) aldolase / oxaloacetate decarboxylase,
  228 aa, LigK/PcmE family (TIGR02798; RraA-like fold, PF03737). PANTHER PTHR33254:SF16,
  the same subfamily as P. putida GalC (genes/PSEPK/galC).
- Strain name history: SYK-6 was originally *Sphingomonas paucimobilis* SYK-6, now
  *Sphingobium* sp. SYK-6.

## Function (experimental)
- CHA aldolase: [PMID:12486039 "This result indicated that LigK catalyzes the conversion of CHA to pyruvate and oxaloacetate."]
- Oxaloacetate decarboxylase (secondary): [PMID:12486039 "It is concluded that LigK is able to decarboxylate oxaloacetate to generate pyruvate."]
  The CHA reaction is much faster: [PMID:12486039 "The V max for CHA aldol cleavage (265 U/mg) is 20 times higher than that for oxaloacetate decarboxylation (13.2 U/mg)."]
- Metal dependence / class II aldolase: [PMID:12486039 "LigK was suggested to be one of the class II aldolases, which require the metal ion."]
- Oligomer: [PMID:12486039 "This result suggested that LigK is a homohexamer."]
- Product inhibition: [PMID:12486039 "CHA aldolase activity was inhibited by oxaloacetate with a K i value of 23 μM."]
- HMG formation from 2 pyruvate is attributed by UniProt to PMID:29658701 (abstract-only in cache; abstract does not mention LigK)
  [file:SPHSK/ligK/ligK-uniprot.txt "Is also able to catalyze the formation of 4-hydroxy-4-methyl-2-oxoglutarate (HMG) from two molecules of pyruvate"].

## Pathway role
- Terminal step of the PCA 4,5-cleavage pathway: [PMID:12486039 "Finally, CHA is cleaved by CHA aldolase to produce pyruvate and oxaloacetate."]
- Essential in vivo: [PMID:12486039 "The obtained mutant strain DLK completely lost the ability to grow on both vanillate and syringate."]
- Syringate-derived carbon (3-O-methylgallate, gallate) converges on OMA:
  [PMID:12486039 "In this alternative pathway, 3MGA was finally converted to OMA and then entered the PCA 4,5-cleavage pathway."]
  and DesB converts gallate to OMA [PMID:16030198 "DesB specifically attacked gallate to generate 4-oxalomesaconate as the reaction product."]
  Hence LigK also performs the last step of gallate catabolism in this organism (NEW GO:0019396),
  matching GalC's GO:0019396 in P. putida.
- Upstream sphingomonad route OMA -> KCH (LigU) -> CHA (LigJ):
  [PMID:29658701 "LigJ catalyzes the hydration of KCH to 4-carboxy-4-hydroxy-2-oxoadipate."]

## Curation decisions
- GO:0047443 (HMG aldolase; definition includes the CHA reaction) = core MF, ACCEPT all three rows.
- GO:0008948 oxaloacetate decarboxylase = real but secondary -> KEEP_AS_NON_CORE (both rows).
- GO:0019617 PCA meta-cleavage IDA = ACCEPT (core BP).
- GO:0046274 lignin catabolic process (UniPathway IEA) = KEEP_AS_NON_CORE (acts on lignin-monomer-derived
  intermediates, not the polymer).
- Proposed CHA-specific aldolase term (same proposed_name as galC review).
