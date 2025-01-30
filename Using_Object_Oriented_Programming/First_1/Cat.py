class cat:
    def __init__(self, name, color ,type , age, stepsPerWalk, stepsPerRun):
        self.name= name
        self.color= color 
        self.age = age
        self.type= type
        self.StepPerWalk = stepsPerWalk
        self.StepPerRun = stepsPerRun
        
    
    def walk(self): 
         print(f"{self.commonstrings()} and I run {self.StepPerWalk} steps/sec")
        
    def run(self): 
        print(f"{self.commonstrings()} I run {self.StepPerRun} steps/sec")
        
    def commonstrings(self):
        result =f"I am {self.name},"
        result +=f" and my color is {self.color},"
        result += f" and I am a {self.type}cat type,"
        result += f" and my age is {self.age},"
        return result


