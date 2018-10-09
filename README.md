# Async helper

Simplified interface to do basic async/await in python

For usage please refer to example.py

##### Why this interface?
Loops are not that easy to handle when using multiple threads as there 
is no automatic initialization of one loop per thread.

This helper hide most of the complexity when only one loop is 
needed per thread.

It also hides loop management operations when using one single thread.
