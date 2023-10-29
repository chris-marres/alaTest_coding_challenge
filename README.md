# alaTest / ValueChecker (ICSS) challenge 2023

## Quick Setup

Copy paste the following snippet to quickly set up the project:

```shell
    git clone https://github.com/chris-marres/alaTest_coding_challenge.git \
    && cd alaTest_coding_challenge \
    && python -m venv venv \
    && source venv/bin/activate \
    && pip install -r source/requirements.txt \
    && python source/main.py update "Operator A" price_lists/operator_a.csv \
    && python source/main.py update "Operator B" price_lists/operator_b.csv
```

Please note that the above snippet creates and activates a python virtual environment to keep the project dependencies isolated, and your global python packages intact. After you are done reviewing the project, don't forget to deactivate the venv simply by typing `deactivate`.

## Usage Examples

Now that the project is up and running here are some example commands you could run:

### Help Messages

```shell
python source/main.py --help
```

```shell
python source/main.py `COMMAND` --help
```

### Query

```shell
python source/main.py query 4673212345
```

# Testing

Extensive testing was done to ensure proper function. You can run the test simply by letting the cli run them for you.

```shell
python source/main test
```

# Benchmarks

The whole idea of the implementation was to create a system where the state of the underlying data structure is persistent. Since there was no option for a database the system stores its state in a file before exiting and reloads the state on startup. While this is a performant enough implementation, the overhead of storing and loading the state each time is big.

For this reason another mode was implemeted where it keeps a session open for multiple queries to be executed. Something like this could be a service or an endpoint.

## Continuous Operation

```shell
python source/main.py continuous
```

And then input as many phone numbers you wish.

Sample snippet:

```shell
for phone_number in 1234567890 wrong 4673212345 0987654321; \
do echo $phone_number; \
done | python source/main.py continuous
```

## Results

I think the results speak for themselves:

|Test Case|Time (seconds)|
|          -         |   -   |
| query_10           | 0.003 |
| query_100          | 3.651 |
| continuous_10      | 0.144 |
| continuous_100     | 0.136 |
| continuous_1000    | 0.149 |
| continuous_10000   | 0.229 |
| continuous_100000  | 0.919 |
| continuous_1000000 | 7.863 |

You can run the benchmark locally too:

```shell
python benchmark.py
```