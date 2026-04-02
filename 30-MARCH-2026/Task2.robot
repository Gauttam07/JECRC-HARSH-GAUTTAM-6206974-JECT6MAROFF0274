*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
*** Test Cases ***
Simple alert
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep  2s
    
    Mouse Over    xpath=//button[@onclick='myFunction()']

    Sleep  2s

    Click Button    xpath=//button[@id='alertBtn']

    Sleep  2s
    Handle Alert
    Sleep    2s


Confirmation Alert
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
    Sleep    2s
    Click Button    xpath=//button[@id='confirmBtn']

    Handle Alert  action=Dismiss


    Sleep    2s

    ${result}=    Get Text    xpath=//p[@id='demo']
    Log To Console    ${result}



Prompt Alert
#    Open Browser  ${url}  chrome
#    Maximize Browser Window
    Sleep  2s
    Click Button    xpath=//button[@id='promptBtn']

    Sleep    2s

#    Input Text Into Alert    HG  action=Dismiss

    Input Text Into Alert    HG
    Sleep  2s

    ${result}=    Get Text    xpath=//p[@id='demo']
    Log To Console    ${result}

    Close Browser
