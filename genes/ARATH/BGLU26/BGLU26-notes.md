# BGLU26 / PEN2 (At2g44490, UniProt O64883) – curation notes

## Sources used
- UniProt O64883 (GH1 family; EC 3.2.1.21 given, not EC 3.2.1.147).
- Falcon deep research (`BGLU26-deep-research-falcon.md`).
- Cached papers: PMID:16293760 (Lipka 2005, abstract only), PMID:19095900 (Bednarek 2009, abstract only),
  PMID:19095898 (Clay 2009, full text), PMID:26721862 (Fuchs 2016, abstract only; newly cached),
  PMID:20605856 (Hiruma 2010, full text; newly cached), PMID:23073694 (van de Mortel 2012), PMID:12938931 (Froehlich 2003, abstract only).
- PMIDs for Fuchs 2016 and Hiruma 2010 were resolved with the PubMed citation lookup tool.

## Journal
- Identity: PEN2 = BGLU26 = At2g44490. GH1 glycoside hydrolase, catalytic Glu183/Glu398 (UniProt ACT_SITE).
- Activity: atypical myrosinase. [PMID:19095900 "activated by the atypical PEN2 myrosinase (a type of beta-thioglucoside glucohydrolase) for antifungal defense"].
  Substrates I3G and 4MO-I3G (UniProt FUNCTION, kinetics: Km 722 uM I3G, Vmax 7.5 umol/min/mg; 4MUG Km 150 uM, Vmax 0.76).
- Key point for MF annotation: the O-glucosidase (4MUG) activity is real in vitro but separable from function:
  [file:ARATH/BGLU26/BGLU26-deep-research-falcon.md "Replacing catalytic Glu183 with Asp eliminated detectable I3G hydrolysis while retaining 4MUG hydrolysis"]
  and the E183D variant does not complement pen2. So beta-glucosidase activity (GO:0008422) is non-core; thioglucosidase activity (GO:0019137) is core.
- No cellulase term is present in GOA for this gene; the generic IEA rows are GO:0004553 (InterPro GH1) and GO:0008422 (EC 3.2.1.21 mapping), plus carbohydrate metabolic process (InterPro).
  The EC mapping follows from UniProt using EC 3.2.1.21 instead of the myrosinase EC 3.2.1.147.
- Localisation: originally peroxisome [PMID:16293760 "The PEN2 glycosyl hydrolase localizes to peroxisomes"]; later shown tail-anchored on peroxisomes AND mitochondria
  [PMID:26721862 "PEN2 is a tail-anchored protein with dual-membrane targeting to peroxisomes and mitochondria"], and mitochondrial outer membrane alone is sufficient
  [PMID:26721862 "Exclusive targeting of PEN2 to the outer membrane of mitochondria complements the pen2 mutant phenotype"].
- Chloroplast envelope (HDA, PMID:12938931) comes from "mixed" envelope proteomics; inconsistent with targeted studies, likely co-purifying organelle membranes.
- Defense: pre-invasion nonhost resistance to powdery mildews [PMID:16293760 "PEN2 restricts pathogen entry of two ascomycete powdery mildew fungi"];
  also Colletotrichum [PMID:20605856 "thereby demonstrating the involvement of PEN2 in nonhost resistance to this pathogen"].
- flg22 callose: [PMID:19095898 "Both pen2-1 and pen2-2 mutants exhibited a loss of the callose response to Flg22"] – PEN2 acts upstream (its products as signal/co-activator); it does not deposit callose.
- Bacteria: [PMID:19095898 "the IGS hydrolytic mutant pen2-1 are slightly but significantly more susceptible to wild-type PtoDC3000"] – minor, non-core.
- ISR (Pf.SS101): pen2 among mutants that lost induced resistance [PMID:23073694 "required for the induction of Pst resistance by Pf .SS101"]. Non-core, upstream.
- Salt stress IBA comes from AT1G66270/AT1G66280 (BGLU21/BGLU22, ER-body myrosinase-like enzymes); no PEN2 evidence and PEN2 is not an ER-body protein. Over-propagation.

## Project curation question 3 (necessity vs participation)
- `defense response to fungus` is justified: PEN2 catalyses the hydrolysis step that generates the antifungal indole-glucosinolate products at the entry site; this is participation (catalysis), not mere necessity.
  The more mechanistic term is `indole glucosinolate catabolic process` (GO:0042344), which is the core process; `glucosinolate metabolic process` IMP should be refined to it.
- Callose deposition, response to bacterium and ISR are upstream/necessity phenotypes -> non-core.
