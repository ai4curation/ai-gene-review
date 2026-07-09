# RPE (Ribulose-phosphate 3-epimerase, Q96AT9) — review notes

## Identity and function
- Human RPE, UniProt Q96AT9, HGNC:10293, gene ID 6120, chromosome 2.
- EC 5.1.3.1; catalyses the reversible epimerisation of D-ribulose 5-phosphate (RU5P)
  to D-xylulose 5-phosphate (XY5P).
  - UniProt FUNCTION: "Catalyzes the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate." [file:human/RPE/RPE-uniprot.txt]
  - CATALYTIC ACTIVITY: Reaction=D-ribulose 5-phosphate = D-xylulose 5-phosphate; Rhea:RHEA:13677; EC=5.1.3.1 [file:human/RPE/RPE-uniprot.txt]
- Enzyme of the **non-oxidative branch of the pentose phosphate pathway**. Together with
  ribose-5-phosphate isomerase (RPIA), it processes the ribulose-5-phosphate produced by
  the oxidative branch, generating the xylulose-5-phosphate and ribose-5-phosphate
  substrates used by transketolase and transaldolase.
  - PMID:20923965 abstract: "RPE functions in the PPP, catalyzing" the reversible conversion of RU5P to XY5P; "an important enzyme for cellular response against oxidative stress."

## Structure / mechanism / cofactor
- (β/α)8 TIM-barrel fold. PMID:20923965: human RPE "folds into a typical (β/α)(8)"
  "triosephosphate isomerase (TIM) barrel with a loop regulating access to the" active site.
- Metal-dependent: binds one divalent metal cation per subunit; active with Fe(2+),
  and probably Mn(2+), Zn(2+), Co(2+) (UniProt COFACTOR).
  PMID:20923965: human RPE "uses Fe(2+) for catalysis" and the structure reveals "an
  octahedrally coordinated Fe(2+) ion" buried in the active site.
- Active site residues Asp-37 (proton acceptor) and Asp-175 (proton donor) (UniProt ACT_SITE);
  metal coordinated by His-35, Asp-37, His-70, Asp-175 (UniProt BINDING "a divalent metal cation").
- Mutagenesis (PMID:20923965): S10A nearly abolishes activity; H35A/D37A/D175A nearly
  abolish / alter structure; L12A, M72A reduce activity ~50%.
- PDB: 3OVP, 3OVQ, 3OVR (in complex with Fe/RU5P/XY5P), 3QC3.

## Quaternary structure
- Homodimer. UniProt SUBUNIT: "Homodimer." (Ref.9 = JCSG structure).
- Reactome R-HSA-71303 / R-HSA-199803: active form is a homodimer (Spencer & Hopkinson 1980).
- GOA has GO:0042803 protein homodimerization activity (IPI, PMID:20923965, with self Q96AT9)
  and multiple GO:0042802 identical protein binding IPIs (self-interaction).

## Localisation
- Cytosolic. Reactome describes "Cytosolic ribulose-5-phosphate-3-epimerase (RPE)".
  GOA: GO:0005829 cytosol (IBA GO_Central; TAS Reactome x2). Consistent with a soluble
  cytosolic PPP enzyme.
- GO:0070062 extracellular exosome (HDA, PMID:23533145): from a shotgun proteomic survey
  of prostatic-secretion exosomes (~900 proteins). This is a bulk proteomic detection,
  not evidence of a functional extracellular localisation; over-annotation.

## Protein interactions (IPI annotations)
- GO:0005515 protein binding (IPI, PMID:32296183, partner UniProtKB:Q9H8W4 = PLEKHF2):
  a HuRI binary-interactome heterotypic PPI. UniProt INTERACTION confirms Q96AT9;Q9H8W4
  PLEKHF2 (NbExp=3). Bare "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED
  (per policy, not REMOVE; it is a real detected interaction but tells us nothing about
  molecular function).
- GO:0042802 identical protein binding (IPI x4: PMID:16189514, PMID:20923965,
  PMID:25416956, PMID:32296183; with self Q96AT9): all self-self interactions capturing
  the homodimer. Biologically real (RPE is a homodimer) but the informative MF term for
  the homodimer is GO:0042803 protein homodimerization activity. Keep the homodimerization
  one as core-relevant; the identical-protein-binding IPIs are lower-value duplicates
  (KEEP_AS_NON_CORE).

## Disease
- No well-established common Mendelian disease. MIM 180480 (gene). Included here for
  completeness of the non-oxidative PPP.

## Annotation-source cross-check (GOA)
- MF core: GO:0004750 D-ribulose-phosphate 3-epimerase activity — IDA (PMID:20923965),
  IBA (GO_REF:0000033), IEA (GO_REF:0000120 via EC 5.1.3.1 / RHEA:13677). Strongly supported → ACCEPT.
- GO:0016857 racemase and epimerase activity, acting on carbohydrates and derivatives
  (IEA, InterPro): parent/grouping term of GO:0004750; correct but less specific → MODIFY to GO:0004750.
- GO:0046872 metal ion binding (IBA + IDA PMID:20923965): correct (divalent cation per subunit) → ACCEPT.
- BP: GO:0009052 non-oxidative branch (IBA), GO:0006098 pentose-phosphate shunt (IDA + IEA),
  GO:0005975 carbohydrate metabolic process (IBA + IEA). All correct; 0009052 is the most
  specific and precise for RPE. 0005975 is a broad grandparent → KEEP_AS_NON_CORE.
</content>
