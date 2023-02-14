import openai

import random

openai.api_key = "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"

engine = "text-davinci-003"

industry_options = ["Finance", "Technology", "Healthcare", "Retail", "Education", "Energy", "Hospitality", "Real Estate", "Entertainment", "Transportation", "Manufacturing", "Construction", "Agriculture",

                    "Telecommunications", "Automotive", "Fashion", "Sports", "Media", "Gaming", "Food", "Beauty", "Fitness", "Home Improvement", "Insurance", "Legal Services", "Public Services", "Non-profit", "Travel", "Gaming"]

greek_names = ["Alexandros", "Andreas", "Christina", "cat ~/.config/code-server/config.yamliliki", "Anastasia", "Nikos", "Ilias"]

industry = input(

    "Please enter your industry from the following options: " + str(industry_options) + "\n")

about_us = input("Please enter a brief description of your business: ")

industry_name = input("Please enter your business name: ")

def generate_story(industry, about_us, industry_name):

    # Randomly select whether to use Storybrand Framework or Standard story prompt

    if random.choice([True, False]):

        # Use Storybrand Framework

        character_name = random.choice(greek_names)

        story_prompt = (

            f"Write a story about how {industry_name} helps {character_name} solve their problem in the {industry} industry.\n",

            f"{industry_name} is the Guide, {about_us} is the Plan, and the Call to Action is to {industry_name}'s solution. ",

            f"The beginning of the story should explain the problem that the \"{character_name}\" is facing and how it is impacting their life. ",

            f"The story should then introduce the \"{character_name}\" to \"{industry_name}\" and explain how their product/service can solve the character's problem. ",

            f"The final part of the story should show how the character's life is different and enhanced after using \"{industry_name}\"'s product/service."

        )

    else:

        # Use standard story prompt

        character_name = random.choice(greek_names)

        story_prompt = (

            f"Write a story about how {industry_name} addresses the needs of {industry} customers.\n"

            f"The beginning of the story must start with how the protagonist, {character_name}  of is suffering from a problem, and how it makes {character_name} feel and how it is impacting {character_name} business life. "

            f"Then the story must follow with how the protagonist discovers the solution from {industry_name}, and how {industry_name}'s product/service makes the protagonist's life easier. "

            f"The final part of the story must finish with how {character_name}'s life is different and enhanced after using {industry_name}'s product/service."

        )

    generated_story = openai.Completion.create(

        model="text-davinci-003",

        prompt=story_prompt,

        max_tokens=1024,

        temperature=0.5,

    )["choices"][0]["text"]

    print(generated_story)

generate_story(industry, about_us, industry_name)
