## Doubly Prime Numbers

A doubly prime number is defined a prime number that also has  it's constituting digits being prime.

*For example*:
  > 5 is prime and it's made up of the number 5 which is prime
  > 13 is prime. 1 is prime and so is 3
  > *Counter example*: 19 is prime.  1 is prime but 9 isn't since it's divisible by 3.

*Disclaimer*:
  > The example includes 1 as Prime Number. In reality 1 is not a prime Number this is just for Test purposes.

Running Doubly Code
-------------------
    > # For OSX / Linux / Windows
    > $ python DoublyPrimes.py

Running Tests
-------------
To run the tests, simply run:

    $ python tests.py


Running code Benchmarking
-------------------------
    # For OSX / Linux using UNIX `time` command
    > $ time python DoublyPrimes.py

When N = 100, you will get something like:

    > real	0m2.146s
    > user	0m0.011s
    > sys	0m0.005s

Using Python Script.

You need to install line profiler.

Releases of `line_profiler` can be installed using pip_:


    $ pip install line_profiler
Then:

    > $ python performance_test.py
