# The pine tree kata

*Goal: Draw a pine tree in the terminal, experiment with splitting
code in functions and finding algorithms*.


# Specifications

Ask for a size, then draw a pine tree in the terminal, like this:

```
Please enter the width of the pine tree
> 9

    #
   ###
  #####
 #######
#########
    #
    #
```

Note the pine tree is made of 2 parts:

A triangle, starting with a row of one `#` character,
and a line of size 9 at the bottom

The leg, which is always two `#` characters, centered
horizontally.

Hints:

The following code produces a line of 5 `-` characters:

```python
line = '-' * 5
print(line)
# output:
-----
```

You can assume the pine tree size will always be an *odd* number.

# Instructions

* Write the code that produces a pine tree, whatever the size
* Try to split the problem in small functions.

# If it's too hard

You may start with the "easy.py" file.

* First, add the missing code to draw the whole triangle
* Then re-write all hard-coded values to use the `width` variable
  instead
* Finally, remove the hard-coded `width`.

# If it's too easy

It's the holiday season ! Your job is to place some random balls inside
the tree, like this:

```
    #
   ###
  #x###
 #####x#
#x##x####
    #
    #
```
