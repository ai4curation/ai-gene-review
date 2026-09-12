# ETFDH (human, UniProtKB:Q16134) — review notes

## Summary of gene function

ETFDH encodes **electron transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO / ETF
dehydrogenase; EC 1.5.5.1)**, a monotopic iron-sulfur flavoprotein of the mitochondrial
**inner membrane**. It accepts electrons from reduced electron-transfer flavoprotein (ETF,
the matrix-soluble ETFA/ETFB heterodimer) and transfers them to **ubiquinone** in the
respiratory chain. This is the terminal step of an electron-transfer relay that couples
~10-11 mitochondrial FAD-dependent flavoprotein dehydrogenases (fatty-acid beta-oxidation
acyl-CoA dehydrogenases; amino-acid and choline catabolism dehydrogenases) to oxidative
phosphorylation.

Cofactors: one **FAD** and one **[4Fe-4S] cluster**; both redox centers are in a 64-kDa
mature monomer.

## Key provenance

- Reaction / linkage to respiratory chain:
  [file:UniProt Q16134 FUNCTION "Links fatty acid beta-oxidation and amino acid catabolism to the respiratory chain by transferring electrons from the electron transfer flavoprotein (ETF) to ubiquinone."]
- Inner membrane localization & mechanism (both cofactors in 64-kDa monomer):
  [PMID:8306995 "Electron-transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO) in the inner mitochondrial membrane accepts electrons from electron-transfer flavoprotein which is located in the mitochondrial matrix and reduces ubiquinone in the mitochondrial membrane. The two redox centers in the protein, FAD and a [4Fe4S]+2,+1 cluster, are present in a 64-kDa monomer."]
- Component of electron-transfer system linking 10 dehydrogenases to bc1:
  [PMID:12049629 "Electron transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO) is an iron-sulphur flavoprotein and a component of an electron-transfer system that links 10 different mitochondrial flavoprotein dehydrogenases to the mitochondrial bc1 complex via electron transfer flavoprotein (ETF) and ubiquinone."]
- Quinone/ubiquinone binding, single site per monomer:
  [PMID:14640977 "consistent with one ubiquinone-binding site per ETF-QO monomer"]
- 4Fe-4S flavoprotein, inner membrane, catalyzes UQ reduction by ETF:
  [PMID:17050691 "Electron transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO) is a 4Fe4S flavoprotein located in the inner mitochondrial membrane. It catalyzes ubiquinone (UQ) reduction by ETF, linking oxidation of fatty acids and some amino acids to the mitochondrial respiratory chain."]
- Single [4Fe-4S] and one FAD per monomer, links primary flavoprotein dehydrogenases with
  main respiratory chain:
  [PMID:18037314 "Human, porcine, and Rhodobacter sphaeroides ETF-QO each contain a single [4Fe-4S](2+,1+) cluster and one equivalent of FAD"]
- MADD / secondary CoQ10 deficiency (disease → beta-oxidation involvement):
  [PMID:17412732 "All of our patients carried autosomal recessive mutations in ETFDH, suggesting that ETFDH deficiency leads to a secondary CoQ10 deficiency."]

## Disease

Biallelic loss-of-function → **glutaric acidemia type II / multiple acyl-CoA dehydrogenase
deficiency (MADD)**, a disorder of fatty acid, amino acid and choline metabolism; the
late-onset myopathic form is frequently **riboflavin-responsive** and is associated with a
**secondary (myopathic) CoQ10 deficiency** (PMID:17412732). Corroborated by the disorder KB
(`dismech/kb/disorders/Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml`), which also notes an
ETFDH-CIII-COQ2 metabolon that routes lipid-derived electrons into the respiratory chain.

## Annotation review reasoning

- **MF core = GO:0004174** electron-transferring-flavoprotein dehydrogenase activity (EC
  1.5.5.1). Directly supported by IDA (PMID:12049629, PMID:8306995, PMID:14640977). IBA/IEA/TAS
  duplicates ACCEPT.
- Cofactor binding: **GO:0050660 FAD binding** (ISS, supported by structure/homolog + UniProt
  BINDING features); **GO:0051539 4 iron, 4 sulfur cluster binding** (IDA PMID:18037314);
  **GO:0051536 iron-sulfur cluster binding** (IEA) is the parent of 0051539 — accept as broader.
- **GO:0048039 ubiquinone binding** (IDA, PMID:14640977) — specific & supported; core.
  **GO:0048038 quinone binding** is its parent (IDA same paper) — accept as broader.
- **GO:0009055 electron transfer activity** (IDA x2) — accurate; the enzyme is an electron
  carrier. Keep (non-core relative to the specific dehydrogenase MF, but correct).
- **GO:0016491 oxidoreductase activity** (IDA) — correct but very general parent of GO:0004174;
  MARK_AS_OVER_ANNOTATED (root-ish MF).
- CC: **GO:0005743 mitochondrial inner membrane** (IBA is_active_in, IDA PMID:8306995, IEA
  SubCell, TAS Reactome) — core location. **GO:0031966 mitochondrial membrane** (IDA) and
  **GO:0005739 mitochondrion** (IDA/HTP/IEA) are broader parents — accept as broader / non-core.
- BP: **GO:0022900 electron transport chain** (IBA/IDA/IEA) and **GO:0022904 respiratory
  electron transport chain** (TAS Reactome) — core process; ETF-QO feeds UQ pool.
  **GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase** (IMP PMID:17412732) —
  ETFDH is required for FAO flux (electron sink); accept as the biologically central linked
  process (its role is to accept the electrons from the acyl-CoA dehydrogenation step).
- **GO:0006979 response to oxidative stress** (IEA from mouse ortholog Ensembl; ISS from mouse
  Q921G7) — this is an ortholog-transferred phenotype-adjacent term, not a direct molecular
  function of ETF-QO; not core. Keep as non-core (mouse ETFDH KO shows oxidative-stress
  phenotype; over-propagated but not clearly wrong) — MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.
- **GO:0005515 protein binding** (IPI x7, PMID:32296183 HuRI Y2H) — bare protein binding to
  keratin-associated proteins, transcription factors (OTX1, GSC2, ZNF581), MYH7B, TRIM69 — no
  functional relevance to a mitochondrial inner-membrane oxidoreductase; classic high-throughput
  Y2H artifacts. Per policy: MARK_AS_OVER_ANNOTATED (not REMOVE), and per curation guideline the
  bare "protein binding" term is uninformative.

Deep research (falcon) file was NOT produced within the 8-min poll window; grounding is from
UniProt Q16134, seeded GOA, the cached experimental publications above, and the MADD disorder KB.
