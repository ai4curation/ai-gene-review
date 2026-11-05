# PA3891 (Q9HXC2) notes

## Identity

- Q9HXC2, unreviewed TrEMBL entry, 387 aa, locus PA3891, no gene symbol.
  UniRule name "Quaternary amine transport ATP-binding protein" (EC 7.6.2.9).
- Domain architecture: N-terminal ABC NBD (PROSITE PS50893, 2..241, Walker A
  ATP-binding site 39..46) followed by tandem CBS domains (259..315, 316..372).
  NCBIfam TIGR01186 (proV), InterPro IPR005892 (Gly-betaine_transp_ATP-bd),
  PANTHER PTHR43117:SF4 (osmoprotectant import ATP-binding protein OsmV).
  [file:PSEAE/PA3891/PA3891-uniprot.txt "FT   DOMAIN          259..315"]
- Operon context (UniProt REST lookup, 2026-10-28): PA3888 (Q9HXC5, permease),
  PA3889 (Q9HXC4, glycine-betaine-binding protein), PA3890 (Q9HXC3, permease),
  PA3891 (ATPase). This is the OpuC-type arrangement with two distinct permeases
  (OpuCB/OpuCD-like), unlike E. coli ProU.
- PA3891 is a soluble NBD subunit (no TM segment). UniRule places it as a
  peripheral protein on the cytoplasmic face of the inner membrane:
  [file:PSEAE/PA3891/PA3891-uniprot.txt "Cell inner membrane"]

## Literature

Only one paper is cited for PA3891, and it is about the P. syringae transporter.

**Chen & Beattie 2007, PMID:17660277 (full text cached).** Characterises OpuC
(PSPTO_4575-4578; the ATPase OpuCA is Q87WH5 = PSPTO_4575) of P. syringae pv.
tomato DC3000 by knockouts, [14C] uptake and competition assays.
- OpuC is the main glycine betaine transporter and one of several choline
  transporters: [PMID:17660277 "one, designated OpuC, functioned as the primary or sole transporter for glycine betaine and as one of multiple transporters for choline under high osmolarity"]
- Specificity of the DC3000 transporter: [PMID:17660277 "The P. syringae pv. tomato OpuC transporter had a high affinity for glycine betaine, a low affinity for choline, and a broad substrate specificity that included acetylcholine, carnitine, and proline betaine."]
  Carnitine, proline betaine and acetylcholine come from competition of
  [14C]betaine/choline uptake, not direct uptake of those compounds.
- CBS domains of the ATPase are needed for function and predict osmoregulatory
  transporters in other pseudomonads; PA3891 was named as the predicted PAO1
  component: [PMID:17660277 "PA3891 in P. aeruginosa PAO1"]
- **The only PA3891 experiment** is a heterologous screen: a PAO1 genomic
  library was put into a DC3000 triple mutant (Delta opuCA, Delta PSPTO_5269,
  Delta PSPTO_0462) and clones restoring growth on 0.5 M NaCl were selected:
  [PMID:17660277 "the transformants were plated on MinA media containing 0.5 M NaCl and either glycine betaine or choline (2 mM)"]
  [PMID:17660277 "The sequence of the complementing clones indicated that transporters involving Psyr4249 from P. syringae pv. syringae strain B728a and PA3891 from P. aeruginosa PAO1 were functional, as predicted."]
  No uptake assay, substrate specificity, ATPase assay, localisation or complex
  assay was done with PA3891 or its PAO1 partners. Which osmoprotectant
  (betaine or choline) the PAO1 clone rescued on is not stated in the text.

PubMed search (2026-10-28) for P. aeruginosa OpuC/PA3891 found no paper
characterising the PAO1 PA3888-PA3891 transporter directly. The P. aeruginosa
Cbc papers (PMID:19919675, PMID:21478341) concern the separate CbcXWV
transporter (PA5378-PA5376), not PA3891.

## Interpretation

- The GO claims on PA3891 are plausible: the ortholog OpuC (DC3000) is a
  betaine (high affinity) / choline (low affinity) osmoprotectant importer, and
  PA3891 complements an opuCA-deficient strain for osmoprotected growth.
- But every PseudoCAP "IDA" row on PA3891 rests on genetic complementation in a
  heterologous host. That is IGI-type (functional complementation) evidence, and
  the substrate specificity is transferred from the DC3000 ortholog (properly
  ISS, which PseudoCAP also used for choline/carnitine).
- PA3891 is an NBD: it hydrolyses ATP and contributes to the ABC transporter
  activity of the PA3888-PA3891 complex. GO convention attaches the ABC-type
  transporter activity to subunits with `enables`; in core functions I record
  it as `contributes_to`, with ATP hydrolysis as the subunit's own activity.
- Glycine betaine is the best-supported substrate (high affinity in the
  ortholog); choline is a low-affinity substrate; carnitine is inferred from
  competition only. The broad term GO:0015418 ABC-type quaternary ammonium
  compound transporting activity summarises the broad specificity.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN001953445 (PTHR43117) | GO:0005886 plasma membrane | 1 (sole) | 31 (24 taxa) | GO:0043190 ABC transporter complex, IDA, PMID:17660277 (PseudoCAP) | INDIRECT-PHENOTYPE | The paper never assays complex formation or location of PA3891; the "IDA" is growth complementation of a P. syringae mutant on high-salt medium. The node term itself is biologically sound for the NBD of an ABC importer (peripheral to the cytoplasmic face of the inner membrane; UniRule RU369116), so the IBA is correct but rests on no experimental localisation. Re-seed with experimental localisation of a clade member if any exists. |
| PTN001953060 (PTHR43117) | GO:0031459 ABC-type glycine betaine transporter activity | 1 (sole) | 23 (18 taxa) | GO:0031459, IDA, PMID:17660277 (PseudoCAP) | INDIRECT-PHENOTYPE | PA3891 evidence is heterologous complementation of osmoprotected growth on plates with either betaine or choline, not a transport assay; the betaine specificity is the DC3000 ortholog's (Q87WH5, OpuCA, uptake and competition assays in the same paper). The node term fits an OpuC-type CBS-NBD clade, so the IBA is plausible, but the seed should be IGI/ISS, or the IBD should be re-seeded on Q87WH5 if it lies in this clade. |

Both seeds: claim plausible, evidence code overstated. Recorded as
PSEUDOCAP WRONG_EVIDENCE_CODE (CHECK) defects on the two seeding IDA rows and
GO_CENTRAL CHECK defects on the two IBA rows. IBAs on PA3891 are kept.

## Review decisions (summary)

- ACCEPT: plasma membrane (IBA, IEA); ABC-type glycine betaine transporter
  activity (IBA, IDA); GO:0015418 (IEA, IDA); ATP binding; ATP hydrolysis;
  glycine betaine transport (IEA, IDA); ABC transporter complex (IDA).
- MODIFY: nucleotide binding (IEA, ISS) -> ATP binding; membrane -> plasma
  membrane; response to osmotic stress -> cellular hyperosmotic salinity
  response; amino-acid betaine transport -> glycine betaine transport.
- KEEP_AS_NON_CORE: choline transport and ABC-type choline transporter activity
  (low-affinity, ortholog-derived); carnitine transport and carnitine
  transporter activity (competition only, ortholog); cellular hyperosmotic
  salinity response (physiological context).
