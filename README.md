# convert/

### What is it?
A simple command-line program that converts Celsius to Fahrenheit and vice-versa.

### How do I use it?
1. Open `Shell` (not `Console`) from the Replit `Tools` pane.
2. At the command line, type,e.g., `python convert f 212` to get 212 Fahrenheit in Celsius degrees.\
To convert a Celsius temperature to Fahrenheit, type, e.g., `python convert c 100`.

(*Hint: Input numbers you don't already know the answers to.*)

### Why did you make `temp` a subpackage when it only needs to be a module? You look like a Dodo bird.
Practice was the impetus for this small project. I recently wrecked a Replit project using command line tools like `poetry`. It almost scared me away from using this fine IDE, so I wanted to make myself comfortable using `poetry` at the command line in Replit's `nix` environment. I also wanted to understand better how to make packages and subpackages. And I wanted to play a bit at using `argparse` and `rich`.

### Your code is too complicated for the work it does. You look like a one-legged kangaroo.
Yes... I wanted to try using `argparse.subparser`, which was sort of fun, but I discovered afterward that this choice seemed to complicate parsing user input within the App class (I'm referring to the `hasattr` nonsense in the App class and related repetitive code).
If I had recalled that argparse differentiates between positional and optional arguments, I think I could have written a more straightforward App class.

What can I say? I'm a noob.

I won't likely fix either of these mistakes but do welcome any other suggestions you may have to make my code more Pythonic and efficient, if you want to share them.

### Your program sucks!
But nothing quite sucks like your mother. I mean, I've never experienced anything li--

### Leave my mother out of this!
I'm afraid it's too late for that, son.

### So long, farewell, auf wiedersehen, good day!
[David Casson](dvcasson@outlook.com), June 3, 2023.