import gmplot
import haversine as hvs

#create map Showalter Location
gmap = gmplot.GoogleMapPlotter(39.168451, -86.51891,15)

#Lindley Hall where we have C200
l1 = (39.165341, -86.523588)
#Luddy Hall the new SICE building
l2 = (39.172725, -86.523295)
#Eigenmann Hall
l3 = (39.1710, -86.5088)
#Ballantine Hall
l4 = (39.1661, -86.5210)
#SRSC 
l5 = (39.1734, -86.5123)
#Jordan Hall
l6 = (39.1648, -86.5211)

#list of points
lats = [l1[0],l2[0],l3[0],l4[0],l5[0],l6[0]]
lons = [l1[1],l2[1],l3[1],l4[1],l5[1],l6[1]]

def markers():
    for i in range(0,lats):
        def shortest(loc1, loc2):
            loc1 = lats[i]
            loc2 = lons[i]
            hvs.dd(loc1,loc2)



x = hvs.hd(l1,l2)
x1 = hvs.hd(l1,l3) 
x2 = hvs.hd(l1,l4) 
x3 = hvs.hd(l1,l5) 
x4 = hvs.hd(l1,l6) #shortest 
y = hvs.hd(l2,l3) 
y1 = hvs.hd(l2,l4) 
y2 = hvs.hd(l2,l5) 
y3 = hvs.hd(l2,l6)
z = hvs.hd(l3,l4)
z1 = hvs.hd(l3,l5)
z2 = hvs.hd(l3,l6)
xy = hvs.hd(l4,l5)
xy1 = hvs.hd(l4,l6)
xyz = hvs.hd(l5,l6)

lats1 = [l1[0],l6[0]]
lons1 = [l1[1],l6[1]]




#add points to map
gmap.scatter(lats,lons,'red',size=30, marker=False)
#add line
gmap.plot(lats1,lons1,'cornflowerblue', size=30, marker=False)
#save to map
gmap.draw("hellokitty.html")
