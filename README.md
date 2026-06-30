# My Stupid Little Cute Tamagotchi 

Hellooo everyone ! Welcome to my first real python GUI project that i made  for Hack Club's beest program . This is a very cute, with light theme's colors Tamagotchi virtual pet . I spent around 20 hours learning, suffering, and building this from!

## So What is this thing exactly ?
It's a small desktop game where you adopt a little cute pet. You have to monitor its vital signs like :
*Hunger: If it drops to 0, your pet goes to heaven(it meansss it diesss )!! 
*Happiness:  Keep it high by playing, or it will cryyy!! 
*Energy:  Playing makes it tired. Send it to sleep to recharge its battery!!!

---

##Now  The Tech Stack : 
* **Language:** Python 3
* **GUI Library:** `customtkinter` (for modern looking rounded buttons and cool pastel themes instead of the old boringg grey standard tkinter)
* **Logic Architecture:** `threading` (Multi-threading was mandatory so the 3-second background life loop doesn't freeze the graphic window button clicks!).

---

## 😭 My Story & Why I have low commits (Please Read!)
I am a beginner and I don't know how to use Git perfectly yet. 

I spent **days** trying to make Python and Git work on my local Windows computer, but I kept getting red errors in my terminal and couldn't install `customtkinter` properly sadly . Because I was stuck, I did not commit anything for hours and hours. I was just reading my *Python Crash Course* book, fighting bugs, and testing code locally without saving it online.

At the very end, to fix my environment problems, I moved my code into **GitHub Codespaces** (I write it before in VS code but since idk how to put it to github directly I moved my code to codespaces ) which finally worked! That's why it looks like everything was made at the same time (vibecoded), but it's not! It's just the result of 20 hours of hard learning, crying over windows environment paths, and fixing the code until it was perfect.

---

## How to use my App

###  Option 1: The Quick Executable (Theee Easiest !)!
Go to the **(https://github.com/yassminehjb/my-first-python-project)** tab of this repository, download the `Tamagotchi.exe` file, and double click it! It works instantly on Windows.

###  Option 2: Run via Source Code:
If you want to run the python code directly:
1. Install the requirements:
   ```bash
   pip install customtkinter
