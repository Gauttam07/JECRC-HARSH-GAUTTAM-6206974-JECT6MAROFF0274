*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html

*** Test Cases ***
Iframe Window Handling'
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Select Frame    id=singleframe
    
    Input Text    xpath=//input[@type="text"]    NIK
    
    Sleep    5s

    Unselect Frame


    Close Browser