# PP_0149 (Q88RI0) notes

Dashboard protein: CP069317.1_106 (https://gene-annotate-dashboard.kbase.us/review/CP069317.1_106), P. putida, tier A, Dark-Function.
Reviewed on Q88RI0 (KT2440 PP_0149), 97.1% identical over all 651 residues (632/651). The exact-sequence UniParc entries are deleted ("Not part of a reference proteome").

## Conclusion

PP_0149 is an exported, probably periplasmic, two-domain protein: DUF7844 followed by Lnb_N. Its molecular function is unknown. Orthologues in other pseudomonads are needed to tolerate quaternary ammonium compounds (QACs). That phenotype reflects envelope integrity in general, not a QAC-dedicated function.

### Topology

- SignalP (UniProt) and DeepTMHMM both predict a cleavable signal peptide at 1-22.
- There is no membrane-spanning segment and no lipobox.
- DeepTMHMM says "periplasmic or secreted". Three things favour the periplasm:
  - Pfam defines Lnb_N as a periplasmic domain.
  - The orthologues have strong cell-autonomous defects in pooled assays.
  - The orthologues are cofit with periplasmic envelope machinery.

### What DUF7844 is

PF25226 (DUF7844) has 576 UniProtKB members, 563 of them in Gammaproteobacteria and 12 in Bdellovibrionota. 574 of the 576 also carry Lnb_N (PF13387). No member has been characterized (BERIL run `20261030T214909Z-pp0149-domain-family`).

**DUF7844 domain (25-254).**
- Pfam predicts an M90 (MtfA) metallopeptidase-like fold.
- PP_0149 has an HExxH motif (H123/E124/H127) that is invariant in 32 representatives (27-69% identity).
- E209 is conserved in all 31 aligned representatives (one has a gap). It is a candidate third zinc ligand of a gluzincin site.
- The GOA IEA term "metallopeptidase activity" is ACCEPTed as a sequence inference.
- eggNOG COG3228 (MtfA) does not imply Mlc/ptsG regulation, and the dashboard annotator was right to reject that.

**Lnb_N domain (272-430).**
- Lnb_N is the NlpC/P60-like periplasmic domain of the *Bacteroides* lipoprotein N-acyltransferase Lnb (PMID:39495918).
- His300, Cys308, Cys318 and N409-C410 are conserved at 91-97%.
- PP_0149 lacks Lnb's transmembrane domain, and P. putida has the canonical Lnt, so the Lnb function is not transferred.

### Locus

- PP_0150 (DUF2388, small, exported) overlaps the PP_0149 start codon by 4 bp, on the same strand.
- PP_0151 (DUF2388) is 37 bp further on.
- This is a likely PP_0151-PP_0150-PP_0149 operon.
- The dashboard neighbourhood block omits PP_0150. It labels PP_0151 and PP_0152 with spurious names ("Holliday junction resolvasome", "Fe receptor"); the PP_0151 review rejects the resolvase name.

### Fitness

The Fitness Browser site returned 403 and `just fetch-fitness` failed, so the data were read from BERDL `kescience.fitnessbrowser`.

**KT2440 (BERIL run `20261030T213322Z-pp0149-fitness`).**
- PP_0149 has no phenotype in 300 experiments: the minimum fit is -0.42, with polymyxin B.
- None of the KT2440 experiments used a QAC.
- Its top cofitness partners score only up to 0.33, which is uninformative. Even so, several are LPS O-antigen, DegS/sigma E and murein genes.

**Orthologues (BERIL run `20261030T213530Z-pp0149-fb-orthologs`).** The Fitness Browser `ortholog` table gives 8 orthologues, with BLAST score ratio about 0.75. Five of them have strong QAC phenotypes, and the Fitness Browser calls those phenotypes specific:

| Strain | Condition | Fit | t |
|---|---|---|---|
| FW300-N2C3 | benzethonium | -5.19 | -23 |
| FW300-N2C3 | benzalkonium | -4.39 | -22 |
| FW300-N2E2 | benzethonium | -2.83 | |
| GW456-L13 | benzethonium | -2.01 | |
| WCS417 | benzalkonium | -2.04 | |
| RCH2 | benzethonium | -2.79 | |

- In RCH2 the orthologue also has strong phenotypes with bacitracin and polymyxin B.
- In N2E3 the phenotype is only mild (-0.7 with benzalkonium).
- N1B4 and *P. syringae* show no QAC phenotype.

### Is the QAC phenotype specific to this gene?

No, not in the sense the call implies.

- **Many genes are hit.** Each QAC experiment in which the orthologue is strongly hit flags 58-176 of 3,349-5,193 genes (fit ≤ -1, t ≤ -4). The orthologue ranks 7th to 88th among them.
- **The other hits are envelope genes.** In N2C3 benzethonium the top genes include BatBD/aerotolerance, Mla (toluene tolerance, MlaD), lytic transglycosylases and LPS kinase. In N2E2 they include FtsE, HtrA, Slt, the YrbCDF (Mla) transporter, VacJ (MlaA) and Pqi.
- **The cofitness partners are envelope genes too.** They are the PP_0150 orthologue (conserved cofitness, 0.63-0.93), the DUF1302 outer membrane protein orthologous to PP_0765 (0.94 in N2C3, 0.71 in WCS417), Pqi/MCE, FtsEX, amidases and lytic transglycosylases.
- **The operon partner shares the phenotype.** The PP_0150 orthologue is also QAC-sensitive (N2C3 -4.55; GW456 -1.17).

So QAC sensitivity marks a PP_0149/PP_0150(/PP_0151) envelope module. It may work with the DUF1302/DUF1329 system and is needed for barrier function. It is not a QAC-specific detoxification or efflux role.

## Dashboard verdict

**Supported, with caveats.** Every factual element of the call is right: DUF7844, exported, and orthologues required for QAC tolerance. But the call is weak on what it implies:
- The QAC tolerance is an envelope-integrity phenotype.
- It has not been tested in KT2440 or in the dashboard strain.
- The call missed the conserved HExxH zincin motif and the operon partner and cofit partner PP_0150.
- The 42% "SmeY" PaperBLAST homolog, an RND pump subunit, is architecturally incompatible with a soluble DUF7844/Lnb_N protein, and the annotator correctly set it aside.

Suggested corrected annotation: "Exported, probably periplasmic, DUF7844/Lnb_N protein with a conserved HExxH zincin-like motif; orthologues required for tolerance to quaternary ammonium biocides and other envelope stresses; molecular function unknown."

| GO term | Code | Note |
|---|---|---|
| GO:0009410 response to xenobiotic stimulus | UNC (1) | Rests on a mutant-sensitivity (necessity) phenotype in orthologues that is shared with many envelope genes; it is not a response process, and KT2440 is untested. |
| GO:0005576 extracellular region | UNC (1) | Export is supported, but the extractor turned "exported" into extracellular. The periplasm is favoured, and the companion review proposes GO:0042597 periplasmic space as NEW (IC). |

## Caveats

- The only phenotypes are from pooled RB-TnSeq of orthologues at about 75% identity. There is no P. putida QAC test, no clean deletion and no localization data.
- The conservation analysis uses pairwise global alignments to one representative per genus, not a full MSA or structure. The roles of E209 as a zinc ligand and of Cys410 as a nucleophile are hypotheses.
- Only abstracts were read for PMID:29769716. PMID:39495918 was read in full text.

## Tooling

- `just fetch-fitness` failed: "no FEBA data source was reachable". The fitness data came from BERDL through the MCP REST endpoint, which needed a curl User-Agent and limit ≤1000.
- `just validate-predictions` also writes `reports/prediction-evidence.json`, a shared report file. That is a side effect of the recipe.

## Files

- `PP_0149-ai-review.yaml`, `PP_0149-dashboard-predictions-review.yaml`
- `PP_0149-bioinformatics/`:
  - scripts: `fb_fitness.py`, `fb_orthologs.py`, `domain_family.py`, `summarize.py`
  - results: `kt2440_fitness_results.json`, `ortholog_fitness_results.json`, `family_results.json`, `pf25226_members.tsv`, `PP_0149_summary.txt`, `family_pfam_interpro.txt`
- `PP_0149-dashboard-prediction-evidence/`: `dashboard_call.json`, `dashboard_page.txt`, `PP_0149_summary.txt`
- History: `history/genes/PSEPK/PP_0149/2026-10-30T215506Z-claude-code-c251a3.yaml`
