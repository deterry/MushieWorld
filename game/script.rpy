# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Lum = Character("Elowen Lumiere")
define Verus = Character("Verus Lumiere")
define anom = Character("???")
define Rex = Character("Prosecutor Arlinpagne II")
define Judge = Character("Judge")


# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg desk_prosecutor
    show char prosecutor
    Rex "Would you be so kind as to state your name and occupation to this courtroom?"
    scene bg desk_defendant
    show char main
    anom "...sure. i suppose i don’t mind."
    Verus "my name is Verus Lumiere. 
    Verus "i suppose i was a college student until about 8:10pm last night, when I was apprehended by Detective Bruntforce. 
    Verus "i guess my profession now would be best described as… ‘defendant'."
    scene bg desk_judge
    show char judge base
    Judge "Lumiere? Where have I heard Lumiere before..."
    Judge "Oh...OH"
    scene bg desk_defendant
    show char detective
    Lum "..." 
    Lum "Are you sure you are comfortable talking about what happened to Myra?"
    scene bg desk_defendant
    show char main
    Verus "i have to, Mom. 
    Verus "Myra wanted...needed to show me this."
    Verus "i have to uncover the truth of what happened that night, even if i have to risk my own life to find it."
    scene bg desk_defendant
    show char detective
    Lum "...okay. If this is what you want..."
    scene bg desk_prosecutor
    show char prosecutor
    Rex "Could you testify to the events that took place leading up to the discovery of the body?"
    scene bg desk_defendant
    show char main
    Verus: "...yeah, sure."

    #Cross_Examination 
    #Intro

    centered "- how i found her -"
    play scrutinizing

    show char main
    Verus "i received a text from Myra at around 6:30pm. We haven't spoken in years, so I was caught off guard by her message."
    Verus "she said to meet her at her new place at 8:30pm, but i couldn't wait that long."
    Verus "i knocked on her door around 7:45pm, but as i turned to leave, a loud crash echoed from inside."
    Verus "panicking, i shouted her name a forced my way inside. i searched her rooms until I found her in her study."
    Verus "seeing her lifeless body...it broke me. i was frozen in place near her body when Detective Bruntforce arrived."

    fade out scrutinizing

    #Lil Transition
    
    scene bg desk_judge
    show char judge base
    Judge "I can’t imagine what that must have been like, seeing such a horrific sight of someone you once deeply cared about."
    scene bg desk_defendant
    show char main
    Verus "i can still see the shock in her eyes. she didn’t even see her attacker coming..."
    scene bg desk_prosecutor
    show char prosecutor
    Rex "...she was definitely taken by surprise."
    scene bg desk_defendant
    show char detective
    Lum "Verus..."

    #Gameplay
    #Cross-Examination
    scene bg desk_defendant
    show char main
    anon "- how i found her -"
    play running

    #Press 1
    Verus "i received a text from Myra at around 6:30pm. We haven't spoken in years, so I was caught off guard by her message."
    #Halt!
    scene bg desk_defendant
    show char detective
    Lum "She reached out to you? After keeping you in the dark for so long, why did she choose to speak with you now?"
    scene bg desk_defendant
    show char main
    Verus "i don’t know, and it seems like i will never know..."
    scene bg desk_judge
    show char judge base
    Judge "..."
    scene bg desk_prosecutor
    show char prosecutor
    Rex "..."
    scene bg desk_defendant
    show char detective
    Lum "Seems like everyone is feeling the impact of this travesty."
    scene bg desk_defendant
    show char main
    Verus "to think I even tried to see her earlier..."

    
    #Press 2
    Verus "she said to meet her at her new place at 8:30pm, but i couldn't wait that long."
    #Halt!
    scene bg desk_defendant
    show char detective
    Lum "Why couldn’t you wait until 8:30pm to see her?"
    scene bg desk_defendant
    show char main
    Verus "would you be able to sit with something that heavy for that long?"
    Verus "to have the person who abandoned you reach out to you for closure?"
    scene bg desk_defendant
    show char detective
    Lum: "...I suppose not."
    scene bg desk_defendant
    show char main
    Verus "i had a lot to i wanted to say to her...but i suppose it will have to remain unsaid."
    scene bg desk_prosecutor
    show char prosecutor
    Rex "What happened when you arrived at her estate?"

    #Press 3
    scene bg desk_defendant
    show char main
    Verus "i knocked on her door around 7:45pm, but as i turned to leave, a loud crash echoed from inside."
    #Halt!
    scene bg desk_defendant
    show char detective
    Lum "A loud crash? Please, tell us more!"
    scene bg desk_defendant
    show char main
    Verus "it sounded like glass shattering."
    scene bg desk_prosecutor
    show char prosecutor
    Rex "Our investigations team found 
    
    Verus: but it would seem that I wasn’t fast enough to protect her. 

    #Press 4
    Verus "panicking, i shouted her name and forced my way inside. i searched the house until I found her in her study."
    #Halt!
    scene bg desk_defendant
    show char detective
    Lum "You forced your way in?!?! 
    Lum "Do you know how dangerous that individual could have been?"
    scene bg desk_defendant
    show char main
    Verus "ofc i did...but i couldn't just stand by and do nothing again."
    scene bg desk_defendant
    show char detective   
    Lum "..."
    Lum "..."
    scene bg desk_prosecutor
    show char prosecutor
    Rex "*ahem* In any case, could you talk more about the state of the body when you found it?"
    scene bg desk_defendant
    show char main
    Verus "..."

    #Press 5
    Verus "seeing her lifeless body...it broke me. i was frozen in place near her body when Detective Bruntforce arrived."
    #Halt!
    scene bg desk_defendant
    show char detective
    Lum "So you stood there and did...nothing?"
    scene bg desk_defendant
    show char main
    Verus "yes, i- i was frozen in place."
    scene bg desk_judge
    show char Judge
    Judge "Well, that's understandable. The experience must have been very traumatic for you."
    Judge "I am sorry that you had to suffer such a terrible experience."
    scene bg desk_prosecutor
    show char prosecutor
    Rex "Hmmm, yes. Most people would be frozen in place..."
    scene bg desk_defendant
    show char detective
    Lum "..."

    #Loop
    DetectiveLumiere "I don’t know why, but I know Verus is not telling the whole truth."
    DetectiveLumiere "He’s holding back, and if I am to save him, I have to bring out the ugly truth he harbors."
#(Loops dialogue)

#Present the Standing Lamp on this dialogue

#"i discovered her body in her study. Unable to move, I hovered in front of her corpse until bruntforce appeared to on the scene."

#DESIST!
fade out running
DetectiveLumiere "..."

DetectiveLumiere  "Verus, if you want me to get you out of this situation, you’re going to have to tell the truth."
show char main
Verus "!!"
show char detective
DetectiveLumiere  "You said that you 'hovered in front of her corpse until Bruntforce arrived'. Is this true?"
show char main
Verus "...yes it is."
show char detective
DetectiveLumiere  "Then why were your fingerprints found on this lamp!"
play intro
play eureka
show char main
Verus "!!"
scene bg desk_judge
show char judge base
Judge  "Huhhh?"
scene bg desk_prosecutor
show char prosecutor
Rex  "...so you have found it."

#(courtroom chatter)
scene bg desk_judge
show char judge base
Judge  "Order please! We need to get to the bottom of this!"
Judge "Verus, why did you lie about not touching the body?"
scene bg desk_defendant
show char main
Verus  "...because of how I found the body."
show char detective
DetectiveLumiere "!!"
scene bg desk_judge
show char judge base
Judge "Order please! We need to get to the bottom of this!"

Judge "Verus, why did you lie about not touching the body?"
scene bg desk_defendant
show char main
Verus "...because of how I found the body."
show char detective
Lum "!!"
scene bg desk_prosecutor
show char prosecutor
Rex "Maybe you should elaborate on the state of the body as you discovered it, including the reason why you tampered with the evidence."
scene bg desk_defendant
show char main
Verus "...okay. I can do it."
centered "END OF DEMO"

return
