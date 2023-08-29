import numpy as np
temp=np.array([[[[8,21],[9,22],[14,28],[10,20],[11,23],[10,27],[12,26]],[[10,29],[11,22],[7,29],[-13,24],[14,31],[7,31],[13,24]],[[7,28],[10,32],[13,30],[8,24],[9,25],[8,32],[14,25]],[[12,29],[8,22],[12,21],[13,31],[13,31],[11,28],[12,22]]],
               [[[13,25],[12,28],[6,30],[13,28],[11,22],[6,28],[15,30]],[[11,29],[8,30],[10,25],[6,20],[9,25],[10,29],[6,30]],[[14,27],[6,30],[14,28],[14,32],[15,28],[9,31],[9,25]],[[8,20],[11,25],[7,28],[6,29],[14,21],[8,32],[15,31]]],
               [[[2,20],[5,21],[8,21],[3,20],[7,21],[3,4],[21,6]],[[2,20],[5,21],[3,18],[3,22],[7,21],[6,2],[20,4]],[[6,19],[8,19],[8,22],[2,18],[2,22],[5,8],[18,3]],[[2,21],[4,21],[3,20],[6,22],[3,20],[7,3],[18,2]]],
               [[[8,18],[8,22],[-10,22],[11,19],[11,20],[12,71],[18,9]],[[10,22],[10,19],[9,22],[12,19],[11,20],[7,9],[20,12]],[[12,18],[12,20],[7,21],[9,21],[11,18],[12,8],[20,11]],[[11,19],[12,20],[7,20],[10,19],[12,18],[10,7],[19,7]]]])

# 1. Represent the data in the given sheet into an appropriate NumPy array so that you can perform the following actions on it.
def fun1(temp):
    print(temp)


# 2.  Write the dimensions and shape of the NumPy array that you have  created.

def fun2(temp):
    print("\nThis nd Array has size of : ",np.shape(temp))
    print("\nThis nd Array has dimension of : ",np.ndim(temp))

# 3. Print the daily temperatures for the first week of each month.

def fun3(temp):
    arr1=temp[0,0,:]
    print("\n\nTemperatures for Week 1 of November : \n")
    print("  Min        Max")
    for i in arr1:
        print(" ",i[0],"        ",i[1])    
    
    arr2=temp[1,0,:]
    print("\nTemperatures for Week 2 of November : \n")
    print("  Min        Max")
    for i in arr2:
        print(" ",i[0],"        ",i[1])

    arr3=temp[2,0,:]
    print("\nTemperatures for Week 3 of November : \n")
    print("  Min        Max")
    for i in arr3:
        print(" ",i[0],"        ",i[1])
    
    arr4=temp[3,0,:]
    print("\nTemperatures for Week 4 of November : \n")
    
    print("  Min        Max")
    for i in arr4:
        print(" ",i[0],"        ",i[1])
    
    
# 4. Print the temperatures for Tuesday of each month.

def fun4(temp):
    arr1=temp[0,:,1]
    print("\n\nTemperatures of Tuesday for November : \n")
    print("  Min        Max")
    for i in arr1:
        print(" ",i[0],"        ",i[1])
    
    arr2=temp[1,:,1]
    print("\n\nTemperatures of Tuesday for December : \n")
    print("  Min        Max")
    for i in arr2:
        print(" ",i[0],"        ",i[1])
    
    arr3=temp[2,:,1]
    print("\n\nTemperatures of Tuesday for January : \n")
    print("  Min        Max")
    for i in arr3:
        print(" ",i[0],"        ",i[1])
    
    arr4=temp[3,:,1]
    print("\n\nTemperatures of Tuesday for February : \n")
    print("  Min        Max")
    for i in arr4:
        print(" ",i[0],"        ",i[1])


# 5. Print only the maximum temperature for all the weekdays of Dec and Feb.

def fun5(temp):
    print("\n\nMaximum temperatures for all the weekdays of December:")
    print("Week 1 : ")
    arr1=temp[0,0,:]
    print("Max Temp")
    for i in arr1:
        print("  ",i[1])
    
    print("\nWeek 2 : ")
    arr2=temp[0,1,:]
    print("Max Temp")
    for i in arr2:
        print("  ",i[1])

    print("\nWeek 3 : ")
    arr3=temp[0,2,:]
    print("Max Temp")
    for i in arr3:
        print("  ",i[1])

    print("\nWeek 4 : ")
    arr2=temp[0,3,:]
    print("Max Temp")
    for i in arr3:
        print("  ",i[1])

# 6. Print all the days along with the week number in November when the minimum temperature was less than 8 degrees.

def fun6(temp):
    arr=temp[0,:,:]
    k=0
    for i in arr:
        flag=0
        if k==0:
            print("\nWeek 1:")
        elif(k==1):
            print("\nWeek 2:")
        elif k==2:
            print("\nWeek 3:")
        elif k==3:
            print("\nWeek 4:")
        print("Min Temp")
        k=k+1

        for j in i:
            if j[0]<8:
                print("  ",np.where(j[0]))
                flag=1
        if flag==0:
            print("All min. temperatures are above 7")

# 7. Print all the weeks in Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees

def fun7(temp):
    print("In December :")
    arr=temp[1,:,:]
    k=1
    for i in arr:
        for j in i:
            if j[1]>20:
                if k==1:
                    print("Week 1")
                    break
                
                elif k==2:
                    print("Week 2")
                    break

                elif k==3:
                    print("Week 3")
                    break

                elif k==4:
                    print("Week 4")
                    break
        k=k+1

    print("\nIn January :")
    arr=temp[2,:,:]
    k=1
    for i in arr:
        for j in i:
            if j[1]>20:
                if k==1:
                    print("Week 1")
                    break
                
                elif k==2:
                    print("Week 2")
                    break

                elif k==3:
                    print("Week 3")
                    break

                elif k==4:
                    print("Week 4")
                    break
        k=k+1    

# 8. Check if there are any absurd values present in the dataset(like some temp which should not be present in the data)
                
def fun8(temp):
    print("Absurd Values are:-")
    print("\nMin Temp      Max Temp")
    for i in temp:
        for j in i:
            for k in j:
                if k[0]>k[1] or (k[1]-k[0]>25):
                    print("  ",k[0],"          ",k[1])
                    

# 9. What strategy would you use to handle such data points?
   
def fun9(temp):
    print("I will use this strategy to handle absurd data point : ")
    print("Interpolation:  If the incorrect values follow a pattern that can be interpolated, you can use interpolation techniques to estimate the correct values based on nearby valid data points.")


# 10. Find and print the indexes of all the outlier(unusual) values present in the above dataset.

def fun10(temp):
    cond1=(temp[...,0]>temp[...,1])
    cond2=(temp[:,:,:,1]-temp[..., 0]>25)
    cond=cond1 | cond2
    indices=np.where(cond)
    return indices

# 11. Replace the outliers with an appropriate value.

def fun11(temp):
    # med=np.median(temp[0,:,:,0])
    # print(med)
    indices=fun10(temp)
    indices=np.array(indices)
    indices=np.transpose(indices)
    for i in indices:
        if i[0]==0:
            temp[i[0],i[1],i[2],0]=np.median(temp[0,:,:,0])
            temp[i[0],i[1],i[2],1]=np.median(temp[0,:,:,1])

        elif i[0]==1:
            temp[i[0],i[1],i[2],0]=np.median(temp[1,:,:,0])
            temp[i[0],i[1],i[2],1]=np.median(temp[1,:,:,1])
        elif i[0]==2:
            temp[i[0],i[1],i[2],0]=np.median(temp[2,:,:,0])
            temp[i[0],i[1],i[2],1]=np.median(temp[2,:,:,1])

        elif i[0]==3:
            temp[i[0],i[1],i[2],0]=np.median(temp[3,:,:,0])
            temp[i[0],i[1],i[2],1]=np.median(temp[3,:,:,1])
    print("All absurd values have changed with median values.....1 : ")
        
    return temp
            

# 12. Find the average max temperature for the winter months in Jaipur.

def fun12(temp):
    summ=0
    for i in temp:
        summ=summ+np.amax(i[:,:,1])
    avg=summ/4
    print("The average max temperature for the winter months in Jaipur is : ",avg)


# 13. Find the weekly min avg temp for the month of Dec in Jaipur

def fun13(temp):
    summ=0
    for i in temp[1]:
        summ=summ+np.amin(i[:,0])

    print("The weekly min avg temp for the month of Dec in Jaipur : ",summ/4)


# 14. Find the overall avg temp for the months Dec and Jan

def fun14(temp):
    avg=np.average(temp[1,:,:,:])

    print("The overall avg temp for the months December : ",round(avg,2))
    avg=np.average(temp[2,:,:,:])

    print("The overall avg temp for the months January : ",round(avg,2))

# 15. Find the least temp experienced by the city in the month of Dec and Jan. Also print the exact date( Day/Week/Month) for the same.

def fun15(temp):
    cond= temp[1,:,:,:]==np.amin(temp[1,:,:,:])
    leasttemp=np.amin(temp[1])
    least=np.where(cond)
    print("Least temp experienced by the city in the month of December : \n")
    
    arr=np.array(least)
    brr=(np.transpose(arr))
    for i in brr:
        print("Least Temp : ",leasttemp)
        print("Day / Week / Month :-  ",end='')
        if i[1]==0:
            print("Monday ",end='/')
        elif i[1]==1:
            print("Tuesday ",end='/')
        elif i[1]==2:
            print("Wednesday ",end='/')
        elif i[1]==3:
            print("Thursday ",end='/')
        elif i[1]==4:
            print("Friday ",end='/')
        elif i[1]==5:
            print("Saturday ",end='/')
        elif i[1]==6:
            print("Sunday ",end='/')
        
        if i[0]==0: 
            print(' Week 1 ',end='/')
        elif i[0]==1: 
            print(' Week 2 ',end='/')
        elif i[0]==2: 
            print(' Week 3 ',end='/')
        elif i[0]==3: 
            print(' Week 4 ',end='/')

        print(" December\n")
        


    cond= temp[2,:,:,:]==np.amin(temp[2,:,:,:])
    leasttemp=np.amin(temp[2])
    least=np.where(cond)
    print("Least temp experienced by the city in the month of January : \n")
    
    arr=np.array(least)
    brr=(np.transpose(arr))
    for i in brr:
        print("Least Temp : ",leasttemp)
        print("Day / Week / Month :-  ",end='')
        if i[1]==0:
            print("Monday ",end='/')
        elif i[1]==1:
            print("Tuesday ",end='/')
        elif i[1]==2:
            print("Wednesday ",end='/')
        elif i[1]==3:
            print("Thursday ",end='/')
        elif i[1]==4:
            print("Friday ",end='/')
        elif i[1]==5:
            print("Saturday ",end='/')
        elif i[1]==6:
            print("Sunday ",end='/')
        
        if i[0]==0: 
            print(' Week 1 ',end='/')
        elif i[0]==1: 
            print(' Week 2 ',end='/')
        elif i[0]==2: 
            print(' Week 3 ',end='/')
        elif i[0]==3: 
            print(' Week 4 ',end='/')

        print(" January\n")
        

# 16. Find the max temp in the month of February and return its date(Day/Week/Month)
        
def fun16(temp):
    cond= temp[3,:,:,:]==np.amax(temp[3,:,:,:])
    maxtemp=np.amax(temp[3])
    tmax=np.where(cond)
    print("Maximum temp experienced by the city in the month of February : \n")
    
    arr=np.array(tmax)
    brr=(np.transpose(arr))
    for i in brr:
        print("Maximum Temp : ",maxtemp)
        print("Day / Week / Month :-  ",end='')
        if i[1]==0:
            print("Monday ",end='/')
        elif i[1]==1:
            print("Tuesday ",end='/')
        elif i[1]==2:
            print("Wednesday ",end='/')
        elif i[1]==3:
            print("Thursday ",end='/')
        elif i[1]==4:
            print("Friday ",end='/')
        elif i[1]==5:
            print("Saturday ",end='/')
        elif i[1]==6:
            print("Sunday ",end='/')
        
        if i[0]==0: 
            print(' Week 1 ',end='/')
        elif i[0]==1: 
            print(' Week 2 ',end='/')
        elif i[0]==2: 
            print(' Week 3 ',end='/')
        elif i[0]==3: 
            print(' Week 4 ',end='/')
            
        print(" February\n")

# 17. Find the days in the month of Nov where the max temp of the day dropped below the avg temp of the month.

def fun17(temp):
    avg=round(np.average(temp[0]),2)
    arr=temp[0,:,:,1]<avg
    brr=np.where(arr)
    trr=np.transpose(brr)
    print("The days in the month of Nov where the max temp of the day dropped below the avg temp of the month : ",len(trr))
    if len(trr)==0:
        print("No such day is there.....")
        return

    for i in trr:
        print("Temp : ",temp[0,i[0],i[1],1])
        print("Day / Week :-  ",end='')
        if i[1]==0:
            print("Monday ",end='/')
        elif i[1]==1:
            print("Tuesday ",end='/')
        elif i[1]==2:
            print("Wednesday ",end='/')
        elif i[1]==3:
            print("Thursday ",end='/')
        elif i[1]==4:
            print("Friday ",end='/')
        elif i[1]==5:
            print("Saturday ",end='/')
        elif i[1]==6:
            print("Sunday ",end='/')
        
        if i[0]==0: 
            print(' Week 1 ')
        elif i[0]==1: 
            print(' Week 2 ')
        elif i[0]==2: 
            print(' Week 3 ')
        elif i[0]==3: 
            print(' Week 4 ')
    
# 18. Convert the above dataset into an array where the weeks of the same month must be present in the same row, but belonging to different months
# should come in a row either below or above the selected month.

def fun18(temp):
    arr=np.reshape(temp,(4,56))
    print("An array where the weeks of the same month must be present in the same row :")
    print(arr)

# 19. The above data is appropriate for an audience who follow the metric system of measurement. Create an array that holds the same data but presented in Fahrenheit.

def fun19(temp):
   fah=((temp*9)/5 + 32)
   print("Array that holds the same data but presented in Fahrenheit :")
   print(fah)

# 20. Sort the above data in descending order on the basis of weekly average for the month of Dec.

def fun20(temp):
    a=np.mean(temp[1::4,0::4,:,:])
    b=np.mean(temp[1::4,1::4,:,:])
    c=np.mean(temp[1::4,2::4,:,:])
    d=np.mean(temp[1::4,3::4,:,:])
    arr=np.array([a,b,c,d])
    arr[::-1].sort()
    print("The above data in descending order on the basis of weekly average for the month of Dec : ")
    print(arr)

# 21. Sort the temp of the first three days of each month in descending order on the basis of overall average for the whole winter
def fun21(temp):
    temp[0,0,0:3,:]

# 22. Create an array that stores the difference between the min and max temp for each day in all the winter months.

def fun22(temp):
    arr=temp[:,:,:,1]-temp[:,:,:,0]
    print("Array that stores the difference between the min and max temp for each day in all the winter months : ")
    print(arr)


# 23. Find and store the difference between the max temp of two consecutive days for each month of winter season.
def fun23(temp):
    arr=temp[:,:,1:,1]-temp[:,:,:6,1]
    return arr
    print("The difference between the max temp of two consecutive days for each month of winter season : \n")
    print(arr)


# 24. Find and store the difference between the minimum temp of two consecutive days for each month of the winter season.

def fun24(temp):
    arr=temp[:,:,1:,0]-temp[:,:,:6,0]
    return arr


# 25. Create an array by combining the data present in arrays created in q.23 and q.24, to store the difference between the min and max temp of each
# day of all the months for the whole winter season, in a single array

def fun25(temp):
    array1=fun23(temp)
    array2=fun24(temp)
    reshaped_array1 = array1[..., np.newaxis]
    reshaped_array2 = array2[..., np.newaxis]
    combined_array = np.concatenate((reshaped_array2, reshaped_array1), axis=3)
    print("Combined array of the difference between the min and max temp of each day of all the months : ")
    print(combined_array)




# main()

repeat=1
while repeat==1:
    print("\n\nEnter 1 to represent the data in the given sheet into an appropriate NumPy array .")
    print("Enter 2 to see the dimensions and shape of the NumPy array that you have created.")
    print("Enter 3 to print the daily temperatures for the first week of each month.")
    print("Enter 4 to print the temperatures for Tuesday of each month")
    print("Enter 5 to print only the maximum temperature for all the weekdays of Dec and Feb.")
    print("Enter 6 to print all the days along with the week number in November when the minimum temperature was less than 8 degrees")
    print("Enter 7 to print all the weeks in Dec and Jan where the maximum temperature has crossed a threshold of 20 degrees.")
    print("Enter 8 to check if there are any absurd values present in the dataset(like some temp which should not be present in the data)")
    print("Enter 9 to see what strategy would you use to handle such data points?")
    print("Enter 10 to find and print the indexes of all the outlier(unusual) values present in the above dataset.")
    print("Enter 11 to replace the outliers with an appropriate value.")
    print("Enter 12 to find the average max temperature for the winter months in Jaipur.")
    print("Enter 13 to find the weekly min avg temp for the month of Dec in Jaipur")
    print("Enter 14 to find the overall avg temp for the months Dec and Jan")
    print("Enter 15 to Find the least temp experienced by the city in the month of Dec and Jan. Also print the exact date( Day/Week/Month) for the same.")
    print("Enter 16 to Find the max temp in the month of Feb and return its date(Day/Week/Month)")
    print("Enter 17 to Find the days in the month of Nov where the max temp of the day dropped below the avg temp of the month.")
    print("Enter 18 to Convert the above dataset into an array where the weeks of the same month must be present in the same row, but belonging to different monthsshould come in a row either below or above the selected month.")
    print("Enter 19 to The above data is appropriate for an audience who follow the metric system of measurement. Create an array that holds the same data but presented in Fahrenheit.")
    print("Enter 20 to Sort the above data in descending order on the basis of weekly average for the month of Dec.")
    print("Enter 21 to Sort the temp of the first three days of each month in descending order on the basis of overall average for the whole winter.")
    print("Enter 22 to Create an array that stores the difference between the min and max temp for each day in all the winter months.")
    print("Enter 23 to Find and store the difference between the max temp of two consecutive days for each month of winter season")
    print("Enter 24 to Find and store the difference between the minimum temp of two consecutive days for each month of the winter season.")
    print("Enter 25 to Create an array by combining the data present in arrays created in q.23 and q.24, to store the difference between the min and max temp of each day of all the months for the whole winter season, in a single array")
    
    ch=int(input("Enter the choice: "))
    print("\n")

    if ch==1:
        fun1(temp)
    elif ch==2:
        fun2(temp) 
    elif ch==3:
        fun3(temp)
    elif ch==4:
        fun4(temp)
    elif ch==5:
        fun5(temp)
    elif ch==6:
        fun6(temp)
    elif ch==7:
        fun7(temp)
    elif ch==8:
        fun8(temp)
    elif ch==9:
        fun9(temp)
    elif ch==10:
        indices=fun10(temp)
        print("Indices of the absurd values are : ")
        print(indices)
    elif ch==11:
        temp=fun11(temp)
    elif ch==12:
        fun12(temp)
    elif ch==13:
        fun13(temp)
    elif ch==14:
        fun14(temp)
    elif ch==15:
        fun15(temp)
    elif ch==16:
        fun16(temp)
    elif ch==17:
        fun17(temp)
    elif ch==18:
        fun18(temp)
    elif ch==19:
        fun19(temp)
    elif ch==20:
        fun20(temp)
    elif ch==21:
        fun21(temp)
    elif ch==22:
        fun22(temp)
    elif ch==23:
        arr=fun23(temp) 
        print("The difference between the max temp of two consecutive days for each month of winter season : \n")
        print(arr)
    elif ch==24:
        arr=fun24(temp)
        print("The difference between the minimum temp of two consecutive days for each month of winter season : \n")
        print(arr)
    elif ch==25:
        fun25(temp)
    else:
        print("You have entered the wrong input......")
    repeat=int(input("Enter 0 to exit... \nEnter 1 to continue to perform more operarions... "))