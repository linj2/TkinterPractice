"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jing Lin.
"""  # TODONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()
    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=100)
    frame1.grid()
    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    print_hello_button = ttk.Button(frame1, text='Print Hello')
    print_hello_button.grid()
    # ------------------------------------------------------------------
    # TODO: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    print_hello_button['command'] = lambda: print('Hello')
    # ------------------------------------------------------------------
    # TODO: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    an_entry_box = ttk.Entry(frame1)
    an_entry_box.grid()

    print_entry_button = ttk.Button(frame1, text='Print entry')
    print_entry_button['command'] = lambda: print_contents(an_entry_box)
    print_entry_button.grid()
    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    second_entry_box = ttk.Entry(frame1)
    second_entry_box.grid()

    print_N_button = ttk.Button(frame1, text='Print N times from first entry')
    print_N_button['command'] = lambda: print_N_times(an_entry_box,second_entry_box)
    print_N_button.grid()
    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    root.mainloop()


def print_contents(entry_box):
    contents_of_entry_box = entry_box.get()
    if contents_of_entry_box == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def print_N_times(first_entry, second_entry):
    contents = first_entry.get()
    n = int(second_entry.get())
    for k in range(n):
        print(contents)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
