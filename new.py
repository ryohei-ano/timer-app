import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.laps = []

    def start(self):
        if self.start_time is None:
            self.start_time = time.time()

    def stop(self):
        if self.start_time is not None:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.laps = []

    def get_time(self):
        if self.start_time is None:
            return self.elapsed_time
        else:
            return self.elapsed_time + time.time() - self.start_time

    def lap(self):
        if self.start_time is not None:
            lap_time = self.get_time()
            self.laps.append(lap_time)
            print(f"Lap {len(self.laps)}: {lap_time:.2f} seconds")

timer = Timer()

def main():
    print("Simple Timer App")
    print("Enter 'start' to start the timer")
    print("Enter 'stop' to stop the timer")
    print("Enter 'lap' to record a lap time")
    print("Enter 'reset' to reset the timer")
    print("Enter 'quit' to quit the app")

    while True:
        user_input = input("> ").lower()
        if user_input == "start":
            timer.start()
            print("Timer started")
        elif user_input == "stop":
            timer.stop()
            print(f"Timer stopped. Elapsed time: {timer.get_time():.2f} seconds")
        elif user_input == "lap":
            timer.lap()
        elif user_input == "reset":
            timer.reset()
            timer.start_time = None  # タイマーを強制的に0秒に戻す
            print("Timer reset")
        elif user_input == "quit":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()