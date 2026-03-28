def generate_resume():
    name = input("Enter Name: ")
    education = input("Enter Education: ")
    skills = input("Enter Skills (comma separated): ")
    projects = input("Enter Projects (comma separated): ")


    print("RESUME")
    
    

    # Summary
    print("SUMMARY")
    print(f"{name} is a motivated B.Tech student with strong interest in software development and Artificial Intelligence.\n")

    # Education
    print("EDUCATION")
    print(f"- {education}\n")

    # Skills
    print("SKILLS")
    skills_list = skills.split(",")
    for skill in skills_list:
        print(f"- {skill.strip()}")
    print()

    # Projects
    print("PROJECTS")
    projects_list = projects.split(",")
    for project in projects_list:
        print(f"- {project.strip()}")
    print()


generate_resume()