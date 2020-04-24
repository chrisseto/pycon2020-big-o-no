# Pycon2020 - Big O No

This is the companion repo for my pycon2020 talk.


## Running benchmarks:

```bash
./bench.sh postgres
```

```bash
./bench.sh cockroach
```

> A single node instance of cockroach doesn't handle large aggregations very well
>
> The benchmarks seen in my talk made use of a https://cockroachlabs.cloud/ 3 node GCP cluster
