*** Settings ***
Documentation  handling multiselect
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
${browser}  chrome

*** Test Cases ***
handle Multiselet and Scroll
    Open Browser  ${url}  ${browser}
    Maximize Browser Window
    Sleep    2s
    
#    Scroll Element Into View    xpath=//label[text()="Sorted List:"]
    
    Mouse Over    id=colors
    Sleep    2s

    Page Should Contain List    id=colors
    @{choice}=  Get List Items    id=colors
    Log To Console    ${choice}
    Sleep    2s

    Select From List By Label    id=colors  Red  Yellow
    Sleep    2s

    @{select}=  Get Selected List Labels    id=colors
    Log To Console    ${select}
    Sleep    2s

    Close Browser

