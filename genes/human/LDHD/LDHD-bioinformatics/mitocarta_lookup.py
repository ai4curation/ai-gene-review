"""What does MitoCarta3.0 record for LDHD's sub-mitochondrial compartment?

Reads the Broad Institute Human.MitoCarta3.0.xls (downloaded by fetch_data.py) and reports
the sub-mitochondrial localisation, the evidence string (which says whether the protein was
seen in the APEX matrix or APEX intermembrane-space proteomes) and the tissues with MS/MS
detection, for LDHD and for comparator inner-membrane dehydrogenases of known topology.
"""
import json

import xlrd

import common as c

GENES = ["LDHD", "D2HGDH", "L2HGDH", "GPD2", "DHODH", "SQOR", "CYCS"]


def main():
    wb = xlrd.open_workbook(c.DATA / "Human.MitoCarta3.0.xls")
    sh = wb.sheet_by_name("A Human MitoCarta3.0")
    hdr = sh.row_values(0)
    out = {}
    for r in range(1, sh.nrows):
        row = dict(zip(hdr, sh.row_values(r)))
        if row["Symbol"] in GENES:
            ev = row["MitoCarta3.0_Evidence"]
            out[row["Symbol"]] = {"sub_mito_localization": row["MitoCarta3.0_SubMitoLocalization"], "evidence": ev,
                                  "APEX_matrix": "APEX_matrix" in ev, "APEX_IMS": "APEX_IMS" in ev,
                                  "msms_tissues": row["Tissues"], "msms_unique_peptides": int(row["MSMS_NUM_PEPTIDES_UNIQUE"] or 0)}
    (c.RESULTS / "mitocarta_lookup.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
