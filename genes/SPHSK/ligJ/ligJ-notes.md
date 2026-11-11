# ligJ (G2IQQ5, Sphingobium sp. SYK-6) - curator notes

Deep research could not be run for this session; these notes were written by hand from the
cached publications and the UniProt record. No `-deep-research-*.md` file exists.

## Identity
- LigJ, 341 aa, amidohydrolase superfamily (cog2159; Pfam PF04909 Amidohydro_2; PANTHER
  PTHR21240 ACMSD-like), zinc-dependent hydratase. Originally named 4-oxalomesaconate (OMA)
  hydratase; now known to act on (3Z)-2-keto-4-carboxy-3-hexenedioate (KCH), the product of LigU.
- Not homologous to the P. putida GalB OMA hydratase (genes/PSEPK/galB), which is the
  founding member of a distinct zinc hydratase family; the two are analogous enzymes for
  the equivalent pathway step.

## Function
- Original assignment (2000): [PMID:11092855 "we found the ligJ gene encoding 4-oxalomesaconate (OMA) hydratase, which catalyzes the conversion of OMA into 4-carboxy-4-hydroxy-2-oxoadipate."]
  The OMA substrate preparation used was a tautomer/isomer mixture:
  [PMID:11092855 "Thus, the OMA preparation contains the two isomeric enol forms and the keto form as shown in Fig. 1 ."]
- Refined substrate (2018): [PMID:29658701 "We have also shown that the product of the LigU-catalyzed reaction is the preferred substrate for the LigJ hydratase."]
  and [PMID:29658701 "LigJ catalyzes the hydration of KCH to 4-carboxy-4-hydroxy-2-oxoadipate."]
- Structure/mechanism: [PMID:30207699 "a single zinc ion is bound in the active site at the C-terminal end of the central β-barrel"];
  Glu-284 general acid/base; [PMID:30207699 "The E284Q mutant was unable to catalyze the hydration of KCH to CHA"].
  Product stereochemistry 4S.
- Homodimer: [PMID:11092855 "This result suggested that LigJ is a homodimer."]
- UniProt reaction: RHEA:58508, EC 4.2.1.- (no EC number assigned to the KCH reaction yet;
  BRENDA files LigJ under EC 4.2.1.83).

## GO term availability
- GO:0047584 "4-oxalmesaconate hydratase activity" is defined on (1E)-4-oxobut-1-ene-1,2,4-tricarboxylate
  (OMA, the LigU substrate; RHEA:17401), i.e. the GalB reaction, not the KCH reaction.
  OLS/QuickGO searches for "hexenedioate", "oxalomesaconate" and the KCH reaction found no term.
  Hence a new term is proposed: "2-keto-4-carboxy-3-hexenedioate hydratase activity"
  (RHEA:58508; parent GO:0016836 hydro-lyase activity), and GO:0016836 is added as NEW.

## Pathway / in vivo
- [PMID:11092855 "The mutant strain DLJ obtained completely lost the ability to grow on both vanillate and syringate."]
- [PMID:11092855 "These results indicated that syringate is converted into OMA via 3MGA, and it enters the PCA 4,5-cleavage pathway."]
- Gallate branch: [PMID:16030198 "DesB specifically attacked gallate to generate 4-oxalomesaconate as the reaction product."]
  So LigJ catalyses a step of both PCA meta-cleavage and gallate catabolism (NEW GO:0019617 and GO:0019396).

## Curation decisions
- hydrolase activity (InterPro2GO, amidohydrolase superfamily): REMOVE - LigJ adds water across a C=C bond
  (a lyase/hydratase, EC 4.2.1), it does not hydrolyse a bond.
- carboxy-lyase activity (InterPro2GO, ACMSD family IPR032465): REMOVE - no decarboxylation; the
  ACMSD-family mapping is an over-propagation of the decarboxylase subfamilies' activity.
- secondary metabolic process (TreeGrafter): MODIFY -> lignin catabolic process (its descendant, already on the gene).
- lignin catabolic process (UniPathway): KEEP_AS_NON_CORE.
- cytoplasm (TreeGrafter): KEEP_AS_NON_CORE (soluble enzyme; no direct localization study).
