# mcrA (A0A7R9R780) — Ca. Ethanoperedens thermophilum ethyl-CoM reductase alpha

Part of the cross-clade MCR review (`projects/ARCHAEA/mcrA-across-clades.md`);
alkane-oxidizer (ACR) representative. UniProt organism: Ca. Methanoperedentaceae
archaeon GB50. RCSB lists the source of PDB 7B1S/7B2C (this entry) as
Candidatus Ethanoperedens thermophilum.

## Literature search

No deep-research provider key is configured (checked 2026-11-13). PubMed searched for
the Ethanoperedens culture and ECR structure papers and the alkane-ACR literature
(PMID:27749816 butane/Syntrophoarchaeum, 30918404 Argoarchaeum, 36266535 heterologous
ACR expression).

## Evidence

- Ethane is the sole growth substrate; ethyl-CoM is the activation product; single MCR
  in genome [PMID:32317322 "Combined substrate and metabolite analysis showed ethane as
  the sole growth substrate and production of ethyl-coenzyme M as the activation
  product."; "Its genome encodes only one MCR."].
- 0.99 A structure: widened chamber, dimethylated F430, Met lower-axial Ni ligand,
  33 A tunnel [PMID:34210888 "A sulfur from methionine replaces the oxygen from a
  canonical glutamine as the nickel lower-axial ligand"].
- No activity assay with methyl-CoM reported; the culture paper only raises a possible
  side reaction [PMID:32317322 "might be formed as a side reaction of the MCR"].
- The entry lacks IPR016212 (MCR alpha family); InterPro2GO rows come from the domain
  entries (IPR003183 etc.), all of which map to methanogenesis and GO:0050524.
- Residue comparison: Q147->M181 (F430 ligand), R225->A259, Q332->N375, C452->Q497.

## Review decisions (2026-11-13)

- GO:0015948 -> MODIFY GO:0043448 alkane catabolic process (no ethane term).
- GO:0050524 -> MODIFY to NTR "ethyl-coenzyme M reductase activity" + GO:0050497
  alkylthioltransferase activity. Rhea has no ethyl-CoM reaction (searched 2026-11-13).
- NEW: GO:0046906 tetrapyrrole binding (IDA, PMID:34210888).
- No complex row: GO:0044674 is defined as the methane-forming MCR; a generalized
  alkyl-CoM reductase complex is raised as a question.
- Source defects: InterPro domain mappings (scope) and the ARBA-derived UniProt name.
