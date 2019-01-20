module topPart(top,wid,height){
	translate([0,0,20])
		cylinder(top,wid,height,center=true);
}
topPart(2,10,10);