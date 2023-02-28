#!/usr/bin/env python3

import sys
import argparse


def main(args=sys.argv[1:]):
    prsr = argparse.ArgumentParser(
        description="Generate stats from FASTQ format files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    prsr.add_argument(
        "fastq_files",
        nargs="*",
        help="One or more .fq (or .fq.gz) files",
        metavar="FASTQ_FILE",
    )
    prsr.add_argument(
        "--count", "-c",
        action="store_const",
        const=True,
        default=False,
        help="Count entries in FASTQ file"
    )
    prsr.add_argument(
        "--length", "-l",
        action="store_const",
        const=True,
        default=False,
        help="Return total length of sequence in each FASTQ file"
    )
    ns_obj = prsr.parse_args(args)

    return None


if __name__ == "__main__":
    print(main())
