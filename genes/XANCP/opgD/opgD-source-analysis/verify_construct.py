"""Compare deposited XccOpgD structure entity and primer to frozen Q8P3C6."""
from pathlib import Path
import hashlib
import json
from Bio.Seq import Seq

HERE = Path(__file__).resolve().parent
raw = HERE.parent / "opgD-uniprot.txt"
s = "".join(raw.read_text().split("SQ   SEQUENCE")[1].splitlines()[1:-1]).replace(" ", "")
r = json.loads((HERE / "8x18-identity-fields.json").read_text())
p = r["entity_poly"]["pdbx_seq_one_letter_code_can"].replace("\n", "")
diffs = [{"position":i+1,"reference":a,"PDB":b} for i,(a,b) in enumerate(zip(s,p)) if a != b]
assert diffs == [{"position":379,"reference":"D","PDB":"N"}]
assert p[len(s):] == "LEHHHHHH"
primer = "actttaagaaggagatatacatatggccaaggcagtggggctgcgtcgc"
translation = str(Seq(primer[primer.index("catatg")+3:]).translate())
assert translation == "MAKAVGLRR" and s[28:36] == translation[1:]
result = {"reference_accession":"Q8P3C6","reference_length":len(s),"reference_sha256":hashlib.sha256(raw.read_bytes()).hexdigest(),"structure":"8X18 entity 1","precursor_differences":diffs,"deposited_C_terminal_extension":p[len(s):],"source_strain":r["entity_src_gen"][0]["gene_src_strain"],"source_taxon":r["entity_src_gen"][0]["pdbx_gene_src_ncbi_taxonomy_id"],"expression_host":r["entity_src_gen"][0]["pdbx_host_org_scientific_name"],"WT_forward_primer":primer,"translated_primer_start":translation,"WT_primer_interpretation":"Added initiation methionine followed by native residues29 onward; deletion of predicted signal residues1–28. This is a sequence-derived interpretation of TableS4, not measured physiological cleavage.","scope":"D379N ligand-bound structure is not the wild-type cyclization assay. Deposited precursor sequence describes identity; the primer establishes signal-deleted recombinant design. Native ATCC33913 flux/localization has not been measured by these construct assays."}
(HERE / "construct-proof.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
