"""Measure warm process launches for a before/after comparison on macOS."""

from statistics import median
from subprocess import run
from time import perf_counter_ns


def batch(count):
    start = perf_counter_ns()
    for _ in range(count):
        run(["/usr/bin/true"], check=True)
    return (perf_counter_ns() - start) / count / 1000


if __name__ == "__main__":
    batch(100)
    samples = [batch(500) for _ in range(11)]
    print("Microseconds per launch, 11 batches of 500:")
    print(" ".join(f"{sample:.1f}" for sample in samples))
    print(f"Median: {median(samples):.1f} us/launch")
