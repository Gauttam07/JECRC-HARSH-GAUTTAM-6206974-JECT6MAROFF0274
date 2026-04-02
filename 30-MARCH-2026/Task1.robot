*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Window Handling
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Mouse Over     xpath=//button[@id='PopUp']
    Sleep    2s
    Click Element    xpath=//button[@id='PopUp']
    Sleep    2s

    @{windows}  Get Window Handles

    Switch Window    NEW
    @{tittle}  Get Window Titles
    Log To Console    ${tittle}
    Sleep    2s


    Switch Window    ${windows}[0]
    @{tittle}  Get Window Titles
    Log To Console    ${tittle}
    Sleep    2s
    
    Page Should Contain    Automation Testing Practice

    Close Browser