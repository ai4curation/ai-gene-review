# NAA30 (N-alpha-acetyltransferase 30 / hMak3 / NAT12) research notes

## Identity
- UniProt Q147X3; HGNC:19844; EC 2.3.1.256. GNAT-fold acetyltransferase, MAK3 subfamily.
- **CATALYTIC subunit of the human NatC N-terminal acetyltransferase complex** (NatC = NAA30 + NAA35 + NAA38, i.e. hMak3/hMak10/hMak31).

## Core function
- Catalyzes co-translational Nt-acetylation of protein N-terminal methionine residues retained before hydrophobic/bulky residues (Met-Leu, Met-Ile, Met-Phe, Met-Trp, Met-Tyr).
  [PMID:19398576 "hMak3 acetylates Met-Leu protein N termini in vitro, suggesting a model in which the human NatC complex functions in cotranslational N-terminal acetylation"]
- NatC associates with ribosomes (cotranslational action). [PMID:19398576 "This complex associates with ribosomes"]
- Nt-acetylation by NatC shields proteins from degradation. [PMID:37891180 title "N-terminal acetylation shields proteins from degradation and promotes age-dependent motility and longevity"]
- ARL8B is an in vivo NatC substrate; NAA30 KD alters hArl8b localization. [PMID:19398576 "Knockdown of hMAK3 alters the subcellular localization of the Arf-like GTPase hArl8b, supporting that hArl8b is a hMak3 substrate in vivo"]
- NatC KD -> p53-dependent apoptosis. [PMID:19398576 "knockdown of NatC subunits results in p53-dependent cell death"]

## Localization
- Cytoplasm (ribosome-associated); also reported nucleus (PMID:25732826, PMID:19398576). Cytosol IDA (HPA).

## Annotation notes
- IDA + IEA acetyltransferase activity = core MF. Accept GO:0004596 IDA; GO:0120518 (N-terminal-methionine acetyltransferase activity) is the more specific EC-based term, accept.
- GO:0016747 (acyltransferase, non-amino-acyl) is a generic GNAT-domain IEA parent — over-annotation relative to the specific Nt-acetyltransferase term.
- NatC complex (part_of) well supported by IDA/IPI/IBA.
- protein binding IPI annotations all WITH NAA35 (Q5VZE5) — real complex partner; keep non-core (better captured by NatC complex membership).
- protein stabilization IDA (PMID:37891180) — downstream BP consequence of Nt-acetylation; keep non-core.
