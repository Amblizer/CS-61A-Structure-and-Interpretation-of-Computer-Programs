<!-- TOC -->

- [Notes on Composing Programs](#notes-on-composing-programs)
    - [1.1 Start](#11-start)
    - [1.2 ELements of programming](#12-elements-of-programming)

<!-- /TOC -->

# Notes on Composing Programs

ref: [Structure and Interpretation of Computer Programs][ref1]

<!-- link -->
[ref1]:http://mitpress.mit.edu/sicp

## 1.1 Start

1. Priciples: beauty, simplicity and readability

2. Definitions:
    - Statements: codes usually describe actions
    - Expressions: codes do computations
    - Functions: a box of series of statements and/or expressions
    - Objects: data and its unalienable properties
    - Interpreters: to evaluate compound expressions in a predictable way

    >functions are objects, objects are functions, and interpreters are instances of both.

3. Expect errors:
    - Debugging: know error itself and dignose it
    - Priciples of debugging:
        - Test incrementally, identify probles early and easily
        - Isolate errors, localise according to output
        - Check assumptions, make sure assumptions check with codes precisely
        - Peer consulting, chart of valuable helpers

            Name|Specialize
            ---|---
            [Official Py Documentation][st1]|Everything

>The fundamental equation of computers is:
>
>computer = powerful + stupid
>
>Programming is about a person using their real insight to build something that the computer can do.
>
>— Francisco Cai and Nick Parlante, Stanford CS101

<!-- links -->
[st1]:https://docs.python.org/3/index.html

## 1.2 ELements of programming

1. Aims programming serves:
    - instruction to a computer
    - a framework of ideas, which is mor important

1. Notice means to combine simple expresions and statement to complex combination and abstractions

1. Expression: operators and operands
    - with infix notation, eg. 1/2 + (1/4 + 1/8 + 1/16) + 1/32 + 1/64 + 1/128
    - with function notaton, eg. max(min(1, -2), min(pow(3, 5), -4)), and have __THREE__ advantages over infix ones:
        - arbitary number of arguments
        - nested expressions in a straightforward way
        - easy to type, no limit to kinds

1. Definitions:
    - '=': assignment operator
    - names: variable nams
    - trees: grow from the top down

1. Pure and non-pure functions
    - _Pure function_ have no side effects beyond return a value, call it for arbitary times with the same arguments must return same values.
    - _Non-pure function_ have side effects
    - Advantages of pure over non-pure:
        - more reliable to compose
        - simpler to test
        - essential for concurrent programs

>_The Zen of Python_ by Tim Peters
>
>Beautiful is better than ugly.
>Explicit is better than implicit.
>Simple is better than complex.
>Complex is better than complicated.
>Flat is better than nested.
>Sparse is better than dense.
>Readability counts.
>Special cases aren't special enough to break the rules.
>Although practicality beats purity.
>Errors should never pass silently.
>Unless explicitly silenced.
>In the face of ambiguity, refuse the temptation to guess.
>There should be one-- and preferably only one --obvious way to >do it.
>Although that way may not be obvious at first unless you're >Dutch.
>Now is better than never.
>Although never is often better than *right* now.
>If the implementation is hard to explain, it's a bad idea.
>If the implementation is easy to explain, it may be a good >idea.
>Namespaces are one honking great idea -- let's do more of those!