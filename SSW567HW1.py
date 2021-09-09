import unittest    
def classify_triangle(a,b,c):
    #Set up variables
    isright= bool
    tritype= ""
    asq= a*a
    bsq= b*b
    csq= c*c

    if(asq+bsq==csq):
        isright=True
    elif(bsq+csq==asq):
        isright=True
    elif(asq+csq==bsq):
        isright=True
    else:
        isright=False

    if(a==b==c):
        tritype = "Equilateral"
    elif(((a+b)<=c) or ((a+c)<=b) or ((b+c)<=a)):
        tritype = "Not A Triangle"
    elif((a==b and b!=c) or (a==c and b!=c) or (b==c and a!=c)):
        tritype = "Isosceles"
    elif(a!=b and b!=c):
        tritype = "Scalene"
    

    if(tritype=="Not A Triangle"):
        return "Not A Triangle"
    elif(isright==True):
        return ("This triangle is Right and " + tritype)
    elif(isright==False):
        return ("This triangle is Not Right and " + tritype)

        
        
def runClassify_triangle(a, b, c):
    print(classify_triangle(a,b,c))


class TestTriangles(unittest.TestCase):

    def test_notATriangle(self): # test invalid inputs
        self.assertNotEqual(classify_triangle(3,4,5),"Not A Triangle")
        self.assertEqual(classify_triangle(3,2,5),"Not A Triangle")
        
    def test_classify_triangle(self): 
        self.assertEqual(classify_triangle(1,1,1),"This triangle is Not Right and Equilateral") #Equilateral test
        self.assertEqual(classify_triangle(5,5,7),"This triangle is Not Right and Isosceles") #Isosceles test w/ not right
        self.assertEqual(classify_triangle(3,4,5),"This triangle is Right and Scalene") #Scalene test w/ right
        self.assertEqual(classify_triangle(3,4,6),"This triangle is Not Right and Scalene") #Scalene test w/ right


if __name__ == '__main__':
    runClassify_triangle(1,2,3) #Not a triangle
    runClassify_triangle(1,1,1) #Equilateral, not right
    runClassify_triangle(3,4,5) #Right scalene
    runClassify_triangle(7,9,12) #Not right scalene
    runClassify_triangle(2,2,3) #Not right isosceles
    unittest.main(exit=False) 
    
    
       
       