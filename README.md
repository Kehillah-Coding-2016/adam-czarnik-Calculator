## Calculator

Here you will design your own calculator using python.  This is a totally open-ended project.  Be sure to review the rubrics regarding projects.

### Ideas

Your calculator should take user input in some fashion.  This can be as simple as taking input as strings from the command line, or as sophisticated as creating a [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) with [TkInter](https://youtu.be/RJB1Ek2Ko_Y) or [Kivy](https://kivy.org/).

If you are not sure where to start, try starting with printing a menu of options for the user to choose from, and then handling their input.  Once you have a menu system in place, consider using something like the `os.system('cls')` or `os.system('clear')` to make your program clean and fancy!

### A note on `eval()`

The `eval()` function in python takes a string as an argument, and evaluates it as actual python code.  For example, 
```
s = '4*7+1'
print(s)
print(eval(s))
```
would produce the following output:
```
'4*7+1'
29
```
*You are not supposed to use `eval()` in your calculator program*.  Instead, parse user input, perhaps using some of the string methods we have learned in class, to compute calculations for the user.

