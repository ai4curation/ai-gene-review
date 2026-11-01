#!/usr/bin/env python3
"""Query BRENDA for Km / turnover-number (kcat) values via its SOAP API.

BRENDA (https://www.brenda-enzymes.org) is the largest enzyme-function database.
Unlike SABIO-RK and M-CSA, its API is NOT anonymous:

  REQUIREMENTS (be aware before running):
    1. A free BRENDA account (register at https://www.brenda-enzymes.org/register.php).
       Academic use is free; check the licence for your use case.
    2. The `zeep` SOAP client:  pip install zeep
    3. Credentials supplied via environment variables:
       export BRENDA_EMAIL="you@example.org"
       export BRENDA_PASSWORD="your-password"   # sent only as a SHA-256 hash

This script makes real SOAP calls; it does not scrape the website. If you lack
credentials, use query_sabiork.py (open) for kinetic parameters instead.

Examples:
    python query_brenda.py --ec 2.7.1.1 --organism "Homo sapiens" --param km
    python query_brenda.py --ec 2.7.1.1 --param kcat
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys

WSDL = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"


def get_client():
    try:
        from zeep import Client
    except ImportError:
        sys.exit("zeep is required: pip install zeep")
    return Client(WSDL)


def credentials() -> tuple[str, str]:
    email = os.environ.get("BRENDA_EMAIL")
    password = os.environ.get("BRENDA_PASSWORD")
    if not email or not password:
        sys.exit("Set BRENDA_EMAIL and BRENDA_PASSWORD (see module docstring).")
    return email, hashlib.sha256(password.encode("utf-8")).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ec", required=True, help="EC number, e.g. 2.7.1.1")
    ap.add_argument("--organism", default="", help='Organism, e.g. "Homo sapiens"')
    ap.add_argument("--param", choices=["km", "kcat"], default="km",
                    help="km -> getKmValue; kcat -> getTurnoverNumber")
    args = ap.parse_args()

    email, pw_hash = credentials()
    client = get_client()

    fields = [email, pw_hash, f"ecNumber*{args.ec}"]
    if args.organism:
        fields.append(f"organism*{args.organism}")
    params = tuple(fields)

    if args.param == "km":
        results = client.service.getKmValue(*params)
        value_key, sub_key = "kmValue", "substrate"
    else:
        results = client.service.getTurnoverNumber(*params)
        value_key, sub_key = "turnoverNumber", "substrate"

    if not results:
        print("No records returned.", file=sys.stderr)
        return

    print(f"# BRENDA {args.param} for EC {args.ec}"
          f"{' / ' + args.organism if args.organism else ''}: {len(results)} records",
          file=sys.stderr)
    print("substrate\tvalue\torganism\tcommentary")
    for r in results:
        get = (lambda k: r.get(k, "")) if isinstance(r, dict) else (lambda k: getattr(r, k, ""))
        print("\t".join(str(get(k)) for k in (sub_key, value_key, "organism", "commentary")))


if __name__ == "__main__":
    main()
