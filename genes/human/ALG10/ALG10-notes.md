# ALG10 (ALG10A) — curation notes

UniProtKB: Q5BKT4 (AG10A_HUMAN). HGNC:23162. Gene symbol ALG10 (synonym ALG10A).
473 aa multi-pass ER membrane protein. CAZy GT59; PANTHER PTHR12989; Pfam PF04922
(DIE2_ALG10); InterPro IPR016900 (Alg10); PIRSF028810.

Note: deep research (falcon) was unavailable at review time (provider out of credits,
HTTP 402). This review is grounded in the UniProt record, the seeded GOA, and the one
cached publication (PMID:32296183). No `-deep-research-*.md` file was fabricated.

## Function

ALG10 is the ER-lumenal alpha-1,2-glucosyltransferase (EC 2.4.1.256) that catalyzes the
**third and final glucose addition** in dolichol-linked oligosaccharide (LLO) assembly.
It transfers glucose from dolichyl-phosphate-glucose (Dol-P-Glc; NOT UDP-Glc) onto the
Glc2Man9GlcNAc2-PP-dolichol intermediate to give the mature, fully assembled
Glc3Man9GlcNAc2-PP-dolichol precursor.

[file:human/ALG10/ALG10-uniprot.txt "adds the third and last glucose residue from
dolichyl phosphate glucose"] ... "Glc(2)Man(9)GlcNAc(2)-PP-Dol to produce
Glc(3)Man(9)GlcNAc(2)-PP-Dol."

The mature Glc3Man9GlcNAc2 glycan is transferred en bloc by the oligosaccharyltransferase
(OST) complex onto asparagine residues (N-X-S/T sequons) of nascent proteins. The
terminal alpha-1,2-linked glucose that ALG10 adds is the key recognition determinant for
efficient OST transfer, and after transfer the glucoses are trimmed by glucosidases I/II,
feeding the calnexin/calreticulin glycoprotein quality-control cycle.

UniProt FUNCTION: [file:human/ALG10/ALG10-uniprot.txt "operates in the biosynthetic
pathway of"] dolichol-linked oligosaccharides ... "Once assembled, the oligosaccharide is
transferred from the lipid to nascent proteins by oligosaccharyltransferases."

Catalytic activity Rhea:RHEA:29543; PhysiologicalDirection left-to-right (RHEA:29544).
Pathway: Protein modification; protein glycosylation (UniPathway UPA00378).

## Localization

ER membrane, multi-pass. UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane
... Multi-pass membrane protein". 10 predicted TM helices (FT TRANSMEM). Catalysis occurs
on the lumenal face of the ER (LLO glucosylation is a lumenal step). GO:0005789
(ER membrane) and GO:0005783 (ER) both apply.

## Family / paralog

Belongs to the ALG10 glucosyltransferase family
[file:human/ALG10/ALG10-uniprot.txt "Belongs to the ALG10 glucosyltransferase family."].
Human has a paralog ALG10B (ALG10-B). ALG10 has additionally been reported to modulate the
Kv1.1 (KCNA1) voltage-gated potassium channel (not part of the LLO/N-glycosylation core
function; not annotated in this GOA snapshot).

## Annotation review summary

GOA (Q5BKT4) carries 15 lines:
- MF GO:0106073 dolichyl pyrophosphate Glc2Man9GlcNAc2 alpha-1,2-glucosyltransferase
  activity (EC 2.4.1.256, RHEA:29543) x3 (IBA GO_REF:0000033, IEA GO_REF:0000120,
  ISS GO_REF:0000024) — core MF; ACCEPT the IBA (best supported), ACCEPT IEA/ISS.
- BP GO:0006487 protein N-linked glycosylation (IBA) — ACCEPT (core BP).
- BP GO:0006488 dolichol-linked oligosaccharide biosynthetic process (IEA InterPro) —
  ACCEPT (core BP; the specific pathway ALG10 acts in).
- CC GO:0005783 endoplasmic reticulum (IBA) — ACCEPT.
- CC GO:0005789 ER membrane (IEA SubCell + ISS) — ACCEPT (more specific, matches
  multi-pass TM topology).
- MF GO:0005515 protein binding (IPI PMID:32296183) x6 — HuRI high-throughput Y2H binary
  interactome; uninformative bare "protein binding". Per project policy on IPI protein
  binding: MARK_AS_OVER_ANNOTATED (do not REMOVE experimental).

Core functions: MF GO:0106073; directly_involved_in GO:0006488 (LLO biosynthesis) and
GO:0006487 (protein N-linked glycosylation); located_in GO:0005789 (ER membrane).
