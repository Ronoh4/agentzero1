#!/usr/bin/env python
import sys
from .crew import ClothingStoreCrew

def run():
    """
    Run the crew.
    """
    print("Initializing Clothing Store Crew...")  # Print statement to indicate the start


    # Initialize ClothingStoreCrew and start the kickoff process
    crew = ClothingStoreCrew()

    # Inputs
    inputs = {
        "question": "What is the origin and top trends of gothic style?",
        "gender": "female"
    }

    # Perform the kickoff using the initialized crew and formatted inputs
    response = crew.crew().kickoff(inputs=inputs)  # Using crew.crew().kickoff for compatibility

    # Return the response as JSON
    return {"response": response}

if __name__ == "__main__":
    run()
