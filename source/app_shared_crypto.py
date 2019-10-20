'''
Created on August 10th 2016
@author: Thierry Souche

This modules contains few generic functions which are useful for crypto modules 
used to manage passwords across the backend application.

'''

from passlib.context import CryptContext


# useful crypto constants used by multiple modules for managing passwords

encryption_algorithm = "sha512_crypt"


# useful crypto functions used by multiple modules for managing passwords

def encryptPassword(password):
    """
    This function encrypts a password and returns a hash.
    """
    context = CryptContext(schemes=[encryption_algorithm])
    # replaced 'encrypt' (deprecated as of 1.7) with 'hash'
    return context.hash(password)

def checkPassword(password, passwordHash):
    """
    This function decrypts a passwordHash and returns the password.
    """
    context = CryptContext(schemes=[encryption_algorithm])
    return context.verify(password, passwordHash)



