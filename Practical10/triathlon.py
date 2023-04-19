#please input all time with the unit of second
class triathlon:
    def __init__(self, first_name, last_name, location, swim, cycle, run):
        self.s = swim
        self.c = cycle
        self.r = run
        self.f = first_name
        self.l = last_name
        self.lo = location
        self.total = swim + cycle + run
    def out_put(self):
        print("Name:", self.f, self.l," Location:", self.lo, " Time for swim:", self.s," Time for cycle:", self.c, " Time for run:", self.r," Total time over the triathlon:", self.total)
#an example
member1 = triathlon('Tutu', 'Jiang', 'Beijing', 100, 100, 200)
member1.out_put()
#Name: Tutu Jiang  Location: Beijing  Time for swim: 100  Time for cycle: 100  Time for run: 200  Total time over the triathlon: 400
