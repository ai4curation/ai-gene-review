# pqsC (Q9I4X1, PA0998) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`). MIBiG BGC0000922
(*P. aeruginosa* PAO1, 2-alkyl-4-quinolone / PQS-precursor cluster). GenBank
AAG04387.1 → UniProt **Q9I4X1** (PQSC_PSEAE), gene *pqsC* / PA0998.

## Function

PqsC is the **catalytic subunit of the heterodimeric condensing enzyme PqsBC**,
which catalyzes the second step of 2-alkyl-4(1H)-quinolone (AQ / HAQ) biosynthesis
in the *pqs* quorum-sensing pathway.

- Pathway (two steps): **PqsD** makes 2-aminobenzoylacetate (2-ABA) from
  anthraniloyl-CoA + malonyl-CoA; then **PqsBC** catalyzes the **decarboxylative
  coupling of 2-ABA to an octanoyl group carried on PqsC** to give
  **2-heptyl-4(1H)-quinolone (HHQ)**, the direct precursor of PQS
  (2-heptyl-3-hydroxy-4(1H)-quinolone; PqsH then adds the 3-OH).
  [PMID:24239007 "PqsD mediates the synthesis of 2-aminobenzoylacetate (2-ABA)...
  then the decarboxylating coupling of 2-ABA to an octanoate group linked to PqsC
  produces HHQ, the direct precursor of PQS. PqsB is tightly associated with PqsC
  and required for the second step."]
- **EC 2.3.1.230** "2-heptyl-4(1H)-quinolone synthase": reaction
  `(2-aminobenzoyl)acetate + octanoyl-CoA + H+ = 2-heptyl-4(1H)-quinolone + CO2 + CoA`
  (UniProt Q9I4X1; ECO:0000269|PMID:24239007, ECO:0000269|PMID:26811339).
- **Crystal structure (PDB 5DWZ)**: PqsBC is an obligate **heterodimer**; PqsC
  carries the catalytic active site **Cys-129 / His-269**; PqsB lacks these
  catalytic residues and is the non-catalytic partner.
  [PMID:26811339 "unique for its heterodimeric arrangement and an active site
  composed of Cys-129 and His-269"]

## Annotation issues identified

- **GO:0006633 fatty acid biosynthetic process (IEA)** — over-propagation from the
  β-ketoacyl-ACP synthase III (FabH/KAS III) InterPro signature. PqsBC is NOT a
  fatty-acid synthase: octanoate is a *substrate*, and the *product* is a quinolone
  QS signal, not a fatty acid. The Dulcey 2013 paper is explicitly titled to make
  this point ("...derive from fatty acids, not 3-ketofatty acids"). → **REMOVE**.
- **GO:0004315 3-oxoacyl-[acyl-carrier-protein] synthase activity (IEA)** — same
  KAS-III-fold over-annotation; the enzyme does not perform the FabH ACP-dependent
  Claisen condensation of fatty-acid synthesis. → **MODIFY** to the accurate parent
  GO:0016747; propose specific new term for EC 2.3.1.230.
- No GO MF term exists for EC 2.3.1.230 → `proposed_new_terms`:
  "2-heptyl-4(1H)-quinolone synthase activity".

## Predicted-complex evidence (BGC project)

Moriwaki et al. (bioRxiv 2025.10.26.684697) predict the PqsB–PqsC heterodimer
(BGC0000922; AAG04386.1/AAG04387.1) at **ipTM 0.95**, structurally matching PDB
5DWZ — consistent with the experimentally established obligate heterodimer.

## References
- PMID:24239007 — Dulcey et al. 2013, Chem Biol (pathway/mechanism). VERIFIED.
- PMID:26811339 — Drees et al. 2016, JBC (PqsBC crystal structure, 5DWZ). VERIFIED.
- PMID:12426334 — Gallagher et al. 2002, J Bacteriol (pqs genetics; IMP source). VERIFIED.
