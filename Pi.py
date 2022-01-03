class piCalculate(self, decimals) :
    
    self.calculations = 0
    self.character = "rem"
    self.decimals = decimals
    self.number = 3
    self.pi = 1
    
    for self.calculations < self.decimals :
        
        if self.character == "rem" :
            
            self.pi -= 1 / self.number
            self.character = "add"
            self.number += 2
            
        if self.character == "add" :
            
            self.pi += 1 / self.number
            self.character = "rem"
            self.number += 2
            
    print("The number is : " +self.pi)
