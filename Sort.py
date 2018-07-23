s=[9,8,7,6,5,4,3,2,1]

# print(s[:len(s)/2])
# print(s[len(s)/2:])

class MergeSort():
    def __init__(self):
        self.name="MERGE SORT"
    
    def sort(self, s):
        if len(s)==1:
            return s
        return self.merge(self.sort(s[:len(s)/2]),self.sort(s[len(s)/2:]))

    def merge(self,left,right):
        result=[]
        while left and right:
            result.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
        result.extend(right if right else left)
        return result

class QuickSort():
    def __init__(self):
        self.name="QUICK SORT"
    
    def qsort(self, s, p, q):
        if p<q:
            k=self.partition(s,p,q)
            self.qsort(s,p,k)
            self.qsort(s,k+1,q)

    def partition(self, s, p, q):
        k = p
        for i in xrange(p+1,q+1):
            if s[i]<=s[p]:
                k+=1
                s[i],s[k]=s[k],s[i]
        s[k],s[p]=s[p],s[k]
        return k

    def sort(self, s):
        self.qsort(s,0,len(s)-1)
        return s

# merge = MergeSort()
# print("THE RESULT OF MERGE SORT")
# print(merge.sort(s))

qsort = QuickSort()
print("THE RESULT OF QUICK SORT")
print(qsort.sort(s))



        