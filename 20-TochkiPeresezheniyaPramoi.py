def tozhkiPeresezheniya(a1,a2):
    x = (a1[2]*a2[1]-a2[2]*a1[1])/(a1[0]*a2[1]-a2[0]*a2[1])*(-1)
    y = (a1[0]*a2[2]-a2[0]*a1[2])/(a1[0]*a2[1]-a2[0]*a2[1])*(-1)

    return(x,y)