import streamlit as st
def write():
    st.title('SkillMatrix testing page')


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
            },
            {
                "name": "Skill3",
                "description": "Longer description of skill3, to test how this looks in the app. ...Some more text, bla bla bla."
            },
            {
                "name": "Skill4",
                "description": "Longer description of skill4, to test how this looks in the app. ...Some more text, bla bla bla."
            }

        ]
    """
    skills = json.loads(json_skills)


    print(skills)

    for skill in skills:
        print(f"{skill['name']}: {skill['description']}")


    st.title('Skills **_section 1_**')
    for skill in skills:
        label = f"<b>{skill['name']}</b>: {skill['description']}"
        st.slider(label,min_value=0, max_value=5, value=0,step=1,key=skill['name']+'1')


    st.title('Skills section 2')
    for skill in skills:
        html_string = f"<b>{skill['name']}</b>"
        st.markdown(html_string, unsafe_allow_html=True)
        st.subheader(skill['name'])
        
        label = f"{skill['description']}"
        st.slider(label,min_value=0, max_value=5, value=0,step=1,key=skill['name']+'2')


    st.markdown('Some **_markdown_**.')


