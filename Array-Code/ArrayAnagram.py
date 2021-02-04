 # Anagram Problem
 # Anagram is a word or phrase formed by rearanging the letters of the diffrent word or phrase typically, using all the letters exactly once.

def is_anagram(str1, str2):

    if len(str1) != len(str2):
         return False

    # O(NlOgN) running time complexity
    str1 = sorted(str1)
    str2 = sorted(str2)

    # O(N) running time complexity 
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    # O(N) + O(NlogN) = O(NlogN) running time comlexity
    
    return True

if __name__ == '__main__':

    s1 = ['f','l','u','s','t','e','r']
    s2 = ['r','e','s','t','f','u','l']
    print(is_anagram(s1,s2))
     
     
