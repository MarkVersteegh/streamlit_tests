
import json



json_skills = """
[
        {
            "name": "Skill1",
            "description": "Longer description of skill1, to test how this looks in the app. ...."
        },
        {
            "name": "Skill2",
            "description": "Longer description of skill2, to test how this looks in the app. ...Some more text, bla bla bla."
        }
    ]
"""
skills = json.loads(json_skills)


print(skills)

for skill in skills:
    print(f"{skill['name']}: {skill['description']}")
