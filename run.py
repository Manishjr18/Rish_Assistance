import multiprocessing
import subprocess
import time

# Function to run RISH
def startRISH():
    try:
        print("Process 1 is running (RISH).")
        from main import start
        start()  # This should run the RISH system
    except Exception as e:
        print(f"Error in Process 1 (RISH): {e}")

# Function to listen for hotwords
def listenHotword():
    try:
        print("Process 2 is running (Hotword detection).")
        from engine.features import hotword
        hotword()  # This should listen for the hotword
    except Exception as e:
        print(f"Error in Process 2 (Hotword detection): {e}")

# Main program to start both processes
if __name__ == '__main__':
    try:
        # Create two processes
        p1 = multiprocessing.Process(target=startRISH)
        p2 = multiprocessing.Process(target=listenHotword)

        # Start both processes
        p1.start()
        p2.start()

        # Allow processes to run in parallel
        p1.join()  # Wait for process 1 to complete

        # Optionally, terminate process 2 when process 1 completes
        if p2.is_alive():
            print("Terminating Process 2 (Hotword detection)...")
            p2.terminate()  # Terminate hotword detection if it's still running
            p2.join()       # Ensure it's cleaned up

    except KeyboardInterrupt:
        # Handle graceful shutdown
        print("Shutting down processes...")
        p1.terminate()
        p2.terminate()
        p1.join()
        p2.join()

    print("System stopped.")
