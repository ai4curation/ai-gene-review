# Citations for Research Query

**Query:** # Hypothesis: what is this generically-named bacterial "membrane protein"?

You are an independent computational biologist. A bacterial protein is annotated
in UniProt only as a generic "Membrane protein". Determine what it actually is —
its fold, the higher-order assembly it forms, and its subcellular localization.

## What is known (do not assume beyond this)

- NCBI Protein Family **NF041162** (NCBIFAM/PGAP), an *equivalog*, ~314 aa members
  across diverse bacteria.
- This representative, UniProt **A0A0D5NHT9** (*Paenibacillus beijingensis*,
  314 aa), is UniProt-named only "**Membrane protein**" — an uninformative
  placeholder.

## Representative sequence

UniProt **A0A0D5NHT9**, 314 aa:

```
MAEQENSVKTLGSSAAYQLANVTKTAPVFEAVTPRFLTRLFEWKGLETGIFRLNKVNEGETTLDILCSQSDDVNITEGFVDCSSKPREYTLNAISTVVNVHTHISDLYSSPYDQVKEQLRLSIESIKERQESQLINSDDYGLLKNAAESQRIQTRFGPPTPDDLDELISKVWKEPSFFLAHPRAIAAFGRECTRRGVPPQTVQLFGAHFLTWRGIPIIPTDKLFVDGQKSPKGKGGKTNILLVRTGEQKQGVVGLYQAGVPGEQSKGLSVRFMGLDKNGIGSYLLSLYCSVAILADDAVAVLEDVDVGNYYDYQ
```

## The decisive question (scope your work to this)

**What is the fold and higher-order assembly of this protein, and where does it
localize?** Answer by:
1. Foldseek fold assignment of the AlphaFold model — what is the closest
   experimentally characterized structural homolog, and does the fold correspond
   to a **self-assembling proteinaceous shell/capsid** (e.g. an HK97 phage-capsid
   fold) rather than an integral-membrane protein?
2. State the **higher-order assembly** implied (monomer? icosahedral shell/
   nanocompartment?) and the correct **subcellular localization / cellular
   component**.
3. Give the most specific identity and cellular-component assignment you can, and
   say whether "**membrane protein**" is correct or a mis-annotation.

Keep other analyses light. Give one clear conclusion with confidence and the one
experiment that would confirm it.
**Provider:** openscientist
**Generated:** 2026-07-18T19:50:22.278965

1. PMID:41481934
2. PMID:42297566
3. PMID:41794648