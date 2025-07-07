# MCPS-Missing-Assignments
Get your missing assignments and their grade weight from StudentVUE (Synergy)

# How to run:

hit the controls Win+R
type in "cmd" and hit enter (or open the command promt any other way)

use "cd path/to/file" (replace path/to/file/ with the full path to the program folder (most likely C:/Users/{user}/Downloads/MCPS-Missing-Assignments/)

run the command "./missing"

enter the data it asks for

and you'll have a list of all your missing assingments right there for you :)

# Post-mortem

I wrote this project back in my junior year of high school while I was struggling a lot with my mental health & intrinsic motivation. And despite the fact I'm writing this post mortem a few years later, there's quite a few things I remember from the afternoon I sat down to write this.

There was absolutely ZERO documentation from Synergy when I attempted to write this project. If it wasn't for pythons questionable ability to convert anything into a string on demand, This project would have been SIGNIFICANTLY harder. I remember sitting down thinking "this'll be a 10 minute project and I'll have all the information I need to sit down and get all the still-valid missing assignments in" and it turning into a 4-hour project sifting through dictionary keys trying to find what exactly will give me the data I was looking for. Sadly, I'm not sure if it still works, as my credentials are now expired since I've graduated. 

When I wrote it I initally just wanted it to be simple and maintainable so I could easly add features here or there or easily update it if the API changed, but by hour 2 of trying to do all of this without any documentation on how the API actually worked, all my dreams had gone out the window and I was left with what became this mess. I also remember wanting to make it use some sort of GUI, and I looked into things like Tkinter but I was not ready to learn a whole Library with it's own syntax after what I had just done, so instead I compiled it as a binary to avoid needing to locally install the studentvue api's library, and uploaded it for anyone to download if they needed information on their missing assignments like I did. Hopefully, though, nobody did :)

This was one of the worst projects I've worked on, tbh, and it caused me more headaches than the entirety of my Operating System, Interpreter, and Compiler ***combined.*** No amount of documention on my part could make up for the absolute software nightmare that is StudentVUE. I remember every time I opened it I'd get so annoyed by it and a few times was particularly tempted to simply make my own way of accessing it in its entirety but this project singlehandedly shattered those dreams of a better life, one where you wouldn't be logged out "as a security measure" after logging in 30 seconds ago, one where your grades and assignments would properly display, where unfocusing the tab would not permanently freeze it.
