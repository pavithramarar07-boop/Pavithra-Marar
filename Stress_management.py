import time
import random

def box_breathing():
    """Guides the user through a 1-minute box breathing cycle."""
    print("\n--- Box Breathing Exercise ---")
    print("Find a comfortable seated position. We will do 3 cycles.")
    print("Inhale (4s) -> Hold (4s) -> Exhale (4s) -> Hold (4s)\n")
    
    time.sleep(2)
    
    for cycle in range(1, 4):
        print(f"--- Cycle {cycle} of 3 ---")
        
        print("Breathe IN slowly... (4 seconds)")
        for i in range(4, 0, -1):
            print(f"{i}...", end="\r", flush=True)
            time.sleep(1)
        print("             ", end="\r")
        
        print("HOLD your breath... (4 seconds)")
        for i in range(4, 0, -1):
            print(f"{i}...", end="\r", flush=True)
            time.sleep(1)
        print("             ", end="\r")
        
        print("Exhale OUT slowly... (4 seconds)")
        for i in range(4, 0, -1):
            print(f"{i}...", end="\r", flush=True)
            time.sleep(1)
        print("             ", end="\r")
        
        print("HOLD empty... (4 seconds)")
        for i in range(4, 0, -1):
            print(f"{i}...", end="\r", flush=True)
            time.sleep(1)
        print("             ", end="\r")
        
    print("Great job! Notice how your body feels right now.\n")

def brain_dump():
    """Allows the user to write down what's bothering them to clear their mind."""
    print("\n--- Brain Dump Journaling ---")
    print("Get it out of your head. Type what is stressing you out right now.")
    thought = input("What's on your mind? (Press Enter when done): ")
    print("\nThank you for sharing. Acknowledging the stress is the first step to letting it go.")
    print("Take a deep breath. You don't have to solve everything right this second.\n")

def get_affirmation():
    """Provides a randomized calming affirmation."""
    affirmations = [
        "This moment will pass, and I am doing the best I can.",
        "I have survived 100% of my hardest days so far.",
        "Peace begins the moment I choose to let go of what I cannot control.",
        "I am allowed to take things one step at a time.",
        "My worth is not measured by my productivity."
    ]
    print("\n--- Daily Affirmation ---")
    print(f'"{random.choice(affirmations)}"\n')

def main():
    print("========================================")
    print("   Welcome to Your Python Stress Relief  ")
    print("========================================")
    
    while True:
        print("\nChoose an option:")
        print("1. Do Box Breathing Exercise (1 min)")
        print("2. Do a Quick Brain Dump (Journaling)")
        print("3. Read a Calming Affirmation")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            box_breathing()
        elif choice == '2':
            brain_dump()
        elif choice == '3':
            get_affirmation()
        elif choice == '4':
            print("\nTake care of yourself! Goodbye. 🌿")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
