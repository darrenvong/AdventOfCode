### Day 3

## Part 1
No code written so far. For part 1, solved by realising that the leading diagonal
from the centre (i.e. this \ direction) is a sequence of odd squares.

My input
was `**277678**`, which turned out to be on the same line as `527^2 = 277729`. As it was
on the same line as `527^2`, it's `527//2 = 263` vertical steps away from the centre.
For the horizontal distance, since my input is `277729 - 277678 = 51` steps away from
the corner, and as it's a square, we know that the corner (`527^2`) is also
`263` horizontal steps away from the centre. Taking the difference between the number
of steps the corner is from the centre and that of my input number (i.e. `263 - 51 = 212`),
this means that the Manhattan distance between my input and `1` is `212 + 263 = 475`!
