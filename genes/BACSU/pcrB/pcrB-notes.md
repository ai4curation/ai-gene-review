# pcrB (yerE; BSU06600; O34790) notes

## Provenance of this review

- No deep-research provider key was available, so no
  `pcrB-deep-research-*.md` file exists.
- `just mod-description-deep-research BACSU pcrB` was run and skipped:
  "no MOD provider configured for organism 'BACSU'".
- PubMed search via MCP (2026-11-02):
  `(heptaprenylglyceryl OR PcrB OR AraM OR "glycerol-1-phosphate dehydrogenase") AND Bacillus`
  gave 11 hits; relevant: PMID:22614947, PMID:23322418, PMID:27226549,
  PMID:40626731, PMID:35767906, PMID:18558723. Also read PMID:21761520,
  PMID:24684232, PMID:21214173 (full text) and PMID:23322418 (full text).
- PMID:21761520 (Guldan 2011, source of the IDA rows) and PMID:24684232
  (source of the EXP row) are abstract-only in the cache.

## Activity

- HepGP synthase: transfers heptaprenyl (C35) from HepPP to the C3 hydroxyl of
  sn-G1P, forming an ether bond [PMID:21761520 "PcrB, the bacterial homologue
  of the archaea-specific geranylgeranylglyceryl phosphate synthase, produces
  heptaprenylglyceryl phosphate in bacillales"]. Group I GGGPS-family enzymes
  are HepGP synthases, group II are GGGP synthases [PMID:24684232].
- Acceptor strictly G1P, not G3P or 3PG; C10 and C20 donors are also used in
  vitro, FPP poorly [PMID:21214173 "PcrB uses G1P (1) exclusively as an
  acceptor"]. The native donor is C35 HepPP; dimerisation is needed to accept
  the long chain [PMID:22614947].
- Mg2+ is required: no product with EDTA or without MgCl2 [PMID:23322418 "No
  product was found, indicating that Mg2+ is likely essential for catalysis."].
- Crystal structures with bound G1P (3VZY, 3W00) [PMID:23322418].
- The C10/C20 use is in vitro substrate range for a C35 enzyme; not
  annotated separately (no GOA rows for it anyway).

## In vivo fate and physiological role of the product

- HepGP is dephosphorylated (by PhoB or another non-specific phosphatase) and
  acetylated by YvoF to HepG and Ac-HepG [PMID:21761520; PMID:27226549].
  These are minor lipids; the pathway does not build a bulk archaeal-type
  membrane lipid (no second prenyl chain is added) [PMID:27226549 "In
  Bacillales, heptaprenylglyceryl phosphate does not become linked to a second
  polyprenyl moiety like ether lipids in Archaea but is dephosphorylated and
  acetylated."].
- Physiological role (Komazin 2025, PMID:40626731, full text): Ac-HepG is the
  acetyl donor for N-terminal acetylation of lipoproteins by the membrane
  enzyme LhaT (YpjA). Deletion of pcrB, yvoF or ypjA abolished lipoprotein
  N-acetylation (loss of 42 Da on the FrxB N-terminal peptide) and back
  complementation restored it; the pathway was reconstituted in vitro with
  PcrB, phosphatase, YvoF and LhaT [PMID:40626731 "Only pcrB, yvoF, and ypjA
  fully suppressed TLR2 activity, indicating these genes are strictly
  required for Ac-LP synthesis."]. The authors argue for a carrier role
  rather than a structural membrane lipid role [PMID:40626731 "A catalytic
  role as a transient carrier for acetyl groups, as opposed to being a
  structural membrane building block for an archeal-type lipid with
  ether-linked isoprenoid chains, is more consistent with the low overall
  abundance of HepG/Ac-HepG observed in B. subtilis membranes (28)."].
- Open: how Ac-HepG/HepG crosses the membrane; whether HepG is recycled; other
  roles of Ac-HepG, since PcrB is more widely distributed than LhaT
  [PMID:40626731].
- Substrate supply: G1P from EgsA (AraM) is the presumed source, but I found no
  accessible data from an egsA mutant on HepG levels. The egsA gene was not
  among the reported Tn-screen hits for lipoprotein N-acetylation
  [PMID:40626731] (my reading of the hit list, not a claim of the paper).

## GO term choices

- GO:0120536 HepGP synthase activity: core MF; EXP/IDA/IEA all ACCEPT.
- GO:0004659 prenyltransferase (IBA, IEA) and GO:0016765 (IEA): correct
  parents of GO:0120536; MODIFY to GO:0120536.
- GO:0046474 glycerophospholipid biosynthetic process (IBA, IDA, IEA) and
  GO:0006650 (IEA): HepGP is formally a glycerophospholipid (O-alkyl
  glycerophosphate), but it is a transient intermediate; the in vivo
  products HepG/Ac-HepG are neutral glycerol ether lipids. GO:0008611 ether
  lipid biosynthetic process (definition: one lipid alcohol in ether
  linkage to glycerol) describes the pathway PcrB actually catalyses (it
  forms the ether bond). MODIFY all to GO:0008611.
- GO:0000287 magnesium ion binding: KEEP_AS_NON_CORE (catalytic cofactor).
- NEW GO:0042158 lipoprotein biosynthetic process (IMP, PMID:40626731):
  PcrB makes the carrier that supplies the acetyl group for lipoprotein
  N-acetylation (cofactor/carrier case). Comparator check (QuickGO,
  2026-11-02): E. coli Lgt (P60955) and Lnt (P23930) carry GO:0042158 (IMP,
  IDA, IBA); E. coli LspA (P00804) does not. For the carrier-synthase
  analogy, E. coli UppS/IspU (P60472), which makes the undecaprenyl carrier,
  carries GO:0009252 peptidoglycan biosynthetic process by IMP. Kept as a
  non-core NEW row.
- No GO term exists for lipoprotein N-acetylation specifically; GO:0006474
  N-terminal protein amino acid acetylation was considered but LhaT, not
  PcrB, performs the transfer.
