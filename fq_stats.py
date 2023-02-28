#!/usr/bin/env python3

import sys
import argparse
import gzip


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
        "--count",
        "-c",
        action="store_const",
        const=True,
        default=False,
        help="Count entries in FASTQ file",
    )
    prsr.add_argument(
        "--length",
        "-l",
        action="store_const",
        const=True,
        default=False,
        help="Return total length of sequence in each FASTQ file",
    )
    ns_obj = prsr.parse_args(args)

    all_stats = {
        "count": 0,
        "length": 0,
    }
    for fastq in ns_obj.fastq_files:
        get_file_stats(fastq, all_stats)

    if ns_obj.length:
        return all_stats["length"]
    elif ns_obj.count:
        return all_stats["count"]
    else:
        return all_stats


def get_file_stats(fastq, stats):

    for rec in fastq_file_records(fastq):
        stats["count"] += 1
        stats["length"] += len(rec["sequence"])


def fastq_file_records(fastq):
    with open_maybe_gzipped(fastq) as fastq_fh:
        while True:
            header = fastq_fh.readline()
            if header == "" or header == b"":
                break
            sequence = fastq_fh.readline()
            _ = fastq_fh.readline()
            quality = fastq_fh.readline()
            yield (
                {
                    "header": header[:-1],
                    "sequence": sequence[:-1],
                    "quality": quality[:-1],
                }
            )


def open_maybe_gzipped(fastq):
    if fastq[-3:] == ".gz":
        return gzip.open(fastq)
    else:
        return open(fastq)


if __name__ == "__main__":
    print(main())
