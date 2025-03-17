# Note: ChatGPT (https://chatgpt.com/) was used to understand how exactly a test case is supposed to be created without any references to the source code

import pytest
from unittest.mock import patch # patch to act as user input for tests
from A1Q1_User_Login_System import LoginSystem

# Supposed usernames in the backend
usernames = ["bob123", "realuser123"]
user_passwords = ["123qwe!@#QWE", "321ewq#@!EWQ"]

# Fixture to create an instance of LoginSystem with the usernames and passwords
@pytest.fixture
def login_system():
    return LoginSystem(usernames, user_passwords)


# User successfully logging in
def test_successful_login(login_system):

    with patch('builtins.input', side_effect=[usernames[0], user_passwords[0]]): # simulating user entering correct credentials
        assert login_system.checkUserExists(usernames[0])  # checking if the login is successful


# two users fail to login - correct username and wrong password
def test_failed_login_attempts(login_system):
    with patch('builtins.input', side_effect=[
        usernames[0], 'wrongpassword',
        usernames[1], 'wrongpassword']):
        assert not login_system.checkUserExists(usernames[0])  # checking if all attempts have failed


# Invalid username
def test_user_not_exists(login_system):
    with patch('builtins.input', side_effect=['fakeuser123']):
        assert login_system.checkUserExists('fakeuser123') is None   # User not found


# locked account
def test_account_locking(login_system):
    with patch('builtins.input', side_effect=[
        usernames[0], 'wrongpassword',
        'wrongpassword',
        'wrongpassword']):
        login_system.checkUserExists(usernames[0])   # checking if all attempts have failed
        assert login_system.user_status[0] == "locked"  # status of account is locked
