*** Settings ***
Documentation    Suite description
Library    SeleniumLibrary 10.0 localhost

*** Test Cases ***
Test title
    Open Browser    http://www.google.de chrome
    Select Window    main

*** Keywords ***
Provided precondition
    Setup system under test