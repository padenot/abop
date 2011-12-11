# abop.py, an Apache Bench Output Processor

This program wraps Apache Bench, and provides a graphical output.

It takes a config file as argument, and searches for `config.json` in the
current directory if none is provided.

A sample configuration file is presented below :

```json
{
  "concurrency" : "100",  // number of requests made at one
  "requests" : "100000",  // total number of requests
  "urls" : {              // A name, and the url to hit for the different
                          // configurations to test
    "Caching" : "http://0.0.0.0:8125/put/babab/plop/ac",
    "Nocaching" : "http://0.0.0.0:8126/put/babab/plop/ac"
  }
}
```

It produces a pdf output, representing the _repartition_ of 
