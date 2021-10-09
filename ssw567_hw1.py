"""System module."""
import unittest
def classify_triangle(input_a,input_b,input_c):
    """Main function to define triangle"""
    isright= bool
    tritype= ""
    asq= input_a*input_a
    bsq= input_b*input_b
    csq= input_c*input_c

    if asq+bsq==csq:
        isright=True
    elif bsq+csq==asq:
        isright=True
    elif asq+csq==bsq:
        isright=True
    else:
        isright=False

    if input_a==input_b==input_c:
        tritype = "Equilateral"
    elif(((input_a+input_b)<=input_c) or ((input_a+input_c)<=input_b)
        or ((input_b+input_c)<=input_a)):
        tritype = "Not A Triangle"
    elif((input_a==input_b and input_b!=input_c) or (input_a==input_c and input_b!=input_c)):
        tritype = "Isosceles"
    elif (input_b==input_c and input_a!=input_c):
        tritype = "Isosceles"
    elif input_b not in (input_a, input_c):
        tritype = "Scalene"
    if tritype=="Not A Triangle":
        return "Not A Triangle"
    if isright is True:
        return "This triangle is Right and " + tritype
    return "This triangle is Not Right and " + tritype
def runclassify_triangle(input_a, input_b, input_c):
    """Function to print classify_triangle"""
    print(classify_triangle(input_a,input_b,input_c))


class TestTriangles(unittest.TestCase):
    """Class for unit tests"""
    def test_notatriangle(self):
        """Invalid inputs test"""
        self.assertNotEqual(classify_triangle(3,4,5),"Not A Triangle")
        self.assertEqual(classify_triangle(3,2,5),"Not A Triangle")
    def test_classify_triangle(self):
        """Main function tests"""
        self.assertEqual(classify_triangle(1,1,1),
        "This triangle is Not Right and Equilateral") #Equilateral test
        self.assertEqual(classify_triangle(5,5,7),
        "This triangle is Not Right and Isosceles") #Isosceles test w/ not right
        self.assertEqual(classify_triangle(3,4,5),
        "This triangle is Right and Scalene") #Scalene test w/ right
        self.assertEqual(classify_triangle(3,4,6),
        "This triangle is Not Right and Scalene") #Scalene test w/ right


if __name__ == '__main__':
    runclassify_triangle(1,2,3) #Not input_a triangle
    runclassify_triangle(1,1,1) #Equilateral, not right
    runclassify_triangle(3,4,5) #Right scalene
    runclassify_triangle(7,9,12) #Not right scalene
    runclassify_triangle(2,2,3) #Not right isosceles
    unittest.main(exit=False)
