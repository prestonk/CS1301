//Preston Knibbe
//B7
//pknibbe3@gatech.edu
//903074340
//I worked on the homework assignment alone, using only this semester's course materials
//This object is a top, a popular childrens toy, and I got the idea when seeing how the hull function works

module topTop(a,b,c){
	color([200/255,167/255,105/255])
	translate([0,0,10])
	cube([a,b,c],center=true);
}

color([211/255,42/255,42/255])
hull(){

translate([0,0,5])

	cylinder(10,2,5,center=true);
	sphere([5,5,5]);


}
topTop(.5,.5,10);