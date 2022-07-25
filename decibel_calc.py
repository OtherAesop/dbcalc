import math

class DBCalc:

    def __init__(self, distance: float, destination_db: int=None, source_db: int=None) -> None:
        """Initialize the calc class with the given information. One value must be known and the other must be unknown.
        
        distance: Length in meters between the destination and the source (e.g. 1 meter)
        destination_db: DbA perceived by listener (e.g. 45 DbA)
        source_db: DbA at sound source (e.g. 65 DbA)"""

        self.dist_traveled = distance
        self.db_destination = destination_db
        self.db_source = source_db

        # reference values
        self.I_reference = 1E-12 # W/m^2

    def _db_from_intensity(self, intensity: float) -> float:
        """Get db from intensity measured in watts per square meter."""
        power = max(intensity, 0.0) # no power less than 0
        return 10 * math.log((power/self.I_reference))

    def get_sound_at_source(self) -> float:
        """Returns the volume of the sound at its source in A weighted decibels.
        
        Returns the DbA value as integer when successful or returns None with error messages."""

        pass

    def get_sound_at_destination(self) -> float:
        """Returns the volume of the source sound at the destination in A weighted decibels/
        
        Returns the DbA value as interger when successful or returns None with error messages."""

        pass


if __name__ == "__main__":
    # Driver code

    # You hear a sound a meter away from you that you measure to be 60 dbA at 1 meter, how loud is it at the source?

    db_calc = DBCalc(1.0, destination_db=60)
    print(f"You hear a sound a meter away from you that you measure to be 60 dbA at 1 meter, how loud is it at the source?")
    print(f"A 60 dbA sound 1 meter away from the source is {db_calc.get_sound_at_source()} dbA at the source.")

    db_calc = DBCalc(2.0, source_db=60)
    print(f"You hear a sound that is 60 dbA at the source from 2 meters away. How loud is it when it reaches your ear?")
    print(f"A 60 dbA sound is {db_calc.get_sound_at_destination()} dbA when you are 2 meters away from the source.")

    # 110 source, .6 m dist