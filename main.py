class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name):
        self.name = name
        print('Hello, my name is', self.name)

    def change_age(self, age):
        self.age = age
        print('I am', self.age, 'years old.')   

    def add_track(self, track):
        self.track = track
        print('My track is', self.track)

    def get_score(self, score):
        self.score = score
        print('I scored', self.score)
        

Bob = Student("Bob", 20, ["FE", "BE"], 43.5)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(80.3)
