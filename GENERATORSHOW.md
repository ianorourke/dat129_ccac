# Generators Run-Through

## Sources

[How To Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/)

[PEP 255 -- Simple Generators](https://www.python.org/dev/peps/pep-0255/)

[Programiz Python Generators](https://www.programiz.com/python-programming/generator)

Deitel, P. J., & Deitel, H. M. (2020). Intro to Python for computer science and data science: Learning to program with AI, 
big data and the cloud. Upper Saddle River, NJ: Pearson.

## Generator Basics

Per Programiz, generators, which can be functions or expression, return (or more accurately "yield" as we will see) objects
that can be iterated one value at a time, in contrast to a list comprehension that will produce an entire list. These
objects can looped over using for statements as well but their advantage is that through "lazy evaluation", generators
make less use of memory and this can make them useful when dealing with larger files.

## Generator Functions, yield, and next()

The use of iter() allows you to make a generator expression. To make a generator function, simply include a yield expression 
rather than a return statement and note that more than one yield expression can be included. Instead of returning a result, 
yield will suspend the results until the program requests another item, creating a generator object <genexpr> to keep track 
of the next value it will generate. (Deitel, Deitel; p. 462) These values are then brought into use through next() 
and as long as their are yield statements, next() will continue produce a result ending with an StopIteration message, 
showing the end of the function.
  
Generators can be useful for evaluating large files and large amounts of data, particularly in instances where
the amount may exceed the amount of available memory you have. In addition, they can be used to create data pipelines
to sort through data as needed without taxing memory.

## Quiz Example

To show in a very basic way how these work, let's show an example in a small quiz program.
Here we have a very rudimentary function with yield statements.

![Generator Function Example](https://github.com/ianorourke/dat129_ccac/blob/main/generator_ex1.png)

For this, we have the answers listed in this function as different results that are kept in place using yield statements.

![Generator Example 2](https://github.com/ianorourke/dat129_ccac/blob/main/generator_ex2.png)

In the main, we have the statements printed that list the questions which next() in place for each result set
previous using yield statements. A variable is set for convenience to call the results of the generator function.

![Generator Example a](https://github.com/ianorourke/dat129_ccac/blob/main/generator_exa.png)
![Generator Example 3](https://github.com/ianorourke/dat129_ccac/blob/main/generator_ex3.png)

As we see, each result is appearing individually. Rather than running the function each time, which can use more memory,
these results are only appear as needed.

![Generator Example 4](https://github.com/ianorourke/dat129_ccac/blob/main/generator_ex4.png)

Until we reach the end. And if we were to add an additional next() that exceeds the yield statements we've set for
the generator function, we get:

![Generator Example 5](https://github.com/ianorourke/dat129_ccac/blob/main/generator_ex5.png)

A StopIteration letting us know that the function is terminated at this point.

Arguably, there are certainly other way a quiz program could be put together, but as you can see from the placement
of next(), these could easily be placed as needed in larger, more complex programs and the results yielded can be
much greater though ultimately, this allows some flexibility with functions that are less demanding on memory and
yield only the results that are requested.

## Other Clauses

In addition to next(), other clauses exist that make use of generators. As described in-depth at Real Python,
these include send(), which produces a generator function that can pass data, close(), which allows you to stop
a generator at a limit you set, and throw(), which utilizes the StopIteration in locating data.
