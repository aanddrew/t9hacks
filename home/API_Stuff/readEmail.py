#Goal is to send an email using python through email
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import json
from apiclient import errors
# If modifying these scopes, delete the file token.pickle.


class readEmailMaster:
  def __init__(self):
    self.service = 0
    self.SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    self.messageID = 0
  def decodeBase64(self,email64):
      emailASCII = base64.b64decode(email64)
      return emailASCII

  def Authentication(self):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    self.service = build('gmail', 'v1', credentials=creds)

  def ListMessagesMatchingQuery(self, service, user_id):
    """List all Messages of the user's mailbox matching the query.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      query: String used to filter messages returned.
      Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
      List of Messages that match the criteria of the query. Note that the
      returned list contains Message IDs, you must use get with the
      appropriate ID to get the details of a Message.
    """
    try:
      response = service.users().messages().list(userId=user_id).execute()
      messages = []
      if 'messages' in response:
        messages.extend(response['messages'])

      while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId=user_id, q=query, pageToken=page_token).execute()
        messages.extend(response['messages'])

      return messages
    except errors.HttpError:
      print('An error occurred: %s') % error

  #This function verify's that the email is part of the game by checking the subject line
  def actuallyRead(self):
    msgs = self.ListMessagesMatchingQuery(self.service , "me") #Gets list of all messages in inbox
    outputMsgs = []
    #Traverse alls messages
    for x in msgs:
      msg_ID = x['id'] #Get the ID in order to get more data
      msg= self.service.users().messages().get(userId='me', id=msg_ID).execute() #Actual json
      if(msg["labelIds"][-1]!="INBOX"):
        continue

      headerLvl= 0;
      #Traverses message data to find the required Sendgame subject
      for i in msg['payload']['headers']:
        headerLvl += 1
        #Verifying subject is Sendgame Output and adding to 
        if (i['value']=="Sendgame Output"):
          outputMsgs.append(msg)
        
    
    latestmsg = outputMsgs[0]
    for i in outputMsgs: #Traverse all messages with Sendgame Output
      if (int(i["internalDate"]) > int(latestmsg["internalDate"])):
        latestmsg = i
    #Sets unique ID
    self.messageID = latestmsg['id']
    email64 = json.dumps(latestmsg['payload']['parts'][0]['body']['data'], sort_keys=True, indent=4, separators=(',', ': '))
    final = self.decodeBase64(email64)
    return final;

  #Gets message ID of latest message
  def getLastId(self):  
      return self.messageID

if __name__ == '__main__':
    yeet = readEmailMaster()
    yeet.Authentication()
    print(yeet.actuallyRead(), yeet.getLastId())
