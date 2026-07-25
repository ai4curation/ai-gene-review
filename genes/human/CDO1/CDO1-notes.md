# CDO1 (Cysteine dioxygenase type 1) — review notes

UniProt: Q16878 (CDO1_HUMAN). HGNC:1795. EC 1.13.11.20. 200 aa, chromosome 5.

## Core biology (from UniProt file, authoritative)

CDO1 is **cysteine dioxygenase type 1**, a cytosolic non-heme mononuclear Fe(II)
thiol dioxygenase that catalyzes the first and rate-limiting/committed step of
cysteine catabolism.

- Function: "Rate-limiting enzyme of the cysteine catabolic process to taurine,
  which catalyzes the oxidation of cysteine to cysteine sulfinic acid with addition
  of molecular dioxygen." [file:human/CDO1/CDO1-uniprot.txt] (FUNCTION, ECO:0000269|PubMed:17135237)
- Catalytic activity: "L-cysteine + O2 = 3-sulfino-L-alanine + H(+)"; Rhea:RHEA:20441;
  EC=1.13.11.20 (ECO:0000269|PubMed:17135237). [file:human/CDO1/CDO1-uniprot.txt]
- Cofactor: "Name=Fe(2+)" — "Binds 1 Fe(2+) cation per subunit. Zn(2+) can be used to a much
  lesser extent (PubMed:17135237). Ni(2+) can be used to a lesser extent
  (By similarity)." [file:human/CDO1/CDO1-uniprot.txt]
- Pathway: "Organosulfur biosynthesis; taurine biosynthesis; hypotaurine
  from L-cysteine: step 1/2." [file:human/CDO1/CDO1-uniprot.txt] (UniPathway UPA00012, UER00537)
- Subunit: "Monomer." [file:human/CDO1/CDO1-uniprot.txt]
- Tissue: "Highly expressed in liver and placenta. Low expression in heart, brain and
  pancreas." [file:human/CDO1/CDO1-uniprot.txt] (ECO:0000269|PubMed:10427686)

## Structure / catalytic cofactor

Ye et al. 2007 (PMID:17135237) solved the first human CDO structure with substrate.
Abstract (cached, abstract-only): "Cysteine dioxygenase is a non-heme mononuclear iron
metalloenzyme that catalyzes the oxidation of cysteine to cysteine sulfinic acid with
addition of molecular dioxygen." A cross-linked **Tyr-157/Cys-93 thioether cofactor**
is catalytically important. [PMID:17135237 "non-heme mononuclear iron metalloenzyme that catalyzes \nthe oxidation of cysteine to cysteine sulfinic acid with addition of molecular \ndioxygen"]
- UniProt FT: catalytic Fe binding at residues 86, 88, 140; CROSSLNK 93..157
  "3'-(S-cysteinyl)-tyrosine (Cys-Tyr)". [file:human/CDO1/CDO1-uniprot.txt]
- Metal-substitution mutagenesis (Y157F almost total loss of activity/Fe; C93S reduces
  activity/Fe by 50%; R60Q reduces activity 70%): supports Fe(2+) as the physiological
  metal and Zn(2+)/Ni(2+) as poor in-vitro substitutes.

## Downstream metabolism / pathway role

- CDO produces cysteinesulfinate (3-sulfino-L-alanine), the branch point toward
  (i) taurine/hypotaurine and (ii) pyruvate + sulfite → sulfate.
- Wilkinson & Waring 2002 (PMID:12110289, abstract-only): "Cysteine dioxygenase (CDO)
  is the initial and rate-limiting enzyme involved in the oxidative degradation of
  cysteine to inorganic sulphate. It is believed to be the major source of sulphate
  in vivo." Cytokines TNF-alpha and TGF-beta inhibit CDO expression in human cell lines.
  [PMID:12110289 "the initial and rate-limiting enzyme involved in \nthe oxidative degradation of cysteine to inorganic sulphate"]
- Satsu et al. 2003 (PMID:12871209, abstract-only): CDO described as "one of the key
  enzymes of taurine biosynthesis"; CDO mRNA up-regulated under hypertonic conditions
  in HepG2 cells. [PMID:12871209 "one of the key enzymes of taurine "]

## Post-translational regulation (LRRC58 / CRL5)

Xiao et al. 2025 (PMID:40963025, FULL TEXT available). CDO1 is degraded by the
CRL5–LRRC58 (Cullin-5 RING) E3 ubiquitin ligase; LRRC58 is the substrate adaptor.
- "LRRC58 is the substrate adaptor of an E3 ubiquitin ligase that mediates
  proteasomal degradation of CDO1, the rate-limiting enzyme of the catabolic shunt
  of cysteine to taurine". [PMID:40963025]
- Functional (IDA) evidence for CDO1 driving cysteine catabolism / taurine synthesis:
  "depletion of LRRC58 drove increased flux from cysteine to hypotaurine and taurine"
  and "The increase in hypotaurine and taurine abundance upon LRRC58 knockdown was
  completely reversed by depletion of CDO1". [PMID:40963025]
- Cysteine abundance gates this: complex degrades CDO1 when cysteine is high, spares it
  when cysteine is low. UniProt PTM: MUTAGEN His-147/Thr-148/Arg-170 disrupt LRRC58
  interaction and ubiquitination. [file:human/CDO1/CDO1-uniprot.txt]
- KW "Ubl conjugation". This is a regulatory input onto CDO1 (CDO1 is the substrate),
  not a molecular function of CDO1 itself; no new MF/BP proposed for CDO1 from it.

## Disease / tumor-suppressor context (background)

CDO1 is frequently epigenetically silenced by promoter hypermethylation across many
cancers and behaves as a candidate tumor suppressor; a somatic E143Q variant was found
in a colorectal cancer sample (UniProt VARIANT VAR_036170, PMID:16959974). This is
background context; not directly reflected in the GO annotations under review.

## Annotation review decisions (summary)

Core (ACCEPT):
- MF: GO:0017172 cysteine dioxygenase activity (IDA PMID:17135237 + IBA/IEA/ISS redundant)
- MF: GO:0008198 ferrous iron binding (IDA PMID:17135237 + IBA/IEA redundant)
- MF: GO:0005506 iron ion binding (IEA; correct parent of ferrous iron binding)
- MF: GO:0016702 oxidoreductase (dioxygenase) activity (IEA; correct parent of CDO activity)
- BP: GO:0019448 L-cysteine catabolic process (IDA PMID:40963025 + TAS/IBA/IEA)
- BP: GO:0042412 taurine biosynthetic process (IDA PMID:40963025 + TAS PMID:12871209 + IEA)
- BP: GO:0006790 sulfur compound metabolic process (IEA; correct general grouping)
- CC: GO:0005829 cytosol (TAS Reactome + TAS PMID:12110289)

Over-annotations (MARK_AS_OVER_ANNOTATED; experimental/ISS not removed):
- MF: GO:0008270 zinc ion binding (IDA + IEA) — Zn(2+) only substitutes "to a much lesser
  extent" in vitro; not the physiological cofactor.
- MF: GO:0016151 nickel cation binding (ISS + IEA) — Ni(2+) "By similarity", "to a lesser
  extent"; not physiological.

Over-propagated electronic (REMOVE; all IEA GO_REF:0000107 transferred from rat/mouse
ortholog expression studies, describe regulation of the rodent gene, not conserved
molecular function of the human protein):
- GO:0007595 lactation, GO:0043200 response to amino acid, GO:0097184 response to azide,
  GO:0051591 response to cAMP, GO:0045471 response to ethanol, GO:0033762 response to
  glucagon, GO:0051384 response to glucocorticoid.
</content>
</invoke>
