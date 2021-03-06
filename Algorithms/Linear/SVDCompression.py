# We would like to get a list of singular vectors that will help us capture most of the variation

# Imports
from scipy.sparse import csr_matrix

# This will rely on the magnitude of the singular vector
def getMinSingularVectorsMethodValMag(inpArray):
    inpArray=csr_matrix(inpArray).asfptype()
    U,S,V = scipy.sparse.linalg.svds(inpArray, k = min(a.shape[0]-1,a.shape[1]-1))
    S1=list(reversed(S))
    cumSum=np.cumsum(S1) / sum(S1)
    minVal=min([i for i,x in enumerate(cumSum) if x >= 0.8])
    print(list(reversed(S1[0:minVal])))
    


# We will now do it in the distance vector way and compare it
# This method is very inconclusive
def getMinSingularVectorsDistance(inpArray):
    a1=csr_matrix(inpArray).asfptype()
    distArr=[]
    for curVectors in range(1,min(inpArray.shape[0]-1,inpArray.shape[1]-1)):
        U,S,V = scipy.sparse.linalg.svds(a1, k=curVectors)
        S=np.diag(S)
        recreated=np.dot(np.dot(U,S),V)
        distArr.append([curVectors,sum([scipy.spatial.distance.euclidean(inpArray[x],recreated[x]) for x in range(inpArray.shape[0])])])
    return(distArr)



if __name__=="__main__":
    a=np.random.randint(low=0,high=5, size=(100,50))
    listOfSingularValues=getMinSingularVectorsMethodValMag(a)
    print(len(listOfSingularValues))
    # 29
    distValues=getMinSingularVectorsDistance(a)
    print(distValues)
