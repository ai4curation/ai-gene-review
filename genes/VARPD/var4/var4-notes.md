# Curation Notes: var4 (A0A0N7FMV9) in Variovorax paradoxus

## Overview
- **UniProt ID:** `A0A0N7FMV9` (`A0A0N7FMV9_VARPD`, 2,345 aa)
- **Gene symbol / GenBank protein:** `var4` (`ALG65339.1`, `EMBL:KT362218`; orthologous to `varG` in *Variovorax* sp. H002 and *V. boronicumulans*)
- **Organism:** *Variovorax paradoxus* strain P4B (`NCBITaxon:34073`)
- **Function:** Hybrid type I polyketide synthase / nonribosomal peptide synthetase (PKS/NRPS) with an embedded C-terminal TauD/TfdA-family $	ext{Fe(II)}$/2-oxoglutarate-dependent $eta$-aspartyl dioxygenase domain.

## Domain Architecture & Biosynthetic Role
- **Domain organization:** Ketosynthase (`PF00109`/`PF02801`, residues 16–450), acyltransferase (`PF00698`), ketoreductase (`PF08659`), phosphopantetheine carrier protein (`PF00550`/`PS50075` at residues 1433–1508, Ser1468), NRPS LCL condensation domain (`PF00668`), and C-terminal TauD-like dioxygenase domain (`PF02668`/`IPR003819`).
- **Evidence:** Extends the $N$-acyl-arginine starter unit with a malonate/methylmalonate ketide unit and $eta$-hydroxylates the position-3 aspartate residue to form photoreactive $eta$-hydroxyaspartate ([PMID:26412281, "The prediction was modified as the presence of an aspartate β-hydroxylating enzyme led to the conclusion that the predicted position 3 aspartate was β-hydroxyaspartate."]). Knockout of the orthologous `varG` gene in *Variovorax* sp. H002 completely abolishes variochelin A–E biosynthesis ([PMID:38590537]). TreeGrafter projections to housekeeping fatty acid synthase (`GO:0004312`) and fatty acid biosynthesis (`GO:0006633`) are `REMOVE`d.
