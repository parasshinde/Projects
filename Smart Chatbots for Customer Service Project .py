#!/usr/bin/env python
# coding: utf-8

# # Installing Rasa

# In[ ]:


pip install rasa


# # Project Structure

# In[ ]:


mkdir smart_chatbot
cd smart_chatbot
rasa init --no-prompt


# # Defining the Training Data

# In[2]:


nlu.yml
This file contains example user inputs and the intents they correspond to:


# In[ ]:


version: "2.0"
nlu:
- intent: greet
  examples: |
    - hello
    - hi
    - hey
    - good morning
    - good evening
    - hey there

- intent: goodbye
  examples: |
    - bye
    - goodbye
    - see you later
    - have a nice day
    - see you

- intent: affirm
  examples: |
    - yes
    - indeed
    - of course
    - that sounds good
    - correct

- intent: deny
  examples: |
    - no
    - never
    - I don't think so
    - don't like that
    - no way

- intent: inform
  examples: |
    - I am looking for customer support
    - I need help with my order
    - Can you assist me with my account


# In[ ]:


domain.yml
This file defines the intents, entities, slots, responses, and actions:


# In[ ]:


version: "2.0"

intents:
  - greet
  - goodbye
  - affirm
  - deny
  - inform

responses:
  utter_greet:
    - text: "Hello! How can I assist you today?"

  utter_goodbye:
    - text: "Goodbye! Have a great day!"

  utter_ask_issue:
    - text: "Could you please describe the issue you're facing?"

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true


# In[ ]:


stories.yml
This file describes the conversation flows:


# In[ ]:


version: "2.0"
stories:
- story: greet and goodbye
  steps:
  - intent: greet
  - action: utter_greet
  - intent: goodbye
  - action: utter_goodbye

- story: customer support query
  steps:
  - intent: inform
  - action: utter_ask_issue


# # Training the Model
# Train the Rasa model with the following command:

# In[ ]:


rasa train


# # Running the Bot
# Start the Rasa server and the action server: 

# In[ ]:


rasa run


# #  Testing the Bot
# You can test the bot by running:

# In[ ]:


rasa shell

