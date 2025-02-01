class TamangModel:
    def __init__(self):
        self.communication = ""
        self.planning = ""
        self.modeling = ""
        self.development = ""
        self.testing = ""
    
    def gather_input(self):
        print("Please provide details for each phase of the YourLastName Model:")
        
        self.communication = input("What communication strategies will be used? ")
        self.planning = input("How will you plan iterative cycles and sprints? ")
        self.modeling = input("How will prototypes and models be created? ")
        self.development = input("How will development occur in iterations? ")
        self.testing = input("How will testing be conducted throughout the process? ")
    
    def display_model(self):
        print("\n--- Tamang Model ---")
        print(f"Communication: {self.communication}")
        print(f"Planning: {self.planning}")
        print(f"Modeling: {self.modeling}")
        print(f"Development: {self.development}")
        print(f"Testing: {self.testing}")
        
if __name__ == "__main__":
    model = TamangModel()
    model.gather_input()
    model.display_model()
