import customtkinter as ctk
import time
import threading

# Main window configuration
ctk.set_appearance_mode("light") 
app = ctk.CTk()
app.title("My stupid little Tamagotchi ✨")
app.geometry("400x600")
app.configure(fg_color="#FFF0F5") # Pastel pink background

# --- STATE VARIABLES (Tamagotchi stats) ---
hunger = 80       # 100 = Full belly, 0 = Starving
happiness = 80    # 100 = Super joyful, 0 = Total depression
energy = 80       # 100 = Full of energy, 0 = Exhausted
is_sleeping = False
age = 0
survival_score = 0
game_over = False

# --- ANIMATION "EMOJIS" (Text pixel-art) ---
AVATARS = {
    "HAPPY":  "( 👁️ 💖 👁️ )\n      🍉  ",
    "NORMAL": "( 👁️ ‿ 👁️ )\n      🧁  ",
    "HUNGRY": "( 👁️ 🍙 👁️ )\n      💬  ",
    "SAD":    "( 😭 💦 😭 )\n      💔  ",
    "SLEEPING": "( 💤 ⭕ 💤 )\n   🤖💤 ",
    "DEAD":   "(  ✖  _  ✖  )\n   💀🪦💀 "
}

# --- AVATAR UPDATE FUNCTION ---
def update_avatar():
    if game_over:
        label_avatar.configure(text=AVATARS["DEAD"], text_color="#8B0000")
        return
    if is_sleeping:
        label_avatar.configure(text=AVATARS["SLEEPING"], text_color="#4682B4")
        return
    
    # Choose expression based on stats
    if hunger < 30 or happiness < 30:
        label_avatar.configure(text=AVATARS["SAD"], text_color="#BA55D3")
    elif hunger < 60:
        label_avatar.configure(text=AVATARS["HUNGRY"], text_color="#FF8C00")
    elif happiness > 75:
        label_avatar.configure(text=AVATARS["HAPPY"], text_color="#FF69B4")
    else:
        label_avatar.configure(text=AVATARS["NORMAL"], text_color="#4A4A4A")

# --- PLAYER ACTIONS ---
def feed():
    global hunger, survival_score
    if game_over or is_sleeping: return
    if hunger < 100:
        hunger = min(100, hunger + 15)
        survival_score += 5
        label_notif.configure(text="Yum! A delicious cupcake! 🧁", text_color="#FF1493")
        update_ui()

def play():
    global happiness, energy, survival_score
    if game_over or is_sleeping: return
    if energy < 20:
        label_notif.configure(text="Too tired to play... 💤", text_color="#FF4500")
        return
    
    happiness = min(100, happiness + 20)
    energy = max(0, energy - 15)
    survival_score += 10
    label_notif.configure(text="Yay! We're having so much fun! 🎈", text_color="#008080")
    update_ui()

def sleep():
    global is_sleeping
    if game_over: return
    is_sleeping = not is_sleeping
    if is_sleeping:
        label_notif.configure(text="Shhh... Sleeping... 🌙", text_color="#4682B4")
        btn_feed.configure(state="disabled")
        btn_play.configure(state="disabled")
        btn_sleep.configure(text="Wake up ☀️", fg_color="#4682B4")
    else:
        label_notif.configure(text="Good morning! ☀️", text_color="#FF8C00")
        btn_feed.configure(state="normal")
        btn_play.configure(state="normal")
        btn_sleep.configure(text="Go to sleep 🌙", fg_color="#A9A9A9")
    update_ui()

# --- LIFE CYCLE LOOP (The core engine) ---
def life_cycle():
    global hunger, happiness, energy, age, game_over, survival_score
    while not game_over:
        time.sleep(3) # Time passes every 3 seconds!
        
        if is_sleeping:
            energy = min(100, energy + 15)
            hunger = max(0, hunger - 2) # Hunger drops slower while sleeping
        else:
            hunger = max(0, hunger - 5)
            happiness = max(0, happiness - 4)
            energy = max(0, energy - 3)
            survival_score += 1
            age += 1
            
        # Game Over Check
        if hunger <= 0 or happiness <= 0:
            game_over = True
            label_notif.configure(text="Oh no... Your Tamagotchi went to heaven 👼", text_color="red")
            btn_feed.configure(state="disabled")
            btn_play.configure(state="disabled")
            btn_sleep.configure(state="disabled")
            
        update_ui()

def update_ui():
    # Update progress bars and avatar look
    progress_hunger.set(hunger / 100)
    progress_happiness.set(happiness / 100)
    progress_energy.set(energy / 100)
    
    label_age.configure(text=f"Age: {age} yrs  |  Score: {survival_score} pts")
    update_avatar()

# --- GRAPHICAL USER INTERFACE ---

# Title & Score
title = ctk.CTkLabel(app, text="✨ MY CUTE TAMAGOTCHI ✨", font=("Comic Sans MS", 20, "bold"), text_color="#DB7093")
title.pack(pady=10)

label_age = ctk.CTkLabel(app, text="Age: 0 yrs  |  Score: 0 pts", font=("Arial", 12, "bold"), text_color="#696969")
label_age.pack()

# Avatar Window
label_avatar = ctk.CTkLabel(app, text=AVATARS["NORMAL"], font=("Courier", 45, "bold"), text_color="#4A4A4A")
label_avatar.pack(pady=30)

# Notifications / Status Message
label_notif = ctk.CTkLabel(app, text="Welcome! Take good care of me 🥰", font=("Arial", 13, "italic"), text_color="#DB7093")
label_notif.pack(pady=5)

# --- STATS BARS (Progress Bars) ---
# Hunger
ctk.CTkLabel(app, text="🍗 Hunger / Satiety:", font=("Arial", 12, "bold")).pack(anchor="w", padx=40)
progress_hunger = ctk.CTkProgressBar(app, width=320, progress_color="#FF6B6B", fg_color="#E0E0E0")
progress_hunger.pack(pady=5)

# Happiness
ctk.CTkLabel(app, text="💖 Happiness:", font=("Arial", 12, "bold")).pack(anchor="w", padx=40)
progress_happiness = ctk.CTkProgressBar(app, width=320, progress_color="#FF8EBB", fg_color="#E0E0E0")
progress_happiness.pack(pady=5)

# Energy
ctk.CTkLabel(app, text="⚡ Energy:", font=("Arial", 12, "bold")).pack(anchor="w", padx=40)
progress_energy = ctk.CTkProgressBar(app, width=320, progress_color="#FFD93D", fg_color="#E0E0E0")
progress_energy.pack(pady=5)

# --- ACTION BUTTONS ---
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=30)

btn_feed = ctk.CTkButton(button_frame, text="Feed 🧁", command=feed, width=100, fg_color="#FFB6C1", hover_color="#FF69B4", text_color="white", font=("Arial", 12, "bold"))
btn_feed.grid(row=0, column=0, padx=5)

btn_play = ctk.CTkButton(button_frame, text="Play 🎈", command=play, width=100, fg_color="#87CEFA", hover_color="#1E90FF", text_color="white", font=("Arial", 12, "bold"))
btn_play.grid(row=0, column=1, padx=5)

btn_sleep = ctk.CTkButton(button_frame, text="Go to sleep 🌙", command=sleep, width=100, fg_color="#A9A9A9", hover_color="#708090", text_color="white", font=("Arial", 12, "bold"))
btn_sleep.grid(row=0, column=2, padx=5)

# Initialize display values
update_ui()

# Run the background life cycle thread so it doesn't freeze the main UI loop!
time_thread = threading.Thread(target=life_cycle, daemon=True)
time_thread.start()

app.mainloop()