*** Settings ***
Documentation    handling checkboxes
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/
@{days}  Sunday  Monday  Tuesday  Wednesday  Thursday  Friday  Saturday

*** Test Cases ***
Handling Radio + Checkboxes
    Open Browser    ${url}    edge
    Maximize Browser Window
    Sleep    3s

    Select Radio Button    gender    male
    Sleep    2s

    # Select all checkboxes
    FOR  ${day}    IN    @{days}
        Click Element    xpath=//label[text()="${day}"]

        Sleep    1s
    END


    # Unselect in reverse order
    FOR    ${day}    IN    @{days[::-1]}
        Click Element    xpath=//label[text()="${day}"]

        Sleep    1s
    END

    Close Browser