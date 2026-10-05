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

**NAD(+)-binding residues.** Several Rossmann-fold contacts are conserved in both comparisons: A75, S97, A127 and N192 (and N248/P249 against O28440). However, the acidic residue that binds the adenine ribose of NAD(+) is not conserved: Q9X1X6 D28 aligns to ASPDH N41 and O28440 D31 to ASPDH V37. The N-terminal glycine-rich positions are also substituted (ASPDH R16/L17). Loss of that aspartate, with a basic residue nearby, is the usual signature of a Rossmann fold that prefers a 2'-phosphorylated dinucleotide (NADP(H)) over NAD(H). This is consistent with the InterPro-derived "NADP binding" and with the reported binding of NAADP (PMID:35841763), but it is a sequence inference only.

## Pathway context

The bacterial NadX route to NAD(+) produces iminoaspartate, which quinolinate synthase (NadA, EC 2.5.1.72) condenses into quinolinate. UniProt has no entry with EC 2.5.1.72 in human or anywhere in Mammalia, while the positive control returns E. coli K-12 NadA. Mammals therefore lack the enzyme downstream of an aspartate dehydrogenase in de novo NAD(+) synthesis.

## Conclusion

The catalytic histidine is probably retained, but the NAD-specific ribose contact is lost, and the downstream pathway enzyme is absent in mammals. These results do not show whether human ASPDH has L-aspartate dehydrogenase activity; they argue against a role in NAD(+) biosynthesis.
