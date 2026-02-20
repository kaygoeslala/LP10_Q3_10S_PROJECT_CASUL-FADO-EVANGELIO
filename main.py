from pyscript import document

def nanamigreen(event):
    answer1 = document.querySelector('input[name="answer1"]:checked')
    answer3 = document.querySelector('input[name="answer3"]:checked')
    grade = document.getElementById("grd").value.strip()
    section = document.getElementById("sct").value.strip().upper()  # make all caps
    result_element = document.getElementById("Result")
    
    if not answer1 or not answer3:
        result_element.textContent = "Please fill the form out completely."
        return

    if answer1.value != "yes" or answer3.value != "yes1":
        result_element.textContent = "Please register online and secure your medical clearance."
        return

    if grade == "7" and section == "RUBY":
        team_name = "Blue Bears"
        image_file = "BB.jpg"
    elif grade == "7" and section == "EMERALD":
        team_name = "Red Bulldogs"
        image_file = "RB.jpg"
    elif grade == "7" and section == "SAPPHIRE":
        team_name = "Yellow Tigers"
        image_file = "YT.jpg"
    
    elif grade == "8" and section == "RUBY":
        team_name = "Green Hornets"
        image_file = "GH.jpg"
    elif grade == "8" and section == "EMERALD":
        team_name = "Blue Bears"
        image_file = "BB.jpg"
    elif grade == "8" and section == "SAPPHIRE":
        team_name = "Red Bulldogs"
        image_file = "RB.jpg"
    
    elif grade == "9" and section == "RUBY":
        team_name = "Yellow Tigers"
        image_file = "YT.jpg"
    elif grade == "9" and section == "EMERALD":
        team_name = "Green Hornets"
        image_file = "GH.jpg"
    elif grade == "9" and section == "SAPPHIRE":
        team_name = "Blue Bears"
        image_file = "BB.jpg"
    
    elif grade == "10" and section == "RUBY":
        team_name = "Red Bulldogs"
        image_file = "RB.jpg"
    elif grade == "10" and section == "EMERALD":
        team_name = "Yellow Tigers"
        image_file = "YT.jpg"
    elif grade == "10" and section == "SAPPHIRE":
        team_name = "Green Hornets"
        image_file = "GH.jpg"
    else:
        result_element.textContent = "No team assigned for this grade and section."
        return

    result_element.innerHTML = f'''
        <div style="text-align: center;">
            <img src="{image_file}" style="max-width: 100%; height: auto; border-radius: 10px;">
            <p style="margin-top: 15px; font-weight: 600; color: #8b5cf6; font-size: 18px;">
                Congratulations! You are part of {team_name}!
            </p>
        </div>
    '''
