*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${NAME}    Arjun
@{NUMS}    1    2    3

*** Test Cases ***
Test Case One
    Log    Hello ${NAME}
    Log To Console    Numbers: ${NUMS}

Test Case Two
    Log    Second test running
    Log To Console    Test completed
