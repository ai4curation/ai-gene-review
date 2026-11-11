# A2cp1_1916 (B8J768) notes

LBNL hackathon, alpha-glucan batch (branch `hackathon/alpha-glucan-batch`), 2026-10-30.
Dashboard gene NC_011891.1_1918 (exact UniParc match to B8J768, A. dehalogenans 2CP-1,
812 aa, 100% identity and coverage). `just fetch-gene` gave taxon code ANAD2.

## Dashboard call

"Putative glycoside hydrolase family 57 protein containing a DUF3536 domain." (tier B).
GO:0016798 (medium).

- GO:0016798 hydrolase activity, acting on glycosyl bonds: **COR** (not in GOA).
- **Verdict: supported.** "Putative" could be dropped (catalytic residues intact), and the
  GH57_6 alpha-glucan subfamily could be named, but the call's refusal to name a reaction
  is right: the nearest characterized relative is under 40% identical and there is no
  gene context.
- Paste-in correction: "GH57 subfamily 6 (DUF3536-type) glycoside hydrolase with conserved
  catalytic Glu154/Asp261; probable alpha-1,4-glucan-active amylase/4-alpha-glucanotransferase;
  not in a treY/treZ trehalose gene cluster in Anaeromyxobacter; exact substrate untested;
  not an alpha-mannosidase."

## Key evidence

- Catalytic residues (run `gh57-catalytic`): Glu154 (CSR-3 WLPETA) and Asp261 (CSR-4
  AVDGETLGHH) at the GH57 nucleophile and proton-donor HMM columns; conserved family-wide in
  DUF3536 proteins (583/583, 582/583).
- CAZy GH57_6 (run `gh57-cazy`), with GSU2359 and DVU_2472. Characterized GH57_6:
  three alpha-amylases and PoGH57 [PMID:38930854 "Both enzymes exhibited activity on
  amylose and MD18."].
- Identities (run `gh57-identity`): GSU2359 45.4%, DVU_2472 39.1%, PoGH57 38.9%, Amo45 37.6%.
- Neighbourhood (run `gh57-synteny`): no alpha-glucan or trehalose gene within 5 genes in
  2CP-1 (neighbours: vWA protein, ThiD, MarC, GDSL lipase, ABC transporter), nor in 2CP-C or
  Anaeromyxobacter sp022808855. So the dashboard's trehalose context (Pontibacter homolog at
  38.8%, STRING link to TreY) does not apply to this gene's own locus.
- STRING links Adeh_2048 (94.6% identical STRING homolog) to TreY Adeh_0293 by
  "fusion, cooccurrence, neighborhood". Run `gh57-fusion-check` found no TreY fusion among
  1369 DUF3536 clusters (all 2-domain, none at or above 1200 aa); the fusion channel is
  probably driven by eggNOG/KO-level TreY labels on GH57 proteins (128 clusters carry K06044
  without a GH13 domain).
- Alpha-mannosidase: no characterized GH57 has an alpha-mannosidase EC; COG1449's name reflects
  GH57/GH38 fold similarity (PMID:12618437).

## Full review decisions

- GO:0003824 IEA: MODIFY to GO:0004553.
- GO:0005975 IEA: MODIFY to GO:0030978 alpha-glucan metabolic process (subfamily inference
  only; no pathway assigned).
- Core function: GO:0004553 in GO:0030978.

## Caveats

- Weaker than GSU2359: no gene context, no characterized relative above 39% identity.
- No FEBA fitness data: `just fetch-fitness ANAD2 A2cp1_1916` found none (no local FEBA data,
  and the bulk download failed to find any).
- Deep research: run once for the family on GSU2359 (claude-code; falcon/perplexity
  unavailable) and reused here, because the family-level literature is identical for both
  genes and no literature mentions A2cp1_1916. That report misnames this strain
  ("Anaeromyxobacter sp. K") and its neighbours; see GSU2359-notes.md.

## Files and runs

- BERIL runs (projects/hackathon): `20261030T234043Z-gh57-catalytic`,
  `20261030T234824Z-gh57-identity`, `20261030T234844Z-gh57-cazy`,
  `20261030T233053Z-gh57-synteny`, `20261030T234618Z-gh57-fusion-check`.
- QC: validate, validate-references, validate-terms, validate-predictions, render,
  validate-history all pass.
