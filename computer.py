class Computer():
    def __init__(self, bits_signo_mantisa, bits_signo_exponente, bits_mantisa, bits_exponente):
        self.bits_signo_mantisa = bits_signo_mantisa
        self.bits_signo_exponente = bits_signo_exponente
        self.bits_mantisa = bits_mantisa
        self.bits_exponente = bits_exponente
        self.signo_mantisa = ""
        self.signo_exponente = ""
        self.mantisa = ""
        self.exponente = ""
        print("Usted ha creado un computador con " + str(self.bits_signo_mantisa) + " bit de signo mantisa, " + str(self.bits_signo_exponente) + " bit signo exponente, " + str(self.bits_mantisa) + " bits mantisa, "+ str(bits_exponente) + " bits exponente")
        self.insertNumber()

    def insertNumber(self):
        num = float(input("Ingrese el numero a transformar: "))
        if num >0 :
            self.signo_mantisa = 1
        else:
            self.signo_mantisa = 0
            num = abs(num)
        #print("Call conversion")
        self.numberToBinary(num)

    def get_exponent(self, Integral):
        Integral = len(Integral)+1
        binary = ""
        while (Integral) : 
            
            rem = Integral % 2
    
            # Append 0 in binary  
            binary += str(rem);  
    
            Integral //= 2
        self. exponente = binary[ : : -1] 
        if len(self.exponente) > self.bits_exponente:
            self.exponente = self.exponente[:self.bits_exponente]
        
        self.printall()

    def printall(self):
        print("signo mantisa",self.signo_mantisa)
        print("mantisa",self.mantisa)
        print("exponente",self.exponente)

    def numberToBinary(self,num):
        
        binary = ""  
  
        # Fetch the integral part of 
        # decimal number  
        Integral = int(num)  
    
        # Fetch the fractional part  
        # decimal number  
        fractional = num - Integral 
  
        # Conversion of integral part to  
        # binary equivalent  
        while (Integral) : 
            
            rem = Integral % 2
    
            # Append 0 in binary  
            binary += str(rem);  
    
            Integral //= 2
      
        # Reverse string to get original 
        # binary equivalent  
        binary = binary[ : : -1]  

  
        # Append point before conversion  
        # of fractional part  
        #binary += '.'
        binary = binary[1:]
        integral_part = binary
        len_bi = self.bits_mantisa - len(binary)
        #print("PASA CONVERSIÓN")
  
        # Conversion of fractional part 
        # to binary equivalent  
        while (len_bi) : 
            
            # Find next bit in fraction  
            fractional *= 2
            fract_bit = int(fractional)  
    
            if (fract_bit == 1) : 
                
                fractional -= fract_bit  
                binary += '1'
                
            else : 
                binary += '0'
    
            len_bi -= 1
        
        
        self.mantisa = binary
        if len(self.mantisa) > self.bits_mantisa:
            self.mantisa = self.mantisa[:self.bits_mantisa]
        self.get_exponent(integral_part)
    


if __name__ == "__main__":
    Computer(1,1,8,3)
    