# Time Monster
Timer, the Time Monster is ready to evaluate your code...

## Requirements
This project is fully compatible with [Python 3]. You can alternatively install it using [pyenv].

## Must know
Timer is a very opinionated implementation of the built-in timeit library. It only uses 4 optional parameters, which you are totally free to extend... Let's see what they do:
- `name`: This is how you will identify the code you are evaluating, the default name is "Johan", we recommend you to watch "Monster" anime to understand why. If you already know, you're a person of culture.
- `setup`: This piece of code will execute ONLY once, at the beginning.
- `code`: This will execute right after `setup`, as many times as you wish.
- `times`: The number of times your code will run.

## Getting Started

1. Copy and paste `time_monster` directory to your project's directory, then you'll be able to import Timer anywhere in your project this way:
```
from time_monster.timer import Timer
```
2. Add `setup` and `code` variables 
```
setup = """
my_dictionary = {
    'a': 1,
    'b': 3,
    'c': 5,
    'd': 7,
    'w': 9,
}
"""
code = """
{my_dictionary.update(**{k: v*2}) for (k,v) in my_dictionary.items()}
"""
```
> Note: Remember you can use all or none of the parameters!
3. Create a timer instance using the parameters you just stored in the 2 variables above.
```
timer = Timer(code=code, name=name)
```
4. Log the results.
```
timer.log()
```
5. Run the file you just added this code to!


## Run more examples
You can experiment with different examples with `run_examples.py`, just enter this project's root and run `python run_examples.py`, you should get a similar result to this one:
```
Loop range
0.19552032600040548
Loop repeat
0.06649102800292894
Loop 2 lists using zip
0.0007736089901300147
Loop 2 lists using range
0.0005506189918378368
Loop 2 lists using range (hardcoded list length)
0.0005270730034681037
```

[Python 3]: <https://www.python.org/downloads/>
[pyenv]: <https://github.com/pyenv/pyenv#installation>
