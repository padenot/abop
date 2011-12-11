# abop.py, an Apache Bench Output Processor

This program wraps Apache Bench, and provides a graphical output.

## Dependencies

- Python
- Matplotlib
- ApacheBench (`ab` should be in the `PATH`)

## Usage

`abop` takes a configuration file as argument, and searches for `config.json` in
the current directory if none is provided.

A sample configuration file is presented below :

```json
{
  "concurrency" : "100",  // number of requests made at one
  "requests" : "100000",  // total number of requests
  "urls" : {              // A name, and the url to hit for the different
                          // configurations to bench
    "Caching" : "http://0.0.0.0:8125/put/babab/plop/ac",
    "Nocaching" : "http://0.0.0.0:8126/put/babab/plop/ac"
  }
}
```

It produces a pdf output, representing the _repartition_ of the servers response
time for the different configurations. An example result looks like that :

![An example run using this tool.](https://github.com/padenot/abop/raw/master/tests/Caching_vs_Nocaching.png "Example run. The caching version is slightly faster.")

You can test for yourself if you have `node` installed, by running the `test.sh`
shell script from the `tests/` directory.

## License

This program is licensed under the terms of the MIT Public License.
