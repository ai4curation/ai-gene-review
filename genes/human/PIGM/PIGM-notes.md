# PIGM (Q9H3S5) review notes

## Identity
- Human PIGM = GPI alpha-1,4-mannosyltransferase I, catalytic subunit; a.k.a. GPI mannosyltransferase I (GPI-MT-I), PIG-M. HGNC:18858. 423 aa, multipass ER membrane protein, GT50 (CAZy), Pfam PF05007 Mannosyl_trans, InterPro IPR007704.

## Core biology (grounded)
- Catalytic subunit of the GPI-mannosyltransferase I (GPI-MT-I) complex (PIGM + PIGX). PIGX stabilizes PIGM.
  [PMID:32156170 "PIGM functions in association with PIGX, which stabilizes PIGM"]
- Transfers the FIRST mannose (Man1), via an alpha-1,4 bond, from dolichol-phosphate-mannose (Dol-P-Man) to GlcN-(acyl)PI, i.e. step 6 of GPI biosynthesis (Rhea:60500).
  [PMID:11226175 "PIG-M transfers the first mannose to glycosylphosphatidylinositol on the lumenal side of the ER"]
  [PMID:32156170 "PIGM and PIGV are GPI-mannosyltransferase (MT) I and II, respectively"]
- Reaction occurs on the LUMENAL side of the ER membrane; catalytic DXD motif (D49, D51) in a lumen-facing domain. D49A almost abolishes and D51A abolishes activity.
  [PMID:11226175 "PIG-M has a functionally important DXD motif, a characteristic of many glycosyltransferases, within a domain facing the lumen of the endoplasmic reticulum (ER)"]
  UniProt MUTAGEN D49 (almost abolishes), D51 (abolishes) — file:human/PIGM/PIGM-uniprot.txt
- Reactome R-HSA-162830: "It is catalyzed by a complex of at least two components, PIG-M and PIG-X (Maeda et al. 2001; Ashida et al. 2005)."

## Localization
- ER membrane, multi-pass (10 TM helices; UniProt topology). IDA in PMID:11226175; SubCell mapping; Reactome TAS; ComplexPortal NAS (CPX-2697).

## Disease
- GPIBD1 (glycosylphosphatidylinositol biosynthesis defect 1, MIM:610293): autosomal recessive; hypomorphic PIGM PROMOTER mutation. Portal/hepatic vein thrombosis, portal hypertension, absence/atypical-absence seizures, macrocephaly, splenomegaly, cytopenias, early cerebral infarctions.
  UniProt DISEASE cites PMID:16767100 (Almeida 2006, Nat Med, promoter mutation) and PMID:31445883 (Pode-Shakked 2019, cerebral+portal vein thrombosis, macrocephaly, atypical absence seizures). Neither is cached in publications/ and neither is a GOA reference; used only as background (via UniProt), not as supporting_text.

## GOA MF term to use (per instruction: read GOA for exact current MF id/label)
- GOA carries GO:0180041 "dol-P-Man:GlcN-acyl-PI alpha-1,4-mannosyltransferase activity" (IDA PMID:11226175; also IEA RHEA). This is the specific catalytic activity term = use for core_functions molecular_function. (Confirmed current label in go.db.)
- Broader MF terms present: GO:0004376 GPI mannosyltransferase activity (IEA InterPro), GO:0000030 mannosyltransferase activity (IBA), GO:0051751 alpha-1,4-mannosyltransferase activity (IEA InterPro) — all correct ancestors; the specific term (0180041) is the accurate one.

## Interaction (IPI) annotations
- Two IPI GO:0005515 "protein binding" from BioPlex (PMID:28514442 BioPlex 2.0; PMID:33961781 BioPlex 3.0), with:from UniProtKB:Q9NQZ5 = STARD7. UniProt records this same IntAct interaction (Q9H3S5–Q9NQZ5 STARD7, NbExp=2). High-throughput AP-MS; STARD7 is a lipid (PC) transfer protein, not the functional GPI-MT-I partner (PIGX). Uninformative "protein binding"; MARK_AS_OVER_ANNOTATED per policy (do not REMOVE bare protein-binding IPIs).

## core_functions term branch checks (go.db)
- GO:0180041 -> molecular_function (subClassOf) OK
- GO:0006506 -> biological_process (subClassOf) OK; GO:0005789 -> cellular_component (subClassOf) OK
</content>
</invoke>
