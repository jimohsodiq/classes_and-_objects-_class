class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name  = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, new_name):
        self.name = new_name
        print("The new name inputted is", new_name)

    def change_age(self, new_age):
        self.name = new_age
        print("The new age inputted is", new_age)

    def add_track(self, new_tracks):
        self.name = new_tracks
        print("The new track inputted is", new_tracks)

    def get_score(self, new_score):
        self.name = new_score
        print("The new score inputted is", new_score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(30.5)
