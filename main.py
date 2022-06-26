#Mostafa Darder
#19108511

import random 

random.seed(10)
size = 500
customer = [i for i in range(1,size+1)]

# IAT & ST Random number 
IAT = [random.randrange(1,10) for i in range(size)]
ST = [random.randrange(1,10) for i in range(size)]
print(len(IAT),len(ST))

# Calc AT
AT = [0 for i in range(size)]
# initial Value
ST[0] = IAT[0]

for i in range(1,size):
  ST[i] = IAT[i]+ST[i-1]
 
Service_starts_at = [0 for i in range(size)]
Waiting_time = [0 for i in range(size)]
Service_ends_at = [0 for i in range(size)]
Time_Customer_Spend = [0 for i in range(size)]
System_ideal = [0 for i in range(size)]

Service_starts_at[0] = ST[0]
Service_ends_at[0] = ST[0]
Time_Customer_Spend[0] = ST[0]
for i in range(1,size):
  # Time Service Begin 
  Service_starts_at[i] = max(ST[i],Service_ends_at[i-1])

  # Time customer waiting in queue   
  Waiting_time[i] = Service_starts_at[i]-ST[i]

  # Time service ends
  Service_ends_at[i] = Service_starts_at[i] + ST[i]  

  # Time Customer Spend in the system
  Time_Customer_Spend[i] = Service_ends_at[i] - ST[i]

  ## Time when system remains ideal
  if (ST[i]>Service_ends_at[i-1]):
    System_ideal[i] = ST[i]-Service_ends_at[i-1]
  else:
    System_ideal[i] = 0 

#-----------------------------------------------------------------------------------------
no_customer_who_are_waiting = len(list(filter(lambda x:x>0,Waiting_time)))
prob_customer_waiting = no_customer_who_are_waiting / size
Average_waiting_time = sum(Waiting_time)/size 
average_waiting_time = sum(Waiting_time) / no_customer_who_are_waiting
#- Server utilization (percentage of time the employee is busy serving a customer)
utilization = (sum(ST)-sum(System_ideal)) /100.0
Average_ST = sum(ST)/size
prob_ideal_server = sum(System_ideal) / Service_ends_at[size-1]  
Average_Time_Between_Arrival = ST[size-1] / (len(ST) - 1)
time_customer_spent = sum(Time_Customer_Spend)/size
Maximum_queue_length = max(Waiting_time)

print("Average waiting time :", (Average_waiting_time))
print('********* \n ')

print("Maximum waiting time for a customer :",(Maximum_queue_length))
print('********* \n ')
print("Probability of customer were waiting :",(prob_customer_waiting))
print('********* \n ')
print("Average service time :",(Average_ST))
print('********* \n ')

print("Probability of idle server :",(prob_ideal_server))
print('********* \n ')


print("Server utilization:" ,(utilization))
print('********* \n ')

print("Average waiting time those who wait :",(average_waiting_time))
print('********* \n ')

print("Average time customer spent in the system :",(time_customer_spent))
print('********* \n ')