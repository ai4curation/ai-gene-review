# SGSH (P51688) review notes

Human SGSH — N-sulphoglucosamine sulphohydrolase (sulfamidase / heparan-N-sulfatase);
EC 3.10.1.1; 502 aa precursor, lysosomal, member of the sulfatase family.

## Verified core biology
- Lysosomal sulfatase in the stepwise **exolytic** degradation of heparan sulfate: hydrolytically
  removes the **N-sulfate group from terminal N-sulfo-D-glucosamine** residues (yields a free amino
  group / D-glucosamine + sulfate). Catalytic reaction (UniProt/Rhea RHEA:17881):
  `N-sulfo-D-glucosamine + H2O = D-glucosamine + sulfate` [file:human/SGSH/SGSH-uniprot.txt].
- Like all sulfatases, requires the **formylglycine (FGly)** catalytic residue (Cys70 → 3-oxoalanine),
  generated post-translationally by SUMF1 (FGE) [PMID:24816101; PMID:15962010].
- Structure (PMID:24816101, PDB 4MHX/4MIV): sulfatase fold, Ca2+-binding active site, FGly70;
  N-sulfatase with low identity to O-sulfatases; Arg282 binds the N-linked sulfate.
- Localises to the **lysosome / lysosomal lumen** (IDA PMID:15146460; SubCell SL-0158; Reactome).
- Deficiency → **Mucopolysaccharidosis type IIIA (Sanfilippo A syndrome)** [MIM:252900], autosomal
  recessive, HS lysosomal storage, severe CNS neurodegeneration. >100 SGSH variants known.

## Annotation review decisions (summary)
- MF **GO:0016250 N-sulfoglucosamine sulfohydrolase activity** — this is the exact current GOA MF term
  (present as IBA, IEA/EC, EXP, and 2× IDA). ACCEPT the experimental/IBA ones as CORE; the IEA (EC/RHEA
  mapping) also ACCEPT (correct, non-redundant electronic support). Used as the core MF.
- BP **GO:0006027 glycosaminoglycan catabolic process** (IBA + 2× IDA) and **GO:0030200 heparan sulfate
  proteoglycan catabolic process** (IBA + IMP) — both ACCEPT. GO:0030200 is the more specific HS branch;
  it is the pathway term used in core_functions (directly_involved_in). (Note: GO:0030200 label says
  "proteoglycan"; SGSH degrades the HS chain — biologically correct as the HS catabolic pathway.)
- CC lysosome (GO:0005764 IBA/IEA/IDA) and lysosomal lumen (GO:0043202 TAS Reactome ×4) — ACCEPT.
- **GO:0070062 extracellular exosome** (HDA, PMID:23533145) — secretome/exosome proteomics; MARK_AS_OVER_ANNOTATED
  (does not reflect the site of action; secreted lysosomal enzyme detected in exosomes).
- **GO:0005515 protein binding** ×3 (IPI; all WITH SUMF1 Q8NBK3) — bare protein binding, uninformative;
  MARK_AS_OVER_ANNOTATED (per policy, not REMOVE). SUMF1 interaction is real and biologically meaningful
  (FGE activates SGSH) but "protein binding" is uninformative.

## References
- Experimental: PMID:7493035 (cloning, EC 3.10.1.1, HS lysosomal degradation), PMID:15146460 (mutant
  expression, activity, lysosomal localisation, MPS IIIA), PMID:24816101 (crystal structure, FGly,
  catalysis, sulfatase family), PMID:15962010 (SUMF1/SUMF2 modulation of sulfatases incl. SGSH).
- Large-scale: PMID:23533145 (exosome proteomics), PMID:33961781 & PMID:40205054 (interactome maps).
</content>
