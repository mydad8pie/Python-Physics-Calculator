import tkinter as tk
import sys

class PhysicsCalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Physics Calculator")

        # Will create an Entry Feild for the input
        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        #All the buttons in the tkinter gui
        self.force_mass_acceleration_button = tk.Button(root, text="Force, Mass, Acceleration", command=self.working_force_mass_acceleration)
        self.distance_time_speed_button = tk.Button(root, text="Distance, Time, Speed", command=self.working_distance_time_speed)
        self.acceleration_speed_time_button = tk.Button(root, text="Acceleration, Speed, Time", command=self.working_acceleration_speed_time)
        self.stop_button = tk.Button(root, text="Stop Code", command=self.stop_code)

        self.force_mass_acceleration_button.pack()
        self.distance_time_speed_button.pack()
        self.acceleration_speed_time_button.pack()
        self.stop_button.pack()

    def get_input(self):
        # Gets the from the entry field
        return self.input_entry.get()

    def clear_input(self):
        # Clears the input field
        self.input_entry.delete(0,tk.END)


    def working_force_mass_acceleration(self):
        #asks what the users wants to work out
        work_out = input("What do you want to work out?").strip().lower()

        #Calulations for force
        if work_out == "force":
            mass = float(input("Mass (kg):"))
            acceleration = float(input("Acceleration (m/s/s):"))
            force = mass * acceleration
            print(force, "N")

        # Calulations for Mass
        elif work_out == "mass":
            force = float(input("Force (N):"))
            acceleration = float(input("Acceleration (m/s/s):"))
            mass = force / acceleration
            print(mass, "kg")

        # Calulations for acceleration
        elif work_out == "acceleration":
            force = float(input("Force (N):"))
            mass = float(input("Mass (kg):"))
            acceleration = force / mass
            print(acceleration, "m/s/s")

    def working_distance_time_speed(self):
        speed_time = input("What do you want to work out?").strip().lower()

        # Calulations for Distance
        if speed_time == "distance":
            time = float(input("Time (s):"))
            speed = float(input("Speed (m/s):"))
            distance = time * speed
            print(distance, "m")

        # Calulations for Time
        elif speed_time == "time":
            distance = float(input("Distance (m):"))
            speed = float(input("Speed (m/s):"))
            time = distance / speed
            print(time, "s")

        # Calulations for Speed
        elif speed_time == "speed":
            distance = float(input("Distance (m):"))
            time = float(input("Time (s):"))
            speed = distance / time
            print(speed, "m/s")

    def working_acceleration_speed_time(self):
        acceleration_time = input("What do you want to work out?").strip().lower()

        # Calulations for acceleration
        if acceleration_time == "acceleration":
            time = float(input("Time (s):"))
            speed = float(input("Speed (m/s):"))
            acceleration = time * speed
            print(acceleration, "m/s/s")

        # Calulations for Time
        elif acceleration_time == "time":
            acceleration = float(input("Acceleration (m/s/s):"))
            speed = float(input("Speed (m/s):"))
            time = acceleration / speed
            print(time, "s")

        # Calulations for Speed
        elif acceleration_time == "speed":
            acceleration = float(input("Acceleration (m/s/s):"))
            time = float(input("Time (s):"))
            speed = acceleration / time
            print(speed, "m/s/s")

    #will stop the program
    def stop_code(self):
        sys.exit()

#shows that the code can be run
if __name__ == "__main__":
    root = tk.Tk()
    app = PhysicsCalculatorApp(root)
    root.mainloop()
