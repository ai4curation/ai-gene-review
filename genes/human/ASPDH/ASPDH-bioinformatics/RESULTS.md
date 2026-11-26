# ASPDH residue and pathway check

Script: `aspdh_sites.py` (run with `uv run python aspdh_sites.py`; raw output in `results.txt`). It fetches sequences and features live from UniProt.

## Alignment to characterized L-aspartate dehydrogenases

Human ASPDH (A6ND91, 283 aa) was aligned globally to two structurally characterized L-aspartate dehydrogenases.

- Thermotoga maritima Q9X1X6: 232 aligned positions, 71 identical (30.6%).
- Archaeoglobus fulgidus O28440: 232 aligned positions, 67 identical (28.9%).

**Catalytic histidine.** O28440 H189 aligns to ASPDH H223 (conserved). For Q9X1X6, the annotated H193 aligns to ASPDH V225, two residues away. The local windows show this is gap placement, not loss of the His:

    Q9X1X6 185-201: DPAMDHNIHIVRISSAI
    ASPDH aligned : DTSLDMHVVDVELSGPR
    O28440 181-197: ADEVEENIHEILVRGEF
    ASPDH aligned : ADTSLTDMHVVDVRGPT

ASPDH's "DMHVV" segment corresponds to the reference "NIHIV"/"NIHEI" motif, so the catalytic histidine is most likely retained as H223.

**NAD(+)-binding residues.** Several Rossmann-fold contacts are conserved in both comparisons: A75, S97, A127 and N192, plus N248/P249 against O28440. About half of the annotated NAD(+) contacts are substituted in each comparison (see `results.txt`), including the N-terminal glycine-rich positions (ASPDH R16/L17).

The global alignment maps the ribose-binding aspartate of the references (Q9X1X6 D28, O28440 D31) to ASPDH N41 and V37 respectively. Those placements are four residues apart, so the region is not well resolved. The local windows show ASPDH carries an aspartate two residues downstream:

    Q9X1X6 20-36: NFEKIYAYDRISKDIPG
    ASPDH aligned : -LELVFVWNRMAGSVPP
    O28440 23-39: GFEIAAILDVRGEHEKM
    ASPDH aligned : GPELGLELVFVWNRDRM

ASPDH residues 41-44 are N-R-D-P, so D43 is a plausible counterpart of the reference aspartate, which is followed by Arg in Q9X1X6 ("YAYDR"), with a gap-placement offset like the one seen for the catalytic histidine. The alignment therefore does not establish whether ASPDH prefers NAD(H) or NADP(H).

## Pathway context

The bacterial NadX route to NAD(+) produces iminoaspartate, which quinolinate synthase (NadA, EC 2.5.1.72) condenses into quinolinate. UniProt has no entry with EC 2.5.1.72 in human or anywhere in Mammalia, while the positive control returns E. coli K-12 NadA. Mammals therefore lack the enzyme downstream of an aspartate dehydrogenase in de novo NAD(+) synthesis.

## Conclusion

The catalytic histidine is probably retained, the cofactor preference cannot be called from the alignment, and the downstream pathway enzyme is absent in mammals. These results do not show whether human ASPDH has L-aspartate dehydrogenase activity; they argue against a role in NAD(+) biosynthesis.
