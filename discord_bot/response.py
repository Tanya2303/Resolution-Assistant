import os
import sys
import datetime
from hedera import (Hbar, AccountId, AccountBalanceQuery)
from get_client import client, OPERATOR_ID
import openai
import wandb

openai.api_key = os.getenv("OPENAI_KEY")
run = wandb.init(project='GPT-3 in Python')
prediction_table = wandb.Table(columns=["prompt", "completion"])

gpt_prompt = "Give suggestion for\n\n I want to keep myself healthy."

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

recipientId = AccountId.fromString("0.0.3")
amount = Hbar.fromTinybars(10_000_000)

@client.event
def list():
    try:
        nec()
        l = len(d)
        k = l
 
        for i in d:
            sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l-1
 
    except Exception as e:
        raise e
 
@client.event
def delete(no):
    try:
        no = int(no)
        nec()
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
        print(f"Deleted todo #{no}")
 
    except Exception as e:
        print(f"Error: todo #{no} does not exist. Nothing deleted.")
 
@client.event
def done(no):
    try:
 
        nec()
        no = int(no)
        st = 'x '+str(datetime.datetime.today()).split()[0]+' '+d[no]
        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked todo #{no} as done.")
         
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: todo #{no} does not exist.")
 
@client.event
def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello World!'

    if message == '/info':
        return 'Hi!, I am Resolution Assistant Bot. Here to help you to complete your New year Resolutions.'

    if p_message == '/help':
        return ('Here are the commands you can use:'
                '\n `/new_year_resolution`: To add a new year resolution.'
                '\n `/list`: To list all the resolutions.'
                '\n `/delete`: To delete a resolution.'
                '\n `/update`: To update a resolution.'
                '\n `/suggest`: To get suggestions for a resolution.'
                '\n `/goal_achieved`: To mark a resolution as achieved.'
                '\n `/eco_points`: To check how many eco points you have achieved.'
                '\n `/remind_me`: To set a reminder for a resolution.'
                '\n `/reedem`: To reedem eco points for a reward.'
                )

    if p_message == '/balance':
        balance = AccountBalanceQuery()
        balance.setAccountId(OPERATOR_ID)
        balance = balance.execute(client)
        return f'Your balance is {balance.hbars}'

    return 'I didn\'t understand what you wrote. Try typing "/help".'
