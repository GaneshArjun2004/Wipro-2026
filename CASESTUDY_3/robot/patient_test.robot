*** Settings ***
Library    SeleniumLibrary

Suite Setup    Open Browser    http://127.0.0.1:5000    chrome
Suite Teardown    Close Browser

*** Test Cases ***
Register Patient
    Input Text    name=name    Test
    Input Text    name=age     22
    Click Button    xpath=//input[@type='submit']
