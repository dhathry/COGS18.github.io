#!/usr/bin/env python
# coding: utf-8

# # Code Projects
# 
# - modular design
# - minimal viable product
# - test-driven development
# - rapid prototyping
# - project organization
# - refactoring
# - code review

# ## Project Check-In
# 

# ### Modular Design

# <div class="alert alert-success">
# Modular design, like modular programming, is the approach of designing and building things as independent modules. 
# </div>

# ### Minimal Viable Product

# <div class="alert alert-success">
# A 'minimal viable product' is a product that contains the minimum amount of implemented features to use the code product - no more, no less.</div>

# ### Test-Driven Development

# <div class="alert alert-success">
# Writing the tests as soon as you have a plan & before you've written the code.
# </div>

# ### Rapid Prototyping

# <div class="alert alert-success">
# Rapid prototyping is an approach for developing things in which you work on minimal prototypes and iterate on them quickly. 
# </div>

# #### Some examples
# 
# - Chatbot: start and end a chat
# - Data Analysis: read a dataset in, make a basic plot
# - Car Inventory: object with method that adds a car to the Inventory
# - Artificial Agents: simple bot moves around randomly

# ## Project Organization

# - **Notebooks**: good for interactive development
#     - For when seeing the inputs and outputs of code running needs to be seen start to finish
#     - file ends in `.ipynb`
# - **Modules**: for storing mature Python code, that you can import
#     - you don't *use* the functions in there, just define them
#     - file ends in `.py`
# - **Scripts**: a Python file for executing a particular task
#     - this takes an input and does something start to finish
#     - file ends in `.py`

# ### Project Workflow

# Typical project workflow:
# 
# - Develop plan and write tests
# - Develop code interactively in a Jupyter notebook/text editor
# - As functions & classes become mature, move them to Python files that you then `import`
#     - As you do so, go back through them to check for code style, add documentation, and run your code tests
# - At the end of a project, (maybe) write a standalone script that runs the project

# #### Project Notes
# 
# 1. Design and write tests
# 2. Write some code
# 2. Test to make sure it works
# 3. Check code style (naming, spacing, etc.)
# 4. Add documentation
# 5. Move to module (if necessary)
# 6. Run all tests

# ### Project Design
# 
# - Idea: atbash encryption: return the capitalized, reverse alphabetical letter for each character in the input string
# 
# - Design:
#     - `atbash_encrypt()` : take input string and retrun atbash encrypted string
#         - inputs: `input_string` 
#         - returns: `atbash_string`
#     - `atbash_decrypt()` : take encrypted string and decrypt using atbash
#         - inputs: `atbash_string`
#         - returns: `decrypted_string`
#     - `atbash_wrapper()` : does either of the above, as specified with input parameter
#         - inputs: `input_string`, `method` (either 'encrypt' or 'decrypt', default: 'encrypt')
#         - returns `output_string`

# ### Adding Unit Tests

# In[ ]:


def test_atbash_encrypt():
    assert callable(atbash_encrypt)
    assert type(atbash_encrypt('hello')) == str
    assert atbash_encrypt('HELLO') == 'SVOOL'
    assert atbash_encrypt('hello') == 'SVOOL'
    
def test_atbash_decrypt():
    assert callable(atbash_decrypt)
    assert type(atbash_decrypt('hello')) == str
    assert atbash_decrypt('SVOOL') == 'HELLO'
    assert atbash_decrypt('svool') == 'HELLO'

def test_atbash_wrapper():
    assert callable(atbash_wrapper)
    assert type(atbash_wrapper('hello', method='encrypt')) == str
    assert atbash_wrapper('hello', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('HELLO', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('SVOOL', method='decrypt') == 'HELLO'
    assert atbash_wrapper('svool', method='decrypt') == 'HELLO'
    assert atbash_wrapper('svool', method='blargh') == "method should be either 'decrypt' or 'encrypt'"


# ...move to test file
# 
# ...will uncomment as I write the code/functions

# ### Writing Code

# #### `atbash_encrypt`

# In[1]:


def atbash_encrypt(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    atbash_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            atbash_string += reverse_alpha[position]
        else:
            atbash_string = None
            break
        
    return atbash_string


# In[ ]:


# smoke test
atbash_encrypt('Hello')


# ### Moving to a module...
# 
# - consider imports at the top

# Note on `imports`: If you want to be able to use modules (imports) within a module/script, be sure to import it at the top. This applies to test files as well.

# In[3]:


get_ipython().system('pytest test_functions.py')


# #### `atbash_decrypt`

# In[4]:


# reminder: consider code style! 
def atbash_decrypt(atbash_string):    
    
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    
    atbash_string = atbash_string.upper()
    decrypted_string = ''
    
    for ltr in atbash_string:
        if ltr in reverse_alpha:
            letterindex = reverse_alpha.find(ltr)
            decrypted_string = decrypted_string + alpha[letterindex]
        else: 
            decrypted_string = decrypted_string + ltr
    
    return decrypted_string


# In[5]:


# smoke test
atbash_decrypt('SVOOL')


# In[ ]:


get_ipython().system('pytest test_atbash.py')


# #### `atbash_wrapper`

# In[6]:


def atbash_wrapper(input_string, method='encrypt'):
    
    if method == 'encrypt':
        output_string = atbash_encrypt(input_string)
    elif method == 'decrypt':
        output_string = atbash_decrypt(input_string)
    else:
        output_string = "method should be either 'decrypt' or 'encrypt'"
    
    return output_string


# In[7]:


# smoke test
atbash_wrapper('hello')


# In[ ]:


get_ipython().system('pytest test_atbash.py')


# ### Documentation
# 
# - Code in final project/exam requires:
#     - numpy-style docstrings
#     - code comments

# ### Putting it all together

# In[1]:


from atbash import atbash_wrapper


# In[2]:


atbash_wrapper('hello')


# In[3]:


atbash_wrapper('svool', method='decrypt')


# In[4]:


atbash_wrapper('hello', method='blargh')


# In[ ]:


get_ipython().system('pytest')


# ### Refactoring

# <div class="alert alert-success">
# Refactoring is the process of restructuring existing computer code, without changing its external behaviour. 
# </div>

# Think of this as restructuring and final edits on your essay. 

# **Nesting Functions** - If you have a whole bunch of functions, if statements, and for/while loops together within a single function, you probably want (need?) to refactor.

# Clean functions accomplish a **single task**!

# **DRY**: Don't Repeat Yourself

# #### Refactoring Example: Chatbot

# In[ ]:


import random 

def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        # Check if the input is a question
        input_string = msg
        if '?' in input_string:
            question = True
        else:
            question = False

        # Check for an end msg 
        if 'quit' in input_string:
            out_msg = 'Bye!'
            chat = False
            
        # If we don't have an output yet, but the input was a question, 
        # return msg related to it being a question
        if not out_msg and question:
            out_msg = "I'm too shy to answer questions. What do you want to talk about?"

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])

        print('OUTPUT:', out_msg)


# In[ ]:


have_a_chat()  


# #### Refactored Example: Chatbot

# What this function does:
# 
# 1. takes an input
# 2. checks if input is a question
# 3. checks if input is supposed to end the chat
# 4. return appropriate response if question, end chat, or other
# 
# That's four different things! Functions should do a single thing...

# In[ ]:


def get_input():
    """ask user for an input message"""
    
    msg = input('INPUT :\t')
    out_msg = None
    
    return msg, out_msg


# In[ ]:


def is_question(input_string):
    """determine if input from user is a question"""
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output


# In[ ]:


def end_chat(input_list):
    """identify if user says 'quit' in input and end chat"""
    
    if 'quit' in input_list:
        output = 'Bye'
        chat = False
    else:
        output = None
        chat = True
        
    return output, chat


# In[ ]:


def return_message(out_msg, question):
    """generic responses for the chatbot to return"""
        
    # If we don't have an output yet, but the input was a question, 
    # return msg related to it being a question
    if not out_msg and question:
        out_msg = "I'm too shy to answer questions. What do you want to talk about?"

    # Catch-all to say something if msg not caught & processed so far
    if not out_msg:
        out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])
        
    return out_msg


# In[ ]:


def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get input message from the user
        msg, out_msg = get_input()
        
        # Check if the input is a question
        question = is_question(msg)
         
        # Check for an end msg 
        out_msg, chat = end_chat(msg)
       
        # specify what to return
        out_msg = return_message(out_msg = out_msg, question = question)
        
        print('OUTPUT:', out_msg)


# In[ ]:


have_a_chat()  


# ## Code Review

# <div class="alert alert-success">
# Code reviews is a process for systematically reviewing someone else's code. 
# </div>
