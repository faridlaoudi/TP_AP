
num_people = int(input("How many people need a ride? "))
taxi_capacity = int(input("How many people can fit in one taxi? "))

if num_people % taxi_capacity == 0 : 
    num_taxi = num_people // taxi_capacity 
    print("The number of taxis required: " , num_taxi )
else : 
    num_taxi = ( num_people // taxi_capacity ) + 1
    print("The number of taxis required: " , num_taxi )
    print("the last taxi will carry : " , num_people % taxi_capacity )


