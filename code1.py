#coding=utf_8_decode  
def Needleman_Wunsch(str1,str2):  
      
    if str1=='' or str2=='':  
        return  ''  
     
    m=len(str1)  
    n=len(str2)  
   
    lcs=[[i*(-2)] for i in range(0,m+1)]  
    lcs[0]=[j*(-2) for j in range(0,n+1)]  
    #  
    for i in range(m):  
        for j in range(n):  
            lcs[i+1].append(  
                            max(  
                                lcs[i][j]+(1 if str1[i] == str2[j] else -1),  
                                lcs[i][j+1]-2,  
                                lcs[i+1][j]-2,  
                                )  
                            )  
    #for i in range(m+1):  
        #print lcs[i]  
    i=m-1  
    j=n-1  
    common_substr1 = u''  
    common_substr2 = u''  
    common_substr1 = u"%s%s" % (str1[i], common_substr1)  
    common_substr2 = u"%s%s" % (str2[j], common_substr2)  
     
    while True:  
        if i == 0 and j == 0:  
            break  
        if str1[i] == str2[j]:  
            if lcs[i-1][j-1]+1>lcs[i-1][j]-2 and lcs[i-1][j-1]+1>lcs[i][j-1]-2:  
                i = i - 1  
                j = j -1  
                common_substr1 = u"%s%s" % (str1[i], common_substr1)  
                common_substr2 = u"%s%s" % (str2[j], common_substr2)  
                  
            else:  
                if lcs[i][j+1] > lcs[i+1][j]:  
                    i = i-1  
                    common_substr1 = u"%s%s" % (str1[i], common_substr1)  
                    common_substr2 = u"%s%s" % ('-', common_substr2)  
                      
                else:  
                    j = j-1  
                    common_substr1 = u"%s%s" % ('-', common_substr1)  
                    common_substr2 = u"%s%s" % (str2[j], common_substr2)  
                      
        else:  
            if lcs[i-1][j-1]+1>lcs[i-1][j]-2 and lcs[i-1][j-1]+1>lcs[i][j-1]-2:  
                i = i - 1  
                j = j -1  
                common_substr1 = u"%s%s" % (str1[i], common_substr1)  
                common_substr2 = u"%s%s" % (str2[j], common_substr2)  
                  
            else:  
                if lcs[i][j+1] > lcs[i+1][j]:  
                    i = i-1  
                    common_substr1 = u"%s%s" % (str1[i], common_substr1)  
                    common_substr2 = u"%s%s" % ('-', common_substr2)  
                      
                else:  
                    j = j-1  
                    common_substr1 = u"%s%s" % ('-', common_substr1)  
                    common_substr2 = u"%s%s" % (str2[j], common_substr2)  
    print common_substr1  
    print common_substr2  
      
  
Needleman_Wunsch("AACAGTTACC","TAAGGTCA")  
