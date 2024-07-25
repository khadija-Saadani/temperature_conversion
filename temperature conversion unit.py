def convert_temperature(temp,unit):
    if unit =='c':
        #celsius to kelvin 
        kelven= temp + 273.15  
        #celsius to fahren
        fahren= (temp * 9/5) + 32
        return f"temperature {temp:.2f}°C is : {kelven:.2f} K and {fahren:.2f}°F"   
    elif unit == 'k':
        #kelvin to celsius 
        celsius= temp - 273.15
        #kelvin to fahren 
        fahren= (temp *9/5) - 459.67
        return f"temperature {temp:.2f} K is :{celsius:.2f}°C ,{fahren:.2f}°F"
    elif unit =='f':
        #fahren to celsius 
        celsius= (temp- 32 )* 5/9
        #fahren to kelvin 
        kelven=(temp+ 459.67) * 5/9
        return f"temperature {temp:.2f}°F is :{celsius:.2f}°C and {kelven:.2f} K "
def main():
    
    while True:
        try :
            temp=float(input("\nPlease enter the temperature value !  : "))
            break #exit the loop if the temperature value is numeric
        except ValueError :
            print("Invalid input. Please enter a numeric temperature.")
    while True :    
        unit=input("Enter the unit of temperature ('C' for Celsius , 'F' for Fahrenheit or 'K' for kelven ):   ").lower()
        if unit in ['c','k','f']:
            print( convert_temperature(temp,unit)   )
            break
        else :
            
            print("invalid input,try again and make sure you enter (C , F or K ) \n")
        
        
       
main()