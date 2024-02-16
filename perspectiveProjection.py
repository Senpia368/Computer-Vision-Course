import matplotlib.pyplot as plt
'''
Simulating the projection of a line segment defined by two points (-5,Z) and (5,Z), where Z ranges from 10 to 1000, and assuming a camera focal length of f=1.
For each distance Z, project the two points into a 1-D sensor under perspective projection, and compute the length of the segment.
'''
def projectionSimulation(dict, focalLength):
    for z in range(10,1001):
        length = abs(((-5 * focalLength)/z) - ((5 * focalLength)/z))
        dict[z] = length

'''
Plots graph from dictionary
'''
def graph(dict):
    z = list(dict.keys())
    values = list(dict.values())

    plt.plot(z,values)
    plt.show


dict = {}
f = 1

projectionSimulation(dict,f)

#print(dict)

plt.plot(dict.keys(),dict.values())
plt.xlabel('Z')
plt.ylabel('Projection Length')
plt.show()

