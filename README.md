# Design considerations in python [WIP]

Python is a language heavily utilised in the data landscape today, yet numerous projects, repositories and applications
suffer with a litany of bad practices, non-optimal designs, and anti-patterns.

Such issues in large part aren't suprising - python is the non-programmer's programming language. Its popularity and low
barriers to entry should be celebrated, but having large swathes of the community coming from non software oriented 
backgrounds brings challenges.

This repo outlines a handful of good practices for production ready python applications. It is by no means attempts to 
be an authoritative resource, and will likely deprecate as the language and ecosystem evolves. But, it hopefully offers:

1) Some useful considerations and examples of practice for those moving from local development work, to productionised code
2) Examples of why we should care about getting these practices right
3) Highlights of problems we wish to avoid

# Who is this repository useful for?

This repository and the patterns outlined are primarily aimed at reasonably python-proficient professionals, who can 
write code to achieve lots of tasks, but who've never actually been taught how to do the following:

1) Future-proof a python project, making it maintainable, documented, and avoiding development conflicts
2) Productionise python applications, so they can be easily containerised to run elsewhere than someone's local machine
3) Design their development to fit in a larger technical design

# Resources

The contents and practices outlined in this repo are in stand-alone documents, with a wrap up section to bring it all together

> 1. [Good practices: linters, formatters, and their enforcement](/docs/Linting-formatting-enforcing.md)
> 2. [Well documented code: Type hinting, docstrings, comments and documentation tools](docs/Well-documented-code.md)
> 3. [Application architecture: How to structure a repo to ship your code anywhere](/docs/Application-architecture-packaging.md)
> 4. [Loggers and application exceptions: Keep your application healthy, or at least know why it's sick](/docs/Logging-and-exceptions.md)