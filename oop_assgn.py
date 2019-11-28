class Students:
    school = "ABC Primary School"

    def __init__(self, jina, math, sci, eng, art, hist):
        self.name = jina
        self.math = int(math)
        self.sci = int(sci)
        self.eng = int(eng)
        self.art = int(art)
        self.hist = int(hist)
        total_marks = math + sci + eng + art + hist
        average = total_marks / 5
        if average < 0:
            print(" Marks don't compute")
        if average > 100:
            print(" Marks don't compute")
        if 100 > average > 79:
            print(jina, total_marks, average, "Grade= A")
        elif 79 > average > 59:
            print(jina, total_marks, average, "Grade= B")
        elif 60 > average > 48:
            print(jina, total_marks, average, "Grade= C")
        elif 49 > average > 39:
            print(jina, total_marks, average, "Grade= D")
        elif 40 > average > 0:
            print(jina, total_marks, average, "Grade= E")


a = Students("Bruce", 39, 12, 24, 14, 60)
