class Tarantula:
    def __init__(self, arm_length, leg_length, eye_count, has_tail, is_furry):
        """Initializes the physical parameters of the Tarantula."""
        # In arachnids, 'arms' often refer to the pedipalps
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.eye_count = int(eye_count)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)

    def describe_physical_traits(self):
        """Prints out and describes the data members of the tarantula."""
        print("--- Tarantula Physical Profile ---")
        print(f"Pedipalp (Arm) Length: {self.arm_length} cm")
        print(f"Walking Leg Length:    {self.leg_length} cm")
        print(f"Number of Eyes:        {self.eye_count}")
        print(f"Possesses a Tail:      {'Yes' if self.has_tail else 'No'}")
        print(f"Is it Furry/Hairy:     {'Yes (Urticating hairs)' if self.is_furry else 'No'}")
        print("----------------------------------")

def main():
    # Creating an instance of a Mexican Redknee Tarantula
    # Note: Tarantulas actually have 8 eyes and are very 'furry'!
    pet_tarantula = Tarantula(
        arm_length=2.5, 
        leg_length=6.0, 
        eye_count=8, 
        has_tail=False, 
        is_furry=True
    )

    # Calling the member function to describe the animal
    pet_tarantula.describe_physical_traits()

if __name__ == "__main__":
    main()