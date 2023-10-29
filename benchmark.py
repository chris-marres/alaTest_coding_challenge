"""Benchmark script."""

import os
import subprocess
from random import randint
from time import perf_counter

benchmark_times = {}


def generate_random_phone_numbers(amount: int):
    return [str(randint(1000000000, 9999999999)) for _ in range(amount)]


def benchmark_query_cli_command(random_phone_numbers: list[str]):
    start_time = perf_counter()

    for phone_number in random_phone_numbers:
        subprocess.Popen(
            ["python", "source/main.py", "query", f"{phone_number}"],
            stdout=subprocess.DEVNULL,
        )

    end_time = perf_counter()

    return end_time - start_time


def benchmark_continuous_cli_command(random_phone_numbers: list[str]):
    start_time = perf_counter()

    cli_process = subprocess.Popen(
        ["python", "source/main.py", "continuous"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    cli_process.communicate(input="\n".join(random_phone_numbers))

    end_time = perf_counter()

    return end_time - start_time


# Clear the operator price manager state.
print("Clearing the operator price manager state...")
os.system("python source/main.py clear")
print("Done.\n")


# Initialize the operator price manager data.
print("Initializing the operator price manager data...")
os.system(
    "python source/main.py update 'Operator A' price_lists/operator_a.csv"
)
os.system(
    "python source/main.py update 'Operator B' price_lists/operator_b.csv"
)
print("Done.\n")


# Benchmark the continuous cli command.
print("Benchmarking the continuous cli command...")
benchmark_times.update(
    {
        f"continuous_{amount}": benchmark_continuous_cli_command(
            generate_random_phone_numbers(amount)
        )
        for amount in [10, 100, 1_000, 10_000, 100_000, 1_000_000]
    }
)
print("Done.\n")


# Benchmark the query cli command.
print("Benchmarking the query cli command...")
benchmark_times.update(
    {
        f"query_{amount}": benchmark_query_cli_command(
            generate_random_phone_numbers(amount)
        )
        for amount in [10, 100]
    }
)
print("Done.\n")


print("Results:")
for benchmark, time in benchmark_times.items():
    print(f"{benchmark}: {time} seconds.")
