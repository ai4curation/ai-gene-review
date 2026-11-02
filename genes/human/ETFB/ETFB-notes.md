# ETFB (P38117) review notes

## Identity / core biology
ETFB is the **beta subunit of the electron-transfer flavoprotein (ETF)**, a soluble
mitochondrial-matrix FAD-containing heterodimer (ETFA + ETFB). ETF is the common
electron acceptor for the matrix FAD-dependent acyl-CoA dehydrogenases (fatty-acid
beta-oxidation and amino-acid catabolism), relaying electrons to ETF-ubiquinone
oxidoreductase (ETFDH) and thence to the respiratory-chain ubiquinone pool.

Supporting text:
- [file:UniProt P38117 FUNCTION "Heterodimeric electron transfer flavoprotein that accepts electrons from several mitochondrial dehydrogenases, including acyl-CoA dehydrogenases, glutaryl-CoA and sarcosine dehydrogenase"]
- [file:UniProt P38117 FUNCTION "It transfers the electrons to the main mitochondrial respiratory chain via ETF-ubiquinone oxidoreductase"]
- [PMID:8962055 abstract "They function as electron shuttles between primary flavoprotein dehydrogenases involved in mitochondrial fatty acid and amino acid catabolism and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase."]
- [PMID:25416781 "ETF acts as a mobile electron carrier that shuttles electrons between several FAD-containing dehydrogenases present in the mitochondrial matrix and the membrane-bound ETF:quinone oxidoreductase"]
- [PMID:25416781 "in addition to complexes I and II, it is the third major provider of electrons to the ubiquinone pool of the mitochondrial respiratory chain"]

## Structure / domain / role of beta subunit
- Heterodimer: two domains from alpha, third domain entirely from beta; FAD lies in a cleft
  between subunits, mostly in the C-terminal portion of alpha [PMID:8962055].
- ETFB binds an AMP molecule that probably has a purely structural role
  [file:UniProt FUNCTION].
- **Recognition loop** (residues 183-205; ~191-200 in older numbering) at the surface of ETFB
  recognizes a hydrophobic patch on interacting dehydrogenases and acts as a static anchor
  [file:UniProt DOMAIN "The recognition loop recognizes a hydrophobic patch at the surface of interacting dehydrogenases and acts as a static anchor at the interface."].
- L195A severely impairs complex formation with ACADM (MCAD) [file:UniProt MUTAGEN 195].

## Localization
- Mitochondrial matrix. UniProt SUBCELLULAR LOCATION: "Mitochondrion matrix".
- Imported into matrix; unusual in lacking a cleavable leader peptide; energy-dependent import
  [PMID:8504797 "the cDNA-encoded beta-ETF polypeptide contains the information necessary to reach the mitochondrial matrix"].
- Reactome notes ETF resides on the matrix face of the mitochondrial inner membrane [R-HSA-169260].
- HPA IDA (GO_REF:0000052) and HTP mito proteome (PMID:34800366) both mitochondrion.

## Complex
- Part of the mitochondrial electron transfer flavoprotein complex (ETFA/ETFB heterodimer;
  ComplexPortal CPX-2731); GO:0045251 IPI from PMID:8962055 crystal structure.

## Regulation / PTM
- ETFBKMT (METTL20) trimethylates Lys-200 and Lys-203, adjacent to the recognition loop,
  reducing ETFB's ability to receive electrons from MCAD and GCDH [PMID:25416781].
- MBTPS1/S1P forms a trimeric complex with ETFA/ETFB, stabilizing the heterodimer and
  promoting FAD binding (flavination) [PMID:35362222 "S1P forms a trimeric complex with ETFA/ETFB. S1P enhances ETFA/ETFB flavination and maintains its stability."].
- ETFRF1 (LYRM5) is a "deflavinase" that removes FAD from ETF [PMID:27499296].

## Disease
- Biallelic ETFB variants cause **multiple acyl-CoA dehydrogenase deficiency (MADD) /
  glutaric acidemia type II (GA2B, MIM:231680)** [file:UniProt DISEASE; PMID:7912128;
  PMID:12815589]. GA2B variants D128N (decreased stability) and R164Q (reduced electron
  transfer activity).

## Annotation review decisions summary
- MF electron transfer activity (GO:0009055): CORE. Multiple IDA/TAS/IBA/IEA -> ACCEPT (one core, rest accept).
- BP fatty acid beta-oxidation using acyl-CoA dehydrogenase (GO:0033539): CORE (IDA/IBA/IEA) -> ACCEPT.
- BP amino acid catabolic process (GO:0009063): supported (dehydrogenases in aa catabolism) -> ACCEPT.
- BP respiratory electron transport chain (GO:0022904): supported (feeds ubiquinone pool) -> ACCEPT.
- CC mitochondrial matrix (GO:0005759): CORE location -> ACCEPT.
- CC mitochondrion (GO:0005739): broader; ACCEPT / KEEP_AS_NON_CORE (matrix is more precise).
- CC electron transfer flavoprotein complex (GO:0045251): CORE complex -> ACCEPT.
- protein binding (GO:0005515) IPIs x5: bare protein binding, uninformative -> MARK_AS_OVER_ANNOTATED
  (do NOT REMOVE experimental IPIs per policy). WITH/FROM: ETFA (P13804), ETFRF1 (Q6IPR1),
  MBTPS1 via PMID:35362222 (P13804|Q14703). These are real interactions but the GO term itself
  is uninformative.

## Deep research
falcon DR file not present within poll window; grounded in UniProt, cached PMIDs, Reactome,
and the MADD disorder KB.


## 2026-10-24 — Current source review and preserved history

All 27 current source contexts are reviewed: 18 ACCEPT, six MODIFY and three KEEP_AS_NON_CORE. The 25 inherited positions remain fixed. One historical ARBA mitochondrion context is absent from the current source; it remains at index 3 as retired with a supported biological MODIFY to matrix. Retirement records source absence, not functional loss. There are 28 total rows and no NEW annotation.

Two formerly aggregated interaction contexts are split without moving quotations. Legacy index 6 retains LYRM5, the partner named in its fixed quotation, while the ETFA context is appended. Legacy index 7 retains the ETFA context with its general BioPlex quotation, and LYRM5 is appended separately. The current ARBA ETF-complex assertion is also appended. Every current source object has one exact active representation; missing supporting_entities are added only from the captured current context, with every existing source value preserved.

All 41 inherited quotation paths, values and reference associations remain fixed (27 annotation, four core and ten reference-finding anchors). Accepted evidence references are appended after existing support prefixes. Thirteen references receive the accepted access assessments, replacing obsolete generic-binding over-annotation commentary; overlapping source scopes are separately labeled. Existing reference identities, titles, order and findings remain unchanged. The two ordered cores, description, natural products and INITIALIZED status are retained for a later synthesis phase.

The source guide records the human alpha/beta carrier assays, the different BioPlex accession labels, grouped MitoCoP products and remaining old-original access limits. Inherited description/core recognition-loop wording and the S1P trimer finding remain synthesis follow-up items: accepted original evidence distinguishes predicted docking and co-IP from an obligate third ETF subunit. Their inherited text/quotes are preserved at this checkpoint, not newly endorsed as expanded mechanistic proof.


## 2026-10-24 — ETFB contribution to electron transfer

ETFB supplies an AMP-binding domain and part of the architecture surrounding the single FAD of assembled ETF. The human structure resolves beta density from Leu4 to Ile255 and places AMP within beta domain III; its stabilizing role is a structural interpretation, not AMP turnover (https://doi.org/10.1073/pnas.93.25.14355, Results cofactor sites). In the human reconstitution, mature untagged Δ19-alpha pairs with full-length His6-beta and transfers electrons from MCAD or GCDH to DCIP. ETFDH performs the distinct downstream ubiquinone-reduction reaction (https://doi.org/10.1074/jbc.M114.614115, Experimental Procedures and Figure 5).

The recognition-loop role remains supported: the human ETF–MCAD structure reports a static anchor coupled to a mobile FAD domain, and beta-E165A changes donor-transfer kinetics (https://doi.org/10.1074/jbc.M404884200; https://doi.org/10.1074/jbc.M505562200). These two papers were available as original abstracts with verified identifiers; publisher body/PDF access failed, so their detailed Methods and product sequences were not independently inspected. This positive but bounded evidence does not establish identical docking for all donors or the 346-residue product. The two inherited core positions now describe facets of the same assembled carrier activity, with electron transfer recorded as a contribution to the complex.

The S1P finding now distinguishes human-cell co-IP/GST association and ETF stability/flavination effects from the proposed computational trimer (https://doi.org/10.15252/emmm.202114904, Results/Figure 3 and docking Methods). The inherited quotation is retained exactly. It does not establish that S1P is an obligatory third subunit of every functional ETF complex. Product-resolved import, donor-specific methylation effects and S1P occupancy remain useful experimental questions.

Final canonical validation passes all six checks, with all 65 authored narratives present in the private rendering. Computed DRAFT retains 3 advisories. The 28 source/review objects comprise 27 current contexts and one explicitly retired historical context. All 41 inherited quotation paths, texts and reference associations, two natural products and two ordered core slots remain preserved. The two cores describe contributions to assembled ETF; no autonomous beta turnover is asserted. All 20 selected normal sources, the 33 private source files and eight unrelated baseline files remain unchanged.


## 2026-10-24 — Structured AMP binding and amino-acid-catabolism context

The human ETF structure places AMP within beta-subunit domain III (PMID:8962055, Results, “AMP Binding”). AMP binding is now explicit within the existing carrier core alongside the contribution to electron transfer. The proposed stabilizing role is kept distinct from an AMP catalytic reaction. The same unit now includes amino-acid catabolism, supported by the assembled human ETF/GCDH glutaryl-CoA-to-DCIP assay (PMID:25416781, Experimental Procedures, “Protein Expression and Purification” and “ETF Activity Assay”; Figure 5). The artificial acceptor and engineered alpha construct do not demonstrate isolated-beta activity or complete respiratory flux.

The [source guide](ETFB-source-guide.md#structured-core-and-curated-record-support) gives the preserved UniProt record’s AMP-contact, recognition-loop and heterodimer locators. No new quotations or annotation rows were added. The three supported generic-binding contexts remain non-core under the [project instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). Ordinary imported relation qualifiers are preserved; complex-level contribution is expressed in the core rather than recast as a source defect.

The retired ARBA mitochondrial context remains a historical review with its matrix refinement, not a requested edit to a current GOA assertion. Its retirement records source absence and does not imply loss of mitochondrial function. The inherited MitoCoP title quotation is retained as provenance; target-level support comes from the previously inspected workbook rows described in the source guide. Earlier dated journal entries and validation counts remain historical checkpoints. Current biological attribution and evidence-access limits are stated in this entry and the source guide.

The revised canonical review passes all six checks; all 65 narrative strings appear in the private rendering. Computed status is DRAFT with 4 advisories: three generic-binding non-core contexts and the supported AMP-binding core term absent from annotation rows under the no-NEW campaign scope. All 27 active contexts, one retired context, 21 original references, one added unchanged-record reference, two ordered cores and 41 inherited quotation anchors remain preserved. Normal source files and the prior history record remain unchanged.
