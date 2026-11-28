# MGAT4D notes

MGAT4D/GnT1IP is the family outlier. Its luminal domain is homologous to GT54
N-acetylglucosaminyltransferases, but the mouse work summarized by UniProt found no
catalytic glucosyltransferase activity and instead showed that it inhibits MGAT1 in the
Golgi.

Huang et al. 2015 established the mechanistic split using mouse GnT1IP-L and the shorter
MGAT4D/GnT1IP-S form: the inhibitory activity maps to the luminal domain, ER retention
reduces inhibition, homomeric interactions occur in the ER, and the relevant heteromeric
interaction with MGAT1 occurs in the Golgi (PMID:26371870). The same paper mined human
testis data and found that human MGAT4D transcripts are markedly reduced in biopsies from
men with impaired spermatogenesis.

PAINT currently propagates catalytic acetylglucosaminyltransferase activity and protein
N-linked glycosylation from MGAT4A/B-like seeds to the SF10 MGAT4D clade. That should be
blocked at the broad SF10 node PTN008989299; the PANTHER tree check in
`interpro/panther/PTHR12062/PTHR12062-tree-check.txt` verifies that this node contains the
human, mouse and rat MGAT4D leaves.
