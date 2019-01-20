#Preston Knibbe
#B7
#pknibbe3@gatech.edu
#903074340
#I worked on the homework assignment alone, using only this semester's course materials



from Graphics import *
area= Window("Face", 500, 600)

head = Oval((250, 350), 175, 200)
head.fill = Color(240,221,180)
head.draw(area)

eye1 = Oval((190, 320), 30, 20)
eye1.fill = Color("white")
eye1.draw(area)

iris1 = Circle((190, 320), 9)
iris1.fill = Color("lightblue")
iris1.draw(area)

pupil1 = Circle((190, 320), 3)
pupil1.fill = Color("black")
pupil1.draw(area)



eye2 = Oval((320, 320), 30, 20)
eye2.fill = Color("white")
eye2.draw(area)

iris2 = Circle((320, 320), 9)
iris2.fill = Color("lightblue")
iris2.draw(area)

pupil2 = Circle((320, 320), 3)
pupil2.fill = Color("black")
pupil2.draw(area)


mouth = Arc((250,380), 90, 360+20, 360-200)
mouth.border = 3
mouth.draw(area)

nose = Polygon((243,310),(258,310),(275,385),(225,385))
nose.fill = Color(244,216,157)
nose.outline = Color(188,157,91)
nose.draw(area)

hat = Polygon((180,100),(320,100),(400,240),(100,240))
hat.fill = Color(230,85,85)
hat.draw(area)

hathair = Line((250,98),(200,50))
hathair.outline = Color(229,227,89)
hathair.border = 3
hathair.draw(area)

hathair2 = Line((250,98),(300,50))
hathair2.outline = Color(229,227,89)
hathair2.border = 3
hathair2.draw(area)

hathair3 = Line((250,98),(250,20))
hathair3.outline = Color(229,227,89)
hathair3.border = 3
hathair3.draw(area)










