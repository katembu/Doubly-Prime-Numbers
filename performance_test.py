import cProfile
from DoublyPrimes import Doubly


def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func


def get_number():
    for x in xrange(5000000):
        yield x


@do_cprofile
def do_test():
    for N in get_number():
        doubly = Doubly(N)
        # Generate Prime Numbers between 1 - N
        p = list(doubly.prime_number_generator())
        # Get Doubly Prime Numbers
        doubly_list = doubly.doubly_list(p)
        return "Doubly List Between 1 - %s : %s " % (N, doubly_list)


# Line by Line profiler
try:
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner

except ImportError:
    def do_profile(follow=[]):
        "Helpful if you accidentally leave in production!"
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner


@do_profile(follow=[get_number])
def test_line_profiler():
    for N in get_number():
        doubly = Doubly(N)
        # Generate Prime Numbers between 1 - N
        p = list(doubly.prime_number_generator())
        # Get Doubly Prime Numbers
        doubly_list = doubly.doubly_list(p)
        return "Doubly List Between 1 - %s : %s " % (N, doubly_list)


if __name__ == '__main__':
    print "================================================"
    print "====================CProfiler==================="
    print "================================================"
    do_test()
    print "================================================"
    print "====================Line Profiler==============="
    print "================================================"

    test_line_profiler()
