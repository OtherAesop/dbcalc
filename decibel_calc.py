import math
import argparse

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
        self.source_dist = .1 # meters
        self.min_intensity = 3.1622776601683794E-15 # -25dbA is the minimum value we can return
        self.min_db = -25

    def _db_from_intensity(self, intensity: float) -> float:
        """Get db from intensity measured in watts per square meter.
        
        Minimum return value is -25"""
        power = max(intensity, self.min_intensity) # min output is -25 dbA
        return 10 * math.log((power/self.I_reference), 10)

    def _intensity_from_db(self, dbA: float) -> float:
        """Get intensity in w/m^2 from a value measured in A weighted decibels.
        
        Minimum return value is 3.1622776601683794E-15"""
        db = max(dbA, self.min_db)
        return math.pow(10, db/10) * self.I_reference

    def get_sound_at_source(self) -> float:
        """Returns the volume of the sound at its source in A weighted decibels.
        
        Returns the DbA value when successful or returns None with error messages."""

        assert self.db_destination, "You must give the dbA at the destination to call `get_sound_at_source`"        

        return max(self.db_destination + (20 * math.log(self.dist_traveled/self.source_dist, 10)), self.min_db)

    def get_sound_at_destination(self) -> float:
        """Returns the volume of the source sound at the destination in A weighted decibels
        
        Returns the DbA value when successful or returns None with error messages."""

        assert self.db_source, "You must give the dbA at the source to call `get_sound_at_destination`"

        return max(self.db_source + (20 * math.log(self.source_dist/self.dist_traveled, 10)), self.min_db)


if __name__ == "__main__":
    # Driver code

    # These lines illustrate usage & concept

    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-c','--calculate', help='calculation mode', choices=['source', 'destination'], required=True)
    parser.add_argument('-s','--source', help='Volume at the source in dbA', type=float, required=True)
    parser.add_argument('-d','--destination', help='Volume at the desintation in dbA', type=float, required=True)
    parser.add_argument('-D','--distance', help='Distance from the source to the destination in meters', type=float, required=True)
    args = vars(parser.parse_args())


    db_calc = DBCalc(args["distance"], args["destination"], args["source"])
    
    if args["calculate"] == "source":
        print(f'A {args["destination"]} dbA sound is {round(db_calc.get_sound_at_source(), 2)} dbA at its source {args["distance"]} meter(s) away.')
    elif args["calculate"] == "destination":
        print(f'A {args["source"]} dbA sound is {round(db_calc.get_sound_at_destination(), 2)} dbA after travelling {args["distance"]} meter(s).')
    else:
        print(f"uhhhh this is probably a bug... {args}")


    # You hear a sound that is 110 dbA at the source from 2/3 meters away. How loud is it when it reaches your ear?
    # 110 source, .6906 m dist -> 94.3 dbA
    #source = 110 # dbA
    #dist = .6096 # meters
    #db_calc = DBCalc(dist, source_db=source)
    #print(f"A {source} dbA sound is {round(db_calc.get_sound_at_destination(), 2)} dbA after travelling {dist} meter(s).")

    # You hear a sound a meter away from you that you measure to be 60 dbA at 1 meter, how loud is it at the source?
    # 60 destination, 1 m dist -> 80 dbA
    #dest = 60 # dbA
    #dist_to_source = 1 # meters
    #db_calc = DBCalc(dist_to_source, destination_db=dest)
    #print(f"A {dest} dbA sound is {round(db_calc.get_sound_at_source(), 2)} dbA at its source {dist_to_source} meter(s) away.")

    #dest = 40 # dbA
    #dist_to_source = 1 # meters
    #db_calc = DBCalc(dist_to_source, destination_db=dest)
    #print(f"A {dest} dbA sound is {round(db_calc.get_sound_at_source(), 2)} dbA at its source {dist_to_source} meter(s) away.")

    #source = 60 # dbA
    #dist = 1 # meters
    #db_calc = DBCalc(dist, source_db=source)
    #print(f"A {source} dbA sound is {round(db_calc.get_sound_at_destination(), 2)} dbA after travelling {dist} meter(s).")

    #source = 71 # dbA
    #dist = .2 # meters
    #db_calc = DBCalc(dist, source_db=source)
    #print(f"A {source} dbA sound is {round(db_calc.get_sound_at_destination(), 2)} dbA after travelling {dist} meter(s).")