#please input all time with the unit of second
class triathlon:
    def __init__(self, first_name, last_name, location, swim, cycle, run):
        self.s = swim
        self.c = cycle
        self.r = run
        self.f = first_name
        self.l = last_name
        self.lo = location
    def out_put(self):
        print("Name:", self.f, self.l," Location:", self.lo, " Time for swim:", self.s," Time for cycle:", self.c, " Time for run:", self.r," Total time over the triathlon:", self.c + self.r + self.s)
#an example
member1 = triathlon('Tutu', 'Jiang', 'Beijing', 100, 100, 200)
member1.out_put()

