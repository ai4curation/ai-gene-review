# Ctns (Q9VCR7) ISS donor family check (2026-10-21 re-review)

Script: `compare_iss_donor_families.py` (live UniProt REST query); raw output in
`compare_iss_donor_families.out`.

## Output (verbatim)

```
Q9VCR7	len=397	gene=Ctns	Pfam=PF04193;	PANTHER=PTHR13131;PTHR13131:SF5;
O60931	len=367	gene=CTNS	Pfam=PF04193;	PANTHER=PTHR13131;PTHR13131:SF5;
O77062	len=479	gene=Eaat1	Pfam=PF00375;	PANTHER=PTHR11958:SF63;PTHR11958;
```

## Interpretation

Ctns and human CTNS share the PQ-loop Pfam domain PF04193 and the same PANTHER
subfamily PTHR13131:SF5 (CYSTINOSIN), so the UniProt ISS transfers from O60931 rest
on a valid orthology relationship.

Eaat1 (FBgn0026439), the similarity partner cited by the FlyBase ISS rows for
amino acid transmembrane transporter activity and amino acid transmembrane transport,
carries Pfam PF00375 and PANTHER PTHR11958 (SLC1 sodium:dicarboxylate symporter
family). It shares neither the domain nor the PANTHER family with Ctns, so it is not
a valid sequence-similarity donor for Ctns.
