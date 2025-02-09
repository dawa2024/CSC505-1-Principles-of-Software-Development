class SoftwareDeveloper:
    def __init__(self, problem_solving, communication, learning):
        self.problem_solving = problem_solving
        self.communication = communication
        self.learning = learning

    def describe(self):
        
        return (f"Excellent Software Developer Traits:\n"
                f"- Problem-Solving: {self.problem_solving}\n"
                f"- Collaboration & Communication: {self.communication}\n"
                f"- Continuous Learning: {self.learning}")

class SoftwareDeveloperBuilder:
    def __init__(self):
        self.problem_solving = None
        self.communication = None
        self.learning = None

    def set_problem_solving(self, level):
        self.problem_solving = level
        return self

    def set_communication(self, level):
        self.communication = level
        return self

    def set_learning(self, level):
        self.learning = level
        return self

    def build(self):
        return SoftwareDeveloper(self.problem_solving, self.communication, self.learning)

# Creating a Software Developer with key traits
builder = SoftwareDeveloperBuilder()
developer = (builder.set_problem_solving("Expert")
                  .set_communication("Team Player")
                  .set_learning("Lifelong Learner")
                  .build())

# Print Description and Steps
print(developer.describe())

print("\nSteps to Build an Excellent Software Developer:")
steps = ["1. Develop strong problem-solving skills",
         "2. Enhance communication and collaboration",
         "3. Commit to continuous learning"]
for step in steps:
    print(step)
