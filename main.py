from src import add
from src import Agent
from src import SYSTEM_PROMPT

def main():
    print("Hello from my-project-str!")


    agent = Agent("Doctor")
    print(f"My agent name is {agent.name}")


    print(f"My agent {agent.name} system prompt is \n {SYSTEM_PROMPT}")

 
    num1 = 10
    num2 = 28
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is {result}")


if __name__ == "__main__":
    main()
